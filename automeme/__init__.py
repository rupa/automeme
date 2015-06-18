from meme import generate

def cli():
    import sys
    sys.stdout.write(u'{0}\n'.format(generate()))
