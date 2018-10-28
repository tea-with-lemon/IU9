import React, { Component } from 'react';
import '../App.css';
import {Form, TextArea} from 'semantic-ui-react';
import Api from "./api";




class CompanyEditForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        console.log(this.props.company);
        this.state = {
            company : JSON.parse(JSON.stringify(this.props.company)),
            name:this.props.company.CompanyName
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e){
        e.preventDefault();
        this.api.fetch('/company/update',{
            method:"POST",
            body:JSON.stringify({
                company: this.state.company,
                name : this.state.name
            })
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
        this.state.company[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    handleDelete = (e) => {
        e.preventDefault();
        this.api.fetch('/company/delete',{
            method: "POST",
            body:JSON.stringify({
                CompanyName:this.state.name
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
    }


    render() {
        return (
            <div>Изменить компанию
                <Form>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="CompanyName" label='Название фирмы' value={this.state.company.CompanyName} onChange={this.handleChange}/>
                        <Form.Input fluid name="Email" label='Почта' value={this.state.company.Email} onChange={this.handleChange}/>
                        <Form.Input fluid name="Addres" label='Адрес' value={this.state.company.Addres} onChange={this.handleChange}/>
                    </Form.Group>
                    <Form.Input control={TextArea} label='Описание' value={this.state.company.Description} name="Description" onChange={this.handleChange}/>
                    <Form.Group>
                        <Form.Button content='Обновить компанию' onClick={this.handleSubmit}/>
                        <Form.Button content='Удалить компанию' onClick={this.handleDelete}/>
                    </Form.Group>
                </Form></div>
        );
    }
}

export default CompanyEditForm;
