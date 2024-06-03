import streamlit as st
import numpy as np

def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.identity(n)

    for j in range(n):
        for i in range(j, n):
            L[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))
        for i in range(j + 1, n):
            U[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]
            if np.isnan(U[j][i]):
                U[j][i] = 0

    return L, U

def doolittle_decomposition(A):
    n = len(A)
    L = np.identity(n)
    U = np.zeros((n, n))

    for j in range(n):
        for i in range(j + 1):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for i in range(j, n):
            L[i][j] = (A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))) / U[j][j]
            if np.isnan(L[i][j]):
                L[i][j] = 0

    return L, U

st.title("K1 Application Matrix Decomposition Calculator")

matrix_input = st.text_area("Enter your matrix (comma separated rows, semicolon separated columns):")
decomposition_type = st.selectbox("Select decomposition method:", ["Crout", "Doolittle"])

if st.button("Decompose"):
    try:
        A = np.array([[float(num) for num in row.split(',')] for row in matrix_input.split(';')])
        st.write("Matrix A:")
        st.write(A)
        if decomposition_type == "Crout":
            L, U = crout_decomposition(A)
        else:
            L, U = doolittle_decomposition(A)

        st.write("Matrix L:")
        st.write(L)
        st.write("Matrix U:")
        st.write(U)
    except Exception as e:
        st.error(f"An error occurred: {e}")