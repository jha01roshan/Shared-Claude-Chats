# Asterisk-AGI-Skript: Einrichtung und Ausführung

- Source: https://grok.com/share/bGVnYWN5_0ed46786-78eb-4b69-a7a9-7661a151842d
- Created: 2025-03-10
- Messages: 2

---

## Human

Ich brauche eine Anleitung, was man alles beachten muss, damit dieses Asterisk-AGI-Skript läuft. Es muss ein Ordner mit Unterordner angelegt werden mit Schreibleseberechtigung. Das Python-Skript selbst braucht Bibliotheken, die mit pip zu installieren sind und wo (nicht in der Asterisk-Konsole), das AGI-Skript muss ausführbar sein und in welchen Ordner ist es zu kopieren. Habe ich was vergessen.

_Attachments: zeitansage_de_agi.py, 3677e48d-b899-4417-8128-edcde652b9ff_

---

## Assistant

Hier ist eine detaillierte Anleitung, was du beachten musst, damit das Asterisk-AGI-Skript erfolgreich läuft. Ich gehe Schritt für Schritt vor und berücksichtige alle genannten Punkte sowie weitere mögliche Stolpersteine:

---

### 1. **Voraussetzungen auf dem System**
- **Asterisk**: Das Skript ist für Asterisk geschrieben und benötigt eine funktionierende Asterisk-Installation (z. B. auf einem Linux-System wie Ubuntu oder CentOS).
- **Python 3**: Stelle sicher, dass Python 3 installiert ist (`python3 --version` im Terminal prüfen).
- **ffmpeg**: Das Skript verwendet `ffmpeg`, um MP3-Dateien in WAV-Dateien zu konvertieren. Installiere es mit:
  ```bash
  sudo apt install ffmpeg  # Für Debian/Ubuntu
  sudo yum install ffmpeg  # Für CentOS/RHEL
  ```
- **Asterisk-Soundpfad**: Das Skript speichert temporäre Audiodateien in `/usr/share/asterisk/sounds/test/`. Dieser Pfad muss existieren und beschreibbar sein.

---

### 2. **Erforderliche Python-Bibliotheken installieren**
Das Skript verwendet die Bibliothek `gTTS` (Google Text-to-Speech). Diese muss mit `pip` installiert werden. Wichtig: Dies geschieht **nicht in der Asterisk-Konsole**, sondern in einer normalen Shell (Terminal) auf dem System.

- Stelle sicher, dass `pip` für Python 3 installiert ist:
  ```bash
  sudo apt install python3-pip  # Für Debian/Ubuntu
  sudo yum install python3-pip  # Für CentOS/RHEL
  ```
- Installiere `gTTS`:
  ```bash
  pip3 install gtts
  ```
- Überprüfe die Installation:
  ```bash
  python3 -c "import gtts; print(gtts.__version__)"
  ```
  Wenn keine Fehlermeldung erscheint, ist die Bibliothek korrekt installiert.

---

### 3. **Ordnerstruktur und Berechtigungen anlegen**
Das Skript speichert Audiodateien in `/usr/share/asterisk/sounds/test/`. Du musst diesen Ordner anlegen und die richtigen Berechtigungen setzen:

- Erstelle den Ordner:
  ```bash
  sudo mkdir -p /usr/share/asterisk/sounds/test
  ```
- Setze die Berechtigungen, damit der Asterisk-Prozess (oft als Benutzer `asterisk` ausgeführt) schreiben und lesen kann:
  ```bash
  sudo chown asterisk:asterisk /usr/share/asterisk/sounds/test
  sudo chmod 775 /usr/share/asterisk/sounds/test
  ```
- Prüfe, ob der Asterisk-Benutzer korrekt ist (abhängig von deiner Installation könnte es ein anderer Benutzer sein, z. B. `root`):
  ```bash
  ps aux | grep asterisk
  ```
  Passe den Benutzer in `chown` entsprechend an, falls nötig.

---

### 4. **Skript ausführbar machen und kopieren**
- Speichere das Skript z. B. als `sprechende_uhr.py`.
- Mache es ausführbar:
  ```bash
  chmod +x spprechende_uhr.py
  ```
- Kopiere es in einen geeigneten Ordner. Üblicherweise werden AGI-Skripte in `/usr/share/asterisk/agi-bin/` abgelegt:
  ```bash
  sudo cp spprechende_uhr.py /usr/share/asterisk/agi-bin/
  sudo chown asterisk:asterisk /usr/share/asterisk/agi-bin/sprechende_uhr.py
  sudo chmod 755 /usr/share/asterisk/agi-bin/sprechende_uhr.py
  ```
- **Warum `/usr/share/asterisk/agi-bin/`?** Dies ist der Standardpfad, den Asterisk für AGI-Skripte durchsucht. Du kannst aber auch einen anderen Pfad verwenden, wenn du ihn in der Asterisk-Konfiguration (z. B. `extensions.conf`) explizit angibst.

---

### 5. **Asterisk-Konfiguration anpassen**
Damit das Skript von Asterisk aufgerufen wird, musst du es in der Dialplan-Konfiguration (`/etc/asterisk/extensions.conf`) einbinden. Beispiel:

```plaintext
[ext-local]
exten => 1234,1,NoOp(Starte Sprechende Uhr)
exten => 1234,n,AGI(/usr/share/asterisk/agi-bin/sprechende_uhr.py)
exten => 1234,n,Hangup()
```

- Erklärung:
  - Wähle die Nummer `1234` (oder eine andere), um das Skript zu starten.
  - `AGI()` ruft das Skript auf.
- Lade die Konfiguration neu:
  ```bash
  asterisk -rx "dialplan reload"
  ```

---

### 6. **Testen des Skripts**
- Starte Asterisk (falls nicht bereits aktiv):
  ```bash
  sudo systemctl start asterisk
  ```
- Verbinde dich mit der Asterisk-Konsole:
  ```bash
  asterisk -rvvv
  ```
- Wähle die konfigurierte Nummer (z. B. `1234`) über einen SIP-Client oder ein anderes Telefon.
- Prüfe die Ausgabe in der Konsole auf Fehler (z. B. fehlende Berechtigungen oder Bibliotheken).

---

### 7. **Mögliche Stolpersteine (Hast du was vergessen?)**
- **Internetverbindung**: `gTTS` benötigt eine Verbindung zu Google-Servern, um die Sprachdaten zu generieren. Ohne Internet funktioniert das Skript nicht.
- **Pfad zu Python 3**: Stelle sicher, dass `#!/usr/bin/env python3` auf deinem System Python 3 korrekt aufruft. Teste mit:
  ```bash
  /usr/bin/env python3 --version
  ```
- **Asterisk-Benutzerrechte**: Wenn Asterisk nicht als `asterisk`-Benutzer läuft, müssen die Berechtigungen entsprechend angepasst werden.
- **Fehlende Pakete**: Neben `gTTS` und `ffmpeg` sind keine weiteren Abhängigkeiten nötig, aber überprüfe, ob `os`, `sys`, `time`, `datetime` und `logging` (Standardbibliotheken) funktionieren.
- **Temporäre Dateien**: Das Skript löscht WAV-Dateien nach dem Abspielen, aber bei Abstürzen könnten Dateien übrig bleiben. Überwache den Ordner `/usr/share/asterisk/sounds/test/`.
- **Firewall**: Falls eine Firewall aktiv ist, stelle sicher, dass Asterisk und das Skript auf die benötigten Ports zugreifen können (SIP, AGI-Kommunikation).

---

### Zusammenfassung der Schritte
1. Installiere Python 3, `pip`, `gTTS` und `ffmpeg`.
2. Erstelle den Ordner `/usr/share/asterisk/sounds/test/` mit Schreib-/Leserechten für den Asterisk-Benutzer.
3. Mache das Skript ausführbar und kopiere es nach `/usr/share/asterisk/agi-bin/`.
4. Konfiguriere den Asterisk-Dialplan (`extensions.conf`).
5. Teste das Skript über eine Telefonverbindung.

Falls etwas fehlt oder unklar ist, lass es mich wissen!
