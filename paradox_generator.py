"""
Paradox Generator - Creates self-referential statements and paradoxes.

This module demonstrates how Gödel numbering enables self-reference,
leading to paradoxes that illustrate the incompleteness theorem.
"""

from typing import Dict, List, Tuple, Optional
from godel_encoder import GodelEncoder


class ParadoxGenerator:
    """
    Generates self-referential statements and paradoxes using Gödel numbering.
    
    This class demonstrates how formal systems can refer to their own
    statements, leading to the famous incompleteness results.
    """
    
    def __init__(self, encoder: GodelEncoder):
        self.encoder = encoder
        self.paradox_templates = self._initialize_templates()
    
    def _initialize_templates(self) -> Dict[str, Dict]:
        """Initialize paradox templates with placeholders for self-reference."""
        return {
            'liar_paradox': {
                'name': 'Liar Paradox',
                'template': 'This statement is false',
                'description': 'A statement that cannot be consistently assigned a truth value.',
                'godel_placeholder': 'G(THIS)',
                'explanation': 'If the statement is true, then it must be false. If it is false, then it must be true.'
            },
            'quine': {
                'name': 'Mathematical Quine',
                'template': 'The statement with Gödel number G(THIS) is unprovable',
                'description': 'A statement that refers to its own Gödel number.',
                'godel_placeholder': 'G(THIS)',
                'explanation': 'This statement claims about itself that it cannot be proven within the formal system.'
            },
            'provability': {
                'name': 'Provability Paradox',
                'template': 'The statement with Gödel number G(THIS) is provable',
                'description': 'A statement about its own provability.',
                'godel_placeholder': 'G(THIS)',
                'explanation': 'This creates a paradox: if provable, it must be true, but if true, it must be provable.'
            },
            'truth': {
                'name': 'Truth Paradox',
                'template': 'The statement with Gödel number G(THIS) is true',
                'description': 'A statement that claims its own truth.',
                'godel_placeholder': 'G(THIS)',
                'explanation': 'This statement refers to itself and claims to be true, creating a circular reference.'
            },
            'consistency': {
                'name': 'Consistency Statement',
                'template': 'The formal system is consistent',
                'description': 'A statement about the consistency of the formal system itself.',
                'godel_placeholder': None,
                'explanation': 'Gödel showed that if a formal system is consistent, it cannot prove its own consistency.'
            }
        }
    
    def generate_self_referential_statement(self, template_name: str, custom_text: str = None) -> Dict:
        """
        Generate a self-referential statement using a template.
        
        Args:
            template_name: Name of the paradox template to use
            custom_text: Optional custom text to replace the template
            
        Returns:
            Dictionary containing the generated statement and metadata
        """
        if template_name not in self.paradox_templates:
            raise ValueError(f"Unknown template: {template_name}")
        
        template = self.paradox_templates[template_name]
        
        if custom_text:
            statement = custom_text
        else:
            statement = template['template']
        
        # Check if the statement contains the placeholder
        has_placeholder = template['godel_placeholder'] in statement if template['godel_placeholder'] else False
        
        # Generate the statement without self-reference first
        base_statement = statement.replace(template['godel_placeholder'], '') if has_placeholder else statement
        
        # Encode the base statement
        try:
            godel_number, encoding_details = self.encoder.encode_statement(base_statement)
        except Exception as e:
            return {
                'error': str(e),
                'template_name': template_name,
                'template': template,
                'custom_text': custom_text
            }
        
        # Create the self-referential version
        if has_placeholder:
            self_referential_statement = statement.replace(template['godel_placeholder'], str(godel_number))
            
            # Now encode the self-referential version
            try:
                final_godel_number, final_encoding = self.encoder.encode_statement(self_referential_statement)
            except Exception as e:
                return {
                    'error': str(e),
                    'template_name': template_name,
                    'base_statement': base_statement,
                    'base_godel_number': godel_number,
                    'self_referential_statement': self_referential_statement
                }
        else:
            self_referential_statement = statement
            final_godel_number = godel_number
            final_encoding = encoding_details
        
        return {
            'template_name': template_name,
            'template': template,
            'base_statement': base_statement,
            'base_godel_number': godel_number,
            'self_referential_statement': self_referential_statement,
            'final_godel_number': final_godel_number,
            'final_encoding': final_encoding,
            'has_self_reference': has_placeholder,
            'paradox_type': self._classify_paradox(template_name, statement)
        }
    
    def _classify_paradox(self, template_name: str, statement: str) -> str:
        """Classify the type of paradox generated."""
        if 'false' in statement.lower():
            return 'Truth Value Paradox'
        elif 'unprovable' in statement.lower():
            return 'Provability Paradox'
        elif 'provable' in statement.lower():
            return 'Provability Paradox'
        elif 'consistent' in statement.lower():
            return 'Meta-mathematical Paradox'
        else:
            return 'Self-Reference Paradox'
    
    def create_custom_paradox(self, statement: str, placeholder: str = 'G(THIS)') -> Dict:
        """
        Create a custom self-referential statement.
        
        Args:
            statement: The statement template with placeholder
            placeholder: The placeholder to replace with Gödel number
            
        Returns:
            Dictionary containing the generated paradox
        """
        if placeholder not in statement:
            return {
                'error': f"Placeholder '{placeholder}' not found in statement"
            }
        
        # Remove placeholder to get base statement
        base_statement = statement.replace(placeholder, '')
        
        try:
            godel_number, encoding_details = self.encoder.encode_statement(base_statement)
        except Exception as e:
            return {
                'error': str(e),
                'statement': statement,
                'placeholder': placeholder
            }
        
        # Create self-referential version
        self_referential_statement = statement.replace(placeholder, str(godel_number))
        
        # Encode the final version
        try:
            final_godel_number, final_encoding = self.encoder.encode_statement(self_referential_statement)
        except Exception as e:
            return {
                'error': str(e),
                'statement': statement,
                'base_statement': base_statement,
                'base_godel_number': godel_number,
                'self_referential_statement': self_referential_statement
            }
        
        return {
            'custom_statement': statement,
            'placeholder': placeholder,
            'base_statement': base_statement,
            'base_godel_number': godel_number,
            'self_referential_statement': self_referential_statement,
            'final_godel_number': final_godel_number,
            'final_encoding': final_encoding,
            'paradox_type': 'Custom Self-Reference Paradox'
        }
    
    def get_paradox_examples(self) -> List[Dict]:
        """Get all available paradox examples."""
        examples = []
        
        for template_name, template in self.paradox_templates.items():
            try:
                example = self.generate_self_referential_statement(template_name)
                if 'error' not in example:
                    examples.append(example)
            except Exception as e:
                examples.append({
                    'template_name': template_name,
                    'template': template,
                    'error': str(e)
                })
        
        return examples
    
    def analyze_paradox(self, paradox_data: Dict) -> Dict:
        """
        Analyze a paradox for educational purposes.
        
        Args:
            paradox_data: The paradox data from generate_self_referential_statement
            
        Returns:
            Analysis of the paradox
        """
        if 'error' in paradox_data:
            return {'error': paradox_data['error']}
        
        analysis = {
            'paradox_name': paradox_data['template']['name'],
            'paradox_type': paradox_data['paradox_type'],
            'explanation': paradox_data['template']['explanation'],
            'self_reference_mechanism': self._explain_self_reference(paradox_data),
            'godel_numbering_analysis': self._analyze_godel_numbering(paradox_data),
            'incompleteness_connection': self._explain_incompleteness_connection(paradox_data)
        }
        
        return analysis
    
    def _explain_self_reference(self, paradox_data: Dict) -> str:
        """Explain how self-reference works in this paradox."""
        if paradox_data['has_self_reference']:
            return f"""
            This paradox uses self-reference through Gödel numbering:
            1. The base statement '{paradox_data['base_statement']}' gets encoded to {paradox_data['base_godel_number']}
            2. This number is then substituted back into the statement
            3. The final statement '{paradox_data['self_referential_statement']}' refers to itself
            4. This creates a circular reference that cannot be resolved consistently
            """
        else:
            return "This paradox doesn't use explicit self-reference but demonstrates meta-mathematical concepts."
    
    def _analyze_godel_numbering(self, paradox_data: Dict) -> str:
        """Analyze the Gödel numbering process for this paradox."""
        if 'final_encoding' in paradox_data:
            encoding = paradox_data['final_encoding']
            return f"""
            Gödel Numbering Analysis:
            - Statement length: {len(encoding['symbols'])} symbols
            - Final Gödel number: {encoding['godel_number']}
            - Prime factors: {encoding['prime_factors']}
            - Each symbol position gets a unique prime number
            - Symbol codes are used as powers of these primes
            """
        else:
            return "Gödel numbering analysis not available."
    
    def _explain_incompleteness_connection(self, paradox_data: Dict) -> str:
        """Explain how this paradox connects to Gödel's incompleteness theorem."""
        if 'unprovable' in paradox_data.get('self_referential_statement', '').lower():
            return """
            This paradox directly demonstrates Gödel's First Incompleteness Theorem:
            - The statement claims it cannot be proven
            - If the system could prove it, the statement would be false (contradiction)
            - If the system cannot prove it, the statement is true but unprovable
            - Therefore, the formal system is incomplete
            """
        elif 'consistent' in paradox_data.get('self_referential_statement', '').lower():
            return """
            This connects to Gödel's Second Incompleteness Theorem:
            - A consistent formal system cannot prove its own consistency
            - If it could, it would create a contradiction
            - This shows the fundamental limitations of formal systems
            """
        else:
            return """
            This paradox illustrates the general principle that self-reference
            in formal systems can lead to undecidable statements, which is
            the core insight behind Gödel's incompleteness theorems.
            """
