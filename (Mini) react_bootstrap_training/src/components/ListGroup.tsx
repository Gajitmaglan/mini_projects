import ListGroup from "react-bootstrap/ListGroup";
import "./list-group.css";

const ItemList = () => {
  return (
    <>
      <ListGroup className="myList">
        <ListGroup.Item variant="dark" className="highlight-on-hover">
          Dark
        </ListGroup.Item>
        <ListGroup.Item className="highlight-on-hover" variant="dark">
          Light
        </ListGroup.Item>
        <ListGroup.Item className="highlight-on-hover" variant="dark">
          Sepia
        </ListGroup.Item>
      </ListGroup>
    </>
  );
};

export default ItemList;
