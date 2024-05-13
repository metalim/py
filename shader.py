import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex shader source code
vertex_shader = """
#version 120
attribute vec4 position;
void main()
{
    gl_Position = position;
}
"""

# Fragment shader source code
fragment_shader = """
#version 120
void main()
{
    vec2 position = gl_FragCoord.xy / vec2(800, 600);
    gl_FragColor = vec4(position.x, position.y, 0.5 + 0.5 * sin(position.x * 10.0), 1.0);
}
"""

def create_shader_program(vertex_src, fragment_src):
    shader = compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )
    return shader

def main():
    # Initialize Pygame and set up the window
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Shader Demo')

    # Compile and use the shader program
    shader = create_shader_program(vertex_shader, fragment_shader)
    glUseProgram(shader)

    # Define the vertex data for a full-screen quad
    vertex_data = np.array([
        -1.0, -1.0,
         1.0, -1.0,
        -1.0,  1.0,
         1.0,  1.0,
    ], dtype=np.float32)

    # Create a Vertex Buffer Object (VBO) and upload the vertex data
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

    # Get the position attribute location from the shader program
    position_location = glGetAttribLocation(shader, 'position')
    glEnableVertexAttribArray(position_location)
    glVertexAttribPointer(position_location, 2, GL_FLOAT, GL_FALSE, 0, None)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the quad
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

        # Swap the buffers
        pygame.display.flip()

    # Cleanup
    glDeleteBuffers(1, [vbo])
    glDeleteProgram(shader)
    pygame.quit()

if __name__ == '__main__':
    main()
