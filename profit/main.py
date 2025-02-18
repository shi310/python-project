
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from logic import odds

p_list = [
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
]
odds.probability(p_list, 49)
