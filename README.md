
# Autoscratch
Copies the source directory or object to a directory called "autoscratch"
in the scratch dir, imitating the dir structure in that dir.
The script then creates a symlink in its place in its original position.

## Example:
```bash  
autoscratch ~/the_project_name/model_a/checkpoints/
```
1. Creates a folder at `/network/scratch/[u]/[username]/autoscratcher/project_name/model_a/`
2. Moves the checkpoints folder into that folder
3. Creates a symbolic link `/home/mila/[u]/[username]/project_name/model_a/checkpoints` to `/network/scratch/[u]/[username]/autoscratcher/project_name/model_a/checkpoints`.


