# DataCity — Base sintética MongoDB

Projeto acadêmico: Ciência de Dados Aplicada à Mobilidade Urbana (cidade fictícia de Nova Esperança).

## Conteúdo
- regioes.json — 300 documentos (setores territoriais sintéticos)
- linhas.json — 1.200 documentos (linhas/serviços sintéticos)
- veiculos.json — 5.000 documentos
- viagens.json — 150.000 documentos
- ocorrencias.json — 25.000 documentos

**Total: 181.500 documentos.** Dados 100% fictícios, gerados para exercícios de análise e performance; não são estatísticas reais de qualquer município. Os volumes de linhas e frota são deliberadamente ampliados para testes acadêmicos e não representam uma rede de ônibus típica.

## Como importar
Requer MongoDB Database Tools (`mongoimport`) e um servidor MongoDB ativo. Os arquivos são arrays JSON, portanto use `--jsonArray`.

Execute os comandos no diretório onde estão os arquivos:

```bash
mongoimport --uri="mongodb://localhost:27017" --db=datacity_db --collection=regioes --file=regioes.json --jsonArray
mongoimport --uri="mongodb://localhost:27017" --db=datacity_db --collection=linhas --file=linhas.json --jsonArray
mongoimport --uri="mongodb://localhost:27017" --db=datacity_db --collection=veiculos --file=veiculos.json --jsonArray
mongoimport --uri="mongodb://localhost:27017" --db=datacity_db --collection=ocorrencias --file=ocorrencias.json --jsonArray
mongoimport --uri="mongodb://localhost:27017" --db=datacity_db --collection=viagens --file=viagens.json --jsonArray
```

Para MongoDB Atlas, substitua a URI por sua connection string. **Não publique credenciais** no GitHub nem compartilhe capturas com senhas.

## Relacionamentos lógicos
- linhas.regiao_id -> regioes._id
- veiculos.linha_id -> linhas._id
- viagens.linha_id -> linhas._id
- viagens.veiculo_id -> veiculos._id
- viagens.regiao_id -> regioes._id
- viagens.ocorrencia_id -> ocorrencias._id (pode ser null)
- ocorrencias.viagem_id -> viagens._id
- ocorrencias.linha_id -> linhas._id

`_id` usa strings estáveis, e não ObjectId. `data` e `data_hora` usam Extended JSON (`{"$date":"...Z"}`), e localizações usam GeoJSON Point com [longitude, latitude]. A ocorrência é opcional e há no máximo uma por viagem neste dataset.

## Criar índices (mongosh)
```javascript
use datacity_db
db.linhas.createIndex({regiao_id:1})
db.veiculos.createIndex({linha_id:1})
db.viagens.createIndex({data:1})
db.viagens.createIndex({linha_id:1,data:1})
db.viagens.createIndex({veiculo_id:1})
db.viagens.createIndex({ocorrencia_id:1})
db.ocorrencias.createIndex({viagem_id:1})
db.ocorrencias.createIndex({localizacao:"2dsphere"})
db.regioes.createIndex({geom:"2dsphere"})
```

## Consultas de validação (mongosh)
```javascript
db.regioes.countDocuments({})
db.linhas.countDocuments({})
db.veiculos.countDocuments({})
db.viagens.countDocuments({})
db.ocorrencias.countDocuments({})

db.viagens.aggregate([
  {$group:{_id:"$linha_id",atraso_medio:{$avg:"$atraso_minutos"},total_viagens:{$sum:1}}},
  {$sort:{atraso_medio:-1}},
  {$limit:10}
])

db.viagens.aggregate([
  {$group:{_id:"$regiao_id",passageiros_registrados:{$sum:"$passageiros"}}},
  {$sort:{passageiros_registrados:-1}},
  {$limit:10}
])
```

## Convenções e cuidados
- Atraso zero significa viagem sem atraso; `duracao_minutos` inclui atraso e `duracao_prevista_minutos` representa duração-base.
- `passageiros` é uma contagem sintética de passageiros registrada por viagem, não identifica pessoas únicas.
- `avaliacao_media` é uma nota sintética entre 1 e 5.
- Algumas linhas estão suspensas e veículos podem estar em manutenção no cadastro; viagens históricas foram geradas para linhas ativas, mas status do veículo é um retrato cadastral, não histórico.
- Os números e correlações são simulados e **não** sustentam decisões reais de transporte público.
- Evite executar importações repetidas sem limpar as coleções: `_id` duplicado provocará erros.
