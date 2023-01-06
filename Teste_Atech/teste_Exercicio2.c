#include "Unity/unity.h"
#include "funcao2.h"

void setup(){}

void teardown(void){}

void test_funcao(int funcao){

    TEST_ASSERT_MESSAGE(1==funcao(),"Teste passou!" );
    TEST_ASSERT_MESSAGE(1!=funcao(),"Teste falhou!" );

};

int main2(){

    UNITY_BEGIN();
    RUN_TEST(test_funcao);
    return UNITY_END();
};