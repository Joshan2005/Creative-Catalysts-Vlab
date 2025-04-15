# save as conductometric_titration.py and run using: streamlit run conductometric_titration.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Conductometric Titration Simulator", layout="centered")

# Title
st.title("🔬 Conductometric Titration Simulator")
st.write("""
This simulation helps visualize the **conductivity changes** during the titration of a strong (HCl) and weak acid (CH₃COOH) mixture with NaOH.
""")

# User Inputs
acid_type = st.selectbox("Choose acid system:", ["HCl only", "CH₃COOH only", "Mixture (HCl + CH₃COOH)"])
volume_added = st.slider("Maximum Volume of NaOH added (mL)", 5.0, 30.0, 15.0, 0.5)

# Simulate Conductance Data
volumes = np.arange(0, volume_added, 0.5)
conductance = []

if acid_type == "HCl only":
    for v in volumes:
        if v < 7:
            c = 10 - v  # decreasing region
        else:
            c = 2 + (v - 7) * 0.8  # increasing region
        conductance.append(c)

elif acid_type == "CH₃COOH only":
    for v in volumes:
        if v < 8:
            c = 4 + v * 0.5  # gradual rise
        else:
            c = 8 + (v - 8) * 1.2  # sharp rise after endpoint
        conductance.append(c)

else:  # Mixture
    for v in volumes:
        if v < 5:
            c = 10 - v * 1.2  # HCl
        elif v < 12:
            c = 5 + (v - 5) * 0.5  # CH3COOH
        else:
            c = 8 + (v - 12) * 1.5  # Excess NaOH
        conductance.append(c)

# Plotting
fig, ax = plt.subplots()
ax.plot(volumes, conductance, marker='o', color='blue')
ax.set_title("Conductance vs Volume of NaOH Added")
ax.set_xlabel("Volume of NaOH (mL)")
ax.set_ylabel("Conductance (mS)")
ax.grid(True)
st.pyplot(fig)

# Info Box
with st.expander("📘 Show Theory"):
    st.write("""
    - **Conductometric titration** measures the change in electrical conductivity during neutralization.
    - When strong acid (HCl) is neutralized, fast-moving H⁺ is replaced by slower Na⁺, conductivity drops.
    - When weak acid (CH₃COOH) is titrated, product salt increases ions — conductivity rises gradually.
    - After complete neutralization, excess OH⁻ causes rapid conductivity increase.
    """)

# Footer
st.success("🧪 Simulation Complete! You can adjust parameters to test different scenarios.")
