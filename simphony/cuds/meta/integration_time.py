import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .computational_method import ComputationalMethod
from . import validation


class IntegrationTime(ComputationalMethod):
    '''the current time, time step, and final time for a simulation stored on each cuds (a specific state).  # noqa
    '''

    cuba_key = CUBA.INTEGRATION_TIME

    def __init__(self,
                 description="",
                 name="",
                 current=0.0,
                 size=0.0,
                 final=0.0):

        self._data = DataContainer()

        self.final = final
        self.size = size
        self.current = current
        self.name = name
        self.description = description
        # This is a system-managed, read-only attribute
        self._definition = 'the current time, time step, and final time for a simulation stored on each cuds (a specific state).'  # noqa
        # This is a system-managed, read-only attribute
        self._physics_equation = []

    @property
    def final(self):
        return self.data[CUBA.FINAL]

    @final.setter
    def final(self, value):
        value = validation.cast_data_type(value, 'final')
        validation.validate_cuba_keyword(value, 'final')
        data = self.data
        data[CUBA.FINAL] = value
        self.data = data

    @property
    def size(self):
        return self.data[CUBA.SIZE]

    @size.setter
    def size(self, value):
        value = validation.cast_data_type(value, 'size')
        validation.validate_cuba_keyword(value, 'size')
        data = self.data
        data[CUBA.SIZE] = value
        self.data = data

    @property
    def current(self):
        return self.data[CUBA.CURRENT]

    @current.setter
    def current(self, value):
        value = validation.cast_data_type(value, 'current')
        validation.validate_cuba_keyword(value, 'current')
        data = self.data
        data[CUBA.CURRENT] = value
        self.data = data

    @property
    def definition(self):
        return self._definition

    @property
    def physics_equation(self):
        return self._physics_equation

    @property
    def data(self):
        return DataContainer(self._data)

    @data.setter
    def data(self, new_data):
        self._data = DataContainer(new_data)

    @property
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.CURRENT, CUBA.DESCRIPTION, CUBA.FINAL, CUBA.NAME,
                CUBA.PHYSICS_EQUATION, CUBA.SIZE, CUBA.UUID)

    @classmethod
    def parents(cls):
        return (CUBA.COMPUTATIONAL_METHOD, CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
