import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Results() {
  const [movie, setMovie] = useState(null);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios(`http://localhost:5000/movie/${movie}`)
      .then((response) => {
        console.log(response.data);
        setMovies(response.data.results || []);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <>
      <div className="carousel w-full">
        {movies.map((movie, index) => (
          <>
            <div id={`slide${index}`} className="carousel-item relative w-full">
              <div className="card bg-base-100 w-96 shadow-xl flex-1">
                <figure className="px-10 pt-10">
                  <img src={movie.Poster} alt="Shoes" className="rounded-xl" />
                </figure>
                <div className="card-body items-center text-center">
                  <h2 className="card-title">{movie.Title}</h2>
                  <p>{movie.Description}</p>
                </div>
                <div className="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
                  <a href={`#slide${index - 1}`} className="btn btn-circle">
                    ❮
                  </a>
                  <a href={`#slide${index - 1}`} className="btn btn-circle">
                    ❯
                  </a>
                </div>
              </div>
            </div>
          </>
        ))}
      </div>
    </>
  );
}
