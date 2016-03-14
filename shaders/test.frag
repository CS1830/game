#version 120

varying vec2 tex_coord;

uniform sampler2D texture;

uniform float life;

void main() {
    gl_FragColor = texture2D(texture, tex_coord) * vec4(0.3, 0.7, 1.0, life);
}