default: 
  uv run manage.py runserver

static: 
  uv run manage.py collectstatic

test:
  uv run pytest
  