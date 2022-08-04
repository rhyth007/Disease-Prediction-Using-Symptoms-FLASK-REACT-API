import React from "react";
import { useState } from "react";
import {
	Grid,
	Paper,
	Avatar,
	Typography,
	TextField,
	Button,
} from "@material-ui/core";
import AddCircleOutlineOutlinedIcon from "@material-ui/icons/AddCircleOutlineOutlined";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import Checkbox from "@material-ui/core/Checkbox";
import { Link } from "react-router-dom";

const RegisterPatient = () => {
	const [showPassword, setShow] = useState(false);
	const [name, setName] = useState("");
	const [email, setEmail] = useState("");
	const [phoneno, setPhoneno] = useState("");
	const [password, setPassword] = useState("");
	const [cnfpassword, setcnfPassword] = useState("");
	const [gender, setGender] = useState("");
	// console.log(phoneno);

	const paperStyle = { padding: 20, width: 350, margin: "0 auto" };
	const headerStyle = { margin: 0 };
	const avatarStyle = { backgroundColor: "#1bbd7e" };
	const marginTop = { marginTop: 5 };
	return (
		<Grid>
			<Paper style={paperStyle}>
				<Grid align="center">
					<Avatar style={avatarStyle}>
						<AddCircleOutlineOutlinedIcon />
					</Avatar>
					<h2 style={headerStyle}>Sign Up As a Patient</h2>
					<Typography variant="caption" gutterBottom>
						Please fill this form to create an account !
					</Typography>
				</Grid>
				<form>
					<TextField
						fullWidth
						label="Name"
						placeholder="Enter your name"
						value={name}
						onChange={(e) => setName(e.target.value)}
					/>
					<TextField
						fullWidth
						label="Email"
						placeholder="Enter your email"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
					/>
					<FormControl component="fieldset" style={marginTop} onChange={(e)=>{setGender(e.target.value)}}>
						<FormLabel component="legend">Gender</FormLabel>
						<RadioGroup
							aria-label="gender"
							name="gender"
							style={{ display: "initial" }}
						>
							<FormControlLabel
								value="female"
								control={<Radio />}
								label="Female"
							/>
							<FormControlLabel value="male" control={<Radio />} label="Male" />
						</RadioGroup>
					</FormControl>
					<TextField
						fullWidth
						label="Phone Number"
						value={phoneno}
						onChange={(e) => {
							setPhoneno(e.target.value);
						}}
						placeholder="Enter your phone number"
					/>
					<TextField
						fullWidth
						label="Password"
						placeholder="Enter your password"
						value={password}
						onChange={(e) => {
							setPassword(e.target.value);
						}}
						type={showPassword ? "text" : "password"}
					/>
					<TextField
						fullWidth
						label="Confirm Password"
						placeholder="Confirm your password"
						value={cnfpassword}
						onChange={(e) => {
							setcnfPassword(e.target.value);
						}}
						type={showPassword ? "text" : "password"}
					/>

					<FormControlLabel
						control={<Checkbox name="checkedA" />}
						label="I accept the terms and conditions."
					/>
					<Button type="submit" variant="contained" color="primary">
						Sign up
					</Button>

					<Typography>
						{console.log(gender)}
						Already a Patient ?<Link to="/login">Log In</Link>
					</Typography>
				</form>

			</Paper>
		</Grid>
	);
};

export default RegisterPatient;
