# SNMP MIB module (MERU-CONFIG-PACKETCAPTURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-PACKETCAPTURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:04 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlEnableDisableOption,
 MwlEncapsulationType,
 MwlOnOffSwitch,
 MwlPacketCaptureMode,
 MwlRateLimitMode,
 MwlRxTxOption) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlEnableDisableOption",
    "MwlEncapsulationType",
    "MwlOnOffSwitch",
    "MwlPacketCaptureMode",
    "MwlRateLimitMode",
    "MwlRxTxOption")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigPacketCapture = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwPacketCaptureProfileTable_Object = MibTable
mwPacketCaptureProfileTable = _MwPacketCaptureProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1)
)
if mibBuilder.loadTexts:
    mwPacketCaptureProfileTable.setStatus("current")
_MwPacketCaptureProfileEntry_Object = MibTableRow
mwPacketCaptureProfileEntry = _MwPacketCaptureProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1)
)
mwPacketCaptureProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-PACKETCAPTURE-MIB", "mwPacketCaptureProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwPacketCaptureProfileEntry.setStatus("current")
_MwPacketCaptureProfileTableIndex_Type = Integer32
_MwPacketCaptureProfileTableIndex_Object = MibTableColumn
mwPacketCaptureProfileTableIndex = _MwPacketCaptureProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 1),
    _MwPacketCaptureProfileTableIndex_Type()
)
mwPacketCaptureProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileTableIndex.setStatus("current")


class _MwPacketCaptureProfileName_Type(DisplayString):
    """Custom type mwPacketCaptureProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwPacketCaptureProfileName_Type.__name__ = "DisplayString"
_MwPacketCaptureProfileName_Object = MibTableColumn
mwPacketCaptureProfileName = _MwPacketCaptureProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 2),
    _MwPacketCaptureProfileName_Type()
)
mwPacketCaptureProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileName.setStatus("current")
_MwPacketCaptureProfileStatus_Type = MwlEnableDisableOption
_MwPacketCaptureProfileStatus_Object = MibTableColumn
mwPacketCaptureProfileStatus = _MwPacketCaptureProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 3),
    _MwPacketCaptureProfileStatus_Type()
)
mwPacketCaptureProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileStatus.setStatus("current")
_MwPacketCaptureProfileConnectivityMode_Type = MwlPacketCaptureMode
_MwPacketCaptureProfileConnectivityMode_Object = MibTableColumn
mwPacketCaptureProfileConnectivityMode = _MwPacketCaptureProfileConnectivityMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 4),
    _MwPacketCaptureProfileConnectivityMode_Type()
)
mwPacketCaptureProfileConnectivityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileConnectivityMode.setStatus("current")
_MwPacketCaptureProfileDestinationIp_Type = IpAddress
_MwPacketCaptureProfileDestinationIp_Object = MibTableColumn
mwPacketCaptureProfileDestinationIp = _MwPacketCaptureProfileDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 5),
    _MwPacketCaptureProfileDestinationIp_Type()
)
mwPacketCaptureProfileDestinationIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileDestinationIp.setStatus("current")
_MwPacketCaptureProfileUDPPort_Type = Unsigned32
_MwPacketCaptureProfileUDPPort_Object = MibTableColumn
mwPacketCaptureProfileUDPPort = _MwPacketCaptureProfileUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 6),
    _MwPacketCaptureProfileUDPPort_Type()
)
mwPacketCaptureProfileUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileUDPPort.setStatus("current")
_MwPacketCaptureProfileDestinationMac_Type = MacAddress
_MwPacketCaptureProfileDestinationMac_Object = MibTableColumn
mwPacketCaptureProfileDestinationMac = _MwPacketCaptureProfileDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 7),
    _MwPacketCaptureProfileDestinationMac_Type()
)
mwPacketCaptureProfileDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileDestinationMac.setStatus("current")
_MwPacketCaptureProfileRxTx_Type = MwlRxTxOption
_MwPacketCaptureProfileRxTx_Object = MibTableColumn
mwPacketCaptureProfileRxTx = _MwPacketCaptureProfileRxTx_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 8),
    _MwPacketCaptureProfileRxTx_Type()
)
mwPacketCaptureProfileRxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileRxTx.setStatus("current")
_MwPacketCaptureProfileRateLimitMode_Type = MwlRateLimitMode
_MwPacketCaptureProfileRateLimitMode_Object = MibTableColumn
mwPacketCaptureProfileRateLimitMode = _MwPacketCaptureProfileRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 9),
    _MwPacketCaptureProfileRateLimitMode_Type()
)
mwPacketCaptureProfileRateLimitMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileRateLimitMode.setStatus("current")
_MwPacketCaptureProfileTokenBucketRate_Type = Unsigned32
_MwPacketCaptureProfileTokenBucketRate_Object = MibTableColumn
mwPacketCaptureProfileTokenBucketRate = _MwPacketCaptureProfileTokenBucketRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 10),
    _MwPacketCaptureProfileTokenBucketRate_Type()
)
mwPacketCaptureProfileTokenBucketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileTokenBucketRate.setStatus("current")
_MwPacketCaptureProfileTokenBucketSize_Type = Unsigned32
_MwPacketCaptureProfileTokenBucketSize_Object = MibTableColumn
mwPacketCaptureProfileTokenBucketSize = _MwPacketCaptureProfileTokenBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 11),
    _MwPacketCaptureProfileTokenBucketSize_Type()
)
mwPacketCaptureProfileTokenBucketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileTokenBucketSize.setStatus("current")


class _MwPacketCaptureProfileApList_Type(DisplayString):
    """Custom type mwPacketCaptureProfileApList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_MwPacketCaptureProfileApList_Type.__name__ = "DisplayString"
_MwPacketCaptureProfileApList_Object = MibTableColumn
mwPacketCaptureProfileApList = _MwPacketCaptureProfileApList_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 12),
    _MwPacketCaptureProfileApList_Type()
)
mwPacketCaptureProfileApList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileApList.setStatus("current")


class _MwPacketCaptureProfileFilter_Type(DisplayString):
    """Custom type mwPacketCaptureProfileFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwPacketCaptureProfileFilter_Type.__name__ = "DisplayString"
_MwPacketCaptureProfileFilter_Object = MibTableColumn
mwPacketCaptureProfileFilter = _MwPacketCaptureProfileFilter_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 13),
    _MwPacketCaptureProfileFilter_Type()
)
mwPacketCaptureProfileFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileFilter.setStatus("current")


class _MwPacketCaptureProfileInterfaceList_Type(DisplayString):
    """Custom type mwPacketCaptureProfileInterfaceList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwPacketCaptureProfileInterfaceList_Type.__name__ = "DisplayString"
_MwPacketCaptureProfileInterfaceList_Object = MibTableColumn
mwPacketCaptureProfileInterfaceList = _MwPacketCaptureProfileInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 14),
    _MwPacketCaptureProfileInterfaceList_Type()
)
mwPacketCaptureProfileInterfaceList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileInterfaceList.setStatus("current")
_MwPacketCaptureProfilePacketTruncationLength_Type = Unsigned32
_MwPacketCaptureProfilePacketTruncationLength_Object = MibTableColumn
mwPacketCaptureProfilePacketTruncationLength = _MwPacketCaptureProfilePacketTruncationLength_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 15),
    _MwPacketCaptureProfilePacketTruncationLength_Type()
)
mwPacketCaptureProfilePacketTruncationLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfilePacketTruncationLength.setStatus("current")
_MwPacketCaptureProfileRateLimiting_Type = MwlOnOffSwitch
_MwPacketCaptureProfileRateLimiting_Object = MibTableColumn
mwPacketCaptureProfileRateLimiting = _MwPacketCaptureProfileRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 16),
    _MwPacketCaptureProfileRateLimiting_Type()
)
mwPacketCaptureProfileRateLimiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileRateLimiting.setStatus("current")
_MwPacketCaptureProfileCaptureSiblingFrames_Type = MwlOnOffSwitch
_MwPacketCaptureProfileCaptureSiblingFrames_Object = MibTableColumn
mwPacketCaptureProfileCaptureSiblingFrames = _MwPacketCaptureProfileCaptureSiblingFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 17),
    _MwPacketCaptureProfileCaptureSiblingFrames_Type()
)
mwPacketCaptureProfileCaptureSiblingFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileCaptureSiblingFrames.setStatus("current")
_MwPacketCaptureProfileEncapsulation_Type = MwlEncapsulationType
_MwPacketCaptureProfileEncapsulation_Object = MibTableColumn
mwPacketCaptureProfileEncapsulation = _MwPacketCaptureProfileEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 18),
    _MwPacketCaptureProfileEncapsulation_Type()
)
mwPacketCaptureProfileEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileEncapsulation.setStatus("current")
_MwPacketCaptureProfileRowStatus_Type = RowStatus
_MwPacketCaptureProfileRowStatus_Object = MibTableColumn
mwPacketCaptureProfileRowStatus = _MwPacketCaptureProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 19),
    _MwPacketCaptureProfileRowStatus_Type()
)
mwPacketCaptureProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPacketCaptureProfileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-PACKETCAPTURE-MIB",
    **{"mwConfigPacketCapture": mwConfigPacketCapture,
       "mwPacketCaptureProfileTable": mwPacketCaptureProfileTable,
       "mwPacketCaptureProfileEntry": mwPacketCaptureProfileEntry,
       "mwPacketCaptureProfileTableIndex": mwPacketCaptureProfileTableIndex,
       "mwPacketCaptureProfileName": mwPacketCaptureProfileName,
       "mwPacketCaptureProfileStatus": mwPacketCaptureProfileStatus,
       "mwPacketCaptureProfileConnectivityMode": mwPacketCaptureProfileConnectivityMode,
       "mwPacketCaptureProfileDestinationIp": mwPacketCaptureProfileDestinationIp,
       "mwPacketCaptureProfileUDPPort": mwPacketCaptureProfileUDPPort,
       "mwPacketCaptureProfileDestinationMac": mwPacketCaptureProfileDestinationMac,
       "mwPacketCaptureProfileRxTx": mwPacketCaptureProfileRxTx,
       "mwPacketCaptureProfileRateLimitMode": mwPacketCaptureProfileRateLimitMode,
       "mwPacketCaptureProfileTokenBucketRate": mwPacketCaptureProfileTokenBucketRate,
       "mwPacketCaptureProfileTokenBucketSize": mwPacketCaptureProfileTokenBucketSize,
       "mwPacketCaptureProfileApList": mwPacketCaptureProfileApList,
       "mwPacketCaptureProfileFilter": mwPacketCaptureProfileFilter,
       "mwPacketCaptureProfileInterfaceList": mwPacketCaptureProfileInterfaceList,
       "mwPacketCaptureProfilePacketTruncationLength": mwPacketCaptureProfilePacketTruncationLength,
       "mwPacketCaptureProfileRateLimiting": mwPacketCaptureProfileRateLimiting,
       "mwPacketCaptureProfileCaptureSiblingFrames": mwPacketCaptureProfileCaptureSiblingFrames,
       "mwPacketCaptureProfileEncapsulation": mwPacketCaptureProfileEncapsulation,
       "mwPacketCaptureProfileRowStatus": mwPacketCaptureProfileRowStatus}
)
