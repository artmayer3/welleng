import logging
logger = logging.getLogger(__name__)

VEDO = False
VTK = False 
PLOTLY = False
TRIMESH = False

logger.info("Visualization disabled - vedo/vtk/plotly not imported")

def plot(*args, **kwargs):
    logger.warning("Visualization disabled - plot() not available")
    return None

def get_lines(*args, **kwargs):
    logger.warning("Visualization disabled - get_lines() not available") 
    return None

def figure(*args, **kwargs):
    logger.warning("Visualization disabled - figure() not available")
    return None

class Plotter:
    def __init__(self, *args, **kwargs):
        logger.warning("Visualization disabled - Plotter not available")
        pass

    def show(self, *args, **kwargs):
        logger.warning("Visualization disabled - show() not available")
        return None