# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set up InfluxDB (assuming it's running in Docker)
docker run -d -p 8086:8086 --name influxdb influxdb:2.0

# Additional setup steps can be added here

Write-Host "Environment setup complete!"
