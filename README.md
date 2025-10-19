# aws-serverless-order-processor
Implementação de uma arquitetura serverless completa na AWS, integrando Lambda, SQS, DynamoDB e SNS — com segurança reforçada via IAM Roles. Tudo automatizado, escalável e monitorado com CloudWatch.

# 🚀 AWS Serverless Order Processor  
> Automação de Pedidos com Amazon SQS, AWS Lambda, DynamoDB e SNS  

---

## 🧠 Visão Geral  

Este projeto implementa uma **arquitetura serverless completa** na AWS para processar pedidos de forma **assíncrona, escalável e automática**, utilizando apenas serviços **gerenciados** e dentro do **Free Tier da AWS**.

💡 A ideia central é demonstrar, na prática, como funciona o fluxo entre:
- **Amazon SQS** → fila de pedidos recebidos  
- **AWS Lambda** → função que processa os pedidos  
- **Amazon DynamoDB** → banco NoSQL para armazenar dados  
- **Amazon SNS** → notificação em tempo real  
- **Amazon CloudWatch** → monitoramento e logs  

---

## ⚙️ Arquitetura do Sistema  


        +-------------+
        |   Cliente   |
        +-------------+
               |
               v
      +-------------------+
      | Amazon SQS Queue  |  ← Recebe pedidos
      +-------------------+
               |
               v
      +---------------------+
      | AWS Lambda (Python) |  ← Processa mensagens
      +---------------------+
          |             |
          v             v
 +----------------+   +-----------------+
 | DynamoDB Table |   | Amazon SNS Topic |
 |  OrdersTable   |   | Order Alerts     |
 +----------------+   +-----------------+

          ↑
          |
   +-------------------+
   | AWS CloudWatch    |
   | Logs & Métricas   |
   +-------------------+


---

## 🧩 Serviços AWS Utilizados  

| Serviço | Descrição |
|----------|------------|
| **Amazon SQS** | Gerencia filas de pedidos e garante entrega assíncrona |
| **AWS Lambda** | Processa as mensagens da fila sem necessidade de servidor |
| **Amazon DynamoDB** | Armazena os dados de pedidos de forma NoSQL |
| **Amazon SNS** | Envia notificações em tempo real sobre novos pedidos |
| **Amazon CloudWatch** | Monitora logs e desempenho da função Lambda |
| **IAM Roles** | Controla o acesso entre os serviços com segurança |

---

## 🧰 Tecnologias e Linguagem  

- **Python 3.x**  
- **Boto3 (AWS SDK for Python)**  
- **AWS Console / IAM Roles**  

---

## 🧠 Funcionamento do Projeto  

1️⃣ Um **pedido** é enviado para a **fila SQS**  
2️⃣ A **função Lambda** é acionada automaticamente  
3️⃣ Os dados do pedido são gravados na **tabela DynamoDB**  
4️⃣ Uma **notificação SNS** é enviada (por e-mail)  
5️⃣ Tudo é monitorado pelo **CloudWatch Logs**  

---

