//
//  FbDelegate.m
//  vk-api
//
//  Created by admin on 24.08.16.
//
//

#import <Foundation/Foundation.h>
#import "FbDelegate.h"

@implementation FbAuth

id<FbDelegate> _delegate;

- (void) setDelegate:(id<FbDelegate>)delegate{
    _delegate = delegate;
}

- (NSString *) login{

    FBSDKLoginManager *login = [[FBSDKLoginManager alloc] init];
    [login
     logInWithReadPermissions: @[@"public_profile"]
     fromViewController:nil
     handler:^(FBSDKLoginManagerLoginResult *result, NSError *error) {
         if (error) {
             NSLog(@"Process error");
         } else if (result.isCancelled) {
             NSLog(@"Cancelled");
         } else {
             NSLog(@"Logged in");
             FBSDKAccessToken  *token = [FBSDKAccessToken currentAccessToken];
             [self getToken:token.tokenString];

         }
     }];

    return @"done";
}

- (void) getToken: (NSString *) token{
    [_delegate getToken:token];
    NSLog(@"Logged");
}
@end