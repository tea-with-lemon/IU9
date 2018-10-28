import React, { Component } from 'react';
import '../App.css';
import { Form } from 'semantic-ui-react';
import Api from "./api";

import DatePicker from 'react-datepicker';
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';

class AddStudentForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            student:{
                BirthDate:this.getDate(moment())
            },
            date: moment()
        };

        this.courseOptions =[
            { key: 'k1', text: '1', value: 1 },
            { key: 'k2', text: '2', value: 2 },
            { key: 'k3', text: '3', value: 3 },
            { key: 'k4', text: '4', value: 4 },
            { key: 'k5', text: '5', value: 5 },
            { key: 'k6', text: '6', value: 6 }
        ];

        this.groupOptions = [
            { key: 'g1', text: '1', value: 1 },
            { key: 'g2', text: '2', value: 2 }
        ];

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    getDate = (date) => {
        return [date._d.getFullYear().toString(),(date._d.getMonth()+1).toString(),date._d.getDate().toString()].join('.');
    }

    handleSubmit(e){
        this.state.student.BirthDate = this.getDate(this.state.date);
        console.log(this.state.student.BirthDate);
        this.api.fetch('/students/addstudent',{
            method:"POST",
            body:JSON.stringify(this.state.student)
        })
            .then( data => {
                if(data.ok){
                    this.props.onSubmit();
                }else{
                    alert(data.msg);
                }
            })
            .catch(err => alert(err))
    }

    handleChange(e){
        this.state.student[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        return (
            <div>Добавить студента
            <Form onSubmit={this.handleSubmit}>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="FirstName" label='Имя' value={this.state.student.FirstName} onChange={this.handleChange}/>
                    <Form.Input fluid name="LastName" label='Фамилия' value={this.state.student.LastName} onChange={this.handleChange}/>
                    <Form.Input fluid name="FName" label='Отчество' value={this.state.student.FName} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="Phone" label='Телефон' value={this.state.student.Phone} onChange={this.handleChange}/>
                    <Form.Input fluid name="Email" label='Почта' value={this.state.student.Email} onChange={this.handleChange}/>
                    <Form.Field>
                        <label>Дата рождения</label>
                        <DatePicker  selected={this.state.date} onChange={(date)=>{
                            this.state.date = date;
                            this.getDate(date);
                            this.forceUpdate()
                        }}/>
                    </Form.Field>
                    <Form.Input fluid name="Entrance" label='Год поступления' value={this.state.student.Entrance} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Group widths='equal'>
                    <Form.Select fluid name="Course"  label="Курс" options={this.courseOptions} onChange={(e,{value}) => {
                        this.state.student.Course = value;
                        this.forceUpdate()
                    }}/>
                    <Form.Select fluid name="Group"  label="Группа" options={this.groupOptions} onChange={(e,{value}) => {
                        this.state.student.Group = value;
                        this.forceUpdate()
                    }}/>
                </Form.Group>
                <Form.Button content='Добавить студента'/>
            </Form></div>
        // name="BirthDate" label='Дата рождения'
        );
    }
}

export default AddStudentForm;
