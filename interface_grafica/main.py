import PySimpleGUI as sg

sg.theme('LightBlue3')

# Definição do Layout Padrão do Projeto
frame_inicial = []

frame_layout_1 = [
    [sg.Text('Escolha um arquivo do formato padrão.')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button('Executar'), sg.Button('Limpar')]]

frame_layout_2 = [
    [sg.Text('Gerar dados automatico pelo programa.')],
    [sg.Text('Deseja ordenar de maior para menor espaço usado?')],
    [sg.Spin([i for i in range(1, 201)], initial_value=1),
     sg.Text('Quantide de usuários')],
    [sg.Text('Escolha o caminho para salvar o arquivo gerado:')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Checkbox('Sim'), sg.Checkbox('Não')],
    [sg.Text('Como você deseja o relatório?')],
    [sg.Checkbox('CSV'), sg.Checkbox('TXT'),
     sg.Checkbox('HTML'), sg.Checkbox('PDF')],
    [sg.Button('Executar'), sg.Button('Limpar')]]

layout = [[sg.Text('Projeto Controle de Cotas de Disco')],
          [sg.Text('_'*60)],
          [sg.Frame('Opção 1', frame_layout_1)],
          [sg.Text('_'*60)],
          [sg.Frame('Opção 2', frame_layout_2)],
          [sg.Text('_'*60)],
          [sg.Button('Quit')]]

# Criação do codigo da janela
window = sg.Window('ACME Inc - Controle de Cotas de Disco', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()
