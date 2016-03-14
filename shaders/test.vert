#version 120

attribute vec3 vPos;
attribute vec2 vTex;

uniform mat4 MVP;

varying vec2 tex_coord;

void main() {
    gl_Position =  MVP * vec4(vPos, 1);
    tex_coord = vTex;
}