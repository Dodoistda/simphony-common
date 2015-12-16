# code auto-generated by material_relations_generate.py
from simphony.material_relations.material_relation import (
    MaterialRelation)
from simphony.core.cuba import CUBA
from simphony.core.data_container import DataContainer


class Coulomb(MaterialRelation):

    """ A Coulomb material-relation

    Attributes
    ----------

    cutoff_distance : <type 'numpy.float64'>
        Cutoff Distance
    dielectric_constant : <type 'numpy.float64'>
        Dielectric Constant

    """

    def __init__(
        self,
        name="Coulomb",
        materials=None,
        cutoff_distance=1.0,
        dielectric_constant=1.0
    ):
        super(Coulomb, self).__init__(
            name=name,
            description="Coulomb material relation",  # noqa
            parameters=DataContainer({
                CUBA.CUTOFF_DISTANCE: cutoff_distance,
                CUBA.DIELECTRIC_CONSTANT: dielectric_constant,
            }),
            supported_parameters=[
                CUBA.CUTOFF_DISTANCE,
                CUBA.DIELECTRIC_CONSTANT,
            ],
            materials=materials,
            num_materials=[1, 2],
            kind=CUBA.COULOMB
        )

    @property
    def cutoff_distance(self):
        return self._parameters[CUBA.CUTOFF_DISTANCE]

    @cutoff_distance.setter
    def cutoff_distance(self, value):
        updated_parameters = self._parameters
        updated_parameters[CUBA.CUTOFF_DISTANCE] = value
        self._parameters = updated_parameters

    @property
    def dielectric_constant(self):
        return self._parameters[CUBA.DIELECTRIC_CONSTANT]

    @dielectric_constant.setter
    def dielectric_constant(self, value):
        updated_parameters = self._parameters
        updated_parameters[CUBA.DIELECTRIC_CONSTANT] = value
        self._parameters = updated_parameters
