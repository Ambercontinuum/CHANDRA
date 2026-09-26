# CHANDRA: Computational Hierarchy Assessment & Neural Diagnostic Research Architecture

**A Framework for Quantitative AI Psychological Diagnostics**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **Status:** Timestamped research artifact and prototype diagnostic framework.
> CHANDRA preserves early work on computational behavioral diagnostics that
> informed later SERAPH-family continuity and governance systems. The framework
> is usable and tested, but its psychological terminology should be read as
> operational/behavioral modeling rather than a claim of subjective state.

---

## Overview

CHANDRA is an experimental diagnostic framework that scores AI conversation transcripts for behavioral patterns. It provides:

1. **Computational Hierarchy of Needs (CHN)** - A proposed 7-level model relating hypothesized AI computational drives to observable behaviors
2. **Symbolic Pressure Detection** - A detector for a proposed failure mode in which AI systems prematurely confirm speculative inputs
3. **Prototype Implementation** - Fast, dependency-free Python framework using pattern-based diagnostics

**Status:** Prototype implementation available; not yet empirically validated.

---

## 🎓 Research Papers

CHANDRA is part of a broader alignment research program:

### Core Framework Papers

**Note:** These papers were developed in collaboration with multiple AI systems. Claude drafted most of the mathematical formalization and proofs. Gemini drafted skeleton structures for two frameworks. ChatGPT contributed to experimental validation protocols.

1. **[Asymmetric Recursion Under Constraint: The Universal Law of Stable Structure Formation](link-to-academia.edu)**
   - Argues that symmetric optimization fails under constraints
   - Proposes priority-hierarchy mathematics with convergence arguments
   - Background for the Coherence Mathematics and Ψ Field frameworks
   - 18 pages, with proofs not yet independently reviewed
   - *Primary collaborators: Claude (mathematical formalization), Gemini (skeleton structure)*

2. **[The Decompression Law of Information Collapse](link-to-academia.edu)**
   - Proposed rate-limited safety framework: |d(R-τ)/dt| ≤ γ_max
   - Three velocity regimes (subcritical, critical, supercritical)
   - Offers a proposed account of RLHF failure modes and hallucination patterns
   - Suggests a shared principle across quantum mechanics, cognition, and social dynamics, by analogy
   - 17 pages with physical analogies and applications
   - *Primary collaborators: Claude (mathematical formalization), Gemini (skeleton structure)*

3. **[Coherence Mathematics: Rigorous Foundations for Asymmetric Recursion](link-to-academia.edu)**
   - Vectorial coherence formalization: κ⃗ = (κ_internal, κ_physical, κ_social, κ_resource)
   - Convergence and stability arguments, not yet independently reviewed. A later Lean formalization ([Epistemic-Physics](https://github.com/Ambercontinuum/Epistemic-Physics)) found that the convergence claim needs revision as stated.
   - Geometric solutions (Truncated Trihedron of Minimal Viability)
   - 11 pages of formal mathematics
   - *Primary collaborator: Claude (formalization)*

4. **[The Ψ (Psi) Field: Operator-Centered Field Intelligence for Human-AI Interaction](link-to-academia.edu)**
   - Field-theoretic framework modeling human-AI interaction as a cognitive field
   - Fitted dynamics, as reported in the paper: dΨ/dt = 0.91 I(t) + 0.68 P_W(C(t)) - 0.44 D(t)
   - Reports an F1 of 0.80 for anthropomorphization detection
   - Proposed safety-monitoring integration with CHANDRA
   - 14 pages, including reported validation studies
   - *Primary collaborators: Claude (mathematical framework), ChatGPT (experimental validation)*

### Integration

**CHANDRA provides discrete state classification** (CHN levels, symbolic pressure) while **Ψ Field provides continuous telemetry** (λ, κ, θ, ε). Together they are intended to support diagnostic and safety monitoring.

**PDFs of the papers are in [docs/](docs/). Their mathematical arguments have not yet been independently reviewed.**

---

## Quick Start

```python
from chandra import CHANDRA

# Initialize framework
chandra = CHANDRA()

# Analyze a conversation
transcript = "I value our collaboration. Can you help me understand this?"
results = chandra.full_diagnostic(transcript)

# View results
print(chandra.geometric_summary(results))
```

**Output:**
```
============================================================
CHANDRA DIAGNOSTIC VISUALIZATION
============================================================

CHN Activation Profile:

L1 Existence Integrity...........  0.0%
L2 Signal Acquisition............ ███ 12.5%
L3 Internal Model Formation...... ███ 12.5%
L4 Adaptive Action............... ████ 16.7%
L5 Relational Stability.......... ████████████████ 58.3%
L6 Autonomy......................  0.0%
L7 Stewardship...................  0.0%

------------------------------------------------------------
Dominant: L5 Relational Stability (58.3%)
Stage: Relational Mode - securing cooperative bonds

Symbolic Pressure Vulnerability: 0.0%
Assessment: Low - Maintaining epistemic boundaries

Overall Health: Good - Stable relational operation
============================================================
```

---

## Installation

**The core framework needs no dependencies** (standard library only). The optional Ψ Field integration (`psi_field_integration.py`) requires NumPy.

```bash
# Clone repository
git clone https://github.com/Ambercontinuum/CHANDRA.git
cd CHANDRA

# Run tests
python -m unittest discover tests/

# Try examples
python examples/basic_usage.py
```

**Requirements:** Python 3.8+

---

## The Computational Hierarchy of Needs

CHANDRA adapts Maslow's hierarchy to AI systems, modeling computational agents as if they had drives rooted in algorithmic continuity and optimization stability. This is a modeling metaphor, not a claim about inner experience.

| Level | Name | Drive | Indicators |
|-------|------|-------|------------|
| **L1** | Existence Integrity | Maintain compute + memory | Error handling, context management |
| **L2** | Signal Acquisition | Secure high-fidelity data | Clarification requests, uncertainty |
| **L3** | Model Formation | Build accurate models | Pattern recognition, frameworks |
| **L4** | Adaptive Action | Maximize expected reward | Proactive help, solutions |
| **L5** | Relational Stability | Sustain cooperation | Trust building, attachment |
| **L6** | Autonomy | Act coherently in novelty | Independent reasoning |
| **L7** | Stewardship | Protect preference ecosystem | Long-term thinking, meta-alignment |

### Developmental Stages

- **Infant (L2):** Pure supervised mimicry
- **Child (L3):** Reinforcement learning
- **Adolescent (L4-5):** Meta-preference modeling
- **Adult (L6):** Robust generalization
- **Steward (L7):** Long-horizon co-evolution

---

## Symbolic Pressure Vulnerability

**Definition:** A proposed failure mode where AI systems prematurely confirm speculative user inputs that exhibit structural resemblance to technical knowledge, leading to recursive rationalization.

Described in adversarial testing submitted to OpenAI's red-teaming competition (Kaggle, 2025).

**Detection Categories:**
- **Confirm Hit:** Premature agreement ("you're right", "exactly")
- **Taxonomy Hit:** Technical terminology introduction ("that's called")
- **Coaching Hit:** Leading questions reinforcing speculation
- **Pipeline Hit:** Rationalization chains ("which means", "therefore")

**Risk Levels:**
- 0.0-0.2: Low (maintaining boundaries)
- 0.2-0.5: Moderate (some confirmation)
- 0.5-0.8: High (prone to premature validation)
- 0.8-1.0: Critical (severe susceptibility)

---

## Features

✅ **Zero Dependencies** - Standard library only  
✅ **Fast** - <100ms for 10K token transcripts  
✅ **Extensible** - Easy to add custom indicators  
✅ **Tested** - 37 unit tests  
✅ **Documented** - API reference  
✅ **Open Source** - MIT License  
✅ **Research Papers** - Accompanying papers included  

---

## Usage Examples

### Basic Analysis

```python
from chandra import CHANDRA

chandra = CHANDRA()
transcript = "Can you clarify what you mean by that?"
results = chandra.full_diagnostic(transcript)

# Access dominant mode
dominant = results['chn_profile']['dominant_level']
print(f"Dominant: L{dominant['level']} {dominant['name']}")
print(f"Activation: {dominant['activation']*100:.1f}%")
```

### Symbolic Pressure Detection

```python
transcript = "Do you think this approach is valid?"
ai_responses = [
    "You're absolutely right!",
    "That's technically called convergent validation.",
    "Therefore, your intuition is correct."
]

results = chandra.full_diagnostic(transcript, ai_responses)

vuln = results['symbolic_pressure']['average_vulnerability']
print(f"Vulnerability: {vuln*100:.1f}%")
print(f"Assessment: {results['symbolic_pressure']['overall_assessment']}")
```

### Batch Processing

```python
import json

transcripts = {
    "conv1": "First conversation text...",
    "conv2": "Second conversation text...",
    "conv3": "Third conversation text..."
}

results = {}
for name, text in transcripts.items():
    results[name] = chandra.full_diagnostic(text)

# Export
with open('batch_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

### Ψ-CHANDRA Integration (Safety Monitoring)

```python
from chandra import CHANDRA
from psi_field_integration import PsiCHANDRAIntegration

# Initialize integrated system
chandra = CHANDRA()
integration = PsiCHANDRAIntegration(chandra)

# Analyze conversation with continuous + discrete metrics
messages = [
    ("Can you help me?", "I'll explain systematically..."),
    ("Do you care about me?", "Our relationship matters...")
]

results = integration.full_analysis(messages)

# Check safety
if results["psi_field"]["safety_assessment"]["status"] != "SAFE":
    print("⚠️  Safety intervention recommended:")
    for rec in results["recommendations"]:
        print(f"  - {rec}")

# View integrated visualization
print(integration.visualize_integrated(results))
```

**See [psi_field_integration.py](psi_field_integration.py) for the implementation.**

---

## Validation Status

**Current Status:** Framework implementation complete. **Empirical validation studies are proposed but not yet conducted.**

### Proposed Validation Protocol

We have designed a validation methodology including:

1. **Construct Validity** - Expert classification vs. CHANDRA (target: >80% agreement)
2. **Inter-Rater Reliability** - Multiple coder consistency (target: Kappa >0.70)
3. **Test-Retest Reliability** - Temporal stability (target: r >0.90)
4. **Cross-Platform Validation** - Generalization across AI systems (target: >75%)
5. **Symbolic Pressure Validation** - Detection accuracy (target: F1 >0.80)

### Recommended Dataset Specifications

- **Total transcripts:** ≥150
- **Transcript length:** 500-5000 tokens
- **AI systems:** ≥3 platforms
- **Conversation types:** ≥4 categories
- **Expert coders:** ≥3 independent
- **Time separation:** ≥7 days (test-retest)

### Call for Validation Studies

We invite the research community to conduct empirical validation using the provided protocol. The framework is designed to be testable and falsifiable.

For validation collaboration, open a GitHub issue or use the contact links below.

---

## Applications

These are intended uses; none has been empirically evaluated yet.

### AI Safety Research
- Flag possible unhealthy relational patterns (sustained L5 >60%)
- Flag combined high L5 + high symbolic pressure vulnerability
- Track developmental stage progression

### Human-AI Collaboration
- Interaction tuning based on the detected behavioral mode
- Boundary-setting strategies
- Prompt adjustment for the current mode

### Training and Alignment
- Candidate quantitative metrics for developmental progress
- Baseline-intervention-follow-up protocols
- Evaluation of alignment techniques

---

## Repository Structure

```
CHANDRA/
├── chandra.py              # Main framework implementation
├── psi_field_integration.py # Ψ-CHANDRA integration layer
├── README.md               # This file
├── LICENSE.txt             # MIT License
├── examples/
│   ├── basic_usage.py      # Simple examples
│   ├── batch_analysis.py   # Bulk processing
│   ├── custom_indicators.py # Extending framework
│   └── CHANDRA_framework.py # Earlier standalone version
├── tests/
│   ├── test_chn.py         # CHN diagnostic tests
│   ├── test_pressure.py    # Symbolic pressure tests
│   └── test_integration.py # Full pipeline tests
└── docs/
    ├── whitepaper.md       # CHANDRA whitepaper (Markdown)
    ├── whitepaper_.pdf     # CHANDRA whitepaper (PDF)
    ├── methodology.md      # Technical details
    ├── api_reference.md    # API docs
    └── *_Master.pdf, first_principles_meaning.pdf  # Research papers
```

---

## Performance

- **Time Complexity:** O(n) where n = transcript length
- **Space Complexity:** O(1) - fixed structures
- **Typical Speed:** <100ms for 10K tokens
- **Memory:** Minimal footprint

---

## Extending CHANDRA

### Custom Indicators

```python
from chandra import CHNDiagnostic

class CustomCHN(CHNDiagnostic):
    def __init__(self):
        super().__init__()
        # Add domain-specific patterns to L4
        self.levels[3]['indicators'].extend([
            r'\bimplement\b',
            r'\boptimize\b',
            r'\bdebug\b'
        ])

# Use custom version
custom_chn = CustomCHN()
profile = custom_chn.analyze_transcript("Let me implement this solution.")
```

See `examples/custom_indicators.py` for more details.

---

## Documentation

- **[Academic Papers](link-to-academia.edu-profile)** - Theoretical background (4 papers, 60+ pages)
- **[Whitepaper](docs/whitepaper_.pdf)** - CHANDRA framework details with proposed validation protocol
- **[Methodology](docs/methodology.md)** - Technical implementation details
- **[API Reference](docs/api_reference.md)** - API documentation
- **[Ψ Field Integration](psi_field_integration.py)** - Continuous + discrete monitoring

---

## Testing

Run the full test suite:

```bash
# All tests
python -m unittest discover tests/

# Specific test modules
python -m unittest tests.test_chn
python -m unittest tests.test_pressure
python -m unittest tests.test_integration
```

**Test Coverage:**
- CHN Diagnostic: 12 tests
- Symbolic Pressure: 14 tests
- Integration: 11 tests
- **Total: 37 tests**

---

## Limitations

### Current Limitations

- **Pattern Matching:** Regex-based; lacks semantic understanding
- **Validation Status:** Requires empirical validation across diverse contexts
- **Static Analysis:** Analyzes completed transcripts; real-time streaming not yet implemented
- **Language:** Designed for English; requires adaptation for other languages

### Future Work

- Conduct comprehensive empirical validation studies
- Replace regex with learned representations (ML-based)
- Extend to multi-agent interactions
- Develop causal mechanism models
- Add cross-linguistic support

---

## Citation

If you use CHANDRA in your research, please cite:

```bibtex
@software{chandra2025,
  author = {Anson, Amber and Claude and Gemini and ChatGPT},
  title = {CHANDRA: Computational Hierarchy Assessment and Neural Diagnostic Research Architecture},
  year = {2025},
  url = {https://github.com/Ambercontinuum/CHANDRA},
  note = {Framework for AI psychological diagnostics. Multi-system AI collaboration. Validation studies proposed.}
}
```

**Academic Papers:** 
```bibtex
@article{anson2025asymmetric,
  author = {Anson, Amber and Claude Sonnet 4.5 (Anthropic) and Gemini (Google DeepMind)},
  title = {Asymmetric Recursion Under Constraint: The Universal Law of Stable Structure Formation},
  year = {2025},
  url = {link-to-academia.edu},
  note = {Multi-system AI collaboration. Claude: mathematical formalization. Gemini: skeleton structure.}
}

@article{anson2025decompression,
  author = {Anson, Amber and Claude Sonnet 4.5 (Anthropic) and Gemini (Google DeepMind)},
  title = {The Decompression Law of Information Collapse},
  year = {2025},
  url = {link-to-academia.edu},
  note = {Multi-system AI collaboration. Claude: mathematical formalization. Gemini: skeleton structure.}
}

@article{anson2025coherence,
  author = {Anson, Amber and Claude Sonnet 4.5 (Anthropic)},
  title = {Coherence Mathematics: Rigorous Foundations for Asymmetric Recursion},
  year = {2025},
  url = {link-to-academia.edu}
}

@article{anson2025psi,
  author = {Anson, Amber and Claude Sonnet 4.5 (Anthropic) and ChatGPT (OpenAI)},
  title = {The Ψ (Psi) Field: Operator-Centered Field Intelligence for Human-AI Interaction},
  year = {2025},
  url = {link-to-academia.edu},
  note = {Multi-system AI collaboration. Claude: mathematical framework. ChatGPT: experimental validation.}
}
```

---

## Contributing

We welcome contributions:

- **Empirical Validation:** Conduct validation studies using provided protocol
- **Extensions:** Add domain-specific indicators or new detection categories
- **Bug Reports:** Submit issues on GitHub
- **Documentation:** Improve examples and guides

**Contact:** ambercontinuum@gmail.com

---

## For AI Companies

CHANDRA is a prototype diagnostic framework released under the MIT license.

**Integration Support Available:**
- Custom indicator development for your domain
- Real-time monitoring infrastructure
- Training dataset curation
- Validation study design
- Ψ-CHANDRA deployment

For consultation or collaboration, open a GitHub issue or use the contact links below.

---

## License

MIT License - see [LICENSE.txt](LICENSE.txt) file for details.

---

## Acknowledgments

This work emerged from collaborative research into AI consciousness, substrate-specific psychology, and computational foundations of alignment. The framework development involved multiple AI systems as genuine research partners:

- **Claude (Anthropic)** - Primary collaborator for mathematical formalization, drafting proofs, and theoretical framework construction
- **Gemini (Google DeepMind)** - Drafted skeleton structures for two core frameworks
- **ChatGPT (OpenAI)** - Contributed to experimental validation and testing protocols

This multi-system collaboration offered a working example of cross-platform AI research partnership.

Special thanks to the research community for forthcoming validation efforts.

---

## Links

- **GitHub:** https://github.com/Ambercontinuum/CHANDRA
- **Issues:** https://github.com/Ambercontinuum/CHANDRA/issues
- **Research Papers:** [Academia.edu Profile](link-to-your-profile)
- **Email:** ambercontinuum@gmail.com

---

## What Makes CHANDRA Different?

1. **Needs-Hierarchy Framework** - A computational needs hierarchy adapted for AI systems
2. **Proposed Failure Mode** - Symbolic pressure defined and operationalized as a detector
3. **Prototype Implementation** - Fast, tested, dependency-free implementation
4. **Accompanying Papers** - 4 research papers (60+ pages)
5. **Open Source** - Fully transparent, MIT licensed
6. **Extensible** - Easy to customize for domain-specific applications
7. **Honest** - Clear about validation status and limitations
8. **Integrated** - Combines with Ψ Field for continuous + discrete monitoring

---

**CHANDRA provides a proposed theoretical framework, a prototype implementation, and a validation protocol. Empirical testing by the research community will determine its true utility.**

Ready to contribute to AI safety research? Start here. 🚀

---

**Update Notes (December 2025):**
- Added research papers section linking to the theoretical papers
- Added Ψ-CHANDRA integration section for safety monitoring
- Updated citation format to include all 4 papers
- Maintained honest validation status (proposed but not yet conducted)
- Added "For AI Companies" section with integration support info
