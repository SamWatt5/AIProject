@echo off
echo Starting the application...
start cmd /k flask --app main run
cd frontend
npm run start