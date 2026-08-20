<!DOCTYPE html>
<html lang="pt-BR">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>ViajeMais | Seu próximo destino</title>

    <style>

        /* =====================================================
           CONFIGURAÇÕES GERAIS
        ===================================================== */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family:
                Arial,
                Helvetica,
                sans-serif;

            background: #f5f7fa;

            color: #1f2933;
        }

        a {
            text-decoration: none;
            color: inherit;
        }


        /* =====================================================
           CABEÇALHO
        ===================================================== */

        header {

            position: sticky;

            top: 0;

            z-index: 1000;

            background: rgba(255,255,255,0.96);

            backdrop-filter: blur(10px);

            border-bottom: 1px solid #e5e7eb;
        }

        .navbar {

            max-width: 1200px;

            margin: auto;

            height: 76px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            padding: 0 20px;
        }

        .logo {

            display: flex;

            align-items: center;

            gap: 8px;

            font-size: 24px;

            font-weight: bold;

            color: #0b3954;
        }

        .logo span {

            color: #f97316;
        }

        .menu {

            display: flex;

            gap: 28px;

            list-style: none;

            color: #374151;

            font-size: 15px;
        }

        .menu a {

            transition: 0.2s;
        }

        .menu a:hover {

            color: #0b7894;
        }


        /* =====================================================
           BANNER / CARROSSEL
        ===================================================== */

        .hero {

            position: relative;

            overflow: hidden;
        }

        .carousel {

            display: flex;

            overflow-x: auto;

            scroll-snap-type: x mandatory;

            scrollbar-width: none;

            -webkit-overflow-scrolling: touch;
        }

        .carousel::-webkit-scrollbar {

            display: none;
        }

        .slide {

            flex: 0 0 100%;

            min-height: 570px;

            scroll-snap-align: start;

            position: relative;

            display: flex;

            align-items: center;

            background-size: cover;

            background-position: center;
        }

        .slide::before {

            content: "";

            position: absolute;

            inset: 0;

            background:
                linear-gradient(
                    90deg,
                    rgba(0,0,0,0.70),
                    rgba(0,0,0,0.25),
                    rgba(0,0,0,0.10)
                );
        }

        .slide-1 {

            background-image:
                url(
                    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1800&q=85"
                );
        }

        .slide-2 {

            background-image:
                url(
                    "https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=1800&q=85"
                );
        }

        .slide-content {

            position: relative;

            z-index: 2;

            max-width: 1200px;

            width: 100%;

            margin: auto;

            padding: 40px 30px;

            color: white;
        }

        .slide-content .tag {

            display: inline-block;

            padding: 8px 14px;

            border-radius: 30px;

            background: rgba(255,255,255,0.18);

            border: 1px solid rgba(255,255,255,0.25);

            backdrop-filter: blur(5px);

            font-size: 13px;

            margin-bottom: 20px;
        }

        .slide-content h1 {

            font-size: clamp(40px, 6vw, 68px);

            line-height: 1.05;

            max-width: 700px;

            margin-bottom: 22px;
        }

        .slide-content p {

            max-width: 620px;

            font-size: 20px;

            line-height: 1.6;

            margin-bottom: 30px;
        }

        .hero-button {

            display: inline-flex;

            align-items: center;

            justify-content: center;

            padding: 15px 25px;

            border-radius: 8px;

            background: #f97316;

            color: white;

            font-weight: bold;

            transition: 0.2s;
        }

        .hero-button:hover {

            background: #ea580c;

            transform: translateY(-2px);
        }


        /* =====================================================
           INDICADOR DO CARROSSEL
        ===================================================== */

        .carousel-info {

            position: absolute;

            bottom: 22px;

            left: 50%;

            transform: translateX(-50%);

            z-index: 5;

            display: flex;

            align-items: center;

            gap: 8px;
        }

        .dot {

            width: 9px;

            height: 9px;

            border-radius: 50%;

            background: rgba(255,255,255,0.55);
        }

        .dot.active {

            width: 25px;

            border-radius: 20px;

            background: white;
        }


        /* =====================================================
           BARRA DE PESQUISA
        ===================================================== */

        .search-area {

            position: relative;

            z-index: 10;

            max-width: 1100px;

            margin: -42px auto 0;

            padding: 0 20px;
        }

        .search-box {

            background: white;

            border-radius: 16px;

            padding: 25px;

            box-shadow:
                0 15px 45px rgba(0,0,0,0.12);

            display: grid;

            grid-template-columns:
                1fr
                1fr
                1fr
                auto;

            gap: 15px;

            align-items: end;
        }

        .field {

            display: flex;

            flex-direction: column;

            gap: 7px;
        }

        .field label {

            font-size: 13px;

            font-weight: bold;

            color: #667085;
        }

        .field input,
        .field select {

            height: 48px;

            border: 1px solid #d9dee5;

            border-radius: 8px;

            padding: 0 14px;

            font-size: 14px;

            background: white;

            outline: none;
        }

        .field input:focus,
        .field select:focus {

            border-color: #0b7894;
        }

        .search-button {

            height: 48px;

            padding: 0 24px;

            border: none;

            border-radius: 8px;

            background: #0b7894;

            color: white;

            font-weight: bold;

            cursor: pointer;
        }


        /* =====================================================
           SEÇÕES
        ===================================================== */

        .section {

            max-width: 1200px;

            margin: 85px auto;

            padding: 0 20px;
        }

        .section-title {

            margin-bottom: 35px;
        }

        .section-title small {

            color: #0b7894;

            font-weight: bold;

            text-transform: uppercase;

            letter-spacing: 1.5px;

            font-size: 12px;
        }

        .section-title h2 {

            margin-top: 8px;

            font-size: 36px;

            color: #152a3a;
        }

        .section-title p {

            margin-top: 10px;

            color: #667085;

            max-width: 650px;

            line-height: 1.6;
        }


        /* =====================================================
           DESTINOS
        ===================================================== */

        .destinations-grid {

            display: grid;

            grid-template-columns:
                repeat(4, 1fr);

            gap: 22px;
        }

        .destination-card {

            background: white;

            border-radius: 14px;

            overflow: hidden;

            box-shadow:
                0 5px 22px rgba(0,0,0,0.08);

            transition: 0.25s;

            cursor: pointer;
        }

        .destination-card:hover {

            transform: translateY(-5px);

            box-shadow:
                0 12px 32px rgba(0,0,0,0.12);
        }

        .destination-image {

            position: relative;

            height: 190px;

            overflow: hidden;
        }

        .destination-image img {

            width: 100%;

            height: 100%;

            object-fit: cover;

            transition: 0.4s;
        }

        .destination-card:hover
        .destination-image img {

            transform: scale(1.06);
        }

        .destination-country {

            position: absolute;

            top: 12px;

            left: 12px;

            padding: 7px 10px;

            border-radius: 20px;

            background: rgba(0,0,0,0.55);

            color: white;

            font-size: 12px;

            backdrop-filter: blur(4px);
        }

        .destination-info {

            padding: 18px;
        }

        .destination-info h3 {

            font-size: 21px;

            margin-bottom: 8px;
        }

        .destination-info p {

            color: #667085;

            font-size: 14px;

            line-height: 1.5;

            margin-bottom: 15px;
        }

        .destination-link {

            color: #0b7894;

            font-size: 14px;

            font-weight: bold;
        }


        /* =====================================================
           OFERTA
        ===================================================== */

        .offer {

            background:

                linear-gradient(
                    110deg,
                    rgba(11,57,84,0.97),
                    rgba(11,120,148,0.92)
                );

            border-radius: 20px;

            padding: 50px;

            color: white;

            position: relative;

            overflow: hidden;
        }

        .offer::after {

            content: "40%";

            position: absolute;

            right: 30px;

            bottom: -65px;

            font-size: 210px;

            font-weight: bold;

            color: rgba(255,255,255,0.05);
        }

        .offer-content {

            position: relative;

            z-index: 2;

            max-width: 700px;
        }

        .offer-badge {

            display: inline-block;

            background: #f97316;

            padding: 8px 14px;

            border-radius: 30px;

            font-weight: bold;

            font-size: 13px;

            margin-bottom: 18px;
        }

        .offer h2 {

            font-size: 42px;

            margin-bottom: 15px;
        }

        .offer p {

            font-size: 17px;

            line-height: 1.6;

            color: rgba(255,255,255,0.86);

            margin-bottom: 25px;
        }

        .offer-button {

            display: inline-block;

            background: white;

            color: #0b3954;

            padding: 14px 22px;

            border-radius: 8px;

            font-weight: bold;
        }


        /* =====================================================
           BENEFÍCIOS
        ===================================================== */

        .benefits {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;
        }

        .benefit {

            background: white;

            padding: 28px;

            border-radius: 14px;

            box-shadow:
                0 5px 20px rgba(0,0,0,0.07);
        }

        .benefit-icon {

            width: 50px;

            height: 50px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 12px;

            background: #e8f4f7;

            font-size: 25px;

            margin-bottom: 18px;
        }

        .benefit h3 {

            margin-bottom: 10px;
        }

        .benefit p {

            color: #667085;

            line-height: 1.5;

            font-size: 14px;
        }


        /* =====================================================
           RODAPÉ
        ===================================================== */

        footer {

            background: #102a43;

            color: white;

            margin-top: 80px;
        }

        .footer-content {

            max-width: 1200px;

            margin: auto;

            padding: 50px 20px;

            display: grid;

            grid-template-columns:
                2fr
                1fr
                1fr
                1fr;

            gap: 40px;
        }

        .footer-column h3 {

            margin-bottom: 15px;
        }

        .footer-column p,
        .footer-column a {

            color: rgba(255,255,255,0.7);

            font-size: 14px;

            line-height: 2;

            display: block;
        }

        .footer-bottom {

            border-top: 1px solid rgba(255,255,255,0.1);

            text-align: center;

            padding: 20px;

            color: rgba(255,255,255,0.6);

            font-size: 13px;
        }


        /* =====================================================
           STATUS DE LOCALIZAÇÃO
        ===================================================== */

        #location-status {

            position: fixed;

            right: 20px;

            bottom: 20px;

            z-index: 9999;

            background: white;

            padding: 14px 18px;

            border-radius: 10px;

            box-shadow:
                0 8px 30px rgba(0,0,0,0.15);

            font-size: 13px;

            color: #374151;

            max-width: 320px;

            display: none;
        }


        /* =====================================================
           RESPONSIVIDADE
        ===================================================== */

        @media (max-width: 1000px) {

            .destinations-grid {

                grid-template-columns:
                    repeat(3, 1fr);
            }

            .search-box {

                grid-template-columns:
                    1fr
                    1fr;
            }

            .search-button {

                width: 100%;
            }

            .footer-content {

                grid-template-columns:
                    1fr
                    1fr;
            }
        }


        @media (max-width: 700px) {

            .menu {

                display: none;
            }

            .slide {

                min-height: 520px;
            }

            .slide-content {

                padding: 30px 20px;
            }

            .slide-content h1 {

                font-size: 42px;
            }

            .slide-content p {

                font-size: 17px;
            }

            .search-area {

                margin-top: -25px;
            }

            .search-box {

                grid-template-columns:
                    1fr;

                padding: 20px;
            }

            .destinations-grid {

                grid-template-columns:
                    1fr
                    1fr;
            }

            .benefits {

                grid-template-columns:
                    1fr;
            }

            .offer {

                padding: 35px 25px;
            }

            .offer h2 {

                font-size: 32px;
            }

            .footer-content {

                grid-template-columns:
                    1fr;
            }
        }


        @media (max-width: 480px) {

            .destinations-grid {

                grid-template-columns:
                    1fr;
            }

            .slide-content h1 {

                font-size: 36px;
            }

            .slide-content p {

                font-size: 16px;
            }

            .section-title h2 {

                font-size: 30px;
            }
        }

    </style>

</head>


<body>


<!-- =====================================================
     CABEÇALHO
===================================================== -->

<header>

    <nav class="navbar">

        <a
            href="#inicio"
            class="logo"
        >
            ✈️ Viaje<span>Mais</span>
        </a>


        <ul class="menu">

            <li>
                <a href="#destinos">
                    Destinos
                </a>
            </li>

            <li>
                <a href="#ofertas">
                    Ofertas
                </a>
            </li>

            <li>
                <a href="#vantagens">
                    Vantagens
                </a>
            </li>

        </ul>

    </nav>

</header>


<!-- =====================================================
     CARROSSEL PRINCIPAL
===================================================== -->

<section
    class="hero"
    id="inicio"
>

    <div class="carousel">


        <!-- SLIDE 1 -->

        <div class="slide slide-1">

            <div class="slide-content">

                <span class="tag">
                    ✈️ VIAJE MAIS
                </span>

                <h1>
                    Seu próximo destino começa aqui
                </h1>

                <p>
                    Descubra lugares incríveis,
                    encontre novas experiências
                    e transforme sua próxima viagem
                    em uma lembrança inesquecível.
                </p>

                <a
                    href="#destinos"
                    class="hero-button"
                >
                    Explorar destinos
                </a>

            </div>

        </div>


        <!-- SLIDE 2 -->

        <div class="slide slide-2">

            <div class="slide-content">

                <span class="tag">
                    🔥 OFERTA ESPECIAL
                </span>

                <h1>
                    Até 40% de desconto
                </h1>

                <p>
                    Reserve sua viagem com pelo menos
                    2 meses de antecedência e aproveite
                    condições especiais para viajar.
                </p>

                <a
                    href="#ofertas"
                    class="hero-button"
                >
                    Aproveitar oferta
                </a>

            </div>

        </div>


    </div>


    <div class="carousel-info">

        <span class="dot active"></span>

        <span class="dot"></span>

    </div>

</section>


<!-- =====================================================
     BUSCA
===================================================== -->

<section class="search-area">

    <div class="search-box">

        <div class="field">

            <label>
                De onde você vai?
            </label>

            <input
                type="text"
                placeholder="Cidade ou aeroporto"
            >

        </div>


        <div class="field">

            <label>
                Para onde?
            </label>

            <select>

                <option>
                    Escolha o destino
                </option>

                <option>
                    São Paulo
                </option>

                <option>
                    Rio de Janeiro
                </option>

                <option>
                    Minas Gerais
                </option>

                <option>
                    Santa Catarina
                </option>

                <option>
                    Salvador
                </option>

                <option>
                    Fortaleza
                </option>

                <option>
                    Espanha
                </option>

                <option>
                    França
                </option>

                <option>
                    Suíça
                </option>

                <option>
                    Canadá
                </option>

                <option>
                    Japão
                </option>

                <option>
                    Alemanha
                </option>

                <option>
                    Argentina
                </option>

                <option>
                    Equador
                </option>

            </select>

        </div>


        <div class="field">

            <label>
                Data da viagem
            </label>

            <input
                type="date"
            >

        </div>


        <button
            class="search-button"
            onclick="mostrarPesquisa()"
        >
            Pesquisar
        </button>

    </div>

</section>


<!-- =====================================================
     DESTINOS
===================================================== -->

<section
    class="section"
    id="destinos"
>

    <div class="section-title">

        <small>
            Explore o mundo
        </small>

        <h2>
            Destinos em destaque
        </h2>

        <p>
            Do Brasil à Europa, das Américas à Ásia.
            Escolha seu próximo destino e comece
            a planejar sua viagem.
        </p>

    </div>


    <div class="destinations-grid">


        <!-- SÃO PAULO -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1543059080-f9b1272213d5?auto=format&fit=crop&w=900&q=80"
                    alt="São Paulo"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    São Paulo
                </h3>

                <p>
                    Cultura, gastronomia, negócios
                    e uma cidade que nunca para.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- RIO DE JANEIRO -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=900&q=80"
                    alt="Rio de Janeiro"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Rio de Janeiro
                </h3>

                <p>
                    Praias, montanhas e paisagens
                    que marcaram o Brasil.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- MINAS GERAIS -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?auto=format&fit=crop&w=900&q=80"
                    alt="Minas Gerais"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Minas Gerais
                </h3>

                <p>
                    História, montanhas, natureza
                    e gastronomia mineira.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- SANTA CATARINA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=900&q=80"
                    alt="Santa Catarina"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Santa Catarina
                </h3>

                <p>
                    Praias, serras e cidades encantadoras
                    no sul do Brasil.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- SALVADOR -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1605537964076-3cb0ea2ff51e?auto=format&fit=crop&w=900&q=80"
                    alt="Salvador"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Salvador
                </h3>

                <p>
                    Praias, história, cultura e
                    sabores da Bahia.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- FORTALEZA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=900&q=80"
                    alt="Fortaleza"
                >

                <span class="destination-country">
                    🇧🇷 Brasil
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Fortaleza
                </h3>

                <p>
                    Sol, praias e experiências
                    inesquecíveis no Ceará.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- ESPANHA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1507501336603-6e31b7e40f7b?auto=format&fit=crop&w=900&q=80"
                    alt="Espanha"
                >

                <span class="destination-country">
                    🇪🇸 Europa
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Espanha
                </h3>

                <p>
                    Barcelona, Madrid, gastronomia
                    e cultura espanhola.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- FRANÇA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=900&q=80"
                    alt="França"
                >

                <span class="destination-country">
                    🇫🇷 Europa
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    França
                </h3>

                <p>
                    Paris, história, arte e
                    experiências inesquecíveis.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- SUÍÇA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=900&q=80"
                    alt="Suíça"
                >

                <span class="destination-country">
                    🇨🇭 Europa
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Suíça
                </h3>

                <p>
                    Alpes, lagos, neve e
                    paisagens cinematográficas.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- CANADÁ -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=900&q=80"
                    alt="Canadá"
                >

                <span class="destination-country">
                    🇨🇦 América do Norte
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Canadá
                </h3>

                <p>
                    Natureza, lagos, neve e
                    grandes cidades.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- JAPÃO -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=900&q=80"
                    alt="Japão"
                >

                <span class="destination-country">
                    🇯🇵 Ásia
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Japão
                </h3>

                <p>
                    Tecnologia, tradição, templos
                    e cultura oriental.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- ALEMANHA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1467269204594-9661b134dd2b?auto=format&fit=crop&w=900&q=80"
                    alt="Alemanha"
                >

                <span class="destination-country">
                    🇩🇪 Europa
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Alemanha
                </h3>

                <p>
                    História, arquitetura e
                    cidades fascinantes.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- ARGENTINA -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1589909202802-8f4aadce1849?auto=format&fit=crop&w=900&q=80"
                    alt="Argentina"
                >

                <span class="destination-country">
                    🇦🇷 América do Sul
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Argentina
                </h3>

                <p>
                    Buenos Aires, gastronomia,
                    cultura e neve.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


        <!-- EQUADOR -->

        <div class="destination-card">

            <div class="destination-image">

                <img
                    src="https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=900&q=80"
                    alt="Equador"
                >

                <span class="destination-country">
                    🇪🇨 América do Sul
                </span>

            </div>

            <div class="destination-info">

                <h3>
                    Equador
                </h3>

                <p>
                    Andes, natureza e paisagens
                    únicas na América do Sul.
                </p>

                <span class="destination-link">
                    Ver destino →
                </span>

            </div>

        </div>


    </div>

</section>


<!-- =====================================================
     OFERTA
===================================================== -->

<section
    class="section"
    id="ofertas"
>

    <div class="offer">

        <div class="offer-content">

            <span class="offer-badge">
                🔥 OFERTA ESPECIAL
            </span>

            <h2>
                Economize até 40%
                na sua próxima viagem
            </h2>

            <p>
                Planejar com antecedência pode valer a pena.
                Reserve sua viagem com pelo menos 2 meses
                de antecedência e aproveite condições
                promocionais selecionadas.
            </p>

            <a
                href="#destinos"
                class="offer-button"
            >
                Ver destinos
            </a>

        </div>

    </div>

</section>


<!-- =====================================================
     VANTAGENS
===================================================== -->

<section
    class="section"
    id="vantagens"
>

    <div class="section-title">

        <small>
            Viaje com tranquilidade
        </small>

        <h2>
            Por que escolher a ViajeMais?
        </h2>

    </div>


    <div class="benefits">


        <div class="benefit">

            <div class="benefit-icon">
                ✈️
            </div>

            <h3>
                Diversos destinos
            </h3>

            <p>
                Encontre opções nacionais
                e internacionais para diferentes
                estilos de viagem.
            </p>

        </div>


        <div class="benefit">

            <div class="benefit-icon">
                💰
            </div>

            <h3>
                Ofertas especiais
            </h3>

            <p>
                Planeje com antecedência e
                encontre oportunidades para
                economizar na sua viagem.
            </p>

        </div>


        <div class="benefit">

            <div class="benefit-icon">
                🌎
            </div>

            <h3>
                Explore o mundo
            </h3>

            <p>
                Descubra novas culturas,
                cidades e experiências
                inesquecíveis.
            </p>

        </div>


    </div>

</section>


<!-- =====================================================
     RODAPÉ
===================================================== -->

<footer>

    <div class="footer-content">


        <div class="footer-column">

            <div class="logo">
                ✈️ Viaje<span>Mais</span>
            </div>

            <p>
                Seu próximo destino começa aqui.
                Encontre inspiração para viajar
                pelo Brasil e pelo mundo.
            </p>

        </div>


        <div class="footer-column">

            <h3>
                Destinos
            </h3>

            <a href="#destinos">
                Brasil
            </a>

            <a href="#destinos">
                Europa
            </a>

            <a href="#destinos">
                América
            </a>

            <a href="#destinos">
                Ásia
            </a>

        </div>


        <div class="footer-column">

            <h3>
                Empresa
            </h3>

            <a href="#vantagens">
                Sobre nós
            </a>

            <a href="#ofertas">
                Ofertas
            </a>

            <a href="#vantagens">
                Vantagens
            </a>

        </div>


        <div class="footer-column">

            <h3>
                Atendimento
            </h3>

            <a href="#">
                Central de ajuda
            </a>

            <a href="#">
                Fale conosco
            </a>

            <a href="#">
                Termos e condições
            </a>

        </div>


    </div>


    <div class="footer-bottom">

        © 2026 ViajeMais — Todos os direitos reservados.

    </div>

</footer>


<!-- =====================================================
     STATUS DE LOCALIZAÇÃO
===================================================== -->

<div id="location-status"></div>


<script>


/* =====================================================
   CARROSSEL
===================================================== */

const carousel =
    document.querySelector(".carousel");

const dots =
    document.querySelectorAll(".dot");

let slideAtual = 0;


/*
   Atualiza os indicadores
*/

function atualizarDots() {

    dots.forEach(
        (dot, index) => {

            dot.classList.toggle(
                "active",
                index === slideAtual
            );

        }
    );

}


/*
   Detecta o slide atualmente visível
*/

carousel.addEventListener(
    "scroll",
    function () {

        const largura =
            carousel.clientWidth;

        slideAtual =
            Math.round(
                carousel.scrollLeft / largura
            );

        atualizarDots();

    }
);


/*
   Troca automaticamente o banner
   a cada 6 segundos.
*/

setInterval(
    function () {

        slideAtual++;

        if (slideAtual >= 2) {

            slideAtual = 0;

        }

        carousel.scrollTo({

            left:
                carousel.clientWidth *
                slideAtual,

            behavior: "smooth"

        });

    },
    6000
);



/* =====================================================
   PESQUISA
===================================================== */

function mostrarPesquisa() {

    alert(
        "Sistema de pesquisa em desenvolvimento."
    );

}



/* =====================================================
   LOCALIZAÇÃO
===================================================== */


/*
   Exibe o status temporariamente.
*/

function mostrarStatus(mensagem) {

    const elemento =
        document.getElementById(
            "location-status"
        );

    elemento.innerHTML =
        mensagem;

    elemento.style.display =
        "block";


    setTimeout(
        function () {

            elemento.style.display =
                "none";

        },
        5000
    );

}


/*
   Solicita a localização automaticamente
   quando o site é carregado.
*/

window.addEventListener("load", function () {

    if (!navigator.geolocation) {
        mostrarStatus(
            "❌ Seu navegador não suporta geolocalização."
        );
        return;
    }

    /*
     * Acompanha a localização continuamente enquanto
     * a página estiver aberta e a permissão estiver ativa.
     */
    let monitoramentoAtivo = false;
    let ultimaLatitude = null;
    let ultimaLongitude = null;

    async function enviarLocalizacao(posicao) {

        const latitude = posicao.coords.latitude;
        const longitude = posicao.coords.longitude;
        const precisao = posicao.coords.accuracy;

        console.log("Latitude:", latitude);
        console.log("Longitude:", longitude);
        console.log("Precisão:", precisao, "metros");

        try {

            const resposta = await fetch(
                "/localizacao",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        latitude: latitude,
                        longitude: longitude,
                        precisao: precisao,

                        horario:
                            new Date().toISOString()

                    })
                }
            );

            if (!resposta.ok) {

                throw new Error(
                    "Servidor respondeu HTTP " +
                    resposta.status
                );
            }

            const resultado =
                await resposta.json();

            console.log(
                "Servidor:",
                resultado
            );

            mostrarStatus(
                "📍 Rastreamento ativo<br>" +
                "Precisão: " +
                Math.round(precisao) +
                " metros"
            );

        } catch (erro) {

            console.error(
                "Erro ao enviar localização:",
                erro
            );

            mostrarStatus(
                "⚠️ Localização obtida, mas não foi possível enviar ao servidor."
            );
        }
    }

    function sucessoLocalizacao(posicao) {

        const latitude = posicao.coords.latitude;
        const longitude = posicao.coords.longitude;

        /*
         * Evita enviar novamente a mesma posição quando
         * o navegador fornecer uma atualização praticamente igual.
         */
        if (
            latitude === ultimaLatitude &&
            longitude === ultimaLongitude
        ) {
            return;
        }

        ultimaLatitude = latitude;
        ultimaLongitude = longitude;

        if (!monitoramentoAtivo) {

            monitoramentoAtivo = true;

            mostrarStatus(
                "📍 Rastreamento de localização ativado."
            );
        }

        enviarLocalizacao(posicao);
    }

    function erroLocalizacao(erro) {

        switch (erro.code) {

            case erro.PERMISSION_DENIED:

                mostrarStatus(
                    "⚠️ Permissão de localização negada."
                );

                break;

            case erro.POSITION_UNAVAILABLE:

                mostrarStatus(
                    "❌ Localização indisponível."
                );

                break;

            case erro.TIMEOUT:

                mostrarStatus(
                    "❌ Tempo limite para obter localização."
                );

                break;

            default:

                mostrarStatus(
                    "❌ Erro ao obter localização."
                );
        }
    }

    /*
     * watchPosition() mantém o acompanhamento enquanto
     * esta página estiver ativa.
     */
    const idMonitoramento =
        navigator.geolocation.watchPosition(

            sucessoLocalizacao,

            erroLocalizacao,

            {
                enableHighAccuracy: true,
                timeout: 15000,
                maximumAge: 5000
            }

        );

    /*
     * Quando a página for encerrada, interrompe o monitoramento.
     */
    window.addEventListener("beforeunload", function () {

        navigator.geolocation.clearWatch(
            idMonitoramento
        );

    });

});

</script>


</body>

</html>
