#include <functional>
#include <gazebo/common/common.hh>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo {
class MyModelPlugin : public ModelPlugin {
    public:
    void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf) {
        // Store the pointer to the model
        this->model = _parent;

        // Listen to the update event. This event is broadcast every
        // simulation iteration.
        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
            std::bind(&MyModelPlugin::OnUpdate, this));

        if (_sdf->HasElement("iter")) {
            this->iter = _sdf->Get<int>("iter");
        }
        if (_sdf->HasElement("linear_vel")) {
            this->linear_vel = _sdf->Get<float>("linear_vel");
        }
    }

    // Called by the world update start event
    public:
    void OnUpdate() {
        // Apply a small linear velocity to the model.

        if (this->counter < iter) this->model->SetLinearVel(ignition::math::Vector3d(linear_vel, 0, 0));
        else if (this->counter < iter*2) this->model->SetLinearVel(ignition::math::Vector3d(0, linear_vel, 0));
        else if (this->counter < iter*3) this->model->SetLinearVel(ignition::math::Vector3d(-linear_vel, 0, 0));
        else if (this->counter < iter*4) this->model->SetLinearVel(ignition::math::Vector3d(0, -linear_vel, 0));
        else this->counter = 0;
        this->counter++;
    }

    // Pointer to the model
    private:
    physics::ModelPtr model;

    int counter;
    int iter;
    float linear_vel;

    // Pointer to the update event connection
    private:
    event::ConnectionPtr updateConnection;
};

// Register this plugin with the simulator
GZ_REGISTER_MODEL_PLUGIN(MyModelPlugin)
} // namespace gazebo