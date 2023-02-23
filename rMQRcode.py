from rmqrcode import rMQR
import rmqrcode
from rmqrcode import QRImage

# pip install rmqrcode
# v0.3.1
# https://github.com/OUDON/rmqrcode-python#readme

data = "https://oudon.xyz"
qr = rMQR.fit(
    data,
    ecc=rmqrcode.ErrorCorrectionLevel.M,
    fit_strategy=rmqrcode.FitStrategy.MINIMIZE_WIDTH
)

# ecc : ErrorCorrectionLevel
    # ErrorCorrectionLevel.M: Approx. 15% Recovery Capacity.
    # ErrorCorrectionLevel.H: Approx. 30% Recovery Capacity.

# fit_strategy : specify how to determine size of rMQR Code.
    # FitStrategy.MINIMIZE_WIDTH: Try to minimize width.
    # FitStrategy.MINIMIZE_HEIGHT: Try to minimize height.
    # FitStrategy.BALANCED: Try to keep balance of width and height.

# Save as Image
image = QRImage(qr, module_size = 8)
image.show()
image.save("my_rMQR.png")