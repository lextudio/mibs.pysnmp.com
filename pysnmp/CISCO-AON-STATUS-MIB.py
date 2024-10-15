# SNMP MIB module (CISCO-AON-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AON-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:36 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,
 CiscoURLString) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "CiscoURLString")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoAonStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646)
)
ciscoAonStatusMIB.setRevisions(
        ("2008-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAonStatusMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAonStatusMIBNotifs = _CiscoAonStatusMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0)
)
_CiscoAonStatusMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAonStatusMIBObjects = _CiscoAonStatusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1)
)
_CaonSystemInfo_ObjectIdentity = ObjectIdentity
caonSystemInfo = _CaonSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1)
)


class _CaonNodeState_Type(Integer32):
    """Custom type caonNodeState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 4),
          ("registered", 2),
          ("unregistered", 1))
    )


_CaonNodeState_Type.__name__ = "Integer32"
_CaonNodeState_Object = MibScalar
caonNodeState = _CaonNodeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 1),
    _CaonNodeState_Type()
)
caonNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonNodeState.setStatus("current")
_CaonBootTime_Type = TimeStamp
_CaonBootTime_Object = MibScalar
caonBootTime = _CaonBootTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 2),
    _CaonBootTime_Type()
)
caonBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonBootTime.setStatus("current")
_CaonLastActivateTime_Type = DateAndTime
_CaonLastActivateTime_Object = MibScalar
caonLastActivateTime = _CaonLastActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 3),
    _CaonLastActivateTime_Type()
)
caonLastActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonLastActivateTime.setStatus("current")
_CaonReceivedMessages_Type = Counter32
_CaonReceivedMessages_Object = MibScalar
caonReceivedMessages = _CaonReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 4),
    _CaonReceivedMessages_Type()
)
caonReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonReceivedMessages.setStatus("current")
if mibBuilder.loadTexts:
    caonReceivedMessages.setUnits("messages")
_CaonAmcIpAddressType_Type = InetAddressType
_CaonAmcIpAddressType_Object = MibScalar
caonAmcIpAddressType = _CaonAmcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 5),
    _CaonAmcIpAddressType_Type()
)
caonAmcIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonAmcIpAddressType.setStatus("current")
_CaonAmcIpAddress_Type = InetAddress
_CaonAmcIpAddress_Object = MibScalar
caonAmcIpAddress = _CaonAmcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 6),
    _CaonAmcIpAddress_Type()
)
caonAmcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonAmcIpAddress.setStatus("current")
_CaonPepCount_Type = Gauge32
_CaonPepCount_Object = MibScalar
caonPepCount = _CaonPepCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 7),
    _CaonPepCount_Type()
)
caonPepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepCount.setStatus("current")
if mibBuilder.loadTexts:
    caonPepCount.setUnits("PEPs")
_CaonPepTable_Object = MibTable
caonPepTable = _CaonPepTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8)
)
if mibBuilder.loadTexts:
    caonPepTable.setStatus("current")
_CaonPepEntry_Object = MibTableRow
caonPepEntry = _CaonPepEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1)
)
caonPepEntry.setIndexNames(
    (0, "CISCO-AON-STATUS-MIB", "caonPepIndex"),
)
if mibBuilder.loadTexts:
    caonPepEntry.setStatus("current")


class _CaonPepIndex_Type(Unsigned32):
    """Custom type caonPepIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CaonPepIndex_Type.__name__ = "Unsigned32"
_CaonPepIndex_Object = MibTableColumn
caonPepIndex = _CaonPepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 1),
    _CaonPepIndex_Type()
)
caonPepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caonPepIndex.setStatus("current")


class _CaonPepName_Type(SnmpAdminString):
    """Custom type caonPepName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CaonPepName_Type.__name__ = "SnmpAdminString"
_CaonPepName_Object = MibTableColumn
caonPepName = _CaonPepName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 2),
    _CaonPepName_Type()
)
caonPepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepName.setStatus("current")


class _CaonPepStyle_Type(Integer32):
    """Custom type caonPepStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWay", 1),
          ("requestResponse", 2))
    )


_CaonPepStyle_Type.__name__ = "Integer32"
_CaonPepStyle_Object = MibTableColumn
caonPepStyle = _CaonPepStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 3),
    _CaonPepStyle_Type()
)
caonPepStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepStyle.setStatus("current")
_CaonPepReceivedMessages_Type = Counter32
_CaonPepReceivedMessages_Object = MibTableColumn
caonPepReceivedMessages = _CaonPepReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 4),
    _CaonPepReceivedMessages_Type()
)
caonPepReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepReceivedMessages.setStatus("current")
_CaonPepFailures_Type = Counter32
_CaonPepFailures_Object = MibTableColumn
caonPepFailures = _CaonPepFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 5),
    _CaonPepFailures_Type()
)
caonPepFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepFailures.setStatus("current")
_CaonPepSecurityFailures_Type = Counter32
_CaonPepSecurityFailures_Object = MibTableColumn
caonPepSecurityFailures = _CaonPepSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 8, 1, 6),
    _CaonPepSecurityFailures_Type()
)
caonPepSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepSecurityFailures.setStatus("current")
_CaonPepEndPointTable_Object = MibTable
caonPepEndPointTable = _CaonPepEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10)
)
if mibBuilder.loadTexts:
    caonPepEndPointTable.setStatus("current")
_CaonPepEndPointEntry_Object = MibTableRow
caonPepEndPointEntry = _CaonPepEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1)
)
caonPepEndPointEntry.setIndexNames(
    (0, "CISCO-AON-STATUS-MIB", "caonPepIndex"),
    (0, "CISCO-AON-STATUS-MIB", "caonPepEndPointIndex"),
)
if mibBuilder.loadTexts:
    caonPepEndPointEntry.setStatus("current")


class _CaonPepEndPointIndex_Type(Unsigned32):
    """Custom type caonPepEndPointIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CaonPepEndPointIndex_Type.__name__ = "Unsigned32"
_CaonPepEndPointIndex_Object = MibTableColumn
caonPepEndPointIndex = _CaonPepEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 1),
    _CaonPepEndPointIndex_Type()
)
caonPepEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caonPepEndPointIndex.setStatus("current")
_CaonPepEndPointUrl_Type = CiscoURLString
_CaonPepEndPointUrl_Object = MibTableColumn
caonPepEndPointUrl = _CaonPepEndPointUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 2),
    _CaonPepEndPointUrl_Type()
)
caonPepEndPointUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonPepEndPointUrl.setStatus("current")
_CaonEndPointAttemptedMessages_Type = Counter32
_CaonEndPointAttemptedMessages_Object = MibTableColumn
caonEndPointAttemptedMessages = _CaonEndPointAttemptedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 3),
    _CaonEndPointAttemptedMessages_Type()
)
caonEndPointAttemptedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonEndPointAttemptedMessages.setStatus("current")
_CaonOneWayDeliveredMessages_Type = Counter32
_CaonOneWayDeliveredMessages_Object = MibTableColumn
caonOneWayDeliveredMessages = _CaonOneWayDeliveredMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 4),
    _CaonOneWayDeliveredMessages_Type()
)
caonOneWayDeliveredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonOneWayDeliveredMessages.setStatus("current")
_CaonOneWayFailedMessages_Type = Counter32
_CaonOneWayFailedMessages_Object = MibTableColumn
caonOneWayFailedMessages = _CaonOneWayFailedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 5),
    _CaonOneWayFailedMessages_Type()
)
caonOneWayFailedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonOneWayFailedMessages.setStatus("current")
_CaonReqResponseDeliveredMessages_Type = Counter32
_CaonReqResponseDeliveredMessages_Object = MibTableColumn
caonReqResponseDeliveredMessages = _CaonReqResponseDeliveredMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 6),
    _CaonReqResponseDeliveredMessages_Type()
)
caonReqResponseDeliveredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonReqResponseDeliveredMessages.setStatus("current")
if mibBuilder.loadTexts:
    caonReqResponseDeliveredMessages.setUnits("messages")
_CaonReqResponseFailedMessages_Type = Counter32
_CaonReqResponseFailedMessages_Object = MibTableColumn
caonReqResponseFailedMessages = _CaonReqResponseFailedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 7),
    _CaonReqResponseFailedMessages_Type()
)
caonReqResponseFailedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonReqResponseFailedMessages.setStatus("current")
if mibBuilder.loadTexts:
    caonReqResponseFailedMessages.setUnits("messages")
_CaonEndPointMinResponseTime_Type = TimeTicks
_CaonEndPointMinResponseTime_Object = MibTableColumn
caonEndPointMinResponseTime = _CaonEndPointMinResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 8),
    _CaonEndPointMinResponseTime_Type()
)
caonEndPointMinResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonEndPointMinResponseTime.setStatus("current")
_CaonEndPointMaxResponseTime_Type = TimeTicks
_CaonEndPointMaxResponseTime_Object = MibTableColumn
caonEndPointMaxResponseTime = _CaonEndPointMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 9),
    _CaonEndPointMaxResponseTime_Type()
)
caonEndPointMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonEndPointMaxResponseTime.setStatus("current")
_CaonEndPointAvgResponseTime_Type = TimeTicks
_CaonEndPointAvgResponseTime_Object = MibTableColumn
caonEndPointAvgResponseTime = _CaonEndPointAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 10, 1, 10),
    _CaonEndPointAvgResponseTime_Type()
)
caonEndPointAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonEndPointAvgResponseTime.setStatus("current")
_CaonCounterDiscontinuityTime_Type = TimeStamp
_CaonCounterDiscontinuityTime_Object = MibScalar
caonCounterDiscontinuityTime = _CaonCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 1, 11),
    _CaonCounterDiscontinuityTime_Type()
)
caonCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caonCounterDiscontinuityTime.setStatus("current")
_CaonNotificationInfo_ObjectIdentity = ObjectIdentity
caonNotificationInfo = _CaonNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2)
)


class _CaonMessageSrcUri_Type(SnmpAdminString):
    """Custom type caonMessageSrcUri based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CaonMessageSrcUri_Type.__name__ = "SnmpAdminString"
_CaonMessageSrcUri_Object = MibScalar
caonMessageSrcUri = _CaonMessageSrcUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 1),
    _CaonMessageSrcUri_Type()
)
caonMessageSrcUri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonMessageSrcUri.setStatus("current")
_CaonMessageSrcIpAddressType_Type = InetAddressType
_CaonMessageSrcIpAddressType_Object = MibScalar
caonMessageSrcIpAddressType = _CaonMessageSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 2),
    _CaonMessageSrcIpAddressType_Type()
)
caonMessageSrcIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonMessageSrcIpAddressType.setStatus("current")
_CaonMessageSrcIpAddress_Type = InetAddress
_CaonMessageSrcIpAddress_Object = MibScalar
caonMessageSrcIpAddress = _CaonMessageSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 3),
    _CaonMessageSrcIpAddress_Type()
)
caonMessageSrcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonMessageSrcIpAddress.setStatus("current")
_CaonMessageSrcPort_Type = CiscoPort
_CaonMessageSrcPort_Object = MibScalar
caonMessageSrcPort = _CaonMessageSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 4),
    _CaonMessageSrcPort_Type()
)
caonMessageSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonMessageSrcPort.setStatus("current")


class _CaonNotificationName_Type(SnmpAdminString):
    """Custom type caonNotificationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaonNotificationName_Type.__name__ = "SnmpAdminString"
_CaonNotificationName_Object = MibScalar
caonNotificationName = _CaonNotificationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 5),
    _CaonNotificationName_Type()
)
caonNotificationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonNotificationName.setStatus("current")


class _CaonNotificationText_Type(SnmpAdminString):
    """Custom type caonNotificationText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CaonNotificationText_Type.__name__ = "SnmpAdminString"
_CaonNotificationText_Object = MibScalar
caonNotificationText = _CaonNotificationText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 6),
    _CaonNotificationText_Type()
)
caonNotificationText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonNotificationText.setStatus("current")
_CaonSendResponseThreshold_Type = TimeTicks
_CaonSendResponseThreshold_Object = MibScalar
caonSendResponseThreshold = _CaonSendResponseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 7),
    _CaonSendResponseThreshold_Type()
)
caonSendResponseThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caonSendResponseThreshold.setStatus("current")


class _CaonNotifEnableIndicators_Type(Bits):
    """Custom type caonNotifEnableIndicators based on Bits"""
    namedValues = NamedValues(
        *(("caonCustomNotifEnabled", 5),
          ("caonDownNotifEnabled", 1),
          ("caonMessageDeliveryFailedNotifEnabled", 3),
          ("caonNewPepDeployedNotifEnabled", 2),
          ("caonSendResponseThresholdExceededNotifEnabled", 4),
          ("caonUpNotifEnabled", 0))
    )

_CaonNotifEnableIndicators_Type.__name__ = "Bits"
_CaonNotifEnableIndicators_Object = MibScalar
caonNotifEnableIndicators = _CaonNotifEnableIndicators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 1, 2, 8),
    _CaonNotifEnableIndicators_Type()
)
caonNotifEnableIndicators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caonNotifEnableIndicators.setStatus("current")
_CiscoAonStatusMIBConform_ObjectIdentity = ObjectIdentity
ciscoAonStatusMIBConform = _CiscoAonStatusMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2)
)
_CiscoAonStatusMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAonStatusMIBCompliances = _CiscoAonStatusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 1)
)
_CiscoAonStatusMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAonStatusMIBGroups = _CiscoAonStatusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2)
)

# Managed Objects groups

caonNodeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 1)
)
caonNodeObjectGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonNodeState"),
        ("CISCO-AON-STATUS-MIB", "caonBootTime"),
        ("CISCO-AON-STATUS-MIB", "caonLastActivateTime"),
        ("CISCO-AON-STATUS-MIB", "caonReceivedMessages"),
        ("CISCO-AON-STATUS-MIB", "caonAmcIpAddressType"),
        ("CISCO-AON-STATUS-MIB", "caonAmcIpAddress"),
        ("CISCO-AON-STATUS-MIB", "caonPepCount"),
        ("CISCO-AON-STATUS-MIB", "caonCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    caonNodeObjectGroup.setStatus("current")

caonPepObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 2)
)
caonPepObjectGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonPepName"),
        ("CISCO-AON-STATUS-MIB", "caonPepStyle"),
        ("CISCO-AON-STATUS-MIB", "caonPepReceivedMessages"),
        ("CISCO-AON-STATUS-MIB", "caonPepFailures"),
        ("CISCO-AON-STATUS-MIB", "caonPepSecurityFailures"))
)
if mibBuilder.loadTexts:
    caonPepObjectGroup.setStatus("current")

caonPepEndPointObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 3)
)
caonPepEndPointObjectGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonPepEndPointUrl"),
        ("CISCO-AON-STATUS-MIB", "caonEndPointAttemptedMessages"),
        ("CISCO-AON-STATUS-MIB", "caonOneWayDeliveredMessages"),
        ("CISCO-AON-STATUS-MIB", "caonOneWayFailedMessages"),
        ("CISCO-AON-STATUS-MIB", "caonReqResponseDeliveredMessages"),
        ("CISCO-AON-STATUS-MIB", "caonReqResponseFailedMessages"),
        ("CISCO-AON-STATUS-MIB", "caonEndPointMinResponseTime"),
        ("CISCO-AON-STATUS-MIB", "caonEndPointMaxResponseTime"),
        ("CISCO-AON-STATUS-MIB", "caonEndPointAvgResponseTime"))
)
if mibBuilder.loadTexts:
    caonPepEndPointObjectGroup.setStatus("current")

caonNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 4)
)
caonNotificationObjectGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddressType"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddress"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcPort"),
        ("CISCO-AON-STATUS-MIB", "caonNotificationName"))
)
if mibBuilder.loadTexts:
    caonNotificationObjectGroup.setStatus("current")

caonCustomNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 11)
)
caonCustomNotifObjectsGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonNotificationName"),
        ("CISCO-AON-STATUS-MIB", "caonNotificationText"))
)
if mibBuilder.loadTexts:
    caonCustomNotifObjectsGroup.setStatus("current")

caonMessageDeliveryFailedNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 12)
)
caonMessageDeliveryFailedNotifObjectsGroup.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonMessageSrcUri"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddressType"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddress"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcPort"))
)
if mibBuilder.loadTexts:
    caonMessageDeliveryFailedNotifObjectsGroup.setStatus("current")

caonNotifEnableObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 13)
)
caonNotifEnableObjectsGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonNotifEnableIndicators")
)
if mibBuilder.loadTexts:
    caonNotifEnableObjectsGroup.setStatus("current")

caonSendThresholdExceededNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 14)
)
caonSendThresholdExceededNotifObjectsGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonSendResponseThreshold")
)
if mibBuilder.loadTexts:
    caonSendThresholdExceededNotifObjectsGroup.setStatus("current")


# Notification objects

caonUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 1)
)
if mibBuilder.loadTexts:
    caonUp.setStatus(
        "current"
    )

caonDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 2)
)
if mibBuilder.loadTexts:
    caonDown.setStatus(
        "current"
    )

caonNewPepDeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 3)
)
caonNewPepDeployed.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonPepName")
)
if mibBuilder.loadTexts:
    caonNewPepDeployed.setStatus(
        "current"
    )

caonMessageDeliveryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 4)
)
caonMessageDeliveryFailed.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonPepEndPointUrl"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcUri"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddressType"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcIpAddress"),
        ("CISCO-AON-STATUS-MIB", "caonMessageSrcPort"))
)
if mibBuilder.loadTexts:
    caonMessageDeliveryFailed.setStatus(
        "current"
    )

caonSendResponseThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 5)
)
caonSendResponseThresholdExceeded.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonPepEndPointUrl"),
        ("CISCO-AON-STATUS-MIB", "caonSendResponseThreshold"))
)
if mibBuilder.loadTexts:
    caonSendResponseThresholdExceeded.setStatus(
        "current"
    )

caonCustomNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 0, 6)
)
caonCustomNotification.setObjects(
      *(("CISCO-AON-STATUS-MIB", "caonNotificationName"),
        ("CISCO-AON-STATUS-MIB", "caonNotificationText"))
)
if mibBuilder.loadTexts:
    caonCustomNotification.setStatus(
        "current"
    )


# Notifications groups

caonUpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 5)
)
caonUpNotificationGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonUp")
)
if mibBuilder.loadTexts:
    caonUpNotificationGroup.setStatus(
        "current"
    )

caonDownNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 6)
)
caonDownNotificationGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonDown")
)
if mibBuilder.loadTexts:
    caonDownNotificationGroup.setStatus(
        "current"
    )

caonNewPepDeployedNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 7)
)
caonNewPepDeployedNotifGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonNewPepDeployed")
)
if mibBuilder.loadTexts:
    caonNewPepDeployedNotifGroup.setStatus(
        "current"
    )

caonSendThresholdExceededNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 8)
)
caonSendThresholdExceededNotifGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonSendResponseThresholdExceeded")
)
if mibBuilder.loadTexts:
    caonSendThresholdExceededNotifGroup.setStatus(
        "current"
    )

caonMessageDeliveryFailedNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 9)
)
caonMessageDeliveryFailedNotifGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonMessageDeliveryFailed")
)
if mibBuilder.loadTexts:
    caonMessageDeliveryFailedNotifGroup.setStatus(
        "current"
    )

caonCustomNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 2, 10)
)
caonCustomNotifGroup.setObjects(
    ("CISCO-AON-STATUS-MIB", "caonCustomNotification")
)
if mibBuilder.loadTexts:
    caonCustomNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAonStatusMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 646, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAonStatusMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AON-STATUS-MIB",
    **{"ciscoAonStatusMIB": ciscoAonStatusMIB,
       "ciscoAonStatusMIBNotifs": ciscoAonStatusMIBNotifs,
       "caonUp": caonUp,
       "caonDown": caonDown,
       "caonNewPepDeployed": caonNewPepDeployed,
       "caonMessageDeliveryFailed": caonMessageDeliveryFailed,
       "caonSendResponseThresholdExceeded": caonSendResponseThresholdExceeded,
       "caonCustomNotification": caonCustomNotification,
       "ciscoAonStatusMIBObjects": ciscoAonStatusMIBObjects,
       "caonSystemInfo": caonSystemInfo,
       "caonNodeState": caonNodeState,
       "caonBootTime": caonBootTime,
       "caonLastActivateTime": caonLastActivateTime,
       "caonReceivedMessages": caonReceivedMessages,
       "caonAmcIpAddressType": caonAmcIpAddressType,
       "caonAmcIpAddress": caonAmcIpAddress,
       "caonPepCount": caonPepCount,
       "caonPepTable": caonPepTable,
       "caonPepEntry": caonPepEntry,
       "caonPepIndex": caonPepIndex,
       "caonPepName": caonPepName,
       "caonPepStyle": caonPepStyle,
       "caonPepReceivedMessages": caonPepReceivedMessages,
       "caonPepFailures": caonPepFailures,
       "caonPepSecurityFailures": caonPepSecurityFailures,
       "caonPepEndPointTable": caonPepEndPointTable,
       "caonPepEndPointEntry": caonPepEndPointEntry,
       "caonPepEndPointIndex": caonPepEndPointIndex,
       "caonPepEndPointUrl": caonPepEndPointUrl,
       "caonEndPointAttemptedMessages": caonEndPointAttemptedMessages,
       "caonOneWayDeliveredMessages": caonOneWayDeliveredMessages,
       "caonOneWayFailedMessages": caonOneWayFailedMessages,
       "caonReqResponseDeliveredMessages": caonReqResponseDeliveredMessages,
       "caonReqResponseFailedMessages": caonReqResponseFailedMessages,
       "caonEndPointMinResponseTime": caonEndPointMinResponseTime,
       "caonEndPointMaxResponseTime": caonEndPointMaxResponseTime,
       "caonEndPointAvgResponseTime": caonEndPointAvgResponseTime,
       "caonCounterDiscontinuityTime": caonCounterDiscontinuityTime,
       "caonNotificationInfo": caonNotificationInfo,
       "caonMessageSrcUri": caonMessageSrcUri,
       "caonMessageSrcIpAddressType": caonMessageSrcIpAddressType,
       "caonMessageSrcIpAddress": caonMessageSrcIpAddress,
       "caonMessageSrcPort": caonMessageSrcPort,
       "caonNotificationName": caonNotificationName,
       "caonNotificationText": caonNotificationText,
       "caonSendResponseThreshold": caonSendResponseThreshold,
       "caonNotifEnableIndicators": caonNotifEnableIndicators,
       "ciscoAonStatusMIBConform": ciscoAonStatusMIBConform,
       "ciscoAonStatusMIBCompliances": ciscoAonStatusMIBCompliances,
       "ciscoAonStatusMIBCompliance": ciscoAonStatusMIBCompliance,
       "ciscoAonStatusMIBGroups": ciscoAonStatusMIBGroups,
       "caonNodeObjectGroup": caonNodeObjectGroup,
       "caonPepObjectGroup": caonPepObjectGroup,
       "caonPepEndPointObjectGroup": caonPepEndPointObjectGroup,
       "caonNotificationObjectGroup": caonNotificationObjectGroup,
       "caonUpNotificationGroup": caonUpNotificationGroup,
       "caonDownNotificationGroup": caonDownNotificationGroup,
       "caonNewPepDeployedNotifGroup": caonNewPepDeployedNotifGroup,
       "caonSendThresholdExceededNotifGroup": caonSendThresholdExceededNotifGroup,
       "caonMessageDeliveryFailedNotifGroup": caonMessageDeliveryFailedNotifGroup,
       "caonCustomNotifGroup": caonCustomNotifGroup,
       "caonCustomNotifObjectsGroup": caonCustomNotifObjectsGroup,
       "caonMessageDeliveryFailedNotifObjectsGroup": caonMessageDeliveryFailedNotifObjectsGroup,
       "caonNotifEnableObjectsGroup": caonNotifEnableObjectsGroup,
       "caonSendThresholdExceededNotifObjectsGroup": caonSendThresholdExceededNotifObjectsGroup}
)
