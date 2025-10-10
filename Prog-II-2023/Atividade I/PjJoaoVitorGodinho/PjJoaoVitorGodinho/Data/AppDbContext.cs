using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using PjJoaoVitorGodinho.Models;

namespace PjJoaoVitorGodinho.Data
{
    public class AppDbContext :
        IdentityDbContext<AppUser>
    {
        public AppDbContext(DbContextOptions options)
            : base(options)
        {
        }

        public DbSet<Psicologo>? Psicologos { get; set; }


    }
}