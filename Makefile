BIN = bin
SRC = src
IMG = images
OUT = html

HOST = boxofjunk
DEST = $(HOST):domains/automeme.net/html

SRC_FILES = $(SRC)/.htaccess $(SRC)/*.py $(SRC)/*.cgi $(SRC)/*.html $(SRC)/*.txt $(SRC)/*.css
IMG_FILES = $(IMG)/*.png $(IMG)/*.jpg $(IMG)/*.gif

JS_JQUERY = $(SRC)/jquery-1.3.2.min.js
JS_FILES  = $(SRC)/plugins.js $(SRC)/pushbutan.js
JS_OUTPUT = $(OUT)/pushbutan.js


live: html
	chmod 711 $(OUT)
	rsync -Pcav --del --rsh=ssh $(OUT)/ $(DEST)/

html: images javascript update

update:
	cp -p $(SRC_FILES) $(IMG_FILES) $(OUT)

javascript: $(JS_JQUERY) $(JS_FILES) $(JS_OUTPUT)

$(JS_OUTPUT):
	cp $(JS_JQUERY) $(JS_OUTPUT)
	cat $(JS_FILES) | $(BIN)/jsmin.py >> $(JS_OUTPUT)

images: $(OUT)/butan-original.png

$(OUT)/butan-original.png:
	$(BIN)/make_butans $(OUT)

clean:
	rm -rfv $(OUT)
	mkdir $(OUT)
