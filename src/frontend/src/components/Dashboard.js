import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Grid, Paper, Typography, Box, CircularProgress } from '@mui/material';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import Map from './Map';
import './Dashboard.css';

const cities = ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'];
function Dashboard() {
  const [soundscapeData, setSoundscapeData] = useState([]);
  const [error, setError] = useState(null);
  const [historicalData, setHistoricalData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const data = await Promise.all(
          cities.map(async (city) => {
            const response = await fetch(`http://localhost:3001/soundscape/${city}`);
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
        );
        setSoundscapeData(prevData => {
          const updatedData = [...prevData];
          data.forEach((newCityData, index) => {
            if (updatedData[index]) {
              updatedData[index] = {
                ...updatedData[index],
                noise_level: newCityData.noise_level,
                frequency_distribution: newCityData.frequency_distribution,
                timestamp: newCityData.timestamp
              };
            } else {
              updatedData[index] = newCityData;
            }
          });
          return updatedData;
        });
        updateHistoricalData(data);
        setError(null);
      } catch (e) {
        console.error("Fetch error:", e);
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
  
    fetchData();
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  const updateHistoricalData = (newData) => {
    setHistoricalData(prevData => {
      const updated = { ...prevData };
      newData.forEach(item => {
        if (!updated[item.location]) {
          updated[item.location] = [];
        }
        updated[item.location].push({
          time: new Date().toLocaleTimeString(),
          noiseLevel: item.noise_level
        });
        if (updated[item.location].length > 20) {
          updated[item.location].shift();
        }
      });
      return updated;
    });
  };

  const getNoiseColor = (level) => {
    if (level < 50) return '#4caf50';
    if (level < 70) return '#ff9800';
    return '#f44336';
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box className="dashboard" sx={{ p: 3, backgroundColor: '#f5f5f5' }}>
      <Typography variant="h2" className="dashboard-title" gutterBottom align="center">
        Indian Urban Soundscape Harmonizer
      </Typography>
      {error && <Typography color="error" align="center">Error: {error}</Typography>}
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Map soundscapeData={soundscapeData} />
        </Grid>
        {soundscapeData.map((data, index) => (
          <Grid item xs={12} md={6} lg={4} key={index}>
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <Paper className="location-data" elevation={3} sx={{ p: 2, height: '100%', borderRadius: '15px', overflow: 'hidden' }}>
                <Typography variant="h5" gutterBottom align="center">{data.location}</Typography>
                <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', my: 2 }}>
                  <motion.div
                    style={{
                      width: 100,
                      height: 100,
                      borderRadius: '50%',
                      backgroundColor: getNoiseColor(data.noise_level),
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center',
                    }}
                    animate={{ scale: [1, 1.1, 1] }}
                    transition={{ duration: 2, repeat: Infinity }}
                  >
                    <Typography variant="h4" sx={{ color: 'white', fontWeight: 'bold' }}>
                      {Math.round(data.noise_level)}
                    </Typography>
                  </motion.div>
                </Box>
                <Typography variant="subtitle1" align="center" gutterBottom>
                  Noise Level: {Math.round(data.noise_level)} dB
                </Typography>
                <Box sx={{ height: 200, mt: 2 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={historicalData[data.location] || []}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="time" />
                      <YAxis domain={[0, 100]} />
                      <Tooltip />
                      <Line type="monotone" dataKey="noiseLevel" stroke="#8884d8" />
                    </LineChart>
                  </ResponsiveContainer>
                </Box>
                <Typography variant="body2" className="frequency-distribution" sx={{ mt: 2 }}>
                  Frequency Distribution: {data.frequency_distribution.map(f => f.toFixed(2)).join(', ')}
                </Typography>
              </Paper>
            </motion.div>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}

export default Dashboard;