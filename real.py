import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Decay constants for different elements (in arbitrary units)
decay_constants = {
    "Uranium-238": 0.05,
    "Carbon-14": 0.1,
    "Potassium-40": 0.07,
    "Thorium-232": 0.03,
    "Radium-226": 0.06,
    "Lead-210": 0.08,
    "Polonium-210": 0.09,
    "Radon-222": 0.04,
    "Uranium-235": 0.02,
    "Thorium-230": 0.01
}


def radioactive_decay(initial_quantity, decay_constant, time):
    return initial_quantity * np.exp(-decay_constant * time)


def main():
    st.title("Radioactive Decay Simulation")
    st.sidebar.title("Simulation Settings")

    initial_quantity = st.sidebar.number_input("Initial Quantity", min_value=1, step=1, value=100)

    # Dropdown for selecting different elements
    selected_element = st.sidebar.selectbox("Select Element", list(decay_constants.keys()))

    decay_constant = decay_constants[selected_element]

    max_time = st.sidebar.number_input("Maximum Time", min_value=1, step=1, value=50)

    st.sidebar.markdown("---")

    time_values = np.arange(0, max_time, 0.1)
    decay_values = radioactive_decay(initial_quantity, decay_constant, time_values)

    st.subheader("Simulation Results")
    st.write("### Decay Curve for", selected_element)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_values, decay_values, label="Radioactive Decay")
    ax.set_xlabel("Time")
    ax.set_ylabel("Quantity")
    ax.legend()

    # Pass the figure object to st.pyplot()
    st.pyplot(fig)


if __name__ == "__main__":
    main()