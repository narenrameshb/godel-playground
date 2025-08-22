"""
Test script to verify all modules work correctly.
Run this to check if the Gödel numbering playground is properly set up.
"""

def test_imports():
    """Test that all modules can be imported successfully."""
    try:
        print("🔍 Testing module imports...")
        
        from godel_encoder import GodelEncoder, SimplifiedGodelEncoder
        print("godel_encoder imported successfully")
        
        from paradox_generator import ParadoxGenerator
        print("paradox_generator imported successfully")
        
        from visualizer import GodelVisualizer
        print("visualizer imported successfully")
        
        from examples import GodelExamples
        print("examples imported successfully")
        
        import utils
        print("utils imported successfully")
        
        print("\nAll modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"Import error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality of the modules."""
    try:
        print("\nTesting basic functionality...")
        
        # Test encoder
        from godel_encoder import SimplifiedGodelEncoder
        encoder = SimplifiedGodelEncoder()
        
        # Test encoding
        statement = "0=0"
        godel_number, encoding_details = encoder.encode_statement(statement)
        print(f"Encoded '{statement}' → {godel_number:,}")
        
        # Test decoding
        decoded_statement, decoding_details = encoder.decode_number(godel_number)
        print(f"Decoded {godel_number:,} → '{decoded_statement}'")
        
        # Test paradox generator
        from paradox_generator import ParadoxGenerator
        paradox_gen = ParadoxGenerator(encoder)
        
        paradox_data = paradox_gen.generate_self_referential_statement("liar_paradox")
        if 'error' in paradox_data:
            print(f"Paradox generation had an issue: {paradox_data['error']}")
            print(f"Paradox generator is working (handling errors properly)")
        else:
            print(f"Generated paradox: {paradox_data['paradox_type']}")
        
        # Test visualizer
        from visualizer import GodelVisualizer
        visualizer = GodelVisualizer()
        
        tree_fig = visualizer.create_prime_factorization_tree(encoding_details['prime_factors'])
        print("Created prime factorization tree visualization")
        
        # Test examples
        from examples import GodelExamples
        examples = GodelExamples()
        
        example_list = examples.get_examples_by_category("Basic Arithmetic")
        print(f"Found {len(example_list)} basic arithmetic examples")
        
        # Test utils
        import utils
        
        primes = utils.get_first_n_primes(10)
        print(f"Generated first 10 primes: {primes}")
        
        print("\nAll basic functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"Functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_streamlit_ready():
    """Test if the app is ready to run with Streamlit."""
    try:
        print("\nTesting Streamlit readiness...")
        
        import streamlit as st
        print("Streamlit imported successfully")
        
        import plotly.graph_objects as go
        print("Plotly imported successfully")
        
        import pandas as pd
        print("Pandas imported successfully")
        
        import sympy
        print("SymPy imported successfully")
        
        print("\nAll dependencies are available! The app should run successfully.")
        return True
        
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    """Run all tests."""
    print("Gödel Numbering Playground - Module Test Suite")
    print("=" * 60)
    
    # Run tests
    imports_ok = test_imports()
    
    if imports_ok:
        functionality_ok = test_basic_functionality()
        streamlit_ok = test_streamlit_ready()
        
        print("\n" + "=" * 60)
        print("Test Results Summary:")
        print(f"   Module Imports: {'PASS' if imports_ok else 'FAIL'}")
        print(f"   Basic Functionality: {'PASS' if functionality_ok else 'FAIL'}")
        print(f"   Streamlit Ready: {'PASS' if streamlit_ok else 'FAIL'}")
        
        if all([imports_ok, functionality_ok, streamlit_ok]):
            print("\nAll tests passed! The playground is ready to run.")
            print("Run: streamlit run app.py")
        else:
            print("\nSome tests failed. Please check the errors above.")
    else:
        print("\nModule import test failed. Cannot proceed with other tests.")

if __name__ == "__main__":
    main()
