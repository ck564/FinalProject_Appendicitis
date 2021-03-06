
# General Parameters
ALPHA = 0.05
DISCOUNT_RATE = 0.03
DELTA_T = 1 / 4
POP_SIZE = 1000
SIM_LENGTH = 30


# Cost of Screening
COST_US = 342
COST_CT = 808


# Cost and utility of each state
COST_STATES_US = [
    0,         # Well
    15021.11,  # Appendicitis       Notes: Appendicitis is made into temporary state
    0,         # Post-Appendicitis
    49971.11,  # Cancer
    0          # Dead
]

COST_STATES_CT = [
    0,         # Well
    14570.14,  # Appendicitis
    0,         # Post-Appendicitis
    49971.11,  # Cancer
    0          # Dead
]

UTIL_STATES = [
    0.91,       # Well
    0.73,       # Appendicitis
    0,          # Post-Appendicitis
    0.83,       # Cancer
    0           # Dead
]

# Transition probability matrices
TRANS_MATRIX_US = [
    [0.41716,   0.5720,     0,       0.0024,     0.00844],   # Well
    [0,         0,          1,       0,          0],         # Appendicitis
    [0.9944,    0,          0,       0.0024,     0.0032],    # Post-Appendicitis
    [0.50,      0,          0,       0.4988,     0.0012],    # Cancer
    [0,         0,          0,       0,          1]          # Dead
]

TRANS_MATRIX_CT = [
    [0.41716,     0.5720,   0,    0.0024,       0.00844],
    [0,           0,        1,    0,            0],
    [0.99439755,  0,        0,    0.002402447,  0.0032],
    [0.50,        0,        0,    0.4988,       0.0012],
    [0,           0,        0,    0,            1]
]

# Notes: (1) We accounted for increased cancer incidence but how are we accounting for increased sensitivity (better detection)
#        (2) Need to adjust cost for appendicitis state to reflect lower rate of false positives
