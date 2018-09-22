/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/views/layout/Layout'

const tableRouter = {
  path: '/userinfo',
  component: Layout,
  redirect: '/userinfo/suer',
  name: 'userinfo',
  meta: {
    title: '用户管理',
    icon: 'table'
  },
  children: [
    {
      path: 'dynamic-table',
      component: () => import('@/views/table/dynamicTable/index'),
      name: 'dynamicTable',
      meta: { title: 'dynamicTable' }
    },
    {
      path: 'userinfo',
      component: () => import('@/views/userinfo/userinfo'),
      name: 'userinfo',
      meta: { title: '用户管理' }
    }
  ]
}
export default tableRouter
