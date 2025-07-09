from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from models.schema import DatasetCreate, DatasetUpdate, QualityLogCreate
from services import dataset_service, quality_log_service
from flasgger import swag_from
import os

bp = Blueprint('datasets', __name__)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client.dataset_catalog
datasets = db.datasets
logs = db.quality_logs

@bp.route('/datasets', methods=['POST'])
@swag_from('swagger.yaml')
def create_dataset():
    data = DatasetCreate(**request.json).dict()
    _id = dataset_service.create_dataset(data, datasets)
    return jsonify({"id": _id}), 201

@bp.route('/datasets', methods=['GET'])
def list_datasets():
    filters = request.args.to_dict()
    result = dataset_service.get_datasets(datasets, filters)
    for r in result:
        r["_id"] = str(r["_id"])
    return jsonify(result)

@bp.route('/datasets/<id>', methods=['GET'])
def get_dataset(id):
    data = dataset_service.get_dataset_by_id(id, datasets)
    if not data:
        return jsonify({"error": "Not found"}), 404
    data["_id"] = str(data["_id"])
    return jsonify(data)

@bp.route('/datasets/<id>', methods=['PUT'])
def update_dataset(id):
    data = DatasetUpdate(**request.json).dict(exclude_unset=True)
    updated = dataset_service.update_dataset(id, data, datasets)
    return (jsonify({"message": "Updated"}), 200) if updated else (jsonify({"error": "Not found"}), 404)

@bp.route('/datasets/<id>', methods=['DELETE'])
def delete_dataset(id):
    deleted = dataset_service.soft_delete_dataset(id, datasets)
    return (jsonify({"message": "Deleted"}), 200) if deleted.modified_count else (jsonify({"error": "Not found"}), 404)

@bp.route('/datasets/<id>/quality-1', methods=['POST'])
def add_quality_log(id):
    data = QualityLogCreate(**request.json).dict()
    result = quality_log_service.add_quality_log(id, data, logs)
    return jsonify({"log_id": str(result.inserted_id)}), 201

@bp.route('/datasets/<id>/quality-1', methods=['GET'])
def get_quality_logs(id):
    result = quality_log_service.get_quality_logs(id, logs)
    for r in result:
        r["_id"] = str(r["_id"])
        r["dataset_id"] = str(r["dataset_id"])
    return jsonify(result)
