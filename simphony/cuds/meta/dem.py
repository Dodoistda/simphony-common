from simphony.core import Default  # noqa
from .computational_method import ComputationalMethod
from simphony.core.cuba import CUBA


class Dem(ComputationalMethod):
    """
    Discrete element method
    """
    cuba_key = CUBA.DEM

    def __init__(self, description=Default, name=Default):
        super(Dem, self).__init__(description=description, name=name)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Dem, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set(() + base_params))

    def _default_definition(self):
        return "Discrete element method"  # noqa

    def _default_physics_equations(self):
        return ['CUBA.GRANULAR_DYNAMICS']  # noqa
