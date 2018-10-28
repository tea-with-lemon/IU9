import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Switch , Route} from 'react-router-dom';
import HomePage from "./components/HomePage";

class App extends Component {
    render(){
        return (
            <div>
                <Switch>
                    <Route exact path="/" component={HomePage}/>
                </Switch>
            </div>
        )
    }
}

export default App;
