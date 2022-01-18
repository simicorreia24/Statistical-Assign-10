#!/usr/bin/env python
# coding: utf-8

# Statistical Assignment 10
# 
# 1. A chicken lays n eggs. Each egg independently does or doesn’t hatch, with probability p of hatching. 
# For each egg that hatches, the chick does or doesn’t survive (independently of the other eggs), 
# with probability s of survival. Let N ⇠Bin(n, p) be the number of eggs which hatch, X be the number 
# of chicks which survive, and Y be the number of chicks which hatch but don’t survive (so X + Y = N).
# Find the marginal PMF of X, and the joint PMF of X and Y . Are they independent?
# 
# Answer
# 
# the probability that a egg hatches and chick survives is psps.
# We can consider each egg as a Bernoulli trial each with a success (hatching and surviving) probability psps.
# There are nn independent trials, so X∼Bin(n,ps)X∼Bin(n,ps).
# 
# But I am trying to prove this more rigorously.
# 
# For any 1≤i≤n1≤i≤n we have
# 
# P(X=i)=∑j=0nP(X=i|N=j)P(N=j)=∑j=inP(X=i|N=j)P(N=j)=∑j=in(ji)si(1−s)j−i(nj)pj(1−p)n−j
# 
# the probability that a egg hatches and chick survives is psps. 
# We can consider each egg as a Bernoulli trial each with a success (hatching and surviving) probability psps. 
# There are nn independent trials, so X∼Bin(n,ps)X∼Bin(n,ps).
# 
# But I am trying to prove this more rigorously.
# 
# For any 1≤i≤n1≤i≤n we have
# 
# P(X=i)=∑j=0nP(X=i|N=j)P(N=j)=∑j=inP(X=i|N=j)P(N=j)=∑j=in(ji)si(1−s)j−i(nj)pj(1−p)n−j
# 
# 
