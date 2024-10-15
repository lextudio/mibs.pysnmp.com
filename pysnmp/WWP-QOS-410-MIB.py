# SNMP MIB module (WWP-QOS-410-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-QOS-410-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:21 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpQos410MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29)
)
wwpQos410MIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpQos410MIBObjects_ObjectIdentity = ObjectIdentity
wwpQos410MIBObjects = _WwpQos410MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1)
)
_WwpQos410_ObjectIdentity = ObjectIdentity
wwpQos410 = _WwpQos410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1)
)
_WwpQos410Table_Object = MibTable
wwpQos410Table = _WwpQos410Table_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpQos410Table.setStatus("current")
_WwpQos410Entry_Object = MibTableRow
wwpQos410Entry = _WwpQos410Entry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1)
)
wwpQos410Entry.setIndexNames(
    (0, "WWP-QOS-410-MIB", "wwpQos410VlanId"),
    (0, "WWP-QOS-410-MIB", "wwpQos410IngressPortId"),
    (0, "WWP-QOS-410-MIB", "wwpQos410EgressPortId"),
)
if mibBuilder.loadTexts:
    wwpQos410Entry.setStatus("current")
_WwpQos410VlanId_Type = VlanId
_WwpQos410VlanId_Object = MibTableColumn
wwpQos410VlanId = _WwpQos410VlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 1),
    _WwpQos410VlanId_Type()
)
wwpQos410VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410VlanId.setStatus("current")


class _WwpQos410IngressPortId_Type(Integer32):
    """Custom type wwpQos410IngressPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQos410IngressPortId_Type.__name__ = "Integer32"
_WwpQos410IngressPortId_Object = MibTableColumn
wwpQos410IngressPortId = _WwpQos410IngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 2),
    _WwpQos410IngressPortId_Type()
)
wwpQos410IngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410IngressPortId.setStatus("current")


class _WwpQos410EgressPortId_Type(Integer32):
    """Custom type wwpQos410EgressPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQos410EgressPortId_Type.__name__ = "Integer32"
_WwpQos410EgressPortId_Object = MibTableColumn
wwpQos410EgressPortId = _WwpQos410EgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 3),
    _WwpQos410EgressPortId_Type()
)
wwpQos410EgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410EgressPortId.setStatus("current")


class _WwpQos410MinRateLimit_Type(Integer32):
    """Custom type wwpQos410MinRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128000),
    )


_WwpQos410MinRateLimit_Type.__name__ = "Integer32"
_WwpQos410MinRateLimit_Object = MibTableColumn
wwpQos410MinRateLimit = _WwpQos410MinRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 4),
    _WwpQos410MinRateLimit_Type()
)
wwpQos410MinRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410MinRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    wwpQos410MinRateLimit.setUnits("kbps")


class _WwpQos410MaxRateLimit_Type(Integer32):
    """Custom type wwpQos410MaxRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128000),
    )


_WwpQos410MaxRateLimit_Type.__name__ = "Integer32"
_WwpQos410MaxRateLimit_Object = MibTableColumn
wwpQos410MaxRateLimit = _WwpQos410MaxRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 5),
    _WwpQos410MaxRateLimit_Type()
)
wwpQos410MaxRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410MaxRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    wwpQos410MaxRateLimit.setUnits("kbps")


class _WwpQos410QueueSize_Type(Integer32):
    """Custom type wwpQos410QueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("qSize128kb", 4),
          ("qSize16kb", 1),
          ("qSize16mb", 11),
          ("qSize1mb", 7),
          ("qSize256kb", 5),
          ("qSize2mb", 8),
          ("qSize32kb", 2),
          ("qSize32mb", 12),
          ("qSize4mb", 9),
          ("qSize512kb", 6),
          ("qSize64kb", 3),
          ("qSize8mb", 10))
    )


_WwpQos410QueueSize_Type.__name__ = "Integer32"
_WwpQos410QueueSize_Object = MibTableColumn
wwpQos410QueueSize = _WwpQos410QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 6),
    _WwpQos410QueueSize_Type()
)
wwpQos410QueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410QueueSize.setStatus("current")


class _WwpQos410Weight_Type(Integer32):
    """Custom type wwpQos410Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("qw1", 1),
          ("qw10", 9),
          ("qw1024", 36),
          ("qw112", 23),
          ("qw12", 10),
          ("qw128", 24),
          ("qw14", 11),
          ("qw16", 12),
          ("qw160", 25),
          ("qw192", 26),
          ("qw2", 2),
          ("qw20", 13),
          ("qw224", 27),
          ("qw24", 14),
          ("qw256", 28),
          ("qw28", 15),
          ("qw3", 3),
          ("qw32", 16),
          ("qw320", 29),
          ("qw384", 30),
          ("qw4", 4),
          ("qw40", 17),
          ("qw448", 31),
          ("qw48", 18),
          ("qw5", 5),
          ("qw512", 32),
          ("qw56", 19),
          ("qw6", 6),
          ("qw64", 20),
          ("qw640", 33),
          ("qw7", 7),
          ("qw768", 34),
          ("qw8", 8),
          ("qw80", 21),
          ("qw896", 35),
          ("qw96", 22))
    )


_WwpQos410Weight_Type.__name__ = "Integer32"
_WwpQos410Weight_Object = MibTableColumn
wwpQos410Weight = _WwpQos410Weight_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 7),
    _WwpQos410Weight_Type()
)
wwpQos410Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410Weight.setStatus("current")
_WwpQos410RowStatus_Type = RowStatus
_WwpQos410RowStatus_Object = MibTableColumn
wwpQos410RowStatus = _WwpQos410RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 8),
    _WwpQos410RowStatus_Type()
)
wwpQos410RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpQos410RowStatus.setStatus("current")
_WwpQos410StatsTable_Object = MibTable
wwpQos410StatsTable = _WwpQos410StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpQos410StatsTable.setStatus("current")
_WwpQos410StatsEntry_Object = MibTableRow
wwpQos410StatsEntry = _WwpQos410StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1)
)
wwpQos410StatsEntry.setIndexNames(
    (0, "WWP-QOS-410-MIB", "wwpQos410StatsVlanId"),
    (0, "WWP-QOS-410-MIB", "wwpQos410StatsIngressPortId"),
    (0, "WWP-QOS-410-MIB", "wwpQos410StatsEgressPortId"),
)
if mibBuilder.loadTexts:
    wwpQos410StatsEntry.setStatus("current")
_WwpQos410StatsVlanId_Type = VlanId
_WwpQos410StatsVlanId_Object = MibTableColumn
wwpQos410StatsVlanId = _WwpQos410StatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 1),
    _WwpQos410StatsVlanId_Type()
)
wwpQos410StatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410StatsVlanId.setStatus("current")


class _WwpQos410StatsIngressPortId_Type(Integer32):
    """Custom type wwpQos410StatsIngressPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQos410StatsIngressPortId_Type.__name__ = "Integer32"
_WwpQos410StatsIngressPortId_Object = MibTableColumn
wwpQos410StatsIngressPortId = _WwpQos410StatsIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 2),
    _WwpQos410StatsIngressPortId_Type()
)
wwpQos410StatsIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410StatsIngressPortId.setStatus("current")


class _WwpQos410StatsEgressPortId_Type(Integer32):
    """Custom type wwpQos410StatsEgressPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQos410StatsEgressPortId_Type.__name__ = "Integer32"
_WwpQos410StatsEgressPortId_Object = MibTableColumn
wwpQos410StatsEgressPortId = _WwpQos410StatsEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 3),
    _WwpQos410StatsEgressPortId_Type()
)
wwpQos410StatsEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410StatsEgressPortId.setStatus("current")


class _WwpQos410StatsType_Type(Integer32):
    """Custom type wwpQos410StatsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("discarded", 2))
    )


_WwpQos410StatsType_Type.__name__ = "Integer32"
_WwpQos410StatsType_Object = MibTableColumn
wwpQos410StatsType = _WwpQos410StatsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 4),
    _WwpQos410StatsType_Type()
)
wwpQos410StatsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410StatsType.setStatus("current")
_WwpQos410RxBytesHi_Type = Counter32
_WwpQos410RxBytesHi_Object = MibTableColumn
wwpQos410RxBytesHi = _WwpQos410RxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 5),
    _WwpQos410RxBytesHi_Type()
)
wwpQos410RxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410RxBytesHi.setStatus("current")
_WwpQos410RxBytesLo_Type = Counter32
_WwpQos410RxBytesLo_Object = MibTableColumn
wwpQos410RxBytesLo = _WwpQos410RxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 6),
    _WwpQos410RxBytesLo_Type()
)
wwpQos410RxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410RxBytesLo.setStatus("current")
_WwpQos410PriToQMapTable_Object = MibTable
wwpQos410PriToQMapTable = _WwpQos410PriToQMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpQos410PriToQMapTable.setStatus("current")
_WwpQos410PriToQMapEntry_Object = MibTableRow
wwpQos410PriToQMapEntry = _WwpQos410PriToQMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1)
)
wwpQos410PriToQMapEntry.setIndexNames(
    (0, "WWP-QOS-410-MIB", "wwpQos410RxPriority"),
)
if mibBuilder.loadTexts:
    wwpQos410PriToQMapEntry.setStatus("current")


class _WwpQos410RxPriority_Type(Integer32):
    """Custom type wwpQos410RxPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpQos410RxPriority_Type.__name__ = "Integer32"
_WwpQos410RxPriority_Object = MibTableColumn
wwpQos410RxPriority = _WwpQos410RxPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 1),
    _WwpQos410RxPriority_Type()
)
wwpQos410RxPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410RxPriority.setStatus("current")


class _WwpQos410TxPriQueue_Type(Integer32):
    """Custom type wwpQos410TxPriQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpQos410TxPriQueue_Type.__name__ = "Integer32"
_WwpQos410TxPriQueue_Object = MibTableColumn
wwpQos410TxPriQueue = _WwpQos410TxPriQueue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 2),
    _WwpQos410TxPriQueue_Type()
)
wwpQos410TxPriQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410TxPriQueue.setStatus("current")
_WwpQos410PortTable_Object = MibTable
wwpQos410PortTable = _WwpQos410PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpQos410PortTable.setStatus("current")
_WwpQos410PortEntry_Object = MibTableRow
wwpQos410PortEntry = _WwpQos410PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1)
)
wwpQos410PortEntry.setIndexNames(
    (0, "WWP-QOS-410-MIB", "wwpQos410PortIndex"),
)
if mibBuilder.loadTexts:
    wwpQos410PortEntry.setStatus("current")


class _WwpQos410PortIndex_Type(Integer32):
    """Custom type wwpQos410PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQos410PortIndex_Type.__name__ = "Integer32"
_WwpQos410PortIndex_Object = MibTableColumn
wwpQos410PortIndex = _WwpQos410PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 1),
    _WwpQos410PortIndex_Type()
)
wwpQos410PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410PortIndex.setStatus("current")


class _WwpQos410PortProvisionedBW_Type(Integer32):
    """Custom type wwpQos410PortProvisionedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpQos410PortProvisionedBW_Type.__name__ = "Integer32"
_WwpQos410PortProvisionedBW_Object = MibTableColumn
wwpQos410PortProvisionedBW = _WwpQos410PortProvisionedBW_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 2),
    _WwpQos410PortProvisionedBW_Type()
)
wwpQos410PortProvisionedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410PortProvisionedBW.setStatus("current")


class _WwpQos410PortTotalBW_Type(Integer32):
    """Custom type wwpQos410PortTotalBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpQos410PortTotalBW_Type.__name__ = "Integer32"
_WwpQos410PortTotalBW_Object = MibTableColumn
wwpQos410PortTotalBW = _WwpQos410PortTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 3),
    _WwpQos410PortTotalBW_Type()
)
wwpQos410PortTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQos410PortTotalBW.setStatus("current")


class _WwpQos410PortProvisionedNotifEnabled_Type(TruthValue):
    """Custom type wwpQos410PortProvisionedNotifEnabled based on TruthValue"""


_WwpQos410PortProvisionedNotifEnabled_Object = MibScalar
wwpQos410PortProvisionedNotifEnabled = _WwpQos410PortProvisionedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 5),
    _WwpQos410PortProvisionedNotifEnabled_Type()
)
wwpQos410PortProvisionedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQos410PortProvisionedNotifEnabled.setStatus("current")
_WwpQos410NotificationPrefix_ObjectIdentity = ObjectIdentity
wwpQos410NotificationPrefix = _WwpQos410NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 2)
)
_WwpQos410Notifications_ObjectIdentity = ObjectIdentity
wwpQos410Notifications = _WwpQos410Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0)
)
_WwpQos410MIBConformance_ObjectIdentity = ObjectIdentity
wwpQos410MIBConformance = _WwpQos410MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 3)
)
_WwpQos410MIBCompliances_ObjectIdentity = ObjectIdentity
wwpQos410MIBCompliances = _WwpQos410MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 1)
)
_WwpQos410MIBGroups_ObjectIdentity = ObjectIdentity
wwpQos410MIBGroups = _WwpQos410MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpQos410PortOverProvisionedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 1)
)
wwpQos410PortOverProvisionedTrap.setObjects(
    ("WWP-QOS-410-MIB", "wwpQos410PortIndex")
)
if mibBuilder.loadTexts:
    wwpQos410PortOverProvisionedTrap.setStatus(
        "current"
    )

wwpQos410PortUnderProvisionedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 2)
)
wwpQos410PortUnderProvisionedTrap.setObjects(
    ("WWP-QOS-410-MIB", "wwpQos410PortIndex")
)
if mibBuilder.loadTexts:
    wwpQos410PortUnderProvisionedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-QOS-410-MIB",
    **{"VlanId": VlanId,
       "wwpQos410MIB": wwpQos410MIB,
       "wwpQos410MIBObjects": wwpQos410MIBObjects,
       "wwpQos410": wwpQos410,
       "wwpQos410Table": wwpQos410Table,
       "wwpQos410Entry": wwpQos410Entry,
       "wwpQos410VlanId": wwpQos410VlanId,
       "wwpQos410IngressPortId": wwpQos410IngressPortId,
       "wwpQos410EgressPortId": wwpQos410EgressPortId,
       "wwpQos410MinRateLimit": wwpQos410MinRateLimit,
       "wwpQos410MaxRateLimit": wwpQos410MaxRateLimit,
       "wwpQos410QueueSize": wwpQos410QueueSize,
       "wwpQos410Weight": wwpQos410Weight,
       "wwpQos410RowStatus": wwpQos410RowStatus,
       "wwpQos410StatsTable": wwpQos410StatsTable,
       "wwpQos410StatsEntry": wwpQos410StatsEntry,
       "wwpQos410StatsVlanId": wwpQos410StatsVlanId,
       "wwpQos410StatsIngressPortId": wwpQos410StatsIngressPortId,
       "wwpQos410StatsEgressPortId": wwpQos410StatsEgressPortId,
       "wwpQos410StatsType": wwpQos410StatsType,
       "wwpQos410RxBytesHi": wwpQos410RxBytesHi,
       "wwpQos410RxBytesLo": wwpQos410RxBytesLo,
       "wwpQos410PriToQMapTable": wwpQos410PriToQMapTable,
       "wwpQos410PriToQMapEntry": wwpQos410PriToQMapEntry,
       "wwpQos410RxPriority": wwpQos410RxPriority,
       "wwpQos410TxPriQueue": wwpQos410TxPriQueue,
       "wwpQos410PortTable": wwpQos410PortTable,
       "wwpQos410PortEntry": wwpQos410PortEntry,
       "wwpQos410PortIndex": wwpQos410PortIndex,
       "wwpQos410PortProvisionedBW": wwpQos410PortProvisionedBW,
       "wwpQos410PortTotalBW": wwpQos410PortTotalBW,
       "wwpQos410PortProvisionedNotifEnabled": wwpQos410PortProvisionedNotifEnabled,
       "wwpQos410NotificationPrefix": wwpQos410NotificationPrefix,
       "wwpQos410Notifications": wwpQos410Notifications,
       "wwpQos410PortOverProvisionedTrap": wwpQos410PortOverProvisionedTrap,
       "wwpQos410PortUnderProvisionedTrap": wwpQos410PortUnderProvisionedTrap,
       "wwpQos410MIBConformance": wwpQos410MIBConformance,
       "wwpQos410MIBCompliances": wwpQos410MIBCompliances,
       "wwpQos410MIBGroups": wwpQos410MIBGroups}
)
