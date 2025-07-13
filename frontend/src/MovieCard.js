import React from 'react';

const MovieCard = ({ movie }) => (
  <div className="movie-card">
    <img src={movie.poster} alt={movie.title} />
    <h3>{movie.title}</h3>
    <a href={movie.downloadLink} target="_blank" rel="noopener noreferrer">
      🎬 Download
    </a>
  </div>
);

export default MovieCard;
