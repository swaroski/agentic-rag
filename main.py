import os
import subprocess

# Run the Streamlit app using a subprocess
def start():
    command = ["streamlit", "run", "agentic_rag_streamlit.py", "--server.port", os.getenv("PORT", "8501")]
    subprocess.run(command)

if __name__ == "__main__":
    start()
