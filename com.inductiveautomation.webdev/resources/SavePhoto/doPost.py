def doPost(request, session):


    import base64
    import os
    import re
    from java.text import SimpleDateFormat
    from java.util import Date

    SAVE_DIR = r"C:\Users\braiden.goodey\OneDrive - Thermo Fisher Scientific\Desktop\Working\Ignition\Test_Pics"

    try:
        data = request.get("postData", {})

        image_data = data.get("imageData", "")
        if not image_data:
            return {"json": {"ok": False, "error": "Missing imageData"}}

        barcode = data.get("barcode", "")
        barcode = re.sub(r"[^A-Za-z0-9._-]+", "_", barcode).strip("_")
        if not barcode:
            barcode = "capture"

        if image_data.startswith("data:image"):
            image_data = image_data.split(",", 1)[1]

        image_bytes = base64.b64decode(image_data)

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

        timestamp = SimpleDateFormat("yyyyMMdd_HHmmss_SSS").format(Date())
        filename = "%s_%s.jpg" % (barcode, timestamp)
        full_path = os.path.join(SAVE_DIR, filename)

        f = open(full_path, "wb")
        try:
            f.write(image_bytes)
        finally:
            f.close()

        return {"json": {"ok": True, "file": full_path}}

    except Exception as e:
        return {"json": {"ok": False, "error": str(e)}}