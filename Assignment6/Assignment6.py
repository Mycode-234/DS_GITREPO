import pymysql
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from bson import ObjectId

# MySQL connection setup
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': 'Tanaya'
}

# MongoDB connection details
mongo_connection_details = {
    'host': 'localhost',
    'port': 27017,
    'db_name': 'Tanaya_Mongo'
}

# Establish MySQL connection
mysql_connection = pymysql.connect(
    host=mysql_config['host'],
    user=mysql_config['user'],
    password=mysql_config['password'],
    db=mysql_config['db']
)

# Establish MongoDB connection
mongo_client = MongoClient(mongo_connection_details['host'], mongo_connection_details['port'])
mongo_db = mongo_client[mongo_connection_details['db_name']]

try:
    with mysql_connection.cursor(pymysql.cursors.DictCursor) as cursor:
        # Fetch categories from MySQL
        cursor.execute("SELECT * FROM category")
        category_data = cursor.fetchall()

        # Debug output for fetched categories
        print("Fetched Categories:", category_data)

        # Validate required fields in categories
        for category in category_data:
            if 'category_id' not in category or 'category_name' not in category:
                print(f"Invalid category data: {category}")

        # Fetch products from MySQL
        cursor.execute("SELECT * FROM product")
        product_data = cursor.fetchall()

        # Debug output for fetched products
        print("Fetched Products:", product_data)

        # Validate required fields in products
        for product in product_data:
            if 'product_id' not in product or 'product_name' not in product or 'category_id' not in product:
                print(f"Invalid product data: {product}")

        # Create mapping between categories and their products
        category_to_product_map = {}
        for product in product_data:
            cat_id = product['category_id']
            prod_info = {
                "product_id": product['product_id'],
                "product_name": product['product_name']
            }
            if cat_id not in category_to_product_map:
                category_to_product_map[cat_id] = []
            category_to_product_map[cat_id].append(prod_info)

        # Debug output for mapping
        print("Category to Product Map:", category_to_product_map)

        # Prepare documents for MongoDB insertion
        mongo_documents = []
        for category in category_data:
            cat_id = category['category_id']
            product_list = category_to_product_map.get(cat_id, [])
            document = {
                "_id": ObjectId(),  # MongoDB _id field
                "category_id": category['category_id'],
                "category_name": category['category_name'],
                "products": product_list
            }
            mongo_documents.append(document)

        # Clear existing data in MongoDB's category collection
        mongo_category_collection = mongo_db['category']
        mongo_category_collection.delete_many({})

        try:
            # Insert data into MongoDB
            mongo_category_collection.insert_many(mongo_documents, ordered=False)
        except BulkWriteError as bulk_error:
            print("Bulk Write Error:", bulk_error.details)

        # Display migrated data
        print("\n=== Migrated Categories and Products to MongoDB ===\n")
        for doc in mongo_documents:
            print(f"Category ID: {doc['category_id']} | Name: {doc['category_name']}")
            for prod in doc['products']:
                print(f"    Product ID: {prod['product_id']} | Name: {prod['product_name']}")

finally:
    # Close MySQL and MongoDB connections
    mysql_connection.close()
    mongo_client.close()

print("\nMigration from MySQL to MongoDB completed successfully.\n")
