from app import schemas


def test_get_all_members(authorized_client, test_members):
    res = authorized_client.get("/organizationmembers/")

    def validate(item):
        return schemas.OrganizationMemberResponse(**item)

    members_list = list(map(validate, res.json()))

    assert res.status_code == 200
    assert len(members_list) == len(test_members)


def test_unauthorized_get_all_members(client, test_members):
    res = client.get("/organizationmembers/")
    assert res.status_code == 401


def test_unauthorized_get_one_member(client, test_members):
    res = client.get(f"/organizationmembers/{test_members[0].id}")
    assert res.status_code == 401


def test_get_one_member_not_exist(authorized_client, test_members):
    res = authorized_client.get("/organizationmembers/999999")
    assert res.status_code == 404


def test_get_one_member(authorized_client, test_members):
    res = authorized_client.get(f"/organizationmembers/{test_members[0].id}")

    assert res.status_code == 200
    member = schemas.OrganizationMemberResponse(**res.json())
    assert member.id == test_members[0].id
    assert member.user_id == test_members[0].user_id
    assert member.organization_id == test_members[0].organization_id
    assert member.role == test_members[0].role