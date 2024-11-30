'use strict'

document.getElementById('submitUserButton').addEventListener('click', () => {
  const userName = document.getElementById('nameInput').value;
  const nation = document.getElementById('nationSelect').value

  fetch(`http://127.0.0.1:5000/get_country?country=${nation}`)
  .then(response => response.json())
  .then(data => {
    console.log(data); // 查看返回的 JSON 数据
    const { name, initial_capa_value } = data;
    document.getElementById('initial-status').innerHTML =
      `Spy ${userName}! <br>
      You have pledged allegiance to ${name},<br>
      Your country's capacity value is ${initial_capa_value}.<br>
      YOU HAVE TO ACHIEVE 200 FOR THE FINAL VICTORIES.`;
  })
  .catch(error => console.error('Error fetching data:', error));
})
