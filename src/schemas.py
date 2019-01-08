from gwa_framework.schemas.base import BaseSchema
from schematics.types import StringType


class GymInputSchema(BaseSchema):
    gym_id = StringType(required=False, serialized_name='gymId')
    logo_id = StringType(required=False, serialized_name='logoId')
    name = StringType(required=True, serialized_name='name', max_length=100, min_length=0)
    cnpj = StringType(required=True, serialized_name='cnpj', max_length=20, min_length=0)
    phone = StringType(required=True, serialized_name='cnpj', max_length=20, min_length=0)


class GymOutputSchema(BaseSchema):
    gym_id = StringType(required=False, serialized_name='gymId')
    logo_id = StringType(required=False, serialized_name='logoId')
    name = StringType(required=True, serialized_name='name', max_length=100, min_length=0)
    cnpj = StringType(required=True, serialized_name='cnpj', max_length=20, min_length=0)
    phone = StringType(required=True, serialized_name='cnpj', max_length=20, min_length=0)
