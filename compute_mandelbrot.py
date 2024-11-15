# compute_mandelbrot.py

import numpy as np

def compute_mandelbrot(width, height, max_iter, center_real, center_imag, x_range, y_range, zoom):
    """
    Computes the Mandelbrot set for the given parameters.

    Parameters:
    - width: Image width (pixels)
    - height: Image height (pixels)
    - max_iter: Maximum number of iterations
    - center_real: Center of the Mandelbrot set (real part)
    - center_imag: Center of the Mandelbrot set (imaginary part)
    - x_range: Horizontal range of the plot
    - y_range: Vertical range of the plot
    - zoom: Zoom level

    Returns:
    - A 2D NumPy array representing the Mandelbrot set.
    """
    # Define the range for the complex plane
    x_min, x_max = center_real - x_range / zoom, center_real + x_range / zoom
    y_min, y_max = center_imag - y_range / zoom, center_imag + y_range / zoom

    # Create a meshgrid of complex numbers
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    # Initialize the array to store the iteration counts
    Z = np.zeros_like(C, dtype=complex)
    mandelbrot_set = np.zeros(C.shape, dtype=int)

    # Compute the Mandelbrot set
    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mandelbrot_set[mask] = i

    return mandelbrot_set
