# Probability Distributions

We have seen how it is possible to assign a probability value to a given
outcome of a random variable.

In practice, it is often useful to assign probability values to **all
the values** that the random variable can assume.

To do so, we can define a **function**, which we will call **probability
distribution** which assigns a probability value to each of the possible
values of a random variable.

In the case of discrete variables, we will talk about "**probability
mass functions**", whereas in the case of continuous variable, we will
refer to "**probability density functions**".

A probability distribution characterizes the random variable and defines
which outcomes it is more likely to observe.

Once we find that a given random variable $X$ is characterized by a
probability distirbution $P(X)$, we can say that **"X follows P"** and
write:

$$X \sim P$$

## Probability Mass Functions (PMF) -- Discrete Variables

If $X$ is discrete, $P(X)$ is called a "probability mass function"
(PMF). $P$ maps the values of $X$ to real numbers indicating whether a
given value is more or less likely.

A PMF on a random variable $X$ is a function

$$P:\chi \rightarrow \lbrack 0,1\rbrack$$

Where $\chi$ is the alphabet of $X$.

This function satisfies the following properties:

-   **The domain of** $\mathbf{P}$ **is the set of all possible states
    of** $\mathbf{X}$**.**

-   $\mathbf{\forall}\mathbf{x}\mathbf{\in}\chi\mathbf{,\ }\mathbf{0}\mathbf{\leq}\mathbf{P}\left( \mathbf{x} \right)\mathbf{\leq}\mathbf{1}$.
    An impossible event has probability 0, whereas a certain event has
    probability 1. No event can have negative probability or probability
    larger than 1.

-   $\sum_{\mathbf{x}\mathbf{\in}\mathbf{\chi}}^{}{\mathbf{P}\mathbf{(}\mathbf{x}\mathbf{)}}\mathbf{=}\mathbf{1}$.
    The sum of the probabilities associated to all possible events must
    be one. This implies that the probability distribution is
    normalized. Also, this means that at least one of the events should
    happen.

**Example:** Let $X$ be the random variable indicating the outcome of a
coin toss.

-   The space of all possible functions (the domain of $P(X)$) is
    $\{ head,\ tail\}$.

-   The probabilities $P(head)$ and $P(tail)$ must be larger than or
    equal to zero and smaller than or equal to 1.

-   Also, $P(head) + P(tail) = 1\ $. This is obvious, as one of the two
    outcomes will always happen. Indeed, if we had $P(tail) = 0.3$, this
    would mean that, 30 times out of 100 times we toss a coin, the
    outcome will be tail. What will happen in all other cases? The
    outcome will be head, hence, $P(head)$, so $P(head) + P(tail) = 1$.

-   In the case of a fair coin, we can characterize $P(X)$ as a
    "discrete uniform distribution", i.e., a distribution which maps any
    value $x \in X$ to a constant, such that the properties of the
    probability mass functions are satisfied.

-   If we have $N$ possible outcomes, the discrete uniform probability
    will be $P(X = x) = \frac{1}{N}$ , which means that all outcomes
    have the same probability.

-   This definition satisfies the constraints. Indeed,
    $\frac{1}{N} \geq 0,\ \forall N$ and
    $\sum_{i}^{}{P\left( X = x_{i} \right)} = 1$.

### Example: Probability Mass Function for a Fair Coin

A probability mass function can be plotted as a 2D diagram where the
values of the function ($P(x)$) is plotted against the values of the
independent variable $x$. This is the diagram associated to the PMF of
the previous example, where $P(head) = P(tail) = 0.5$.

![](./media/image1.png){width="6.6930555555555555in"
height="4.461805555555555in"}

### Example: Probability Mass Function for a Skewed Coin

Now suppose we tossed our coin for 10000 times and discovered that 6000
times the outcome was "head", whereas 4000 times it was "tail". We
deduce the coin is not fair.

Using a **frequentist** approach, we can manually assign values to our
PMF using the general formula:

$$P(x) = \frac{\# trials\ in\ which\ X = x}{\#\ trials}$$

That is, in our case:

$$P(head) = \frac{6000}{10000} = 0.6;P(tail) = \frac{4000}{10000} = 0.4$$

We shall note that the probability we just defined satisfies all
properties of probabilities, i.e.:

-   $0 \leq P(x) \leq 1\ \forall x$

-   $\sum_{x}^{}{P(x) = 1}.$

![](./media/image2.png){width="6.6930555555555555in" height="4.4625in"}

### Exercise: Probability Mass Function

Let $X$ be a random variable representing the outcome of rolling a fair
dice with $6$ faces:

-   What is the space of possible values of $X$?

-   What is its cardinality?

-   What is the associated probability mass function $P(X)$?

-   Suppose the dice is not fair and $P(X = 1) = 0.2$, whereas all other
    outcomes are equally probable. What is the probability mass function
    of $P(X)$?

-   Draw the PMF obtained for the dice.

## Probability Density Functions (PDF) -- Continuous Variables

Probability distributions are called "probability density functions"
when the random variable is continuous.

To be a probability density function over a variable $X$, a function
$P:\chi \rightarrow \lbrack 0,1\rbrack$ must satisfy the following
properties:

-   The domain of P is the set of all possible values of $X$.

-   $\forall x \in \chi,\ P(x) \geq 0$. No probability can be negative.

-   $\int P(x)dx = 1$. This is equivalent to $\sum P(x) = 1\ $in the
    case of discrete variable. The sum turns into an integral in the
    case of continuous variables.

**Example**

-   Let us consider a random number generator which outputs numbers
    comprised between $a$ and $b$.

-   Let $X$ be a random variable assuming the values generated by the
    random number generator.

-   The PDF of $X$ will be a uniform distribution such that:

    -   $P(x) = 0\ \forall x < a\ \ or\ x > b$;

    -   $P(x) = \frac{1}{b - a}\ \forall a \leq x \leq b$;

We can see that this PDF satisfies all constraints:

-   $P(x) \geq 0\ \forall x.$

-   $\int P(x)dx = 1$ (prove that this is true as an exercise).

### Example: Uniform PDF

The diagram shows an illustration of a uniform PDF with bounds a and b,
i.e., $U(a,b)$. Of course, continuous distributions can be (and
generally are) much more complicated than that.

![Risultati immagini per uniform probability density
function](./media/image3.png){width="4.475in"
height="2.8568875765529307in"}

## Expectation

When it is known that a random variable follows a probability
distribution, **it is possible to characterize that variable** (and
hence the related probability distribution) **with some statistics**.

The most straightforward of them is the expectation. **The concept of
expectation is very related to the concept of mean.** When we compute
the mean of a given set of numbers, we usually sum all the numbers
together and then divide by the total.

Since a probability distribution will tell us which values will be more
frequent than others, we can compute this mean with a weighted average,
where the weights are given by the probability distribution.

Specifically, we can define the expectation of a random variable X as
follows:

$$E_{X\sim P}\lbrack X\rbrack = \sum_{x \in \chi}^{}{xP(x)}$$

In the case of continuous variables, the expectation takes the form of
an integral:

$$E_{X \sim P}\lbrack X\rbrack = \int xP(x)dx$$

This is very related to the concept of mean value (or expected value) of
a random variable.

## Variance

The variance gives a measure of how much variability there is in a
variable $X$ around its mean $E\lbrack X\rbrack$.

The variance is defined as follows:

$$var\lbrack X\rbrack = E\lbrack\left( X - E\lbrack X\rbrack \right)^{2}\rbrack$$

## Covariance

The covariance gives a measure of how two variables are linearly related
to each other. It allows to **measure to what extent the increase of one
of the variables corresponds to an increase of the value of the other
one**.

Given two random variables $X$ and $Y$, the covariance is defined as
follows:

$$Cov(X,Y) = E\lbrack\left( X - E\lbrack X\rbrack \right)\left( Y - E\lbrack Y\rbrack \right)\rbrack$$

We can distinguish the following terms:

-   $E\lbrack X\rbrack$ and $E\lbrack Y\rbrack$ are the expectations of
    $X$ and $Y.$

-   $(X - E\lbrack X\rbrack)$ and $(Y - E\lbrack Y\rbrack)$ are the
    differences between the samples and the expected values.

-   $\left( X - E\lbrack X\rbrack \right)\left( Y - E\lbrack Y\rbrack \right)$
    computes the product between the differences.

    -   If the signs of the terms agree, the product is positive.

    -   If the signs of the terms disagree, the product is negative.

        1.  In practice, if when $X$ is larger than the mean, then $Y$
            is larger than the mean and vice versa, when $X\ $is lower
            than the mean then $Y$ is lower than the mean, then the two
            variables are *correlated,* and the covariance is high.

If $X$ is a multi-dimensional variable
$X = \lbrack X_{1},X_{2},\ldots,X_{n}\rbrack$, we can compute all the
possible covariances between variable pairs:
$Cov\lbrack X_{i},X_{j}\rbrack$. This allows to create a matrix, which
is generally referred to as **the covariance matrix**. The general term
of the covariance matrix $Cov(X)$ is given by:

$$Cov(X)_{i,j} = Cov(X_{i},X_{j})$$

# Common Probability Distributions

There are several common probability distributions which can be used to
describe random events. **These distributions have an analytical
formulation which depends generally on one or more parameters.**

When we have **enough evidence that a given random variable is well
described by one of these distributions**, we can simply "fit" the
distribution to the data (i.e., choose the correct parameters for the
distribution) and use the analytical formulation to deal with the random
variable.

It is hence useful to know the **most common probability distributions**
so that we can recognize the cases in which they can be used.

## Bernoulli Distribution

The Bernoulli distribution is a distribution over a single binary random
variable, i.e., the variable $X$ can take only two values:
$\left\{ 0,1 \right\}$.

The distribution is controlled by a single parameter
$\phi \in \lbrack 0,1\rbrack$, which gives the probability of the
variable to be equal to 1.

The analytical formulation of the Bernoulli distribution is very simple:

-   $P(X = 1) = \phi$;

-   $P(X = 0) = 1 - \phi$

The expected value and variance of the associated random variable are:

-   $E\lbrack x\rbrack = \phi$;

-   $Var(x) = \phi(1 - \phi)$.

**Example**

The skewed coin in the previous example landed on "head" $60\%$ of the
times. If we define $X = 1$ when the outcome is head and $X = 0$ when
the outcome is tail, then the variable follows a Bernoulli distribution
with $\phi = 0.6$.

## Binomial Distribution

![](./media/image4.png){width="6.6930555555555555in"
height="4.461805555555555in"}

The binomial distribution is a discrete probability distribution (PMF**)
over natural numbers with parameters** $\mathbf{n}$ **and**
$\mathbf{p}$**;**

It models **the probability of obtaining** $\mathbf{k}$ **successes in a
sequence of** $\mathbf{n}$ **independent experiments which follow a
Bernoulli distribution with parameter**
$\mathbf{p}\mathbf{\ (}\mathbf{\phi}\mathbf{=}\mathbf{p}\mathbf{)}$**;**

The probability mass function of the distribution is given by:

$$P(k) = \binom{n}{k}p^{k}(1 - p)^{n - k}$$

Where:

-   $k$ is the number of successes

-   $n$ is the number of independent trials

-   $p$ is the probability of a success in a single trial

The expected value is $E\lbrack x\rbrack = np$;

The variance is $Var\lbrack k\rbrack = np(1 - p)$;

**Example**

What is the probability of tossing a coin three times and obtaining
three heads? We have:

-   $k = 3$: number of successes (three times head)

-   $n = 3$: number of trials

-   $p = 0.5$: the probability of getting a head when tossing a coin

The required probability will be given by:

$$P(3) = \binom{3}{3}{0.5}^{3}(1 - 0.5)^{3 - 3} = {0.5}^{3} = 0.125$$

**Exercise**

What is the probability of tossing an unfair coin
($P\left( 'head^{'} \right) = 0.6$) 7 times and obtaining $2$ tails?

## Categorical Distribution

The **multinoulli** or **categorical** distribution is a distribution of
a *single discrete variable with* $k$ *different states*, where $k$ is
finite.

-   The distribution is parametrized by a vector
    $\mathbf{p} \in \lbrack 0,1\rbrack^{k - 1}$, where $p_{i}$ gives the
    probability of the i^th^ state.

-   The probability of the k^th^ state is given by
    $1 - \sum_{i = 1}^{k - 1}{p_{i}\ }$.

-   $\mathbf{p}$ must be such that $\sum_{i = 1}^{k - 1}p_{i} \leq 1$ to
    obtain a valid probability distribution.

-   The analytical form of the distribution is given by:
    $p(x = i) = p_{i}$;

This distribution is the **generalization of the Bernoulli distribution
to the case of multiple states**.

**Example:**

Rolling a fair die. In this case, $k = 6$ and
$p_{i} = \frac{1}{k}\ ,\ i = 0,\ldots,k - 1\ $.

## Multinomial Distribution

The multinomial distribution **generalizes the binomial distribution to
the case in which the experiments are not binary**, but they can have
multiple outcomes (e.g., *a dice vs a coin*).

In particular, the multinomial distribution models the probability of
obtaining exactly $(n_{1},\ldots,n_{k})$ occurrences (with
$n = \sum_{i}^{}n_{i}$) for each of the $k$ possible outcomes in a
sequence of $n$ independent experiments which follow a Categorial
distribution with probabilities $p_{1},\ldots,p_{k}$.

The parameters of the distribution are:

-   $n$: the number of trials

-   $k$: the number of possible outcomes

-   $p_{1},\ldots,p_{k}$ the probabilities of obtaining a given class in
    each trial (with $\sum_{i = 1}^{k}p_{i} = 1$)

The PMF of the distribution is:

$$P\left( n_{1},\ldots,n_{k} \right) = \frac{n!}{n_{1}!\ldots n_{k}!}p_{1}^{n_{1}} \cdot \ldots \cdot p_{k}^{n_{k}}$$

The mean is: $E\left\lbrack n_{i} \right\rbrack = np_{i}$.

The variance is:
$Var\left\lbrack n_{i} \right\rbrack = np_{i}(1 - p_{i})$.

The covariance between two of the input variables is:
$Cov\left( n_{i},n_{j} \right) = - np_{i}p_{j}\ (i \neq j)$.

**Example**

Given a fair die with 6 possible outcomes, what is the probability of
getting 3 times 1, 2 times 2, 4 time 3, 5 times 4, 0 times 5, and 1 time
6, rolling the dice for 15 times?

We have:

-   $n = 15$

-   $k = 6$

-   $p_{1} = p_{2} = \ldots p_{6} = \frac{1}{6}$

The required probability is given by:

$$P(3,2,4,5,0,1) = \frac{15!}{3!2!4!5!0!1!} \cdot \frac{1}{6^{3}} \cdot \frac{1}{6^{2}} \cdot \frac{1}{6^{4}} \cdot \frac{1}{6^{5}} \cdot \frac{1}{6^{0}} \cdot \frac{1}{6^{1}} = 8.04 \cdot 10^{- 5}$$

## Gaussian Distribution

The Bernoulli and Categorical distributions are PMF, i.e., distributions
over discrete random variables.

A common PDF when dealing with real values is the **Gaussian
distribution,** also known as **Normal Distribution**.

The distribution is characterized by two parameters:

-   The mean $\mu\mathfrak{\in R}$

-   The standard deviation $\sigma \in (0, + \infty)$

In practice, the distribution is often *seen in terms of* $\mu$ *and*
$\sigma^{2}$ rather than $\sigma$, where $\sigma^{2}$ is called **the
variance**.

The analytical formulation of the Normal distribution is as follows:

$$N\left( x;\mu,\sigma^{2} \right) = \sqrt{\frac{1}{2\pi\sigma^{2}}}e^{- \frac{1}{2\sigma^{2}}(x - \mu)^{2}}$$

The term under the square root is a normalization term which ensures
that the distribution integrates to 1.

The expectation and variance of a variable following the Normal
distribution are as follows:

-   $E\lbrack x\rbrack = \mu$

-   $Var\lbrack x\rbrack = \sigma^{2}$

The Gaussian distribution is very used when we do not have much prior
knowledge on the real distribution we wish to model. This in mainly due
to the **central limit theorem**, which states that the sum of many
independent random variables with the same distribution is approximately
normally distributed.

### Interpretation

![](./media/image5.png){width="6.6930555555555555in"
height="3.3583333333333334in"}

If we plot the PDF of a Normal distribution, we can find that it is easy
to interpret the meaning of its parameters:

-   The resulting curve has a maximum (highest probability) when
    $x = \mu$

-   The curve is symmetric, with the inflection points at
    $x = \mu \pm \sigma$

-   The example shows a normal distribution for $\mu = 0$ and
    $\sigma = 1$

![Risultati immagini per gaussian
distribution](./media/image6.gif){width="4.9540266841644796in"
height="3.361111111111111in"}

Another notable property of the Normal distribution is that:

-   About $68\%$ of the density is comprised in the interval
    $\lbrack - \sigma,\sigma\rbrack$;

-   About $95\%$ of the density is comprised in the interval
    $\lbrack - 2\sigma,2\sigma\rbrack$;

-   Almost 100% of the density is comprised in the interval
    $\lbrack - 3\sigma,3\sigma\rbrack$.

### Multivariate Gaussian

The formulation of the Gaussian distribution generalizes to the
multivariate case, i.e., the case in which $X$ is n-dimensional.

In that case, the distribution is parametrized by a **n-dimensional
vector** $\mathbf{\mu}$ and a
$\mathbf{n}\mathbf{\times}\mathbf{n}\mathbf{\ }$**positive definite
symmetric matrix** $\mathbf{\Sigma}$. The formulation of the
multi-variate Gaussian is:

$$N\left( \mathbf{x;\mu,}\mathbf{\Sigma} \right) = \sqrt{\frac{1}{(2\pi)^{n}\det(\Sigma)}}e^{( - \frac{1}{2}\left( \mathbf{x} - \mathbf{\mu} \right)^{T}\Sigma^{- 1}\left( \mathbf{x} - \mathbf{\mu} \right))}$$

Examples of bivariate Gaussian distributions are shown below.

![](./media/image7.png){width="6.508333333333334in"
height="2.3983234908136484in"}![](./media/image8.png){width="6.508333333333334in"
height="2.3983234908136484in"}In the 2D case, $\mathbf{\mu}$ is a 2D
point representing the center of the Gaussian (the position of the
mode), whereas the matrix $\Sigma$ influences the "shape" of the
Gaussian.

### Estimation of the Parameters of a Gaussian Distribution

We have noted that in many cases we can assume a random variable follows
a Gaussian distribution. However, it is not yet clear how to choose the
parameters of the Gaussian distribution.

Given some data (remember, data is values assumed by random variables!),
we can obtain the parameters of the Gaussian distribution related to the
data with a **maximum likelihood** estimation.

This consists in computing the mean and variance parameters using the
following formula (in the univariate case):

-   $\mu = \frac{1}{n}\sum_{j}^{}x_{j}$

-   $\sigma^{2} = \frac{1}{n}\sum_{j}^{}\left( x_{j} - \mu \right)^{2}$

Where $x_{j}$ represent the different data points.

In the multi-variate case, the computation of the multi-dimensional
$\mathbf{\mu}$ vector is similar:

-   $\mathbf{\mu} = \frac{1}{n}\sum_{j}^{}\mathbf{x}_{j}$

-   $\Sigma$ is instead computed as the covariance matrix related to
    $X$: $\Sigma = Cov(\mathbf{X})$, i.e.,
    $\Sigma_{ij} = Cov\left( \mathbf{X}_{i},\mathbf{X}_{j} \right)$

# Information Theory

Probability Theory allows to deal with the uncertain, however, it does
not allow to quantify it. Information theory provides the tools to
**quantify how much information is present in a signal**.

When dealing with data, it can be useful to understand which data is
informative and which is not, with respect to a given goal.

The basic intuition behind information theory is that learning an
unlikely event has occurred is more informative than learning a likely
event has occurred.

For instance, the event "the sun rose this morning" is very likely and
hence it is not very informative. The message "there was a solar eclipse
this morning" is instead very unlikely, and hence informative.

## Self-information

We would like to quantify information in a way that formalizes the
intuition discussed before:

-   Likely events should have *low information content*

-   Less likely events should have *higher information content*

    1.  Moreover, **independent events should have additive
        information**. For example, finding out that a tossed coin has
        come up as heads twice should convey twice as much information
        as finding out that a tossed coin has come up as heads once.

To satisfy these three properties, the notion of **self-information** is
introduced. Given a random variable $X \sim P$, the self-information of
an event $X = x$ is defined as:

$$I(x) = - logP(x)$$

If the base of the logarithm is 2, then the self-information is measured
in **bits**.

If the base of the logarithm is e, then the self-information is measures
in **nats.**

![](./media/image11.png){width="4.379285870516186in" height="3.0625in"}

It should be noted that this definition of self-information satisfies
the three conditions. Indeed:

-   As $P(x)$ gets larger, $I(x)$ gets smaller and vice versa

-   The self-information for two independent variables $X$ and $Y$ is
    given by:

$$I(X = x,Y = y) = - \log P(X = x,Y = y)$$

-   Since the variables are independent, $P(X,Y) = P(X)P(Y)$, hence:

$$I(X = x,Y = y) = - \log\left\lbrack P(X = x)P(Y = y) \right\rbrack = - logP(X = x) - \log P(Y = y) = I(x) + I(y)$$

-   Hence, also the additivity of the entropies of independent variables
    is satisfied.

## Entropy

*Self-information is defined on a single outcome*. We can quantify the
amount of **uncertainty** in an entire probability distribution using
the **Shannon entropy**:

$$H(X) = E_{X \sim P}\left\lbrack I(x) \right\rbrack = - E_{X \sim P}\left\lbrack \log{P(x)} \right\rbrack$$

In the case of a discrete variable:

$$H(X) = - \sum_{x}^{}{P(x)logP(x)}$$

Where the summation is over all values of $x \in \ \chi$, with $\chi$
alphabet of $X$. In the case of a continuous variable, the sum is
substituted by an integral:

$$H(X) = - \int_{}^{}{P(x)logP(x)dx}$$

The Shannon entropy of a distribution is **the expected amount of
information in an event drawn from that distribution**.

The entropy is measured in **bits** or **nats** (depending on the base
of the logarithm) and can be interpreted as **the amount of information
required on the average to describe the random variable**.

**Example**

-   Let's consider a die with six faces.

-   We can describe the outcomes of rolling the dice with a random
    variable $X$ with alphabet $\chi = \ \left\{ 1,\ldots,6 \right\}$.

-   If the dice is fair, then $P(x) = \frac{1}{6},\ \forall x \in \chi$.

-   The entropy associated with this random variable is:
    $H(X) = - \sum_{i = 1}^{6}{\frac{1}{6}\log}\frac{1}{6} = \log(6) = 2.58\ bits$.

    1.  This makes sense as the minimum number of bits needed to
        represent 8 numbers is 3 ($2^{3} = 8$). Since we have less than
        8 numbers, in average we need less than 3 bits.

&nbsp;

-   Let's suppose the dice is not fair and in particular Let's suppose
    it follows a categorical distribution with
    $\mathbf{p} = \lbrack 0.1,0.1,0.1,0.1,0.1\rbrack$. The probability
    of number "6" will be $0.5$;

-   Intuitively, we need less bits to represent this variable. Indeed,
    since event $X = 6$ is much more frequent, we can represent it with
    the least number of bits, whereas we can represent less frequent
    outcomes with more bits. In particular, the entropy of the variable
    will be:

$$H(X) = - \sum_{i = 1}^{5}{0.1\log{0.1}} - 0.5\log(0.5) = 2.16\ bits$$

-   The number of bits required to represent the variable in average is
    2.16 bits, smaller than in the case of the fair die.

# Questions

-   What is data?

-   Is there a difference between data and information?

-   What is the difference between a variable and a random variable?

-   What is the goal of probability theory?

-   What is the difference between independence and conditional
    independence among random variables?

-   What are the units of measurement of information?

# References

-   Parts of chapter 1 of \[1\];

-   Most of chapter 3 of \[2\];

-   Some parts of chapter 1 of \[3\].

\[1\] Bishop, Christopher M. *Pattern recognition and machine learning*.
springer, 2006.
<https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf>

\[2\] Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. *Deep
learning*. MIT press, 2016. <https://www.deeplearningbook.org/>

\[3\] Cover, Thomas M., and Joy A. Thomas. *Elements of information
theory*. John Wiley & Sons, 2012.
