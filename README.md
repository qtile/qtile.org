# Qtile website
## Vocab
- `qtile` or `qtile.org`: qtile's website.
- `qtail`: Hugo theme built using TailwindCSS for qtile.org website.

## Dependencies
- Hugo - [Hugo installation docs for your OS](https://gohugo.io/installation/)
- NodeJS
- NPM

## Setting up qtile.org locally
- Install Hugo, nodejs and npm on your computer 
- Fork and clone [qtile.org repository](https://github.com/qtile/qtile.org) locally to your computer
- Go to `qtail` directory. `cd qtile.org/themes/qtail`
- Run `npm install` in your terminal. This will install Tailwind CSS and it's dependencies necessary for qtile.org.
- Go to the main website directory `/qtile.org` and run `hugo server` or `hugo server --disableFastRender`
- Run `npm run watch-qtail` on one terminal in `themes/qtail` and `hugo server --disableFastRender` in another terminal window/tab for watching and generating file changes on the fly. This is the ideal environment for making changes.

## Commands for making changes to qtile.org

| Commands      | Description
| ------------- | -----------
| `hugo`        | Publish / generate the qtile.org website files. Run this after making any content or theme changes. This will generate the files necessary in `/public` directory. If this is the first time running the command, it will create the `/public` directory.
| `hugo server` or `hugo server --disableFastRender` | Live server for hotloading after any changes to the site contents.
| `npm run build-qtail` | Generates the new `style.css` using tailwindcss cli after any css change
| `npm run watch-qtail` | Generates `style.css` and hotreloads `style.css` based on every change
