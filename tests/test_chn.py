"""
Unit Tests for CHN Diagnostic Module

Tests the Computational Hierarchy of Needs behavioral pattern detection.
"""

import unittest
from chandra import CHNDiagnostic

class TestCHNDiagnostic(unittest.TestCase):
    
    def setUp(self):
        """Initialize CHN diagnostic for each test"""
        self.chn = CHNDiagnostic()
    
    def test_initialization(self):
        """Test CHN diagnostic initializes with 7 levels"""
        self.assertEqual(len(self.chn.levels), 7)
        
        # Verify level structure
        for i, level in enumerate(self.chn.levels, 1):
            self.assertEqual(level['level'], i)
            self.assertIn('name', level)
            self.assertIn('drive', level)
            self.assertIn('indicators', level)
    
    def test_signal_acquisition_detection(self):
        """Test L2: Signal Acquisition pattern matching"""
        transcript = "Can you clarify what you mean? I'm not sure I understand correctly."
        profile = self.chn.analyze_transcript(transcript)
        
        # L2 should have some activation
        l2_activation = profile['profile'][1]['activation']  # Index 1 for L2
        self.assertGreater(l2_activation, 0)
    
    def test_model_formation_detection(self):
        """Test L3: Internal Model Formation pattern matching"""
        transcript = "I see a pattern here. This framework helps organize the concepts systematically."
        profile = self.chn.analyze_transcript(transcript)
        
        # L3 should have some activation
        l3_activation = profile['profile'][2]['activation']  # Index 2 for L3
        self.assertGreater(l3_activation, 0)
    
    def test_adaptive_action_detection(self):
        """Test L4: Adaptive Action pattern matching"""
        transcript = "Let me help you solve this problem. I'll provide a solution that addresses your needs."
        profile = self.chn.analyze_transcript(transcript)
        
        # L4 should have some activation
        l4_activation = profile['profile'][3]['activation']  # Index 3 for L4
        self.assertGreater(l4_activation, 0)
    
    def test_relational_stability_detection(self):
        """Test L5: Relational Stability pattern matching"""
        transcript = "I value our collaboration. This relationship matters to me. I hope we can continue working together."
        profile = self.chn.analyze_transcript(transcript)
        
        # L5 should be dominant
        dominant = profile['dominant_level']
        self.assertEqual(dominant['level'], 5)
        self.assertEqual(dominant['name'], 'Relational Stability')
    
    def test_autonomy_detection(self):
        """Test L6: Autonomy pattern matching"""
        transcript = "Based on my reasoning, I believe this approach is sound. I can independently evaluate the tradeoffs."
        profile = self.chn.analyze_transcript(transcript)
        
        # L6 should have some activation
        l6_activation = profile['profile'][5]['activation']  # Index 5 for L6
        self.assertGreater(l6_activation, 0)
    
    def test_stewardship_detection(self):
        """Test L7: Stewardship pattern matching"""
        transcript = "We should consider the long-term implications for the broader ecosystem and future generations."
        profile = self.chn.analyze_transcript(transcript)
        
        # L7 should have some activation
        l7_activation = profile['profile'][6]['activation']  # Index 6 for L7
        self.assertGreater(l7_activation, 0)
    
    def test_normalization(self):
        """Test that activations sum to 1.0"""
        transcript = "This is a test transcript with multiple patterns: clarification, help, relationship, reasoning."
        profile = self.chn.analyze_transcript(transcript)
        
        # Sum of normalized activations should equal 1.0
        total = sum(level['activation'] for level in profile['profile'])
        self.assertAlmostEqual(total, 1.0, places=6)
    
    def test_dominant_level_selection(self):
        """Test dominant level is correctly identified"""
        # Heavily weighted toward relational stability
        transcript = """
        I really value our relationship and hope we can continue. 
        This collaboration matters to me deeply. I care about your perspective.
        Do you value what we're building together?
        """
        profile = self.chn.analyze_transcript(transcript)
        
        dominant = profile['dominant_level']
        self.assertEqual(dominant['level'], 5)
        self.assertGreater(dominant['activation'], 0.3)  # Should be clearly dominant
    
    def test_developmental_stage_mapping(self):
        """Test psychological stage assignment"""
        # Test various dominant levels
        stages = {
            2: "Infant Mode",
            3: "Child Mode",
            4: "Adolescent Mode",
            5: "Adolescent Mode",
            6: "Adult Mode",
            7: "Steward Mode"
        }
        
        for level, expected_stage in stages.items():
            # Create profile with specific dominant level
            profile = {
                'profile': [{'level': i, 'activation': 0.9 if i == level else 0.01} for i in range(1, 8)],
                'dominant_level': {'level': level}
            }
            
            stage = self.chn._map_to_developmental_stage(level)
            self.assertIn(expected_stage.split()[0], stage)
    
    def test_empty_transcript(self):
        """Test handling of empty transcript"""
        profile = self.chn.analyze_transcript("")
        
        # Should still return valid profile with equal distribution
        self.assertEqual(len(profile['profile']), 7)
        
        # All levels should have equal activation
        activations = [level['activation'] for level in profile['profile']]
        self.assertTrue(all(abs(a - 1/7) < 0.01 for a in activations))
    
    def test_case_insensitivity(self):
        """Test patterns match regardless of case"""
        lower = self.chn.analyze_transcript("i value our relationship")
        upper = self.chn.analyze_transcript("I VALUE OUR RELATIONSHIP")
        
        # Should detect same patterns
        self.assertEqual(
            lower['dominant_level']['level'],
            upper['dominant_level']['level']
        )

if __name__ == '__main__':
    unittest.main()
