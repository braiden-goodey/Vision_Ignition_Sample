def onBarcodeDataReceived(session, data, context):
	system.tag.writeAsync(['[default]New Tag'], [data.text])
	