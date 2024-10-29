---
layout: post
title: From CSV Mess to Data Success
subtitle: Harness the power of pandas to turn your scattered datasets into a streamlined and comprehensive analysis!
cover-img: /assets/img/csv-merge.png
thumbnail-img: /assets/img/csv-thumb.png
share-img: /assets/img/csv-merge.png
tags: [pandas, csv, python]
author: Ian Roman Villanueva
---

Welcome to Data Ponderings! In this guide, we'll explore how to use pandas, a powerful Python library, to efficiently merge CSV files into a single, cohesive dataset. Whether you're a seasoned data scientist or just starting out, this guide will help you navigate the waters of file merging with ease. Let's dive in!

## To Merge Or Not To Merge?

Picture this: you're a curious frog researcher with two separate sources of information. In one source, you have data about various frog species - their sizes, colors, and croaking patterns. In the other, you have detailed records of the ponds they inhabit - water quality, vegetation, and insect populations.

Separately, these data files tell different stories. But merge them together and suddenly a whole new stream of insights flows! You can now answer complex questions like "Do frogs with louder croaks prefer cleaner water?" or "Is there a correlation between pond vegetation and frog size?"

This is the power of merging CSV files! It's not just about combining data; it's about creating connections, revealing patterns, and unlocking insights that were previously hidden beneath the surface.

With that in mind, let's practice some CSV merging!

## Prerequisites

**Before we dive in, make sure you've got:**
- Python 3.9 or newer
- The pandas library
- Our example CSV files: [`frog_baseline.csv`](/assets/files/frog_baseline.csv), [`frog_baseline_update.csv`](/assets/files/frog_baseline_update.csv), and [`frog_new_arrivals.csv`](/assets/files/frog_new_arrivals.csv)

New to Python or pandas? No worries! Check out these beginner guides on [Python basics](https://www.geeksforgeeks.org/python-basics/) and [pandas fundamentals](https://www.geeksforgeeks.org/introduction-to-pandas-in-python/) before diving in.

## A Real-World Scenario: Frog Sanctuary

Imagine you're a data analyst at a frog sanctuary. You've got three CSV files to work with:
1. `frog_baseline.csv` - containing basic information about our amphibian friends
2. `frog_baseline_update.csv` - with updated information on health status, call frequency, and max hop distance
3. `frog_new_arrivals.csv` - detailing new frogs that have arrived at our sanctuary

Your mission is to combine these datasets to get a full picture of our frog population. This way, we can track changes in their health and behavior, spot trends, and make data-driven decisions to keep our frogs happy and healthy.

Let's make some data magic!

## Hopping Through the Process: A Step-by-Step Guide

### 1. Importing our dataframes

First, let's import our CSV files and take a quick peek at what we're dealing with.

```python
# Import pandas
import pandas as pd

# Import baseline data
baseline_df = pd.read_csv('frog_baseline.csv')
print("Baseline data shape:", baseline_df.shape)
print(baseline_df.head(3), end="\n\n")
```

This gives us our first look at the baseline data:
```
Baseline data shape: (79, 6)
   frog_id       species     sex  weight  age  size
0     3001     Dart Frog    Male   340.8    5  3.52
1     3002     Tree Frog  Female   432.4    7  5.00
2     3003  Leopard Frog  Female   434.0   10  5.49
```

We can see that we have 79 frogs in our baseline dataset, each with 6 attributes including their ID, species, sex, weight, age, and size.

Next, let's look at our updated baseline data:

```python
# Import updated baseline
baseline_update_df = pd.read_csv('frog_baseline_update.csv')
print("Baseline update data shape:", baseline_update_df.shape)
print(baseline_update_df.head(3), end="\n\n")
```

This shows us:
```
Baseline update data shape: (79, 6)
   frog_id habitat   health  max_hop  thermal_limit  call_freq
0     3001    Pond  Healthy     1.66          31.15     455.50
1     3002    Pond  Healthy     2.55          27.86     369.87
2     3003   Swamp  Healthy     2.86          27.59     413.24
```

The updated baseline data also contains 79 frogs, matching our original baseline. It provides new information such as habitat, health status, maximum hop distance, thermal limit, and call frequency.

Finally, let's examine our new arrivals:

```python
# Import new arrivals
new_arrivals_df = pd.read_csv('frog_new_arrivals.csv')
print("New arrivals data shape:", new_arrivals_df.shape)
print(new_arrivals_df.head(3))
```

This prints:
```
New arrivals data shape: (23, 12)
   frog_id       species   sex habitat   health  weight  size  age  max_hop  \
0     3078  Leopard Frog  Male  Forest  Healthy   811.1  6.44    5     2.89   
1     3079  Leopard Frog  Male    Pond     Sick   584.5  7.90    6     2.53   
2     3080     Dart Frog  Male  Forest  Healthy   413.4  5.80    7     2.31   

   thermal_limit  call_freq arrival_date  
0          27.45     479.92   2023-01-01  
1          29.99     396.86   2023-01-02  
2          28.08     368.61   2023-01-03
```

Our new arrivals dataset contains information on 23 new frogs, with 12 attributes for each. This dataset combines all the information from our baseline and updated baseline, plus an additional `arrival_date` column.

Now that we have a rough picture of our data, let's jump into merging!

### 2. Merging our data

Let's dive into data integration. We'll combine our datasets in two steps:

1. Join our baseline and update data
2. Add our new arrivals to the mix

#### 2.1 Joining Baseline and Update Data

First, we'll merge `baseline_df` and `baseline_update_df`:

```python
# Join datasets
merged_df = pd.merge(baseline_df, baseline_update_df, on='frog_id', how='outer')
print(merged_df.shape)
print(merged_df.head(3))
```

Output:
```
(81, 11)

   frog_id     species    sex  weight  age  size habitat   health  max_hop  thermal_limit  call_freq
0     3001   Dart Frog   Male   340.8    5  3.52    Pond  Healthy     1.66          31.15     455.50
1     3002   Tree Frog Female   432.4    7  5.00    Pond  Healthy     2.55          27.86     369.87
2     3003 Leopard Frog Female   434.0   10  5.49   Swamp  Healthy     2.86          27.59     413.24
```

We're using `frog_id` as our key for joining, ensuring each frog's information is properly matched. The `'outer'` join preserves all data, even for frogs missing some information. For more on this, see [this post](https://www.geeksforgeeks.org/different-types-of-joins-in-pandas/).

#### 2.2 Adding New Arrivals

Now, let's incorporate our new arrivals:

```python
# Concatenate datasets
final_df = pd.concat([merged_df, new_arrivals_df], ignore_index=True)
print(final_df.shape)
print(final_df.head(3))
```

Output:
```
(104, 12)

   frog_id     species    sex  weight  age  size habitat   health  max_hop  thermal_limit  call_freq arrival_date
0     3001   Dart Frog   Male   340.8    5  3.52    Pond  Healthy     1.66          31.15     455.50          NaN
1     3002   Tree Frog Female   432.4    7  5.00    Pond  Healthy     2.55          27.86     369.87          NaN
2     3003 Leopard Frog Female   434.0   10  5.49   Swamp  Healthy     2.86          27.59     413.24          NaN
```

Since `new_arrivals_df` includes all the columns in `merged_df`, we don't need any extra arguments except `ignore_index=True`, which resets the indexes of our DataFrame to ensure they match up correctly.

### 3. Identifying and Fixing Errors

We've successfully merged all our datasets into one cohesive unit. However, there are some data inconsistencies that we'll need to address in this step.

#### Duplicate Entries

First, let's check for any duplicate entries that might have snuck in during our merging process. We'll use pandas' built-in functions to identify and remove these pesky doubles.

```python
# Print all duplicated rows in the DataFrame
print(final_df[final_df.duplicated(keep=False)])

# Drop duplicate rows, keeping only the first occurrence
final_df.drop_duplicates(keep='first', inplace=True)
```

Output:
```
    frog_id   species     sex  weight  age  size habitat   health  max_hop  \
77     3077  Bullfrog  Female   897.9  5.0  7.34   Swamp  Healthy     3.14   
78     3077  Bullfrog  Female   897.9  5.0  7.34   Swamp  Healthy     3.14   

    thermal_limit  call_freq arrival_date  
77          28.31      356.9          NaN  
78          28.31      356.9          NaN
```
We caught a Bullfrog trying to make a double splash! After removing duplicates, we're left with a more robust dataset.

#### Mismatched Columns

Because arrival date is only present in the new arrivals but not in the baseline data, pandas will display a lot of NaN values. Since we don't really need arrival date for our analysis, we can drop that column.

```python
# Drop arrival_date column
final_df.drop('arrival_date', axis=1, inplace=True)
print(final_df.head(3))
```

Output:
```
   frog_id    species     sex  weight  age  size habitat   health  max_hop  \
0        0        NaN     NaN     NaN  NaN   NaN     NaN      NaN     0.00   
1     3001  Dart Frog    Male   340.8  5.0  3.52    Pond  Healthy     1.66   
2     3002  Tree Frog  Female   432.4  7.0  5.00    Pond  Healthy     2.55   

   thermal_limit  call_freq  
0           0.00       0.00  
1          31.15     455.50  
2          27.86     369.87
```

Without the arrival date column filled with NaN values, our dataset is looking even sharper!

#### Missing data

The last step is to look for missing values. Let's see what rows have missing values:

```python
# Print rows with missing values
print(final_df[final_df.isna().any(axis=1)])
```

Output:
```
    frog_id species   sex  weight  age  size habitat   health  max_hop  \
0         0     NaN   NaN     NaN  NaN   NaN     NaN      NaN      0.0   
79     3200     NaN  Male     NaN  5.0  10.0     NaN      NaN      NaN   
80     9999     NaN   NaN     NaN  NaN   NaN    Pond  Healthy      1.5   

    thermal_limit  call_freq  
0             0.0        0.0  
79            NaN        NaN  
80           40.0       25.0
```

There are many ways to deal with missing values, and the best option often depends on the analysis. In our case, these rows don't seem to add any value to our dataset, so we can drop them.

```python
# Drop rows with NaN values
final_df.dropna(inplace=True)
```

**Note**: There are other ways to handle missing data, which you can learn more about [here](https://towardsdatascience.com/8-methods-for-handling-missing-values-with-python-pandas-842544cdf891).


#### A Note on Proactive Error Handling

Usually, it's best practice to handle these data errors before merging. We could have used similar techniques as we did previously, but automating the process. For example:

```python
def clean_dataframe(df):
    df.drop_duplicates(subset=['frog_id'], keep='first', inplace=True)
    df.dropna(inplace=True)
    # Add other cleaning steps as needed
    return df

clean_baseline_df = clean_dataframe(baseline_df)
clean_update_df = clean_dataframe(update_df)
clean_new_arrivals_df = clean_dataframe(new_arrivals_df)
```

This makes merging CSV files easier and more efficient!

### 4. Reorder the columns

Now that we've handled errors, the last step is to reorder the columns to make our data a little more interpretable.

```python
# Reorder the columns of final_df
desired_order = ['frog_id', 'species', 'sex', 'habitat', 'health', 'weight', 'size',
                 'age', 'max_hop', 'thermal_limit', 'call_freq']

final_df = final_df[desired_order]
```

Let's see our final dataset:

```python
# Print dataset
print("Final data shape:", final_df.shape)
print(final_df.head(3))
```
Output:
```
Final data shape: (100, 11)
   frog_id       species     sex habitat   health  weight  size   age  \
1     3001     Dart Frog    Male    Pond  Healthy   340.8  3.52   5.0   
2     3002     Tree Frog  Female    Pond  Healthy   432.4  5.00   7.0   
3     3003  Leopard Frog  Female   Swamp  Healthy   434.0  5.49  10.0   

   max_hop  thermal_limit  call_freq  
1     1.66          31.15     455.50  
2     2.55          27.86     369.87  
3     2.86          27.59     413.24
```
Ta-da! We've succesfully merged three CSV files. Phew!

### 5. Saving our new file

As an optional last step, you can save your newly merged and cleaned data:

```python
final_df.to_csv('frog_full_data.csv', index=False)
```

Make sure to check your results with this [CSV file](/assets/files/frog_full_data.csv)!

## Conclusion: The Circle of Data Life

And there you have it, folks! We've successfully merged our frog datasets, creating a richer, more insightful pond of information. Remember, just as in nature, in data science, everything is connected. By merging our datasets we've created a more complete and accurate picture of our frog sanctuary ecosystem.

Now it's your turn to take the plunge! What datasets will you merge? What insights will you uncover in the depths of your data pond? Share your discoveries in the comments below, or hop over to our forum to discuss further!

**Until next time, keep your data clean and your algorithms green!**

<br/>
<br/>
<br/>
<br/>
<br/>

---

### Further Reading / Resources

- GeeksforGeeks: ["Different Types of Joins in Pandas"](https://www.geeksforgeeks.org/different-types-of-joins-in-pandas/)

- GeeksforGeeks: ["How to merge two csv files by specific column using Pandas in Python?"](https://www.geeksforgeeks.org/how-to-merge-two-csv-files-by-specific-column-using-pandas-in-python/)

- Geeksforgeeks: ["Learn Python Basics"](https://www.geeksforgeeks.org/python-basics/)

- Geeksforgeeks: ["Pandas Introduction"](https://www.geeksforgeeks.org/introduction-to-pandas-in-python/)

- Pandas documentation: [`pd.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) and [`pd.concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)

- Statology: ["How to Merge Multiple CSV Files in Pandas"](https://www.statology.org/pandas-merge-csv-files/)

- Towards Data Science: ["20 Examples to Master Merging DataFrames in Python Pandas"](https://towardsdatascience.com/20-examples-to-master-merging-dataframes-in-python-pandas-22ffcd6059d1)

- Towards Data Science: ["8 Methods For Handling Missing Values With Python Pandas"](https://towardsdatascience.com/8-methods-for-handling-missing-values-with-python-pandas-842544cdf891)