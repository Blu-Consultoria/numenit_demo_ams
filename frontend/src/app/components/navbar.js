"use client";

import React, { useState } from 'react';
import { FaTachometerAlt, FaTools, FaKey, FaBook, FaClock, FaBars } from 'react-icons/fa';

const navItems = [
    { label: 'Dashboard', path: '/dashboard', icon: <FaTachometerAlt /> },
    { label: 'Administrar Chamados', path: '/chamados', icon: <FaTools /> },
    { label: 'Gerenciador de Segredos', path: '/segredos', icon: <FaKey /> },
    { label: 'Base de Conhecimento', path: '/conhecimento', icon: <FaBook /> },
    { label: 'Banco de Horas', path: '/banco-horas', icon: <FaClock /> },
];

const Sidebar = () => {
    const [expanded, setExpanded] = useState(true);

    return (
        <nav className={`h-screen bg-[#222e3c] text-white flex flex-col py-6 transition-all duration-300 ${expanded ? 'w-60' : 'w-20'}`}>
            <button
                className="mb-8 mx-auto text-2xl focus:outline-none"
                onClick={() => setExpanded(!expanded)}
                aria-label="Expandir/reduzir menu"
            >
                <FaBars />
            </button>
            {expanded && (
                <div className="mb-8 text-center font-bold text-2xl">
                    Numenit Demo
                </div>
            )}
            <ul className="list-none p-0 m-0 flex-1">
                {navItems.map(item => (
                    <li key={item.path} className="my-4">
                        <a
                            href={item.path}
                            className="flex items-center px-4 py-3 rounded transition-colors duration-200 hover:bg-[#30405a] text-white no-underline"
                        >
                            <span className="text-xl">{item.icon}</span>
                            {expanded && <span className="ml-4">{item.label}</span>}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default Sidebar;
