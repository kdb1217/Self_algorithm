def solution(id_list, report, k):
    answer = [0] * len(id_list)
    arrcnt = {}
    repcnt = {}
    for i in range(len(id_list)):
        arrcnt[id_list[i]] = 0
        repcnt[id_list[i]] = []
    
    processed_reports = set()
    
    for r in report:
        tmp = r.split(" ")
        reporter = tmp[0]
        reported = tmp[1]
        
        if r in processed_reports:
            continue
        
        processed_reports.add(r)
        
        if reported in arrcnt:
            arrcnt[reported] += 1
            repcnt[reporter].append(reported)
    
    for i in range(len(id_list)):
        reported_users = repcnt[id_list[i]]
        for user in reported_users:
            if arrcnt[user] >= k:
                answer[i] += 1
    
    return answer
