using PSIUWeb.Data.Interface;
using PSIUWeb.Models;
using System.Linq;

namespace PSIUWeb.Data.EF
{
    public class EFPsicoRepository : IPsicoRepository
    {
        private AppDbContext context;

        public EFPsicoRepository(AppDbContext ctx)
        {
            context = ctx;
        }

        public Psico? Create(Psico psico)
        {
            try
            {
                context.Psicos?.Add(psico);
                context.SaveChanges();
            }
            catch
            {
                return null;
            }

            return psico;
        }

        public Psico? Delete(int id)
        {
            Psico? psico = GetPsicoById(id);

            if (psico == null)
                return null;

            context.Psicos?.Remove(psico);
            context.SaveChanges();

            return psico;


        }

        public Psico? GetPsicoById(int id)
        {
            Psico? psico =
                context
                    .Psicos?
                    .Where(psico => psico.Id == id)
                    .FirstOrDefault();

            return psico;

        }

        public IQueryable<Psico>? GetPsicos()
        {
            return context.Psicos;
        }

        public Psico? Update(Psico psico)
        {
            try
            {
                context.Psicos?.Update(psico);
                context.SaveChanges();
            }
            catch
            {
                return null;
            }

            return psico;
        }


    }
}
