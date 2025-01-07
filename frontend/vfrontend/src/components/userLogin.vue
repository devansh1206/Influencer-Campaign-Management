<template>
    <div class="container d-flex justify-content-center mt-5">
      <div class="card p-4 shadow-sm" style="width: 400px;">
        <h2 class="text-center mb-4">User Login</h2>
        <form @submit.prevent="onSubmit">
          <!-- Email Input -->
          <div class="form-group">
            <label for="email">Email</label>
            <input
              type="email"
              id="email"
              v-model="userLoginForm.email"
              class="form-control"
              placeholder="Enter your email"
              required
            />
          </div>
          
          <!-- Password Input -->
          <div class="form-group mt-3">
            <label for="userpassword">Password</label>
            <input
              type="password"
              id="userpassword"
              v-model="userLoginForm.userPassword"
              class="form-control"
              placeholder="Enter your password"
              required
            />
          </div>
  
          <!-- Submit Button -->
          <button type="submit" class="btn btn-info w-100 mt-4">Login</button>
        </form>
  
        <!-- Links to Register as Influencer/Sponsor -->
        <div class="d-flex justify-content-between mt-3">
          <button @click="toInfluencerRegister" class="btn btn-outline-success">Register as Influencer</button>
          <button @click="toSponsorRegister" class="btn btn-outline-secondary">Register as Sponsor</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: "userLogin",
    data() {
      return {
        userLoginForm: {
          email: "",
          userPassword: "",
        }
      }
    },
    methods: {
      login(payload) {
        const path = "http://localhost:5000/login";
        axios.post(path, payload)
          .then((res) => {
            console.log(res.data);
            console.log(res.data.message);
            const role = res.data.user_data.role;

            this.$store.commit('setUser', res.data);

            if(role==1){ // admin
                this.$router.push("/adminHome")
            }else if(role==2){ // influencer
                this.$router.push("/userHome")
            }else { // sponsor
                this.$router.push("/sponsorHome")
            }
          })
          .catch((err) => {
            console.error(err);
          });
      },
      onSubmit(e) {
        e.preventDefault();
        const payload = {
          email: this.userLoginForm.email,
          password: this.userLoginForm.userPassword,
        };
        this.login(payload);
      },
      toInfluencerRegister() {
        this.$router.push('/influencerRegister');
      },
      toSponsorRegister() {
        this.$router.push('/sponsorRegister');
      },
      initForm() {
        this.userLoginForm.username = "";
        this.userLoginForm.userPassword = "";
      }
    }
  };
  </script>
  
  <style scoped>
  /* Style for the card and overall layout */
  .container {
    margin-top: 50px;
  }
  
  .card {
    border-radius: 10px;
    padding: 20px;
  }
  
  h2 {
    font-size: 1.8rem;
  }
  
  button {
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #17a2b8 !important;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  </style>
  