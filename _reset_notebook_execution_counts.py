#!/usr/bin/env python3
"""Pre-commit hook to reset execution counts in Jupyter notebooks."""

import json
import sys
from pathlib import Path


def reset_notebook_execution_counts(notebook_path):
    """Reset all execution counts in a Jupyter notebook to None.

    Parameters
    ----------
    notebook_path : Path
        Path to the Jupyter notebook file

    Returns
    -------
    bool
        True if changes were made, False otherwise
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    modified = False

    # Reset execution_count for cells
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            if cell.get('execution_count') is not None:
                cell['execution_count'] = None
                modified = True

            # Reset execution_count in outputs
            for output in cell.get('outputs', []):
                if output.get('execution_count') is not None:
                    output['execution_count'] = None
                    modified = True

                # Remove execution time metadata
                if 'metadata' in output:
                    if 'execution' in output['metadata']:
                        del output['metadata']['execution']
                        modified = True
                    # Clean up empty metadata
                    if not output['metadata']:
                        del output['metadata']
                        modified = True

    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
            f.write('\n')

    return modified


def main():
    """Process all notebook files passed as arguments."""
    modified_files = []

    for file_path in sys.argv[1:]:
        path = Path(file_path)
        if path.suffix == '.ipynb':
            if reset_notebook_execution_counts(path):
                modified_files.append(file_path)
                print(f"Reset execution counts in {file_path}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
