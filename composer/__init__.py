from content import Text, Image, Embed, Container
from cgi import escape

default_base_class_names = {
    Text.type   : 'TextBlock',
    Image.type  : 'ImageBlock',
    Embed.type  : 'EmbedBlock',
}

# Override base_class_name to use different selectors
def renderBlock(block, classes=None, attrs=None, base_class_name=None):
    print block.toJSON()
    # because classes=[] in the sig is bad
    if not classes:
        classes = []
    if not attrs:
        attrs = {}
    if not base_class_name:
        base_class_name = default_base_class_names[block.type]

    attrs['data-content_id'] = block.id
    classes.append(base_class_name)

    for prop, val in block.layout.items():
        attrs[u"data-" + prop] = val

    if block.get('role'):
        attrs[u"data-role"] = block.role


    block_template = u"<{tag} class='{classes}' {attrs}>{content}</{tag}>"

    if block.type == Image.type:
        content = u'<div class="content">'
        content += u"<img src='{0}'>".format(_pickImageSrc(block))
        content += _getCaption(block)
        content += '</div>'
    elif block.type == Text.type:
        content = _renderBlockContent(block)
    elif block.type == Embed.type:
        content = u'<div class="content">'
        if block.content[0:7] == '<iframe':
            content += block.content
        else:
            attrs['data-embed_url'] = block.content
        content += _getCaption(block)
        content += '</div>'

    attrs = ["{0}='{1}'".format(k,v) for k, v in attrs.items()]
    markup = block_template.format(
            tag         = _pickTag(block),
            classes     = escape(u' '.join(classes)),
            attrs       = escape(u' '.join(attrs)),
            content     = content
        )
    return markup


    # if block.get('content', None):
    #     embed_content = block.get('content')
    #     if embed_content[0:7] == '<iframe':
    #         embed_url = ''
    #     else:
    #         embed_url = "data-embed_url='%s'" % embed_content
    #         embed_content = ''
    #     markup_str = u"""
    #         <div data-content_id='{content_id}' class='EmbedBlock {classes}' {url}>
    #             <div class="content">
    #                 {content}
    #                 {caption}
    #             </div>
    #         </div>
    #     """.format(
    #         url     = embed_url,
    #         classes = _parse_layout(block),
    #         content = embed_content,
    #         caption = get_caption(block),
    #         content_id = block['id']
    #     )
    # else:
    #     markup_str = ''
    # return markup_str



def _pickImageSrc(block):
    return block.content.get('640', {}).get('url')

def _pickTag(block):
    if block.type == Text.type:
        TAGS = {
            'paragraph' : 'p',
            'pre'       : 'p',
            'quote'     : 'blockquote',
            'heading'   : 'h2',
        }
        return TAGS.get(block.role, 'p')
    return 'div'

def _renderBlockContent(block):
    return block.toHTML()

def _getCaption(block):
    annotations = block.get('annotations', [])
    if annotations:
        caption = filter(lambda a: 'caption' == a['type'], annotations)
        if caption:
            caption = caption[0]
            return u"<div class='Caption'>%s</div>" % (escape(caption['content']),)
    return u''
