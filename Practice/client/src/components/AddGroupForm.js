import React, { Component } from 'react';
import '../App.css';
import {Checkbox, Form, List, TextArea} from 'semantic-ui-react';
import Api from "./api";
import 'react-datepicker/dist/react-datepicker.css';

class AddGroupForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            group:{},
            companies : [],
            students : [],
            searchCompany:'',
            searchStudent:'',
            checked:false
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    searchCompanies = (name) =>{
        this.api.fetch(`/company/find?CompanyName=${name}`)
            .then(response =>{
                this.setState({companies:response.companies})
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

    handleSubmit(e){
        this.api.fetch('/group/add',{
            method:"POST",
            body:JSON.stringify(this.state.group)
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
        this.state.group[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        const search = (
            <div style={{margin:"10px"}}>
                <Form onSubmit={()=>this.searchCompanies(this.state.searchCompany)}>
                    <Form.Group>
                        <Form.Input width={2} fluid name="search" placeholder="Введите название компании" value={this.state.searchCompany} onChange={(e)=>this.setState({searchCompany:e.target.value})}/>
                        <Form.Button content='Поиск компаний'/>
                    </Form.Group>
                </Form>
                <List divided>
                    {this.state.companies.map(company => {
                        return (
                            <List.Item onClick={()=>{
                                this.state.group.CompanyName = company.CompanyName;
                                this.forceUpdate()
                            }}>
                                <List.Icon name='right triangle' size='large' verticalAlign='middle'/>
                                <List.Content>
                                    <List.Description as='a'>{company.CompanyName}</List.Description>
                                </List.Content>
                            </List.Item>
                        )
                    })}
                </List>

                <Form onSubmit={()=>this.searchStudents(this.state.searchStudent)}>
                    <Form.Group>
                        <Form.Input width={2} fluid name="search" placeholder="Введите фаимлию" value={this.state.searchStudent} onChange={(e)=>this.setState({searchStudent:e.target.value})}/>
                        <Form.Button content='Поиск студентов'/>
                    </Form.Group>
                </Form>
                <List divided>
                    {this.state.students.map(student => {
                        return (
                            <List.Item onClick={()=>{
                                this.state.group.Student = student.StudentID;
                                this.forceUpdate()
                            }}>
                                <List.Icon name='right triangle' size='large' verticalAlign='middle'/>
                                <List.Content>
                                    <List.Description as='a'>{`Студент ${student.FirstName} ${student.LastName}, курс ${student.Course}, группа ${student.Group}`}</List.Description>
                                </List.Content>
                            </List.Item>
                        )
                    })}
                </List>
            </div>
        );

        return (
            <div>Добавить студента в группу
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="Student" label='Студент' value={this.state.group.Student} onChange={this.handleChange}/>
                        <Form.Input fluid name="PracticeYear" label='Год' value={this.state.group.PracticeYear} onChange={this.handleChange}/>
                        <Form.Input fluid name="CompanyName" label='Компания' value={this.state.group.CompanyName} onChange={this.handleChange}/>
                        <Checkbox style={{marginRight:"70px",marginTop:"30px"}} label="Бригадир" checked={this.state.group.Head} onChange={()=>{
                            this.state.group.Head = !this.state.group.Head;
                            this.forceUpdate()
                        }}/>
                    </Form.Group>
                    <Form.Button content='Добавить пользователя'/>
                </Form>
                {search}
            </div>
        );
    }
}

export default AddGroupForm;
