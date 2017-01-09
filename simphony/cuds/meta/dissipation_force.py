from simphony.core import Default  # noqa
from . import validation
from simphony.core.cuba import CUBA
from .material_relation import MaterialRelation


class DissipationForce(MaterialRelation):
    """
    Viscous normal force describing the inelasticity of particle
    collisions
    """
    cuba_key = CUBA.DISSIPATION_FORCE

    def __init__(self,
                 material,
                 restitution_coefficient=Default,
                 description=Default,
                 name=Default):

        super(DissipationForce, self).__init__(
            material=material, description=description, name=name)
        self._init_restitution_coefficient(restitution_coefficient)

    def supported_parameters(self):
        try:
            base_params = super(DissipationForce, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return (CUBA.RESTITUTION_COEFFICIENT, ) + base_params

    def _default_models(self):
        return ['CUBA.ATOMISTIC']  # noqa

    def _default_definition(self):
        return "Viscous normal force describing the inelasticity of particle collisions"  # noqa

    def _init_restitution_coefficient(self, value):
        if value is Default:
            value = self._default_restitution_coefficient()

        self.restitution_coefficient = value

    @property
    def restitution_coefficient(self):
        return self.data[CUBA.RESTITUTION_COEFFICIENT]

    @restitution_coefficient.setter
    def restitution_coefficient(self, value):
        value = self._validate_restitution_coefficient(value)
        self.data[CUBA.RESTITUTION_COEFFICIENT] = value

    def _validate_restitution_coefficient(self, value):
        value = validation.cast_data_type(value, 'RESTITUTION_COEFFICIENT')
        validation.check_shape_at_least(value, [1])
        validation.validate_cuba_keyword(value, 'RESTITUTION_COEFFICIENT')
        return value

    def _default_restitution_coefficient(self):
        return 1.0
