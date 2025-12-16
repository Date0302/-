CREATE EXTERNAL TABLE IF NOT EXISTS cloudtrail_logs (
  Records array<
    struct<
      eventVersion:string,
      userIdentity:struct<
        type:string,
        arn:string,
        accountId:string
      >,
      eventTime:string,
      eventSource:string,
      eventName:string,
      awsRegion:string,
      sourceIPAddress:string,
      userAgent:string,
      eventType:string,
      recipientAccountId:string,
      eventCategory:string
    >
  >
  >)
  >ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
  >LOCATION 's3://security-project-logs/';