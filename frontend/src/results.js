import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

export default function Results() {
  const { movie_title } = useParams();
  const [results, setResults] = useState([]);
  const [startingMovie, setStartingMovie] = useState([]);

  useEffect(() => {
    axios(`http://localhost:5000/result/${movie_title}`)
      .then((response) => {
        console.log(response.data);
        setResults(Object.values(response.data.results));
      })
      .catch((err) => {
        console.log(err);
      });
  }, [movie_title]);

  useEffect(() => {
    axios(`http://localhost:5000/movie/${movie_title}`)
      .then((response) => {
        console.log(response.data);
        setStartingMovie(response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [movie_title]);

  function MovieCard({ movie }) {
    return (
      <div className="card w-80 bg-base-300 m-2">
        <div className="card-body">
          <img src={movie.Poster} alt={movie.Title} className="rounded-lg" />
          <h1 className="card-title">{movie.Title}</h1>
          <h2 className="card-title">Directed by:</h2>
          <p className="card-normal">{movie.Director}</p>
          <h2 className="card-subtitle">Cast:</h2>
          <p className="card-normal">{movie.Cast}</p>
          <h2 className="card-subtitle">Genres:</h2>
          <p className="card-normal">{movie.Genre}</p>
        </div>
      </div>
    );
  }

  function StartingMovieCard({ movie }) {
    return (
      <div className="card w-80 bg-base-300">
        <div className="card-body">
          <img src={movie.Poster} alt={movie.Title} className="rounded-lg" />
          <div>
            <h1 className="card-title">{movie.Title}</h1>
            <h2 className="card-title">Directed by:</h2>
            <p className="card-normal">{movie.Director}</p>
            <h2 className="card-subtitle">Cast:</h2>
            <p className="card-normal">{movie.Cast}</p>
            <h2 className="card-subtitle">Genres:</h2>
            <p className="card-normal">{movie.Genre}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="flex justify-between">
        <div className="w-1/6">
          <StartingMovieCard movie={startingMovie} />
        </div>
        <div className="w-4/6">
          <div className="carousel carousel-center rounded-box w-3/6 bg-base-200">
            {results.map((movie, index) => (
              <div key={index} className="carousel-item">
                <MovieCard movie={movie} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
