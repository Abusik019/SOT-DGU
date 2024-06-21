import './App.css'
import { Routes, Route } from 'react-router-dom'
import Main from './pages/Main'
import Methodology from './pages/Methodology';
import { Header } from './components/Header';

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/' element={<Main />}/>
        <Route path='/methodology' element={<Methodology />}/>
      </Routes>
    </>
  )
}

export default App
