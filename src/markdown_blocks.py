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
          