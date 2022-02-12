Código desenvolvido em python que com base no clima alerta se haverá necessidade de levar guarda-chuva para a cidade informada.

O nome do arquivo é "umbrela.py" e deve ser executado com um compilador python. O código possui integração com o serviço "Current weather data" 
da API publica "OpenWeatherMap" (mais informações em https://openweathermap.org).

Para chamada ao serviço foi necessário cria uma conta para obter uma chave ("API key") a qual é necessaria para a chamada do serviço.

O parâmetro necessário para execução do código é o nome da cidade. Caso seja digitado uma cidade inexistente será apresentado uma mensagem de erro.

Caso a API retorne que já está chovendo, o que podemos identificar através do atributo "weather.main" (mais informações em https://openweathermap.org/weather-conditions)
quando o mesmo apresenta algum dos seguintes valores "Thunderstorm", "Drizzle", "Rain", o sistema irá apresentar a mensagem "Está chovendo. Por favor leve um guarda-chuva".

Caso o valor do atributo "weather.main" seja diferente dos acima informados, será utilizado outro critério que leva em consideração a umidade e pressão atmosférica.

Se a umidade estiver alta (acima de 90%) e a pressão estivar baixa (abaixo de 1015 hPa) há grande probabilidade de chuva e o sistema irá apresentar
a mensagem "Provavelmente irá chover. Por favor leve um guarda-chuva".

Agora se nenhum dos dois critérios acima forem atendidos o sistema irá apresentar a mensagem "Hoje você não precisa levar um guarda-chuva".

Além da informação da necessidade ou não de se levar um guarda-chuva o sistema também irá apresentar as seguintes informações complementares:
- Nome da cidade / Sigla do país
- Temperatura em Celsius
- Umidade do ar
- Pressão atmosférica
- Condição do tempo
