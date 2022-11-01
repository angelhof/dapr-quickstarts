
PORT=5002
## If we don't use the --workers option, then it
## spawns workers equal to the $WEB_CONCURRENCY variable.
WORKERS=4
## We need to tweak this number to avoid any limits being hit
CONCURRENT_REQUESTS=100

## --reload is only used when debugging
uvicorn frontend:app --port "${PORT}" --workers "${WORKERS}" --limit-concurrency "${CONCURRENT_REQUESTS}"

