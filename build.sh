#!/bin/bash

echo "🚀 Building Monorepo Services..."

# Linting
poetry run black services/
poetry run isort services/
poetry run flake8 services/

# Tests
poetry run pytest services/name-extractor/tests/
poetry run pytest services/data-processor/tests/

echo "✅ Build Complete!"
