def doGet(request, session):
	return {'html': '<html><body>Hello World</body></html>'}
	data = request['postData']

if isinstance(data, dict):
    barcode = data.get('barcode', '')
else:
    barcode = data or ''

if barcode:
    system.tag.writeBlocking(
        ['[default]BarcodeLastScan'],
        [barcode]
    )

return {'json': {'ok': True, 'barcode': barcode}}