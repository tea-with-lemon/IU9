import React, { Component } from 'react';
import '../App.css';
import { Icon, Label, Menu, Table } from 'semantic-ui-react'
import UserEditForm from "./UserEditForm";
import AddStudentForm from "./AddStudentForm";

class StudentsPage extends Component {
    constructor(){
        super();
        this.state = {
            msg : 'Студенты :',
            students : [],
            headers : ['Имя', 'Фамилия' ,'Отчество','Дата рождения','Дата поступления','Курс','Группа','Телефон','Почта'],
            fields : ['FirstName','LastName','FName', 'BirthDate', 'Entrance', 'Course', 'Group', 'Phone', 'Email'],
            showRedact : false,
            redactNmb : 0,
        }
        this.getStudents = this.getStudents.bind(this);
    }

    getStudents(){
        fetch("/students")
            .then(data => data.json())
            .then(json => {
                if(json.ok){
                    this.setState({students:json.students})
                }else{
                    this.setState({msg:json.msg})
                }
            })
    }

    componentDidMount(){
        this.getStudents();
    }

    render() {
        const editForm = this.state.showRedact ? (
            <div><UserEditForm valuse={this.state.redactNmb} user={this.state.students[this.state.redactNmb]} onSubmit={this.getStudents}/></div>
        ):(
            null
        );
        return (
            <div>
                {this.state.msg}
                <form>
                </form>
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
                        {this.state.students.map((student,index) => {
                            return <Table.Row onClick={()=>{
                                this.setState({showRedact:!this.state.showRedact,redactNmb:index});
                            }}>
                                <Table.Cell> {index+1} </Table.Cell>
                                {this.state.fields.map(field => {
                                    return <Table.Cell>
                                        {!!student[field] ? student[field] : ''}
                                    </Table.Cell>
                                })}
                            </Table.Row>
                        })}
                    </Table.Body>
                </Table>
                {editForm}
                <AddStudentForm onSubmit={this.getStudents}/>
            </div>
        );
    }
}

export default StudentsPage;
