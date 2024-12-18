---
layout: post
title: "The GSS Voyage: Exploring Social Depths"
subtitle: A data-driven exploration of the GSS (General Social Survey) data that reveals demographic trends, living condition differences, and fascinating population facts.
cover-img: /assets/img/american-flag.jpg
thumbnail-img: /assets/img/flag-thumb.jpg
share-img: /assets/img/american-flag.jpg
tags: [gss, Data Analysis, python,]
author: Ian Roman Villanueva
---

All code available here: [repository](https://github.com/eatsfrog/gss-analysis.git).

Have you ever been curious about what we can learn about society from survey data? Today, we're diving into the General Social Survey (GSS), a treasure trove of information collected from 1972 to 2022. The GSS is a comprehensive survey that captures a "snapshot" of American society over time. It covers a wide range of topics, from work and education to social attitudes and demographics. With such a rich dataset at our fingertips, we're sure to uncover some intriguing insights.

## The Data Wrangling Challenge

Before we can start our analysis, we need to tackle the data wrangling process. It's like preparing a gourmet meal - the ingredients (data) need to be cleaned and prepped before we can create something delicious (insights)!

## The Motivating Question

Our primary question is: How can we use the GSS dataset to uncover meaningful trends and patterns in American society over the past 50 years?

## Ethical Considerations

It's important to follow proper procedure when analyzing or using data. The GSS data is publicly available and designed for research purposes. We've ensured our analysis respects privacy by working with anonymized data and adhering to the usage guidelines set by NORC at the University of Chicago, which conducts the survey.

### GSS Year Distribution

Alright, let's get started! First, since the GSS has been going on for so long, let's take a look at what years had the most respondents.

![GSS Year Distribution](/assets/img/year-dist.png)

Right away, we can see that 2006 was the year with the most respondents by a long shot, followed by 2021 and 2022. Another thing that we can notice is that we have data available for almost every year between 1972 and 1998, but after 1998 we only have data for even years (except 2021 due to COVID). Pretty interesting, huh!

Note: from this point forward, we'll be using the latest data to make our conclusions, which comes from the year 2022. This is to make our conclusions timely and relevant.

### Age Distribution

Now, let's answer a common question we might have: what's the average age of a respondent? I got the answer for you!

![Age Distribution](/assets/img/age-dist.png)

The mean and the median age are both around 48-49, but as we can see, that's not the full story. Since our data is shaped like a camel's back, that means our distribution is bimodal. By splitting our data in half and calculating the median, we can find the peaks.

![Age Distribution (Bimodal)](/assets/img/age-dist-adjusted.png)

Much better! Now we can see that most respondents will either be around 32 or 60 years old. Great! But we want to get a full picture of our sample, so let's take a look at other aspects of the data.

### Household Size and Composition

The next thing we'll be looking at is the household size of the respondents. Let's take a peek!

![Household Size Distribution](/assets/img/size-dist.png)

Quite the surprise, right? As it turns out, most respondents will be living either alone or in a 2-person household. But this doesn't tell us a lot. Are the other people relatives or friends? Are the other people adults, teens, or babies? Let's break it down and take a look at "household composition" (who lives in the household).

![Household Composition by Size](/assets/img/size-dist-comp.png)

As we can see, most households are composed of adults almost exclusively, with the red bars are reaching for the sky! We can begin to see a pattern here. If most households are composed of adults, and most households have 2 people in them... Then, that must mean that these are couples! That's a good hunch, but we need to verify it and justify it with the data.

### Marital Status

Let's take a look at the marital status of the respondents.

![Marital Status Distribution](/assets/img/marit-dist.png)

Huh? Quite the plot twist! Although married status is the most common, we have a large number of responses indicating that the person was divorced or never married. There might be some explanation for this, such as: "these people are cohabiting with their partner without being married"; but numbers speak louder than words!

## Wrapping Up

Data analysis is like being a detective, piecing together clues from numbers and variables to understand the bigger picture. This GSS dataset is a goldmine of information, waiting for curious minds to explore and uncover insights. So, whether you're a data enthusiast, a social scientist, or just someone curious about how society has changed over the past 50 years, the GSS dataset offers a fascinating journey through time and social trends.

**Keep your data clean and your algorithms green!**
