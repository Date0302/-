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

## 📊 作品集速览

| 指标 | 数值 |
|:----:|:----:|
| 🏗️ **生产级 AWS 项目** | **3 个** |
| 🧩 **使用的 AWS 服务** | **15+** |
| 📐 **架构设计文档** | **10+** |
| ⚡ **无服务器 Lambda 函数** | **8 个** |
| 🤖 **核心方向** | **AI + 云 + 安全** |
| 🔄 **CI/CD 就绪** | ✅ |
| 🌐 **多语言文档** | **英文 / 中文 / 日本語** |
| 🔒 **最小权限 IAM 设计** | ✅ |

## 🎯 为什么创建这个仓库？

本仓库旨在展示**实战云工程能力** — 而不仅仅是源代码。

☁️每个 AWS 项目都包含：

| ✓ 架构设计图 | ✓ IAM 策略 | ✓ 部署指南 |
|-------------|------------|-----------|
| ✓ 监控配置 | ✓ 安全设计 | ✓ 示例数据 |
| ✓ 项目管理计划 | ✓ 多语言文档 | ✓ 故障排查指南 |

## 🏆 精选项目

### ☁️ AWS 云项目

#### 1. 成本感知型 GenAI 文档助手
> **智能成本优化的无服务器 RAG 系统 — 在准确性和成本之间取得平衡**

**架构流程**

```
S3 上传 → SQS → Lambda（文档处理器）
                    ↓
            嵌入生成器 → 向量存储
                    ↓
查询路由器（向量搜索 / 直接 LLM）→ Bedrock → 响应
```

**AWS 服务**：Lambda · S3 · SQS · Bedrock · IAM · CloudWatch

**核心亮点**
- 🧠 成本感知查询路由，智能选择向量搜索或直接 LLM 调用
- ⚡ 4 个 Lambda 函数协同，异步流水线设计
- 🔒 完整的最小权限 IAM 架构

➡️ **[了解更多 →](./AWS%20Project/Cost-Aware%20GenAI%20Document%20Assistant/README.CN.md)**

#### 2. 无服务器图像处理系统
> **自动伸缩的图片上传与处理流水线 — 零服务器运维**

**架构流程**
```
Cognito 用户 → Lambda（生成上传 URL）→ S3 预签名 URL
                                              ↓
                                        S3 上传事件
                                              ↓
                                      SQS → Lambda（图像处理器）
                                              ↓
                                    DynamoDB（元数据）+ SNS（通知）
```

**AWS 服务**：Lambda · S3 · SQS · Cognito · DynamoDB · SNS · CloudWatch

**核心亮点**
- 🔐 基于 Cognito 认证的安全预签名 URL 上传
- 📦 原图/处理图分离存储，按用户目录隔离
- 📊 自定义 S3 存储指标，对接 CloudWatch 仪表盘

➡️ **[了解更多 →](./AWS%20Project/Images%20Processing%20Project/README.CN.md)**

#### 3. 安全事件自动化与合规审计平台
> **AWS 集中式安全日志分析 — 自动检测 & 审计就绪**

**架构流程**

```
CloudTrail → S3（KMS 加密）
                ↓
        EventBridge 规则 → Lambda → Step Functions（事件响应）
                ↓
            Athena（即席查询）→ QuickSight（仪表盘）
```

**AWS 服务**：CloudTrail · S3 · KMS · EventBridge · Lambda · Step Functions · Athena · QuickSight · IAM

**核心亮点**
- 🛡️ 端到端 KMS 加密 + 最小权限 IAM
- 🔄 自动事件检测 + Step Functions 响应工作流
- 📈 合规就绪架构，支持 Athena 审计查询

➡️ **[了解更多 →](./AWS%20Project/Security%20Incident%20Automation%20%26%20Compliance%20Audit%20Platform%20Project/README.CN.md)**

## 🖼️ 架构图一览

| 图像处理系统 | 安全审计平台 | GenAI 文档助手 |
|-------------|-------------|---------------|
| ![Image Processing Architecture Project Architecture Diagram.drawio](../../../AWS项目/AWS Project/my-projects-lab-main6月/my-projects-lab-main/AWS Project/Images Processing Project/Achitecture/Image Processing Architecture Project Architecture Diagram.drawio.png) | !![Security Incident Automation & Compliance Audit Platform Project Architecture Images.drawio](../../../AWS项目/AWS Project/my-projects-lab-main6月/my-projects-lab-main/AWS Project/Security Incident Automation & Compliance Audit Platform Project/Achitecture/Security Incident Automation & Compliance Audit Platform Project Architecture Images.drawio.png) | ![Cost-Aware GenAI Document Assistant.drawio](../../../AWS项目/AWS Project/my-projects-lab-main6月/my-projects-lab-main/AWS Project/Cost-Aware GenAI Document Assistant/Achitecture/Cost-Aware GenAI Document Assistant.drawio.png) |

## 🐍 算法与数据科学

| 项目 | 描述 | 技术点 |
|:----:|:----:|:------:|
| A\* 路径规划 | 经典启发式搜索算法 | 启发式搜索、路径优化 |
| K-Means 聚类 | 无监督机器学习聚类 | 质心聚类、无监督学习 |
| 模糊推理系统 | 模糊逻辑推理引擎 | 隶属度函数、规则推理 |
| VGG-16 | CNN 图像分类模型 | 深度学习、迁移学习 |
| 网络爬虫 | 网页数据抓取与提取 | HTTP 请求、HTML 解析 |

## 🛠️ 技术栈

| 分类 | 技术 |
|------|------|
| **☁️ 云计算** | AWS Lambda, S3, SQS, SNS, Cognito, DynamoDB, CloudTrail, Athena, QuickSight, EventBridge, Step Functions, Bedrock, KMS, IAM, CloudWatch |
| **🐍 编程语言** | Python, Java, C++, SQL |
| **🏗️ 基础设施** | 无服务器架构、IAM 策略、CI/CD（GitHub Actions） |
| **🤖 机器学习 / AI** | RAG、向量嵌入、K-Means、模糊逻辑、CNN（VGG-16）、A* 算法 |
| **🔧 工具** | Git、Draw.io、Pillow、Boto3 |

## 🗺️ 路线图

未来规划：

**Terraform / AWS CDK** — 所有项目基础设施即代码化

**Amazon EKS** — Kubernetes 容器编排

**多账号 Landing Zone** — 企业级 AWS 组织架构

**CI/CD 增强** — 完整自动化测试与部署流水线

**AI Agent** — 具备工具调用能力的自主 AI 代理

**可观测性套件** — X-Ray + CloudWatch 统一监控

## 📁 项目结构

```
my-projects-lab/
├── AWS Project/
│   ├── Cost-Aware GenAI Document Assistant/   # 成本感知 RAG 系统
│   ├── Images Processing Project/             # 无服务器图像处理流水线
│   └── Security Incident Automation &         # 安全日志分析与合规审计
│       Compliance Audit Platform Project/
├── Python code/                               # 算法、机器学习、工具
├── Java code/                                 # Java 应用与示例
├── C++ code/                                  # 系统编程项目
├── LICENSE
├── SECURITY.md
└── README.md
```

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/Date0302/my-projects-lab.git

# 进入项目目录
cd my-projects-lab/AWS\ Project/Images\ Processing\ Project/

# 按照项目 README 进行部署
```

每个 AWS 项目都包含完整的部署指南、架构图和 IAM 策略模板 — 可直接部署到你自己的 AWS 账户。

## 📬 联系方式

欢迎交流云架构、安全和 AI 相关的机会。

- 📧 **邮箱**：LQHJFCQY@gmail.com
- 🔗 **GitHub**：[Date0302](https://github.com/Date0302)

欢迎提交 Issue 或 Pull Request！🙌

## 📄 许可证

本项目使用 **MIT License** 开源协议，详情见 [LICENSE](LICENSE) 文件。
