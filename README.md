# drugstore



1. 프로젝트 checkout
2. 루트 경로(drugsiore/) 에서 shell 실행후 가상환경 생성
    ```
    python -m venv venv
    source venv/bin/activate
    ``` 
3. 패키지 다운로드
    ```
    pip install -r requirements.txt
    ```
4. 테이블 생성
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
