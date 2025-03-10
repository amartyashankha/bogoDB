#!/usr/bin/env python3
import json
import random
import os
import numpy as np
from constants import (
    NUM_NODES,
    MAX_EDGES_PER_NODE,
    NUM_QUERIES,
    LAMBDA_PARAM,
    RANDOM_SEED,
    DATA_DIR,
    INITIAL_GRAPH_FILE,
    QUERIES_FILE,
)


def generate_initial_graph(
    num_nodes=NUM_NODES, max_edges_per_node=MAX_EDGES_PER_NODE, seed=RANDOM_SEED
):
    """
    Generate initial graph with random connections and weights.

    Args:
        num_nodes: Number of nodes in the graph
        max_edges_per_node: Maximum number of outgoing edges per node
        seed: Random seed for reproducibility

    Returns:
        A dictionary representing the graph as an adjacency list with weights
    """
    random.seed(seed)
    np.random.seed(seed)

    graph = {}

    for node in range(num_nodes):
        # Decide how many outgoing edges this node will have (1 to max_edges_per_node)
        num_edges = random.randint(1, max_edges_per_node)

        # Select random neighbors
        possible_neighbors = list(range(num_nodes))
        possible_neighbors.remove(node)  # Remove self-loops
        neighbors = random.sample(
            possible_neighbors, min(num_edges, len(possible_neighbors))
        )

        # Assign random weights to each edge
        neighbor_weights = {}
        for neighbor in neighbors:
            # Generate a random weight between 0.1 and 1.0
            weight = round(random.uniform(0.1, 1.0), 2)
            neighbor_weights[str(neighbor)] = weight

        graph[str(node)] = neighbor_weights

    return graph


def generate_queries(
    num_nodes=NUM_NODES,
    num_queries=NUM_QUERIES,
    lambda_param=LAMBDA_PARAM,
    seed=RANDOM_SEED,
):
    """
    Generate queries using an exponential distribution over node IDs.

    Args:
        num_nodes: Number of nodes in the graph
        num_queries: Number of queries to generate
        lambda_param: Parameter for exponential distribution
        seed: Random seed for reproducibility

    Returns:
        A list of node IDs to query
    """
    np.random.seed(seed)

    # Generate exponentially distributed values
    exp_values = np.random.exponential(scale=1 / lambda_param, size=num_queries)

    # Scale to fit within the range of node IDs
    scaled_values = (exp_values % num_nodes).astype(int)

    return scaled_values.tolist()


if __name__ == "__main__":
    # Create data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Generate and save initial graph
    initial_graph = generate_initial_graph()
    with open(INITIAL_GRAPH_FILE, "w") as f:
        json.dump(initial_graph, f, indent=2)

    # Generate and save queries
    queries = generate_queries()
    with open(QUERIES_FILE, "w") as f:
        json.dump(queries, f, indent=2)

    print(f"Generated initial graph with {NUM_NODES} nodes")
    print(f"Generated {NUM_QUERIES} queries with exponential distribution")

    # Calculate and print some statistics about the graph
    total_edges = sum(len(edges) for edges in initial_graph.values())
    avg_edges_per_node = total_edges / NUM_NODES
    print(f"Total edges in graph: {total_edges}")
    print(f"Average edges per node: {avg_edges_per_node:.2f}")
