import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example: Creating a synthetic dataset (replace with real data)
np.random.seed(42)

# Generating synthetic accident data
n_samples = 1000
severity = np.random.choice(['Minor', 'Moderate', 'Severe'], size=n_samples, p=[0.6, 0.3, 0.1])
weather = np.random.choice(['Clear', 'Rain', 'Snow'], size=n_samples, p=[0.7, 0.2, 0.1])
age_group = np.random.choice(['<30', '30-50', '>50'], size=n_samples, p=[0.4, 0.4, 0.2])
speeding = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.3, 0.7])

accident_data = pd.DataFrame({
    'Severity': severity,
    'Weather': weather,
    'Age_Group': age_group,
    'Speeding': speeding
})

# Example: EDA
print(accident_data.head())
print(accident_data.describe())

# Visualizations
plt.figure(figsize=(14, 10))

# Plot 1: Distribution of Accident Severity
plt.subplot(2, 2, 1)
accident_data['Severity'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.xticks(rotation=0)

# Plot 2: Distribution of Weather Conditions
plt.subplot(2, 2, 2)
accident_data['Weather'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather')
plt.ylabel('Count')
plt.xticks(rotation=0)

# Plot 3: Distribution of Age Groups
plt.subplot(2, 2, 3)
accident_data['Age_Group'].value_counts().plot(kind='bar', color='salmon')
plt.title('Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=0)

# Plot 4: Distribution of Speeding
plt.subplot(2, 2, 4)
accident_data['Speeding'].value_counts().plot(kind='bar', color='gold')
plt.title('Distribution of Speeding')
plt.xlabel('Speeding Involved')
plt.ylabel('Count')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
