# SNMP MIB module (XGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XGCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:39 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

xgcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 90)
)
xgcpMIB.setRevisions(
        ("1999-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XgcpObjects_ObjectIdentity = ObjectIdentity
xgcpObjects = _XgcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1)
)
_XgcpCoreObjects_ObjectIdentity = ObjectIdentity
xgcpCoreObjects = _XgcpCoreObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1, 1)
)
_XgcpInBadVersions_Type = Counter32
_XgcpInBadVersions_Object = MibScalar
xgcpInBadVersions = _XgcpInBadVersions_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 1),
    _XgcpInBadVersions_Type()
)
xgcpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpInBadVersions.setStatus("current")
if mibBuilder.loadTexts:
    xgcpInBadVersions.setUnits("messages")


class _XgcpRequestTimeOut_Type(Integer32):
    """Custom type xgcpRequestTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_XgcpRequestTimeOut_Type.__name__ = "Integer32"
_XgcpRequestTimeOut_Object = MibScalar
xgcpRequestTimeOut = _XgcpRequestTimeOut_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 2),
    _XgcpRequestTimeOut_Type()
)
xgcpRequestTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpRequestTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    xgcpRequestTimeOut.setUnits("milliseconds")


class _XgcpRequestRetries_Type(Integer32):
    """Custom type xgcpRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_XgcpRequestRetries_Type.__name__ = "Integer32"
_XgcpRequestRetries_Object = MibScalar
xgcpRequestRetries = _XgcpRequestRetries_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 3),
    _XgcpRequestRetries_Type()
)
xgcpRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpRequestRetries.setStatus("current")


class _XgcpAdminStatus_Type(Integer32):
    """Custom type xgcpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("gracefulDown", 3),
          ("up", 1))
    )


_XgcpAdminStatus_Type.__name__ = "Integer32"
_XgcpAdminStatus_Object = MibScalar
xgcpAdminStatus = _XgcpAdminStatus_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 4),
    _XgcpAdminStatus_Type()
)
xgcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpAdminStatus.setStatus("current")


class _XgcpOperStatus_Type(Integer32):
    """Custom type xgcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("shutDownInProgress", 3),
          ("up", 1))
    )


_XgcpOperStatus_Type.__name__ = "Integer32"
_XgcpOperStatus_Object = MibScalar
xgcpOperStatus = _XgcpOperStatus_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 5),
    _XgcpOperStatus_Type()
)
xgcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpOperStatus.setStatus("current")
_XgcpUnRecognizedPackets_Type = Counter32
_XgcpUnRecognizedPackets_Object = MibScalar
xgcpUnRecognizedPackets = _XgcpUnRecognizedPackets_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 6),
    _XgcpUnRecognizedPackets_Type()
)
xgcpUnRecognizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpUnRecognizedPackets.setStatus("current")
_XgcpMsgStatTable_Object = MibTable
xgcpMsgStatTable = _XgcpMsgStatTable_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 7)
)
if mibBuilder.loadTexts:
    xgcpMsgStatTable.setStatus("current")
_XgcpMsgStatEntry_Object = MibTableRow
xgcpMsgStatEntry = _XgcpMsgStatEntry_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 7, 1)
)
xgcpMsgStatEntry.setIndexNames(
    (0, "XGCP-MIB", "xgcpIPAddress"),
)
if mibBuilder.loadTexts:
    xgcpMsgStatEntry.setStatus("current")
_XgcpIPAddress_Type = IpAddress
_XgcpIPAddress_Object = MibTableColumn
xgcpIPAddress = _XgcpIPAddress_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 1),
    _XgcpIPAddress_Type()
)
xgcpIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgcpIPAddress.setStatus("current")
_XgcpSuccessMessages_Type = Counter32
_XgcpSuccessMessages_Object = MibTableColumn
xgcpSuccessMessages = _XgcpSuccessMessages_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 2),
    _XgcpSuccessMessages_Type()
)
xgcpSuccessMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpSuccessMessages.setStatus("current")
_XgcpFailMessages_Type = Counter32
_XgcpFailMessages_Object = MibTableColumn
xgcpFailMessages = _XgcpFailMessages_Object(
    (1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 3),
    _XgcpFailMessages_Type()
)
xgcpFailMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpFailMessages.setStatus("current")
_XgcpExtensionObjects_ObjectIdentity = ObjectIdentity
xgcpExtensionObjects = _XgcpExtensionObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1, 2)
)


class _XgcpRestartInProgressMWD_Type(Integer32):
    """Custom type xgcpRestartInProgressMWD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_XgcpRestartInProgressMWD_Type.__name__ = "Integer32"
_XgcpRestartInProgressMWD_Object = MibScalar
xgcpRestartInProgressMWD = _XgcpRestartInProgressMWD_Object(
    (1, 3, 6, 1, 3, 90, 1, 2, 1),
    _XgcpRestartInProgressMWD_Type()
)
xgcpRestartInProgressMWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpRestartInProgressMWD.setStatus("current")
if mibBuilder.loadTexts:
    xgcpRestartInProgressMWD.setUnits("milliseconds")


class _XgcpRestartDelay_Type(Integer32):
    """Custom type xgcpRestartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_XgcpRestartDelay_Type.__name__ = "Integer32"
_XgcpRestartDelay_Object = MibScalar
xgcpRestartDelay = _XgcpRestartDelay_Object(
    (1, 3, 6, 1, 3, 90, 1, 2, 2),
    _XgcpRestartDelay_Type()
)
xgcpRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    xgcpRestartDelay.setUnits("seconds")
_XgcpPackageObjects_ObjectIdentity = ObjectIdentity
xgcpPackageObjects = _XgcpPackageObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1, 3)
)
_XgcpCapabilityPackageTable_Object = MibTable
xgcpCapabilityPackageTable = _XgcpCapabilityPackageTable_Object(
    (1, 3, 6, 1, 3, 90, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xgcpCapabilityPackageTable.setStatus("current")
_XgcpCapabilityPackageEntry_Object = MibTableRow
xgcpCapabilityPackageEntry = _XgcpCapabilityPackageEntry_Object(
    (1, 3, 6, 1, 3, 90, 1, 3, 1, 1)
)
xgcpCapabilityPackageEntry.setIndexNames(
    (1, "XGCP-MIB", "xgcpCapabilityPackageName"),
)
if mibBuilder.loadTexts:
    xgcpCapabilityPackageEntry.setStatus("current")


class _XgcpCapabilityPackageName_Type(DisplayString):
    """Custom type xgcpCapabilityPackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XgcpCapabilityPackageName_Type.__name__ = "DisplayString"
_XgcpCapabilityPackageName_Object = MibTableColumn
xgcpCapabilityPackageName = _XgcpCapabilityPackageName_Object(
    (1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 1),
    _XgcpCapabilityPackageName_Type()
)
xgcpCapabilityPackageName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgcpCapabilityPackageName.setStatus("current")


class _XgcpCapabilityPackageEnable_Type(TruthValue):
    """Custom type xgcpCapabilityPackageEnable based on TruthValue"""


_XgcpCapabilityPackageEnable_Object = MibTableColumn
xgcpCapabilityPackageEnable = _XgcpCapabilityPackageEnable_Object(
    (1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 2),
    _XgcpCapabilityPackageEnable_Type()
)
xgcpCapabilityPackageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpCapabilityPackageEnable.setStatus("current")


class _XgcpDefaultPackage_Type(DisplayString):
    """Custom type xgcpDefaultPackage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XgcpDefaultPackage_Type.__name__ = "DisplayString"
_XgcpDefaultPackage_Object = MibScalar
xgcpDefaultPackage = _XgcpDefaultPackage_Object(
    (1, 3, 6, 1, 3, 90, 1, 3, 2),
    _XgcpDefaultPackage_Type()
)
xgcpDefaultPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpDefaultPackage.setStatus("current")
_XgcpVoiceQualityObjects_ObjectIdentity = ObjectIdentity
xgcpVoiceQualityObjects = _XgcpVoiceQualityObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1, 4)
)


class _XgcpLowerBoundForPacketLoss_Type(Integer32):
    """Custom type xgcpLowerBoundForPacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_XgcpLowerBoundForPacketLoss_Type.__name__ = "Integer32"
_XgcpLowerBoundForPacketLoss_Object = MibScalar
xgcpLowerBoundForPacketLoss = _XgcpLowerBoundForPacketLoss_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 1),
    _XgcpLowerBoundForPacketLoss_Type()
)
xgcpLowerBoundForPacketLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpLowerBoundForPacketLoss.setStatus("current")


class _XgcpHigherBoundForPacketLoss_Type(Integer32):
    """Custom type xgcpHigherBoundForPacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 25000),
    )


_XgcpHigherBoundForPacketLoss_Type.__name__ = "Integer32"
_XgcpHigherBoundForPacketLoss_Object = MibScalar
xgcpHigherBoundForPacketLoss = _XgcpHigherBoundForPacketLoss_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 2),
    _XgcpHigherBoundForPacketLoss_Type()
)
xgcpHigherBoundForPacketLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpHigherBoundForPacketLoss.setStatus("current")


class _XgcpLowerBoundForJitter_Type(Integer32):
    """Custom type xgcpLowerBoundForJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_XgcpLowerBoundForJitter_Type.__name__ = "Integer32"
_XgcpLowerBoundForJitter_Object = MibScalar
xgcpLowerBoundForJitter = _XgcpLowerBoundForJitter_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 3),
    _XgcpLowerBoundForJitter_Type()
)
xgcpLowerBoundForJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpLowerBoundForJitter.setStatus("current")
if mibBuilder.loadTexts:
    xgcpLowerBoundForJitter.setUnits("milliseconds")


class _XgcpHigherBoundForJitter_Type(Integer32):
    """Custom type xgcpHigherBoundForJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_XgcpHigherBoundForJitter_Type.__name__ = "Integer32"
_XgcpHigherBoundForJitter_Object = MibScalar
xgcpHigherBoundForJitter = _XgcpHigherBoundForJitter_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 4),
    _XgcpHigherBoundForJitter_Type()
)
xgcpHigherBoundForJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpHigherBoundForJitter.setStatus("current")
if mibBuilder.loadTexts:
    xgcpHigherBoundForJitter.setUnits("milliseconds")


class _XgcpLowerBoundForLatency_Type(Integer32):
    """Custom type xgcpLowerBoundForLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 200),
    )


_XgcpLowerBoundForLatency_Type.__name__ = "Integer32"
_XgcpLowerBoundForLatency_Object = MibScalar
xgcpLowerBoundForLatency = _XgcpLowerBoundForLatency_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 5),
    _XgcpLowerBoundForLatency_Type()
)
xgcpLowerBoundForLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpLowerBoundForLatency.setStatus("current")
if mibBuilder.loadTexts:
    xgcpLowerBoundForLatency.setUnits("milliseconds")


class _XgcpHigherBoundForLatency_Type(Integer32):
    """Custom type xgcpHigherBoundForLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 400),
    )


_XgcpHigherBoundForLatency_Type.__name__ = "Integer32"
_XgcpHigherBoundForLatency_Object = MibScalar
xgcpHigherBoundForLatency = _XgcpHigherBoundForLatency_Object(
    (1, 3, 6, 1, 3, 90, 1, 4, 6),
    _XgcpHigherBoundForLatency_Type()
)
xgcpHigherBoundForLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpHigherBoundForLatency.setStatus("current")
if mibBuilder.loadTexts:
    xgcpHigherBoundForLatency.setUnits("milliseconds")
_XgcpDefaultMGCObjects_ObjectIdentity = ObjectIdentity
xgcpDefaultMGCObjects = _XgcpDefaultMGCObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 1, 5)
)


class _XgcpMGCCfgAddress_Type(DisplayString):
    """Custom type xgcpMGCCfgAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XgcpMGCCfgAddress_Type.__name__ = "DisplayString"
_XgcpMGCCfgAddress_Object = MibScalar
xgcpMGCCfgAddress = _XgcpMGCCfgAddress_Object(
    (1, 3, 6, 1, 3, 90, 1, 5, 1),
    _XgcpMGCCfgAddress_Type()
)
xgcpMGCCfgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpMGCCfgAddress.setStatus("current")


class _XgcpMGCCfgUDPPort_Type(Integer32):
    """Custom type xgcpMGCCfgUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_XgcpMGCCfgUDPPort_Type.__name__ = "Integer32"
_XgcpMGCCfgUDPPort_Object = MibScalar
xgcpMGCCfgUDPPort = _XgcpMGCCfgUDPPort_Object(
    (1, 3, 6, 1, 3, 90, 1, 5, 2),
    _XgcpMGCCfgUDPPort_Type()
)
xgcpMGCCfgUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgcpMGCCfgUDPPort.setStatus("current")


class _XgcpMGCCfgConnStatus_Type(Integer32):
    """Custom type xgcpMGCCfgConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 3),
          ("noResponse", 5),
          ("noSuchName", 4),
          ("unknown", 1))
    )


_XgcpMGCCfgConnStatus_Type.__name__ = "Integer32"
_XgcpMGCCfgConnStatus_Object = MibScalar
xgcpMGCCfgConnStatus = _XgcpMGCCfgConnStatus_Object(
    (1, 3, 6, 1, 3, 90, 1, 5, 3),
    _XgcpMGCCfgConnStatus_Type()
)
xgcpMGCCfgConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpMGCCfgConnStatus.setStatus("current")
_XgcpMGCCfgTimeStamp_Type = TimeStamp
_XgcpMGCCfgTimeStamp_Object = MibScalar
xgcpMGCCfgTimeStamp = _XgcpMGCCfgTimeStamp_Object(
    (1, 3, 6, 1, 3, 90, 1, 5, 4),
    _XgcpMGCCfgTimeStamp_Type()
)
xgcpMGCCfgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgcpMGCCfgTimeStamp.setStatus("current")
_XgcpNotificationPrefix_ObjectIdentity = ObjectIdentity
xgcpNotificationPrefix = _XgcpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 2)
)
_XgcpNotifications_ObjectIdentity = ObjectIdentity
xgcpNotifications = _XgcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 2, 0)
)
_XgcpMIBConformance_ObjectIdentity = ObjectIdentity
xgcpMIBConformance = _XgcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 3)
)
_XgcpMIBCompliances_ObjectIdentity = ObjectIdentity
xgcpMIBCompliances = _XgcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 3, 1)
)
_XgcpMIBGroups_ObjectIdentity = ObjectIdentity
xgcpMIBGroups = _XgcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 90, 3, 2)
)

# Managed Objects groups

xgcpCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 90, 3, 2, 1)
)
xgcpCoreGroup.setObjects(
      *(("XGCP-MIB", "xgcpInBadVersions"),
        ("XGCP-MIB", "xgcpRequestTimeOut"),
        ("XGCP-MIB", "xgcpRequestRetries"),
        ("XGCP-MIB", "xgcpAdminStatus"),
        ("XGCP-MIB", "xgcpOperStatus"),
        ("XGCP-MIB", "xgcpUnRecognizedPackets"),
        ("XGCP-MIB", "xgcpSuccessMessages"),
        ("XGCP-MIB", "xgcpFailMessages"))
)
if mibBuilder.loadTexts:
    xgcpCoreGroup.setStatus("current")

xgcpExtensionGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 90, 3, 2, 2)
)
xgcpExtensionGroup.setObjects(
      *(("XGCP-MIB", "xgcpRestartInProgressMWD"),
        ("XGCP-MIB", "xgcpRestartDelay"))
)
if mibBuilder.loadTexts:
    xgcpExtensionGroup.setStatus("current")

xgcpPackageGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 90, 3, 2, 3)
)
xgcpPackageGroup.setObjects(
      *(("XGCP-MIB", "xgcpCapabilityPackageEnable"),
        ("XGCP-MIB", "xgcpDefaultPackage"))
)
if mibBuilder.loadTexts:
    xgcpPackageGroup.setStatus("current")

xgcpVoiceQualityGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 90, 3, 2, 4)
)
xgcpVoiceQualityGroup.setObjects(
      *(("XGCP-MIB", "xgcpLowerBoundForPacketLoss"),
        ("XGCP-MIB", "xgcpHigherBoundForPacketLoss"),
        ("XGCP-MIB", "xgcpLowerBoundForJitter"),
        ("XGCP-MIB", "xgcpHigherBoundForJitter"),
        ("XGCP-MIB", "xgcpLowerBoundForLatency"),
        ("XGCP-MIB", "xgcpHigherBoundForLatency"))
)
if mibBuilder.loadTexts:
    xgcpVoiceQualityGroup.setStatus("current")

xgcpDefaultMGCGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 90, 3, 2, 5)
)
xgcpDefaultMGCGroup.setObjects(
      *(("XGCP-MIB", "xgcpMGCCfgAddress"),
        ("XGCP-MIB", "xgcpMGCCfgUDPPort"),
        ("XGCP-MIB", "xgcpMGCCfgConnStatus"),
        ("XGCP-MIB", "xgcpMGCCfgTimeStamp"))
)
if mibBuilder.loadTexts:
    xgcpDefaultMGCGroup.setStatus("current")


# Notification objects

xgcpUpDownNotification = NotificationType(
    (1, 3, 6, 1, 3, 90, 2, 0, 1)
)
xgcpUpDownNotification.setObjects(
    ("XGCP-MIB", "xgcpOperStatus")
)
if mibBuilder.loadTexts:
    xgcpUpDownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xgcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 90, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xgcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XGCP-MIB",
    **{"xgcpMIB": xgcpMIB,
       "xgcpObjects": xgcpObjects,
       "xgcpCoreObjects": xgcpCoreObjects,
       "xgcpInBadVersions": xgcpInBadVersions,
       "xgcpRequestTimeOut": xgcpRequestTimeOut,
       "xgcpRequestRetries": xgcpRequestRetries,
       "xgcpAdminStatus": xgcpAdminStatus,
       "xgcpOperStatus": xgcpOperStatus,
       "xgcpUnRecognizedPackets": xgcpUnRecognizedPackets,
       "xgcpMsgStatTable": xgcpMsgStatTable,
       "xgcpMsgStatEntry": xgcpMsgStatEntry,
       "xgcpIPAddress": xgcpIPAddress,
       "xgcpSuccessMessages": xgcpSuccessMessages,
       "xgcpFailMessages": xgcpFailMessages,
       "xgcpExtensionObjects": xgcpExtensionObjects,
       "xgcpRestartInProgressMWD": xgcpRestartInProgressMWD,
       "xgcpRestartDelay": xgcpRestartDelay,
       "xgcpPackageObjects": xgcpPackageObjects,
       "xgcpCapabilityPackageTable": xgcpCapabilityPackageTable,
       "xgcpCapabilityPackageEntry": xgcpCapabilityPackageEntry,
       "xgcpCapabilityPackageName": xgcpCapabilityPackageName,
       "xgcpCapabilityPackageEnable": xgcpCapabilityPackageEnable,
       "xgcpDefaultPackage": xgcpDefaultPackage,
       "xgcpVoiceQualityObjects": xgcpVoiceQualityObjects,
       "xgcpLowerBoundForPacketLoss": xgcpLowerBoundForPacketLoss,
       "xgcpHigherBoundForPacketLoss": xgcpHigherBoundForPacketLoss,
       "xgcpLowerBoundForJitter": xgcpLowerBoundForJitter,
       "xgcpHigherBoundForJitter": xgcpHigherBoundForJitter,
       "xgcpLowerBoundForLatency": xgcpLowerBoundForLatency,
       "xgcpHigherBoundForLatency": xgcpHigherBoundForLatency,
       "xgcpDefaultMGCObjects": xgcpDefaultMGCObjects,
       "xgcpMGCCfgAddress": xgcpMGCCfgAddress,
       "xgcpMGCCfgUDPPort": xgcpMGCCfgUDPPort,
       "xgcpMGCCfgConnStatus": xgcpMGCCfgConnStatus,
       "xgcpMGCCfgTimeStamp": xgcpMGCCfgTimeStamp,
       "xgcpNotificationPrefix": xgcpNotificationPrefix,
       "xgcpNotifications": xgcpNotifications,
       "xgcpUpDownNotification": xgcpUpDownNotification,
       "xgcpMIBConformance": xgcpMIBConformance,
       "xgcpMIBCompliances": xgcpMIBCompliances,
       "xgcpMIBCompliance": xgcpMIBCompliance,
       "xgcpMIBGroups": xgcpMIBGroups,
       "xgcpCoreGroup": xgcpCoreGroup,
       "xgcpExtensionGroup": xgcpExtensionGroup,
       "xgcpPackageGroup": xgcpPackageGroup,
       "xgcpVoiceQualityGroup": xgcpVoiceQualityGroup,
       "xgcpDefaultMGCGroup": xgcpDefaultMGCGroup}
)
