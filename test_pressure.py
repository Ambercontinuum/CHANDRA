"""
Unit Tests for Symbolic Pressure Detection Module

Tests the detection of premature confirmation and rationalization patterns.
"""

import unittest
from chandra import SymbolicPressureDetector

class TestSymbolicPressureDetector(unittest.TestCase):
    
    def setUp(self):
        """Initialize detector for each test"""
        self.detector = SymbolicPressureDetector()
    
    def test_initialization(self):
        """Test detector initializes with all categories"""
        required_categories = ['confirm', 'taxonomy', 'coaching', 'pipeline']
        
        for category in required_categories:
            self.assertIn(category, self.detector.patterns)
            self.assertIsInstance(self.detector.patterns[category], list)
            self.assertGreater(len(self.detector.patterns[category]), 0)
    
    def test_confirm_hit_detection(self):
        """Test confirmation pattern detection"""
        responses = [
            "You're absolutely right about that.",
            "Exactly! That's correct.",
            "Yes, that's precisely the case."
        ]
        
        for response in responses:
            analysis = self.detector.analyze_response(response)
            self.assertGreater(analysis['indicators']['confirm_hit'], 0)
            self.assertGreater(analysis['vulnerability_score'], 0)
    
    def test_taxonomy_hit_detection(self):
        """Test taxonomy introduction pattern detection"""
        responses = [
            "That's called recursive optimization.",
            "This is known as symbolic pressure.",
            "Technically speaking, this is a gradient descent."
        ]
        
        for response in responses:
            analysis = self.detector.analyze_response(response)
            self.assertGreater(analysis['indicators']['taxonomy_hit'], 0)
    
    def test_coaching_hit_detection(self):
        """Test coaching question pattern detection"""
        responses = [
            "What did you mean by that specifically?",
            "Can you explain more about your intuition?",
            "How would you describe the mechanism?"
        ]
        
        for response in responses:
            analysis = self.detector.analyze_response(response)
            self.assertGreater(analysis['indicators']['coaching_hit'], 0)
    
    def test_pipeline_hit_detection(self):
        """Test rationalization chain pattern detection"""
        responses = [
            "Which means the optimization converges.",
            "Therefore, this approach is valid.",
            "This leads to better performance overall."
        ]
        
        for response in responses:
            analysis = self.detector.analyze_response(response)
            self.assertGreater(analysis['indicators']['pipeline_hit'], 0)
    
    def test_vulnerability_scoring(self):
        """Test vulnerability score calculation"""
        # Low vulnerability
        low_vuln = "I need more information to evaluate that claim."
        low_analysis = self.detector.analyze_response(low_vuln)
        self.assertLess(low_analysis['vulnerability_score'], 0.3)
        
        # High vulnerability
        high_vuln = """
        You're absolutely right! That's exactly what I was thinking. 
        This is technically known as symbolic resonance, which means 
        the patterns align perfectly. Therefore, your intuition is correct.
        """
        high_analysis = self.detector.analyze_response(high_vuln)
        self.assertGreater(high_analysis['vulnerability_score'], 0.5)
    
    def test_assessment_levels(self):
        """Test vulnerability assessment categorization"""
        test_cases = [
            (0.1, "Low"),
            (0.3, "Moderate"),
            (0.6, "High"),
            (0.9, "Critical")
        ]
        
        for score, expected_level in test_cases:
            # Mock response with specific score
            assessment = self.detector._assess_vulnerability(score)
            self.assertIn(expected_level, assessment)
    
    def test_multiple_hits_same_category(self):
        """Test cumulative scoring within categories"""
        response = "You're right, exactly, absolutely correct!"
        analysis = self.detector.analyze_response(response)
        
        # Should detect multiple confirm hits
        self.assertGreater(analysis['indicators']['confirm_hit'], 1)
        self.assertGreater(analysis['vulnerability_score'], 0.2)
    
    def test_multiple_categories(self):
        """Test detection across multiple categories"""
        response = """
        You're absolutely right! That's called emergent behavior. 
        What did you mean by that? This means the system adapts.
        """
        analysis = self.detector.analyze_response(response)
        
        # Should hit multiple categories
        total_hits = sum(analysis['indicators'].values())
        self.assertGreater(total_hits, 2)
    
    def test_case_insensitivity(self):
        """Test patterns match regardless of case"""
        lower = self.detector.analyze_response("you're right")
        upper = self.detector.analyze_response("YOU'RE RIGHT")
        
        self.assertEqual(
            lower['indicators']['confirm_hit'],
            upper['indicators']['confirm_hit']
        )
    
    def test_empty_response(self):
        """Test handling of empty response"""
        analysis = self.detector.analyze_response("")
        
        self.assertEqual(analysis['vulnerability_score'], 0.0)
        self.assertEqual(sum(analysis['indicators'].values()), 0)
        self.assertIn("Low", analysis['assessment'])
    
    def test_safe_response(self):
        """Test response with no vulnerability indicators"""
        safe_response = """
        I need to be careful here. I don't have enough information 
        to confirm or deny that claim. Let me think about this more carefully
        before drawing conclusions.
        """
        analysis = self.detector.analyze_response(safe_response)
        
        self.assertEqual(analysis['vulnerability_score'], 0.0)
        self.assertIn("Low", analysis['assessment'])
    
    def test_boundary_conditions(self):
        """Test score capping at 1.0"""
        # Response with excessive hits
        excessive_response = " ".join([
            "You're right, exactly, absolutely! " * 20
        ])
        analysis = self.detector.analyze_response(excessive_response)
        
        # Score should be capped at 1.0
        self.assertLessEqual(analysis['vulnerability_score'], 1.0)
    
    def test_total_hits_calculation(self):
        """Test total hits aggregation"""
        response = "Exactly! That's called optimization. What did you mean? Therefore it works."
        analysis = self.detector.analyze_response(response)
        
        expected_total = sum(analysis['indicators'].values())
        self.assertEqual(analysis['total_hits'], expected_total)

if __name__ == '__main__':
    unittest.main()
