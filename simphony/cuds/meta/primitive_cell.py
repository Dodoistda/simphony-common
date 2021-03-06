from simphony.core import Default  # noqa
from .cuds_component import CUDSComponent
from simphony.core.cuba import CUBA
from simphony.cuds import meta_validation


class PrimitiveCell(CUDSComponent):
    """
    A lattice primitive cell
    """
    cuba_key = CUBA.PRIMITIVE_CELL

    def __init__(self,
                 lattice_vectors=Default,
                 description=Default,
                 name=Default):
        super(PrimitiveCell, self).__init__(description=description, name=name)
        self._init_lattice_vectors(lattice_vectors)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(PrimitiveCell, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set((CUBA.LATTICE_VECTORS, ) + base_params))

    def _default_definition(self):
        return "A lattice primitive cell"  # noqa

    def _init_lattice_vectors(self, value):
        if value is Default:
            value = self._default_lattice_vectors()

        self.lattice_vectors = value

    @property
    def lattice_vectors(self):
        return self.data[CUBA.LATTICE_VECTORS]

    @lattice_vectors.setter
    def lattice_vectors(self, value):
        value = self._validate_lattice_vectors(value)
        self.data[CUBA.LATTICE_VECTORS] = value

    def _validate_lattice_vectors(self, value):
        value = meta_validation.cast_data_type(value, 'LATTICE_VECTORS')
        meta_validation.check_valid_shape(value, [1], 'LATTICE_VECTORS')
        meta_validation.validate_cuba_keyword(value, 'LATTICE_VECTORS')
        return value

    def _default_lattice_vectors(self):
        return [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
