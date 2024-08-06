<h1>README.md для скрипта Hamster Kombat</h1>
<h1> project was writed using library "request" for sending http request for HamsterKombatAPI, soooo... Now - requests is outdated library, cause it's sync library. I think - we should use AIOHTTP in the next versions. Now im looking for transfer the project from the console to the web, that's all. Thank you for reading it! | S0ra - main developer </h1>
<p>Привет!</p>

<p>Этот скрипт для игры Hamster Kombat поможет вам очень быстро собрать все ваши коины. Пожелайте своим пальчикам удачи! Все, что вам нужно сделать:</p>
<ol>
    <li><strong>Установить Python</strong></li>
    <li><strong>Ввести в консоли всю энергию, которую израсходует скрипт</strong></li>
    <li><strong>Не забыть положить в <code>config.py</code> свой ключ авторизации!</strong></li>
</ol>

<p>Но давайте по порядку.</p>

<h2>Установка:</h2>

<ol>
    <li>
        <strong>Установка Python</strong>:
            <ul>
                <li><strong>Для Windows</strong>:
                    <ul>
                        <li>Зайдите на официальный сайт <a href="https://www.python.org/downloads/windows/">python.org</a>.</li>
                        <li>Скачайте последнюю версию инсталлятора для Windows и запустите его.</li>
                        <li>Убедитесь, что выбрана опция <strong>"Add Python to PATH"</strong>, и завершите установку.</li>
                    </ul>
                </li>
                <li><strong>Для Linux</strong>:
                    <p>Откройте терминал и выполните команды:</p>
                    <pre><code>sudo apt update
sudo apt install python3</code></pre>
                </li>
                <li><strong>Для Mac OS</strong>:
                    <p>Можно использовать <code>Homebrew</code>. Убедитесь, что он установлен, затем выполните:</p>
                    <pre><code>brew install python</code></pre>
                </li>
                <li><strong>Для Termux</strong>:
                    <p>Запустите Termux и выполните:</p>
                    <pre><code>pkg install python</code></pre>
                </li>
            </ul>
        </li>
        <li>
            <strong>Склонируйте репозиторий</strong>:
            <pre><code>git clone https://github.com/Yarous/HamsterKombat_abuser
cd HamsterKombat_abuser</code></pre>
        </li>
        <li>
            <strong>Установите все необходимые библиотеки</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
            <p>Или, если возникнут проблемы, попробуйте:</p>
            <pre><code>pip3 install -r requirements.txt</code></pre>
        </li>
</ol>

<h2>Теперь нам нужно найти ваш ключ авторизации. Для этого запустите Telegram в веб-версии.</h2>
    <img src="https://i.imgur.com/xShABl7.png" alt="Картинка для веб-версии Telegram">
    
<p>Перейдите в Hamster Kombat. Конечно, он не заработает просто так и будет жаловаться на то, что вы сидите с компьютера, но это легко обойти.</p>
<img src="https://i.imgur.com/eH2ApAB.png" alt="Картинка с жалобой о компьютере">

<h2>Запустите режим разработчика (DevTools).</h2>

<p>Кликните правой кнопкой мыши в любом месте на странице и выберите <em>Исследовать</em> или <em>Inspect</em>.</p>
<img src="https://i.imgur.com/n4fXc1P.png" alt="Картинка с открытием DevTools">

<p>Нажмите на значок с квадратом и мышью, затем наведитесь на окно игры.</p>
<img src="https://i.imgur.com/lJ5vq6x.png" alt="Первое изображение с наведением">
<img src="https://i.imgur.com/RJdCjgH.png" alt="Второе изображение с наведением">

<p>Теперь нажмите левую кнопку мыши и найдите тег <code>&lt;iframe&gt;</code> в коде. Скопируйте содержимое атрибута <code>src</code> (или можете искать ключ прямо в браузере, не копируя).</p>
<img src="https://i.imgur.com/GrDhMP5.png" alt="Первое изображение с тегом iframe">
<img src="https://i.imgur.com/Egzty9k.png" alt="Второе изображение с тегом iframe">

<p>Теперь дважды кликните по содержимому тега <code>src</code>, после чего вы сможете изменить его. Найдите строчку <code>tgWebAppPlatform=weba&amp;</code> и замените <code>weba</code> на <code>android</code> или <code>ios</code>.</p>
<img src="https://i.imgur.com/cyOP2W5.png" alt="Картинка с атрибутом tgWebAppPlatform">

<img src="https://i.imgur.com/mbcVzzG.png" alt="Картинка с изменением platform">

<p>Теперь нажмите на любое место в коде, кроме этого содержимого, чтобы применить изменения. Подождите немного — готово! Вы вошли в игру с компьютера.</p>
<img src="https://i.imgur.com/cxVngg0.png" alt="Картинка с успешным входом">

<p><strong>Не закрывайте инструменты разработчика!</strong></p>

<p>Лучше перейдите во вкладку <strong>Network</strong> и очистите её от запросов. В Firefox слева сверху есть кнопка <em>Clear</em>, а в браузерах на базе Chromium (Яндекс Браузер, Google Chrome, Opera и т.д.) нажмите <code>Ctrl + L</code>. Если не поможет, воспользуйтесь поиском в интернете.</p>

<h2>Теперь — ваше любимое занятие: потапайте хомяка, сколько угодно.</h2> 

<p>Как только вы остановитесь, подождите пару секунд — в <strong>Network</strong> должны появиться два запроса. Вам нужен тот, у которого в столбце <strong>Method</strong> указан <strong>POST</strong>.</p>
<img src="https://i.imgur.com/7zApXSg.png" alt="Первое изображение с методом POST">
<img src="https://i.imgur.com/HXAHTQn.png" alt="Второе изображение с методом POST">

<p>Нажмите на него, и справа у вас откроется информация о запросе. Перейдите в раздел <strong>Headers</strong>.</p>
<img src="https://i.imgur.com/clBBXyK.png" alt="Первое изображение с заголовками">

<p>В <strong>Request Headers</strong> должен быть заголовок <strong>authorization</strong>.</p>
<img src="https://i.imgur.com/qjbDNOC.png" alt="Картинка с заголовком authorization">

<p>Нажмите на него правой кнопкой мыши и выберите <em>Copy Value</em>.</p>
<img src="https://i.imgur.com/WbuFFRf.png" alt="Картинка с копированием значения">

<p>Готово — можно закрывать браузер, возвращаемся к программе!</p>

<h2>Теперь откройте <code>config.py</code> в любом текстовом редакторе или IDE</h2> 
<p>(Блокнот, VIM, Nano, Visual Studio Code, PyCharm и т.д.) и поместите между двумя двойными кавычками значение, которое вы скопировали, не забывая удалить <code>your_key</code>.</p>
<img src="https://i.imgur.com/c3i0qAe.png" alt="Первая картинка с редактированием config.py">
<img src="https://i.imgur.com/TmJaoXw.png" alt="Вторая картинка с редактированием config.py">
<img src="https://i.imgur.com/MjeLtuJ.png" alt="Третья картинка с редактированием config.py">

<h2>Запустите главный файл:</h2>
<pre><code>python main.py</code></pre>
<p>Или используйте <code>python3</code>, если у вас установлен именно этот командный интерпретатор:</p>
<pre><code>python3 main.py</code></pre>

<p>Вводите ваше максимальное значение энергии (заряженной) и нажмите <em>Enter</em>. Если вы все сделали правильно, вы можете обновить страницу с Hamster Kombat и посмотреть, прибавились ли коины. Также, обратите внимание на сообщения в консоли: если все правильно, вы получите поздравительное сообщение, если нет — сообщение об ошибке.</p>

<p>Вот и всё! Ждите дальнейших обновлений! А еще - смотрите больше красных панд!</p>
