#import "VKDelegate.h"
#import <UIKit/UIViewController.h>
#import "VKSdkFramework.framework/Headers/VKSdk.h"

@implementation OurVk

VKSdk *vkInstance;

//Set Delegate
id<VKSdkDelegate> _delegate;
id<VKSdkUIDelegate> _uiDelegate;
NSString *userID;

- (NSString *) getUserId{
    return userID;
}

- (void) setDelegate:(id)delegate{
    _delegate = delegate;
}

- (void) SetUiDelegate: (id) uiDelegate{
    _uiDelegate = uiDelegate;
}

//override delagate method
- (void) vkSdkAccessAuthorizationFinishedWithResult:(VKAuthorizationResult *)result{
    NSString *res = result.token.accessToken;
    userID = result.token.userId;
    [_delegate vkSdkAccessAuthorizationFinishedWithResult:res];
}

- (void) vkSdkUserAuthorizationFailed{
    [_delegate vkSdkUserAuthorizationFailed];
}

- (void) vkSdkAccessTokenUpdated:(VKAccessToken *)newToken oldToken:(VKAccessToken *)oldToken{
    userID = newToken.userId;
    [_delegate vkSdkAccessTokenUpdated:newToken.accessToken oldToken:oldToken.accessToken];
}

- (void) vkSdkTokenHasExpired:(VKAccessToken *)expiredToken{
    [_delegate vkSdkTokenHasExpired:expiredToken];
}

- (void) vkSdkAuthorizationStateUpdatedWithResult:(VKAuthorizationResult *)result{
    NSString *res = result.token.accessToken;
    userID = result.token.userId;
    [_delegate vkSdkAuthorizationStateUpdatedWithResult:res];
}


////////////////////////////////////////////////////////////////////////
// MAIN
////////////////////////////////////////////////////////////////////////


- (void) vkSession:(NSString *)appID {
    NSArray *SCOPE = @[@"friends", @"email"];

    vkInstance = [VKSdk initializeWithAppId:appID];
    [vkInstance registerDelegate:self];
    [vkInstance setUiDelegate:_uiDelegate];


    [VKSdk wakeUpSession:SCOPE completeBlock:^(VKAuthorizationState state, NSError *error) {
        if (state == VKAuthorizationAuthorized) {
            printf("auth");
            // Authorized and ready to go
        } else if (state == VKAuthorizationInitialized){
            printf("need auth");
            [VKSdk authorize:SCOPE];
        }else if (state == VKAuthorizationError){
            printf("error1");
        }
        else if (error) {
            printf("error");
            // Some error happend, but you may try later
        }
    }];
}
@end

@implementation VKUIDelegate

- (void) presentController:(UIViewController *)controller{
    UIViewController *top = [UIApplication sharedApplication].keyWindow.rootViewController;
    [top presentViewController:controller animated:YES completion:nil];
}

@end