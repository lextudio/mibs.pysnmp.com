# SNMP MIB module (HUAWEI-TUNNEL-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TUNNEL-TE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:19 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsExtendedTunnelId,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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
 Bits,
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwTunnelTeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151)
)
hwTunnelTeMib.setRevisions(
        ("2013-08-28 17:26",
         "2006-06-30 15:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTunnelTeMibObject_ObjectIdentity = ObjectIdentity
hwTunnelTeMibObject = _HwTunnelTeMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1)
)
_HwTunnelDiffServTable_Object = MibTable
hwTunnelDiffServTable = _HwTunnelDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1)
)
if mibBuilder.loadTexts:
    hwTunnelDiffServTable.setStatus("current")
_HwTunnelDiffServEntry_Object = MibTableRow
hwTunnelDiffServEntry = _HwTunnelDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1)
)
hwTunnelDiffServEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelDiffServIndex"),
)
if mibBuilder.loadTexts:
    hwTunnelDiffServEntry.setStatus("current")
_HwTunnelDiffServIndex_Type = InterfaceIndex
_HwTunnelDiffServIndex_Object = MibTableColumn
hwTunnelDiffServIndex = _HwTunnelDiffServIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1, 1),
    _HwTunnelDiffServIndex_Type()
)
hwTunnelDiffServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelDiffServIndex.setStatus("current")


class _HwTunnelDiffServMode_Type(Integer32):
    """Custom type hwTunnelDiffServMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("uniform", 2))
    )


_HwTunnelDiffServMode_Type.__name__ = "Integer32"
_HwTunnelDiffServMode_Object = MibTableColumn
hwTunnelDiffServMode = _HwTunnelDiffServMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1, 2),
    _HwTunnelDiffServMode_Type()
)
hwTunnelDiffServMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelDiffServMode.setStatus("current")


class _HwTunnelDiffServServiceClass_Type(Integer32):
    """Custom type hwTunnelDiffServServiceClass based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("invalidClass", 255))
    )


_HwTunnelDiffServServiceClass_Type.__name__ = "Integer32"
_HwTunnelDiffServServiceClass_Object = MibTableColumn
hwTunnelDiffServServiceClass = _HwTunnelDiffServServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1, 3),
    _HwTunnelDiffServServiceClass_Type()
)
hwTunnelDiffServServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelDiffServServiceClass.setStatus("current")


class _HwTunnelDiffServColor_Type(Integer32):
    """Custom type hwTunnelDiffServColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("invalidColor", 255),
          ("red", 3),
          ("yellow", 2))
    )


_HwTunnelDiffServColor_Type.__name__ = "Integer32"
_HwTunnelDiffServColor_Object = MibTableColumn
hwTunnelDiffServColor = _HwTunnelDiffServColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1, 4),
    _HwTunnelDiffServColor_Type()
)
hwTunnelDiffServColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelDiffServColor.setStatus("current")


class _HwTunnelTeFlowQueue_Type(OctetString):
    """Custom type hwTunnelTeFlowQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwTunnelTeFlowQueue_Type.__name__ = "OctetString"
_HwTunnelTeFlowQueue_Object = MibTableColumn
hwTunnelTeFlowQueue = _HwTunnelTeFlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 1, 1, 5),
    _HwTunnelTeFlowQueue_Type()
)
hwTunnelTeFlowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeFlowQueue.setStatus("current")
_HwTunnelTeVsiTable_Object = MibTable
hwTunnelTeVsiTable = _HwTunnelTeVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2)
)
if mibBuilder.loadTexts:
    hwTunnelTeVsiTable.setStatus("obsolete")
_HwTunnelTeVsiEntry_Object = MibTableRow
hwTunnelTeVsiEntry = _HwTunnelTeVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1)
)
hwTunnelTeVsiEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVsiIndex"),
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVsiName"),
)
if mibBuilder.loadTexts:
    hwTunnelTeVsiEntry.setStatus("obsolete")
_HwTunnelTeVsiIndex_Type = InterfaceIndex
_HwTunnelTeVsiIndex_Object = MibTableColumn
hwTunnelTeVsiIndex = _HwTunnelTeVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1, 1),
    _HwTunnelTeVsiIndex_Type()
)
hwTunnelTeVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeVsiIndex.setStatus("obsolete")


class _HwTunnelTeVsiName_Type(OctetString):
    """Custom type hwTunnelTeVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwTunnelTeVsiName_Type.__name__ = "OctetString"
_HwTunnelTeVsiName_Object = MibTableColumn
hwTunnelTeVsiName = _HwTunnelTeVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1, 2),
    _HwTunnelTeVsiName_Type()
)
hwTunnelTeVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeVsiName.setStatus("obsolete")


class _HwTunnelTeVsiCir_Type(Integer32):
    """Custom type hwTunnelTeVsiCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeVsiCir_Type.__name__ = "Integer32"
_HwTunnelTeVsiCir_Object = MibTableColumn
hwTunnelTeVsiCir = _HwTunnelTeVsiCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1, 3),
    _HwTunnelTeVsiCir_Type()
)
hwTunnelTeVsiCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVsiCir.setStatus("obsolete")


class _HwTunnelTeVsiPir_Type(Integer32):
    """Custom type hwTunnelTeVsiPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeVsiPir_Type.__name__ = "Integer32"
_HwTunnelTeVsiPir_Object = MibTableColumn
hwTunnelTeVsiPir = _HwTunnelTeVsiPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1, 4),
    _HwTunnelTeVsiPir_Type()
)
hwTunnelTeVsiPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVsiPir.setStatus("obsolete")


class _HwTunnelTeVsiFlowQueue_Type(OctetString):
    """Custom type hwTunnelTeVsiFlowQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwTunnelTeVsiFlowQueue_Type.__name__ = "OctetString"
_HwTunnelTeVsiFlowQueue_Object = MibTableColumn
hwTunnelTeVsiFlowQueue = _HwTunnelTeVsiFlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 2, 1, 5),
    _HwTunnelTeVsiFlowQueue_Type()
)
hwTunnelTeVsiFlowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVsiFlowQueue.setStatus("obsolete")
_HwTunnelTeVllTable_Object = MibTable
hwTunnelTeVllTable = _HwTunnelTeVllTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3)
)
if mibBuilder.loadTexts:
    hwTunnelTeVllTable.setStatus("obsolete")
_HwTunnelTeVllEntry_Object = MibTableRow
hwTunnelTeVllEntry = _HwTunnelTeVllEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1)
)
hwTunnelTeVllEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVllIndex"),
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVllInterfaceName"),
)
if mibBuilder.loadTexts:
    hwTunnelTeVllEntry.setStatus("obsolete")
_HwTunnelTeVllIndex_Type = InterfaceIndex
_HwTunnelTeVllIndex_Object = MibTableColumn
hwTunnelTeVllIndex = _HwTunnelTeVllIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1, 1),
    _HwTunnelTeVllIndex_Type()
)
hwTunnelTeVllIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeVllIndex.setStatus("obsolete")


class _HwTunnelTeVllInterfaceName_Type(OctetString):
    """Custom type hwTunnelTeVllInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwTunnelTeVllInterfaceName_Type.__name__ = "OctetString"
_HwTunnelTeVllInterfaceName_Object = MibTableColumn
hwTunnelTeVllInterfaceName = _HwTunnelTeVllInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1, 2),
    _HwTunnelTeVllInterfaceName_Type()
)
hwTunnelTeVllInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeVllInterfaceName.setStatus("obsolete")


class _HwTunnelTeVllCir_Type(Integer32):
    """Custom type hwTunnelTeVllCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeVllCir_Type.__name__ = "Integer32"
_HwTunnelTeVllCir_Object = MibTableColumn
hwTunnelTeVllCir = _HwTunnelTeVllCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1, 3),
    _HwTunnelTeVllCir_Type()
)
hwTunnelTeVllCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVllCir.setStatus("obsolete")


class _HwTunnelTeVllPir_Type(Integer32):
    """Custom type hwTunnelTeVllPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeVllPir_Type.__name__ = "Integer32"
_HwTunnelTeVllPir_Object = MibTableColumn
hwTunnelTeVllPir = _HwTunnelTeVllPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1, 4),
    _HwTunnelTeVllPir_Type()
)
hwTunnelTeVllPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVllPir.setStatus("obsolete")


class _HwTunnelTeVllFlowQueue_Type(OctetString):
    """Custom type hwTunnelTeVllFlowQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwTunnelTeVllFlowQueue_Type.__name__ = "OctetString"
_HwTunnelTeVllFlowQueue_Object = MibTableColumn
hwTunnelTeVllFlowQueue = _HwTunnelTeVllFlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 3, 1, 5),
    _HwTunnelTeVllFlowQueue_Type()
)
hwTunnelTeVllFlowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeVllFlowQueue.setStatus("obsolete")
_HwTunnelTeL3vpnTable_Object = MibTable
hwTunnelTeL3vpnTable = _HwTunnelTeL3vpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4)
)
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnTable.setStatus("obsolete")
_HwTunnelTeL3vpnEntry_Object = MibTableRow
hwTunnelTeL3vpnEntry = _HwTunnelTeL3vpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1)
)
hwTunnelTeL3vpnEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeL3vpnIndex"),
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeL3vpnName"),
)
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnEntry.setStatus("obsolete")
_HwTunnelTeL3vpnIndex_Type = InterfaceIndex
_HwTunnelTeL3vpnIndex_Object = MibTableColumn
hwTunnelTeL3vpnIndex = _HwTunnelTeL3vpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1, 1),
    _HwTunnelTeL3vpnIndex_Type()
)
hwTunnelTeL3vpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnIndex.setStatus("obsolete")


class _HwTunnelTeL3vpnName_Type(OctetString):
    """Custom type hwTunnelTeL3vpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwTunnelTeL3vpnName_Type.__name__ = "OctetString"
_HwTunnelTeL3vpnName_Object = MibTableColumn
hwTunnelTeL3vpnName = _HwTunnelTeL3vpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1, 2),
    _HwTunnelTeL3vpnName_Type()
)
hwTunnelTeL3vpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnName.setStatus("obsolete")


class _HwTunnelTeL3vpnCir_Type(Integer32):
    """Custom type hwTunnelTeL3vpnCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeL3vpnCir_Type.__name__ = "Integer32"
_HwTunnelTeL3vpnCir_Object = MibTableColumn
hwTunnelTeL3vpnCir = _HwTunnelTeL3vpnCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1, 3),
    _HwTunnelTeL3vpnCir_Type()
)
hwTunnelTeL3vpnCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnCir.setStatus("obsolete")


class _HwTunnelTeL3vpnPir_Type(Integer32):
    """Custom type hwTunnelTeL3vpnPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwTunnelTeL3vpnPir_Type.__name__ = "Integer32"
_HwTunnelTeL3vpnPir_Object = MibTableColumn
hwTunnelTeL3vpnPir = _HwTunnelTeL3vpnPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1, 4),
    _HwTunnelTeL3vpnPir_Type()
)
hwTunnelTeL3vpnPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnPir.setStatus("obsolete")


class _HwTunnelTeL3vpnFlowQueue_Type(OctetString):
    """Custom type hwTunnelTeL3vpnFlowQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwTunnelTeL3vpnFlowQueue_Type.__name__ = "OctetString"
_HwTunnelTeL3vpnFlowQueue_Object = MibTableColumn
hwTunnelTeL3vpnFlowQueue = _HwTunnelTeL3vpnFlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 4, 1, 5),
    _HwTunnelTeL3vpnFlowQueue_Type()
)
hwTunnelTeL3vpnFlowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnFlowQueue.setStatus("obsolete")
_HwTunnelTeStatisticsTable_Object = MibTable
hwTunnelTeStatisticsTable = _HwTunnelTeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 5)
)
if mibBuilder.loadTexts:
    hwTunnelTeStatisticsTable.setStatus("current")
_HwTunnelTeStatisticsEntry_Object = MibTableRow
hwTunnelTeStatisticsEntry = _HwTunnelTeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 5, 1)
)
hwTunnelTeStatisticsEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    hwTunnelTeStatisticsEntry.setStatus("current")
_HwTunnelTeStatisticsIfIndex_Type = InterfaceIndex
_HwTunnelTeStatisticsIfIndex_Object = MibTableColumn
hwTunnelTeStatisticsIfIndex = _HwTunnelTeStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 5, 1, 1),
    _HwTunnelTeStatisticsIfIndex_Type()
)
hwTunnelTeStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelTeStatisticsIfIndex.setStatus("current")
_HwTunnelTeUpDownStatistics_Type = Unsigned32
_HwTunnelTeUpDownStatistics_Object = MibTableColumn
hwTunnelTeUpDownStatistics = _HwTunnelTeUpDownStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 5, 1, 2),
    _HwTunnelTeUpDownStatistics_Type()
)
hwTunnelTeUpDownStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelTeUpDownStatistics.setStatus("current")
_HwTunnTeCounterDiscontinuityTime_Type = TimeStamp
_HwTunnTeCounterDiscontinuityTime_Object = MibTableColumn
hwTunnTeCounterDiscontinuityTime = _HwTunnTeCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 5, 1, 3),
    _HwTunnTeCounterDiscontinuityTime_Type()
)
hwTunnTeCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnTeCounterDiscontinuityTime.setStatus("current")
_HwCtTemplateTable_Object = MibTable
hwCtTemplateTable = _HwCtTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6)
)
if mibBuilder.loadTexts:
    hwCtTemplateTable.setStatus("current")
_HwCtTemplateEntry_Object = MibTableRow
hwCtTemplateEntry = _HwCtTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1)
)
hwCtTemplateEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateIndex"),
)
if mibBuilder.loadTexts:
    hwCtTemplateEntry.setStatus("current")


class _HwCtTemplateIndex_Type(Integer32):
    """Custom type hwCtTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwCtTemplateIndex_Type.__name__ = "Integer32"
_HwCtTemplateIndex_Object = MibTableColumn
hwCtTemplateIndex = _HwCtTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 1),
    _HwCtTemplateIndex_Type()
)
hwCtTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCtTemplateIndex.setStatus("current")


class _HwCtTemplateName_Type(OctetString):
    """Custom type hwCtTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HwCtTemplateName_Type.__name__ = "OctetString"
_HwCtTemplateName_Object = MibTableColumn
hwCtTemplateName = _HwCtTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 2),
    _HwCtTemplateName_Type()
)
hwCtTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateName.setStatus("current")
_HwCtTemplateCt0_Type = Unsigned32
_HwCtTemplateCt0_Object = MibTableColumn
hwCtTemplateCt0 = _HwCtTemplateCt0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 3),
    _HwCtTemplateCt0_Type()
)
hwCtTemplateCt0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt0.setStatus("current")


class _HwCtTemplateCt1_Type(Unsigned32):
    """Custom type hwCtTemplateCt1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt1_Type.__name__ = "Unsigned32"
_HwCtTemplateCt1_Object = MibTableColumn
hwCtTemplateCt1 = _HwCtTemplateCt1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 4),
    _HwCtTemplateCt1_Type()
)
hwCtTemplateCt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt1.setStatus("current")


class _HwCtTemplateCt2_Type(Unsigned32):
    """Custom type hwCtTemplateCt2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt2_Type.__name__ = "Unsigned32"
_HwCtTemplateCt2_Object = MibTableColumn
hwCtTemplateCt2 = _HwCtTemplateCt2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 5),
    _HwCtTemplateCt2_Type()
)
hwCtTemplateCt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt2.setStatus("current")


class _HwCtTemplateCt3_Type(Unsigned32):
    """Custom type hwCtTemplateCt3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt3_Type.__name__ = "Unsigned32"
_HwCtTemplateCt3_Object = MibTableColumn
hwCtTemplateCt3 = _HwCtTemplateCt3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 6),
    _HwCtTemplateCt3_Type()
)
hwCtTemplateCt3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt3.setStatus("current")


class _HwCtTemplateCt4_Type(Unsigned32):
    """Custom type hwCtTemplateCt4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt4_Type.__name__ = "Unsigned32"
_HwCtTemplateCt4_Object = MibTableColumn
hwCtTemplateCt4 = _HwCtTemplateCt4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 7),
    _HwCtTemplateCt4_Type()
)
hwCtTemplateCt4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt4.setStatus("current")


class _HwCtTemplateCt5_Type(Unsigned32):
    """Custom type hwCtTemplateCt5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt5_Type.__name__ = "Unsigned32"
_HwCtTemplateCt5_Object = MibTableColumn
hwCtTemplateCt5 = _HwCtTemplateCt5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 8),
    _HwCtTemplateCt5_Type()
)
hwCtTemplateCt5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt5.setStatus("current")


class _HwCtTemplateCt6_Type(Unsigned32):
    """Custom type hwCtTemplateCt6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt6_Type.__name__ = "Unsigned32"
_HwCtTemplateCt6_Object = MibTableColumn
hwCtTemplateCt6 = _HwCtTemplateCt6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 9),
    _HwCtTemplateCt6_Type()
)
hwCtTemplateCt6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt6.setStatus("current")


class _HwCtTemplateCt7_Type(Unsigned32):
    """Custom type hwCtTemplateCt7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtTemplateCt7_Type.__name__ = "Unsigned32"
_HwCtTemplateCt7_Object = MibTableColumn
hwCtTemplateCt7 = _HwCtTemplateCt7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 10),
    _HwCtTemplateCt7_Type()
)
hwCtTemplateCt7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCt7.setStatus("current")


class _HwCtTemplateCommit_Type(Integer32):
    """Custom type hwCtTemplateCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("notCommit", 1))
    )


_HwCtTemplateCommit_Type.__name__ = "Integer32"
_HwCtTemplateCommit_Object = MibTableColumn
hwCtTemplateCommit = _HwCtTemplateCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 11),
    _HwCtTemplateCommit_Type()
)
hwCtTemplateCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateCommit.setStatus("current")
_HwCtTemplateRowStatus_Type = RowStatus
_HwCtTemplateRowStatus_Object = MibTableColumn
hwCtTemplateRowStatus = _HwCtTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 6, 1, 12),
    _HwCtTemplateRowStatus_Type()
)
hwCtTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtTemplateRowStatus.setStatus("current")
_HwCtConfigTunnelCtTable_Object = MibTable
hwCtConfigTunnelCtTable = _HwCtConfigTunnelCtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7)
)
if mibBuilder.loadTexts:
    hwCtConfigTunnelCtTable.setStatus("current")
_HwCtConfigTunnelCtEntry_Object = MibTableRow
hwCtConfigTunnelCtEntry = _HwCtConfigTunnelCtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1)
)
hwCtConfigTunnelCtEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCtIfIndex"),
)
if mibBuilder.loadTexts:
    hwCtConfigTunnelCtEntry.setStatus("current")
_HwCtConfigTunnelCtIfIndex_Type = InterfaceIndex
_HwCtConfigTunnelCtIfIndex_Object = MibTableColumn
hwCtConfigTunnelCtIfIndex = _HwCtConfigTunnelCtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 1),
    _HwCtConfigTunnelCtIfIndex_Type()
)
hwCtConfigTunnelCtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCtIfIndex.setStatus("current")


class _HwCtConfigTunnelName_Type(OctetString):
    """Custom type hwCtConfigTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCtConfigTunnelName_Type.__name__ = "OctetString"
_HwCtConfigTunnelName_Object = MibTableColumn
hwCtConfigTunnelName = _HwCtConfigTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 2),
    _HwCtConfigTunnelName_Type()
)
hwCtConfigTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelName.setStatus("current")


class _HwCtConfigTunnelCommit_Type(Integer32):
    """Custom type hwCtConfigTunnelCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("notCommit", 1))
    )


_HwCtConfigTunnelCommit_Type.__name__ = "Integer32"
_HwCtConfigTunnelCommit_Object = MibTableColumn
hwCtConfigTunnelCommit = _HwCtConfigTunnelCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 3),
    _HwCtConfigTunnelCommit_Type()
)
hwCtConfigTunnelCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCommit.setStatus("current")


class _HwCtConfigTemplateName_Type(OctetString):
    """Custom type hwCtConfigTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HwCtConfigTemplateName_Type.__name__ = "OctetString"
_HwCtConfigTemplateName_Object = MibTableColumn
hwCtConfigTemplateName = _HwCtConfigTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 4),
    _HwCtConfigTemplateName_Type()
)
hwCtConfigTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTemplateName.setStatus("current")


class _HwCtConfigTunnelCt0Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt0Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt0Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt0Band_Object = MibTableColumn
hwCtConfigTunnelCt0Band = _HwCtConfigTunnelCt0Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 5),
    _HwCtConfigTunnelCt0Band_Type()
)
hwCtConfigTunnelCt0Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt0Band.setStatus("current")


class _HwCtConfigTunnelCt1Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt1Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt1Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt1Band_Object = MibTableColumn
hwCtConfigTunnelCt1Band = _HwCtConfigTunnelCt1Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 6),
    _HwCtConfigTunnelCt1Band_Type()
)
hwCtConfigTunnelCt1Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt1Band.setStatus("current")


class _HwCtConfigTunnelCt2Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt2Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt2Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt2Band_Object = MibTableColumn
hwCtConfigTunnelCt2Band = _HwCtConfigTunnelCt2Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 7),
    _HwCtConfigTunnelCt2Band_Type()
)
hwCtConfigTunnelCt2Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt2Band.setStatus("current")


class _HwCtConfigTunnelCt3Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt3Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt3Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt3Band_Object = MibTableColumn
hwCtConfigTunnelCt3Band = _HwCtConfigTunnelCt3Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 8),
    _HwCtConfigTunnelCt3Band_Type()
)
hwCtConfigTunnelCt3Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt3Band.setStatus("current")


class _HwCtConfigTunnelCt4Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt4Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt4Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt4Band_Object = MibTableColumn
hwCtConfigTunnelCt4Band = _HwCtConfigTunnelCt4Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 9),
    _HwCtConfigTunnelCt4Band_Type()
)
hwCtConfigTunnelCt4Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt4Band.setStatus("current")


class _HwCtConfigTunnelCt5Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt5Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt5Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt5Band_Object = MibTableColumn
hwCtConfigTunnelCt5Band = _HwCtConfigTunnelCt5Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 10),
    _HwCtConfigTunnelCt5Band_Type()
)
hwCtConfigTunnelCt5Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt5Band.setStatus("current")


class _HwCtConfigTunnelCt6Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt6Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt6Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt6Band_Object = MibTableColumn
hwCtConfigTunnelCt6Band = _HwCtConfigTunnelCt6Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 11),
    _HwCtConfigTunnelCt6Band_Type()
)
hwCtConfigTunnelCt6Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt6Band.setStatus("current")


class _HwCtConfigTunnelCt7Band_Type(Unsigned32):
    """Custom type hwCtConfigTunnelCt7Band based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwCtConfigTunnelCt7Band_Type.__name__ = "Unsigned32"
_HwCtConfigTunnelCt7Band_Object = MibTableColumn
hwCtConfigTunnelCt7Band = _HwCtConfigTunnelCt7Band_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 7, 1, 12),
    _HwCtConfigTunnelCt7Band_Type()
)
hwCtConfigTunnelCt7Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtConfigTunnelCt7Band.setStatus("current")
_HwCtStatisticsTable_Object = MibTable
hwCtStatisticsTable = _HwCtStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8)
)
if mibBuilder.loadTexts:
    hwCtStatisticsTable.setStatus("current")
_HwCtStatisticsEntry_Object = MibTableRow
hwCtStatisticsEntry = _HwCtStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1)
)
hwCtStatisticsEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    hwCtStatisticsEntry.setStatus("current")
_HwCtStatisticsIfIndex_Type = InterfaceIndex
_HwCtStatisticsIfIndex_Object = MibTableColumn
hwCtStatisticsIfIndex = _HwCtStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 1),
    _HwCtStatisticsIfIndex_Type()
)
hwCtStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCtStatisticsIfIndex.setStatus("current")


class _HwCtStatisticsTunnelName_Type(OctetString):
    """Custom type hwCtStatisticsTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCtStatisticsTunnelName_Type.__name__ = "OctetString"
_HwCtStatisticsTunnelName_Object = MibTableColumn
hwCtStatisticsTunnelName = _HwCtStatisticsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 2),
    _HwCtStatisticsTunnelName_Type()
)
hwCtStatisticsTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsTunnelName.setStatus("current")
_HwCtStatisticsCt0OutByteRate_Type = Counter64
_HwCtStatisticsCt0OutByteRate_Object = MibTableColumn
hwCtStatisticsCt0OutByteRate = _HwCtStatisticsCt0OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 3),
    _HwCtStatisticsCt0OutByteRate_Type()
)
hwCtStatisticsCt0OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt0OutByteRate.setStatus("current")
_HwCtStatisticsCt0OutPktRate_Type = Counter64
_HwCtStatisticsCt0OutPktRate_Object = MibTableColumn
hwCtStatisticsCt0OutPktRate = _HwCtStatisticsCt0OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 4),
    _HwCtStatisticsCt0OutPktRate_Type()
)
hwCtStatisticsCt0OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt0OutPktRate.setStatus("current")
_HwCtStatisticsCt0OutPkt_Type = Counter64
_HwCtStatisticsCt0OutPkt_Object = MibTableColumn
hwCtStatisticsCt0OutPkt = _HwCtStatisticsCt0OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 5),
    _HwCtStatisticsCt0OutPkt_Type()
)
hwCtStatisticsCt0OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt0OutPkt.setStatus("current")
_HwCtStatisticsCt0OutPktByte_Type = Counter64
_HwCtStatisticsCt0OutPktByte_Object = MibTableColumn
hwCtStatisticsCt0OutPktByte = _HwCtStatisticsCt0OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 6),
    _HwCtStatisticsCt0OutPktByte_Type()
)
hwCtStatisticsCt0OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt0OutPktByte.setStatus("current")
_HwCtStatisticsCt0OutErrorPkt_Type = Counter64
_HwCtStatisticsCt0OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt0OutErrorPkt = _HwCtStatisticsCt0OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 7),
    _HwCtStatisticsCt0OutErrorPkt_Type()
)
hwCtStatisticsCt0OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt0OutErrorPkt.setStatus("current")
_HwCtStatisticsCt1OutByteRate_Type = Counter64
_HwCtStatisticsCt1OutByteRate_Object = MibTableColumn
hwCtStatisticsCt1OutByteRate = _HwCtStatisticsCt1OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 8),
    _HwCtStatisticsCt1OutByteRate_Type()
)
hwCtStatisticsCt1OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt1OutByteRate.setStatus("current")
_HwCtStatisticsCt1OutPktRate_Type = Counter64
_HwCtStatisticsCt1OutPktRate_Object = MibTableColumn
hwCtStatisticsCt1OutPktRate = _HwCtStatisticsCt1OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 9),
    _HwCtStatisticsCt1OutPktRate_Type()
)
hwCtStatisticsCt1OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt1OutPktRate.setStatus("current")
_HwCtStatisticsCt1OutPkt_Type = Counter64
_HwCtStatisticsCt1OutPkt_Object = MibTableColumn
hwCtStatisticsCt1OutPkt = _HwCtStatisticsCt1OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 10),
    _HwCtStatisticsCt1OutPkt_Type()
)
hwCtStatisticsCt1OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt1OutPkt.setStatus("current")
_HwCtStatisticsCt1OutPktByte_Type = Counter64
_HwCtStatisticsCt1OutPktByte_Object = MibTableColumn
hwCtStatisticsCt1OutPktByte = _HwCtStatisticsCt1OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 11),
    _HwCtStatisticsCt1OutPktByte_Type()
)
hwCtStatisticsCt1OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt1OutPktByte.setStatus("current")
_HwCtStatisticsCt1OutErrorPkt_Type = Counter64
_HwCtStatisticsCt1OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt1OutErrorPkt = _HwCtStatisticsCt1OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 12),
    _HwCtStatisticsCt1OutErrorPkt_Type()
)
hwCtStatisticsCt1OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt1OutErrorPkt.setStatus("current")
_HwCtStatisticsCt2OutByteRate_Type = Counter64
_HwCtStatisticsCt2OutByteRate_Object = MibTableColumn
hwCtStatisticsCt2OutByteRate = _HwCtStatisticsCt2OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 13),
    _HwCtStatisticsCt2OutByteRate_Type()
)
hwCtStatisticsCt2OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt2OutByteRate.setStatus("current")
_HwCtStatisticsCt2OutPktRate_Type = Counter64
_HwCtStatisticsCt2OutPktRate_Object = MibTableColumn
hwCtStatisticsCt2OutPktRate = _HwCtStatisticsCt2OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 14),
    _HwCtStatisticsCt2OutPktRate_Type()
)
hwCtStatisticsCt2OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt2OutPktRate.setStatus("current")
_HwCtStatisticsCt2OutPkt_Type = Counter64
_HwCtStatisticsCt2OutPkt_Object = MibTableColumn
hwCtStatisticsCt2OutPkt = _HwCtStatisticsCt2OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 15),
    _HwCtStatisticsCt2OutPkt_Type()
)
hwCtStatisticsCt2OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt2OutPkt.setStatus("current")
_HwCtStatisticsCt2OutPktByte_Type = Counter64
_HwCtStatisticsCt2OutPktByte_Object = MibTableColumn
hwCtStatisticsCt2OutPktByte = _HwCtStatisticsCt2OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 16),
    _HwCtStatisticsCt2OutPktByte_Type()
)
hwCtStatisticsCt2OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt2OutPktByte.setStatus("current")
_HwCtStatisticsCt2OutErrorPkt_Type = Counter64
_HwCtStatisticsCt2OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt2OutErrorPkt = _HwCtStatisticsCt2OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 17),
    _HwCtStatisticsCt2OutErrorPkt_Type()
)
hwCtStatisticsCt2OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt2OutErrorPkt.setStatus("current")
_HwCtStatisticsCt3OutByteRate_Type = Counter64
_HwCtStatisticsCt3OutByteRate_Object = MibTableColumn
hwCtStatisticsCt3OutByteRate = _HwCtStatisticsCt3OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 18),
    _HwCtStatisticsCt3OutByteRate_Type()
)
hwCtStatisticsCt3OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt3OutByteRate.setStatus("current")
_HwCtStatisticsCt3OutPktRate_Type = Counter64
_HwCtStatisticsCt3OutPktRate_Object = MibTableColumn
hwCtStatisticsCt3OutPktRate = _HwCtStatisticsCt3OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 19),
    _HwCtStatisticsCt3OutPktRate_Type()
)
hwCtStatisticsCt3OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt3OutPktRate.setStatus("current")
_HwCtStatisticsCt3OutPkt_Type = Counter64
_HwCtStatisticsCt3OutPkt_Object = MibTableColumn
hwCtStatisticsCt3OutPkt = _HwCtStatisticsCt3OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 20),
    _HwCtStatisticsCt3OutPkt_Type()
)
hwCtStatisticsCt3OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt3OutPkt.setStatus("current")
_HwCtStatisticsCt3OutPktByte_Type = Counter64
_HwCtStatisticsCt3OutPktByte_Object = MibTableColumn
hwCtStatisticsCt3OutPktByte = _HwCtStatisticsCt3OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 21),
    _HwCtStatisticsCt3OutPktByte_Type()
)
hwCtStatisticsCt3OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt3OutPktByte.setStatus("current")
_HwCtStatisticsCt3OutErrorPkt_Type = Counter64
_HwCtStatisticsCt3OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt3OutErrorPkt = _HwCtStatisticsCt3OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 22),
    _HwCtStatisticsCt3OutErrorPkt_Type()
)
hwCtStatisticsCt3OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt3OutErrorPkt.setStatus("current")
_HwCtStatisticsCt4OutByteRate_Type = Counter64
_HwCtStatisticsCt4OutByteRate_Object = MibTableColumn
hwCtStatisticsCt4OutByteRate = _HwCtStatisticsCt4OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 23),
    _HwCtStatisticsCt4OutByteRate_Type()
)
hwCtStatisticsCt4OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt4OutByteRate.setStatus("current")
_HwCtStatisticsCt4OutPktRate_Type = Counter64
_HwCtStatisticsCt4OutPktRate_Object = MibTableColumn
hwCtStatisticsCt4OutPktRate = _HwCtStatisticsCt4OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 24),
    _HwCtStatisticsCt4OutPktRate_Type()
)
hwCtStatisticsCt4OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt4OutPktRate.setStatus("current")
_HwCtStatisticsCt4OutPkt_Type = Counter64
_HwCtStatisticsCt4OutPkt_Object = MibTableColumn
hwCtStatisticsCt4OutPkt = _HwCtStatisticsCt4OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 25),
    _HwCtStatisticsCt4OutPkt_Type()
)
hwCtStatisticsCt4OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt4OutPkt.setStatus("current")
_HwCtStatisticsCt4OutPktByte_Type = Counter64
_HwCtStatisticsCt4OutPktByte_Object = MibTableColumn
hwCtStatisticsCt4OutPktByte = _HwCtStatisticsCt4OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 26),
    _HwCtStatisticsCt4OutPktByte_Type()
)
hwCtStatisticsCt4OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt4OutPktByte.setStatus("current")
_HwCtStatisticsCt4OutErrorPkt_Type = Counter64
_HwCtStatisticsCt4OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt4OutErrorPkt = _HwCtStatisticsCt4OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 27),
    _HwCtStatisticsCt4OutErrorPkt_Type()
)
hwCtStatisticsCt4OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt4OutErrorPkt.setStatus("current")
_HwCtStatisticsCt5OutByteRate_Type = Counter64
_HwCtStatisticsCt5OutByteRate_Object = MibTableColumn
hwCtStatisticsCt5OutByteRate = _HwCtStatisticsCt5OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 28),
    _HwCtStatisticsCt5OutByteRate_Type()
)
hwCtStatisticsCt5OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt5OutByteRate.setStatus("current")
_HwCtStatisticsCt5OutPktRate_Type = Counter64
_HwCtStatisticsCt5OutPktRate_Object = MibTableColumn
hwCtStatisticsCt5OutPktRate = _HwCtStatisticsCt5OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 29),
    _HwCtStatisticsCt5OutPktRate_Type()
)
hwCtStatisticsCt5OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt5OutPktRate.setStatus("current")
_HwCtStatisticsCt5OutPkt_Type = Counter64
_HwCtStatisticsCt5OutPkt_Object = MibTableColumn
hwCtStatisticsCt5OutPkt = _HwCtStatisticsCt5OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 30),
    _HwCtStatisticsCt5OutPkt_Type()
)
hwCtStatisticsCt5OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt5OutPkt.setStatus("current")
_HwCtStatisticsCt5OutPktByte_Type = Counter64
_HwCtStatisticsCt5OutPktByte_Object = MibTableColumn
hwCtStatisticsCt5OutPktByte = _HwCtStatisticsCt5OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 31),
    _HwCtStatisticsCt5OutPktByte_Type()
)
hwCtStatisticsCt5OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt5OutPktByte.setStatus("current")
_HwCtStatisticsCt5OutErrorPkt_Type = Counter64
_HwCtStatisticsCt5OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt5OutErrorPkt = _HwCtStatisticsCt5OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 32),
    _HwCtStatisticsCt5OutErrorPkt_Type()
)
hwCtStatisticsCt5OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt5OutErrorPkt.setStatus("current")
_HwCtStatisticsCt6OutByteRate_Type = Counter64
_HwCtStatisticsCt6OutByteRate_Object = MibTableColumn
hwCtStatisticsCt6OutByteRate = _HwCtStatisticsCt6OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 33),
    _HwCtStatisticsCt6OutByteRate_Type()
)
hwCtStatisticsCt6OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt6OutByteRate.setStatus("current")
_HwCtStatisticsCt6OutPktRate_Type = Counter64
_HwCtStatisticsCt6OutPktRate_Object = MibTableColumn
hwCtStatisticsCt6OutPktRate = _HwCtStatisticsCt6OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 34),
    _HwCtStatisticsCt6OutPktRate_Type()
)
hwCtStatisticsCt6OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt6OutPktRate.setStatus("current")
_HwCtStatisticsCt6OutPkt_Type = Counter64
_HwCtStatisticsCt6OutPkt_Object = MibTableColumn
hwCtStatisticsCt6OutPkt = _HwCtStatisticsCt6OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 35),
    _HwCtStatisticsCt6OutPkt_Type()
)
hwCtStatisticsCt6OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt6OutPkt.setStatus("current")
_HwCtStatisticsCt6OutPktByte_Type = Counter64
_HwCtStatisticsCt6OutPktByte_Object = MibTableColumn
hwCtStatisticsCt6OutPktByte = _HwCtStatisticsCt6OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 36),
    _HwCtStatisticsCt6OutPktByte_Type()
)
hwCtStatisticsCt6OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt6OutPktByte.setStatus("current")
_HwCtStatisticsCt6OutErrorPkt_Type = Counter64
_HwCtStatisticsCt6OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt6OutErrorPkt = _HwCtStatisticsCt6OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 37),
    _HwCtStatisticsCt6OutErrorPkt_Type()
)
hwCtStatisticsCt6OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt6OutErrorPkt.setStatus("current")
_HwCtStatisticsCt7OutByteRate_Type = Counter64
_HwCtStatisticsCt7OutByteRate_Object = MibTableColumn
hwCtStatisticsCt7OutByteRate = _HwCtStatisticsCt7OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 38),
    _HwCtStatisticsCt7OutByteRate_Type()
)
hwCtStatisticsCt7OutByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt7OutByteRate.setStatus("current")
_HwCtStatisticsCt7OutPktRate_Type = Counter64
_HwCtStatisticsCt7OutPktRate_Object = MibTableColumn
hwCtStatisticsCt7OutPktRate = _HwCtStatisticsCt7OutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 39),
    _HwCtStatisticsCt7OutPktRate_Type()
)
hwCtStatisticsCt7OutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt7OutPktRate.setStatus("current")
_HwCtStatisticsCt7OutPkt_Type = Counter64
_HwCtStatisticsCt7OutPkt_Object = MibTableColumn
hwCtStatisticsCt7OutPkt = _HwCtStatisticsCt7OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 40),
    _HwCtStatisticsCt7OutPkt_Type()
)
hwCtStatisticsCt7OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt7OutPkt.setStatus("current")
_HwCtStatisticsCt7OutPktByte_Type = Counter64
_HwCtStatisticsCt7OutPktByte_Object = MibTableColumn
hwCtStatisticsCt7OutPktByte = _HwCtStatisticsCt7OutPktByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 41),
    _HwCtStatisticsCt7OutPktByte_Type()
)
hwCtStatisticsCt7OutPktByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt7OutPktByte.setStatus("current")
_HwCtStatisticsCt7OutErrorPkt_Type = Counter64
_HwCtStatisticsCt7OutErrorPkt_Object = MibTableColumn
hwCtStatisticsCt7OutErrorPkt = _HwCtStatisticsCt7OutErrorPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 8, 1, 42),
    _HwCtStatisticsCt7OutErrorPkt_Type()
)
hwCtStatisticsCt7OutErrorPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCtStatisticsCt7OutErrorPkt.setStatus("current")
_HwCtFlowTemplateTable_Object = MibTable
hwCtFlowTemplateTable = _HwCtFlowTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9)
)
if mibBuilder.loadTexts:
    hwCtFlowTemplateTable.setStatus("current")
_HwCtFlowTemplateEntry_Object = MibTableRow
hwCtFlowTemplateEntry = _HwCtFlowTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1)
)
hwCtFlowTemplateEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwCtFlowTemplateID"),
)
if mibBuilder.loadTexts:
    hwCtFlowTemplateEntry.setStatus("current")


class _HwCtFlowTemplateID_Type(Integer32):
    """Custom type hwCtFlowTemplateID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCtFlowTemplateID_Type.__name__ = "Integer32"
_HwCtFlowTemplateID_Object = MibTableColumn
hwCtFlowTemplateID = _HwCtFlowTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 1),
    _HwCtFlowTemplateID_Type()
)
hwCtFlowTemplateID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCtFlowTemplateID.setStatus("current")


class _HwCtFlowTemplateName_Type(OctetString):
    """Custom type hwCtFlowTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_HwCtFlowTemplateName_Type.__name__ = "OctetString"
_HwCtFlowTemplateName_Object = MibTableColumn
hwCtFlowTemplateName = _HwCtFlowTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 11),
    _HwCtFlowTemplateName_Type()
)
hwCtFlowTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtFlowTemplateName.setStatus("current")


class _HwCt0Cos_Type(Integer32):
    """Custom type hwCt0Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt0Cos_Type.__name__ = "Integer32"
_HwCt0Cos_Object = MibTableColumn
hwCt0Cos = _HwCt0Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 12),
    _HwCt0Cos_Type()
)
hwCt0Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt0Cos.setStatus("current")


class _HwCt0Scheduler_Type(Integer32):
    """Custom type hwCt0Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt0Scheduler_Type.__name__ = "Integer32"
_HwCt0Scheduler_Object = MibTableColumn
hwCt0Scheduler = _HwCt0Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 13),
    _HwCt0Scheduler_Type()
)
hwCt0Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt0Scheduler.setStatus("current")


class _HwCt0Valid_Type(Integer32):
    """Custom type hwCt0Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt0Valid_Type.__name__ = "Integer32"
_HwCt0Valid_Object = MibTableColumn
hwCt0Valid = _HwCt0Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 14),
    _HwCt0Valid_Type()
)
hwCt0Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt0Valid.setStatus("current")


class _HwCt1Cos_Type(Integer32):
    """Custom type hwCt1Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt1Cos_Type.__name__ = "Integer32"
_HwCt1Cos_Object = MibTableColumn
hwCt1Cos = _HwCt1Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 15),
    _HwCt1Cos_Type()
)
hwCt1Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt1Cos.setStatus("current")


class _HwCt1Scheduler_Type(Integer32):
    """Custom type hwCt1Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt1Scheduler_Type.__name__ = "Integer32"
_HwCt1Scheduler_Object = MibTableColumn
hwCt1Scheduler = _HwCt1Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 16),
    _HwCt1Scheduler_Type()
)
hwCt1Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt1Scheduler.setStatus("current")


class _HwCt1Valid_Type(Integer32):
    """Custom type hwCt1Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt1Valid_Type.__name__ = "Integer32"
_HwCt1Valid_Object = MibTableColumn
hwCt1Valid = _HwCt1Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 17),
    _HwCt1Valid_Type()
)
hwCt1Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt1Valid.setStatus("current")


class _HwCt2Cos_Type(Integer32):
    """Custom type hwCt2Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt2Cos_Type.__name__ = "Integer32"
_HwCt2Cos_Object = MibTableColumn
hwCt2Cos = _HwCt2Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 18),
    _HwCt2Cos_Type()
)
hwCt2Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt2Cos.setStatus("current")


class _HwCt2Scheduler_Type(Integer32):
    """Custom type hwCt2Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt2Scheduler_Type.__name__ = "Integer32"
_HwCt2Scheduler_Object = MibTableColumn
hwCt2Scheduler = _HwCt2Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 19),
    _HwCt2Scheduler_Type()
)
hwCt2Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt2Scheduler.setStatus("current")


class _HwCt2Valid_Type(Integer32):
    """Custom type hwCt2Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt2Valid_Type.__name__ = "Integer32"
_HwCt2Valid_Object = MibTableColumn
hwCt2Valid = _HwCt2Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 20),
    _HwCt2Valid_Type()
)
hwCt2Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt2Valid.setStatus("current")


class _HwCt3Cos_Type(Integer32):
    """Custom type hwCt3Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt3Cos_Type.__name__ = "Integer32"
_HwCt3Cos_Object = MibTableColumn
hwCt3Cos = _HwCt3Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 21),
    _HwCt3Cos_Type()
)
hwCt3Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt3Cos.setStatus("current")


class _HwCt3Scheduler_Type(Integer32):
    """Custom type hwCt3Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt3Scheduler_Type.__name__ = "Integer32"
_HwCt3Scheduler_Object = MibTableColumn
hwCt3Scheduler = _HwCt3Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 22),
    _HwCt3Scheduler_Type()
)
hwCt3Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt3Scheduler.setStatus("current")


class _HwCt3Valid_Type(Integer32):
    """Custom type hwCt3Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt3Valid_Type.__name__ = "Integer32"
_HwCt3Valid_Object = MibTableColumn
hwCt3Valid = _HwCt3Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 23),
    _HwCt3Valid_Type()
)
hwCt3Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt3Valid.setStatus("current")


class _HwCt4Cos_Type(Integer32):
    """Custom type hwCt4Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt4Cos_Type.__name__ = "Integer32"
_HwCt4Cos_Object = MibTableColumn
hwCt4Cos = _HwCt4Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 24),
    _HwCt4Cos_Type()
)
hwCt4Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt4Cos.setStatus("current")


class _HwCt4Scheduler_Type(Integer32):
    """Custom type hwCt4Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt4Scheduler_Type.__name__ = "Integer32"
_HwCt4Scheduler_Object = MibTableColumn
hwCt4Scheduler = _HwCt4Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 25),
    _HwCt4Scheduler_Type()
)
hwCt4Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt4Scheduler.setStatus("current")


class _HwCt4Valid_Type(Integer32):
    """Custom type hwCt4Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt4Valid_Type.__name__ = "Integer32"
_HwCt4Valid_Object = MibTableColumn
hwCt4Valid = _HwCt4Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 26),
    _HwCt4Valid_Type()
)
hwCt4Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt4Valid.setStatus("current")


class _HwCt5Cos_Type(Integer32):
    """Custom type hwCt5Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt5Cos_Type.__name__ = "Integer32"
_HwCt5Cos_Object = MibTableColumn
hwCt5Cos = _HwCt5Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 27),
    _HwCt5Cos_Type()
)
hwCt5Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt5Cos.setStatus("current")


class _HwCt5Scheduler_Type(Integer32):
    """Custom type hwCt5Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt5Scheduler_Type.__name__ = "Integer32"
_HwCt5Scheduler_Object = MibTableColumn
hwCt5Scheduler = _HwCt5Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 28),
    _HwCt5Scheduler_Type()
)
hwCt5Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt5Scheduler.setStatus("current")


class _HwCt5Valid_Type(Integer32):
    """Custom type hwCt5Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt5Valid_Type.__name__ = "Integer32"
_HwCt5Valid_Object = MibTableColumn
hwCt5Valid = _HwCt5Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 29),
    _HwCt5Valid_Type()
)
hwCt5Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt5Valid.setStatus("current")


class _HwCt6Cos_Type(Integer32):
    """Custom type hwCt6Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt6Cos_Type.__name__ = "Integer32"
_HwCt6Cos_Object = MibTableColumn
hwCt6Cos = _HwCt6Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 30),
    _HwCt6Cos_Type()
)
hwCt6Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt6Cos.setStatus("current")


class _HwCt6Scheduler_Type(Integer32):
    """Custom type hwCt6Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt6Scheduler_Type.__name__ = "Integer32"
_HwCt6Scheduler_Object = MibTableColumn
hwCt6Scheduler = _HwCt6Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 31),
    _HwCt6Scheduler_Type()
)
hwCt6Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt6Scheduler.setStatus("current")


class _HwCt6Valid_Type(Integer32):
    """Custom type hwCt6Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt6Valid_Type.__name__ = "Integer32"
_HwCt6Valid_Object = MibTableColumn
hwCt6Valid = _HwCt6Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 32),
    _HwCt6Valid_Type()
)
hwCt6Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt6Valid.setStatus("current")


class _HwCt7Cos_Type(Integer32):
    """Custom type hwCt7Cos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwCt7Cos_Type.__name__ = "Integer32"
_HwCt7Cos_Object = MibTableColumn
hwCt7Cos = _HwCt7Cos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 33),
    _HwCt7Cos_Type()
)
hwCt7Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt7Cos.setStatus("current")


class _HwCt7Scheduler_Type(Integer32):
    """Custom type hwCt7Scheduler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwCt7Scheduler_Type.__name__ = "Integer32"
_HwCt7Scheduler_Object = MibTableColumn
hwCt7Scheduler = _HwCt7Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 34),
    _HwCt7Scheduler_Type()
)
hwCt7Scheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt7Scheduler.setStatus("current")


class _HwCt7Valid_Type(Integer32):
    """Custom type hwCt7Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwCt7Valid_Type.__name__ = "Integer32"
_HwCt7Valid_Object = MibTableColumn
hwCt7Valid = _HwCt7Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 35),
    _HwCt7Valid_Type()
)
hwCt7Valid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCt7Valid.setStatus("current")


class _HwCtFlowTemplateCommit_Type(Integer32):
    """Custom type hwCtFlowTemplateCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("nocommit", 2))
    )


_HwCtFlowTemplateCommit_Type.__name__ = "Integer32"
_HwCtFlowTemplateCommit_Object = MibTableColumn
hwCtFlowTemplateCommit = _HwCtFlowTemplateCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 36),
    _HwCtFlowTemplateCommit_Type()
)
hwCtFlowTemplateCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtFlowTemplateCommit.setStatus("current")
_HwCtFlowTemplateRowStatus_Type = RowStatus
_HwCtFlowTemplateRowStatus_Object = MibTableColumn
hwCtFlowTemplateRowStatus = _HwCtFlowTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 9, 1, 51),
    _HwCtFlowTemplateRowStatus_Type()
)
hwCtFlowTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtFlowTemplateRowStatus.setStatus("current")
_HwDsteInterfaceCfgTable_Object = MibTable
hwDsteInterfaceCfgTable = _HwDsteInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 10)
)
if mibBuilder.loadTexts:
    hwDsteInterfaceCfgTable.setStatus("current")
_HwDsteInterfaceCfgEntry_Object = MibTableRow
hwDsteInterfaceCfgEntry = _HwDsteInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 10, 1)
)
hwDsteInterfaceCfgEntry.setIndexNames(
    (0, "HUAWEI-TUNNEL-TE-MIB", "hwDsteIfIndex"),
)
if mibBuilder.loadTexts:
    hwDsteInterfaceCfgEntry.setStatus("current")
_HwDsteIfIndex_Type = InterfaceIndex
_HwDsteIfIndex_Object = MibTableColumn
hwDsteIfIndex = _HwDsteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 10, 1, 1),
    _HwDsteIfIndex_Type()
)
hwDsteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDsteIfIndex.setStatus("current")


class _HwAppliedCtFlowTemplateName_Type(OctetString):
    """Custom type hwAppliedCtFlowTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_HwAppliedCtFlowTemplateName_Type.__name__ = "OctetString"
_HwAppliedCtFlowTemplateName_Object = MibTableColumn
hwAppliedCtFlowTemplateName = _HwAppliedCtFlowTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 10, 1, 11),
    _HwAppliedCtFlowTemplateName_Type()
)
hwAppliedCtFlowTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAppliedCtFlowTemplateName.setStatus("current")


class _HwCtBandWidthShareCfg_Type(Integer32):
    """Custom type hwCtBandWidthShareCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("share", 1),
          ("unshare", 2))
    )


_HwCtBandWidthShareCfg_Type.__name__ = "Integer32"
_HwCtBandWidthShareCfg_Object = MibTableColumn
hwCtBandWidthShareCfg = _HwCtBandWidthShareCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 1, 10, 1, 12),
    _HwCtBandWidthShareCfg_Type()
)
hwCtBandWidthShareCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCtBandWidthShareCfg.setStatus("current")
_HwTunnelDsTeTrap_ObjectIdentity = ObjectIdentity
hwTunnelDsTeTrap = _HwTunnelDsTeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2)
)
_HwTunnelTeConformance_ObjectIdentity = ObjectIdentity
hwTunnelTeConformance = _HwTunnelTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3)
)
_HwTunnelTeCompliances_ObjectIdentity = ObjectIdentity
hwTunnelTeCompliances = _HwTunnelTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 1)
)
_HwTunnelTeGroups_ObjectIdentity = ObjectIdentity
hwTunnelTeGroups = _HwTunnelTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3)
)

# Managed Objects groups

hwTunnelDiffServGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 1)
)
hwTunnelDiffServGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwTunnelDiffServMode"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelDiffServServiceClass"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelDiffServColor"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeFlowQueue"))
)
if mibBuilder.loadTexts:
    hwTunnelDiffServGroup.setStatus("current")

hwTunnelTeVsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 2)
)
hwTunnelTeVsiGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVsiCir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVsiPir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVsiFlowQueue"))
)
if mibBuilder.loadTexts:
    hwTunnelTeVsiGroup.setStatus("current")

hwTunnelTeVllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 3)
)
hwTunnelTeVllGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVllCir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVllPir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeVllFlowQueue"))
)
if mibBuilder.loadTexts:
    hwTunnelTeVllGroup.setStatus("current")

hwTunnelTeL3vpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 4)
)
hwTunnelTeL3vpnGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeL3vpnCir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeL3vpnPir"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeL3vpnFlowQueue"))
)
if mibBuilder.loadTexts:
    hwTunnelTeL3vpnGroup.setStatus("current")

hwTunnelTeStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 5)
)
hwTunnelTeStatisticsGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwTunnelTeUpDownStatistics"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwTunnTeCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    hwTunnelTeStatisticsGroup.setStatus("current")

hwCtTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 6)
)
hwCtTemplateGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt0"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt1"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt2"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt3"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt4"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt5"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt6"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCt7"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateCommit"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hwCtTemplateGroup.setStatus("current")

hwCtConfigCtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 7)
)
hwCtConfigCtGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCommit"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTemplateName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt0Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt1Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt2Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt3Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt4Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt5Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt6Band"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelCt7Band"))
)
if mibBuilder.loadTexts:
    hwCtConfigCtGroup.setStatus("current")

hwCtStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 8)
)
hwCtStatisticsGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsTunnelName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt0OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt0OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt0OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt0OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt0OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt1OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt1OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt1OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt1OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt1OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt2OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt2OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt2OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt2OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt2OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt3OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt3OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt3OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt3OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt3OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt4OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt4OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt4OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt4OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt4OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt5OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt5OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt5OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt5OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt5OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt6OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt6OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt6OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt6OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt6OutErrorPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt7OutByteRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt7OutPktRate"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt7OutPkt"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt7OutPktByte"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtStatisticsCt7OutErrorPkt"))
)
if mibBuilder.loadTexts:
    hwCtStatisticsGroup.setStatus("current")

hwCtFlowTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 10)
)
hwCtFlowTemplateGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwCtFlowTemplateName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt0Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt0Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt0Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt1Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt1Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt1Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt2Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt2Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt2Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt3Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt3Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt3Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt4Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt4Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt4Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt5Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt5Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt5Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt6Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt6Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt6Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt7Cos"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt7Scheduler"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCt7Valid"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtFlowTemplateCommit"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtFlowTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hwCtFlowTemplateGroup.setStatus("current")

hwDsteInterfaceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 11)
)
hwDsteInterfaceCfgGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwAppliedCtFlowTemplateName"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwCtBandWidthShareCfg"))
)
if mibBuilder.loadTexts:
    hwDsteInterfaceCfgGroup.setStatus("current")


# Notification objects

hwMplsFqShortage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 1)
)
hwMplsFqShortage.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsFqShortage.setStatus(
        "obsolete"
    )

hwMplsSqShortage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 2)
)
hwMplsSqShortage.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsSqShortage.setStatus(
        "obsolete"
    )

hwMplsSqBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 3)
)
hwMplsSqBandwidthExceed.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsSqBandwidthExceed.setStatus(
        "obsolete"
    )

hwMplsHsbFqShortage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 4)
)
hwMplsHsbFqShortage.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsHsbFqShortage.setStatus(
        "obsolete"
    )

hwMplsHsbSqShortage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 5)
)
hwMplsHsbSqShortage.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsHsbSqShortage.setStatus(
        "obsolete"
    )

hwMplsHsbSqBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 2, 6)
)
hwMplsHsbSqBandwidthExceed.setObjects(
    ("HUAWEI-TUNNEL-TE-MIB", "hwCtConfigTunnelName")
)
if mibBuilder.loadTexts:
    hwMplsHsbSqBandwidthExceed.setStatus(
        "obsolete"
    )


# Notifications groups

hwTunnelTeTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 3, 9)
)
hwTunnelTeTrapGroup.setObjects(
      *(("HUAWEI-TUNNEL-TE-MIB", "hwMplsHsbSqBandwidthExceed"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwMplsHsbSqShortage"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwMplsHsbFqShortage"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwMplsSqBandwidthExceed"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwMplsSqShortage"),
        ("HUAWEI-TUNNEL-TE-MIB", "hwMplsFqShortage"))
)
if mibBuilder.loadTexts:
    hwTunnelTeTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwTunnelTeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 151, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwTunnelTeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TUNNEL-TE-MIB",
    **{"hwTunnelTeMib": hwTunnelTeMib,
       "hwTunnelTeMibObject": hwTunnelTeMibObject,
       "hwTunnelDiffServTable": hwTunnelDiffServTable,
       "hwTunnelDiffServEntry": hwTunnelDiffServEntry,
       "hwTunnelDiffServIndex": hwTunnelDiffServIndex,
       "hwTunnelDiffServMode": hwTunnelDiffServMode,
       "hwTunnelDiffServServiceClass": hwTunnelDiffServServiceClass,
       "hwTunnelDiffServColor": hwTunnelDiffServColor,
       "hwTunnelTeFlowQueue": hwTunnelTeFlowQueue,
       "hwTunnelTeVsiTable": hwTunnelTeVsiTable,
       "hwTunnelTeVsiEntry": hwTunnelTeVsiEntry,
       "hwTunnelTeVsiIndex": hwTunnelTeVsiIndex,
       "hwTunnelTeVsiName": hwTunnelTeVsiName,
       "hwTunnelTeVsiCir": hwTunnelTeVsiCir,
       "hwTunnelTeVsiPir": hwTunnelTeVsiPir,
       "hwTunnelTeVsiFlowQueue": hwTunnelTeVsiFlowQueue,
       "hwTunnelTeVllTable": hwTunnelTeVllTable,
       "hwTunnelTeVllEntry": hwTunnelTeVllEntry,
       "hwTunnelTeVllIndex": hwTunnelTeVllIndex,
       "hwTunnelTeVllInterfaceName": hwTunnelTeVllInterfaceName,
       "hwTunnelTeVllCir": hwTunnelTeVllCir,
       "hwTunnelTeVllPir": hwTunnelTeVllPir,
       "hwTunnelTeVllFlowQueue": hwTunnelTeVllFlowQueue,
       "hwTunnelTeL3vpnTable": hwTunnelTeL3vpnTable,
       "hwTunnelTeL3vpnEntry": hwTunnelTeL3vpnEntry,
       "hwTunnelTeL3vpnIndex": hwTunnelTeL3vpnIndex,
       "hwTunnelTeL3vpnName": hwTunnelTeL3vpnName,
       "hwTunnelTeL3vpnCir": hwTunnelTeL3vpnCir,
       "hwTunnelTeL3vpnPir": hwTunnelTeL3vpnPir,
       "hwTunnelTeL3vpnFlowQueue": hwTunnelTeL3vpnFlowQueue,
       "hwTunnelTeStatisticsTable": hwTunnelTeStatisticsTable,
       "hwTunnelTeStatisticsEntry": hwTunnelTeStatisticsEntry,
       "hwTunnelTeStatisticsIfIndex": hwTunnelTeStatisticsIfIndex,
       "hwTunnelTeUpDownStatistics": hwTunnelTeUpDownStatistics,
       "hwTunnTeCounterDiscontinuityTime": hwTunnTeCounterDiscontinuityTime,
       "hwCtTemplateTable": hwCtTemplateTable,
       "hwCtTemplateEntry": hwCtTemplateEntry,
       "hwCtTemplateIndex": hwCtTemplateIndex,
       "hwCtTemplateName": hwCtTemplateName,
       "hwCtTemplateCt0": hwCtTemplateCt0,
       "hwCtTemplateCt1": hwCtTemplateCt1,
       "hwCtTemplateCt2": hwCtTemplateCt2,
       "hwCtTemplateCt3": hwCtTemplateCt3,
       "hwCtTemplateCt4": hwCtTemplateCt4,
       "hwCtTemplateCt5": hwCtTemplateCt5,
       "hwCtTemplateCt6": hwCtTemplateCt6,
       "hwCtTemplateCt7": hwCtTemplateCt7,
       "hwCtTemplateCommit": hwCtTemplateCommit,
       "hwCtTemplateRowStatus": hwCtTemplateRowStatus,
       "hwCtConfigTunnelCtTable": hwCtConfigTunnelCtTable,
       "hwCtConfigTunnelCtEntry": hwCtConfigTunnelCtEntry,
       "hwCtConfigTunnelCtIfIndex": hwCtConfigTunnelCtIfIndex,
       "hwCtConfigTunnelName": hwCtConfigTunnelName,
       "hwCtConfigTunnelCommit": hwCtConfigTunnelCommit,
       "hwCtConfigTemplateName": hwCtConfigTemplateName,
       "hwCtConfigTunnelCt0Band": hwCtConfigTunnelCt0Band,
       "hwCtConfigTunnelCt1Band": hwCtConfigTunnelCt1Band,
       "hwCtConfigTunnelCt2Band": hwCtConfigTunnelCt2Band,
       "hwCtConfigTunnelCt3Band": hwCtConfigTunnelCt3Band,
       "hwCtConfigTunnelCt4Band": hwCtConfigTunnelCt4Band,
       "hwCtConfigTunnelCt5Band": hwCtConfigTunnelCt5Band,
       "hwCtConfigTunnelCt6Band": hwCtConfigTunnelCt6Band,
       "hwCtConfigTunnelCt7Band": hwCtConfigTunnelCt7Band,
       "hwCtStatisticsTable": hwCtStatisticsTable,
       "hwCtStatisticsEntry": hwCtStatisticsEntry,
       "hwCtStatisticsIfIndex": hwCtStatisticsIfIndex,
       "hwCtStatisticsTunnelName": hwCtStatisticsTunnelName,
       "hwCtStatisticsCt0OutByteRate": hwCtStatisticsCt0OutByteRate,
       "hwCtStatisticsCt0OutPktRate": hwCtStatisticsCt0OutPktRate,
       "hwCtStatisticsCt0OutPkt": hwCtStatisticsCt0OutPkt,
       "hwCtStatisticsCt0OutPktByte": hwCtStatisticsCt0OutPktByte,
       "hwCtStatisticsCt0OutErrorPkt": hwCtStatisticsCt0OutErrorPkt,
       "hwCtStatisticsCt1OutByteRate": hwCtStatisticsCt1OutByteRate,
       "hwCtStatisticsCt1OutPktRate": hwCtStatisticsCt1OutPktRate,
       "hwCtStatisticsCt1OutPkt": hwCtStatisticsCt1OutPkt,
       "hwCtStatisticsCt1OutPktByte": hwCtStatisticsCt1OutPktByte,
       "hwCtStatisticsCt1OutErrorPkt": hwCtStatisticsCt1OutErrorPkt,
       "hwCtStatisticsCt2OutByteRate": hwCtStatisticsCt2OutByteRate,
       "hwCtStatisticsCt2OutPktRate": hwCtStatisticsCt2OutPktRate,
       "hwCtStatisticsCt2OutPkt": hwCtStatisticsCt2OutPkt,
       "hwCtStatisticsCt2OutPktByte": hwCtStatisticsCt2OutPktByte,
       "hwCtStatisticsCt2OutErrorPkt": hwCtStatisticsCt2OutErrorPkt,
       "hwCtStatisticsCt3OutByteRate": hwCtStatisticsCt3OutByteRate,
       "hwCtStatisticsCt3OutPktRate": hwCtStatisticsCt3OutPktRate,
       "hwCtStatisticsCt3OutPkt": hwCtStatisticsCt3OutPkt,
       "hwCtStatisticsCt3OutPktByte": hwCtStatisticsCt3OutPktByte,
       "hwCtStatisticsCt3OutErrorPkt": hwCtStatisticsCt3OutErrorPkt,
       "hwCtStatisticsCt4OutByteRate": hwCtStatisticsCt4OutByteRate,
       "hwCtStatisticsCt4OutPktRate": hwCtStatisticsCt4OutPktRate,
       "hwCtStatisticsCt4OutPkt": hwCtStatisticsCt4OutPkt,
       "hwCtStatisticsCt4OutPktByte": hwCtStatisticsCt4OutPktByte,
       "hwCtStatisticsCt4OutErrorPkt": hwCtStatisticsCt4OutErrorPkt,
       "hwCtStatisticsCt5OutByteRate": hwCtStatisticsCt5OutByteRate,
       "hwCtStatisticsCt5OutPktRate": hwCtStatisticsCt5OutPktRate,
       "hwCtStatisticsCt5OutPkt": hwCtStatisticsCt5OutPkt,
       "hwCtStatisticsCt5OutPktByte": hwCtStatisticsCt5OutPktByte,
       "hwCtStatisticsCt5OutErrorPkt": hwCtStatisticsCt5OutErrorPkt,
       "hwCtStatisticsCt6OutByteRate": hwCtStatisticsCt6OutByteRate,
       "hwCtStatisticsCt6OutPktRate": hwCtStatisticsCt6OutPktRate,
       "hwCtStatisticsCt6OutPkt": hwCtStatisticsCt6OutPkt,
       "hwCtStatisticsCt6OutPktByte": hwCtStatisticsCt6OutPktByte,
       "hwCtStatisticsCt6OutErrorPkt": hwCtStatisticsCt6OutErrorPkt,
       "hwCtStatisticsCt7OutByteRate": hwCtStatisticsCt7OutByteRate,
       "hwCtStatisticsCt7OutPktRate": hwCtStatisticsCt7OutPktRate,
       "hwCtStatisticsCt7OutPkt": hwCtStatisticsCt7OutPkt,
       "hwCtStatisticsCt7OutPktByte": hwCtStatisticsCt7OutPktByte,
       "hwCtStatisticsCt7OutErrorPkt": hwCtStatisticsCt7OutErrorPkt,
       "hwCtFlowTemplateTable": hwCtFlowTemplateTable,
       "hwCtFlowTemplateEntry": hwCtFlowTemplateEntry,
       "hwCtFlowTemplateID": hwCtFlowTemplateID,
       "hwCtFlowTemplateName": hwCtFlowTemplateName,
       "hwCt0Cos": hwCt0Cos,
       "hwCt0Scheduler": hwCt0Scheduler,
       "hwCt0Valid": hwCt0Valid,
       "hwCt1Cos": hwCt1Cos,
       "hwCt1Scheduler": hwCt1Scheduler,
       "hwCt1Valid": hwCt1Valid,
       "hwCt2Cos": hwCt2Cos,
       "hwCt2Scheduler": hwCt2Scheduler,
       "hwCt2Valid": hwCt2Valid,
       "hwCt3Cos": hwCt3Cos,
       "hwCt3Scheduler": hwCt3Scheduler,
       "hwCt3Valid": hwCt3Valid,
       "hwCt4Cos": hwCt4Cos,
       "hwCt4Scheduler": hwCt4Scheduler,
       "hwCt4Valid": hwCt4Valid,
       "hwCt5Cos": hwCt5Cos,
       "hwCt5Scheduler": hwCt5Scheduler,
       "hwCt5Valid": hwCt5Valid,
       "hwCt6Cos": hwCt6Cos,
       "hwCt6Scheduler": hwCt6Scheduler,
       "hwCt6Valid": hwCt6Valid,
       "hwCt7Cos": hwCt7Cos,
       "hwCt7Scheduler": hwCt7Scheduler,
       "hwCt7Valid": hwCt7Valid,
       "hwCtFlowTemplateCommit": hwCtFlowTemplateCommit,
       "hwCtFlowTemplateRowStatus": hwCtFlowTemplateRowStatus,
       "hwDsteInterfaceCfgTable": hwDsteInterfaceCfgTable,
       "hwDsteInterfaceCfgEntry": hwDsteInterfaceCfgEntry,
       "hwDsteIfIndex": hwDsteIfIndex,
       "hwAppliedCtFlowTemplateName": hwAppliedCtFlowTemplateName,
       "hwCtBandWidthShareCfg": hwCtBandWidthShareCfg,
       "hwTunnelDsTeTrap": hwTunnelDsTeTrap,
       "hwMplsFqShortage": hwMplsFqShortage,
       "hwMplsSqShortage": hwMplsSqShortage,
       "hwMplsSqBandwidthExceed": hwMplsSqBandwidthExceed,
       "hwMplsHsbFqShortage": hwMplsHsbFqShortage,
       "hwMplsHsbSqShortage": hwMplsHsbSqShortage,
       "hwMplsHsbSqBandwidthExceed": hwMplsHsbSqBandwidthExceed,
       "hwTunnelTeConformance": hwTunnelTeConformance,
       "hwTunnelTeCompliances": hwTunnelTeCompliances,
       "hwTunnelTeCompliance": hwTunnelTeCompliance,
       "hwTunnelTeGroups": hwTunnelTeGroups,
       "hwTunnelDiffServGroup": hwTunnelDiffServGroup,
       "hwTunnelTeVsiGroup": hwTunnelTeVsiGroup,
       "hwTunnelTeVllGroup": hwTunnelTeVllGroup,
       "hwTunnelTeL3vpnGroup": hwTunnelTeL3vpnGroup,
       "hwTunnelTeStatisticsGroup": hwTunnelTeStatisticsGroup,
       "hwCtTemplateGroup": hwCtTemplateGroup,
       "hwCtConfigCtGroup": hwCtConfigCtGroup,
       "hwCtStatisticsGroup": hwCtStatisticsGroup,
       "hwTunnelTeTrapGroup": hwTunnelTeTrapGroup,
       "hwCtFlowTemplateGroup": hwCtFlowTemplateGroup,
       "hwDsteInterfaceCfgGroup": hwDsteInterfaceCfgGroup}
)
