#import necessary modules; "re" for RegEx and "json" for JSON format data
import re
import json
# here will be Elasticsearch module

#example line of web server log file:
#233.223.117.90 - - [27/Dec/2037:12:00:00 +0530] "DELETE /usr/admin HTTP/1.0" 502 4963 

# def func. to read log file data line by line
def read_log_lines(logfile):
    #RegEX pattern for log line to break it down in fields (9 according to log line content) and necessay info extraction
    pattern = re.compile(r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\S+)')
    extracted_data = []

    with open(logfile) as file:
        for line in file:
            match = pattern.match(line)
            if match:
                #selected only necessary fields, the rest are ignorred here, but can be included if needed
                ip_address = match.group(1)
                timestamp = match.group(4)
                http_method = match.group(5)
                url = match.group(6)
                http_status = match.group(8)
                response_size = match.group(9)
                fields = {
                    'ip_address': ip_address,
                    'timestamp': timestamp,
                    'http_method': http_method,
                    'url': url,
                    'http_status': http_status,
                    'response_size': response_size
                }
                extracted_data.append(fields)
    return extracted_data

# def. func to write extracted info in a JSON file
def write_json(extracted_fields):
    with open('output.json', 'w') as jsonfile:
        json.dump(extracted_fields, jsonfile)

# def. main func.
def main():
    logfile = 'logfile'
    extracted_fields = read_log_lines(logfile)
    write_json(extracted_fields)
    print("Extracted fields are saved in 'output.json' file. ")

# call main func.
if __name__ == '__main__':
    main()
