# Flask Libreria

Progetto di **TPI** per la creazione di una libreria digitale.  
Il backend è sviluppato con **Flask** e utilizza **SQLite** come database, mentre il frontend è realizzato con **React** e **ViteJS**.

---

## Diagramma della logica

![Diagramma della logica dell'applicativo](diagramma_flask_libreria_drawio.svg)

---

## Analisi dei requisiti

1. Gestione dei libri tramite API REST  
2. Persistenza dei dati con database SQLite  
3. Interfaccia frontend moderna e responsiva  
4. Funzionalità CRUD (Create, Read, Update, Delete)  
5. Integrazione tra backend e frontend  

---

## Funzionalità implementate

- [x] Configurazione database SQLite  
- [x] Endpoint **GET /api/libri**  
- [x] Endpoint **POST /api/libri**  
- [x] Endpoint **DELETE /api/libri/[id]**  
- [x] Endpoint **DELETE /api/libri**  
- [x] Creazione del frontend con React + Vite  
  - [x] Miglioramento estetico dell'interfaccia  

---

## Attività rimanenti

- [ ] Ottimizzazione del backend (validazioni, gestione errori)  
- [ ] Miglioramenti al frontend (UI/UX, messaggi di errore, rifiniture grafiche)  

---

## Struttura del progetto

### Backend (Flask)
- API REST per la gestione dei libri  
- Connessione al database SQLite  
- Validazione delle richieste  

### Frontend (React + ViteJS)
- Interfaccia utente per la visualizzazione e gestione dei libri  
- Componenti modulari e riutilizzabili  
- Gestione degli stati e delle chiamate API  

---

## Istruzioni di avvio

1. Clonare il repository  
2. Installare SQLite3 e creare il database `libri.sqlite3` nella cartella backend con il comando:  
   ```bash
   sqlite3 libri.sqlite3
   ```
3. Creare la tabella libro con il comando:
   ```sql
   CREATE TABLE libro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    autore TEXT NOT NULL,
    anno INTEGER NOT NULL
   );
   ```
4. Installare le dipendenze del backend:
   ```bash
   pip install flask flask_cors
   ```
   (SQLite3 è già incluso di default in Python)
5. Avviare il server Flask:
   ```bash
   python3 main.py
   ```
6. Installare le dipendenze del frontend:
   ```bash
   npm install
   ```
7. Avviare il frontend:
   ```bash
   npm run dev
   ```

---

## Licenza

Questo progetto è rilasciato sotto la licenza GPL3.
Per maggiori dettagli, consulta il file [LICENSE](LICENSE)

---

https://sqlite.org/codeofethics.html
