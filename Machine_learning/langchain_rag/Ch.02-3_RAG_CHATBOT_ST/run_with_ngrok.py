import os
from pyngrok import ngrok
import subprocess

# Streamlit 기본 포트인 8501에 대한 http 터널 생성
public_url = ngrok.connect(8501)
print(f"Streamlit Public URL: {public_url}")

# Streamlit 앱 실행
try:
    # app.py 파일의 절대 경로를 사용합니다.
    app_path = os.path.abspath("app.py")
    process = subprocess.Popen(["streamlit", "run", app_path, "--server.port", "8501"])
    process.wait()
except KeyboardInterrupt:
    print("Shutting down Streamlit and ngrok.")
    ngrok.kill()
    process.kill()
