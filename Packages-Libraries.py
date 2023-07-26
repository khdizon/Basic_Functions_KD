### Python Libraries ###

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |23 July 2023| Ken Dizon | Initial version |

# base 
import pandas as pd #dataframes
import numpy as np #math library 
import scipy #computation

# base visualization
import matplotlib.pyplot as plt 
%matplotlib inline
import plotly.express as px


# warnings off
import warnings
warnings.filterwarnings("ignore")
# or
# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


#ipy
import ipyleaflet as ipl
import ipywidgets as ipw
from ipyleaflet import (basemaps, Map, Marker, CircleMarker, MarkerCluster,
                        Icon, SearchControl, FullScreenControl, LayerGroup)
import ipywidgets as ipw
from ipywidgets import (Text, HTML)
