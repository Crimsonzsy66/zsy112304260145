"""
Install gensim if missing and run the optimized model
"""
import subprocess
import sys
import os

def install_gensim():
    """Install gensim if not already installed"""
    try:
        import gensim
        print(f"✓ gensim {gensim.__version__} is already installed")
        return True
    except ImportError:
        print("✗ gensim not found. Installing...")
        print("-" * 50)

        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "gensim"])
            print("-" * 50)
            print("✓ gensim installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install gensim: {e}")
            print("\nPlease run manually:")
            print("  pip install gensim")
            return False

def main():
    print("="*60)
    print("  Optimized Sentiment Analysis Model Runner")
    print("="*60)
    print()

    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Install gensim if needed
    if not install_gensim():
        sys.exit(1)

    print()
    print("="*60)
    print("  Starting model training...")
    print("="*60)
    print()
    print("Configuration:")
    print("  - Feature: TF-IDF (1-4 gram, 100k features)")
    print("  - Classifier: LinearSVC (C=0.5)")
    print("  - CV Folds: 5")
    print("  - Expected CV AUC: ~0.968")
    print()
    print("-"*60)
    print()

    # Run the optimized script
    try:
        exec(open('run_optimized.py').read())
    except Exception as e:
        print()
        print("="*60)
        print(f"✗ Error running model: {e}")
        print("="*60)
        sys.exit(1)

if __name__ == "__main__":
    main()
