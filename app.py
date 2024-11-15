# app.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="Mandelbrot Set Visualizer", layout="wide")

# Streamlit Title and Instructions
st.title("Mandelbrot Set Visualizer")
st.write("Use the controls in the sidebar to customize the Mandelbrot set visualization.")

# Sidebar for user input
st.sidebar.header("Visualization Parameters")
width = st.sidebar.number_input("Image Width", min_value=100, max_value=2000, value=800, step=100)
height = st.sidebar.number_input("Image Height", min_value=100, max_value=2000, value=800, step=100)
max_iter = st.sidebar.slider("Maximum Iterations", min_value=10, max_value=1000, value=100, step=10)
aspect_ratio = st.sidebar.selectbox("Aspect Ratio", ["1:1 (Square)", "16:9 (Wide)", "4:3 (Classic)"], index=0)

# Map aspect ratios to actual values
aspect_mapping = {"1:1 (Square)": (1.5, 1.5), "16:9 (Wide)": (1.5, 0.85), "4:3 (Classic)": (1.5, 1.125)}
y_range, x_range = aspect_mapping[aspect_ratio]

center_real = st.sidebar.slider("Center (Real Part)", min_value=-2.0, max_value=1.0, value=-0.5, step=0.01)
center_imag = st.sidebar.slider("Center (Imaginary Part)", min_value=-1.5, max_value=1.5, value=0.0, step=0.01)
zoom = st.sidebar.slider("Zoom Level", min_value=1.0, max_value=10.0, value=1.0, step=0.1)

colormap = st.sidebar.selectbox("Colormap", plt.colormaps(), index=plt.colormaps().index("coolwarm"))

# Mandelbrot Function
def compute_mandelbrot(width, height, max_iter, center_real, center_imag, x_range, y_range, zoom):
    x_min, x_max = center_real - x_range / zoom, center_real + x_range / zoom
    y_min, y_max = center_imag - y_range / zoom, center_imag + y_range / zoom

    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C, dtype=complex)
    mandelbrot_set = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mandelbrot_set[mask] = i

    return mandelbrot_set

# Generate and Display Mandelbrot Set
mandelbrot_set = compute_mandelbrot(width, height, max_iter, center_real, center_imag, x_range, y_range, zoom)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(mandelbrot_set, extent=[-x_range, x_range, -y_range, y_range], cmap=colormap, origin="lower")
ax.set_title(f'Mandelbrot Set\nCenter: ({center_real}, {center_imag}), Zoom: {zoom}x')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
plt.colorbar(ax.imshow(mandelbrot_set, extent=[-x_range, x_range, -y_range, y_range], cmap=colormap), ax=ax, label='Iterations')

# Display the plot in Streamlit
st.pyplot(fig)
