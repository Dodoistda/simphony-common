from simphony.core import Default  # noqa
from . import validation
from .thermostat import Thermostat
from simphony.core.cuba import CUBA


class TemperatureRescaling(Thermostat):
    """
    A simple temperature rescaling thermostat. The coupling time
    specifies how offen the temperature should be relaxed or
    coupled to the bath.
    """
    cuba_key = CUBA.TEMPERATURE_RESCALING

    def __init__(self,
                 coupling_time=Default,
                 temperature=Default,
                 material=Default,
                 description=Default,
                 name=Default):
        super(TemperatureRescaling, self).__init__(
            material=material, description=description, name=name)
        self._init_coupling_time(coupling_time)
        self._init_temperature(temperature)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(TemperatureRescaling,
                                cls).supported_parameters()
        except AttributeError:
            base_params = set()
        return set([
            CUBA.COUPLING_TIME,
            CUBA.TEMPERATURE,
        ]) | base_params

    def _default_models(self):
        return ['CUBA.ATOMISTIC', 'CUBA.MESOSCOPIC']  # noqa

    def _default_definition(self):
        return "A simple temperature rescaling thermostat. The coupling time specifies how offen the temperature should be relaxed or coupled to the bath."  # noqa

    def _init_coupling_time(self, value):
        if value is Default:
            value = self._default_coupling_time()

        self.coupling_time = value

    @property
    def coupling_time(self):
        return self.data[CUBA.COUPLING_TIME]

    @coupling_time.setter
    def coupling_time(self, value):
        value = self._validate_coupling_time(value)
        self.data[CUBA.COUPLING_TIME] = value

    def _validate_coupling_time(self, value):
        value = validation.cast_data_type(value, 'COUPLING_TIME')
        validation.check_valid_shape(value, [1], 'COUPLING_TIME')
        validation.validate_cuba_keyword(value, 'COUPLING_TIME')
        return value

    def _default_coupling_time(self):
        return 1e-06

    def _init_temperature(self, value):
        if value is Default:
            value = self._default_temperature()

        self.temperature = value

    @property
    def temperature(self):
        return self.data[CUBA.TEMPERATURE]

    @temperature.setter
    def temperature(self, value):
        value = self._validate_temperature(value)
        self.data[CUBA.TEMPERATURE] = value

    def _validate_temperature(self, value):
        value = validation.cast_data_type(value, 'TEMPERATURE')
        validation.check_valid_shape(value, [2], 'TEMPERATURE')
        validation.check_elements(value, [2], 'TEMPERATURE')

        return value

    def _default_temperature(self):
        return [0.0, 0.0]
