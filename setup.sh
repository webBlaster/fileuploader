export FLASK_APP=main.py
export FLASK_ENV=development

#cloudinary api keys
export CLOUD_NAME=webblaster
export CLOUD_API_KEY=435854196983661
export CLOUD_API_SECRET=J_82bJf3irUzd9aYaQMjMD98QtA

#database
export DATABASE_URL=postgres://uloptrxlevybej:4e9942987b58006a0ae41f2702778c034c6fe35896037d77c503d355a24f71f0@ec2-18-209-187-54.compute-1.amazonaws.com:5432/da8vm3pfoloosi

echo "done setting up environ vars"