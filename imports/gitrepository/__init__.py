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


class GitRepository(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iofluxcdtoolkitsource.GitRepository",
):
    '''GitRepository is the Schema for the gitrepositories API.

    :schema: GitRepository
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GitRepositorySpec"] = None,
    ) -> None:
        '''Defines a "GitRepository" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: GitRepositorySpec defines the desired state of a Git repository.
        '''
        props = GitRepositoryProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GitRepositorySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "GitRepository".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: GitRepositorySpec defines the desired state of a Git repository.
        '''
        props = GitRepositoryProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "GitRepository".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class GitRepositoryProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GitRepositorySpec"] = None,
    ) -> None:
        '''GitRepository is the Schema for the gitrepositories API.

        :param metadata: 
        :param spec: GitRepositorySpec defines the desired state of a Git repository.

        :schema: GitRepository
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = GitRepositorySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: GitRepository#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["GitRepositorySpec"]:
        '''GitRepositorySpec defines the desired state of a Git repository.

        :schema: GitRepository#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["GitRepositorySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpec",
    jsii_struct_bases=[],
    name_mapping={
        "interval": "interval",
        "url": "url",
        "git_implementation": "gitImplementation",
        "ignore": "ignore",
        "include": "include",
        "recurse_submodules": "recurseSubmodules",
        "ref": "ref",
        "secret_ref": "secretRef",
        "suspend": "suspend",
        "timeout": "timeout",
        "verify": "verify",
    },
)
class GitRepositorySpec:
    def __init__(
        self,
        *,
        interval: builtins.str,
        url: builtins.str,
        git_implementation: typing.Optional["GitRepositorySpecGitImplementation"] = None,
        ignore: typing.Optional[builtins.str] = None,
        include: typing.Optional[typing.Sequence["GitRepositorySpecInclude"]] = None,
        recurse_submodules: typing.Optional[builtins.bool] = None,
        ref: typing.Optional["GitRepositorySpecRef"] = None,
        secret_ref: typing.Optional["GitRepositorySpecSecretRef"] = None,
        suspend: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[builtins.str] = None,
        verify: typing.Optional["GitRepositorySpecVerify"] = None,
    ) -> None:
        '''GitRepositorySpec defines the desired state of a Git repository.

        :param interval: The interval at which to check for repository updates.
        :param url: The repository URL, can be a HTTP/S or SSH address.
        :param git_implementation: Determines which git client library to use. Defaults to go-git, valid values are ('go-git', 'libgit2'). Default: go-git, valid values are ('go-git', 'libgit2').
        :param ignore: Ignore overrides the set of excluded patterns in the .sourceignore format (which is the same as .gitignore). If not provided, a default will be used, consult the documentation for your version to find out what those are.
        :param include: Extra git repositories to map into the repository.
        :param recurse_submodules: When enabled, after the clone is created, initializes all submodules within, using their default settings. This option is available only when using the 'go-git' GitImplementation.
        :param ref: The Git reference to checkout and monitor for changes, defaults to master branch.
        :param secret_ref: The secret name containing the Git credentials. For HTTPS repositories the secret must contain username and password fields. For SSH repositories the secret must contain identity, identity.pub and known_hosts fields.
        :param suspend: This flag tells the controller to suspend the reconciliation of this source.
        :param timeout: The timeout for remote Git operations like cloning, defaults to 20s.
        :param verify: Verify OpenPGP signature for the Git commit HEAD points to.

        :schema: GitRepositorySpec
        '''
        if isinstance(ref, dict):
            ref = GitRepositorySpecRef(**ref)
        if isinstance(secret_ref, dict):
            secret_ref = GitRepositorySpecSecretRef(**secret_ref)
        if isinstance(verify, dict):
            verify = GitRepositorySpecVerify(**verify)
        self._values: typing.Dict[str, typing.Any] = {
            "interval": interval,
            "url": url,
        }
        if git_implementation is not None:
            self._values["git_implementation"] = git_implementation
        if ignore is not None:
            self._values["ignore"] = ignore
        if include is not None:
            self._values["include"] = include
        if recurse_submodules is not None:
            self._values["recurse_submodules"] = recurse_submodules
        if ref is not None:
            self._values["ref"] = ref
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref
        if suspend is not None:
            self._values["suspend"] = suspend
        if timeout is not None:
            self._values["timeout"] = timeout
        if verify is not None:
            self._values["verify"] = verify

    @builtins.property
    def interval(self) -> builtins.str:
        '''The interval at which to check for repository updates.

        :schema: GitRepositorySpec#interval
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The repository URL, can be a HTTP/S or SSH address.

        :schema: GitRepositorySpec#url
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def git_implementation(
        self,
    ) -> typing.Optional["GitRepositorySpecGitImplementation"]:
        '''Determines which git client library to use.

        Defaults to go-git, valid values are ('go-git', 'libgit2').

        :default: go-git, valid values are ('go-git', 'libgit2').

        :schema: GitRepositorySpec#gitImplementation
        '''
        result = self._values.get("git_implementation")
        return typing.cast(typing.Optional["GitRepositorySpecGitImplementation"], result)

    @builtins.property
    def ignore(self) -> typing.Optional[builtins.str]:
        '''Ignore overrides the set of excluded patterns in the .sourceignore format (which is the same as .gitignore). If not provided, a default will be used, consult the documentation for your version to find out what those are.

        :schema: GitRepositorySpec#ignore
        '''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List["GitRepositorySpecInclude"]]:
        '''Extra git repositories to map into the repository.

        :schema: GitRepositorySpec#include
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List["GitRepositorySpecInclude"]], result)

    @builtins.property
    def recurse_submodules(self) -> typing.Optional[builtins.bool]:
        '''When enabled, after the clone is created, initializes all submodules within, using their default settings.

        This option is available only when using the 'go-git' GitImplementation.

        :schema: GitRepositorySpec#recurseSubmodules
        '''
        result = self._values.get("recurse_submodules")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ref(self) -> typing.Optional["GitRepositorySpecRef"]:
        '''The Git reference to checkout and monitor for changes, defaults to master branch.

        :schema: GitRepositorySpec#ref
        '''
        result = self._values.get("ref")
        return typing.cast(typing.Optional["GitRepositorySpecRef"], result)

    @builtins.property
    def secret_ref(self) -> typing.Optional["GitRepositorySpecSecretRef"]:
        '''The secret name containing the Git credentials.

        For HTTPS repositories the secret must contain username and password fields. For SSH repositories the secret must contain identity, identity.pub and known_hosts fields.

        :schema: GitRepositorySpec#secretRef
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["GitRepositorySpecSecretRef"], result)

    @builtins.property
    def suspend(self) -> typing.Optional[builtins.bool]:
        '''This flag tells the controller to suspend the reconciliation of this source.

        :schema: GitRepositorySpec#suspend
        '''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''The timeout for remote Git operations like cloning, defaults to 20s.

        :schema: GitRepositorySpec#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify(self) -> typing.Optional["GitRepositorySpecVerify"]:
        '''Verify OpenPGP signature for the Git commit HEAD points to.

        :schema: GitRepositorySpec#verify
        '''
        result = self._values.get("verify")
        return typing.cast(typing.Optional["GitRepositorySpecVerify"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkitsource.GitRepositorySpecGitImplementation")
class GitRepositorySpecGitImplementation(enum.Enum):
    '''Determines which git client library to use.

    Defaults to go-git, valid values are ('go-git', 'libgit2').

    :default: go-git, valid values are ('go-git', 'libgit2').

    :schema: GitRepositorySpecGitImplementation
    '''

    GO_GIT = "GO_GIT"
    '''go-git.'''
    LIBGIT2 = "LIBGIT2"
    '''libgit2.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecInclude",
    jsii_struct_bases=[],
    name_mapping={
        "repository": "repository",
        "from_path": "fromPath",
        "to_path": "toPath",
    },
)
class GitRepositorySpecInclude:
    def __init__(
        self,
        *,
        repository: "GitRepositorySpecIncludeRepository",
        from_path: typing.Optional[builtins.str] = None,
        to_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''GitRepositoryInclude defines a source with a from and to path.

        :param repository: Reference to a GitRepository to include.
        :param from_path: The path to copy contents from, defaults to the root directory.
        :param to_path: The path to copy contents to, defaults to the name of the source ref.

        :schema: GitRepositorySpecInclude
        '''
        if isinstance(repository, dict):
            repository = GitRepositorySpecIncludeRepository(**repository)
        self._values: typing.Dict[str, typing.Any] = {
            "repository": repository,
        }
        if from_path is not None:
            self._values["from_path"] = from_path
        if to_path is not None:
            self._values["to_path"] = to_path

    @builtins.property
    def repository(self) -> "GitRepositorySpecIncludeRepository":
        '''Reference to a GitRepository to include.

        :schema: GitRepositorySpecInclude#repository
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast("GitRepositorySpecIncludeRepository", result)

    @builtins.property
    def from_path(self) -> typing.Optional[builtins.str]:
        '''The path to copy contents from, defaults to the root directory.

        :schema: GitRepositorySpecInclude#fromPath
        '''
        result = self._values.get("from_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to_path(self) -> typing.Optional[builtins.str]:
        '''The path to copy contents to, defaults to the name of the source ref.

        :schema: GitRepositorySpecInclude#toPath
        '''
        result = self._values.get("to_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecInclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecIncludeRepository",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GitRepositorySpecIncludeRepository:
    def __init__(self, *, name: builtins.str) -> None:
        '''Reference to a GitRepository to include.

        :param name: Name of the referent.

        :schema: GitRepositorySpecIncludeRepository
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: GitRepositorySpecIncludeRepository#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecIncludeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecRef",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "commit": "commit",
        "semver": "semver",
        "tag": "tag",
    },
)
class GitRepositorySpecRef:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        commit: typing.Optional[builtins.str] = None,
        semver: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The Git reference to checkout and monitor for changes, defaults to master branch.

        :param branch: The Git branch to checkout, defaults to master.
        :param commit: The Git commit SHA to checkout, if specified Tag filters will be ignored.
        :param semver: The Git tag semver expression, takes precedence over Tag.
        :param tag: The Git tag to checkout, takes precedence over Branch.

        :schema: GitRepositorySpecRef
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if commit is not None:
            self._values["commit"] = commit
        if semver is not None:
            self._values["semver"] = semver
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The Git branch to checkout, defaults to master.

        :schema: GitRepositorySpecRef#branch
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit(self) -> typing.Optional[builtins.str]:
        '''The Git commit SHA to checkout, if specified Tag filters will be ignored.

        :schema: GitRepositorySpecRef#commit
        '''
        result = self._values.get("commit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def semver(self) -> typing.Optional[builtins.str]:
        '''The Git tag semver expression, takes precedence over Tag.

        :schema: GitRepositorySpecRef#semver
        '''
        result = self._values.get("semver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The Git tag to checkout, takes precedence over Branch.

        :schema: GitRepositorySpecRef#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GitRepositorySpecSecretRef:
    def __init__(self, *, name: builtins.str) -> None:
        '''The secret name containing the Git credentials.

        For HTTPS repositories the secret must contain username and password fields. For SSH repositories the secret must contain identity, identity.pub and known_hosts fields.

        :param name: Name of the referent.

        :schema: GitRepositorySpecSecretRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: GitRepositorySpecSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecVerify",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "secret_ref": "secretRef"},
)
class GitRepositorySpecVerify:
    def __init__(
        self,
        *,
        mode: "GitRepositorySpecVerifyMode",
        secret_ref: typing.Optional["GitRepositorySpecVerifySecretRef"] = None,
    ) -> None:
        '''Verify OpenPGP signature for the Git commit HEAD points to.

        :param mode: Mode describes what git object should be verified, currently ('head').
        :param secret_ref: The secret name containing the public keys of all trusted Git authors.

        :schema: GitRepositorySpecVerify
        '''
        if isinstance(secret_ref, dict):
            secret_ref = GitRepositorySpecVerifySecretRef(**secret_ref)
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def mode(self) -> "GitRepositorySpecVerifyMode":
        '''Mode describes what git object should be verified, currently ('head').

        :schema: GitRepositorySpecVerify#mode
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast("GitRepositorySpecVerifyMode", result)

    @builtins.property
    def secret_ref(self) -> typing.Optional["GitRepositorySpecVerifySecretRef"]:
        '''The secret name containing the public keys of all trusted Git authors.

        :schema: GitRepositorySpecVerify#secretRef
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["GitRepositorySpecVerifySecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecVerify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iofluxcdtoolkitsource.GitRepositorySpecVerifyMode")
class GitRepositorySpecVerifyMode(enum.Enum):
    '''Mode describes what git object should be verified, currently ('head').

    :schema: GitRepositorySpecVerifyMode
    '''

    HEAD = "HEAD"
    '''head.'''


@jsii.data_type(
    jsii_type="iofluxcdtoolkitsource.GitRepositorySpecVerifySecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GitRepositorySpecVerifySecretRef:
    def __init__(self, *, name: builtins.str) -> None:
        '''The secret name containing the public keys of all trusted Git authors.

        :param name: Name of the referent.

        :schema: GitRepositorySpecVerifySecretRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        :schema: GitRepositorySpecVerifySecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitRepositorySpecVerifySecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GitRepository",
    "GitRepositoryProps",
    "GitRepositorySpec",
    "GitRepositorySpecGitImplementation",
    "GitRepositorySpecInclude",
    "GitRepositorySpecIncludeRepository",
    "GitRepositorySpecRef",
    "GitRepositorySpecSecretRef",
    "GitRepositorySpecVerify",
    "GitRepositorySpecVerifyMode",
    "GitRepositorySpecVerifySecretRef",
]

publication.publish()
