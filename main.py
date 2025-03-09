from fastapi import FastAPI
from starlette.responses import RedirectResponse
import subprocess
import os

app = FastAPI()

# Route to redirect to Streamlit
@app.get("/")
async def root():
    # Redirect to Streamlit app
    return RedirectResponse(url="/streamlit")

# Run Streamlit as a subprocess
@app.get("/streamlit")
async def run_streamlit():
    # Check if Streamlit is already running
    if not os.getenv("STREAMLIT_RUNNING"):
        os.environ["STREAMLIT_RUNNING"] = "true"
        # Run Streamlit as a subprocess
        subprocess.Popen(["streamlit", "run", "app.py", "--server.port=8501"])
    # Redirect to the Streamlit app
    return RedirectResponse(url="http://localhost:8501")
