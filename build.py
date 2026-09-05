import base64, re

IMG_DIR = "images"

def b64(path, mime):
    with open(f"{IMG_DIR}/{path}", "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"

IMAGES = {
    "PROFILE": b64("profile.jpg", "image/jpeg"),
    "CABINET": b64("cabinet.jpg", "image/jpeg"),
    "CABINET_OPEN": b64("cabinet_open.jpg", "image/jpeg"),
    "CART_BUILD": b64("cart_build.jpg", "image/jpeg"),
    "CART_FINISHED": b64("cart_finished.jpg", "image/jpeg"),
    "CART_CAD1": b64("cart_cad1.jpg", "image/jpeg"),
    "CART_CAD2": b64("cart_cad2.jpg", "image/jpeg"),
    "GRAINWAVE_LOGO": b64("grainwave_logo.png", "image/png"),
}

with open("template.html", "r") as f:
    html = f.read()

for key, uri in IMAGES.items():
    html = html.replace(f"{{{{{key}}}}}", uri)

with open("index.html", "w") as f:
    f.write(html)

print("Built index.html:", len(html), "bytes")
