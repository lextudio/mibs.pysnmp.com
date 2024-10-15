# SNMP MIB module (EdgeSwitch-QOS-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-QOS-COS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:00 2024
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "EdgeSwitch-QOS-MIB",
    "fastPathQOS")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

fastPathQOSCOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3)
)
fastPathQOSCOS.setRevisions(
        ("2011-01-26 00:00",
         "2010-03-17 00:00",
         "2009-10-27 00:00",
         "2009-01-06 00:00",
         "2008-09-23 00:00",
         "2007-12-19 00:00",
         "2007-05-23 00:00",
         "2004-05-03 00:00")
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1)
)
_AgentCosMapIpPrecTable_Object = MibTable
agentCosMapIpPrecTable = _AgentCosMapIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    agentCosMapIpPrecTable.setStatus("current")
_AgentCosMapIpPrecEntry_Object = MibTableRow
agentCosMapIpPrecEntry = _AgentCosMapIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 1, 1)
)
agentCosMapIpPrecEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosMapIpPrecIntfIndex"),
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosMapIpPrecValue"),
)
if mibBuilder.loadTexts:
    agentCosMapIpPrecEntry.setStatus("current")
_AgentCosMapIpPrecIntfIndex_Type = InterfaceIndexOrZero
_AgentCosMapIpPrecIntfIndex_Object = MibTableColumn
agentCosMapIpPrecIntfIndex = _AgentCosMapIpPrecIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 1, 1, 1),
    _AgentCosMapIpPrecIntfIndex_Type()
)
agentCosMapIpPrecIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosMapIpPrecIntfIndex.setStatus("current")


class _AgentCosMapIpPrecValue_Type(Unsigned32):
    """Custom type agentCosMapIpPrecValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentCosMapIpPrecValue_Type.__name__ = "Unsigned32"
_AgentCosMapIpPrecValue_Object = MibTableColumn
agentCosMapIpPrecValue = _AgentCosMapIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 1, 1, 2),
    _AgentCosMapIpPrecValue_Type()
)
agentCosMapIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosMapIpPrecValue.setStatus("current")


class _AgentCosMapIpPrecTrafficClass_Type(Unsigned32):
    """Custom type agentCosMapIpPrecTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentCosMapIpPrecTrafficClass_Type.__name__ = "Unsigned32"
_AgentCosMapIpPrecTrafficClass_Object = MibTableColumn
agentCosMapIpPrecTrafficClass = _AgentCosMapIpPrecTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 1, 1, 3),
    _AgentCosMapIpPrecTrafficClass_Type()
)
agentCosMapIpPrecTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosMapIpPrecTrafficClass.setStatus("current")
_AgentCosMapIpDscpTable_Object = MibTable
agentCosMapIpDscpTable = _AgentCosMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    agentCosMapIpDscpTable.setStatus("current")
_AgentCosMapIpDscpEntry_Object = MibTableRow
agentCosMapIpDscpEntry = _AgentCosMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 2, 1)
)
agentCosMapIpDscpEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosMapIpDscpIntfIndex"),
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    agentCosMapIpDscpEntry.setStatus("current")
_AgentCosMapIpDscpIntfIndex_Type = InterfaceIndexOrZero
_AgentCosMapIpDscpIntfIndex_Object = MibTableColumn
agentCosMapIpDscpIntfIndex = _AgentCosMapIpDscpIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 2, 1, 3),
    _AgentCosMapIpDscpTrafficClass_Type()
)
agentCosMapIpDscpTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosMapIpDscpTrafficClass.setStatus("current")
_AgentCosMapIntfTrustTable_Object = MibTable
agentCosMapIntfTrustTable = _AgentCosMapIntfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    agentCosMapIntfTrustTable.setStatus("current")
_AgentCosMapIntfTrustEntry_Object = MibTableRow
agentCosMapIntfTrustEntry = _AgentCosMapIntfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 3, 1)
)
agentCosMapIntfTrustEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosMapIntfTrustIntfIndex"),
)
if mibBuilder.loadTexts:
    agentCosMapIntfTrustEntry.setStatus("current")
_AgentCosMapIntfTrustIntfIndex_Type = InterfaceIndexOrZero
_AgentCosMapIntfTrustIntfIndex_Object = MibTableColumn
agentCosMapIntfTrustIntfIndex = _AgentCosMapIntfTrustIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 3, 1, 1),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("trustDot1p", 2),
          ("trustIpDscp", 4),
          ("trustIpPrecedence", 3),
          ("untrusted", 1))
    )


_AgentCosMapIntfTrustMode_Type.__name__ = "Integer32"
_AgentCosMapIntfTrustMode_Object = MibTableColumn
agentCosMapIntfTrustMode = _AgentCosMapIntfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 3, 1, 2),
    _AgentCosMapIntfTrustMode_Type()
)
agentCosMapIntfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosMapIntfTrustMode.setStatus("current")
_AgentCosMapUntrustedTrafficClass_Type = Unsigned32
_AgentCosMapUntrustedTrafficClass_Object = MibTableColumn
agentCosMapUntrustedTrafficClass = _AgentCosMapUntrustedTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 1, 3, 1, 3),
    _AgentCosMapUntrustedTrafficClass_Type()
)
agentCosMapUntrustedTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosMapUntrustedTrafficClass.setStatus("current")
_AgentCosQueueCfgGroup_ObjectIdentity = ObjectIdentity
agentCosQueueCfgGroup = _AgentCosQueueCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2)
)
_AgentCosQueueNumQueuesPerPort_Type = Unsigned32
_AgentCosQueueNumQueuesPerPort_Object = MibScalar
agentCosQueueNumQueuesPerPort = _AgentCosQueueNumQueuesPerPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 1),
    _AgentCosQueueNumQueuesPerPort_Type()
)
agentCosQueueNumQueuesPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueNumQueuesPerPort.setStatus("current")
_AgentCosQueueNumDropPrecedenceLevels_Type = Unsigned32
_AgentCosQueueNumDropPrecedenceLevels_Object = MibScalar
agentCosQueueNumDropPrecedenceLevels = _AgentCosQueueNumDropPrecedenceLevels_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 2),
    _AgentCosQueueNumDropPrecedenceLevels_Type()
)
agentCosQueueNumDropPrecedenceLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueNumDropPrecedenceLevels.setStatus("current")
_AgentCosQueueControlTable_Object = MibTable
agentCosQueueControlTable = _AgentCosQueueControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    agentCosQueueControlTable.setStatus("current")
_AgentCosQueueControlEntry_Object = MibTableRow
agentCosQueueControlEntry = _AgentCosQueueControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1)
)
agentCosQueueControlEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueIntfIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueControlEntry.setStatus("current")
_AgentCosQueueIntfIndex_Type = InterfaceIndexOrZero
_AgentCosQueueIntfIndex_Object = MibTableColumn
agentCosQueueIntfIndex = _AgentCosQueueIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 1),
    _AgentCosQueueIntfIndex_Type()
)
agentCosQueueIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosQueueIntfIndex.setStatus("current")


class _AgentCosQueueIntfShapingRate_Type(Unsigned32):
    """Custom type agentCosQueueIntfShapingRate based on Unsigned32"""
    defaultValue = 0


_AgentCosQueueIntfShapingRate_Object = MibTableColumn
agentCosQueueIntfShapingRate = _AgentCosQueueIntfShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 3),
    _AgentCosQueueMgmtTypeIntf_Type()
)
agentCosQueueMgmtTypeIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtTypeIntf.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 3, 1, 6),
    _AgentCosQueueIntfShapingRateUnits_Type()
)
agentCosQueueIntfShapingRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCosQueueIntfShapingRateUnits.setStatus("current")
_AgentCosQueueTable_Object = MibTable
agentCosQueueTable = _AgentCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    agentCosQueueTable.setStatus("current")
_AgentCosQueueEntry_Object = MibTableRow
agentCosQueueEntry = _AgentCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1)
)
agentCosQueueEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueIntfIndex"),
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueEntry.setStatus("current")
_AgentCosQueueIndex_Type = Unsigned32
_AgentCosQueueIndex_Object = MibTableColumn
agentCosQueueIndex = _AgentCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1, 4),
    _AgentCosQueueMaxBandwidth_Type()
)
agentCosQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMaxBandwidth.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 4, 1, 5),
    _AgentCosQueueMgmtType_Type()
)
agentCosQueueMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtType.setStatus("current")
_AgentCosQueueMgmtTable_Object = MibTable
agentCosQueueMgmtTable = _AgentCosQueueMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    agentCosQueueMgmtTable.setStatus("current")
_AgentCosQueueMgmtEntry_Object = MibTableRow
agentCosQueueMgmtEntry = _AgentCosQueueMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1)
)
agentCosQueueMgmtEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueIntfIndex"),
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueIndex"),
    (0, "EdgeSwitch-QOS-COS-MIB", "agentCosQueueDropPrecIndex"),
)
if mibBuilder.loadTexts:
    agentCosQueueMgmtEntry.setStatus("current")
_AgentCosQueueDropPrecIndex_Type = Unsigned32
_AgentCosQueueDropPrecIndex_Object = MibTableColumn
agentCosQueueDropPrecIndex = _AgentCosQueueDropPrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 1),
    _AgentCosQueueDropPrecIndex_Type()
)
agentCosQueueDropPrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCosQueueDropPrecIndex.setStatus("current")
_AgentCosQueueMgmtTailDropThreshold_Type = Sixteenths
_AgentCosQueueMgmtTailDropThreshold_Object = MibTableColumn
agentCosQueueMgmtTailDropThreshold = _AgentCosQueueMgmtTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 2),
    _AgentCosQueueMgmtTailDropThreshold_Type()
)
agentCosQueueMgmtTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtTailDropThreshold.setStatus("obsolete")
_AgentCosQueueMgmtWredMinThreshold_Type = Sixteenths
_AgentCosQueueMgmtWredMinThreshold_Object = MibTableColumn
agentCosQueueMgmtWredMinThreshold = _AgentCosQueueMgmtWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 3),
    _AgentCosQueueMgmtWredMinThreshold_Type()
)
agentCosQueueMgmtWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredMinThreshold.setStatus("obsolete")
_AgentCosQueueMgmtWredMaxThreshold_Type = Sixteenths
_AgentCosQueueMgmtWredMaxThreshold_Object = MibTableColumn
agentCosQueueMgmtWredMaxThreshold = _AgentCosQueueMgmtWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 5),
    _AgentCosQueueMgmtWredDropProbScale_Type()
)
agentCosQueueMgmtWredDropProbScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredDropProbScale.setStatus("obsolete")
_AgentCosQueueMgmtPercentTailDropThreshold_Type = Percent
_AgentCosQueueMgmtPercentTailDropThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentTailDropThreshold = _AgentCosQueueMgmtPercentTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 6),
    _AgentCosQueueMgmtPercentTailDropThreshold_Type()
)
agentCosQueueMgmtPercentTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtPercentTailDropThreshold.setStatus("current")
_AgentCosQueueMgmtPercentWredMinThreshold_Type = Percent
_AgentCosQueueMgmtPercentWredMinThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentWredMinThreshold = _AgentCosQueueMgmtPercentWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 7),
    _AgentCosQueueMgmtPercentWredMinThreshold_Type()
)
agentCosQueueMgmtPercentWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtPercentWredMinThreshold.setStatus("current")
_AgentCosQueueMgmtPercentWredMaxThreshold_Type = Percent
_AgentCosQueueMgmtPercentWredMaxThreshold_Object = MibTableColumn
agentCosQueueMgmtPercentWredMaxThreshold = _AgentCosQueueMgmtPercentWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 3, 2, 5, 1, 9),
    _AgentCosQueueMgmtWredDropProbability_Type()
)
agentCosQueueMgmtWredDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCosQueueMgmtWredDropProbability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-QOS-COS-MIB",
    **{"PercentByFives": PercentByFives,
       "Percent": Percent,
       "Sixteenths": Sixteenths,
       "fastPathQOSCOS": fastPathQOSCOS,
       "agentCosMapCfgGroup": agentCosMapCfgGroup,
       "agentCosMapIpPrecTable": agentCosMapIpPrecTable,
       "agentCosMapIpPrecEntry": agentCosMapIpPrecEntry,
       "agentCosMapIpPrecIntfIndex": agentCosMapIpPrecIntfIndex,
       "agentCosMapIpPrecValue": agentCosMapIpPrecValue,
       "agentCosMapIpPrecTrafficClass": agentCosMapIpPrecTrafficClass,
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
       "agentCosQueueMgmtWredDropProbability": agentCosQueueMgmtWredDropProbability}
)
