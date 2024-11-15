import streamlit as st
import matplotlib.pyplot as plt
import sqlite3
from compute_mandelbrot import compute_mandelbrot
from datetime import datetime

# Database setup
DATABASE = "parameters.db"

def initialize_database():
    """Initialize the SQLite database if not exists."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parameters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            width INTEGER,
            height INTEGER,
            max_iter INTEGER,
            center_real REAL,
            center_imag REAL,
            x_range REAL,
            y_range REAL,
            zoom REAL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def update_database(params):
    """Update the database with the latest parameter values."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO parameters (width, height, max_iter, center_real, center_imag, x_range, y_range, zoom)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (params["width"], params["height"], params["max_iter"], params["center_real"], 
          params["center_imag"], params["x_range"], params["y_range"], params["zoom"]))
    conn.commit()
    conn.close()

# Initialize database
initialize_database()

# App title
st.title("Mandelbrot Set Visualization with Database Logging")

# Sidebar for user inputs
st.sidebar.header("Visualization Parameters")
width = st.sidebar.slider("Image Width", 400, 1600, 800, key="width")
height = st.sidebar.slider("Image Height", 400, 1600, 800, key="height")
max_iter = st.sidebar.slider("Max Iterations", 50, 500, 100, key="max_iter")
center_real = st.sidebar.number_input("Center Real Part", -2.0, 2.0, -0.5, key="center_real")
center_imag = st.sidebar.number_input("Center Imaginary Part", -2.0, 2.0, 0.0, key="center_imag")
x_range = st.sidebar.slider("X Range", 0.5, 3.0, 1.5, key="x_range")
y_range = st.sidebar.slider("Y Range", 0.5, 3.0, 1.5, key="y_range")
zoom = st.sidebar.slider("Zoom", 0.5, 5.0, 1.0, key="zoom")

# Log parameters and update database
params = {
    "width": width,
    "height": height,
    "max_iter": max_iter,
    "center_real": center_real,
    "center_imag": center_imag,
    "x_range": x_range,
    "y_range": y_range,
    "zoom": zoom
}
update_database(params)

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

# Display database contents for debugging
st.sidebar.header("Database Contents")
if st.sidebar.button("Show Parameter Log"):
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query("SELECT * FROM parameters ORDER BY updated_at DESC", conn)
    st.sidebar.write(df)
    conn.close()
