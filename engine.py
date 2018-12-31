from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.providers.ibmq import least_busy
from qiskit import IBMQ, execute, BasicAer
from oracle import *
import QuantumHelper

passList = [ "pass","1234","coolPassword","noPass"]

def getAvailablePasswords():
    return passList

def getSelectedHash(passV):
    return digester(passV)

def StartQuantum(realMachine, userHash):
    # Quantum Register
    qr = QuantumRegister(2)
    # Classical Register
    cr = ClassicalRegister(2)
    # Circuit
    qc = QuantumCircuit(qr,cr)
    print("Circuit Set Succesfully")

    if realMachine:
        # You should enter your credentials in Python beforehand
        # To do that, try importing IBMQ and then IBMQ.save_account(YOUR_TOKEN)
        IBMQ.load_accounts()
        print("Account Loaded..")
        backend = least_busy(IBMQ.backends(simulator=False))
    else:
        backend = BasicAer.get_backend('qasm_simulator')

    print("Starting circuit design..")

    # Super position with Hadamard gates
    qc.h(qr[1])
    qc.h(qr[0])

    # Set outcome returned from Oracle function based on user input
    # We don't know what oracle function does. It returns 0,1,2,3 based on result.
    oracleResult = oracle( userHash )
    QuantumHelper.OutcomeSetter( oracleResult , qc, qr)

    # Quantum inversion step. Real power of Grover's Algorithm
    qc.h(qr[0])
    qc.h(qr[1])
    qc.x(qr[1])
    qc.x(qr[0])
    qc.h(qr[1])
    qc.cx(qr[0], qr[1])
    qc.h(qr[1])
    qc.x(qr[1])
    qc.x(qr[0])
    qc.h(qr[0])
    qc.h(qr[1])
    # End of Quantum Inversion

    # We can measure now
    qc.measure(qr,cr)

    # Executing our circuit..
    print("Executing design..")
    results = execute(qc, backend=backend, shots=1).result()
    resultPass = passList[int(list((results.get_counts(qc)).keys())[0],2)]
    resStr = f'Quantum Gods have spoken. Your passwords was {resultPass}\n Found in 1 shot. \n Traditional computer would find this in {oracleResult+1} shot'
    return resStr
