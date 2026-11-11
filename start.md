# Návod na spustenie a zastavenie RAG aplikácie

Tento dokument slúži ako rýchly sprievodca, ako kedykoľvek spustiť alebo vypnúť aplikáciu **ApexBuild Construction Ontology RAG**.

---

## 🚀 Rýchle spustenie (Quick Start)

### Krok 1: Uistite sa, že beží Ollama
Ollama beží väčšinou automaticky na pozadí v macOS lište. Pre overenie alebo manuálne spustenie stačí otvoriť nový Terminál a spustiť:
```bash
ollama run qwen2.5:7b
```
*(alebo ak beží na pozadí, netreba robiť nič).*

---

### Krok 2: Prejdite do priečinka projektu a spustite Streamlit
V Termináli zadajte:
```bash
cd /Users/kristianragancik/Documents/SaSW/RAG
streamlit run app.py
```

Po spustení sa v Termináli zobrazí:
```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

Aplikácia sa automaticky otvorí vo vašom predvolenom webovom prehliadači na adrese:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🛑 Ako aplikáciu vypnúť

1. Prepnite sa do okna **Terminálu**, kde beží `streamlit run app.py`.
2. Stlačte klávesovú skratku **`Ctrl + C`**.
3. Tým sa webový server okamžite ukončí a uvoľní port `8501`.

---

## ⚡ Užitočné príkazy a riešenie problémov

### 1. Ak je port 8501 obsadený
Ak ste zabudli starý proces vypnúť a píše vám, že port je obsadený, viete ho uvoľniť príkazom:
```bash
lsof -ti:8501 | xargs kill -9
```

### 2. Spustenie na inom porte
Ak chcete aplikáciu spustiť na inom porte (napr. 8502):
```bash
streamlit run app.py --server.port 8502
```

### 3. Prebudovanie / opätovné vygenerovanie 10 PDF dokumentov
Ak by ste v budúcnosti chceli vygenerovať PDF súbory nanovo:
```bash
python3 generate_pdfs.py
```
*(Potom v aplikácii v ľavom paneli pod **Advanced Parameters** kliknite na **🔄 Rebuild Vector Index** alebo reštartujte aplikáciu).*

