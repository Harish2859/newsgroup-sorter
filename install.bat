@echo off
echo Installing Newsgroup Classifier UI...
echo.

echo Installing Python dependencies...
pip install scikit-learn numpy pandas matplotlib seaborn

echo.
echo Installing Node.js dependencies...
npm install

echo.
echo Setup complete!
echo.
echo To run the application:
echo 1. Start the backend server: npm run server
echo 2. In another terminal, start the React app: npm start
echo.
pause