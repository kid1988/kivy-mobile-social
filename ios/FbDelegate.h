//
//  FbDelegate.h
//  vk-api
//
//  Created by admin on 24.08.16.
//
//

#import <FBSDKCoreKit/FBSDKCoreKit.h>
#import <FBSDKLoginKit/FBSDKLoginKit.h>

@protocol FbDelegate <NSObject>

- (void) getToken: (NSString *) token;

@end

@interface FbAuth : NSObject <FbDelegate>
@property (strong, nonatomic) id<FbDelegate> delegate;
- (void) setDelegate:(id<FbDelegate>)delegate;
- (NSString *) login;
@end
