.PHONY: public
public: qtail content/default_config.py
	hugo --gc --minify

.PHONY: qtail
qtail:
	(cd themes/qtail/ && npm run build-qtail)

content/default_config.py:
	curl --fail --output $@ https://raw.githubusercontent.com/qtile/qtile/master/libqtile/resources/default_config.py
	# delete the license header; it's annoying to scroll past
	sed '1,26d' -i $@

deps:
	(cd themes/qtail/ && npm install @tailwindcss/typography)

clean:
	rm -rf public resources themes/qtail/assets/style.css content/default_config.py
