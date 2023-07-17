import streamlit as st

def multiplicar_numeros(num1, num2):
    return num1 * num2

def main():
    st.title("Aplicación de multiplicación")
    
    num1 = st.number_input("Ingrese el primer número", value=0)
    num2 = st.number_input("Ingrese el segundo número", value=0)
    
    if st.button("Multiplicar"):
        resultado = multiplicar_numeros(num1, num2)
        st.success(f"El resultado de la multiplicación es: {resultado}")

if __name__ == '__main__':
    main()