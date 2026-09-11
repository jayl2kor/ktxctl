"""DynaPath encoding from carpedm20/korail2 PR #54 (BSD; see LICENSE)."""

import time
from typing import Final, TypedDict

DYNAPATH_PATHS: Final = (
    "/classes/com.korail.mobile.certification.TicketReservation",
    "/classes/com.korail.mobile.nonMember.NonMemTicket",
    "/classes/com.korail.mobile.seatMovie.ScheduleView",
    "/classes/com.korail.mobile.seatMovie.ScheduleViewSpecial",
    "/classes/com.korail.mobile.trn.prcFare.do",
    "/classes/com.korail.mobile.login.Login",
)

AuthHeaders = TypedDict("AuthHeaders", {"x-dynapath-m-token": str}, total=False)


class DynaPathMasterEngine:
    """Encode request tokens using an application start timestamp."""

    APP_ID: Final = "com.korail.talk"
    AS_VALUE: Final = "%5B38ff229cb34c7dda8e28220a2d750cce%5D"
    DEVICE_MODEL: Final = "SM-S928N"
    OS_TYPE: Final = "Android"
    SDK_VERSION: Final = "v1"
    TABLE: Final = "3FE9jgRD4KdCyuawklqGJYmvfMn15P7US8XbxeLQtWT6OicBAopINs2Vh0HZrz"
    I8: Final = 161
    I9: Final = 30
    I10: Final = 2

    def __init__(self) -> None:
        self.app_start_ts = str(int(time.time() * 1000))

    def string2xA1s(self, data_str: str) -> list[int]:
        result: list[int] = []
        for char in data_str:
            cp = ord(char)
            if cp < 128:
                result.append(cp)
            elif cp < 2048:
                result.append(128 | ((cp >> 7) & 15))
                result.append(cp & 127)
            elif cp >= 262144:
                result.extend((160, (cp >> 14) & 127, (cp >> 7) & 127, cp & 127))
            elif (63488 & cp) != 55296:
                result.extend((((cp >> 14) & 15) | 144, (cp >> 7) & 127, cp & 127))
        return result

    def make_key(self, key_str: str) -> int:
        big_int_add = 0
        for char in key_str:
            cp = ord(char)
            i9_bit = 32768
            for _ in range(16):
                if (i9_bit & cp) != 0:
                    break
                i9_bit >>= 1
            big_int_add = (big_int_add * (i9_bit << 1)) + cp
        return big_int_add

    def _internal_i(self, base_table: str, remainder: int, current_sb: str) -> str:
        j8_count = 0
        for char in base_table:
            if char not in current_sb:
                if j8_count == remainder:
                    return char
                j8_count += 1
        return " "

    def make_encode_table(self, num: int, encode_size: int, base_table: str) -> str:
        sb = ""
        for i in range(encode_size):
            divisor = encode_size - i
            sb += self._internal_i(base_table, num % divisor, sb)
            num //= divisor
        return sb

    def encode_normal_be(
        self, data_str: str, table: str, i8: int = 161, i9: int = 30, i10: int = 2,
    ) -> str:
        list_data = self.string2xA1s(data_str)
        sb: list[str] = []
        i_arr = [0] * (i10 + 1)
        idx, size = 0, len(list_data) % i10
        size2 = len(list_data) - size
        while idx < size2:
            val = 0
            for _ in range(i10):
                val = (val * i8) + list_data[idx]
                idx += 1
            for i in range(i10 + 1):
                i_arr[i] = val % i9
                val //= i9
            for i in range(i10, -1, -1):
                sb.append(table[i_arr[i]])
        if size > 0:
            val = 0
            for _ in range(size):
                val = (val * i8) + list_data[idx]
                idx += 1
            for i in range(size + 1):
                i_arr[i] = val % i9
                val //= i9
            while size >= 0:
                sb.append(table[i_arr[size]])
                size -= 1
        return "".join(sb)

    def generate_token(self, device_id: str, ts: int, rand: str) -> str:
        plaintext = (
            f"ai={self.APP_ID}&di={device_id}&as={self.AS_VALUE}&"
            f"su=false&dbg=false&emu=false&hk=false&it={self.app_start_ts}&"
            f"ts={ts}&rt=0&os=13&dm={self.DEVICE_MODEL}&st={self.OS_TYPE}&sv={self.SDK_VERSION}"
        )
        dyn_key = f"v1+{rand}+{ts}"
        key_enc = self.encode_normal_be(dyn_key, self.TABLE, self.I8, self.I9, self.I10)
        big_key = self.make_key(dyn_key)
        custom_table = self.make_encode_table(big_key, self.I9, self.TABLE)
        body_enc = self.encode_normal_be(plaintext, custom_table, self.I8, self.I9, self.I10)
        return f"bEeEP{self.TABLE[len(key_enc)]}{key_enc}{body_enc}"
