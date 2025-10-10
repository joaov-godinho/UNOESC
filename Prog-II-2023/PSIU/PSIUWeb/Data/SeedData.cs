using Microsoft.EntityFrameworkCore;
using PSIUWeb.Models;

namespace PSIUWeb.Data
{
    public static class SeedData
    {

        public static void EnsurePopulated( 
            IApplicationBuilder app 
        )
        {
            AppDbContext context =
                app.ApplicationServices.CreateScope()
                .ServiceProvider.GetRequiredService<AppDbContext>();

            if (context.Database.GetPendingMigrations().Any())
            { 
                context.Database.Migrate();
            }

            if (!context.Pacients.Any())
            {
                context.Pacients.AddRange(
                    new Pacient
                    {
                        Name = "Mauricio",
                        BirthDate = new DateTime(1984, 7, 5),
                        Race = Race.Pardo,
                        Height = 180,
                        Weight = 88
                    },
                    new Pacient
                    {
                        Name = "Marcos",
                        BirthDate = new DateTime(1987, 2, 28),
                        Race = Race.Pardo,
                        Height = 175,
                        Weight = 90
                    }
                );

                context.SaveChanges();
            }

            if (!context.Psicos.Any())
            {
                context.Psicos.AddRange(
                    new Psico
                    {
                        Name = "Mauricio",
                        BirthDate = new DateTime(1984, 7, 5),
                        Race = Race.Pardo,
                        Crp = 18098765,
                        Endereco = "Rua Severino Paese",
                        Liberado = true
                    },
                    new Psico
                    {
                        Name = "Marcos",
                        BirthDate = new DateTime(1987, 2, 28),
                        Race = Race.Pardo,
                        Crp = 12345678,
                        Endereco = "Rua Severino Paese",
                        Liberado = true

                    }
                );

                context.SaveChanges();
            }

            if (!context.Midias.Any())
            {
                context.Midias.AddRange(
                    new Midia
                    {
                        Url = "teste",
                        TypeMidia = TypeMidia.Imagem
                    },
                    new Midia
                    {
                        Url = "teste2",
                        TypeMidia = TypeMidia.Música
                    }
                );

                context.SaveChanges();
            }

        }

    }
}
