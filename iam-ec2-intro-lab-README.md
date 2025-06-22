
# 🛡️ AWS Lab: Introduction to IAM and EC2

## 🎯 Objective

Gain hands-on experience with Identity and Access Management (IAM) by creating users, groups, and attaching policies. Learn how to provision an EC2 instance and configure access using key pairs and security groups.

---

## 🧪 Lab Tasks

### 🔹 Task 1: Create IAM Users and Groups

#### 👥 IAM Users
- Navigate to **IAM > Users > Add users**
- Create users:
  - `John`, `Sarah` for Dev Team
  - `Ted`, `Rita` for HR Team

#### 🧑‍🤝‍🧑 IAM Groups
- Navigate to **IAM > User groups > Create group**
- Create two groups:
  - `DevTeam` → Attach `AmazonEC2FullAccess`
  - `HRTeam` → Attach `AmazonS3ReadOnlyAccess`
- Add users to respective groups

---

### 🔹 Task 2: Launch EC2 Instance

1. Go to **EC2 > Instances > Launch Instances**
2. Instance details:
   - **Name**: `MyIAMTestEC2`
   - **AMI**: Amazon Linux 2
   - **Type**: t2.micro (Free tier)
   - **Key pair**: Create a new one, e.g., `IAMKeyPair.pem`
   - **Network settings**:
     - Create new security group
     - Allow **SSH (port 22)** and **HTTP (port 80)** from Anywhere
3. Launch the instance

---

### 🔹 Task 3: Connect to EC2 Instance

- Navigate to **Instances > Select instance > Connect**
- Choose **EC2 Instance Connect (browser-based)**
- Confirm connection with user `ec2-user`

---

## ✅ Final Outcome

| Resource      | Name            | Configuration                      |
|---------------|------------------|------------------------------------|
| IAM Users     | John, Sarah      | Dev Team                           |
| IAM Users     | Ted, Rita        | HR Team                            |
| IAM Groups    | DevTeam, HRTeam  | EC2 Full / S3 Read-only policies   |
| EC2 Instance  | MyIAMTestEC2     | Amazon Linux 2, SSH & HTTP allowed |

---

## 🧠 Skills Gained

- IAM user/group creation
- IAM policy attachment and permission control
- EC2 provisioning and access setup
- Key pair generation and usage
- Network and security group configuration

---
