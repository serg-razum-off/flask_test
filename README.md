# Project Run
`uv run uvicorn fin_app.main:app --reload `
`uv run uvicorn fin_app.main:app --reload > server.log 2>&1 &`

## killing
`kill $(lsof -ti:8000)`
`fuser -k 8000/tcp`
`pkill -f uvicorn`
