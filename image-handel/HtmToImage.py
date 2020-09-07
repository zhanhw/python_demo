import imgkit

path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wk)
html = imgkit.from_url(url="http://dqt.boka.vc/", config=config, output_path="out.png")
