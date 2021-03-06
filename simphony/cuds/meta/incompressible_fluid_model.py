from simphony.core import Default  # noqa
from simphony.core.cuba import CUBA
from .compressibility_model import CompressibilityModel


class IncompressibleFluidModel(CompressibilityModel):
    """
    Incompressible fluid model
    """
    cuba_key = CUBA.INCOMPRESSIBLE_FLUID_MODEL

    def __init__(self, description=Default, name=Default):
        super(IncompressibleFluidModel, self).__init__(
            description=description, name=name)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(IncompressibleFluidModel,
                                cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set(() + base_params))

    def _default_models(self):
        return ['CUBA.CONTINUUM']  # noqa

    def _default_definition(self):
        return "Incompressible fluid model"  # noqa

    def _default_variables(self):
        return [
            'CUBA.VELOCITY', 'CUBA.POSITION', 'CUBA.DENSITY', 'CUBA.VISCOSITY'
        ]  # noqa
