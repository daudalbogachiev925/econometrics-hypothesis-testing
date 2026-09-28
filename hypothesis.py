"""Проверка статистических гипотез."""
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(42)

# === 1. Двухвыборочный t-тест ===
group_a = np.random.normal(50, 10, 100)
group_b = np.random.normal(55, 10, 100)

t_stat, p_val = stats.ttest_ind(group_a, group_b)
print("=== Двухвыборочный t-тест ===")
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
print("Различие значимо:", p_val < 0.05)

# === 2. Парный t-тест ===
before = np.random.normal(70, 8, 50)
after = before + np.random.normal(2, 5, 50)

t_stat, p_val = stats.ttest_rel(before, after)
print("\n=== Парный t-тест ===")
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
print("Эффект значим:", p_val < 0.05)

# === 3. Хи-квадрат ===
table = np.array([[30, 20], [25, 25]])
chi2, p_val, dof, expected = stats.chi2_contingency(table)
print("\n=== Хи-квадрат ===")
print(f"chi2 = {chi2:.4f}, p = {p_val:.4f}, dof = {dof}")
print("Связь есть:", p_val < 0.05)

# === 4. ANOVA ===
g1 = np.random.normal(50, 5, 30)
g2 = np.random.normal(55, 5, 30)
g3 = np.random.normal(60, 5, 30)

f_stat, p_val = stats.f_oneway(g1, g2, g3)
print("\n=== ANOVA ===")
print(f"F = {f_stat:.4f}, p = {p_val:.4f}")
print("Различия есть:", p_val < 0.05)

# === 5. Сводная таблица ===
results = pd.DataFrame({
    "Тест": ["t-тест (незав.)", "t-тест (парный)", "Хи-квадрат", "ANOVA"],
    "Статистика": [t_stat, t_stat, chi2, f_stat],
    "p-value": [p_val, p_val, p_val, p_val]
})
print("\n", results)
