using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace PSIUWeb.Migrations
{
    public partial class MidiaEnum : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "TipoMidia",
                table: "Midias");

            migrationBuilder.AddColumn<int>(
                name: "TypeMidia",
                table: "Midias",
                type: "int",
                nullable: false,
                defaultValue: 0);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "TypeMidia",
                table: "Midias");

            migrationBuilder.AddColumn<string>(
                name: "TipoMidia",
                table: "Midias",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");
        }
    }
}
