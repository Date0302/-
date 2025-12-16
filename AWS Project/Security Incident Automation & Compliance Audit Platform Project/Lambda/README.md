# Security Orchestration Lambda Function

This Lambda function serves as the central security orchestration layer in the AWS Security Automation Project. It receives security-related events from multiple AWS services, performs centralized logging, sends alerts, and triggers automated response workflows using AWS Step Functions.

## Supported Event Sources

This Lambda is triggered by Amazon EventBridge and supports the following security event types:

| Source Service   | Event Type                  | Description                                         |
| ---------------- | --------------------------- | --------------------------------------------------- |
| Amazon GuardDuty | GuardDuty Security Finding  | Unauthorized access, cryptocurrency mining activity |
| Amazon Inspector | Inspector2 Security Finding | Critical vulnerability discoveries                  |
| AWS CloudTrail   | AWS API Call via CloudTrail | Risky IAM policy changes                            |
| Amazon Macie     | Macie Security Finding      | Sensitive data exposure/public S3 access            |

## Core Responsibilities

### 1. Centralized Event Processing

- Identifies event sources and types
- Classifies security incidents

### 2. Security Event Logging

- Stores structured JSON logs in Amazon S3
- Supports downstream analysis via Athena and QuickSight

### 3. Security Alert Notification

- Sends real-time alerts for each processed event
- Alerts include event source, type, and processing results

------

### 4. Automated Response Orchestration

Based on the event type, the Lambda triggers dedicated AWS Step Functions state machines for further automated remediation.

| Incident Type              | Step Functions State Machine |
| -------------------------- | ---------------------------- |
| Unauthorized Access        | SFN-UnauthorizedAccess       |
| Cryptocurrency Mining      | SFN-CryptoMining             |
| Inspector Critical Finding | SFN-InspectorCritical        |
| IAM Policy Change          | SFN-IAMPolicyChange          |
| Macie Sensitive Data       | SFN-MacieSensitiveData       |

⚠ Remediation actions within Step Functions are **intentionally implemented as placeholders** to demonstrate architectural design rather than modify production environment resources.

## IAM Permissions

The Lambda execution role requires the following permissions:

- Amazon S3: `PutObject`
- Amazon SNS: `Publish`
- AWS Step Functions: `StartExecution`
- Amazon CloudWatch Logs: Basic logging permissions

## Design Notes

- This Lambda is designed as a single-entry security control point
- Emphasizes observability, auditability, and extensibility
- Separates detection, orchestration, and remediation logic
- Suitable for SOC-style security monitoring and analysis use cases

# 安全编排Lambda函数

该Lambda函数作为中央安全编排层，在AWS安全自动化项目中发挥核心作用。它接收来自多个AWS服务的安全相关事件，进行集中日志记录、发送警报，并使用AWS Step Functions触发自动化响应工作流。

## 支持的事件源

此Lambda由Amazon EventBridge触发，支持以下安全事件类型：

| 源服务           | 事件类型                    | 描述                             |
| ---------------- | --------------------------- | -------------------------------- |
| Amazon GuardDuty | GuardDuty安全发现           | 未经授权的访问、加密货币挖矿活动 |
| Amazon Inspector | Inspector2安全发现          | 严重漏洞发现                     |
| AWS CloudTrail   | 通过CloudTrail的AWS API调用 | 有风险的IAM策略变更              |
| Amazon Macie     | Macie安全发现               | 敏感数据暴露/公开S3访问          |

##  核心职责

### 1. 集中式事件处理

- 识别事件源和类型
- 对安全事件进行分类

### 2.安全事件日志记录

- 在Amazon S3中存储结构化的JSON日志
- 支持通过Athena和QuickSight进行下游分析

### 3.安全警报通知

- 为每个处理的事件发送实时警报
- 警报包含事件源、类型和处理结果

------

### 4.自动化响应编排

根据事件类型，Lambda会触发专用的AWS Step Functions状态机以进行进一步的自动化修复。

| 事件类型          | Step Functions状态机   |
| ----------------- | ---------------------- |
| 未经授权的访问    | SFN-UnauthorizedAccess |
| 加密货币挖矿      | SFN-CryptoMining       |
| Inspector严重发现 | SFN-InspectorCritical  |
| IAM策略变更       | SFN-IAMPolicyChange    |
| Macie敏感数据     | SFN-MacieSensitiveData |

⚠Step Functions内部的修复操作**有意实现为占位符**，旨在演示架构设计，而非修改生产环境资源。



##  IAM权限

Lambda执行角色需要以下权限：

Amazon S3: `PutObject`

Amazon SNS: `Publish`

AWS Step Functions: `StartExecution`

Amazon CloudWatch Logs: 基本日志记录权限

## 设计说明

此Lambda设计为单一入口安全控制点

强调可观测性、可审计性和可扩展性

分离检测、编排和修复逻辑

适用于SOC风格的安全监控和分析用例

