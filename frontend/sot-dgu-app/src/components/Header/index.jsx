import Navbar from '../Navbar'
import styles from './style.module.css'
import logo from '../../assets/logo.png'

export const Header = () => {
  return (
    <div className={styles.header}>
      <Navbar />
      <img src={logo}/>
      <button>Войти</button>
    </div>
  )
}
