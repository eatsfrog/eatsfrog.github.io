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

Welcome to Data Ponderings! Today, we're diving into the essential skill of merging CSV files. As data scientists, we often encounter multiple datasets that need to be combined for comprehensive analysis. We'll explore how to use pandas, a powerful Python library, to efficiently merge these files into a single, cohesive dataset. Whether you're a seasoned data hopper or just starting to dip your toes in the data pond, this guide will help you navigate the waters of file merging with ease.

## The Power of Merging

Imagine you're a curious frog researcher with two separate sources of information: one about frogs and another about lily pads. Separately, these datasets offer interesting insights. But when merged, they create a lake of discovery! You can answer complex questions like "Do older frogs prefer larger lily pads?" or "Is there a correlation between water depth and frog age?"

This is the power of merging CSV files. It's not just about combining data; it's about creating connections, revealing patterns, and unlocking insights that were previously hidden beneath the surface.

## Setting Up Our Pond

Before we dive in, make sure you have:

- Python installed (preferably version 3.7+)
- pandas library (`pip install pandas` or `conda install pandas`)
- Basic Python programming experience
- Our example CSV files: `frog_data.csv` and `lily_pad_data.csv`

## A Real-World Scenario

Let's say we're running a frog sanctuary. We have two CSV files:

1. `frog_data.csv` - containing information about our amphibian friends
2. `lily_pad_data.csv` - detailing the lily pads in our pond

We want to combine these to see which frogs are hanging out on which lily pads. Time to make some data magic!

## Hopping Through the Process: A Step-by-Step Guide

### 1. Importing Our Data

First, let's import pandas and read our CSV files:

```python
import pandas as pd

frogs_df = pd.read_csv('frog_data.csv')
lily_pads_df = pd.read_csv('lily_pad_data.csv')

print("Frogs DataFrame:")
print(frogs_df)
print("\nFrogs DataFrame Info:")
print(frogs_df.info())

print("\nLily Pads DataFrame:")
print(lily_pads_df)
print("\nLily Pads DataFrame Info:")
print(lily_pads_df.info())
```

Output:
```
Frogs DataFrame:
   frog_id frog_name  lily_pad_id  age
0        1    Freddy          101    2
1        2    Gertie          102    3
2        3     Larry          101    1
3        4      Lola          103    4
4        5     Benny          101    2

Frogs DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   frog_id      5 non-null      int64
 1   frog_name    5 non-null      object
 2   lily_pad_id  5 non-null      int64
 3   age          5 non-null      int64
dtypes: int64(3), object(1)
memory usage: 288.0+ bytes
None

Lily Pads DataFrame:
   lily_pad_id lily_pad_size  water_depth
0          101         Small          0.5
1          102        Medium          1.0
2          103         Large          1.5

Lily Pads DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   lily_pad_id    3 non-null      int64  
 1   lily_pad_size  3 non-null      object 
 2   water_depth    3 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 200.0+ bytes
None
```

### 2. Merging the Files

Now, let's explore two methods to combine our data: `merge()` and `concat()`. They're like two different species of water plants - both useful, but in different situations.

#### Using merge()

`merge()` is perfect when we have a common column to join on:

```python
combined_df = pd.merge(frogs_df, lily_pads_df, on='lily_pad_id', how='left')
print("Combined DataFrame using merge():")
print(combined_df)
print("\nCombined DataFrame Info:")
print(combined_df.info())
```

Output:
```
Combined DataFrame using merge():
   frog_id frog_name  lily_pad_id  age lily_pad_size  water_depth
0        1    Freddy          101    2         Small          0.5
1        2    Gertie          102    3        Medium          1.0
2        3     Larry          101    1         Small          0.5
3        4      Lola          103    4         Large          1.5
4        5     Benny          101    2         Small          0.5

Combined DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 0 to 4
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   frog_id        5 non-null      int64  
 1   frog_name      5 non-null      object 
 2   lily_pad_id    5 non-null      int64  
 3   age            5 non-null      int64  
 4   lily_pad_size  5 non-null      object 
 5   water_depth    5 non-null      float64
dtypes: float64(1), int64(3), object(2)
memory usage: 280.0+ bytes
None
```

#### Using concat()

`concat()` is great for stacking dataframes:

```python
stacked_df = pd.concat([frogs_df, lily_pads_df], axis=0)
print("Stacked DataFrame using concat():")
print(stacked_df)
print("\nStacked DataFrame Info:")
print(stacked_df.info())
```

Output:
```
Stacked DataFrame using concat():
   frog_id frog_name  lily_pad_id  age lily_pad_size  water_depth
0      1.0    Freddy        101.0  2.0           NaN          NaN
1      2.0    Gertie        102.0  3.0           NaN          NaN
2      3.0     Larry        101.0  1.0           NaN          NaN
3      4.0      Lola        103.0  4.0           NaN          NaN
4      5.0     Benny        101.0  2.0           NaN          NaN
0      NaN       NaN        101.0  NaN         Small          0.5
1      NaN       NaN        102.0  NaN        Medium          1.0
2      NaN       NaN        103.0  NaN         Large          1.5

Stacked DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
Int64Index: 8 entries, 0 to 2
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   frog_id        5 non-null      float64
 1   frog_name      5 non-null      object 
 2   lily_pad_id    8 non-null      float64
 3   age            5 non-null      float64
 4   lily_pad_size  3 non-null      object 
 5   water_depth    3 non-null      float64
dtypes: float64(4), object(2)
memory usage: 448.0+ bytes
None
```

### 3. Dealing with Common Issues

Like algae in a pond, data can sometimes get a bit messy. Here are some common issues and how to address them:

#### Missing Values

```python
combined_df.fillna('Unknown', inplace=True)
print("Combined DataFrame after filling NaN values:")
print(combined_df)
```

Output:
```
Combined DataFrame after filling NaN values:
   frog_id frog_name  lily_pad_id  age lily_pad_size  water_depth
0        1    Freddy          101    2         Small          0.5
1        2    Gertie          102    3        Medium          1.0
2        3     Larry          101    1         Small          0.5
3        4      Lola          103    4         Large          1.5
4        5     Benny          101    2         Small          0.5
```

#### Mismatched Columns

```python
combined_df = combined_df.reindex(columns=frogs_df.columns.union(lily_pads_df.columns))
print("Combined DataFrame after reindexing columns:")
print(combined_df)
```

Output:
```
Combined DataFrame after reindexing columns:
   frog_id frog_name  lily_pad_id  age lily_pad_size  water_depth
0        1    Freddy          101    2         Small          0.5
1        2    Gertie          102    3        Medium          1.0
2        3     Larry          101    1         Small          0.5
3        4      Lola          103    4         Large          1.5
4        5     Benny          101    2         Small          0.5
```

#### Duplicates

```python
combined_df.drop_duplicates(inplace=True)
print("Combined DataFrame after removing duplicates:")
print(combined_df)
```

Output:
```
Combined DataFrame after removing duplicates:
   frog_id frog_name  lily_pad_id  age lily_pad_size  water_depth
0        1    Freddy          101    2         Small          0.5
1        2    Gertie          102    3        Medium          1.0
2        3     Larry          101    1         Small          0.5
3        4      Lola          103    4         Large          1.5
4        5     Benny          101    2         Small          0.5
```

### 4. Saving Our New File

Finally, let's save our newly merged data:

```python
combined_df.to_csv('frog_lily_pad_data.csv', index=False)
print("New CSV file 'frog_lily_pad_data.csv' has been created.")
```

Output:
```
New CSV file 'frog_lily_pad_data.csv' has been created.
```

## Conclusion: The Circle of Data Life

And there you have it, folks! We've successfully merged our frog and lily pad data, creating a richer, more insightful pond of information. Remember, just as in nature, in data science, everything is connected. By merging our datasets, we've created a more complete picture of our frog sanctuary ecosystem.

Now it's your turn to take the plunge! What datasets will you merge? What insights will you uncover in the depths of your data pond? Share your discoveries in the comments below, or hop over to our forum to discuss further!

Until next time, keep your data clean and your algorithms green!