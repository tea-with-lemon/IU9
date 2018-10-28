import React, { Component } from 'react';
import '../App.css';
import {Icon, Label, List, Menu, Table} from 'semantic-ui-react'
import UserEditForm from "./UserEditForm";
import AddStudentForm from "./AddStudentForm";
import Api from "./api";
import AddCompanyForm from "./AddCompanyForm";
import AddManagerForm from "./AddManagerForm";
import AddPracticeForm from "./AddPracticeForm";
import GroupEditForm from "./GroupEditForm";
import PracticeEditForm from "./PracticeEditForm";

class PracticePage extends Component {
    constructor(){
        super();
        this.api = new Api();
        this.state = {
            practice: [],
            headers : ['Номер договора', 'Начало','Конец','Оценка','Рекомендованная оценка','Описание задания','Наличие отчета','Бригадир','Студент','Руководитель от компании','Руководитель от кафедры'],
            fields : ['TreatmentNumber','StartDate','EndDate','Mark','RecomendedMark', 'Task','Report','Student','Head','ManagerCompany','ManagerBMSTU'],
            showRedact : false,
            redactNmb : 0,
        };
    }

    getPractice = ()=>{
        this.api.fetch('/practice/getall')
            .then(response=>{
                this.setState({practice:response.practice})
            }).catch(err => alert(err))
    }



    componentDidMount(){
        this.getPractice();
    }

    render() {
        const editForm = this.state.showRedact ? (
            <div><PracticeEditForm  practice={this.state.practice[this.state.redactNmb]} onSubmit={this.getPractice}/></div>
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
                        {this.state.practice.map((manager,index) => {
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
                <AddPracticeForm onSubmit={this.getPractice}/>
            </div>
        );
    }
}

export default PracticePage;
