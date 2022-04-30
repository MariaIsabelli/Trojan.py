import 'package:flutter/material.dart';
import 'home_controller.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final HomeController _homeController = HomeController();

  @override
  Widget build(BuildContext context) {
    final Size _size = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        title: const Text('App trojan ;)'),
        backgroundColor: Colors.red,
      ),
      body: Padding(
        padding: EdgeInsets.symmetric(horizontal: _size.width * 0.05),
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.only(top: _size.height * 0.01),
              child: const Text(
                'Esse app é um trojan simples mobile feito unicamente com fins de mostrar esse conhecimento.',
                style: TextStyle(fontSize: 18),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(top: _size.height * 0.05),
              child: const Text(
                '#ConhecimentoNãoÉCrime',
                style: TextStyle(fontSize: 20),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(
                  top: _size.height * 0.05, bottom: _size.height * 0.025),
              child: const Text(
                'Para executar o trojan basta clicar no botão inferior ao lado direto, ele basicamente vai se conectar a um ip e uma porta e permitir comandos remotos',
                style: TextStyle(fontSize: 18),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(
                  top: _size.height * 0.05, bottom: _size.height * 0.025),
              child: const Text(
                'Aqui a baixo estão todas as pessoas envolvidas com esse repositorio, se quiser estar aqui basta contribuir ;)',
                style: TextStyle(fontSize: 18),
              ),
            ),
            Expanded(
              child: GridView.builder(
                itemCount: _homeController.linkContributors.length,
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 3,
                  crossAxisSpacing: 10,
                  mainAxisSpacing: 10,
                ),
                itemBuilder: (BuildContext context, int index) => ClipRRect(
                  borderRadius: BorderRadius.circular(15),
                  child: Image.network(_homeController.linkContributors[index],
                      frameBuilder:
                          (context, child, frame, wasSynchronouslyLoaded) {
                    return child;
                  }, loadingBuilder: (context, child, loadingProgress) {
                    if (loadingProgress == null) {
                      return child;
                    } else {
                      return const Center(
                        child: CircularProgressIndicator(),
                      );
                    }
                  }),
                ),
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.pushNamed(context, '/trojan'),
        backgroundColor: Colors.red,
        child: const Center(
          child: Icon(Icons.play_arrow_outlined),
        ),
      ),
    );
  }
}
