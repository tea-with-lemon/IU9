import React, { Component } from 'react';
import logo from '../logo.svg';
import '../App.css';

class HomePage extends Component {
    constructor(){
        super();
        this.state = {
            msg : 'Hello, World!'
        }
    }

    componentDidMount(){
        this.setState({msg:"new"});
        fetch("/test")
            .then(data=>data.json())
            .then(json => this.setState({msg:JSON.stringify(json)}))
            .catch(err => alert(err))
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <p>
                        Edit <code>src/App.js</code> and save to reload.
                    </p>
                    <a
                        className="App-link"
                        href="https://reactjs.org"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {this.state.msg}
                    </a>
                    <button onClick={()=>this.setState({msg:"new msg"})}>baton</button>
                </header>
            </div>
        );
    }
}

export default HomePage;
