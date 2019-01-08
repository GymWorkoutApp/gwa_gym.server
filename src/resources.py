from typing import Dict
from uuid import uuid4

from gwa_framework.resource.base import BaseResource
from gwa_framework.utils.decorators import validate_schema

from src.cache import cache
from src.database import master_async_session, read_replica_async_session
from src.models import GymModel
from src.schemas import GymInputSchema, GymOutputSchema


class GymResource(BaseResource):
    cache = cache
    method_decorators = {
        'create': [validate_schema(GymInputSchema)],
        'update': [validate_schema(GymInputSchema)],
    }

    def create(self, request_model: 'GymInputSchema') -> Dict:
        gym = GymModel()
        gym.id = request_model.gym_id or str(uuid4())
        gym.name = request_model.name
        gym.cnpj = request_model.cnpj
        gym.phone = request_model.phone
        gym.logo_id = request_model.logo_id
        with master_async_session() as session:
            session.add(gym)
            output = GymOutputSchema()
            output.gym_id = gym.id
            output.name = gym.name
            output.cnpj = gym.cnpj
            output.phone = gym.phone
            output.logo_id = gym.logo_id
            output.validate()
            return output.to_primitive()

    def update(self, request_model: 'GymInputSchema', gym_id=None):
        gym = GymModel()
        gym.id = gym_id
        gym.name = request_model.name
        gym.cnpj = request_model.cnpj
        gym.phone = request_model.phone
        gym.logo_id = request_model.logo_id
        with master_async_session() as session:
            session.merge(gym)
            output = GymOutputSchema()
            output.gym_id = gym.id
            output.name = gym.name
            output.cnpj = gym.cnpj
            output.phone = gym.phone
            output.logo_id = gym.logo_id
            output.validate()
            return output.to_primitive()

    def list(self, args=None, kwargs=None):
        with read_replica_async_session() as session:
            results = []
            for gym in session.query(GymModel).all():
                output = GymOutputSchema()
                output.gym_id = gym.id
                output.name = gym.name
                output.cnpj = gym.cnpj
                output.phone = gym.phone
                output.logo_id = gym.logo_id
                output.validate()
                results.append(output.to_primitive())
        return results

    def retrieve(self, gym_id):
        with read_replica_async_session() as session:
            gym = session.query(GymModel).filter_by(id=gym_id).first()
            output = GymOutputSchema()
            output.gym_id = gym.id
            output.name = gym.name
            output.cnpj = gym.cnpj
            output.phone = gym.phone
            output.logo_id = gym.logo_id
            output.validate()
            return output.to_primitive()

    def destroy(self, gym_id):
        with master_async_session() as session:
            session.query(GymModel).filter_by(id=gym_id).delete()
            return None


resources_v1 = [
    {'resource': GymResource, 'urls': ['/gyms/<gym_id>'], 'endpoint': 'Gyms GymId',
     'methods': ['GET', 'PUT', 'PATCH', 'DELETE']},
    {'resource': GymResource, 'urls': ['/gyms'], 'endpoint': 'Gyms',
     'methods': ['POST', 'GET']},
]
