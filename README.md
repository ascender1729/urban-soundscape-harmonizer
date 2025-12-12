
# Urban Soundscape Harmonizer

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [System Architecture](#system-architecture)
5. [Prerequisites](#prerequisites)
6. [Installation](#installation)
7. [Configuration](#configuration)
8. [Running the Application](#running-the-application)
9. [API Documentation](#api-documentation)
10. [Frontend Structure](#frontend-structure)
11. [Backend Structure](#backend-structure)
12. [IoT Simulation](#iot-simulation)
13. [Data Flow](#data-flow)
14. [Troubleshooting](#troubleshooting)
15. [Future Enhancements](#future-enhancements)
16. [Contributing](#contributing)
17. [License](#license)

## Introduction

The Urban Soundscape Harmonizer is an innovative project aimed at monitoring and analyzing urban noise levels in real-time across major Indian cities. By leveraging IoT simulations, machine learning, and data visualization techniques, this project provides a comprehensive view of the acoustic environment in urban areas.

Our system simulates IoT sensors deployed in six major Indian cities: Mumbai, Delhi, Bangalore, Kolkata, Chennai, and Hyderabad. These virtual sensors collect noise level data and frequency distributions, which are then processed, stored, and visualized in an interactive dashboard.

## Features

- Real-time noise level monitoring for six major Indian cities
- Interactive map showing sensor locations and current noise levels
- Dynamic charts displaying historical noise level data
- Color-coded noise level indicators for quick assessment
- Simulated IoT sensor data generation
- RESTful API for data retrieval and storage
- Responsive web design for various device sizes

## Technologies Used

- Frontend:
  - React.js
  - Material-UI
  - Framer Motion (for animations)
  - Recharts (for data visualization)
  - Leaflet (for map integration)

- Backend:
  - FastAPI (Python)
  - Uvicorn (ASGI server)

- Database:
  - InfluxDB (for time-series data storage)

- IoT Simulation:
  - Python

- Development Tools:
  - Git & GitHub (version control)
  - npm (package management)
  - Visual Studio Code (recommended IDE)

## System Architecture

The Urban Soundscape Harmonizer consists of three main components:

1. **Frontend**: A React-based web application that provides an interactive dashboard for visualizing noise data.
2. **Backend**: A FastAPI server that handles data processing, storage, and retrieval.
3. **IoT Simulation**: A Python script that simulates IoT sensors generating noise level data.

These components interact as follows:

1. The IoT simulation generates noise data for each city.
2. This data is sent to the backend via HTTP POST requests.
3. The backend processes the data and stores it in InfluxDB.
4. The frontend periodically fetches the latest data from the backend and updates the dashboard.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- Node.js 14+
- npm 6+
- Git
- InfluxDB 2.0+

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ascender1729/urban-soundscape-harmonizer.git
   cd urban-soundscape-harmonizer
   ```

2. Set up the backend:
   ```
   cd src/backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```
   cd ../../src/frontend
   npm install
   ```

4. Install InfluxDB following the official documentation for your operating system.

## Configuration

1. Backend Configuration:
   - Create a `.env` file in the `src/backend` directory with the following content:
     ```
     INFLUXDB_URL=http://localhost:8086
     INFLUXDB_TOKEN=your_influxdb_token
     INFLUXDB_ORG=your_organization
     INFLUXDB_BUCKET=soundscape
     ```
   - Replace `your_influxdb_token` and `your_organization` with your InfluxDB credentials.

2. Frontend Configuration:
   - If your backend is running on a different port or host, update the API URL in `src/frontend/src/config.js`.

## Running the Application

1. Start the InfluxDB server (follow InfluxDB documentation for your OS).

2. Start the backend:
   ```
   cd src/backend
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   uvicorn main:app --reload --port 3001
   ```

3. Start the frontend (in a new terminal):
   ```
   cd src/frontend
   npm start
   ```

4. Run the IoT simulation (in another new terminal):
   ```
   cd src/iot
   python sensor_simulation.py
   ```

5. Open your browser and navigate to `http://localhost:3000` to view the dashboard.

## API Documentation

The backend provides the following API endpoints:

- `GET /`: Welcome message
- `POST /soundscape`: Submit new soundscape data
- `GET /soundscape/{location}`: Retrieve soundscape data for a specific location

For detailed API documentation, run the backend and visit `http://localhost:3001/docs`.

## Frontend Structure

The frontend is organized as follows:

- `src/`
  - `components/`: React components
    - `Dashboard.js`: Main dashboard component
    - `Map.js`: Map component for visualizing sensor locations
  - `App.js`: Root component
  - `index.js`: Entry point

Key components:

- `Dashboard`: Manages the overall layout and data fetching
- `Map`: Renders the interactive map using Leaflet

## Backend Structure

The backend is structured as follows:

- `main.py`: FastAPI application and route definitions
- `models.py`: Pydantic models for data validation
- `database.py`: InfluxDB connection and query functions

## IoT Simulation

The IoT simulation (`sensor_simulation.py`) generates random noise level data for each city. It sends this data to the backend every 5 seconds, simulating real-time sensor readings.

## Data Flow

1. IoT simulation generates data
2. Data is sent to the backend via POST request
3. Backend validates and stores data in InfluxDB
4. Frontend fetches latest data from backend every 5 seconds
5. Dashboard updates with new data

## Troubleshooting

- If the frontend fails to fetch data, ensure the backend is running and the API URL is correct in `config.js`.
- If the backend fails to start, check your InfluxDB connection settings in the `.env` file.
- For InfluxDB connection issues, verify that the InfluxDB server is running and accessible.

## Future Enhancements

- Implement user authentication
- Add more cities and sensor types
- Integrate machine learning for noise prediction
- Develop mobile app versions
- Implement real-time notifications for high noise levels

## Contributing

We welcome contributions to the Urban Soundscape Harmonizer! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📖 Citation

If you use this project in your research or work, please cite it as:

### BibTeX
```bibtex
@software{dubasi2024_urbansoundscape,
  author       = {Dubasi, Pavan Kumar},
  title        = {Urban Soundscape Harmonizer: IoT-based Urban Noise Monitoring System},
  year         = {2024},
  publisher    = {GitHub},
  url          = {https://github.com/ascender1729/urban-soundscape-harmonizer}
}
```

### APA Format
Dubasi, P. K. (2024). *Urban Soundscape Harmonizer: IoT-based Urban Noise Monitoring System*. GitHub. https://github.com/ascender1729/urban-soundscape-harmonizer

### IEEE Format
P. K. Dubasi, "Urban Soundscape Harmonizer: IoT-based Urban Noise Monitoring System," GitHub, 2024. [Online]. Available: https://github.com/ascender1729/urban-soundscape-harmonizer

---

## 👤 Author

**Pavan Kumar Dubasi**  
Principal AI Consultant | VibeTensor

- 🌐 Website: [dubasipavankumar.com](https://dubasipavankumar.com)
- 💼 LinkedIn: [in/im-pavankumar](https://linkedin.com/in/im-pavankumar)
- 🐦 Twitter: [@the_complex_one](https://twitter.com/the_complex_one)
- 📧 Email: pavan.dubasi2024@gmail.com
- 🆔 ORCID: [0009-0006-1060-4598](https://orcid.org/0009-0006-1060-4598)
