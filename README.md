# Gödel Numbering Playground

A web app that shows how Gödel numbering works - turning logical statements into numbers using prime factorization. Lets you explore self-reference and paradoxes in math.

## What it does

- **Gödel Numbering**: Converts logical statements to numbers using prime factorization
- **Web Interface**: Streamlit app with real-time encoding/decoding
- **Paradox Generation**: Creates self-referential statements and analyzes paradoxes
- **Visualizations**: Shows prime factorization trees and charts
- **Examples**: Goes from basic to advanced concepts

## Getting started

### Requirements
- Python 3.8+
- pip

### Setup
```bash
git clone <repository-url>
cd godel-playground
pip install -r requirements.txt
streamlit run app.py
```

## How to use

### Web App
Just run `streamlit run app.py` and open the URL it shows.

### Command line demo
```bash
python demo.py
```

### Run tests
```bash
python test_modules.py
```

## Files

```
godel-playground/
├── app.py                 # Main Streamlit app
├── godel_encoder.py       # Core encoding/decoding logic
├── paradox_generator.py   # Self-reference and paradox creation
├── visualizer.py          # Prime factorization visualizations
├── examples.py            # Educational examples
├── utils.py               # Helper functions
├── test_modules.py        # Tests
├── demo.py                # Command line demo
├── requirements.txt       # Dependencies
├── setup.py               # Package config
├── README.md              # This file
├── CHANGELOG.md           # History
└── LICENSE                # MIT License
```

## Supported symbols

| Type | Symbols | What they mean |
|------|---------|----------------|
| Constants | `0` | Zero |
| Functions | `S` | Successor function |
| Operations | `+`, `×` | Addition, multiplication |
| Relations | `=` | Equality |
| Logic | `¬`, `→`, `∀`, `∃` | Negation, implication, quantifiers |
| Variables | `a`, `b`, `c`, `x`, `y`, `z` | Variables |
| Punctuation | `(`, `)` | Parentheses |

## How Gödel numbering works

1. **Symbol Encoding**: Each symbol gets a unique prime number code
2. **Position Encoding**: Each position gets a unique prime number
3. **Power Calculation**: Raise each position prime to the power of the symbol code
4. **Final Number**: Multiply all results together

**Example**: `x=0`
- Symbols: `x` (code 47), `=` (code 11), `0` (code 2)
- Positions: 1st (prime 2), 2nd (prime 3), 3rd (prime 5)
- Calculation: 2^47 × 3^11 × 5^2
- Result: A very large number representing the statement

## Development

### Testing
```bash
python test_modules.py
```

### Quality checks
```bash
pip install -e .[dev]
```

## Contributing

1. Fork the repo
2. Create a feature branch
3. Make changes
4. Run tests
5. Submit a pull request
