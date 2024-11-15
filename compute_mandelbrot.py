# compute_mandelbrot.py

import numpy as np

def compute_mandelbrot(
    width=800, 
    height=800, 
    max_iter=100, 
    center_real=-0.5, 
    center_imag=0.0, 
    x_range=1.5, 
    y_range=1.5, 
    zoom=1.0
):
    """
    Compute the Mandelbrot set for given parameters.

    Parameters:
    - width (int): Image width in pixels.
    - height (int): Image height in pixels.
    - max_iter (int): Maximum number of iterations to determine divergence.
    - center_real (float): Real part of the center of the complex plane.
    - center_imag (float): Imaginary part of the center of the complex plane.
    - x_range (float): Range for the real axis.
    - y_range (float): Range for the imaginary axis.
    - zoom (float): Zoom level (higher values zoom in).

    Returns:
    - mandelbrot_set (np.ndarray): A 2D array representing iteration counts.
    - bounds (tuple): Tuple of bounds (x_min, x_max, y_min, y_max) for plotting.
    """
    # Adjust the bounds based on zoom level and center
    x_min, x_max = center_real - x_range / zoom, center_real + x_range / zoom
    y_min, y_max = center_imag - y_range / zoom, center_imag + y_range / zoom

    # Generate a grid of complex numbers
    real = np.linspace(x_min, x_max, width)
    imag = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(real, imag)
    C = X + 1j * Y

    # Initialize arrays for computation
    Z = np.zeros_like(C, dtype=complex)
    mandelbrot_set = np.zeros(C.shape, dtype=int)

    # Mandelbrot computation: Iterative update for all points
    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mandelbrot_set[mask] = i

    return mandelbrot_set, (x_min, x_max, y_min, y_max)
