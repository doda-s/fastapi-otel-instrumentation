from utils.utils import process_order

def order(search_radius, type: str):
    if type == "car":
        process_order(search_radius, type)
    if type == "bike":
        process_order(search_radius, type)
    if type == "scooter":
        process_order(search_radius, type)