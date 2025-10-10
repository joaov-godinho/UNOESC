using PSIUWeb.Models;

namespace PSIUWeb.Data.Interface
{
    public interface IContentCategoryRepository
    {
        public ContentCategory? GetContentCategoryById(int id);

        public IQueryable<ContentCategory>? GetContentCategories();

        public ContentCategory? Update(ContentCategory cc);

        public ContentCategory? Delete(int id);

        public ContentCategory? Create(ContentCategory cc);
    }
}
