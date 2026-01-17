import { useState } from "react";

const BookForm = ({ formData, setFormData, addLibro, loading, generi }) => {
  const [errors, setErrors] = useState({});

  const validateYear = (year) => {
    const currentYear = new Date().getFullYear();
    const yearNum = parseInt(year);

    if (!year) return "⚠️ L'anno è obbligatorio";
    if (isNaN(yearNum))
      return "⚠️ Per favore inserisci un anno valido (es: 2024)";
    if (yearNum < 0) return "⚠️ L'anno non può essere negativo";
    if (yearNum > currentYear + 1)
      return `⚠️ L'anno non può essere maggiore di ${currentYear + 1}`;

    return "";
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });

    // Validate year in real-time
    if (name === "anno") {
      const yearError = validateYear(value);
      setErrors({
        ...errors,
        anno: yearError,
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate all fields before submission
    const yearError = validateYear(formData.anno);

    if (yearError) {
      setErrors({ anno: yearError });
      return;
    }

    // Clear errors and submit
    setErrors({});
    addLibro(e);
  };

  return (
    <div className="card">
      <div className="form-header">
        <h2>➕ Aggiungi Nuovo Libro</h2>
        <p>Riempi i dettagli per aggiungere un libro alla tua collezione</p>
      </div>
      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          name="titolo"
          placeholder="Titolo"
          value={formData.titolo}
          onChange={handleChange}
          required
          className="form-input"
        />
        <input
          type="text"
          name="autore"
          placeholder="Autore"
          value={formData.autore}
          onChange={handleChange}
          required
          className="form-input"
        />
        <div className="form-group">
          <input
            type="text"
            name="anno"
            placeholder="Anno"
            value={formData.anno}
            onChange={handleChange}
            required
            className={`form-input ${errors.anno ? "error" : ""}`}
          />
          {errors.anno && <div className="error-message">{errors.anno}</div>}
        </div>
        <select
          name="genere"
          value={formData.genere}
          onChange={handleChange}
          className="form-select"
        >
          {generi.map((genere) => (
            <option key={genere} value={genere}>
              {genere}
            </option>
          ))}
        </select>
        <button
          type="submit"
          className="btn btn-primary"
          disabled={loading || errors.anno}
        >
          Aggiungi Libro
        </button>
      </form>
    </div>
  );
};

export default BookForm;
