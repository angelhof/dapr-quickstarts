Run the multithreaded flask app using the following script:

```sh
dapr run --app-id multiplyapp --app-port 5001 --dapr-http-port 3501 bash flask-script.sh
```

And then send multiple requests with one of the following two:

```sh
dapr invoke --app-id multiplyapp --method multiply --data-file operands.json

curl -s http://localhost:5001/multiply -H Content-Type:application/json --data @operands.json
```
