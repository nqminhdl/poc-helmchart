from constructs import Construct
from cdk8s import App, Chart

from imports import helmrelease
from imports import gitrepository
from imports import k8s
from handler import Yamldata


class BundleChart(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

    def manifests(self, config: str, chart_version: str, namespaces: list, components: list):
        gitrepository.GitRepository(
            self, "bundle-bundle-charts",
            metadata={
                "name": "bundle-bundle-charts",
                "namespace": "flux-system"
            },
            spec=gitrepository.GitRepositorySpec(
                interval="10m",
                url="ssh://git@github.com/minh-nguyenquang/poc-helmchart.git",
                ref=gitrepository.GitRepositorySpecRef(
                    tag="0.2.0"
                ),
                secret_ref=gitrepository.GitRepositorySpecSecretRef(
                    name="flux-system"
                )
            )
        )

        for namespace in namespaces:
            k8s.KubeNamespace(
                self, f"{namespace}",
                metadata={
                    "name": f"{namespace}"
                }
            )

        helmrelease.HelmRelease(
            self, "certificate",
            metadata={
                "name": "certificate"
            },
            spec=helmrelease.HelmReleaseSpec(
                interval="5m",
                chart=helmrelease.HelmReleaseSpecChart(
                    spec=helmrelease.HelmReleaseSpecChartSpec(
                        chart=".",
                        version=f"{chart_version}",
                        interval="5m",
                        source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                            kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                            name="bundle-infra-components",
                            namespace="flux-system"
                        )
                    )
                ),
                values_from=[
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="certificate_cert-manager-values"
                    )
                ]
            )
        )

        helmrelease.HelmRelease(
            self, "ingress",
            metadata={
                "name": "ingress"
            },
            spec=helmrelease.HelmReleaseSpec(
                interval="5m",
                chart=helmrelease.HelmReleaseSpecChart(
                    spec=helmrelease.HelmReleaseSpecChartSpec(
                        chart=".",
                        version=f"{chart_version}",
                        interval="5m",
                        source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                            kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                            name="bundle-infra-components",
                            namespace="flux-system"
                        )
                    )
                ),
                values_from=[
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="ingress_ingress-nginx-values"
                    )
                ]
            )
        )

        helmrelease.HelmRelease(
            self, "monitoring",
            metadata={
                "name": "monitoring"
            },
            spec=helmrelease.HelmReleaseSpec(
                interval="5m",
                chart=helmrelease.HelmReleaseSpecChart(
                    spec=helmrelease.HelmReleaseSpecChartSpec(
                        chart=".",
                        version=f"{chart_version}",
                        interval="5m",
                        source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                            kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                            name="bundle-infra-components",
                            namespace="flux-system"
                        )
                    )
                ),
                values_from=[
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="monitoring_kube-prometheus-stack-values"
                    ),
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="monitoring_loki-values"
                    ),
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="monitoring_prometheus-blackbox-exporter-values"
                    ),
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="monitoring_promtail-values"
                    ),
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="monitoring_tempo-values"
                    )
                ]
            )
        )

        helmrelease.HelmRelease(
            self, "scaling",
            metadata={
                "name": "scaling"
            },
            spec=helmrelease.HelmReleaseSpec(
                interval="5m",
                chart=helmrelease.HelmReleaseSpecChart(
                    spec=helmrelease.HelmReleaseSpecChartSpec(
                        chart=".",
                        version=f"{chart_version}",
                        interval="5m",
                        source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                            kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                            name="bundle-infra-components",
                            namespace="flux-system"
                        )
                    )
                ),
                values_from=[
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="scaling_aws-node-termination-handler-values"
                    ),
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="scaling_keda-values"
                    )
                ]
            )
        )

        helmrelease.HelmRelease(
            self, "secrets",
            metadata={
                "name": "secrets"
            },
            spec=helmrelease.HelmReleaseSpec(
                interval="5m",
                chart=helmrelease.HelmReleaseSpecChart(
                    spec=helmrelease.HelmReleaseSpecChartSpec(
                        chart=".",
                        version=f"{chart_version}",
                        interval="5m",
                        source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                            kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                            name="bundle-infra-components",
                            namespace="flux-system"
                        )
                    )
                ),
                values_from=[
                    helmrelease.HelmReleaseSpecValuesFrom(
                        kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                        name="secrets_sealed-secrets-values"
                    )
                ]
            )
        )

        if "mesh" in components:
            helmrelease.HelmRelease(
                self, "mesh",
                metadata={
                    "name": "mesh"
                },
                spec=helmrelease.HelmReleaseSpec(
                    interval="5m",
                    chart=helmrelease.HelmReleaseSpecChart(
                        spec=helmrelease.HelmReleaseSpecChartSpec(
                            chart=".",
                            version=f"{chart_version}",
                            interval="5m",
                            source_ref=helmrelease.HelmReleaseSpecChartSpecSourceRef(
                                kind=helmrelease.HelmReleaseSpecChartSpecSourceRefKind.HELM_REPOSITORY,
                                name="bundle-infra-components",
                                namespace="flux-system"
                            )
                        )
                    ),
                    values_from=[
                        helmrelease.HelmReleaseSpecValuesFrom(
                            kind=helmrelease.HelmReleaseSpecValuesFromKind.CONFIG_MAP,
                            name="mesh_linkerd2-values"
                        ),
                        helmrelease.HelmReleaseSpecValuesFrom(
                            kind=helmrelease.HelmReleaseSpecValuesFromKind.SECRET,
                            name="linkerd-certs",
                            target_path="identityTrustAnchorsPEM",
                            values_key="ca.crt"
                        ),
                        helmrelease.HelmReleaseSpecValuesFrom(
                            kind=helmrelease.HelmReleaseSpecValuesFromKind.SECRET,
                            name="linkerd-certs",
                            target_path="identity.issuer.tls.crtPEM",
                            values_key="issuer.crt"
                        ),
                        helmrelease.HelmReleaseSpecValuesFrom(
                            kind=helmrelease.HelmReleaseSpecValuesFromKind.SECRET,
                            name="linkerd-certs",
                            target_path="identity.issuer.tls.keyPEM",
                            values_key="issuer.key"
                        )
                    ]
                )
            )
