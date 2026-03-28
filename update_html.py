import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Colors
text = text.replace('#050a15', '#FAF9F6')
text = text.replace('#ffffff', '#333333')
text = text.replace('rgba(255, 255, 255', 'rgba(51, 51, 51')
text = text.replace('#d4af37', '#e5a5b5')
text = text.replace('rgba(212, 175, 55', 'rgba(229, 165, 181')
text = text.replace('#ffb6c1', '#d47e95')
text = text.replace('rgba(26, 11, 46', 'rgba(250, 249, 246')

text = text.replace("background: linear-gradient(135deg, #1a0b2e 0%, #050a15 100%);", "background: linear-gradient(135deg, #f4edf0 0%, #faf9f6 100%);")
text = text.replace("background: linear-gradient(rgba(5, 10, 21, 0.85), rgba(26, 11, 46, 0.9)), url('https://images.unsplash.com/photo-1520764805728-48b4eeb2ce71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80') center/cover;", "background: transparent;")
text = text.replace("color: #f8f8f8 !important;", "color: #555555 !important;")
text = text.replace("color: #f8f8f8;", "color: #555555;")
text = text.replace("text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.8);", "text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8);")
text = text.replace("text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);", "text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.9);")

new_style = """
        /* --- TULIPÁN DE FONDO ANIMADO --- */
        #fondo-animado {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            max-width: 600px;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        #fondo-animado svg {
            width: 300px;
            height: 800px;
            overflow: visible;
        }

        .petal {
            transform-origin: 100px 248px;
            transition: transform 0.1s ease-out;
        }

        .section {
            backdrop-filter: blur(8px);
        }
"""
text = text.replace("</style>", new_style + "</style>")

svg_bg = """
    <!-- FONDO ANIMADO DE TULIPÁN -->
    <div id="fondo-animado">
        <svg viewBox="0 0 200 600" xmlns="http://www.w3.org/2000/svg">
            <path id="stem" d="M100,250 C100,350 95,550 95,600" stroke="#8CA274" stroke-width="5" fill="none" />
            <path id="leaf-left" d="M98,400 C60,350 45,250 40,200 C50,250 85,350 98,400" fill="#A8BA94" />
            <path id="leaf-right" d="M96,450 C130,400 145,300 150,260 C140,320 115,400 96,450" fill="#99AD83" />
            <g id="petalos">
                <path class="petal petal-back" d="M85,150 C80,100 100,90 100,90 C100,90 120,100 115,150 C110,195 90,195 85,150" fill="#EFD0D9" />
                <path class="petal petal-left" d="M100,245 C70,240 50,170 55,115 C65,120 75,160 95,245" fill="#ECAFC0" />
                <path class="petal petal-right" d="M100,245 C130,240 150,170 145,115 C135,120 125,160 105,245" fill="#EAB6C7" />
                <path class="petal petal-center" d="M80,160 C75,100 100,98 100,98 C100,98 125,100 120,160 C120,230 100,248 100,248 C100,248 80,230 80,160" fill="#FDEEED" />
            </g>
        </svg>
    </div>
"""

text = text.replace("<body>\n    <!--AQUI VA LA MUSICA-->", "<body>\n" + svg_bg + "\n    <!--AQUI VA LA MUSICA-->")

js_animation = """
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            const docHeight = Math.max(
                document.body.scrollHeight, document.documentElement.scrollHeight,
                document.body.offsetHeight, document.documentElement.offsetHeight,
                document.body.clientHeight, document.documentElement.clientHeight
            );
            const windowHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
            const maxScroll = Math.max(1, docHeight - windowHeight);
            
            const progress = Math.min(scrollY / Math.max(1, maxScroll * 0.9), 1);

            const back = document.querySelector('.petal-back');
            const left = document.querySelector('.petal-left');
            const right = document.querySelector('.petal-right');
            const center = document.querySelector('.petal-center');

            if(back) back.style.transform = `translate(${progress * 20}px, ${progress * 150}px) rotate(${progress * -15}deg)`;
            if(left) left.style.transform = `translate(${progress * -50}px, ${progress * 200}px) rotate(${progress * -40}deg)`;
            if(right) right.style.transform = `translate(${progress * 60}px, ${progress * 180}px) rotate(${progress * 35}deg)`;
            if(center) center.style.transform = `translate(${progress * 10}px, ${progress * 220}px) rotate(${progress * 15}deg)`;
        });
"""

text = text.replace("</script>\n</body>", js_animation + "</script>\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated HTML.")
