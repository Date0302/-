# S3 Setup Guide

This project uses two S3 buckets:

1. `my-unique-image-upload-bucket`(User-uploaded original images)
2. `my-image-processed-first`(Images processed by Lambda)

This document describes all steps for creating and securing the storage.

------

## 1. Create S3 Bucket (Original Images)

Navigate to:

**Amazon S3 → Create bucket**

###  Settings:

- 

  Bucket name:

  ```
  my-unique-image-upload-bucket
  ```

- Region: ap-northeast-1 (Tokyo)

- Object ownership: Bucket owner enforced

- Block Public Access: ON (Enable all)

Click Create.

------

## 2. Enforce HTTPS

Go to bucket → Permissions → Bucket policy

Add:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-unique-image-upload-bucket",
        "arn:aws:s3:::my-unique-image-upload-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

------

## 3. Configure CORS

Navigate to: **Permissions → CORS**

```
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["PUT", "GET", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
```

------

## 4. Configure Lifecycle Rules

Navigate to:

**Management → Lifecycle rules → Create rule**

Example policy:

### Rule 1: User-uploaded images

- Transition to Standard-IA after 30 days
- Transition to Glacier Flexible Retrieval after 90 days

------

## 5. Create Second Bucket (Processed Images)

```
my-image-processed-first
```

Settings are the same as the first bucket.

------

## 6. Use Prefixes for User Directory Isolation

The pre-signed URL upload path is:

```
user-uploads/<identity-id>/<uuid>.jpg
```

This structure effectively prevents users from overwriting each other's permissions.

------

## 🎉 S3 Setup Complete!

Your storage now has:

HTTPS enforcement

CORS support

Lifecycle automation

User directory isolation

Secure upload mechanism

# S3 Setup Guide

本项目使用两个 S3 bucket：

1. `my-unique-image-upload-bucket`（用户上传原图）
2. `my-image-processed-first`（Lambda 处理后的图片）

本文档介绍创建与强化安全的所有步骤。

---

## 1. 创建 S3 Bucket（原图）

进入：
**Amazon S3 → Create bucket**

###  设置：

- Bucket name:
  ```
  my-unique-image-upload-bucket
  ```
- Region: ap-northeast-1（东京）
- Object ownership: Bucket owner enforced
- Block Public Access: ON（全部开启）

点击 Create。

---

## 2. 强制 HTTPS

进入 bucket → Permissions → Bucket policy  
添加：

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-unique-image-upload-bucket",
        "arn:aws:s3:::my-unique-image-upload-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

---

### 3. 设置 CORS

进入：**Permissions → CORS**

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["PUT", "GET", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
```

---

## 4. 配置生命周期（Lifecycle）

进入：

**Management → Lifecycle rules → Create rule**

示例策略：

### Rule 1：用户上传图像

- 30 天后移动到 Standard-IA  
- 90 天后移动到 Glacier Flexible Retrieval  

---

## 5. 创建第二个 bucket（处理后的图像）

```
my-image-processed-first
```

设置与第一个相同。

---

## 6. 使用前缀隔离用户目录

预签名 URL 的上传路径是：

```
user-uploads/<identity-id>/<uuid>.jpg
```

这种结构能有效保证用户间不会互相覆盖权限。

---

## 🎉 S3 设置完成！

你的存储已具备：

 HTTPS 强制  
 CORS 支持  
 生命周期自动化  
 用户隔离子目录  
 安全上传机制  