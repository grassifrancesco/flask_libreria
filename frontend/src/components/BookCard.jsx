const BookCard = ({ libro, deleteLibro }) => {
  const getGenreColor = (genere) => {
    const colors = {
      Fantasy: "#8b5cf6",
      Horror: "#ef4444",
      Thriller: "#f59e0b",
      Romanzo: "#3b82f6",
      Storico: "#6b7280",
      Fantascienza: "#06b6d4",
      Biografia: "#10b981",
    };
    return colors[genere] || "#6b7280";
  };

  return (
    <div className="libro-card">
      <div className="book-header">
        <h3>{libro.titolo}</h3>
        <span
          className="genre-badge"
          style={{ backgroundColor: getGenreColor(libro.genere) }}
        >
          {libro.genere}
        </span>
      </div>
      <div className="book-info">
        <div className="info-row">
          <span className="info-icon">✍️</span>
          <span>{libro.autore}</span>
        </div>
        <div className="info-row">
          <span className="info-icon">📅</span>
          <span>{libro.anno}</span>
        </div>
      </div>
      <button className="btn-delete" onClick={() => deleteLibro(libro.id)}>
        Elimina
      </button>
    </div>
  );
};

export default BookCard;
