#include <functional>
#include <gazebo/common/common.hh>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo {
class ObstaclePlugin : public ModelPlugin {
    public:
    void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf) {
        // Store the pointer to the model
        this->model = _parent;

        // Listen to the update event. This event is broadcast every
        // simulation iteration.
        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
            std::bind(&ObstaclePlugin::OnUpdate, this));

        if (_sdf->HasElement("iter")) {
            this->iter = _sdf->Get<int>("iter");
        }
        if (_sdf->HasElement("linear_vel")) {
            this->linear_vel = _sdf->Get<float>("linear_vel");
        }
        if (_sdf->HasElement("direction")) {
            this->direction = _sdf->Get<int>("direction");
        }
    }

    // Called by the world update start event
    public:
    void OnUpdate() {
        switch (direction)
        {
        case 0:
            vel_x = linear_vel;
            break;
        case 1:
            vel_y = linear_vel;
            break;
        case 2:
            vel_x = -linear_vel;
            break;
        case 3:
            vel_y = -linear_vel;
            break;
        default:
            break;
        }
        if (counter < iter) this->model->SetLinearVel(ignition::math::Vector3d(vel_x, vel_y, 0));
        else if (counter < iter*2) this->model->SetLinearVel(ignition::math::Vector3d(-vel_x, -vel_y, 0));
        else counter = 0;
        counter++;
    }

    // Pointer to the model
    private:
    physics::ModelPtr model;

    int counter;
    int iter;
    float linear_vel;
    int direction;
    float vel_x = 0;
    float vel_y = 0;

    // Pointer to the update event connection
    private:
    event::ConnectionPtr updateConnection;
};

// Register this plugin with the simulator
GZ_REGISTER_MODEL_PLUGIN(ObstaclePlugin)
} // namespace gazebo