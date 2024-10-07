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

## To Merge Or Not To Merge?

Picture this: you're a curious frog researcher with multiple sources of information about frogs. You have baseline data, updated information, and new arrivals. Separately, these data files offer interesting insights. But merge them together? Suddenly, you're diving into a lake of discovery! You can now answer complex questions about frog populations, conservation status, and habitat preferences across different datasets.

This is the power of merging CSV files. It's not just about combining data; it's about creating connections, revealing patterns, and unlocking insights that were previously hidden beneath the surface.

**Before we dive in, make sure you've got:**
- Python installed (preferably version 3.7+)
- pandas library (install it with `pip install pandas` or `conda install pandas`)
- Basic Python programming experience
- Our example CSV files: [frog_baseline.csv](/assets/datasets/frog_baseline.csv), [frog_baseline_update.csv](/assets/datasets/frog_baseline_update.csv), and [frog_new_arrivals.csv](/assets/datasets/frog_new_arrivals.csv)

## A Real-World Scenario

Let's say we're running a frog sanctuary. We have three CSV files:
1. "frog_baseline.csv" - containing baseline information about our amphibian friends
2. "frog_baseline_update.csv" - with updated information on health status and diet type
3. "frog_new_arrivals.csv" - detailing new frogs that have arrived at our sanctuary

We want to combine these to get a comprehensive view of our frog population. Time to make some data magic!

## Hopping Through the Process: A Step-by-Step Guide

### 1. Importing our data

First, let's import pandas and read our CSV files:

```python
import pandas as pd

baseline_df = pd.read_csv('frog_baseline.csv')
update_df = pd.read_csv('frog_baseline_update.csv')
new_arrivals_df = pd.read_csv('frog_new_arrivals.csv')

print(baseline_df.head())
print(update_df.head())
print(new_arrivals_df.head())
```

This gives us a quick peek at our data.

### 2. Understanding pd.merge and pd.concat

#### pd.merge

`pd.merge` is used to combine DataFrames based on a common column or index. It's similar to a SQL join operation. The basic syntax is:

```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None)
```

- `left` and `right` are the DataFrames to merge
- `how` specifies the type of merge: 'inner', 'outer', 'left', or 'right'
- `on` specifies the column(s) to merge on
- `left_on` and `right_on` are used when the merge columns have different names in the left and right DataFrames

#### pd.concat

`pd.concat` is used to concatenate DataFrames along a particular axis. The basic syntax is:

```python
pd.concat([df1, df2, ...], axis=0, ignore_index=False)
```

- The first argument is a list of DataFrames to concatenate
- `axis=0` concatenates vertically (stacking), while `axis=1` concatenates horizontally
- `ignore_index=True` resets the index of the result

### 3. Merging the files

Now, let's merge our files:

```python
# Merge baseline with updates
merged_df = pd.merge(baseline_df, update_df, on='Frog_ID', how='outer')

# Concatenate with new arrivals
final_df = pd.concat([merged_df, new_arrivals_df], ignore_index=True)

print(final_df.head())
print(final_df.info())
```

### 4. Identifying and Fixing Errors

Now that we've merged our data, let's identify and fix some common issues:

#### Duplicate Entries

```python
duplicates = final_df.duplicated(subset=['Frog_ID'], keep=False)
print(f"Number of duplicate entries: {duplicates.sum()}")

# Remove duplicates, keeping the first occurrence
final_df.drop_duplicates(subset=['Frog_ID'], keep='first', inplace=True)
```

#### Missing Values

```python
missing_values = final_df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Fill missing values with 'Unknown'
final_df.fillna('Unknown', inplace=True)
```

#### Mismatched Columns

```python
print("Columns in the final DataFrame:")
print(final_df.columns)

# Ensure all expected columns are present
expected_columns = ['Frog_ID', 'Sex', 'Age', 'Weight', 'Location', 'Health_Status', 'Diet_Type', 'Last_Checkup', 'Notes']
for col in expected_columns:
    if col not in final_df.columns:
        final_df[col] = 'Unknown'

# Reorder columns
final_df = final_df[expected_columns]
```

#### Data Type Inconsistencies

```python
print(final_df.dtypes)

# Convert 'Age' to integer, replacing any non-numeric values with NaN
final_df['Age'] = pd.to_numeric(final_df['Age'], errors='coerce').fillna(0).astype(int)

# Convert 'Weight' to float
final_df['Weight'] = pd.to_numeric(final_df['Weight'], errors='coerce')

# Convert 'Last_Checkup' to datetime
final_df['Last_Checkup'] = pd.to_datetime(final_df['Last_Checkup'], errors='coerce')
```

### 5. Analyzing our cleaned data

Let's check our final dataset:

```python
print(final_df.info())
print(final_df.describe())
```

### 6. Saving our new file

Finally, let's save our newly merged and cleaned data:

```python
final_df.to_csv('comprehensive_frog_data.csv', index=False)
```

This creates a new CSV in your current directory with all our frog data combined and cleaned.

## A Note on Proactive Error Handling

If we had wanted to fix these errors from the beginning, we could have used similar techniques before merging or concatenating the DataFrames. For example:

```python
def clean_dataframe(df):
    df.drop_duplicates(subset=['Frog_ID'], keep='first', inplace=True)
    df.fillna('Unknown', inplace=True)
    # Add other cleaning steps as needed
    return df

clean_baseline_df = clean_dataframe(baseline_df)
clean_update_df = clean_dataframe(update_df)
clean_new_arrivals_df = clean_dataframe(new_arrivals_df)
```

However, for the purposes of this guide, we chose to demonstrate error handling after merging to highlight common issues that can arise during the process.

## Conclusion: The Circle of Data Life

And there you have it, folks! We've successfully merged our frog datasets, creating a richer, more insightful pond of information. Remember, just as in nature, in data science, everything is connected. By merging our datasets and addressing common issues, we've created a more complete and accurate picture of our frog sanctuary ecosystem.

Now it's your turn to take the plunge! What datasets will you merge? What insights will you uncover in the depths of your data pond? Share your discoveries in the comments below, or hop over to our forum to discuss further!

**Until next time, keep your data clean and your algorithms green!**