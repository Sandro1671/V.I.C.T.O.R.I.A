FROM mcr.microsoft.com/dotnet/runtime:7.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["VICTORIA/VICTORIA.csproj", "VICTORIA/"]
RUN dotnet restore "VICTORIA/VICTORIA.csproj"
COPY . .
WORKDIR "/src/VICTORIA"
RUN dotnet build "VICTORIA.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "VICTORIA.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "VICTORIA.dll"]
