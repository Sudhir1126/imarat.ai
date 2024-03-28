# integration_scalability.py

class ConstructionProject:
    def __init__(self, project_name, project_size):
        self.project_name = project_name
        self.project_size = project_size
        self.assets = []
    
    def add_asset(self, asset):
        self.assets.append(asset)
    
    def remove_asset(self, asset):
        self.assets.remove(asset)

class Asset:
    def __init__(self, asset_id, asset_type):
        self.asset_id = asset_id
        self.asset_type = asset_type

# Example usage
project = ConstructionProject("Project A", "Large")
asset1 = Asset("001", "Excavator")
asset2 = Asset("002", "Crane")
project.add_asset(asset1)
project.add_asset(asset2)
