def markdown_to_blocks(markdown):
    # Its job is to split the input string into distinct blocks and strip any leading or trailing whitespace from each block. It should also remove any "empty" blocks due to excessive newlines.
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    block_type_paragraph = "paragraph"
    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered_list = "unordered_list"
    block_type_ordered_list = "ordered_list"

    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if (
        block.startswith('#')
        or block.startswith('##')
        or block.startswith('###')
        or block.startswith('####')
        or block.startswith('#####')
        or block.startswith('######')
    ):
        return block_type_heading
    
    # Code blocks must start with 3 backticks and end with 3 backticks.
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    if block.startswith('>'):
        return block_type_quote
    if block.startswith('* ') or block.startswith('- '):
        return block_type_unordered_list
    if block[0].isdigit() and block[1] == '.':
        return block_type_ordered_list
    else:
        return block_type_paragraph
     
    
    



# def markdown_to_blocks(markdown):
#     # Its job is to split the input string into distinct blocks and strip any leading or trailing whitespace from each block. It should also remove any "empty" blocks due to excessive newlines.
#     blocks = markdown.split("\n\n")
#     for block in blocks: 
#         block.strip()
#         if block == "":
#             blocks.remove(block)
#     return blocks
          