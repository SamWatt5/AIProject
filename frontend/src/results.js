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
      <div className="card w-96 bg-base-300 m-2">
        <div className="card-body grid gap-4 grid-cols-3 grid-rows-1">
          <div className="row-span-1 col-span-1">
            <img src={movie.Poster} alt={movie.Title} className="rounded-lg " />
            <h1 className="card-title">{movie.Title}</h1>
          </div>
          <div className="columns-2 col-span-2">
            <h2 className="card-subtitle">Directed by:</h2>
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
      <h1 className="text-3xl text-center">
        Found {results.length} movies similar to {startingMovie.Title}...
      </h1>
      <div className="grid gap-4 grid-cols-3 grid-rows-2 text-center">
        <div className="row-span-1 col-span-3 col-start-2">
          <MovieCard movie={startingMovie} />
        </div>
        <div className="row-span-1">
          <div className="carousel carousel-center rounded-box w-screen bg-base-200">
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
