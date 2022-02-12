Código desenvolvido em python para alertar sofre o clima e se ha necessidade de levar guarda chuva para a cidade informada.

O nome do arquivo é "umbrela.py" e deve ser executado com um compilador python, o código possui integração com o serviço "Current weather data" 
da API publica "OpenWeatherMap" (mais informações em https://openweathermap.org).

Para chamada a o serviço foi necessario cria uma conta para obter um chave a qual é necessaria para a chamada do serviço.

O parametro necessario para execução do código é o nome da cidade. Caso seja digitado uma cidade inexistente será apresentado uma mensagem de erro.

Se a API retornar que já chovendo que pode ser identificado atraves do atributo "weather.main" (mais informações em https://openweathermap.org/weather-conditions),
onde foram considerados os valores "Thunderstorm", "Drizzle", "Rain", o sistema irá apresentar a mensagem "Está chovendo por favor leve um guarda chuva".

Caso o valor do atributo "weather.main" seja diferente dos acima informados, será utilizado outro critério que leva em consideração a umidade e pressão atmosferica.

Se a umidade estiver alta (acima de 90%) e a pressão estivar baixa (abaixo de 1015 hPa) há grande probabilidadede chuva e o sistema irá apresentar
a mensagem "Provavelmente irá chover, por favor leve um guarda chuva".

Agora se nenhum dos dois critérios acima forem atendidos o sistema irá apresentar a mensagem "Hoje você não precisa levar um guarda chuva".

Além da informação da necessidade ou não de se levar um guarda-chuva o sistema também irá apresentar as seguintes informações complementares:
- Nome da cidade / Sigla do país
- Temperatura em Celsius
- Umidade do ar
- Pressão atmosférica
- Condição do tempo
