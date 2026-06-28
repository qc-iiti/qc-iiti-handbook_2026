# pip install qiskit qiskit-aer

"""
================================================================================
CIRCUIT EXPLANATION: THE GREENBERGER-HORNE-ZEILINGER (GHZ) STATE
================================================================================
This script creates a 3-qubit GHZ state, which is a maximally entangled 
quantum state. Here is what it does conceptually:

1. Initialization: We start with 3 qubits, all resting in the baseline |0⟩ state.
2. Superposition: A Hadamard (H) gate places the first qubit (q0) into a 50/50 
   superposition of |0⟩ and |1⟩. 
3. Entanglement: We use Controlled-NOT (CNOT) gates to link the state of q1 and 
   q2 to q0. 

Because of this entanglement, if q0 collapses into |0⟩ upon measurement, it 
forces q1 and q2 to instantly collapse into |0⟩ as well. If q0 collapses into |1⟩, 
the others must follow. As a result, the individual identities of the qubits are 
lost; they exist only as a collective system. The final combined state is a 
superposition of all zeros or all ones:

                     |Ψ⟩ = (1/√2) * (|000⟩ + |111⟩)

When measured, you will never see mixed states like |010⟩ or |101⟩. All three 
qubits will always completely agree on the final outcome.
================================================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Creating a quantum circuit. 3 qubits, 3 classical bits.
qc = QuantumCircuit(3, 3)   

# Step 1: Superpose q0
qc.h(0)

# Step 2: Entangle q1 with q0
qc.cx(0, 1)

# Step 3: Entangle q2 with q0
qc.cx(0, 2)

# Measure all three qubits into their respective classical bits
qc.measure([0, 1, 2], [0, 1, 2])

# Gives a visual representation of the circuit
print(qc.draw('text'))

# Instantiates the local simulator
simulator = AerSimulator()

# Runs the circuit and extracts the measurement count dictionary
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

# ── Results ───────────────────────────────────────────────────────────────────
# This block iterates through the simulation data to create a readable, 
# text-based histogram. It converts raw counts into percentages and draws 
# visual bars to represent the probability distribution of the states.
print("\nMeasurement results (1000 shots):")
for state, count in sorted(counts.items()):
    # Create a visual bar where every 20 counts equals one block character (█)
    bar = "█" * (count // 20)
    # Print the state in Dirac notation |abc⟩, the bar graph, the raw count, and percentage
    print(f"  |{state}⟩  {bar}  ({count} times, {count/10:.1f}%)")



