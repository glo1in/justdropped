fetch('top10_drops.json')
  .then(response => response.json())
  .then(drops => {
    const container = document.getElementById('drop-list');
    drops.forEach(drop => {
      const card = document.createElement('div');
      card.className = 'drop-card';
      card.innerHTML = `
        <img src="${drop.image}" alt="${drop.name}" width="200" /><br>
        <strong>${drop.name}</strong><br>
        Release Date: ${new Date(drop.release_date).toLocaleString()}<br>
        <a href="${drop.url}" target="_blank">More Info</a><br>
        <button onclick="subscribe('${drop.name}', '${drop.release_date}')">Notify Me</button>
      `;
      container.appendChild(card);
    });
  });

function subscribe(name, date) {
  const email = prompt("Enter your email to get alerts:");
  if (email) {
    fetch('https://your-backend.com/subscribe', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, name, date })
    });
    alert("Subscribed!");
  }
}
