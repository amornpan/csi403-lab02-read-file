"""
Lab 02: Reading Markdown Files - Auto-grading Tests
"""

import pytest
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Get paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_PATH = os.path.join(BASE_DIR, 'exercise', 'Lab02_Exercise.ipynb')
DATA_DIR = os.path.join(BASE_DIR, 'data')


@pytest.fixture(scope="session")
def student_namespace():
    """Execute student notebook and return namespace with variables."""
    
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create namespace with proper working directory
    namespace = {'__name__': '__main__'}
    
    # Change to exercise directory for relative paths to work
    original_dir = os.getcwd()
    exercise_dir = os.path.join(BASE_DIR, 'exercise')
    os.chdir(exercise_dir)
    
    try:
        for cell in nb.cells:
            if cell.cell_type == 'code':
                # Skip verification cells
                if '# Quick check' in cell.source or '# Verification' in cell.source:
                    continue
                try:
                    exec(cell.source, namespace)
                except Exception as e:
                    print(f"Cell execution warning: {e}")
    finally:
        os.chdir(original_dir)
    
    return namespace


class TestExercise1:
    """Test Exercise 1: Read File Content (25 points)"""
    
    def test_file_content_exists(self, student_namespace):
        assert 'file_content' in student_namespace, "Variable 'file_content' not found"
    
    def test_file_content_is_string(self, student_namespace):
        assert isinstance(student_namespace.get('file_content'), str), "file_content should be a string"
    
    def test_file_content_has_rubella(self, student_namespace):
        content = student_namespace.get('file_content', '')
        assert 'Rubella' in content, "file_content should contain 'Rubella'"


class TestExercise2:
    """Test Exercise 2: Count Characters (25 points)"""
    
    def test_char_count_exists(self, student_namespace):
        assert 'char_count' in student_namespace, "Variable 'char_count' not found"
    
    def test_char_count_is_int(self, student_namespace):
        assert isinstance(student_namespace.get('char_count'), int), "char_count should be an integer"
    
    def test_char_count_correct(self, student_namespace):
        content = student_namespace.get('file_content', '')
        expected = len(content)
        actual = student_namespace.get('char_count', 0)
        assert actual == expected, f"char_count should be {expected}, got {actual}"


class TestExercise3:
    """Test Exercise 3: Count Lines (25 points)"""
    
    def test_line_count_exists(self, student_namespace):
        assert 'line_count' in student_namespace, "Variable 'line_count' not found"
    
    def test_line_count_is_int(self, student_namespace):
        assert isinstance(student_namespace.get('line_count'), int), "line_count should be an integer"
    
    def test_line_count_correct(self, student_namespace):
        content = student_namespace.get('file_content', '')
        expected = len(content.split('\n'))
        actual = student_namespace.get('line_count', 0)
        assert actual == expected, f"line_count should be {expected}, got {actual}"


class TestExercise4:
    """Test Exercise 4: Find Text (25 points)"""
    
    def test_symptom_count_exists(self, student_namespace):
        assert 'symptom_count' in student_namespace, "Variable 'symptom_count' not found"
    
    def test_symptom_count_is_int(self, student_namespace):
        assert isinstance(student_namespace.get('symptom_count'), int), "symptom_count should be an integer"
    
    def test_symptom_count_correct(self, student_namespace):
        content = student_namespace.get('file_content', '')
        expected = content.lower().count('symptom')
        actual = student_namespace.get('symptom_count', 0)
        assert actual == expected, f"symptom_count should be {expected}, got {actual}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
