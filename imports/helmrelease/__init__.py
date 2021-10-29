import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


class HelmRelease(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iofluxcdtoolkithelm.HelmRelease",
):
    '''HelmRelease is the Schema for the helmreleases API.

    :schema: HelmRelease
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["HelmReleaseSpec"] = None,
    ) -> None:
        '''Defines a "HelmRelease" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: HelmReleaseSpec defines the desired state of a Helm release.
        '''
        props = HelmReleaseProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["HelmReleaseSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "HelmRelease".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: HelmReleaseSpec defines the desired state of a Helm release.
        '''
        props = HelmReleaseProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "HelmRelease".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class HelmReleaseProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["HelmReleaseSpec"] = None,
    ) -> None:
        '''HelmRelease is the Schema for the helmreleases API.

        :param metadata: 
        :param spec: HelmReleaseSpec defines the desired state of a Helm release.

        :schema: HelmRelease
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = HelmReleaseSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: HelmRelease#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["HelmReleaseSpec"]:
        '''HelmReleaseSpec defines the desired state of a Helm release.

        :schema: HelmRelease#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["HelmReleaseSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpec",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "interval": "interval",
        "depends_on": "dependsOn",
        "install": "install",
        "kube_config": "kubeConfig",
        "max_history": "maxHistory",
        "post_renderers": "postRenderers",
        "release_name": "releaseName",
        "rollback": "rollback",
        "service_account_name": "serviceAccountName",
        "storage_namespace": "storageNamespace",
        "suspend": "suspend",
        "target_namespace": "targetNamespace",
        "test": "test",
        "timeout": "timeout",
        "uninstall": "uninstall",
        "upgrade": "upgrade",
        "values": "values",
        "values_from": "valuesFrom",
    },
)
class HelmReleaseSpec:
    def __init__(
        self,
        *,
        chart: "HelmReleaseSpecChart",
        interval: builtins.str,
        depends_on: typing.Optional[typing.Sequence["HelmReleaseSpecDependsOn"]] = None,
        install: typing.Optional["HelmReleaseSpecInstall"] = None,
        kube_config: typing.Optional["HelmReleaseSpecKubeConfig"] = None,
        max_history: typing.Optional[jsii.Number] = None,
        post_renderers: typing.Optional[typing.Sequence["HelmReleaseSpecPostRenderers"]] = None,
        release_name: typing.Optional[builtins.str] = None,
        rollback: typing.Optional["HelmReleaseSpecRollback"] = None,
        service_account_name: typing.Optional[builtins.str] = None,
        storage_namespace: typing.Optional[builtins.str] = None,
        suspend: typing.Optional[builtins.bool] = None,
        target_namespace: typing.Optional[builtins.str] = None,
        test: typing.Optional["HelmReleaseSpecTest"] = None,
        timeout: typing.Optional[builtins.str] = None,
        uninstall: typing.Optional["HelmReleaseSpecUninstall"] = None,
        upgrade: typing.Optional["HelmReleaseSpecUpgrade"] = None,
        values: typing.Any = None,
        values_from: typing.Optional[typing.Sequence["HelmReleaseSpecValuesFrom"]] = None,
    ) -> None:
        '''HelmReleaseSpec defines the desired state of a Helm release.

        :param chart: Chart defines the template of the v1beta1.HelmChart that should be created for this HelmRelease.
        :param interval: Interval at which to reconcile the Helm release.
        :param depends_on: DependsOn may contain a dependency.CrossNamespaceDependencyReference slice with references to HelmRelease resources that must be ready before this HelmRelease can be reconciled.
        :param install: Install holds the configuration for Helm install actions for this HelmRelease.
        :param kube_config: KubeConfig for reconciling the HelmRelease on a remote cluster. When specified, KubeConfig takes precedence over ServiceAccountName.
        :param max_history: MaxHistory is the number of revisions saved by Helm for this HelmRelease. Use '0' for an unlimited number of revisions; defaults to '10'.
        :param post_renderers: PostRenderers holds an array of Helm PostRenderers, which will be applied in order of their definition.
        :param release_name: ReleaseName used for the Helm release. Defaults to a composition of '[TargetNamespace-]Name'. Default: a composition of '[TargetNamespace-]Name'.
        :param rollback: Rollback holds the configuration for Helm rollback actions for this HelmRelease.
        :param service_account_name: The name of the Kubernetes service account to impersonate when reconciling this HelmRelease.
        :param storage_namespace: StorageNamespace used for the Helm storage. Defaults to the namespace of the HelmRelease. Default: the namespace of the HelmRelease.
        :param suspend: Suspend tells the controller to suspend reconciliation for this HelmRelease, it does not apply to already started reconciliations. Defaults to false. Default: false.
        :param target_namespace: TargetNamespace to target when performing operations for the HelmRelease. Defaults to the namespace of the HelmRelease. Default: the namespace of the HelmRelease.
        :param test: Test holds the configuration for Helm test actions for this HelmRelease.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm action. Defaults to '5m0s'. Default: 5m0s'.
        :param uninstall: Uninstall holds the configuration for Helm uninstall actions for this HelmRelease.
        :param upgrade: Upgrade holds the configuration for Helm upgrade actions for this HelmRelease.
        :param values: Values holds the values for this Helm release.
        :param values_from: ValuesFrom holds references to resources containing Helm values for this HelmRelease, and information about how they should be merged.

        :schema: HelmReleaseSpec
        '''
        if isinstance(chart, dict):
            chart = HelmReleaseSpecChart(**chart)
        if isinstance(install, dict):
            install = HelmReleaseSpecInstall(**install)
        if isinstance(kube_config, dict):
            kube_config = HelmReleaseSpecKubeConfig(**kube_config)
        if isinstance(rollback, dict):
            rollback = HelmReleaseSpecRollback(**rollback)
        if isinstance(test, dict):
            test = HelmReleaseSpecTest(**test)
        if isinstance(uninstall, dict):
            uninstall = HelmReleaseSpecUninstall(**uninstall)
        if isinstance(upgrade, dict):
            upgrade = HelmReleaseSpecUpgrade(**upgrade)
        self._values: typing.Dict[str, typing.Any] = {
            "chart": chart,
            "interval": interval,
        }
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if install is not None:
            self._values["install"] = install
        if kube_config is not None:
            self._values["kube_config"] = kube_config
        if max_history is not None:
            self._values["max_history"] = max_history
        if post_renderers is not None:
            self._values["post_renderers"] = post_renderers
        if release_name is not None:
            self._values["release_name"] = release_name
        if rollback is not None:
            self._values["rollback"] = rollback
        if service_account_name is not None:
            self._values["service_account_name"] = service_account_name
        if storage_namespace is not None:
            self._values["storage_namespace"] = storage_namespace
        if suspend is not None:
            self._values["suspend"] = suspend
        if target_namespace is not None:
            self._values["target_namespace"] = target_namespace
        if test is not None:
            self._values["test"] = test
        if timeout is not None:
            self._values["timeout"] = timeout
        if uninstall is not None:
            self._values["uninstall"] = uninstall
        if upgrade is not None:
            self._values["upgrade"] = upgrade
        if values is not None:
            self._values["values"] = values
        if values_from is not None:
            self._values["values_from"] = values_from

    @builtins.property
    def chart(self) -> "HelmReleaseSpecChart":
        '''Chart defines the template of the v1beta1.HelmChart that should be created for this HelmRelease.

        :schema: HelmReleaseSpec#chart
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast("HelmReleaseSpecChart", result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Interval at which to reconcile the Helm release.

        :schema: HelmReleaseSpec#interval
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List["HelmReleaseSpecDependsOn"]]:
        '''DependsOn may contain a dependency.CrossNamespaceDependencyReference slice with references to HelmRelease resources that must be ready before this HelmRelease can be reconciled.

        :schema: HelmReleaseSpec#dependsOn
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List["HelmReleaseSpecDependsOn"]], result)

    @builtins.property
    def install(self) -> typing.Optional["HelmReleaseSpecInstall"]:
        '''Install holds the configuration for Helm install actions for this HelmRelease.

        :schema: HelmReleaseSpec#install
        '''
        result = self._values.get("install")
        return typing.cast(typing.Optional["HelmReleaseSpecInstall"], result)

    @builtins.property
    def kube_config(self) -> typing.Optional["HelmReleaseSpecKubeConfig"]:
        '''KubeConfig for reconciling the HelmRelease on a remote cluster.

        When specified, KubeConfig takes precedence over ServiceAccountName.

        :schema: HelmReleaseSpec#kubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional["HelmReleaseSpecKubeConfig"], result)

    @builtins.property
    def max_history(self) -> typing.Optional[jsii.Number]:
        '''MaxHistory is the number of revisions saved by Helm for this HelmRelease.

        Use '0' for an unlimited number of revisions; defaults to '10'.

        :schema: HelmReleaseSpec#maxHistory
        '''
        result = self._values.get("max_history")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def post_renderers(
        self,
    ) -> typing.Optional[typing.List["HelmReleaseSpecPostRenderers"]]:
        '''PostRenderers holds an array of Helm PostRenderers, which will be applied in order of their definition.

        :schema: HelmReleaseSpec#postRenderers
        '''
        result = self._values.get("post_renderers")
        return typing.cast(typing.Optional[typing.List["HelmReleaseSpecPostRenderers"]], result)

    @builtins.property
    def release_name(self) -> typing.Optional[builtins.str]:
        '''ReleaseName used for the Helm release.

        Defaults to a composition of '[TargetNamespace-]Name'.

        :default: a composition of '[TargetNamespace-]Name'.

        :schema: HelmReleaseSpec#releaseName
        '''
        result = self._values.get("release_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rollback(self) -> typing.Optional["HelmReleaseSpecRollback"]:
        '''Rollback holds the configuration for Helm rollback actions for this HelmRelease.

        :schema: HelmReleaseSpec#rollback
        '''
        result = self._values.get("rollback")
        return typing.cast(typing.Optional["HelmReleaseSpecRollback"], result)

    @builtins.property
    def service_account_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Kubernetes service account to impersonate when reconciling this HelmRelease.

        :schema: HelmReleaseSpec#serviceAccountName
        '''
        result = self._values.get("service_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_namespace(self) -> typing.Optional[builtins.str]:
        '''StorageNamespace used for the Helm storage.

        Defaults to the namespace of the HelmRelease.

        :default: the namespace of the HelmRelease.

        :schema: HelmReleaseSpec#storageNamespace
        '''
        result = self._values.get("storage_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspend(self) -> typing.Optional[builtins.bool]:
        '''Suspend tells the controller to suspend reconciliation for this HelmRelease, it does not apply to already started reconciliations.

        Defaults to false.

        :default: false.

        :schema: HelmReleaseSpec#suspend
        '''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def target_namespace(self) -> typing.Optional[builtins.str]:
        '''TargetNamespace to target when performing operations for the HelmRelease.

        Defaults to the namespace of the HelmRelease.

        :default: the namespace of the HelmRelease.

        :schema: HelmReleaseSpec#targetNamespace
        '''
        result = self._values.get("target_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test(self) -> typing.Optional["HelmReleaseSpecTest"]:
        '''Test holds the configuration for Helm test actions for this HelmRelease.

        :schema: HelmReleaseSpec#test
        '''
        result = self._values.get("test")
        return typing.cast(typing.Optional["HelmReleaseSpecTest"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm action.

        Defaults to '5m0s'.

        :default: 5m0s'.

        :schema: HelmReleaseSpec#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uninstall(self) -> typing.Optional["HelmReleaseSpecUninstall"]:
        '''Uninstall holds the configuration for Helm uninstall actions for this HelmRelease.

        :schema: HelmReleaseSpec#uninstall
        '''
        result = self._values.get("uninstall")
        return typing.cast(typing.Optional["HelmReleaseSpecUninstall"], result)

    @builtins.property
    def upgrade(self) -> typing.Optional["HelmReleaseSpecUpgrade"]:
        '''Upgrade holds the configuration for Helm upgrade actions for this HelmRelease.

        :schema: HelmReleaseSpec#upgrade
        '''
        result = self._values.get("upgrade")
        return typing.cast(typing.Optional["HelmReleaseSpecUpgrade"], result)

    @builtins.property
    def values(self) -> typing.Any:
        '''Values holds the values for this Helm release.

        :schema: HelmReleaseSpec#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Any, result)

    @builtins.property
    def values_from(self) -> typing.Optional[typing.List["HelmReleaseSpecValuesFrom"]]:
        '''ValuesFrom holds references to resources containing Helm values for this HelmRelease, and information about how they should be merged.

        :schema: HelmReleaseSpec#valuesFrom
        '''
        result = self._values.get("values_from")
        return typing.cast(typing.Optional[typing.List["HelmReleaseSpecValuesFrom"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecChart",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class HelmReleaseSpecChart:
    def __init__(self, *, spec: "HelmReleaseSpecChartSpec") -> None:
        '''Chart defines the template of the v1beta1.HelmChart that should be created for this HelmRelease.

        :param spec: Spec holds the template for the v1beta1.HelmChartSpec for this HelmRelease.

        :schema: HelmReleaseSpecChart
        '''
        if isinstance(spec, dict):
            spec = HelmReleaseSpecChartSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {
            "spec": spec,
        }

    @builtins.property
    def spec(self) -> "HelmReleaseSpecChartSpec":
        '''Spec holds the template for the v1beta1.HelmChartSpec for this HelmRelease.

        :schema: HelmReleaseSpecChart#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("HelmReleaseSpecChartSpec", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecChart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecChartSpec",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "source_ref": "sourceRef",
        "interval": "interval",
        "reconcile_strategy": "reconcileStrategy",
        "values_file": "valuesFile",
        "values_files": "valuesFiles",
        "version": "version",
    },
)
class HelmReleaseSpecChartSpec:
    def __init__(
        self,
        *,
        chart: builtins.str,
        source_ref: "HelmReleaseSpecChartSpecSourceRef",
        interval: typing.Optional[builtins.str] = None,
        reconcile_strategy: typing.Optional["HelmReleaseSpecChartSpecReconcileStrategy"] = None,
        values_file: typing.Optional[builtins.str] = None,
        values_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Spec holds the template for the v1beta1.HelmChartSpec for this HelmRelease.

        :param chart: The name or path the Helm chart is available at in the SourceRef.
        :param source_ref: The name and namespace of the v1beta1.Source the chart is available at.
        :param interval: Interval at which to check the v1beta1.Source for updates. Defaults to 'HelmReleaseSpec.Interval'. Default: HelmReleaseSpec.Interval'.
        :param reconcile_strategy: Determines what enables the creation of a new artifact. Valid values are ('ChartVersion', 'Revision'). See the documentation of the values for an explanation on their behavior. Defaults to ChartVersion when omitted. Default: ChartVersion when omitted.
        :param values_file: Alternative values file to use as the default chart values, expected to be a relative path in the SourceRef. Deprecated in favor of ValuesFiles, for backwards compatibility the file defined here is merged before the ValuesFiles items. Ignored when omitted.
        :param values_files: Alternative list of values files to use as the chart values (values.yaml is not included by default), expected to be a relative path in the SourceRef. Values files are merged in the order of this list with the last file overriding the first. Ignored when omitted.
        :param version: Version semver expression, ignored for charts from v1beta1.GitRepository and v1beta1.Bucket sources. Defaults to latest when omitted. Default: latest when omitted.

        :schema: HelmReleaseSpecChartSpec
        '''
        if isinstance(source_ref, dict):
            source_ref = HelmReleaseSpecChartSpecSourceRef(**source_ref)
        self._values: typing.Dict[str, typing.Any] = {
            "chart": chart,
            "source_ref": source_ref,
        }
        if interval is not None:
            self._values["interval"] = interval
        if reconcile_strategy is not None:
            self._values["reconcile_strategy"] = reconcile_strategy
        if values_file is not None:
            self._values["values_file"] = values_file
        if values_files is not None:
            self._values["values_files"] = values_files
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def chart(self) -> builtins.str:
        '''The name or path the Helm chart is available at in the SourceRef.

        :schema: HelmReleaseSpecChartSpec#chart
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_ref(self) -> "HelmReleaseSpecChartSpecSourceRef":
        '''The name and namespace of the v1beta1.Source the chart is available at.

        :schema: HelmReleaseSpecChartSpec#sourceRef
        '''
        result = self._values.get("source_ref")
        assert result is not None, "Required property 'source_ref' is missing"
        return typing.cast("HelmReleaseSpecChartSpecSourceRef", result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Interval at which to check the v1beta1.Source for updates. Defaults to 'HelmReleaseSpec.Interval'.

        :default: HelmReleaseSpec.Interval'.

        :schema: HelmReleaseSpecChartSpec#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reconcile_strategy(
        self,
    ) -> typing.Optional["HelmReleaseSpecChartSpecReconcileStrategy"]:
        '''Determines what enables the creation of a new artifact.

        Valid values are ('ChartVersion', 'Revision'). See the documentation of the values for an explanation on their behavior. Defaults to ChartVersion when omitted.

        :default: ChartVersion when omitted.

        :schema: HelmReleaseSpecChartSpec#reconcileStrategy
        '''
        result = self._values.get("reconcile_strategy")
        return typing.cast(typing.Optional["HelmReleaseSpecChartSpecReconcileStrategy"], result)

    @builtins.property
    def values_file(self) -> typing.Optional[builtins.str]:
        '''Alternative values file to use as the default chart values, expected to be a relative path in the SourceRef.

        Deprecated in favor of ValuesFiles, for backwards compatibility the file defined here is merged before the ValuesFiles items. Ignored when omitted.

        :schema: HelmReleaseSpecChartSpec#valuesFile
        '''
        result = self._values.get("values_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative list of values files to use as the chart values (values.yaml is not included by default), expected to be a relative path in the SourceRef. Values files are merged in the order of this list with the last file overriding the first. Ignored when omitted.

        :schema: HelmReleaseSpecChartSpec#valuesFiles
        '''
        result = self._values.get("values_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version semver expression, ignored for charts from v1beta1.GitRepository and v1beta1.Bucket sources. Defaults to latest when omitted.

        :default: latest when omitted.

        :schema: HelmReleaseSpecChartSpec#version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecChartSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecChartSpecReconcileStrategy")
class HelmReleaseSpecChartSpecReconcileStrategy(enum.Enum):
    '''Determines what enables the creation of a new artifact.

    Valid values are ('ChartVersion', 'Revision'). See the documentation of the values for an explanation on their behavior. Defaults to ChartVersion when omitted.

    :default: ChartVersion when omitted.

    :schema: HelmReleaseSpecChartSpecReconcileStrategy
    '''

    CHART_VERSION = "CHART_VERSION"
    '''ChartVersion.'''
    REVISION = "REVISION"
    '''Revision.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecChartSpecSourceRef",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "api_version": "apiVersion",
        "kind": "kind",
        "namespace": "namespace",
    },
)
class HelmReleaseSpecChartSpecSourceRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        kind: typing.Optional["HelmReleaseSpecChartSpecSourceRefKind"] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The name and namespace of the v1beta1.Source the chart is available at.

        :param name: Name of the referent.
        :param api_version: APIVersion of the referent.
        :param kind: Kind of the referent.
        :param namespace: Namespace of the referent.

        :schema: HelmReleaseSpecChartSpecSourceRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if kind is not None:
            self._values["kind"] = kind
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: HelmReleaseSpecChartSpecSourceRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''APIVersion of the referent.

        :schema: HelmReleaseSpecChartSpecSourceRef#apiVersion
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional["HelmReleaseSpecChartSpecSourceRefKind"]:
        '''Kind of the referent.

        :schema: HelmReleaseSpecChartSpecSourceRef#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional["HelmReleaseSpecChartSpecSourceRefKind"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the referent.

        :schema: HelmReleaseSpecChartSpecSourceRef#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecChartSpecSourceRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecChartSpecSourceRefKind")
class HelmReleaseSpecChartSpecSourceRefKind(enum.Enum):
    '''Kind of the referent.

    :schema: HelmReleaseSpecChartSpecSourceRefKind
    '''

    HELM_REPOSITORY = "HELM_REPOSITORY"
    '''HelmRepository.'''
    GIT_REPOSITORY = "GIT_REPOSITORY"
    '''GitRepository.'''
    BUCKET = "BUCKET"
    '''Bucket.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecDependsOn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class HelmReleaseSpecDependsOn:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CrossNamespaceDependencyReference holds the reference to a dependency.

        :param name: Name holds the name reference of a dependency.
        :param namespace: Namespace holds the namespace reference of a dependency.

        :schema: HelmReleaseSpecDependsOn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name holds the name reference of a dependency.

        :schema: HelmReleaseSpecDependsOn#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace holds the namespace reference of a dependency.

        :schema: HelmReleaseSpecDependsOn#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecDependsOn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecInstall",
    jsii_struct_bases=[],
    name_mapping={
        "crds": "crds",
        "create_namespace": "createNamespace",
        "disable_hooks": "disableHooks",
        "disable_open_api_validation": "disableOpenApiValidation",
        "disable_wait": "disableWait",
        "disable_wait_for_jobs": "disableWaitForJobs",
        "remediation": "remediation",
        "replace": "replace",
        "skip_cr_ds": "skipCrDs",
        "timeout": "timeout",
    },
)
class HelmReleaseSpecInstall:
    def __init__(
        self,
        *,
        crds: typing.Optional["HelmReleaseSpecInstallCrds"] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        disable_hooks: typing.Optional[builtins.bool] = None,
        disable_open_api_validation: typing.Optional[builtins.bool] = None,
        disable_wait: typing.Optional[builtins.bool] = None,
        disable_wait_for_jobs: typing.Optional[builtins.bool] = None,
        remediation: typing.Optional["HelmReleaseSpecInstallRemediation"] = None,
        replace: typing.Optional[builtins.bool] = None,
        skip_cr_ds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Install holds the configuration for Helm install actions for this HelmRelease.

        :param crds: CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here. Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Create`` and if omitted CRDs are installed but not updated. Skip: do neither install nor replace (update) any CRDs. Create: new CRDs are created, existing CRDs are neither updated nor deleted. CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted. By default, CRDs are applied (installed) during Helm install action. With this option users can opt-in to CRD replace existing CRDs on Helm install actions, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions. Default: Create` and if omitted CRDs are installed but not updated.
        :param create_namespace: CreateNamespace tells the Helm install action to create the HelmReleaseSpec.TargetNamespace if it does not exist yet. On uninstall, the namespace will not be garbage collected.
        :param disable_hooks: DisableHooks prevents hooks from running during the Helm install action.
        :param disable_open_api_validation: DisableOpenAPIValidation prevents the Helm install action from validating rendered templates against the Kubernetes OpenAPI Schema.
        :param disable_wait: DisableWait disables the waiting for resources to be ready after a Helm install has been performed.
        :param disable_wait_for_jobs: DisableWaitForJobs disables waiting for jobs to complete after a Helm install has been performed.
        :param remediation: Remediation holds the remediation configuration for when the Helm install action for the HelmRelease fails. The default is to not perform any action.
        :param replace: Replace tells the Helm install action to re-use the 'ReleaseName', but only if that name is a deleted release which remains in the history.
        :param skip_cr_ds: SkipCRDs tells the Helm install action to not install any CRDs. By default, CRDs are installed if not already present. Deprecated use CRD policy (``crds``) attribute with value ``Skip`` instead.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm install action. Defaults to 'HelmReleaseSpec.Timeout'. Default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecInstall
        '''
        if isinstance(remediation, dict):
            remediation = HelmReleaseSpecInstallRemediation(**remediation)
        self._values: typing.Dict[str, typing.Any] = {}
        if crds is not None:
            self._values["crds"] = crds
        if create_namespace is not None:
            self._values["create_namespace"] = create_namespace
        if disable_hooks is not None:
            self._values["disable_hooks"] = disable_hooks
        if disable_open_api_validation is not None:
            self._values["disable_open_api_validation"] = disable_open_api_validation
        if disable_wait is not None:
            self._values["disable_wait"] = disable_wait
        if disable_wait_for_jobs is not None:
            self._values["disable_wait_for_jobs"] = disable_wait_for_jobs
        if remediation is not None:
            self._values["remediation"] = remediation
        if replace is not None:
            self._values["replace"] = replace
        if skip_cr_ds is not None:
            self._values["skip_cr_ds"] = skip_cr_ds
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def crds(self) -> typing.Optional["HelmReleaseSpecInstallCrds"]:
        '''CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here.

        Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Create`` and if omitted CRDs are installed but not updated.
        Skip: do neither install nor replace (update) any CRDs.
        Create: new CRDs are created, existing CRDs are neither updated nor deleted.
        CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted.
        By default, CRDs are applied (installed) during Helm install action. With this option users can opt-in to CRD replace existing CRDs on Helm install actions, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions.

        :default: Create` and if omitted CRDs are installed but not updated.

        :schema: HelmReleaseSpecInstall#crds
        '''
        result = self._values.get("crds")
        return typing.cast(typing.Optional["HelmReleaseSpecInstallCrds"], result)

    @builtins.property
    def create_namespace(self) -> typing.Optional[builtins.bool]:
        '''CreateNamespace tells the Helm install action to create the HelmReleaseSpec.TargetNamespace if it does not exist yet. On uninstall, the namespace will not be garbage collected.

        :schema: HelmReleaseSpecInstall#createNamespace
        '''
        result = self._values.get("create_namespace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_hooks(self) -> typing.Optional[builtins.bool]:
        '''DisableHooks prevents hooks from running during the Helm install action.

        :schema: HelmReleaseSpecInstall#disableHooks
        '''
        result = self._values.get("disable_hooks")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_open_api_validation(self) -> typing.Optional[builtins.bool]:
        '''DisableOpenAPIValidation prevents the Helm install action from validating rendered templates against the Kubernetes OpenAPI Schema.

        :schema: HelmReleaseSpecInstall#disableOpenAPIValidation
        '''
        result = self._values.get("disable_open_api_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait(self) -> typing.Optional[builtins.bool]:
        '''DisableWait disables the waiting for resources to be ready after a Helm install has been performed.

        :schema: HelmReleaseSpecInstall#disableWait
        '''
        result = self._values.get("disable_wait")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait_for_jobs(self) -> typing.Optional[builtins.bool]:
        '''DisableWaitForJobs disables waiting for jobs to complete after a Helm install has been performed.

        :schema: HelmReleaseSpecInstall#disableWaitForJobs
        '''
        result = self._values.get("disable_wait_for_jobs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remediation(self) -> typing.Optional["HelmReleaseSpecInstallRemediation"]:
        '''Remediation holds the remediation configuration for when the Helm install action for the HelmRelease fails.

        The default is to not perform any action.

        :schema: HelmReleaseSpecInstall#remediation
        '''
        result = self._values.get("remediation")
        return typing.cast(typing.Optional["HelmReleaseSpecInstallRemediation"], result)

    @builtins.property
    def replace(self) -> typing.Optional[builtins.bool]:
        '''Replace tells the Helm install action to re-use the 'ReleaseName', but only if that name is a deleted release which remains in the history.

        :schema: HelmReleaseSpecInstall#replace
        '''
        result = self._values.get("replace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def skip_cr_ds(self) -> typing.Optional[builtins.bool]:
        '''SkipCRDs tells the Helm install action to not install any CRDs.

        By default, CRDs are installed if not already present.
        Deprecated use CRD policy (``crds``) attribute with value ``Skip`` instead.

        :schema: HelmReleaseSpecInstall#skipCRDs
        '''
        result = self._values.get("skip_cr_ds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm install action.

        Defaults to 'HelmReleaseSpec.Timeout'.

        :default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecInstall#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecInstall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecInstallCrds")
class HelmReleaseSpecInstallCrds(enum.Enum):
    '''CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here.

    Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Create`` and if omitted CRDs are installed but not updated.
    Skip: do neither install nor replace (update) any CRDs.
    Create: new CRDs are created, existing CRDs are neither updated nor deleted.
    CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted.
    By default, CRDs are applied (installed) during Helm install action. With this option users can opt-in to CRD replace existing CRDs on Helm install actions, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions.

    :default: Create` and if omitted CRDs are installed but not updated.

    :schema: HelmReleaseSpecInstallCrds
    '''

    SKIP = "SKIP"
    '''Skip.'''
    CREATE = "CREATE"
    '''Create.'''
    CREATE_REPLACE = "CREATE_REPLACE"
    '''CreateReplace.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecInstallRemediation",
    jsii_struct_bases=[],
    name_mapping={
        "ignore_test_failures": "ignoreTestFailures",
        "remediate_last_failure": "remediateLastFailure",
        "retries": "retries",
    },
)
class HelmReleaseSpecInstallRemediation:
    def __init__(
        self,
        *,
        ignore_test_failures: typing.Optional[builtins.bool] = None,
        remediate_last_failure: typing.Optional[builtins.bool] = None,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Remediation holds the remediation configuration for when the Helm install action for the HelmRelease fails.

        The default is to not perform any action.

        :param ignore_test_failures: IgnoreTestFailures tells the controller to skip remediation when the Helm tests are run after an install action but fail. Defaults to 'Test.IgnoreFailures'. Default: Test.IgnoreFailures'.
        :param remediate_last_failure: RemediateLastFailure tells the controller to remediate the last failure, when no retries remain. Defaults to 'false'. Default: false'.
        :param retries: Retries is the number of retries that should be attempted on failures before bailing. Remediation, using an uninstall, is performed between each attempt. Defaults to '0', a negative integer equals to unlimited retries. Default: 0', a negative integer equals to unlimited retries.

        :schema: HelmReleaseSpecInstallRemediation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore_test_failures is not None:
            self._values["ignore_test_failures"] = ignore_test_failures
        if remediate_last_failure is not None:
            self._values["remediate_last_failure"] = remediate_last_failure
        if retries is not None:
            self._values["retries"] = retries

    @builtins.property
    def ignore_test_failures(self) -> typing.Optional[builtins.bool]:
        '''IgnoreTestFailures tells the controller to skip remediation when the Helm tests are run after an install action but fail.

        Defaults to 'Test.IgnoreFailures'.

        :default: Test.IgnoreFailures'.

        :schema: HelmReleaseSpecInstallRemediation#ignoreTestFailures
        '''
        result = self._values.get("ignore_test_failures")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remediate_last_failure(self) -> typing.Optional[builtins.bool]:
        '''RemediateLastFailure tells the controller to remediate the last failure, when no retries remain.

        Defaults to 'false'.

        :default: false'.

        :schema: HelmReleaseSpecInstallRemediation#remediateLastFailure
        '''
        result = self._values.get("remediate_last_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Retries is the number of retries that should be attempted on failures before bailing.

        Remediation, using an uninstall, is performed between each attempt. Defaults to '0', a negative integer equals to unlimited retries.

        :default: 0', a negative integer equals to unlimited retries.

        :schema: HelmReleaseSpecInstallRemediation#retries
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecInstallRemediation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecKubeConfig",
    jsii_struct_bases=[],
    name_mapping={"secret_ref": "secretRef"},
)
class HelmReleaseSpecKubeConfig:
    def __init__(
        self,
        *,
        secret_ref: typing.Optional["HelmReleaseSpecKubeConfigSecretRef"] = None,
    ) -> None:
        '''KubeConfig for reconciling the HelmRelease on a remote cluster.

        When specified, KubeConfig takes precedence over ServiceAccountName.

        :param secret_ref: SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value. It must be in the same namespace as the HelmRelease. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the HelmRelease.

        :schema: HelmReleaseSpecKubeConfig
        '''
        if isinstance(secret_ref, dict):
            secret_ref = HelmReleaseSpecKubeConfigSecretRef(**secret_ref)
        self._values: typing.Dict[str, typing.Any] = {}
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def secret_ref(self) -> typing.Optional["HelmReleaseSpecKubeConfigSecretRef"]:
        '''SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value.

        It must be in the same namespace as the HelmRelease. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the HelmRelease.

        :schema: HelmReleaseSpecKubeConfig#secretRef
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["HelmReleaseSpecKubeConfigSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecKubeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecKubeConfigSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class HelmReleaseSpecKubeConfigSecretRef:
    def __init__(self, *, name: builtins.str) -> None:
        '''SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value.

        It must be in the same namespace as the HelmRelease. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the HelmRelease.

        :param name: Name of the referent.

        :schema: HelmReleaseSpecKubeConfigSecretRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: HelmReleaseSpecKubeConfigSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecKubeConfigSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderers",
    jsii_struct_bases=[],
    name_mapping={"kustomize": "kustomize"},
)
class HelmReleaseSpecPostRenderers:
    def __init__(
        self,
        *,
        kustomize: typing.Optional["HelmReleaseSpecPostRenderersKustomize"] = None,
    ) -> None:
        '''PostRenderer contains a Helm PostRenderer specification.

        :param kustomize: Kustomization to apply as PostRenderer.

        :schema: HelmReleaseSpecPostRenderers
        '''
        if isinstance(kustomize, dict):
            kustomize = HelmReleaseSpecPostRenderersKustomize(**kustomize)
        self._values: typing.Dict[str, typing.Any] = {}
        if kustomize is not None:
            self._values["kustomize"] = kustomize

    @builtins.property
    def kustomize(self) -> typing.Optional["HelmReleaseSpecPostRenderersKustomize"]:
        '''Kustomization to apply as PostRenderer.

        :schema: HelmReleaseSpecPostRenderers#kustomize
        '''
        result = self._values.get("kustomize")
        return typing.cast(typing.Optional["HelmReleaseSpecPostRenderersKustomize"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomize",
    jsii_struct_bases=[],
    name_mapping={
        "images": "images",
        "patches_json6902": "patchesJson6902",
        "patches_strategic_merge": "patchesStrategicMerge",
    },
)
class HelmReleaseSpecPostRenderersKustomize:
    def __init__(
        self,
        *,
        images: typing.Optional[typing.Sequence["HelmReleaseSpecPostRenderersKustomizeImages"]] = None,
        patches_json6902: typing.Optional[typing.Sequence["HelmReleaseSpecPostRenderersKustomizePatchesJson6902"]] = None,
        patches_strategic_merge: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Kustomization to apply as PostRenderer.

        :param images: Images is a list of (image name, new name, new tag or digest) for changing image names, tags or digests. This can also be achieved with a patch, but this operator is simpler to specify.
        :param patches_json6902: JSON 6902 patches, defined as inline YAML objects.
        :param patches_strategic_merge: Strategic merge patches, defined as inline YAML objects.

        :schema: HelmReleaseSpecPostRenderersKustomize
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if images is not None:
            self._values["images"] = images
        if patches_json6902 is not None:
            self._values["patches_json6902"] = patches_json6902
        if patches_strategic_merge is not None:
            self._values["patches_strategic_merge"] = patches_strategic_merge

    @builtins.property
    def images(
        self,
    ) -> typing.Optional[typing.List["HelmReleaseSpecPostRenderersKustomizeImages"]]:
        '''Images is a list of (image name, new name, new tag or digest) for changing image names, tags or digests.

        This can also be achieved with a patch, but this operator is simpler to specify.

        :schema: HelmReleaseSpecPostRenderersKustomize#images
        '''
        result = self._values.get("images")
        return typing.cast(typing.Optional[typing.List["HelmReleaseSpecPostRenderersKustomizeImages"]], result)

    @builtins.property
    def patches_json6902(
        self,
    ) -> typing.Optional[typing.List["HelmReleaseSpecPostRenderersKustomizePatchesJson6902"]]:
        '''JSON 6902 patches, defined as inline YAML objects.

        :schema: HelmReleaseSpecPostRenderersKustomize#patchesJson6902
        '''
        result = self._values.get("patches_json6902")
        return typing.cast(typing.Optional[typing.List["HelmReleaseSpecPostRenderersKustomizePatchesJson6902"]], result)

    @builtins.property
    def patches_strategic_merge(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Strategic merge patches, defined as inline YAML objects.

        :schema: HelmReleaseSpecPostRenderersKustomize#patchesStrategicMerge
        '''
        result = self._values.get("patches_strategic_merge")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderersKustomize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomizeImages",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "digest": "digest",
        "new_name": "newName",
        "new_tag": "newTag",
    },
)
class HelmReleaseSpecPostRenderersKustomizeImages:
    def __init__(
        self,
        *,
        name: builtins.str,
        digest: typing.Optional[builtins.str] = None,
        new_name: typing.Optional[builtins.str] = None,
        new_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Image contains an image name, a new name, a new tag or digest, which will replace the original name and tag.

        :param name: Name is a tag-less image name.
        :param digest: Digest is the value used to replace the original image tag. If digest is present NewTag value is ignored.
        :param new_name: NewName is the value used to replace the original name.
        :param new_tag: NewTag is the value used to replace the original tag.

        :schema: HelmReleaseSpecPostRenderersKustomizeImages
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if digest is not None:
            self._values["digest"] = digest
        if new_name is not None:
            self._values["new_name"] = new_name
        if new_tag is not None:
            self._values["new_tag"] = new_tag

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is a tag-less image name.

        :schema: HelmReleaseSpecPostRenderersKustomizeImages#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def digest(self) -> typing.Optional[builtins.str]:
        '''Digest is the value used to replace the original image tag.

        If digest is present NewTag value is ignored.

        :schema: HelmReleaseSpecPostRenderersKustomizeImages#digest
        '''
        result = self._values.get("digest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_name(self) -> typing.Optional[builtins.str]:
        '''NewName is the value used to replace the original name.

        :schema: HelmReleaseSpecPostRenderersKustomizeImages#newName
        '''
        result = self._values.get("new_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_tag(self) -> typing.Optional[builtins.str]:
        '''NewTag is the value used to replace the original tag.

        :schema: HelmReleaseSpecPostRenderersKustomizeImages#newTag
        '''
        result = self._values.get("new_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderersKustomizeImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomizePatchesJson6902",
    jsii_struct_bases=[],
    name_mapping={"patch": "patch", "target": "target"},
)
class HelmReleaseSpecPostRenderersKustomizePatchesJson6902:
    def __init__(
        self,
        *,
        patch: typing.Sequence["HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch"],
        target: "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target",
    ) -> None:
        '''JSON6902Patch contains a JSON6902 patch and the target the patch should be applied to.

        :param patch: Patch contains the JSON6902 patch document with an array of operation objects.
        :param target: Target points to the resources that the patch document should be applied to.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902
        '''
        if isinstance(target, dict):
            target = HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target(**target)
        self._values: typing.Dict[str, typing.Any] = {
            "patch": patch,
            "target": target,
        }

    @builtins.property
    def patch(
        self,
    ) -> typing.List["HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch"]:
        '''Patch contains the JSON6902 patch document with an array of operation objects.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902#patch
        '''
        result = self._values.get("patch")
        assert result is not None, "Required property 'patch' is missing"
        return typing.cast(typing.List["HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch"], result)

    @builtins.property
    def target(self) -> "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target":
        '''Target points to the resources that the patch document should be applied to.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902#target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderersKustomizePatchesJson6902(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch",
    jsii_struct_bases=[],
    name_mapping={"op": "op", "path": "path", "from_": "from", "value": "value"},
)
class HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch:
    def __init__(
        self,
        *,
        op: "HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp",
        path: builtins.str,
        from_: typing.Optional[builtins.str] = None,
        value: typing.Any = None,
    ) -> None:
        '''JSON6902 is a JSON6902 operation object.

        https://tools.ietf.org/html/rfc6902#section-4

        :param op: 
        :param path: 
        :param from_: 
        :param value: 

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "op": op,
            "path": path,
        }
        if from_ is not None:
            self._values["from_"] = from_
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def op(self) -> "HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp":
        '''
        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch#op
        '''
        result = self._values.get("op")
        assert result is not None, "Required property 'op' is missing"
        return typing.cast("HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp", result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch#path
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''
        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Any:
        '''
        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp"
)
class HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp(enum.Enum):
    '''
    :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp
    '''

    TEST = "TEST"
    '''test.'''
    REMOVE = "REMOVE"
    '''remove.'''
    ADD = "ADD"
    '''add.'''
    REPLACE = "REPLACE"
    '''replace.'''
    MOVE = "MOVE"
    '''move.'''
    COPY = "COPY"
    '''copy.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target",
    jsii_struct_bases=[],
    name_mapping={
        "annotation_selector": "annotationSelector",
        "group": "group",
        "kind": "kind",
        "label_selector": "labelSelector",
        "name": "name",
        "namespace": "namespace",
        "version": "version",
    },
)
class HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target:
    def __init__(
        self,
        *,
        annotation_selector: typing.Optional[builtins.str] = None,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        label_selector: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Target points to the resources that the patch document should be applied to.

        :param annotation_selector: AnnotationSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource annotations.
        :param group: Group is the API group to select resources from. Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md
        :param kind: Kind of the API Group to select resources from. Together with Group and Version it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md
        :param label_selector: LabelSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource labels.
        :param name: Name to match resources with.
        :param namespace: Namespace to select resources from.
        :param version: Version of the API Group to select resources from. Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if annotation_selector is not None:
            self._values["annotation_selector"] = annotation_selector
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def annotation_selector(self) -> typing.Optional[builtins.str]:
        '''AnnotationSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource annotations.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#annotationSelector
        '''
        result = self._values.get("annotation_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the API group to select resources from.

        Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the API Group to select resources from.

        Together with Group and Version it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_selector(self) -> typing.Optional[builtins.str]:
        '''LabelSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource labels.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to match resources with.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to select resources from.

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of the API Group to select resources from.

        Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target#version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecRollback",
    jsii_struct_bases=[],
    name_mapping={
        "cleanup_on_fail": "cleanupOnFail",
        "disable_hooks": "disableHooks",
        "disable_wait": "disableWait",
        "disable_wait_for_jobs": "disableWaitForJobs",
        "force": "force",
        "recreate": "recreate",
        "timeout": "timeout",
    },
)
class HelmReleaseSpecRollback:
    def __init__(
        self,
        *,
        cleanup_on_fail: typing.Optional[builtins.bool] = None,
        disable_hooks: typing.Optional[builtins.bool] = None,
        disable_wait: typing.Optional[builtins.bool] = None,
        disable_wait_for_jobs: typing.Optional[builtins.bool] = None,
        force: typing.Optional[builtins.bool] = None,
        recreate: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Rollback holds the configuration for Helm rollback actions for this HelmRelease.

        :param cleanup_on_fail: CleanupOnFail allows deletion of new resources created during the Helm rollback action when it fails.
        :param disable_hooks: DisableHooks prevents hooks from running during the Helm rollback action.
        :param disable_wait: DisableWait disables the waiting for resources to be ready after a Helm rollback has been performed.
        :param disable_wait_for_jobs: DisableWaitForJobs disables waiting for jobs to complete after a Helm rollback has been performed.
        :param force: Force forces resource updates through a replacement strategy.
        :param recreate: Recreate performs pod restarts for the resource if applicable.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm rollback action. Defaults to 'HelmReleaseSpec.Timeout'. Default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecRollback
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cleanup_on_fail is not None:
            self._values["cleanup_on_fail"] = cleanup_on_fail
        if disable_hooks is not None:
            self._values["disable_hooks"] = disable_hooks
        if disable_wait is not None:
            self._values["disable_wait"] = disable_wait
        if disable_wait_for_jobs is not None:
            self._values["disable_wait_for_jobs"] = disable_wait_for_jobs
        if force is not None:
            self._values["force"] = force
        if recreate is not None:
            self._values["recreate"] = recreate
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def cleanup_on_fail(self) -> typing.Optional[builtins.bool]:
        '''CleanupOnFail allows deletion of new resources created during the Helm rollback action when it fails.

        :schema: HelmReleaseSpecRollback#cleanupOnFail
        '''
        result = self._values.get("cleanup_on_fail")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_hooks(self) -> typing.Optional[builtins.bool]:
        '''DisableHooks prevents hooks from running during the Helm rollback action.

        :schema: HelmReleaseSpecRollback#disableHooks
        '''
        result = self._values.get("disable_hooks")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait(self) -> typing.Optional[builtins.bool]:
        '''DisableWait disables the waiting for resources to be ready after a Helm rollback has been performed.

        :schema: HelmReleaseSpecRollback#disableWait
        '''
        result = self._values.get("disable_wait")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait_for_jobs(self) -> typing.Optional[builtins.bool]:
        '''DisableWaitForJobs disables waiting for jobs to complete after a Helm rollback has been performed.

        :schema: HelmReleaseSpecRollback#disableWaitForJobs
        '''
        result = self._values.get("disable_wait_for_jobs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Force forces resource updates through a replacement strategy.

        :schema: HelmReleaseSpecRollback#force
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def recreate(self) -> typing.Optional[builtins.bool]:
        '''Recreate performs pod restarts for the resource if applicable.

        :schema: HelmReleaseSpecRollback#recreate
        '''
        result = self._values.get("recreate")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm rollback action.

        Defaults to 'HelmReleaseSpec.Timeout'.

        :default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecRollback#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecRollback(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecTest",
    jsii_struct_bases=[],
    name_mapping={
        "enable": "enable",
        "ignore_failures": "ignoreFailures",
        "timeout": "timeout",
    },
)
class HelmReleaseSpecTest:
    def __init__(
        self,
        *,
        enable: typing.Optional[builtins.bool] = None,
        ignore_failures: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Test holds the configuration for Helm test actions for this HelmRelease.

        :param enable: Enable enables Helm test actions for this HelmRelease after an Helm install or upgrade action has been performed.
        :param ignore_failures: IgnoreFailures tells the controller to skip remediation when the Helm tests are run but fail. Can be overwritten for tests run after install or upgrade actions in 'Install.IgnoreTestFailures' and 'Upgrade.IgnoreTestFailures'.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation during the performance of a Helm test action. Defaults to 'HelmReleaseSpec.Timeout'. Default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecTest
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if enable is not None:
            self._values["enable"] = enable
        if ignore_failures is not None:
            self._values["ignore_failures"] = ignore_failures
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enable(self) -> typing.Optional[builtins.bool]:
        '''Enable enables Helm test actions for this HelmRelease after an Helm install or upgrade action has been performed.

        :schema: HelmReleaseSpecTest#enable
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_failures(self) -> typing.Optional[builtins.bool]:
        '''IgnoreFailures tells the controller to skip remediation when the Helm tests are run but fail.

        Can be overwritten for tests run after install or upgrade actions in 'Install.IgnoreTestFailures' and 'Upgrade.IgnoreTestFailures'.

        :schema: HelmReleaseSpecTest#ignoreFailures
        '''
        result = self._values.get("ignore_failures")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation during the performance of a Helm test action.

        Defaults to 'HelmReleaseSpec.Timeout'.

        :default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecTest#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecTest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecUninstall",
    jsii_struct_bases=[],
    name_mapping={
        "disable_hooks": "disableHooks",
        "keep_history": "keepHistory",
        "timeout": "timeout",
    },
)
class HelmReleaseSpecUninstall:
    def __init__(
        self,
        *,
        disable_hooks: typing.Optional[builtins.bool] = None,
        keep_history: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Uninstall holds the configuration for Helm uninstall actions for this HelmRelease.

        :param disable_hooks: DisableHooks prevents hooks from running during the Helm rollback action.
        :param keep_history: KeepHistory tells Helm to remove all associated resources and mark the release as deleted, but retain the release history.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm uninstall action. Defaults to 'HelmReleaseSpec.Timeout'. Default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecUninstall
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_hooks is not None:
            self._values["disable_hooks"] = disable_hooks
        if keep_history is not None:
            self._values["keep_history"] = keep_history
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def disable_hooks(self) -> typing.Optional[builtins.bool]:
        '''DisableHooks prevents hooks from running during the Helm rollback action.

        :schema: HelmReleaseSpecUninstall#disableHooks
        '''
        result = self._values.get("disable_hooks")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def keep_history(self) -> typing.Optional[builtins.bool]:
        '''KeepHistory tells Helm to remove all associated resources and mark the release as deleted, but retain the release history.

        :schema: HelmReleaseSpecUninstall#keepHistory
        '''
        result = self._values.get("keep_history")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm uninstall action.

        Defaults to 'HelmReleaseSpec.Timeout'.

        :default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecUninstall#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecUninstall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecUpgrade",
    jsii_struct_bases=[],
    name_mapping={
        "cleanup_on_fail": "cleanupOnFail",
        "crds": "crds",
        "disable_hooks": "disableHooks",
        "disable_open_api_validation": "disableOpenApiValidation",
        "disable_wait": "disableWait",
        "disable_wait_for_jobs": "disableWaitForJobs",
        "force": "force",
        "preserve_values": "preserveValues",
        "remediation": "remediation",
        "timeout": "timeout",
    },
)
class HelmReleaseSpecUpgrade:
    def __init__(
        self,
        *,
        cleanup_on_fail: typing.Optional[builtins.bool] = None,
        crds: typing.Optional["HelmReleaseSpecUpgradeCrds"] = None,
        disable_hooks: typing.Optional[builtins.bool] = None,
        disable_open_api_validation: typing.Optional[builtins.bool] = None,
        disable_wait: typing.Optional[builtins.bool] = None,
        disable_wait_for_jobs: typing.Optional[builtins.bool] = None,
        force: typing.Optional[builtins.bool] = None,
        preserve_values: typing.Optional[builtins.bool] = None,
        remediation: typing.Optional["HelmReleaseSpecUpgradeRemediation"] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Upgrade holds the configuration for Helm upgrade actions for this HelmRelease.

        :param cleanup_on_fail: CleanupOnFail allows deletion of new resources created during the Helm upgrade action when it fails.
        :param crds: CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here. Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Skip`` and if omitted CRDs are neither installed nor upgraded. Skip: do neither install nor replace (update) any CRDs. Create: new CRDs are created, existing CRDs are neither updated nor deleted. CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted. By default, CRDs are not applied during Helm upgrade action. With this option users can opt-in to CRD upgrade, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions. Default: Skip` and if omitted CRDs are neither installed nor upgraded.
        :param disable_hooks: DisableHooks prevents hooks from running during the Helm upgrade action.
        :param disable_open_api_validation: DisableOpenAPIValidation prevents the Helm upgrade action from validating rendered templates against the Kubernetes OpenAPI Schema.
        :param disable_wait: DisableWait disables the waiting for resources to be ready after a Helm upgrade has been performed.
        :param disable_wait_for_jobs: DisableWaitForJobs disables waiting for jobs to complete after a Helm upgrade has been performed.
        :param force: Force forces resource updates through a replacement strategy.
        :param preserve_values: PreserveValues will make Helm reuse the last release's values and merge in overrides from 'Values'. Setting this flag makes the HelmRelease non-declarative.
        :param remediation: Remediation holds the remediation configuration for when the Helm upgrade action for the HelmRelease fails. The default is to not perform any action.
        :param timeout: Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm upgrade action. Defaults to 'HelmReleaseSpec.Timeout'. Default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecUpgrade
        '''
        if isinstance(remediation, dict):
            remediation = HelmReleaseSpecUpgradeRemediation(**remediation)
        self._values: typing.Dict[str, typing.Any] = {}
        if cleanup_on_fail is not None:
            self._values["cleanup_on_fail"] = cleanup_on_fail
        if crds is not None:
            self._values["crds"] = crds
        if disable_hooks is not None:
            self._values["disable_hooks"] = disable_hooks
        if disable_open_api_validation is not None:
            self._values["disable_open_api_validation"] = disable_open_api_validation
        if disable_wait is not None:
            self._values["disable_wait"] = disable_wait
        if disable_wait_for_jobs is not None:
            self._values["disable_wait_for_jobs"] = disable_wait_for_jobs
        if force is not None:
            self._values["force"] = force
        if preserve_values is not None:
            self._values["preserve_values"] = preserve_values
        if remediation is not None:
            self._values["remediation"] = remediation
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def cleanup_on_fail(self) -> typing.Optional[builtins.bool]:
        '''CleanupOnFail allows deletion of new resources created during the Helm upgrade action when it fails.

        :schema: HelmReleaseSpecUpgrade#cleanupOnFail
        '''
        result = self._values.get("cleanup_on_fail")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def crds(self) -> typing.Optional["HelmReleaseSpecUpgradeCrds"]:
        '''CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here.

        Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Skip`` and if omitted CRDs are neither installed nor upgraded.
        Skip: do neither install nor replace (update) any CRDs.
        Create: new CRDs are created, existing CRDs are neither updated nor deleted.
        CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted.
        By default, CRDs are not applied during Helm upgrade action. With this option users can opt-in to CRD upgrade, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions.

        :default: Skip` and if omitted CRDs are neither installed nor upgraded.

        :schema: HelmReleaseSpecUpgrade#crds
        '''
        result = self._values.get("crds")
        return typing.cast(typing.Optional["HelmReleaseSpecUpgradeCrds"], result)

    @builtins.property
    def disable_hooks(self) -> typing.Optional[builtins.bool]:
        '''DisableHooks prevents hooks from running during the Helm upgrade action.

        :schema: HelmReleaseSpecUpgrade#disableHooks
        '''
        result = self._values.get("disable_hooks")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_open_api_validation(self) -> typing.Optional[builtins.bool]:
        '''DisableOpenAPIValidation prevents the Helm upgrade action from validating rendered templates against the Kubernetes OpenAPI Schema.

        :schema: HelmReleaseSpecUpgrade#disableOpenAPIValidation
        '''
        result = self._values.get("disable_open_api_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait(self) -> typing.Optional[builtins.bool]:
        '''DisableWait disables the waiting for resources to be ready after a Helm upgrade has been performed.

        :schema: HelmReleaseSpecUpgrade#disableWait
        '''
        result = self._values.get("disable_wait")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_wait_for_jobs(self) -> typing.Optional[builtins.bool]:
        '''DisableWaitForJobs disables waiting for jobs to complete after a Helm upgrade has been performed.

        :schema: HelmReleaseSpecUpgrade#disableWaitForJobs
        '''
        result = self._values.get("disable_wait_for_jobs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Force forces resource updates through a replacement strategy.

        :schema: HelmReleaseSpecUpgrade#force
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def preserve_values(self) -> typing.Optional[builtins.bool]:
        '''PreserveValues will make Helm reuse the last release's values and merge in overrides from 'Values'.

        Setting this flag makes the HelmRelease non-declarative.

        :schema: HelmReleaseSpecUpgrade#preserveValues
        '''
        result = self._values.get("preserve_values")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remediation(self) -> typing.Optional["HelmReleaseSpecUpgradeRemediation"]:
        '''Remediation holds the remediation configuration for when the Helm upgrade action for the HelmRelease fails.

        The default is to not perform any action.

        :schema: HelmReleaseSpecUpgrade#remediation
        '''
        result = self._values.get("remediation")
        return typing.cast(typing.Optional["HelmReleaseSpecUpgradeRemediation"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout is the time to wait for any individual Kubernetes operation (like Jobs for hooks) during the performance of a Helm upgrade action.

        Defaults to 'HelmReleaseSpec.Timeout'.

        :default: HelmReleaseSpec.Timeout'.

        :schema: HelmReleaseSpecUpgrade#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecUpgrade(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecUpgradeCrds")
class HelmReleaseSpecUpgradeCrds(enum.Enum):
    '''CRDs upgrade CRDs from the Helm Chart's crds directory according to the CRD upgrade policy provided here.

    Valid values are ``Skip``, ``Create`` or ``CreateReplace``. Default is ``Skip`` and if omitted CRDs are neither installed nor upgraded.
    Skip: do neither install nor replace (update) any CRDs.
    Create: new CRDs are created, existing CRDs are neither updated nor deleted.
    CreateReplace: new CRDs are created, existing CRDs are updated (replaced) but not deleted.
    By default, CRDs are not applied during Helm upgrade action. With this option users can opt-in to CRD upgrade, which is not (yet) natively supported by Helm. https://helm.sh/docs/chart_best_practices/custom_resource_definitions.

    :default: Skip` and if omitted CRDs are neither installed nor upgraded.

    :schema: HelmReleaseSpecUpgradeCrds
    '''

    SKIP = "SKIP"
    '''Skip.'''
    CREATE = "CREATE"
    '''Create.'''
    CREATE_REPLACE = "CREATE_REPLACE"
    '''CreateReplace.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecUpgradeRemediation",
    jsii_struct_bases=[],
    name_mapping={
        "ignore_test_failures": "ignoreTestFailures",
        "remediate_last_failure": "remediateLastFailure",
        "retries": "retries",
        "strategy": "strategy",
    },
)
class HelmReleaseSpecUpgradeRemediation:
    def __init__(
        self,
        *,
        ignore_test_failures: typing.Optional[builtins.bool] = None,
        remediate_last_failure: typing.Optional[builtins.bool] = None,
        retries: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional["HelmReleaseSpecUpgradeRemediationStrategy"] = None,
    ) -> None:
        '''Remediation holds the remediation configuration for when the Helm upgrade action for the HelmRelease fails.

        The default is to not perform any action.

        :param ignore_test_failures: IgnoreTestFailures tells the controller to skip remediation when the Helm tests are run after an upgrade action but fail. Defaults to 'Test.IgnoreFailures'. Default: Test.IgnoreFailures'.
        :param remediate_last_failure: RemediateLastFailure tells the controller to remediate the last failure, when no retries remain. Defaults to 'false' unless 'Retries' is greater than 0. Default: false' unless 'Retries' is greater than 0.
        :param retries: Retries is the number of retries that should be attempted on failures before bailing. Remediation, using 'Strategy', is performed between each attempt. Defaults to '0', a negative integer equals to unlimited retries. Default: 0', a negative integer equals to unlimited retries.
        :param strategy: Strategy to use for failure remediation. Defaults to 'rollback'. Default: rollback'.

        :schema: HelmReleaseSpecUpgradeRemediation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore_test_failures is not None:
            self._values["ignore_test_failures"] = ignore_test_failures
        if remediate_last_failure is not None:
            self._values["remediate_last_failure"] = remediate_last_failure
        if retries is not None:
            self._values["retries"] = retries
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def ignore_test_failures(self) -> typing.Optional[builtins.bool]:
        '''IgnoreTestFailures tells the controller to skip remediation when the Helm tests are run after an upgrade action but fail.

        Defaults to 'Test.IgnoreFailures'.

        :default: Test.IgnoreFailures'.

        :schema: HelmReleaseSpecUpgradeRemediation#ignoreTestFailures
        '''
        result = self._values.get("ignore_test_failures")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remediate_last_failure(self) -> typing.Optional[builtins.bool]:
        '''RemediateLastFailure tells the controller to remediate the last failure, when no retries remain.

        Defaults to 'false' unless 'Retries' is greater than 0.

        :default: false' unless 'Retries' is greater than 0.

        :schema: HelmReleaseSpecUpgradeRemediation#remediateLastFailure
        '''
        result = self._values.get("remediate_last_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Retries is the number of retries that should be attempted on failures before bailing.

        Remediation, using 'Strategy', is performed between each attempt. Defaults to '0', a negative integer equals to unlimited retries.

        :default: 0', a negative integer equals to unlimited retries.

        :schema: HelmReleaseSpecUpgradeRemediation#retries
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional["HelmReleaseSpecUpgradeRemediationStrategy"]:
        '''Strategy to use for failure remediation.

        Defaults to 'rollback'.

        :default: rollback'.

        :schema: HelmReleaseSpecUpgradeRemediation#strategy
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional["HelmReleaseSpecUpgradeRemediationStrategy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecUpgradeRemediation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecUpgradeRemediationStrategy")
class HelmReleaseSpecUpgradeRemediationStrategy(enum.Enum):
    '''Strategy to use for failure remediation.

    Defaults to 'rollback'.

    :default: rollback'.

    :schema: HelmReleaseSpecUpgradeRemediationStrategy
    '''

    ROLLBACK = "ROLLBACK"
    '''rollback.'''
    UNINSTALL = "UNINSTALL"
    '''uninstall.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecValuesFrom",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "optional": "optional",
        "target_path": "targetPath",
        "values_key": "valuesKey",
    },
)
class HelmReleaseSpecValuesFrom:
    def __init__(
        self,
        *,
        kind: "HelmReleaseSpecValuesFromKind",
        name: builtins.str,
        optional: typing.Optional[builtins.bool] = None,
        target_path: typing.Optional[builtins.str] = None,
        values_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''ValuesReference contains a reference to a resource containing Helm values, and optionally the key they can be found at.

        :param kind: Kind of the values referent, valid values are ('Secret', 'ConfigMap').
        :param name: Name of the values referent. Should reside in the same namespace as the referring resource.
        :param optional: Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.
        :param target_path: TargetPath is the YAML dot notation path the value should be merged at. When set, the ValuesKey is expected to be a single flat value. Defaults to 'None', which results in the values getting merged at the root. Default: None', which results in the values getting merged at the root.
        :param values_key: ValuesKey is the data key where the values.yaml or a specific value can be found at. Defaults to 'values.yaml'. Default: values.yaml'.

        :schema: HelmReleaseSpecValuesFrom
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if optional is not None:
            self._values["optional"] = optional
        if target_path is not None:
            self._values["target_path"] = target_path
        if values_key is not None:
            self._values["values_key"] = values_key

    @builtins.property
    def kind(self) -> "HelmReleaseSpecValuesFromKind":
        '''Kind of the values referent, valid values are ('Secret', 'ConfigMap').

        :schema: HelmReleaseSpecValuesFrom#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast("HelmReleaseSpecValuesFromKind", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the values referent.

        Should reside in the same namespace as the referring resource.

        :schema: HelmReleaseSpecValuesFrom#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Optional marks this ValuesReference as optional.

        When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

        :schema: HelmReleaseSpecValuesFrom#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def target_path(self) -> typing.Optional[builtins.str]:
        '''TargetPath is the YAML dot notation path the value should be merged at.

        When set, the ValuesKey is expected to be a single flat value. Defaults to 'None', which results in the values getting merged at the root.

        :default: None', which results in the values getting merged at the root.

        :schema: HelmReleaseSpecValuesFrom#targetPath
        '''
        result = self._values.get("target_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values_key(self) -> typing.Optional[builtins.str]:
        '''ValuesKey is the data key where the values.yaml or a specific value can be found at. Defaults to 'values.yaml'.

        :default: values.yaml'.

        :schema: HelmReleaseSpecValuesFrom#valuesKey
        '''
        result = self._values.get("values_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmReleaseSpecValuesFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkithelm.HelmReleaseSpecValuesFromKind")
class HelmReleaseSpecValuesFromKind(enum.Enum):
    '''Kind of the values referent, valid values are ('Secret', 'ConfigMap').

    :schema: HelmReleaseSpecValuesFromKind
    '''

    SECRET = "SECRET"
    '''Secret.'''
    CONFIG_MAP = "CONFIG_MAP"
    '''ConfigMap.'''


__all__ = [
    "HelmRelease",
    "HelmReleaseProps",
    "HelmReleaseSpec",
    "HelmReleaseSpecChart",
    "HelmReleaseSpecChartSpec",
    "HelmReleaseSpecChartSpecReconcileStrategy",
    "HelmReleaseSpecChartSpecSourceRef",
    "HelmReleaseSpecChartSpecSourceRefKind",
    "HelmReleaseSpecDependsOn",
    "HelmReleaseSpecInstall",
    "HelmReleaseSpecInstallCrds",
    "HelmReleaseSpecInstallRemediation",
    "HelmReleaseSpecKubeConfig",
    "HelmReleaseSpecKubeConfigSecretRef",
    "HelmReleaseSpecPostRenderers",
    "HelmReleaseSpecPostRenderersKustomize",
    "HelmReleaseSpecPostRenderersKustomizeImages",
    "HelmReleaseSpecPostRenderersKustomizePatchesJson6902",
    "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Patch",
    "HelmReleaseSpecPostRenderersKustomizePatchesJson6902PatchOp",
    "HelmReleaseSpecPostRenderersKustomizePatchesJson6902Target",
    "HelmReleaseSpecRollback",
    "HelmReleaseSpecTest",
    "HelmReleaseSpecUninstall",
    "HelmReleaseSpecUpgrade",
    "HelmReleaseSpecUpgradeCrds",
    "HelmReleaseSpecUpgradeRemediation",
    "HelmReleaseSpecUpgradeRemediationStrategy",
    "HelmReleaseSpecValuesFrom",
    "HelmReleaseSpecValuesFromKind",
]

publication.publish()
