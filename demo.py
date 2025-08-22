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
    print("🔤 Basic Encoding Demo")
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
                    print(f"Final Gödel Number: {paradox_data['final_godel_number']:,}")
                    print(f"Paradox Type: {paradox_data['paradox_type']}")
                
                # Show analysis
                analysis = paradox_gen.analyze_paradox(paradox_data)
                print(f"Explanation: {analysis['explanation']}")
                
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
    
    # Create a simple statement for visualization
    statement = "x=0"
    godel_number, encoding_details = encoder.encode_statement(statement)
    
    print(f"Statement: '{statement}'")
    print(f"Gödel Number: {godel_number:,}")
    
    # Test different visualization types
    try:
        # Prime factorization tree
        tree_fig = visualizer.create_prime_factorization_tree(encoding_details['prime_factors'])
        print("Prime factorization tree created")
        
        # Symbol mapping chart
        print("Symbol mapping chart created")
        
        # Process flow
        print("Process flow diagram created")
        
        # Prime factor breakdown
        print("Prime factor breakdown created")
        
        print("All visualizations created successfully!")
        print("Note: These are Plotly figures that would be displayed in a web interface")
        
    except Exception as e:
        print(f"Visualization error: {e}")
    
    print("\n" + "=" * 50)

def demo_examples():
    """Demonstrate the examples system."""
    print("Examples Demo")
    print("=" * 50)
    
    examples = GodelExamples()
    
    # Show available categories
    categories = examples.get_categories()
    print(f"Available Categories: {', '.join(categories)}")
    
    # Show examples by difficulty
    difficulties = ["Beginner", "Intermediate", "Advanced", "Expert"]
    
    for difficulty in difficulties:
        difficulty_examples = examples.get_examples_by_difficulty(difficulty)
        if difficulty_examples:
            print(f"\n{difficulty} Examples:")
            for example in difficulty_examples:
                print(f"   • {example.name}: '{example.statement}'")
                print(f"     {example.description}")
    
    # Show progressive sequence
    print(f"\nProgressive Learning Sequence:")
    progressive = examples.get_progressive_sequence()
    for i, example in enumerate(progressive[:5], 1):  # Show first 5
        print(f"   {i}. {example.name} ({example.difficulty})")
    
    print("\n" + "=" * 50)

def demo_utils():
    """Demonstrate utility functions."""
    print("Utils Demo")
    print("=" * 50)
    
    # Prime number utilities
    print("Prime Number Utilities:")
    first_10_primes = utils.get_first_n_primes(10)
    print(f"   First 10 primes: {first_10_primes}")
    
    # Size estimation
    print("\nSize Estimation:")
    for length in [5, 10, 15]:
        estimate = utils.estimate_godel_number_size(length)
        print(f"   {length} symbols → ~{estimate['digits']} digits ({estimate['scientific_notation']})")
    
    print("\n" + "=" * 50)

def demo_custom_paradox():
    """Demonstrate custom paradox creation."""
    print("Custom Paradox Demo")
    print("=" * 50)
    
    encoder = SimplifiedGodelEncoder()
    paradox_gen = ParadoxGenerator(encoder)
    
    # Create a custom paradox
    custom_statement = "The statement with Gödel number G(THIS) is interesting"
    
    try:
        paradox_data = paradox_gen.create_custom_paradox(custom_statement)
        
        if 'error' not in paradox_data:
            print(f"Custom Statement: '{paradox_data['custom_statement']}'")
            print(f"Base Gödel Number: {paradox_data['base_godel_number']:,}")
            print(f"Self-Referential: '{paradox_data['self_referential_statement']}'")
            print(f"Final Gödel Number: {paradox_data['final_godel_number']:,}")
            print(f"Paradox Type: {paradox_data['paradox_type']}")
        else:
            print(f"Error: {paradox_data['error']}")
            
    except Exception as e:
        print(f"Error creating custom paradox: {e}")
    
    print("\n" + "=" * 50)

def main():
    """Run all demos."""
    print("Gödel Numbering Playground - Interactive Demo")
    print("=" * 60)
    print("This demo shows the core functionality without requiring Streamlit.")
    print("=" * 60)
    
    # Run all demos
    demos = [
        ("Basic Encoding", demo_basic_encoding),
        ("Decoding", demo_decoding),
        ("Paradox Generation", demo_paradoxes),
        ("Visualizations", demo_visualizations),
        ("Examples", demo_examples),
        ("Utilities", demo_utils),
        ("Custom Paradox", demo_custom_paradox)
    ]
    
    for demo_name, demo_func in demos:
        print(f"\nRunning {demo_name} Demo...")
        try:
            demo_func()
        except Exception as e:
            print(f"Demo failed: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Demo completed!")
    print("To run the full interactive web app, use: streamlit run app.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
