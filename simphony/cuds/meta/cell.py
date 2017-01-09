from simphony.core.cuba import CUBA
from .mesh_element import MeshElement


class Cell(MeshElement):
    """
    Element for storing 3D geometrical objects
    """
    cuba_key = CUBA.CELL

    def __init__(self, point):

        super(Cell, self).__init__(point=point)

    def supported_parameters(self):
        try:
            base_params = super(Cell, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _default_definition(self):
        return "Element for storing 3D geometrical objects"  # noqa
