@echo off
start cmd /k flask --app main run
cd frontend
npm run start