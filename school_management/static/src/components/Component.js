/** @odoo-module **/
import { registry } from "@web/core/registry";
const { Component, useState, xml} = owl;
console.log('MY Module');
class A extends Component {
    setup(){
        console.log('FROM A')

    }
}
A.template = 'school_management.A';

class B extends Component {
  
    static template = xml`<span>child b</span>`;
}

class Form extends Component {
    static template = "Form";
  
    setup() {
      this.state = useState({
        text: "",
        othertext: "",
        number: '',
        color: "",
        bool: false
      });
    }
  }


class Tasks extends Component {
    static template = "Tasks";
   
    static props = ["task"]
}

class Root extends Component {
    static template = "Root";
    

    static components = {Tasks} 

    setup() {
        this.state = useState({
            name: "",
            color: "#fff000",
            isCompleted: false,
        });

        this.tasks = useState([])
    }

    addTask() {
        if (!this.state.name){
            alert("Please provide name of the task.")
            return
        }

        const id = Math.random().toString().substring(2,12)
    

        this.tasks.push({
            id:id,
            name:this.state.name,
            color:this.state.color,
            isCompleted: false,
        })

        let state = this.state
        this.state = {...state, name:"", color:"#fff000"}

        console.log(this.tasks)
    }
}


class Parent extends Component {
    static template = 'Parent';
    static components = { A, B, Form, Tasks, Root }
    state = useState({form_render:"" });

    get myComponent() {
        if (this.state.form_render === 'a') {
            return A;
        } else if(this.state.form_render==='b'){
            return B;
        }
        else if(this.state.form_render==='root'){
            return Root;
        }
        else {
            return B;
        }
    }
}



  
registry.category('actions').add('component_client_action', Parent);


