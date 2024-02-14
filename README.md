# DirectDownloadAPI

## Install
	
- 소스 CheckOut
	
	```bash
	
	```

- python: 3.6 이상 (3.7 테스트됨)
- 가상환경 설정(권장)

	```bash
	$ cd directDownload
	$ python3 -m venv .venv
	$ source .venv/bin/activate
	```
	
- 라이브러리

	```bash
	$ pip install –r requirement.txt	
	```
	
## Run

- getinfo.py 에서 포트 수정 가능

    ```bash
    $ nphup python getinfo.py > /dev/null & disown -h
     ```

## API

### direct
- path: /direct
- method: POST(multipart/form-data)
- params:
	- guno: grade unit number
