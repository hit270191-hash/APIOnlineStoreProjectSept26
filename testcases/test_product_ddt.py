import pytest
import requests
import json
import os
from datamodels.Product import Product
from routes.Routes import Routes
from utils.Data_Provider import read_json_data
from utils.Data_Provider import read_excel_data
from dataclasses import asdict

json_path= os.path.abspath(os.path.join(os.path.dirname(__file__), "../testdata/productdata.json"))
xl_path= os.path.abspath(os.path.join(os.path.dirname(__file__), "../testdata/products_data.xlsx"))

new_product_id = None

class TestProduct:

    @pytest.fixture(autouse=True)
    def init_class_var(self,setup):
        self.base_url = setup["base_url"]
        self.config= setup["config_reader"]

    @pytest.mark.parametrize("product_test_data",read_json_data(json_path))
    # @pytest.mark.parametrize("product_test_data", read_excel_data(xl_path, "products_data"))
    def test_create_delete_product(self,product_test_data):
        product_data=product_test_data[0]               #remove [0] while running with excel or CSV
        title= product_data["title"]
        description= product_data["description"]
        price= product_data["price"]
        category= product_data["category"]
        stock= product_data["stock"]
        payload= Product(title,description,price,category,stock)


        global new_product_id
        # print(type(self.payload.__dict__))
        res= requests.post(self.base_url+Routes.CREATE_PRODUCT, json=asdict(payload))
        assert res.status_code == 201, "Wrong status code"
        data= res.json()
        print(json.dumps(data, indent=4))
        new_product_id= data["id"]
        print("New record created...")

        res = requests.delete(self.base_url + Routes.DELETE_PRODUCT.format(id=new_product_id))
        assert res.status_code == 200, "Wrong status code"
        print("Record deleted...")


#HTML Report

#  pytest -v -s --html=reports/report.html .\testcases\test_product_ddt.py

#Allure Report
#pytest -s -v --alluredir=reports\allure-result .\testcases\test_product_ddt.py
#allure generate reports\allure-result -o reports\allure-html --clean
#allure open .\reports\allure-html
