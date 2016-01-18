import unittest
import uuid

from simphony.cuds.material_relations.cohesion_force import (
    Cohesion_Force)
from simphony.testing.abc_check_material_relation import (
    CheckMaterialRelation)


class TestCohesion_ForceMaterialRelation(
    CheckMaterialRelation,
    unittest.TestCase
):
    def container_factory(
        self,
            name="Cohesion_Force",
            materials=[uuid.uuid4() for _ in xrange(1)]):
        return Cohesion_Force(
            name=name,
            materials=materials
        )

    def test_cohesion_energy_density(self):
        relation = self.container_factory('foo_relation')

        self.assertEqual(relation.cohesion_energy_density, 0.0)

    def test_cohesion_energy_density_update(self):
        relation = self.container_factory('foo_relation')

        original = relation.cohesion_energy_density
        relation.cohesion_energy_density = original + 1

        self.assertEqual(relation.cohesion_energy_density, original + 1)

if __name__ == '__main__':
    unittest.main()
