import json
import os
import sys

# Score configuration
SCORES = {
    "word_count": 10,
    "char_frequency": 10,
    "sentiment_analysis": 10,
    "text_summary": 10
}

def calculate_score():
    """Calculate the total score based on test results"""
    score = 0
    passed_tests = []
    failed_tests = []
    
    try:
        # Run tests and capture results
        import subprocess
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/test_text_processor.py", "-v"],
            capture_output=True,
            text=True
        )
        
        # Parse test results
        output = result.stdout
        
        # Check each test function
        for test_name, max_score in SCORES.items():
            if f"test_{test_name}" in output and "PASSED" in output:
                score += max_score
                passed_tests.append(test_name)
            else:
                failed_tests.append(test_name)
        
        # Create score report
        report = {
            "total_score": score,
            "max_score": sum(SCORES.values()),
            "passed_tests": passed_tests,
            "failed_tests": failed_tests,
            "test_results": output
        }
        
        # Write score to JSON file
        with open("score.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        
        print(f"Score calculated: {score}/{sum(SCORES.values())}")
        print("Score saved to score.json")
        
    except Exception as e:
        print(f"Error calculating score: {e}")
        # Create error report
        report = {
            "total_score": 0,
            "max_score": sum(SCORES.values()),
            "error": str(e)
        }
        with open("score.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    calculate_score()