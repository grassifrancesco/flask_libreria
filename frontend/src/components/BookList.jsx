import BookCard from "./BookCard";

const BookList = ({ libri, loading, deleteLibro, deleteAllLibri }) => {
  return (
    <div className="card book-list-container">
      <div className="header">
        <h2>📚 Libri ({libri.length})</h2>
        {libri.length > 0 && (
          <button className="btn-delete" onClick={deleteAllLibri}>
            Elimina Tutti
          </button>
        )}
      </div>

      {loading && <p className="loading">Caricamento...</p>}

      {libri.length === 0 && !loading && (
        <p className="empty">Nessun libro nella libreria</p>
      )}

      <div className="libri-grid">
        {libri.map((libro) => (
          <BookCard key={libro.id} libro={libro} deleteLibro={deleteLibro} />
        ))}
      </div>
    </div>
  );
};

export default BookList;
