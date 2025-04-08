import pandas as pd
from gqlalchemy import Memgraph

# Connect to Memgraph
memgraph = Memgraph("127.0.0.1", 7687)

# Read Parquet file
df = pd.read_parquet("/workspaces/GraphRAG/PKP/GraphRAG/ragtest/output/create_final_nodes.parquet")

# Create nodes and relationships in Memgraph
for index, row in df.iterrows():
    id_value = str(row['id']).replace("'", "\\'")
    name = str(row['title']).replace("'", "\\'")
    query = f"CREATE (:Entity {{id: '{id_value}', name: '{name}'}})"
    print(query)  # Debugging
    memgraph.execute(query)