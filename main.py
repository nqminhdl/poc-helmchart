#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart

from handler import Yamldata
from k8s import BundleChart
from os import environ

spec = environ['SPEC']
config = Yamldata(file_path=f'{spec}.yaml')
chart_version = '0.2.0'
namespaces = config.return_data()['namespaces']
components = list(config.return_data()['components'].keys())

# Generate infra k8s manifests
app = App()
BundleChart(app, "bundle-infra-charts").manifests(config=config,
                                                  chart_version=chart_version,
                                                  namespaces=namespaces,
                                                  components=components
                                                  )
app.synth()

# Split helm release into different folders
config.return_helm_release(
    components=components,
    dist_file_path='./dist/bundle-infra-charts.k8s.yaml',
    spec=spec
)
