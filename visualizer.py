"""
Visualizer - Prime factorization and visual components for Gödel numbering.

This module provides interactive visualizations of the encoding/decoding process,
including prime factorization trees, symbol mappings, and educational diagrams.
"""

import plotly.graph_objects as go
from typing import Dict
import math


class GodelVisualizer:
    """
    Creates interactive visualizations for Gödel numbering demonstrations.
    
    This class provides various visualization methods to help users understand
    the relationship between logical statements and their Gödel numbers.
    """
    
    def __init__(self):
        self.colors = {
            'symbols': '#1f77b4',
            'primes': '#ff7f0e',
            'powers': '#2ca02c',
            'factors': '#d62728',
            'highlight': '#9467bd'
        }
    
    def create_prime_factorization_tree(self, prime_factors: Dict[int, int], 
                                      title: str = "Prime Factorization Tree") -> go.Figure:
        """
        Create an interactive tree visualization of prime factorization.
        
        Args:
            prime_factors: Dictionary mapping primes to their powers
            title: Title for the visualization
            
        Returns:
            Plotly figure object
        """
        if not prime_factors:
            return self._create_empty_figure("No prime factors to display")
        
        # Create tree structure
        fig = go.Figure()
        
        # Calculate positions for tree nodes
        primes = list(prime_factors.keys())
        powers = list(prime_factors.values())
        
        # Create tree layout
        y_positions = []
        x_positions = []
        labels = []
        parents = []
        
        # Root node (Gödel number)
        root_label = f"Gödel Number<br>{math.prod(p**power for p, power in prime_factors.items()):,}"
        y_positions.append(0)
        x_positions.append(0)
        labels.append(root_label)
        parents.append("")
        
        # Prime factor nodes
        for i, (prime, power) in enumerate(prime_factors.items()):
            y_positions.append(-1)
            x_positions.append((i - len(primes)/2) * 2)
            labels.append(f"Prime: {prime}<br>Power: {power}<br>Contribution: {prime**power:,}")
            parents.append(root_label)
            
            # Power detail nodes
            y_positions.append(-2)
            x_positions.append((i - len(primes)/2) * 2)
            labels.append(f"{prime}^{power} = {prime**power:,}")
            parents.append(f"Prime: {prime}<br>Power: {power}<br>Contribution: {prime**power:,}")
        
        # Create tree edges
        edge_x = []
        edge_y = []
        
        for i, parent in enumerate(parents):
            if parent:
                # Find parent index
                parent_idx = labels.index(parent)
                edge_x.extend([x_positions[parent_idx], x_positions[i], None])
                edge_y.extend([y_positions[parent_idx], y_positions[i], None])
        
        # Add edges
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            mode='lines',
            line=dict(color='gray', width=2),
            showlegend=False,
            hoverinfo='none'
        ))
        
        # Add nodes
        fig.add_trace(go.Scatter(
            x=x_positions, y=y_positions,
            mode='markers+text',
            text=labels,
            textposition="middle center",
            marker=dict(
                size=20,
                color=['#9467bd'] + ['#ff7f0e'] * len(primes) + ['#2ca02c'] * len(primes),
                line=dict(color='white', width=2)
            ),
            showlegend=False,
            hoverinfo='text'
        ))
        
        # Update layout
        fig.update_layout(
            title=title,
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='white',
            height=500
        )
        
        return fig
    

    

    

    

    

    
    def _create_empty_figure(self, message: str) -> go.Figure:
        """Create an empty figure with a message."""
        fig = go.Figure()
        fig.add_annotation(
            x=0.5, y=0.5,
            text=message,
            showarrow=False,
            font=dict(size=16, color='gray')
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='white'
        )
        return fig
    

