# ☁️ AWS Hands-On Labs & Production Blueprint Collection

[![CI](https://github.com/KoshaG0hil/aws-hands-on-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/KoshaG0hil/aws-hands-on-labs/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CloudFormation](https://img.shields.io/badge/IaC-AWS%20CloudFormation-FF9900.svg)](#)

A practical collection of hands-on AWS infrastructure labs covering **Identity & Access Management (IAM)**, **Elastic Compute Cloud (EC2)**, **Virtual Private Clouds (VPC)**, and **Infrastructure as Code (CloudFormation)**. Designed for cloud engineers, solution architects, and certification candidates seeking step-by-step verified architectures.

---

## 📚 Labs Included

| Lab Title | Core AWS Services | Focus Area | Detailed Guide |
|-----------|-------------------|------------|----------------|
| **1. IAM Least-Privilege & EC2 Role Attachment** | IAM, EC2, CloudWatch | Identity Governance & Credential-free Compute | [View Guide](iam-ec2-intro-lab-README.md) |
| **2. Multi-Tier Custom VPC & Subnet Design** | VPC, Subnets, IGW, Route Tables | Network Isolation & Routing | [View Guide](vpc-custom-subnet-lab-README.md) |
| **3. Automated Full-Stack LAMP Infrastructure** | CloudFormation, EC2, RDS (MySQL), ALB | Automated IaC Provisioning | [View Guide](Clean_CloudFormation_LAMP_Lab_README.md) |

---

## 🚀 Quickstart & Validation

### Prerequisites

- Python 3.11+
- AWS CLI configured (optional for local audit)

### Local Validation Suite

Verify CloudFormation templates and lab manifest completeness:

```bash
pip install -r requirements.txt
python cli.py
```

### Running Test Suite

```bash
pytest tests/ -v
```

---

## 🛠️ Deploying Lab 3: CloudFormation LAMP Stack

You can deploy the automated LAMP stack directly using the AWS CLI:

```bash
aws cloudformation create-stack \
  --stack-name lamp-production-stack \
  --template-body file://LAMP_template.json \
  --parameters ParameterKey=DBPassword,ParameterValue="SecurePass123!"
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
