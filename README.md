# Partisan-Confidence-Model
Simulation files for the *Partisan Confidence* model of opinion evolution written in python programming language. 
The Project include three folders as below: 
1. Corollaries: A jupyter notebook for verifying collaries. 
2. One-dimensional: Two jupyter notebooks for simulating the Partisan confidenc-lite (PC-lite) and Partisan confidence (PC) model 
3. Two-dimensional: Two jupyter notebooks for simulating the Partisan confidenc-lite multi-dimensional (MDPC-lite) and Partisan confidenc multi-dimensional (MDPC) model 

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

## multi-dimensional model 
Suppose that there $`\mathcal{M} = \{1, ..., m}`$ topics for discussion. Take $`x^{(k)}_i(t)\in [-1,1]`$ as the opinion of agent $`i`$ at time $`t`$ about topic $`k \in \mathcal{M}`$. Opinion evolution according to the MDPC-lite and MDPC model is given below. 
### MDPC-lite: $`m \ geq 2`$

```math
x^{(k)}_i(t+1) - x^{(k)}_i(t) = \sum_{j\neq i} w_{ij}(t) |x^{(k)}_j(t)| \left( sgn(x^{(k)}_j(t)) - x^{(k)}_i(t) \right) 
```

### MDPC: $`m = 2`$
```math
x^{(k)}_i(t+1) - x^{(k)}_i(t) = \sum_{j\neq i} w_{ij}(t) d_i(\vec{x}_i(t), \vec{x_j(t)})|x^{(k)}_j(t)| \left( sgn(x^{(k)}_j(t)) - x^{(k)}_i(t) \right) 
```




