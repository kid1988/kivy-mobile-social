#import <Foundation/NSObject.h>
#import <UIKit/UIViewController.h>
#import "VKSdkFramework.framework/Headers/VKSdk.h"


@interface VKUIDelegate : UIViewController
- (void) presentController: (UIViewController *) controller;

@end

@interface OurVk : NSObject <VKSdkDelegate>
@property (strong, nonatomic) id<VKSdkDelegate> delegate;
@property (strong, nonatomic) id<VKSdkUIDelegate> uiDelegate;
- (void) setDelegate: (id<VKSdkDelegate>) delegate;
- (void) setUiDelegate: (id<VKSdkUIDelegate>) uiDelegate;
- (void) vkSession: (NSString *) appId;
- (NSString *) getUserId;

@end
