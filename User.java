package com.gaosheng;

public class User {
	private String id;
	private String username;
	private String password;
	private String sex;
	private String age;
	private String phone;
	
	
	
	
	
	public String getId() {
		return id;
	}





	public void setId(String id) {
		this.id = id;
	}





	public String getUsername() {
		return username;
	}





	public void setUsername(String username) {
		this.username = username;
	}





	public String getPassword() {
		return password;
	}





	public void setPassword(String password) {
		this.password = password;
	}





	public String getSex() {
		return sex;
	}





	public void setSex(String sex) {
		this.sex = sex;
	}





	public String getAge() {
		return age;
	}





	public void setAge(String age) {
		this.age = age;
	}





	public String getPhone() {
		return phone;
	}





	public void setPhone(String phone) {
		this.phone = phone;
	}





	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return this.id+","+this.username+","+this.password+","+this.sex;
	}
	
	
}
