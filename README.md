# Self Healing AWS Platform CI/CD Observability Kubernetes Automated Remediation (WIP)

# What it is

# Architecture diagram

# How to run it

# Project status 

## Phase 1 - Core Cloud Platform

## Phase 1 - Core Cloud Platform Progress Tracker

| Area | What I Am Building | Tools / Services | Purpose | Completion Evidence | Status | Expected Completion Date |
|---|---|---|---|---|---|---|
| Application | Simple containerised web/API application with `/`, `/health`, and `/version` endpoints | Django, Docker | Provides a real application to deploy, test, monitor, and later use for failure scenarios | App runs locally and endpoints return expected responses | Completed | 25/05/2026 |
| Containerisation | Docker image for the application | Docker, Dockerfile | Packages the application so it can run consistently locally and in AWS | Docker image builds successfully and runs locally | On Hold | TBD |
| Source Control | GitHub repository with clean project structure | GitHub | Stores application code, Terraform, CI/CD workflows, and documentation in one structured repo | Repo contains `app/`, `terraform/`, `.github/workflows/`, and `docs/` folders | On Hold | TBD |
| CI Pipeline | Automated test and build workflow | GitHub Actions | Validates application code before deployment | GitHub Actions workflow runs successfully on push or pull request | On Hold | TBD |
| AWS Authentication | Secure GitHub Actions access to AWS | GitHub Actions OIDC, AWS IAM Role | Allows GitHub Actions to deploy to AWS without long-lived access keys | GitHub Actions successfully assumes AWS IAM role | On Hold | TBD |
| Container Registry | Store application Docker images | Amazon ECR | Stores versioned Docker images for ECS deployment | Docker image is pushed to ECR with a Git SHA tag | On Hold | TBD |
| Networking | Production-style AWS network foundation | VPC, public subnets, private subnets, route tables, Internet Gateway | Provides secure network isolation for the application platform | VPC, subnets, route tables, and internet gateway created through Terraform | On Hold | TBD |
| Load Balancing | Public entry point for the application | Application Load Balancer, Target Group | Routes public traffic to healthy application containers | ALB DNS loads the application and target group shows healthy targets | On Hold | TBD |
| Compute Platform | Run the containerised app | ECS Fargate | Runs the application without managing EC2 servers | ECS service is running with the desired task count | On Hold | TBD |
| IAM | Required permissions for ECS and deployments | IAM roles, IAM policies | Provides secure permissions for ECS tasks, deployments, and GitHub Actions | IAM roles and policies are created with scoped permissions | On Hold | TBD |
| Logging | Capture application logs | CloudWatch Logs | Provides basic visibility into application behaviour and requests | Application logs appear in the CloudWatch log group | On Hold | TBD |
| Terraform | Provision AWS infrastructure as code | Terraform modules and environment folders | Makes the AWS infrastructure repeatable, version-controlled, and reusable | `terraform plan` and `terraform apply` complete successfully | On Hold | TBD |
| Deployment | Deploy app image to AWS | GitHub Actions, ECR, ECS Fargate | Automates delivery of the application into AWS | New image version is deployed to ECS successfully | On Hold | TBD |
| Health Checks | Verify app availability | ALB health checks, `/health` endpoint | Confirms the application is running correctly after deployment | `/health` endpoint returns healthy and ALB target group is healthy | On Hold | TBD |
| Documentation | Explain how the platform works | README, architecture docs, screenshots | Makes the project understandable to recruiters, engineers, and future maintainers | README includes architecture, build steps, screenshots, and deployment evidence | On Hold | TBD |

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
