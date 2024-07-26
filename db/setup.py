import csv
from pymongo import MongoClient

# Function to connect to MongoDB and return the database object
def get_db():
    conn = "mongodb://localhost:27017/"
    client = MongoClient(conn)
    db = client['dev']
    return db

# Read CSV file and store words in MongoDB
def main():
    with open('words.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Validate required fields
            
            print("Entry:", row)
            if not all(row[field] for field in ['word', 'def']):
                print("Invalid entry, skipping:", row)
                continue

            word_data = {
                'word': row['word'],
                'def': row['def']
            }

            # Create a new Word document
            word_document = word_data

            # Connect to MongoDB and insert the document into the collection
            db = get_db()
            db.Word.insert_one(word_document)
    print("DB setup completed successfully")

if __name__ == "__main__":
    main()
