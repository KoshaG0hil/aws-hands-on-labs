
# 🚀 AWS Lab: Custom VPC with Public & Private Subnets

## 🧩 Objective

Create a custom Virtual Private Cloud (VPC) from scratch with:
- A public subnet in `us-east-1a`
- A private subnet in `us-east-1b`
- Internet Gateway for outbound internet access
- Separate route tables for public and private traffic flow

---

## 🔧 Lab Steps

### 🔹 1. Create a New VPC
- Navigate to: **VPC > Your VPCs > Create VPC**
- Choose: **VPC only**
- Set the following:
  - **Name tag**: `MyVPC`
  - **IPv4 CIDR block**: `10.0.0.0/16`
  - **IPv6 CIDR block**: None
  - **Tenancy**: Default
- Click **Create VPC**

---

### 🔹 2. Create Subnets

#### 🟢 Public Subnet
- Navigate to: **Subnets > Create subnet**
- Choose VPC: `MyVPC`
- **Subnet Name**: `MyPublicSubnet`
- **Availability Zone**: `us-east-1a`
- **CIDR block**: `10.0.1.0/24`
- Click **Create subnet**

#### 🔒 Private Subnet
- Create another subnet:
- **Subnet Name**: `MyPrivateSubnet`
- **Availability Zone**: `us-east-1b`
- **CIDR block**: `10.0.2.0/24`
- Click **Create subnet**

---

### 🔹 3. Create and Attach Internet Gateway
- Go to **Internet Gateways > Create internet gateway**
- Name: `MyInternetGateway`
- Click **Create**
- Select it → Click **Actions > Attach to VPC**
- Choose `MyVPC` → Click **Attach**

---

### 🔹 4. Create Route Tables

#### 🌐 Public Route Table
- Go to: **Route Tables > Create route table**
- Name: `PublicRouteTable`
- VPC: `MyVPC`
- Click **Create**

#### 🔐 Private Route Table
- Repeat steps above
- Name: `PrivateRouteTable`
- VPC: `MyVPC`
- Click **Create**

---

### 🔹 5. Associate Subnets to Route Tables

#### ➕ Public Subnet Association
- Select `PublicRouteTable`
- Go to **Subnet Associations > Edit subnet associations**
- Select `MyPublicSubnet` → Save

#### ➕ Private Subnet Association
- Select `PrivateRouteTable`
- Go to **Subnet Associations > Edit subnet associations**
- Select `MyPrivateSubnet` → Save

⚠️ Do not associate anything with the default (main) route table.

---

### 🔹 6. Add Internet Route to Public Route Table
- Go to `PublicRouteTable > Routes > Edit routes`
- Click **Add route**
  - **Destination**: `0.0.0.0/0`
  - **Target**: `MyInternetGateway`
- Click **Save changes**

---

## ✅ Final Outcome

| Resource Type     | Name              | Details                       |
|-------------------|-------------------|-------------------------------|
| VPC               | `MyVPC`           | `10.0.0.0/16`                 |
| Public Subnet     | `MyPublicSubnet`  | `10.0.1.0/24` – AZ: us-east-1a |
| Private Subnet    | `MyPrivateSubnet` | `10.0.2.0/24` – AZ: us-east-1b |
| Internet Gateway  | `MyInternetGateway` | Attached to VPC             |
| Public Route Table| `PublicRouteTable`| Internet route configured     |
| Private Route Table| `PrivateRouteTable`| Internal-only routing       |

---

## 🧠 Skills Gained

- Custom VPC design
- Subnet creation and CIDR allocation
- Internet Gateway setup
- Route table configuration
- Network segmentation in AWS

---

## 📸 Optional: Screenshots

You can upload screenshots under an `images/` folder and embed them like:

```markdown
![VPC Screenshot](./images/vpc-created.png)
```
