# UI Art Director

**Uma skill de IA para criar interfaces com identidade e cuidado visual.**

[English](README.md) · [Skill](skills/ui-art-director/SKILL.md) · [Casos de avaliação](evals/cases.json) · [MIT](LICENSE)

A UI Art Director orienta um agente de programação na direção visual, implementação, inspeção do resultado e refinamento. Aplica-se a sites, aplicações web, aplicações móveis e de desktop e HUDs de jogos, adaptando as decisões ao produto.

Um portefólio expressivo, uma ferramenta de trabalho com muitos dados e um HUD de combate precisam de soluções diferentes. A skill procura essa adequação, em vez de repetir sempre o mesmo estilo.

## O que inclui

- Direção visual concreta para trabalhos de maior dimensão.
- Composição, hierarquia e tipografia antes dos pormenores decorativos.
- Orientações específicas para sites, aplicações e HUDs.
- Análise de referências e orientações específicas para dashboards.
- Um módulo de animação com ritmo, sequências, interrupção e redução de movimento.
- Inspeção da interface renderizada quando existem ferramentas para isso.
- Correções baseadas em problemas observados e um ponto claro de conclusão.
- Um processo para evoluir a skill através de feedback e avaliações comparáveis.

É uma skill de instruções no formato [Agent Skills](https://agentskills.io/specification). A qualidade depende do modelo, do contexto, dos recursos e das ferramentas disponíveis. Não promete perfeição nem aprendizagem automática infinita.

## Instalar no Codex

Descarrega ou clona o repositório e copia a pasta **completa** `skills/ui-art-director` para:

| Âmbito | Destino |
| --- | --- |
| Projeto atual | `.agents/skills/ui-art-director/` dentro do projeto |
| Todos os teus projetos | `~/.agents/skills/ui-art-director/` |

No Windows, a localização pessoal é normalmente `%USERPROFILE%\.agents\skills\ui-art-director`.

Mantém as pastas `references/` e `agents/` e a `LICENSE` junto do `SKILL.md`. Revê uma instalação existente antes de a substituir. O Codex deteta alterações; se a skill não aparecer, reinicia-o. Consulta a [documentação oficial da OpenAI](https://learn.chatgpt.com/docs/build-skills) para os locais de descoberta.

O formato também pode ser usado por outros agentes compatíveis, seguindo as instruções de instalação de cada um. Esta versão inicial ainda não foi testada em vários agentes.

## Usar

```text
Usa $ui-art-director para melhorar esta aplicação. Mantém as funcionalidades
e a tecnologia atual. Define uma direção visual coerente, implementa-a e
verifica o resultado nos tamanhos de ecrã suportados.
```

```text
Usa $ui-art-director para melhorar este HUD. Dá prioridade à leitura durante
o jogo, mantém a zona da mira livre e preserva o suporte de comando.
```

```text
Usa $ui-art-director para polir este formulário. Mantém a identidade atual;
melhora o espaçamento, os rótulos, o foco e as mensagens de erro.
```

A seleção automática está ativa nos agentes que a suportam quando o pedido corresponde à descrição. A skill não se aplica a tarefas exclusivamente de backend.

## Melhorar continuamente

O processo é **compreender → definir → construir → inspecionar → refinar → verificar**. Cada tarefa tem um fim. As decisões aceites podem ficar no registo de design do projeto para orientar trabalhos seguintes. A skill pública deve evoluir com falhas demonstradas e comparações, sem transformar o gosto de um projeto numa regra para todos.

## Estado e validação

A versão **0.2.0** ainda está numa fase inicial. A validação verifica a estrutura, os metadados, as ligações locais e a integridade dos casos de avaliação. Não mede qualidade estética nem prova que um modelo segue sempre as instruções.

Para executar as verificações, usa Python 3.10 ou superior:

```text
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
```

Estas dependências servem apenas para validar o repositório. A utilização da skill não exige Python, telemetria, serviços externos ou outras skills.

Existem [casos de avaliação](evals/README.md) para orientar testes reais. Ainda são necessárias comparações visuais renderizadas dos resultados de agentes; não são apresentados resultados de qualidade estética.

## Demonstração de animações

Descarrega e abre [motion-lab.html](skills/ui-art-director/assets/motion-lab.html) num navegador moderno. Inclui três exemplos originais: revelação de um título com máscara, entradas em sequência e um painel que acompanha cliques repetidos durante a transição. Experimenta também a opção de reduzir movimento.

O ficheiro funciona sozinho, sem bibliotecas externas. Os tempos são exemplos ajustáveis. O [registo de verificação](evals/motion-lab-checks.md) descreve os comportamentos observados e os limites dos testes. As [notas das fontes](skills/ui-art-director/references/tutorial-sources.md) identificam os tutoriais enviados pelo utilizador, as partes analisadas e as adaptações. A referência de animação usa After Effects; a skill adapta os princípios ao comportamento de interfaces interativas.

## Contribuir e licença

As instruções de contribuição estão em [CONTRIBUTING.md](CONTRIBUTING.md). Envia apenas exemplos, capturas e dados que possam ser partilhados publicamente.

Licença [MIT](LICENSE). Os recursos de terceiros usados nos projetos mantêm as respetivas licenças.
