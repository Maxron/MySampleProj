## Makefile Environment 
PROJECT_NAME := MySamplePorj
WORKSPACE := $(PWD)
DIST_FOLDER := $(WORKSPACE)/dist/
BUILD_TARGET := $(WORKSPACE)/build/
EGG_TARGET := $(WORKSPACE)/MySampleProj.egg-info/
DEMO_COMMAND := demo_wei

TARGET_FILE = $(shell find dist -iname MySampleProj*.tar.gz |sort -r |head -n 1)

.PHONY: build
build: app/__main__.py
	@echo "Running setup.py build"
	python setup.py sdist bdist_wheel bdist_egg

.PHONY: install
install: $(TARGET_FILE)
	@echo "Target file: "$(TARGET_FILE)
ifeq ($(TARGET_FILE),)
	$(error "No such file found !!")
else
	pip install $(TARGET_FILE)
endif

.PHONY: demo
demo:
ifeq ( ,$(shell which $(DEMO_COMMAND)))
	$(error "Demo command not found !! : $(DEMO_COMMAND)")
else
	demo_wei
endif

.PHONY: clean
clean:
	@echo "Delete output files..."
	rm -rf $(DIST_FOLDER) $(EGG_TARGET) $(BUILD_TARGET)

.PHONY: all
all: build
