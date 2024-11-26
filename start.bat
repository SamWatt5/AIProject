@echo off
start cmd /k flask --app main run
cd frontend
npm install
pause
cd frontend
npm start