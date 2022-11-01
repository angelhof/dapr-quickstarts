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

And then send requests with the following:

```sh
# Frontend
curl -X POST -s http://localhost:5002/book -H Content-Type:application/json --data @reservation.json

# Backend
curl -X POST -s http://localhost:5001/book_hotel/10 -H Content-Type:application/json --data @user.json
```

Send load to the application using (after having installed wrk2 in the current directory):
```sh
./wrk2/wrk -t1 -c1 -d20 -R1 --latency http://localhost:5002/book -s workload.lua
```

## TODO Items

__TODO:__ Figure out how to clean the state store.

__TODO:__ Check out distributed locks (because they do not support transactional updates).