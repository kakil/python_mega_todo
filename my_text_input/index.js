const { Streamlit, StreamlitComponentBase, withStreamlitConnection } = require("streamlit-component-lib");
const React = require("react");
const ReactDOM = require("react-dom");

class CustomTextInput extends StreamlitComponentBase {
  render() {
    return (
      <input
        type="text"
        style={{ color: "blue" }}  // Set the text color here
        onChange={(event) => {
          Streamlit.setComponentValue(event.target.value);
        }}
      />
    );
  }
}

export default withStreamlitConnection(CustomTextInput);

const domContainer = document.querySelector('#root');
ReactDOM.render(React.createElement(CustomTextInput), domContainer);
