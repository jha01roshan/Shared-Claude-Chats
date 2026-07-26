# Task management app with Starlette

- Source: https://claude.ai/share/b5285fbc-5849-4939-b473-dcb66f73503b
- Author: Simon
- Created: 2026-03-22
- Messages: 4

---

## Human

Build a task management app with Starlette, it should have projects and tasks and comments and labels

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me build this comprehensive task management app. I'll create a full-stack Starlette application with a polished UI, SQLite database, and complete CRUD for projects, tasks, comments, and labels.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me create the frontend — a polished single-page app with a distinctive editorial/utilitarian design:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

All tests pass. Let me copy the project to the output directory:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's your **TaskFlow** task management app built with Starlette 1.0. Here's what's included:

**Architecture** — Three files, clean separation:
- `main.py` — Starlette app with 16 REST API endpoints, CORS middleware, and lifespan-managed DB init
- `database.py` — Async SQLite layer (aiosqlite) with full CRUD for all entities
- `templates/index.html` — Single-page app with a dark editorial UI

**Data Model** — Five tables with foreign keys and cascade deletes:
- **Projects** — name, description, color, progress tracking
- **Tasks** — status (todo/in_progress/done), priority (low→urgent), belongs to a project
- **Labels** — color-coded tags with many-to-many task association
- **Comments** — threaded on tasks, with author and timestamps
- **Task-Labels** — junction table

**Features** — Dashboard with stats, Kanban board view (3 columns), project filtering, inline status/priority editing, comment threads, label management, and seed data to start with.

**To run it:**
```bash
cd taskflow
pip install starlette uvicorn aiosqlite jinja2
uvicorn main:app --reload --port 8000
```
Then open `http://localhost:8000`.

---

## Human

Turn your tests into pytest tests

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

All 48 tests pass. Let me copy the updated file to outputs.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**48 tests, all passing in under 1 second.** Here's what's covered:

**Test structure** — 7 classes organized by domain, using a session-scoped `TestClient` fixture that initializes a temporary SQLite database with seed data (auto-cleaned after the run).

| Class | Tests | What it covers |
|---|---|---|
| `TestHomepage` | 2 | HTML response, app name present |
| `TestStats` | 2 | All stat keys returned, seed counts correct |
| `TestProjects` | 10 | List, create, detail, update (full + partial), delete, cascade to tasks, validation errors, defaults |
| `TestTasks` | 12 | List, filter by project/status, priority sorting, create with/without labels, detail with nested data, update status/priority/labels, clear labels, delete, cascade to comments |
| `TestComments` | 6 | Create with/without author, validation, appear on task detail, delete |
| `TestLabels` | 7 | List, sorted order, create with/without color, validation, delete, cascade removal from tasks |
| `TestIntegration` | 3 | Full create→update→verify→cleanup workflow, stats mutation tracking, CORS headers |

Run with `python -m pytest test_taskflow.py -v` from the `taskflow/` directory.
