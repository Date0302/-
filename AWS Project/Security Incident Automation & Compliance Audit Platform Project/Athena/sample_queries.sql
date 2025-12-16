SELECT
  r.eventName,
  COUNT(*) AS cnt
FROM cloudtrail_logs
CROSS JOIN UNNEST(Records) AS t(r)
GROUP BY r.eventName
ORDER BY cnt DESC
LIMIT 10;