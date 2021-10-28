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

tls:
	@-openssl req -x509 -nodes -newkey rsa:4096 -keyout "sealed-secrets.key" -out "sealed-secrets.crt" -subj "/CN=sealed-secret/O=sealed-secret"
	@-kubectl create secret tls sealed-secrets-tls --cert=sealed-secrets.crt --key=sealed-secrets.key --dry-run=client -o yaml
	@-mv sealed-secrets.crt encrypt.pub
	@-rm sealed-secrets.key
