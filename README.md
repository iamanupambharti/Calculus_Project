# Optimizing Drug Dosage: A Calculus-Based Analysis of Pharmacokinetics

## Overview

This project delves into the fascinating intersection of Calculus and Health Informatics, specifically focusing on Pharmacokinetics—the journey of a drug through the body. We explore how mathematical models can predict drug behavior, helping to optimize dosages for maximum effectiveness and safety.

Our work centers on the **Surge Function**, a powerful tool for modeling how drug concentrations rise and fall in the bloodstream over time. By applying fundamental calculus concepts, we can unlock critical insights from this model.

## The Model: Surge Function

The concentration of the drug in the bloodstream is modeled by the Surge Function:

`C(t) = A * t * e^(-k * t)`

Where:
- `C(t)` is the drug concentration at time `t`.
- `A` is a constant related to the dose and absorption rate.
- `k` is the elimination rate constant of the drug.
- `t` is the time, usually in hours.

This elegant equation captures the initial increase in concentration as the drug is absorbed, followed by a gradual decrease as it is metabolized and eliminated by the body.

## Calculus in Action

Calculus provides us with two key instruments to analyze our model:

### 1. Peak Effectiveness (Differentiation)

To find out when the drug is most potent, we need to determine the time of its maximum concentration. This is a classic optimization problem solved using differentiation. By taking the derivative of `C(t)` with respect to `t` and setting it to zero, we can find the exact time of peak effectiveness, `t_peak`.

### 2. Total Exposure (Integration)

How much of the drug is the body exposed to over a specific period? This is crucial for understanding both its therapeutic effects and potential toxicity. We answer this question by calculating the **Area Under the Curve (AUC)**, which represents the total drug exposure, also known as "Bioavailability." This is achieved through definite integration of our concentration function `C(t)` over a given time interval.

## Python Simulation

To bring these concepts to life, we've developed a Python simulation (`drug_simulation.py`). This script not only calculates the theoretical `t_peak` and AUC but also generates a visual representation of the drug concentration curve.

This allows us to:
- Visualize the drug's journey in the body.
- Verify our calculus-based findings against a computational model.
- See the direct impact of the parameters `A` and `k` on the drug's behavior.

### How to Run the Simulation

1.  **Prerequisites:** Make sure you have Python installed, along with the following libraries:
    *   `numpy`
    *   `matplotlib`
    *   `scipy`

    You can install them using pip:
    ```bash
    pip install numpy matplotlib scipy
    ```

2.  **Execute the script:**
    ```bash
    python drug_simulation.py
    ```

The script will print the calculated peak time, peak concentration, and total drug exposure (AUC). It will also generate and display a graph, saving it as `concentration_graph.png`.

### Key Parameters in the Simulation

You can tweak these values at the top of the `drug_simulation.py` file to see how they affect the outcome:

- `A`: Influences the height of the curve. A higher `A` means a higher peak concentration.
- `k`: Controls how quickly the drug is eliminated. A larger `k` leads to a faster drop in concentration and an earlier peak.
- `t_end`: The total time duration for the simulation.
