
## This is not much of a fancy method. Will be richer soon, right now it only have OutcomeSetter

# Set outcome in terms of Quantum Logic based on Oracle's result i
def OutcomeSetter(i,qc,qr):
    if i == 3:
        # 11
        qc.h(qr[1])
        qc.cx(qr[0], qr[1])
        qc.h(qr[1])
    elif i == 2:
        # 10
        qc.h(qr[1])
        qc.x(qr[0])
        qc.cx(qr[0], qr[1])
        qc.x(qr[0])
        qc.h(qr[1])
    elif i == 1:
        # 01
        qc.h(qr[0])
        qc.x(qr[1])
        qc.cx(qr[1], qr[0])
        qc.x(qr[1])
        qc.h(qr[0])
    else:
        # 00
        qc.x(qr[0])
        qc.x(qr[1])
        qc.h(qr[1])
        qc.cx(qr[0], qr[1])
        qc.x(qr[0])
        qc.h(qr[1])
        qc.x(qr[1])
