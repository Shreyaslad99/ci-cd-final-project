# Evidence checklist — capture from your own account and cluster

- [ ] Public GitHub URL to `README.md` with project name and details.
- [ ] Public GitHub URL to `.github/workflows/workflow.yml`; show the complete flake8 and nose steps.
- [ ] Public GitHub URL to `.tekton/tasks.yml`; show both `cleanup` and `nose` task definitions.
- [ ] Full GitHub Actions job log copied from an actual successful run. Include setup, checkout, container initialization, dependency install, lint, tests, post-action steps, and job completion where present.
- [ ] Screenshot `oc-pipelines-console-pvc-details.png` from the OpenShift console showing StorageClass `skills-network-learner` and requested capacity `1Gi` / `1GB`.
- [ ] Screenshot `oc-pipelines-oc-final.png` showing cleanup, git-clone, flake8, nose, buildah, and deploy / openshift-client.
- [ ] Screenshot `oc-pipelines-oc-green.png` from an actual successful run of the complete pipeline.
- [ ] Application logs from the deployed pod showing the exact `SERVICERUNNING` message and listener on port `8000`.

**Do not invent logs or fabricate screenshots.** Save screenshots from the actual GitHub Actions / OpenShift interfaces. Screenshot filenames alone do not prove the criteria were met.
