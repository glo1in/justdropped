fetch('/top10_drops.json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Failed to fetch JSON: ${response.status}`);
    }
    return response.json();
  })
  .then(drops => {
    console.log("Loaded drops:", drops);
    const container = document.getElementById('drop-list');
    if (!Array.isArray(drops) || drops.length === 0) {
      container.innerHTML = '<p>No drops available.</p>';
      return;
    }

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
  })
  .catch(error => {
    console.error("Error loading drop data:", error);
    document.getElementById('drop-list').innerHTML = '<p>Error loading drops.</p>';
  });
