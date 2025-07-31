# 🧪 PubMed Scraper CLI Tool

A command-line Python tool to search PubMed articles by keyword and extract information about papers that include **non-academic authors**.

---

## 🔍 Features

- Search PubMed articles using a query
- Automatically filters papers with at least one **non-academic author**
- Extracts key info: Title, Publication Date, Authors, Affiliations
- Saves results to a clean `.csv` file
- Supports logging and error handling
- Built using **Poetry** for clean dependency management

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pubmed-scraper.git
cd pubmed-scraper
```

### 2. Install Dependencies

Make sure Poetry is installed:  
[Poetry Installation Guide](https://python-poetry.org/docs/#installation)

Then run:

```bash
poetry install
```

---

## ▶️ Usage

After installing:

```bash
poetry run get-papers-list --query "covid" --file result.csv
```

Optional flags:
- `--debug` – Show debug logs

---

## 🧩 Code Organization

```
pubmed_scraper/
├── src/
│   └── pubmed_scraper/
│       ├── fetch.py          # Core functions for fetching and parsing articles
│       ├── cli.py            # Command-line interface logic
│       └── __init__.py
├── tests/
│   └── test_fetch.py         # Tests for fetch functionality
├── pyproject.toml            # Poetry config & dependencies
├── README.md
└── result.csv                # Output file (generated)
```

---

## 🛠 Built With

- [Poetry](https://python-poetry.org/)
- [Requests](https://docs.python-requests.org/)
- [Rich](https://rich.readthedocs.io/en/stable/)
- [Entrez API (NCBI)](https://www.ncbi.nlm.nih.gov/home/develop/api/)

---

## 📋 License

MIT License

---

## 🙋‍♀️ Author

Pratha Khare  
Feel free to fork, star, and raise issues!
### ✅ Maintained by Pratha Khare

> Version: 1.0.0
