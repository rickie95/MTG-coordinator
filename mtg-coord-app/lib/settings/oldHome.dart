import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

final String serverURL = "http://192.168.1.68:5000";

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  List<String> entries = <String>['empty'];

  Future<void> fetchPlayers() async {
    final response = await http.get(serverURL + '/players');

    if (response.statusCode == 200) {
      print(response.body);
      entries.clear();
      for (String elem in json.decode(response.body)){
        entries.add(elem);
      }
      print(entries);
    }else {
      print("response wasn't good");
      throw Exception('Failed to load album');
    }
  }


  void _refreshPlayersList() {
    setState(() {
      //IO.Socket socket = IO.io('http://192.168.1.68:5000', <String, dynamic>{
      //  'transports': ['websocket'],
      //  'autoConnect': true
      //});
      //socket.emit('fromApp', 'hello');
      try{
        fetchPlayers();
      }catch(ex) {
        print(ex);
      }
    });
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: ListView.builder(
        itemCount: entries.length,
        itemBuilder: (BuildContext context, int index) {
          return Container(
            height: 50,
            child: Center(child: Text(entries[index])),
          );
        },
      ),

      floatingActionButton: FloatingActionButton(
        onPressed: _refreshPlayersList,
        tooltip: 'Increment',
        child: Icon(Icons.refresh),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}