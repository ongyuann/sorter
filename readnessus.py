
filename = "HCR OpSpace_s7677y.nessus"

def read():
    with open(filename,"r") as f:
        res = f.read()
    f.close()
    #print(res)
    return res

res = read()

def printlistvertical(res):
    for i in range(len(res)):
        print("%d: %s" % (i,res[i]))
    pass

def process(res):
    res_list = res.split("\n")

    #res_list = res_list[22168:]
    #print(len(res_list))
    #printlistvertical(res_list[145:155]) #75:85
    '''
    # structure
    21 compliance result (fail/pass) <<-- take this
    23 compliance benchmark name (benchmark) <<-- take this
    28 report-item body (finding title) <<-- take this
    32 cve id <<-- take this
    33 cvss base score <<-- take this
    34 cvss temporal score <<-- take this
    43 description header <<-- take this
    44 description body <<-- take this
    58 solution / recommendation <<-- take this
    59 synopsis / observation <<-- take this
    ...
    87 description header <-- take this
    88 description body <-- take this
    ...
    102 solution
    103 synopsis
    ...
    '''

    res_chunks = {}
    res_unix = []
    res_unix_index = []
    failed_descriptions = []
    failed_titles = []
    failed_solutions = []
    failed_failed = []
    #'''
    for i in range(len(res_list)):
        res_list_i = res_list[i]
        #tmp_chunk = []
        if "Unix Compliance Checks" in res_list_i:
            if "pluginFamily" in res_list_i:
                tmp_chunk = res_list[i:i+66]
                failed_chunk = []
                for i in tmp_chunk:
                    if "result" in i:
                        if "FAILED" in i:
                            failed_chunk = tmp_chunk
                for i in failed_chunk:
                    #print("[+] ###########################")
                    if "result" in i:
                        #print(i)
                        failed_failed.append(i)
                        pass
                    if "solution" in i:
                        #print(i)
                        failed_solutions.append(i)
                        pass
                    if "compliance-info" in i:
                        #print(i)
                        if "informational-id" in i:
                            continue
                        else:
                            failed_descriptions.append(i)
                        pass
                    if "compliance-check-name" in i:
                        #print(i)
                        failed_titles.append(i)
                        pass
                    if "compliance-actual-value" in i:
                        #print(i)
                        pass
                #res_unix_index.append(i)
    #'''
    #print(failed_descriptions[0])
    print("[+] len(failed_descriptions): %d" % (len(failed_descriptions)))
    #print(failed_titles)
    print("[+] len(failed_titles): %d" % len(failed_titles))
    print("[+] len(failed_solutions) %d" % len(failed_solutions))
    print("[+] len(failed_failed) %d" % len(failed_failed))
    #print(res_chunk[0])
    '''
    for i in res_chunk[0]:
        if "result" in i:
            print(i)
        if "solution" in i:
            print(i)
        if "compliance-info" in i:
            print(i)
        if "compliance-check-name" in i:
            print(i)
        if "compliance-actual-value" in i:
            print(i)
        #print(i)
    '''
    #print(res_unix_index)
    print("[+] len(res_unix): %d" % len(res_unix))
    #print(res_list)
    pass

process(res)


'''
if "FAILED" in res_list[i+21]:
    res_unix.append(res_list[i]) #chunk head
    res_unix.append(res_list[i+21]) #fail/pass
    res_unix.append(res_list[i+23]) #benchmark
    res_unix.append(res_list[i+28]) #finding title
    res_unix.append(res_list[i+43]) #description header
    res_unix.append(res_list[i+44]) #description body
    res_unix.append(res_list[i+58]) #solution
'''

'''
# structure
0 pluginFamily
1 agent
2 compliance true/false
3 compliance check type
4 compliance supports parse validation
5 compliance supports replacement
6 compliance plugin fname
7 plugin modification date
8 plugin_name
9 plugin_publication_date
10 plugin_type
11 risk_factor
12 script_version
13 benchmark_version
14 compliance-check-name (benchmark)
15 compliance check id
16 compliance source
17 compliance audit file (benchmark)
18 compliance policy value (fail/pass)
19 compliance functional id
20 compliance uname (uname -a output)
21 compliance result (fail/pass) <<-- take this
22 compliance informational id
23 compliance benchmark name (benchmark) <<-- take this
24 compliance-control-id
25 compliance-see-also
26 compliance-full-id
27 report-item header
28 report-item body (finding title) <<-- take this
29 age of vuln
30 agent
31 cpe
32 cve id <<-- take this
33 cvss base score <<-- take this
34 cvss temporal score <<-- take this
35 cvss3 temporal vector
36 cvss3 vector
37 cvss3 impact
38 cvss2 base score
39 cvss2 score source (usually cve)
40 cvss2 temporal score
41 cvss2 temporal vector
42 cvss2 vector
43 description header <<-- take this
44 description body <<-- take this
45 exploit code maturity
46 exploitability
47 plugin name
48 patch publication date
49 plugin modification date
50 plugin name (finding title)
51 plugin publication date
52 plugin type (local/remote)
53 product coverage
54 risk factor
55 script version
56 see also header
57 see also body
58 solution / recommendation <<-- take this
59 synopsis / observation <<-- take this
60 thorough_tests (true/false)
61 threat_intensity_last_28
62 threat recency
63 threat_sources_last_28
64 vpr_score
65 vuln_publication_date
66 plugin_output header
67 plugin_output: path
68 plugin_output: installed version
69 plugin_output: fixed version
70 plugin-output closer
71 reportitem closer
72 reportitem
73 age_of_vuln
74 agent
...
87 description header <-- take this
88 description body <-- take this
...
102 solution
103 synopsis
'''
