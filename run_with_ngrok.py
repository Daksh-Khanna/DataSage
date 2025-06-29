from pyngrok import ngrok
import subprocess
import time
from config import NGROK_TOKEN

# Set your auth token
ngrok.set_auth_token(NGROK_TOKEN)

# Start the Streamlit app in a separate process
process = subprocess.Popen(["streamlit", "run", "app.py"])

# Give Streamlit a couple seconds to start
time.sleep(2)

# Open ngrok tunnel to port 8501
public_url = ngrok.connect(8501)
print("Public URL:", public_url)

# Keep the script running so ngrok tunnel stays open
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Shutting down...")
    process.terminate()
    ngrok.disconnect(public_url)
