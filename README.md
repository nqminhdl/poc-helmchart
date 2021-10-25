# Umbrella Helm Chart

## How to add new helm chart

Pull helm chart

```bash
# Add new helm repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

# Update helm repo to get latest chart version
helm repo update

# Pull latest helm chart
cd charts
helm pull ingress-nginx/ingress-nginx

# Pull specific helm chart version
cd charts
helm pull ingress-nginx/ingress-nginx --version 4.0.3

# Uncompress helm chart tgz
tar xvf ingress-nginx-4.0.6.tgz
```

Update `Chart.yaml` to add new dependency charts

```yaml
dependencies:
  - name: ingress-nginx
    version: "4.0.*"
    repository: "file://../charts/ingress-nginx" # This is to load local charts
    condition: ingressNginx.enabled
```

Update default values for new chart in `values.yaml`

```yaml
---
ingressNginx:
  enabled: false
  serviceMonitor:
    enabled: false
```

## How to upgrade chart version

Follow steps in [How to add new helm chart](#How-to-add-new-helm-chart)
