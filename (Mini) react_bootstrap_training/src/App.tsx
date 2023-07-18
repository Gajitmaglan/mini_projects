import "bootstrap/dist/css/bootstrap.css";
import BasicExample from "./components/card";
import ShopNavbar from "./components/shopnavbar";
import ItemList from "./components/ListGroup";
import ContactForm from "./components/Form";
import "bootstrap/dist/css/bootstrap.css";

const App = () => {
  return (
    <div style={{ backgroundColor: "#343a40", paddingBottom: "0.5rem" }}>
      <ShopNavbar />
      {/* <ItemList /> */}
      <BasicExample />
      <ContactForm />
    </div>
  );
};

export default App;
