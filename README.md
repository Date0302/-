# README

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AWS-Serverless-orange?logo=amazon-aws&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Last_Commit-Aug_2026-green" alt="Last Commit">
</p>

#### 🌐 Language / 言語 / 语言

&nbsp;&nbsp;🇺🇸 English: [README.md](README.md)                     &nbsp;&nbsp;🇯🇵 日本語: [README.ja.md](README.ja.md)                        &nbsp;&nbsp;🇨🇳 中文: [README.zh-CN.md](README.zh-CN.md)

## 📊 Portfolio Overview

| Metric | Value |
|:----:|:----:|
| 🏗️ **Production-grade AWS Projects** | **3** |
| 🧩 **AWS Services Used** | **15+** |
| 📐 **Architecture Design Docs** | **10+** |
| ⚡ **Serverless Lambda Functions** | **8** |
| 🤖 **Core Focus** | **AI + Cloud + Security** |
| 🔄 **CI/CD Ready** | ✅ |
| 🌐 **Multilingual Documentation** | **English / 中文 / 日本語** |
| 🔒 **Least Privilege IAM Design** | ✅ |

## 🎯 Why This Repository?

This repository showcases practical cloud engineering capabilities — not just source code.

☁️Each AWS project includes:

| ✓ Architecture Diagrams | ✓ IAM Policies | ✓ Deployment Guides |
|:-----------:|:----------:|:---------:|
| ✓ Monitoring Config | ✓ Security Design | ✓ Sample Data |
| ✓ Project Management Plan | ✓ Multilingual Docs | ✓ Troubleshooting Guide |

## 🏆 Featured Projects

### ☁️ AWS Cloud Projects

#### 1. Cost-Aware GenAI Document Assistant

> **Intelligent cost-optimized serverless RAG system — balancing accuracy and cost**

**Architecture Flow**
```
S3 Upload → SQS → Lambda (Document Processor)
                    ↓
            Embedding Generator → Vector Store
                    ↓
Query Router (Vector Search / Direct LLM) → Bedrock → Response
```

**AWS Services**: Lambda · S3 · SQS · Bedrock · IAM · CloudWatch

**Key Highlights**
- 🧠 Cost-aware query routing, intelligently choosing between vector search or direct LLM calls
- ⚡ 4 Lambda functions working together, asynchronous pipeline design
- 🔒 Complete least-privilege IAM architecture

➡️ **[Learn More →](./AWS%20Project/Cost-Aware%20GenAI%20Document%20Assistant/README.CN.md)**

#### 2. Serverless Image Processing System

> **Auto-scaling image upload and processing pipeline — zero server operations**

**Architecture Flow**
```
Cognito User → Lambda (Generate Upload URL) → S3 Presigned URL
                                              ↓
                                        S3 Upload Event
                                              ↓
                                      SQS → Lambda (Image Processor)
                                              ↓
                                    DynamoDB (Metadata) + SNS (Notification)
```

**AWS Services**: Lambda · S3 · SQS · Cognito · DynamoDB · SNS · CloudWatch

**Key Highlights**
- 🔐 Secure presigned URL uploads based on Cognito authentication
- 📦 Original/processed images stored separately, isolated by user directories
- 📊 Custom S3 storage metrics, integrated with CloudWatch dashboards

➡️ **[Learn More →](./AWS%20Project/Images%20Processing%20Project/README.CN.md)**

#### 3. Security Incident Automation & Compliance Audit Platform

> **AWS centralized security log analysis — automated detection & audit-ready**

**Architecture Flow**
```
CloudTrail → S3 (KMS Encrypted)
                ↓
        EventBridge Rules → Lambda → Step Functions (Incident Response)
                ↓
            Athena (Ad-hoc Queries) → QuickSight (Dashboards)
```

**AWS Services**: CloudTrail · S3 · KMS · EventBridge · Lambda · Step Functions · Athena · QuickSight · IAM

**Key Highlights**
- 🛡️ End-to-end KMS encryption + least-privilege IAM
- 🔄 Automated incident detection + Step Functions response workflow
- 📈 Compliance-ready architecture with Athena audit queries

➡️ **[Learn More →](./AWS%20Project/Security%20Incident%20Automation%20%26%20Compliance%20Audit%20Platform%20Project/README.CN.md)**

## 🖼️ Architecture Gallery

<table>
<tr>
<td align="center">
<b>Image Processing System</b><br>
<img src="assets/image-processing.png" width="320">
</td>
<td align="center">
<b>Security Audit Platform</b><br>
<img src="assets/security-platform.png" width="320">
</td>
<td align="center">
<b>GenAI Document Assistant</b><br>
<img src="assets/genai.png" width="320">
</td>
</tr>
</table>

## 🐍 Algorithms & Data Science

| Project | Description | Tech Points |
|:----:|:----:|:------:|
| A\* Pathfinding | Classic heuristic search algorithm | Heuristic search, path optimization |
| K-Means Clustering | Unsupervised ML clustering | Centroid clustering, unsupervised learning |
| Fuzzy Inference System | Fuzzy logic inference engine | Membership functions, rule-based reasoning |
| VGG-16 | CNN image classification model | Deep learning, transfer learning |
| Web Crawler | Web data scraping and extraction | HTTP requests, HTML parsing |

## 🛠️ Tech Stack

| Category | Technologies |
|------|------|
| **☁️ Cloud Computing** | AWS Lambda, S3, SQS, SNS, Cognito, DynamoDB, CloudTrail, Athena, QuickSight, EventBridge, Step Functions, Bedrock, KMS, IAM, CloudWatch |
| **🐍 Programming Languages** | Python, Java, C++, SQL |
| **🏗️ Infrastructure** | Serverless architecture, IAM policies, CI/CD (GitHub Actions) |
| **🤖 Machine Learning / AI** | RAG, vector embeddings, K-Means, fuzzy logic, CNN (VGG-16), A* algorithm |
| **🔧 Tools** | Git, Draw.io, Pillow, Boto3 |

## 🗺️ Roadmap

Future plans:

Terraform / AWS CDK — Infrastructure as Code for all projects
Amazon EKS — Kubernetes container orchestration
Multi-Account Landing Zone — Enterprise-grade AWS Organization architecture
CI/CD Enhancement — Complete automated testing and deployment pipeline
AI Agent — Autonomous AI agent with tool-calling capabilities
Observability Suite — X-Ray + CloudWatch unified monitoring**

## 📁 Project Structure

```
my-projects-lab/
├── AWS Project/
│   ├── Cost-Aware GenAI Document Assistant/   # Cost-aware RAG system
│   ├── Images Processing Project/             # Serverless image processing pipeline
│   └── Security Incident Automation &         # Security log analysis & compliance audit
│       Compliance Audit Platform Project/
├── Python code/                               # Algorithms, machine learning, tools
├── Java code/                                 # Java applications and examples
├── C++ code/                                  # Systems programming projects
├── LICENSE
├── SECURITY.md
└── README.md
```

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Date0302/my-projects-lab.git

# Navigate to the project directory
cd my-projects-lab/AWS\ Project/Images\ Processing\ Project/

# Follow the project README for deployment
```

Each AWS project includes complete deployment guides, architecture diagrams, and IAM policy templates — deployable directly to your own AWS account.

## 📬 Contact

Feel free to reach out about cloud architecture, security, and AI opportunities.
- 📧 **Email**: LQHJFCQY@gmail.com
- 🔗 **GitHub**: [Date0302](https://github.com/Date0302)

Issues and Pull Requests are welcome! 🙌

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
