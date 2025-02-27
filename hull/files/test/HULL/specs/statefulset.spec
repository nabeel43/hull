# StatefulSet

Test creation of objects and features.

* Prepare default test case for kind "StatefulSet" including suites "pod"

## Render and Validate
* Render
* Expected number of "24" objects were rendered
* Validate

## Metadata
* Check basic metadata functionality

## Pod
* Render
* Check pod functionality

## Violate schema
* Fail to render the templates for values file "values_fail_required.hull.yaml" to test execution folder because error contains "objects.statefulset.failing: serviceName is required"

___

* Clean the test execution folder