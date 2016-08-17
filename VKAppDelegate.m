//
//  VKAppDelegate.m
//  vk-api
//
//  Created by admin on 12.08.16.
//
//

#import "VKAppDelegate.h"
#import "VKSdkFramework.framework/Headers/VKSdk.h"
#import <UIKit/UIApplication.h>


@implementation SDLUIKitDelegate (Maintenance)

//+ (NSString *)getAppDelegateClassName
//{
//    /* subclassing notice: when you subclass this appdelegate, make sure to add
//     * a category to override this method and return the actual name of the
//     * delegate */
//    return @"SDLUIKitDelegate";
//}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation
{
    [VKSdk processOpenURL:url fromApplication:UIApplicationOpenURLOptionsSourceApplicationKey];
    NSURL *fileURL = url.filePathURL;
    if (fileURL != nil) {
        SDL_SendDropFile([fileURL.path UTF8String]);
    } else {
        SDL_SendDropFile([url.absoluteString UTF8String]);
    }
    return YES;
}

@end
