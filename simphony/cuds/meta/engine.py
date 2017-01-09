from simphony.core import Default  # noqa
from . import validation
from simphony.core.cuba import CUBA
from .software_tool import SoftwareTool


class Engine(SoftwareTool):
    """
    Represents a software tool which is used to solve the
    physics equation
    """
    cuba_key = CUBA.ENGINE

    def __init__(self, engine_feature, version=Default):

        super(Engine, self).__init__(version=version)
        self._init_engine_feature(engine_feature)

    def supported_parameters(self):
        try:
            base_params = super(Engine, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return (CUBA.ENGINE_FEATURE, ) + base_params

    def _default_definition(self):
        return "Represents a software tool which is used to solve the physics equation"  # noqa

    def _init_engine_feature(self, value):
        if value is Default:
            value = self._default_engine_feature()

        self.engine_feature = value

    @property
    def engine_feature(self):
        return self.data[CUBA.ENGINE_FEATURE]

    @engine_feature.setter
    def engine_feature(self, value):
        value = self._validate_engine_feature(value)
        self.data[CUBA.ENGINE_FEATURE] = value

    def _validate_engine_feature(self, value):
        value = validation.cast_data_type(value, 'ENGINE_FEATURE')
        validation.check_shape_at_least(value, [None])

        def flatten(container):
            for i in container:
                if isinstance(i, (list, tuple)):
                    for j in flatten(i):
                        yield j
                else:
                    yield i

        if hasattr(value, "flatten"):
            flat_array = value.flatten()
        else:
            flat_array = flatten(value)

        for entry in flat_array:
            validation.validate_cuba_keyword(entry, 'ENGINE_FEATURE')

        return value

    def _default_engine_feature(self):
        raise TypeError("No default for engine_feature")
