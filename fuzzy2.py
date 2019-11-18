import math
import time
from random import randint

# angulo
derecha_enfrente = lambda g: 1 if (g['angle']>= 0 and g['angle'] < 25) else (-1/20) * g['angle'] + 9/4 if (g['angle'] >= 25 and g['angle'] < 45) else 0