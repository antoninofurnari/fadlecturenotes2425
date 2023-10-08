# What is Data? An informal Definition
We will start by giving an informal definition of data. It is not by any means a complete definition, but it will suffice as a starting point to get an intuitive understanding of what data is:

>Data is a **set of values** **collected** with respect to some **variables** which describe a given **phenomenon**.

In the definition above, we mentioned some key concepts, which are discussed in the following sections.

## Set of Values
Data is a "set of values", in the sense that, when we deal with data, we actually deal with *multiple instances* of values associated to the same event or phenomenon. Examples:

|Example|Comment|
|-|-|
|We want to study how the heights of students change with the years| We need sets of recorded heights, not just one height|
|We want to study how a given drug affects the recovering from a disease | We need to record sets of values about drug assumption and recover, just one case will not be enough|
|We need to create a system which can generate text from a prompt | We need to record several examples of prompt-text generation, just one would not be enough to study how such generation should be made|

Since we deal with sets of values, we will often use the term **dataset** to refer to a given collection of data related to a given phenomenon.

## Data collection
Data is always collected in some way. This is important to consider, as the collection process may introduce some form of bias or error. While we will get back later on how data can be collected, popular ways to collect data include **surveys** (asking questions to people) and **physical measurements** (e.g., physically measuring the heights of people). Note that both collection methods (though these are not the only possible) may bring their own source of error. Indeed, **people may lie** or report incorrect information, while our **measurement tools** may be flawed or have a **limited precision**. In all cases, **imperfect data** due to the way it has been collected is part of the game (we cannot expert perfect data). We often say that we "observe" data. This is a broader therm to say that we do not come up with data, but it comes from some external source we are interested it (hence we collect it). Hence, we often refer to a given value we deal with as an **observation**. For instance, the height of a single person in the classroom can be called an observation.

## Variables
The values we collect are associated to abstract entities which we will call "variables". Again, we will get to a more formal definition later. For the moment, consider that these entities are **similar to the mathematical variables** we are used to or to the variables we encounter in many **programming languages**. We could see them as "containers" for the data, but also, and more importantly, as **abstract entities defining which data they are expected to hold**. 

### Example - Mathematical Variables
For instance, if we are solving a geometric problem, such as **computing the area of a triangle**, we may define a variable $h$ which will be responsible for "containing" the value of the height of the triangle. We can then define a variable $b$, which will hold the value for the base. We can hence solve the problem of computing the area of the triangle by using the formula 

$$a=\frac{b\cdot h}{2}$$

where $a$ is an additional variable which will "hold" the value of the area. Note that we can observe different triangles and assign different values to each variable every time, but we always expect $b$ to contain the length of the base, $h$ to contain the height, and $a$ to contain the area. If we weren't to do so, the formula above would be useless. 

### Example - Programming Variables
Similarly, if we create a computer program to solve the same problem, we will probably define three double variables with the same names and expect them to always contain values coherent with the ones we had in mind when we defined such variabile:

```c
double b;
double h;
double a;

input(&b, &h);

a = (b*h)/2;
```

### Example - Statistical Variables
In a very similar way, when analyzing data, **we will define variables expected to contain values related to a specific event or phenomenon**. For instance, we may define a **statistical variable** $H$ to contain the value of the height of people in the class. We often have **more than one variable** in a data analysis problem. This is useful when we want to **measure or analyze more than one aspect** of the problem we are considering. For instance, we may want to measure both the height and weight of people in the class. In that case, we could also introduce an **additional statistical variable** $W$ which will contain the values of the weight of people. We may later (as we will see) **ask questions** on how the values of the two variables are somehow related. 

When we have more than one variable related to different aspects of the same event (e.g., height and weight, where the "event" is observing a given person in the classroom), we will say that the set of values related to the given variables is **an observation**. For instance the pair of values $(H,W)=(175cm, 68Kg)$ can be seen as an observation. Since this pair of values can be represented as a point in a 2D space, we also call it a **data point**. In this context, a set of observations (e.g., heights and weights of 30 people) is generally called a **dataset**.

For example, the graph below represents four observations related to the following measurements of six different subjects:

|Subject|Height (cm)|Weight (Kg)|
|-|-|-|
|1|175|70|
|2|160|60|
|3|180|78|
|4|160|75|
|5|155|58|
|6|190|110|


![](/_static/lecture_specific/intro_data_analysis/datapoint.png)

## Phenomenon
When we analyze data, we are usually interested in **investigating some phenomenon**. For instance, we may be curious of **what is the rate of overweight students in a school**. This can be useful, e.g., to understand whether a new diet proposed in the school canteen is generating good or bad consequences. The phenomenon we want to study is important to keep in mind when collecting and analyzing data, as an inappropriate data collection could create some bias or make our conclusions limited. For instance, **if we collected only data of male subjects**, we may not be able to fully understand the problem we am considering.

## An example of a dataset
Before closing our brief discussion of what data is, it is worth mentioning that datasets are usually stored in tables in which **columns represent the different variables** and **rows represent the different observations**. If you have ever had a look at a spreadsheet, you probably already see an example of a dataset!

Let's conside the following example of a dataset of marks of $5$ subjects obtained by three students:


||Maths | Geography | English | Physics | Chemistry |
|-|-|-|-|-|-|
|x001|8|9|30|8|10|
|x038|9|7|27|6||
|x002|6|-1|18|5|6|
|x012|7|7|25|4|10|
|x042|10|10|30|10|10|

Each row is an **observation** related to a given student, while each column represents a different **variable** (the marks obtained in the different courses).

Before moving on, think for a moment what you could do with a dataset like this (maybe imagine a larger one):

* You could take the average of all marks obtained by a student (average by rows) to get a ranking of the students. This could be useful to understand which students may need help.
* You could compute the average of the votes obtained in each course (average by column) to identify the subjects which are "more difficult" for the students than others.
* You could group the courses into humanity-based and science-based to identify which students excel in each field.

The examples above are all (very simple) examples of data analysis. As you can see, even with a simple dataset like this and no knowledge of complex notions of data analysis, we can already do a lot of analysis.