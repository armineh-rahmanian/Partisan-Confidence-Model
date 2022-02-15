# Partisan-Confidence-Model
Simulation files for the *Partisan Confidence* model of opinion evolution written in python programming language. 
The Project include three folders as below: 
1. Corollaries: A jupyter notebook for verifying collaries. 
2. One-dimensional: Two jupyter notebooks for simulating the Partisan confidenc-lite (PC-lite) and Partisan confidence (PC) model.
- PC-lite_case_1.ipynb: There bubbles and some are considered outside the bubbles. 
- PC-lite_case_2.ipynb: Two bubbles are considered in the population. 
- PC_case_2.ipynb: Two bubbles are considered in the population. 
4. Two-dimensional: Two jupyter notebooks for simulating the Partisan confidenc-lite multi-dimensional (MDPC-lite) and Partisan confidenc multi-dimensional (MDPC) model 
- MDPC-lite_case_2.ipynb: Two bubbles are considered in the population. 
- MDPC_case_2.ipynb: Two bubbles are considered in the population. 
## One-dimensional model 
Suppose that $`x_i(t)\in [-1,1]`$ stands for the opinion of agent $`i`$ at time $`t`$ about a specific and fixed subject. Opinion evolution according to the PC-lite and PC model is given below. 
### PC-lite: 


```math
x_i(t+1) - x_i(t) = \sum_{j\neq i} w_{ij}(t) |x_j(t)| \left( sgn(x_j(t)) - x_i(t) \right) 
```

### PC
```math
x_i(t+1) - x_i(t) = \sum_{j\neq i} w_{ij}(t) d_i(x_i(t), x_j(t))|x_j(t)| \left( sgn(x_j(t)) - x_i(t) \right) 
```
where $`d_i: [-1,1]^2 \to [0,1]`$ is the discount function accounting for confirmation bias in the model described as below. If two individuals share the same general belief 

```math
d_i(x_i(t), x_j(t)) = 1 ~~\text{if}~~sgn(x_i(t)) = sgn(x_j(t)), 
```
and if two individuals share different general beliefs

```math
d_i(x_i(t), x_j(t)) \leq  \hat{d}_i(|x_i(t)|)  ~~\text{if}~~sgn(x_i(t)) = sgn(x_j(t)) 
```
where $`\hat{d}_i:[-1,1] \to [0,1]`$ is a non-increasing discounting function.  

## multi-dimensional model 
Suppose that there are $`\mathcal{M} = \{1, ..., m\}`$ topics for discussion. Take $`x^{(k)}_i(t)\in [-1,1]`$ as the opinion of agent $`i`$ at time $`t`$ about topic $`k \in \mathcal{M}`$. Opinion evolution according to the MDPC-lite and MDPC model is given below. 
### MDPC-lite: $`m \geq 2`$

```math
x^{(k)}_i(t+1) - x^{(k)}_i(t) = \sum_{j\neq i} w_{ij}(t) |x^{(k)}_j(t)| \left( sgn(x^{(k)}_j(t)) - x^{(k)}_i(t) \right) 
```

### MDPC: $`m = 2`$
```math
x^{(k)}_i(t+1) - x^{(k)}_i(t) = \sum_{j\neq i} w_{ij}(t) d_i(\vec{x}_i(t), \vec{x_j(t)})|x^{(k)}_j(t)| \left( sgn(x^{(k)}_j(t)) - x^{(k)}_i(t) \right) 
```
where $`d_i: [-1,1]^2 \to [0,1]`$ is the discount function accounting for confirmation bias in the model described as below. If two individuals share the same general belief 

```math
d_i(\vec{x}_i(t), \vec{x}_j(t)) = 1 ~~\text{if}~~sgn(\vec{x}_i(t)) = sgn(\vec{x}_j(t))~~\text{or}~~\vec{x}_i(t) = \mathbf{0}~~\text{or}~~\vec{x}_j(t) = \mathbf{0}, 
```
and if two individuals share different general beliefs

```math
d_i(\vec{x}_i(t), \vec{x}_j(t)) \leq  \hat{h}_i(\theta)  ~~\text{if}~~sgn(\vec{x}_i(t)) \neq sgn(\vec{x}_j(t))~~\text{and}~~\vec{x}_i(t) \neq \mathbf{0}~~\text{and}~~\vec{x}_j(t) \neq \mathbf{0}. 
```
where $`\hat{h}_i:[0, \pi] \to [0,1]`$ is a non-increasing discounting function and $`\theta`$ is the angle between $`\vec{x}_i`$ and $`\vec{x}_j`$ given as below. 

```math
\theta = \frac{\vec{x}_i.\vec{x}_j}{\|\vec{x}_i\|_2\times\|\vec{x}_j\|_2}
```



