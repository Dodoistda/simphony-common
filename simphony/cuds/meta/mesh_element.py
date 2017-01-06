from .cuds_item import CUDSItem
from . import validation
from simphony.core import Default
from simphony.core.cuba import CUBA


class MeshElement(CUDSItem):
    """
    ['An element for storing geometrical objects']
    """

    cuba_key = CUBA.MESH_ELEMENT

    def __init__(self, point, *args, **kwargs):
        super(MeshElement, self).__init__(*args, **kwargs)

        self._init_definition()
        self._init_point(point)

    def supported_parameters(self):
        try:
            base_params = super(MeshElement, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return (CUBA.POINT, ) + base_params

    def _init_definition(self):
        self._definition = "An element for storing geometrical objects"  # noqa

    @property
    def definition(self):
        return self._definition

    def _init_point(self, value):
        if value is Default:
            raise TypeError("Value for point must be specified")

        self.point = value

    @property
    def point(self):
        return self.data[CUBA.POINT]

    @point.setter
    def point(self, value):
        value = self._validate_point(value)
        self.data[CUBA.POINT] = value

    def _validate_point(self, value):
        import itertools
        value = validation.cast_data_type(value, 'CUBA.POINT')
        validation.check_shape(value, [None])
        for tuple_ in itertools.product(*[range(x) for x in [None]]):
            entry = value
            for idx in tuple_:
                entry = entry[idx]
            validation.validate_cuba_keyword(entry, 'CUBA.POINT')

        return value
