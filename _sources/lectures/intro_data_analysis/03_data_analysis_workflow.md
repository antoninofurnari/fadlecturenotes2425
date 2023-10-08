
# Data Analysis Workflow
The typical workflow of data analysis is composed of the following stages:
1. Define your data analysis question
2. Collect the data needed to answer the data analysis question
3. Clean and format the data
4. Explore and describe the data
5. Choose suitable models for the analysis
6. Fit, fine-tune, evaluate, and compare the models for the considered data analysis
7. Review the data analysis when new data is available

Let's see more in detail what the different steps are about.

## Define your data analysis question
We can see data analysis as the process of answering a question. For instance, in the example above on the theory of evolution, Darwin tried to answer the question "do species appear as an adaptation to features of the environment?". Similarly, if we perform a causal analysis, we are trying to answer a question such as "does consuming too much sugar causes diabetes?" and if we perform a predictive analysis, we want to answer questions such as "What is the probability that this subject will develop diabetes?". If we see data analysis as the process of answering questions, the very first step in the data analysis process is to state the question in a way that it is accurate and can be answered with the data. We may revisit this step to refine the question based on what we discovered from the analysis performed so far.

## Collect the data needed to answer the data analysis question
In this stage, we will collect the data we need to answer the data analysis question. If we want to assess whether consuming too much sugar can cause diabetes, we could look for surveys already made on the topic, or we could set a study in which we go around and ask people what are their eating habits.

## Clean and format the data
The collected data does not always come in a "clean" form. In particular, we could have missing data, due to errors in the data collection or people uwilling to answer all questions. For instance, we may ask for age, but some subjects may refuse to tell us which is their age. In other cases, we may have outliers, i.e., "strange" numbers probably due to errors in data collection. For instance, if we find an age of 156 years, that may just be a typo and the intended age was just 56 years. In this stage, we will use a set of techniques to fix these problems in order to filter or clean the data.

## Explore and describe the data
This step consists in exploring the data to make sure that it can be used to answer the question. For instance, we may want to check if the data has been collected properly to answer our question, if it is of sufficient quantity and quality. We will also start to see informally if the question we choose can be plausibly answered with this data.

## Choose suitable models for the analysis
In this stage, we will select a set of models which seem to be suitable for answering our question. For instance, if we want to assess if we can predict whether a give subject will develop diabetes, we could choose classification models. The choice of the specific classification model will also be based on our understanding of the data (e.g., is the problem multi-dimensional? do we have enough data? etc.).

## Fit, fine-tune, evaluate, and compare the models for the considered data analysis
In this stage, we fit the chosen models to the data. After fitting them, we will need to evaluate how well they model the data. In many cases, we will fit more than one model and compare them to decide which of them is the most appropriate.

## Interpret the results
Once models have been built, we need to interpret our results in order to answer our question. For instance, we may observe a causal relationship between consuming sugars and developing diabetes, but we still need to interpret this result to get an understanding of why and how this happens.

## Communicate your results
This stage is concerned with communicating the results of our analysis in an most accurate and understandable way. The way in which we communicate may depend on the specific audience we are talking to. We will use an informal language if the audience is general and non-technical, or a more technical one if we are writing the results of our analysis in a research paper.

## Review the data analysis when new data is available
At some point, new data may be available. In this stage, we should revise our analysis and update our question, answer, or choice of models.


## Non-Linear Workflow
It should be noted that the process is not exactly linear. A good data analysis will iterate over the different steps and possibly jump back to any of those steps to revise it. For instance, after fitting the models on the data in step 5, one may note that some other models could give better results, and jump back to step 4 to refine the choice of the models, to then return to step 5.

The figure below shows the described workflow. Solid arrows illustrate the main flow, while dashed arrows show possible alternative paths after performing data exploration (step 4). Similar dashed arrows pointing to any past node may apply to the other nodes as well. In the example below, after exploratory data analysis (step 4), we may note that the data is not clean (maybe we find some outliers) or not adequately formatted, so we jump back to step 3. Similarly, we may find that we need more data, and jump back to step 2, or we may want to revisit and refine our data analysis question (step 1).

```{mermaid}
flowchart TD
    A(1. Define your data analysis question)
    B(2. Collect the data needed to answer the data analysis question)
    C(3. Clean and format the data)
    D(4. Explore and describe the data)
    E(5. Choose suitable models for the analysis)
    F(6. Fit, fine-tune, evaluate, and compare the models for the considered data analysis)
    G(7. Review the data analysis when new data is available)

    A --> B --> C --> D --> E --> F --> G

    D-.-> A
    D -.-> B
    D -.-> C
```

## Example
A data analyst working for an e-commerce company is tasked with analyzing customer reviews to improve product quality and customer satisfaction. The analyst starts by defining the question that the data analysis needs to answer (**step 1 - define your data analysis question**): "What are the common themes and issues in customer reviews, and how can we address them to improve product quality and satisfaction?" To answer this question, the analyst collects a diverse dataset of customer reviews from various sources (**step 2 - collect the data needed**), including the company's website, social media, and third-party review platforms. This dataset includes text reviews, ratings, and timestamps.

Once the data is collected, the analyst proceeds with data cleaning and formatting (**step 3 - clean and format the data**) since the initial dataset is messy with spelling errors, duplicate reviews, and inconsistent formatting. This involves data preprocessing, such as removing punctuation and converting text to lowercase. After cleaning the data, the analyst explores and describes it (**step 4 - explore and describe the data**) using techniques like word clouds, frequency distributions, and sentiment analysis to uncover common words, sentiments, and trends within the reviews.

To extract more meaningful insights from the text data, the analyst decides to apply natural language processing (NLP) techniques (**step 5 - choose suitable models for analysis**). Specifically, Latent Dirichlet Allocation (LDA) for topic modeling is chosen to identify recurring themes within the reviews. However, upon implementing LDA and reviewing the results, the analyst realizes that some topics are unclear and overlapping (**step 6 - fit, fine-tune, evaluate, and compare the models**).

Acknowledging the need to revisit the analysis, the analyst decides to backtrack to the data exploration step (**step 4 - explore and describe the data**) to gain a deeper understanding of the customer feedback. During this reassessment, it becomes evident that customers frequently mention product quality issues when discussing customer service experiences, leading to topic overlap. Armed with this insight, the analyst decides to categorize reviews into "product-related" and "service-related" (**step 5 - choose suitable models for analysis**) before applying topic modeling.

With the revised approach, the analyst proceeds to categorize reviews and then applies LDA separately to the two categories (**step 6 - Fit, fine-tune, evaluate, and compare the models for the considered data analysis**). This results in more interpretable topics, such as "defective products," "timely shipping," and "responsive customer support." The analyst then analyzes these topics to generate actionable insights for product improvement and customer service enhancements.

To ensure continuous improvement, the analyst commits to ongoing review and monitoring (**step 7 - Review the data analysis when new data is available**) of customer reviews, periodically updating the analysis to identify new emerging issues or trends. This iterative approach to data analysis allows for refining strategies and addressing evolving customer concerns over time.