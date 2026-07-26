# Google Chrome instalou IA no seu computador sem avisar

- Source: https://claude.ai/share/86a59075-faaf-4c5d-8706-4e5926759452
- Author: Petr
- Created: 2026-05-06
- Messages: 2

---

## Human

Co je pravdivého na této informaci

O Google acabou de transformar mais de 1 bilhão de computadores em depósito de IA.  Inclusive o seu.  Sem pedir. Sem avisar. Sem um único popup.  O Chrome baixou 4GB de modelo de inteligência artificial no seu disco. O arquivo se chama weights.bin, são os pesos do Gemini Nano. Fica numa pasta chamada OptGuideOnDeviceModel dentro do seu perfil do Chrome.  Você não autorizou nada. Até existe uma configuração para impedir, mas tá enterrada em submenus que ninguém encontra. E as AI features vêm ligadas por padrão.  Se você deletar o arquivo, o Chrome baixa de novo. Sozinho. Em silêncio. Você decide o que fica no seu disco e o navegador simplesmente ignora.  Funciona assim em Windows, macOS e Ubuntu. Logs forenses no macOS mostram que o arquivo foi instalado dia 24 de abril de 2026, misturado com patches de segurança. Desenvolvedores dizem que isso já rola há mais de um ano.  E tem um detalhe que deixa tudo mais ridículo:  O Chrome 147 coloca um botão "AI Mode" na barra de endereço. Você vê aquilo, sabe que tem modelo de IA no seu computador, e assume que suas buscas rodam localmente.  Não rodam. O AI Mode é 100% cloud. Tudo vai para os servidores do Google. O modelo de 4GB no seu disco não tem nada a ver com aquele botão.  Ele serve para quê? "Help me write" e detecção de scam. Coisas que vivem em submenus de clique-direito que você provavelmente nunca abriu.  O Google ocupou 4GB do seu disco sem pedir, para rodar coisas que quase ninguém usa, enquanto a IA que você de fato vê manda tudo para a nuvem.  Na Europa, pesquisadores já apontam violação do Artigo 5(3) da Diretiva ePrivacy, que exige consentimento antes de armazenar software no dispositivo do usuário.  Como desativar:  → chrome://flags → Busque "Optimization Guide On Device Model" → Desative → Reinicie o Chrome → Delete a pasta OptGuideOnDeviceModel  Seu computador só é seu se você ficar de olho.

---

## Assistant

```
This block is not supported on your current device yet.
```

Tato informace je **převážně pravdivá**, ale obsahuje i několik zjednodušení nebo nepřesností. Zde je přehled:

---

## ✅ Co je pravda

**Soubor weights.bin a složka OptGuideOnDeviceModel skutečně existují.**
Chrome stahuje 4GB soubor s názvem `weights.bin` do složky `OptGuideOnDeviceModel` — jde o váhy modelu Gemini Nano, on-device jazykového modelu od Googlu.

**Stahování probíhá bez výslovného souhlasu.**
Stahování proběhne automaticky, jakmile Chrome vyhodnotí, že vaše zařízení splňuje hardwarové požadavky — bez žádosti o souhlas a bez jakéhokoliv oznámení.

**Pokud soubor smažete, Chrome ho stáhne znovu.**
Pokud soubor odstraníte nebo přejmenujete, Chrome ho automaticky obnoví při dalším spuštění prohlížeče.

**Funguje to na Windows, macOS i Ubuntu.**
Toto chování bylo potvrzeno na Windows 11, Apple Silicon a Ubuntu.

**AI Mode v adresním řádku používá cloud, ne lokální model.**
Složka s 4GB modelem neslouží pro hlavní AI funkce Chromu. AI Mode, který se zobrazuje v adresním řádku, běží na serverech Googlu, nikoliv z lokálně uložených vah.

**Lokální model slouží jen pro omezené funkce.**
Model Gemini Nano pohání funkce jako „Help me write" (asistence při psaní textu), on-device detekci podvodů a Summarizer API.

**Otázky ohledně GDPR/ePrivacy jsou oprávněné.**
Podle článku 5(3) evropské směrnice ePrivacy vyžaduje ukládání informací na zařízení uživatele „předchozí, svobodný, specifický, informovaný a jednoznačný souhlas."

---

## ⚠️ Co je zjednodušené nebo zavádějící

**Model není špionážní software.**
Tento soubor není spyware ani virus — ve skutečnosti chrání soukromí uživatele při používání AI funkcí, protože zpracování probíhá lokálně na zařízení bez odesílání dat do cloudu.

**Tvrzení o „skrytém nastavení" je přehnané.**
Nastavení v `chrome://flags` nebo v podnikových politikách existuje, ale jeho dostupnost závisí na verzi Chromu a platformě.

**„Smíchání s bezpečnostními záplatami"** — toto konkrétní tvrzení z virálních příspěvků není ověřitelné.

---

## 🔧 Jak to skutečně vypnout

Postup popsaný v příspěvku je v zásadě funkční:

1. Otevřete `chrome://flags`
2. Vyhledejte `Optimization Guide On Device Model`
3. Nastavte na `Disabled`
4. Restartujte Chrome
5. Smažte složku `OptGuideOnDeviceModel`

Na **Windows** je ještě spolehlivější metoda přes registr — nastavit klíč `GenAILocalFoundationalModelSettings` na hodnotu `1`.

---

**Shrnutí:** Jádro příběhu je pravdivé a představuje legitimní problém s ochranou soukromí. Virální příspěvek to však místy dramatizuje — model není malware, má reálné funkční využití a chování Googlu je spíše problém transparentnosti a souhlasu než záměrné škodlivosti.
