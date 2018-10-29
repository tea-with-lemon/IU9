import React, { Component } from 'react';
import '../App.css';
import {Checkbox, Form} from 'semantic-ui-react';
import Api from "./api";

import DatePicker from 'react-datepicker';
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';
import List from "semantic-ui-react/dist/commonjs/elements/List/List";

class PracticeEditForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            practice:this.props.practice,
            number:this.props.practice.TreatmentNumber,
            students:[],
            managers:[],
            searchManager:'',
            searchStudent:'',
            StartDate: moment(),
            EndDate: moment(),
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    getDate = (date) => {
        return [date._d.getFullYear().toString(),(date._d.getMonth()+1).toString(),date._d.getDate().toString()].join('.');
    }

    handleSubmit = (e) => {
        this.state.practice.Startdate = this.getDate(this.state.StartDate);
        this.state.practice.EndDate = this.getDate(this.state.EndDate);
        this.api.fetch('/practice/update',{
            method:"POST",
            body:JSON.stringify({
                practice: this.state.practice,
                number:this.state.number
            })
        })
            .then( data => {
                if(data.ok){
                    this.state.number = this.state.practice.TreatmentNumber;
                    this.props.onSubmit();
                }else{
                    alert(data.message);
                }
            })
            .catch(err => alert(err))
    };

    handleDelete(){
        this.api.fetch('/practice/delete',{
            method:"POST",
            body:JSON.stringify({number:this.state.number})
        })
            .then( data => {
                if(data.ok){
                    this.props.onSubmit();
                }else{
                    alert(data.message);
                }
            })
            .catch(err => alert(err))
    };


    searchStudents = (name) =>{
        this.api.fetch(`/students/find?LastName=${name}`)
            .then(response =>{
                this.setState({students:response.students})
            })
            .catch(err => alert(err))
    };

    searchManagers = (name) =>{
        this.api.fetch(`/manager/find?LastName=${name}`)
            .then(response =>{
                this.setState({managers:response.managers})
            })
            .catch(err => alert(err))
    };

    handleChange(e){
        this.state.practice[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        const search = (
            <div>
                <Form onSubmit={()=>this.searchStudents(this.state.searchStudent)}>
                    <Form.Group>
                        <Form.Input width={2} fluid name="search" placeholder="Введите фаимлию" value={this.state.searchStudent} onChange={(e)=>this.setState({searchStudent:e.target.value})}/>
                        <Form.Button content='Поиск студентов'/>
                    </Form.Group>
                </Form>
                <List divided>
                    {this.state.students.map(student => {
                        return (
                            <List.Item>
                                <List.Icon name='right triangle' size='large' verticalAlign='middle'/>
                                <List.Content>
                                    <List.Description as='a'>{`Студент ${student.FirstName} ${student.LastName}, курс ${student.Course}, группа ${student.Group}, идентификатор ${student.StudentID}`}</List.Description>
                                </List.Content>
                            </List.Item>
                        )
                    })}
                </List>

                <Form onSubmit={()=>this.searchManagers(this.state.searchManager)}>
                    <Form.Group>
                        <Form.Input width={2} fluid name="search" placeholder="Введите фаимлию" value={this.state.searchManager} onChange={(e)=>this.setState({searchManager:e.target.value})}/>
                        <Form.Button content='Поиск руководителей'/>
                    </Form.Group>
                </Form>
                <List divided>
                    {this.state.managers.map( manager => {
                        return (
                            <List.Item>
                                <List.Icon name='right triangle' size='large' verticalAlign='middle'/>
                                <List.Content>
                                    <List.Description as='a'>{`Руководитель ${manager.FirstName} ${manager.LastName}, компания : ${manager.CompanyName}, идентификатор : ${manager.ManagerID}`}</List.Description>
                                </List.Content>
                            </List.Item>
                        )
                    })}
                </List>
            </div>
        )
        return (
            <div>Обновить практику
                <Form>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="TreatmentNumber" label='Номер договора' value={this.state.practice.TreatmentNumber} onChange={this.handleChange}/>
                        <Form.Field width={4}>
                            <label>Дата начала</label>
                            <DatePicker  selected={this.state.StartDate} onChange={(date)=>{
                                this.state.StartDate = date;
                                this.forceUpdate()
                            }}/>
                        </Form.Field>
                        <Form.Field width={4}>
                            <label>Дата окончания</label>
                            <DatePicker  selected={this.state.EndDate} onChange={(date)=>{
                                this.state.EndDate = date;
                                this.forceUpdate()
                            }}/>
                        </Form.Field>
                        <Form.Input  width={6} fluid name="Mark" label='Оценка' value={this.state.practice.Mark} onChange={this.handleChange}/>
                        <Form.Input  width={6} fluid name="RecomendedMark" label='Рекомендованная оценка' value={this.state.practice.RecomendedMark} onChange={this.handleChange}/>
                        <Checkbox style={{marginRight:"70px",marginTop:"30px"}} label="Наличие отчета" checked={this.state.practice.Report} onChange={()=>{
                            this.state.practice.Report = !this.state.practice.Report;
                            this.forceUpdate()
                        }}/>
                    </Form.Group>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="Student" label='Студент' value={this.state.practice.Student} onChange={this.handleChange}/>
                        <Form.Input fluid name="Head" label='Бригадир' value={this.state.practice.Head} onChange={this.handleChange}/>
                        <Form.Input fluid name="ManagerCompany" label='Руководитель от предприятия' value={this.state.practice.ManagerCompany} onChange={this.handleChange}/>
                        <Form.Input fluid name="ManagerBMSTU" label='Руководитель от кафедры' value={this.state.practice.ManagerBMSTU} onChange={this.handleChange}/>
                        <Form.Input fluid name="Task" label='Описание задания' value={this.state.practice.Task} onChange={this.handleChange}/>
                    </Form.Group>
                    <Form.Group>
                        <Form.Button content='Обновить практику' onClick={this.handleSubmit}/>
                        <Form.Button content='Удалить практику' onClick={this.handleDelete}/>
                    </Form.Group>

                </Form>
                {search}
            </div>
            // name="BirthDate" label='Дата рождения'
        );
    }
}

export default PracticeEditForm;
