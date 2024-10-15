# SNMP MIB module (AP-DIAMETER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP-DIAMETER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:03 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApDiamResultCode,
 ApTransportType) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApDiamResultCode",
    "ApTransportType")

(SysMgmtPercentage,) = mibBuilder.importSymbols(
    "APSYSMGMT-MIB",
    "SysMgmtPercentage")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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


# MODULE-IDENTITY

apDiameterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApDiamMIBModule_ObjectIdentity = ObjectIdentity
apDiamMIBModule = _ApDiamMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1)
)
_ApDiamMIBObjects_ObjectIdentity = ObjectIdentity
apDiamMIBObjects = _ApDiamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1)
)
_ApDiamiMIBTabularObjects_ObjectIdentity = ObjectIdentity
apDiamiMIBTabularObjects = _ApDiamiMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2)
)
_ApDiamClfErrorStatsTable_Object = MibTable
apDiamClfErrorStatsTable = _ApDiamClfErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apDiamClfErrorStatsTable.setStatus("current")
_ApDiamClfErrorStatsEntry_Object = MibTableRow
apDiamClfErrorStatsEntry = _ApDiamClfErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1)
)
apDiamClfErrorStatsEntry.setIndexNames(
    (0, "AP-DIAMETER-MIB", "apDiamClfExtPolSvrIndex"),
)
if mibBuilder.loadTexts:
    apDiamClfErrorStatsEntry.setStatus("current")


class _ApDiamClfExtPolSvrIndex_Type(Integer32):
    """Custom type apDiamClfExtPolSvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDiamClfExtPolSvrIndex_Type.__name__ = "Integer32"
_ApDiamClfExtPolSvrIndex_Object = MibTableColumn
apDiamClfExtPolSvrIndex = _ApDiamClfExtPolSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 1),
    _ApDiamClfExtPolSvrIndex_Type()
)
apDiamClfExtPolSvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apDiamClfExtPolSvrIndex.setStatus("current")


class _ApDiamClfExtPolSvrName_Type(DisplayString):
    """Custom type apDiamClfExtPolSvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDiamClfExtPolSvrName_Type.__name__ = "DisplayString"
_ApDiamClfExtPolSvrName_Object = MibTableColumn
apDiamClfExtPolSvrName = _ApDiamClfExtPolSvrName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 2),
    _ApDiamClfExtPolSvrName_Type()
)
apDiamClfExtPolSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamClfExtPolSvrName.setStatus("current")
_ApDiamClfErrorsRecent_Type = Gauge32
_ApDiamClfErrorsRecent_Object = MibTableColumn
apDiamClfErrorsRecent = _ApDiamClfErrorsRecent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 3),
    _ApDiamClfErrorsRecent_Type()
)
apDiamClfErrorsRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamClfErrorsRecent.setStatus("current")
_ApDiamClfErrorsTotal_Type = Counter32
_ApDiamClfErrorsTotal_Object = MibTableColumn
apDiamClfErrorsTotal = _ApDiamClfErrorsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 4),
    _ApDiamClfErrorsTotal_Type()
)
apDiamClfErrorsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamClfErrorsTotal.setStatus("current")
_ApDiamClfErrorsPerMax_Type = Counter32
_ApDiamClfErrorsPerMax_Object = MibTableColumn
apDiamClfErrorsPerMax = _ApDiamClfErrorsPerMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 5),
    _ApDiamClfErrorsPerMax_Type()
)
apDiamClfErrorsPerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamClfErrorsPerMax.setStatus("current")
_ApDiamInterfaceStatsTable_Object = MibTable
apDiamInterfaceStatsTable = _ApDiamInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apDiamInterfaceStatsTable.setStatus("current")
_ApDiamInterfaceStatsEntry_Object = MibTableRow
apDiamInterfaceStatsEntry = _ApDiamInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1)
)
apDiamInterfaceStatsEntry.setIndexNames(
    (0, "AP-DIAMETER-MIB", "apDiamInterfaceType"),
    (0, "AP-DIAMETER-MIB", "apDiamInterfaceAddress"),
)
if mibBuilder.loadTexts:
    apDiamInterfaceStatsEntry.setStatus("current")
_ApDiamInterfaceType_Type = InetAddressType
_ApDiamInterfaceType_Object = MibTableColumn
apDiamInterfaceType = _ApDiamInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 1),
    _ApDiamInterfaceType_Type()
)
apDiamInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamInterfaceType.setStatus("current")
_ApDiamInterfaceAddress_Type = InetAddress
_ApDiamInterfaceAddress_Object = MibTableColumn
apDiamInterfaceAddress = _ApDiamInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 2),
    _ApDiamInterfaceAddress_Type()
)
apDiamInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamInterfaceAddress.setStatus("current")
_ApDiamMessagesSent_Type = Unsigned32
_ApDiamMessagesSent_Object = MibTableColumn
apDiamMessagesSent = _ApDiamMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 3),
    _ApDiamMessagesSent_Type()
)
apDiamMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamMessagesSent.setStatus("current")
_ApDiamMessagesSentFailed_Type = Unsigned32
_ApDiamMessagesSentFailed_Object = MibTableColumn
apDiamMessagesSentFailed = _ApDiamMessagesSentFailed_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 4),
    _ApDiamMessagesSentFailed_Type()
)
apDiamMessagesSentFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamMessagesSentFailed.setStatus("current")
_ApDiamMessagesReSent_Type = Unsigned32
_ApDiamMessagesReSent_Object = MibTableColumn
apDiamMessagesReSent = _ApDiamMessagesReSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 5),
    _ApDiamMessagesReSent_Type()
)
apDiamMessagesReSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamMessagesReSent.setStatus("current")
_ApDiamMessagesReceived_Type = Unsigned32
_ApDiamMessagesReceived_Object = MibTableColumn
apDiamMessagesReceived = _ApDiamMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 6),
    _ApDiamMessagesReceived_Type()
)
apDiamMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamMessagesReceived.setStatus("current")
_ApDiamMessagesProcessed_Type = Unsigned32
_ApDiamMessagesProcessed_Object = MibTableColumn
apDiamMessagesProcessed = _ApDiamMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 7),
    _ApDiamMessagesProcessed_Type()
)
apDiamMessagesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamMessagesProcessed.setStatus("current")
_ApDiamConnectionTimeouts_Type = Unsigned32
_ApDiamConnectionTimeouts_Object = MibTableColumn
apDiamConnectionTimeouts = _ApDiamConnectionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 8),
    _ApDiamConnectionTimeouts_Type()
)
apDiamConnectionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamConnectionTimeouts.setStatus("current")
_ApDiamBadStateDrops_Type = Unsigned32
_ApDiamBadStateDrops_Object = MibTableColumn
apDiamBadStateDrops = _ApDiamBadStateDrops_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 9),
    _ApDiamBadStateDrops_Type()
)
apDiamBadStateDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamBadStateDrops.setStatus("current")
_ApDiamBadTypeDrops_Type = Unsigned32
_ApDiamBadTypeDrops_Object = MibTableColumn
apDiamBadTypeDrops = _ApDiamBadTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 10),
    _ApDiamBadTypeDrops_Type()
)
apDiamBadTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamBadTypeDrops.setStatus("current")
_ApDiamBadIDDrops_Type = Unsigned32
_ApDiamBadIDDrops_Object = MibTableColumn
apDiamBadIDDrops = _ApDiamBadIDDrops_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 11),
    _ApDiamBadIDDrops_Type()
)
apDiamBadIDDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamBadIDDrops.setStatus("current")
_ApDiamAuthFailDrops_Type = Unsigned32
_ApDiamAuthFailDrops_Object = MibTableColumn
apDiamAuthFailDrops = _ApDiamAuthFailDrops_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 12),
    _ApDiamAuthFailDrops_Type()
)
apDiamAuthFailDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamAuthFailDrops.setStatus("current")
_ApDiamInvalidPeerMessages_Type = Unsigned32
_ApDiamInvalidPeerMessages_Object = MibTableColumn
apDiamInvalidPeerMessages = _ApDiamInvalidPeerMessages_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 13),
    _ApDiamInvalidPeerMessages_Type()
)
apDiamInvalidPeerMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiamInvalidPeerMessages.setStatus("current")
_ApDiamNotificationObjects_ObjectIdentity = ObjectIdentity
apDiamNotificationObjects = _ApDiamNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2)
)
_ApDiamNotifObjects_ObjectIdentity = ObjectIdentity
apDiamNotifObjects = _ApDiamNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1)
)


class _ApDiamAcctSrvrHostName_Type(DisplayString):
    """Custom type apDiamAcctSrvrHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDiamAcctSrvrHostName_Type.__name__ = "DisplayString"
_ApDiamAcctSrvrHostName_Object = MibScalar
apDiamAcctSrvrHostName = _ApDiamAcctSrvrHostName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 1),
    _ApDiamAcctSrvrHostName_Type()
)
apDiamAcctSrvrHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiamAcctSrvrHostName.setStatus("current")


class _ApDiamAcctSrvrIPPort_Type(DisplayString):
    """Custom type apDiamAcctSrvrIPPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDiamAcctSrvrIPPort_Type.__name__ = "DisplayString"
_ApDiamAcctSrvrIPPort_Object = MibScalar
apDiamAcctSrvrIPPort = _ApDiamAcctSrvrIPPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 2),
    _ApDiamAcctSrvrIPPort_Type()
)
apDiamAcctSrvrIPPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiamAcctSrvrIPPort.setStatus("current")


class _ApDiamAcctSrvrOriginRealm_Type(DisplayString):
    """Custom type apDiamAcctSrvrOriginRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDiamAcctSrvrOriginRealm_Type.__name__ = "DisplayString"
_ApDiamAcctSrvrOriginRealm_Object = MibScalar
apDiamAcctSrvrOriginRealm = _ApDiamAcctSrvrOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 3),
    _ApDiamAcctSrvrOriginRealm_Type()
)
apDiamAcctSrvrOriginRealm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiamAcctSrvrOriginRealm.setStatus("current")


class _ApDiamAcctSrvrOriginHost_Type(DisplayString):
    """Custom type apDiamAcctSrvrOriginHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApDiamAcctSrvrOriginHost_Type.__name__ = "DisplayString"
_ApDiamAcctSrvrOriginHost_Object = MibScalar
apDiamAcctSrvrOriginHost = _ApDiamAcctSrvrOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 4),
    _ApDiamAcctSrvrOriginHost_Type()
)
apDiamAcctSrvrOriginHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiamAcctSrvrOriginHost.setStatus("current")
_ApDiamAcctSrvrTransportType_Type = ApTransportType
_ApDiamAcctSrvrTransportType_Object = MibScalar
apDiamAcctSrvrTransportType = _ApDiamAcctSrvrTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 5),
    _ApDiamAcctSrvrTransportType_Type()
)
apDiamAcctSrvrTransportType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiamAcctSrvrTransportType.setStatus("current")
_ApAcctMsgQueueAvailCurrent_Type = SysMgmtPercentage
_ApAcctMsgQueueAvailCurrent_Object = MibScalar
apAcctMsgQueueAvailCurrent = _ApAcctMsgQueueAvailCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 6),
    _ApAcctMsgQueueAvailCurrent_Type()
)
apAcctMsgQueueAvailCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apAcctMsgQueueAvailCurrent.setStatus("current")
_ApAcctMsgQueueMinorThreshold_Type = SysMgmtPercentage
_ApAcctMsgQueueMinorThreshold_Object = MibScalar
apAcctMsgQueueMinorThreshold = _ApAcctMsgQueueMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 7),
    _ApAcctMsgQueueMinorThreshold_Type()
)
apAcctMsgQueueMinorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apAcctMsgQueueMinorThreshold.setStatus("current")
_ApAcctMsgQueueMajorThreshold_Type = SysMgmtPercentage
_ApAcctMsgQueueMajorThreshold_Object = MibScalar
apAcctMsgQueueMajorThreshold = _ApAcctMsgQueueMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 8),
    _ApAcctMsgQueueMajorThreshold_Type()
)
apAcctMsgQueueMajorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apAcctMsgQueueMajorThreshold.setStatus("current")
_ApAcctMsgQueueCriticalThreshold_Type = SysMgmtPercentage
_ApAcctMsgQueueCriticalThreshold_Object = MibScalar
apAcctMsgQueueCriticalThreshold = _ApAcctMsgQueueCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 9),
    _ApAcctMsgQueueCriticalThreshold_Type()
)
apAcctMsgQueueCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apAcctMsgQueueCriticalThreshold.setStatus("current")
_ApDiameterResultCode_Type = ApDiamResultCode
_ApDiameterResultCode_Object = MibScalar
apDiameterResultCode = _ApDiameterResultCode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 10),
    _ApDiameterResultCode_Type()
)
apDiameterResultCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDiameterResultCode.setStatus("current")
_ApDiamNotifPrefix_ObjectIdentity = ObjectIdentity
apDiamNotifPrefix = _ApDiamNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2)
)
_ApDiamNotifications_ObjectIdentity = ObjectIdentity
apDiamNotifications = _ApDiamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0)
)
_ApDiamConformance_ObjectIdentity = ObjectIdentity
apDiamConformance = _ApDiamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3)
)
_ApDiamObjectGroups_ObjectIdentity = ObjectIdentity
apDiamObjectGroups = _ApDiamObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1)
)
_ApDiamNotificationGroups_ObjectIdentity = ObjectIdentity
apDiamNotificationGroups = _ApDiamNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2)
)

# Managed Objects groups

apDiamClfErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 1)
)
apDiamClfErrorStatsGroup.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamClfExtPolSvrName"),
        ("AP-DIAMETER-MIB", "apDiamClfErrorsRecent"),
        ("AP-DIAMETER-MIB", "apDiamClfErrorsTotal"),
        ("AP-DIAMETER-MIB", "apDiamClfErrorsPerMax"))
)
if mibBuilder.loadTexts:
    apDiamClfErrorStatsGroup.setStatus("current")

apDiamInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2)
)
apDiamInterfaceStatsGroup.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamMessagesSent"),
        ("AP-DIAMETER-MIB", "apDiamMessagesSentFailed"),
        ("AP-DIAMETER-MIB", "apDiamMessagesReSent"),
        ("AP-DIAMETER-MIB", "apDiamMessagesReceived"),
        ("AP-DIAMETER-MIB", "apDiamMessagesProcessed"),
        ("AP-DIAMETER-MIB", "apDiamConnectionTimeouts"),
        ("AP-DIAMETER-MIB", "apDiamBadStateDrops"),
        ("AP-DIAMETER-MIB", "apDiamBadTypeDrops"),
        ("AP-DIAMETER-MIB", "apDiamBadIDDrops"),
        ("AP-DIAMETER-MIB", "apDiamAuthFailDrops"),
        ("AP-DIAMETER-MIB", "apDiamInvalidPeerMessages"))
)
if mibBuilder.loadTexts:
    apDiamInterfaceStatsGroup.setStatus("current")

apDiamACCTObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 1)
)
apDiamACCTObjectsGroup.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
)
if mibBuilder.loadTexts:
    apDiamACCTObjectsGroup.setStatus("current")

apDiamACCTResultObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 3)
)
apDiamACCTResultObjectsGroup.setObjects(
    ("AP-DIAMETER-MIB", "apDiameterResultCode")
)
if mibBuilder.loadTexts:
    apDiamACCTResultObjectsGroup.setStatus("current")


# Notification objects

apDiameterAcctSrvrUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 1)
)
apDiameterAcctSrvrUpTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
)
if mibBuilder.loadTexts:
    apDiameterAcctSrvrUpTrap.setStatus(
        "current"
    )

apDiameterAcctSrvrDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 2)
)
apDiameterAcctSrvrDownTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
)
if mibBuilder.loadTexts:
    apDiameterAcctSrvrDownTrap.setStatus(
        "current"
    )

apAcctMsgQueueFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 3)
)
apAcctMsgQueueFullTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apAcctMsgQueueAvailCurrent"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueMinorThreshold"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueMajorThreshold"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueCriticalThreshold"))
)
if mibBuilder.loadTexts:
    apAcctMsgQueueFullTrap.setStatus(
        "current"
    )

apAcctMsgQueueFullClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 4)
)
apAcctMsgQueueFullClearTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apAcctMsgQueueAvailCurrent"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueMinorThreshold"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueMajorThreshold"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueCriticalThreshold"))
)
if mibBuilder.loadTexts:
    apAcctMsgQueueFullClearTrap.setStatus(
        "current"
    )

apDiameterSrvrErrorResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 5)
)
apDiameterSrvrErrorResultTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"),
        ("AP-DIAMETER-MIB", "apDiameterResultCode"))
)
if mibBuilder.loadTexts:
    apDiameterSrvrErrorResultTrap.setStatus(
        "current"
    )

apDiameterSrvrSuccessResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 6)
)
apDiameterSrvrSuccessResultTrap.setObjects(
      *(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"),
        ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"),
        ("AP-DIAMETER-MIB", "apDiameterResultCode"))
)
if mibBuilder.loadTexts:
    apDiameterSrvrSuccessResultTrap.setStatus(
        "current"
    )


# Notifications groups

apDiamACCTNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 2)
)
apDiamACCTNotificationsGroup.setObjects(
      *(("AP-DIAMETER-MIB", "apDiameterAcctSrvrUpTrap"),
        ("AP-DIAMETER-MIB", "apDiameterAcctSrvrDownTrap"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueFullTrap"),
        ("AP-DIAMETER-MIB", "apAcctMsgQueueFullClearTrap"))
)
if mibBuilder.loadTexts:
    apDiamACCTNotificationsGroup.setStatus(
        "current"
    )

apDiamACCTResultNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 4)
)
apDiamACCTResultNotificationsGroup.setObjects(
      *(("AP-DIAMETER-MIB", "apDiameterSrvrErrorResultTrap"),
        ("AP-DIAMETER-MIB", "apDiameterSrvrSuccessResultTrap"))
)
if mibBuilder.loadTexts:
    apDiamACCTResultNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP-DIAMETER-MIB",
    **{"apDiameterModule": apDiameterModule,
       "apDiamMIBModule": apDiamMIBModule,
       "apDiamMIBObjects": apDiamMIBObjects,
       "apDiamiMIBTabularObjects": apDiamiMIBTabularObjects,
       "apDiamClfErrorStatsTable": apDiamClfErrorStatsTable,
       "apDiamClfErrorStatsEntry": apDiamClfErrorStatsEntry,
       "apDiamClfExtPolSvrIndex": apDiamClfExtPolSvrIndex,
       "apDiamClfExtPolSvrName": apDiamClfExtPolSvrName,
       "apDiamClfErrorsRecent": apDiamClfErrorsRecent,
       "apDiamClfErrorsTotal": apDiamClfErrorsTotal,
       "apDiamClfErrorsPerMax": apDiamClfErrorsPerMax,
       "apDiamInterfaceStatsTable": apDiamInterfaceStatsTable,
       "apDiamInterfaceStatsEntry": apDiamInterfaceStatsEntry,
       "apDiamInterfaceType": apDiamInterfaceType,
       "apDiamInterfaceAddress": apDiamInterfaceAddress,
       "apDiamMessagesSent": apDiamMessagesSent,
       "apDiamMessagesSentFailed": apDiamMessagesSentFailed,
       "apDiamMessagesReSent": apDiamMessagesReSent,
       "apDiamMessagesReceived": apDiamMessagesReceived,
       "apDiamMessagesProcessed": apDiamMessagesProcessed,
       "apDiamConnectionTimeouts": apDiamConnectionTimeouts,
       "apDiamBadStateDrops": apDiamBadStateDrops,
       "apDiamBadTypeDrops": apDiamBadTypeDrops,
       "apDiamBadIDDrops": apDiamBadIDDrops,
       "apDiamAuthFailDrops": apDiamAuthFailDrops,
       "apDiamInvalidPeerMessages": apDiamInvalidPeerMessages,
       "apDiamNotificationObjects": apDiamNotificationObjects,
       "apDiamNotifObjects": apDiamNotifObjects,
       "apDiamAcctSrvrHostName": apDiamAcctSrvrHostName,
       "apDiamAcctSrvrIPPort": apDiamAcctSrvrIPPort,
       "apDiamAcctSrvrOriginRealm": apDiamAcctSrvrOriginRealm,
       "apDiamAcctSrvrOriginHost": apDiamAcctSrvrOriginHost,
       "apDiamAcctSrvrTransportType": apDiamAcctSrvrTransportType,
       "apAcctMsgQueueAvailCurrent": apAcctMsgQueueAvailCurrent,
       "apAcctMsgQueueMinorThreshold": apAcctMsgQueueMinorThreshold,
       "apAcctMsgQueueMajorThreshold": apAcctMsgQueueMajorThreshold,
       "apAcctMsgQueueCriticalThreshold": apAcctMsgQueueCriticalThreshold,
       "apDiameterResultCode": apDiameterResultCode,
       "apDiamNotifPrefix": apDiamNotifPrefix,
       "apDiamNotifications": apDiamNotifications,
       "apDiameterAcctSrvrUpTrap": apDiameterAcctSrvrUpTrap,
       "apDiameterAcctSrvrDownTrap": apDiameterAcctSrvrDownTrap,
       "apAcctMsgQueueFullTrap": apAcctMsgQueueFullTrap,
       "apAcctMsgQueueFullClearTrap": apAcctMsgQueueFullClearTrap,
       "apDiameterSrvrErrorResultTrap": apDiameterSrvrErrorResultTrap,
       "apDiameterSrvrSuccessResultTrap": apDiameterSrvrSuccessResultTrap,
       "apDiamConformance": apDiamConformance,
       "apDiamObjectGroups": apDiamObjectGroups,
       "apDiamClfErrorStatsGroup": apDiamClfErrorStatsGroup,
       "apDiamNotificationGroups": apDiamNotificationGroups,
       "apDiamInterfaceStatsGroup": apDiamInterfaceStatsGroup,
       "apDiamACCTObjectsGroup": apDiamACCTObjectsGroup,
       "apDiamACCTNotificationsGroup": apDiamACCTNotificationsGroup,
       "apDiamACCTResultObjectsGroup": apDiamACCTResultObjectsGroup,
       "apDiamACCTResultNotificationsGroup": apDiamACCTResultNotificationsGroup}
)
