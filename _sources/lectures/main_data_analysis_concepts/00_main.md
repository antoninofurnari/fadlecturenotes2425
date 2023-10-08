# Main data analysis concepts
In this lecture, we will consider the main data analysis concepts.

## Observations, Populations, Samples

We will see three fundamental concepts: observations, populations, samples.

### Observations
We will call observations, the units by which we measure data. These could be persons, cars, animals, plants, etc. We often indicate an observation as $x$. Please consider these as "abstract" entities, not necessarily numerical observations. E.g., "let's consider a person $x$".

### Population
When we study a given phenomenon, we will be interested in a set of observations, which is called a "population". For instance:
* if we want to study the distribution of heights of people in the world, we will need to look at the population of all people in the world.
* if we want to study the age of people attending a computer science course in Italy, then we need to look at the population of all students of computer science courses in Italy.

Note that a population can sometimes be a theoretical concept and identify sets of elements which are not even finite. E.g., *"all movies which will ever be filmed"*.

We can denote a population with the symbol $\Omega$. Al our observations will be $\omega \in \Omega$.

### Sample
In practice, working with population can be very hard, as it is not always possible to obtain observations from those large sets. Intuitively, in practice, working on a large enough set of observations from a population could be good enough. We refer to a subset of a population as "a sample": $\{\omega^{(1)}, \omega^{(2)}, \ldots, \omega^{(n)}\} \subseteq \Omega$.

### Example
We want to study how the height of people in the world changed in the years. Here the **population** $\Omega$ is the set of people ever existed on earth, a **sample** $\{\omega^{(1)},\ldots,\omega^{(n)}\} \subseteq \Omega$ is a subset of people for which we have some data (e.g., say we measured height of many people in most countries since the 16th century). An observation is a person $\omega^{(i)}$.

## Variables
We have identified our problem, defined a suitable population and identified a sample of observations. While observations are abstract concepts such as "a person" or "a student", we usually want to capture specific features of such observations, such as "the person's age" or "the student's height". We collect these features by means of **statistical variables**.

We may also be interested in different features of an observation. For instance, for each person in a population, we may want to record their age, gender, and height. We can introduce a variable to capture each of these features. For instance, given observation $\omega$, we may obtain "height = 180cm", "weight=80Kg", "gender=male".

Formally, we'll define a variable $X$ as:

$$X : \Omega \to S$$
$$ \omega \mapsto x$$

Where $S$ is the set of possible values for variable $X$. The definition above specifies that a variable maps an abstract observation $\omega$ to some (possibly more concrete) value $x \in S$.

### Example
Given the population of all people currently living in the world $\Omega$, we define a variable $H$ to collect the heights of the observed people $\omega$:

$$H : \Omega \to \mathbb{R}$$
$$ \omega \mapsto h $$

Given an observation $\omega^{(1)}$, we may obtain $H(\omega)=180$. We often say that $H$ assumes the value $180$ and write: $H=180$.


### Quantitative and Qualitative
Variables can be of two main kinds:

* **Qualitative**: represent properties that can be observed and cannot generally be measured with a numerical value (e.g., ‘color’, ‘sex’);

* **Quantitative**: represent properties that can be quantified with a number (e.g., ‘height’, ‘weight’, ‘age’).

### Discrete and Continuous
Variables can also be discrete or continues:

* **Discrete variables** can assume a finite number (or a countable infinite number) of possible values
* **Continuous variable** assume a continuous, infinite number of values, which can be generally denoted with real numbers

### Scalar and Multi-Dimensional

Variables can be:

* **scalar** or uni-dimensional: they assume real numbers (e.g., $X=1$)
* **multi-dimensional**: they assume vector or matrix values, (e.g., $X = \binom{1}{3}$, or $X = \begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}$).

### Examples

Let's see some examples:

#### Discrete Scalar Variables

We want to assess if a coin is fair or not. 
* We consider as population all possible tosses of that coin.
* An observation will be a specific tossing.
* A discrete scalar variable $X$ may record the outcome of a given tossing. The set of possible values will be $S=\{head,\ tail\}$ (discrete values). The variable is scalar as it will contain a single value.
* If we toss a coin, we may get $X=tail$.

#### Continuous Scalar Variables

We want to study the heights in centimeters of students in this class.
* Our population is the set of all students in this class.
* We can use a continuous scalar variable $X$ to record the heights of the students. In this case, we can choose $S=\mathbb{R}_+$.
* If we pick a student, we may get $X=175$.

#### Continuous Multi-Dimensional Variables

We want to study the positions of all cars in the world.
* Our population is the set of all cars in the world.
* We could use the variable $X$ to denote the latitude and longitude coordinates of a car in the world. The set of possible values may be $S=\mathbb{R}^2$.
* Once we pick a car, we may have $X = \binom{37}{15}$.

### Scales
The values of the variables can sometimes be ordered. For instance, we can say that a student is taller than another one. In other cases, an order is not possible. For instance, it may not be meaningful to order students by color of the eyes or gender. We can classify whether and how a variable can be sorted using scales. Variables can be characterized with respect to the following scales:

* **Nominal scale**: nominal variables cannot be ordered. Examples are the gender of a person and the color of the eyes.
* **Ordinal scale**: ordinal variables can be ordered, but the difference between two ordinal variables is usually not meaningful. For instance, we may have the following scale to classify the level of expertise of a basketball player: *novice, amateur, intermediate, expert*. While this scale allows to meaningful sort players, the difference between two levels may not be meaningful.
* **Continuous scale**: continuous variables are generally expressed with real numbers and can be ordered. For instance, the *height of people* and the *amount of money in the bank account* are examples of continuous variables.

## Data Collection

Data collection is the crucial first step in the data analysis process. It involves gathering observations that will serve as the foundation for all subsequent analysis. The methods of data collection can vary widely depending on the goals of the analysis, the type of data required, and available resources. 

### Survey

Surveys are a common method of data collection used to gather information from individuals or groups. They involve asking specific questions to respondents, often in a structured format. Surveys can be conducted through various means, such as paper questionnaires, online forms, telephone interviews, or in-person interviews. Surveys are particularly useful when seeking opinions, attitudes, preferences, or demographic information from a target population.

Key characteristics of surveys:
- Structured and standardized questions.
- Can be administered in various formats.
- Allow for quantifiable responses.

### Experiments

Another way to collect data is through experiments. These allow to collect data in a **controlled** way and they are usually employed to establish cause-and-effect relationships between variables. In an experiment, researchers manipulate one or more independent variables to observe their effects on dependent variables. Experiments are characterized by their ability to provide evidence of causation, which is a significant advantage in many scientific and practical applications. 

The most common form of experiments for data collection are **randomized controlled experiments** (or randomized controlled trials), which have the following characteristics:
- Controlled manipulation of variables.
- Random assignment of participants (in randomized experiments).
- Replicability to test hypotheses.

#### Randomized Controlled Experiments - Example
We want to test whether a given drug is effective in treating a disease. We will consider a suitable population (e.g., all people affected by the disease), obtain a suitable sample (a random set of people, diverse by age, gender and health conditions) and set up an experiment in which half of the people take the drug, while the remaining half take a placebo. The assignment are **randomized** to avoid any bias in the data. We will discuss this better when we'll talk of causal inference.


### Observational Data
Observational data collection involves the passive recording of information as it naturally occurs, without any interference or manipulation by the researcher. This method is commonly used when experiments are not feasible, ethical, or practical. For instance, if we want to affect the effects of smoke on young people, it would be unethical to ask people to smoke. Observational studies can be valuable for exploring patterns, relationships, and behaviors in real-world settings.

Key characteristics of observational data:
- No direct manipulation of variables.
- Captures data as it naturally occurs.
- Useful for studying complex, uncontrolled environments.

### Primary and Secondary Data

Data can be classified into two main categories: primary and secondary.

- **Primary Data:** This type of data is collected firsthand by researchers for a specific purpose. Primary data collection methods include surveys, experiments, interviews, and observations. Primary data is original and tailored to the research objectives.

- **Secondary Data:** Secondary data is pre-existing data collected for purposes other than the current research. Researchers can obtain secondary data from sources such as government agencies, academic studies, industry reports, and databases. Secondary data can be a valuable resource for cost-effective research and historical analysis.

## Data Sets, Design Matrix, and Features
As we have already seen, data is usually organized in a tabular format for convenience. The "table" structure is often called a **data matrix** or a **design matrix**. In this format, each column of the matrix represents a variable, which is often also referred to as a **feature**, while each row is a different observation.

We have already seen an example of dataset, which we'll report in the following:

|ID|Maths | Geography | English | Physics | Chemistry |
|-|-|-|-|-|-|
|x001|8|9|30|8|10|
|x038|9|7|27|6||
|x002|6|-1|18|5|6|
|x012|7|7|25|4|10|
|x042|10|10|30|10|10|

Note that we can also see each row of this matrix as a multi-dimensional variable (a vector) summarizing the main properties of the observations. Indeed, in the example above, each student is a different observation, while their grades in different subjects are the different **features** and each row can be seen as a **feature vector**.

## References
* Chapter 1 of *Heumann, Christian, and Michael Schomaker Shalabh. Introduction to statistics and data analysis. Springer International Publishing Switzerland, 2016.*