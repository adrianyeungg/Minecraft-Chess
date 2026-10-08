#
# Code by Alexander Pruss and under the MIT license
#
import collections
import collections.abc
# patch for 3.10+
collections.Iterable = collections.abc.Iterable
collections.Callable = collections.abc.Callable
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence

from mcpi.minecraft import Minecraft
from mcpi.entity import *
import mcpi.block as block
from mcpi.settings import *
from math import *
from mcpi.vec3 import *

Block = block.Block
