from .computational_method import ComputationalMethod
from simphony.core.cuba import CUBA


class Fem(ComputationalMethod):
    """
    ['Finite element method']
    """

    cuba_key = CUBA.FEM

    def __init__(self, *args, **kwargs):
        super(Fem, self).__init__(*args, **kwargs)

        self._init_definition()
        self._init_physics_equations()

    def supported_parameters(self):
        try:
            base_params = super(Fem, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _init_definition(self):
        self._definition = "Finite element method"  # noqa

    @property
    def definition(self):
        return self._definition

    def _init_physics_equations(self):
        self._physics_equations = ['CUBA.CFD']  # noqa

    @property
    def physics_equations(self):
        return self._physics_equations
