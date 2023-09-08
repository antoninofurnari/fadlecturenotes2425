# Data, Uncertainty and Random Variables

## Informal Definition of Data

We have seen data social media is “all about the data” and about what we can do with this data. We will start by giving a definition of what we mean by ‘data’.

Following Wikipedia, we could say that:

‘Data is a set of values of subjects  
with respect to qualitative or quantitative variables’

<u>Qualitative</u>: properties that can be observed and cannot generally be measured with a numerical value (e.g., ‘color’, ‘sex’);

<u>Quantitative</u>: properties that can be quantified with a number (e.g., ‘height’, ‘weight’, ‘age’).

```{figure} /_static/lecture_specific/data_probability/image1.png
```

For example, a twitter post (a ‘tweet’) is data, i.e., a set of data with respect to different variables, such as user, time, text, images, comments, etc.

Some of these entities (e.g., comments) can be in turn a list of entities (e.g., a list of comments).

## Uncertainty & Importance of Probability Theory

We have seen that dealing with data means dealing with some variables assuming some values.

However, what can we say about what values will assume such variables?

In some cases, it is possible to predict the values of variables with perfect accuracy, given a set of initial conditions. For instance, think about a system of equations describing the speed of objects according to Newtonian laws.

In other cases, modeling the relationship between variables in a deterministic way is not possible.

We often say that this is due to <u>uncertainty.</u>

**Uncertainty in a system can be due to different factors:**

- <u>Inherent stochasticity in the system being modeled.</u> For example, most interpretations of quantum mechanics describe the dynamics of subatomic particles as being probabilistic. We can also create theoretical scenarios that we postulate to have random dynamics, such as a hypothetical card game where we assume that the cards are truly shuﬄed into a random order.

- <u>Incomplete observability.</u> Even deterministic systems can appear stochastic when we cannot observe all the variables that drive the behavior of the system. For example, in the Monty Hall problem, a game show contestant is asked to choose between three doors and wins a prize held behind the chosen door. Two doors lead to a goat while a third leads to a car. The outcome given the contestant’s choice is deterministic, but from the contestant’s point of view, the outcome is uncertain.

- <u>Incomplete modeling.</u> When we use a model that must discard some of the information we have observed, the discarded information results in uncertainty in the model’s predictions. For example, suppose we build a robot that can exactly observe the location of every object around it. If the robot discretizes space when predicting the future location of these objects, then the discretization makes the robot immediately become uncertain about the precise position of objects: each object could be anywhere within the discrete cell that it was observed to occupy.

**Examples**

- <u>Tossing a coin or rolling a dice</u>: these kind of experiments are generally impossible to model in a deterministic way. This can be due to our limited ability to model the event (i.e., rolling a dice might be deterministic, but deriving a set of equations to determine the outcome might be too hard).

- <u>Determining if a patient has a given pathology</u>: different pathologies might have similar symptoms. Hence, observing some of them does not allow to determine with perfect accuracy if the patient has that pathology. In this case, uncertainty might arise from incomplete observability.

**Importance of Probability Theory**

Probability theory provides a consistent framework to work with uncertain events.

It allows to quantify and manipulate uncertainty with a set of axioms, as well as to derive new uncertain statements.

Probability theory is hence an important tool to work with data. We will start to revise the main concepts behind probability theory by talking about random variables.

## Random Variable

We discovered that ‘data’ has something to do with ‘variables’. When dealing with uncertain events, we need to use the concept of ‘random variables’. Informally (from wikipedia):

‘A random variable is a variable whose values  
depend on outcomes of a random phenomenon.’

A random variable is characterized by a set of possible values often called ‘<u>probability space</u>’ or ‘<u>alphabet</u>’ (this last term comes from information theory, where we often deal with sources emitting symbols from an alphabet, in which case the values of $X$ will be the symbols).

Random variables can be <u>discrete</u> or <u>continuous</u>. Discrete random variables can assume a finite number (or a countable infinite number) of possible values, whereas a continuous random variable is generally associated with a real number.

A random variable is generally denoted by a <u>capital letter</u>, such as $X$.

Random variables can be <u>scalar</u> (e.g., X=1) or <u>multi-dimensional</u> (e.g., $X = \binom{1}{3}$, or $X = \begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}$).

A random variable is always related to some <u>uncertain phenomenon</u> which generates observations. This is often referred also as ‘experiment’. For instance, if a random variable takes the values of tossing a coin, then ‘tossing a coin’ is the underlying experiment.

**Example – discrete scalar**

- For example, $X$ may denote the outcome of tossing a coin;

- In this context, ‘tossing a coin’ is the random phenomenon characterizing the random variable;

- The space of possible values that $X$ can assume (the alphabet of $X$) can be defined as $\left\{ head,\ tail \right\}$. In this example, $X$ is discrete;

- If tossing the coin, the outcome is $head$, then the variable $X$ assumes the value $X = head$.

**Example – continuous scalar**

- $X$ may denote the height in meters of a student in this class;

- If we pick a student of heigh 1.75m, then $X = 1.75$;

**Example – continuous multi-dimensional**

- $X$ may denote the latitude and longitude coordinates of a car in the world;

- Once we pick a car, we may have $X = \binom{37}{15}$.

### Example

```{figure} /_static/lecture_specific/data_probability/image2.png
```

Let’s assume we have two colored boxes: one red and one blue.

Each box contains two kinds of fruits: apples and oranges.

We consider the experiment of randomly drawing some fruit from one of the two boxes. This happens in two stages:

- We first randomly pick one of the two boxes;

- Then we randomly pick one of the fruits in the box;

- After observing the type of the fruit, we replace it in the same box.

The outcome of the experiment can be characterized by <u>two random variables</u>:

- B represents the color of the box and can take values r (red) and b (blue).

- F represents the kind of fruit and can take values a (apple) and o (orange).

- If we pick an orange from the blue box, then the outcome of the experiment can be characterized by the values $F = o$, $B = b$;

  1.  As per our definition of data, the values $F = o$, $B = b$ are ‘data’. Indeed, they represent a ‘bidimensional data point’ and describe the outcome of an experiment.

      An alternative view of having two random variables, is to have a single multi-dimensional variable $X = \lbrack o,b\rbrack$.

## More Formal Definition of Data

We will define “data” as:

“The values assumed by a random variable”

**Example**

- For instance, if the outcome of tossing a coing is $head$, then $X = head$ <u>is data</u>;

- It should be clear that the ‘data’ is <u>the pair</u> \<random variable, value\> and not just the value. Indeed $head$ alone would not be very useful (we don’t know which phenomenon it is related to), whereas $X = head$ can be useful, as we know that $X$ is the random variable describing the outcome of tossing a coin;

- In this example, the data $X = head$ is representing a fact: ‘I tossed a coin and the outcome was $head$’. This is also called ‘an event’;

**Example**

- We can characterize a tweet with the following random variabiles:

  1.  $X$: its textual content;

      $Y_{1},\ldots,Y_{n}$: the attached images;

      $Z$: the date of publication;

- Once we pick a tweet, we may have:

  1.  $X = "Hello\ world"$;

      $Y_{1} = \begin{pmatrix}
      128 & \cdots & 12 \\
       \vdots & \ddots & \vdots \\
      33 & \cdots & 65 \\
      \end{pmatrix}$ - a matrix representing an attached image;

      $Z = 26/09/2019,\ 15:19$

# Probability

Since random variables are related to stochastic phenomena, we cannot say much about the outcome of a single phenomenon.

However, we expect to be able to characterize the class of experiments related to a random variable, to infer rules on what values the random variable is likely to take.

For instance, in the case of coin tossing, we can observe that, if I toss a coin for a large number of times, the number of heads will be roughly similar to the number of tails.

This kind of observations is useful, as it can give us a prior on what values we are likely to encounter and what are not.

To formally express such rules, we can define the concept of probability on a random variable.

Specifically, it is possible to assign a probability value to a given outcome. This is generally represented with a capital P:

- For instance, $P(B = b)$ represents the probability of picking a blue box in the previous example;

- A probability $P(B = b)$ is a number comprised between 0 and 1 which quantifies how likely we believe the event to be;

  - 0 means impossible;

  - 1 means certain;

When it is clear from the context which variable we are referring to, the probability can also be expressed simply as:

$$P(b) = P(B = b)$$

While it is intuitive to understand that a probability quantifies how likely that an event actually happens, we have not yet seen **how to assign probabilities to outcomes**. We will see that there are two main approaches to reason about probabilities: the frequentist approach and the Bayesian approach.

## Frequentist Approach to Probability

There are two main approaches to probability: frequentist and Bayesian.

**Frequentist approach**:

Probability theory was initially developed to analyze the frequency of events. For instance, it can be used to study events like drawing a certain hand of cards in a poker game. These events are repeatable and can be dealt with using frequencies. In this sense, when we say that an event has probability $p$ of occurring, it means that if we repeat the experiment infinitely many times, then a proportion $p$ of the repetitions would result in that outcome.

According to the frequentist approach, we can estimate probabilities by repeating an experiment for a large number of times and then computing:

- The number of trials: how many times we performed the experiment;

- The number of favorable outcomes: how many times the outcome of the experiment was favorable.

The probability is hence obtained by dividing the number of favorable outcomes by the number of trials.

For instance, let’s suppose we want to estimate the probability of obtaining a ‘head’ by tossing a coin. Let’s suppose we toss the coin 1000 times and obtain 499 heads and 501 tails. We can compute the probability of obtaining head as follows:

- Number of trials: 1000;

- Number of favorable outcomes: 499.

The probability of obtaining head will be 499/1000=0.49

**Examples:**

- The probability of obtaining ‘head’ when tossing a coin is 0.5. We know that because, if we toss a coin for a large number of times, about half of the times, we will obtain ‘head’;

- The probability of picking a red ball from a box with 40 red balls and 60 blue balls is 0.4. We know this because, if we repeat the experiment for a large number of times, we will observe that proportion.

### Example of Probability

```{figure} /_static/lecture_specific/data_probability/image3.png
```

Suppose we repeat this experiment for many times and observe that:

- We pick the red box 40% of the times;

- We pick the blue box 60% of the times;

- Once we selected a box, we are equally likely to select any of the fruits contained in it.

Using a frequentist approach, we can define the probabilities:

- $P(B = b) = \frac{6}{10}$

- $P(B = r) = \frac{4}{10}$

- This is done by using the formula:

  1.  $P(X = x) = \frac{\#\ of\ times\ X = x}{\#\ trials}$

## Joint probability

We can define **univariate** (= with respect to only one variable) probabilities $P(B)$ and $P(F)$ as we have seen in the previous examples.

However, in some cases, it is useful to define probabilities on more than one variable at the time. For instance, we could be interested in studying the probability of picking a given fruit from a given box. In this case, we would be interested in the **joint probability** $P(B,F)$.

In general, we can have joint probabilities with arbitrary numbers of variable. For instance, $P\left( X_{1},X_{2},X_{3},\ldots,X_{n} \right)$.

Joint probabilities are symmetric, i.e., $P(X,Y) = P(Y,X)$.

We should note that, when dealing with multiple unidimensional variables, we can always define a new multi-variate variable comprising all of them:

- $X = \left\lbrack X_{1},X_{2} \right\rbrack;$

- $P(X) = P\left( X_{1},X_{2} \right)$.

### Example

```{figure} /_static/lecture_specific/data_probability/image4.png
```

We can see the concept of joint probability in the context of the examples of the two boxes;

We have seen how to define the univariate probability $P(B)$ over the whole probability space of $B$;

However, we could be interested in the probability of both variables jointly: $P(B,F)$, i.e., the joint probability of B and F.

To ‘measure’ the joint probability, we could repeat the experiment for many times and observe the outcomes.

We could then build a ‘contingency table’ which keeps track of how many times we observed a given combination.

In the slide, we show an example for two general random variables $X$ and $Y$ (they could be B and F):

- $n_{ij}$ represents the number of times we observed $X = x_{i}$ and $Y = y_{j}$;
- $c_{i}$ represents the number of times $X$ assumed the value $x_{i}$, independently from the value assumed by $Y$;
- $r_{j}$ represents the number of times $Y$ assumed the value $y_{j}$, independently from the value assumed by $X$;

We can measure the joint probability $P(X = x_{i},Y = y_{j})$ with a frequentist approach using the formula:

$$P\left( X = x_{i},\ Y = y_{j} \right) = \frac{n_{ij}}{N}$$

where $N$ is the total number of trials (i.e., the sum of all the values in the matrix).

Also, we note that we can define the probabilities of X and Y as follow:

- $P\left( X = x_{i} \right) = \frac{c_{i}}{N}$

- $P\left( Y = y_{j} \right) = \frac{r_{j}}{N}$

## Sum Rule (Marginal Probability)

Sometimes we can compute probabilities on a set of variables, but we are interested on a probability on a subset of them.

In particular, we have seen that, given the contingency table related to the two variables X and Y, we can estimate both the joint probability $P(X,Y)$ and the probability of each of the variables: $P(X)$ and $P(Y)$.

To compute these probabilities, we can use the **sum rule of probability**:

$$P(X = x) = \sum_{y}^{}{P(X = x,Y = y)}$$

The act of computing $P(X)$ from $P(X,Y)$ is also known as marginalization and $P(X)$ is also named **marginal probability**.

### Frequentist Derivation

```{figure} /_static/lecture_specific/data_probability/image5.png
```

We can see how the sum rule of probability can be derived from the simple example of the contingency table seen before;

Indeed, given the contingency table between variables X and Y, we have:

- $c_{i} = \sum_{j}^{}n_{ij}$: the number of trials in which $X = x_{i}$ is obtained by summing the numbers in the i-th colum;

- $r_{j} = \sum_{i}^{}n_{ij}$: the number of trials in which $Y = y_{j}$ is obtained by summing th enumbers in the j-th row;

Therefore:

- $P\left( X = x_{i} \right) = \frac{c_{i}}{N} = \frac{\sum_{j}^{}n_{ij}}{N} = \sum_{j}^{}\frac{n_{ij}}{N} = \sum_{j}^{}{P(X = x_{i},\ Y = y_{j})}$;

- $P\left( Y = y_{i} \right) = \frac{r_{j}}{N} = \frac{\sum_{i}^{}n_{ij}}{N} = \sum_{i}^{}\frac{n_{ij}}{N} = \sum_{i}^{}{P(X = x_{i},\ Y = y_{j})}$;

## Conditional Probability

In many cases, we are interested in the the probability of some event, given that some other event happened.

This is called **conditional** **probability** and is denoted as$\ P\left( X = x \middle| Y = y \right)$ and read as ‘P of X=y given that Y=y’. In this context, $Y = y$ is the condition, and we are interested in studying the probability of X only in the cases in which the condition is verified.

For instance, in the case of the two boxes, we could be interested in $P(F = a|B = b)$, that is to say, what is the probability of picking an apple, given that we know that we are drawing from the blue box?

It should be noted that, in general $P\left( X \middle| Y \right) \neq P(X)$.

We can define the conditional probability as follows:

$$P\left( X = x \middle| Y = y \right) = \frac{P(X = x,\ Y = y)}{P(Y = y)}$$

The conditional probability is defined only when $P(Y = y) > 0$, that is, we cannot define a probability conditioned on an event that never happens.

In terms of sets, this can be seen as follows:

$$P\left( A \middle| B \right) = \frac{P(A \cap B)}{P(B)}$$

Where $P(A \cap B)$ measures the probability that events A and B happen together, whereas $P(B)$ represents the probability that B happens alone. The probability $P(A|B)$ measures how likely it is that A happens, knowing that B has happened. We can see this graphically in terms of sets as follows:

```{figure} /_static/lecture_specific/data_probability/image6.png
```

## Product Rule (Factorization)

We can see the definition of conditional probability:

$$P\left( X = x \middle| Y = y \right) = \frac{P(X = x,\ Y = y)}{P(Y = y)}$$

As follows:

$$P(X = x,Y = y) = P\left( X = x \middle| Y = y \right)P(Y = y)$$

which is often referred to as **the product rule**.

The product rule allows to compute joint probabilities starting from conditional probabilities and marginal probabilities. This is useful because measuring joint probabilities generally involves creating large tables, whereas conditional and marginal probabilities might be easier to derive.

This operation of expressing a joint probability in terms of two factors is known as <u>factorization</u>.

### Frequentist Derivation

```{figure} /_static/lecture_specific/data_probability/image7.png
```

Also in this case, we can derive the product rule from our example;

In particular, the conditional probability $P(X = x_{i}|Y = y_{j})$ can be computed as follows in a frequentist way:

$$P\left( X = x_{i} \middle| Y = y_{j} \right) = \frac{n_{ij}}{r_{j}}$$

Since we are restricting our probabilities to the cases in which $Y = y_{j}$, the total number of trials to be consider, is the number of trials in which $Y = y_{j}$, which is $r_{j}$;

We note that:

$$P\left( X = x_{i},Y = y_{j} \right) = \frac{n_{ij}}{N} = \frac{n_{ij}}{r_{j}} \cdot \frac{r_{j}}{N} = P\left( X = x_{i} \middle| Y = y_{j} \right)P(Y = y_{i})$$

## The Fundamental Rules of Probability

```{figure} /_static/lecture_specific/data_probability/image8.png
```

To summarize, there are two fundamental rules of probability:

- Sum rule: allows to perform marginalization;

- Product rule: allows to factorize probability (i.e., breaking them into factors);

These two rules are the foundations of the framework of probability and allow to reason about random variables and uncertain statements.

All other rules and theorems (including Bayes’ rule) are derived from these two statements.

## The Chain Rule of Conditional Probabilities

When dealing with multiple variables, the product rule can be applied in an iterative fashion, thus obtaining the ‘chain rule’ of conditional probabilities.

For instance:

$$P(X,Y,Z) = P\left( X \middle| Y,Z \right)P(Y,Z)$$

Since:

$$P(Y,Z) = P\left( Y \middle| Z \right)P(Z)$$

We obtain:

$$P(X,Y,Z) = P\left( X \middle| Y,Z \right)P\left( Y \middle| Z \right)P(Z)$$

Since joint probabilities are symmetric, we could equally obtain:

$$P(X,Y,Z) = P\left( Z \middle| Y,X \right)P\left( Y \middle| X \right)P(X)$$

This rule can be formalized as follows:

$$P\left( X_{1},\ldots,\ X_{n} \right) = P\left( X_{1} \right)\prod_{i = 2}^{n}{P(X_{i}|X_{1},\ldots,\ X_{i - 1})}$$

## Bayes’ Theorem

Given two variables A and B, from the product rule, we obtain:

- $P(A,B) = P\left( A \middle| B \right)P(B)$

- $P(B,A) = P\left( B \middle| A \right)P(A)$

Since joint probabilities are symmetric, we have:

$$P(A,B) = P(B,A) \rightarrow P\left( A \middle| B \right)P(B) = P\left( B \middle| A \right)P(A)$$

Which implies:

> $P\left( A \middle| B \right) = \frac{P\left( B \middle| A \right)P(A)}{P(B)}$;

This last expression is known as Bayes’ Theorem (or Bayes’ rule).

Using the sum rule, the denominator can be seen in terms of the quantities appearing in the numerator:

- $P(B) = \sum_{A}^{}{P(}B|A)P(A)$

- We can see the denominator as a normalization constant required to make sure that $P(A|B)$ is a valid probability.

The Bayes’ rule can be used to ‘invert’ conditional proabilities, i.e., to turn probabilities of the kind $P(A|B)$ into probabilities of the kind $P(B|A)$;

The different terms on the Bayes’ rule have names:

- $P(A)$ is called ‘the prior’;

- $P(B|A)$ is called ‘the likelihood’;

- $P(B)$ is called ‘the evidence’;

- $P(A|B)$ is called ‘the posterior’;

- We will get back to these names with examples in the following slides.

### Bayesian Approach to Probability

Some events are not related to repeatable experiments, but they are still characterized by uncertainty. Examples of such events are ‘will the sun extinguish in 4.5 billion years?’ or ‘given the observation of some symptoms, does the patient have a given pathology’. These events are not related to repeatable experiments. Yet, they are characterized by uncertainty. Also, observing more data might help reduce uncertainty. For instance, if a new symptom is observed, we might be less uncertain about one outcome or another.

**  
Examples:**

- The probability of a patient to have a flu given the observation of their temperature;

- The probability that the average temperature of the planet will increase by 1° next year if we reduce the emission of CO2 by a given amount

#### Degree of belief

An important concept related to Bayesian probability is the one of “degree of belief”. Since the experiments are not repeatable, to quantify probability we cannot count the number of favorable outcomes. Instead, we ‘inject’ our belief into the system. Specifically, this is done using the Bayes’ rule, which provide the tools to insert our degree of belief in a consistent way. We will talk about the Bayes’ rule later.

**Example:**

Let’s suppose we toss a coin three times and we obtain three heads. Now, three is not a large number and hence, if we try to apply the frequentist approach, we wrongly estimate that the probability of getting head is 1, while the probability of getting tail is zero. By using the Bayesian approach, we can insert our belief that the coin is fair by introducing a “prior probability” that the probability of getting head is 0.5.

## Example of Probability Manipulation

```{figure} /_static/lecture_specific/data_probability/image9.png
```

Let’s get back to our example of the two boxes and let’s suppose that, by repeating several trials, we discovered the following probabilities (in a frequentist way):

- $P(B = r) = \frac{4}{10}$

- $P(B = b) = \frac{6}{10}$

We also focused on a given box and performed different trials, observing the following proportions:

- $P\left( F = a \middle| B = r \right) = \frac{1}{4}$

- $P\left( F = o \middle| B = r \right) = \frac{3}{4}$

- $P\left( F = a \middle| B = b \right) = \frac{3}{4}$

- $P\left( F = o \middle| B = b \right) = \frac{1}{4}$

We shall note that these probabilities are normalized such that:

- $P(B = r) + P(B = b) = 1$

- $P\left( F = a \middle| B = r \right) + P\left( F = o \middle| B = r \right) = 1$

- $P\left( F = a \middle| B = b \right) + P\left( F = o \middle| B = b \right) = 1$

We can now use the rules we have seen before to answer questions such as:

1.  What is the overall probability of choosing an apple?

    What is the probability of picking a red box, given that we have drawn an orange?

**What is the overall probability of choosing an apple?**

To answer this question, we need to find $P(F = a)$. We note that, by the sum rule:

$$P(F = a) = P(F = a,B = b) + P(F = a,B = r)$$

We also observe that the joint probabilities can be recovered using the product rule:

$$P(F = a,B = b) = P\left( F = a \middle| B = b \right)P(B = b)$$

$$P(F = a,B = r) = P\left( F = a \middle| B = r \right)P(B = r)$$

Hence, our probability can be found using the formula:

$$P(F = a) = P\left( F = a \middle| B = b \right)P(B = b) + P\left( F = a \middle| B = r \right)P(B = r) =$$

$$= \frac{3}{4} \cdot \frac{6}{10} + \frac{1}{4} \cdot \frac{4}{10} = \frac{18 + 4}{40} = \frac{22}{40} = \frac{11}{20}$$

From the definition of probability, we have:

$$P(F = a) + P(F = o) = 1$$

Hence:

$$P(F = o) = 1 - P(F = a) = 1 - \frac{11}{20} = \frac{9}{20}$$

**What is the probability of picking a red box, given that we have drawn an orange?**

To answer this question, we need to find the conditional probability $P(B = r|F = o)$. To find this probability, we need to ‘invert’ our conditional probabilities using the Bayes’ rule:

$$P\left( B = r \middle| F = o \right) = \frac{P\left( F = o \middle| B = r \right)P(B = r)}{P(F = o)} = \frac{\frac{3}{4} \cdot \frac{4}{10}}{\frac{9}{20}} = \frac{12}{40} \cdot \frac{20}{9} = \frac{6}{9} = \frac{2}{3}$$

**Interpretation of Bayes’ rule:**

We can give the following interpretation of Bayes’ rule. If somebody asked us what is probability of picking the red box, we would have said it is $P(B = r) = \frac{4}{10}$. We call this ‘prior probability’ as it is our **best guess given that no additional constrain is provided**. Once we are told that we have picked an orange, our **belief** on the identity of the box can be refined. In particular, we know that the red box contains more oranges than the blue one, so we should assign probabilities accordingly. We use the Bayes’ theorem to obtain the conditional probability $P(B = r|F = o)$ as done above. We call this the ‘posterior probability’, as this is our updated estimate, once we know the identity of the fruit. To refine our guess, we use the ‘likelihood’ $P(F = o|B = r)$ which tells us how many oranges are in the red box and the ‘evidence’ $P(F = o)$ which tells us how many oranges there are at all.

### Excercise

Suppose that we have three colored boxes r (red), b (blue), and g (green). Box r contains 3 apples, 4 oranges, and 3 limes, box b contains 1 apple, 1 orange, and 0 limes, and box g contains 3 apples, 3 oranges, and 4 limes. If a box is chosen at random with probabilities P(r)=0.2, P(b)=0.2, P(g)=0.6, and a piece of fruit is extracted from the box (with equal probability of selecting any of the items in the box), then what is the probability of selecting an apple? If we observe that the selected fruit is in fact an orange, what is the probability that it came from the green box?

## Independence and Conditional Independence

**Independence**

Two variables $X$ and $Y$ are **said to be independent** if and only if:

$$P(X,Y) = P(X)P(Y)$$

It should be noted that the expression above **is generally not true** as we cannot always assume that two variables are independent.

Independence can be denoted as:

$$X\bot Y$$

**Examples**

Intuitively, two variables are independent if the values of one of them do not affect the values of the other one:

- Weight and height of a person are **not independent**. Indeed, taller people are usually heavier;

- Height and richness are **independent**, as the richness does not depend on the height of a person;

**Conditional independence**

Two random variales $X$ and $Y$ are said to be **conditionally independent** given a random variable $Z$ if:

$$P\left( X,Y \middle| Z \right) = P\left( X \middle| Z \right)P\left( Y \middle| Z \right)$$

Conditional independence can be denoted as:

$$X\bot Y\ |\ Z$$

**Example**

- Height and vocabulary are not independent: taller people are usually older, and hence they have a more sophisticated vocabulary (they know more words). However, if we condition on age, they become independent. Indeed, among people of the same age, height should not influence vocabulary. Hence, height and vocabulary are **conditionally independent** with respect to age;

## References

- Parts of chapter 1 of \[1\];

- Most of chapter 3 of \[2\];

- Some parts of chapter 1 of \[3\].

\[1\] Bishop, Christopher M. *Pattern recognition and machine learning*. springer, 2006. <https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf>

\[2\] Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. *Deep learning*. MIT press, 2016. <https://www.deeplearningbook.org/>

\[3\] Cover, Thomas M., and Joy A. Thomas. *Elements of information theory*. John Wiley & Sons, 2012.
