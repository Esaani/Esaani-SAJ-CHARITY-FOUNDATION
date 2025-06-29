import { programs } from "@/data/programsData";

export default function WhatWeDoPage() {
  return (
    <div className="max-w-6xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold mb-8 text-center">What We Do</h1>
      <p className="text-lg text-gray-600 mb-12 text-center max-w-3xl mx-auto">
        Our comprehensive programs address the most pressing needs in our communities. 
        We focus on education, nutrition, youth development, healthcare, and community support.
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {programs.map(program => (
          <div key={program.id} className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
            <div className="relative h-48 bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
              <span className="text-6xl">{program.icon}</span>
            </div>
            <div className="p-6">
              <h2 className="text-xl font-semibold mb-3">{program.title}</h2>
              <p className="text-gray-600 mb-4">{program.description}</p>
              <div className="space-y-2">
                {program.details.map((detail, index) => (
                  <div key={index} className="flex items-center text-sm text-gray-700">
                    <span className="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>
                    {detail}
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
} 