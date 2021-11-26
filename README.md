
# Autoscratch
Moves the target file or directory to the scratch in a subdirectory imitating its current position in $HOME, and then replaces it by a symlink.

# Example:
```bash  
autoscratch ~/the_project_name/model_a/checkpoints/
```
1. Creates a folder at `/network/scratch/[u]/[username]/autoscratch/project_name/model_a/`
2. Moves the checkpoints folder into that folder
3. Creates a symbolic link `/home/mila/[u]/[username]/project_name/model_a/checkpoints` to `/network/scratch/[u]/[username]/autoscratch/project_name/model_a/checkpoints`.

# Setup
```
git clone git@github.com:JulesGM/autoscratch.git
cd autoscratch
pip install .
```
