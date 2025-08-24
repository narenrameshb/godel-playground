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
                historical_context="Universal quantifiers are fundamental to mathematical logic.",
                learning_objectives=[
                    "Understand universal quantification",
                    "See how quantifiers are encoded",
                    "Learn about logical structure"
                ],
                related_concepts=["Universal quantifier", "Logical structure", "Identity"]
            ),
            
            # Advanced Examples
            GodelExample(
                name="Peano Axiom",
                statement="∀x(S(x)≠0)",
                description="Peano axiom stating that zero is not the successor of any number.",
                category="Advanced Logic",
                difficulty="Advanced",
                historical_context="This is one of Peano's fundamental axioms for arithmetic.",
                learning_objectives=[
                    "Understand complex logical statements",
                    "See how multiple concepts combine",
                    "Learn about axiomatic systems"
                ],
                related_concepts=["Peano axioms", "Complex logic", "Axiomatic systems"]
            ),
            
            GodelExample(
                name="Mathematical Induction",
                statement="∀x(P(x)→P(S(x)))",
                description="Induction step: if P holds for x, it holds for the successor of x.",
                category="Advanced Logic",
                difficulty="Advanced",
                historical_context="Mathematical induction is a fundamental proof technique.",
                learning_objectives=[
                    "Understand implication in logic",
                    "See complex quantifier structures",
                    "Learn about mathematical induction"
                ],
                related_concepts=["Mathematical induction", "Implication", "Complex logic"]
            )
        ]
    
    def _get_categories(self) -> List[str]:
        """Get unique categories from examples."""
        return list(set(example.category for example in self.examples))
    
    def get_examples_by_category(self, category: str) -> List[GodelExample]:
        """Get examples filtered by category."""
        return [example for example in self.examples if example.category == category]
    
    def get_examples_by_difficulty(self, difficulty: str) -> List[GodelExample]:
        """Get examples filtered by difficulty level."""
        return [example for example in self.examples if example.difficulty == difficulty]
    
    def get_example_by_name(self, name: str) -> GodelExample:
        """Get a specific example by name."""
        for example in self.examples:
            if example.name == name:
                return example
        return None
    
    def get_random_example(self) -> GodelExample:
        """Get a random example from the collection."""
        import random
        return random.choice(self.examples)
    
    def search_examples(self, query: str) -> List[GodelExample]:
        """Search examples by name, description, or concepts."""
        query = query.lower()
        results = []
        
        for example in self.examples:
            if (query in example.name.lower() or 
                query in example.description.lower() or
                any(query in concept.lower() for concept in example.related_concepts)):
                results.append(example)
        
        return results
    
    def get_learning_progression(self) -> Dict[str, List[GodelExample]]:
        """Get examples organized by learning progression."""
        return {
            'Beginner': self.get_examples_by_difficulty('Beginner'),
            'Intermediate': self.get_examples_by_difficulty('Intermediate'),
            'Advanced': self.get_examples_by_difficulty('Advanced')
        }
    
    def get_category_summary(self) -> Dict[str, Dict]:
        """Get summary statistics for each category."""
        summary = {}
        
        for category in self.categories:
            examples = self.get_examples_by_category(category)
            difficulties = [ex.difficulty for ex in examples]
            
            summary[category] = {
                'count': len(examples),
                'difficulties': list(set(difficulties)),
                'examples': [ex.name for ex in examples]
            }
        
        return summary
