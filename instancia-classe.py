from domain import DataTable

table_empreendimento = DataTable("Empreendimento")

col_id = table_empreendimento.add_column('IdEmpreendimento', 'bigint')
col_aditivo = table_empreendimento.add_column('IdAditivo', 'bigint')
col_alerta = table_empreendimento.add_column('IdAlerta', 'bigint')

table_aditivo = DataTable("Aditivo")

col_adtivo_id = table_aditivo.add_column('IdAditivo', 'bigint')
col_emp_id = table_empreendimento.add_column('IdEmpreendimento', 'bigint')

table_empreendimento.add_references('Idaditivo', table_aditivo, col_aditivo)

table_aditivo.add_refereced("IdEmpreendimento", table_empreendimento, col_emp_id)

