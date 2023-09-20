import numpy as np
from scipy import stats

with open("bm25.avg_p.txt", 'r') as file:
    file1 = [float(line.rstrip('\n')) for line in file]

with open("inl2.avg_p.txt", 'r') as file:
    file2 = [float(line.rstrip('\n')) for line in file]

sample1 = np.array(file1)
sample2 = np.array(file2)

t_statistic, p_value = stats.ttest_rel(sample1, sample2)

print(p_value)

with open("significance.txt", 'w') as file:
    file.write(str(p_value))