from src.models.OperazioneDAO import OperazioneDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.QrCodeDAO import QrCodeDAO


class QrCodeFacade:
    def __init__(self):
        self.operazione_dao = OperazioneDAO()
        self.autotrasportatore_dao = AutotrasportatoreDAO()
        self.qrcode_dao = QrCodeDAO()

    def ottieniQrcodeValidazione(self, operazione_id):
        operazione = self.operazione_dao.ottieni_operazione_per_id(operazione_id)
        autotrasportatore = self.autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)
        qrcode = self.qrcode_dao.ottieni_qrCode_per_id(autotrasportatore.qrCode_id)

        return qrcode, operazione