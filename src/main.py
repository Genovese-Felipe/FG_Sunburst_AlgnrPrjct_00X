from data_generator import generate_construction_data
from visualizer import create_sunburst_figure

def main():
    """
    Main function to generate data, create visualization, and save the output.
    """
    # Generate the data
    data_df = generate_construction_data()

    # Create the sunburst figure
    final_fig = create_sunburst_figure(data_df)

    # Define the output file name
    output_file_name = "sunburst_dashboard.html"

    # Export to a standalone HTML file
    final_fig.write_html(output_file_name, full_html=True, include_plotlyjs='cdn')

    print(f"✅ Chart successfully exported to '{output_file_name}'")

if __name__ == "__main__":
    main()