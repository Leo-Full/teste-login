# Testes de Login com Selenium + pytest

Projeto de automação de testes end-to-end (E2E) cobrindo os cenários positivo e negativo do fluxo de login, usando Python, Selenium WebDriver e pytest.

**Aplicação testada:** [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) (aplicação pública mantida pela Elemental Selenium para prática de automação).

## O que é testado

| Teste | Cenário | Resultado esperado |
|---|---|---|
| `test_login_com_sucesso` | Usuário e senha corretos | Redireciona para a área segura, exibindo "You logged into a secure area" |
| `test_login_com_senha_errada` | Usuário correto, senha incorreta | Permanece na tela de login, exibindo "Your password is invalid!" |

## Tecnologias

- **Python 3.14**
- **Selenium WebDriver** — automação do navegador
- **pytest** — framework de testes
- **webdriver-manager** — gerencia automaticamente a versão do ChromeDriver

## Como rodar

```bash
pip install selenium pytest webdriver-manager
python -m pytest test_login.py -v
```

## Decisões técnicas e aprendizados

- **Espera explícita, não `sleep()`**: os testes usam `WebDriverWait` com `expected_conditions` para aguardar o estado certo da página (mudança de URL, elemento visível), evitando testes lentos ou instáveis (*flaky tests*).
- **Elemento presente ≠ elemento visível**: a página possui um `<div id="flash-messages">` (container sempre presente, até vazio) e um `<div id="flash">` (a mensagem em si, só renderizada quando há sucesso/erro). Esperar pela *presença* do elemento errado gera falso positivo — a solução foi esperar explicitamente pela *visibilidade* do elemento correto (`id="flash"`).
- **Testes independentes**: cada função de teste cria e encerra sua própria instância do navegador, evitando dependência de estado entre execuções.

## Autor

Leonildo Neto
