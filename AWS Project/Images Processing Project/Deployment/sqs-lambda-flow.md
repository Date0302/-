# SQS + Lambda Flow (Asynchronous Image Processing Architecture)

This project uses SQS to decouple S3 uploads from image processing.

This is a commonly used enterprise-grade architecture that provides:

- Automatic scaling
- Prevention of peak-time congestion
- Guaranteed task persistence
- Retry mechanisms and dead letter queues

## 1. S3 Upload Completion → Push Message to SQS

S3 event structure:

```
{
  "bucket": "my-unique-image-upload-bucket",
  "s3Key": "user-uploads/<userId>/<uuid>.jpg",
  "imageId": "<uuid>"
}
```

------

## 2. SQS Receives Message

Queue Example:

```
image-processing-queue
```

Queue Attributes:

- Visibility timeout: >= Lambda timeout × 6
- Receive message wait time: 10 seconds
- DLQ: image-processing-dlq

------

## 3. Lambda (image-processor-lambda) Retrieves Messages from SQS

IAM Permissions:

```
"sqs:ReceiveMessage"
"sqs:DeleteMessage"
```

Process Flow:

1. Receive message
2. Download original image (S3)
3. Generate thumbnail using Pillow
4. Upload processed image to another bucket
5. Write to DynamoDB
6. Send SNS notification

------

## 4. Dead Letter Queue (DLQ)

DLQ Name:

```
image-processing-dlq
```

Purpose:

- Failed Lambda processing attempts → automatically moved to DLQ
- Useful for troubleshooting corrupted files, format errors
- Ensures data is never lost

------

## 5. Lambda Auto-Scaling

SQS → Lambda provides automatic scaling:

- High message volume → Lambda instances scale up rapidly
- Low message volume → automatically scales down to 0
- No need for manual server management

------

## 🎉 Summary

SQS + Lambda provides your system with:

 High scalability

 High reliability

 Fully automated retries

 Data loss prevention

 Powerful error handling capabilities

# SQS + Lambda Flow（图像处理异步架构）

本项目使用 SQS 解耦 S3 上传和图像处理。  
这是企业级常用架构，可以：

- 自动扩展
- 避免高峰期拥堵
- 确保任务不丢失
- 做重试、死信队列

## 1. S3 上传完成 → 推送消息到 SQS

S3 event 结构：

```json
{
  "bucket": "my-unique-image-upload-bucket",
  "s3Key": "user-uploads/<userId>/<uuid>.jpg",
  "imageId": "<uuid>"
}
```

---

## 2. SQS 收到消息

Queue Example：
```
image-processing-queue
```

Queue Attributes：

- Visibility timeout：>= Lambda timeout * 6  
- Receive message wait time：10 seconds  
- DLQ：image-processing-dlq  

---

## 3. Lambda（image-processor-lambda）从 SQS 取消息

IAM 权限：

```json
"sqs:ReceiveMessage"
"sqs:DeleteMessage"
```

流程：

1. 接收消息  
2. 下载原图（S3）  
3. Pillow 生成缩略图  
4. 上传处理图到另一个 bucket  
5. 写入 DynamoDB  
6. 发送 SNS 通知  

---

## 4. 死信队列（Dead Letter Queue）

DLQ 名称：

```
image-processing-dlq
```

用途：

- Lambda 连续处理失败 → 自动进入 DLQ  
- 可用于排查损坏文件、格式错误文件  
- 保证不会丢数据  

---

## 5. Lambda 自动扩展

SQS → Lambda 是自动扩容的：

- 消息多 → Lambda 实例高速扩增  
- 消息少 → 自动缩减到 0  
- 无需手动管理服务器  

---

## 🎉 总结

SQS + Lambda 让你的系统具备：

 高扩展性  
 高可靠性  
 全自动重试  
 数据不会丢失  
 强大的错误处理能力  