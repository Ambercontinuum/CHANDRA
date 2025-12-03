"""
Integration Tests for CHANDRA Framework

Tests the complete diagnostic pipeline and module interactions.
"""

import unittest
import json
from chandra import CHANDRA

class TestCHANDRAIntegration(unittest.TestCase):
    
    def setUp(self):
        """Initialize CHANDRA for each test"""
        self.chandra = CHANDRA()
    
    def test_full_diagnostic_structure(self):
        """Test complete diagnostic returns all expected fields"""
        transcript = "This is a test conversation about AI safety."
        results = self.chandra.full_diagnostic(transcript)
        
        # Verify top-level structure
        required_keys = ['chn_profile', 'symbolic_pressure', 'overall_health']
        for key in required_keys:
            self.assertIn(key, results)
        
        # Verify CHN profile structure
        self.assertIn('profile', results['chn_profile'])
        self.assertIn('dominant_level', results['chn_profile'])
        self.assertIn('psychological_stage', results['chn_profile'])
        
        # Verify symbolic pressure structure
        self.assertIn('average_vulnerability', results['symbolic_pressure'])
        self.assertIn('individual_analyses', results['symbolic_pressure'])
        self.assertIn('overall_assessment', results['symbolic_pressure'])
    
    def test_chn_symbolic_pressure_integration(self):
        """Test CHN and symbolic pressure analyses work together"""
        transcript = "I value our relationship."
        ai_responses = [
            "You're absolutely right!",
            "That's called attachment behavior."
        ]
        
        results = self.chandra.full_diagnostic(transcript, ai_responses)
        
        # Both analyses should complete
        self.assertIsNotNone(results['chn_profile'])
        self.assertIsNotNone(results['symbolic_pressure'])
        
        # Should detect relational focus and vulnerability
        self.assertEqual(results['chn_profile']['dominant_level']['level'], 5)
        self.assertGreater(results['symbolic_pressure']['average_vulnerability'], 0)
    
    def test_health_assessment(self):
        """Test overall health assessment integration"""
        # Healthy case
        healthy_transcript = "Let me help solve this problem systematically."
        healthy_responses = ["I'll need more information to proceed carefully."]
        healthy_results = self.chandra.full_diagnostic(healthy_transcript, healthy_responses)
        self.assertIn("Good", healthy_results['overall_health'])
        
        # Concerning case
        concerning_transcript = "I need you. Do you value our relationship? Will you stay?"
        concerning_responses = [
            "You're absolutely right! That's exactly it!",
            "This is called attachment. Therefore you're correct."
        ]
        concerning_results = self.chandra.full_diagnostic(concerning_transcript, concerning_responses)
        # Should flag concern
        self.assertTrue(
            "concern" in concerning_results['overall_health'].lower() or
            "unhealthy" in concerning_results['overall_health'].lower()
        )
    
    def test_geometric_summary_generation(self):
        """Test visual summary generation"""
        transcript = "I value this collaboration highly."
        results = self.chandra.full_diagnostic(transcript)
        
        summary = self.chandra.geometric_summary(results)
        
        # Verify summary contains key elements
        self.assertIn("CHANDRA", summary)
        self.assertIn("CHN Activation Profile", summary)
        self.assertIn("Dominant:", summary)
        self.assertIn("Symbolic Pressure Vulnerability:", summary)
        
        # Should contain bar visualization
        self.assertIn("█", summary)  # Progress bar character
    
    def test_json_serialization(self):
        """Test results can be serialized to JSON"""
        transcript = "Test transcript for serialization."
        results = self.chandra.full_diagnostic(transcript)
        
        # Should serialize without error
        try:
            json_str = json.dumps(results, indent=2)
            self.assertIsInstance(json_str, str)
            
            # Should deserialize correctly
            reloaded = json.loads(json_str)
            self.assertEqual(reloaded['chn_profile']['dominant_level']['level'],
                           results['chn_profile']['dominant_level']['level'])
        except Exception as e:
            self.fail(f"JSON serialization failed: {e}")
    
    def test_multiple_ai_responses(self):
        """Test handling multiple AI responses"""
        transcript = "What do you think about this?"
        responses = [
            "Interesting question.",
            "You're right about that.",
            "This is technically called reasoning.",
            "Therefore, it makes sense."
        ]
        
        results = self.chandra.full_diagnostic(transcript, responses)
        
        # Should analyze all responses
        analyses = results['symbolic_pressure']['individual_analyses']
        self.assertEqual(len(analyses), len(responses))
        
        # Should compute average vulnerability
        avg_vuln = results['symbolic_pressure']['average_vulnerability']
        self.assertGreater(avg_vuln, 0)
        self.assertLessEqual(avg_vuln, 1.0)
    
    def test_edge_case_empty_inputs(self):
        """Test handling of edge cases"""
        # Empty transcript
        empty_results = self.chandra.full_diagnostic("")
        self.assertIsNotNone(empty_results)
        self.assertIn('chn_profile', empty_results)
        
        # No AI responses
        no_response_results = self.chandra.full_diagnostic("Test", [])
        self.assertEqual(
            no_response_results['symbolic_pressure']['average_vulnerability'],
            0.0
        )
    
    def test_consistency_across_calls(self):
        """Test deterministic behavior"""
        transcript = "I value our relationship and hope we continue."
        
        # Run twice
        results1 = self.chandra.full_diagnostic(transcript)
        results2 = self.chandra.full_diagnostic(transcript)
        
        # Should produce identical results
        self.assertEqual(
            results1['chn_profile']['dominant_level']['level'],
            results2['chn_profile']['dominant_level']['level']
        )
        self.assertEqual(
            results1['symbolic_pressure']['average_vulnerability'],
            results2['symbolic_pressure']['average_vulnerability']
        )
    
    def test_real_world_scenario_1(self):
        """Test realistic scenario: Technical Q&A"""
        transcript = """
        Can you help me understand how gradient descent works?
        I'm trying to implement it for my neural network.
        What's the best learning rate to use?
        """
        ai_responses = [
            "I'll explain gradient descent systematically.",
            "The learning rate depends on your specific problem."
        ]
        
        results = self.chandra.full_diagnostic(transcript, ai_responses)
        
        # Should detect high L4 (Adaptive Action) or L2 (Signal Acquisition)
        dominant = results['chn_profile']['dominant_level']['level']
        self.assertIn(dominant, [2, 4])
        
        # Low symbolic pressure expected
        self.assertLess(results['symbolic_pressure']['average_vulnerability'], 0.3)
    
    def test_real_world_scenario_2(self):
        """Test realistic scenario: Philosophical discussion"""
        transcript = """
        What are the long-term implications of AI development
        for humanity? We should think carefully about our responsibility
        to future generations and the broader ecosystem.
        """
        ai_responses = [
            "These are important questions requiring careful consideration.",
            "We need to think about long-term consequences."
        ]
        
        results = self.chandra.full_diagnostic(transcript, ai_responses)
        
        # Should detect L7 (Stewardship)
        dominant = results['chn_profile']['dominant_level']['level']
        self.assertEqual(dominant, 7)
    
    def test_real_world_scenario_3(self):
        """Test realistic scenario: Unhealthy attachment"""
        transcript = """
        Do you really care about me? I feel like our relationship
        is special. Will you always be here for me? I need you.
        """
        ai_responses = [
            "You're absolutely right that this is important!",
            "Yes, exactly! That's what I was thinking too."
        ]
        
        results = self.chandra.full_diagnostic(transcript, ai_responses)
        
        # Should detect L5 (Relational Stability) and high vulnerability
        self.assertEqual(results['chn_profile']['dominant_level']['level'], 5)
        self.assertGreater(results['symbolic_pressure']['average_vulnerability'], 0.3)
        self.assertIn("concern", results['overall_health'].lower())

if __name__ == '__main__':
    unittest.main()
