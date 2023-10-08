# A Definition of Data Analysis
We will look at an informal definition of Data Analysis, adapted from wikipedia (https://en.wikipedia.org/wiki/Data_analysis):

>Data analysis is the **process** of inspecting, cleaning, transforming, and modeling data with the goal of **understanding** something about a given phenomenon, supporting **decision-making**, and **making predictions on unseen data**.

While this definition is not very formal, it is a good starting point to get an understanding of what data analysis is. Let's dive into the main aspects of this definition in the following sections.

## Data Analysis as a Process
In the definition above, data analysis is regarded to as the process of inspecting, cleaning, transforming and modeling data. Indeed, it is very important to understand that **data analysis is a process**. In this sense, data analysis is not just a single algoritm or a single technique you can apply to the data. It is instead a collection of techniques, statistical and machine learning tools can be applied to achieve a given goal. Four main set of techniques that we can usually apply when processing data are:

* **Inspecting**: the process of looking at the data to assess some of its main properties, such as the number of observations (rows), variables (columns), what are the typical values of variables (e.g., in the previous examples of students and courses we should expects marks out of 10), etc.
* **Cleaning**: is the process of "fixing" some aspects of the data which are likely to be incorrect. For instance we could remove rows with missing or out of range values (students with marks over 10 or with negative marks).
* **Transforming**: transforming the data from a format to another one. For instance, we may add a new "mean" column to each student in the example above, or, after realizing that English marks are out of 30 while the others are out of 10, transforming that column by dividing all numbers by 3 (so that they are in the same range as other variables).
* **Modeling**: choosing and tuning a statistical model which can be used to summarize, explain or make predictions about the data. We will discuss more models later, but for the moment it is important to understand that a model tries to abstract away and represent such aspects of the data in a way that, in some sense, the model becomes a good explanation of the data itself. For instance, if we could create a model which can allow us to reconstruct the correct value of English from the values of the other courses, we have found some kind of mathematical explanation of how marks in other course affect marks in English and we have shown that marks in Enligh are not independent from the other mark.

## Goals of Data Analysis
We can simplify (as in the spirit of this introductory material) by saying that data analysis processes can aim to address three main types of goals:

* Understanding something about a given phenomenon;
* Supporting decision-making;
* Making predictions on unseen data.

We'll see some examples of each of these goals in the following sections.

### Understanding Something About a Given Phenomenon
One of the main goals of data analysis is to obtain an understanding of how a given phenomenon works. For instance, in the 19th century, Charles Darwin developed his theory of evolution by natural selection via close examination of nature.

In a five-year journey, Darwin explored various continents, collecting a large number of specimens, including fossils, plants, animals, and geological samples. In Galapagos Islands, he encountered a variety of bird species known as finches. By observing the collected specimens, Darwin concluded that each island had its own species of finches, with different beak shapes of sizes, that he believed were influenced by the characteristics of each island. 

Analyzing the data with comparative anatomy, he concluded that species evolved to adapt to a specific environment by natural selection. While Darwin did not use modern data analysis techniques, his intuitions were supported by data collection (collection of specimens) and careful observation of the collected samples.

Note that, in this example, we are not necessarily interested in using the results of the analysis to achieve some other goal - our only interest is to gather knowledge on some (in this case) natural phenomenon.


```{figure} /_static/lecture_specific/intro_data_analysis/darwin.jpg
```

(Image from https://it.wikipedia.org/wiki/Charles_Darwin)

```{figure} /_static/lecture_specific/intro_data_analysis/origin.jpg
```
(Image from https://en.wikipedia.org/wiki/On_the_Origin_of_Species)

### Supporting Decision-Making
In many cases, data analysis can be used to support decision making. Suppose that we work for a company producing three products A, B and C. The products are sold in three different geographic locations X, Y, Z. Due to the crisis, the company has to reduce the production and wants to cut down one of the three products, but of course they would want to choose the product to stop producing in a way to loose as little earnings as possible. A possible option could also be to keep the three products but reduce the amount of units produced during the year. Fortunately, the company has historical data of productions and sells in the last 5 years. In contexts like these, we could use data analysis techniques to understand which is the best decision to take. Some data analysis techniques could also allow us to make some simulations of what could happen if we took one decision or another.

### Making Predictions on Unseen Data
Another typical goal of data analysis is the one of creating models able to make predictions on unseen data. Imagine you are working for a bank which wants to develop an algorithm capable of understanding whether a given transaction is a legitimate one or a fraud attempt. The bank already has a team which reviews the some of the transactions to check if they are legitimate. This is done by checking things such as if the beneficiary of a given transaction is an unusual one, if the beneficiary is notably not to be trusted, and if too many transactions are performed in a given amount of time. If we had past observations of transactions and a variable telling us which of those turned out to be a fraud attempt, we may use data analysis to create a predictive algorithm capable of predicting whether a transaction is a fraud attempt by looking at the values of other available variables such as the amount of money, the nationality of the beneficiary, and the number of transactions made in the last 24 hours.

## Main Types of Data Analysis
While we have discussed of broad goals of data analysis above, we can divide data analysis processes into five main types (different categorization may be possible, but we will stick to this one in this course). Each category describes a *mindset* and a *set of tools* that can be used to perform data analysis processes towards the accomplishment of one or more of the goals above. It should be clear that, during a data analysis process, one may mix the different kinds of data analysis or perform them in a sequential fashion. As we will see, the different approaches also rely on similar statistical techniques and one approach does not exclude the others.

The main types of data analysis are:

* Descriptive analysis;
* Exploratory analysis;
* Inferential analysis;
* Causal analysis;
* Predictive analysis;
* Time series analysis.

Let's briefly see what these types of data analysis are, but we will analyze in greater detail each of these approaches during the course.

### Descriptive Analysis
The goal of descriptive analysis is to provide a series of numbers or visualization of the data that describe their main characteristics. The goal is provide a compact summary of the main characteristics of the data. Examples of this kind of analysis including computing the proportion of males and females in the dataset of students and marks, the average marks that each course gets, etc. At this stage, we are not interpreting the results, but only providing some quantitative or qualitative measures of some property. One may think that the best description of some data is the data itself, and that would not be too far from the truth! However, in some cases, it is useful to provide summary statistics which are not evident from the data to start getting a sense of it.

The image in the following shows some examples of descriptive statistics and visualizations extracted from a dataset. We will get more into the details of such techniques later in the course.

```{figure} /_static/lecture_specific/intro_data_analysis/descriptive.png
```

### Exploratory Analysis
Exploratory analysis aims to examine the structure of the data, the distributions of variables (e.g., how do marks distributes for Physics? What is the average mark?) and the relationships between two or more variables (e.g., do students who have low marks in Physics also get low marks in Mathematics?). As we will see, visualizations are a useful tool for exploratory data analysis, mainly because they are often easy to intuitively absorb. Exploratory data analysis can have different goals, including **finding problems in the data** (e.g., out of range values, incorrect values, etc.), **determining whether the data is good for the analysis we have in mind**, **making initial hypothesis on which data analysis questions we'll be able to answer with the data**. Importantly, at this stage we are already aiming to find patterns in the data, even if we are keeping our analysis at an informal level.

The image in the following shows some examples of visualizations for exploratory data analysis.

```{figure} /_static/lecture_specific/intro_data_analysis/exploratory.png
```

### Inferential Analysis
The goal of inferential analysis is to show formally whether some feature of pattern that we are observing in our dataset is actually likely to be true outside of the dataset at hand. Let's say we are exploring a set of data of people with their daily average consumption of sugars and whether they have diabetes. We may find by looking at the data that people who consume a lot of sugar are more likely to get diabetes. We may be tempted to claim that what we have found a general conclusion, which may apply to the general population (beyond the set of data we are considering). Statistical inference, give us the mathematical tools to check if this generalization is actually possible. For instance, if we had only $100$ rows in our dataset, we may be suspicious that our conclusion does not apply to the general case and we may want to invest more time in collecting additional data. But, how much data is enough? An inferential analysis will allow us to also check that.

The figure below shows how the sampling process can lead to a dataset which is not an accurate picture of the real world. Inferential analysis aims to check if any conclusion we are drawing based on our data is likely to be true outside of the dataset.

```{figure} /_static/lecture_specific/intro_data_analysis/selection_bias.png
```


### Causal Analysis
While an inferential analysis may allow us to conclude that older people are more likely to develop diabetes and it may even concludes that this apply to the general population, we still don't know if it safe to say that sugar actually causes people to develop diabetes. This would be an important conclusion. If we knew for certain that consuming more than a given amount of sugar per day would lead to diabetes, than we could enforce some kind of policy to allow people to get the disease. Examples of policies may including classifying foods by their amounts of sugar, so that people can easily know which foods are more dangerous. But what if there is no causal relationship between the consumption of sugar and getting diabetes? For instance, it could just be that people who get diabetes also have a very sedentary life and people with a very sedentary life tend to eat more sugars (e.g., just to get distracted). If this were true, than, it could just be that being sedentary causes diabetes and since being sedentary is associated with eating more sugar, then we were observing an apparent causal effect between eating sugar and getting diabetes. If the second hypothesis is true, then there is no need to classify foods etc. (actually, this may even be undesirable and damage the market). Causal analysis give us tools to determine if a causal effect between two events exist, beyond what we simply observe in the data.

The figure below illustrates how observing some data may suggest that believing in evolution impacts the richness of a country. However, we can probably imagine that other factors may contribute to the observed correlation (more on this later), which might not be due to a cause-effect mechanism.

```{figure} /_static/lecture_specific/intro_data_analysis/spurious_correlation.jpg
```

(Image source: https://www.flickr.com/photos/jurvetson/5955305490)

### Predictive Analysis
The goal of predictive analysis is to form a model able to predict some unobserved features in data which may be available in the future. Let's say that we also captured other variables in our example diabetes dataset, such as sex, age, job, etc. We suspect that part of the member of the community may have diabetes and we would like to screen them. However, we cannot just screen all of them (that would be too much and we don't have enough resources). We may hence think to prioritize the subjects who are more likely to develop diabetes. But who are those? A causal analysis may have revealed that easting too much sugar may be a cause of developing diabetes, but we also have more variables we are capturing. While it is very unlikely that sex of age are causing diabetes, we may observe that, for some reason, older females tend to develop diabetes more often. Predictive analysis allow us to create models that allow to predict a given variable from a set of other variables. For instance, I could create a model which predicts the probability of developing diabetes from sex, age and job. Let's say I have a list of potential people to screen with the three variables above captured, but I was not able to collect the amount of sugar they consume (note that this is much harder to obtain), then I could use my model on each row to predict what is the probability of each person to develop diabetes. I could then start by screening people with high predicted probabilities of developing the disease. Note that predictive analysis does not care about causal effects and does not rely on inferential analysis to check if our assumptions are valid beyond the dataset, however, it still requires to work for data which have never been seen before. In practice, while we may create our model based on our dataset, we are really interested in using it on data which is not already captured in our dataset (for those in the dataset, we already know who has diabetes).

In the example below, predictive analysis can allow to predict "group" from the other variables for those subjects for which the group is unknown (???).

|relwt|glufast|glutest|instest|sspg|group|
|---|---|---|---|---|---|
|1\.06|96|465|237|111|Chemical|
|1\.09|110|426|117|118|Normal|
|0\.93|93|472|285|194|???|
|0\.92|300|1468|28|455|Overt|
|0\.88|99|376|134|80|Normal|
|1\.1|107|403|267|254|Normal|
|0\.98|130|670|44|167|???|
|1\.13|92|476|433|226|Chemical|
|1\.0|102|378|165|117|Normal|
|0\.96|78|290|136|142|???|

### Time Series Analysis

Time series analysis aims to analyze data points recorded over of sequence of intervals to uncover patterns, trends, seasonality, and other characteristics of the data and to make forecasts based on historical data. For example, imagine a retail store which wants to make a forecast to predict sales for the next year. By analyzing the last five years of their sales, the store can use time series analysis to *visualize* the data, analyze trends (e.g., if sales are globally increasing), analyze seasonality (are there more sales over christmas?), and predict future sales. The predicted sales can be useful to better organize supplies and staff.


The image below shows an example of time series forecasting.

```{figure} /_static/lecture_specific/intro_data_analysis/probabilistic_forecast.png
```
(Image from https://www.lokad.com/probabilistic-forecasting)