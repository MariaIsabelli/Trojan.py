import 'package:flutter/material.dart';

import 'trojan_controller.dart';

class TrojanPage extends StatefulWidget {
  const TrojanPage({super.key});

  @override
  State<TrojanPage> createState() => _TrojanPageState();
}

class _TrojanPageState extends State<TrojanPage> {
  final TrojanController trojanController = TrojanController();

  @override
  void dispose() {
    trojanController.disposeForm();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final Size size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        title: const Text('App trojan ;)'),
        backgroundColor: Colors.red,
      ),
      body: Form(
        key: trojanController.formKey,
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: size.width * 0.1),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextFormField(
                controller: trojanController.textEditingControllerIp,
                keyboardType: TextInputType.number,
                validator: (String? value) {
                  if (value == null || value.isEmpty) {
                    return 'Campo não pode ficar vazio';
                  } else {
                    return null;
                  }
                },
                decoration: const InputDecoration(
                  labelText: 'Coloque o Ip',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(
                      Radius.circular(20),
                    ),
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.only(top: size.height * 0.1),
                child: TextFormField(
                  controller: trojanController.textEditingControllerPort,
                  keyboardType: TextInputType.number,
                  validator: (String? value) {
                    if (value == null || value.isEmpty) {
                      return 'Campo não pode ficar vazio';
                    } else {
                      return null;
                    }
                  },
                  decoration: const InputDecoration(
                    labelText: 'Coloque a porta',
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(
                        Radius.circular(20),
                      ),
                    ),
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.only(top: size.height * 0.1),
                child: ValueListenableBuilder(
                  valueListenable: trojanController.isConected,
                  builder: (BuildContext context, bool value, Widget? child) =>
                      ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(20.0),
                      ),
                      backgroundColor: value ? Colors.green : Colors.red,
                    ),
                    onPressed: () =>
                        trojanController.connectTrojan(context).then((value) {
                      if (value) {
                        Navigator.pushReplacementNamed(context, '/output',
                            arguments: trojanController);
                        trojanController.runTrojan();
                      }
                    }),
                    child: SizedBox(
                      height: size.height * 0.07,
                      child: Center(
                        child: Text(
                          value ? 'Conectado!!!' : 'Conectar',
                          style: const TextStyle(fontSize: 18),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
