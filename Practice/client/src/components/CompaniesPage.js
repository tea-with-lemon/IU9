import React, { Component } from 'react';
import '../App.css';
import { Icon, Label, Menu, Table } from 'semantic-ui-react'
import UserEditForm from "./UserEditForm";
import AddStudentForm from "./AddStudentForm";
import Api from "./api";
import AddCompanyForm from "./AddCompanyForm";
import CompanyEditForm from "./CompanyEditForm";

class CompaniesPage extends Component {
    constructor(){
        super();
        this.api = new Api();
        this.state = {
            companies: [],
            headers : ['Название компании', 'Описание' ,'Адрес','Почта'],
            fields : ['CompanyName','Description','Addres', 'Email'],
            showRedact : false,
            redactNmb : 0,
        };
        this.getCompanies = this.getCompanies.bind(this);
    }

    getCompanies(){
        this.api.fetch('/company/getall')
            .then(response=>{
                this.setState({companies:response.companies})
            }).catch(err => alert(err))
    }

    componentDidMount(){
        this.getCompanies();
    }

    render() {
        const editForm = this.state.showRedact ? (
            <div><CompanyEditForm  company={this.state.companies[this.state.redactNmb]} onSubmit={this.getCompanies}/></div>
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
                        {this.state.companies.map((company,index) => {
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
                <AddCompanyForm onSubmit={this.getCompanies}/>
            </div>
        );
    }
}

export default CompaniesPage;
