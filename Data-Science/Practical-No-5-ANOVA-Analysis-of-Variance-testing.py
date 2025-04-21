import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import matplotlib.pyplot as plt

# Actual data
method_a = [80, 82, 85, 78, 88]
method_b = [75, 79, 82, 80, 81]
method_c = [70, 75, 78, 72, 80]

# Combine data into a DataFrame
data = pd.DataFrame({
    'Method A': method_a,
    'Method B': method_b,
    'Method C': method_c
})

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(method_a, method_b, method_c)

# Print ANOVA results
print("One-way ANOVA:")
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis. At least one group mean is different.")
else:
    print("Fail to reject the null hypothesis. No significant difference in group means.")

# Perform Tukey's HSD post-hoc test
flatten_data = np.concatenate([method_a, method_b, method_c])
group_labels = np.repeat(['Method A', 'Method B', 'Method C'], len(method_a))
posthoc = pairwise_tukeyhsd(flatten_data, group_labels)

# Print post-hoc results
print("\nPost-hoc test:")
print(posthoc)

# Plot the post-hoc test results
posthoc.plot_simultaneous()
plt.title("Tukey HSD: Comparison of Teaching Methods")
plt.xlabel("Score Difference")
plt.show()
