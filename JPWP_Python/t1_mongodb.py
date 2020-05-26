import json

import pymongo

# Zmień frazy w nawiasach trójkątnych na podane przez autorów ćwiczeń <database>-<username>-<password>
# db18-user18-aBxbUHL9U3aqUIaK
client = pymongo.MongoClient("mongodb+srv://user18:aBxbUHL9U3aqUIaK@mrpass-ssbep.mongodb.net/db18?retryWrites=true&w=majority")
db = client.db18


def get_collection():
    c1 = db.coll1
    c2 = db.coll2
    response = {
        "coll1": list(c1.find()),
        "coll2": list(c2.find())
    }
    print(response)


def add_record():
    with open('doc.json', 'r') as f:
        data = json.load(f)

    c = db.coll1
    idd = c.insert_one(data).inserted_id
    print(idd)


def remove_document_by_criteria():
    c2 = db.coll2
    q = {
        'published': {
            '$lt': '2017-01-01'
        }}
    response = c2.delete_many(q)
    print(response.deleted_count)


def get_author(obj):
    return obj['author']


def list_collection():
    c2 = db.coll2
    data = c2.find()
    print(sorted(data, key=get_author))


def main():
    get_collection()
    add_record()
    remove_document_by_criteria()
    list_collection()


if __name__ == "__main__":
    main()
