import json
import os
import matplotlib.pyplot as plt

# Objectives:
#   median kilobytes transferred per har page (a single har file represents a single page) - 1 kilobyte = 1000 bytes, use headerSize and bodySize
#   median number of requests per page
#   percentage of URLs using HTTPS
#   percentage of requests over HTTP/1.1 and HTTP/2
#   median, min, and max page load time
#   median, min, and max number of bytes spent on HTTP headers

cwd = os.getcwd()
harhar = os.path.join(cwd, "harhar")
directory = os.chdir(harhar)

kiloArr = [] # array of bytes
requestArr = [] # arry of requests
pageArr = [] # array of page load times
headerArr = [] # array of number of bytes spent on HTTP headers
httpsArr = [] # array of URLs using HTTPS
http11Arr = [] # array of requests of HTTP/1.1
http2Arr = [] # array of requests of HTTP/2

totalRequests = 0
totalHttp1 = 0
totalHttp2 = 0

for har in os.listdir(): # har is str
    if har != ".DS_Store":
        data_file = har
        with open(data_file, encoding = 'utf-8') as f:
            jdata = json.load(f)
            
            fileCount = len(os.listdir())

            # start of kilobytes calculation ---
            everyEntry = 0
            entryCount = len(jdata['log']['entries']) 
            
            for everyEntry in range(0, entryCount): # loops through number of entries in har file
                getBodySizeByte = int(jdata['log']['entries'][everyEntry]['request']['bodySize'])
                getHeadersSizeByte = int(jdata['log']['entries'][everyEntry]['request']['headersSize'])
                totalRequests += 1

            totalBytes = getBodySizeByte + getHeadersSizeByte
            kilobytes = totalBytes / 1000
            kiloArr.append(kilobytes)

            k = len(kiloArr)
            kiloArr.sort()

            if k % 2 == 0: # used to find median in Task 2a
                kmedian1 = kiloArr[k//2]
                kmedian2 = kiloArr[k//2 - 1]
                kmedian = (kmedian1 + kmedian2) / 2
            else:
                kmedian = kiloArr[k//2]

            # end of kilobyte calculation ---

            # start of request ---
            everyRequest = 0
            requestCount = len(jdata['log']['entries'])

            for everyRequest in range(0, requestCount): # loops through number of entries in har file
                getRequest = entryCount # number of requests equals the number of entries
                
            requestArr.append(getRequest)

            r = len(requestArr)
            requestArr.sort()

            if r % 2 == 0: # used to find median of sorted requests
                rmedian1 = requestArr[r//2]
                rmedian2 = requestArr[r//2 - 1]
                rmedian = (rmedian1 + rmedian2) / 2
            else:
                rmedian = requestArr[r//2]

            # end of request ---

            # start of page load time calculation ---
            pageCount = 0
            pageCount = len(jdata['log'])

            for pageCount in range(0, pageCount):
                getLoadTime = int(jdata['log']['pages'][0]['pageTimings']['onLoad'])
            
            if getLoadTime <= 0:
                getLoadTime = getLoadTime * -1

            pageArr.append(getLoadTime)

            p = len(pageArr)
            pageArr.sort()

            if p % 2 == 0: # used to find median of sorted page load times
                pmedian1 = pageArr[p//2]
                pmedian2 = pageArr[p//2 - 1]
                pmedian = (pmedian1 + pmedian2) / 2
            else:
                pmedian = pageArr[p//2]

            minPage = min(pageArr) # min page load time
            maxPage = max(pageArr) # max page load time
            
            # end of page load time calculation ---

            # start of header finding ---

            everyHeader = 0
            everyHttp = 0
            httpCount = len(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
            headerCount = len(jdata['log']['entries'][everyEntry]['request']['headers'])

            for everyHttp in range(0, httpCount):
                getHttpBytes = str(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
                for everyHeader in range(0, headerCount):
                    getHeaderCount = int(jdata['log']['entries'][everyEntry]['request']['headersSize'])
            
            headerArr.append(getHeaderCount)

            h = len(headerArr)
            headerArr.sort()

            if h % 2 == 0:
                hmedian1 = headerArr[h//2]
                hmedian2 = headerArr[p//2 - 1]
                hmedian = (hmedian1 + hmedian2) / 2
            else:
                hmedian = headerArr[h//2]

            minHeader = min(headerArr)
            maxHeader = max(headerArr)            
            
            # end of header finding ---

            # start of URL percentage calculation ---

            # Note: total HTTP used / request amount * 100

            everyHttpsURL = 0
            #httpsURLCount = len(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
            urlPercentage = 0

            for everyHttpsURL in range(0, entryCount):
                getHttpsURL = str(jdata['log']['entries'][everyEntry]['request']['url'])

            if "https" in getHttpsURL:
                httpsURL = int(everyHttpsURL)
                urlPercentage = (httpsURL / fileCount) * 100
            
            httpsArr.append(urlPercentage)

            # end of URL percentage calculation ---
            
            # start of http calculation ---
              
            everyHttp11 = 0
            everyHttp2 = 0
            
            for everyHttp11 in range(0, entryCount):
                getHttp = jdata['log']['entries'][everyEntry]['request']['httpVersion']
            
                if "HTTP/1.1" in getHttp:
                    everyHttp11 += 1
                    totalHttp1 += 1
                   
                elif "HTTP/2" in getHttp:
                    everyHttp2 += 1
                    totalHttp2 += 1
        
            http11Arr.append((everyHttp11/getRequest) * 100)
            http2Arr.append((everyHttp2/getRequest) * 100)

            http11Per = (totalHttp1/totalRequests) * 100
            http2Per = (totalHttp2/totalRequests) * 100
            
            # end of http calculation --- 


            '''# start of HTTP/1.1 calculation ---

            everyHttp11 = 0
            http11Count = len(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
            http11Res = 0
        
            for everyHttp11 in range(0, http11Count):
                getHttp11 = str(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
                #getHttp2 = str(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
                
            if "HTTP/1.1" in getHttp11:
                https11 = int(everyHttp11)
                #everyhttp11 += 1
                http11Res = (https11 / getRequest) * 100
                #print(getHttp11)

            http1Arr.append(http11Res)

            # end of HTTP/1.1 calculation ---

            # start of HTTP/2 calcuation --- 

            everyHttp2 = 0
            http2Count = len(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
            http2Res = 0
            for everyHttp2 in range(0, http2Count):
                getHttp2 = str(jdata['log']['entries'][everyEntry]['request']['httpVersion'])
            
            if "HTTP/2" in getHttp2:
                http2 = int(everyHttp2)
                http2Res = (http2 / getRequest) * 100
                #print(getHttp2)
            
            http2Arr.append(http2Res)

            '''# end of HTTP/2 calculation ---

print("Number of Files in harhar folder: ", fileCount) # num of files in harhar folder

print("\nMedian of Total Kilobytes: " + str(kmedian))

print("\nMedian of requests per page: " + str(rmedian))

print("\nPercentage of URLs using HTTPS: " + str(urlPercentage))

print("\nPercentage of URLS using HTTP/1.1: ", http11Per)
print("Percentage of URLS using HTTP/2: ", http2Per)

print("\nMedian load time: " + str(pmedian))
print("Min load time: " + str(minPage))
print("Max load time: " + str(maxPage))

print("\nMedian byte: " + str(hmedian))
print("The min number of bytes spent on headers: " + str(minHeader))
print("The max number of bytes spent on headers: " + str(maxHeader))

# Arrays Sorted
kiloArr.sort() 
requestArr.sort() 
pageArr.sort() 
headerArr.sort()
httpsArr.sort() 
http11Arr.sort() 
http2Arr.sort() 

# Task 3 Plot
# uncomment

plt.plot(http11Arr, requestArr, label='HTTP/1.1')
plt.plot(http2Arr, requestArr, label='HTTP/2')

plt.title('HTTP Percentages used VS Requests')
plt.xlabel('Number of Requests')
plt.ylabel("HTTP percentage used")

plt.legend()
plt.show()