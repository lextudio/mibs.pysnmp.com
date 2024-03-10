.DEFAULT_GOAL := help

fetch:  ## Download all mibs from the source
	@# Wget recursive
	wget --recursive --reject-regex 'index.html*' \
	  --no-parent --no-host-directories https://mibs.pysnmp.com/asn1/
	rm -rf asn1/index.html*

compile:  ## Compile all MIBs into .py files
	@total_files=$$(ls asn1 | wc -l); \
	finished_files=0; \
	for f in $$(ls asn1); do \
	  echo "## Compiling $$f: mibdump --mib-source=file://$$(pwd)/asn1 --destination-directory=./pysnmp $$f"; \
	  timeout 5s mibdump \
	    --mib-source=file://$$(pwd)/asn1 \
	    --destination-directory=./pysnmp \
	    $$f || echo "## Compiling $$f timed out after 10 seconds"; \
	  finished_files=$$(($$finished_files + 1)); \
	  echo "## Progress: $$finished_files/$$total_files compiled"; \
	done

compile-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD asn1/); do \
		echo "## Compiling $$f"; \
		timeout 5s mibdump \
			--mib-source=file://$$(pwd)/asn1 \
			--destination-directory=./pysnmp \
			$$f || echo "## Compiling $$f timed out after 10 seconds"; \
	done

compile-with-texts:  ## Compile With Texts all MIBs into .py files
	@total_files=$$(ls asn1 | wc -l); \
	finished_files=0; \
	for f in $$(ls asn1); do \
	  echo "## Compiling $$f with texts: mibdump --generate-mib-texts --mib-source=file://$$(pwd)/asn1 --destination-directory=./pysnmp $$f"; \
	  timeout 5s mibdump \
	    --generate-mib-texts \
	    --mib-source=file://$$(pwd)/asn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f || echo "## Compiling $$f with texts timed out after 10 seconds"; \
	  finished_files=$$(($$finished_files + 1)); \
	  echo "## Progress: $$finished_files/$$total_files compiled"; \
	done

compile-with-texts-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD asn1/); do \
	  echo "## Compiling $$f with texts"; \
	  timeout 5s mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/asn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f || echo "## Compiling $$f timed out after 10 seconds"; \
	done

compile-json:  ## Compile With Texts all MIBs into .py files
	@total_files=$$(ls asn1 | wc -l); \
	finished_files=0; \
	for f in $$(ls asn1); do \
	  echo "## Compiling $$f to json: mibdump --generate-mib-texts --no-python-compile --mib-source=file://$$(pwd)/asn1 --destination-format=json --destination-directory=./json $$f"; \
	  timeout 5s mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/asn1 \
	    --destination-format=json \
	    --destination-directory=./json \
	    $$f || echo "## Compiling $$f to json timed out after 10 seconds"; \
	  finished_files=$$(($$finished_files + 1)); \
	  echo "## Progress: $$finished_files/$$total_files compiled"; \
	done

compile-json-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD asn1/); do \
	  echo "## Compiling $$f to json"; \
	  timeout 5s mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/asn1 \
	    --destination-format=json \
	    --destination-directory=./json \
	    $$f || echo "## Compiling $$f timed out after 10 seconds"; \
	done

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

changed: compile-changed compile-with-texts-changed compile-json-changed  ## Call all "-changed" tasks

all: compile compile-with-texts compile-json  ## Call all tasks
