import PyPDF2

#carrega o arquivo pdf
pdfFileObj = open('meupdf.pdf', 'rb')

#faz leitura do arquivo pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#captura primeira página do pdf
pageObj = pdfReader.getPage(0)

#extrai texto do pdf e passa para variavel 
text = pageObj.extractText()

#mostra texto do pdf
print(text)
