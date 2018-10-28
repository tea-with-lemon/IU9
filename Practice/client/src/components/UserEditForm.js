import React, { Component } from 'react';
import '../App.css';
import { Form } from 'semantic-ui-react';
import Api from "./api";




class UserEditForm extends Component {
    constructor(props){
        super(props);
        this.api = new Api();
        let user = this.props.user;
        let editedUser = JSON.parse(JSON.stringify(user));
        this.state = {
            user,
            editedUser
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

    handleSubmit(e){
        e.preventDefault();
        console.log(JSON.stringify(this.state.editedUser));
        this.api.fetch('/students/update',{
            method:"POST",
            body:JSON.stringify(this.state.editedUser)
        })
            .then( data => {
                if(data.ok){
                    this.props.onSubmit();
                    this.setState({user:JSON.parse(JSON.stringify(this.state.editedUser))})
                }else{
                    alert(data.msg);
                    this.setState({editedUser:JSON.parse(JSON.stringify(this.state.user))})
                }
            })
            .catch(err => alert(err))
    }

    handleChange(e){
        this.state.editedUser[e.target.name] = e.target.value;
        this.forceUpdate()
    }

    handleDelete = (e) => {
        e.preventDefault();
        this.api.fetch('/students/delete',{
            method: "POST",
            body:JSON.stringify({
                id:this.state.user.StudentID
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
            <Form>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="FirstName" label='Имя' value={this.state.editedUser.FirstName} onChange={this.handleChange}/>
                    <Form.Input fluid name="LastName" label='Фамилия' value={this.state.editedUser.LastName} onChange={this.handleChange}/>
                    <Form.Input fluid name="FName" label='Отчество' value={this.state.editedUser.FName} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Group widths='equal'>
                    <Form.Input fluid name="Phone" label='Телефон' value={this.state.editedUser.Phone} onChange={this.handleChange}/>
                    <Form.Input fluid name="Email" label='Почта' value={this.state.editedUser.Email} onChange={this.handleChange}/>
                    <Form.Input fluid name="Entrance" label='Год поступления' value={this.state.editedUser.Entrance} onChange={this.handleChange}/>
                </Form.Group>
                <Form.Group widths='equal'>
                    <Form.Select fluid name="Course" placeholder={this.state.editedUser.Course} label="Курс" options={this.courseOptions} onChange={(e,{value}) => {
                        this.state.editedUser.Course = value;
                        this.forceUpdate()
                    }}/>
                    <Form.Select fluid name="Group" placeholder={this.state.editedUser.Group} label="Группа" options={this.groupOptions} onChange={(e,{value}) => {
                        this.state.editedUser.Group = value;
                        this.forceUpdate()
                    }}/>
                </Form.Group>
                <Form.Group >
                    <Form.Button content='Обновить' onClick={this.handleSubmit}/>
                    <Form.Button content='Удалить' onClick={this.handleDelete}/>
                </Form.Group>
            </Form>
        );
    }
}

export default UserEditForm;
