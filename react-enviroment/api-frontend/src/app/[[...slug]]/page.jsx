import { ClientOnly } from './client'
 
export function generateStaticParams() {
  return [
    { slug: [''] },
    { slug: ['lobby'] },
  ];
}
 
export default function Page() {
  return <ClientOnly />
}