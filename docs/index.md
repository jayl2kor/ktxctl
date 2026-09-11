# 문서 인덱스

| 항목 | 위치 | 설명 |
| --- | --- | --- |
| 프로젝트 사용법 | [README](../README.md) | ktxctl 설치 및 예약 도구 사용법 |
| ktxctl CLI 및 코레일 클라이언트 | [모듈 README](../ktxctl/README.md) | ktxctl 패키지 구성과 실행 방법 |
| CLI 진입점 | [cli.py](../ktxctl/cli.py) | ktxctl.cli:ktxctl 명령 진입점 |
| KTX 클라이언트 | [ktx.py](../ktxctl/ktx.py) | 내장 korail2, 로그인·조회·예약 |
| KTX 요청 토큰 | [ktx_auth.py](../ktxctl/ktx_auth.py) | PR #54의 DynaPath 인코딩 |
| 작업 관리 | [TODO](../TODO.md) | PR #54 이식, SRT 기능 제거 및 ktxctl 명령·패키지 변경 작업 상태 |
| 변경 검증 | [validation.md](validation.md) | 오프라인 동작·터미널·설치·배포 검증 결과 |

2026-09-11: SRT 전용 코드를 제거하고 코레일 전용으로 구성했습니다.
실행 명령과 Python 패키지명을 모두 `ktxctl`로 변경했습니다.
설치 대상은 `ktxctl` 패키지이며 CLI 진입점은 `ktxctl.cli:ktxctl`입니다.
코레일 일반열차를 제외하는 `KTX만` 옵션도 유지합니다.
현재 수정본의 로컬 설치와 사용법은 프로젝트 README를 참고하세요.

2026-09-11: korail2 PR #54의 토큰 헤더, 로그인 Sid, 앱 식별 정보 및 조회
POST 변경을 반영했습니다. 적용 커밋과 원본 요청 방식의 세부 사항은 모듈
README에 기록했습니다.
