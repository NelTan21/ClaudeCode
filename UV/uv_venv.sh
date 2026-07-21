uv init --python 3.13 your-project-name		# Creates new uv Project on folder
uv venv                 # creates .venv/ automatically
uv add requests         # installs into .venv, updates pyproject.toml + lockfile
uv run script.py        # runs inside .venv without manual activation
rm -rf .venv	# Deletes the venv directory itself (this is the answer to your question)
uv remove <package>	#Removes a dependency from pyproject.toml + lockfile — not the venv
uv cache 	# clean	Clears uv's global download/wheel cache (shared across all projects), unrelated to any one project's .venv/
uv python uninstall <version>	# Removes an installed Python interpreter version that uv manages — not a venv


# In Linux (and generally in Python tooling):
# -----------------------------------------------
# venv — Python's built-in module (python3 -m venv) for creating an isolated Python environment. 
# Each project gets its own folder (commonly .venv/) with its own interpreter and site-packages, 
# so dependencies don't clash between projects or pollute your system Python.
python3 -m venv .venv
source .venv/bin/activate   # Linux/WSL
pip install requests

filtz21@Panda2:~/claudecode/asteroids_nel$ uv venv
	# Using CPython 3.13.14
	# Creating virtual environment at: .venv
	# Activate with: source .venv/bin/activate
#

# Activate the Virtual environment
filtz21@Panda2:~/claudecode/asteroids_nel$ source .venv/bin/activate
(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ 

# uv add is uv's equivalent of pip install / apt install — it fetches the package (here pygame version 2.6.1 from PyPI) and installs it into your project's .venv/.
# it writes pygame==2.6.1 into pyproject.toml and updates uv.lock
(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ uv add pygame==2.6.1
	# Resolved 2 packages in 1.42s
	# Prepared 1 package in 2.84s
	# Installed 1 package in 49ms
	#  + pygame==2.6.1
#




