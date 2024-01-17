from src.models.OperazioneDAO import OperazioneDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.QrCodeDAO import QrCodeDAO

from src.models.IncludeDAO import IncludeDAO
from src.models.IssueDAO import IssueDAO
from src.models.MerceDAO import MerceDAO
from src.models.OperatoreMobileDAO import OperatoreMobileDAO
from src.models.OperatoreSalaDAO import OperatoreSalaDAO
from src.models.PercorsoDAO import PercorsoDAO
from src.models.VeicoloDAO import VeicoloDAO


class InterfaceFacade:
    def __init__(self):
        self.operazione_dao = OperazioneDAO()
        self.autotrasportatore_dao = AutotrasportatoreDAO()
        self.qrcode_dao = QrCodeDAO()
        self.veicolo_dao = VeicoloDAO()
        self.include_dao = IncludeDAO()
        self.merce_dao = MerceDAO()
        self.issue_dao = IssueDAO()
        self.percorso_dao = PercorsoDAO()
        self.operatoreMobile_dao = OperatoreMobileDAO()
        self.operatoreSala_dao = OperatoreSalaDAO()

    #ricerca il qrCode e l'operazione da andare ad aggiornare quando viene aperta/chiusa un'issue
    def ottieniQrcodeValidazione(self, operazione_id):
        operazione = self.operazione_dao.ottieni_operazione_per_id(operazione_id)
        autotrasportatore = self.autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)
        qrcode = self.qrcode_dao.ottieni_qrCode_per_id(autotrasportatore.qrCode_id)

        return qrcode, operazione

    #ricerca di tutti gli elementi connessi ad un operazione
    def ottieniInfoOperazione(self, operazione):
        # Ottieni le informazioni dell'autotrasportatore usando l'ID in operazione
        autotrasportatore = self.autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)

        # Ottieni le informazioni del veicolo usando l'ID in operazione
        veicolo = self.veicolo_dao.ottieni_veicolo_per_id(operazione.veicolo_id)

        # Ottieni le informazioni dell'include usando l'ID dell'operazione
        include = self.include_dao.ottieni_include_per_operazione_id(operazione.id)

        # Ottieni le informazioni della merce usando l'ID in include
        merce = self.merce_dao.ottieni_merce_per_id(include.merce_id)

        # Ottieni le informazioni dell'issue usando l'ID dell'operazione così da individuare l'operatore mobile
        issue = self.issue_dao.ottieni_issue_per_id_operazione(operazione.id)

        #Ottieni le informazioni sul percorso usando l'id in operazione
        percorso = self.percorso_dao.ottieni_percorso_per_id(operazione.percorso_id)

        operatore_mobile = None
        operatore_sala = None

        if issue is not None and issue != {}:
            operatore_mobile = self.operatoreMobile_dao.ottieni_operatore_mobile_per_id(issue.operatoreMobile_id)
            operatore_sala = self.operatoreSala_dao.ottieni_operatore_sala_per_id(issue.operatoreSala_id)

        return autotrasportatore, veicolo, include, operatore_mobile, operatore_sala, issue, merce, percorso