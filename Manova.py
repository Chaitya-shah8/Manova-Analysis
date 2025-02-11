import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.multivariate.manova import MANOVA
from statsmodels.stats.multicomp import pairwise_tukeyhsd

heart = pd.read_csv("C:\\Users\\Metanoid\\Downloads\\MANOVA_R-main\\MANOVA_R-main\\heart.csv")


print(heart.info())
print(heart.describe())

_, p_value_chol = stats.shapiro(heart['chol'])
_, p_value_thalach = stats.shapiro(heart['thalach'])


plt.figure(figsize=(10, 5))


plt.subplot(1, 2, 1)
sns.histplot(heart['chol'], kde=True, color='blue')
plt.title(f'Cholesterol Distribution (Shapiro-Wilk p={p_value_chol:.3f})')


plt.subplot(1, 2, 2)
sns.histplot(heart['thalach'], kde=True, color='red')
plt.title(f'Max Heart Rate Distribution (Shapiro-Wilk p={p_value_thalach:.3f})')

plt.tight_layout()
plt.show()


z_chol = np.abs(stats.zscore(heart['chol']))
z_thalach = np.abs(stats.zscore(heart['thalach']))

outliers_chol = np.where(z_chol > 3)
outliers_thalach = np.where(z_thalach > 3)

print(f"Aykırı Değerler - Cholesterol: {outliers_chol}")
print(f"Aykırı Değerler - Thalach: {outliers_thalach}")


heart_clean = heart[(z_chol <= 3) & (z_thalach <= 3)]


shapiro_chol_clean = stats.shapiro(heart_clean['chol'])
shapiro_thalach_clean = stats.shapiro(heart_clean['thalach'])

print(f"Shapiro-Wilk Test (Temizlenmiş Veri) - Cholesterol: p-value = {shapiro_chol_clean.pvalue}")
print(f"Shapiro-Wilk Test (Temizlenmiş Veri) - Thalach: p-value = {shapiro_thalach_clean.pvalue}")


cor_matrix = heart[['chol', 'thalach']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Cholesterol and Max Heart Rate Correlation')
plt.show()


manova_model = MANOVA.from_formula('chol + thalach ~ cp', data=heart)
manova_results = manova_model.fit()

print(manova_results.summary())


print(manova_results)

model = ols('chol ~ C(cp)', data=heart).fit()
tukey_result = pairwise_tukeyhsd(endog=heart['chol'], groups=heart['cp'], alpha=0.05)


tukey_result.plot_simultaneous()
plt.title('Tukey HSD Test for Cholesterol')
plt.show()


X = heart[['chol', 'thalach']]
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]


plt.figure(figsize=(8, 6))
sns.barplot(x='VIF', y='feature', data=vif_data, palette='viridis')
plt.title('Variance Inflation Factor (VIF)')
plt.show()


plt.figure(figsize=(12, 6))

# Cholesterol
plt.subplot(1, 2, 1)
sns.boxplot(data=heart, x='cp', y='chol', palette='Set2')
plt.title('Cholesterol by Chest Pain Type')

# Max Heart Rate
plt.subplot(1, 2, 2)
sns.boxplot(data=heart, x='cp', y='thalach', palette='Set2')
plt.title('Max Heart Rate by Chest Pain Type')

plt.tight_layout()
plt.show()
