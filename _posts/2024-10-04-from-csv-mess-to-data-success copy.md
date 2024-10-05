---
layout: post
title: From CSV Mess to Data Success
subtitle: Learn the power of Pandas merging!
cover-img: /assets/img/csv-merge.png
thumbnail-img: /assets/img/csv-thumb.png
share-img: /assets/img/csv-merge.png
tags: [pandas, csv, python]
author: Ian Roman Villanueva
---

Hey there, fellow data wranglers! 👋 Ever found yourself drowning in a sea of CSV files, desperately trying to piece together a coherent dataset? Trust me, I've been there. It's like trying to solve a jigsaw puzzle while blindfolded and riding a unicycle. But fear not! I'm here to throw you a lifeline in the form of pandas, your new best friend in the data manipulation world.

## Why Merge CSV Files?

[Brief explanation of the necessity of merging files and a quick introduction to CSVs]

## Enter Pandas: Your CSV Merging Solution

[Introduce pandas and its capabilities for handling CSV files]

Before we dive into merging CSVs, there are a few requirements I assume.

**Requirements:**
- [Python](https://www.python.org/downloads) or [Anaconda](https://docs.anaconda.com/anaconda/install) installation
- pandas library (see [here](https://pandas.pydata.org/docs/getting_started/install.html]) for help)
- Basic knowledge of Python and data manipulation concepts. If you're new to Python, check out the links I've added [below](#references-and-further-reading).
- CSV files I will be using throughout this tutorial: [here] [here] [here]

## Setting the Stage: Our E-commerce Data Drama

Picture this: You're a data analyst at "Totally Not Amazon," a booming e-commerce company. Your boss (let's call her Karen, because of course it's Karen) bursts into your cubicle, spilling coffee everywhere, and demands a comprehensive sales analysis... by yesterday. 😱

The catch? The data is spread across multiple CSV files, each representing a different region. It's time to roll up your sleeves and get pandas-tastic!

## Act 1: Setting Up Our Pandas Playground

First things first, let's import pandas and create some sample data. Don't worry, I promise this is the least exciting part of our adventure.

```python
import pandas as pd
import numpy as np

# Let's create some juicy sample data
df1 = pd.DataFrame({
    'Order_ID': [1, 2, 3, 4, 5],
    'Product': ['Rubber Duck', 'Inflatable Unicorn', 'Novelty Socks', 'Lava Lamp', 'Disco Ball'],
    'Quantity': [10, 20, 15, 30, 25],
    'Region': ['North', 'South', 'East', 'West', 'North']
})
df1.to_csv('sales_region1.csv', index=False)

df2 = pd.DataFrame({
    'Order_ID': [6, 7, 8, 9, 10],
    'Product': ['Inflatable Unicorn', 'Novelty Socks', 'Rubber Duck', 'Disco Ball', 'Lava Lamp'],
    'Quantity': [12, 18, 22, 27, 33],
    'Region': ['South', 'East', 'West', 'North', 'South']
})
df2.to_csv('sales_region2.csv', index=False)

customer_df = pd.DataFrame({
    'Order_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Customer': ['John "The Duck" Smith', 'Emma "Unicorn Queen" Johnson', 'Alex "Sock Enthusiast" Brown', 'Sarah "Groovy" Williams', 'Mike "Disco King" Davis', 'Lisa "Party Animal" Wilson', 'Tom "Sockstar" Taylor', 'Anna "Quack Attack" Anderson', 'Chris "Glitter Ball" Martinez', 'Kate "Lava Lover" Thompson']
})
customer_df.to_csv('customer_data.csv', index=False)
```

## Act 2: The Great Concatenation Caper

Now, let's tackle our first challenge: combining those regional sales files. Enter `pd.concat()`, the superhero of stacking DataFrames!

```python
# Time to read those CSVs like they're the latest bestsellers
df1 = pd.read_csv('sales_region1.csv')
df2 = pd.read_csv('sales_region2.csv')

# Concatenate like your job depends on it (because it probably does)
combined_df = pd.concat([df1, df2], ignore_index=True)

print("Behold, our merged sales data in all its glory!")
print(combined_df)
```

Voilà! We've just performed the pandas equivalent of a perfect high-five. Our regional data is now one big happy family.

## Act 3: The Merge Miracle

But wait, there's more! We've got customer data sitting on the sidelines, feeling left out. Time for `pd.merge()` to work its magic and bring everyone to the party.

```python
# Bring in the customer data, fashionably late
customer_df = pd.read_csv('customer_data.csv')

# Merge like you've never merged before
merged_df = pd.merge(combined_df, customer_df, on='Order_ID')

print("Ladies and gentlemen, I present to you, the fully merged masterpiece!")
print(merged_df)
```

And just like that, we've created a data masterpiece that would make even Picasso jealous.

## The Grand Finale: Tackling the Troublemakers

Of course, it wouldn't be a true data adventure without some pesky problems to solve. Let's face them head-on!

### Missing Values: The Ghost in the Machine

```python
# Banish those ghosts (missing values) to the netherworld (or just fill them with zeros)
merged_df.fillna(0, inplace=True)

print("Poof! Missing values begone!")
```

### Mismatched Columns: The Square Peg in a Round Hole

```python
# When columns don't play nice, we make them behave
well_behaved_df = pd.merge(df1[['Order_ID', 'Product']], df2[['Order_ID', 'Quantity']], on='Order_ID')

print("Columns aligned faster than planets in retrograde!")
```

### Duplicates: The Clones Attack

```python
# Duplicates, prepare to be terminated
merged_df.drop_duplicates(subset=['Order_ID'], keep='first', inplace=True)

print("Duplicates eliminated with the precision of a Jedi master!")
```

## The Epic Conclusion

And there you have it, folks! We've conquered CSV files, tamed wild data, and emerged victorious. Karen will be so impressed, she might even learn your name!

Remember, in the world of data, pandas is your trusty sidekick. With `pd.concat()` and `pd.merge()` in your toolkit, you're ready to face any data challenge that comes your way. Now go forth and merge with confidence, you data superhero, you!
---

## References and Further Reading

[List of resources and additional information]