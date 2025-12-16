# AWS Security Log Analytics Project

## Overview
This project implements a security log analytics and visualization platform
using native AWS services.  
It focuses on collecting, analyzing, and visualizing AWS security-related logs
for audit and threat detection purposes.

The project is designed as a learning and demonstration project
to showcase AWS security architecture, log analytics, and visualization skills.

## Architecture
The architecture is based on a centralized logging and analytics approach.

Main flow:

AWS CloudTrail generates management event logs

Logs are stored in an encrypted Amazon S3 bucket

Amazon Athena is used to query logs directly from S3

Amazon QuickSight is used to build security dashboards

AWS Lambda is used for testing and simulating security events

Amazon EventBridge is used to trigger Lambda functions

(Architecture diagram provided in the repository)

## AWS Services Used
AWS CloudTrail

Amazon S3

AWS Lambda

Amazon EventBridge

Amazon Athena

Amazon QuickSight

AWS IAM

AWS KMS

## Key Features
Centralized storage of CloudTrail logs in S3

Serverless log analytics using Athena

Security-related API activity analysis

Visualization of AWS account activity using QuickSight

Encrypted log storage using AWS KMS

Least-privilege IAM role design

## Security Design
CloudTrail logs are encrypted using AWS KMS

S3 bucket enforces default server-side encryption

IAM roles follow least-privilege principles

Analytics is read-only and does not modify production resources

## Project Status
This project is completed as a hands-on security analytics lab.
Some queries and dashboards are simplified for demonstration purposes.

# AWS 安全日志分析项目

## 概述

本项目采用原生 AWS 服务实现了一个安全日志分析与可视化平台。

项目重点在于收集、分析和可视化 AWS 安全相关日志，用于审计和威胁检测目的。

该项目设计为一个学习和演示项目，旨在展示 AWS 安全架构、日志分析和可视化技能。

## 架构

该架构基于集中式日志记录和分析方法。

主要流程：

AWS CloudTrail 生成管理事件日志

日志存储在加密的 Amazon S3 存储桶中

使用 Amazon Athena 直接从 S3 查询日志

使用 Amazon QuickSight 构建安全仪表板

使用 AWS Lambda 测试和模拟安全事件

使用 Amazon EventBridge 触发 Lambda 函数

（架构图已在代码库中提供）

## 使用的 AWS 服务

AWS CloudTrail

Amazon S3

AWS Lambda

Amazon EventBridge

Amazon Athena

Amazon QuickSight

AWS IAM

AWS KMS

## 主要特性

在 S3 中集中存储 CloudTrail 日志

使用 Athena 进行无服务器日志分析

安全相关的 API 活动分析

使用 QuickSight 可视化 AWS 账户活动

使用 AWS KMS 的加密日志存储

遵循最小权限原则的 IAM 角色设计

## 安全设计

CloudTrail 日志使用 AWS KMS 加密

S3 存储桶强制执行默认服务器端加密

IAM 角色遵循最小权限原则

分析过程为只读，不会修改生产资源

## 项目状态

该项目已作为一个动手实践的安全分析实验完成。

部分查询和仪表板为演示目的进行了简化。