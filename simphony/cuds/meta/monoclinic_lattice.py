from .bravais_lattice import BravaisLattice
from simphony.core.cuba import CUBA


class MonoclinicLattice(BravaisLattice):
    """
    A monoclinic lattice
    """
    cuba_key = CUBA.MONOCLINIC_LATTICE

    def __init__(self,
                 primitive_cell,
                 origin,
                 lattice_parameter=Default,
                 size=Default,
                 description=Default,
                 name=Default):

        super(MonoclinicLattice, self).__init__(
            lattice_parameter=lattice_parameter,
            primitive_cell=primitive_cell,
            size=size,
            origin=origin,
            description=description,
            name=name)

    def supported_parameters(self):
        try:
            base_params = super(MonoclinicLattice, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _default_definition(self):
        return "A monoclinic lattice"  # noqa
