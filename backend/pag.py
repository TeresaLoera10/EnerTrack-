import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import { AlertTriangle } from "lucide-react";

export default function EnergyDashboard() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    if (username === "admin" && password === "password") {
      setLoggedIn(true);
    } else {
      alert("Usuario o contraseña incorrectos");
    }
  };

  const data = [
    { name: "Enero", consumo: 120 },
    { name: "Febrero", consumo: 150 },
    { name: "Marzo", consumo: 90 },
    { name: "Abril", consumo: 180 },
    { name: "Mayo", consumo: 210 },
  ];

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      {!loggedIn ? (
        <Card className="p-6 w-96 shadow-lg">
          <h2 className="text-xl font-bold mb-4 text-center">Login</h2>
          <Input placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} className="mb-2" />
          <Input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} className="mb-4" />
          <Button className="w-full" onClick={handleLogin}>Ingresar</Button>
        </Card>
      ) : (
        <div className="p-6 w-full max-w-4xl">
          <h2 className="text-2xl font-bold mb-4">Consumo Energético</h2>
          <Card className="mb-6">
            <CardContent>
              <LineChart width={600} height={300} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="consumo" stroke="#8884d8" />
              </LineChart>
            </CardContent>
          </Card>
          <div className="flex items-center gap-2 p-4 bg-red-200 text-red-800 rounded-lg">
            <AlertTriangle />
            <span>Alerta: Consumo energético elevado en mayo.</span>
          </div>
        </div>
      )}
    </div>
  );
}
