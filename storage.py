import json

def load_quotations():
  with open("/content/drive/MyDrive/Quotation Tracker/quotations.json","r") as quotation_file:
    return json.load(quotation_file)
def save_quotations(quotations):
  with open("/content/drive/MyDrive/Quotation Tracker/quotations.json", "w") as quotation_file:
    json.dump(quotations, quotation_file, indent=4)