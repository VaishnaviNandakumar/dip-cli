import filetype
kind = filetype.guess('sample.png')
print(kind.mime)