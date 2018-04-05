def validate(kind):
    if not kind in ('bigint', 'numeric', 'varchar'):
        raise Exception("Tipo inválido")

    