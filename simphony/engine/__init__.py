""" Simphony engine module

This module is dynamicaly populated at import with the
registered plugins modules. Plugins modules need to be
registered at the 'simphony.engine' entry point.
"""
from .extension import ABCEngineExtension
from .extension import EngineInterface
from .extension import EngineManager


__all__ = ['ABCEngineExtension', 'EngineInterface',
           'get_supported_engines', 'create_wrapper']


# TODO: Use an application server and put this in app context.
# Wrapper manager class.
_ENGINE_MANAGER = EngineManager()


def get_supported_engines():
    """Show a list of supported engines."""
    return _ENGINE_MANAGER.get_supported_engines()


def create_wrapper(cuds, engine_name, engine_interface=None):
    """Create a wrapper to the given engine.

    Parameters
    ----------
    cuds: CUDS
        A cuds object which contains model information.
    engine_name: str
        Name of the underlying engine to launch the simulation with.
    engine_interface: EngineInterface
        The interface to the engine, internal or fileio.
    """
    return _ENGINE_MANAGER.create_wrapper(cuds, engine_name, engine_interface)


def load_engine_extentions():
    """ Discover and load engine extension modules.

    """
    from stevedore import extension
    mgr = extension.ExtensionManager(
        namespace='simphony.engine',
        invoke_on_load=False)
    extensions = {}
    for ext in mgr.extensions:
        extensions[ext.name] = ext.plugin
        # Load engine metadata
        _ENGINE_MANAGER.load_metadata(ext.plugin)
    return extensions


# Populate the module namespace
globals().update(load_engine_extentions())

# cleanup
del load_engine_extentions
