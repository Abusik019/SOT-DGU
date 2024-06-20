import React from 'react';
import { DownOutlined } from '@ant-design/icons';
import { Dropdown, Space } from 'antd';
import { NavLink } from 'react-router-dom'

const items = [
  {
    label: (
      <NavLink to="/methodology">
        О центре
      </NavLink>
    ),
    key: '0',
  },
  {
    label: (
      <NavLink to="/methodology">
        Сотрудники
      </NavLink>
    ),
    key: '1',
  },
  {
    label: (
      <NavLink to="/methodology">
        Материалы
      </NavLink>
    ),
    key: '2',
  },
  {
    label: (
      <NavLink to="/methodology">
        Презентации
      </NavLink>
    ),
    key: '3',
  },
  {
    label: (
      <NavLink to="/methodology">
        Видеоматериалы
      </NavLink>
    ),
    key: '4',
  },
  {
    label: (
      <NavLink to="/methodology">
        Контакты
      </NavLink>
    ),
    key: '5',
  },
  {
    label: (
      <NavLink to="/methodology">
        Нормативные документы
      </NavLink>
    ),
    key: '6',
  },
];
const Navbar = () => (
  <Dropdown
    menu={{
      items,
    }}
  >
    <a onClick={(e) => e.preventDefault()}>
      <Space>
        Меню
        <DownOutlined />
      </Space>
    </a>
  </Dropdown>
);
export default Navbar;