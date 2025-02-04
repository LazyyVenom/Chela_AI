let soundWaveHeights = [];
let initialized = false;

function sound_wave() {
    const container = document.getElementById("sound_wave");
    
    if (!initialized) {
        for (let i = 0; i < 50; i++) {
            let initialHeight;
            if (i < 5 || i >= 45) {
                initialHeight = Math.floor(Math.random() * 10) + 20; // Smaller initial height for starting and ending elements
            } else {
                initialHeight = Math.floor(Math.random() * 100) + 50;
            }
            soundWaveHeights.push(initialHeight);
            container.innerHTML += `<canvas id="soundWaveCanvas${i}" class="soundWaveCanvas" width="7" height="${initialHeight}" style="margin-right:2px;"></canvas>`;
        }
        initialized = true;
        return;
    }
    
    for (let i = 0; i < 50; i++) {
        let delta = Math.floor(Math.random() * 21) - 10; // Increased deviation range
        let newHeight = soundWaveHeights[i] + delta;
        
        newHeight = Math.max(20, Math.min(150, newHeight));
        soundWaveHeights[i] = newHeight;
        
        let canvas = document.getElementById("soundWaveCanvas" + i);
        canvas.height = newHeight;
    }
}

setInterval(sound_wave, 20);