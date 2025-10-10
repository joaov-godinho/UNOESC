using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Arquivos.Data;
using Arquivos.Models;

namespace Arquivos.Utils
{
    public static class Bootstrapper
    {
        public static void ChargeClients()
        {
            var c1 = new Client{
                Id = 1,
                FirstName = "João Vitor",
                LastName = "Godinho",
                CPF = "000.000.000-00",
                email = "joaovitor.godinho@unoesc.edu.br"
            };
            DataSet.Clients.Add(c1);

            DataSet.Clients.Add(
                new Client{
                Id = 2,
                FirstName = "Mauricio Roberto",
                LastName = "Gonzatto",
                CPF = "000.000.000-01",
                email = "mauricio.gonzatto@unoesc.edu.br"
              }
            );
            
            DataSet.Clients.Add(
                new Client{
                Id = 3,
                FirstName = "Fulano",
                LastName = "Silva",
                CPF = "000.000.000-02",
                email = "fulano.silva@unoesc.edu.br"
                }
            );
        }
        public static void ChargeAnimals()
        {
            DataSet.Animals.Add(
                new Animal{
                    Id = 1,
                    Name = "Bidu",
                    Raca = "Pinscher",
                    Nascimento = "10-10-2018"
                } 
            );   
        }

        public static void ChargeVets()
        {
            DataSet.Vets.Add(
                new Vet{
                    Id = 1,
                    FirstName = "Ciclano",
                    LastName = "Pinto",
                    CPF = "000.000.000-03",
	                CRMV = "98765"
                } 
            );   
        }

        public static void ChargeClinicas()
        {
            DataSet.Clinicas.Add(
                new Clinica{
                    Id = 1,
                    Name = "PetVet",
                    CNPJ = "00.000.000/0001-01",
                    Telefone = "(49) 99970-7070",
	        Endereco = "Rua x, Videira - SC, Brasil"
                }
            );
        }
    }
}