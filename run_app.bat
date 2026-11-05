@echo off
echo ========================================================
echo  24CS2506 - Building Applications using GPT-4
echo  Experiment 4: Personalized Recommendation System
echo ========================================================
echo.
echo Launching Streamlit Web Application on port 8503...
echo.

cd /d "%~dp0"
python -m streamlit run app.py --server.port 8503 --server.headless false

pause

