import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load seed weight and leaf area data from csv files
seed_weight = pd.read_csv('seed_weight.csv', header=0).values
leaf_area = pd.read_csv('leaf_area.csv', header=0).values

# Define regions and colors for each region
regions = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E', 'Region F']
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

# Perform Pearson's correlation between seed weight and leaf area data for each region
correlations = []
for i in range(6):
    r, p = pearsonr(seed_weight[:, i], leaf_area[:, i])
    correlations.append(r)

# Plot scatter plot with six subplots, one for each region
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    ax.scatter(seed_weight[:, i], leaf_area[:, i], c=colors[i])
    ax.set_title(regions[i] + ', r = {:.2f}'.format(correlations[i]))
    ax.set_xlabel('Seed Weight')
    ax.set_ylabel('Leaf Area')

# Add legend outside of the plots showing the regions
fig.legend(regions, loc='center right', ncol=1, bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()
