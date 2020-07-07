import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

final String serverURL = "http://192.168.1.68:5000";

class LifeCounterPage extends StatefulWidget {
  LifeCounterPage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _LifeCounterPageState createState() => _LifeCounterPageState();
}

class _LifeCounterPageState extends State<LifeCounterPage> {
  void pippoCallback() {
    print("the guy still thinks that this button isn't a dummy one");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        child: Column(
          mainAxisSize: MainAxisSize.max,
          children: <Widget>[
            Expanded(
              child: ListView(
              padding: EdgeInsets.zero,
              children: <Widget>[
                DrawerHeader(
                  child:  Column(
                    children: <Widget>[
                      Expanded(
                        child: Text('MTG Organizer')
                      ),
                      Container(
                          child: Align(
                            alignment: FractionalOffset.bottomRight,
                            // This container holds all the children that will be aligned
                            // on the bottom and should not scroll with the above ListView
                            child:  Container(
                              child: Column(
                                children: <Widget>[
                                  ListTile(
                                    leading: Icon(Icons.account_circle, color: Colors.white,),
                                    title: Text('John Doe', style: TextStyle(color: Colors.white),),
                                  )
                                  /*
                                  Text('John Doe', style: TextStyle(color: Colors.white),)
                                  */
                                ],
                              ),
                            ),
                          ),
                      ),
                    ],
                  ),
                  decoration: BoxDecoration(
                    color: Colors.blue,
                  ),
                ),
                ListTile(
                  leading: Icon(Icons.favorite),
                  title: Text('Life Counter'),
                  onTap: () {
                    // Update the state of the app.
                    // ...
                  },
                ),
                ListTile(
                  leading: Icon(Icons.people),
                  title: Text('Tournament'),
                  onTap: () {
                    // Update the state of the app.
                    // ...
                  },
                ),
                ListTile(
                  leading: Icon(Icons.person),
                  title: Text('My Profile'),
                  onTap: () {
                    // Update the state of the app.
                    // ...
                  },
                ),
                ListTile(
                  leading: Icon(Icons.chat),
                  title: Text('Messages'),
                  onTap: () {
                    // Update the state of the app.
                    // ...
                  },
                ),
              ],
            ),

      ),
            Container(
              // This align moves the children to the bottom
              child: Align(
                  alignment: FractionalOffset.bottomCenter,
                  // This container holds all the children that will be aligned
                  // on the bottom and should not scroll with the above ListView
                  child:  Container(
                    child: Column(
                      children: <Widget>[
                        Divider(),
                        ListTile(
                            leading: Icon(Icons.settings),
                            title: Text('Settings'),
                            onTap: () {},
                        ),

                        ListTile(
                            leading: Icon(Icons.help),
                            title: Text('Help and Feedback'),
                          onTap: () {},
                        ),
                      ],
                    )
                )
              ),
            )
          ],
        ),
      ),
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(
        children: [
          Center(
            child: RaisedButton(
              child: Text("START A NEW MATCH"),
              onPressed: pippoCallback,
              textColor: Colors.white,
              color: Colors.indigo,
            ),
          ),
        ],
      ),
    );
  }
}
