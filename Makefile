BIN = bin
SRC = src
IMG = images
OUT = html

HOST = boxofjunk
DEST = $(HOST):domains/automeme.net/html
DEST_DEV = $(HOST):domains/dev.automeme.net/html

SRC_FILES = $(SRC)/.htaccess $(SRC)/*.py $(SRC)/*.cgi $(SRC)/*.html $(SRC)/*.txt $(SRC)/*.css
IMG_FILES = $(IMG)/*.png $(IMG)/*.jpg $(IMG)/*.gif

JS_JQUERY = $(SRC)/jquery-1.3.2.min.js
JS_FILES  = $(SRC)/plugins.js $(SRC)/pushbutan.js
JS_OUTPUT = $(OUT)/pushbutan.js


default:
	@echo "make live or make dev?"

live: html
	chmod 711 $(OUT)
	rsync -Pcav --del --rsh=ssh $(OUT)/ $(DEST)/

dev: html
	chmod 711 $(OUT)
	rsync -Pcav --del --rsh=ssh $(OUT)/ $(DEST_DEV)/

html: images javascript update

update:
	cp -p $(SRC_FILES) $(IMG_FILES) $(OUT)

javascript:
	cp $(JS_JQUERY) $(JS_OUTPUT)
	cat $(JS_FILES) | $(BIN)/jsmin.py >> $(JS_OUTPUT)

images: $(OUT)/butan-original.png

$(OUT)/butan-original.png:
	$(BIN)/make_butans $(OUT)

clean:
	rm -rfv $(OUT)
	mkdir $(OUT)
