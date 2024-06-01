function getRandomScenarios(category, count) {
  const shuffled = category.slice();
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled.slice(0, count);
}

function fetchAndRender() {
  fetch('../json/all_scenarios.json')
    .then(response => response.json())
    .then(data => {
      const categories = ["static", "tracking", "target-switching"];
      const categoryMapping = {
        "Clicking": "static",
        "Tracking": "tracking",
        "Target Switching": "target-switching"
      };

      categories.forEach(category => {

        const filteredScenarios = data.filter(s => s.scenario && s.scenario.aimType && categoryMapping[s.scenario.aimType] === category);

        if (filteredScenarios.length === 0) {
          const placeholders = document.querySelectorAll(`.${category} span`);
          placeholders.forEach(placeholder => {
            placeholder.textContent = "Click the button to generate the scenarios!";
          });
          return;
        }

        const randomScenarios = getRandomScenarios(filteredScenarios, 3);

        const placeholders = document.querySelectorAll(`.${category} span`);
        placeholders.forEach((placeholder, index) => {
          placeholder.textContent = randomScenarios[index].scenarioName;
        });
      });
    })
    .catch(error => {
      console.error('Error fetching JSON:', error);
    });
}

document.querySelector('.btn').addEventListener('click', fetchAndRender);

