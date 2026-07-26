import json
file_path = "data\products.json"



def get_all_products():
    with open(file_path , 'r') as p:
        return json.load(p)
    