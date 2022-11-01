To install fastAPI we need both fastAPI and uvicorn:
```sh
python3 -m pip install fastapi "uvicorn[standard]"
```

Run the two services by running the following two commands (in different windows)

```sh
## Backend
dapr run --app-id backend --app-port 5001 --dapr-http-port 3501 bash run_server.sh

## Frontend
dapr run --app-id frontend --app-port 5002 --dapr-http-port 3502 bash run_frontend.sh
```

And then send requests with the followins:

```sh
# Frontend
curl -X POST -s http://localhost:5002/book -H Content-Type:application/json --data @reservation.json

# Backend
curl -X POST -s http://localhost:5001/book_hotel/10 -H Content-Type:application/json --data @user.json
```