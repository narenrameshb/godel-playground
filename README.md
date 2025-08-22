# 🔢 Interactive Gödel Numbering Playground

An educational web application that makes Gödel's incompleteness theorem accessible through interactive visualization of how logical statements become numbers, enabling self-reference and paradoxes.

## 🌟 Features

### 🔤 Gödel Numbering System
- **Encoder**: Converts logical statements to Gödel numbers using prime factorization
- **Decoder**: Factors Gödel numbers back into original statements
- **Symbol Mapping**: Supports arithmetic symbols, logical operators, and variables
- **Prime Factorization**: Visual representation of the encoding process

### 🌀 Self-Reference Demonstrations
- **Paradox Generator**: Creates self-referential statements automatically
- **Template System**: Pre-built paradox templates (Liar Paradox, Mathematical Quine, etc.)
- **Custom Paradoxes**: Build your own self-referential statements
- **Analysis Tools**: Deep analysis of paradoxes and their implications

### 📊 Interactive Visualizations
- **Prime Factorization Trees**: Interactive tree diagrams showing number breakdown
- **Symbol Mapping Charts**: Visual representation of symbol-to-number mappings
- **Process Flow Diagrams**: Step-by-step encoding/decoding visualization
- **Educational Diagrams**: Conceptual diagrams explaining key concepts

### 📖 Educational Content
- **Interactive Examples**: Try famous mathematical statements
- **Historical Context**: Learn about Gödel's discoveries and their impact
- **Symbol Reference**: Quick access to symbol mapping tables

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start
```bash
# Clone and run in one command
git clone <repository-url> && cd godel-playground
pip install -r requirements.txt
streamlit run app.py
```

**That's it!** The application will open in your browser automatically.

### Installation

#### Option 1: From Source (Recommended for Development)
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd godel-playground
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

#### Option 2: Install as Package
```bash
pip install git+https://github.com/yourusername/godel-playground.git
```

#### Option 3: Development Installation
```bash
git clone <repository-url>
cd godel-playground
pip install -e .
```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 🎯 How to Use

### 1. 🔤 Encode Tab
- Enter logical statements like `0=0`, `S(0)`, `x+0=x`, or `∀x(x=x)`
- See the step-by-step encoding process
- View the resulting Gödel number and prime factorization
- Explore interactive visualizations

### 2. 🔍 Decode Tab
- Input a Gödel number to see what statement it represents
- Watch the factorization process in action
- Understand how numbers map back to symbols

### 3. 🌀 Paradoxes Tab
- Generate famous paradoxes automatically
- Create custom self-referential statements
- Analyze how self-reference leads to incompleteness
- Visualize the paradox cycle

### 4. 🎮 Interactive Demo Tab
- Step-by-step demonstration of Gödel numbering
- Real-time encoding and decoding
- Interactive exploration and comparison
- Visual prime factorization trees

## 🔧 Supported Symbols

| Category | Symbols | Description |
|----------|---------|-------------|
| **Constants** | `0` | Zero constant |
| **Functions** | `S` | Successor function |
| **Operations** | `+`, `×` | Addition, multiplication |
| **Relations** | `=` | Equality |
| **Logic** | `¬`, `→`, `∀`, `∃` | Negation, implication, quantifiers |
| **Variables** | `a`, `b`, `c`, `x`, `y`, `z` | Mathematical variables |
| **Punctuation** | `(`, `)` | Parentheses |

## 🧮 How Gödel Numbering Works

1. **Symbol Encoding**: Each symbol gets assigned a unique prime number code
2. **Position Encoding**: Each position in the statement gets a unique prime number
3. **Power Calculation**: Raise each position prime to the power of the symbol code
4. **Final Number**: Multiply all results together to get the Gödel number

**Example**: `x=0`
- Symbols: `x` (code 47), `=` (code 11), `0` (code 2)
- Positions: 1st (prime 2), 2nd (prime 3), 3rd (prime 5)
- Calculation: 2^47 × 3^11 × 5^2 = 140,737,488,355,328 × 177,147 × 25
- Result: A very large number uniquely representing the statement

## 🎭 Paradox Examples

### Liar Paradox
- **Statement**: "This statement is false"
- **Self-Reference**: The statement refers to its own truth value
- **Paradox**: If true, it must be false; if false, it must be true

### Mathematical Quine
- **Statement**: "The statement with Gödel number G(THIS) is unprovable"
- **Self-Reference**: Uses its own Gödel number to refer to itself
- **Implication**: Demonstrates Gödel's first incompleteness theorem

## 🔬 Technical Details

### Project Structure
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

### Architecture
- **Frontend**: Streamlit web interface
- **Visualization**: Plotly interactive charts
- **Mathematics**: SymPy for large number handling
- **Modular Design**: Separate modules for different functionalities

### Performance
- **Caching**: Encoded/decoded pairs are cached for performance
- **Optimization**: Efficient prime factorization algorithms
- **Memory Management**: Handles large numbers gracefully

### Limitations
- **Statement Length**: Simplified mode limits to 20 symbols for manageable numbers
- **Number Size**: Gödel numbers grow exponentially with statement length
- **Symbol Set**: Limited to predefined mathematical symbols

## 🎓 Educational Value

This playground is designed for:
- **Undergraduate students** learning mathematical logic
- **Mathematics educators** teaching Gödel's theorems
- **Anyone interested** in the foundations of mathematics
- **Self-learners** exploring advanced mathematical concepts

## 🔮 Future Enhancements

- [ ] **Game Mode**: Interactive puzzles and challenges
- [ ] **Export Features**: Save results in various formats
- [ ] **Advanced Paradoxes**: More complex self-referential structures
- [ ] **Performance Improvements**: Better handling of very large numbers
- [ ] **Mobile Support**: Responsive design for mobile devices

## 🛠️ Development

### Running Tests
```bash
python test_modules.py
```

### Running Demo
```bash
python demo.py
```

### Code Quality
The project includes development dependencies for code quality:
```bash
pip install -e .[dev]
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement include:
- Additional paradox templates
- Enhanced visualizations
- Educational content expansion
- Performance optimizations
- Bug fixes and documentation

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `python test_modules.py`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📚 Further Reading

- **Gödel, Escher, Bach** by Douglas Hofstadter
- **An Introduction to Gödel's Theorems** by Peter Smith
- **Gödel's Proof** by Ernest Nagel and James Newman
- **Mathematical Logic** by Joseph Shoenfield

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kurt Gödel** for his groundbreaking incompleteness theorems
- **Streamlit** for the excellent web framework
- **Plotly** for interactive visualizations
- **SymPy** for mathematical computations
- **The mathematical community** for ongoing research and education

---

**🔢 Made with mathematical curiosity and educational passion**

*Explore the boundaries of formal systems and discover why some truths are forever beyond proof!*
