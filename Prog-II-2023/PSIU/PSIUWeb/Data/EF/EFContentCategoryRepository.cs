using PSIUWeb.Data.Interface;
using PSIUWeb.Models;

namespace PSIUWeb.Data.EF
{
    public class EFContentCategoryRepository : IContentCategoryRepository
    {

        private AppDbContext context;

        public EFContentCategoryRepository(AppDbContext context)
        {
            this.context = context;
        }
        public ContentCategory? Create(ContentCategory cc)
        {
            try
            {
                context.ContentCategories?.Add(cc);
                context.SaveChanges();
            }
            catch
            {
                return null;
            }

            return cc;
        }

        public ContentCategory? Delete(int id)
        {
            ContentCategory? cc = GetContentCategoryById(id);

            if (cc == null)
                return null;

            context.ContentCategories?.Remove(cc);
            context.SaveChanges();

            return cc;
        }

        public IQueryable<ContentCategory>? GetContentCategories()
        {
            return context.ContentCategories;
        }

        public ContentCategory? GetContentCategoryById(int id)
        {
            ContentCategory? cc =
                context
                    .ContentCategories?
                    .Where(cc => cc.Id == id)
                    .FirstOrDefault();

            return cc;
        }

        public ContentCategory? Update(ContentCategory cc)
        {
            try
            {
                context.ContentCategories?.Update(cc);
                context.SaveChanges();
            }
            catch
            {
                return null;
            }

            return cc;
        }
    }
}
