# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current Feature
Information relevant to the current feature that is being worked on can be found in @context/current-feature.md

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload

# Seed the database (verbs, moods, tenses)
python -m app.db.seed

# Run all tests
pytest

# Run a single test
pytest tests/path/test_file.py::test_name
```

---

## Current Implementation Status

**Implemented:**
- `GET /verbs` — lists all verbs
- `GET /moods` — lists all moods
- `GET /tenses` — lists all tenses
- `GET /users` — lists all users (does not yet follow standard response wrapper)
- ORM models: `Verb`, `Mood`, `Tense`, `User`
- Database seeding: 10 common verbs, 3 moods (Indicative, Subjunctive, Imperative), 16 tenses

**Not yet implemented (core work remaining):**
- `Conjugation` ORM model (see section 5.4)
- `GET /conjugations` endpoint with filtering (see section 2.1) — this is the primary feature
- Conjugation seed data
- Test suite (`tests/` directory exists but is empty)

---

## 1. Project Overview

Build a **RESTful API** using FastAPI that provides Spanish verb conjugations.

This backend will:

* Return conjugations for one or more verbs
* Support filtering by mood and tense
* Serve a React frontend for practicing verb conjugations

---

## 2. Core Features

### 2.1 Conjugations Endpoint

**GET `/conjugations`**

Returns conjugations based on query parameters.

#### Query Parameters

| Parameter | Required | Description                       |
| --------- | -------- | --------------------------------- |
| `verb`    | ✅ Yes    | Comma-separated list of verb IDs  |
| `mood`    | ❌ No     | Comma-separated list of mood IDs  |
| `tense`   | ❌ No     | Comma-separated list of tense IDs |

#### Example

```
/conjugations?verb=1,4,9&mood=1,2&tense=2,5
```

---

### Behavior

* At least one `verb` ID **must** be provided
* If `mood` is omitted → return all moods
* If `tense` is omitted → return all tenses
* If both are omitted → return all conjugations for the verb(s)

---

### Response Shape (IMPORTANT)

The response MUST be **nested and frontend-friendly**:

```json
{
  "data": [
    {
      "verb": {
        "id": 1,
        "infinitive": "hablar"
      },
      "moods": [
        {
          "id": 1,
          "name": "Indicative",
          "tenses": [
            {
              "id": 1,
              "name": "Present",
              "conjugations": [
                { "person": "yo", "value": "hablo" },
                { "person": "tú", "value": "hablas" },
                { "person": "él/ella", "value": "habla" },
                { "person": "nosotros", "value": "hablamos" },
                { "person": "vosotros", "value": "habláis" },
                { "person": "ellos", "value": "hablan" }
              ]
            }
          ]
        }
      ]
    }
  ],
  "error": null
}
```

---

### Rules for Response Construction

* Group data as:

  ```
  verb → moods → tenses → conjugations
  ```
* Do NOT return flat lists
* Do NOT duplicate parent data unnecessarily
* Always maintain consistent structure regardless of filters
* Always return persons in this order:

```
yo, tú, él/ella, nosotros, vosotros, ellos
```

---

## 2.2 Verbs Endpoint

**GET `/verbs`**

Returns all verbs with their IDs.

---

## 3. Error Handling

* Missing `verb` parameter → **400 Bad Request**
* Invalid IDs → **404 Not Found** or **422 Unprocessable Entity**

### Error Format

```json
{
  "data": null,
  "error": {
    "message": "Description of the error"
  }
}
```

---

## 4. Tech Stack

* FastAPI
* SQLAlchemy (ORM)
* SQLite (initial database)

---

## 5. Data Model

### 5.1 Verb

* `id` (int, PK)
* `infinitive` (string)

### 5.2 Mood

* `id` (int, PK)
* `name` (string)

### 5.3 Tense

* `id` (int, PK)
* `name` (string)
* `mood_id` (FK → Mood)

### 5.4 Conjugation

* `id` (int, PK)
* `verb_id` (FK → Verb)
* `tense_id` (FK → Tense)
* `mood_id` (FK → Mood)
* `person` (string) ✅ REQUIRED
* `value` (string)

> Naming must be consistent (e.g., `tense_id`, NOT `tenseNameId`)

---

## 6. Architecture Principles

Use a **layered architecture**:

### Layers

1. **API Layer (Routes)**

   * Handles HTTP requests/responses
   * No business logic

2. **Service Layer**

   * Contains business logic
   * Builds nested response structure
   * Coordinates repositories

3. **Repository Layer**

   * Handles database access
   * No business logic

4. **Models**

   * SQLAlchemy ORM models

5. **Schemas**

   * Pydantic models for validation and serialization

---

### Rules

* Do NOT mix concerns:

  * No DB logic in routes
  * No business logic in repositories
* Keep functions small and focused
* Prefer explicitness over magic

---

## 7. Project Structure

```
/app
  /api
    /routes
  /services
  /repositories
  /models
  /schemas
  /core        # config, utilities
  /db          # session, base
```

---

## 8. Coding Guidelines

* Use **type hints everywhere**
* Use **Pydantic models** for all request/response validation
* Prefer **async functions** where appropriate
* Use **dependency injection** for DB sessions
* Write clear, readable code over clever code

---

## 9. API Design Rules

* Follow RESTful conventions
* Always return structured responses:

```json
{
  "data": ...,
  "error": null
}
```

* Use appropriate HTTP status codes
* Keep endpoints consistent and predictable

---

## 10. Database Guidelines

* Use SQLAlchemy ORM
* Avoid raw SQL unless absolutely necessary
* Maintain proper foreign key relationships
* Ensure indexing on:

  * `verb_id`
  * `mood_id`
  * `tense_id`

---

## 11. Service Layer Expectations (CRITICAL)

The service layer MUST:

* Fetch raw data from repositories
* Transform flat database rows into nested structure
* Apply filtering logic (verbs, moods, tenses)
* Ensure consistent ordering of:

  * moods
  * tenses
  * persons

Avoid:

* Returning raw DB rows
* Doing transformation in routes

---

## 12. Testing Expectations

Use **pytest**

### Test Coverage

* Service layer logic
* Filtering behavior:

  * Multiple verbs
  * Optional mood/tense filters
  * Missing parameters
* Edge cases:

  * Invalid IDs
  * Empty results

---

## 13. Claude Code Instructions

Claude SHOULD:

* Follow layered architecture strictly
* Generate modular, testable code
* Keep implementations simple (MVP-first)
* Ask for clarification when needed
* Suggest improvements if architecture is violated

Claude SHOULD NOT:

* Combine layers
* Overengineer
* Introduce unnecessary abstractions

---

## 14. Style Guidelines

* Keep code simple and readable
* Prefer clarity over performance (unless specified)
* Avoid premature optimization

---

## 15. Future Enhancements (Not MVP)

* Add endpoints:

  * `/moods`
  * `/tenses`
* Add metadata to responses
* Add authentication
* Add user progress tracking

---

## 16. Guiding Principle

When making decisions, always ask:

> “Does this follow the layered architecture and MVP scope?”

If not → simplify.
