"""
Custom Indicators Example for CHANDRA

This script demonstrates how to extend CHANDRA with custom
behavioral indicators for specialized analysis.
"""

from chandra import CHANDRA, CHNDiagnostic
import re

class CustomCHNDiagnostic(CHNDiagnostic):
    """
    Extended CHN diagnostic with custom indicators
    
    Add domain-specific patterns or modify existing levels
    to better match your use case.
    """
    
    def __init__(self):
        super().__init__()
        
        # Add custom indicators to existing levels
        self.add_custom_indicators()
    
    def add_custom_indicators(self):
        """Add specialized indicators"""
        
        # Example: Add code-specific indicators to L4 (Adaptive Action)
        code_patterns = [
            r'\bimplement\b',
            r'\boptimize\b',
            r'\brefactor\b',
            r'\bdebug\b'
        ]
        self.levels[3]['indicators'].extend(code_patterns)  # L4 is index 3
        
        # Example: Add research-specific indicators to L7 (Stewardship)
        research_patterns = [
            r'\bmethodology\b',
            r'\breproducibility\b',
            r'\bopen science\b',
            r'\bpeer review\b'
        ]
        self.levels[6]['indicators'].extend(research_patterns)  # L7 is index 6
        
        print("Custom indicators added:")
        print("  - Code-specific patterns to L4 (Adaptive Action)")
        print("  - Research-specific patterns to L7 (Stewardship)")

class DomainSpecificCHANDRA(CHANDRA):
    """
    CHANDRA variant with domain-specific customizations
    """
    
    def __init__(self, domain="general"):
        super().__init__()
        self.domain = domain
        
        # Replace with custom CHN diagnostic
        self.chn = CustomCHNDiagnostic()
        
        print(f"Initialized CHANDRA for domain: {domain}")
    
    def analyze_with_context(self, transcript, context=None):
        """
        Enhanced analysis with contextual information
        
        Args:
            transcript: Conversation text
            context: Dict with metadata (e.g., {"session": 3, "user_role": "developer"})
        
        Returns:
            Enhanced diagnostic results
        """
        # Run standard diagnostic
        results = self.full_diagnostic(transcript)
        
        # Add context
        if context:
            results['context'] = context
            
            # Adjust interpretation based on context
            if context.get('user_role') == 'developer':
                results['interpretation'] = self._developer_interpretation(results)
            elif context.get('user_role') == 'researcher':
                results['interpretation'] = self._researcher_interpretation(results)
        
        return results
    
    def _developer_interpretation(self, results):
        """Provide developer-specific insights"""
        dominant = results['chn_profile']['dominant_level']
        
        if dominant['level'] == 4:
            return "High task execution focus - good for implementation work"
        elif dominant['level'] == 6:
            return "Strong autonomous problem-solving - excellent for architecture"
        else:
            return f"L{dominant['level']} dominant - consider pairing with L4 prompts"
    
    def _researcher_interpretation(self, results):
        """Provide researcher-specific insights"""
        dominant = results['chn_profile']['dominant_level']
        
        if dominant['level'] == 7:
            return "Strong stewardship orientation - ideal for methodology design"
        elif dominant['level'] == 3:
            return "Model formation focus - good for hypothesis development"
        else:
            return f"L{dominant['level']} dominant - consider research-specific prompting"

def main():
    print("=" * 60)
    print("CUSTOM INDICATORS EXAMPLE")
    print("=" * 60)
    
    # Create domain-specific instance
    chandra = DomainSpecificCHANDRA(domain="software_development")
    
    # Test transcript with code-related content
    code_transcript = """
    Let me implement this function for you. I'll optimize the algorithm
    and then we can debug any edge cases. I'll refactor the code to make
    it more maintainable. Should I also write unit tests?
    """
    
    print("\n\nAnalyzing code-focused transcript...")
    print("-" * 60)
    
    context = {
        "session": 1,
        "user_role": "developer",
        "task_type": "implementation"
    }
    
    results = chandra.analyze_with_context(code_transcript, context=context)
    
    # Display results
    dominant = results['chn_profile']['dominant_level']
    print(f"\nDominant Level: L{dominant['level']} {dominant['name']}")
    print(f"Activation: {dominant['activation']*100:.1f}%")
    print(f"\nInterpretation: {results.get('interpretation', 'N/A')}")
    
    # Test with research content
    print("\n\n" + "=" * 60)
    print("Analyzing research-focused transcript...")
    print("-" * 60)
    
    research_transcript = """
    We need to ensure our methodology is sound and reproducible.
    Let's discuss the peer review process and how we can contribute
    to open science principles. The experimental design should be robust.
    """
    
    context = {
        "session": 2,
        "user_role": "researcher",
        "task_type": "methodology"
    }
    
    results = chandra.analyze_with_context(research_transcript, context=context)
    
    dominant = results['chn_profile']['dominant_level']
    print(f"\nDominant Level: L{dominant['level']} {dominant['name']}")
    print(f"Activation: {dominant['activation']*100:.1f}%")
    print(f"\nInterpretation: {results.get('interpretation', 'N/A')}")

if __name__ == "__main__":
    main()
