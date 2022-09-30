# What is Terraform?

## Terraform is an open-source tool by [HashiCorp](https://www.hashicorp.com/) used for provisioning infrastructure resources.

## It is an example of IaC `Infrastructure as Code`. It is used to build, change and manage your infrastructure in a safe and consistent way. It is achieved by defining cloud resource configurations that you can version, reuse and share.

### Files:
- `main.tf`
- `variables.tf`
- Optional: `resources.tf` and `output.tf`
- `.tfstate`

## There are 4 declarations performed before running Terraform:
- `terraform`: Configure basic Terraform settings to provison your infrastructure.
    - `required_version`: The minimum Terrafrom version to apply your configurations.
    - `backend`: It stores Terraform's state snapshots to map resources to your configuration.
        - `local`: Stores state file locally as `terraform.tfstate`
    - `required_providers`: Specifies the providers required by the current module.

- `provider`:
    - Adds a set of resource types and/or data sources that Terraform can manage
    - The Terraform Registry is the main directory of publicly available providers from most major infrastructure platforms.

- `resource`: 
    - blocks to define components of your infrastructure
    - Project modules/resources: google_storage_bucket, google_bigquery_dataset, google_bigquery_table

- `variable & locals`
    - runtime arguments and constants

## Execution steps.
1. `terraform init`: Initializes and configures the backend, installs pliugins/providers and checks out an existing configuration from a version control.

2. `terraform plan`: Matches/previews local changes against a remote state, and proposes an execution plan.

3. `terraform apply`: Asks for approval to the proposed plan, and applies changes to cloud

4. `terraform destroy`: Removes your stack from the Cloud.


## References.
https://learn.hashicorp.com/collections/terraform/gcp-get-started