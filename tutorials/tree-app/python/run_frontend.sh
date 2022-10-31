
PORT=5002
## If we don't use the --workers option, then it
## spawns workers equal to the $WEB_CONCURRENCY variable.
WORKERS=4

uvicorn frontend:app --port "${PORT}" --workers "${WORKERS}" --reload
