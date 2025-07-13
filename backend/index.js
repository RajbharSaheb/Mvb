const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();
const Movie = require('./movieModel');
app.use(cors());

const dbName = process.env.MONGO_DB_NAME;
const mongoURI = `${process.env.MONGODB_URI}/${dbName}`;

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('✅ MongoDB connected'))
  .catch(err => console.error(err));

app.get('/api/movies', async (req, res) => {
  try {
    const movies = await Movie.find();
    res.json(movies);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch movies' });
  }
});

app.listen(5000, () => {
  console.log('🚀 Backend running on http://localhost:5000');
});
