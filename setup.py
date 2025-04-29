from setuptools import setup, find_packages

setup(
    name="customer_segmentation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.2.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.14.0",
        "streamlit>=1.22.0",
        "jupyter>=1.0.0",
        "openpyxl>=3.1.0",
        "scipy>=1.10.0",
    ],
)