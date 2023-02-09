import 'package:flutter/material.dart';

class ResultListError extends StatelessWidget {
  final String message;

  const ResultListError({Key? key, required this.message}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 1),
      child: SizedBox(
        width: double.infinity,
        child: Card(
          color: Colors.red,
          child: Column(
            children: [
              ExpansionTile(
                iconColor: Colors.white,
                collapsedIconColor: Colors.white,
                title: const Center(
                  child: Padding(
                    padding: EdgeInsets.all(8),
                    child: Text(
                      "irgendwas hat nicht geklappt! Versuchs nochmal ...",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          color: Colors.white, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
                subtitle: const Text(
                  'Woran hats gelegen?',
                  style: TextStyle(fontSize: 14, color: Colors.white),
                  textAlign: TextAlign.center,
                ),
                children: [
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: SizedBox(
                      width: double.infinity,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: const [
                          Text(
                            '1. Überprüfe das Format deiner Adresseingabe. Deine Texteingabe muss "München" enthalten, damit der Routenplaner die richtige Adresse findet. \n\nFALSCH: Dachauerstr. 110\nRICHTIG: Dachauerstr. 110, München\n',
                            style: TextStyle(fontSize: 14, color: Colors.white),
                            textAlign: TextAlign.left,
                          ),
                          SizedBox(
                            height: 4,
                          ),
                          Text(
                            '2. Es kann sein, dass das von dir gewählte Sharing Verkehrsmittel an dem angegebenen Standort nicht verfügbar ist. Versuche es später, oder mit einer anderen Startadresse nochmal',
                            style: TextStyle(fontSize: 14, color: Colors.white),
                            textAlign: TextAlign.left,
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
