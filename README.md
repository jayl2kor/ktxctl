# ktxctl: KTX Reservation Assistant

이 저장소는 코레일(KTX 및 일반열차) 예매 전용으로 구성되어 있습니다.
실행 명령과 Python 패키지명은 모두 `ktxctl`입니다.

> [!WARNING]
> 본 프로그램의 모든 상업적, 영리적 이용을 엄격히 금지합니다. 본 프로그램 사용에 따른 민형사상 책임을 포함한 모든 책임은 사용자에게 있으며, 본 프로그램의 개발자는 민형사상 책임을 포함한 어떠한 책임도 부담하지 않습니다. 본 프로그램을 내려받음으로써 모든 사용자는 위 사항에 이의 없이 동의하는 것으로 간주됩니다.

로그인 정보, 카드 정보, 예매 설정은 로컬 컴퓨터의
[keyring](https://pypi.org/project/keyring/)에 저장됩니다.
로그인·예매·결제 요청에는 필요한 정보가 코레일에 전송되며,
텔레그램 알림을 설정하면 예매 정보가 텔레그램으로 전송됩니다.

## 주요 기능

- 코레일 열차 조회 및 자동 예매
- 일반실·특실 선택과 매진 열차 예약대기
- 어린이·경로·장애인 승객 예매
- 자동 신용카드 결제
- 자주 사용하는 역 설정
- 텔레그램 알림

## 설치 및 실행

현재 저장소의 변경 사항을 사용하려면 저장소 루트에서 로컬 설치합니다.
이미 `.venv`가 있으면 `uv venv .venv`는 생략하세요.

```sh
uv venv .venv
uv pip install --python .venv/bin/python -e .
.venv/bin/ktxctl --help
.venv/bin/ktxctl
```

기존 `srtgo` 패키지가 설치된 환경에서는 먼저 제거한 뒤 로컬 패키지를 다시 설치하세요.

```sh
uv pip uninstall --python .venv/bin/python srtgo
uv pip install --python .venv/bin/python -e .
.venv/bin/ktxctl
```

## 사용법

1. `로그인 설정`에서 코레일 계정을 저장합니다.
2. 필요하면 `역 설정`, `예매 옵션 설정`, `카드 설정`, `텔레그램 설정`을 실행합니다.
3. `예매 시작`에서 출발·도착역, 날짜, 시각, 승객과 예약할 열차를 선택합니다.
4. 일반실·특실 선택 유형과 카드 결제 여부를 선택해 예매를 시작합니다.
5. `예매 확인/결제/취소`에서 예약을 확인하고 결제하거나 취소합니다.

철도 사업자 선택 없이 코레일 메뉴가 실행됩니다. `KTX만` 옵션을 선택하면
KTX 열차만 조회하고, 해제하면 코레일 일반열차도 조회합니다.

기존 KTX 로그인·역 설정과 카드·텔레그램 설정은 계속 사용합니다.
예매 옵션은 코레일용으로 새로 저장하므로 `예매 옵션 설정` 메뉴에서 다시 설정하세요.
내장 korail2 클라이언트에는 [PR #54](https://github.com/carpedm20/korail2/pull/54)가
반영되어 있으며, 세부 사항과 이전 검증 기록은 [모듈 README](ktxctl/README.md)에 있습니다.

## Acknowledgments

This project includes code from [korail2](https://github.com/carpedm20/korail2)
by carpedm20, licensed under the BSD License. Copyright and license notices
are retained in [LICENSE](LICENSE).

[문서 인덱스](docs/index.md) · [작업 목록](TODO.md)
