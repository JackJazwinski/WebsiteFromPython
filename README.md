# 🐍 Flask 3-in-1 Demo

A single‑file Flask project that bundles three tiny apps behind one server: a password‑guessing game, a product data lookup, and a live user patcher. The goal is to showcase core Flask patterns—routing, form handling, redirects, and in‑memory data manipulation—using only Python.

## ✨ Features

- **Zero dependencies** beyond Flask itself
- **Three independent flows** exposed from the same app
  - **Password Game** – basic auth logic with redirects
  - **Data Request** – query‑string parsing & dynamic rendering
  - **User Patcher** – add or update records then render a live table
- **Inline HTML/CSS** so you don’t need Jinja templates while learning
- **Hot‑reload ready** via `flask run` or `python app.py`

## 🏃‍♂️ Quick start

```bash
# clone & enter
$ git clone https://github.com/your‑handle/flask‑3‑in‑1.git
$ cd flask‑3‑in‑1

# (optional) create a venv
$ python -m venv .venv && source .venv/bin/activate

# install Flask
$ pip install Flask

# run the dev server
$ python app.py  # -> http://127.0.0.1:5000
```

Set `FLASK_DEBUG=0` or use `app.run(debug=False)` before deploying.

## 🗺️ Route map

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Home page with links to each demo |
| GET | `/passwordGame` | Password input form |
| POST | `/login` | Auth handler → redirects |
| GET | `/logout` | Success page |
| GET | `/error` | Error page |
| GET | `/dataRequest` | Search form for product data |
| GET | `/productDetails` | Result rendering based on query string |
| GET/POST | `/patcher` | Add or patch users & view table |

## 🗂 Project Layout

```
flask‑3‑in‑1/
└── app.py          # all routes & logic in one file
```

Feel free to split templates and static files into folders once you outgrow the inline approach.

## 🚀 Extending it

- Swap the in‑memory lists/dicts with a real database (SQLAlchemy, TinyDB, etc.)
- Replace inline HTML with Jinja templates for cleaner markup reuse
- Add Flask‑Login if you need persistent user sessions beyond the simple password check

## 🙌 Contributing

Pull requests and issues are welcome! If you find a typo or have an idea for a fourth mini‑app, open an issue first so we can discuss.

---

*Originally built as a mid‑term assignment; published so the next learner can hit the ground running.*

