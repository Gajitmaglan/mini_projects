import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

const cardImageList: string[] = [
  "/src/components/img/collection/1-286x286.jpg",
  "/src/components/img/collection/2-286x286.jpg",
  "/src/components/img/collection/3-286x286.jpg",
  "/src/components/img/collection/4-286x286.jpg",
  "/src/components/img/collection/5-286x286.jpg",
  "/src/components/img/collection/6-286x286.jpg",
  "/src/components/img/collection/7-286x286.jpg",
  "/src/components/img/collection/8-286x286.jpg",
  "/src/components/img/collection/9-286x286.jpg",
  "/src/components/img/collection/10-286x286.jpg",
];

function BasicExample() {
  return (
    <>
      <div className="d-flex flex-wrap justify-content-center">
        {cardImageList.map((image, index) => (
          <Card
            key={index}
            className="m-4"
            bg="dark"
            text="white"
            style={{ width: "18rem" }}
          >
            <Card.Img variant="top" src={image} />
            <Card.Body>
              <Card.Title className="text-center">Card Title</Card.Title>
              <Card.Text className="text-center">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </Card.Text>
              <div className="text-center">
                <Button className="mx-auto" variant="dark">
                  Add to Cart
                </Button>
                <Button className="mx-auto" variant="dark">
                  Buy Now
                </Button>
              </div>
            </Card.Body>
          </Card>
        ))}
      </div>
    </>
  );
}

export default BasicExample;
