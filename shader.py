import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import time

# Vertex shader source code
vertex_shader = """
#version 330 core
layout(location = 0) in vec4 position;
void main()
{
    gl_Position = position;
}
"""

# Fragment shader source code
fragment_shader = """
#version 330 core
out vec4 outColor;
uniform float time;
void main()
{
    vec2 position = gl_FragCoord.xy / vec2(800, 600);

    // Base wave patterns
    float wave1 = sin(position.x * 10.0 + time) * cos(position.y * 10.0 + time);
    float wave2 = sin(position.x * 15.0 + time * 0.5) * cos(position.y * 15.0 + time * 0.5);
    float wave3 = sin(position.x * 20.0 - time * 1.5) * cos(position.y * 20.0 - time * 1.5);

    // Combine waves
    float combinedWaves = wave1 + wave2 + wave3;

    // Color pattern based on combined waves
    float r = 0.5 + 0.5 * sin(combinedWaves * 3.0 + time);
    float g = 0.5 + 0.5 * cos(combinedWaves * 2.0 - time);
    float b = 0.5 + 0.5 * sin(combinedWaves * 4.0 + time * 0.5);

    outColor = vec4(r, g, b, 1.0);
}
"""

def create_shader_program(vertex_src, fragment_src):
    shader = compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )
    return shader

def main():
    # Initialize Pygame
    pygame.init()

    # Set OpenGL attributes
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # Attempt to create an OpenGL context
    try:
        screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    except pygame.error as e:
        print(f"Failed to create OpenGL 3.3 context: {e}")
        return

    pygame.display.set_caption('Animated Shader Demo')

    # Create a Vertex Array Object (VAO)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

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

    # Define the layout of the vertex data
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Get the location of the uniforms
    time_location = glGetUniformLocation(shader, 'time')

    # Main loop
    running = True
    start_time = time.time()
    accumulated_time = 0.0
    speed = 1.0
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    speed += 0.1
                elif event.key == K_DOWN:
                    speed -= 0.1

        # Calculate the elapsed time
        current_time = time.time()
        frame_time = current_time - start_time
        start_time = current_time
        accumulated_time += frame_time * speed

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Update the uniforms
        glUniform1f(time_location, accumulated_time)

        # Draw the quad
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

        # Swap the buffers
        pygame.display.flip()

    # Cleanup
    glDeleteBuffers(1, [vbo])
    glDeleteVertexArrays(1, [vao])
    glDeleteProgram(shader)
    pygame.quit()

if __name__ == '__main__':
    main()
