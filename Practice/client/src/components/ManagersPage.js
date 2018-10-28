import React, { Component } from 'react';
import '../App.css';
import {Icon, Label, List, Menu, Table} from 'semantic-ui-react'
import UserEditForm from "./UserEditForm";
import AddStudentForm from "./AddStudentForm";
import Api from "./api";
import AddCompanyForm from "./AddCompanyForm";
import AddManagerForm from "./AddManagerForm";
import CompanyEditForm from "./CompanyEditForm";
import ManagerEditForm from "./ManagerEditForm";

class ManagersPage extends Component {
    constructor(){
        super();
        this.api = new Api();
        this.state = {
            managers: [],
            headers : ['Имя', 'Фамилия' ,'Отчество','Телефон','Почта','Компания','Идентификатор'],
            fields : ['FirstName','LastName','FName','Phone','Email', 'CompanyName','ManagerID'],
            showRedact : false,
            redactNmb : 0,
        };
        this.getManagers = this.getManagers.bind(this);
    }

    getManagers(){
        this.api.fetch('/manager/getall')
            .then(response=>{
                this.setState({managers:response.managers})
            }).catch(err => alert(err))
    }



    componentDidMount(){
        this.getManagers();
    }

    render() {
        const editForm = this.state.showRedact ? (
            <div><ManagerEditForm  manager={this.state.managers[this.state.redactNmb]} onSubmit={this.getManagers}/></div>
        ):(
            null
        );
        return (
            <div>
                <Table celled selectable>
                    <Table.Header>
                        <Table.Row>
                            <Table.HeaderCell>№</Table.HeaderCell>
                            {this.state.headers.map(header => {
                                return (
                                    <Table.HeaderCell>{header}</Table.HeaderCell>
                                )
                            })}
                        </Table.Row>
                    </Table.Header>
                    <Table.Body>
                        {this.state.managers.map((manager,index) => {
                            return <Table.Row onClick={()=>{
                                this.setState({showRedact:!this.state.showRedact,redactNmb:index});
                            }}>
                                <Table.Cell> {index+1} </Table.Cell>
                                {this.state.fields.map(field => {
                                    return <Table.Cell>
                                        {!!manager[field] ? manager[field] : ''}
                                    </Table.Cell>
                                })}
                            </Table.Row>
                        })}
                    </Table.Body>
                </Table>
                {editForm}
                <AddManagerForm onSubmit={this.getManagers}/>
            </div>
        );
    }
}

export default ManagersPage;
