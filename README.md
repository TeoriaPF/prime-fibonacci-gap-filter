# Prime-Fibonacci Gap Filter

An original research concept and Python implementation exploring the transitional constraints of consecutive prime gaps using even Fibonacci numbers (specifically 8 and 34) combined with a logarithmic macro-trend.

## Core Hypothesis
While prime numbers exhibit chaotic distributions, their consecutive gaps (\(d_n = p_{n+1} - p_n\)) demonstrate structured probabilistic behaviors when encountering even Fibonacci bounds. By analyzing these transition anomalies, we can establish memory-based filtering constraints to optimize prime search algorithms.

## Key Statistical Findings (Evaluated up to 2,000,000)
1. **The Fibonacci Blocking Effect (Gap 8):** When a prime gap equals 8, the probability of the immediate subsequent gap being 2 or 8 drops to exactly **0.00%**. The sequence dynamically breaks out towards non-Fibonacci even numbers (such as 6, 10, or 4).
2. **The Elastic Rebound Effect (Gap 34):** Unlike gap 8, a massive gap of 34 triggers an immediate rebound, sending the subsequent gap back to smaller Fibonacci bounds (2 and 8) in **33.44%** of analyzed cases.
3. **Macro-Trend Anchoring:** Compounding these Markovian transition matrix constraints with Gauss's Prime Number Theorem (\(\frac{d_n}{\ln(p_n)} \approx 1\)) restricts prediction error variations.

## Evaluation Metrics (10,000 Primes Test)
* **Mean Absolute Error (MAE):** 4.82 integers
* **Perfect Match Rate (Error = 0):** 7.82%
* **Confidence Window Accuracy (Error ≤ 4):** 54.12%

## Python Implementation
You can find the predictive model under `prime_filter.py`. It benchmarks a non-homogeneous Markov chain variant against localized prime sequences.
