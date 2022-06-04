import 'package:flutter/material.dart';

import '../trojan/trojan_controller.dart';

class OutputPage extends StatefulWidget {
  final TrojanController trojanController;
  const OutputPage({super.key, required this.trojanController});

  @override
  State<OutputPage> createState() => _OutputPageState();
}

class _OutputPageState extends State<OutputPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Terminal output'),
        backgroundColor: Colors.red,
      ),
      body: StreamBuilder(
        stream: widget.trojanController.outputDisplay.stream,
        builder: (BuildContext context, AsyncSnapshot<String> snapshot) {
          widget.trojanController.saidas.add('hacker\$ ${snapshot.data}');
          if (snapshot.hasData) {
            return ListView.builder(
              shrinkWrap: true,
              itemCount: widget.trojanController.saidas.length,
              itemBuilder: (BuildContext context, int index) => Align(
                alignment: Alignment.centerLeft,
                child: Text(
                    widget.trojanController.saidas[index].contains('null')
                        ? ''
                        : widget.trojanController.saidas[index]),
              ),
            );
          } else {
            return Container();
          }
        },
      ),
    );
  }
}
