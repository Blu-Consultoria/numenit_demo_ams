import React from 'react'
import Sidebar from '@/app/components/navbar'

const Page = () => {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <div>page</div>
    </div>
  )
}

export default Page