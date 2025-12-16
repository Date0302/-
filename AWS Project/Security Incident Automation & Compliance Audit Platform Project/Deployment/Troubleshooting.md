# Troubleshooting

## 1. Athena Query Returns No Results

Issue: Athena Query Returns No Results

### **Symptoms**

Query executes successfully
Result set is empty

### **Cause**

CloudTrail logs exist but no matching events occurred during the selected time range

### **Resolution**

Verify CloudTrail logs exist in the S3 bucket
Adjust query time range or filters

## 2. TABLE_NOT_FOUND Error

Issue: TABLE_NOT_FOUND Error in Athena

### **Cause**

Incorrect database selected in Athena

### **Resolution**

Switch to the correct database (e.g. `logs_database`)

------

## 3. Lambda SNS Publish Access Denied

Issue: Lambda Cannot Publish to SNS

### **Cause**

Missing `sns:Publish` permission in Lambda IAM role

### **Resolution**

Attach an IAM policy allowing `sns:Publish` on the target SNS topic

## 4. Step Functions StartExecution Access Denied

Issue: Step Functions Execution Fails

### **Cause**

Lambda execution role lacks `states:StartExecution` permission

### **Resolution**

Add `states:StartExecution` permission for the target state machines

## 5. State Machine Does Not Exist

Issue: StateMachineDoesNotExist Error

### **Cause**

ncorrect or outdated Step Functions ARN configured in Lambda

### **Resolution**

Verify the correct state machine ARN and region

## 6.Summarize

The core lesson from this AWS troubleshooting guide is that most deployment issues stem from incorrect permission configurations and misconfigured resource references. 

Typical cases include Lambda functions failing to publish SNS notifications or trigger Step Functions due to missing `sns:Publish`/`states:StartExecution`permissions in their IAM roles, and "State Machine Does Not Exist" errors caused by incorrect or outdated ARNs.

 For data queries, empty Athena results often indicate no matching events in the time range, while `TABLE_NOT_FOUND`errors usually result from querying the wrong database. 

The universal resolution path is: accurately diagnose the error message, systematically verify and correct IAM policies or resource ARNs, and validate the fix through testing.



# 故障排除指南

## 1.Athena 查询无结果

### **症状**

查询执行成功

结果集为空

### **原因**

CloudTrail 日志存在，但在选定时间范围内未发生匹配的事件

### **解决方案**

验证 CloudTrail 日志是否存在于 S3 存储桶中

调整查询时间范围或筛选条件

## 2. TABLE_NOT_FOUND 错误

### **原因**

在 Athena 中选择了错误的数据库

### **解决方案**

切换到正确的数据库（例如 `logs_database`）

## 3. Lambda SNS 发布权限被拒绝

### **原因**

Lambda IAM 角色缺少 `sns:Publish`权限

### **解决方案**

附加允许对目标 SNS 主题进行 `sns:Publish`的 IAM 策略

## 4. Step Functions 启动执行权限被拒绝

### **原因**

Lambda 执行角色缺少 `states:StartExecution`权限

### **解决方案**

添加针对目标状态机的 `states:StartExecution`权限

## 5. 状态机不存在

### **原因**

Lambda 中配置的 Step Functions ARN 不正确或已过时

### **解决方案**

验证正确的状态机 ARN 和区域

## 6.总结

这份AWS故障排除指南的核心经验是：绝大多数部署问题源于权限配置错误和资源配置引用错误。

具体表现为Lambda函数因IAM角色缺少`sns:Publish`或`states:StartExecution`权限而无法发布通知或触发工作流，以及因Step Functions状态机的ARN配置不正确或过时而导致“状态机不存在”错误。

对于数据查询问题，Athena查询无结果通常并非配置错误，而是所选时间范围内确实没有匹配的日志事件；而`TABLE_NOT_FOUND`错误则往往是因为在查询时未切换到正确的数据库。

解决这些问题的通用思路是：首先精确识别错误信息，然后系统性地检查并修正IAM权限或资源ARN引用，最后通过验证测试确认问题已解决。
