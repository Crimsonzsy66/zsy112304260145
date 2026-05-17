"""
Check if all required dependencies are installed
"""
def check_dependencies():
    required = {
        'numpy': 'numpy',
        'pandas': 'pandas',
        'sklearn': 'scikit-learn',
        'gensim': 'gensim',
        'bs4': 'beautifulsoup4',
        'lxml': 'lxml'
    }

    missing = []
    installed = []

    for name, package in required.items():
        try:
            __import__(name)
            installed.append(package)
            print(f"✓ {package:20s} installed")
        except ImportError:
            missing.append(package)
            print(f"✗ {package:20s} MISSING")

    print("\n" + "="*50)
    if missing:
        print(f"Missing packages: {', '.join(missing)}")
        print("\nInstall missing packages with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    else:
        print("All dependencies are installed! ✓")
        print("\nYou can now run:")
        print("  python run_optimized.py")
        return True

if __name__ == "__main__":
    check_dependencies()
