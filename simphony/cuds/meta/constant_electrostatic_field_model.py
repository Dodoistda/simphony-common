import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .electrostatic_model import ElectrostaticModel
from . import validation


class ConstantElectrostaticFieldModel(ElectrostaticModel):
    '''A constant electrostatic field model  # noqa
    '''

    cuba_key = CUBA.CONSTANT_ELECTROSTATIC_FIELD_MODEL

    def __init__(self,
                 data=None,
                 description=None,
                 name=None,
                 electrostatic_field=None):

        if electrostatic_field is None:
            self.electrostatic_field = [0.0, 0.0, 0.0]
        self.name = name
        self.description = description
        if data:
            internal_data = self.data
            internal_data.update(data)
            self.data = internal_data

        # This is a system-managed, read-only attribute
        self._models = [CUBA.MESOSCOPIC, CUBA.CONTINUUM]
        # This is a system-managed, read-only attribute
        self._definition = 'A constant electrostatic field model'  # noqa
        # This is a system-managed, read-only attribute
        self._variables = [CUBA.ELECTRIC_FIELD, CUBA.CHARGE]

    @property
    def electrostatic_field(self):
        return self.data[CUBA.ELECTROSTATIC_FIELD]

    @electrostatic_field.setter
    def electrostatic_field(self, value):
        value = validation.cast_data_type(value, 'electrostatic_field')
        validation.validate_cuba_keyword(value, 'electrostatic_field')
        data = self.data
        data[CUBA.ELECTROSTATIC_FIELD] = value
        self.data = data

    @property
    def data(self):
        try:
            data_container = self._data
        except AttributeError:
            self._data = DataContainer()
            data_container = self._data

        return DataContainer(data_container)

    @data.setter
    def data(self, new_data):
        self._data = DataContainer(new_data)

    @property
    def models(self):
        return self._models

    @property
    def definition(self):
        return self._definition

    @property
    def variables(self):
        return self._variables

    @property
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.DESCRIPTION, CUBA.UUID, CUBA.ELECTROSTATIC_FIELD,
                CUBA.NAME)

    @classmethod
    def parents(cls):
        return (CUBA.ELECTROSTATIC_MODEL, CUBA.PHYSICS_EQUATION,
                CUBA.MODEL_EQUATION, CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
