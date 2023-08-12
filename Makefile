.PHONY: public
public: qtail
	hugo --gc --minify

.PHONY: qtail
qtail:
	(cd themes/qtail/ && npm run build-qtail)

deps:
	(cd themes/qtail/ && npm install @tailwindcss/typography)

clean:
	rm -rf public resources themes/qtail/assets/style.css
