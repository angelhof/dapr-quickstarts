
from app import User

import json
import logging
import psutil
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from dapr.clients import DaprClient

class Reservation(BaseModel):
    user_name: str
    user_id: str
    hotel_id: str


#code
DAPR_STORE_NAME = "statestore"
logging.basicConfig(level = logging.INFO)


@app.post("/book")
def book(reservation: Reservation):
    ## TODO: Can we not restart the client on every request?
    with DaprClient() as client:
        #Using Dapr SDK to save and get state
        user = User(name=reservation.user_name, id=reservation.user_id)
        resp = client.invoke_method(app_id="backend",
                                    method_name=f"/book_hotel/{reservation.hotel_id}",
                                    data=user.json(),
                                    http_verb="POST",
                                    content_type="application/json")
            # data: Union[bytes, str, GrpcMessage] = '',
            # content_type: Optional[str] = None,
        ## TODO: This load here is unnecessary (since we will
        ##       need to reserialize it here). Can we just return the string?
        ##       
        ##       FastAPI has type for request (and does auto encode/decode)
        ##       but not for response!
        json_resp = json.loads(resp.data)
        logging.info('Data returned: ' + str(resp.data))

        # proc = psutil.Process()
        # logging.info(proc.open_files())
        # for proc in psutil.process_iter():
            # print(proc.open_files())
    return json_resp



# app.run(host="0.0.0.0",port=appPort)
