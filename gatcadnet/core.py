# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['path', 'device']

# %% ../nbs/00_core.ipynb 4
import torch
from torch import tensor
import torch_geometric
from pathlib import Path
from svgpathtools import svg2paths
import cmath
from svgpathtools import Line,Arc
from svgpathtools import Path as svg_path
from svgpathtools import wsvg
from svgpathtools import disvg
import matplotlib.pyplot as plt
from math import pi
from math import tan, atan, sin ,degrees, radians
from os import walk
from torch_geometric.data import Dataset, Data
import os
from tqdm import tqdm
import networkx as nx
from torch_geometric.utils import to_networkx
from torch_geometric.utils import *
import matplotlib.pyplot as plt
from torch_geometric.loader import DataLoader
import torch.nn.functional as F
from torch.nn import Linear, Dropout
from einops import rearrange, reduce
import timeit

# %% ../nbs/00_core.ipynb 6
path = Path()
device ='cuda:0'
