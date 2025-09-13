# BogoDB: Random-Walk Graph Database Challenge

This is an interview challenge that tests your ability to optimize a graph structure for a database system that uses random walks to find data.

## Overview

BogoDB is a database where:
- Data is stored as nodes in a weighted graph
- Queries use random walks guided by edge weights to find target nodes
- Each query performs multiple random walks to find the target node
- The goal is to improve both success rate and path efficiency

## Challenge

Your task is to optimize the graph structure for better query performance:
1. Fork this repository
2. Implement your optimization strategy in `candidate_submission/optimize_graph.py`
3. Document your approach directly in this README (see "Your Solution" section below)
4. Submit your repository URL as your solution

## Getting Started

### Setup

First, ensure you have [uv](https://docs.astral.sh/uv/) installed:
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then set up the project:
```bash
# Clone your fork of the repository
git clone https://github.com/YOUR-USERNAME/bogoDB.git
cd bogoDB

# Install dependencies using uv
uv sync

# Run the full pipeline
./run_all.sh
```

### System Parameters

The system uses these constants (defined in `scripts/constants.py`):

| Parameter | Value | Description |
|-----------|-------|-------------|
| NUM_NODES | 500 | Total number of nodes in the graph |
| MAX_EDGES_PER_NODE | 3 | Maximum outgoing edges per node |
| MAX_TOTAL_EDGES | 1000 | Maximum total edges in the graph |
| NUM_QUERIES | 200 | Number of queries in the test set |
| MAX_DEPTH | 10000 | Maximum steps in a random walk |
| NUM_WALKS_PER_QUERY | 10 | Number of random walks per query |

### How It Works

- **Nodes**: Simple integers from 0 to 499
- **Edges**: Weighted connections (weights control probability of traversal)
- **Queries**: Generated using an exponential distribution (some nodes queried more often)
- **Random Walks**: Start at random nodes and follow weighted edges
- **Success**: A query is successful if it reaches the target before max depth

## Implementation

Your task is to complete the `optimize_graph` function in `candidate_submission/optimize_graph.py`:

```python
def optimize_graph(initial_graph, results, ...):
    # TODO: Implement your optimization strategy here
    # ...
    return optimized_graph
```

### Constraints

Your optimized graph must adhere to:
- **Maximum total edges**: 1000 (2 * number of nodes)
- **Maximum outgoing edges per node**: 3
- **All 500 nodes must be present** in the graph
- **Edge weights**: Must be positive and ≤ 10
- **No self-loops** are allowed (a node cannot connect to itself)

The evaluation script will reject graphs that don't meet these constraints.

## Evaluation

Your solution will be evaluated based on:

1. **Approach and Reasoning** (primary)
   - How you analyze the problem
   - Your optimization strategies
   - The trade-offs you consider

2. **Performance** (secondary)
   - Success rate: % of queries that find their target
   - Path length: Shorter paths are better
   - A combined score that balances both metrics

## Tips

- Analyze the query pattern in the initial results
- Consider which nodes are frequently queried
- Think about the balance between exploration and exploitation
- Random walks behave differently than shortest-path algorithms
- Both success rate and path length matter, but they often trade off

## Running Your Solution

```bash
# Run the full pipeline
./run_all.sh

# Or run just your optimizer
uv run candidate_submission/optimize_graph.py

# Then evaluate your solution
uv run scripts/evaluate_graph.py
```

The evaluation will compare your optimized graph against the initial random graph.

## Submission

To submit your solution:

1. Implement your optimization strategy in `optimize_graph.py`
2. Run the full pipeline (`./run_all.sh`) to test your solution
3. Update the "Your Solution" section below with your documentation
4. Commit and push your changes to your forked repository
5. Submit the URL to your forked repository

We expect you to iterate on multiple approaches before arriving at your final solution. In your documentation, include insights from your journey - what worked, what didn't, and how your understanding evolved.

## Your Solution

**Replace this section with your solution documentation.**

### Approach & Analysis

[Describe how you analyzed the query patterns and what insights you found]

### Optimization Strategy

[Explain your optimization strategy in detail]

### Implementation Details

[Describe the key aspects of your implementation]

### Results

[Share the performance metrics of your solution]

### Trade-offs & Limitations

[Discuss any trade-offs or limitations of your approach]

### Iteration Journey

[Briefly describe your iteration process - what approaches you tried, what you learned, and how your solution evolved]

---

* Be concise but thorough - aim for 500-1000 words total
* Include specific data and metrics where relevant
* Explain your reasoning, not just what you did