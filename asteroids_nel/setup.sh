Official Documentation: https://www.pygame.org/docs/

filtz21@Panda2:~/claudecode$ uv init --python 3.13 asteroids_nel
	# Initialized project `asteroids-nel` at `/home/filtz21/claudecode/asteroids_nel`
filtz21@Panda2:~/claudecode$ cd asteroids_nel/
filtz21@Panda2:~/claudecode/asteroids_nel$ uv venv
	# Using CPython 3.13.14
	# Creating virtual environment at: .venv
	# Activate with: source .venv/bin/activate

## Activate the Virtual environment
filtz21@Panda2:~/claudecode/asteroids_nel$ source .venv/bin/activate
(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ 

## (uv add) is uv's equivalent of pip install / apt install — it fetches the package (here pygame version 2.6.1 from PyPI) and installs it into your project's .venv/.
## it writes pygame==2.6.1 into pyproject.toml and updates uv.lock
(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ uv add pygame==2.6.1
	# Resolved 2 packages in 1.42s
	# Prepared 1 package in 2.84s
	# Installed 1 package in 49ms
	#  + pygame==2.6.1
## Open main.py. It should have been created when you ran uv init.
(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ nvim main.py
import pygame
print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
:wq

(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ uv run main.py
	# pygame 2.6.1 (SDL 2.28.4, Python 3.13.14)
	# Hello from the pygame community. https://www.pygame.org/contribute.html
	# Starting Asteroids with pygame version: 2.6.1(asteroids_nel) filtz21@Panda2:~/claudecode/asteroids_nel$ uv run main.py
	# pygame 2.6.1 (SDL 2.28.4, Python 3.13.14)
	# Hello from the pygame community. https://www.pygame.org/contribute.html
	# Starting Asteroids with pygame version: 2.6.1





