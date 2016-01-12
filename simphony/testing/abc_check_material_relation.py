import abc

from simphony.testing.utils import create_data_container
from simphony.core.data_container import DataContainer
from simphony.core.material_relation_definitions import (
    MATERIAL_RELATION_DEFINITIONS)


class CheckMaterialRelation(object):

    __metaclass__ = abc.ABCMeta

    def setUp(self):
        pass

    @abc.abstractmethod
    def container_factory(self, name):
        """ Create and return a material relations with the default parameters

        """

    def test_material_relation_name_update(self):
        """ Test that name is set correctly and updated correctly

        """

        relation = self.container_factory('foo_relation')
        self.assertEqual(relation.name, 'foo_relation')

        relation.name = 'foo_relation_2'
        self.assertEqual(relation.name, 'foo_relation_2')

    def test_material_relation_invalid_name_update(self):
        """ Test that name is updated correctly

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(TypeError):
            relation.name = 42

    def test_material_relation_description_update(self):
        """ Test that description is updated correctly

        """

        relation = self.container_factory()
        extended_desc = relation.description + '_extended'
        relation.description = extended_desc

        self.assertEqual(relation.description, extended_desc)

    def test_material_relation_invalid_description_update(self):
        """ Test that description is updated correctly

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(TypeError):
            relation.name = 42

    def test_material_relation_parameters(self):
        """ Test that material relation parameters are set correctly

        """
        # when
        relation = self.container_factory('foo_relation')

        default_data_container = DataContainer()
        info = MATERIAL_RELATION_DEFINITIONS[relation.kind]
        for parameter in info.supported_parameters:
            default_data_container[parameter.cuba_key] = \
                parameter.default_value

        # then
        self.assertEqual(relation.parameters, default_data_container)

    def test_material_relation_parameters_update(self):
        """ Test that material relation parameters are updated correctly

        """

        # given
        relation = self.container_factory('foo_relation')

        parameters = create_data_container(
            restrict=relation.supported_parameters)

        # when
        relation.parameters = parameters

        # then
        self.assertEqual(relation.parameters, parameters)
        self.assertIsNot(relation.parameters, parameters)

    def test_material_relation_supported_parameters(self):
        pass

    def test_material_relation_supported_parameters_update(self):
        relation = self.container_factory('foo_relation')

        with self.assertRaises(AttributeError):
            relation.kind = "invalid attribute"

    def test_material_relation_materials_update(self):
        pass

    def test_material_relation_kind_update(self):
        relation = self.container_factory('foo_relation')

        with self.assertRaises(AttributeError):
            relation.kind = "invalid attribute"
