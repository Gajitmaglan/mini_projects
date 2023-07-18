import { useState } from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import "./form.css";

const ContactForm = () => {
  const formControlStyles = {
    backgroundColor: "#343a40",
    color: "white",
  };

  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Here, you can handle the form submission, such as making an API call or performing validation

    // Clear form fields after successful submission
    setName("");
    setSurname("");
    setEmail("");
    setPhone("");
    setMessage("");
  };

  return (
    <Form
      onSubmit={handleSubmit}
      className="bg-dark text-light p-4 w-50 mx-auto mb-5 placeholder-light"
    >
      <Row>
        <Col>
          <Form.Group controlId="formName">
            <Form.Label>Name</Form.Label>
            <Form.Control
              style={formControlStyles}
              type="text"
              placeholder="Enter your name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </Form.Group>
        </Col>

        <Col>
          <Form.Group controlId="formSurname">
            <Form.Label>Surname</Form.Label>
            <Form.Control
              style={formControlStyles}
              type="text"
              placeholder="Enter your surname"
              value={surname}
              onChange={(e) => setSurname(e.target.value)}
            />
          </Form.Group>
        </Col>
      </Row>

      <Form.Group controlId="formEmail">
        <Form.Label>Email</Form.Label>
        <Form.Control
          style={formControlStyles}
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formPhone">
        <Form.Label>Mobile Phone</Form.Label>
        <Form.Control
          style={formControlStyles}
          type="tel"
          placeholder="Enter your mobile phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formMessage">
        <Form.Label>Message</Form.Label>
        <Form.Control
          style={formControlStyles}
          as="textarea"
          rows={3}
          placeholder="Enter your message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </Form.Group>

      <div className="text-center mt-3">
        <Button variant="dark" type="submit" className="mx-auto">
          Submit
        </Button>
      </div>
    </Form>
  );
};

export default ContactForm;
