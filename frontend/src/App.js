
import './App.css';
import React from 'react';


class App extends React.Component {

    constructor(props){
      super(props);
        this.state = {
          todoList:[],
          activeItems:{
            id:null,
            nom:"",
            prenom:"",
            completed:false

          },
          editing:false,
      }
      this.fetchTasks = this.fetchTasks.bind(this);
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
    componentWillMount(){
      this.fetchTasks();

    }

    fetchTasks(){
      console.log("recuperation fetch reussie");
      fetch('http://localhost:8000/')
      
      .then(response => response.json())
      .then(data => this.setState({
        todoList:data
      }))
      
    }
      
    handleChange(e){
      var name = e.target.name;
      var value = e.target.value;
      console.log("name:", name);
      console.log("value :", value);
      this.setState({
        activeItems:{
          ...this.state.activeItems,
          title:value
        }
      })
    }
    handleSubmit(e){
      e.preventDefault();
      console.log("ITEM:", this.state.activeItems);

    }
    render(){

      var tasks = this.state.todoList;
      return(
        <div className='conatiner'>
            <div className='task-container'>
               <div className='form-wrapper'>
                    <form onSubmit={this.handleSubmit} id="form">
                       <div className='flex-wrapper'>
                          <div style={{flex:6}}>
                              <br></br>
                              <input onChange={this.handleChange} className='form-control' id="nom" type="text" placeholder='nom' name='nom'/>
                              <br></br>
                              <input  onChange={this.handleChange} className='form-control' id="prenom" type="text" placeholder='prenom' name='prenom'/>
                          </div>

                          <div style={{flex:1}}>
                              <input id="submit" className='btn btn-danger'  type="submit" name='Ajouter'/>
                          </div>
                       </div>
                    </form>
                    <div id='list-wrapper'>
                       {tasks.map(function(task,index){
                         return(
                           <div key={index} className="task-wrapper flex-wrapper" >
                             <div style={{flex:7}}>
                               <span>{task.nom} - {task.prenom}</span>
                             </div>
                             <div style={{flex:1}}>
                                 <button className="btn btn-sm btn-info">Edit</button>  
                             </div>
                             <div style={{flex:1}}>
                             <button className="btn btn-sm btn-danger">Delete</button>
                             </div>
                           </div>
                         )
                       })}
                    </div>
               </div>
            </div>
        </div>
      )
    }
}

export default App;
