from datetime import datetime
from bson import ObjectId

def add_quality_log(dataset_id, data, collection):
    log = {
        "dataset_id": ObjectId(dataset_id),
        "status": data["status"],
        "details": data["details"],
        "timestamp": datetime.utcnow()
    }
    return collection.insert_one(log)

def get_quality_logs(dataset_id, collection):
    return list(collection.find({"dataset_id": ObjectId(dataset_id)}))
