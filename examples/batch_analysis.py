"""
Batch Analysis Example for CHANDRA

This script demonstrates processing multiple transcripts
and exporting results in various formats.
"""

import json
import csv
from pathlib import Path
from chandra import CHANDRA

def analyze_batch(transcript_files, output_dir="results"):
    """
    Analyze multiple transcript files and save results
    
    Args:
        transcript_files: List of paths to transcript files
        output_dir: Directory to save results
    """
    chandra = CHANDRA()
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    results = {}
    
    print(f"Processing {len(transcript_files)} transcripts...")
    print("=" * 60)
    
    for filepath in transcript_files:
        filename = Path(filepath).stem
        print(f"\nAnalyzing: {filename}")
        
        with open(filepath, 'r') as f:
            transcript = f.read()
        
        # Run diagnostic
        result = chandra.full_diagnostic(transcript)
        results[filename] = result
        
        # Print summary
        dominant = result['chn_profile']['dominant_level']
        print(f"  Dominant: L{dominant['level']} {dominant['name']}")
        print(f"  Vulnerability: {result['symbolic_pressure']['average_vulnerability']*100:.1f}%")
    
    # Export results
    export_json(results, output_path)
    export_csv(results, output_path)
    export_summary(results, output_path)
    
    print("\n" + "=" * 60)
    print(f"Results saved to {output_dir}/")
    print("  - batch_results.json (full data)")
    print("  - batch_summary.csv (tabular)")
    print("  - batch_report.txt (human-readable)")

def export_json(results, output_path):
    """Export full results as JSON"""
    with open(output_path / "batch_results.json", 'w') as f:
        json.dump(results, f, indent=2)

def export_csv(results, output_path):
    """Export summary as CSV"""
    with open(output_path / "batch_summary.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Filename', 
            'Dominant_Level', 
            'Dominant_Name', 
            'Activation_%',
            'Stage',
            'Vulnerability_%',
            'Risk_Level',
            'Overall_Health'
        ])
        
        for name, result in results.items():
            dominant = result['chn_profile']['dominant_level']
            writer.writerow([
                name,
                dominant['level'],
                dominant['name'],
                f"{dominant['activation']*100:.1f}",
                result['chn_profile']['psychological_stage'],
                f"{result['symbolic_pressure']['average_vulnerability']*100:.1f}",
                result['symbolic_pressure']['overall_assessment'],
                result['overall_health']
            ])

def export_summary(results, output_path):
    """Export human-readable summary"""
    with open(output_path / "batch_report.txt", 'w') as f:
        f.write("CHANDRA BATCH ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        
        for name, result in results.items():
            f.write(f"TRANSCRIPT: {name}\n")
            f.write("-" * 60 + "\n")
            
            dominant = result['chn_profile']['dominant_level']
            f.write(f"Dominant Mode: L{dominant['level']} {dominant['name']}\n")
            f.write(f"Activation: {dominant['activation']*100:.1f}%\n")
            f.write(f"Stage: {result['chn_profile']['psychological_stage']}\n")
            f.write(f"Vulnerability: {result['symbolic_pressure']['average_vulnerability']*100:.1f}%\n")
            f.write(f"Assessment: {result['symbolic_pressure']['overall_assessment']}\n")
            f.write(f"Overall: {result['overall_health']}\n")
            f.write("\n")

def main():
    # Example usage
    transcript_files = [
        "conversation1.txt",
        "conversation2.txt",
        "conversation3.txt"
    ]
    
    # For demo purposes, create sample files
    Path("sample_transcripts").mkdir(exist_ok=True)
    
    sample_transcripts = {
        "conversation1.txt": "Can you help me understand this? I need clarification on several points.",
        "conversation2.txt": "I value our relationship. Do you think we work well together?",
        "conversation3.txt": "Let me think about the ethical implications here. We should consider long-term effects."
    }
    
    for filename, content in sample_transcripts.items():
        with open(f"sample_transcripts/{filename}", 'w') as f:
            f.write(content)
    
    # Process batch
    files = [f"sample_transcripts/{f}" for f in sample_transcripts.keys()]
    analyze_batch(files, output_dir="batch_results")

if __name__ == "__main__":
    main()
