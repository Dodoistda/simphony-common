# code auto-generated by material_relations_generate.py
from simphony.cuds.material_relations.material_relation import (
    MaterialRelation)
from simphony.core.cuba import CUBA
from simphony.core.cuds_material_relation import CUDSMaterialRelation
from simphony.core.data_container import DataContainer


class Cohesion_Force(MaterialRelation):

    """ A Cohesion_Force material-relation

    Viscous normal force describing the inelasticity of particle collisions.

    Attributes
    ----------
    cohesion_energy_density : <type 'numpy.float64'>
        Work of adhesion per unit contact area

    """  # noqa

    def __init__(
        self,
        name,
        materials,
        description="",
        cohesion_energy_density=0.0
    ):
        super(Cohesion_Force, self).__init__(
            name=name,
            description=description,
            kind=CUDSMaterialRelation.COHESION_FORCE,
            materials=materials,
            parameters=DataContainer({
                CUBA.COHESION_ENERGY_DENSITY: cohesion_energy_density,
            })
        )

    @property
    def cohesion_energy_density(self):
        return self._parameters[CUBA.COHESION_ENERGY_DENSITY]

    @cohesion_energy_density.setter
    def cohesion_energy_density(self, value):
        self._parameters[CUBA.COHESION_ENERGY_DENSITY] = value
