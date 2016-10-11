import uuid
from simphony.core import data_container as dc
from simphony.core import cuba as cb
from .rheology_model import RheologyModel
from . import validation


class PowerLawViscosityModel(RheologyModel):

    '''Power law model for a variable viscosity function that is limited by minimum and maximum values  # noqa
    '''

    cuba_key = cb.CUBA.POWER_LAW_VISCOSITY_MODEL

    def __init__(self, description=None, name=None, data=None, linear_constant=1e-5, minimum_viscosity=1e-5, maximum_viscosity=1e-3, power_law_index=1.0):

        self.description = description
        self.name = name
        if data:
            self.data = data
        self.linear_constant = linear_constant
        self.minimum_viscosity = minimum_viscosity
        self.maximum_viscosity = maximum_viscosity
        self.power_law_index = power_law_index
        # This is a system-managed, read-only attribute
        self._models = [cb.CUBA.CONTINUUM]
        # This is a system-managed, read-only attribute
        self._definition = 'Power law model for a variable viscosity function that is limited by minimum and maximum values'  # noqa
        # This is a system-managed, read-only attribute
        self._variables = []

    @property
    def data(self):
        try:
            data_container = self._data
        except AttributeError:
            self._data = dc.DataContainer()
            return self._data
        else:
            # One more check in case the
            # property setter is by-passed
            if not isinstance(data_container, dc.DataContainer):
                raise TypeError("data is not a DataContainer. "
                                "data.setter is by-passed.")
            return data_container

    @data.setter
    def data(self, new_data):
        if isinstance(new_data, dc.DataContainer):
            self._data = new_data
        else:
            self._data = dc.DataContainer(new_data)

    @property
    def linear_constant(self):
        return self.data[cb.CUBA.LINEAR_CONSTANT]

    @linear_constant.setter
    def linear_constant(self, value):
        value = validation.cast_data_type(value, 'linear_constant')
        validation.validate_cuba_keyword(value, 'linear_constant')
        self.data[cb.CUBA.LINEAR_CONSTANT] = value

    @property
    def minimum_viscosity(self):
        return self.data[cb.CUBA.MINIMUM_VISCOSITY]

    @minimum_viscosity.setter
    def minimum_viscosity(self, value):
        value = validation.cast_data_type(value, 'minimum_viscosity')
        validation.validate_cuba_keyword(value, 'minimum_viscosity')
        self.data[cb.CUBA.MINIMUM_VISCOSITY] = value

    @property
    def maximum_viscosity(self):
        return self.data[cb.CUBA.MAXIMUM_VISCOSITY]

    @maximum_viscosity.setter
    def maximum_viscosity(self, value):
        value = validation.cast_data_type(value, 'maximum_viscosity')
        validation.validate_cuba_keyword(value, 'maximum_viscosity')
        self.data[cb.CUBA.MAXIMUM_VISCOSITY] = value

    @property
    def power_law_index(self):
        return self.data[cb.CUBA.POWER_LAW_INDEX]

    @power_law_index.setter
    def power_law_index(self, value):
        value = validation.cast_data_type(value, 'power_law_index')
        validation.validate_cuba_keyword(value, 'power_law_index')
        self.data[cb.CUBA.POWER_LAW_INDEX] = value

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
        return (cb.CUBA.DESCRIPTION, cb.CUBA.MINIMUM_VISCOSITY, cb.CUBA.LINEAR_CONSTANT, cb.CUBA.UUID, cb.CUBA.POWER_LAW_INDEX, cb.CUBA.MAXIMUM_VISCOSITY, cb.CUBA.NAME)

    @classmethod
    def parents(cls):
        return (cb.CUBA.RHEOLOGY_MODEL, cb.CUBA.PHYSICS_EQUATION, cb.CUBA.MODEL_EQUATION, cb.CUBA.CUDS_COMPONENT, cb.CUBA.CUDS_ITEM)
