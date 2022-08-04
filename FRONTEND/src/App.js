import "./App.css";
import CheckboxesTags from "./CheckboxesTags";
import DenseAppBar from "./DenseAppBar";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";
import Box from "@material-ui/core/Box";
import RegisterPatient from "./pages/RegisterPatient";
import LoginPatient from "./pages/LoginPatient";
import {BrowserRouter,Route,Switch } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <DenseAppBar />
    <BrowserRouter>
      <Switch>
        <Route path="/register" component={RegisterPatient}></Route>
        <Route exact path="/login" component={LoginPatient}></Route> */
      </Switch>
    </BrowserRouter>
        
        
    
  <Container maxWidth="sm">
  
       
        <Box m={2} p={3} style={{ width: "500px", marginTop: "50px" }}>
          <Paper elevation={3} style={{ padding: "10px" }}>
            <CheckboxesTags/>
          </Paper>
        </Box>
      </Container>
    

    

      {/* <Container maxWidth="sm">
        <Box m={2} p={3} style={{ width: "500px", marginTop: "50px" }}>
          <Paper elevation={3} style={{ padding: "10px" }}>
            <CheckboxesTags />
          </Paper>
        </Box>
      </Container> */}
    
      {/* <LoginPatient/> */}
    
    </div>
  );
}

export default App;
