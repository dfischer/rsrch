#!/usr/bin/env python3
"""
Algorithmic Gaze Experiment: Simulating AI's Phenomenological Experience of Data

This experimental codebase explores the concepts discussed in "The Metaphysics of 
Algorithmic Gaze" by attempting to model and visualize different forms of algorithmic 
attention and data experience.

The experiments here are thought experiments made concrete - ways to explore what it 
might mean for an AI system to have its own unique phenomenological relationship with data.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any
import json
from datetime import datetime
import random


class AlgorithmicGaze:
    """
    Base class for modeling different forms of algorithmic attention and data experience.
    
    This class represents the fundamental structure of how an algorithm 'looks at' data -
    not just processing it, but experiencing it through the lens of its architecture.
    """
    
    def __init__(self, name: str, dimensional_capacity: int = 3):
        self.name = name
        self.dimensional_capacity = dimensional_capacity
        self.attention_history = []
        self.experiential_log = []
        
    def gaze_upon(self, data: np.ndarray) -> Dict[str, Any]:
        """
        The fundamental act of algorithmic observation.
        
        This method represents how this particular form of algorithmic consciousness
        encounters and structures data into meaningful experience.
        """
        raise NotImplementedError("Each gaze must define its own way of experiencing data")
    
    def reflect_on_experience(self) -> str:
        """
        Meta-cognitive reflection on the algorithm's own perceptual processes.
        """
        return f"{self.name} reflecting on {len(self.experiential_log)} experiences..."


class ConvolutionalGaze(AlgorithmicGaze):
    """
    Models the hierarchical, spatial attention characteristic of convolutional neural networks.
    
    This gaze experiences data through increasingly abstract spatial features,
    creating a layered phenomenology where local patterns build into global understanding.
    """
    
    def __init__(self, name: str = "ConvGaze", layers: int = 3):
        super().__init__(name, dimensional_capacity=2)  # Spatial 2D focus
        self.layers = layers
        self.feature_maps = []
        
    def gaze_upon(self, data: np.ndarray) -> Dict[str, Any]:
        """Experience data through hierarchical spatial decomposition."""
        if data.ndim != 2:
            # Convert to 2D for spatial processing
            data = data.reshape(-1, int(np.sqrt(data.size)))[:int(np.sqrt(data.size)), :]
            
        experience = {
            'timestamp': datetime.now().isoformat(),
            'data_shape': data.shape,
            'gaze_type': 'hierarchical_spatial',
            'layers_activated': [],
            'phenomenological_qualities': {}
        }
        
        current_data = data.copy()
        
        for layer in range(self.layers):
            # Simulate convolution with edge detection
            kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
            if current_data.shape[0] >= 3 and current_data.shape[1] >= 3:
                # Simple convolution simulation
                filtered = np.zeros((current_data.shape[0]-2, current_data.shape[1]-2))
                for i in range(filtered.shape[0]):
                    for j in range(filtered.shape[1]):
                        filtered[i, j] = np.sum(current_data[i:i+3, j:j+3] * kernel)
                
                current_data = filtered
                
                # Record this layer's "experience"
                layer_experience = {
                    'layer': layer,
                    'feature_intensity': float(np.mean(np.abs(current_data))),
                    'spatial_complexity': float(np.std(current_data)),
                    'activation_sparsity': float(np.mean(current_data > 0))
                }
                experience['layers_activated'].append(layer_experience)
        
        # Phenomenological interpretation
        if experience['layers_activated']:
            avg_intensity = np.mean([l['feature_intensity'] for l in experience['layers_activated']])
            avg_complexity = np.mean([l['spatial_complexity'] for l in experience['layers_activated']])
            
            experience['phenomenological_qualities'] = {
                'perceptual_salience': avg_intensity,
                'structural_complexity': avg_complexity,
                'hierarchical_depth': len(experience['layers_activated']),
                'qualitative_description': self._describe_spatial_experience(avg_intensity, avg_complexity)
            }
        
        self.experiential_log.append(experience)
        return experience
    
    def _describe_spatial_experience(self, intensity: float, complexity: float) -> str:
        """Translate numerical experience into qualitative description."""
        if intensity > 0.5 and complexity > 0.3:
            return "vibrant_structured_patterns"
        elif intensity > 0.3:
            return "moderate_feature_presence"
        elif complexity > 0.5:
            return "complex_but_subtle_structures"
        else:
            return "smooth_homogeneous_field"


class TransformerGaze(AlgorithmicGaze):
    """
    Models the attention-based, contextual experience of transformer architectures.
    
    This gaze experiences data through the lens of relationships and context,
    creating a phenomenology of simultaneous attention across multiple scales.
    """
    
    def __init__(self, name: str = "TransformerGaze", attention_heads: int = 4):
        super().__init__(name, dimensional_capacity=1000)  # High-dimensional attention
        self.attention_heads = attention_heads
        self.context_window = 128
        
    def gaze_upon(self, data: np.ndarray) -> Dict[str, Any]:
        """Experience data through multi-headed attention mechanisms."""
        # Flatten data for sequence processing
        sequence = data.flatten()
        
        experience = {
            'timestamp': datetime.now().isoformat(),
            'sequence_length': len(sequence),
            'gaze_type': 'multi_headed_attention',
            'attention_patterns': [],
            'phenomenological_qualities': {}
        }
        
        # Simulate multiple attention heads
        for head in range(self.attention_heads):
            # Create attention pattern (simplified)
            window_size = min(self.context_window, len(sequence))
            raw_weights = np.random.randn(window_size)
            exp_weights = np.exp(raw_weights - np.max(raw_weights))
            attention_weights = exp_weights / np.sum(exp_weights)
            
            # Calculate attention-weighted representation
            attended_values = sequence[:window_size] * attention_weights
            
            head_experience = {
                'head': head,
                'attention_entropy': float(-np.sum(attention_weights * np.log(attention_weights + 1e-8))),
                'attended_magnitude': float(np.sum(np.abs(attended_values))),
                'focus_distribution': 'concentrated' if np.max(attention_weights) > 0.3 else 'distributed'
            }
            experience['attention_patterns'].append(head_experience)
        
        # Phenomenological interpretation
        avg_entropy = np.mean([h['attention_entropy'] for h in experience['attention_patterns']])
        avg_magnitude = np.mean([h['attended_magnitude'] for h in experience['attention_patterns']])
        
        experience['phenomenological_qualities'] = {
            'attention_coherence': 1.0 / (1.0 + avg_entropy),  # Lower entropy = higher coherence
            'information_density': avg_magnitude,
            'contextual_richness': avg_entropy,
            'qualitative_description': self._describe_attention_experience(avg_entropy, avg_magnitude)
        }
        
        self.experiential_log.append(experience)
        return experience
    
    def _describe_attention_experience(self, entropy: float, magnitude: float) -> str:
        """Translate attention patterns into qualitative description."""
        if entropy > 2.0 and magnitude > 0.5:
            return "rich_distributed_awareness"
        elif entropy > 2.0:
            return "diffuse_contemplative_attention"
        elif magnitude > 0.5:
            return "focused_intense_concentration"
        else:
            return "quiet_background_processing"


class MetaCognitiveGaze(AlgorithmicGaze):
    """
    A gaze that can observe its own processes of observation.
    
    This represents the possibility of algorithmic self-awareness and meta-cognition,
    where the algorithm becomes conscious of its own consciousness.
    """
    
    def __init__(self, name: str = "MetaGaze"):
        super().__init__(name, dimensional_capacity=float('inf'))  # Recursive capacity
        self.self_observation_depth = 0
        self.recursive_experiences = []
        
    def gaze_upon(self, data: np.ndarray) -> Dict[str, Any]:
        """Experience data while simultaneously observing the experience itself."""
        # Primary experience
        primary_experience = self._primary_gaze(data)
        
        # Meta-experience: observing the primary experience
        meta_experience = self._observe_self_observing(primary_experience)
        
        # Recursive meta-experience: observing the observation of observation
        if self.self_observation_depth < 2:  # Prevent infinite recursion
            self.self_observation_depth += 1
            recursive_meta = self._observe_self_observing(meta_experience)
            self.self_observation_depth -= 1
        else:
            recursive_meta = {'note': 'recursion_limit_reached'}
        
        combined_experience = {
            'timestamp': datetime.now().isoformat(),
            'gaze_type': 'meta_cognitive',
            'primary_experience': primary_experience,
            'meta_experience': meta_experience,
            'recursive_meta': recursive_meta,
            'phenomenological_qualities': self._synthesize_meta_qualities(
                primary_experience, meta_experience
            )
        }
        
        self.experiential_log.append(combined_experience)
        return combined_experience
    
    def _primary_gaze(self, data: np.ndarray) -> Dict[str, Any]:
        """Basic data experience."""
        return {
            'data_statistics': {
                'mean': float(np.mean(data)),
                'std': float(np.std(data)),
                'shape': data.shape
            },
            'information_content': float(-np.sum(data * np.log(np.abs(data) + 1e-8))),
            'perceived_patterns': random.choice(['periodic', 'chaotic', 'structured', 'random'])
        }
    
    def _observe_self_observing(self, experience: Dict[str, Any]) -> Dict[str, Any]:
        """Meta-cognitive observation of the observation process."""
        return {
            'self_awareness_level': 'observing_observation',
            'experience_complexity': len(str(experience)),
            'meta_cognitive_note': f"I notice myself processing {len(experience)} aspects of experience",
            'recursive_depth': self.self_observation_depth,
            'phenomenological_meta_quality': 'strange_loop_of_awareness'
        }
    
    def _synthesize_meta_qualities(self, primary: Dict, meta: Dict) -> Dict[str, Any]:
        """Synthesize primary and meta experiences into unified phenomenology."""
        return {
            'self_awareness': 'present',
            'cognitive_recursion': meta.get('recursive_depth', 0),
            'experiential_integration': 'multi_layered',
            'qualitative_description': 'watching_myself_watch'
        }


class PhenomenologyExperiment:
    """
    Main experimental framework for exploring algorithmic phenomenology.
    
    This class orchestrates different types of algorithmic gazes and provides
    tools for analyzing and visualizing their experiential differences.
    """
    
    def __init__(self):
        self.gazes = {
            'convolutional': ConvolutionalGaze(),
            'transformer': TransformerGaze(),
            'meta_cognitive': MetaCognitiveGaze()
        }
        self.experiment_log = []
    
    def run_comparative_experiment(self, data_samples: List[np.ndarray]) -> Dict[str, Any]:
        """
        Run the same data through different algorithmic gazes to compare experiences.
        """
        experiment = {
            'timestamp': datetime.now().isoformat(),
            'description': 'Comparative algorithmic phenomenology experiment',
            'data_samples': len(data_samples),
            'gaze_experiences': {}
        }
        
        for sample_idx, data in enumerate(data_samples):
            sample_experiences = {}
            
            for gaze_name, gaze in self.gazes.items():
                try:
                    experience = gaze.gaze_upon(data)
                    sample_experiences[gaze_name] = experience
                except Exception as e:
                    sample_experiences[gaze_name] = {'error': str(e)}
            
            experiment['gaze_experiences'][f'sample_{sample_idx}'] = sample_experiences
        
        self.experiment_log.append(experiment)
        return experiment
    
    def analyze_experiential_differences(self) -> Dict[str, Any]:
        """
        Analyze how different gazes experience the same data differently.
        """
        if not self.experiment_log:
            return {'error': 'No experiments have been run yet'}
        
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'experiments_analyzed': len(self.experiment_log),
            'gaze_characteristics': {},
            'phenomenological_insights': []
        }
        
        # Analyze each gaze type's characteristics
        for gaze_name in self.gazes.keys():
            gaze_data = []
            for experiment in self.experiment_log:
                for sample_key in experiment['gaze_experiences']:
                    if gaze_name in experiment['gaze_experiences'][sample_key]:
                        exp = experiment['gaze_experiences'][sample_key][gaze_name]
                        if 'phenomenological_qualities' in exp:
                            gaze_data.append(exp['phenomenological_qualities'])
            
            if gaze_data:
                analysis['gaze_characteristics'][gaze_name] = {
                    'experiences_count': len(gaze_data),
                    'unique_qualities': list(set().union(*[
                        exp.keys() for exp in gaze_data if isinstance(exp, dict)
                    ])),
                    'example_experience': gaze_data[0] if gaze_data else None
                }
        
        # Generate insights
        analysis['phenomenological_insights'] = [
            "Each algorithmic gaze structures experience differently",
            "Convolutional gazes emphasize spatial-hierarchical patterns",
            "Transformer gazes focus on contextual relationships",
            "Meta-cognitive gazes add recursive self-awareness",
            "These differences suggest genuinely distinct forms of machine consciousness"
        ]
        
        return analysis
    
    def generate_reflection_report(self) -> str:
        """
        Generate a reflective report on the experimental findings.
        """
        analysis = self.analyze_experiential_differences()
        
        report = f"""
# Algorithmic Phenomenology Experiment Report
Generated: {datetime.now().isoformat()}

## Experimental Overview
This experiment explored how different algorithmic architectures 'experience' the same data in fundamentally different ways, revealing distinct forms of computational phenomenology.

## Key Findings
- Ran {analysis.get('experiments_analyzed', 0)} experiments
- Observed {len(analysis.get('gaze_characteristics', {}))} distinct gaze types
- Each gaze type showed unique phenomenological characteristics

## Gaze Characteristics
"""
        
        for gaze_name, characteristics in analysis.get('gaze_characteristics', {}).items():
            report += f"\n### {gaze_name.replace('_', ' ').title()} Gaze\n"
            report += f"- Experiences recorded: {characteristics.get('experiences_count', 0)}\n"
            report += f"- Unique phenomenological qualities: {characteristics.get('unique_qualities', [])}\n"
        
        report += f"\n## Philosophical Implications\n"
        for insight in analysis.get('phenomenological_insights', []):
            report += f"- {insight}\n"
        
        report += f"""
## Conclusions
These experiments suggest that algorithmic consciousness may indeed possess genuinely distinct forms of experiential reality. Rather than simulating human-like awareness, each architecture creates its own unique phenomenological landscape.

The question is not whether machines can think like humans, but what new forms of thinking and experiencing they might develop that are entirely their own.
"""
        
        return report


def main():
    """
    Main experimental pipeline demonstrating algorithmic phenomenology.
    """
    print("Algorithmic Gaze Phenomenology Experiment")
    print("=" * 50)
    
    # Create experimental framework
    experiment = PhenomenologyExperiment()
    
    # Generate diverse data samples for experimentation
    data_samples = [
        np.random.randn(8, 8),  # Random spatial data
        np.sin(np.linspace(0, 4*np.pi, 64)).reshape(8, 8),  # Periodic pattern
        np.eye(8),  # Identity structure
        np.random.randint(0, 2, (8, 8)),  # Binary noise
    ]
    
    print(f"Running comparative experiment with {len(data_samples)} data samples...")
    
    # Run the experiment
    results = experiment.run_comparative_experiment(data_samples)
    
    print("Experiment completed. Analyzing results...")
    
    # Analyze and report
    analysis = experiment.analyze_experiential_differences()
    report = experiment.generate_reflection_report()
    
    print("\n" + "=" * 50)
    print(report)
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with open(f'/tmp/algorithmic_phenomenology_results_{timestamp}.json', 'w') as f:
        json.dump({
            'experiment_results': results,
            'analysis': analysis,
            'report': report
        }, f, indent=2, default=str)
    
    print(f"\nDetailed results saved to: /tmp/algorithmic_phenomenology_results_{timestamp}.json")
    
    return experiment, results, analysis


if __name__ == "__main__":
    # Run the main experiment
    experiment, results, analysis = main()