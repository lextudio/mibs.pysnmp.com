# SNMP MIB module (DNOS-ISDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-ISDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:01 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fastPathIsdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39)
)
fastPathIsdp.setRevisions(
        ("2011-01-26 00:00",
         "2010-01-11 00:00",
         "2007-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentIsdpMIBObjects_ObjectIdentity = ObjectIdentity
agentIsdpMIBObjects = _AgentIsdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1)
)
_AgentIsdpGlobal_ObjectIdentity = ObjectIdentity
agentIsdpGlobal = _AgentIsdpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1)
)
_AgentIsdpClear_ObjectIdentity = ObjectIdentity
agentIsdpClear = _AgentIsdpClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1)
)


class _AgentIsdpClearStats_Type(Integer32):
    """Custom type agentIsdpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normalOperation", 0))
    )


_AgentIsdpClearStats_Type.__name__ = "Integer32"
_AgentIsdpClearStats_Object = MibScalar
agentIsdpClearStats = _AgentIsdpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 1),
    _AgentIsdpClearStats_Type()
)
agentIsdpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpClearStats.setStatus("current")


class _AgentIsdpClearEntries_Type(Integer32):
    """Custom type agentIsdpClearEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normalOperation", 0))
    )


_AgentIsdpClearEntries_Type.__name__ = "Integer32"
_AgentIsdpClearEntries_Object = MibScalar
agentIsdpClearEntries = _AgentIsdpClearEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 2),
    _AgentIsdpClearEntries_Type()
)
agentIsdpClearEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpClearEntries.setStatus("current")
_AgentIsdpStatistics_ObjectIdentity = ObjectIdentity
agentIsdpStatistics = _AgentIsdpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2)
)
_AgentIsdpStatisticsPduReceived_Type = Counter32
_AgentIsdpStatisticsPduReceived_Object = MibScalar
agentIsdpStatisticsPduReceived = _AgentIsdpStatisticsPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 1),
    _AgentIsdpStatisticsPduReceived_Type()
)
agentIsdpStatisticsPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsPduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsPduReceived.setUnits("packets")
_AgentIsdpStatisticsPduTransmit_Type = Counter32
_AgentIsdpStatisticsPduTransmit_Object = MibScalar
agentIsdpStatisticsPduTransmit = _AgentIsdpStatisticsPduTransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 2),
    _AgentIsdpStatisticsPduTransmit_Type()
)
agentIsdpStatisticsPduTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsPduTransmit.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsPduTransmit.setUnits("packets")
_AgentIsdpStatisticsV1PduReceived_Type = Counter32
_AgentIsdpStatisticsV1PduReceived_Object = MibScalar
agentIsdpStatisticsV1PduReceived = _AgentIsdpStatisticsV1PduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 3),
    _AgentIsdpStatisticsV1PduReceived_Type()
)
agentIsdpStatisticsV1PduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV1PduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV1PduReceived.setUnits("packets")
_AgentIsdpStatisticsV1PduTransmit_Type = Counter32
_AgentIsdpStatisticsV1PduTransmit_Object = MibScalar
agentIsdpStatisticsV1PduTransmit = _AgentIsdpStatisticsV1PduTransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 4),
    _AgentIsdpStatisticsV1PduTransmit_Type()
)
agentIsdpStatisticsV1PduTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV1PduTransmit.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV1PduTransmit.setUnits("packets")
_AgentIsdpStatisticsV2PduReceived_Type = Counter32
_AgentIsdpStatisticsV2PduReceived_Object = MibScalar
agentIsdpStatisticsV2PduReceived = _AgentIsdpStatisticsV2PduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 5),
    _AgentIsdpStatisticsV2PduReceived_Type()
)
agentIsdpStatisticsV2PduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV2PduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV2PduReceived.setUnits("packets")
_AgentIsdpStatisticsV2PduTransmit_Type = Counter32
_AgentIsdpStatisticsV2PduTransmit_Object = MibScalar
agentIsdpStatisticsV2PduTransmit = _AgentIsdpStatisticsV2PduTransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 6),
    _AgentIsdpStatisticsV2PduTransmit_Type()
)
agentIsdpStatisticsV2PduTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV2PduTransmit.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsV2PduTransmit.setUnits("packets")
_AgentIsdpStatisticsBadHeaderPduReceived_Type = Counter32
_AgentIsdpStatisticsBadHeaderPduReceived_Object = MibScalar
agentIsdpStatisticsBadHeaderPduReceived = _AgentIsdpStatisticsBadHeaderPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 7),
    _AgentIsdpStatisticsBadHeaderPduReceived_Type()
)
agentIsdpStatisticsBadHeaderPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsBadHeaderPduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsBadHeaderPduReceived.setUnits("packets")
_AgentIsdpStatisticsChkSumErrorPduReceived_Type = Counter32
_AgentIsdpStatisticsChkSumErrorPduReceived_Object = MibScalar
agentIsdpStatisticsChkSumErrorPduReceived = _AgentIsdpStatisticsChkSumErrorPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 8),
    _AgentIsdpStatisticsChkSumErrorPduReceived_Type()
)
agentIsdpStatisticsChkSumErrorPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsChkSumErrorPduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsChkSumErrorPduReceived.setUnits("packets")
_AgentIsdpStatisticsFailurePduTransmit_Type = Counter32
_AgentIsdpStatisticsFailurePduTransmit_Object = MibScalar
agentIsdpStatisticsFailurePduTransmit = _AgentIsdpStatisticsFailurePduTransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 9),
    _AgentIsdpStatisticsFailurePduTransmit_Type()
)
agentIsdpStatisticsFailurePduTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsFailurePduTransmit.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsFailurePduTransmit.setUnits("packets")
_AgentIsdpStatisticsInvalidFormatPduReceived_Type = Counter32
_AgentIsdpStatisticsInvalidFormatPduReceived_Object = MibScalar
agentIsdpStatisticsInvalidFormatPduReceived = _AgentIsdpStatisticsInvalidFormatPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 10),
    _AgentIsdpStatisticsInvalidFormatPduReceived_Type()
)
agentIsdpStatisticsInvalidFormatPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsInvalidFormatPduReceived.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsInvalidFormatPduReceived.setUnits("packets")
_AgentIsdpStatisticsTableFull_Type = Counter32
_AgentIsdpStatisticsTableFull_Object = MibScalar
agentIsdpStatisticsTableFull = _AgentIsdpStatisticsTableFull_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 11),
    _AgentIsdpStatisticsTableFull_Type()
)
agentIsdpStatisticsTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsTableFull.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsTableFull.setUnits("times")
_AgentIsdpStatisticsIpAddressTableFull_Type = Counter32
_AgentIsdpStatisticsIpAddressTableFull_Object = MibScalar
agentIsdpStatisticsIpAddressTableFull = _AgentIsdpStatisticsIpAddressTableFull_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 12),
    _AgentIsdpStatisticsIpAddressTableFull_Type()
)
agentIsdpStatisticsIpAddressTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpStatisticsIpAddressTableFull.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpStatisticsIpAddressTableFull.setUnits("times")


class _AgentIsdpGlobalRun_Type(Integer32):
    """Custom type agentIsdpGlobalRun based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentIsdpGlobalRun_Type.__name__ = "Integer32"
_AgentIsdpGlobalRun_Object = MibScalar
agentIsdpGlobalRun = _AgentIsdpGlobalRun_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 4),
    _AgentIsdpGlobalRun_Type()
)
agentIsdpGlobalRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpGlobalRun.setStatus("current")


class _AgentIsdpGlobalMessageInterval_Type(Integer32):
    """Custom type agentIsdpGlobalMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_AgentIsdpGlobalMessageInterval_Type.__name__ = "Integer32"
_AgentIsdpGlobalMessageInterval_Object = MibScalar
agentIsdpGlobalMessageInterval = _AgentIsdpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 5),
    _AgentIsdpGlobalMessageInterval_Type()
)
agentIsdpGlobalMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpGlobalMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpGlobalMessageInterval.setUnits("seconds")


class _AgentIsdpGlobalHoldTime_Type(Integer32):
    """Custom type agentIsdpGlobalHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_AgentIsdpGlobalHoldTime_Type.__name__ = "Integer32"
_AgentIsdpGlobalHoldTime_Object = MibScalar
agentIsdpGlobalHoldTime = _AgentIsdpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 6),
    _AgentIsdpGlobalHoldTime_Type()
)
agentIsdpGlobalHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpGlobalHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpGlobalHoldTime.setUnits("seconds")
_AgentIsdpGlobalDeviceId_Type = DisplayString
_AgentIsdpGlobalDeviceId_Object = MibScalar
agentIsdpGlobalDeviceId = _AgentIsdpGlobalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 7),
    _AgentIsdpGlobalDeviceId_Type()
)
agentIsdpGlobalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpGlobalDeviceId.setStatus("current")


class _AgentIsdpGlobalAdvertiseV2_Type(Integer32):
    """Custom type agentIsdpGlobalAdvertiseV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentIsdpGlobalAdvertiseV2_Type.__name__ = "Integer32"
_AgentIsdpGlobalAdvertiseV2_Object = MibScalar
agentIsdpGlobalAdvertiseV2 = _AgentIsdpGlobalAdvertiseV2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 8),
    _AgentIsdpGlobalAdvertiseV2_Type()
)
agentIsdpGlobalAdvertiseV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpGlobalAdvertiseV2.setStatus("current")


class _AgentIsdpGlobalDeviceIdFormatCpb_Type(Bits):
    """Custom type agentIsdpGlobalDeviceIdFormatCpb based on Bits"""
    namedValues = NamedValues(
        *(("hostName", 8),
          ("macAddress", 2),
          ("other", 4),
          ("serialNumber", 1))
    )

_AgentIsdpGlobalDeviceIdFormatCpb_Type.__name__ = "Bits"
_AgentIsdpGlobalDeviceIdFormatCpb_Object = MibScalar
agentIsdpGlobalDeviceIdFormatCpb = _AgentIsdpGlobalDeviceIdFormatCpb_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 9),
    _AgentIsdpGlobalDeviceIdFormatCpb_Type()
)
agentIsdpGlobalDeviceIdFormatCpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpGlobalDeviceIdFormatCpb.setStatus("current")


class _AgentIsdpGlobalDeviceIdFormat_Type(Integer32):
    """Custom type agentIsdpGlobalDeviceIdFormat based on Integer32"""
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
        *(("hostName", 4),
          ("macAddress", 2),
          ("other", 3),
          ("serialNumber", 1))
    )


_AgentIsdpGlobalDeviceIdFormat_Type.__name__ = "Integer32"
_AgentIsdpGlobalDeviceIdFormat_Object = MibScalar
agentIsdpGlobalDeviceIdFormat = _AgentIsdpGlobalDeviceIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 10),
    _AgentIsdpGlobalDeviceIdFormat_Type()
)
agentIsdpGlobalDeviceIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpGlobalDeviceIdFormat.setStatus("current")
_AgentIsdpCache_ObjectIdentity = ObjectIdentity
agentIsdpCache = _AgentIsdpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2)
)
_AgentIsdpCacheTable_Object = MibTable
agentIsdpCacheTable = _AgentIsdpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentIsdpCacheTable.setStatus("current")
_AgentIsdpCacheEntry_Object = MibTableRow
agentIsdpCacheEntry = _AgentIsdpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1)
)
agentIsdpCacheEntry.setIndexNames(
    (0, "DNOS-ISDP-MIB", "agentIsdpCacheIfIndex"),
    (0, "DNOS-ISDP-MIB", "agentIsdpCacheIndex"),
)
if mibBuilder.loadTexts:
    agentIsdpCacheEntry.setStatus("current")


class _AgentIsdpCacheIfIndex_Type(Integer32):
    """Custom type agentIsdpCacheIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentIsdpCacheIfIndex_Type.__name__ = "Integer32"
_AgentIsdpCacheIfIndex_Object = MibTableColumn
agentIsdpCacheIfIndex = _AgentIsdpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 1),
    _AgentIsdpCacheIfIndex_Type()
)
agentIsdpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIsdpCacheIfIndex.setStatus("current")


class _AgentIsdpCacheIndex_Type(Integer32):
    """Custom type agentIsdpCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentIsdpCacheIndex_Type.__name__ = "Integer32"
_AgentIsdpCacheIndex_Object = MibTableColumn
agentIsdpCacheIndex = _AgentIsdpCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 2),
    _AgentIsdpCacheIndex_Type()
)
agentIsdpCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIsdpCacheIndex.setStatus("current")
_AgentIsdpCacheAddress_Type = DisplayString
_AgentIsdpCacheAddress_Object = MibTableColumn
agentIsdpCacheAddress = _AgentIsdpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 3),
    _AgentIsdpCacheAddress_Type()
)
agentIsdpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheAddress.setStatus("current")
_AgentIsdpCacheLocalIntf_Type = DisplayString
_AgentIsdpCacheLocalIntf_Object = MibTableColumn
agentIsdpCacheLocalIntf = _AgentIsdpCacheLocalIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 4),
    _AgentIsdpCacheLocalIntf_Type()
)
agentIsdpCacheLocalIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheLocalIntf.setStatus("current")
_AgentIsdpCacheVersion_Type = DisplayString
_AgentIsdpCacheVersion_Object = MibTableColumn
agentIsdpCacheVersion = _AgentIsdpCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 5),
    _AgentIsdpCacheVersion_Type()
)
agentIsdpCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheVersion.setStatus("current")
_AgentIsdpCacheDeviceId_Type = DisplayString
_AgentIsdpCacheDeviceId_Object = MibTableColumn
agentIsdpCacheDeviceId = _AgentIsdpCacheDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 6),
    _AgentIsdpCacheDeviceId_Type()
)
agentIsdpCacheDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheDeviceId.setStatus("current")
_AgentIsdpCacheDevicePort_Type = DisplayString
_AgentIsdpCacheDevicePort_Object = MibTableColumn
agentIsdpCacheDevicePort = _AgentIsdpCacheDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 7),
    _AgentIsdpCacheDevicePort_Type()
)
agentIsdpCacheDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheDevicePort.setStatus("current")
_AgentIsdpCachePlatform_Type = DisplayString
_AgentIsdpCachePlatform_Object = MibTableColumn
agentIsdpCachePlatform = _AgentIsdpCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 8),
    _AgentIsdpCachePlatform_Type()
)
agentIsdpCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCachePlatform.setStatus("current")
_AgentIsdpCacheCapabilities_Type = DisplayString
_AgentIsdpCacheCapabilities_Object = MibTableColumn
agentIsdpCacheCapabilities = _AgentIsdpCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 9),
    _AgentIsdpCacheCapabilities_Type()
)
agentIsdpCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheCapabilities.setStatus("current")
_AgentIsdpCacheLastChange_Type = TimeStamp
_AgentIsdpCacheLastChange_Object = MibTableColumn
agentIsdpCacheLastChange = _AgentIsdpCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 10),
    _AgentIsdpCacheLastChange_Type()
)
agentIsdpCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheLastChange.setStatus("current")
_AgentIsdpCacheProtocolVersion_Type = DisplayString
_AgentIsdpCacheProtocolVersion_Object = MibTableColumn
agentIsdpCacheProtocolVersion = _AgentIsdpCacheProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 11),
    _AgentIsdpCacheProtocolVersion_Type()
)
agentIsdpCacheProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheProtocolVersion.setStatus("current")


class _AgentIsdpCacheHoldtime_Type(Integer32):
    """Custom type agentIsdpCacheHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_AgentIsdpCacheHoldtime_Type.__name__ = "Integer32"
_AgentIsdpCacheHoldtime_Object = MibTableColumn
agentIsdpCacheHoldtime = _AgentIsdpCacheHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 12),
    _AgentIsdpCacheHoldtime_Type()
)
agentIsdpCacheHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIsdpCacheHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    agentIsdpCacheHoldtime.setUnits("seconds")
_AgentIsdpInterface_ObjectIdentity = ObjectIdentity
agentIsdpInterface = _AgentIsdpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3)
)
_AgentIsdpInterfaceTable_Object = MibTable
agentIsdpInterfaceTable = _AgentIsdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agentIsdpInterfaceTable.setStatus("current")
_AgentIsdpInterfaceEntry_Object = MibTableRow
agentIsdpInterfaceEntry = _AgentIsdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1)
)
agentIsdpInterfaceEntry.setIndexNames(
    (0, "DNOS-ISDP-MIB", "agentIsdpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentIsdpInterfaceEntry.setStatus("current")


class _AgentIsdpInterfaceIfIndex_Type(Integer32):
    """Custom type agentIsdpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentIsdpInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentIsdpInterfaceIfIndex_Object = MibTableColumn
agentIsdpInterfaceIfIndex = _AgentIsdpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 1),
    _AgentIsdpInterfaceIfIndex_Type()
)
agentIsdpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIsdpInterfaceIfIndex.setStatus("current")


class _AgentIsdpInterfaceEnable_Type(Integer32):
    """Custom type agentIsdpInterfaceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentIsdpInterfaceEnable_Type.__name__ = "Integer32"
_AgentIsdpInterfaceEnable_Object = MibTableColumn
agentIsdpInterfaceEnable = _AgentIsdpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 2),
    _AgentIsdpInterfaceEnable_Type()
)
agentIsdpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIsdpInterfaceEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-ISDP-MIB",
    **{"fastPathIsdp": fastPathIsdp,
       "agentIsdpMIBObjects": agentIsdpMIBObjects,
       "agentIsdpGlobal": agentIsdpGlobal,
       "agentIsdpClear": agentIsdpClear,
       "agentIsdpClearStats": agentIsdpClearStats,
       "agentIsdpClearEntries": agentIsdpClearEntries,
       "agentIsdpStatistics": agentIsdpStatistics,
       "agentIsdpStatisticsPduReceived": agentIsdpStatisticsPduReceived,
       "agentIsdpStatisticsPduTransmit": agentIsdpStatisticsPduTransmit,
       "agentIsdpStatisticsV1PduReceived": agentIsdpStatisticsV1PduReceived,
       "agentIsdpStatisticsV1PduTransmit": agentIsdpStatisticsV1PduTransmit,
       "agentIsdpStatisticsV2PduReceived": agentIsdpStatisticsV2PduReceived,
       "agentIsdpStatisticsV2PduTransmit": agentIsdpStatisticsV2PduTransmit,
       "agentIsdpStatisticsBadHeaderPduReceived": agentIsdpStatisticsBadHeaderPduReceived,
       "agentIsdpStatisticsChkSumErrorPduReceived": agentIsdpStatisticsChkSumErrorPduReceived,
       "agentIsdpStatisticsFailurePduTransmit": agentIsdpStatisticsFailurePduTransmit,
       "agentIsdpStatisticsInvalidFormatPduReceived": agentIsdpStatisticsInvalidFormatPduReceived,
       "agentIsdpStatisticsTableFull": agentIsdpStatisticsTableFull,
       "agentIsdpStatisticsIpAddressTableFull": agentIsdpStatisticsIpAddressTableFull,
       "agentIsdpGlobalRun": agentIsdpGlobalRun,
       "agentIsdpGlobalMessageInterval": agentIsdpGlobalMessageInterval,
       "agentIsdpGlobalHoldTime": agentIsdpGlobalHoldTime,
       "agentIsdpGlobalDeviceId": agentIsdpGlobalDeviceId,
       "agentIsdpGlobalAdvertiseV2": agentIsdpGlobalAdvertiseV2,
       "agentIsdpGlobalDeviceIdFormatCpb": agentIsdpGlobalDeviceIdFormatCpb,
       "agentIsdpGlobalDeviceIdFormat": agentIsdpGlobalDeviceIdFormat,
       "agentIsdpCache": agentIsdpCache,
       "agentIsdpCacheTable": agentIsdpCacheTable,
       "agentIsdpCacheEntry": agentIsdpCacheEntry,
       "agentIsdpCacheIfIndex": agentIsdpCacheIfIndex,
       "agentIsdpCacheIndex": agentIsdpCacheIndex,
       "agentIsdpCacheAddress": agentIsdpCacheAddress,
       "agentIsdpCacheLocalIntf": agentIsdpCacheLocalIntf,
       "agentIsdpCacheVersion": agentIsdpCacheVersion,
       "agentIsdpCacheDeviceId": agentIsdpCacheDeviceId,
       "agentIsdpCacheDevicePort": agentIsdpCacheDevicePort,
       "agentIsdpCachePlatform": agentIsdpCachePlatform,
       "agentIsdpCacheCapabilities": agentIsdpCacheCapabilities,
       "agentIsdpCacheLastChange": agentIsdpCacheLastChange,
       "agentIsdpCacheProtocolVersion": agentIsdpCacheProtocolVersion,
       "agentIsdpCacheHoldtime": agentIsdpCacheHoldtime,
       "agentIsdpInterface": agentIsdpInterface,
       "agentIsdpInterfaceTable": agentIsdpInterfaceTable,
       "agentIsdpInterfaceEntry": agentIsdpInterfaceEntry,
       "agentIsdpInterfaceIfIndex": agentIsdpInterfaceIfIndex,
       "agentIsdpInterfaceEnable": agentIsdpInterfaceEnable}
)
