import numpy as np
from scipy.stats import chisquare, chi2_contingency
observed = np.array([20, 30, 25, 25])
chi_stat, p_value = chisquare(observed)
print("Chi-Square Goodness of Fit Test")
print("Observed Frequencies:", observed)
print("Chi-Square Statistic:", round(chi_stat, 4))
print("P-Value:", round(p_value, 4))
if p_value < 0.05:
    print("Result: Reject the null hypothesis")
else:
    print("Result: Fail to reject the null hypothesis")
data = np.array([[20, 30], [25, 25]])
chi_stat, p_value, dof, expected = chi2_contingency(data)
print("\nChi-Square Test of Independence")
print("Observed Data:")
print(data)
print("Expected Frequencies:")
print(expected)
print("Chi-Square Statistic:", round(chi_stat, 4))
print("P-Value:", round(p_value, 4))
print("Degrees of Freedom:", dof)
if p_value < 0.05:
    print("Result: Variables are associated")
else:
    print("Result: No significant association")