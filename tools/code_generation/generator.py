#!/usr/bin/env python3
"""
Code generator for C++ classes, services, and tests.
"""

import argparse
import os
import re
from pathlib import Path
import json


def load_template(template_path):
    """Load a template file."""
    with open(template_path, 'r') as f:
        return f.read()


def process_template(template_content, variables):
    """Process template with variables using simple substitution."""
    result = template_content
    
    for key, value in variables.items():
        pattern = f"{{{{{key}}}}}"
        result = result.replace(pattern, str(value))
    
    return result


def generate_class(config):
    """Generate C++ class files from configuration."""
    template_dir = Path(__file__).parent / "templates"
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load templates
    header_template = load_template(template_dir / "class_template.hpp.tmpl")
    impl_template = load_template(template_dir / "class_template.cpp.tmpl")
    
    # Process variables
    variables = {
        "CLASS_NAME": config["class_name"],
        "NAMESPACE": config["namespace"],
        "CLASS_DESCRIPTION": config.get("description", f"{config['class_name']} class"),
        "HEADER_FILE": f"{config['class_name'].lower()}.hpp"
    }
    
    # Generate header file
    header_content = process_template(header_template, variables)
    header_path = output_dir / f"{config['class_name'].lower()}.hpp"
    with open(header_path, 'w') as f:
        f.write(header_content)
    
    print(f"Generated header: {header_path}")
    
    # Generate implementation file
    impl_content = process_template(impl_template, variables)
    impl_path = output_dir / f"{config['class_name'].lower()}.cpp"
    with open(impl_path, 'w') as f:
        f.write(impl_content)
    
    print(f"Generated implementation: {impl_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate C++ code from templates")
    parser.add_argument("--config", required=True, help="Configuration JSON file")
    parser.add_argument("--type", required=True, choices=["class", "service", "test"], 
                       help="Type of code to generate")
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    if args.type == "class":
        generate_class(config)
    else:
        print(f"Generation type '{args.type}' not yet implemented")


if __name__ == "__main__":
    main()