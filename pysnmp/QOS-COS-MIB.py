# SNMP MIB module (QOS-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOS-COS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:59 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(qos,) = mibBuilder.importSymbols(
    "QOS-MIB",
    "qos")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PercentByFives(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(85, 85),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(95, 95),
        ValueRangeConstraint(100, 100),
    )



class Percent(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class Sixteenths(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AgentCosMapCfgGroup_ObjectIdentity = ObjectIdentity
agentCosMapCfgGroup = _AgentCosMapCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1)
)
_AgentCosMapIpDscpTable_Object = MibTable
agentCosMapIpDscpTable = _AgentCosMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    agentCosMapIpDscpTable.setStatus("current")
_AgentCosMapIpDscpEntry_Object = MibTableRow
agentCosMapIpDscpEntry = _AgentCosMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 2, 1)
)
agentCosMapIpDscpEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosMapIpDscpIntfIndex"),
    (0, "QOS-COS-MIB", "agentCosMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    agentCosMapIpDscpEntry.setStatus("current")
_AgentCosMapIpDscpIntfIndex_Type = InterfaceIndexOrZero
_AgentCosMapIpDscpIntfIndex_Object = MibTableColumn
agentCosMapIpDscpIntfIndex = _AgentCosMapIpDscpIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 2, 1, 1),
    _AgentCosMapIpDscpIntfIndex_Type()
)
agentCosMapIpDscpIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosMapIpDscpIntfIndex.setStatus("current")


class _AgentCosMapIpDscpValue_Type(Unsigned32):
    """Custom type agentCosMapIpDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentCosMapIpDscpValue_Type.__name__ = "Unsigned32"
_AgentCosMapIpDscpValue_Object = MibTableColumn
agentCosMapIpDscpValue = _AgentCosMapIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 2, 1, 2),
    _AgentCosMapIpDscpValue_Type()
)
agentCosMapIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosMapIpDscpValue.setStatus("current")


class _AgentCosMapIpDscpTrafficClass_Type(Unsigned32):
    """Custom type agentCosMapIpDscpTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentCosMapIpDscpTrafficClass_Type.__name__ = "Unsigned32"
_AgentCosMapIpDscpTrafficClass_Object = MibTableColumn
agentCosMapIpDscpTrafficClass = _AgentCosMapIpDscpTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 2, 1, 3),
    _AgentCosMapIpDscpTrafficClass_Type()
)
agentCosMapIpDscpTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosMapIpDscpTrafficClass.setStatus("current")
_AgentCosMapIntfTrustTable_Object = MibTable
agentCosMapIntfTrustTable = _AgentCosMapIntfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    agentCosMapIntfTrustTable.setStatus("current")
_AgentCosMapIntfTrustEntry_Object = MibTableRow
agentCosMapIntfTrustEntry = _AgentCosMapIntfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 3, 1)
)
agentCosMapIntfTrustEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosMapIntfTrustIntfIndex"),
)
if mibBuilder.loadTexts:
    agentCosMapIntfTrustEntry.setStatus("current")
_AgentCosMapIntfTrustIntfIndex_Type = InterfaceIndexOrZero
_AgentCosMapIntfTrustIntfIndex_Object = MibTableColumn
agentCosMapIntfTrustIntfIndex = _AgentCosMapIntfTrustIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 3, 1, 1),
    _AgentCosMapIntfTrustIntfIndex_Type()
)
agentCosMapIntfTrustIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosMapIntfTrustIntfIndex.setStatus("current")


class _AgentCosMapIntfTrustMode_Type(Integer32):
    """Custom type agentCosMapIntfTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("trustDot1p", 2),
          ("trustIpDscp", 4),
          ("untrusted", 1))
    )


_AgentCosMapIntfTrustMode_Type.__name__ = "Integer32"
_AgentCosMapIntfTrustMode_Object = MibTableColumn
agentCosMapIntfTrustMode = _AgentCosMapIntfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 3, 1, 2),
    _AgentCosMapIntfTrustMode_Type()
)
agentCosMapIntfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosMapIntfTrustMode.setStatus("current")
_AgentCosMapUntrustedTrafficClass_Type = Unsigned32
_AgentCosMapUntrustedTrafficClass_Object = MibTableColumn
agentCosMapUntrustedTrafficClass = _AgentCosMapUntrustedTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 1, 3, 1, 3),
    _AgentCosMapUntrustedTrafficClass_Type()
)
agentCosMapUntrustedTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosMapUntrustedTrafficClass.setStatus("current")
_AgentCosQueueCfgGroup_ObjectIdentity = ObjectIdentity
agentCosQueueCfgGroup = _AgentCosQueueCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2)
)
_AgentCosQueueNumQueuesPerPort_Type = Unsigned32
_AgentCosQueueNumQueuesPerPort_Object = MibScalar
agentCosQueueNumQueuesPerPort = _AgentCosQueueNumQueuesPerPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 1),
    _AgentCosQueueNumQueuesPerPort_Type()
)
agentCosQueueNumQueuesPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueNumQueuesPerPort.setStatus("current")
_AgentCosQueueNumDropPrecedenceLevels_Type = Unsigned32
_AgentCosQueueNumDropPrecedenceLevels_Object = MibScalar
agentCosQueueNumDropPrecedenceLevels = _AgentCosQueueNumDropPrecedenceLevels_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 2),
    _AgentCosQueueNumDropPrecedenceLevels_Type()
)
agentCosQueueNumDropPrecedenceLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueNumDropPrecedenceLevels.setStatus("current")
_AgentCosQueueControlTable_Object = MibTable
agentCosQueueControlTable = _AgentCosQueueControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    agentCosQueueControlTable.setStatus("current")
_AgentCosQueueControlEntry_Object = MibTableRow
agentCosQueueControlEntry = _AgentCosQueueControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1)
)
agentCosQueueControlEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueIntfIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueControlEntry.setStatus("current")
_AgentCosQueueIntfIndex_Type = InterfaceIndexOrZero
_AgentCosQueueIntfIndex_Object = MibTableColumn
agentCosQueueIntfIndex = _AgentCosQueueIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 1),
    _AgentCosQueueIntfIndex_Type()
)
agentCosQueueIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosQueueIntfIndex.setStatus("current")


class _AgentCosQueueIntfShapingRate_Type(Percent):
    """Custom type agentCosQueueIntfShapingRate based on Percent"""
    defaultValue = 0


_AgentCosQueueIntfShapingRate_Object = MibTableColumn
agentCosQueueIntfShapingRate = _AgentCosQueueIntfShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 2),
    _AgentCosQueueIntfShapingRate_Type()
)
agentCosQueueIntfShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueIntfShapingRate.setStatus("current")


class _AgentCosQueueMgmtTypeIntf_Type(Integer32):
    """Custom type agentCosQueueMgmtTypeIntf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("taildrop", 1),
          ("wred", 2))
    )


_AgentCosQueueMgmtTypeIntf_Type.__name__ = "Integer32"
_AgentCosQueueMgmtTypeIntf_Object = MibTableColumn
agentCosQueueMgmtTypeIntf = _AgentCosQueueMgmtTypeIntf_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 3),
    _AgentCosQueueMgmtTypeIntf_Type()
)
agentCosQueueMgmtTypeIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtTypeIntf.setStatus("deprecated")


class _AgentCosQueueWredDecayExponent_Type(Unsigned32):
    """Custom type agentCosQueueWredDecayExponent based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AgentCosQueueWredDecayExponent_Type.__name__ = "Unsigned32"
_AgentCosQueueWredDecayExponent_Object = MibTableColumn
agentCosQueueWredDecayExponent = _AgentCosQueueWredDecayExponent_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 4),
    _AgentCosQueueWredDecayExponent_Type()
)
agentCosQueueWredDecayExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueWredDecayExponent.setStatus("current")


class _AgentCosQueueDefaultsRestore_Type(Integer32):
    """Custom type agentCosQueueDefaultsRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueDefaultsRestore_Type.__name__ = "Integer32"
_AgentCosQueueDefaultsRestore_Object = MibTableColumn
agentCosQueueDefaultsRestore = _AgentCosQueueDefaultsRestore_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 5),
    _AgentCosQueueDefaultsRestore_Type()
)
agentCosQueueDefaultsRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueDefaultsRestore.setStatus("current")


class _AgentCosQueueIntfShapingRateUnits_Type(Integer32):
    """Custom type agentCosQueueIntfShapingRateUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("percent", 1))
    )


_AgentCosQueueIntfShapingRateUnits_Type.__name__ = "Integer32"
_AgentCosQueueIntfShapingRateUnits_Object = MibTableColumn
agentCosQueueIntfShapingRateUnits = _AgentCosQueueIntfShapingRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 3, 1, 6),
    _AgentCosQueueIntfShapingRateUnits_Type()
)
agentCosQueueIntfShapingRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueIntfShapingRateUnits.setStatus("current")
_AgentCosQueueTable_Object = MibTable
agentCosQueueTable = _AgentCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    agentCosQueueTable.setStatus("current")
_AgentCosQueueEntry_Object = MibTableRow
agentCosQueueEntry = _AgentCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1)
)
agentCosQueueEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueIntfIndex"),
    (0, "QOS-COS-MIB", "agentCosQueueIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueEntry.setStatus("current")
_AgentCosQueueIndex_Type = Unsigned32
_AgentCosQueueIndex_Object = MibTableColumn
agentCosQueueIndex = _AgentCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1, 1),
    _AgentCosQueueIndex_Type()
)
agentCosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosQueueIndex.setStatus("current")


class _AgentCosQueueSchedulerType_Type(Integer32):
    """Custom type agentCosQueueSchedulerType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("weighted", 2))
    )


_AgentCosQueueSchedulerType_Type.__name__ = "Integer32"
_AgentCosQueueSchedulerType_Object = MibTableColumn
agentCosQueueSchedulerType = _AgentCosQueueSchedulerType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1, 2),
    _AgentCosQueueSchedulerType_Type()
)
agentCosQueueSchedulerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueSchedulerType.setStatus("current")


class _AgentCosQueueMinBandwidth_Type(Percent):
    """Custom type agentCosQueueMinBandwidth based on Percent"""
    defaultValue = 0


_AgentCosQueueMinBandwidth_Object = MibTableColumn
agentCosQueueMinBandwidth = _AgentCosQueueMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1, 3),
    _AgentCosQueueMinBandwidth_Type()
)
agentCosQueueMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMinBandwidth.setStatus("current")


class _AgentCosQueueMaxBandwidth_Type(Percent):
    """Custom type agentCosQueueMaxBandwidth based on Percent"""
    defaultValue = 0


_AgentCosQueueMaxBandwidth_Object = MibTableColumn
agentCosQueueMaxBandwidth = _AgentCosQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1, 4),
    _AgentCosQueueMaxBandwidth_Type()
)
agentCosQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMaxBandwidth.setStatus("deprecated")


class _AgentCosQueueMgmtType_Type(Integer32):
    """Custom type agentCosQueueMgmtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("taildrop", 1),
          ("wred", 2))
    )


_AgentCosQueueMgmtType_Type.__name__ = "Integer32"
_AgentCosQueueMgmtType_Object = MibTableColumn
agentCosQueueMgmtType = _AgentCosQueueMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 4, 1, 5),
    _AgentCosQueueMgmtType_Type()
)
agentCosQueueMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtType.setStatus("current")
_AgentCosQueueMgmtTable_Object = MibTable
agentCosQueueMgmtTable = _AgentCosQueueMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    agentCosQueueMgmtTable.setStatus("current")
_AgentCosQueueMgmtEntry_Object = MibTableRow
agentCosQueueMgmtEntry = _AgentCosQueueMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1)
)
agentCosQueueMgmtEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueIntfIndex"),
    (0, "QOS-COS-MIB", "agentCosQueueIndex"),
    (0, "QOS-COS-MIB", "agentCosQueueDropPrecIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueMgmtEntry.setStatus("current")
_AgentCosQueueDropPrecIndex_Type = Unsigned32
_AgentCosQueueDropPrecIndex_Object = MibTableColumn
agentCosQueueDropPrecIndex = _AgentCosQueueDropPrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 1),
    _AgentCosQueueDropPrecIndex_Type()
)
agentCosQueueDropPrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosQueueDropPrecIndex.setStatus("current")
_AgentCosQueueMgmtTailDropThreshold_Type = Sixteenths
_AgentCosQueueMgmtTailDropThreshold_Object = MibTableColumn
agentCosQueueMgmtTailDropThreshold = _AgentCosQueueMgmtTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 2),
    _AgentCosQueueMgmtTailDropThreshold_Type()
)
agentCosQueueMgmtTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtTailDropThreshold.setStatus("obsolete")
_AgentCosQueueMgmtWredMinThreshold_Type = Sixteenths
_AgentCosQueueMgmtWredMinThreshold_Object = MibTableColumn
agentCosQueueMgmtWredMinThreshold = _AgentCosQueueMgmtWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 3),
    _AgentCosQueueMgmtWredMinThreshold_Type()
)
agentCosQueueMgmtWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredMinThreshold.setStatus("obsolete")
_AgentCosQueueMgmtWredMaxThreshold_Type = Sixteenths
_AgentCosQueueMgmtWredMaxThreshold_Object = MibTableColumn
agentCosQueueMgmtWredMaxThreshold = _AgentCosQueueMgmtWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 4),
    _AgentCosQueueMgmtWredMaxThreshold_Type()
)
agentCosQueueMgmtWredMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredMaxThreshold.setStatus("obsolete")


class _AgentCosQueueMgmtWredDropProbScale_Type(Unsigned32):
    """Custom type agentCosQueueMgmtWredDropProbScale based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentCosQueueMgmtWredDropProbScale_Type.__name__ = "Unsigned32"
_AgentCosQueueMgmtWredDropProbScale_Object = MibTableColumn
agentCosQueueMgmtWredDropProbScale = _AgentCosQueueMgmtWredDropProbScale_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 5),
    _AgentCosQueueMgmtWredDropProbScale_Type()
)
agentCosQueueMgmtWredDropProbScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredDropProbScale.setStatus("obsolete")
_AgentCosQueueMgmtPercentTailDropThreshold_Type = Percent
_AgentCosQueueMgmtPercentTailDropThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentTailDropThreshold = _AgentCosQueueMgmtPercentTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 6),
    _AgentCosQueueMgmtPercentTailDropThreshold_Type()
)
agentCosQueueMgmtPercentTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtPercentTailDropThreshold.setStatus("current")
_AgentCosQueueMgmtPercentWredMinThreshold_Type = Percent
_AgentCosQueueMgmtPercentWredMinThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentWredMinThreshold = _AgentCosQueueMgmtPercentWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 7),
    _AgentCosQueueMgmtPercentWredMinThreshold_Type()
)
agentCosQueueMgmtPercentWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtPercentWredMinThreshold.setStatus("current")
_AgentCosQueueMgmtPercentWredMaxThreshold_Type = Percent
_AgentCosQueueMgmtPercentWredMaxThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentWredMaxThreshold = _AgentCosQueueMgmtPercentWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 8),
    _AgentCosQueueMgmtPercentWredMaxThreshold_Type()
)
agentCosQueueMgmtPercentWredMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtPercentWredMaxThreshold.setStatus("current")


class _AgentCosQueueMgmtWredDropProbability_Type(Percent):
    """Custom type agentCosQueueMgmtWredDropProbability based on Percent"""
    defaultValue = 10


_AgentCosQueueMgmtWredDropProbability_Object = MibTableColumn
agentCosQueueMgmtWredDropProbability = _AgentCosQueueMgmtWredDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 5, 1, 9),
    _AgentCosQueueMgmtWredDropProbability_Type()
)
agentCosQueueMgmtWredDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredDropProbability.setStatus("current")
_AgentCosQueueETSControlTable_Object = MibTable
agentCosQueueETSControlTable = _AgentCosQueueETSControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    agentCosQueueETSControlTable.setStatus("current")
_AgentCosQueueETSControlEntry_Object = MibTableRow
agentCosQueueETSControlEntry = _AgentCosQueueETSControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1)
)
agentCosQueueETSControlEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueETSIntfIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueETSControlEntry.setStatus("current")
_AgentCosQueueETSIntfIndex_Type = InterfaceIndexOrZero
_AgentCosQueueETSIntfIndex_Object = MibTableColumn
agentCosQueueETSIntfIndex = _AgentCosQueueETSIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1, 1),
    _AgentCosQueueETSIntfIndex_Type()
)
agentCosQueueETSIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueETSIntfIndex.setStatus("current")


class _AgentCosQueueETSAdminMode_Type(Integer32):
    """Custom type agentCosQueueETSAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueETSAdminMode_Type.__name__ = "Integer32"
_AgentCosQueueETSAdminMode_Object = MibTableColumn
agentCosQueueETSAdminMode = _AgentCosQueueETSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1, 2),
    _AgentCosQueueETSAdminMode_Type()
)
agentCosQueueETSAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueETSAdminMode.setStatus("current")


class _AgentCosQueueETSSchedulerType_Type(Integer32):
    """Custom type agentCosQueueETSSchedulerType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("werr", 2),
          ("wrr", 1))
    )


_AgentCosQueueETSSchedulerType_Type.__name__ = "Integer32"
_AgentCosQueueETSSchedulerType_Object = MibTableColumn
agentCosQueueETSSchedulerType = _AgentCosQueueETSSchedulerType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1, 3),
    _AgentCosQueueETSSchedulerType_Type()
)
agentCosQueueETSSchedulerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueETSSchedulerType.setStatus("current")


class _AgentCosQueueETSLanWeight_Type(Unsigned32):
    """Custom type agentCosQueueETSLanWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AgentCosQueueETSLanWeight_Type.__name__ = "Unsigned32"
_AgentCosQueueETSLanWeight_Object = MibTableColumn
agentCosQueueETSLanWeight = _AgentCosQueueETSLanWeight_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1, 4),
    _AgentCosQueueETSLanWeight_Type()
)
agentCosQueueETSLanWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueETSLanWeight.setStatus("current")


class _AgentCosQueueETSSanWeight_Type(Unsigned32):
    """Custom type agentCosQueueETSSanWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AgentCosQueueETSSanWeight_Type.__name__ = "Unsigned32"
_AgentCosQueueETSSanWeight_Object = MibTableColumn
agentCosQueueETSSanWeight = _AgentCosQueueETSSanWeight_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 6, 1, 5),
    _AgentCosQueueETSSanWeight_Type()
)
agentCosQueueETSSanWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueETSSanWeight.setStatus("current")
_AgentCosQueueETSTable_Object = MibTable
agentCosQueueETSTable = _AgentCosQueueETSTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 7)
)
if mibBuilder.loadTexts:
    agentCosQueueETSTable.setStatus("current")
_AgentCosQueueETSEntry_Object = MibTableRow
agentCosQueueETSEntry = _AgentCosQueueETSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 7, 1)
)
agentCosQueueETSEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueETSifIndex"),
    (0, "QOS-COS-MIB", "agentCosQueueETSIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueETSEntry.setStatus("current")
_AgentCosQueueETSifIndex_Type = InterfaceIndexOrZero
_AgentCosQueueETSifIndex_Object = MibTableColumn
agentCosQueueETSifIndex = _AgentCosQueueETSifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 7, 1, 1),
    _AgentCosQueueETSifIndex_Type()
)
agentCosQueueETSifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueETSifIndex.setStatus("current")
_AgentCosQueueETSIndex_Type = Unsigned32
_AgentCosQueueETSIndex_Object = MibTableColumn
agentCosQueueETSIndex = _AgentCosQueueETSIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 7, 1, 2),
    _AgentCosQueueETSIndex_Type()
)
agentCosQueueETSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueETSIndex.setStatus("current")


class _AgentCosQueueETSPgMapping_Type(Integer32):
    """Custom type agentCosQueueETSPgMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipc", 3),
          ("lan", 1),
          ("san", 2))
    )


_AgentCosQueueETSPgMapping_Type.__name__ = "Integer32"
_AgentCosQueueETSPgMapping_Object = MibTableColumn
agentCosQueueETSPgMapping = _AgentCosQueueETSPgMapping_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 7, 1, 3),
    _AgentCosQueueETSPgMapping_Type()
)
agentCosQueueETSPgMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueETSPgMapping.setStatus("current")
_AgentCosQueueCNGroup_ObjectIdentity = ObjectIdentity
agentCosQueueCNGroup = _AgentCosQueueCNGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8)
)


class _AgentCosQueueCNAdminMode_Type(Integer32):
    """Custom type agentCosQueueCNAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueCNAdminMode_Type.__name__ = "Integer32"
_AgentCosQueueCNAdminMode_Object = MibScalar
agentCosQueueCNAdminMode = _AgentCosQueueCNAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 1),
    _AgentCosQueueCNAdminMode_Type()
)
agentCosQueueCNAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNAdminMode.setStatus("current")


class _AgentCosQueueCNTagEtherTypeRecognize_Type(Integer32):
    """Custom type agentCosQueueCNTagEtherTypeRecognize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueCNTagEtherTypeRecognize_Type.__name__ = "Integer32"
_AgentCosQueueCNTagEtherTypeRecognize_Object = MibScalar
agentCosQueueCNTagEtherTypeRecognize = _AgentCosQueueCNTagEtherTypeRecognize_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 2),
    _AgentCosQueueCNTagEtherTypeRecognize_Type()
)
agentCosQueueCNTagEtherTypeRecognize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNTagEtherTypeRecognize.setStatus("current")


class _AgentCosQueueCNTagEtherTypeValue_Type(Unsigned32):
    """Custom type agentCosQueueCNTagEtherTypeValue based on Unsigned32"""
    defaultValue = 8937

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentCosQueueCNTagEtherTypeValue_Type.__name__ = "Unsigned32"
_AgentCosQueueCNTagEtherTypeValue_Object = MibScalar
agentCosQueueCNTagEtherTypeValue = _AgentCosQueueCNTagEtherTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 3),
    _AgentCosQueueCNTagEtherTypeValue_Type()
)
agentCosQueueCNTagEtherTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNTagEtherTypeValue.setStatus("current")


class _AgentCosQueueCNMsgEtherTypeValue_Type(Unsigned32):
    """Custom type agentCosQueueCNMsgEtherTypeValue based on Unsigned32"""
    defaultValue = 8935

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentCosQueueCNMsgEtherTypeValue_Type.__name__ = "Unsigned32"
_AgentCosQueueCNMsgEtherTypeValue_Object = MibScalar
agentCosQueueCNMsgEtherTypeValue = _AgentCosQueueCNMsgEtherTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 4),
    _AgentCosQueueCNMsgEtherTypeValue_Type()
)
agentCosQueueCNMsgEtherTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNMsgEtherTypeValue.setStatus("current")


class _AgentCosQueueCNCPIDDevId_Type(Unsigned32):
    """Custom type agentCosQueueCNCPIDDevId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AgentCosQueueCNCPIDDevId_Type.__name__ = "Unsigned32"
_AgentCosQueueCNCPIDDevId_Object = MibScalar
agentCosQueueCNCPIDDevId = _AgentCosQueueCNCPIDDevId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 5),
    _AgentCosQueueCNCPIDDevId_Type()
)
agentCosQueueCNCPIDDevId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNCPIDDevId.setStatus("current")


class _AgentCosQueueCNCPIDLSBMode_Type(Integer32):
    """Custom type agentCosQueueCNCPIDLSBMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpIndex", 1),
          ("qNo", 2))
    )


_AgentCosQueueCNCPIDLSBMode_Type.__name__ = "Integer32"
_AgentCosQueueCNCPIDLSBMode_Object = MibScalar
agentCosQueueCNCPIDLSBMode = _AgentCosQueueCNCPIDLSBMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 6),
    _AgentCosQueueCNCPIDLSBMode_Type()
)
agentCosQueueCNCPIDLSBMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNCPIDLSBMode.setStatus("current")


class _AgentCosQueueCNOuterCFIBits_Type(Integer32):
    """Custom type agentCosQueueCNOuterCFIBits based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_AgentCosQueueCNOuterCFIBits_Type.__name__ = "Integer32"
_AgentCosQueueCNOuterCFIBits_Object = MibScalar
agentCosQueueCNOuterCFIBits = _AgentCosQueueCNOuterCFIBits_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 7),
    _AgentCosQueueCNOuterCFIBits_Type()
)
agentCosQueueCNOuterCFIBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNOuterCFIBits.setStatus("current")


class _AgentCosQueueCNOuterDot1pBits_Type(Integer32):
    """Custom type agentCosQueueCNOuterDot1pBits based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AgentCosQueueCNOuterDot1pBits_Type.__name__ = "Integer32"
_AgentCosQueueCNOuterDot1pBits_Object = MibScalar
agentCosQueueCNOuterDot1pBits = _AgentCosQueueCNOuterDot1pBits_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 8),
    _AgentCosQueueCNOuterDot1pBits_Type()
)
agentCosQueueCNOuterDot1pBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNOuterDot1pBits.setStatus("current")


class _AgentCosQueueCNOuterTPIDValue_Type(Integer32):
    """Custom type agentCosQueueCNOuterTPIDValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AgentCosQueueCNOuterTPIDValue_Type.__name__ = "Integer32"
_AgentCosQueueCNOuterTPIDValue_Object = MibScalar
agentCosQueueCNOuterTPIDValue = _AgentCosQueueCNOuterTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 9),
    _AgentCosQueueCNOuterTPIDValue_Type()
)
agentCosQueueCNOuterTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNOuterTPIDValue.setStatus("current")


class _AgentCosQueueCNOuterVlanId_Type(Integer32):
    """Custom type agentCosQueueCNOuterVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4093),
    )


_AgentCosQueueCNOuterVlanId_Type.__name__ = "Integer32"
_AgentCosQueueCNOuterVlanId_Object = MibScalar
agentCosQueueCNOuterVlanId = _AgentCosQueueCNOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 10),
    _AgentCosQueueCNOuterVlanId_Type()
)
agentCosQueueCNOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNOuterVlanId.setStatus("current")


class _AgentCosQueueCNInnerCFIBits_Type(Integer32):
    """Custom type agentCosQueueCNInnerCFIBits based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_AgentCosQueueCNInnerCFIBits_Type.__name__ = "Integer32"
_AgentCosQueueCNInnerCFIBits_Object = MibScalar
agentCosQueueCNInnerCFIBits = _AgentCosQueueCNInnerCFIBits_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 11),
    _AgentCosQueueCNInnerCFIBits_Type()
)
agentCosQueueCNInnerCFIBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNInnerCFIBits.setStatus("current")


class _AgentCosQueueCNInnerDot1pBits_Type(Integer32):
    """Custom type agentCosQueueCNInnerDot1pBits based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AgentCosQueueCNInnerDot1pBits_Type.__name__ = "Integer32"
_AgentCosQueueCNInnerDot1pBits_Object = MibScalar
agentCosQueueCNInnerDot1pBits = _AgentCosQueueCNInnerDot1pBits_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 12),
    _AgentCosQueueCNInnerDot1pBits_Type()
)
agentCosQueueCNInnerDot1pBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNInnerDot1pBits.setStatus("current")


class _AgentCosQueueCNNoGeneration_Type(Integer32):
    """Custom type agentCosQueueCNNoGeneration based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueCNNoGeneration_Type.__name__ = "Integer32"
_AgentCosQueueCNNoGeneration_Object = MibScalar
agentCosQueueCNNoGeneration = _AgentCosQueueCNNoGeneration_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 8, 13),
    _AgentCosQueueCNNoGeneration_Type()
)
agentCosQueueCNNoGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNNoGeneration.setStatus("current")
_AgentCosQueueCNPriorityTable_Object = MibTable
agentCosQueueCNPriorityTable = _AgentCosQueueCNPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9)
)
if mibBuilder.loadTexts:
    agentCosQueueCNPriorityTable.setStatus("current")
_AgentCosQueueCNPriorityEntry_Object = MibTableRow
agentCosQueueCNPriorityEntry = _AgentCosQueueCNPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1)
)
agentCosQueueCNPriorityEntry.setIndexNames(
    (0, "QOS-COS-MIB", "agentCosQueueCNifIndex"),
    (0, "QOS-COS-MIB", "agentCosQueueCNPriorityIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueCNPriorityEntry.setStatus("current")
_AgentCosQueueCNifIndex_Type = InterfaceIndex
_AgentCosQueueCNifIndex_Object = MibTableColumn
agentCosQueueCNifIndex = _AgentCosQueueCNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1, 1),
    _AgentCosQueueCNifIndex_Type()
)
agentCosQueueCNifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueCNifIndex.setStatus("current")


class _AgentCosQueueCNPriorityIndex_Type(Unsigned32):
    """Custom type agentCosQueueCNPriorityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentCosQueueCNPriorityIndex_Type.__name__ = "Unsigned32"
_AgentCosQueueCNPriorityIndex_Object = MibTableColumn
agentCosQueueCNPriorityIndex = _AgentCosQueueCNPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1, 2),
    _AgentCosQueueCNPriorityIndex_Type()
)
agentCosQueueCNPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueCNPriorityIndex.setStatus("current")


class _AgentCosQueueCNQueueIndex_Type(Unsigned32):
    """Custom type agentCosQueueCNQueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentCosQueueCNQueueIndex_Type.__name__ = "Unsigned32"
_AgentCosQueueCNQueueIndex_Object = MibTableColumn
agentCosQueueCNQueueIndex = _AgentCosQueueCNQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1, 3),
    _AgentCosQueueCNQueueIndex_Type()
)
agentCosQueueCNQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueCNQueueIndex.setStatus("current")


class _AgentCosQueueCNPriorityAdminMode_Type(Integer32):
    """Custom type agentCosQueueCNPriorityAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentCosQueueCNPriorityAdminMode_Type.__name__ = "Integer32"
_AgentCosQueueCNPriorityAdminMode_Object = MibTableColumn
agentCosQueueCNPriorityAdminMode = _AgentCosQueueCNPriorityAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1, 4),
    _AgentCosQueueCNPriorityAdminMode_Type()
)
agentCosQueueCNPriorityAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueCNPriorityAdminMode.setStatus("current")
_AgentCosQueueCNPriorityCNMCount_Type = Counter32
_AgentCosQueueCNPriorityCNMCount_Object = MibTableColumn
agentCosQueueCNPriorityCNMCount = _AgentCosQueueCNPriorityCNMCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 3, 2, 9, 1, 5),
    _AgentCosQueueCNPriorityCNMCount_Type()
)
agentCosQueueCNPriorityCNMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueCNPriorityCNMCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOS-COS-MIB",
    **{"PercentByFives": PercentByFives,
       "Percent": Percent,
       "Sixteenths": Sixteenths,
       "cos": cos,
       "agentCosMapCfgGroup": agentCosMapCfgGroup,
       "agentCosMapIpDscpTable": agentCosMapIpDscpTable,
       "agentCosMapIpDscpEntry": agentCosMapIpDscpEntry,
       "agentCosMapIpDscpIntfIndex": agentCosMapIpDscpIntfIndex,
       "agentCosMapIpDscpValue": agentCosMapIpDscpValue,
       "agentCosMapIpDscpTrafficClass": agentCosMapIpDscpTrafficClass,
       "agentCosMapIntfTrustTable": agentCosMapIntfTrustTable,
       "agentCosMapIntfTrustEntry": agentCosMapIntfTrustEntry,
       "agentCosMapIntfTrustIntfIndex": agentCosMapIntfTrustIntfIndex,
       "agentCosMapIntfTrustMode": agentCosMapIntfTrustMode,
       "agentCosMapUntrustedTrafficClass": agentCosMapUntrustedTrafficClass,
       "agentCosQueueCfgGroup": agentCosQueueCfgGroup,
       "agentCosQueueNumQueuesPerPort": agentCosQueueNumQueuesPerPort,
       "agentCosQueueNumDropPrecedenceLevels": agentCosQueueNumDropPrecedenceLevels,
       "agentCosQueueControlTable": agentCosQueueControlTable,
       "agentCosQueueControlEntry": agentCosQueueControlEntry,
       "agentCosQueueIntfIndex": agentCosQueueIntfIndex,
       "agentCosQueueIntfShapingRate": agentCosQueueIntfShapingRate,
       "agentCosQueueMgmtTypeIntf": agentCosQueueMgmtTypeIntf,
       "agentCosQueueWredDecayExponent": agentCosQueueWredDecayExponent,
       "agentCosQueueDefaultsRestore": agentCosQueueDefaultsRestore,
       "agentCosQueueIntfShapingRateUnits": agentCosQueueIntfShapingRateUnits,
       "agentCosQueueTable": agentCosQueueTable,
       "agentCosQueueEntry": agentCosQueueEntry,
       "agentCosQueueIndex": agentCosQueueIndex,
       "agentCosQueueSchedulerType": agentCosQueueSchedulerType,
       "agentCosQueueMinBandwidth": agentCosQueueMinBandwidth,
       "agentCosQueueMaxBandwidth": agentCosQueueMaxBandwidth,
       "agentCosQueueMgmtType": agentCosQueueMgmtType,
       "agentCosQueueMgmtTable": agentCosQueueMgmtTable,
       "agentCosQueueMgmtEntry": agentCosQueueMgmtEntry,
       "agentCosQueueDropPrecIndex": agentCosQueueDropPrecIndex,
       "agentCosQueueMgmtTailDropThreshold": agentCosQueueMgmtTailDropThreshold,
       "agentCosQueueMgmtWredMinThreshold": agentCosQueueMgmtWredMinThreshold,
       "agentCosQueueMgmtWredMaxThreshold": agentCosQueueMgmtWredMaxThreshold,
       "agentCosQueueMgmtWredDropProbScale": agentCosQueueMgmtWredDropProbScale,
       "agentCosQueueMgmtPercentTailDropThreshold": agentCosQueueMgmtPercentTailDropThreshold,
       "agentCosQueueMgmtPercentWredMinThreshold": agentCosQueueMgmtPercentWredMinThreshold,
       "agentCosQueueMgmtPercentWredMaxThreshold": agentCosQueueMgmtPercentWredMaxThreshold,
       "agentCosQueueMgmtWredDropProbability": agentCosQueueMgmtWredDropProbability,
       "agentCosQueueETSControlTable": agentCosQueueETSControlTable,
       "agentCosQueueETSControlEntry": agentCosQueueETSControlEntry,
       "agentCosQueueETSIntfIndex": agentCosQueueETSIntfIndex,
       "agentCosQueueETSAdminMode": agentCosQueueETSAdminMode,
       "agentCosQueueETSSchedulerType": agentCosQueueETSSchedulerType,
       "agentCosQueueETSLanWeight": agentCosQueueETSLanWeight,
       "agentCosQueueETSSanWeight": agentCosQueueETSSanWeight,
       "agentCosQueueETSTable": agentCosQueueETSTable,
       "agentCosQueueETSEntry": agentCosQueueETSEntry,
       "agentCosQueueETSifIndex": agentCosQueueETSifIndex,
       "agentCosQueueETSIndex": agentCosQueueETSIndex,
       "agentCosQueueETSPgMapping": agentCosQueueETSPgMapping,
       "agentCosQueueCNGroup": agentCosQueueCNGroup,
       "agentCosQueueCNAdminMode": agentCosQueueCNAdminMode,
       "agentCosQueueCNTagEtherTypeRecognize": agentCosQueueCNTagEtherTypeRecognize,
       "agentCosQueueCNTagEtherTypeValue": agentCosQueueCNTagEtherTypeValue,
       "agentCosQueueCNMsgEtherTypeValue": agentCosQueueCNMsgEtherTypeValue,
       "agentCosQueueCNCPIDDevId": agentCosQueueCNCPIDDevId,
       "agentCosQueueCNCPIDLSBMode": agentCosQueueCNCPIDLSBMode,
       "agentCosQueueCNOuterCFIBits": agentCosQueueCNOuterCFIBits,
       "agentCosQueueCNOuterDot1pBits": agentCosQueueCNOuterDot1pBits,
       "agentCosQueueCNOuterTPIDValue": agentCosQueueCNOuterTPIDValue,
       "agentCosQueueCNOuterVlanId": agentCosQueueCNOuterVlanId,
       "agentCosQueueCNInnerCFIBits": agentCosQueueCNInnerCFIBits,
       "agentCosQueueCNInnerDot1pBits": agentCosQueueCNInnerDot1pBits,
       "agentCosQueueCNNoGeneration": agentCosQueueCNNoGeneration,
       "agentCosQueueCNPriorityTable": agentCosQueueCNPriorityTable,
       "agentCosQueueCNPriorityEntry": agentCosQueueCNPriorityEntry,
       "agentCosQueueCNifIndex": agentCosQueueCNifIndex,
       "agentCosQueueCNPriorityIndex": agentCosQueueCNPriorityIndex,
       "agentCosQueueCNQueueIndex": agentCosQueueCNQueueIndex,
       "agentCosQueueCNPriorityAdminMode": agentCosQueueCNPriorityAdminMode,
       "agentCosQueueCNPriorityCNMCount": agentCosQueueCNPriorityCNMCount}
)
