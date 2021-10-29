import yaml
import glob
from pathlib import Path
from os import listdir, path
from shutil import copy2


class Yamldata():
    def __init__(self, file_path: str):
        self.data = yaml.safe_load(open(file_path))

    def return_data(self):
        return self.data

    def return_helm_release(self, components: list, dist_file_path: str, spec: str):
        generated_data = list(yaml.load_all(
            open(dist_file_path), Loader=yaml.SafeLoader))

        for component in components:
            Path(
                f"./dist/{component}/values").mkdir(parents=True, exist_ok=True)
            src_value_path = f"./values/aws/{spec}"
            dst_value_path = f"./dist/{component}"

            # Copy helm values from values directory to generated directory
            src_helm_value_files = glob.glob(
                f"{src_value_path}/{component}*.yaml", recursive=True)

            for src_helm_value_file in src_helm_value_files:
                dst_helm_value_file = src_helm_value_file.split("/")[-1]
                copy2(src=src_helm_value_file,
                      dst=f"{dst_value_path}/values/{dst_helm_value_file}")

            # Copy linkerd-cert.yaml to
            if component == "mesh":
                copy2(src="./linkerd-certs.yaml", dst=f"{dst_value_path}/")

            namespaces = []
            helmrelases = []
            for i in generated_data:
                if i["kind"] == "Namespace":
                    namespaces.append(i)
                if i["kind"] == "HelmRelease":
                    helmrelases.append(i)

            for i in namespaces:
                namespace_file = f"{dst_value_path}/namespace.yaml"
                if i["metadata"]["name"] == f"k8s-component-{component}":
                    with open(namespace_file, "w") as file:
                        yaml.dump(i, file)

            for i in helmrelases:
                release_file = f"{dst_value_path}/release.yaml"
                if i["metadata"]["name"] == component:
                    with open(release_file, "w") as file:
                        yaml.dump(i, file)

            # Generate kustomization.yaml
            kustomization_template = {"apiVersion": "kustomize.config.k8s.io/v1beta1", "kind": "Kustomization",
                                      "resources": [""], "configMapGenerator": {""}, "generatorOptions": {"disableNameSuffixHash": True}}

            # Prepare kustomization resources
            resources = listdir(dst_value_path)
            resources.remove("values")
            kustomization_template["resources"] = resources

            # Preapare kustomization configmapGenerator
            configmap_generators = []
            value_files = glob.glob(
                f"{dst_value_path}/values/*.yaml", recursive=False)
            for value_file in value_files:
                value_file = value_file.split("/")[-1]
                component_value = {"name": f"{value_file.split('.')[0]}", "files": [
                    f"{value_file}=values/{value_file}"]}
                configmap_generators.append(component_value)
            kustomization_template["configMapGenerator"] = configmap_generators

            with open(f"{dst_value_path}/kustomization.yaml", "w") as file:
                yaml.dump(kustomization_template, file, sort_keys=False)
