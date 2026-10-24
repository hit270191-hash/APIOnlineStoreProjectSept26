import requests
import pytest
from routes.Routes import Routes
from payloads.Payload import Payload
import json
from dataclasses import asdict

class TestCart:
    @pytest.fixture(autouse=True)
    def init_class_var(self,setup):
        self.base_url = setup['base_url']
        # self.config= setup['config']
        self.payload = Payload().cart_payload()

    def test_get_cart(self):
        global cart_id
        res= requests.post(self.base_url+Routes.Create_Cart,json = asdict(self.payload))
        assert res.status_code == 201, "Wrong status code"
        data= res.json()
        print(json.dumps(data, indent=4))
        cart_id= data["id"]
        print(cart_id)
