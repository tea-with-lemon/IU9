import React, { Component } from 'react';
import '../App.css';
import {Checkbox, Form, List, TextArea} from 'semantic-ui-react';
import Api from "./api";
import 'react-datepicker/dist/react-datepicker.css';

class GroupEditForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            group: this.props.group,
            companies : [],
            students : [],
            year:this.props.group.PracticeYear,
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
        this.api.fetch('/group/update',{
            method:"POST",
            body:JSON.stringify({
                group:this.state.group,
                year: this.state.year
            })
        })
            .then( data => {
                if(data.ok){
                    this.props.onSubmit();
                    this.setState({year:this.state.group.PracticeYear})
                }else{
                    alert(data.msg);
                }
            })
            .catch(err => alert(err))
    }

    handleDelete = (e)=>{
        this.api.fetch('/group/delete',{
            method:"POST",
            body:JSON.stringify({
                id:this.state.group.Student,
                year: this.state.year
            })
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
            </div>
        );

        return (
            <div>Обновить студента : {this.state.group.FirstName} {this.state.group.LastName} {this.state.group.Course} курс {this.state.group.Group} группа
                <Form >
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="PracticeYear" label='Год' value={this.state.group.PracticeYear} onChange={this.handleChange}/>
                        <Form.Input fluid name="CompanyName" label='Компания' value={this.state.group.CompanyName} onChange={this.handleChange}/>
                        <Checkbox style={{marginRight:"70px",marginTop:"30px"}} label="Бригадир" checked={this.state.group.Head} onChange={()=>{
                            this.state.group.Head = !this.state.group.Head;
                            this.forceUpdate()
                        }}/>
                    </Form.Group>
                    <Form.Group >
                        <Form.Button content='Обновить пользователя' onClick={this.handleSubmit}/>
                        <Form.Button content='Удалить пользователя' onClick={this.handleDelete}/>
                    </Form.Group>
                </Form>
                {search}
            </div>
        );
    }
}

export default GroupEditForm;
