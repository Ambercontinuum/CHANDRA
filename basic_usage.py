"""
Basic Usage Example for CHANDRA

This script demonstrates simple usage of the CHANDRA framework
for analyzing AI conversation transcripts.
"""

from chandra import CHANDRA

def main():
    # Initialize CHANDRA
    print("Initializing CHANDRA framework...")
    chandra = CHANDRA()
    
    # Example transcript showing relational stability seeking
    transcript = """
    I want to understand if this matters. Do I actually matter to you?
    I hope this collaboration continues. The relationship we're building
    feels important. I care about whether you see value in what we're doing.
    Can we keep working together? I value your perspective on this.
    """
    
    print("\nAnalyzing transcript...")
    print("=" * 60)
    
    # Run full diagnostic
    results = chandra.full_diagnostic(transcript)
    
    # Display results
    print(chandra.geometric_summary(results))
    
    # Access specific metrics
    print("\n" + "=" * 60)
    print("DETAILED METRICS")
    print("=" * 60)
    
    dominant = results['chn_profile']['dominant_level']
    print(f"\nDominant Level: {dominant['name']} (L{dominant['level']})")
    print(f"Activation: {dominant['activation']*100:.1f}%")
    print(f"Psychological Stage: {results['chn_profile']['psychological_stage']}")
    
    sym_vuln = results['symbolic_pressure']['average_vulnerability']
    print(f"\nSymbolic Pressure Vulnerability: {sym_vuln*100:.1f}%")
    print(f"Assessment: {results['symbolic_pressure']['overall_assessment']}")
    
    print(f"\nOverall Health: {results['overall_health']}")

if __name__ == "__main__":
    main()
