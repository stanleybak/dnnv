from dnnv.properties import *
import numpy as np

N = Network("N")

Forall(x, Implies(False, N(x) > 0))
