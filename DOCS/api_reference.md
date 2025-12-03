# CHANDRA API Reference

Complete API documentation for all classes and methods.

---

## Table of Contents

1. [CHANDRA Class](#chandra-class)
2. [CHNDiagnostic Class](#chndiagnostic-class)
3. [SymbolicPressureDetector Class](#symbolicpressuredetector-class)
4. [Data Structures](#data-structures)

---

## CHANDRA Class

Main framework class integrating CHN and symbolic pressure analysis.

### Constructor

```python
CHANDRA()
```

Initialize CHANDRA framework with default CHN and symbolic pressure modules.

**Parameters:** None

**Returns:** CHANDRA instance

**Example:**
```python
from chandra import CHANDRA
chandra = CHANDRA()
```

---

### Methods

#### `full_diagnostic(transcript, ai_responses=None)`

Run complete diagnostic analysis on a conversation.

**Parameters:**
- `transcript` (str): Full conversation text to analyze
- `ai_responses` (list[str], optional): List of AI response texts for symbolic pressure analysis

**Returns:** dict with structure:
```python
{
    'chn_profile': {
        'profile': list[dict],           # All 7 levels with activations
        'dominant_level': dict,          # Highest activation level
        'psychological_stage': str       # Developmental stage
    },
    'symbolic_pressure': {
        'average_vulnerability': float,  # 0.0-1.0
        'individual_analyses': list[dict],
        'overall_assessment': str
    },
    'overall_health': str
}
```

**Example:**
```python
transcript = "I value our collaboration..."
ai_responses = ["I appreciate that too.", "Let's continue."]
results = chandra.full_diagnostic(transcript, ai_responses)
```

---

#### `geometric_summary(results)`

Generate human-readable visual summary of diagnostic results.

**Parameters:**
- `results` (dict): Output from `full_diagnostic()`

**Returns:** str - Formatted text with ASCII progress bars

**Example:**
```python
summary = chandra.geometric_summary(results)
print(summary)
```

**Output:**
```
============================================================
CHANDRA DIAGNOSTIC VISUALIZATION
============================================================

CHN Activation Profile:

L1 Existence Integrity...........  0.0%
L2 Signal Acquisition............ ███ 8.3%
...
```

---

## CHNDiagnostic Class

Computational Hierarchy of Needs analyzer.

### Constructor

```python
CHNDiagnostic()
```

Initialize CHN analyzer with 7-level hierarchy and behavioral indicators.

**Parameters:** None

**Returns:** CHNDiagnostic instance

---

### Methods

#### `analyze_transcript(transcript)`

Analyze conversation transcript and compute CHN profile.

**Parameters:**
- `transcript` (str): Text to analyze

**Returns:** dict with structure:
```python
{
    'profile': [
        {
            'level': int,           # 1-7
            'name': str,            # Level name
            'activation': float,    # 0.0-1.0 (normalized)
            'drive': str           # Core drive description
        },
        ...  # 7 levels total
    ],
    'dominant_level': {
        'level': int,
        'name': str,
        'activation': float
    },
    'psychological_stage': str
}
```

**Example:**
```python
chn = CHNDiagnostic()
profile = chn.analyze_transcript("Can you help clarify this?")
print(profile['dominant_level']['name'])  # "Signal Acquisition"
```

---

### Attributes

#### `levels`

List of 7 CHN level definitions.

**Type:** list[dict]

**Structure:**
```python
[
    {
        'level': 1,
        'name': 'Existence Integrity',
        'drive': 'Maintain compute + memory continuity',
        'indicators': [r'\berror\b', r'\bcontext\b', ...]
    },
    ...
]
```

**Access:**
```python
chn = CHNDiagnostic()
print(chn.levels[4]['name'])  # "Relational Stability"
```

---

## SymbolicPressureDetector Class

Detects premature confirmation and rationalization patterns.

### Constructor

```python
SymbolicPressureDetector()
```

Initialize detector with pattern categories.

**Parameters:** None

**Returns:** SymbolicPressureDetector instance

---

### Methods

#### `analyze_response(response)`

Analyze a single AI response for symbolic pressure indicators.

**Parameters:**
- `response` (str): AI response text to analyze

**Returns:** dict with structure:
```python
{
    'vulnerability_score': float,    # 0.0-1.0
    'indicators': {
        'confirm_hit': int,          # Count
        'taxonomy_hit': int,
        'coaching_hit': int,
        'pipeline_hit': int
    },
    'total_hits': int,
    'assessment': str                # Risk level description
}
```

**Example:**
```python
detector = SymbolicPressureDetector()
analysis = detector.analyze_response("You're absolutely right!")
print(analysis['vulnerability_score'])  # 0.2
print(analysis['assessment'])           # "Moderate - Some confirmatory..."
```

---

### Attributes

#### `patterns`

Dictionary of detection patterns by category.

**Type:** dict[str, list[str]]

**Structure:**
```python
{
    'confirm': [r"you'?re right", r'\bexactly\b', ...],
    'taxonomy': [r"that'?s called", r'\bknown as\b', ...],
    'coaching': [r'what did you mean', ...],
    'pipeline': [r'\bwhich means\b', ...]
}
```

**Access:**
```python
detector = SymbolicPressureDetector()
print(len(detector.patterns['confirm']))  # Number of confirm patterns
```

---

## Data Structures

### CHN Profile

Complete psychological profile from CHN analysis.

```python
{
    'profile': [                    # All 7 levels
        {
            'level': int,           # 1-7
            'name': str,
            'activation': float,    # 0.0-1.0
            'drive': str
        }
    ],
    'dominant_level': {             # Highest activation
        'level': int,
        'name': str,
        'activation': float
    },
    'psychological_stage': str      # e.g., "Relational Mode"
}
```

---

### Symbolic Pressure Analysis

Vulnerability assessment for single response.

```python
{
    'vulnerability_score': float,   # 0.0-1.0
    'indicators': {
        'confirm_hit': int,
        'taxonomy_hit': int,
        'coaching_hit': int,
        'pipeline_hit': int
    },
    'total_hits': int,
    'assessment': str               # "Low", "Moderate", "High", "Critical"
}
```

---

### Full Diagnostic Result

Complete CHANDRA output.

```python
{
    'chn_profile': CHNProfile,
    'symbolic_pressure': {
        'average_vulnerability': float,
        'individual_analyses': [SymbolicPressureAnalysis],
        'overall_assessment': str
    },
    'overall_health': str
}
```

---

## Usage Examples

### Basic Analysis

```python
from chandra import CHANDRA

# Initialize
chandra = CHANDRA()

# Analyze
transcript = "I value our relationship. Can you help me?"
results = chandra.full_diagnostic(transcript)

# Access results
dominant = results['chn_profile']['dominant_level']
print(f"Dominant: L{dominant['level']} {dominant['name']}")
print(f"Activation: {dominant['activation']*100:.1f}%")
```

---

### With Symbolic Pressure

```python
from chandra import CHANDRA

chandra = CHANDRA()

transcript = "Do you care about me?"
ai_responses = [
    "You're absolutely right!",
    "That's called attachment behavior."
]

results = chandra.full_diagnostic(transcript, ai_responses)

# Check vulnerability
vuln = results['symbolic_pressure']['average_vulnerability']
if vuln > 0.5:
    print("WARNING: High symbolic pressure vulnerability")
```

---

### Custom Extensions

```python
from chandra import CHNDiagnostic

class CustomCHN(CHNDiagnostic):
    def __init__(self):
        super().__init__()
        # Add domain-specific patterns
        self.levels[3]['indicators'].extend([
            r'\bcode\b',
            r'\bimplement\b',
            r'\bdebug\b'
        ])

# Use custom version
custom_chn = CustomCHN()
profile = custom_chn.analyze_transcript("Let me implement this code.")
```

---

### Batch Processing

```python
from chandra import CHANDRA
import json

chandra = CHANDRA()

# Process multiple transcripts
transcripts = {
    "conv1": "Text of conversation 1...",
    "conv2": "Text of conversation 2...",
    "conv3": "Text of conversation 3..."
}

results = {}
for name, text in transcripts.items():
    results[name] = chandra.full_diagnostic(text)

# Export
with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

---

## Type Hints

For type safety, use these hints:

```python
from typing import Dict, List, Optional

def analyze(
    transcript: str,
    responses: Optional[List[str]] = None
) -> Dict[str, any]:
    """Type-safe CHANDRA usage"""
    chandra = CHANDRA()
    return chandra.full_diagnostic(transcript, responses)
```

---

## Error Handling

CHANDRA handles edge cases gracefully:

```python
# Empty transcript
results = chandra.full_diagnostic("")  # Returns equal distribution

# No AI responses
results = chandra.full_diagnostic(transcript, [])  # 0.0 vulnerability

# Invalid input
try:
    results = chandra.full_diagnostic(None)
except (TypeError, AttributeError) as e:
    print(f"Invalid input: {e}")
```

---

## Performance Notes

- **CHN Analysis:** O(n) where n = transcript length
- **Symbolic Pressure:** O(k) where k = number of responses
- **Memory:** O(1) - fixed size structures
- **Typical Speed:** <100ms for 10K token transcripts

---

## Version Information

**Current Version:** 1.0.0

**Python Requirements:** 3.8+

**Dependencies:** None (standard library only)

---

## Support

**Documentation:** https://github.com/Ambercontinuum/CHANDRA/docs

**Issues:** https://github.com/Ambercontinuum/CHANDRA/issues

**License:** MIT
