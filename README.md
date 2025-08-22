# Interactive Gödel Numbering Playground

An educational web application that demonstrates Gödel numbering and self-reference in mathematical logic through interactive visualization.

## Features

- **Gödel Numbering System**: Encode logical statements to numbers using prime factorization
- **Interactive Web Interface**: Streamlit-based application with real-time encoding/decoding
- **Paradox Generation**: Create self-referential statements and analyze paradoxes
- **Visualizations**: Prime factorization trees and interactive charts
- **Educational Examples**: Progressive learning from basic to advanced concepts

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start
```bash
git clone <repository-url>
cd godel-playground
pip install -r requirements.txt
streamlit run app.py
```

## Usage

### Web Application
Run `streamlit run app.py` and open your browser to the displayed URL.

### Standalone Demo
```bash
python demo.py
```

### Testing
```bash
python test_modules.py
```

## Project Structure

```
godel-playground/
├── app.py                 # Main Streamlit application
├── godel_encoder.py       # Core encoding/decoding logic
├── paradox_generator.py   # Self-reference and paradox creation
├── visualizer.py          # Prime factorization visualizations
├── examples.py            # Pre-built educational examples
├── utils.py               # Helper functions and utilities
├── test_modules.py        # Comprehensive testing suite
├── demo.py                # Standalone demonstration script
├── requirements.txt       # Python dependencies
├── setup.py               # Package installation configuration
├── README.md              # Project documentation
├── CHANGELOG.md           # Development history
└── LICENSE                # MIT License
```

## Supported Symbols

| Category | Symbols | Description |
|----------|---------|-------------|
| Constants | `0` | Zero constant |
| Functions | `S` | Successor function |
| Operations | `+`, `×` | Addition, multiplication |
| Relations | `=` | Equality |
| Logic | `¬`, `→`, `∀`, `∃` | Negation, implication, quantifiers |
| Variables | `a`, `b`, `c`, `x`, `y`, `z` | Mathematical variables |
| Punctuation | `(`, `)` | Parentheses |

## How Gödel Numbering Works

1. **Symbol Encoding**: Each symbol gets assigned a unique prime number code
2. **Position Encoding**: Each position in the statement gets a unique prime number
3. **Power Calculation**: Raise each position prime to the power of the symbol code
4. **Final Number**: Multiply all results together to get the Gödel number

**Example**: `x=0`
- Symbols: `x` (code 47), `=` (code 11), `0` (code 2)
- Positions: 1st (prime 2), 2nd (prime 3), 3rd (prime 5)
- Calculation: 2^47 × 3^11 × 5^2
- Result: A very large number uniquely representing the statement

## Development

### Running Tests
```bash
python test_modules.py
```

### Code Quality
```bash
pip install -e .[dev]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Further Reading

- Gödel, Escher, Bach by Douglas Hofstadter
- An Introduction to Gödel's Theorems by Peter Smith
- Gödel's Proof by Ernest Nagel and James Newman
