# Setup

## 1.Prerequisites

AWS Account (ap-northeast-1)
AWS CLI configured with sufficient permissions
Basic knowledge of:
AWS Lambda
IAM
Amazon EventBridge
AWS Step Functions
Amazon SNS
Amazon Athena
Amazon QuickSight

## 2. Create S3 Log Bucket

### Step 1: Create S3 Log Bucket

Create an S3 bucket to store CloudTrail and Lambda processing logs.

Example:

Bucket name: `security-project-logs`

Region: `ap-northeast-1`

This bucket is used for:

CloudTrail logs

Security event processing results

Athena queries

## 3. Enable CloudTrail

### Step 2: Enable CloudTrail

1. Open AWS CloudTrail
2. Create a new trail
3. Enable:
   
   Management events
   
   Write and Read events
4. Set the S3 destination to:
   
   `security-project-logs`

## 4. Create SNS Topic

### Step 3: Create SNS Topic

Create an SNS topic to receive security incident notifications.

Example:

Topic name: `security-incident-topic`

Region: `ap-northeast-1`

This topic is triggered by the Lambda function when a security event is detected.

## 5. Create Step Functions

### Step 4: Create Step Functions State Machines

Create the following AWS Step Functions state machines:

SFN-UnauthorizedAccess

SFN-CryptoMining

SFN-InspectorCritical

SFN-IAMPolicyChange

SFN-MacieSensitiveData

Each state machine represents an automated response workflow for a specific type of security incident.。

## 6. Create Lambda Function

### Step 5: Create Lambda Function

Create a Lambda function to process security events from multiple AWS services.

Runtime: Python 3.11

Function name: `security-event-handler`

Trigger source:

Amazon EventBridge

This Lambda function:

Identifies security event sources (GuardDuty, Inspector, CloudTrail, Macie)

Sends notifications via SNS

Triggers corresponding Step Functions workflows

## 7. Configure EventBridge Rules

### Step 6: Configure EventBridge Rules

Create EventBridge rules to route security events to the Lambda function.

Event sources include:

AWS GuardDuty Findings

AWS Inspector2 Findings

AWS CloudTrail API calls

AWS Macie Findings

## 8. Athena & QuickSight

### Step 7: Athena & QuickSight Setup

1. Create an Athena database:
   
   `logs_database`
2. Create tables for CloudTrail logs stored in S3
3. Run sample queries to verify log availability
4. Connect Athena as a data source in Amazon QuickSight
5. Build dashboards for:
   
   Security events frequency
   
   API activity trends

## 9. Deployment Summary

### Deployment Summary

After completing the steps above, the platform will be able to:

Detect security incidents

Trigger automated response workflows

Notify via SNS

Store and analyze logs using Athena and QuickSight

# 搭建指南

## 1. 前置要求

AWS 账户（亚太地区-东京 ap-northeast-1）

配置具有足够权限的 AWS CLI

掌握以下基础知识： 

AWS Lambda 

IAM 

Amazon EventBridge 

AWS Step Functions 

Amazon SNS 

Amazon Athena 

Amazon QuickSight

## 2. 创建 S3 日志存储桶

### 步骤 1：创建 S3 日志存储桶

创建一个 S3 存储桶用于存储 CloudTrail 和 Lambda 处理日志。

示例：

存储桶名称：`security-project-logs`

区域：`ap-northeast-1`

此存储桶用于：

CloudTrail 日志

安全事件处理结果

Athena 查询

## 3. 启用 CloudTrail

### 步骤 2：启用 CloudTrail

1. 打开 AWS CloudTrail
2. 创建新的跟踪
3. 启用： 管理事件 写和读事件
4. 将 S3 目标设置为： `security-project-logs`

## 4. 创建 SNS 主题

### 步骤 3：创建 SNS 主题

创建一个 SNS 主题来接收安全事件通知。

示例：

主题名称：`security-incident-topic`

区域：`ap-northeast-1`

当检测到安全事件时，Lambda 函数将触发此主题。

## 5. 创建 Step Functions

### 步骤 4：创建 Step Functions 状态机

创建以下 AWS Step Functions 状态机：

SFN-UnauthorizedAccess

SFN-CryptoMining

SFN-InspectorCritical

SFN-IAMPolicyChange

SFN-MacieSensitiveData

每个状态机代表针对特定类型安全事件的自动化响应工作流。

## 6. 创建 Lambda 函数

### 步骤 5：创建 Lambda 函数

创建一个 Lambda 函数来处理来自多个 AWS 服务的安全事件。

运行时：Python 3.11

函数名称：`security-event-handler`

触发源： Amazon EventBridge

此 Lambda 函数的功能：

识别安全事件源（GuardDuty、Inspector、CloudTrail、Macie）

通过 SNS 发送通知

触发相应的 Step Functions 工作流

## 7. 配置 EventBridge 规则

### 步骤 6：配置 EventBridge 规则

创建 EventBridge 规则，将安全事件路由到 Lambda 函数。

事件源包括：

AWS GuardDuty 安全发现

AWS Inspector2 安全发现

AWS CloudTrail API 调用

AWS Macie 安全发现

## 8. Athena 和 QuickSight 设置

### 步骤 7：Athena 和 QuickSight 设置

1. 创建一个 Athena 数据库： `logs_database`
2. 为存储在 S3 中的 CloudTrail 日志创建表
3. 运行示例查询以验证日志可用性
4. 在 Amazon QuickSight 中将 Athena 连接为数据源
5. 构建以下仪表板： 安全事件频率 API 活动趋势

## 9. 部署总结

### 部署总结

完成上述步骤后，该平台将能够：

检测安全事件

触发自动化响应工作流

通过 SNS 发送通知

使用 Athena 和 QuickSight 存储和分析日志
