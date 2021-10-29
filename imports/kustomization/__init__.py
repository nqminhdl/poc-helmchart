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


class Kustomization(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iofluxcdtoolkitkustomize.Kustomization",
):
    '''Kustomization is the Schema for the kustomizations API.

    :schema: Kustomization
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["KustomizationSpec"] = None,
    ) -> None:
        '''Defines a "Kustomization" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: KustomizationSpec defines the desired state of a kustomization.
        '''
        props = KustomizationProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["KustomizationSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Kustomization".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: KustomizationSpec defines the desired state of a kustomization.
        '''
        props = KustomizationProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "Kustomization".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class KustomizationProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["KustomizationSpec"] = None,
    ) -> None:
        '''Kustomization is the Schema for the kustomizations API.

        :param metadata: 
        :param spec: KustomizationSpec defines the desired state of a kustomization.

        :schema: Kustomization
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = KustomizationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: Kustomization#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["KustomizationSpec"]:
        '''KustomizationSpec defines the desired state of a kustomization.

        :schema: Kustomization#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["KustomizationSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "interval": "interval",
        "prune": "prune",
        "source_ref": "sourceRef",
        "decryption": "decryption",
        "depends_on": "dependsOn",
        "force": "force",
        "health_checks": "healthChecks",
        "images": "images",
        "kube_config": "kubeConfig",
        "patches": "patches",
        "patches_json6902": "patchesJson6902",
        "patches_strategic_merge": "patchesStrategicMerge",
        "path": "path",
        "post_build": "postBuild",
        "retry_interval": "retryInterval",
        "service_account_name": "serviceAccountName",
        "suspend": "suspend",
        "target_namespace": "targetNamespace",
        "timeout": "timeout",
        "validation": "validation",
    },
)
class KustomizationSpec:
    def __init__(
        self,
        *,
        interval: builtins.str,
        prune: builtins.bool,
        source_ref: "KustomizationSpecSourceRef",
        decryption: typing.Optional["KustomizationSpecDecryption"] = None,
        depends_on: typing.Optional[typing.Sequence["KustomizationSpecDependsOn"]] = None,
        force: typing.Optional[builtins.bool] = None,
        health_checks: typing.Optional[typing.Sequence["KustomizationSpecHealthChecks"]] = None,
        images: typing.Optional[typing.Sequence["KustomizationSpecImages"]] = None,
        kube_config: typing.Optional["KustomizationSpecKubeConfig"] = None,
        patches: typing.Optional[typing.Sequence["KustomizationSpecPatches"]] = None,
        patches_json6902: typing.Optional[typing.Sequence["KustomizationSpecPatchesJson6902"]] = None,
        patches_strategic_merge: typing.Optional[typing.Sequence[typing.Any]] = None,
        path: typing.Optional[builtins.str] = None,
        post_build: typing.Optional["KustomizationSpecPostBuild"] = None,
        retry_interval: typing.Optional[builtins.str] = None,
        service_account_name: typing.Optional[builtins.str] = None,
        suspend: typing.Optional[builtins.bool] = None,
        target_namespace: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
        validation: typing.Optional["KustomizationSpecValidation"] = None,
    ) -> None:
        '''KustomizationSpec defines the desired state of a kustomization.

        :param interval: The interval at which to reconcile the Kustomization.
        :param prune: Prune enables garbage collection.
        :param source_ref: Reference of the source where the kustomization file is.
        :param decryption: Decrypt Kubernetes secrets before applying them on the cluster.
        :param depends_on: DependsOn may contain a dependency.CrossNamespaceDependencyReference slice with references to Kustomization resources that must be ready before this Kustomization can be reconciled.
        :param force: Force instructs the controller to recreate resources when patching fails due to an immutable field change.
        :param health_checks: A list of resources to be included in the health assessment.
        :param images: Images is a list of (image name, new name, new tag or digest) for changing image names, tags or digests. This can also be achieved with a patch, but this operator is simpler to specify.
        :param kube_config: The KubeConfig for reconciling the Kustomization on a remote cluster. When specified, KubeConfig takes precedence over ServiceAccountName.
        :param patches: Strategic merge and JSON patches, defined as inline YAML objects, capable of targeting objects based on kind, label and annotation selectors.
        :param patches_json6902: JSON 6902 patches, defined as inline YAML objects.
        :param patches_strategic_merge: Strategic merge patches, defined as inline YAML objects.
        :param path: Path to the directory containing the kustomization.yaml file, or the set of plain YAMLs a kustomization.yaml should be generated for. Defaults to 'None', which translates to the root path of the SourceRef. Default: None', which translates to the root path of the SourceRef.
        :param post_build: PostBuild describes which actions to perform on the YAML manifest generated by building the kustomize overlay.
        :param retry_interval: The interval at which to retry a previously failed reconciliation. When not specified, the controller uses the KustomizationSpec.Interval value to retry failures.
        :param service_account_name: The name of the Kubernetes service account to impersonate when reconciling this Kustomization.
        :param suspend: This flag tells the controller to suspend subsequent kustomize executions, it does not apply to already started executions. Defaults to false. Default: false.
        :param target_namespace: TargetNamespace sets or overrides the namespace in the kustomization.yaml file.
        :param timeout: Timeout for validation, apply and health checking operations. Defaults to 'Interval' duration. Default: Interval' duration.
        :param validation: Validate the Kubernetes objects before applying them on the cluster. The validation strategy can be 'client' (local dry-run), 'server' (APIServer dry-run) or 'none'. When 'Force' is 'true', validation will fallback to 'client' if set to 'server' because server-side validation is not supported in this scenario.

        :schema: KustomizationSpec
        '''
        if isinstance(source_ref, dict):
            source_ref = KustomizationSpecSourceRef(**source_ref)
        if isinstance(decryption, dict):
            decryption = KustomizationSpecDecryption(**decryption)
        if isinstance(kube_config, dict):
            kube_config = KustomizationSpecKubeConfig(**kube_config)
        if isinstance(post_build, dict):
            post_build = KustomizationSpecPostBuild(**post_build)
        self._values: typing.Dict[str, typing.Any] = {
            "interval": interval,
            "prune": prune,
            "source_ref": source_ref,
        }
        if decryption is not None:
            self._values["decryption"] = decryption
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if force is not None:
            self._values["force"] = force
        if health_checks is not None:
            self._values["health_checks"] = health_checks
        if images is not None:
            self._values["images"] = images
        if kube_config is not None:
            self._values["kube_config"] = kube_config
        if patches is not None:
            self._values["patches"] = patches
        if patches_json6902 is not None:
            self._values["patches_json6902"] = patches_json6902
        if patches_strategic_merge is not None:
            self._values["patches_strategic_merge"] = patches_strategic_merge
        if path is not None:
            self._values["path"] = path
        if post_build is not None:
            self._values["post_build"] = post_build
        if retry_interval is not None:
            self._values["retry_interval"] = retry_interval
        if service_account_name is not None:
            self._values["service_account_name"] = service_account_name
        if suspend is not None:
            self._values["suspend"] = suspend
        if target_namespace is not None:
            self._values["target_namespace"] = target_namespace
        if timeout is not None:
            self._values["timeout"] = timeout
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def interval(self) -> builtins.str:
        '''The interval at which to reconcile the Kustomization.

        :schema: KustomizationSpec#interval
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prune(self) -> builtins.bool:
        '''Prune enables garbage collection.

        :schema: KustomizationSpec#prune
        '''
        result = self._values.get("prune")
        assert result is not None, "Required property 'prune' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def source_ref(self) -> "KustomizationSpecSourceRef":
        '''Reference of the source where the kustomization file is.

        :schema: KustomizationSpec#sourceRef
        '''
        result = self._values.get("source_ref")
        assert result is not None, "Required property 'source_ref' is missing"
        return typing.cast("KustomizationSpecSourceRef", result)

    @builtins.property
    def decryption(self) -> typing.Optional["KustomizationSpecDecryption"]:
        '''Decrypt Kubernetes secrets before applying them on the cluster.

        :schema: KustomizationSpec#decryption
        '''
        result = self._values.get("decryption")
        return typing.cast(typing.Optional["KustomizationSpecDecryption"], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List["KustomizationSpecDependsOn"]]:
        '''DependsOn may contain a dependency.CrossNamespaceDependencyReference slice with references to Kustomization resources that must be ready before this Kustomization can be reconciled.

        :schema: KustomizationSpec#dependsOn
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecDependsOn"]], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Force instructs the controller to recreate resources when patching fails due to an immutable field change.

        :schema: KustomizationSpec#force
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def health_checks(
        self,
    ) -> typing.Optional[typing.List["KustomizationSpecHealthChecks"]]:
        '''A list of resources to be included in the health assessment.

        :schema: KustomizationSpec#healthChecks
        '''
        result = self._values.get("health_checks")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecHealthChecks"]], result)

    @builtins.property
    def images(self) -> typing.Optional[typing.List["KustomizationSpecImages"]]:
        '''Images is a list of (image name, new name, new tag or digest) for changing image names, tags or digests.

        This can also be achieved with a patch, but this operator is simpler to specify.

        :schema: KustomizationSpec#images
        '''
        result = self._values.get("images")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecImages"]], result)

    @builtins.property
    def kube_config(self) -> typing.Optional["KustomizationSpecKubeConfig"]:
        '''The KubeConfig for reconciling the Kustomization on a remote cluster.

        When specified, KubeConfig takes precedence over ServiceAccountName.

        :schema: KustomizationSpec#kubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional["KustomizationSpecKubeConfig"], result)

    @builtins.property
    def patches(self) -> typing.Optional[typing.List["KustomizationSpecPatches"]]:
        '''Strategic merge and JSON patches, defined as inline YAML objects, capable of targeting objects based on kind, label and annotation selectors.

        :schema: KustomizationSpec#patches
        '''
        result = self._values.get("patches")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecPatches"]], result)

    @builtins.property
    def patches_json6902(
        self,
    ) -> typing.Optional[typing.List["KustomizationSpecPatchesJson6902"]]:
        '''JSON 6902 patches, defined as inline YAML objects.

        :schema: KustomizationSpec#patchesJson6902
        '''
        result = self._values.get("patches_json6902")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecPatchesJson6902"]], result)

    @builtins.property
    def patches_strategic_merge(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Strategic merge patches, defined as inline YAML objects.

        :schema: KustomizationSpec#patchesStrategicMerge
        '''
        result = self._values.get("patches_strategic_merge")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to the directory containing the kustomization.yaml file, or the set of plain YAMLs a kustomization.yaml should be generated for. Defaults to 'None', which translates to the root path of the SourceRef.

        :default: None', which translates to the root path of the SourceRef.

        :schema: KustomizationSpec#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_build(self) -> typing.Optional["KustomizationSpecPostBuild"]:
        '''PostBuild describes which actions to perform on the YAML manifest generated by building the kustomize overlay.

        :schema: KustomizationSpec#postBuild
        '''
        result = self._values.get("post_build")
        return typing.cast(typing.Optional["KustomizationSpecPostBuild"], result)

    @builtins.property
    def retry_interval(self) -> typing.Optional[builtins.str]:
        '''The interval at which to retry a previously failed reconciliation.

        When not specified, the controller uses the KustomizationSpec.Interval value to retry failures.

        :schema: KustomizationSpec#retryInterval
        '''
        result = self._values.get("retry_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Kubernetes service account to impersonate when reconciling this Kustomization.

        :schema: KustomizationSpec#serviceAccountName
        '''
        result = self._values.get("service_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspend(self) -> typing.Optional[builtins.bool]:
        '''This flag tells the controller to suspend subsequent kustomize executions, it does not apply to already started executions.

        Defaults to false.

        :default: false.

        :schema: KustomizationSpec#suspend
        '''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def target_namespace(self) -> typing.Optional[builtins.str]:
        '''TargetNamespace sets or overrides the namespace in the kustomization.yaml file.

        :schema: KustomizationSpec#targetNamespace
        '''
        result = self._values.get("target_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout for validation, apply and health checking operations.

        Defaults to 'Interval' duration.

        :default: Interval' duration.

        :schema: KustomizationSpec#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation(self) -> typing.Optional["KustomizationSpecValidation"]:
        '''Validate the Kubernetes objects before applying them on the cluster.

        The validation strategy can be 'client' (local dry-run), 'server' (APIServer dry-run) or 'none'. When 'Force' is 'true', validation will fallback to 'client' if set to 'server' because server-side validation is not supported in this scenario.

        :schema: KustomizationSpec#validation
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["KustomizationSpecValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecDecryption",
    jsii_struct_bases=[],
    name_mapping={"provider": "provider", "secret_ref": "secretRef"},
)
class KustomizationSpecDecryption:
    def __init__(
        self,
        *,
        provider: "KustomizationSpecDecryptionProvider",
        secret_ref: typing.Optional["KustomizationSpecDecryptionSecretRef"] = None,
    ) -> None:
        '''Decrypt Kubernetes secrets before applying them on the cluster.

        :param provider: Provider is the name of the decryption engine.
        :param secret_ref: The secret name containing the private OpenPGP keys used for decryption.

        :schema: KustomizationSpecDecryption
        '''
        if isinstance(secret_ref, dict):
            secret_ref = KustomizationSpecDecryptionSecretRef(**secret_ref)
        self._values: typing.Dict[str, typing.Any] = {
            "provider": provider,
        }
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def provider(self) -> "KustomizationSpecDecryptionProvider":
        '''Provider is the name of the decryption engine.

        :schema: KustomizationSpecDecryption#provider
        '''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast("KustomizationSpecDecryptionProvider", result)

    @builtins.property
    def secret_ref(self) -> typing.Optional["KustomizationSpecDecryptionSecretRef"]:
        '''The secret name containing the private OpenPGP keys used for decryption.

        :schema: KustomizationSpecDecryption#secretRef
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["KustomizationSpecDecryptionSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecDecryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecDecryptionProvider")
class KustomizationSpecDecryptionProvider(enum.Enum):
    '''Provider is the name of the decryption engine.

    :schema: KustomizationSpecDecryptionProvider
    '''

    SOPS = "SOPS"
    '''sops.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecDecryptionSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KustomizationSpecDecryptionSecretRef:
    def __init__(self, *, name: builtins.str) -> None:
        '''The secret name containing the private OpenPGP keys used for decryption.

        :param name: Name of the referent.

        :schema: KustomizationSpecDecryptionSecretRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: KustomizationSpecDecryptionSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecDecryptionSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecDependsOn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class KustomizationSpecDependsOn:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CrossNamespaceDependencyReference holds the reference to a dependency.

        :param name: Name holds the name reference of a dependency.
        :param namespace: Namespace holds the namespace reference of a dependency.

        :schema: KustomizationSpecDependsOn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name holds the name reference of a dependency.

        :schema: KustomizationSpecDependsOn#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace holds the namespace reference of a dependency.

        :schema: KustomizationSpecDependsOn#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecDependsOn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecHealthChecks",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "api_version": "apiVersion",
        "namespace": "namespace",
    },
)
class KustomizationSpecHealthChecks:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''NamespacedObjectKindReference contains enough information to let you locate the typed referenced object in any namespace.

        :param kind: Kind of the referent.
        :param name: Name of the referent.
        :param api_version: API version of the referent, if not specified the Kubernetes preferred version will be used.
        :param namespace: Namespace of the referent, when not specified it acts as LocalObjectReference.

        :schema: KustomizationSpecHealthChecks
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of the referent.

        :schema: KustomizationSpecHealthChecks#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: KustomizationSpecHealthChecks#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the referent, if not specified the Kubernetes preferred version will be used.

        :schema: KustomizationSpecHealthChecks#apiVersion
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the referent, when not specified it acts as LocalObjectReference.

        :schema: KustomizationSpecHealthChecks#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecHealthChecks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecImages",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "digest": "digest",
        "new_name": "newName",
        "new_tag": "newTag",
    },
)
class KustomizationSpecImages:
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

        :schema: KustomizationSpecImages
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

        :schema: KustomizationSpecImages#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def digest(self) -> typing.Optional[builtins.str]:
        '''Digest is the value used to replace the original image tag.

        If digest is present NewTag value is ignored.

        :schema: KustomizationSpecImages#digest
        '''
        result = self._values.get("digest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_name(self) -> typing.Optional[builtins.str]:
        '''NewName is the value used to replace the original name.

        :schema: KustomizationSpecImages#newName
        '''
        result = self._values.get("new_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_tag(self) -> typing.Optional[builtins.str]:
        '''NewTag is the value used to replace the original tag.

        :schema: KustomizationSpecImages#newTag
        '''
        result = self._values.get("new_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecKubeConfig",
    jsii_struct_bases=[],
    name_mapping={"secret_ref": "secretRef"},
)
class KustomizationSpecKubeConfig:
    def __init__(
        self,
        *,
        secret_ref: typing.Optional["KustomizationSpecKubeConfigSecretRef"] = None,
    ) -> None:
        '''The KubeConfig for reconciling the Kustomization on a remote cluster.

        When specified, KubeConfig takes precedence over ServiceAccountName.

        :param secret_ref: SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value. It must be in the same namespace as the Kustomization. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the Kustomization.

        :schema: KustomizationSpecKubeConfig
        '''
        if isinstance(secret_ref, dict):
            secret_ref = KustomizationSpecKubeConfigSecretRef(**secret_ref)
        self._values: typing.Dict[str, typing.Any] = {}
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def secret_ref(self) -> typing.Optional["KustomizationSpecKubeConfigSecretRef"]:
        '''SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value.

        It must be in the same namespace as the Kustomization. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the Kustomization.

        :schema: KustomizationSpecKubeConfig#secretRef
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["KustomizationSpecKubeConfigSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecKubeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecKubeConfigSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KustomizationSpecKubeConfigSecretRef:
    def __init__(self, *, name: builtins.str) -> None:
        '''SecretRef holds the name to a secret that contains a 'value' key with the kubeconfig file as the value.

        It must be in the same namespace as the Kustomization. It is recommended that the kubeconfig is self-contained, and the secret is regularly updated if credentials such as a cloud-access-token expire. Cloud specific ``cmd-path`` auth helpers will not function without adding binaries and credentials to the Pod that is responsible for reconciling the Kustomization.

        :param name: Name of the referent.

        :schema: KustomizationSpecKubeConfigSecretRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: KustomizationSpecKubeConfigSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecKubeConfigSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatches",
    jsii_struct_bases=[],
    name_mapping={"patch": "patch", "target": "target"},
)
class KustomizationSpecPatches:
    def __init__(
        self,
        *,
        patch: typing.Optional[builtins.str] = None,
        target: typing.Optional["KustomizationSpecPatchesTarget"] = None,
    ) -> None:
        '''Patch contains either a StrategicMerge or a JSON6902 patch, either a file or inline, and the target the patch should be applied to.

        :param patch: Patch contains the JSON6902 patch document with an array of operation objects.
        :param target: Target points to the resources that the patch document should be applied to.

        :schema: KustomizationSpecPatches
        '''
        if isinstance(target, dict):
            target = KustomizationSpecPatchesTarget(**target)
        self._values: typing.Dict[str, typing.Any] = {}
        if patch is not None:
            self._values["patch"] = patch
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def patch(self) -> typing.Optional[builtins.str]:
        '''Patch contains the JSON6902 patch document with an array of operation objects.

        :schema: KustomizationSpecPatches#patch
        '''
        result = self._values.get("patch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional["KustomizationSpecPatchesTarget"]:
        '''Target points to the resources that the patch document should be applied to.

        :schema: KustomizationSpecPatches#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["KustomizationSpecPatchesTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatchesJson6902",
    jsii_struct_bases=[],
    name_mapping={"patch": "patch", "target": "target"},
)
class KustomizationSpecPatchesJson6902:
    def __init__(
        self,
        *,
        patch: typing.Sequence["KustomizationSpecPatchesJson6902Patch"],
        target: "KustomizationSpecPatchesJson6902Target",
    ) -> None:
        '''JSON6902Patch contains a JSON6902 patch and the target the patch should be applied to.

        :param patch: Patch contains the JSON6902 patch document with an array of operation objects.
        :param target: Target points to the resources that the patch document should be applied to.

        :schema: KustomizationSpecPatchesJson6902
        '''
        if isinstance(target, dict):
            target = KustomizationSpecPatchesJson6902Target(**target)
        self._values: typing.Dict[str, typing.Any] = {
            "patch": patch,
            "target": target,
        }

    @builtins.property
    def patch(self) -> typing.List["KustomizationSpecPatchesJson6902Patch"]:
        '''Patch contains the JSON6902 patch document with an array of operation objects.

        :schema: KustomizationSpecPatchesJson6902#patch
        '''
        result = self._values.get("patch")
        assert result is not None, "Required property 'patch' is missing"
        return typing.cast(typing.List["KustomizationSpecPatchesJson6902Patch"], result)

    @builtins.property
    def target(self) -> "KustomizationSpecPatchesJson6902Target":
        '''Target points to the resources that the patch document should be applied to.

        :schema: KustomizationSpecPatchesJson6902#target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("KustomizationSpecPatchesJson6902Target", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPatchesJson6902(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatchesJson6902Patch",
    jsii_struct_bases=[],
    name_mapping={"op": "op", "path": "path", "from_": "from", "value": "value"},
)
class KustomizationSpecPatchesJson6902Patch:
    def __init__(
        self,
        *,
        op: "KustomizationSpecPatchesJson6902PatchOp",
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

        :schema: KustomizationSpecPatchesJson6902Patch
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
    def op(self) -> "KustomizationSpecPatchesJson6902PatchOp":
        '''
        :schema: KustomizationSpecPatchesJson6902Patch#op
        '''
        result = self._values.get("op")
        assert result is not None, "Required property 'op' is missing"
        return typing.cast("KustomizationSpecPatchesJson6902PatchOp", result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :schema: KustomizationSpecPatchesJson6902Patch#path
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KustomizationSpecPatchesJson6902Patch#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Any:
        '''
        :schema: KustomizationSpecPatchesJson6902Patch#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPatchesJson6902Patch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatchesJson6902PatchOp"
)
class KustomizationSpecPatchesJson6902PatchOp(enum.Enum):
    '''
    :schema: KustomizationSpecPatchesJson6902PatchOp
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
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatchesJson6902Target",
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
class KustomizationSpecPatchesJson6902Target:
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

        :schema: KustomizationSpecPatchesJson6902Target
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

        :schema: KustomizationSpecPatchesJson6902Target#annotationSelector
        '''
        result = self._values.get("annotation_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the API group to select resources from.

        Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesJson6902Target#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the API Group to select resources from.

        Together with Group and Version it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesJson6902Target#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_selector(self) -> typing.Optional[builtins.str]:
        '''LabelSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource labels.

        :schema: KustomizationSpecPatchesJson6902Target#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to match resources with.

        :schema: KustomizationSpecPatchesJson6902Target#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to select resources from.

        :schema: KustomizationSpecPatchesJson6902Target#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of the API Group to select resources from.

        Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesJson6902Target#version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPatchesJson6902Target(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPatchesTarget",
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
class KustomizationSpecPatchesTarget:
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

        :schema: KustomizationSpecPatchesTarget
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

        :schema: KustomizationSpecPatchesTarget#annotationSelector
        '''
        result = self._values.get("annotation_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the API group to select resources from.

        Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesTarget#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the API Group to select resources from.

        Together with Group and Version it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesTarget#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_selector(self) -> typing.Optional[builtins.str]:
        '''LabelSelector is a string that follows the label selection expression https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api It matches with the resource labels.

        :schema: KustomizationSpecPatchesTarget#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to match resources with.

        :schema: KustomizationSpecPatchesTarget#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to select resources from.

        :schema: KustomizationSpecPatchesTarget#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of the API Group to select resources from.

        Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources. https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md

        :schema: KustomizationSpecPatchesTarget#version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPatchesTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPostBuild",
    jsii_struct_bases=[],
    name_mapping={"substitute": "substitute", "substitute_from": "substituteFrom"},
)
class KustomizationSpecPostBuild:
    def __init__(
        self,
        *,
        substitute: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        substitute_from: typing.Optional[typing.Sequence["KustomizationSpecPostBuildSubstituteFrom"]] = None,
    ) -> None:
        '''PostBuild describes which actions to perform on the YAML manifest generated by building the kustomize overlay.

        :param substitute: Substitute holds a map of key/value pairs. The variables defined in your YAML manifests that match any of the keys defined in the map will be substituted with the set value. Includes support for bash string replacement functions e.g. ${var:=default}, ${var:position} and ${var/substring/replacement}.
        :param substitute_from: SubstituteFrom holds references to ConfigMaps and Secrets containing the variables and their values to be substituted in the YAML manifests. The ConfigMap and the Secret data keys represent the var names and they must match the vars declared in the manifests for the substitution to happen.

        :schema: KustomizationSpecPostBuild
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if substitute is not None:
            self._values["substitute"] = substitute
        if substitute_from is not None:
            self._values["substitute_from"] = substitute_from

    @builtins.property
    def substitute(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Substitute holds a map of key/value pairs.

        The variables defined in your YAML manifests that match any of the keys defined in the map will be substituted with the set value. Includes support for bash string replacement functions e.g. ${var:=default}, ${var:position} and ${var/substring/replacement}.

        :schema: KustomizationSpecPostBuild#substitute
        '''
        result = self._values.get("substitute")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def substitute_from(
        self,
    ) -> typing.Optional[typing.List["KustomizationSpecPostBuildSubstituteFrom"]]:
        '''SubstituteFrom holds references to ConfigMaps and Secrets containing the variables and their values to be substituted in the YAML manifests.

        The ConfigMap and the Secret data keys represent the var names and they must match the vars declared in the manifests for the substitution to happen.

        :schema: KustomizationSpecPostBuild#substituteFrom
        '''
        result = self._values.get("substitute_from")
        return typing.cast(typing.Optional[typing.List["KustomizationSpecPostBuildSubstituteFrom"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPostBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPostBuildSubstituteFrom",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "name": "name"},
)
class KustomizationSpecPostBuildSubstituteFrom:
    def __init__(
        self,
        *,
        kind: "KustomizationSpecPostBuildSubstituteFromKind",
        name: builtins.str,
    ) -> None:
        '''SubstituteReference contains a reference to a resource containing the variables name and value.

        :param kind: Kind of the values referent, valid values are ('Secret', 'ConfigMap').
        :param name: Name of the values referent. Should reside in the same namespace as the referring resource.

        :schema: KustomizationSpecPostBuildSubstituteFrom
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def kind(self) -> "KustomizationSpecPostBuildSubstituteFromKind":
        '''Kind of the values referent, valid values are ('Secret', 'ConfigMap').

        :schema: KustomizationSpecPostBuildSubstituteFrom#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast("KustomizationSpecPostBuildSubstituteFromKind", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the values referent.

        Should reside in the same namespace as the referring resource.

        :schema: KustomizationSpecPostBuildSubstituteFrom#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecPostBuildSubstituteFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecPostBuildSubstituteFromKind"
)
class KustomizationSpecPostBuildSubstituteFromKind(enum.Enum):
    '''Kind of the values referent, valid values are ('Secret', 'ConfigMap').

    :schema: KustomizationSpecPostBuildSubstituteFromKind
    '''

    SECRET = "SECRET"
    '''Secret.'''
    CONFIG_MAP = "CONFIG_MAP"
    '''ConfigMap.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecSourceRef",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "api_version": "apiVersion",
        "namespace": "namespace",
    },
)
class KustomizationSpecSourceRef:
    def __init__(
        self,
        *,
        kind: "KustomizationSpecSourceRefKind",
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Reference of the source where the kustomization file is.

        :param kind: Kind of the referent.
        :param name: Name of the referent.
        :param api_version: API version of the referent.
        :param namespace: Namespace of the referent, defaults to the Kustomization namespace.

        :schema: KustomizationSpecSourceRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def kind(self) -> "KustomizationSpecSourceRefKind":
        '''Kind of the referent.

        :schema: KustomizationSpecSourceRef#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast("KustomizationSpecSourceRefKind", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: KustomizationSpecSourceRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the referent.

        :schema: KustomizationSpecSourceRef#apiVersion
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the referent, defaults to the Kustomization namespace.

        :schema: KustomizationSpecSourceRef#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustomizationSpecSourceRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecSourceRefKind")
class KustomizationSpecSourceRefKind(enum.Enum):
    '''Kind of the referent.

    :schema: KustomizationSpecSourceRefKind
    '''

    GIT_REPOSITORY = "GIT_REPOSITORY"
    '''GitRepository.'''
    BUCKET = "BUCKET"
    '''Bucket.'''


@jsii.enum(jsii_type="iofluxcdtoolkitkustomize.KustomizationSpecValidation")
class KustomizationSpecValidation(enum.Enum):
    '''Validate the Kubernetes objects before applying them on the cluster.

    The validation strategy can be 'client' (local dry-run), 'server' (APIServer dry-run) or 'none'. When 'Force' is 'true', validation will fallback to 'client' if set to 'server' because server-side validation is not supported in this scenario.

    :schema: KustomizationSpecValidation
    '''

    NONE = "NONE"
    '''none.'''
    CLIENT = "CLIENT"
    '''client.'''
    SERVER = "SERVER"
    '''server.'''


__all__ = [
    "Kustomization",
    "KustomizationProps",
    "KustomizationSpec",
    "KustomizationSpecDecryption",
    "KustomizationSpecDecryptionProvider",
    "KustomizationSpecDecryptionSecretRef",
    "KustomizationSpecDependsOn",
    "KustomizationSpecHealthChecks",
    "KustomizationSpecImages",
    "KustomizationSpecKubeConfig",
    "KustomizationSpecKubeConfigSecretRef",
    "KustomizationSpecPatches",
    "KustomizationSpecPatchesJson6902",
    "KustomizationSpecPatchesJson6902Patch",
    "KustomizationSpecPatchesJson6902PatchOp",
    "KustomizationSpecPatchesJson6902Target",
    "KustomizationSpecPatchesTarget",
    "KustomizationSpecPostBuild",
    "KustomizationSpecPostBuildSubstituteFrom",
    "KustomizationSpecPostBuildSubstituteFromKind",
    "KustomizationSpecSourceRef",
    "KustomizationSpecSourceRefKind",
    "KustomizationSpecValidation",
]

publication.publish()
