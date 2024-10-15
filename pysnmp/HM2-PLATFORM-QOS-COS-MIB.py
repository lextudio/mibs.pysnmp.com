# SNMP MIB module (HM2-PLATFORM-QOS-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-QOS-COS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:20 2024
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

(hm2PlatformQoS,) = mibBuilder.importSymbols(
    "HM2-PLATFORM-QOS-MIB",
    "hm2PlatformQoS")

(HmEnabledStatus,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformQosCos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3)
)
hm2PlatformQosCos.setRevisions(
        ("2011-10-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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

_Hm2AgentCosMapCfgGroup_ObjectIdentity = ObjectIdentity
hm2AgentCosMapCfgGroup = _Hm2AgentCosMapCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1)
)
_Hm2AgentCosMapIpPrecTable_Object = MibTable
hm2AgentCosMapIpPrecTable = _Hm2AgentCosMapIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIpPrecTable.setStatus("current")
_Hm2AgentCosMapIpPrecEntry_Object = MibTableRow
hm2AgentCosMapIpPrecEntry = _Hm2AgentCosMapIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1)
)
hm2AgentCosMapIpPrecEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecIntfIndex"),
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecValue"),
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIpPrecEntry.setStatus("current")
_Hm2AgentCosMapIpPrecIntfIndex_Type = InterfaceIndexOrZero
_Hm2AgentCosMapIpPrecIntfIndex_Object = MibTableColumn
hm2AgentCosMapIpPrecIntfIndex = _Hm2AgentCosMapIpPrecIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 1),
    _Hm2AgentCosMapIpPrecIntfIndex_Type()
)
hm2AgentCosMapIpPrecIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpPrecIntfIndex.setStatus("current")


class _Hm2AgentCosMapIpPrecValue_Type(Unsigned32):
    """Custom type hm2AgentCosMapIpPrecValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentCosMapIpPrecValue_Type.__name__ = "Unsigned32"
_Hm2AgentCosMapIpPrecValue_Object = MibTableColumn
hm2AgentCosMapIpPrecValue = _Hm2AgentCosMapIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 2),
    _Hm2AgentCosMapIpPrecValue_Type()
)
hm2AgentCosMapIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpPrecValue.setStatus("current")


class _Hm2AgentCosMapIpPrecTrafficClass_Type(Unsigned32):
    """Custom type hm2AgentCosMapIpPrecTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentCosMapIpPrecTrafficClass_Type.__name__ = "Unsigned32"
_Hm2AgentCosMapIpPrecTrafficClass_Object = MibTableColumn
hm2AgentCosMapIpPrecTrafficClass = _Hm2AgentCosMapIpPrecTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 3),
    _Hm2AgentCosMapIpPrecTrafficClass_Type()
)
hm2AgentCosMapIpPrecTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpPrecTrafficClass.setStatus("current")
_Hm2AgentCosMapIpDscpTable_Object = MibTable
hm2AgentCosMapIpDscpTable = _Hm2AgentCosMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIpDscpTable.setStatus("current")
_Hm2AgentCosMapIpDscpEntry_Object = MibTableRow
hm2AgentCosMapIpDscpEntry = _Hm2AgentCosMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1)
)
hm2AgentCosMapIpDscpEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpIntfIndex"),
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIpDscpEntry.setStatus("current")
_Hm2AgentCosMapIpDscpIntfIndex_Type = InterfaceIndexOrZero
_Hm2AgentCosMapIpDscpIntfIndex_Object = MibTableColumn
hm2AgentCosMapIpDscpIntfIndex = _Hm2AgentCosMapIpDscpIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 1),
    _Hm2AgentCosMapIpDscpIntfIndex_Type()
)
hm2AgentCosMapIpDscpIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpDscpIntfIndex.setStatus("current")


class _Hm2AgentCosMapIpDscpValue_Type(Unsigned32):
    """Custom type hm2AgentCosMapIpDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentCosMapIpDscpValue_Type.__name__ = "Unsigned32"
_Hm2AgentCosMapIpDscpValue_Object = MibTableColumn
hm2AgentCosMapIpDscpValue = _Hm2AgentCosMapIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 2),
    _Hm2AgentCosMapIpDscpValue_Type()
)
hm2AgentCosMapIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpDscpValue.setStatus("current")


class _Hm2AgentCosMapIpDscpTrafficClass_Type(Unsigned32):
    """Custom type hm2AgentCosMapIpDscpTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentCosMapIpDscpTrafficClass_Type.__name__ = "Unsigned32"
_Hm2AgentCosMapIpDscpTrafficClass_Object = MibTableColumn
hm2AgentCosMapIpDscpTrafficClass = _Hm2AgentCosMapIpDscpTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 3),
    _Hm2AgentCosMapIpDscpTrafficClass_Type()
)
hm2AgentCosMapIpDscpTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosMapIpDscpTrafficClass.setStatus("current")
_Hm2AgentCosMapIntfTrustTable_Object = MibTable
hm2AgentCosMapIntfTrustTable = _Hm2AgentCosMapIntfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIntfTrustTable.setStatus("current")
_Hm2AgentCosMapIntfTrustEntry_Object = MibTableRow
hm2AgentCosMapIntfTrustEntry = _Hm2AgentCosMapIntfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1)
)
hm2AgentCosMapIntfTrustEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIntfTrustIntfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentCosMapIntfTrustEntry.setStatus("current")
_Hm2AgentCosMapIntfTrustIntfIndex_Type = InterfaceIndexOrZero
_Hm2AgentCosMapIntfTrustIntfIndex_Object = MibTableColumn
hm2AgentCosMapIntfTrustIntfIndex = _Hm2AgentCosMapIntfTrustIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 1),
    _Hm2AgentCosMapIntfTrustIntfIndex_Type()
)
hm2AgentCosMapIntfTrustIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosMapIntfTrustIntfIndex.setStatus("current")


class _Hm2AgentCosMapIntfTrustMode_Type(Integer32):
    """Custom type hm2AgentCosMapIntfTrustMode based on Integer32"""
    defaultValue = 2

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


_Hm2AgentCosMapIntfTrustMode_Type.__name__ = "Integer32"
_Hm2AgentCosMapIntfTrustMode_Object = MibTableColumn
hm2AgentCosMapIntfTrustMode = _Hm2AgentCosMapIntfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 2),
    _Hm2AgentCosMapIntfTrustMode_Type()
)
hm2AgentCosMapIntfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosMapIntfTrustMode.setStatus("current")
_Hm2AgentCosMapUntrustedTrafficClass_Type = Unsigned32
_Hm2AgentCosMapUntrustedTrafficClass_Object = MibTableColumn
hm2AgentCosMapUntrustedTrafficClass = _Hm2AgentCosMapUntrustedTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 3),
    _Hm2AgentCosMapUntrustedTrafficClass_Type()
)
hm2AgentCosMapUntrustedTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentCosMapUntrustedTrafficClass.setStatus("current")
_Hm2AgentCosQueueCfgGroup_ObjectIdentity = ObjectIdentity
hm2AgentCosQueueCfgGroup = _Hm2AgentCosQueueCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2)
)
_Hm2AgentCosQueueNumQueuesPerPort_Type = Unsigned32
_Hm2AgentCosQueueNumQueuesPerPort_Object = MibScalar
hm2AgentCosQueueNumQueuesPerPort = _Hm2AgentCosQueueNumQueuesPerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 1),
    _Hm2AgentCosQueueNumQueuesPerPort_Type()
)
hm2AgentCosQueueNumQueuesPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentCosQueueNumQueuesPerPort.setStatus("current")
_Hm2AgentCosQueueNumDropPrecedenceLevels_Type = Unsigned32
_Hm2AgentCosQueueNumDropPrecedenceLevels_Object = MibScalar
hm2AgentCosQueueNumDropPrecedenceLevels = _Hm2AgentCosQueueNumDropPrecedenceLevels_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 2),
    _Hm2AgentCosQueueNumDropPrecedenceLevels_Type()
)
hm2AgentCosQueueNumDropPrecedenceLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentCosQueueNumDropPrecedenceLevels.setStatus("current")
_Hm2AgentCosQueueControlTable_Object = MibTable
hm2AgentCosQueueControlTable = _Hm2AgentCosQueueControlTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueControlTable.setStatus("current")
_Hm2AgentCosQueueControlEntry_Object = MibTableRow
hm2AgentCosQueueControlEntry = _Hm2AgentCosQueueControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1)
)
hm2AgentCosQueueControlEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueControlEntry.setStatus("current")
_Hm2AgentCosQueueIntfIndex_Type = InterfaceIndexOrZero
_Hm2AgentCosQueueIntfIndex_Object = MibTableColumn
hm2AgentCosQueueIntfIndex = _Hm2AgentCosQueueIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 1),
    _Hm2AgentCosQueueIntfIndex_Type()
)
hm2AgentCosQueueIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosQueueIntfIndex.setStatus("current")


class _Hm2AgentCosQueueIntfShapingRate_Type(Unsigned32):
    """Custom type hm2AgentCosQueueIntfShapingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hm2AgentCosQueueIntfShapingRate_Type.__name__ = "Unsigned32"
_Hm2AgentCosQueueIntfShapingRate_Object = MibTableColumn
hm2AgentCosQueueIntfShapingRate = _Hm2AgentCosQueueIntfShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 2),
    _Hm2AgentCosQueueIntfShapingRate_Type()
)
hm2AgentCosQueueIntfShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueIntfShapingRate.setStatus("current")


class _Hm2AgentCosQueueMgmtTypeIntf_Type(Integer32):
    """Custom type hm2AgentCosQueueMgmtTypeIntf based on Integer32"""
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


_Hm2AgentCosQueueMgmtTypeIntf_Type.__name__ = "Integer32"
_Hm2AgentCosQueueMgmtTypeIntf_Object = MibTableColumn
hm2AgentCosQueueMgmtTypeIntf = _Hm2AgentCosQueueMgmtTypeIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 3),
    _Hm2AgentCosQueueMgmtTypeIntf_Type()
)
hm2AgentCosQueueMgmtTypeIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtTypeIntf.setStatus("current")


class _Hm2AgentCosQueueWredDecayExponent_Type(Unsigned32):
    """Custom type hm2AgentCosQueueWredDecayExponent based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hm2AgentCosQueueWredDecayExponent_Type.__name__ = "Unsigned32"
_Hm2AgentCosQueueWredDecayExponent_Object = MibTableColumn
hm2AgentCosQueueWredDecayExponent = _Hm2AgentCosQueueWredDecayExponent_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 4),
    _Hm2AgentCosQueueWredDecayExponent_Type()
)
hm2AgentCosQueueWredDecayExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueWredDecayExponent.setStatus("current")
_Hm2AgentCosQueueDefaultsRestore_Type = HmEnabledStatus
_Hm2AgentCosQueueDefaultsRestore_Object = MibTableColumn
hm2AgentCosQueueDefaultsRestore = _Hm2AgentCosQueueDefaultsRestore_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 5),
    _Hm2AgentCosQueueDefaultsRestore_Type()
)
hm2AgentCosQueueDefaultsRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueDefaultsRestore.setStatus("current")


class _Hm2AgentCosQueueIntfShapingRateUnits_Type(Integer32):
    """Custom type hm2AgentCosQueueIntfShapingRateUnits based on Integer32"""
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


_Hm2AgentCosQueueIntfShapingRateUnits_Type.__name__ = "Integer32"
_Hm2AgentCosQueueIntfShapingRateUnits_Object = MibTableColumn
hm2AgentCosQueueIntfShapingRateUnits = _Hm2AgentCosQueueIntfShapingRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 6),
    _Hm2AgentCosQueueIntfShapingRateUnits_Type()
)
hm2AgentCosQueueIntfShapingRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentCosQueueIntfShapingRateUnits.setStatus("current")
_Hm2AgentCosQueueTable_Object = MibTable
hm2AgentCosQueueTable = _Hm2AgentCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueTable.setStatus("current")
_Hm2AgentCosQueueEntry_Object = MibTableRow
hm2AgentCosQueueEntry = _Hm2AgentCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1)
)
hm2AgentCosQueueEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"),
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueEntry.setStatus("current")
_Hm2AgentCosQueueIndex_Type = Unsigned32
_Hm2AgentCosQueueIndex_Object = MibTableColumn
hm2AgentCosQueueIndex = _Hm2AgentCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 1),
    _Hm2AgentCosQueueIndex_Type()
)
hm2AgentCosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosQueueIndex.setStatus("current")


class _Hm2AgentCosQueueSchedulerType_Type(Integer32):
    """Custom type hm2AgentCosQueueSchedulerType based on Integer32"""
    defaultValue = 1

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


_Hm2AgentCosQueueSchedulerType_Type.__name__ = "Integer32"
_Hm2AgentCosQueueSchedulerType_Object = MibTableColumn
hm2AgentCosQueueSchedulerType = _Hm2AgentCosQueueSchedulerType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 2),
    _Hm2AgentCosQueueSchedulerType_Type()
)
hm2AgentCosQueueSchedulerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueSchedulerType.setStatus("current")


class _Hm2AgentCosQueueMinBandwidth_Type(Percent):
    """Custom type hm2AgentCosQueueMinBandwidth based on Percent"""
    defaultValue = 0


_Hm2AgentCosQueueMinBandwidth_Object = MibTableColumn
hm2AgentCosQueueMinBandwidth = _Hm2AgentCosQueueMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 3),
    _Hm2AgentCosQueueMinBandwidth_Type()
)
hm2AgentCosQueueMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMinBandwidth.setStatus("current")


class _Hm2AgentCosQueueMaxBandwidth_Type(Percent):
    """Custom type hm2AgentCosQueueMaxBandwidth based on Percent"""
    defaultValue = 0


_Hm2AgentCosQueueMaxBandwidth_Object = MibTableColumn
hm2AgentCosQueueMaxBandwidth = _Hm2AgentCosQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 4),
    _Hm2AgentCosQueueMaxBandwidth_Type()
)
hm2AgentCosQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMaxBandwidth.setStatus("current")


class _Hm2AgentCosQueueMgmtType_Type(Integer32):
    """Custom type hm2AgentCosQueueMgmtType based on Integer32"""
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


_Hm2AgentCosQueueMgmtType_Type.__name__ = "Integer32"
_Hm2AgentCosQueueMgmtType_Object = MibTableColumn
hm2AgentCosQueueMgmtType = _Hm2AgentCosQueueMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 5),
    _Hm2AgentCosQueueMgmtType_Type()
)
hm2AgentCosQueueMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtType.setStatus("current")
_Hm2AgentCosQueueMgmtTable_Object = MibTable
hm2AgentCosQueueMgmtTable = _Hm2AgentCosQueueMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtTable.setStatus("current")
_Hm2AgentCosQueueMgmtEntry_Object = MibTableRow
hm2AgentCosQueueMgmtEntry = _Hm2AgentCosQueueMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1)
)
hm2AgentCosQueueMgmtEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"),
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"),
    (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueDropPrecIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtEntry.setStatus("current")
_Hm2AgentCosQueueDropPrecIndex_Type = Unsigned32
_Hm2AgentCosQueueDropPrecIndex_Object = MibTableColumn
hm2AgentCosQueueDropPrecIndex = _Hm2AgentCosQueueDropPrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 1),
    _Hm2AgentCosQueueDropPrecIndex_Type()
)
hm2AgentCosQueueDropPrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentCosQueueDropPrecIndex.setStatus("current")
_Hm2AgentCosQueueMgmtTailDropThreshold_Type = Sixteenths
_Hm2AgentCosQueueMgmtTailDropThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtTailDropThreshold = _Hm2AgentCosQueueMgmtTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 2),
    _Hm2AgentCosQueueMgmtTailDropThreshold_Type()
)
hm2AgentCosQueueMgmtTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtTailDropThreshold.setStatus("obsolete")
_Hm2AgentCosQueueMgmtWredMinThreshold_Type = Sixteenths
_Hm2AgentCosQueueMgmtWredMinThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtWredMinThreshold = _Hm2AgentCosQueueMgmtWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 3),
    _Hm2AgentCosQueueMgmtWredMinThreshold_Type()
)
hm2AgentCosQueueMgmtWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtWredMinThreshold.setStatus("obsolete")
_Hm2AgentCosQueueMgmtWredMaxThreshold_Type = Sixteenths
_Hm2AgentCosQueueMgmtWredMaxThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtWredMaxThreshold = _Hm2AgentCosQueueMgmtWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 4),
    _Hm2AgentCosQueueMgmtWredMaxThreshold_Type()
)
hm2AgentCosQueueMgmtWredMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtWredMaxThreshold.setStatus("obsolete")


class _Hm2AgentCosQueueMgmtWredDropProbScale_Type(Unsigned32):
    """Custom type hm2AgentCosQueueMgmtWredDropProbScale based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2AgentCosQueueMgmtWredDropProbScale_Type.__name__ = "Unsigned32"
_Hm2AgentCosQueueMgmtWredDropProbScale_Object = MibTableColumn
hm2AgentCosQueueMgmtWredDropProbScale = _Hm2AgentCosQueueMgmtWredDropProbScale_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 5),
    _Hm2AgentCosQueueMgmtWredDropProbScale_Type()
)
hm2AgentCosQueueMgmtWredDropProbScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtWredDropProbScale.setStatus("obsolete")
_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Type = Percent
_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtPercentTailDropThreshold = _Hm2AgentCosQueueMgmtPercentTailDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 6),
    _Hm2AgentCosQueueMgmtPercentTailDropThreshold_Type()
)
hm2AgentCosQueueMgmtPercentTailDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtPercentTailDropThreshold.setStatus("current")
_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Type = Percent
_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtPercentWredMinThreshold = _Hm2AgentCosQueueMgmtPercentWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 7),
    _Hm2AgentCosQueueMgmtPercentWredMinThreshold_Type()
)
hm2AgentCosQueueMgmtPercentWredMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtPercentWredMinThreshold.setStatus("current")
_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Type = Percent
_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Object = MibTableColumn
hm2AgentCosQueueMgmtPercentWredMaxThreshold = _Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 8),
    _Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Type()
)
hm2AgentCosQueueMgmtPercentWredMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtPercentWredMaxThreshold.setStatus("current")


class _Hm2AgentCosQueueMgmtWredDropProbability_Type(Percent):
    """Custom type hm2AgentCosQueueMgmtWredDropProbability based on Percent"""
    defaultValue = 10


_Hm2AgentCosQueueMgmtWredDropProbability_Object = MibTableColumn
hm2AgentCosQueueMgmtWredDropProbability = _Hm2AgentCosQueueMgmtWredDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 9),
    _Hm2AgentCosQueueMgmtWredDropProbability_Type()
)
hm2AgentCosQueueMgmtWredDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentCosQueueMgmtWredDropProbability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-QOS-COS-MIB",
    **{"Percent": Percent,
       "Sixteenths": Sixteenths,
       "hm2PlatformQosCos": hm2PlatformQosCos,
       "hm2AgentCosMapCfgGroup": hm2AgentCosMapCfgGroup,
       "hm2AgentCosMapIpPrecTable": hm2AgentCosMapIpPrecTable,
       "hm2AgentCosMapIpPrecEntry": hm2AgentCosMapIpPrecEntry,
       "hm2AgentCosMapIpPrecIntfIndex": hm2AgentCosMapIpPrecIntfIndex,
       "hm2AgentCosMapIpPrecValue": hm2AgentCosMapIpPrecValue,
       "hm2AgentCosMapIpPrecTrafficClass": hm2AgentCosMapIpPrecTrafficClass,
       "hm2AgentCosMapIpDscpTable": hm2AgentCosMapIpDscpTable,
       "hm2AgentCosMapIpDscpEntry": hm2AgentCosMapIpDscpEntry,
       "hm2AgentCosMapIpDscpIntfIndex": hm2AgentCosMapIpDscpIntfIndex,
       "hm2AgentCosMapIpDscpValue": hm2AgentCosMapIpDscpValue,
       "hm2AgentCosMapIpDscpTrafficClass": hm2AgentCosMapIpDscpTrafficClass,
       "hm2AgentCosMapIntfTrustTable": hm2AgentCosMapIntfTrustTable,
       "hm2AgentCosMapIntfTrustEntry": hm2AgentCosMapIntfTrustEntry,
       "hm2AgentCosMapIntfTrustIntfIndex": hm2AgentCosMapIntfTrustIntfIndex,
       "hm2AgentCosMapIntfTrustMode": hm2AgentCosMapIntfTrustMode,
       "hm2AgentCosMapUntrustedTrafficClass": hm2AgentCosMapUntrustedTrafficClass,
       "hm2AgentCosQueueCfgGroup": hm2AgentCosQueueCfgGroup,
       "hm2AgentCosQueueNumQueuesPerPort": hm2AgentCosQueueNumQueuesPerPort,
       "hm2AgentCosQueueNumDropPrecedenceLevels": hm2AgentCosQueueNumDropPrecedenceLevels,
       "hm2AgentCosQueueControlTable": hm2AgentCosQueueControlTable,
       "hm2AgentCosQueueControlEntry": hm2AgentCosQueueControlEntry,
       "hm2AgentCosQueueIntfIndex": hm2AgentCosQueueIntfIndex,
       "hm2AgentCosQueueIntfShapingRate": hm2AgentCosQueueIntfShapingRate,
       "hm2AgentCosQueueMgmtTypeIntf": hm2AgentCosQueueMgmtTypeIntf,
       "hm2AgentCosQueueWredDecayExponent": hm2AgentCosQueueWredDecayExponent,
       "hm2AgentCosQueueDefaultsRestore": hm2AgentCosQueueDefaultsRestore,
       "hm2AgentCosQueueIntfShapingRateUnits": hm2AgentCosQueueIntfShapingRateUnits,
       "hm2AgentCosQueueTable": hm2AgentCosQueueTable,
       "hm2AgentCosQueueEntry": hm2AgentCosQueueEntry,
       "hm2AgentCosQueueIndex": hm2AgentCosQueueIndex,
       "hm2AgentCosQueueSchedulerType": hm2AgentCosQueueSchedulerType,
       "hm2AgentCosQueueMinBandwidth": hm2AgentCosQueueMinBandwidth,
       "hm2AgentCosQueueMaxBandwidth": hm2AgentCosQueueMaxBandwidth,
       "hm2AgentCosQueueMgmtType": hm2AgentCosQueueMgmtType,
       "hm2AgentCosQueueMgmtTable": hm2AgentCosQueueMgmtTable,
       "hm2AgentCosQueueMgmtEntry": hm2AgentCosQueueMgmtEntry,
       "hm2AgentCosQueueDropPrecIndex": hm2AgentCosQueueDropPrecIndex,
       "hm2AgentCosQueueMgmtTailDropThreshold": hm2AgentCosQueueMgmtTailDropThreshold,
       "hm2AgentCosQueueMgmtWredMinThreshold": hm2AgentCosQueueMgmtWredMinThreshold,
       "hm2AgentCosQueueMgmtWredMaxThreshold": hm2AgentCosQueueMgmtWredMaxThreshold,
       "hm2AgentCosQueueMgmtWredDropProbScale": hm2AgentCosQueueMgmtWredDropProbScale,
       "hm2AgentCosQueueMgmtPercentTailDropThreshold": hm2AgentCosQueueMgmtPercentTailDropThreshold,
       "hm2AgentCosQueueMgmtPercentWredMinThreshold": hm2AgentCosQueueMgmtPercentWredMinThreshold,
       "hm2AgentCosQueueMgmtPercentWredMaxThreshold": hm2AgentCosQueueMgmtPercentWredMaxThreshold,
       "hm2AgentCosQueueMgmtWredDropProbability": hm2AgentCosQueueMgmtWredDropProbability}
)
