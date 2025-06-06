# CSIT - Continuous System Integration Testing

- [CSIT - Continuous System Integration Testing](#csit---continuous-system-integration-testing)
  - [Architecture](#architecture)
- [Integration tests](#integration-tests)
  - [Directory structure](#directory-structure)
  - [Running tests](#running-tests)
  - [Running tests using GitHub actions](#running-tests-using-github-actions)
  - [How to extend tests with your own test](#how-to-extend-tests-with-your-own-test)
- [Samples](#samples)
  - [Running tests](#running-tests-1)
- [Updating the `agntcy/dir` testdata](#updating-the-agntcydir-testdata)
- [Copyright Notice](#copyright-notice)

## Architecture

Agncty CSIT system design needs to meet continuously expanding requirements of
Agntcy projects including Agent Gateway Protocol, Agent Directory and many more.

The directory structure of the CSIT:

```
csit
└── integrations
│   ├── Taskfile.yaml                   # Task definitions
│   ├── docs                            # Documentations
│   ├── environment
│   │   └── kind                        # kind related manifests
│   ├── agntcy-dir                      # Agent directory related tests, components, etc...
│   │   ├── components                  # the compontents charts
│   │   ├── examples                    # the examples that can be used for testing
│   │   ├── manifests                   # requred manifests for tests
│   │   └── tests                       # tests
│   └── agntcy-agp                      # Agent Gateway related tests, components, etc...
│       └── agentic-apps                # Agentic apps for gateway tests
│           ├── autogen_agent
│           └── langchain_agent
│
└── samples
    ├── app1                            # Agentic application example
    │   ├── model.json                  # Required model file
    │   ├── build.config.yaml           # Required build configuration file
    ├── app2                            # Another agentic application example
    │   ├── model.json
    │   ├── build.config.yaml
```


# Integration tests

> Focuses on testing interactions between integrated components.

## Directory structure

Inside csit integrations directory contains the tasks that creating the test
environment, deploying the components that will be tested, and running the tests.

```
integrations
├── Taskfile.yaml                   # Task definitions
├── docs                            # Documentations
├── environment
│   └── kind                        # kind related manifests
├── agntcy-dir                      # Agent directory related tests, components, etc...
│   ├── components                  # the compontents charts
│   ├── examples                    # the examples that can be used for testing
│   ├── manifests                   # requred manifests for tests
│   └── tests                       # tests
└── agntcy-agp                      # Agent Gateway related tests, components, etc...
    └── agentic-apps                # Agentic apps for gateway tests
        ├── autogen_agent
        └── langchain_agent
```

## Running tests

We can launch tests using taskfile locally or in GitHub actions.
Running locally we need to create a test cluster and deploy the test env on
it before running the tests.
It requires the following tools to be installed on local machine:
  - [Taskfile](https://taskfile.dev/installation/)
  - [Go](https://go.dev/doc/install)
  - [Docker](https://docs.docker.com/get-started/get-docker/)
  - [Kind](https://kind.sigs.k8s.io/docs/user/quick-start#installation)
  - [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
  - [Helm](https://helm.sh/docs/intro/install/)

```bash
cd integrations
task kind:create
task directory:test-env:deploy
task directory:test
```

We can focus on specified tests:
```bash
task directory:test:compiler
```

After we finish the tests we can destroy the test cluster
```bash
task kind:destroy
```


## Running tests using GitHub actions

We can run integration test using Github actions using `gh` command line tool or using the GitHub web UI

```bash
gh workflow run test-integrations -f testenv=kind
```

If we want to run the tests on a specified branch

```bash
gh workflow run test-integrations --ref feat/integration/deploy-agent-directory -f testenv=kind
```


## How to extend tests with your own test

Contributing your own tests to our project is a great way to improve the robustness and coverage of our testing suite. Follow these steps to add your tests.

1. Fork and Clone the Repository

Fork the repository to your GitHub account.
Clone your fork to your local machine.

```bash
git clone https://github.com/your-username/repository.git
cd repository
```

2. Create a New Branch

Create a new branch for your test additions to keep your changes organized and separate from the main codebase.


```bash
git checkout -b add-new-test
```

3. Navigate to the Integrations Directory

Locate the integrations directory where the test components are organized.

```bash
cd integrations
```

4. Add Your Test

Create a new sub-directory for your test if necessary, following the existing structure. For example, integrations/new-component.
Add all necessary test files, such as scripts, manifests, and configuration files.

5. Update Taskfile

Modify the Taskfile.yaml to include tasks for deploying and running your new test.

```yaml
tasks:
  test:env:new-component:deploy:
    desc: Desription of deployig new component elements
    cmds:
      - # Command for deploying your components if needed

  test:env:new-component:cleanup:
    desc: Desription of cleaning up component elements
    cmds:
      - # Command for cleaning up your components if needed

  test:new-component:
    desc: Desription of the test
    cmds:
      - # Commands to set up and run your test
```

6. Test Locally

Before pushing your changes, test them locally to ensure everything works as expected.

```bash
task kind:create
task new-componet:test-env:deploy
task new-component:test
task new-componet:test-env:cleanup
task kind:destroy
```

7. Document Your Test

Update the documentation in the docs folder to include details about your new test. Explain the purpose of the test, any special setup instructions, and how it fits into the overall testing strategy.

8. Commit and Push Your Changes

Commit your changes with a descriptive message and push them to your fork.

```bash
git add .
git commit -m "feat: add new test for component X"
git push origin add-new-test
```

9. Submit a Pull Request

Go to the original repository on GitHub and submit a pull request from your branch.
Provide a detailed description of what your test covers and any additional context needed for reviewers.

# Samples

The directory sturcture of the samples applications:

```
samples
├── app1                            # Agentic application example
│   ├── model.json                  # Required model file
│   ├── build.config.yaml           # Required build configuration file
├── app2                            # Another agentic application example
│   ├── model.json
│   ├── build.config.yaml
```

The samples directory in the CSIT repository serves two primary purposes related to the testing of agentic applications:


1. Compilation and Execution Verification: The agentic applications stored within the samples directory are subjected to sample tests. These tests are designed to run whenever changes are made to the agentic apps to ensure they compile correctly and are able to execute as expected.
2. Base for Agent Directory Integration Test:
The agentic applications in the samples directory also serve as the foundation for the agent model build and push test. This specific test checks for the presence of two required files: model.json and build.config.yaml. If these files are present within an agentic application, the integration agent model build and push testa are triggered. This test is crucial for validating the construction and verification of the agent model, ensuring that all necessary components are correctly configured and operational.

## Running tests

We can launch tests using taskfile locally or in GitHub actions.
Running locally we need some tools to build the sample applications and run the tests.
It requires the followings on local machine:
  - [Taskfile](https://taskfile.dev/installation/)
  - [Python 3.12.X](https://www.python.org/downloads/)
  - [Poetry](https://python-poetry.org/docs/#installation)
  - [Docker](https://docs.docker.com/get-started/get-docker/)
  - [Kind](https://kind.sigs.k8s.io/docs/user/quick-start#installation)
  - [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

```bash
cd samples/[app-name]
task run:test
```

## Updating the agntcy/dir testdata

If we want to update the `integrations/agntcy-dir/examples/dir/e2e/testdata` directory we will need to add `agntcy/dir` as a remote and create a patch for it by diffing with the `agntcy/dir` repo

```bash
# add agntcy/dir as remote
git remote add -f dir https://github.com/agntcy/dir.git
# fetch dir
git fetch dir
# example of updating the integrations/agntcy-dir/examples/dir/e2e/testdata directory to the agntcy/dir main
git diff --binary HEAD:integrations/agntcy-dir/examples/dir/e2e/testdata dir/main:e2e/testdata | git apply --directory=integrations/agntcy-dir/examples/dir/e2e/testdata
```

## Copyright Notice

[Copyright Notice and License](./LICENSE.md)

Distributed under Apache 2.0 License. See LICENSE for more information.
Copyright AGNTCY Contributors (https://github.com/agntcy)
