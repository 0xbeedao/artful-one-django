default: 
  uv run manage.py runserver

static: 
  uv run manage.py collectstatic

css: 
  bun run build-css-once

css-watch: 
  bun run build-css
