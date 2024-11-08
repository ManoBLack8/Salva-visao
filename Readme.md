
# Projeto de Detecção Facial com Alerta Visual

Este projeto utiliza **OpenCV** e **MediaPipe** para detectar rostos em tempo real com a câmera do computador. Quando o rosto detectado ocupa uma grande área da tela (indicando proximidade da câmera), o programa exibe um alerta visual em tela cheia usando **Tkinter**, sobrepondo outras janelas temporariamente.

## Motivação

Este projeto tem o intuito de **proteger a visão das pessoas**, especialmente das crianças. Muitas vezes, os pais não conseguem monitorar a distância que as crianças mantêm em relação à tela, o que pode trazer danos à visão a longo prazo. Este projeto foi desenvolvido para alertar sobre essa proximidade excessiva, ajudando a reduzir os danos visuais e promovendo a saúde ocular do "nós" do futuro.

## Funcionalidades

- 📸 **Detecção de Rosto**: Detecta rostos em tempo real utilizando a biblioteca MediaPipe.
- 🟥 **Alerta Visual**: Exibe um retângulo ao redor do rosto detectado, que fica vermelho se o rosto estiver muito próximo.
- 🖥️ **Alerta de Tela Cheia**: Quando o rosto se aproxima excessivamente, um alerta em tela cheia é exibido, sobrepondo outras janelas, para chamar a atenção do usuário.

## Tecnologias Utilizadas

- **Python**
- **OpenCV** - para manipulação e exibição de vídeo
- **MediaPipe** - para detecção de rostos
- **Tkinter** - para exibir o alerta de tela cheia

## Requisitos

Antes de iniciar, instale as dependências do projeto:

```bash
pip install opencv-python mediapipe
```

## Como Executar

1. Clone o repositório e navegue até o diretório do projeto.
2. Execute o programa com o comando:

   ```bash
   python nome_do_arquivo.py
   ```

3. A câmera será ativada e o programa iniciará a detecção facial.
4. **Saia do programa** pressionando a tecla `q` na janela de vídeo.

## Criar um Executável

Para distribuir o programa sem precisar do Python instalado no sistema, você pode criar um executável com o **PyInstaller**:

1. Instale o PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:

   ```bash
   pyinstaller --onefile nome_do_arquivo.py
   ```

3. O executável será criado na pasta `dist`. Você pode adicionar um ícone personalizado com o parâmetro `--icon`:

   ```bash
   pyinstaller --onefile --icon=icone.ico nome_do_arquivo.py
   ```

Agora você terá um arquivo `.exe` que pode ser executado em qualquer sistema com o mesmo sistema operacional (Windows, macOS ou Linux).

## Estrutura do Código

- **Detecção de rosto**: Usa MediaPipe para detectar rostos e calcula a posição e tamanho do retângulo ao redor do rosto.
- **Lógica de alerta**: Verifica o tamanho do rosto detectado. Se exceder uma largura definida, exibe um alerta em tela cheia.
- **Exibição do tamanho**: O tamanho do rosto em pixels é exibido ao lado do rosto na imagem.

## Exemplo de Uso

Quando o rosto se aproxima da câmera e o retângulo de detecção fica vermelho, um alerta em tela cheia aparece com uma mensagem de aviso.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.