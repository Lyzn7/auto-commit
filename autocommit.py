import os
import git
from datetime import datetime

# Konfigurasi
repo_path = "/path/to/your/repo"  # Ganti dengan path repositori lokal
commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
branch = "main"

def auto_commit():
    repo = git.Repo(repo_path)
    
    # Menambahkan semua perubahan
    repo.git.add(all=True)
    
    # Commit perubahan
    repo.index.commit(commit_message)
    
    # Push ke GitHub
    origin = repo.remote(name="origin")
    origin.push(refspec=f"{branch}:{branch}")

    print(f"Committed and pushed: {commit_message}")

if __name__ == "__main__":
    auto_commit()
