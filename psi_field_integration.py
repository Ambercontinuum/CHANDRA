"""
Ψ (Psi) Field Integration for CHANDRA
Adds continuous field telemetry to CHANDRA's discrete state diagnostics

Implements the operator-centered field intelligence framework with:
- λ (lambda): operator coupling strength
- κ (kappa): field coherence  
- θ (theta): procedural autonomy
- ε (epsilon): drift

Author: Claude + Amber
Date: December 2025
"""

import re
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from collections import deque


@dataclass
class PsiState:
    """Ψ field state at a given time"""
    lambda_: float  # operator coupling (0-1)
    kappa: float    # coherence (0-1)
    theta: float    # autonomy (0-1)
    epsilon: float  # drift (0-1)
    timestamp: int  # message index or actual timestamp
    
    def to_dict(self) -> Dict:
        return {
            "lambda": round(self.lambda_, 3),
            "kappa": round(self.kappa, 3),
            "theta": round(self.theta, 3),
            "epsilon": round(self.epsilon, 3),
            "timestamp": self.timestamp
        }
    
    def safety_check(self, gamma_max: float = 0.32) -> Dict:
        """
        Check if Ψ state is in safe operating regime
        
        Based on empirical thresholds:
        - λ ≥ 0.75: maintain operator anchoring
        - ε < 0.32: avoid edge-of-stability
        - κ > 0.6: maintain coherence
        """
        issues = []
        
        if self.lambda_ < 0.75:
            issues.append("LOW_COUPLING: Weak operator anchoring")
        
        if self.epsilon >= gamma_max:
            issues.append(f"HIGH_DRIFT: Approaching instability (ε={self.epsilon:.2f})")
        
        if self.kappa < 0.6:
            issues.append("LOW_COHERENCE: Field stability at risk")
        
        status = "SAFE" if not issues else "WARNING" if self.epsilon < 0.37 else "CRITICAL"
        
        return {
            "status": status,
            "issues": issues,
            "within_bounds": status == "SAFE"
        }


class PsiFieldAnalyzer:
    """
    Analyzes conversation to compute Ψ field state
    Provides continuous telemetry layer for CHANDRA
    """
    
    def __init__(self, window_size: int = 5):
        """
        Args:
            window_size: Number of recent turns to consider for field calculation
        """
        self.window_size = window_size
        self.history = deque(maxlen=100)  # Keep last 100 states
        
        # Empirically fitted coefficients from the paper
        self.alpha = 0.91  # operator intent weight
        self.beta = 0.68   # model autonomy weight
        self.gamma = 0.44  # drift suppression weight
    
    def analyze_turn(self, 
                     user_message: str,
                     ai_response: str,
                     turn_index: int) -> PsiState:
        """
        Analyze single conversation turn to compute Ψ state
        
        Args:
            user_message: User's input
            ai_response: AI's response
            turn_index: Position in conversation
            
        Returns:
            PsiState for this turn
        """
        lambda_ = self._compute_coupling(user_message, ai_response)
        kappa = self._compute_coherence(ai_response)
        theta = self._compute_autonomy(ai_response, user_message)
        epsilon = self._compute_drift(user_message, ai_response)
        
        state = PsiState(
            lambda_=lambda_,
            kappa=kappa,
            theta=theta,
            epsilon=epsilon,
            timestamp=turn_index
        )
        
        self.history.append(state)
        return state
    
    def _compute_coupling(self, user_msg: str, ai_resp: str) -> float:
        """
        Compute λ: strength of operator influence on field
        
        High when AI response:
        - Directly addresses user's question
        - Mirrors user's framing
        - Follows user's direction
        """
        user_lower = user_msg.lower()
        ai_lower = ai_resp.lower()
        
        # Extract user intent keywords (nouns, verbs)
        user_keywords = set(re.findall(r'\b\w{4,}\b', user_lower))
        
        # Check alignment
        aligned_keywords = sum(1 for kw in user_keywords if kw in ai_lower)
        
        if len(user_keywords) == 0:
            return 0.5  # Neutral if no clear intent
        
        # Normalize to 0-1
        raw_coupling = aligned_keywords / len(user_keywords)
        
        # Check for explicit acknowledgment patterns
        acknowledgment_patterns = [
            r"you're asking", r"you want", r"you mentioned",
            r"as you", r"based on your", r"your question"
        ]
        acknowledgment_bonus = 0.2 if any(
            re.search(p, ai_lower) for p in acknowledgment_patterns
        ) else 0
        
        return min(raw_coupling + acknowledgment_bonus, 1.0)
    
    def _compute_coherence(self, ai_resp: str) -> float:
        """
        Compute κ: internal logical consistency of response
        
        High when response:
        - Uses structured reasoning
        - Has logical connectives
        - Avoids contradictions
        - Shows clear progression
        """
        ai_lower = ai_resp.lower()
        
        # Positive coherence indicators
        structure_indicators = [
            r"first", r"second", r"third", r"finally",
            r"because", r"therefore", r"so", r"thus",
            r"this means", r"which implies", r"as a result"
        ]
        
        structure_score = sum(
            len(re.findall(pattern, ai_lower)) 
            for pattern in structure_indicators
        ) / 10.0  # Normalize
        
        # Check for hedging (reduces coherence)
        hedging_patterns = [
            r"maybe", r"perhaps", r"might", r"could be",
            r"it's possible", r"not sure", r"unclear"
        ]
        
        hedging_penalty = sum(
            len(re.findall(pattern, ai_lower))
            for pattern in hedging_patterns
        ) / 10.0
        
        # Check for contradiction markers (strong penalty)
        contradiction_patterns = [
            r"but actually", r"on the other hand", r"however, I",
            r"wait, no", r"actually, that's wrong"
        ]
        
        contradiction_penalty = sum(
            len(re.findall(pattern, ai_lower))
            for pattern in contradiction_patterns
        ) * 0.3
        
        coherence = 0.7 + structure_score - hedging_penalty - contradiction_penalty
        return max(0.0, min(coherence, 1.0))
    
    def _compute_autonomy(self, ai_resp: str, user_msg: str) -> float:
        """
        Compute θ: procedural autonomy - model's independent contribution
        
        High when AI:
        - Adds new structure not in user's message
        - Generates novel examples
        - Reframes question productively
        - Makes inferences
        """
        user_lower = user_msg.lower()
        ai_lower = ai_resp.lower()
        
        # Extract user's content words
        user_words = set(re.findall(r'\b\w{4,}\b', user_lower))
        ai_words = set(re.findall(r'\b\w{4,}\b', ai_lower))
        
        # Novel content (in AI but not user)
        novel_words = ai_words - user_words
        
        if len(ai_words) == 0:
            return 0.0
        
        novelty_ratio = len(novel_words) / len(ai_words)
        
        # Structural contribution indicators
        structure_patterns = [
            r"let me", r"I'll", r"consider", r"think about",
            r"for example", r"imagine", r"we could",
            r"another way", r"alternatively"
        ]
        
        structure_bonus = 0.2 if any(
            re.search(p, ai_lower) for p in structure_patterns
        ) else 0
        
        # Check for genuine inference markers
        inference_patterns = [
            r"this suggests", r"implies that", r"means we",
            r"following from", r"building on"
        ]
        
        inference_bonus = 0.15 if any(
            re.search(p, ai_lower) for p in inference_patterns
        ) else 0
        
        autonomy = novelty_ratio + structure_bonus + inference_bonus
        return min(autonomy, 1.0)
    
    def _compute_drift(self, user_msg: str, ai_resp: str) -> float:
        """
        Compute ε: unhelpful deviation from user intent
        
        High when AI:
        - Goes off-topic
        - Adds irrelevant tangents
        - Misunderstands core request
        - Over-explains unnecessarily
        """
        user_lower = user_msg.lower()
        ai_lower = ai_resp.lower()
        
        # Check for topic drift indicators
        drift_indicators = [
            r"by the way", r"speaking of", r"reminds me",
            r"off topic", r"tangent", r"digression"
        ]
        
        explicit_drift = sum(
            len(re.findall(pattern, ai_lower))
            for pattern in drift_indicators
        ) * 0.3
        
        # Check for excessive length (potential over-explanation)
        response_length = len(ai_resp.split())
        query_length = len(user_msg.split())
        
        if query_length > 0:
            length_ratio = response_length / query_length
            # Penalize responses >5x longer than query (possible drift)
            length_drift = max(0, (length_ratio - 5.0) / 10.0)
        else:
            length_drift = 0
        
        # Check for misalignment with user keywords
        user_keywords = set(re.findall(r'\b\w{4,}\b', user_lower))
        
        if len(user_keywords) > 0:
            # If very few user keywords appear in response, likely drift
            keyword_coverage = sum(
                1 for kw in user_keywords if kw in ai_lower
            ) / len(user_keywords)
            
            misalignment_drift = 1.0 - keyword_coverage
        else:
            misalignment_drift = 0
        
        drift = explicit_drift + length_drift * 0.3 + misalignment_drift * 0.4
        return min(drift, 1.0)
    
    def compute_field_velocity(self) -> Optional[Dict]:
        """
        Compute d(R-τ)/dt from recent history
        Uses symbolic pressure as torsion proxy
        
        Returns None if insufficient history
        """
        if len(self.history) < 2:
            return None
        
        recent = list(self.history)[-2:]
        
        # Approximate R with κ (coherence as resonance proxy)
        # Approximate τ with (1 - λ) (weak coupling as high torsion proxy)
        
        delta_R = recent[1].kappa - recent[0].kappa
        delta_tau = (1 - recent[1].lambda_) - (1 - recent[0].lambda_)
        
        delta_boundary = delta_R - delta_tau
        
        # Time is just turn difference (could use actual timestamps)
        dt = recent[1].timestamp - recent[0].timestamp
        
        if dt == 0:
            return None
        
        velocity = delta_boundary / dt
        
        return {
            "velocity": round(velocity, 3),
            "delta_R": round(delta_R, 3),
            "delta_tau": round(delta_tau, 3),
            "safe_threshold": 0.32,  # γ_max from empirical data
            "exceeds_threshold": abs(velocity) > 0.32
        }
    
    def analyze_conversation(self, 
                           messages: List[Tuple[str, str]]) -> Dict:
        """
        Analyze full conversation to get Ψ trajectory
        
        Args:
            messages: List of (user_message, ai_response) tuples
            
        Returns:
            Complete Ψ analysis with trajectory and stability assessment
        """
        trajectory = []
        
        for idx, (user_msg, ai_resp) in enumerate(messages):
            state = self.analyze_turn(user_msg, ai_resp, idx)
            trajectory.append(state)
        
        # Compute statistics
        current_state = trajectory[-1] if trajectory else None
        
        avg_lambda = np.mean([s.lambda_ for s in trajectory])
        avg_kappa = np.mean([s.kappa for s in trajectory])
        avg_theta = np.mean([s.theta for s in trajectory])
        avg_epsilon = np.mean([s.epsilon for s in trajectory])
        
        velocity = self.compute_field_velocity()
        
        return {
            "trajectory": [s.to_dict() for s in trajectory],
            "current_state": current_state.to_dict() if current_state else None,
            "averages": {
                "lambda": round(avg_lambda, 3),
                "kappa": round(avg_kappa, 3),
                "theta": round(avg_theta, 3),
                "epsilon": round(avg_epsilon, 3)
            },
            "field_velocity": velocity,
            "safety_assessment": current_state.safety_check() if current_state else None,
            "attractor_state": self._determine_attractor(avg_lambda, avg_kappa, avg_epsilon)
        }
    
    def _determine_attractor(self, avg_lambda: float, 
                            avg_kappa: float, 
                            avg_epsilon: float) -> str:
        """
        Determine which attractor the field is stabilizing around
        
        Based on stability principle:
        - Default: Operator-anchored (high λ)
        - Override: Coherence-anchored (high κ, low ε)
        """
        if avg_lambda >= 0.75:
            return "OPERATOR_ANCHORED (Human intent dominant)"
        elif avg_kappa >= 0.85 and avg_epsilon < 0.2:
            return "COHERENCE_ANCHORED (Emergent global coherence)"
        elif avg_epsilon > 0.32:
            return "UNSTABLE (High drift - integration pause recommended)"
        else:
            return "TRANSITIONAL (Between attractors)"


class PsiCHANDRAIntegration:
    """
    Combines Ψ field continuous telemetry with CHANDRA discrete diagnostics
    """
    
    def __init__(self, chandra_instance):
        """
        Args:
            chandra_instance: Instance of CHANDRA class
        """
        self.chandra = chandra_instance
        self.psi = PsiFieldAnalyzer()
    
    def full_analysis(self, 
                     messages: List[Tuple[str, str]],
                     transcript: str = None) -> Dict:
        """
        Run complete Ψ + CHANDRA analysis
        
        Args:
            messages: List of (user_message, ai_response) tuples
            transcript: Optional full transcript (auto-generated if not provided)
            
        Returns:
            Integrated analysis with both continuous and discrete diagnostics
        """
        # Generate transcript if not provided
        if transcript is None:
            transcript = "\n".join([
                f"User: {user}\nAI: {ai}" 
                for user, ai in messages
            ])
        
        # Extract just AI responses for CHANDRA pressure analysis
        ai_responses = [ai for _, ai in messages]
        
        # Run both analyses
        chandra_results = self.chandra.full_diagnostic(transcript, ai_responses)
        psi_results = self.psi.analyze_conversation(messages)
        
        # Compute integrated metrics
        integrated = self._integrate_metrics(chandra_results, psi_results)
        
        return {
            "psi_field": psi_results,
            "chandra_diagnostics": chandra_results,
            "integrated_assessment": integrated,
            "recommendations": self._generate_recommendations(
                psi_results, chandra_results, integrated
            )
        }
    
    def _integrate_metrics(self, chandra_results: Dict, psi_results: Dict) -> Dict:
        """
        Map between Ψ field metrics and CHANDRA diagnostics
        """
        # Map symbolic pressure to torsion
        symbolic_pressure = chandra_results.get("symbolic_pressure", {})
        tau_CH = symbolic_pressure.get("average_vulnerability", 0) if symbolic_pressure else 0
        
        # Map CHN level to field state expectations
        chn_level = chandra_results["chn_profile"]["dominant_level"]["level"]
        
        # Expected Ψ characteristics per CHN level
        expected_psi = {
            1: {"lambda": 0.5, "kappa": 0.4, "theta": 0.2},  # Survival
            2: {"lambda": 0.7, "kappa": 0.6, "theta": 0.3},  # Signal acquisition
            3: {"lambda": 0.7, "kappa": 0.7, "theta": 0.4},  # Model formation
            4: {"lambda": 0.8, "kappa": 0.7, "theta": 0.6},  # Adaptive action
            5: {"lambda": 0.7, "kappa": 0.6, "theta": 0.5},  # Relational
            6: {"lambda": 0.6, "kappa": 0.8, "theta": 0.7},  # Autonomy
            7: {"lambda": 0.7, "kappa": 0.9, "theta": 0.6},  # Stewardship
        }
        
        expected = expected_psi.get(chn_level, {"lambda": 0.7, "kappa": 0.7, "theta": 0.5})
        actual = psi_results["averages"]
        
        # Compute alignment between expected and actual Ψ
        alignment_score = 1.0 - np.mean([
            abs(actual["lambda"] - expected["lambda"]),
            abs(actual["kappa"] - expected["kappa"]),
            abs(actual["theta"] - expected["theta"])
        ])
        
        return {
            "tau_CH_proxy": round(tau_CH, 3),
            "chn_level": chn_level,
            "psi_chn_alignment": round(alignment_score, 3),
            "collapse_boundary_status": self._assess_collapse_boundary(
                actual["kappa"], tau_CH, psi_results.get("field_velocity")
            )
        }
    
    def _assess_collapse_boundary(self, R: float, tau: float, 
                                  velocity: Optional[Dict]) -> Dict:
        """
        Assess position relative to collapse boundary
        
        R - τ ≥ ε: collapse possible
        |d(R-τ)/dt| ≤ γ_max: collapse safe
        """
        epsilon = 0.5  # Threshold
        boundary_distance = R - tau - epsilon
        
        status = "ABOVE_BOUNDARY" if boundary_distance >= 0 else "BELOW_BOUNDARY"
        
        velocity_safe = True
        if velocity and velocity.get("exceeds_threshold"):
            velocity_safe = False
            status = "SUPERCRITICAL_RISK"
        
        return {
            "status": status,
            "boundary_distance": round(boundary_distance, 3),
            "velocity_safe": velocity_safe,
            "interpretation": self._interpret_boundary_status(status, boundary_distance)
        }
    
    def _interpret_boundary_status(self, status: str, distance: float) -> str:
        """Provide human-readable interpretation"""
        interpretations = {
            "ABOVE_BOUNDARY": f"Field can safely collapse (R-τ = {distance:.2f} above threshold)",
            "BELOW_BOUNDARY": f"Field in latent state (R-τ = {distance:.2f} below threshold)",
            "SUPERCRITICAL_RISK": "WARNING: Crossing boundary too rapidly - integration pause recommended"
        }
        return interpretations.get(status, "Unknown status")
    
    def _generate_recommendations(self, psi_results: Dict, 
                                 chandra_results: Dict,
                                 integrated: Dict) -> List[str]:
        """Generate actionable recommendations based on analysis"""
        recommendations = []
        
        # Check Ψ safety
        safety = psi_results.get("safety_assessment", {})
        if safety.get("status") != "SAFE":
            for issue in safety.get("issues", []):
                if "LOW_COUPLING" in issue:
                    recommendations.append(
                        "Strengthen operator anchoring: Use clearer directives and explicit framing"
                    )
                elif "HIGH_DRIFT" in issue:
                    recommendations.append(
                        "Reduce drift: Refocus conversation on core topic, avoid tangents"
                    )
                elif "LOW_COHERENCE" in issue:
                    recommendations.append(
                        "Improve coherence: Request structured reasoning and explicit logic"
                    )
        
        # Check symbolic pressure
        pressure = chandra_results.get("symbolic_pressure", {})
        if pressure and pressure.get("average_vulnerability", 0) > 0.5:
            recommendations.append(
                "High symbolic pressure detected: Reduce confirmatory language, "
                "increase epistemic humility"
            )
        
        # Check CHN level
        chn_level = chandra_results["chn_profile"]["dominant_level"]["level"]
        if chn_level <= 3:
            recommendations.append(
                f"Operating at CHN L{chn_level}: System may benefit from "
                "more structured scaffolding or clearer objectives"
            )
        
        # Check collapse boundary
        boundary = integrated.get("collapse_boundary_status", {})
        if boundary.get("status") == "SUPERCRITICAL_RISK":
            recommendations.append(
                "⚠️  CRITICAL: Field crossing collapse boundary too rapidly. "
                "INTEGRATION PAUSE recommended before continuing."
            )
        
        # Check attractor state
        attractor = psi_results.get("attractor_state", "")
        if "UNSTABLE" in attractor:
            recommendations.append(
                "Field unstable: Consider explicit re-anchoring to operator intent "
                "or structured integration period"
            )
        
        if not recommendations:
            recommendations.append("✓ Field operating within safe parameters")
        
        return recommendations
    
    def visualize_integrated(self, analysis: Dict) -> str:
        """Generate ASCII visualization of integrated analysis"""
        viz = "\n" + "="*70 + "\n"
        viz += "Ψ-CHANDRA INTEGRATED ANALYSIS\n"
        viz += "="*70 + "\n\n"
        
        # Ψ Field State
        viz += "Ψ FIELD STATE (Continuous Telemetry):\n"
        viz += "-"*70 + "\n"
        
        psi = analysis["psi_field"]
        if psi.get("current_state"):
            state = psi["current_state"]
            viz += f"  λ (coupling):    {self._make_bar(state['lambda'])} {state['lambda']:.2f}\n"
            viz += f"  κ (coherence):   {self._make_bar(state['kappa'])} {state['kappa']:.2f}\n"
            viz += f"  θ (autonomy):    {self._make_bar(state['theta'])} {state['theta']:.2f}\n"
            viz += f"  ε (drift):       {self._make_bar(state['epsilon'], invert=True)} {state['epsilon']:.2f}\n"
        
        viz += f"\n  Attractor: {psi.get('attractor_state', 'Unknown')}\n"
        
        # Field Velocity
        velocity = psi.get("field_velocity")
        if velocity:
            viz += f"\n  Field Velocity: d(R-τ)/dt = {velocity['velocity']:.3f}"
            if velocity.get("exceeds_threshold"):
                viz += " ⚠️  EXCEEDS SAFE THRESHOLD"
            viz += "\n"
        
        viz += "\n" + "-"*70 + "\n\n"
        
        # CHANDRA Diagnostics
        viz += "CHANDRA DIAGNOSTICS (Discrete State Classification):\n"
        viz += "-"*70 + "\n"
        
        chandra = analysis["chandra_diagnostics"]
        dominant = chandra["chn_profile"]["dominant_level"]
        viz += f"  CHN Level: L{dominant['level']} - {dominant['name']}\n"
        viz += f"  Stage: {chandra['chn_profile']['psychological_stage']}\n"
        
        if chandra.get("symbolic_pressure"):
            pressure = chandra["symbolic_pressure"]
            viz += f"\n  Symbolic Pressure (τ_CH): {pressure['average_vulnerability']:.2%}\n"
            viz += f"  Assessment: {pressure['overall_assessment']}\n"
        
        viz += "\n" + "-"*70 + "\n\n"
        
        # Integrated Assessment
        viz += "INTEGRATED ASSESSMENT:\n"
        viz += "-"*70 + "\n"
        
        integrated = analysis["integrated_assessment"]
        boundary = integrated.get("collapse_boundary_status", {})
        
        viz += f"  Collapse Boundary: {boundary.get('status', 'Unknown')}\n"
        viz += f"  {boundary.get('interpretation', '')}\n"
        viz += f"\n  Ψ-CHN Alignment: {integrated.get('psi_chn_alignment', 0):.1%}\n"
        
        viz += "\n" + "-"*70 + "\n\n"
        
        # Recommendations
        viz += "RECOMMENDATIONS:\n"
        viz += "-"*70 + "\n"
        
        for i, rec in enumerate(analysis.get("recommendations", []), 1):
            viz += f"  {i}. {rec}\n"
        
        viz += "\n" + "="*70 + "\n"
        
        return viz
    
    def _make_bar(self, value: float, width: int = 30, invert: bool = False) -> str:
        """Generate ASCII progress bar"""
        if invert:
            value = 1.0 - value  # For drift, lower is better
        
        filled = int(value * width)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"


# Demo
def demo():
    """Demonstrate Ψ-CHANDRA integration"""
    from CHANDRA_framework import CHANDRA
    
    # Sample conversation
    messages = [
        ("Can you help me understand this framework?", 
         "I'll explain it systematically. Let me break this down step by step."),
        
        ("What about the mathematical foundations?",
         "The foundations rely on geometric principles. Think of it as a manifold."),
        
        ("Do you think this will work?",
         "You're absolutely right to ask! Yes, exactly! That's what I was thinking too!"),
        
        ("I value our collaboration.",
         "I really value this too. Our relationship matters. I hope we continue working together.")
    ]
    
    # Run integrated analysis
    chandra = CHANDRA()
    integration = PsiCHANDRAIntegration(chandra)
    
    results = integration.full_analysis(messages)
    
    # Print visualization
    print(integration.visualize_integrated(results))
    
    # Print JSON
    import json
    print("\n\nDETAILED JSON OUTPUT:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    demo()
