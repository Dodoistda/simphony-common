import uuid
from simphony.core import data_container as dc
from simphony.core import cuba as cb
from .material_relation import MaterialRelation
from . import validation


class SjkrCohesionForce(MaterialRelation):

    '''Additional normal force tending to maintain the contact  # noqa
    '''

    cuba_key = cb.CUBA.SJKR_COHESION_FORCE

    def __init__(self, material, description=None, name=None, data=None, cohesion_energy_density=0.0):

        self.material = material
        self.description = description
        self.name = name
        if data:
            self.data = data
        self.cohesion_energy_density = cohesion_energy_density
        # This is a system-managed, read-only attribute
        self._models = [cb.CUBA.ATOMISTIC]
        # This is a system-managed, read-only attribute
        self._definition = 'Additional normal force tending to maintain the contact'  # noqa
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
    def cohesion_energy_density(self):
        return self.data[cb.CUBA.COHESION_ENERGY_DENSITY]

    @cohesion_energy_density.setter
    def cohesion_energy_density(self, value):
        value = validation.cast_data_type(value, 'cohesion_energy_density')
        validation.validate_cuba_keyword(value, 'cohesion_energy_density')
        self.data[cb.CUBA.COHESION_ENERGY_DENSITY] = value

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
        return (cb.CUBA.DESCRIPTION, cb.CUBA.COHESION_ENERGY_DENSITY, cb.CUBA.MATERIAL, cb.CUBA.UUID, cb.CUBA.NAME)

    @classmethod
    def parents(cls):
        return (cb.CUBA.MATERIAL_RELATION, cb.CUBA.MODEL_EQUATION, cb.CUBA.CUDS_COMPONENT, cb.CUBA.CUDS_ITEM)
