from collections import defaultdict

http_requests = defaultdict(int)
webhook_results = defaultdict(int)

def record_http(path, status):
    http_requests[(path, status)] += 1

def record_webhook(result):
    webhook_results[result] += 1

def metrics_text():
    lines = []
    for (path, status), count in http_requests.items():
        lines.append(f'http_requests_total{{path="{path}",status="{status}"}} {count}')
    for result, count in webhook_results.items():
        lines.append(f'webhook_requests_total{{result="{result}"}} {count}')
    return "\n".join(lines)
