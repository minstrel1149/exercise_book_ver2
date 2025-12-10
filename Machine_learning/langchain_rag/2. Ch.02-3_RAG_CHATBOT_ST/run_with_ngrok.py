import os
from pyngrok import ngrok
import subprocess

public_url = ngrok.connect(8501)
print(f'Streamlit Public URL: {public_url}')

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

