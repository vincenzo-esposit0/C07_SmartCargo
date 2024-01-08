def registrazioneAccount(accountJson):
    try:
        if autotrasportatore_dao.is_autotrasportatore_registrato(accountJson["email"]):
            return jsonify({'message': 'Utente già registrato'}), 400