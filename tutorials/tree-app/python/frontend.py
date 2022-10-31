#
# Copyright 2021 The Dapr Authors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from app import User

import logging
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

    return resp.data



# app.run(host="0.0.0.0",port=appPort)
