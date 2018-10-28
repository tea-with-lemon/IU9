import React, { Component } from 'react';
import '../App.css';
import { Form } from 'semantic-ui-react';
import Api from "./api";




class AddStudentForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {student:{}};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e){
        // e.preventDefault();
        console.log(JSON.stringify(this.state.editedUser));
        this.api.fetch('/students/addstudent',{
            method:"POST",
            body:JSON.stringify(this.state.student)
        })
            .then( data => {
                if(data.ok){
                    this.props.onSubmit();
                    this.setState({student:{}})
                }else{
                    alert(data.msg);
                }
            })
            .catch(err => alert(err))
    }

    handleChange(e){
        console.log(e.target.name);
        console.log(e.target.value);
        this.state.student[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        return (
            <div>Add a user:
            <Form onSubmit={this.handleSubmit}>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="FirstName" label='Имя' value={this.state.student.FirstName} onChange={this.handleChange}/>
                    <Form.Input fluid name="LastName" label='Фамилия' value={this.state.student.LastName} onChange={this.handleChange}/>
                    <Form.Input fluid name="FName" label='Отчество' value={this.state.student.FName} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="Phone" label='Телефон' value={this.state.student.Phone} onChange={this.handleChange}/>
                    <Form.Input fluid name="Email" label='Почта' value={this.state.student.Email} onChange={this.handleChange}/>
                    <Form.Input fluid name="BirthDate" label='Дата рождения' value={this.state.student.BirthDate} onChange={this.handleChange}/>
                    <Form.Input fluid name="Entrance" label='Год поступления' value={this.state.student.Entrance} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Button content='Добавить студента'/>
            </Form></div>
        );
    }
}

export default AddStudentForm;
