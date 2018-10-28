import React, { Component } from 'react';
import '../App.css';
import { Icon, Label, Menu, Table } from 'semantic-ui-react'
import UserEditForm from "./UserEditForm";
import AddStudentForm from "./AddStudentForm";
import Api from "./api";
import AddCompanyForm from "./AddCompanyForm";
import CompanyEditForm from "./CompanyEditForm";
import AddGroupForm from "./AddGroupForm";
import GroupEditForm from "./GroupEditForm";

class GroupPage extends Component {
    constructor(){
        super();
        this.api = new Api();
        this.state = {
            groups: [],
            headers : ['Имя', 'Фамилия' ,'Курс','Группа','Год','Компания','Бригадир'],
            fields : ['FirstName','LastName','Course', 'Group','PracticeYear','CompanyName','Head'],
            showRedact : false,
            redactNmb : 0,
        };
    }

    getGroups = () => {
        this.api.fetch('/group/getall')
            .then(response=>{
                this.setState({groups:response.groups})
            }).catch(err => alert(err))
    }

    componentDidMount(){
        this.getGroups();
    }

    render() {
        const editForm = this.state.showRedact ? (
            <div><GroupEditForm  group={this.state.groups[this.state.redactNmb]} onSubmit={this.getGroups}/></div>
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
                        {this.state.groups.map((company,index) => {
                            return <Table.Row onClick={()=>{
                                this.setState({showRedact:!this.state.showRedact,redactNmb:index});
                            }}>
                                <Table.Cell> {index+1} </Table.Cell>
                                {this.state.fields.map(field => {
                                    return <Table.Cell>
                                        {!!company[field] ? company[field] : ''}
                                    </Table.Cell>
                                })}
                            </Table.Row>
                        })}
                    </Table.Body>
                </Table>
                {editForm}
                <AddGroupForm onSubmit={this.getGroups}/>
            </div>
        );
    }
}

export default GroupPage;
