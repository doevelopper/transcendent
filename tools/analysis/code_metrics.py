#!/usr/bin/env python3
"""
Code analysis tool for C++ codebase metrics.
"""

import os
import re
import argparse
from pathlib import Path
import json


class CodeAnalyzer:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.metrics = {
            "total_files": 0,
            "total_lines": 0,
            "code_lines": 0,
            "comment_lines": 0,
            "blank_lines": 0,
            "classes": 0,
            "functions": 0,
            "complexity": 0
        }
        
    def analyze(self):
        """Analyze all C++ files in the source directory."""
        cpp_files = list(self.source_dir.rglob("*.cpp")) + list(self.source_dir.rglob("*.hpp"))
        
        for file_path in cpp_files:
            self._analyze_file(file_path)
            
        return self.metrics
    
    def _analyze_file(self, file_path):
        """Analyze a single C++ file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            self.metrics["total_files"] += 1
            
            lines = content.split('\n')
            self.metrics["total_lines"] += len(lines)
            
            in_comment_block = False
            
            for line in lines:
                line = line.strip()
                
                if not line:
                    self.metrics["blank_lines"] += 1
                elif line.startswith('/*') or in_comment_block:
                    self.metrics["comment_lines"] += 1
                    in_comment_block = not line.endswith('*/')
                elif line.startswith('//'):
                    self.metrics["comment_lines"] += 1
                else:
                    self.metrics["code_lines"] += 1
                    
            # Count classes and functions
            self.metrics["classes"] += len(re.findall(r'class\s+\w+', content))
            self.metrics["functions"] += len(re.findall(r'\w+\s*\([^)]*\)\s*{', content))
            
            # Simple cyclomatic complexity (count decision points)
            decision_keywords = ['if', 'else', 'for', 'while', 'switch', 'case', 'catch']
            for keyword in decision_keywords:
                self.metrics["complexity"] += len(re.findall(rf'\b{keyword}\b', content))
                
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Analyze C++ code metrics")
    parser.add_argument("--source-dir", required=True, help="Source directory to analyze")
    parser.add_argument("--output", help="Output file for metrics (JSON format)")
    
    args = parser.parse_args()
    
    analyzer = CodeAnalyzer(args.source_dir)
    metrics = analyzer.analyze()
    
    # Calculate derived metrics
    if metrics["total_lines"] > 0:
        metrics["comment_ratio"] = metrics["comment_lines"] / metrics["total_lines"]
        metrics["code_ratio"] = metrics["code_lines"] / metrics["total_lines"]
    
    if metrics["functions"] > 0:
        metrics["avg_complexity_per_function"] = metrics["complexity"] / metrics["functions"]
    
    # Print results
    print("Code Analysis Results:")
    print(f"Total files: {metrics['total_files']}")
    print(f"Total lines: {metrics['total_lines']}")
    print(f"Code lines: {metrics['code_lines']}")
    print(f"Comment lines: {metrics['comment_lines']}")
    print(f"Blank lines: {metrics['blank_lines']}")
    print(f"Classes: {metrics['classes']}")
    print(f"Functions: {metrics['functions']}")
    print(f"Cyclomatic complexity: {metrics['complexity']}")
    
    if "comment_ratio" in metrics:
        print(f"Comment ratio: {metrics['comment_ratio']:.2%}")
        print(f"Code ratio: {metrics['code_ratio']:.2%}")
    
    if "avg_complexity_per_function" in metrics:
        print(f"Average complexity per function: {metrics['avg_complexity_per_function']:.2f}")
    
    # Save to file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(metrics, f, indent=2)
        print(f"Metrics saved to {args.output}")


if __name__ == "__main__":
    main()