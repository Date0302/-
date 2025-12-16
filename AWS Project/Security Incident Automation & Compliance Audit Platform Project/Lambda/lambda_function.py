import boto3
import json
from datetime import datetime

# 初始化客户端
s3 = boto3.client('s3')
sns = boto3.client('sns')
sfn = boto3.client('stepfunctions')

# 配置
LOG_BUCKET = "security-project-logs"  # S3 日志桶
SNS_TOPIC_ARN = "arn:aws:sns:ap-northeast-1:796796207962:security-incident-topic"

# Step Functions ARN 配置
STEP_FUNCTIONS_ARN = {
    "UnauthorizedAccess": "arn:aws:states:ap-northeast-1:796796207962:stateMachine:SFN-UnauthorizedAccess",
    "CryptoMining": "arn:aws:states:ap-northeast-1:796796207962:stateMachine:SFN-CryptoMining",
    "InspectorCritical": "arn:aws:states:ap-northeast-1:796796207962:stateMachine:SFN-InspectorCritical",
    "IAMPolicyChange": "arn:aws:states:ap-northeast-1:796796207962:stateMachine:SFN-IAMPolicyChange",
    "MacieSensitiveData": "arn:aws:states:ap-northeast-1:796796207962:stateMachine:SFN-MacieSensitiveData"
}

# ---------------- 修复动作占位函数 ----------------
def handle_unauthorized_access(event):
    instance_id = event['detail']['resource']['instanceDetails']['instanceId']
    # TODO: 替换为真正隔离 EC2 的 API 调用
    return f"Isolated EC2 instance {instance_id}"

def handle_crypto_mining(event):
    instance_id = event['detail']['resource']['instanceDetails']['instanceId']
    # TODO: 替换为停止挖矿实例 API
    return f"Stopped crypto mining on {instance_id}"

def handle_inspector_critical(event):
    finding_id = event['detail'].get('findingArn', 'Unknown')
    return f"Processed Inspector critical finding {finding_id}"

def handle_iam_policy_change(event):
    # TODO: 替换为禁用 Access Key / 回滚策略 API
    return "Reverted unsafe IAM policy change"

def handle_s3_public(event):
    bucket_name = event['detail']['resource'].get('bucketName', 'Unknown')
    # TODO: 替换为阻止 S3 Public API
    return f"Removed public access for S3 bucket {bucket_name}"

def log_unknown_event(event):
    return "Unknown event type, no action taken"
def lambda_handler(event, context):
    try:
        # 识别事件类型
        source = event.get("source", "")
        detail_type = event.get("detail-type", "")
        step_arn = None
        action_result = ""

        if source == "aws.guardduty" and detail_type == "GuardDuty Finding":
            detail_type_guard = event['detail'].get("type", "")
            if "UnauthorizedAccess" in detail_type_guard:
                action_result = handle_unauthorized_access(event)
                step_arn = STEP_FUNCTIONS_ARN["UnauthorizedAccess"]
            elif "CryptoCurrency" in detail_type_guard:
                action_result = handle_crypto_mining(event)
                step_arn = STEP_FUNCTIONS_ARN["CryptoMining"]

        elif source == "aws.inspector2" and detail_type == "Inspector2 Finding":
            action_result = handle_inspector_critical(event)
            step_arn = STEP_FUNCTIONS_ARN["InspectorCritical"]

        elif source == "aws.cloudtrail" and detail_type == "AWS API Call via CloudTrail":
            action_result = handle_iam_policy_change(event)
            step_arn = STEP_FUNCTIONS_ARN["IAMPolicyChange"]

        elif source == "aws.macie" and detail_type == "Macie Finding":
            action_result = handle_s3_public(event)
            step_arn = STEP_FUNCTIONS_ARN["MacieSensitiveData"]

        else:
            action_result = log_unknown_event(event)
        # SNS 通知
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"Event {source}/{detail_type} handled. Action: {action_result}",
            Subject="Security Alert"
        )

        # 调用 Step Functions
        if step_arn:
            sfn.start_execution(
                stateMachineArn=step_arn,
                input=json.dumps(event)
            )

        return {"status": "success", "action": action_result}

    except Exception as e:
        print(f"Error processing event: {e}")
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"Error processing event: {str(e)}",
            Subject="Security Alert - Error"
        )
        raise e
