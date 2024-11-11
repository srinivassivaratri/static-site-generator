# Static Site Generator

A lightweight static site generator that converts Markdown files into a fully functioning website, with no web development knowledge required.

## Why?

I needed to create multiple simple websites but WordPress and other CMS platforms were overkill, required databases, and constant maintenance. I built this static site generator that takes Markdown files and generates clean HTML - now I can create and deploy websites in minutes with just text files.

## Quick Start

1. Install dependencies:
```bash
python -m pip install --upgrade pip
```

2. Clone and run:
```bash
git clone https://github.com/yourusername/static-site-generator
cd static-site-generator
./main.sh
```

3. Your site will be generated in the `public` folder

## Usage

1. Write your content in Markdown files in the `content` directory
2. Add any images/CSS/JS files to the `static` directory
3. Run `./main.sh` to generate your site
4. Deploy the `public` directory to any web host

### Supported Markdown Features

- Headers (# h1, ## h2, etc)
- Bold text (**bold**)
- Italic text (*italic*)
- Code blocks (```code```)
- Links ([text](url))
- Images (![alt](url))
- Lists (ordered and unordered)
- Blockquotes (> quote)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`./test.sh`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request
