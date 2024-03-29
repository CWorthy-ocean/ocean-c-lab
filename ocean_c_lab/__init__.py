from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    __version__ = '0.0.0'  # pragma: no cover

from .box_models import *
from .co2calc import *
from .glodap import open_glodap
