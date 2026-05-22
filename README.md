# Self Healing AWS Platform CI/CD Observability Kubernetes Automated Remediation (WIP)

# What it is

# Architecture diagram

# How to run it

# Project status 

## Phase 1

## Phase 1 - Core Cloud Platform

| Area | What I Am Building | Tools / Services | Purpose | Completion Evidence | Completed/ Progression/ On-Hold | Expected Conpleted date |  
|---|---|---|---|---|---|---|
| Application | Simple containerised web/API application with `/`, `/health`, and `/version` endpoints | Django, Docker | test | test | Progression | 25/05/2026 | 
| Containerisation | Docker image for the application | Docker, Dockerfile | Packages the app consistently for local and AWS deployment | Docker image builds successfully and runs locally |
| Source Control | GitHub repository with clean project structure | GitHub | Stores app code, Terraform, workflows, and documentation | Repo contains `app/`, `terraform/`, `.github/workflows/`, and `docs/` |
| CI Pipeline | Automated test and build workflow | GitHub Actions | Validates app code before deployment | Workflow passes on push or pull request |
| AWS Authentication | Secure GitHub Actions access to AWS | GitHub Actions OIDC, AWS IAM Role | Avoids long-lived AWS access keys in GitHub secrets | GitHub Actions successfully assumes AWS role |
| Container Registry | Store application Docker images | Amazon ECR | Holds versioned images for deployment to ECS | Image pushed to ECR with Git SHA tag |
| Networking | Production-style AWS network foundation | VPC, public subnets, private subnets, route tables, Internet Gateway | Creates isolated networking for the platform | VPC and subnets created successfully with Terraform |
| Load Balancing | Public entry point for the application | Application Load Balancer, Target Group | Routes user traffic to healthy ECS tasks | ALB DNS loads the application successfully |
| Compute Platform | Run the containerised app | ECS Fargate | Hosts the app without managing EC2 servers | ECS service is running desired task count |
| IAM | Required permissions for ECS and deployments | IAM roles, IAM policies | Allows ECS tasks and GitHub Actions to operate securely | IAM roles created with scoped permissions |
| Logging | Capture application logs | CloudWatch Logs | Provides basic operational visibility | App logs appear in CloudWatch log group |
| Terraform | Provision AWS infrastructure as code | Terraform modules and environment folders | Makes infrastructure repeatable and version controlled | `terraform plan` and `terraform apply` complete successfully |
| Deployment | Deploy app image to AWS | GitHub Actions, ECR, ECS Fargate | Automates app delivery into AWS | New image version deployed to ECS |
| Health Checks | Verify app availability | ALB health checks, `/health` endpoint | Confirms the service is running correctly | ALB target group shows healthy targets |
| Documentation | Explain how the platform works | README, architecture docs, screenshots | Makes the project understandable to recruiters and engineers | README includes architecture, build steps, and proof screenshots |

## Phase 2

## Phase 3

## Phase 4

## Phase 5

## Phase 6

# Project documentation is highly likely to grow with the project overall. So the below are just notes at this stage, till I have figured out the next parts I will be amending to my project.

## 1. Project Overview
### 1.1 Problem Statement
### 1.2 Solution Summary
### 1.3 Business Value
### 1.4 Key Features

## 2. Architecture Overview
### 2.1 High-Level Architecture
### 2.2 AWS Cost Data Flow
### 2.3 CI/CD Flow
### 2.4 Observability Flow
### 2.5 Alerting and Remediation Flow

## 3. Implementation Approach & Reusability
### 3.1 How the Solution is Built
### 3.2 Infrastructure as Code Design
### 3.3 CI/CD Pipeline Design
### 3.4 Data Flow & Query Execution
### 3.5 Reusable Components
### 3.6 Environment Strategy

## 4. Observability and Dashboard Design
### 4.1 Dashboard Design Principles
### 4.2 AWS Cost Overview Dashboard
### 4.3 AWS Service Cost Analysis Dashboard
### 4.4 Environment Cost Analysis Dashboard
### 4.5 CloudWatch Cost Analysis Dashboard
### 4.6 Platform Health Dashboard
### 4.7 Incident and Remediation Dashboard
### 4.8 Stakeholder Views

## 5. Operational Model
### 5.1 How This Will Be Maintained
### 5.2 Alert Handling Process
### 5.3 Incident Scenarios
### 5.4 Automated Remediation
### 5.5 Runbooks
### 5.6 Handover
### 5.7 Troubleshooting

## 6. Why Grafana Over AWS Cost Explorer
### 6.1 Key Advantages of Grafana
### 6.2 Technical Advantages
### 6.3 Cost Optimisation Value
### 6.4 Scalability and Future Value

## 7. Security Controls
### 7.1 IAM and Least Privilege
### 7.2 GitHub Actions OIDC
### 7.3 Secrets Management
### 7.4 AWS Config and Compliance
### 7.5 Image and Infrastructure Scanning

## 8. Cost Optimisation
### 8.1 Cost Visibility
### 8.2 CloudWatch Cost Analysis
### 8.3 Environment-Based Cost Tracking
### 8.4 Cost Alerts and Anomaly Detection
### 8.5 Future Cost Improvements

## 9. Lessons Learned

## 10. Future Improvements

## 11. Screenshots and Demo

## 12. Repository Structure
