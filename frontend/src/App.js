
import './App.css';
import React from 'react';


class App extends React.Component {
    render(){
      return(
        <div className='conatiner'>
            <div className='task-container'>
               <div className='form-wrapper'>
                    <form id="form">
                       <div className='flex-wrapper'>
                          <div style={{flex:6}}>
                              <input  className='form-control' id="nom" type="text" placeholder='nom' name='nom'/>
                              <input  className='form-control' id="nom" type="text" placeholder='nom' name='nom'/>
                          </div>

                          <div style={{flex:1}}>
                              <input id="submit" className='btn btn-danger'  type="submit" name='Ajouter'/>
                          </div>
                       </div>
                    </form>
                    <div id='list-wrapper'>

                    </div>
               </div>
            </div>
        </div>
      )
    }
}

export default App;
