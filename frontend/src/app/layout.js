import localFont from "next/font/local";
import "./globals.css";

const quicksandFont = localFont({
  src: [
    {
      path: "./fonts/Quicksand-Light.ttf",
      weight: "100",
      style: "normal",
    },  
    {
      path: "./fonts/Quicksand-Medium.ttf",
      weight: "300",
      style: "normal",
    },
    {
      path: "./fonts/Quicksand-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "./fonts/Quicksand-SemiBold.ttf",
      weight: "500",
      style: "normal",
    },    
    {
      path: "./fonts/Quicksand-Bold.ttf",
      weight: "600",
      style: "normal",
    },
  ],
  variable: "--font-quicksand",
});

export const metadata = {
  title: "Numen ES - Demo",
  description: "Hub de Operações da Numen IT.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={quicksandFont.variable}
      >
        {children}
      </body>
    </html>
  );
}