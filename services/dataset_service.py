from datetime import datetime
from bson import ObjectId
from pymongo.collection import Collection

def create_dataset(data, collection: Collection):
    data.update({
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "is_deleted": False
    })
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_datasets(collection: Collection, filters: dict):
    query = {"is_deleted": False}
    if "owner" in filters:
        query["owner"] = filters["owner"]
    if "tag" in filters:
        query["tags"] = filters["tag"]
    return list(collection.find(query))

def get_dataset_by_id(dataset_id, collection: Collection):
    return collection.find_one({"_id": ObjectId(dataset_id), "is_deleted": False})

def update_dataset(dataset_id, updates, collection: Collection):
    updates["updated_at"] = datetime.utcnow()
    result = collection.update_one(
        {"_id": ObjectId(dataset_id)},
        {"$set": updates}
    )
    return result.modified_count

def soft_delete_dataset(dataset_id, collection: Collection):
    return collection.update_one(
        {"_id": ObjectId(dataset_id)},
        {"$set": {"is_deleted": True, "updated_at": datetime.utcnow()}}
    )
