from collections import namedtuple

ExecucaoFinanceira = namedtuple('ExecucaoFinanceira', ['IdExecucoFinanceira', 'IdEmpreendimento', 'IdInstituicaoContrato',
                                                       'IdLicitacao', 'ValContrato', 'ValTotal', 'DatAssinatura', 'DatInicioVigencia',
                                                       'DatFinalVigencia'])

execucao = ExecucaoFinanceira('1', '2', '123', '-1', '76', '0', '19/03/2010', '23/03/2010', '05/10/2013')

print('Valor do contrato', execucao.ValContrato,'\n')
print(execucao)

print('\n', execucao.DatAssinatura)