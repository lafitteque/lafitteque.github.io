export default function generateWavePath(height, amplitude, frequency) {
    let path = "M0,0 ";
    const step = 5;
    for (let y = 0; y <= height-20; y += step) {
      const x = amplitude * Math.sin((2 * Math.PI * frequency * y) / 100);
      path += `L${x},${y} `;
    }
    return path;
  }
  // console.log("Coucou, je debugg la vaguelette")
  document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll('.wave-block');

    headers.forEach(header => {
      const uniqueId = header.id.slice(11);  // Récupère la partie unique de l'ID
      const content = document.querySelector(`#content-${uniqueId}`);
      const waveSvg = document.querySelector(`#dynamic-wave-${uniqueId}`);

      // console.log("avant la condition")
      if (content && waveSvg) {
        // console.log("la vaguelette est créée")
        const rect = content.getBoundingClientRect();
        const height = rect.height;
    
        const amplitude = 20; // Ajuster selon les besoins
        const frequency = 2.5;
    
        const pathData = generateWavePath(height, amplitude, frequency);
    
        waveSvg.setAttribute('viewBox', `-${amplitude} 0 ${2 * amplitude} ${height}`);
        waveSvg.setAttribute('height', height);
        waveSvg.innerHTML = `<path d="${pathData}" fill="none" stroke="#707070" stroke-width="2" />`;
      }
    });
  });
  
  