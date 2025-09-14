#!/usr/bin/env python3
"""
Dependency analysis tool for C++ projects.
"""

import os
import re
import argparse
from pathlib import Path
import json
from collections import defaultdict, deque


class DependencyAnalyzer:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.dependencies = defaultdict(set)
        self.reverse_dependencies = defaultdict(set)
        
    def analyze(self):
        """Analyze dependencies in C++ files."""
        cpp_files = list(self.source_dir.rglob("*.cpp")) + list(self.source_dir.rglob("*.hpp"))
        
        for file_path in cpp_files:
            self._analyze_file(file_path)
            
        return self._generate_report()
    
    def _analyze_file(self, file_path):
        """Analyze dependencies in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get relative path for consistent naming
            rel_path = str(file_path.relative_to(self.source_dir))
            
            # Find include statements
            includes = re.findall(r'#include\s*[<"]([^>"]+)[>"]', content)
            
            for include in includes:
                # Skip system headers
                if not include.startswith('<') and not include.startswith('std'):
                    self.dependencies[rel_path].add(include)
                    self.reverse_dependencies[include].add(rel_path)
                    
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
    
    def _generate_report(self):
        """Generate dependency analysis report."""
        report = {
            "total_files": len(self.dependencies),
            "files": {}
        }
        
        for file_path, deps in self.dependencies.items():
            file_info = {
                "dependencies": list(deps),
                "dependency_count": len(deps),
                "dependents": list(self.reverse_dependencies.get(file_path, [])),
                "dependent_count": len(self.reverse_dependencies.get(file_path, []))
            }
            report["files"][file_path] = file_info
        
        # Find circular dependencies
        report["circular_dependencies"] = self._find_circular_dependencies()
        
        # Find most depended upon files
        most_depended = sorted(
            [(f, len(deps)) for f, deps in self.reverse_dependencies.items()],
            key=lambda x: x[1],
            reverse=True
        )[:10]
        report["most_depended_upon"] = most_depended
        
        return report
    
    def _find_circular_dependencies(self):
        """Find circular dependencies using DFS."""
        visited = set()
        rec_stack = set()
        cycles = []
        
        def dfs(node, path):
            if node in rec_stack:
                # Found a cycle
                cycle_start = path.index(node)
                cycle = path[cycle_start:] + [node]
                cycles.append(cycle)
                return
            
            if node in visited:
                return
            
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for dependency in self.dependencies.get(node, []):
                dfs(dependency, path.copy())
            
            rec_stack.remove(node)
        
        for file_path in self.dependencies:
            if file_path not in visited:
                dfs(file_path, [])
        
        return cycles


def main():
    parser = argparse.ArgumentParser(description="Analyze C++ dependencies")
    parser.add_argument("--source-dir", required=True, help="Source directory to analyze")
    parser.add_argument("--output", help="Output file for dependency report (JSON)")
    parser.add_argument("--format", choices=["json", "dot"], default="json", 
                       help="Output format")
    
    args = parser.parse_args()
    
    analyzer = DependencyAnalyzer(args.source_dir)
    report = analyzer.analyze()
    
    if args.format == "json":
        print("Dependency Analysis Results:")
        print(f"Total files analyzed: {report['total_files']}")
        print(f"Circular dependencies found: {len(report['circular_dependencies'])}")
        
        if report['circular_dependencies']:
            print("\nCircular dependencies:")
            for i, cycle in enumerate(report['circular_dependencies']):
                print(f"  {i+1}: {' -> '.join(cycle)}")
        
        print("\nMost depended upon files:")
        for file_path, count in report['most_depended_upon']:
            print(f"  {file_path}: {count} dependents")
    
    # Save report
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()