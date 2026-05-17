import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# N-Queens Performance Analysis Graphs
# Based ONLY on actual experimental outputs
# ==========================================

# -----------------------------
# Common Board Sizes
# -----------------------------
all_n = [10, 30, 50, 100, 200, 500]
small_n = [10, 30, 50, 100]

# -----------------------------
# DFS Results
# -----------------------------
dfs_n = [4, 8, 10]
dfs_time = [0.007, 0.002, 0.004]
dfs_memory = [0.47, 0.50, 0.51]

# -----------------------------
# Hill Climbing Results
# -----------------------------
hc_n = [10, 30, 50]
hc_time = [0.01, 144.80, 409.73]
hc_memory = [0.38, 0.97, 1.32]
hc_conflicts = [0, 0, 0]

# -----------------------------
# Simulated Annealing Results
# -----------------------------
sa_n = [10, 30, 50, 100, 200, 500]
sa_time = [0.018, 0.381, 0.715, 2.94, 18.18, 129.39]
sa_memory = [0.86, 1.02, 1.20, 2.38, 4.72, 19.38]
sa_conflicts = [2, 8, 20, 40, 113, 394]

# -----------------------------
# Genetic Algorithm Results
# -----------------------------
ga_n = [10, 30, 50, 500]
ga_time = [1.15, 336.77, 1033.90, 8823.39]
ga_memory = [35.59, 62.00, 91.53, 448.67]
ga_conflicts = [0, 1, 2, 360]

# =====================================================
# GRAPH 1 — EXECUTION TIME COMPARISON
# =====================================================
plt.figure(figsize=(10, 6))

plt.plot(dfs_n, dfs_time,
         marker='o', linewidth=2,
         label='DFS')

plt.plot(hc_n, hc_time,
         marker='s', linewidth=2,
         label='Hill Climbing')

plt.plot(sa_n, sa_time,
         marker='^', linewidth=2,
         label='Simulated Annealing')

plt.plot(ga_n, ga_time,
         marker='d', linewidth=2,
         label='Genetic Algorithm')

plt.xlabel('Number of Queens (N)', fontsize=12)
plt.ylabel('Execution Time (Seconds)', fontsize=12)
plt.title('Execution Time Comparison of N-Queens Algorithms', fontsize=13)

# Log scale is important because GA values are very large
plt.yscale('log')

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('runtime_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('runtime_comparison.pdf', bbox_inches='tight')

plt.close()

# =====================================================
# GRAPH 2 — MEMORY USAGE COMPARISON
# =====================================================
plt.figure(figsize=(10, 6))

plt.plot(dfs_n, dfs_memory,
         marker='o', linewidth=2,
         label='DFS')

plt.plot(hc_n, hc_memory,
         marker='s', linewidth=2,
         label='Hill Climbing')

plt.plot(sa_n, sa_memory,
         marker='^', linewidth=2,
         label='Simulated Annealing')

plt.plot(ga_n, ga_memory,
         marker='d', linewidth=2,
         label='Genetic Algorithm')

plt.xlabel('Number of Queens (N)', fontsize=12)
plt.ylabel('Peak Memory Usage (KB)', fontsize=12)
plt.title('Memory Usage Comparison of N-Queens Algorithms', fontsize=13)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('memory_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('memory_comparison.pdf', bbox_inches='tight')

plt.close()

# =====================================================
# GRAPH 3 — CONFLICT COMPARISON
# =====================================================
plt.figure(figsize=(10, 6))

plt.plot(hc_n, hc_conflicts,
         marker='s', linewidth=2,
         label='Hill Climbing')

plt.plot(sa_n, sa_conflicts,
         marker='^', linewidth=2,
         label='Simulated Annealing')

plt.plot(ga_n, ga_conflicts,
         marker='d', linewidth=2,
         label='Genetic Algorithm')

plt.xlabel('Number of Queens (N)', fontsize=12)
plt.ylabel('Remaining Conflicts', fontsize=12)
plt.title('Conflict Comparison of Heuristic Algorithms', fontsize=13)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('conflict_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('conflict_comparison.pdf', bbox_inches='tight')

plt.close()

# =====================================================
# GRAPH 4 — SIMULATED ANNEALING SCALABILITY
# =====================================================
plt.figure(figsize=(10, 6))

plt.plot(sa_n, sa_time,
         marker='o', linewidth=2)

plt.xlabel('Number of Queens (N)', fontsize=12)
plt.ylabel('Execution Time (Seconds)', fontsize=12)
plt.title('Scalability of Simulated Annealing', fontsize=13)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('sa_scalability.png', dpi=300, bbox_inches='tight')
plt.savefig('sa_scalability.pdf', bbox_inches='tight')

plt.close()

# =====================================================
# GRAPH 5 — GENETIC ALGORITHM PERFORMANCE
# =====================================================
plt.figure(figsize=(10, 6))

plt.plot(ga_n, ga_time,
         marker='o', linewidth=2,
         label='Execution Time')

plt.xlabel('Number of Queens (N)', fontsize=12)
plt.ylabel('Execution Time (Seconds)', fontsize=12)
plt.title('Genetic Algorithm Performance Analysis', fontsize=13)

plt.yscale('log')

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('ga_performance.png', dpi=300, bbox_inches='tight')
plt.savefig('ga_performance.pdf', bbox_inches='tight')

plt.close()

# =====================================================
# GRAPH 6 — ALGORITHM FEASIBILITY ANALYSIS
# =====================================================
algorithms = ['DFS', 'Hill Climbing', 'SA', 'GA']
feasibility = [1, 3, 6, 4]

plt.figure(figsize=(8, 5))

bars = plt.bar(algorithms, feasibility)

plt.xlabel('Algorithms', fontsize=12)
plt.ylabel('Maximum Solved/Tested Board Size Count', fontsize=12)
plt.title('Algorithm Feasibility and Scalability', fontsize=13)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('feasibility_analysis.png', dpi=300, bbox_inches='tight')
plt.savefig('feasibility_analysis.pdf', bbox_inches='tight')

plt.close()

print('All graphs generated successfully.')
print('Generated files:')
print('- runtime_comparison')
print('- memory_comparison')
print('- conflict_comparison')
print('- sa_scalability')
print('- ga_performance')
print('- feasibility_analysis')
