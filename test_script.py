#!/usr/bin/env python3
"""
Test script for the Today in History Logger
Run this to test if everything works before pushing to GitHub
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import requests
        from datetime import datetime
        import random
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_api_connection():
    """Test if the history API is accessible"""
    try:
        import requests
        url = "https://history.muffinlabs.com/date/1/1"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ API connection successful")
            return True
        else:
            print(f"❌ API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False

def test_script_execution():
    """Test if the main script can be executed"""
    try:
        import subprocess
        result = subprocess.run([sys.executable, "history_logger.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ Script execution successful")
            print(f"Output: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Script execution failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Script execution error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Today in History Logger...\n")
    
    tests = [
        ("Import Test", test_imports),
        ("API Connection Test", test_api_connection),
        ("Script Execution Test", test_script_execution)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready to push to GitHub.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 