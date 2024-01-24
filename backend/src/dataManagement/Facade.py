from src.models.MultipleDaoAccess import MultipleDaoAccess


class InterfaceFacade:
    def __init__(self):
        self.multipleDaoAccess = MultipleDaoAccess()

    def ottieniQrcodeValidazione(self, operazione_id):
        qrcode, operazione = self.multipleDaoAccess.ottieniQrcodeValidazione(operazione_id)

        return qrcode, operazione

    def ottieniInfoOperazione(self, operazione):
        autotrasportatore, veicolo, include, operatore_mobile, operatore_sala, issue, merce, percorso = self.multipleDaoAccess.ottieniInfoOperazione(operazione)

        return autotrasportatore, veicolo, include, operatore_mobile, operatore_sala, issue, merce, percorso
