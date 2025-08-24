"""
Interactive Gödel Numbering Playground - Main Streamlit Application.

This is the main application that demonstrates Gödel numbering and self-reference
in mathematical logic through an interactive web interface.
"""

import streamlit as st
import pandas as pd
from typing import Dict

# Import our modules
from godel_encoder import GodelEncoder, SimplifiedGodelEncoder
from paradox_generator import ParadoxGenerator
from visualizer import GodelVisualizer
from examples import GodelExamples
import utils

# Page configuration
st.set_page_config(
    page_title="Gödel Numbering Playground",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
    }
    .math-display {
        font-family: 'Courier New', monospace;
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 0.25rem;
        border: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'encoder' not in st.session_state:
    st.session_state.encoder = SimplifiedGodelEncoder()
if 'paradox_generator' not in st.session_state:
    st.session_state.paradox_generator = ParadoxGenerator(st.session_state.encoder)
if 'visualizer' not in st.session_state:
    st.session_state.visualizer = GodelVisualizer()
if 'examples' not in st.session_state:
    st.session_state.examples = GodelExamples()

# Main header
st.markdown('<h1 class="main-header">Gödel Numbering Playground</h1>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="font-size: 1.2rem; color: #666;">
        Explore Gödel's incompleteness theorem through interactive visualization of 
        how logical statements become numbers, enabling self-reference and paradoxes.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Quick Examples")
    
    # Quick example buttons
    demo_statements = utils.create_demo_statements()
    selected_example = st.selectbox("Choose a demo statement:", demo_statements)
    
    if st.button("Try This Example"):
        st.session_state.current_statement = selected_example
        st.session_state.active_tab = "Encode"
        st.rerun()
    
    st.markdown("---")
    
    # Symbol reference table
    st.header("Symbol Reference")
    symbol_map = st.session_state.encoder.get_symbol_table()
    
    # Create a compact symbol table
    symbol_df = pd.DataFrame([
        {"Symbol": symbol, "Code": code} 
        for symbol, code in symbol_map.items()
    ])
    
    st.dataframe(symbol_df, use_container_width=True)
    
    st.markdown("---")
    
    # Settings
    st.header("Settings")
    use_simplified = st.checkbox("Use Simplified Mode", value=True, 
                                help="Use smaller numbers for easier demonstration")
    
    if use_simplified != isinstance(st.session_state.encoder, SimplifiedGodelEncoder):
        if use_simplified:
            st.session_state.encoder = SimplifiedGodelEncoder()
        else:
            st.session_state.encoder = GodelEncoder()
        st.session_state.paradox_generator = ParadoxGenerator(st.session_state.encoder)
        st.rerun()

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Encode", "Decode", "Paradoxes", "Interactive Demo"
])

# Tab 1: Encode
with tab1:
    st.header("Encode Logical Statements to Gödel Numbers")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input section
        st.subheader("Input Statement")
        statement = st.text_input(
            "Enter a logical statement:",
            value=st.session_state.get('current_statement', '0=0'),
            placeholder="e.g., 0=0, S(0), x+0=x, ∀x(x=x)",
            help="Use supported symbols: 0, S, +, ×, =, (, ), ¬, →, ∀, ∃, a-z variables"
        )
        
        if st.button("Encode Statement", type="primary"):
            if statement.strip():
                try:
                    godel_number, encoding_details = st.session_state.encoder.encode_statement(statement)
                    st.session_state.current_encoding = encoding_details
                    st.session_state.current_godel_number = godel_number
                    st.success(f"Successfully encoded! Gödel number: {godel_number:,}")
                except Exception as e:
                    st.error(f"Encoding error: {str(e)}")
            else:
                st.warning("Please enter a statement to encode.")
    
    with col2:
        # Quick info
        st.subheader("How It Works")
        st.markdown("""
        1. **Break down** statement into symbols
        2. **Assign codes** to each symbol
        3. **Assign primes** to each position
        4. **Calculate** prime^code for each position
        5. **Multiply** all results together
        """)
        
        # Size estimator
        if statement:
            try:
                size_estimate = utils.estimate_godel_number_size(len(statement))
                st.info(f"**Estimated size:** {size_estimate['digits']} digits")
            except:
                pass

# Tab 2: Decode
with tab2:
    st.header("Decode Gödel Numbers to Statements")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Input Gödel Number")
        godel_input = st.text_input(
            "Enter a Gödel number to decode:",
            placeholder="e.g., 51840, 123456789",
            help="Enter a natural number to see what statement it represents"
        )
        
        if st.button("Decode Number", type="primary"):
            if godel_input.strip():
                try:
                    godel_number = int(godel_input)
                    decoded_statement, decoding_details = st.session_state.encoder.decode_number(godel_number)
                    st.session_state.current_decoding = decoding_details
                    st.session_state.current_decoded_statement = decoded_statement
                    st.success(f"Successfully decoded! Statement: `{decoded_statement}`")
                except ValueError:
                    st.error("Please enter a valid integer.")
                except Exception as e:
                    st.error(f"Decoding error: {str(e)}")
            else:
                st.warning("Please enter a number to decode.")

# Tab 3: Paradoxes
with tab3:
    st.header("Self-Reference and Paradoxes")
    
    st.markdown("""
    This section demonstrates how Gödel numbering enables self-reference, 
    leading to paradoxes that illustrate the incompleteness theorem.
    """)
    
    # Paradox templates
    st.subheader("Paradox Templates")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Choose a paradox template:**")
        paradox_type = st.selectbox(
            "Paradox Type:",
            ["liar_paradox", "quine", "provability", "truth", "consistency"],
            format_func=lambda x: {
                "liar_paradox": "Liar Paradox",
                "quine": "Mathematical Quine",
                "provability": "Provability Paradox",
                "truth": "Truth Paradox",
                "consistency": "Consistency Statement"
            }[x]
        )
        
        if st.button("Generate Paradox", type="primary"):
            try:
                paradox_data = st.session_state.paradox_generator.generate_self_referential_statement(paradox_type)
                st.session_state.current_paradox = paradox_data
                st.success("Paradox generated successfully!")
            except Exception as e:
                st.error(f"Error generating paradox: {str(e)}")

# Tab 4: Interactive Demo
with tab4:
    st.header("Interactive Gödel Numbering Demo")
    
    st.markdown("""
    This section provides a step-by-step interactive demonstration of how Gödel numbering works.
    Enter a logical statement and see exactly how it gets converted to a number!
    """)
    
    # Demo statement input
    col1, col2 = st.columns([3, 1])
    
    with col1:
        demo_statement = st.text_input(
            "Enter a logical statement:",
            value="x=0",
            placeholder="Try: 0=0, S(0), x+0=x, ∀x(x=x)"
        )
    
    with col2:
        st.markdown("**Quick Examples:**")
        if st.button("0=0", key="ex1"):
            demo_statement = "0=0"
            st.rerun()
        if st.button("S(0)", key="ex2"):
            demo_statement = "S(0)"
            st.rerun()
        if st.button("x=0", key="ex3"):
            demo_statement = "x=0"
            st.rerun()
    
    if st.button("Start Interactive Demo", type="primary"):
        if demo_statement.strip():
            try:
                # Encode the statement
                godel_number, encoding_details = st.session_state.encoder.encode_statement(demo_statement)
                
                st.success(f"Successfully encoded: '{demo_statement}' → {godel_number:,}")
                
                # Step-by-step breakdown
                st.subheader("Step-by-Step Breakdown")
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Statement Analysis:**")
                    st.markdown(f"- **Statement:** `{demo_statement}`")
                    st.markdown(f"- **Length:** {len(demo_statement)} symbols")
                    st.markdown(f"- **Final Gödel Number:** {godel_number:,}")
                    
                    # Symbol breakdown table
                    st.markdown("**Symbol Breakdown:**")
                    symbol_data = []
                    for item in encoding_details['symbol_codes']:
                        contribution = item['prime'] ** item['code']
                        symbol_data.append({
                            "Position": item['position'],
                            "Symbol": item['symbol'],
                            "Code": item['code'],
                            "Prime": item['prime'],
                            "Power": item['code'],
                            "Contribution": f"{contribution:,}"
                        })
                    
                    symbol_df = pd.DataFrame(symbol_data)
                    st.dataframe(symbol_df, use_container_width=True)
                
                with col2:
                    st.markdown("**Mathematical Process:**")
                    st.markdown("**Formula:** ∏(position_prime ^ symbol_code)")
                    
                    # Show the calculation
                    calculation_steps = []
                    for item in encoding_details['symbol_codes']:
                        step = f"{item['prime']}^{item['code']} = {item['prime'] ** item['code']:,}"
                        calculation_steps.append(step)
                    
                    st.markdown("**Steps:**")
                    for i, step in enumerate(calculation_steps):
                        st.markdown(f"{i+1}. {step}")
                    
                    st.markdown("**Final:** " + " × ".join(calculation_steps))
                    st.markdown(f"**Result:** {godel_number:,}")
                
                # Prime factorization visualization
                st.subheader("Prime Factorization Tree")
                tree_fig = st.session_state.visualizer.create_prime_factorization_tree(
                    encoding_details['prime_factors'],
                    f"Prime Factorization of '{demo_statement}' → {godel_number:,}"
                )
                st.plotly_chart(tree_fig, use_container_width=True)
                
                # Symbol mapping chart
                st.subheader("Symbol to Number Mapping")
                mapping_fig = st.session_state.visualizer.create_symbol_mapping_chart(
                    encoding_details,
                    f"Symbol Mapping for '{demo_statement}'"
                )
                st.plotly_chart(mapping_fig, use_container_width=True)
                
                # Process flow
                st.subheader("Encoding Process Flow")
                flow_fig = st.session_state.visualizer.create_encoding_process_flow(encoding_details)
                st.plotly_chart(flow_fig, use_container_width=True)
                
                # Interactive exploration
                st.subheader("Interactive Exploration")
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Try decoding this number back:**")
                    if st.button("Decode Back to Statement"):
                        try:
                            decoded_statement, decoding_details = st.session_state.encoder.decode_number(godel_number)
                            if decoded_statement == demo_statement:
                                st.success(f"Perfect! Decoded back to: '{decoded_statement}'")
                            else:
                                st.warning(f"Decoded to: '{decoded_statement}' (should be '{demo_statement}')")
                        except Exception as e:
                            st.error(f"Decoding error: {str(e)}")
                
                with col2:
                    st.markdown("**Compare with other statements:**")
                    compare_statements = ["0=0", "S(0)", "x=0", "0+0=0"]
                    if demo_statement not in compare_statements:
                        compare_statements.append(demo_statement)
                    
                    selected_compare = st.selectbox("Choose to compare:", compare_statements)
                    if st.button("Compare"):
                        try:
                            compare_number, compare_details = st.session_state.encoder.encode_statement(selected_compare)
                            st.info(f"'{selected_compare}' → {compare_number:,}")
                            
                            # Show size comparison
                            if compare_number > godel_number:
                                st.markdown(f"**'{selected_compare}' is {compare_number/godel_number:.1f}x larger**")
                            elif compare_number < godel_number:
                                st.markdown(f"**'{demo_statement}' is {godel_number/compare_number:.1f}x larger**")
                            else:
                                st.markdown("**Both statements have the same Gödel number**")
                        except Exception as e:
                            st.error(f"Comparison error: {str(e)}")
                
            except Exception as e:
                st.error(f"Demo error: {str(e)}")
                st.info("Try a simpler statement like '0=0' or 'x=0'")
        else:
            st.warning("Please enter a statement for the demo.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>Gödel Numbering Playground</strong> - Making abstract mathematics tangible and interactive</p>
    <p>Built with Streamlit, Plotly, and mathematical curiosity</p>
</div>
""", unsafe_allow_html=True)
