"""
Examples - Pre-built famous examples and educational content.

This module contains famous mathematical statements, paradoxes, and
progressive examples to help users understand Gödel numbering concepts.
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class GodelExample:
    """Data structure for Gödel numbering examples."""
    name: str
    statement: str
    description: str
    category: str
    difficulty: str
    historical_context: str
    learning_objectives: List[str]
    related_concepts: List[str]


class GodelExamples:
    """Collection of pre-built examples for Gödel numbering demonstrations."""
    
    def __init__(self):
        self.examples = self._initialize_examples()
        self.categories = self._get_categories()
    
    def _initialize_examples(self) -> List[GodelExample]:
        """Initialize the collection of examples."""
        return [
            # Basic Arithmetic Examples
            GodelExample(
                name="Zero Equality",
                statement="0=0",
                description="The simplest possible arithmetic statement asserting that zero equals itself.",
                category="Basic Arithmetic",
                difficulty="Beginner",
                historical_context="This represents the most fundamental arithmetic truth, often used as an axiom.",
                learning_objectives=[
                    "Understand basic symbol encoding",
                    "See how simple statements map to numbers",
                    "Learn the role of equality in formal systems"
                ],
                related_concepts=["Equality", "Axioms", "Basic arithmetic"]
            ),
            
            GodelExample(
                name="Successor Function",
                statement="S(0)",
                description="The successor of zero, representing the number 1 in Peano arithmetic.",
                category="Basic Arithmetic",
                difficulty="Beginner",
                historical_context="The successor function is fundamental to Peano's axiomatization of arithmetic.",
                learning_objectives=[
                    "Learn about the successor function",
                    "Understand function notation",
                    "See how parentheses are encoded"
                ],
                related_concepts=["Successor function", "Peano arithmetic", "Function notation"]
            ),
            
            GodelExample(
                name="Simple Addition",
                statement="0+0=0",
                description="Basic addition statement showing how arithmetic operations are encoded.",
                category="Basic Arithmetic",
                difficulty="Beginner",
                historical_context="Addition is one of the fundamental operations in arithmetic.",
                learning_objectives=[
                    "See addition operation encoding",
                    "Understand multi-symbol statements",
                    "Learn about arithmetic operations"
                ],
                related_concepts=["Addition", "Arithmetic operations", "Equality"]
            ),
            
            # Intermediate Examples
            GodelExample(
                name="Variable Assignment",
                statement="x=0",
                description="A statement assigning a value to a variable.",
                category="Variables and Logic",
                difficulty="Intermediate",
                historical_context="Variables allow us to make general statements about numbers.",
                learning_objectives=[
                    "Learn about variable encoding",
                    "Understand assignment statements",
                    "See how variables differ from constants"
                ],
                related_concepts=["Variables", "Assignment", "Generalization"]
            ),
            
            GodelExample(
                name="Universal Quantifier",
                statement="∀x(x=x)",
                description="A universal statement claiming that every number equals itself.",
                category="Variables and Logic",
                difficulty="Intermediate",
                historical_context="Universal quantifiers allow us to make statements about all objects.",
                learning_objectives=[
                    "Learn about universal quantifiers",
                    "Understand logical structure",
                    "See how quantifiers are encoded"
                ],
                related_concepts=["Universal quantifiers", "Logical structure", "Identity"]
            ),
            
            # Advanced Examples
            GodelExample(
                name="Gödel Sentence Template",
                statement="The statement with Gödel number G(THIS) is unprovable",
                description="A template for creating Gödel's famous undecidable statement.",
                category="Self-Reference",
                difficulty="Expert",
                historical_context="This is the core of Gödel's first incompleteness theorem.",
                learning_objectives=[
                    "Understand Gödel's incompleteness",
                    "Learn about self-reference",
                    "See undecidable statements"
                ],
                related_concepts=["Gödel's incompleteness", "Self-reference", "Undecidability"]
            )
        ]
    
    def _get_categories(self) -> List[str]:
        """Get all available categories."""
        return list(set(example.category for example in self.examples))
    
    def get_examples_by_category(self, category: str) -> List[GodelExample]:
        """Get examples filtered by category."""
        return [ex for ex in self.examples if ex.category == category]
    
    def get_examples_by_difficulty(self, difficulty: str) -> List[GodelExample]:
        """Get examples filtered by difficulty level."""
        return [ex for ex in self.examples if ex.difficulty == difficulty]
    
    def get_progressive_sequence(self) -> List[GodelExample]:
        """Get examples in a progressive learning sequence."""
        difficulty_order = ["Beginner", "Intermediate", "Advanced", "Expert"]
        progressive = []
        
        for difficulty in difficulty_order:
            difficulty_examples = self.get_examples_by_difficulty(difficulty)
            progressive.extend(difficulty_examples)
        
        return progressive
    
    def get_categories(self) -> List[str]:
        """Get all available categories."""
        return self.categories
