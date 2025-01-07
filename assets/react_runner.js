import React, {
  useState,
  useEffect,
  useContext,
  useReducer,
  useRef,
  useMemo,
  useCallback,
} from "react";
import {
  LiveProvider,
  LiveEditor,
  LiveError,
  LivePreview,
} from "react-live-runner";
// import "bootstrap/dist/css/bootstrap.min.css";

export function ReactRunner({ code, preview, editor, error }) {
  // const code = "<h1>JT</h1>";
  const scope = {
    React,
    useState,
    useEffect,
    useContext,
    useReducer,
    useRef,
    useMemo,
    useCallback,
  };
  // console.log(code);
  return (
    <div
    // className="container rounded"
    // style={{ height: "70vh", width: "55vw", overflow: "auto" }}
    >
      <ErrorBoundary>
        <LiveProvider code={code} scope={scope}>
          <LivePreview />
          {error && <LiveError />}
          {editor && <LiveEditor />}
        </LiveProvider>
      </ErrorBoundary>

      {/* <LiveProvider code={code} scope={scope}>
        <div className="d-flex flex-column flex-lg-row h-100">
          <div
            className="rounded p-2 mb-3 mb-lg-0 me-lg-3"
            style={{ height: "70vh", width:"100%", flex: "1", overflow: "auto" }}
          >
            <LivePreview />
          </div>
          <div
            className="rounded p-2"
            style={{ height: "70vh", flex: "1", overflow: "auto" }}
          >
            <LiveEditor />
          </div>
        </div>
        <div className="text-danger mt-3">
          <LiveError />
        </div>
      </LiveProvider> */}
    </div>
  );
}

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, errorMessage: "" };
  }

  static getDerivedStateFromError(error) {
    // Update state to display fallback UI
    return { hasError: true, errorMessage: error.message };
  }

  componentDidCatch(error, errorInfo) {
    // Log error details (optional)
    console.error("ErrorBoundary caught an error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Render fallback UI
      return (
        <div className="text-danger">
          <h2>Something went wrong:</h2>
          <p>{this.state.errorMessage}</p>
        </div>
      );
    }

    return this.props.children;
  }
}
