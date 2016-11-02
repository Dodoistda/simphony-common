import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .condition import Condition


class Free(Condition):
    '''Free boundary condition  # noqa
    '''

    cuba_key = CUBA.FREE

    def __init__(self, data=None, description=None, name=None):

        self.name = name
        self.description = description
        if data:
            internal_data = self.data
            internal_data.update(data)
            self.data = internal_data

        # This is a system-managed, read-only attribute
        self._models = [
            CUBA.ELECTRONIC, CUBA.ATOMISTIC, CUBA.MESOSCOPIC, CUBA.CONTINUUM
        ]
        # This is a system-managed, read-only attribute
        self._definition = 'Free boundary condition'  # noqa

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
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.DESCRIPTION, CUBA.UUID, CUBA.NAME)

    @classmethod
    def parents(cls):
        return (CUBA.CONDITION, CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
