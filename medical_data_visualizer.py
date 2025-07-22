import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# 3. Normalize 'cholesterol' and 'gluc' (0 is good, 1 is bad)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Categorical Plot
def draw_cat_plot():
    # 5. Melt data
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat for Seaborn
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Plot with sns.catplot()
    plot = sns.catplot(data=df_cat,
                       x='variable',
                       y='total',
                       hue='value',
                       col='cardio',
                       kind='bar')

    # 8. Get figure object
    fig = plot.fig

    return fig

# 9. Heat Map
def draw_heat_map():
    # 10. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11. Calculate correlation matrix
    corr = df_heat.corr()

    # 12. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 14. Draw heatmap
    sns.heatmap(corr,
                mask=mask,
                annot=True,
                fmt=".1f",
                center=0,
                vmax=0.3,
                vmin=-0.1,
                square=True,
                linewidths=0.5,
                cbar_kws={"shrink": 0.5})

    return fig
