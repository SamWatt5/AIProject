import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function App() {
  const [movie, setMovie] = useState(null);
  const [movies, setMovies] = useState([]);
  const navigate = useNavigate();

  function onChange(event) {
    setMovie(event.target.value);
  }

  function searchMovie() {
    if (movie == null) return;

    axios(`http://localhost:5000/search/${movie}`)
      .then((response) => {
        console.log(response.data);
        setMovies(response.data.movies);
      })
      .catch((err) => {
        console.log(err);
      });

    document.getElementById("moviesModal").showModal();
  }

  function goToResults(movie_title) {
    console.log(movie_title);
    navigate(`/result/${movie_title}`);
  }

  return (
    <>
      <div className="left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 absolute w-1/2 h-1/2 card card-side bg-base-200 shadow-xl">
        <div className="card-body">
          <h2 className="card-title text-3xl">Search for movie</h2>
          <p>Type the name into the search box then press search</p>
          <input
            type="text"
            onChange={onChange}
            placeholder="Type here"
            className="input input-bordered w-3/4 top-1/2 absolute"
          />
          <div className="card-actions justify-end">
            <button className="btn btn-primary" onClick={searchMovie}>
              Search
            </button>
          </div>
        </div>
      </div>
      <dialog id="moviesModal" className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-xl">Movies</h3>
          {movies && (
            <>
              {movies.map((movie, index) => (
                <>
                  <form
                    key={index}
                    method="dialog"
                    className="p-3 bg-base-200 w-3/4 rounded m-2"
                  >
                    <button
                      className="btn mr-5 btn-secondary inline"
                      onClick={() => goToResults(movie)}
                    >
                      {index + 1}
                    </button>
                    <p className="inline">{movie}</p>
                  </form>
                </>
              ))}
            </>
          )}
        </div>
        <form method="dialog" className="modal-backdrop">
          <button>close</button>
        </form>
      </dialog>
    </>
  );
}

export default App;
