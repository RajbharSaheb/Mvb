const mongoose = require('mongoose');

const movieSchema = new mongoose.Schema({
  title: String,
  poster: String,
  downloadLink: String,
});

const collectionName = process.env.MONGO_COLLECTION;
module.exports = mongoose.model('Movie', movieSchema, collectionName);
