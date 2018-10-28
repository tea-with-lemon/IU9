import React, { Component } from 'react';
import '../App.css';
import {Form, List, TextArea} from 'semantic-ui-react';
import Api from "./api";
import 'react-datepicker/dist/react-datepicker.css';

class AddManagerForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            manager:{},
            companies : [],
            search:'',
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

    handleSubmit(e){
        this.api.fetch('/manager/add',{
            method:"POST",
            body:JSON.stringify(this.state.manager)
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
        this.state.manager[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        const searchCompanies = (
            <div style={{margin:"10px"}}>
                <Form onSubmit={()=>this.searchCompanies(this.state.search)}>
                    <Form.Group>
                        <Form.Input width={2} fluid name="search" placeholder="Введите название компании" value={this.state.search} onChange={(e)=>this.setState({search:e.target.value})}/>
                        <Form.Button content='Поиск'/>
                    </Form.Group>
                </Form>
                <List divided>
                    {this.state.companies.map(company => {
                        return (
                            <List.Item onClick={()=>{
                                this.state.manager.CompanyName = company.CompanyName;
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
            <div>Добавить руководителя
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="FirstName" label='Имя' value={this.state.manager.FirstName} onChange={this.handleChange}/>
                        <Form.Input fluid name="LastName" label='Фамилия' value={this.state.manager.LastName} onChange={this.handleChange}/>
                        <Form.Input fluid name="FName" label='Отчество' value={this.state.manager.FName} onChange={this.handleChange}/>
                    </Form.Group>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="Phone" label='Телефон' value={this.state.manager.Phone} onChange={this.handleChange}/>
                        <Form.Input fluid name="Email" label='Почта' value={this.state.manager.Email} onChange={this.handleChange}/>
                        <Form.Input fluid name="CompanyName" label='Компания' value={this.state.manager.CompanyName} onChange={this.handleChange}/>
                    </Form.Group>
                    <Form.Button content='Добавить руководителя'/>
                </Form>
                {searchCompanies}
            </div>
            // name="BirthDate" label='Дата рождения'
        );
    }
}

export default AddManagerForm;
