# Contributing to Doomscrolling Blocker

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Set up your environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

4. Make your changes
5. Run linting: `ruff check .` and `black .`
6. Run tests: `pytest`
7. Commit with a clear message and open a Pull Request

## Code Style

- Formatter: **black**
- Linter: **ruff**
- Type hints encouraged throughout

## Webcam Testing

CI skips webcam tests. For local testing, ensure a webcam is connected and set `CAMERA_INDEX` appropriately.
