from app.utils.organization import create_random_org

def test_create_org(client):
    data = {"name":"myorganization"}
    response = client.post("/org",json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "myorganization"
    assert response.json()["status"] == 'Active'
    
def test_fetch_org_created(client, database_session):
    org = create_random_org(database=database_session)
    response = client.get(f"org/{org.org_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == org.name
    
    