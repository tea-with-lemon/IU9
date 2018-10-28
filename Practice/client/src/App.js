import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Switch , Route} from 'react-router-dom';
import HomePage from "./components/HomePage";
import StudentsPage from "./components/StudentsPage";

class App extends Component {
    render(){
        return (
            <div>
                <Switch>
                    <Route exact path="/" component={HomePage}/>
                    <Route path="/students" component={StudentsPage}/>
                </Switch>
            </div>
        )
    }
}

export default App;
