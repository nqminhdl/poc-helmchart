clean:
	@-rm -rf test/*

build:
	@if [[ ${spec} == minimal ]]; then \
		helm template test . -f values-${spec}.yaml --output-dir test; \
	elif [[ ${spec} == production ]]; then \
		helm template test . -f values-${spec}.yaml --output-dir test \
	else \
		echo "Bundle chart only supports minimal and production specs"; \
	fi

	@-echo '------------------List of charts------------------'
	@-ls test/*/* | awk '{print $0}'
	@-echo ''
