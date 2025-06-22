# Cloud DevOps Engineer Lab – Management & Governance

## Lab Title:
**Automating LAMP Stack Deployment using AWS CloudFormation**

---

## 🧪 Lab Overview:
In this lab, you'll learn how to automate the deployment of a LAMP (Linux, Apache, MySQL, PHP) stack using AWS CloudFormation. You'll use a template stored in an S3 bucket to launch and configure resources with minimal manual steps.

---

## 📌 Region:
US East (N. Virginia) – `us-east-1`

---

## 🔹 Task 1: Exploring Templates in an S3 Bucket

1. Go to **S3** under the **Storage** section in AWS Console.
2. Find a bucket named similar to `whizlabs.1400.54051021`.
3. Open the bucket and locate the file: `LAMP_template.json`.
4. Copy the **Object URL** of the file and save it temporarily (you’ll need it for CloudFormation).

---

## 🔹 Task 2: Create CloudFormation Stack

1. Go to **CloudFormation** under **Management and Governance**.
2. Click on **Create Stack**.
3. Choose: `With new resources (standard)`
4. Select **Amazon S3 URL** and paste the Object URL of `LAMP_template.json`.

### Stack Details:
- **Stack name**: `MyFirstCFStack`

### Parameters:
- **DB Name**: `MyDatabase`
- **DB Password**: `whizlabsdb123`
- **DB Root Password**: `whizlabsdbroot123`
- **DB User**: `WhizlabsDBUser`
- **Instance Type**: `t2.micro`
- **Key Name**: Select `whizlabs-key` from the list
- **SSH Location**: `0.0.0.0/0`

Click **Next**.

---

## 🔹 Task 3: Configure Stack Options

- Add Tag:
  - **Key**: `Name`
  - **Value**: `MyCF`

Leave other options at default. Click **Next**, then **Submit** to create the stack.

Check the **Status** as `CREATE_IN_PROGRESS` and wait until it changes to `CREATE_COMPLETE`.

---

## 🔹 Task 4: Testing

1. Go to the **Outputs** tab of the stack.
2. Copy the output URL (e.g., `http://ec2-18-212-56-170.compute-1.amazonaws.com/`)
3. Open it in a browser.

✅ If you see a PHP info page with DB connection success, the CloudFormation deployment worked!

---

## ✅ Conclusion

This lab demonstrates how AWS CloudFormation can automate infrastructure provisioning, increasing reliability and reducing manual effort. It's a best practice for DevOps workflows and production-ready deployments.