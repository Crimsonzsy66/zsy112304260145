"""
Direct execution script to run the optimized sentiment analysis model
Best configuration: TF-IDF (1-4 gram, 100k features) + LinearSVC (C=0.5)
Expected CV AUC: ~0.968
"""
import sys
import os
from pathlib import Path
from datetime import datetime
import time

code_dir = r'c:\Users\ASUS\Downloads\baomihua\baomihua\code'
os.chdir(code_dir)

if str(code_dir) not in sys.path:
    sys.path.insert(0, code_dir)

sys.argv = [
    'experiment_word2vec_auc.py',
    '--feature', 'tfidf',
    '--classifier', 'linear_svc',
    '--lr-c', '0.5',
    '--ngram-min', '1',
    '--ngram-max', '4',
    '--max-features', '100000',
    '--folds', '5'
]

if __name__ == '__main__':
    start_time = time.time()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting optimized model training...")
    print("Configuration: TF-IDF (1-4 gram) + LinearSVC (C=0.5)")
    print(f"Working directory: {os.getcwd()}")
    print("-" * 60)

    try:
        from experiment_word2vec_auc import main

        main()
        elapsed_time = time.time() - start_time
        print("-" * 60)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Training completed successfully!")
        print(f"Total time: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)")
    except ModuleNotFoundError as e:
        print(f"[ERROR] Module not found: {str(e)}")
        print(f"Please ensure you're running from the correct directory and all files exist.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Training failed: {str(e)}")
        raise
