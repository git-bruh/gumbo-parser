project(
    'gumbo-parser',
    'c',
    license: 'Apache-2.0',
    default_options: ['buildtype=debugoptimized', 'warning_level=3', 'c_std=c99'],
)

cc = meson.get_compiler('c')

src = [
    'src/attribute.c',
    'src/char_ref.c',
    'src/error.c',
    'src/gumbo_edit.c',
    'src/parser.c',
    'src/string_buffer.c',
    'src/string_piece.c',
    'src/svg_attrs.c',
    'src/svg_tags.c',
    'src/tag.c',
    'src/tokenizer.c',
    'src/utf8.c',
    'src/util.c',
    'src/vector.c',
]

c_args = ['-fstack-protector-strong']

warning_c_args = ['-Wno-missing-field-initializers']

headers = ['include/gumbo.h', 'include/tag_enum.h']

incdir = include_directories('include')

add_project_arguments(c_args, language: 'c')
add_project_arguments(cc.get_supported_arguments(warning_c_args), language: 'c')

install_headers(headers)
gumbo_parser = library(
    'gumbo',
    src,
    include_directories: incdir,
    gnu_symbol_visibility: 'hidden',
    install: true,
)

gumbo_dep = declare_dependency(
    include_directories: incdir,
    link_with: gumbo_parser,
)
