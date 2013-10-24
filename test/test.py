# coding: utf-8

import random
import codecs
import string
import subprocess
import os
import sys

sys.path.append('../')

from composer import renderBlock
from content.models import instanceFromRaw

try:
    os.mkdir('output')
except OSError:
    pass

subprocess.call(['compass', 'compile', '--sass-dir', '.', '--css-dir', 'output/'])


GREEKED = [c for c in u' ▁▂▃▄▅▆▇█▉▊▋▌▍▎' + ' '*10]
CHARS   = [c for c in (string.letters + ' '*10)]
def randChars(n=100, greek=True):
    if greek:
        chars = GREEKED
    else:
        chars = CHARS
    return u''.join([random.choice(chars) for i in xrange(n)])



sample_data = [
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'heading',
        'content': randChars(10),
        'annotations': [],
        'layout': {
            'align': 'left',
        }
    },
    {
        'id': 'image:1234',
        'alt_text' : "alt text",
        'type': 'image',
        'content': {
            '640': {
                'url': 'http://placekitten.com/640/400/',
            },
            '1280': {
                'url': 'http://placekitten.com/1280/800/',
            },
        },
        'original': {
            'url': 'http://placekitten.com/2560/1600/',
        },
        'annotations': [{
            'type': 'caption',
            'content': randChars(20),
        }],
        'layout': {
            'size': 'large',
            'position': 'right',
        }
    },
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'paragraph',
        'content': randChars(400),
        'annotations': [{
            'type': 'link',
            'start': 10,
            'end': 20,
            'url': 'http://example.com',
        },{
            'type': 'emphasis',
            'start': 30,
            'end': 40,
        },{
            'type': 'strong',
            'start': 35,
            'end': 50,
        }],
        'layout': {
            'align': 'left',
        }
    },
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'quote',
        'content': randChars(400),
        'annotations': [],
        'layout': {
            'align': 'center',
        }
    },
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'pre',
        'content': randChars(400),
        'annotations': [],
        'layout': {
            'align': 'left',
        }
    },
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'paragraph',
        'content': randChars(400),
        'annotations': [],
        'layout': {
            'align': 'left',
        }
    },
    {
        'id': 'embed:abcde',
        'type': 'embed',
        'content': '<iframe width="560" height="315" src="//www.youtube.com/embed/JAbug3AhYmw" frameborder="0" allowfullscreen></iframe>',
        'annotations': [],
        'layout': {
            'size': 'medium',
            'position': 'left',
        }
    },
    {
        'id': 'text:1234',
        'type': 'text',
        'role': 'paragraph',
        'content': randChars(400),
        'annotations': [],
        'layout': {
            'align': 'left',
        }
    },
]

output = '<link rel="stylesheet" type="text/css" href="test.css"><meta charset="utf-8">'
output += u''.join(map(lambda x: renderBlock(instanceFromRaw(x)), sample_data))
with codecs.open('output/test.html', 'w', 'utf-8') as f:
    f.write(output)
