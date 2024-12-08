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

  function MovieCard({ movie, index }) {
    return (
      <div className="card w-96 bg-base-300 m-2" id={`slide${index}`}>
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

  let pos = { top: 0, left: 0, x: 0, y: 0 };
  const ele = document.getElementById("container");

  function mouseDownHandler(e) {
    ele.style.cursor = "grabbing";
    ele.style.userSelect = "none";

    pos = {
      left: ele.scrollLeft,
      top: ele.scrollTop,
      x: e.clientX,
      y: e.clientY,
    };

    document.addEventListener("mousemove", mouseMoveHandler);
    document.addEventListener("mouseup", mouseUpHandler);
  }

  function mouseMoveHandler(e) {
    const dx = e.clientX - pos.x;
    const dy = e.clientY - pos.y;
    ele.scrollTop = pos.top - dy;
    ele.scrollLeft = pos.left - dx;
  }

  function mouseUpHandler(e) {
    ele.style.cursor = 'grab';
    ele.style.removeProperty('user-select');

    document.removeEventListener('mousemove', mouseMoveHandler);
    document.removeEventListener('mouseup', mouseUpHandler);
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
          <div id="container" onMouseDown={mouseDownHandler} className="inline-flex w-screen bg-base-200 overflow-scroll" style={{ scrollbar: "hidden"}}>
            {results.map((movie, index) => (
              <div key={index} className="flex">
                <MovieCard movie={movie} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
