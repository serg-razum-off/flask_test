# Project Run
`uv run uvicorn fin_app.main:app --reload `
`uv run uvicorn fin_app.main:app --reload > server.log 2>&1 &`

## killing
`pkill -f uvicorn`
`fuser -k 8000/tcp` if [Errno 98] Already in use
`kill $(lsof -ti:8000)` alternative
