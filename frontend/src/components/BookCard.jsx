const BookCard = ({ libro, deleteLibro }) => {
  return (
    <div className="libro-card">
      <h3>{libro.titolo}</h3>
      <p>
        <strong>Autore:</strong> {libro.autore}
      </p>
      <p>
        <strong>Anno:</strong> {libro.anno}
      </p>
      <p>
        <strong>Genere:</strong> {libro.genere}
      </p>
      <button className="btn-delete" onClick={() => deleteLibro(libro.id)}>
        Elimina
      </button>
    </div>
  );
};

export default BookCard;
