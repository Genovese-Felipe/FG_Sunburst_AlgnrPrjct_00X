# Sunburst Chart Generator

This project generates an interactive sunburst chart to visualize hierarchical cost data for a construction project. The chart is created using Plotly and the data is managed with pandas.

## Project Structure

- `src/`: Contains the main source code for the project.
  - `data_generator.py`: A module to generate the hierarchical cost data.
  - `visualizer.py`: A module to create and style the sunburst chart.
  - `main.py`: The main script to run the data generation and visualization process.
- `tests/`: Contains unit tests for the project.
  - `test_data_generator.py`: Tests for the data generation module.
  - `test_visualizer.py`: Tests for the visualization module.
- `requirements.txt`: A file listing the project's dependencies.
- `pytest.ini`: Configuration file for pytest.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

To generate the sunburst chart, run the `main.py` script from the root of the project:

```bash
python src/main.py
```

This will create a `sunburst_dashboard.html` file in the root directory, which you can open in your web browser to view the interactive chart.

## Running the Tests

To run the unit tests, use `pytest`:

```bash
pytest
```

This will discover and run all the tests in the `tests/` directory.