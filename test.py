import pdfkit
# pdfkit.from_url('http://baidu.com','out.pdf')
pdfkit.from_file('result.html','out.pdf')
# pdfkit.from_string('Hello!','out.pdf')