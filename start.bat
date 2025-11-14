@echo off
echo Starting Newsgroup Classifier...
echo.

echo Starting backend server...
start "Backend Server" cmd /k "node server.js"

timeout /t 3 /nobreak > nul

echo Starting React frontend...
start "React Frontend" cmd /k "npm start"

echo.
echo Both servers are starting...
echo Backend: http://localhost:5001
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause > nul