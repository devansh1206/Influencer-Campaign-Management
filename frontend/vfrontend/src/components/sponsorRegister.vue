<template>
    <div class="container mt-5">
      <div class="card shadow-sm">
        <div class="card-header bg-primary text-white text-center">
          <h2>Register as Sponsor</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="registerSponsor">
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" v-model="form.email" required class="form-control" id="email" placeholder="Enter email" />
            </div>
  
            <div class="form-group mt-3">
              <label for="password">Password</label>
              <input type="password" v-model="form.password" required class="form-control" id="password" placeholder="Enter password" />
            </div>
  
            <div class="form-group mt-3">
              <label for="fullName">Full Name</label>
              <input type="text" v-model="form.full_name" required class="form-control" id="fullName" placeholder="Enter your full name" />
            </div>
  
            <div class="form-group mt-3">
              <label for="phone">Phone</label>
              <input type="text" v-model="form.phone" class="form-control" id="phone" placeholder="Enter phone number" />
            </div>
  
            <div class="form-group mt-3">
              <label for="address">Address</label>
              <input type="text" v-model="form.address" class="form-control" id="address" placeholder="Enter your address" />
            </div>
  
            <div class="form-group mt-3">
              <label for="industry">Industry</label>
              <input type="text" v-model="form.industry" required class="form-control" id="industry" placeholder="Enter industry type" />
            </div>
  
            <div class="form-group mt-3">
              <label for="website">Website URL</label>
              <input type="url" v-model="form.website" class="form-control" id="website" placeholder="Enter website URL" />
            </div>
  
            <div class="form-group mt-3">
              <label for="budget">Budget</label>
              <input type="number" v-model="form.budget" required class="form-control" id="budget" placeholder="Enter budget" />
            </div>
  
            <div class="form-group mt-3">
              <label for="profilePicture">Profile Picture URL</label>
              <input type="text" v-model="form.profile_picture" class="form-control" id="profilePicture" placeholder="Enter profile picture URL" />
            </div>
  
            <button type="submit" class="btn btn-primary w-100 mt-4">Register as Sponsor</button>
          </form>
  
          <!-- Display message -->
          <div v-if="message" class="alert mt-3" :class="{'alert-success': success, 'alert-danger': !success}">
            {{ message }}
          </div>
  
          <!-- Links to other pages -->
          <div class="d-flex justify-content-between mt-3">
            <button @click="toInfluencerRegister" class="btn btn-outline-success">Register as Influencer</button>
            <button @click="toLogin" class="btn btn-outline-secondary">Already a User? Login</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "sponsorRegister",
    data() {
      return {
        form: {
          email: '',
          password: '',
          full_name: '',
          phone: '',
          address: '',
          industry: '',
          website: '',
          budget: '',
          profile_picture: ''
        },
        message: '',
        success: false
      };
    },
    methods: {
      async registerSponsor() {
        try {
          const payload = { ...this.form, role: 'sponsor' };
          const response = await axios.post('http://localhost:5000/sponsorRegister', payload);
  
          this.message = response.data.message;
          this.success = response.data.success;
  
          if (this.success) {
            this.form = { email: '', password: '', full_name: '', phone: '', address: '', industry: '', website: '', budget: '', profile_picture: '' };
          }
        } catch (error) {
          console.error(error);
          this.message = error.response.data.message || 'Registration failed';
          this.success = false;
        }
      },
      toInfluencerRegister() {
        this.$router.push('/influencerRegister');
      },
      toLogin() {
        this.$router.push('/userLogin');
      }
    }
  };
  </script>
  
  <style scoped>
  .register-sponsor {
    max-width: 500px;
    margin: 0 auto;
  }
  
  .card {
    border-radius: 10px;
  }
  
  .card-header {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  
  button {
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #0d6efd !important;
  }
  </style>
  