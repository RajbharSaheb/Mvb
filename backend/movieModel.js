const mongoose = require('mongoose');

// Define schema based on your existing collection's structure
const movieSchema = new mongoose.Schema({}, { strict: false });

// Use the exact collection name
module.exports = mongoose.model('RajbharPahadan', movieSchema, 'RajbharPahadan');
//                ^ model name         ^ schema      ^ actual collection name
