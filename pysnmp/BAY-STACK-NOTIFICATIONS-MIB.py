# SNMP MIB module (BAY-STACK-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:14 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(bayStackConfigExpectedStackSize,
 bayStackUnitConfigIndex) = mibBuilder.importSymbols(
    "BAY-STACK-MIB",
    "bayStackConfigExpectedStackSize",
    "bayStackUnitConfigIndex")

(dot1xAuthBackendAuthState,
 dot1xAuthPaeState) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthBackendAuthState",
    "dot1xAuthPaeState")

(InterfaceIndex,
 ifAdminStatus,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAdminStatus",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(s5AgSysUsbTargetUnit,
 s5AgentScriptStatus) = mibBuilder.importSymbols(
    "S5-AGENT-MIB",
    "s5AgSysUsbTargetUnit",
    "s5AgentScriptStatus")

(s5ChasComType,) = mibBuilder.importSymbols(
    "S5-CHASSIS-MIB",
    "s5ChasComType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackNotificationsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 2)
)
bayStackNotificationsMib.setRevisions(
        ("2014-07-07 00:00",
         "2014-01-27 00:00",
         "2013-10-11 00:00",
         "2013-08-22 00:00",
         "2013-03-19 00:00",
         "2012-09-04 00:00",
         "2012-08-22 00:00",
         "2012-08-16 00:00",
         "2012-06-21 00:00",
         "2012-06-20 00:00",
         "2011-11-30 00:00",
         "2010-12-21 00:00",
         "2009-09-28 00:00",
         "2008-07-09 00:00",
         "2008-03-31 00:00",
         "2007-03-05 00:00",
         "2006-04-06 00:00",
         "2006-04-04 00:00",
         "2005-08-22 00:00",
         "2005-06-30 00:00",
         "2005-03-26 00:00",
         "2004-08-06 00:00",
         "2004-08-02 00:00",
         "2004-07-20 00:00",
         "2003-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsnObjects_ObjectIdentity = ObjectIdentity
bsnObjects = _BsnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1)
)
_BsnEapAccessViolationMacAddress_Type = MacAddress
_BsnEapAccessViolationMacAddress_Object = MibScalar
bsnEapAccessViolationMacAddress = _BsnEapAccessViolationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 1),
    _BsnEapAccessViolationMacAddress_Type()
)
bsnEapAccessViolationMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapAccessViolationMacAddress.setStatus("current")


class _BsnLoginFailureType_Type(Integer32):
    """Custom type bsnLoginFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("serialConsole", 4),
          ("ssh", 2),
          ("telnet", 1),
          ("web", 3))
    )


_BsnLoginFailureType_Type.__name__ = "Integer32"
_BsnLoginFailureType_Object = MibScalar
bsnLoginFailureType = _BsnLoginFailureType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 2),
    _BsnLoginFailureType_Type()
)
bsnLoginFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLoginFailureType.setStatus("current")
_BsnLoginFailureAddressType_Type = InetAddressType
_BsnLoginFailureAddressType_Object = MibScalar
bsnLoginFailureAddressType = _BsnLoginFailureAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 3),
    _BsnLoginFailureAddressType_Type()
)
bsnLoginFailureAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLoginFailureAddressType.setStatus("current")
_BsnLoginFailureAddress_Type = InetAddress
_BsnLoginFailureAddress_Object = MibScalar
bsnLoginFailureAddress = _BsnLoginFailureAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 4),
    _BsnLoginFailureAddress_Type()
)
bsnLoginFailureAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLoginFailureAddress.setStatus("current")
_BsnLoginFailureUsername_Type = SnmpAdminString
_BsnLoginFailureUsername_Object = MibScalar
bsnLoginFailureUsername = _BsnLoginFailureUsername_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 5),
    _BsnLoginFailureUsername_Type()
)
bsnLoginFailureUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLoginFailureUsername.setStatus("current")


class _BsnActualStackSize_Type(Integer32):
    """Custom type bsnActualStackSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BsnActualStackSize_Type.__name__ = "Integer32"
_BsnActualStackSize_Object = MibScalar
bsnActualStackSize = _BsnActualStackSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 6),
    _BsnActualStackSize_Type()
)
bsnActualStackSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnActualStackSize.setStatus("current")
_BsnEapUbpFailureIfIndex_Type = InterfaceIndex
_BsnEapUbpFailureIfIndex_Object = MibScalar
bsnEapUbpFailureIfIndex = _BsnEapUbpFailureIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 7),
    _BsnEapUbpFailureIfIndex_Type()
)
bsnEapUbpFailureIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapUbpFailureIfIndex.setStatus("current")
_BsnEapUbpFailureMacAddress_Type = MacAddress
_BsnEapUbpFailureMacAddress_Object = MibScalar
bsnEapUbpFailureMacAddress = _BsnEapUbpFailureMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 8),
    _BsnEapUbpFailureMacAddress_Type()
)
bsnEapUbpFailureMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapUbpFailureMacAddress.setStatus("current")


class _BsnEapUbpFailureRoleString_Type(OctetString):
    """Custom type bsnEapUbpFailureRoleString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BsnEapUbpFailureRoleString_Type.__name__ = "OctetString"
_BsnEapUbpFailureRoleString_Object = MibScalar
bsnEapUbpFailureRoleString = _BsnEapUbpFailureRoleString_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 9),
    _BsnEapUbpFailureRoleString_Type()
)
bsnEapUbpFailureRoleString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapUbpFailureRoleString.setStatus("current")


class _BsnTrialLicenseExpirationTime_Type(Integer32):
    """Custom type bsnTrialLicenseExpirationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BsnTrialLicenseExpirationTime_Type.__name__ = "Integer32"
_BsnTrialLicenseExpirationTime_Object = MibScalar
bsnTrialLicenseExpirationTime = _BsnTrialLicenseExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 10),
    _BsnTrialLicenseExpirationTime_Type()
)
bsnTrialLicenseExpirationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrialLicenseExpirationTime.setStatus("current")


class _BsnTrialLicenseExpirationNumber_Type(Integer32):
    """Custom type bsnTrialLicenseExpirationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BsnTrialLicenseExpirationNumber_Type.__name__ = "Integer32"
_BsnTrialLicenseExpirationNumber_Object = MibScalar
bsnTrialLicenseExpirationNumber = _BsnTrialLicenseExpirationNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 11),
    _BsnTrialLicenseExpirationNumber_Type()
)
bsnTrialLicenseExpirationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrialLicenseExpirationNumber.setStatus("current")
_BsnEnteredForcedStackModeMAC_Type = MacAddress
_BsnEnteredForcedStackModeMAC_Object = MibScalar
bsnEnteredForcedStackModeMAC = _BsnEnteredForcedStackModeMAC_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 12),
    _BsnEnteredForcedStackModeMAC_Type()
)
bsnEnteredForcedStackModeMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEnteredForcedStackModeMAC.setStatus("current")
_BsnEapRAVErrorMacAddress_Type = MacAddress
_BsnEapRAVErrorMacAddress_Object = MibScalar
bsnEapRAVErrorMacAddress = _BsnEapRAVErrorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 13),
    _BsnEapRAVErrorMacAddress_Type()
)
bsnEapRAVErrorMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapRAVErrorMacAddress.setStatus("current")
_BsnEapRAVErrorPort_Type = InterfaceIndex
_BsnEapRAVErrorPort_Object = MibScalar
bsnEapRAVErrorPort = _BsnEapRAVErrorPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 14),
    _BsnEapRAVErrorPort_Type()
)
bsnEapRAVErrorPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEapRAVErrorPort.setStatus("current")
_BsnEnteredForcedStackModeAddressType_Type = InetAddressType
_BsnEnteredForcedStackModeAddressType_Object = MibScalar
bsnEnteredForcedStackModeAddressType = _BsnEnteredForcedStackModeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 15),
    _BsnEnteredForcedStackModeAddressType_Type()
)
bsnEnteredForcedStackModeAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEnteredForcedStackModeAddressType.setStatus("current")
_BsnEnteredForcedStackModeAddress_Type = InetAddress
_BsnEnteredForcedStackModeAddress_Object = MibScalar
bsnEnteredForcedStackModeAddress = _BsnEnteredForcedStackModeAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 16),
    _BsnEnteredForcedStackModeAddress_Type()
)
bsnEnteredForcedStackModeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnEnteredForcedStackModeAddress.setStatus("current")


class _BsnStackProtectionEvent_Type(Integer32):
    """Custom type bsnStackProtectionEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cannotJoinStack", 1),
          ("unitIgnored", 2))
    )


_BsnStackProtectionEvent_Type.__name__ = "Integer32"
_BsnStackProtectionEvent_Object = MibScalar
bsnStackProtectionEvent = _BsnStackProtectionEvent_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 17),
    _BsnStackProtectionEvent_Type()
)
bsnStackProtectionEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStackProtectionEvent.setStatus("current")


class _BsnUSBInfo_Type(DisplayString):
    """Custom type bsnUSBInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsnUSBInfo_Type.__name__ = "DisplayString"
_BsnUSBInfo_Object = MibScalar
bsnUSBInfo = _BsnUSBInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 18),
    _BsnUSBInfo_Type()
)
bsnUSBInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnUSBInfo.setStatus("current")


class _BsnSFPInfo_Type(DisplayString):
    """Custom type bsnSFPInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsnSFPInfo_Type.__name__ = "DisplayString"
_BsnSFPInfo_Object = MibScalar
bsnSFPInfo = _BsnSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 19),
    _BsnSFPInfo_Type()
)
bsnSFPInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSFPInfo.setStatus("current")


class _BsnAaaUserName_Type(SnmpAdminString):
    """Custom type bsnAaaUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 16),
    )


_BsnAaaUserName_Type.__name__ = "SnmpAdminString"
_BsnAaaUserName_Object = MibScalar
bsnAaaUserName = _BsnAaaUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 20),
    _BsnAaaUserName_Type()
)
bsnAaaUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAaaUserName.setStatus("current")
_BsnNotifications_ObjectIdentity = ObjectIdentity
bsnNotifications = _BsnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2)
)
_BsnNotifications0_ObjectIdentity = ObjectIdentity
bsnNotifications0 = _BsnNotifications0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

bsnConfigurationSavedToNvram = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    bsnConfigurationSavedToNvram.setStatus(
        "current"
    )

bsnEapAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 2)
)
bsnEapAccessViolation.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapAccessViolationMacAddress"))
)
if mibBuilder.loadTexts:
    bsnEapAccessViolation.setStatus(
        "current"
    )

bsnPortSpeedDuplexMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 3)
)
bsnPortSpeedDuplexMismatch.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnPortSpeedDuplexMismatch.setStatus(
        "current"
    )

bsnStackManagerReconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 4)
)
if mibBuilder.loadTexts:
    bsnStackManagerReconfiguration.setStatus(
        "current"
    )

bsnLacTrunkUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 5)
)
if mibBuilder.loadTexts:
    bsnLacTrunkUnavailable.setStatus(
        "current"
    )

bsnLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 6)
)
bsnLoginFailure.setObjects(
      *(("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureType"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureAddressType"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureAddress"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureUsername"))
)
if mibBuilder.loadTexts:
    bsnLoginFailure.setStatus(
        "current"
    )

bsnMLTHealthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 7)
)
bsnMLTHealthFailure.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    bsnMLTHealthFailure.setStatus(
        "current"
    )

bsnTrunkPortDisabledToPreventBroadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 8)
)
bsnTrunkPortDisabledToPreventBroadcastStorm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnTrunkPortDisabledToPreventBroadcastStorm.setStatus(
        "current"
    )

bsnLacPortDisabledToPreventBroadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 9)
)
bsnLacPortDisabledToPreventBroadcastStorm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnLacPortDisabledToPreventBroadcastStorm.setStatus(
        "current"
    )

bsnTrunkPortEnabledToPreventBroadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 10)
)
bsnTrunkPortEnabledToPreventBroadcastStorm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnTrunkPortEnabledToPreventBroadcastStorm.setStatus(
        "current"
    )

bsnLacPortDisabledDueToLossOfVLACPDU = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 11)
)
bsnLacPortDisabledDueToLossOfVLACPDU.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnLacPortDisabledDueToLossOfVLACPDU.setStatus(
        "current"
    )

bsnLacPortEnabledDueToReceiptOfVLACPDU = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 12)
)
bsnLacPortEnabledDueToReceiptOfVLACPDU.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnLacPortEnabledDueToReceiptOfVLACPDU.setStatus(
        "current"
    )

bsnStackConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 13)
)
bsnStackConfigurationError.setObjects(
      *(("BAY-STACK-MIB", "bayStackConfigExpectedStackSize"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnActualStackSize"))
)
if mibBuilder.loadTexts:
    bsnStackConfigurationError.setStatus(
        "current"
    )

bsnEapUbpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 14)
)
bsnEapUbpFailure.setObjects(
      *(("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureIfIndex"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureMacAddress"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureRoleString"))
)
if mibBuilder.loadTexts:
    bsnEapUbpFailure.setStatus(
        "current"
    )

bsnTrialLicenseExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 15)
)
bsnTrialLicenseExpiration.setObjects(
      *(("BAY-STACK-NOTIFICATIONS-MIB", "bsnTrialLicenseExpirationTime"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnTrialLicenseExpirationNumber"))
)
if mibBuilder.loadTexts:
    bsnTrialLicenseExpiration.setStatus(
        "current"
    )

bsnEnteredForcedStackMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 16)
)
bsnEnteredForcedStackMode.setObjects(
      *(("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeMAC"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeAddressType"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeAddress"))
)
if mibBuilder.loadTexts:
    bsnEnteredForcedStackMode.setStatus(
        "current"
    )

bsnTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 17)
)
bsnTemperatureExceeded.setObjects(
    ("S5-CHASSIS-MIB", "s5ChasComType")
)
if mibBuilder.loadTexts:
    bsnTemperatureExceeded.setStatus(
        "current"
    )

bsnEapRAVError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 18)
)
bsnEapRAVError.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapRAVErrorMacAddress"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapRAVErrorPort"))
)
if mibBuilder.loadTexts:
    bsnEapRAVError.setStatus(
        "current"
    )

bsnEapRateLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 19)
)
bsnEapRateLimitExceeded.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnEapRateLimitExceeded.setStatus(
        "current"
    )

bsnSystemUp365Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 20)
)
bsnSystemUp365Days.setObjects(
    ("BAY-STACK-MIB", "bayStackUnitConfigIndex")
)
if mibBuilder.loadTexts:
    bsnSystemUp365Days.setStatus(
        "current"
    )

bsnUSBInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 21)
)
bsnUSBInsertion.setObjects(
      *(("S5-AGENT-MIB", "s5AgSysUsbTargetUnit"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnUSBInfo"))
)
if mibBuilder.loadTexts:
    bsnUSBInsertion.setStatus(
        "current"
    )

bsnUSBRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 22)
)
bsnUSBRemoval.setObjects(
    ("S5-AGENT-MIB", "s5AgSysUsbTargetUnit")
)
if mibBuilder.loadTexts:
    bsnUSBRemoval.setStatus(
        "current"
    )

bsnSFPInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 23)
)
bsnSFPInsertion.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-NOTIFICATIONS-MIB", "bsnSFPInfo"))
)
if mibBuilder.loadTexts:
    bsnSFPInsertion.setStatus(
        "current"
    )

bsnSFPRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 24)
)
bsnSFPRemoval.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bsnSFPRemoval.setStatus(
        "current"
    )

bsnROPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 25)
)
if mibBuilder.loadTexts:
    bsnROPasswordExpired.setStatus(
        "current"
    )

bsnRWPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 26)
)
if mibBuilder.loadTexts:
    bsnRWPasswordExpired.setStatus(
        "current"
    )

bsnStackProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 27)
)
bsnStackProtection.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnStackProtectionEvent")
)
if mibBuilder.loadTexts:
    bsnStackProtection.setStatus(
        "current"
    )

bsnRunScripts = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 28)
)
bsnRunScripts.setObjects(
    ("S5-AGENT-MIB", "s5AgentScriptStatus")
)
if mibBuilder.loadTexts:
    bsnRunScripts.setStatus(
        "current"
    )

bsnAaaUserAccountNotUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 29)
)
bsnAaaUserAccountNotUsed.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName")
)
if mibBuilder.loadTexts:
    bsnAaaUserAccountNotUsed.setStatus(
        "current"
    )

bsnAaaAlreadyConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 30)
)
bsnAaaAlreadyConnected.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName")
)
if mibBuilder.loadTexts:
    bsnAaaAlreadyConnected.setStatus(
        "current"
    )

bsnAaaIncorrectLogOnThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 31)
)
bsnAaaIncorrectLogOnThresholdExceeded.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName")
)
if mibBuilder.loadTexts:
    bsnAaaIncorrectLogOnThresholdExceeded.setStatus(
        "current"
    )

bsnAaaMaxNoOfSessionsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 32)
)
bsnAaaMaxNoOfSessionsExceeded.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName")
)
if mibBuilder.loadTexts:
    bsnAaaMaxNoOfSessionsExceeded.setStatus(
        "current"
    )

bsnAuditUnsentMessages = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 33)
)
if mibBuilder.loadTexts:
    bsnAuditUnsentMessages.setStatus(
        "current"
    )

bsnAuditRecordEventsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 34)
)
if mibBuilder.loadTexts:
    bsnAuditRecordEventsFailure.setStatus(
        "current"
    )

bsnAuditStartUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 35)
)
if mibBuilder.loadTexts:
    bsnAuditStartUpTrap.setStatus(
        "current"
    )

bsnAuditShutDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 36)
)
if mibBuilder.loadTexts:
    bsnAuditShutDownTrap.setStatus(
        "current"
    )

bsnAaaUserPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 37)
)
bsnAaaUserPasswordExpired.setObjects(
    ("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName")
)
if mibBuilder.loadTexts:
    bsnAaaUserPasswordExpired.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-NOTIFICATIONS-MIB",
    **{"bayStackNotificationsMib": bayStackNotificationsMib,
       "bsnObjects": bsnObjects,
       "bsnEapAccessViolationMacAddress": bsnEapAccessViolationMacAddress,
       "bsnLoginFailureType": bsnLoginFailureType,
       "bsnLoginFailureAddressType": bsnLoginFailureAddressType,
       "bsnLoginFailureAddress": bsnLoginFailureAddress,
       "bsnLoginFailureUsername": bsnLoginFailureUsername,
       "bsnActualStackSize": bsnActualStackSize,
       "bsnEapUbpFailureIfIndex": bsnEapUbpFailureIfIndex,
       "bsnEapUbpFailureMacAddress": bsnEapUbpFailureMacAddress,
       "bsnEapUbpFailureRoleString": bsnEapUbpFailureRoleString,
       "bsnTrialLicenseExpirationTime": bsnTrialLicenseExpirationTime,
       "bsnTrialLicenseExpirationNumber": bsnTrialLicenseExpirationNumber,
       "bsnEnteredForcedStackModeMAC": bsnEnteredForcedStackModeMAC,
       "bsnEapRAVErrorMacAddress": bsnEapRAVErrorMacAddress,
       "bsnEapRAVErrorPort": bsnEapRAVErrorPort,
       "bsnEnteredForcedStackModeAddressType": bsnEnteredForcedStackModeAddressType,
       "bsnEnteredForcedStackModeAddress": bsnEnteredForcedStackModeAddress,
       "bsnStackProtectionEvent": bsnStackProtectionEvent,
       "bsnUSBInfo": bsnUSBInfo,
       "bsnSFPInfo": bsnSFPInfo,
       "bsnAaaUserName": bsnAaaUserName,
       "bsnNotifications": bsnNotifications,
       "bsnNotifications0": bsnNotifications0,
       "bsnConfigurationSavedToNvram": bsnConfigurationSavedToNvram,
       "bsnEapAccessViolation": bsnEapAccessViolation,
       "bsnPortSpeedDuplexMismatch": bsnPortSpeedDuplexMismatch,
       "bsnStackManagerReconfiguration": bsnStackManagerReconfiguration,
       "bsnLacTrunkUnavailable": bsnLacTrunkUnavailable,
       "bsnLoginFailure": bsnLoginFailure,
       "bsnMLTHealthFailure": bsnMLTHealthFailure,
       "bsnTrunkPortDisabledToPreventBroadcastStorm": bsnTrunkPortDisabledToPreventBroadcastStorm,
       "bsnLacPortDisabledToPreventBroadcastStorm": bsnLacPortDisabledToPreventBroadcastStorm,
       "bsnTrunkPortEnabledToPreventBroadcastStorm": bsnTrunkPortEnabledToPreventBroadcastStorm,
       "bsnLacPortDisabledDueToLossOfVLACPDU": bsnLacPortDisabledDueToLossOfVLACPDU,
       "bsnLacPortEnabledDueToReceiptOfVLACPDU": bsnLacPortEnabledDueToReceiptOfVLACPDU,
       "bsnStackConfigurationError": bsnStackConfigurationError,
       "bsnEapUbpFailure": bsnEapUbpFailure,
       "bsnTrialLicenseExpiration": bsnTrialLicenseExpiration,
       "bsnEnteredForcedStackMode": bsnEnteredForcedStackMode,
       "bsnTemperatureExceeded": bsnTemperatureExceeded,
       "bsnEapRAVError": bsnEapRAVError,
       "bsnEapRateLimitExceeded": bsnEapRateLimitExceeded,
       "bsnSystemUp365Days": bsnSystemUp365Days,
       "bsnUSBInsertion": bsnUSBInsertion,
       "bsnUSBRemoval": bsnUSBRemoval,
       "bsnSFPInsertion": bsnSFPInsertion,
       "bsnSFPRemoval": bsnSFPRemoval,
       "bsnROPasswordExpired": bsnROPasswordExpired,
       "bsnRWPasswordExpired": bsnRWPasswordExpired,
       "bsnStackProtection": bsnStackProtection,
       "bsnRunScripts": bsnRunScripts,
       "bsnAaaUserAccountNotUsed": bsnAaaUserAccountNotUsed,
       "bsnAaaAlreadyConnected": bsnAaaAlreadyConnected,
       "bsnAaaIncorrectLogOnThresholdExceeded": bsnAaaIncorrectLogOnThresholdExceeded,
       "bsnAaaMaxNoOfSessionsExceeded": bsnAaaMaxNoOfSessionsExceeded,
       "bsnAuditUnsentMessages": bsnAuditUnsentMessages,
       "bsnAuditRecordEventsFailure": bsnAuditRecordEventsFailure,
       "bsnAuditStartUpTrap": bsnAuditStartUpTrap,
       "bsnAuditShutDownTrap": bsnAuditShutDownTrap,
       "bsnAaaUserPasswordExpired": bsnAaaUserPasswordExpired}
)
