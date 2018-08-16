<template>



    <div>

        <Table :loading="loading" :columns="columns1" :data="data1"></Table>


        <Modal
                v-model="modal1"
                title="编辑"
                @on-ok="ok"
                @on-cancel="cancel">

            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                <FormItem label="Name" prop="name">
                    <Input v-model="formValidate.login_account" placeholder="用户账户"></Input>
                </FormItem>
                <FormItem label="E-mail" prop="mail">
                    <Input v-model="formValidate.mail" placeholder="邮箱"></Input>
                </FormItem>
                <FormItem label="City" prop="city">
                    <Select v-model="formValidate.icon" placeholder="图标">
                        <Option value="beijing">New York</Option>
                        <Option value="shanghai">London</Option>
                        <Option value="shenzhen">Sydney</Option>
                    </Select>
                </FormItem>
                <FormItem label="Date">
                    <Row>
                        <Col span="11">
                        <FormItem prop="date">
                            <DatePicker type="date" placeholder="Select date" v-model="formValidate.date"></DatePicker>
                        </FormItem>
                        </Col>
                        <Col span="2" style="text-align: center">-</Col>
                        <Col span="11">
                        <FormItem prop="time">
                            <TimePicker type="time" placeholder="Select time" v-model="formValidate.time"></TimePicker>
                        </FormItem>
                        </Col>
                    </Row>
                </FormItem>
                <FormItem label="Gender" prop="gender">
                    <RadioGroup v-model="formValidate.gender">
                        <Radio label="male">Male</Radio>
                        <Radio label="female">Female</Radio>
                    </RadioGroup>
                </FormItem>
                <FormItem label="Hobby" prop="interest">
                    <CheckboxGroup v-model="formValidate.interest">
                        <Checkbox label="Eat"></Checkbox>
                        <Checkbox label="Sleep"></Checkbox>
                        <Checkbox label="Run"></Checkbox>
                        <Checkbox label="Movie"></Checkbox>
                    </CheckboxGroup>
                </FormItem>
                <FormItem label="Desc" prop="desc">
                    <Input v-model="formValidate.desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="Enter something..."></Input>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="handleSubmit('formValidate')">Submit</Button>
                    <Button @click="handleReset('formValidate')" style="margin-left: 8px">Reset</Button>
                </FormItem>
            </Form>
        </Modal>



    </div>





</template>
<script>



    export default {
        data () {
            return {
                loading: true,
                modal1: false,
                columns1: [
                    {
                        title: '登录名',
                        key: 'login_account'
                    },
                    {
                        title: '邮箱',
                        key: 'email'
                    },
                    {
                        title: '头像',
                        key: 'icon'
                    },
                    {
                        title: 'Action',
                        key: 'action',
                        width: 150,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.show(params.index)
                                        }
                                    }
                                }, 'View'),
                                h('Button', {
                                    props: {
                                        type: 'success',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.edit(params.index)
                                        }
                                    }
                                }, '编辑'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.remove(params.index)
                                        }
                                    }
                                }, 'Delete')
                            ]);
                        }
                    }
                ],
                data1: [],
                formValidate: {
                    login_account: '',
                    email: '',
                    icon: '',
                    gender: '',
                    interest: [],
                    date: '',
                    time: '',
                    desc: ''
                },
                ruleValidate: {
                    login_account: [
                        { required: true, message: 'The name cannot be empty', trigger: 'blur' }
                    ],
                    email: [
                        { required: true, message: 'Mailbox cannot be empty', trigger: 'blur' },
                        { type: 'email', message: 'Incorrect email format', trigger: 'blur' }
                    ],
                    icon: [
                        { required: true, message: 'Please select the city', trigger: 'change' }
                    ],
                    gender: [
                        { required: true, message: 'Please select gender', trigger: 'change' }
                    ],
                    interest: [
                        { required: true, type: 'array', min: 1, message: 'Choose at least one hobby', trigger: 'change' },
                        { type: 'array', max: 2, message: 'Choose two hobbies at best', trigger: 'change' }
                    ],
                    date: [
                        { required: true, type: 'date', message: 'Please select the date', trigger: 'change' }
                    ],
                    time: [
                        { required: true, type: 'string', message: 'Please select time', trigger: 'change' }
                    ],
                    desc: [
                        { required: true, message: 'Please enter a personal introduction', trigger: 'blur' },
                        { type: 'string', min: 20, message: 'Introduce no less than 20 words', trigger: 'blur' }
                    ]
                }
            }
        },

        methods: {
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        this.$Message.success('Success!');
                    } else {
                        this.$Message.error('Fail!');
                    }
                })
            },
            show (index) {
                this.$Modal.info({
                    title: 'User Info',
                    content: `登录名称：${this.data1[index].login_account}<br>email：${this.data1[index].email}<br>头像：${this.data1[index].icon}`
                })
            },
            edit (index) {


                this.modal1=true;
                this.formValidate.login_account=this.data1[index].login_account;

//                this.$Modal.info({
//                    title: 'User Info',
//                    content: `登录名称：${this.data1[index].login_account}<br>email：${this.data1[index].email}<br>头像：${this.data1[index].icon}`
//                })
            },
            remove (index) {
                this.data1.splice(index, 1);
            }
        },
        created: function () {
            // `this` 指向 vm 实例


            var self = this;

            self.loading=true;

            $.ajax({
                    url:'http://127.0.0.1:5000/api/v1.1/commonuserinfos?page=1',
                    type:'get',
                    data: {},
                    success:function(data){


                        self.data1=data.items;

                    },
                    error:function(XMLHttpRequest, textStatus, errorThrown){
                        console.log("error")

                    },
                    complete:function (data) {
                        console.log("complete")
                        self.loading=false;
                    }
            });


        }
    }
</script>
<style scoped>


    .modal-header {

        display: block;
    }
</style>