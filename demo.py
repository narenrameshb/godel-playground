"""
Demo script for Gödel Numbering Playground.

This script demonstrates the core functionality without requiring Streamlit.
Run this to see how Gödel numbering works with simple examples.
"""

from godel_encoder import SimplifiedGodelEncoder
from paradox_generator import ParadoxGenerator
from visualizer import GodelVisualizer
from examples import GodelExamples
import utils

def demo_basic_encoding():
    """Demonstrate basic encoding functionality."""
    print("Basic Encoding Demo")
    print("=" * 50)
    
    encoder = SimplifiedGodelEncoder()
    
    # Test statements
    test_statements = [
        "0=0",
        "S(0)",
        "x=0",
        "0+0=0",
        "∀x(x=x)"
    ]
    
    for statement in test_statements:
        try:
            godel_number, encoding_details = encoder.encode_statement(statement)
            print(f"\nStatement: '{statement}'")
            print(f"Gödel Number: {godel_number:,}")
            print(f"Length: {len(statement)} symbols")
            print(f"Prime Factors: {encoding_details['prime_factors']}")
            
            # Show symbol breakdown
            print("   Symbol Breakdown:")
            for symbol_info in encoding_details['symbol_codes']:
                contribution = symbol_info['prime'] ** symbol_info['code']
                print(f"     Position {symbol_info['position']}: '{symbol_info['symbol']}' → {symbol_info['code']} → Prime {symbol_info['prime']} → {contribution:,}")
                
        except Exception as e:
            print(f"Error encoding '{statement}': {e}")
    
    print("\n" + "=" * 50)

def demo_decoding():
    """Demonstrate decoding functionality."""
    print("Decoding Demo")
    print("=" * 50)
    
    encoder = SimplifiedGodelEncoder()
    
    # Encode a statement first
    statement = "x=0"
    godel_number, _ = encoder.encode_statement(statement)
    
    print(f"Original Statement: '{statement}'")
    print(f"Gödel Number: {godel_number:,}")
    
    # Now decode it
    try:
        decoded_statement, decoding_details = encoder.decode_number(godel_number)
        print(f"Decoded Statement: '{decoded_statement}'")
        print(f"Match: {'Yes' if statement == decoded_statement else 'No'}")
        print(f"Decoding Details:")
        print(f"   Prime Factors: {decoding_details['prime_factors']}")
        print(f"   Symbol Reconstruction:")
        for symbol_info in decoding_details['decoded_symbols']:
            print(f"     Position {symbol_info['position']}: Prime {symbol_info['prime']}^{symbol_info['power']} → '{symbol_info['symbol']}'")
            
    except Exception as e:
        print(f"Error decoding: {e}")
    
    print("\n" + "=" * 50)

def demo_paradoxes():
    """Demonstrate paradox generation."""
    print("Paradox Generation Demo")
    print("=" * 50)
    
    encoder = SimplifiedGodelEncoder()
    paradox_gen = ParadoxGenerator(encoder)
    
    # Generate different types of paradoxes
    paradox_types = ["liar_paradox", "quine", "provability"]
    
    for paradox_type in paradox_types:
        try:
            paradox_data = paradox_gen.generate_self_referential_statement(paradox_type)
            
            if 'error' not in paradox_data:
                print(f"\n{paradox_data['template']['name']}")
                print(f"Base Statement: '{paradox_data['base_statement']}'")
                print(f"Base Gödel Number: {paradox_data['base_godel_number']:,}")
                
                if paradox_data['has_self_reference']:
                    print(f"Self-Referential: '{paradox_data['self_referential_statement']}'")
                
                print(f"Explanation: {paradox_data['explanation']}")
                
                # Analyze the paradox
                analysis = paradox_gen.analyze_paradox(paradox_data)
                if 'logical_implications' in analysis:
                    print("   Logical Implications:")
                    for implication in analysis['logical_implications']:
                        print(f"     - {implication}")
                
            else:
                print(f"Error with {paradox_type}: {paradox_data['error']}")
                
        except Exception as e:
            print(f"Error generating {paradox_type}: {e}")
    
    print("\n" + "=" * 50)

def demo_visualizations():
    """Demonstrate visualization capabilities."""
    print("Visualization Demo")
    print("=" * 50)
    
    encoder = SimplifiedGodelEncoder()
    visualizer = GodelVisualizer()
    
    # Create a sample statement
    statement = "x=0"
    godel_number, encoding_details = encoder.encode_statement(statement)
    
    print(f"Statement: '{statement}'")
    print(f"Gödel Number: {godel_number:,}")
    
    # Create visualizations
    try:
        # Prime factorization tree
        tree_fig = visualizer.create_prime_factorization_tree(
            encoding_details['prime_factors'],
            f"Prime Factorization of '{statement}'"
        )
        print("Created prime factorization tree visualization")
        
        # Symbol mapping chart
        mapping_fig = visualizer.create_symbol_mapping_chart(
            encoding_details,
            f"Symbol Mapping for '{statement}'"
        )
        print("Created symbol mapping chart")
        
        # Process flow
        flow_fig = visualizer.create_encoding_process_flow(encoding_details)
        print("Created encoding process flow diagram")
        
        print("All visualizations created successfully!")
        
    except Exception as e:
        print(f"Error creating visualizations: {e}")
    
    print("\n" + "=" * 50)

def demo_examples():
    """Demonstrate the examples collection."""
    print("Examples Collection Demo")
    print("=" * 50)
    
    examples = GodelExamples()
    
    # Show all categories
    categories = examples.categories
    print(f"Available categories: {', '.join(categories)}")
    
    # Show examples by difficulty
    for difficulty in ["Beginner", "Intermediate", "Advanced"]:
        difficulty_examples = examples.get_examples_by_difficulty(difficulty)
        print(f"\n{difficulty} examples ({len(difficulty_examples)}):")
        for example in difficulty_examples:
            print(f"  - {example.name}: {example.statement}")
            print(f"    {example.description}")
    
    # Show learning progression
    progression = examples.get_learning_progression()
    print(f"\nLearning progression:")
    for level, level_examples in progression.items():
        print(f"  {level}: {len(level_examples)} examples")
    
    print("\n" + "=" * 50)

def demo_utils():
    """Demonstrate utility functions."""
    print("Utility Functions Demo")
    print("=" * 50)
    
    # Prime number utilities
    primes = utils.get_first_n_primes(10)
    print(f"First 10 primes: {primes}")
    
    # Size estimation
    size_estimate = utils.estimate_godel_number_size(5)
    print(f"Size estimate for 5-symbol statement:")
    print(f"  Estimated digits: {size_estimate['digits']}")
    print(f"  Scientific notation: {size_estimate['scientific_notation']}")
    
    # Statement validation
    test_statements = ["0=0", "x=0", "invalid@symbol", ""]
    for statement in test_statements:
        validation = utils.validate_statement(statement)
        print(f"\nValidation for '{statement}':")
        print(f"  Valid: {validation['valid']}")
        if validation['errors']:
            print(f"  Errors: {validation['errors']}")
        if validation['warnings']:
            print(f"  Warnings: {validation['warnings']}")
    
    # Prime info
    prime_info = utils.get_prime_info(17)
    if 'error' not in prime_info:
        print(f"\nPrime 17 info:")
        print(f"  Position: {prime_info['position']}")
        print(f"  Next prime: {prime_info['next_prime']}")
        print(f"  Previous prime: {prime_info['previous_prime']}")
    
    print("\n" + "=" * 50)

def main():
    """Run all demos."""
    print("Gödel Numbering Playground - Demo Mode")
    print("=" * 60)
    
    try:
        demo_basic_encoding()
        demo_decoding()
        demo_paradoxes()
        demo_visualizations()
        demo_examples()
        demo_utils()
        
        print("\nAll demos completed successfully!")
        print("The playground is working correctly.")
        
    except Exception as e:
        print(f"\nDemo failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
