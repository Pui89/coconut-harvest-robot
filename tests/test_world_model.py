from coconut_harvest_robot.world_model import OrchardWorldModel,Point3D,TargetState

def test_predict_target_position():
    w=OrchardWorldModel(robot_position=Point3D(0,0,0))
    w.upsert(TargetState("c1",Point3D(1,2,3),Point3D(1,0,0),.9,0.0))
    assert w.predict("c1",2).x==3
