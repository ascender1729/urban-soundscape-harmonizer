import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Fix for default marker icons
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const cityCoordinates = {
  'Mumbai': [19.0760, 72.8777],
  'Delhi': [28.6139, 77.2090],
  'Bangalore': [12.9716, 77.5946],
  'Kolkata': [22.5726, 88.3639],
  'Chennai': [13.0827, 80.2707],
  'Hyderabad': [17.3850, 78.4867]
};

function Map({ soundscapeData }) {
  const center = [20.5937, 78.9629]; // Coordinates for center of India

  return (
    <div style={{ height: '400px', width: '100%', marginBottom: '20px', borderRadius: '15px', overflow: 'hidden' }}>
      <MapContainer center={center} zoom={5} style={{ height: '100%', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {soundscapeData.map((data, index) => (
          <Marker 
            key={index} 
            position={cityCoordinates[data.location]}
          >
            <Popup>
              <strong>{data.location}</strong><br />
              Noise Level: {data.noise_level.toFixed(2)} dB
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default Map;