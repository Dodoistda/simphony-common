from simphony.core import Default  # noqa
from .cuds_component import CUDSComponent
from simphony.core.cuba import CUBA
from simphony.cuds import meta_validation


class Node(CUDSComponent):
    """
    A node on a structured grid like lattice
    """
    cuba_key = CUBA.NODE

    def __init__(self, index, description=Default, name=Default):
        super(Node, self).__init__(description=description, name=name)
        self._init_index(index)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Node, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set((CUBA.INDEX, ) + base_params))

    def _default_definition(self):
        return "A node on a structured grid like lattice"  # noqa

    def _init_index(self, value):
        if value is Default:
            value = self._default_index()

        self.index = value

    @property
    def index(self):
        return self.data[CUBA.INDEX]

    @index.setter
    def index(self, value):
        value = self._validate_index(value)
        self.data[CUBA.INDEX] = value

    def _validate_index(self, value):
        value = meta_validation.cast_data_type(value, 'INDEX')
        meta_validation.check_valid_shape(value, [1], 'INDEX')
        meta_validation.validate_cuba_keyword(value, 'INDEX')
        return value

    def _default_index(self):
        raise TypeError("No default for index")
