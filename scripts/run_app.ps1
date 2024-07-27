# Start the backend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd src/backend; uvicorn main:app --reload"

# Start the frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd src/frontend; npm start"

# Start the IoT simulation
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python src/iot/sensor_simulation.py"

Write-Host "Application is running!"
