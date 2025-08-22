"""
Utils - Helper functions for Gödel numbering playground.

This module provides utility functions for prime numbers, factoring,
and other mathematical operations needed for the playground.
"""

import math
from typing import List, Dict
from sympy import isprime





def get_first_n_primes(n: int) -> List[int]:
    """
    Get the first n prime numbers.
    
    Args:
        n: Number of primes to get
        
    Returns:
        List of the first n prime numbers
    """
    primes = []
    num = 2
    
    while len(primes) < n:
        if isprime(num):
            primes.append(num)
        num += 1
    
    return primes

















def estimate_godel_number_size(statement_length: int, avg_symbol_code: int = 30) -> Dict:
    """
    Estimate the size of a Gödel number based on statement length.
    
    Args:
        statement_length: Length of the statement
        avg_symbol_code: Average symbol code value
        
    Returns:
        Dictionary with size estimates
    """
    # Rough estimate: product of first n primes raised to average symbol code
    primes = get_first_n_primes(statement_length)
    
    # Calculate rough estimate
    rough_estimate = 1
    for prime in primes:
        rough_estimate *= (prime ** avg_symbol_code)
    
    # Calculate logarithms for better understanding
    log_estimate = math.log10(rough_estimate)
    
    return {
        'statement_length': statement_length,
        'primes_used': primes,
        'rough_estimate': rough_estimate,
        'log_estimate': log_estimate,
        'scientific_notation': f"{rough_estimate:.2e}" if rough_estimate < 1e308 else "overflow",
        'digits': int(log_estimate) + 1
    }











def create_demo_statements() -> List[str]:
    """
    Create a list of demo statements for quick testing.
    
    Returns:
        List of demo statements
    """
    return [
        "0=0",
        "S(0)",
        "0+0=0",
        "x=0",
        "∀x(x=x)",
        "(x=0)→(x+x=0)",
        "S(S(0))=2",
        "∀x∀y(x+y=y+x)",
        "¬(0=1)",
        "∃x(x=0)"
    ]
