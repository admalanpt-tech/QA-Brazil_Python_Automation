from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from helpers import retrieve_phone_code

class UrbanRoutesPage:
    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Chamar Taxi
    call_a_taxi_button = (By.XPATH, '//button[text()="Chamar um táxi"]')

    #Tarifas
    comfort_tariff_option = (By.XPATH,'//div[@class="tcard-title" and text()="Comfort"]')
    current_tariff        = (By.XPATH,'//div[@class="tcard active"]//div[@class="tcard-title"]')

    #Numero de Telefone
    add_phone_number_main_button = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Número de telefone")]')
    phone_number_input_field     = (By.ID,    'phone')
    phone_number_next_button     = (By.XPATH, '//button[text()="Próximo"]')
    phone_code_field             = (By.ID,    'code')
    phone_number_confirm_button  = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    registered_phone_number      = (By.XPATH, '//div[contains(@class, "np-text")]')


    #Metodo de Pagamento
    payment_methode_button = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Método de pagamento")]')
    add_card_option_button = (By.XPATH, '//div[contains(text(), "Adicionar cartão")]')
    card_number_input      = (By.ID,    'number')
    card_code_input        = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    final_add_card_button  = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    current_payment_method  = (By.XPATH,'//div[contains(@class, "pp-value-text")]')


    #Adicionar Comentário. Pedir cobertor, leçóis e sorvete.
    message_for_driver_field               = (By.ID, 'comment')
    blanket_and_handkerchiefs_option_div   = (By.XPATH, "//div[contains(text(), 'Cobertor e lençóis')]/following-sibling::div[1]/div")
    blanket_and_handkerchiefs_option_input = (By.XPATH, "//div[contains(text(), 'Cobertor e lençóis')]/following-sibling::div[1]/div/input")
    add_icecream_buton                     = (By.XPATH, "//div[text()='Sorvete']/following::div[contains(@class, 'counter-plus')][1]")
    current_icecream_amount_field          = (By.XPATH, "//div[text()='Sorvete']/following::div[contains(@class, 'counter-value')][1]")

    #Confirmação do Pedido
    order_button  = (By.XPATH, '//div[contains(@class, "smart-button")]')
    order_timer   = (By.XPATH, '//div[contains(@class, "order-header-time")]')

    #Inicialização
def __init__(self, driver):
        # Inicializa a página e configura a espera padrão dos elementos
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Utilitários
def _find(self, locator):
        # Encontra um elemento na tela aguardando até que ele exista
        return self.wait.until(EC.presence_of_element_located(locator))

def _click(self, locator):
        # Espera o elemento ficar clicável antes de executar o clique
        self.wait.until(EC.element_to_be_clickable(locator)).click()

def _type(self, locator, text):
        # Limpa o campo e digita o texto informado
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

def _get_value(self, locator):
        # Lê o valor atual de um campo de entrada
        return self._find(locator).get_attribute('value')

def _get_text(self, locator):
        # Lê o texto visível de um elemento da página
        return self._find(locator).text

def _press_tab(self):
        # Pressiona TAB no elemento que está com foco
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    #Endereços
def set_route_addresses(self, from_address, to_address):
        # Preenche os endereços de origem e destino ("De" e "Para") da corrida
        self._type(self.FROM_FIELD, from_address)
        self._type(self.TO_FIELD, to_address)

def get_from_field_text(self):
        # Retorna o conteúdo atual do campo "De"
        return self._get_value(self.FROM_FIELD)

def get_to_field_text(self):
        # Retorna o conteúdo atual do campo "Para"
        return self._get_value(self.TO_FIELD)

    #Táxi
def click_call_a_taxi_button(self):
        # Clica no botão "Chamar um táxi"
        self._click(self.CALL_A_TAXI_BUTTON)

    #Tarifas
def click_comfort_option(self):
        # Seleciona a tarifa "Comfort"
        self._click(self.COMFORT_TARIFF_OPTION)

def get_selected_tariff_option(self):
        # Mostra qual tarifa está selecionada no momento
        return self._get_text(self.CURRENT_TARIFF)

    #Telefone
        # Fluxo do set_phone:
        # 1. Clica em "Adicionar telefone"
        # 2. Digita o número
        # 3. Clica em "Próximo"
        # 4. Recupera o código com o método do helper
        # 5. Digita o código
        # 6. Clica em "Confirmar"

def set_phone(self, phone_number):

        #Passo 1 : Abrir o formulário de telefone.
        self._click(sel.ADD_PHONE_NUMBER_MAIN_BUTTON)
        # Passo 2: Digitar o número informado no teste.
        self._type(self.PHONE_NUMBER_INPUT_FIELD, phone_number)
        # Passo 3: Avançar para a etapa de confirmação.
        self._click(self.PHONE_NUMBER_NEXT_BUTTON)
        # Passo 4: Recuperar o código exibido nos logs da aplicação.
        phone_code = retrieve_phone_code(self.driver)
        # Passo 5: Digitar o código recebido.
        self._type(self.PHONE_CODE_FIELD, phone_code)
        # Passo 6: Confirmar o telefone cadastrado.
        self._click(self.PHONE_NUMBER_CONFIRM_BUTTON)

def get_inserted_phone_number(self):
        # Retorna o telefone exibido após a confirmação
        return self._get_text(self.REGISTERED_PHONE_NUMBER)

    #Pagamento
        # Fluxo do set_card:
        # 1. Abre a janela de pagamento
        # 2. Escolhe adicionar um novo cartão
        # 3. Digita o número do cartão
        # 4. Digita o código de segurança
        # 5. Pressiona TAB para validar o formulário
        # 6. Confirma o cadastro do cartão

def set_card(self, card_number, card_code):

        # Passo 1: Abrir a área de métodos de pagamento.
        self._click(self.PAYMENT_METHOD_BUTTON)
        # Passo 2: Escolher a opção de adicionar cartão.
        self._click(self.ADD_CARD_OPTION_BUTTON)
        # Passo 3: Preencher o número do cartão.
        self._type(self.CARD_NUMBER_INPUT, card_number)
        # Passo 4: Preencher o código de segurança.
        self._type(self.CARD_CODE_INPUT, card_code)
        # Passo 5: Tirar o foco do campo para habilitar o botão de confirmação.
        self._press_tab()
        # Passo 6: Finalizar o cadastro do cartão.
        self._click(self.FINAL_ADD_CARD_BUTTON)

def get_current_payment_method(self):
        # Retorna a forma de pagamento atualmente selecionada
        return self._get_text(self.CURRENT_PAYMENT_METHOD)

    #Mensagem ao Motorista
def set_message_for_driver(self, message):
        # Preenche a mensagem personalizada que será enviada ao motorista
        self._type(self.MESSAGE_FOR_DRIVER_FIELD, message)

def get_message_for_driver(self):
        # Retorna a mensagem que está preenchida no campo
        return self._get_value(self.MESSAGE_FOR_DRIVER_FIELD)

    #Cobertor e Lençóis
def click_blanket_and_handkerchiefs_option(self):
        # Marca a opção de cobertor e lençóis para a corrida
        self._click(self.BLANKET_AND_HANDKERCHIEFS_OPTION_DIV)

def is_blanket_and_handkerchiefs_option_checked(self):
        # Verifica se a opção de cobertor e lençóis foi marcada
        return self._find(self.BLANKET_AND_HANDKERCHIEFS_OPTION_INPUT).is_selected()

    #Sorvete
        # Fluxo do add_icecream:
        # 1. Repete o clique no botão "+"
        # 2. Para de clicar quando atinge a quantidade esperada
def add_icecream(self, amount):
        for _ in range(amount):
            self._click(self.ADD_ICECREAM_BUTTON)

def get_current_icecream_amount(self):
        # Retorna a quantidade atual de sorvetes selecionados
        return int(self._get_text(self.CURRENT_ICECREAM_AMOUNT_FIELD).strip())

    #Pedido
def click_order_button(self):
        # Clica no botão final para pedir o carro
        self._click(self.ORDER_BUTTON)

def is_order_taxi_popup_displayed(self):
        # Verifica se o timer do pop-up de busca do carro apareceu na tela
        return self._find(self.ORDER_TIMER).is_displayed()












