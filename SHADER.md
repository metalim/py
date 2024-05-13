# Animated Shader Demo

This project demonstrates an animated shader using Pygame and PyOpenGL. The animation features a dynamic wave pattern that can be adjusted in speed using the UP and DOWN arrow keys.

## Requirements

- Python 3.12.3 or later
- Pygame 2.5.2
- PyOpenGL 3.1.6

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/metalim/py.git
cd py
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:

- On Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install the Required Packages

Install the necessary packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

Run the Python script to start the animated shader demo:

```bash
python animated_shader_demo.py
```

### Controls

- **UP Arrow Key**: Increase the speed of the animation.
- **DOWN Arrow Key**: Decrease the speed of the animation.

## Project Structure

```plaintext
py/
│
├── animated_shader_demo.py
├── requirements.txt
└── README.md
```

## Dependencies

- Pygame 2.5.2: A set of Python modules designed for writing video games.
- PyOpenGL 3.1.6: Python bindings for OpenGL.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Pygame community for the continuous support and development of Pygame.
- PyOpenGL for providing the OpenGL bindings for Python.
