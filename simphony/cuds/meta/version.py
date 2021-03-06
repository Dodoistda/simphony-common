from simphony.core import Default  # noqa
from simphony.cuds import meta_validation
from simphony.core.cuba import CUBA
from .cuds_item import CUDSItem


class Version(CUDSItem):
    """
    Version of a software tool used in a simulation
    """
    cuba_key = CUBA.VERSION

    def __init__(self, full, major, minor, patch):
        super(Version, self).__init__()
        self._init_minor(minor)
        self._init_major(major)
        self._init_full(full)
        self._init_patch(patch)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Version, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(
            set((
                CUBA.MINOR,
                CUBA.MAJOR,
                CUBA.FULL,
                CUBA.PATCH, ) + base_params))

    def _init_minor(self, value):
        if value is Default:
            value = self._default_minor()

        self.minor = value

    @property
    def minor(self):
        return self.data[CUBA.MINOR]

    @minor.setter
    def minor(self, value):
        value = self._validate_minor(value)
        self.data[CUBA.MINOR] = value

    def _validate_minor(self, value):
        value = meta_validation.cast_data_type(value, 'MINOR')
        meta_validation.check_valid_shape(value, [1], 'MINOR')
        meta_validation.validate_cuba_keyword(value, 'MINOR')
        return value

    def _default_minor(self):
        raise TypeError("No default for minor")

    def _default_definition(self):
        return "Version of a software tool used in a simulation"  # noqa

    def _init_major(self, value):
        if value is Default:
            value = self._default_major()

        self.major = value

    @property
    def major(self):
        return self.data[CUBA.MAJOR]

    @major.setter
    def major(self, value):
        value = self._validate_major(value)
        self.data[CUBA.MAJOR] = value

    def _validate_major(self, value):
        value = meta_validation.cast_data_type(value, 'MAJOR')
        meta_validation.check_valid_shape(value, [1], 'MAJOR')
        meta_validation.validate_cuba_keyword(value, 'MAJOR')
        return value

    def _default_major(self):
        raise TypeError("No default for major")

    def _init_full(self, value):
        if value is Default:
            value = self._default_full()

        self.full = value

    @property
    def full(self):
        return self.data[CUBA.FULL]

    @full.setter
    def full(self, value):
        value = self._validate_full(value)
        self.data[CUBA.FULL] = value

    def _validate_full(self, value):
        value = meta_validation.cast_data_type(value, 'FULL')
        meta_validation.check_valid_shape(value, [1], 'FULL')
        meta_validation.validate_cuba_keyword(value, 'FULL')
        return value

    def _default_full(self):
        raise TypeError("No default for full")

    def _init_patch(self, value):
        if value is Default:
            value = self._default_patch()

        self.patch = value

    @property
    def patch(self):
        return self.data[CUBA.PATCH]

    @patch.setter
    def patch(self, value):
        value = self._validate_patch(value)
        self.data[CUBA.PATCH] = value

    def _validate_patch(self, value):
        value = meta_validation.cast_data_type(value, 'PATCH')
        meta_validation.check_valid_shape(value, [1], 'PATCH')
        meta_validation.validate_cuba_keyword(value, 'PATCH')
        return value

    def _default_patch(self):
        raise TypeError("No default for patch")
