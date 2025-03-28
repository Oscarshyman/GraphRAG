# 1. Install Memgraph
If Memgraph is not already installed, you can install it on your local machine or run it in a Docker container. For Docker:

`docker run -p 7687:7687 -p 3000:3000 memgraph/memgraph-platform`

This will start Memgraph along with its visualization tool, Memgraph Lab, accessible at http://localhost:3000.

# 2. Install Required Python Libraries
To work with Parquet files and Memgraph, install the following libraries:

`pip install pandas pyarrow gqlalchemy`


# 3. Load Parquet Data into Memgraph
Use Python to read the Parquet files and load the data into Memgraph. see `load_parquet.py`



