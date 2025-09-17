import numpy as np

dice = np.random.randint(1, 7, size=10)
print("Dice rolls:", dice)
# Dice rolls: [4 3 3 5 1 3 4 3 3 3]

rand_floats = np.random.rand(5)
print("Random floats:", rand_floats)
# Random floats: [0.42416641 0.08373173 0.39528311 0.12747657 0.04950654]

norm_samples = np.random.randn(5)
print("Standard Deviation:", norm_samples)
# Standard Deviation: [ 0.9701766  -1.84866214  0.59856822 -0.26656435  0.21496875]

rolls = np.random.randint(1, 7, size = 20)
print(rolls)
max_roll = max(rolls)
min_roll = min(rolls)
print(max_roll)
print(min_roll)
# [4 2 3 2 2 5 6 3 1 3 2 1 3 4 3 5 6 6 1 2]
# 6
# 1

floats = 10 * np.random.rand(10)
print(floats)
# [8.68963237 9.81168611 7.82009461 4.32851562 8.6915595  3.1769847
#  1.39594734 5.82033355 5.22510035 0.77193175]

sample = np.random.randn(1000)
print(sample[:10])
# [ 1.33946797 -0.11874673  1.05923663  0.90257227 -0.15100542 -0.68193573
#   2.22704714  1.4455776  -1.33325406  1.70338336]