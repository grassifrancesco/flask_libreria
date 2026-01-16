import { useState } from "react"
import "./App.css"

function App() {
  const [profile, setProfile] = useState(null)
  const [loading, setLoading] = useState(false)

  const getFakeProfile = async () => {
    setLoading(true)
    try {
      const res = await fetch("http://localhost:12346/fake")
      const data = await res.json()
      setProfile(data.data)   // perché la tua API restituisce { success, data }
    } catch (err) {
      console.error("Errore nel fetch:", err)
    }
    setLoading(false)
  }

  return (
    <div className="container">
      <h1 className="title">Fake Profile Generator</h1>

      <button className="btn" onClick={getFakeProfile}>
        Genera Profilo
      </button>

      {loading && <p className="loading">Caricamento...</p>}

      {profile && (
        <div className="card profile-card">
          <h2>{profile.nome}</h2>
          <p><strong>Email:</strong> {profile.email}</p>
          <p><strong>Telefono:</strong> {profile.telefono}</p>
          <p><strong>Indirizzo:</strong> {profile.indirizzo}</p>
          <p><strong>Azienda:</strong> {profile.azienda}</p>
          <p><strong>Lavoro:</strong> {profile.lavoro}</p>
          <p><strong>Data di nascita:</strong> {profile.data_nascita}</p>
          <p><strong>Username:</strong> {profile.username}</p>
        </div>
      )}
    </div>
  )
}

export default App
