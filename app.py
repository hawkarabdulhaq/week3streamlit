# app.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="Mandelbrot Set Visualizer", layout="wide")

# Streamlit Title and Instructions
st.title("Mandelbrot Set Visualizer")
st.write("Adjust the parameters below to generate and visualize the Mandelbrot set.")

# Sidebar for user input
st.sidebar.header("Visualization Parameters")
width = st.sidebar.number_input("Image Width", min_value=100, max_value=2000, value=800, step=100)
height = st.sidebar.number_input("Image Height", min_value=100, max_value=2000, value=800, step=100)
max_iter = st.sidebar.slider("Maximum Iterations", min_value=10, max_value=500, value=100, step=10)

# Mandelbrot Function
def compute_mandelbrot(width, height, max_iter):
    x = np.linspace(-2, 1, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C, dtype=complex)
    mandelbrot_set = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mandelbrot_set += mask

    return mandelbrot_set

# Generate and Display Mandelbrot Set
mandelbrot_set = compute_mandelbrot(width, height, max_iter)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(mandelbrot_set, extent=(-2, 1, -1.5, 1.5), cmap='coolwarm')
ax.set_title('Mandelbrot Set')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
plt.colorbar(ax.imshow(mandelbrot_set, extent=(-2, 1, -1.5, 1.5), cmap='coolwarm'), ax=ax, label='Iterations')

# Display the plot in Streamlit
st.pyplot(fig)
