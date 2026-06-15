def doPost(request, session):
    logger = system.util.getLogger("ScannedData")

    data = request.get("postData", {})
    barcode = data.get("barcode", "") if isinstance(data, dict) else str(data).strip()

    logger.info("Received barcode=%r" % (barcode,))

    if barcode:
        system.tag.writeBlocking(["[default]BarcodeLastScan"], [barcode])

    return {"json": {"ok": True, "barcode": barcode}}