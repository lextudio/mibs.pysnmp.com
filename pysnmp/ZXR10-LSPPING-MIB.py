# SNMP MIB module (ZXR10-LSPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-LSPPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:55 2024
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
 enterprises,
 experimental,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxr10L2vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L2vpn")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10LspPingMIB_ObjectIdentity = ObjectIdentity
zxr10LspPingMIB = _Zxr10LspPingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5)
)
_LspPingTable_Object = MibTable
lspPingTable = _LspPingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1)
)
if mibBuilder.loadTexts:
    lspPingTable.setStatus("current")
_LspPingEntry_Object = MibTableRow
lspPingEntry = _LspPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1)
)
lspPingEntry.setIndexNames(
    (0, "ZXR10-LSPPING-MIB", "lspPingSerial"),
)
if mibBuilder.loadTexts:
    lspPingEntry.setStatus("current")
_LspPingSerial_Type = Integer32
_LspPingSerial_Object = MibTableColumn
lspPingSerial = _LspPingSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 1),
    _LspPingSerial_Type()
)
lspPingSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingSerial.setStatus("current")


class _LspPingType_Type(Integer32):
    """Custom type lspPingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 0),
          ("rsvp-te", 1),
          ("vccv", 2))
    )


_LspPingType_Type.__name__ = "Integer32"
_LspPingType_Object = MibTableColumn
lspPingType = _LspPingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 2),
    _LspPingType_Type()
)
lspPingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingType.setStatus("current")
_LspPingLdpPrefix_Type = IpAddress
_LspPingLdpPrefix_Object = MibTableColumn
lspPingLdpPrefix = _LspPingLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 3),
    _LspPingLdpPrefix_Type()
)
lspPingLdpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingLdpPrefix.setStatus("current")
_LspPingLdpPrefixlen_Type = Integer32
_LspPingLdpPrefixlen_Object = MibTableColumn
lspPingLdpPrefixlen = _LspPingLdpPrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 4),
    _LspPingLdpPrefixlen_Type()
)
lspPingLdpPrefixlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingLdpPrefixlen.setStatus("current")
_LspPingMplsTeTunnelIfName_Type = Integer32
_LspPingMplsTeTunnelIfName_Object = MibTableColumn
lspPingMplsTeTunnelIfName = _LspPingMplsTeTunnelIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 5),
    _LspPingMplsTeTunnelIfName_Type()
)
lspPingMplsTeTunnelIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingMplsTeTunnelIfName.setStatus("current")
_LspPingAtomDesAddr_Type = IpAddress
_LspPingAtomDesAddr_Object = MibTableColumn
lspPingAtomDesAddr = _LspPingAtomDesAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 6),
    _LspPingAtomDesAddr_Type()
)
lspPingAtomDesAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingAtomDesAddr.setStatus("current")
_LspPingAtomVcid_Type = Integer32
_LspPingAtomVcid_Object = MibTableColumn
lspPingAtomVcid = _LspPingAtomVcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 7),
    _LspPingAtomVcid_Type()
)
lspPingAtomVcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingAtomVcid.setStatus("current")


class _LspPingIfOption_Type(Integer32):
    """Custom type lspPingIfOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("option", 1))
    )


_LspPingIfOption_Type.__name__ = "Integer32"
_LspPingIfOption_Object = MibTableColumn
lspPingIfOption = _LspPingIfOption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 8),
    _LspPingIfOption_Type()
)
lspPingIfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingIfOption.setStatus("current")


class _LspPingPacketCount_Type(Integer32):
    """Custom type lspPingPacketCount based on Integer32"""
    defaultValue = 5


_LspPingPacketCount_Object = MibTableColumn
lspPingPacketCount = _LspPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 9),
    _LspPingPacketCount_Type()
)
lspPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingPacketCount.setStatus("current")


class _LspPingTimeOut_Type(Integer32):
    """Custom type lspPingTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LspPingTimeOut_Type.__name__ = "Integer32"
_LspPingTimeOut_Object = MibTableColumn
lspPingTimeOut = _LspPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 10),
    _LspPingTimeOut_Type()
)
lspPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingTimeOut.setStatus("current")


class _LspPingDataLen_Type(Integer32):
    """Custom type lspPingDataLen based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 8192),
    )


_LspPingDataLen_Type.__name__ = "Integer32"
_LspPingDataLen_Object = MibTableColumn
lspPingDataLen = _LspPingDataLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 11),
    _LspPingDataLen_Type()
)
lspPingDataLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingDataLen.setStatus("current")


class _LspPingTrapOncompletion_Type(TruthValue):
    """Custom type lspPingTrapOncompletion based on TruthValue"""


_LspPingTrapOncompletion_Object = MibTableColumn
lspPingTrapOncompletion = _LspPingTrapOncompletion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 12),
    _LspPingTrapOncompletion_Type()
)
lspPingTrapOncompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingTrapOncompletion.setStatus("current")


class _LspPingRosStatus_Type(Integer32):
    """Custom type lspPingRosStatus based on Integer32"""
    defaultValue = 1

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
        *(("not-active", 1),
          ("ping-completed", 4),
          ("ping-processing", 3),
          ("start-ping", 2))
    )


_LspPingRosStatus_Type.__name__ = "Integer32"
_LspPingRosStatus_Object = MibTableColumn
lspPingRosStatus = _LspPingRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 13),
    _LspPingRosStatus_Type()
)
lspPingRosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingRosStatus.setStatus("current")
_LspPingEntryOwner_Type = DisplayString
_LspPingEntryOwner_Object = MibTableColumn
lspPingEntryOwner = _LspPingEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 1, 1, 14),
    _LspPingEntryOwner_Type()
)
lspPingEntryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspPingEntryOwner.setStatus("current")
_LspPingResultTable_Object = MibTable
lspPingResultTable = _LspPingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2)
)
if mibBuilder.loadTexts:
    lspPingResultTable.setStatus("current")
_LspPingResultEntry_Object = MibTableRow
lspPingResultEntry = _LspPingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1)
)
lspPingResultEntry.setIndexNames(
    (0, "ZXR10-LSPPING-MIB", "lspPingResultSerial"),
)
if mibBuilder.loadTexts:
    lspPingResultEntry.setStatus("current")
_LspPingResultSerial_Type = Integer32
_LspPingResultSerial_Object = MibTableColumn
lspPingResultSerial = _LspPingResultSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 1),
    _LspPingResultSerial_Type()
)
lspPingResultSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultSerial.setStatus("current")
_LspPingResultSentPkts_Type = Integer32
_LspPingResultSentPkts_Object = MibTableColumn
lspPingResultSentPkts = _LspPingResultSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 2),
    _LspPingResultSentPkts_Type()
)
lspPingResultSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultSentPkts.setStatus("current")
_LspPingResultRcvPkts_Type = Integer32
_LspPingResultRcvPkts_Object = MibTableColumn
lspPingResultRcvPkts = _LspPingResultRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 3),
    _LspPingResultRcvPkts_Type()
)
lspPingResultRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRcvPkts.setStatus("current")
_LspPingResultRoundTripMinTime_Type = Integer32
_LspPingResultRoundTripMinTime_Object = MibTableColumn
lspPingResultRoundTripMinTime = _LspPingResultRoundTripMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 4),
    _LspPingResultRoundTripMinTime_Type()
)
lspPingResultRoundTripMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundTripMinTime.setStatus("current")
_LspPingResultRoundTripMaxTime_Type = Integer32
_LspPingResultRoundTripMaxTime_Object = MibTableColumn
lspPingResultRoundTripMaxTime = _LspPingResultRoundTripMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 5),
    _LspPingResultRoundTripMaxTime_Type()
)
lspPingResultRoundTripMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundTripMaxTime.setStatus("current")
_LspPingResultRoundTripAvgTime_Type = Integer32
_LspPingResultRoundTripAvgTime_Object = MibTableColumn
lspPingResultRoundTripAvgTime = _LspPingResultRoundTripAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 6),
    _LspPingResultRoundTripAvgTime_Type()
)
lspPingResultRoundTripAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundTripAvgTime.setStatus("current")
_LspPingResultEntryOwner_Type = DisplayString
_LspPingResultEntryOwner_Object = MibTableColumn
lspPingResultEntryOwner = _LspPingResultEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 9),
    _LspPingResultEntryOwner_Type()
)
lspPingResultEntryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultEntryOwner.setStatus("current")
_LspPingResultRoundWobbleMinTime_Type = Integer32
_LspPingResultRoundWobbleMinTime_Object = MibTableColumn
lspPingResultRoundWobbleMinTime = _LspPingResultRoundWobbleMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 10),
    _LspPingResultRoundWobbleMinTime_Type()
)
lspPingResultRoundWobbleMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundWobbleMinTime.setStatus("current")
_LspPingResultRoundWobbleMaxTime_Type = Integer32
_LspPingResultRoundWobbleMaxTime_Object = MibTableColumn
lspPingResultRoundWobbleMaxTime = _LspPingResultRoundWobbleMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 11),
    _LspPingResultRoundWobbleMaxTime_Type()
)
lspPingResultRoundWobbleMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundWobbleMaxTime.setStatus("current")
_LspPingResultRoundWobbleAvgTime_Type = Integer32
_LspPingResultRoundWobbleAvgTime_Object = MibTableColumn
lspPingResultRoundWobbleAvgTime = _LspPingResultRoundWobbleAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 2, 1, 12),
    _LspPingResultRoundWobbleAvgTime_Type()
)
lspPingResultRoundWobbleAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspPingResultRoundWobbleAvgTime.setStatus("current")
_LsppingNotifications_ObjectIdentity = ObjectIdentity
lsppingNotifications = _LsppingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 3)
)

# Managed Objects groups


# Notification objects

lsppingTrapResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 5, 3, 1)
)
lsppingTrapResult.setObjects(
      *(("ZXR10-LSPPING-MIB", "lspPingResultSerial"),
        ("ZXR10-LSPPING-MIB", "lspPingResultSentPkts"),
        ("ZXR10-LSPPING-MIB", "lspPingResultRcvPkts"),
        ("ZXR10-LSPPING-MIB", "lspPingResultRoundTripMinTime"),
        ("ZXR10-LSPPING-MIB", "lspPingResultRoundTripMaxTime"),
        ("ZXR10-LSPPING-MIB", "lspPingResultRoundTripAvgTime"))
)
if mibBuilder.loadTexts:
    lsppingTrapResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-LSPPING-MIB",
    **{"DisplayString": DisplayString,
       "zxr10LspPingMIB": zxr10LspPingMIB,
       "lspPingTable": lspPingTable,
       "lspPingEntry": lspPingEntry,
       "lspPingSerial": lspPingSerial,
       "lspPingType": lspPingType,
       "lspPingLdpPrefix": lspPingLdpPrefix,
       "lspPingLdpPrefixlen": lspPingLdpPrefixlen,
       "lspPingMplsTeTunnelIfName": lspPingMplsTeTunnelIfName,
       "lspPingAtomDesAddr": lspPingAtomDesAddr,
       "lspPingAtomVcid": lspPingAtomVcid,
       "lspPingIfOption": lspPingIfOption,
       "lspPingPacketCount": lspPingPacketCount,
       "lspPingTimeOut": lspPingTimeOut,
       "lspPingDataLen": lspPingDataLen,
       "lspPingTrapOncompletion": lspPingTrapOncompletion,
       "lspPingRosStatus": lspPingRosStatus,
       "lspPingEntryOwner": lspPingEntryOwner,
       "lspPingResultTable": lspPingResultTable,
       "lspPingResultEntry": lspPingResultEntry,
       "lspPingResultSerial": lspPingResultSerial,
       "lspPingResultSentPkts": lspPingResultSentPkts,
       "lspPingResultRcvPkts": lspPingResultRcvPkts,
       "lspPingResultRoundTripMinTime": lspPingResultRoundTripMinTime,
       "lspPingResultRoundTripMaxTime": lspPingResultRoundTripMaxTime,
       "lspPingResultRoundTripAvgTime": lspPingResultRoundTripAvgTime,
       "lspPingResultEntryOwner": lspPingResultEntryOwner,
       "lspPingResultRoundWobbleMinTime": lspPingResultRoundWobbleMinTime,
       "lspPingResultRoundWobbleMaxTime": lspPingResultRoundWobbleMaxTime,
       "lspPingResultRoundWobbleAvgTime": lspPingResultRoundWobbleAvgTime,
       "lsppingNotifications": lsppingNotifications,
       "lsppingTrapResult": lsppingTrapResult}
)
