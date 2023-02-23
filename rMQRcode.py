from rmqrcode import rMQR
import rmqrcode
from rmqrcode import QRImage

# pip install rmqrcode
# v0.3.1
# https://github.com/OUDON/rmqrcode-python#readme

data = "https://stone-program.com/"
qr = rMQR.fit(
    data,
    ecc=rmqrcode.ErrorCorrectionLevel.M,
    fit_strategy=rmqrcode.FitStrategy.BALANCED
)

# ecc : ErrorCorrectionLevel
    # ErrorCorrectionLevel.M: Approx. 15% Recovery Capacity.
    # ErrorCorrectionLevel.H: Approx. 30% Recovery Capacity.

# fit_strategy : specify how to determine size of rMQR Code.
    # FitStrategy.MINIMIZE_WIDTH: Try to minimize width.
    # FitStrategy.MINIMIZE_HEIGHT: Try to minimize height.
    # FitStrategy.BALANCED: Try to keep balance of width and height.

# Save as Image
image = QRImage(qr, module_size = 128)
image.show()
image.save("my_rMQR_Balanced.png")