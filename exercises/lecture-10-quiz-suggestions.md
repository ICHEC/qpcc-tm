# Lecture 10 quiz question suggestions

These questions draw on the QUBO formulation, anomalous problem instances,
classical solver behaviour, scaling, degeneracy, and the QAOA workflow.

## Multiple choice

### 1. Outlier anomaly: which method is most vulnerable?

Consider the number-partitioning instance

$$
\{100,9,8,7,6,5,4,3,2,1\}.
$$

Its best partition may contain very different numbers of items on the two
sides. Which strategy is most vulnerable if it relies on building two
apparently balanced groups through irreversible placement decisions?

- A. Pick-me-first
- B. Greedy search
- C. Simulated annealing
- D. VQE

**Answer:** A. Pick-me-first makes a sequence of local placement decisions and
does not reconsider earlier choices. A large outlier can make the best
partition structurally different from the nearly uniform cases for which this
rule works well.

### 2. Trapped at a local minimum

A solver reaches a partition whose cost is lower than that of every partition
reachable by one allowed move. However, it is not the global optimum: reaching
the best partition requires first accepting a move that increases the cost.
Which solver is unable to escape under its standard update rule?

- A. Greedy search that accepts only cost-reducing moves
- B. Simulated annealing at a sufficiently high temperature
- C. Exhaustive enumeration of all partitions
- D. QAOA

**Answer:** A. Strict greedy search cannot cross the energy barrier because its
first required move increases the cost. Simulated annealing can accept such a
move probabilistically, exhaustive enumeration checks every candidate rather
than following a local path, and QAOA is not restricted to a sequence of
accepted single-item moves.

### 3. Anomaly diagnosis

Two solvers are tested on the same rugged QUBO landscape:

- Solver P always chooses the best immediately improving neighbour.
- Solver Q sometimes accepts a worse neighbour early in the run and becomes
  more selective later.

Which result is the strongest evidence that the landscape contains local
minima separated by energy barriers?

- A. P repeatedly stops above the best known cost, while Q sometimes reaches it
- B. P and Q always return the same optimum
- C. Both solvers evaluate the objective
- D. Q uses binary variables

**Answer:** A. Solver P behaves like greedy search and cannot leave a local
minimum. Solver Q behaves like simulated annealing and can sometimes cross the
barrier while its temperature is high.

### 4. Scaling anomaly

An exact solver enumerates all distinct two-way partitions, treating an
assignment and its complement as the same split. What is the dominant scaling
of the number of candidates?

- A. $N$
- B. $N^2$
- C. $2^{N-1}$
- D. $\log_2N$

**Answer:** C. There are $2^N$ binary assignments, but complementary assignments
exchange the labels A and B and describe the same partition.

### 5. Degenerate energy levels

A QUBO energy histogram shows that many different bit strings have exactly the
same cost. What does this indicate?

- A. The energy level is degenerate
- B. The QUBO matrix must be antisymmetric
- C. Every bit string is optimal
- D. The cost function has become continuous

**Answer:** A. Degeneracy means that distinct configurations share an objective
value. The degenerate level may be the ground level or a higher-energy level.

### 6. Domain-based choice: VQE or QAOA

Which pairing is the most appropriate starting point?

- A. Molecular ground-state energy: QAOA; delivery scheduling encoded as a QUBO: VQE
- B. Molecular ground-state energy: VQE; delivery scheduling encoded as a QUBO: QAOA
- C. Both problems always require VQE
- D. Both problems always require QAOA

**Answer:** B. VQE targets the ground state of a physical Hamiltonian. QAOA is
structured around a discrete cost Hamiltonian and a mixer over candidate
solutions.

### 7. The quantum–classical handoff

The quantum processor runs a QAOA circuit many times and returns a frequency
distribution of measured bit strings. What should the classical computer do
next?

- A. Calculate the weighted-average QUBO cost and use it to choose new values of $\boldsymbol\gamma$ and $\boldsymbol\beta$
- B. Apply the cost and mixer gates directly to the measured classical bits
- C. Replace the QUBO matrix with an identity matrix
- D. Select the most frequent bit string and stop after the first iteration

**Answer:** A. The measured frequencies estimate the expected cost. A classical
optimiser uses that value to update the circuit angles, after which the quantum
processor prepares and measures a new QAOA state.

### 8. Cost Hamiltonian versus mixer Hamiltonian

Which statement correctly distinguishes the two QAOA Hamiltonians?

- A. $H_C$ encodes objective values, while $H_M$ creates transitions between candidate bit strings
- B. $H_M$ stores the QUBO coefficients, while $H_C$ measures the qubits
- C. Both Hamiltonians only contribute a global phase
- D. $H_C$ removes the need for a classical optimiser

**Answer:** A. The cost unitary creates objective-dependent relative phases.
The mixer changes amplitudes and allows interference between candidate
solutions.

### 9. From QUBO scores to Hamiltonian energies

Why does the ground state of the QAOA cost Hamiltonian represent an optimal
solution of the original QUBO?

- A. Each computational-basis state represents a bit string, and its Hamiltonian eigenvalue equals that bit string's QUBO cost
- B. Every Hamiltonian has the all-zero state as its ground state
- C. The mixer assigns the same energy to every bit string
- D. Measurement automatically sorts the outcomes by cost

**Answer:** A. The binary-to-spin mapping constructs $H_C$ so that
$H_C|\mathbf{x}\rangle=f(\mathbf{x})|\mathbf{x}\rangle$. The basis state with
the lowest eigenvalue therefore encodes a bit string with the minimum QUBO
cost.

## Sequencing question

### 10. From a QUBO to a QAOA candidate solution

Arrange these stages in the correct order:

1. Sample bit strings and evaluate their classical QUBO scores.
2. Map the binary objective to a cost Hamiltonian.
3. Use a classical optimiser to update $\boldsymbol\gamma$ and
   $\boldsymbol\beta$, repeating the variational loop until the expected cost
   converges.
4. Prepare $|+\rangle^{\otimes n}$.
5. Alternate the cost and mixer unitaries.
6. Estimate the expected cost.

**Answer:** Perform 2 once. Then repeat 4, 5, 6, and 3: re-prepare the initial
state, run the parameterised QAOA circuit, estimate its cost, and update the
angles. After convergence, run the circuit with the best angles and perform 1.
