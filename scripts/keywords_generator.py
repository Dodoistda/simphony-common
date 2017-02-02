from simphony_metaparser.utils import traverse, without_cuba_prefix

from . import utils


class KeywordsGenerator(object):
    """Generator for the keywords.py file."""
    def generate(self, ontology, output):
        """ Create a dictionary of keywords from the cuba and simphony_metadata
        yaml-extracted dictionaries. Writes the generated code in the file
        object output.
        """
        lines = [
            '# code auto-generated by the\n',
            '# simphony-metadata/scripts/generate.py script.\n',
            'from collections import namedtuple\n',
            '\n',
            'import numpy\n',
            'import uuid  # noqa\n',
            '\n',
            '\n',
            'ATTRIBUTES = [\n'
            '    "name", "definition", "key", "shape", "length", "dtype"]\n'  # noqa
            'Keyword = namedtuple("Keyword", ATTRIBUTES)\n',
            '\n',
            '\n',
            'KEYWORDS = {\n']
        data_types = {
            'uuid': 'uuid.UUID',
            'string': 'numpy.str',
            'double': 'numpy.float64',
            'integer': 'numpy.int32',
            'boolean': 'bool'}
        template = (
            "    '{key}': Keyword(\n"
            "        name='{name}',\n"
            "        definition='{definition}',  # noqa\n"
            "        key='{key}',\n"
            "        shape={shape},\n"
            "        length={length},\n"
            "        dtype={type}),\n")
        for data_type in sorted(ontology.data_types,
                                key=lambda x: x.name):
            template_ctx = dict(
                type=data_types[data_type.type],
                name=utils.cuba_key_to_meta_class_name(
                    data_type.name),
                definition="",
                key=without_cuba_prefix(data_type.name),
                shape=data_type.shape,
                length=data_type.length,
            )
            lines.extend(template.format(**template_ctx))

        for cuds_item in sorted(
                [d for d, _ in traverse(ontology.root_cuds_item)],
                key=lambda x: x.name):
            template_ctx = dict(
                type="None",
                name=utils.cuba_key_to_meta_class_name(cuds_item.name),
                definition="",
                key=without_cuba_prefix(cuds_item.name),
                shape=[1],
                length="None")
            lines.extend(template.format(**template_ctx))
        lines.append('}\n')

        output.writelines(lines)
