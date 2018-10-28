import React, { Component } from 'react';
import '../App.css';
import {Form, List, TextArea} from 'semantic-ui-react';
import Api from "./api";





class ManagerEditForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        console.log(this.props.manager);
        this.state = {
            manager : JSON.parse(JSON.stringify(this.props.manager)),
            companies: [],
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
        e.preventDefault();
        this.api.fetch('/manager/update',{
            method:"POST",
            body:JSON.stringify(this.state.manager)
        })
            .then( data => {
                if(!data.ok){
                    alert(data.msg);
                }
                this.props.onSubmit();
            })
            .catch(err => alert(err))
    }

    handleChange(e){
        this.state.manager[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    handleDelete = (e) => {
        e.preventDefault();
        console.log()
        this.api.fetch('/manager/delete',{
            method: "POST",
            body:JSON.stringify({
                id:this.state.manager.ManagerID
            })
        })
            .then(response=>{
                if(response.ok){
                    this.props.onSubmit();
                }else{
                    alert(response.msg)
                }
            })
            .catch(err => alert(err))
    };


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
            <div>Изменить руководителя
                <Form >
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
                    <Form.Group>
                        <Form.Button content='Обновить руководителя' onClick={this.handleSubmit}/>
                        <Form.Button content='Удалить руководителя' onClick={this.handleDelete}/>
                    </Form.Group>
                </Form>
                {searchCompanies}
            </div>
        );
    }
}

export default ManagerEditForm;
