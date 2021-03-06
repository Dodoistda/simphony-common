from simphony.core import Default  # noqa
from .condition import Condition
from simphony.core.cuba import CUBA
from simphony.cuds import meta_validation


class Neumann(Condition):
    """
    Neumann boundary condition, it specifies the values that the
    derivative of a solution is to take on the boundary of the
    domain.
    """
    cuba_key = CUBA.NEUMANN

    def __init__(self,
                 material=Default,
                 variable=Default,
                 description=Default,
                 name=Default):
        super(Neumann, self).__init__(description=description, name=name)
        self._init_models()
        self._init_variable(variable)
        self._init_material(material)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Neumann, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set((
            CUBA.VARIABLE,
            CUBA.MATERIAL, ) + base_params))

    def _init_models(self):
        self._models = self._default_models()  # noqa

    @property
    def models(self):
        return self._models

    def _default_models(self):
        return ['CUBA.CONTINUUM']  # noqa

    def _default_definition(self):
        return "Neumann boundary condition, it specifies the values that the derivative of a solution is to take on the boundary of the domain."  # noqa

    def _init_variable(self, value):
        if value is Default:
            value = self._default_variable()

        self.variable = value

    @property
    def variable(self):
        return self.data[CUBA.VARIABLE]

    @variable.setter
    def variable(self, value):
        value = self._validate_variable(value)
        self.data[CUBA.VARIABLE] = value

    def _validate_variable(self, value):
        value = meta_validation.cast_data_type(value, 'VARIABLE')
        meta_validation.check_valid_shape(value, [None], 'VARIABLE')
        meta_validation.check_elements(value, [None], 'VARIABLE')

        return value

    def _default_variable(self):
        return []

    def _init_material(self, value):
        if value is Default:
            value = self._default_material()

        self.material = value

    @property
    def material(self):
        return self.data[CUBA.MATERIAL]

    @material.setter
    def material(self, value):
        value = self._validate_material(value)
        self.data[CUBA.MATERIAL] = value

    def _validate_material(self, value):
        value = meta_validation.cast_data_type(value, 'MATERIAL')
        meta_validation.check_valid_shape(value, [None], 'MATERIAL')
        meta_validation.check_elements(value, [None], 'MATERIAL')

        return value

    def _default_material(self):
        return []
