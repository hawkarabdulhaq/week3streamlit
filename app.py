import streamlit as st
import matplotlib.pyplot as plt
from compute_mandelbrot import compute_mandelbrot

# App title
st.title("Mandelbrot Set Visualization")

# Sidebar for user inputs
st.sidebar.header("Visualization Parameters")
width = st.sidebar.slider("Image Width", 400, 1600, 800)
height = st.sidebar.slider("Image Height", 400, 1600, 800)
max_iter = st.sidebar.slider("Max Iterations", 50, 500, 100)
center_real = st.sidebar.number_input("Center Real Part", -2.0, 2.0, -0.5)
center_imag = st.sidebar.number_input("Center Imaginary Part", -2.0, 2.0, 0.0)
x_range = st.sidebar.slider("X Range", 0.5, 3.0, 1.5)
y_range = st.sidebar.slider("Y Range", 0.5, 3.0, 1.5)
zoom = st.sidebar.slider("Zoom", 0.5, 5.0, 1.0)

# Compute Mandelbrot set
mandelbrot_set, bounds = compute_mandelbrot(
    width=width,
    height=height,
    max_iter=max_iter,
    center_real=center_real,
    center_imag=center_imag,
    x_range=x_range,
    y_range=y_range,
    zoom=zoom
)

# Plotting the Mandelbrot set
x_min, x_max, y_min, y_max = bounds

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap="hot", origin="lower")
ax.set_title(f"Mandelbrot Set\nCenter: ({center_real}, {center_imag}), Zoom: {zoom}")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
st.pyplot(fig)
