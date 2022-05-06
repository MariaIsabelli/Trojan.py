import 'package:app_trojan/src/modules/trojan/trojan_page.dart';
import 'package:flutter/material.dart';

import '../src/modules/home/home_page.dart';
import 'animations/animated_page_route_builder_elastic_out.dart';

class Routes {
  static Route<dynamic>? routes(RouteSettings settings) {
    if (settings.name == '/home') {
      return MaterialPageRoute(
        builder: (BuildContext context) => const MyHomePage(),
      );
    } else if (settings.name == '/trojan') {
      return AnimatedPageRouteBuilderElasticOut(
        route: const TrojanPage(),
        duration: const Duration(milliseconds: 500),
      );
    } else {
      return null;
    }
  }
}
