#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}===== BogoDB Challenge Pipeline =====${NC}"
echo "This script runs the entire BogoDB pipeline in sequence."

mkdir -p data

# Step 1: Generate initial data
echo -e "${GREEN}1. Generating initial data...${NC}"
uv run -m scripts.generate_initial_data
echo ""

# Step 2: Run initial queries
echo -e "${GREEN}2. Running initial queries on the random graph...${NC}"
uv run -m scripts.random_walk
echo ""

# Step 3: Visualize the query distribution
echo -e "${GREEN}3. Visualizing query distribution...${NC}"
uv run -m scripts.visualize_results
echo ""

# Step 4: Run optimization (candidate's solution)
echo -e "${BLUE}===== OPTIMIZATION PHASE =====${NC}"
echo -e "${GREEN}4. Running your optimization strategy...${NC}"
uv run -m candidate_submission.optimize_graph
echo ""

# Step 5: Evaluate the optimized graph
if [ -f "candidate_submission/optimized_graph.json" ]; then
    echo -e "${GREEN}5. Evaluating optimized graph...${NC}"
    echo -e "${BLUE}===== EVALUATION RESULTS =====${NC}"
    uv run -m scripts.evaluate_graph
    echo ""
else
    echo -e "${RED}Error: No optimized graph found.${NC}"
    echo "Make sure your optimizer generates 'candidate_submission/optimized_graph.json'"
    echo ""
fi

echo -e "${BLUE}===== Pipeline Completed! =====${NC}"
echo "Check the 'data' directory for results and visualizations." 