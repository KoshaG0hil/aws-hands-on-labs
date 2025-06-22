
# CloudFormation LAMP Stack Lab

## Overview

In this lab, you'll use AWS CloudFormation to provision a LAMP server stack using a predefined JSON template stored in Amazon S3.

---

## Step-by-Step Instructions

### 1. Explore Templates in S3

- Go to **S3** under the **Storage** section.
- Open the available bucket.
- Locate the file named `LAMP_template.json`.
- Copy the **Object URL** of this file and save it for later use.

---

### 2. Create a CloudFormation Stack

- Navigate to **CloudFormation** under the **Management & Governance** section.
- Click **Create Stack** and choose **With new resources (standard)**.
- Under **Specify template**:
  - **Template source**: Select **Amazon S3 URL**
  - **Amazon S3 URL**: Paste the URL copied earlier.

Click **Next**.

#### Stack Details

- **Stack name**: `MyFirstCFStack`

**Parameters**:
- **DB Name**: `MyDatabase`
- **DB Password**: `dbpassword123`
- **DB Root Password**: `dbroot123`
- **DB User**: `DBUser`
- **Instance Type**: `t2.micro`
- **Key Name**: Select your SSH key pair
- **SSH Location**: `0.0.0.0/0`

Click **Next**.

#### Stack Options

- **Tags**:
  - **Key**: `Name`
  - **Value**: `MyCF`
- Leave other options as default.
- Click **Next**.

#### Review and Create

- Review the stack details.
- Click **Create Stack**.

Wait for the stack creation to complete (`CREATE_COMPLETE` status).

---

### 3. Test the Deployment

- Go to the **Outputs** tab of the created stack.
- Click the **URL** provided to access the server homepage.
- If the page shows PHP info and a successful DB connection, your LAMP stack was created successfully.

---

## Summary

This lab demonstrated how to:
- Launch a LAMP stack using CloudFormation.
- Configure parameters in a stack template.
- Deploy infrastructure as code using S3 and CloudFormation.
