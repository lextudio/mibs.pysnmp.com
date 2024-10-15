# SNMP MIB module (TPT-SMS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-SMS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:10 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tpt_reg,) = mibBuilder.importSymbols(
    "TIPPINGPOINT-REG-MIB",
    "tpt-reg")

(tpt_sms_eventsV2,
 tpt_sms_groups,
 tpt_sms_notifypayload,
 tpt_smsMIBs) = mibBuilder.importSymbols(
    "TPT-SMSMIBS",
    "tpt-sms-eventsV2",
    "tpt-sms-groups",
    "tpt-sms-notifypayload",
    "tpt-smsMIBs")


# MODULE-IDENTITY

tptSmsTrapsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TptSmsQuarantineNotifyId_Type(Integer32):
    """Custom type tptSmsQuarantineNotifyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TptSmsQuarantineNotifyId_Type.__name__ = "Integer32"
_TptSmsQuarantineNotifyId_Object = MibScalar
tptSmsQuarantineNotifyId = _TptSmsQuarantineNotifyId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 1),
    _TptSmsQuarantineNotifyId_Type()
)
tptSmsQuarantineNotifyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyId.setStatus("current")
_TptSmsQuarantineNotifyData_Type = OctetString
_TptSmsQuarantineNotifyData_Object = MibScalar
tptSmsQuarantineNotifyData = _TptSmsQuarantineNotifyData_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 2),
    _TptSmsQuarantineNotifyData_Type()
)
tptSmsQuarantineNotifyData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyData.setStatus("current")
_TptSmsQuarantinePolicyMatchData_Type = OctetString
_TptSmsQuarantinePolicyMatchData_Object = MibScalar
tptSmsQuarantinePolicyMatchData = _TptSmsQuarantinePolicyMatchData_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 3),
    _TptSmsQuarantinePolicyMatchData_Type()
)
tptSmsQuarantinePolicyMatchData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantinePolicyMatchData.setStatus("current")
_TptSmsQuarantineNotifyType_Type = OctetString
_TptSmsQuarantineNotifyType_Object = MibScalar
tptSmsQuarantineNotifyType = _TptSmsQuarantineNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 4),
    _TptSmsQuarantineNotifyType_Type()
)
tptSmsQuarantineNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyType.setStatus("current")
_TptSmsQuarantineDeviceIP_Type = IpAddress
_TptSmsQuarantineDeviceIP_Object = MibScalar
tptSmsQuarantineDeviceIP = _TptSmsQuarantineDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 5),
    _TptSmsQuarantineDeviceIP_Type()
)
tptSmsQuarantineDeviceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineDeviceIP.setStatus("current")
_TptSmsQuarantineDeviceMAC_Type = OctetString
_TptSmsQuarantineDeviceMAC_Object = MibScalar
tptSmsQuarantineDeviceMAC = _TptSmsQuarantineDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 6),
    _TptSmsQuarantineDeviceMAC_Type()
)
tptSmsQuarantineDeviceMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineDeviceMAC.setStatus("current")
_TptSmsQuarantineSwitchPort_Type = OctetString
_TptSmsQuarantineSwitchPort_Object = MibScalar
tptSmsQuarantineSwitchPort = _TptSmsQuarantineSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 7),
    _TptSmsQuarantineSwitchPort_Type()
)
tptSmsQuarantineSwitchPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineSwitchPort.setStatus("current")
_TptSmsQuarantineEndpointUser_Type = OctetString
_TptSmsQuarantineEndpointUser_Object = MibScalar
tptSmsQuarantineEndpointUser = _TptSmsQuarantineEndpointUser_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 8),
    _TptSmsQuarantineEndpointUser_Type()
)
tptSmsQuarantineEndpointUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineEndpointUser.setStatus("current")
_TptSmsQuarantineNotifyActionList_Type = OctetString
_TptSmsQuarantineNotifyActionList_Object = MibScalar
tptSmsQuarantineNotifyActionList = _TptSmsQuarantineNotifyActionList_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 9),
    _TptSmsQuarantineNotifyActionList_Type()
)
tptSmsQuarantineNotifyActionList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyActionList.setStatus("current")
_TptSmsQuarantineNotifyParamList_Type = OctetString
_TptSmsQuarantineNotifyParamList_Object = MibScalar
tptSmsQuarantineNotifyParamList = _TptSmsQuarantineNotifyParamList_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 10),
    _TptSmsQuarantineNotifyParamList_Type()
)
tptSmsQuarantineNotifyParamList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyParamList.setStatus("current")
_TptSmsQuarantineNotifyOptionList_Type = OctetString
_TptSmsQuarantineNotifyOptionList_Object = MibScalar
tptSmsQuarantineNotifyOptionList = _TptSmsQuarantineNotifyOptionList_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 11),
    _TptSmsQuarantineNotifyOptionList_Type()
)
tptSmsQuarantineNotifyOptionList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyOptionList.setStatus("current")
_TptSmsQuarantinePolicyName_Type = OctetString
_TptSmsQuarantinePolicyName_Object = MibScalar
tptSmsQuarantinePolicyName = _TptSmsQuarantinePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 12),
    _TptSmsQuarantinePolicyName_Type()
)
tptSmsQuarantinePolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsQuarantinePolicyName.setStatus("current")
_TptSmsRepDvVersion_Type = OctetString
_TptSmsRepDvVersion_Object = MibScalar
tptSmsRepDvVersion = _TptSmsRepDvVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 13),
    _TptSmsRepDvVersion_Type()
)
tptSmsRepDvVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsRepDvVersion.setStatus("current")
_TptSmsMessage_Type = OctetString
_TptSmsMessage_Object = MibScalar
tptSmsMessage = _TptSmsMessage_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 14),
    _TptSmsMessage_Type()
)
tptSmsMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptSmsMessage.setStatus("current")

# Managed Objects groups

tptSmsQuarantineDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 1)
)
tptSmsQuarantineDataGroup.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyMatchData"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineDataGroup.setStatus("current")


# Notification objects

tptSmsQuarantineRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 1)
)
tptSmsQuarantineRequest.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineRequest.setStatus(
        "current"
    )

tptSmsQuarantineAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 2)
)
tptSmsQuarantineAck.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineAck.setStatus(
        "current"
    )

tptSmsQuarantineReleaseRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 3)
)
tptSmsQuarantineReleaseRequest.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineReleaseRequest.setStatus(
        "current"
    )

tptSmsQuarantineReleaseAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 4)
)
tptSmsQuarantineReleaseAck.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineReleaseAck.setStatus(
        "current"
    )

tptSmsQuarantinePolicyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 5)
)
tptSmsQuarantinePolicyNotification.setObjects(
    ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyMatchData")
)
if mibBuilder.loadTexts:
    tptSmsQuarantinePolicyNotification.setStatus(
        "current"
    )

tptSmsUnQuarantineRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 6)
)
tptSmsUnQuarantineRequest.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceIP"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceMAC"))
)
if mibBuilder.loadTexts:
    tptSmsUnQuarantineRequest.setStatus(
        "current"
    )

tptSmsBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 7)
)
if mibBuilder.loadTexts:
    tptSmsBoot.setStatus(
        "current"
    )

tptSmsReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 8)
)
if mibBuilder.loadTexts:
    tptSmsReboot.setStatus(
        "current"
    )

tptSmsShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 9)
)
if mibBuilder.loadTexts:
    tptSmsShuttingDown.setStatus(
        "current"
    )

tptSmsReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 10)
)
if mibBuilder.loadTexts:
    tptSmsReady.setStatus(
        "current"
    )

tptSmsAuthenticationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 11)
)
if mibBuilder.loadTexts:
    tptSmsAuthenticationError.setStatus(
        "current"
    )

tptSmsEgpNeighborDownstate = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 12)
)
if mibBuilder.loadTexts:
    tptSmsEgpNeighborDownstate.setStatus(
        "current"
    )

tptSmsSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 13)
)
if mibBuilder.loadTexts:
    tptSmsSystemRestart.setStatus(
        "current"
    )

tptSmsQuarantineCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 14)
)
tptSmsQuarantineCommand.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceIP"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyName"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineCommand.setStatus(
        "current"
    )

tptSmsRepDvVerifySuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 15)
)
tptSmsRepDvVerifySuccess.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsRepDvVersion"),
        ("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
)
if mibBuilder.loadTexts:
    tptSmsRepDvVerifySuccess.setStatus(
        "current"
    )

tptSmsRepDvVerifyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 16)
)
tptSmsRepDvVerifyFail.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsRepDvVersion"),
        ("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
)
if mibBuilder.loadTexts:
    tptSmsRepDvVerifyFail.setStatus(
        "current"
    )

tptSmsTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 17)
)
tptSmsTest.setObjects(
    ("TPT-SMS-TRAP-MIB", "tptSmsMessage")
)
if mibBuilder.loadTexts:
    tptSmsTest.setStatus(
        "current"
    )

tptSmsRebootingDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 18)
)
tptSmsRebootingDevice.setObjects(
    ("TPT-SMS-TRAP-MIB", "tptSmsMessage")
)
if mibBuilder.loadTexts:
    tptSmsRebootingDevice.setStatus(
        "current"
    )

tptDeviceNonComm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 19)
)
tptDeviceNonComm.setObjects(
    ("TPT-SMS-TRAP-MIB", "tptSmsMessage")
)
if mibBuilder.loadTexts:
    tptDeviceNonComm.setStatus(
        "current"
    )

tptDeviceBooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 20)
)
tptDeviceBooted.setObjects(
    ("TPT-SMS-TRAP-MIB", "tptSmsMessage")
)
if mibBuilder.loadTexts:
    tptDeviceBooted.setStatus(
        "current"
    )


# Notifications groups

tptSmsQuarantineNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 2)
)
tptSmsQuarantineNotifyGroup.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineRequest"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineReleaseRequest"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyNotification"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyGroup.setStatus(
        "current"
    )

tptSmsQuarantineNotifyAckGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 3)
)
tptSmsQuarantineNotifyAckGroup.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineAck"),
        ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineReleaseAck"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineNotifyAckGroup.setStatus(
        "current"
    )

tptSmsQuarantineRequestGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 4)
)
tptSmsQuarantineRequestGroup.setObjects(
      *(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineCommand"),
        ("TPT-SMS-TRAP-MIB", "tptSmsUnQuarantineRequest"))
)
if mibBuilder.loadTexts:
    tptSmsQuarantineRequestGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-SMS-TRAP-MIB",
    **{"tptSmsQuarantineDataGroup": tptSmsQuarantineDataGroup,
       "tptSmsQuarantineNotifyGroup": tptSmsQuarantineNotifyGroup,
       "tptSmsQuarantineNotifyAckGroup": tptSmsQuarantineNotifyAckGroup,
       "tptSmsQuarantineRequestGroup": tptSmsQuarantineRequestGroup,
       "tptSmsQuarantineRequest": tptSmsQuarantineRequest,
       "tptSmsQuarantineAck": tptSmsQuarantineAck,
       "tptSmsQuarantineReleaseRequest": tptSmsQuarantineReleaseRequest,
       "tptSmsQuarantineReleaseAck": tptSmsQuarantineReleaseAck,
       "tptSmsQuarantinePolicyNotification": tptSmsQuarantinePolicyNotification,
       "tptSmsUnQuarantineRequest": tptSmsUnQuarantineRequest,
       "tptSmsBoot": tptSmsBoot,
       "tptSmsReboot": tptSmsReboot,
       "tptSmsShuttingDown": tptSmsShuttingDown,
       "tptSmsReady": tptSmsReady,
       "tptSmsAuthenticationError": tptSmsAuthenticationError,
       "tptSmsEgpNeighborDownstate": tptSmsEgpNeighborDownstate,
       "tptSmsSystemRestart": tptSmsSystemRestart,
       "tptSmsQuarantineCommand": tptSmsQuarantineCommand,
       "tptSmsRepDvVerifySuccess": tptSmsRepDvVerifySuccess,
       "tptSmsRepDvVerifyFail": tptSmsRepDvVerifyFail,
       "tptSmsTest": tptSmsTest,
       "tptSmsRebootingDevice": tptSmsRebootingDevice,
       "tptDeviceNonComm": tptDeviceNonComm,
       "tptDeviceBooted": tptDeviceBooted,
       "tptSmsQuarantineNotifyId": tptSmsQuarantineNotifyId,
       "tptSmsQuarantineNotifyData": tptSmsQuarantineNotifyData,
       "tptSmsQuarantinePolicyMatchData": tptSmsQuarantinePolicyMatchData,
       "tptSmsQuarantineNotifyType": tptSmsQuarantineNotifyType,
       "tptSmsQuarantineDeviceIP": tptSmsQuarantineDeviceIP,
       "tptSmsQuarantineDeviceMAC": tptSmsQuarantineDeviceMAC,
       "tptSmsQuarantineSwitchPort": tptSmsQuarantineSwitchPort,
       "tptSmsQuarantineEndpointUser": tptSmsQuarantineEndpointUser,
       "tptSmsQuarantineNotifyActionList": tptSmsQuarantineNotifyActionList,
       "tptSmsQuarantineNotifyParamList": tptSmsQuarantineNotifyParamList,
       "tptSmsQuarantineNotifyOptionList": tptSmsQuarantineNotifyOptionList,
       "tptSmsQuarantinePolicyName": tptSmsQuarantinePolicyName,
       "tptSmsRepDvVersion": tptSmsRepDvVersion,
       "tptSmsMessage": tptSmsMessage,
       "tptSmsTrapsModule": tptSmsTrapsModule}
)
