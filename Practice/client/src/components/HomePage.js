import React, { Component } from 'react';
import logo from '../logo.svg';
import '../App.css';
import {Tab} from "semantic-ui-react";
import StudentsPage from "./StudentsPage";
import CompaniesPage from "./CompaniesPage";
import ManagersPage from "./ManagersPage";
import PracticePage from "./PracticePage";
import GroupPage from "./GroupPage";

class HomePage extends Component {
    constructor(){
        super();
        this.panes = [
            { menuItem: 'Студенты', render: () => <Tab.Pane attached={false}><StudentsPage/></Tab.Pane> },
            { menuItem: 'Компании', render: () => <Tab.Pane attached={false}><CompaniesPage/></Tab.Pane> },
            { menuItem: 'Руководители', render: () => <Tab.Pane attached={false}><ManagersPage/></Tab.Pane> },
            { menuItem: 'Практика', render: () => <Tab.Pane attached={false}><PracticePage/></Tab.Pane> },
            { menuItem: 'Группы', render: () => <Tab.Pane attached={false}><GroupPage/></Tab.Pane> },
        ]
    }
    render() {
        return (
            <Tab menu={{pointing:true}} panes={this.panes}/>
        );
    }
}

export default HomePage;
