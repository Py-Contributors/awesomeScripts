from hill_cypher.encryption import HillCypher

if __name__ == '__main__':
    plain_text = "ACT"
    key = "GYBNQKURP"
    hill_cypher = HillCypher(plain_text, key)
    hill_cypher.encrypt_text()