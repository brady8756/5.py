from qiskit import QuantumCircuit, Aer
import numpy as np
import streamlit as st


def quantum_superposition():

    circuit = QuantumCircuit(1,1)

    circuit.h(0)

    circuit.measure(0,0)

    simulator = Aer.get_backend('aer_simulator')

    result = simulator.run(circuit).result().get_counts()

    return result

def get_random_value_add():
    res = quantum_superposition()
    values = list(res.values())
    keys = list(res.keys())
    random_value = int(keys[np.argmax(values)])
    return random_value

def get_random_value():
    res1 = quantum_superposition()
    values = list(res1.values())
    keys = list(res1.keys())
    random_value1 = int(keys[np.argmax(values)])

    res2 = quantum_superposition()
    values = list(res2.values())
    keys = list(res2.keys())
    random_value2 = int(keys[np.argmax(values)])

    res3 = quantum_superposition()
    values = list(res3.values())
    keys = list(res3.keys())
    random_value3 = int(keys[np.argmax(values)])

    res4 = quantum_superposition()
    values = list(res4.values())
    keys = list(res4.keys())
    random_value4 = int(keys[np.argmax(values)])

    res5 = quantum_superposition()
    values = list(res5.values())
    keys = list(res5.keys())
    random_value5 = int(keys[np.argmax(values)])

    res6 = quantum_superposition()
    values = list(res6.values())
    keys = list(res6.keys())
    random_value6 = int(keys[np.argmax(values)])

    res7 = quantum_superposition()
    values = list(res7.values())
    keys = list(res7.keys())
    random_value7 = int(keys[np.argmax(values)])

    res8 = quantum_superposition()
    values = list(res8.values())
    keys = list(res8.keys())
    random_value8 = int(keys[np.argmax(values)])

    res9 = quantum_superposition()
    values = list(res9.values())
    keys = list(res9.keys())
    random_value9 = int(keys[np.argmax(values)])

    total_rand = random_value1+random_value2+random_value3+random_value4+random_value5+random_value6+random_value7+random_value8+random_value9
    return total_rand

def validate(arr):
    flag = True
    zero_ket = '|0>'
    one_ket = '|1>'

    if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success('user has won!')
        flag=False

    if arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success('computer won!')
        flag=False

    elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success('user has won!')
        flag=False

    if not flag:
        return 0

    if flag:
        for index in [0,1,2]:
            if(list(arr[index])==[one_ket,one_ket,one_ket]):
                st.success('User has won!')
                return 0
        
        for index in [0,1,2]:
            if(list(arr[index])==[zero_ket,zero_ket,zero_ket]):
                st.success('computer won!')
                return 0
        
        for index in [0,1,2]:
            if(list(arr[:,index])==[one_ket,one_ket,one_ket]):
                st.success('User has won!')
                return 0
        
        for index in [0,1,2]:
            if(list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
                st.success('computer  has won!')
                return 0
        
        if '|Ѱ>' not in arr:
            st.write('It is draw!')
            return 0
    return 1
