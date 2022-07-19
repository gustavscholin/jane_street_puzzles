# Solution for Jane Street puzzle July 2022, Andy's Morning Stroll

https://www.janestreet.com/puzzles/andys-morning-stroll-index/

My approach here is to first calculate the expected number of steps Andy takes when walking on the football. This is done by modelling Andy's stroll as a Markov Process by setting up the transition probability matrix $P$. There is a theorem stating that

$$\lim _{t \rightarrow + \infty} P^{t} = \mathbb{1} \pi^{\prime}$$

where $\pi$ is the *invariant probability distribution*. The expected number of steps for Andy on the football, $n_0$, can then be calculated as

$$n_0 = \frac{1}{\pi_{0}}.$$

Note that I calculate the number of steps when starting in state 0 but since it doesn't matter where you start on the football this number will be the same no matter in which state you start.

To calculate $p$, the probability that the number of steps on the tile floor is strictly more steps than $n_0$, I start by finding all possible strolls on the tile floor where the number of steps are less than or equal to $n_0$. In each step of a stroll there are 3 choices with equal probability, therefore, the probability for a stroll $s$ with $k$ steps is

$$P(s(k)) = (1/3)^k.$$

This means that

$$p = 1 - \sum_{s(k) \in S}P(s(k)) = 1 - \sum_{s(k) \in S}(1/3)^k$$

where $S$ is all strolls on the tile floor where the number of steps are less than or equal to $n_0$.

The script includes simulations to verify the results and took about 4 min to run on my laptop.
