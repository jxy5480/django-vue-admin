<template>
  <main>
    <div class="container" id="content">
      <form @submit.prevent="submit">
        <h2 class="mb-2">Login</h2>
        <div class="input">
          <label for="username">Username</label>
          <br />
          <input
            class="form-control"
            type="text"
            name="username"
            placeholder="Enter username"
          />
        </div>
        <div class="input">
          <label for="password">Password</label>
          <br />
          <input
            class="form-control"
            type="password"
            name="password"
            placeholder="Enter password"
          />
        </div>
        <button type="submit" class="mt-4 btn-pers" id="login_button">
          Login
        </button>
        <div
          class="alert alert-warning alert-dismissible fade show mt-5 d-none"
          role="alert"
          id="alert_1"
        ></div>
      </form>
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  setup() {
    const submit = async (e) => {
      const form = new FormData(e.target);
      const inputs = Object.fromEntries(form.entries());
      await axios.post("http://0.0.0.0:8000/api/portal/login/", inputs);
    };

    return {
      submit,
    };
  },
};
</script>
