import streamlit as st
import math

st.title("Advanced Calculator ")

st.write(" Enter Numbers")
numbers_input = st.text_area("Input numbers separated by commas (e.g., 2, 4, 9)")
st.write(" Select the Operation")
operation = st.selectbox(
    "Choose an operation:",
    ["Select an operation", "Square", "Cube", "Square Root", "Cube Root"]
)

if st.button("Calculate"):
    if numbers_input and operation != "Select an operation":
        try:
            numbers = [float(num.strip()) for num in numbers_input.split(",")]
            st.write("### Results")
            st.write("| Number | Result |")

            for num in numbers:
                if operation == "Square":
                    result = num ** 2
                elif operation == "Cube":
                    result = num ** 3
                elif operation == "Square Root":
                    result = math.sqrt(num) if num >= 0 else "N/A (Negative)"
                elif operation == "Cube Root":
                    result = num ** (1 / 3)

                st.write(f"| {num} | {result} |")

        except ValueError:
            st.error("Invalid input! Please enter valid numbers separated by commas.")
    elif not numbers_input:
        st.warning("Please enter numbers to calculate.")
    else:
        st.warning("Please select an operation.")
