import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section is not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    # takes raw text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images
    # Because it's such a pain in the butt, I'll just give you the regex I used: r"!\[(.*?)\]\((.*?)\)". If you want to understand each piece, again, I'd recommend pasting it into regexr
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # takes raw text and returns a list of tuples. Each tuple should contain the text and the URL of any markdown links
    # Because it's such a pain in the butt, I'll just give you the regex I used: r"\[(.*?)\]\((.*?)\)". If you want to understand each piece, again, I'd recommend pasting it into regexr
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    # Again, I don't want to give you a step by step guide, but here are some tips:

    # Make use of the extraction functions we wrote

    # If there are no images/links, just put the TextNode back in the original list
    # Don't append any TextNodes to the output that have empty contents
    # Your split_nodes_image and split_nodes_link functions will be very similar.
    # You can use the .split() method with large strings as the delimeter, and it has an optional second "maxsplits" parameter, which you can set to 1 if you only want to split the string once at most. For each image extracted from the text, I just split the text before and after the image markdown.
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    # This function should be simple now that you've done all the hard work. It should just call each of your splitting functions in turn.
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimeter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimeter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimeter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    








    

    







