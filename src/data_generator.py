import pandas as pd

def generate_construction_data():
    """Generates the detailed hierarchical data as a pandas DataFrame."""
    data = [
        # Pillar 1: Project Design
        {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Blueprint Design', 'task': 'Initial Schematics & 3D Model', 'cost': 65000},
        {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Structural Analysis', 'task': 'Foundation & Frame Calculations', 'cost': 95000},
        {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'MEP Engineering', 'task': 'HVAC & Electrical Plans', 'cost': 85000},
        # Pillar 2: Management & Logistics
        {'pillar': 'Management', 'area': 'Administration', 'service': 'Project Management', 'task': 'On-Site Supervision & Reporting', 'cost': 130000},
        {'pillar': 'Management', 'area': 'Administration', 'service': 'Permits & Legal', 'task': 'City & Environmental Approvals', 'cost': 90000},
        {'pillar': 'Management', 'area': 'Logistics', 'service': 'Supply Chain', 'task': 'Material Sourcing & Delivery', 'cost': 70000},
        # Pillar 3: Construction
        {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Excavation & Grading', 'task': 'Earthwork and Site Prep', 'cost': 160000},
        {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Concrete Work', 'task': 'Foundation Pouring & Curing', 'cost': 310000},
        {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Framing & Steel', 'task': 'Wood & Steel Frame Erection', 'cost': 480000},
        {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'task': 'Complete Wiring & Fixtures', 'cost': 240000},
        {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Plumbing & HVAC', 'task': 'Piping, Drains & Ductwork', 'cost': 260000},
        {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Drywall & Painting', 'task': 'Interior Walls and Ceilings', 'cost': 190000},
        {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Flooring & Tiling', 'task': 'Hardwood and Ceramic Installation', 'cost': 175000},
    ]
    return pd.DataFrame(data)