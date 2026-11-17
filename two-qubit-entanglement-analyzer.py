import numpy as np
from qiskit.quantum_info import Statevector , DensityMatrix, partial_trace

def partial_trace_B(rho_ab):
    rho_a = np.zeros((2,2) , dtype=complex)

    for a in range(2):
        for a_prime in range(2):
            for b in range(2):
                row = 2 * a + b
                col = 2 *a_prime + b

                rho_a[a , a_prime] += rho_ab[row , col]

    return rho_a

def analyze_entanglement(psi):
    rho_ab = (DensityMatrix(psi)).data

    rho_a = partial_trace_B(rho_ab)

    purity = np.trace(rho_a @ rho_a)

    is_entangled = not(np.allclose(purity , 1))
    
    return rho_a , purity , is_entangled

test_bell = Statevector(np.array([1 / np.sqrt(2) , 0 , 0 , 1 / np.sqrt(2)]))

test_rho_a , test_purity , test_is_entangled = analyze_entanglement(test_bell)

print(test_rho_a , test_purity , test_is_entangled)
