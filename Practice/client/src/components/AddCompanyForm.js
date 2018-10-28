import React, { Component } from 'react';
import '../App.css';
import {Form, TextArea} from 'semantic-ui-react';
import Api from "./api";
import 'react-datepicker/dist/react-datepicker.css';

class AddCompanyForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        this.state = {
            company:{},
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }



    handleSubmit(e){
        this.api.fetch('/company/add',{
            method:"POST",
            body:JSON.stringify(this.state.company)
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
        this.state.company[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    render() {
        return (
            <div>Добавить компанию
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group widths='equal'>
                        <Form.Input fluid name="CompanyName" label='Название фирмы' value={this.state.company.CompanyName} onChange={this.handleChange}/>
                        <Form.Input fluid name="Email" label='Почта' value={this.state.company.Email} onChange={this.handleChange}/>
                        <Form.Input fluid name="Addres" label='Адрес' value={this.state.company.Addres} onChange={this.handleChange}/>
                    </Form.Group>
                    <Form.Input control={TextArea} label='Описание' value={this.state.company.Description} name="Description" onChange={this.handleChange}/>
                    <Form.Button content='Добавить компанию'/>
                </Form></div>
            // name="BirthDate" label='Дата рождения'
        );
    }
}

export default AddCompanyForm;
