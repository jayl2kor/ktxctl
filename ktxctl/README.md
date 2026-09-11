# ktxctl CLI 및 패키지

- `cli.py`: 코레일 전용 역·승객 선택, 예약 및 결제를 제공하는 `ktxctl` CLI. 실행 진입점은 `ktxctl.cli:ktxctl`입니다.
- `ktx.py`: korail2에서 가져온 KTX API 클라이언트와 열차·승객 모델.
- `ktx_auth.py`: KTX 요청의 DynaPath 토큰 인코딩.
- `__init__.py`: Python 패키지 진입점.

## 코레일 전용 구성

SRT 클라이언트, SRT 역 목록과 사업자 선택 메뉴를 제거했습니다.
실행 명령과 Python 패키지명은 모두 `ktxctl`이며, 배포에는 `ktxctl` 패키지만 포함합니다.
기존 KTX 로그인·역 설정과
카드·텔레그램 설정을 계속 사용합니다. `KTX만` 예매 옵션은
코레일 일반열차를 제외하는 조회 필터로 유지합니다.
예매 옵션은 keyring의 `KTX` 서비스에 새로 저장하며 이전 SRT 설정을
읽거나 이관하지 않습니다. `예매 옵션 설정` 메뉴에서 다시 설정하세요.

## korail2 PR #54

[원본 PR](https://github.com/carpedm20/korail2/pull/54)의 커밋
`4b134266fff097ea0fd54e9f760cb128b6c8f878`을 내장 클라이언트에 이식했습니다.
별도 `korail2` 패키지 설치는 필요하지 않습니다. 기존 `curl_cffi` 세션을 사용합니다.

- 앱 버전 `250601002`, Android 13 / SM-S928N User-Agent 적용.
- 로그인·열차 조회·예약 요청에 `x-dynapath-m-token` 헤더 추가.
- 로그인 본문에 AES-CBC로 생성한 `Sid` 추가.
- 조회는 POST와 쿼리 매개변수, 예약은 GET과 쿼리 매개변수를 사용.

PR 원본과 동일하게 조회의 `Sid`는 빈 문자열이며 예약에는 `Sid`를 추가하지
않습니다. 원본이 계산만 하고 전송하지 않는 값을 별도로 확장하지 않았습니다.
토큰 엔진은 별도 파일로 분리하고 타입 표기를 추가했습니다.

## 로컬 실행 및 검증

SRT 제거 및 이름 변경 후의 검증 결과는 [검증 기록](../docs/validation.md)을 참고하세요.

이미 `.venv`가 있으면 가상환경 생성은 생략하세요. 이전 패키지가 설치된 환경의
제거 및 재설치 방법은 [프로젝트 README](../README.md#설치-및-실행)를 참고하세요.

```sh
uv venv .venv
uv pip install --python .venv/bin/python -e .
.venv/bin/ktxctl --help
uv build
```

2026-09-11 PR #54 이식 당시의 검증 기록(SRT 제거 전):
원본 토큰 출력 12개 및 문자 인코딩 6개 비교,
Sid 복호화, 보호 경로 6개와 비보호 경로 확인. 로컬 HTTP 서버에 실제
`curl_cffi`로 로그인·조회·예약·조회 결과 없음 경로를 실행했습니다.
실제 코레일 서버의 로그인·예매 성공 여부는 검증하지 않았습니다.

[문서 인덱스](../docs/index.md) · [작업 목록](../TODO.md)
