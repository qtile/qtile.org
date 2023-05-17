all:
	cd themes/qtail/; 
	npm run build-qtail;
public:
	hugo --gc --minify;

clean:
	rm -rf public resources themes/qtail/assets/style.css
