from simphony.core.cuba import CUBA
from .mesh_element import MeshElement


class Face(MeshElement):
    """
    ['Element for storing 2D geometrical objects']
    """

    cuba_key = CUBA.FACE

    def __init__(self, *args, **kwargs):
        super(Face, self).__init__(*args, **kwargs)

        self._init_definition()

    def supported_parameters(self):
        try:
            base_params = super(Face, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _init_definition(self):
        self._definition = "Element for storing 2D geometrical objects"  # noqa

    @property
    def definition(self):
        return self._definition
