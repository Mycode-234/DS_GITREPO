import json
import pymongo

def load_json(file_name):
    """Loads JSON data from a file."""
    with open(file_name) as file:
        return json.load(file)

def generate_city_country_mapping():
    """Create a map linking cities to their respective countries."""
    return {
        "newyork": "usa",
        "dallas": "usa",
        "beijing": "china",
        "colombo": "sri_lanka",
        "hongkong": "china",
        "kandy": "sri_lanka",
        "wuhan": "china",
        "chicago": "usa"
    }

def connect_to_mongo(db_name, collection_name):
    """Establish a MongoDB connection and access the desired collection."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client[db_name]
    return database[collection_name]

def calculate_total_expense(ticket_data, visa_costs, city_to_country):
    """Calculate the total cost for each ticket based on visa fees and ticket price."""
    last_city = ticket_data['visa_stamped_location'][-1]
    country = city_to_country.get(last_city)
    if country:
        visa_cost = visa_costs[country]
        return visa_cost + int(ticket_data['ticket_price'])
    return None

def show_passenger_details(ticket_data_list, visa_costs, city_to_country):
    """Display details of passengers including their total travel costs."""
    print('Passenger Details:')
    for ticket in ticket_data_list:
        total_cost = calculate_total_expense(ticket, visa_costs, city_to_country)
        if total_cost is not None:
            print(f"Passenger ID {ticket['ticket_id']}: Name: {ticket['passenger_name']}, Total Cost: {total_cost}")

def run():
    json_content = load_json("data.json")
    city_country_mapping = generate_city_country_mapping()
    tickets_collection = connect_to_mongo("Passenger_Management", "tickets")

    ticket_data = list(tickets_collection.find({}))
    show_passenger_details(ticket_data, json_content['visa_rates'], city_country_mapping)

if __name__ == "__main__":
    run()
