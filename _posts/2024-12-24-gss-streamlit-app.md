---
layout: post
title: "Leaping into the GSS Age Pool: Exploring the GSS Data with Streamlit"
subtitle: Explore age distribution trends in the General Social Survey dataset, highlighting demographic shifts over time and introducing an interactive Streamlit app that allows users to visualize and analyze these patterns across various factors.
cover-img: /assets/img/map-glass.png
thumbnail-img: /assets/img/streamlit-thumb.png
share-img: /assets/img/map-glass.png
tags: [gss, Data Analysis, python, streamlit]
author: Ian Roman Villanueva
---

[Last time](https://eatsfrog.github.io/2024-12-18-surprising-facts-about-america/), we took a quick look at the General Social Survey, which offers a fascinating window into American society, capturing demographic trends and social attitudes across five decades. Today, we'll explore key insights from this rich dataset and introduce an interactive tool that lets you explore these patterns yourself.

## Age Patterns and Generational Divides

One of the most striking discoveries in our analysis was the bimodal age distribution in American society for 2022 (shown below). Rather than following a normal bell curve, the age distribution reveals two distinct peaks - one around 32 years and another near 60 years.

![Age Distribution](/assets/img/age-dist-adjusted.png)

The younger peak represents millennials and younger Gen X individuals, while the older peak captures baby boomers. This demographic structure helps explain many conflicting tensions in social dynamics, from housing market pressures to political polarization.

## Household Dynamics: Beyond Traditional Assumptions

Our analysis also revealed surprising patterns in household composition. While conventional wisdom might suggest that most Americans live in traditional family units, the data tells a more nuanced story:

![Household Composition by Size](/assets/img/size-dist-comp.png)

We can observe that:

* The majority of respondents live either alone or in two-person households
* Adult-only households dominate across all household sizes

Additionally, marital status data reveals an even more complex picture:

![Marital Status Distribution](/assets/img/marit-dist.png)

Despite high numbers of two-person households, marital status data shows significant diversity, with large populations of divorced and never-married individuals. This disconnect between household size and marital status suggests a shift away from traditional living arrangements, possibly reflecting changing social norms and economic realities.

## Lights, Camera, Interaction

To help you dive deeper into these social patterns, I've developed an [interactive Streamlit application](https://gss-app-stat386.streamlit.app/) that puts the power of data visualization at your fingertips. The app allows you to explore demographic trends through multiple interactive features:

* Year Range Selection: Analyze trends across any period from 1972 to 2022
* Demographic Filters: Filter data by sex, marital status, and political party affiliation
* Statistical Overlays: Toggle mean, median, and peak indicators for deeper analysis
* Dynamic Visualization: Watch how distributions change as you adjust parameters

Here's a screenshot showing how the app allows users to make selections:

![Streamlit App Screenshot](/assets/img/streamlit-screenshot.png)

You can find the complete code for this Streamlit app in my [GitHub repository](https://github.com/eatsfrog/gss-streamlit-app), and you can interact with the app directly [here](https://gss-app-stat386.streamlit.app/).

## Making Data Come Alive

This [app](https://gss-app-stat386.streamlit.app/) can help you transform static numbers and figures into a launchpad for ideas. Want to understand how age distributions differ between political parties? Simply select different party affiliations from the dropdown menu. Curious about changes in household composition over time? Adjust the year range slider to watch the patterns evolve.

This interactive approach to data exploration allows users (from beginners to experts) to:

* Test their own hypotheses about social trends
* Discover unexpected patterns in demographic data
* Understand how different social factors intersect

But most importantly, it makes data analysis fun and engaging, turning what might seem like a dry subject into a dynamic and interactive experience. My biggest hope is that this app will inspire curiosity and spark new ideas, leading you to explore the dataset and draw your own conclusions!

## Looking Forward

Whether you're a researcher, student, or simply curious about social trends, the GSS Visualization App offers a unique way to explore and understand simple demographic patterns. The combination of careful data analysis and interactive visualization tools opens new possibilities for understanding our society. As more GSS data is released, we'll be able to track how these patterns evolve and what they tell us about America's future.

I encourage you to explore the data yourself and discover your own insights into American society's changing landscape. Remember: behind every data point is a human story, and together these stories paint a picture of who we are as a society.

**As always, keep your data clean and your algorithms green!**

---

## Further Reading

1. General Social Survey - Dataset: [https://gss.norc.org/us/en/gss/get-the-data.html](https://gss.norc.org/us/en/gss/get-the-data.html)
2. General Social Survey - Data Explorer: [https://gssdataexplorer.norc.org/](https://gssdataexplorer.norc.org/)
3. GitHub Repository: [gss-streamlit-app](https://github.com/eatsfrog/gss-streamlit-app)
4. GSS Data Analysis Post: [https://eatsfrog.github.io/2024-12-18-surprising-facts-about-america/](https://eatsfrog.github.io/2024-12-18-surprising-facts-about-america/)
5. Streamlit App: [GSS Visualization App](https://gss-app-stat386.streamlit.app/)
6. Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)
