# flask_libreria

Progetto di TPI per la creazione di una libreria digitale.  
Il backend è sviluppato con **Flask** e utilizza **SQLite** come database, mentre il frontend è realizzato con **React** e **ViteJS**.

---

## Diagramma della logica

![Diagramma della logica riguardo il funzionamento dell'applicativo](diagramma_flask_libreria_drawio.svg)

---

## Analisi dei requisiti

1. Gestione dei libri tramite API REST
2. Persistenza dei dati con database SQLite
3. Interfaccia frontend moderna e responsiva
4. Funzionalità CRUD (Create, Read, Update, Delete)
5. Integrazione tra backend e frontend
- ecc.

---

## Funzionalità implementate

- [x] Configurazione database SQLite  
- [x] Endpoint **GET /api/libri**  
- [x] Endpoint **POST /api/libri**  
- [x] Endpoint **DELETE /api/libri/<id>**  
- [x] Endpoint **DELETE /api/libri**  
- [x] Creazione del frontend con React + Vite  
  - [x] Miglioramento estetico dell'interfaccia  

---

## Attività rimanenti

- [ ] Sistemare il backend (ottimizzazione, validazioni, gestione errori)  
- [ ] Sistemare il frontend (UI/UX, allineamento messaggi di errore, rifiniture grafiche)  

---

## Struttura del progetto

- **Backend (Flask)**  
  - API REST per la gestione dei libri  
  - Connessione al database SQLite  
  - Validazione delle richieste  

- **Frontend (React + ViteJS)**  
  - Interfaccia utente per la visualizzazione e gestione dei libri  
  - Componenti modulari e riutilizzabili  
  - Gestione degli stati e delle chiamate API  

---

## Istruzioni di avvio

1. Clonare il repository  
2. Installare le dipendenze del backend (`pip install flask flask_cors`) SQLite3 dovrebbe essere già installato di default
3. Avviare il server Flask (`python3 main.py`)  
4. Installare le dipendenze del frontend (`npm install`)  
5. Avviare il frontend (`npm run dev`)

---

## Licenza

Questo progetto è rilasciato sotto la licenza GPL3. Per maggiori dettagli, consulta il file [LICENSE.md](LICENSE.md).

---

## Codice di etica

Il codice di etica di SQLite è disponibile all'indirizzo [https://sqlite.org/codeofethics.html](https://sqlite.org/codeofethics.html).
