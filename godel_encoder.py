"""
Gödel Numbering System - Core encoding and decoding logic.

This module implements the Gödel numbering system that converts logical statements
to natural numbers using prime factorization, enabling self-reference in formal systems.
"""

import math
from typing import Dict, List, Tuple, Optional
from sympy import factorint, isprime


class GodelEncoder:
    """
    Encodes logical statements to Gödel numbers using prime factorization.
    
    Each symbol gets assigned a unique prime number, and the Gödel number
    is the product of primes raised to powers corresponding to symbol positions.
    """
    
    def __init__(self):
        # Symbol mapping: symbol -> prime number
        self.symbol_map = {
            '0': 2,      # Zero
            'S': 3,      # Successor function
            '+': 5,      # Addition
            '×': 7,      # Multiplication (using × instead of * for clarity)
            '=': 11,     # Equality
            '(': 13,     # Left parenthesis
            ')': 17,     # Right parenthesis
            '¬': 19,     # Negation
            '→': 23,     # Implication
            '∀': 29,     # Universal quantifier
            '∃': 31,     # Existential quantifier
            'a': 37,     # Variable a
            'b': 41,     # Variable b
            'c': 43,     # Variable c
            'x': 47,     # Variable x
            'y': 53,     # Variable y
            'z': 59,     # Variable z
            ' ': 61,     # Space (for demonstration)
        }
        
        # Reverse mapping for decoding
        self.reverse_map = {v: k for k, v in self.symbol_map.items()}
        
        # Cache for performance
        self._cache = {}
    
    def encode_statement(self, statement: str) -> Tuple[int, Dict]:
        """
        Encode a logical statement to its Gödel number.
        
        Args:
            statement: The logical statement to encode
            
        Returns:
            Tuple of (godel_number, encoding_details)
        """
        if statement in self._cache:
            return self._cache[statement]
        
        # Clean the statement and split into symbols
        symbols = list(statement.strip())
        
        # Get prime numbers for each position (starting from position 1)
        primes = self._get_primes(len(symbols))
        
        # Encode each symbol
        encoding_details = {
            'statement': statement,
            'symbols': symbols,
            'symbol_codes': [],
            'prime_powers': [],
            'prime_factors': {},
            'godel_number': 1
        }
        
        godel_number = 1
        
        for i, symbol in enumerate(symbols):
            if symbol in self.symbol_map:
                symbol_code = self.symbol_map[symbol]
                prime = primes[i]
                power = symbol_code
                
                encoding_details['symbol_codes'].append({
                    'position': i + 1,
                    'symbol': symbol,
                    'code': symbol_code,
                    'prime': prime,
                    'power': power
                })
                
                encoding_details['prime_powers'].append({
                    'prime': prime,
                    'power': power,
                    'contribution': prime ** power
                })
                
                # Update prime factorization
                if prime in encoding_details['prime_factors']:
                    encoding_details['prime_factors'][prime] += power
                else:
                    encoding_details['prime_factors'][prime] = power
                
                godel_number *= (prime ** power)
            else:
                # Unknown symbol - assign a default code
                symbol_code = 67  # Next available prime
                prime = primes[i]
                power = symbol_code
                
                encoding_details['symbol_codes'].append({
                    'position': i + 1,
                    'symbol': symbol,
                    'code': symbol_code,
                    'prime': prime,
                    'power': power,
                    'note': 'Unknown symbol'
                })
                
                encoding_details['prime_powers'].append({
                    'prime': prime,
                    'power': power,
                    'contribution': prime ** power
                })
                
                if prime in encoding_details['prime_factors']:
                    encoding_details['prime_factors'][prime] += power
                else:
                    encoding_details['prime_factors'][prime] = power
                
                godel_number *= (prime ** power)
        
        encoding_details['godel_number'] = godel_number
        
        # Cache the result
        self._cache[statement] = (godel_number, encoding_details)
        
        return godel_number, encoding_details
    
    def decode_number(self, godel_number: int) -> Tuple[str, Dict]:
        """
        Decode a Gödel number back to its original statement.
        
        Args:
            godel_number: The Gödel number to decode
            
        Returns:
            Tuple of (decoded_statement, decoding_details)
        """
        if godel_number in self._cache:
            return self._cache[godel_number]
        
        # Factor the number
        prime_factors = factorint(godel_number)
        
        # Sort primes to maintain position order
        sorted_primes = sorted(prime_factors.keys())
        
        decoding_details = {
            'godel_number': godel_number,
            'prime_factors': prime_factors,
            'sorted_primes': sorted_primes,
            'decoded_symbols': [],
            'decoded_statement': ''
        }
        
        decoded_symbols = []
        
        for i, prime in enumerate(sorted_primes):
            power = prime_factors[prime]
            
            # Find the symbol corresponding to this power
            symbol = self.reverse_map.get(power, f'?{power}')
            
            decoding_details['decoded_symbols'].append({
                'position': i + 1,
                'prime': prime,
                'power': power,
                'symbol': symbol
            })
            
            decoded_symbols.append(symbol)
        
        decoded_statement = ''.join(decoded_symbols)
        decoding_details['decoded_statement'] = decoded_statement
        
        # Cache the result
        self._cache[godel_number] = (decoded_statement, decoding_details)
        
        return decoded_statement, decoding_details
    
    def _get_primes(self, count: int) -> List[int]:
        """
        Get the first 'count' prime numbers.
        
        Args:
            count: Number of primes needed
            
        Returns:
            List of prime numbers
        """
        primes = []
        num = 2
        
        while len(primes) < count:
            if isprime(num):
                primes.append(num)
            num += 1
        
        return primes
    
    def get_symbol_table(self) -> Dict[str, int]:
        """Get the current symbol mapping table."""
        return self.symbol_map.copy()
    
    def add_symbol(self, symbol: str, code: int):
        """
        Add a new symbol to the encoding system.
        
        Args:
            symbol: The symbol to add
            code: The prime number code for the symbol
        """
        if isprime(code) and code not in self.reverse_map:
            self.symbol_map[symbol] = code
            self.reverse_map[code] = symbol
            self._cache.clear()  # Clear cache when symbols change
        else:
            raise ValueError(f"Code {code} must be a unique prime number")
    
    def clear_cache(self):
        """Clear the encoding/decoding cache."""
        self._cache.clear()


class SimplifiedGodelEncoder(GodelEncoder):
    """
    Simplified version using smaller numbers for educational purposes.
    
    This version uses smaller prime numbers and limits statement length
    to keep Gödel numbers manageable for demonstration.
    """
    
    def __init__(self):
        super().__init__()
        
        # Override with smaller primes for demonstration
        self.symbol_map = {
            '0': 2,      # Zero
            'S': 3,      # Successor function
            '+': 5,      # Addition
            '×': 7,      # Multiplication
            '=': 11,     # Equality
            '(': 13,     # Left parenthesis
            ')': 17,     # Right parenthesis
            '¬': 19,     # Negation
            '→': 23,     # Implication
            '∀': 29,     # Universal quantifier
            '∃': 31,     # Existential quantifier
            'a': 37,     # Variable a
            'b': 41,     # Variable b
            'c': 43,     # Variable c
            'x': 47,     # Variable x
            'y': 53,     # Variable y
            'z': 59,     # Variable z
        }
        
        self.reverse_map = {v: k for k, v in self.symbol_map.items()}
        self.max_length = 20  # Limit statement length
    
    def encode_statement(self, statement: str) -> Tuple[int, Dict]:
        """
        Encode with length limit for manageable numbers.
        
        Args:
            statement: The logical statement to encode
            
        Returns:
            Tuple of (godel_number, encoding_details)
        """
        if len(statement) > self.max_length:
            raise ValueError(f"Statement too long. Maximum length is {self.max_length} symbols.")
        
        return super().encode_statement(statement)
