using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace PSIUWeb.Migrations
{
    public partial class PsicoEndereco : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Cep",
                table: "Psicos");

            migrationBuilder.AddColumn<string>(
                name: "Endereco",
                table: "Psicos",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Endereco",
                table: "Psicos");

            migrationBuilder.AddColumn<int>(
                name: "Cep",
                table: "Psicos",
                type: "int",
                nullable: false,
                defaultValue: 0);
        }
    }
}
