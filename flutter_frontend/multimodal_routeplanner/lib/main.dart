import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner_page.dart';
import 'package:multimodal_routeplanner/02_application/bloc/cost_details_bloc.dart';
import 'package:multimodal_routeplanner/02_application/bloc/diagram_type_bloc.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_planner/advanced_route_planner_bloc.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_planner_bloc.dart';

import '02_application/bloc/route_info_bloc.dart';
import '02_application/bloc/visualization_bloc.dart';
import 'theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Route Planner',
        theme: AppTheme.lightTheme,
        darkTheme: AppTheme.darkTheme,
        themeMode: ThemeMode.light,
        debugShowCheckedModeBanner: false,
        home: MultiBlocProvider(providers: [
          BlocProvider(
            create: (BuildContext context) => RoutePlannerBloc(),
          ),
          BlocProvider(
            create: (BuildContext context) => VisualizationBloc(),
          ),
          BlocProvider(
            create: (BuildContext context) => CostDetailsBloc(),
          ),
          BlocProvider(
            create: (BuildContext context) => DiagramTypeBloc(),
          ),
          BlocProvider(
            create: (BuildContext context) => RouteInfoBloc(),
          ),
          BlocProvider(
            create: (BuildContext context) => AdvancedRoutePlannerBloc(),
          ),
        ], child: const AdvancedRoutePlannerPage()));
  }
}
