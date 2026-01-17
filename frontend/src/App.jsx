import { useState, useEffect, useCallback } from "react";
import "./App.css";
import { Header, BookForm, BookList } from "./components";

function App() {
  const [libri, setLibri] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [formData, setFormData] = useState({
    titolo: "",
    autore: "",
    anno: "",
    genere: "Fantasy",
  });

  const generi = [
    "Fantasy",
    "Horror",
    "Thriller",
    "Romanzo",
    "Storico",
    "Fantascienza",
    "Biografia",
  ];

  const fetchLibri = useCallback(async () => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:12346/api/libri");
      const data = await res.json();
      if (data.success) {
        setLibri(data.data);
      }
    } catch (err) {
      console.error("Errore nel fetch:", err);
    }
    setLoading(false);
  }, []);

  // Carica i libri all'avvio
  useEffect(() => {
    fetchLibri();
  }, [fetchLibri]);

  const addLibro = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await fetch("http://localhost:12346/api/libri", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await res.json();
      if (data.success) {
        setFormData({ titolo: "", autore: "", anno: "", genere: "Fantasy" });
        fetchLibri();
        setError("");
      } else {
        setError(data.error || "Errore nell'aggiunta del libro");
      }
    } catch (err) {
      console.error("Errore nell'aggiunta:", err);
      setError("Errore di connessione al server");
    }
    setLoading(false);
  };

  const deleteLibro = async (id) => {
    setLoading(true);
    try {
      const res = await fetch(`http://localhost:12346/api/libri/${id}`, {
        method: "DELETE",
      });
      const data = await res.json();
      if (data.success) {
        fetchLibri();
      }
    } catch (err) {
      console.error("Errore nella cancellazione:", err);
    }
    setLoading(false);
  };

  const deleteAllLibri = async () => {
    if (window.confirm("Sei sicuro di voler eliminare tutti i libri?")) {
      setLoading(true);
      try {
        const res = await fetch("http://localhost:12346/api/libri", {
          method: "DELETE",
        });
        const data = await res.json();
        if (data.success) {
          fetchLibri();
        }
      } catch (err) {
        console.error("Errore nella cancellazione:", err);
      }
      setLoading(false);
    }
  };

return (
    <div className="container">
      <Header />
      
      {error && (
        <div className="error-banner">
          {error}
          <button className="error-close" onClick={() => setError("")}>
            ×
          </button>
        </div>
      )}
      
      <BookForm
        formData={formData}
        setFormData={setFormData}
        addLibro={addLibro}
        loading={loading}
        generi={generi}
      />
      
      <BookList
        libri={libri}
        loading={loading}
        deleteLibro={deleteLibro}
        deleteAllLibri={deleteAllLibri}
      />
    </div>
  );
}

export default App;
