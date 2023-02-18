from selenium.webdriver.chrome.options import Options
def DefineOpcoesChrome():
    opcoes = CriaClasseOpcoes()
    OpcaoTelaMaximizada(opcoes)
    OpcaoDiretorioDownload(opcoes)
    return opcoes

def CriaClasseOpcoes():
    return Options()

def OpcaoTelaMaximizada(opcoes):
    opcoes.add_argument('--start-maximized')


def OpcaoDiretorioDownload(opcoes):
    perfil = {
        'download.default_directory': r'C:\Users\T-Gamer\Desktop\projetos\HackathonVincixRPA\Arquivos Excel',
    }
    opcoes.add_experimental_option('prefs', perfil)