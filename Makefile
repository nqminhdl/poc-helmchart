clean:
	@-rm -rf test/*
	@test -f encrypt.pub && rm encrypt.pub
	@test -f linkerd-certs.yaml && rm linkerd-certs.yaml
	@test -f sealed-secrets-tls.yaml && rm sealed-secrets-tls.yaml

build:
	@if [[ ${spec} == minimal ]]; then \
		cat values/aws/${spec}/* > values-${spec}.yaml; \
		helm template test . -f values-${spec}.yaml --output-dir test; \
	elif [[ ${spec} == production ]]; then \
		cat values/aws/${spec}/* > values-${spec}.yaml; \
		helm template test . -f values-${spec}.yaml --output-dir test; \
	else \
		echo "Bundle chart only supports minimal and production specs"; \
	fi

	@-echo '------------------List of charts------------------'
	@-ls test/*/* | awk '{print $0}'
	@-echo ''

tls-sealed-secrets:
	@-openssl req -x509 -nodes -newkey rsa:4096 \
			-keyout "sealed-secrets.key" \
			-out "sealed-secrets.crt" \
			-subj "/CN=sealed-secret/O=sealed-secret"
	@-kubectl create secret tls sealed-secrets-tls \
			--namespace=flux-system \
			--cert=sealed-secrets.crt \
			--key=sealed-secrets.key \
			--dry-run=client \
			-o yaml > sealed-secrets-tls.yaml
	@-mv sealed-secrets.crt encrypt.pub
	@-rm sealed-secrets.key

tls-linkerd2:
	@-step certificate create root.linkerd.cluster.local ca.crt ca.key \
			--profile root-ca --no-password --insecure
	@-step certificate create identity.linkerd.cluster.local issuer.crt issuer.key \
			--profile intermediate-ca --not-after 8760h --no-password --insecure \
			--ca ca.crt --ca-key ca.key
	@-kubectl create secret generic linkerd-certs \
			--namespace=k8s-component-linkerd \
			--from-file=ca.key=ca.key \
			--from-file=ca.crt=ca.crt \
			--from-file=issuer.crt=issuer.crt \
			--from-file=issuer.key=issuer.key \
			--dry-run=client \
			-o yaml > linkerd-certs-base64.yaml
	@-cat linkerd-certs-base64.yaml | kubeseal --cert encrypt.pub --format yaml > linkerd-certs.yaml
	@-echo 'Clean up generate certs and raw base64 secret'
	@-ls | grep -E 'key|crt|base64' | awk '{print $0}'
	@-rm ca.crt ca.key issuer.crt issuer.key linkerd-certs-base64.yaml
