# Two-Qubit Entanglement Analyzer

A Python project that implements the partial trace operation and analyzes entanglement in two-qubit pure quantum states using NumPy and Qiskit.

The goal of this project is to understand the relationship between reduced density matrices, purity, and quantum entanglement by implementing the underlying mathematical operations directly.

## 1. Project Overview

This project provides the following features:

- Construct two-qubit pure states using Qiskit.
- Generate density matrices from statevectors.
- Implement the partial trace operation manually using NumPy.
- Calculate the purity of a reduced density matrix.
- Determine whether a normalized two-qubit pure state is entangled.
- Display the reduced density matrix, purity, and entanglement result.

## 2. Mathematical Background

### 2.1 Density Matrix

For a pure quantum state, the density matrix is defined as

$$
\rho_{AB}=|\psi\rangle\langle\psi|
$$

A two-qubit system has a Hilbert space of dimension

$$
2^2=4
$$

Therefore, the density matrix of the entire system is a 4×4 complex matrix.

### 2.2 Partial Trace

The partial trace operation is used to obtain the reduced density matrix of a subsystem.

For a two-qubit system AB, tracing out B gives

$$
\rho_A=\mathrm{Tr}_B(\rho_{AB})
$$

The matrix elements are calculated using

$$
(\rho_A)_{a,a'}=
\sum_{b=0}^{1}(\rho_{AB})_{ab,a'b}
$$

The computational basis indices are converted into NumPy indices using

$$
\mathrm{index}=2a+b
$$

The function `partial_trace_B()` implements this operation using three nested Python loops.

In Qiskit's state ordering, A corresponds to q1 and B to q0.

### 2.3 Purity

The purity of a density matrix is defined as

$$
P=\mathrm{Tr}(\rho^2)
$$

For a single-qubit density matrix:

- P = 1 indicates a pure state.
- 0.5 ≤ P < 1 indicates a mixed state.

For a normalized bipartite pure state, the reduced density matrix can be used to determine entanglement.

If the reduced state is pure, the bipartite state is separable. If the reduced state is mixed, the bipartite state is entangled.

This project uses numerical comparison with P = 1 to implement this criterion.

## 3. Implementation

### Partial Trace Function

`partial_trace_B(rho_ab)`

- Accepts a 4×4 NumPy density matrix.
- Traces out the second subsystem, B.
- Returns the 2×2 reduced density matrix of subsystem A.

### Entanglement Analysis Function

`analyze_entanglement(psi)`

- Accepts a two-qubit pure state.
- Constructs its full density matrix using Qiskit.
- Calls the manually implemented partial trace function.
- Calculates the purity of the reduced density matrix.
- Returns the reduced density matrix, purity, and entanglement classification.

## 4. Test Case: Bell State

The example uses the Bell state

$$
|\Phi^+\rangle=
\frac{|00\rangle+|11\rangle}{\sqrt2}
$$

After tracing out subsystem B, the reduced density matrix becomes

$$
\rho_A=
\frac12
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
$$

Its purity is

$$
P=\mathrm{Tr}(\rho_A^2)=\frac12
$$

Since the overall state is pure but the reduced state is mixed, the two qubits are entangled.

Expected output:

```text
Reduced density matrix:
[[0.5+0.j 0. +0.j]
 [0. +0.j 0.5+0.j]]

Purity: 0.5
Entangled: True
```

Small floating-point differences may occur.

## 5. Requirements

- Python 3
- NumPy
- Qiskit

The project was developed in a Windows Visual Studio Python environment.

## 6. Installation and Usage

Install the required libraries:

```bash
pip install numpy qiskit
```

Run the Python script:

```bash
python two_qubit_entanglement.py
```

The program prints the reduced density matrix, its purity, and the entanglement classification.

## 7. Limitations

- The entanglement classification assumes a normalized two-qubit pure state.
- Mixed-state entanglement detection is not supported.
- The partial trace implementation is limited to two qubits and traces out subsystem B.
- The current example tests a Bell state.
- Explicit input validation and a comprehensive automated test suite are not included.
- The implementation uses nested loops for educational purposes rather than performance optimization.

## 8. Learning Outcomes

Through this project, I practiced:

- Density matrices and composite quantum systems
- Partial trace operations
- Reduced density matrices and their physical interpretation
- Purity-based entanglement detection for pure states
- NumPy matrix multiplication and array indexing
- Python functions, loops, and modular code organization

This project is part of my ongoing study of quantum software engineering, focusing on implementing fundamental quantum information operations from their mathematical definitions.
