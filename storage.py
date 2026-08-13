import json

FILEPATH = "quotations.json"

def load_quotations():
    with open(FILEPATH, "r") as quotation_file:
        return json.load(quotation_file)

def save_quotations(quotations):
    with open(FILEPATH, "w") as quotation_file:
        json.dump(quotations, quotation_file, indent=4)
