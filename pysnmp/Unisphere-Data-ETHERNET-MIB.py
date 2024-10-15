# SNMP MIB module (Unisphere-Data-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:39 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34)
)
usdEthernetMIB.setRevisions(
        ("2002-04-05 19:47",
         "2001-01-02 16:55",
         "2000-04-18 00:00",
         "2000-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdEthernetObjects_ObjectIdentity = ObjectIdentity
usdEthernetObjects = _UsdEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1)
)
_UsdEthernetIfLayer_ObjectIdentity = ObjectIdentity
usdEthernetIfLayer = _UsdEthernetIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1)
)
_UsdEthernetIfTable_Object = MibTable
usdEthernetIfTable = _UsdEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdEthernetIfTable.setStatus("current")
_UsdEthernetIfEntry_Object = MibTableRow
usdEthernetIfEntry = _UsdEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1)
)
usdEthernetIfEntry.setIndexNames(
    (0, "Unisphere-Data-ETHERNET-MIB", "usdEthernetIfIndex"),
)
if mibBuilder.loadTexts:
    usdEthernetIfEntry.setStatus("current")
_UsdEthernetIfIndex_Type = InterfaceIndex
_UsdEthernetIfIndex_Object = MibTableColumn
usdEthernetIfIndex = _UsdEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 1),
    _UsdEthernetIfIndex_Type()
)
usdEthernetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdEthernetIfIndex.setStatus("current")


class _UsdEthernetIfDuplexMode_Type(Integer32):
    """Custom type usdEthernetIfDuplexMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 1),
          ("fullDuplex", 3),
          ("halfDuplex", 2))
    )


_UsdEthernetIfDuplexMode_Type.__name__ = "Integer32"
_UsdEthernetIfDuplexMode_Object = MibTableColumn
usdEthernetIfDuplexMode = _UsdEthernetIfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 2),
    _UsdEthernetIfDuplexMode_Type()
)
usdEthernetIfDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdEthernetIfDuplexMode.setStatus("current")


class _UsdEthernetIfSpeed_Type(Integer32):
    """Custom type usdEthernetIfSpeed based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("speed1000Mbps", 4),
          ("speed100Mbps", 3),
          ("speed10Mbps", 2))
    )


_UsdEthernetIfSpeed_Type.__name__ = "Integer32"
_UsdEthernetIfSpeed_Object = MibTableColumn
usdEthernetIfSpeed = _UsdEthernetIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 3),
    _UsdEthernetIfSpeed_Type()
)
usdEthernetIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdEthernetIfSpeed.setStatus("current")


class _UsdEthernetIfMtu_Type(Integer32):
    """Custom type usdEthernetIfMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9188),
    )


_UsdEthernetIfMtu_Type.__name__ = "Integer32"
_UsdEthernetIfMtu_Object = MibTableColumn
usdEthernetIfMtu = _UsdEthernetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 4),
    _UsdEthernetIfMtu_Type()
)
usdEthernetIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdEthernetIfMtu.setStatus("current")


class _UsdEthernetIfOperDuplexMode_Type(Integer32):
    """Custom type usdEthernetIfOperDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 1),
          ("fullDuplex", 3),
          ("halfDuplex", 2))
    )


_UsdEthernetIfOperDuplexMode_Type.__name__ = "Integer32"
_UsdEthernetIfOperDuplexMode_Object = MibTableColumn
usdEthernetIfOperDuplexMode = _UsdEthernetIfOperDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 5),
    _UsdEthernetIfOperDuplexMode_Type()
)
usdEthernetIfOperDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdEthernetIfOperDuplexMode.setStatus("current")
_UsdEthernetSubIfLayer_ObjectIdentity = ObjectIdentity
usdEthernetSubIfLayer = _UsdEthernetSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2)
)
_UsdEthernetSubIfNextIfIndex_Type = UsdNextIfIndex
_UsdEthernetSubIfNextIfIndex_Object = MibScalar
usdEthernetSubIfNextIfIndex = _UsdEthernetSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 1),
    _UsdEthernetSubIfNextIfIndex_Type()
)
usdEthernetSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdEthernetSubIfNextIfIndex.setStatus("current")
_UsdEthernetSubIfTable_Object = MibTable
usdEthernetSubIfTable = _UsdEthernetSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdEthernetSubIfTable.setStatus("current")
_UsdEthernetSubIfEntry_Object = MibTableRow
usdEthernetSubIfEntry = _UsdEthernetSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1)
)
usdEthernetSubIfEntry.setIndexNames(
    (0, "Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdEthernetSubIfEntry.setStatus("current")
_UsdEthernetSubIfIndex_Type = InterfaceIndex
_UsdEthernetSubIfIndex_Object = MibTableColumn
usdEthernetSubIfIndex = _UsdEthernetSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 1),
    _UsdEthernetSubIfIndex_Type()
)
usdEthernetSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdEthernetSubIfIndex.setStatus("current")
_UsdEthernetSubIfRowStatus_Type = RowStatus
_UsdEthernetSubIfRowStatus_Object = MibTableColumn
usdEthernetSubIfRowStatus = _UsdEthernetSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 2),
    _UsdEthernetSubIfRowStatus_Type()
)
usdEthernetSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdEthernetSubIfRowStatus.setStatus("current")
_UsdEthernetSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdEthernetSubIfLowerIfIndex_Object = MibTableColumn
usdEthernetSubIfLowerIfIndex = _UsdEthernetSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 3),
    _UsdEthernetSubIfLowerIfIndex_Type()
)
usdEthernetSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdEthernetSubIfLowerIfIndex.setStatus("current")


class _UsdEthernetSubIfId_Type(Integer32):
    """Custom type usdEthernetSubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UsdEthernetSubIfId_Type.__name__ = "Integer32"
_UsdEthernetSubIfId_Object = MibTableColumn
usdEthernetSubIfId = _UsdEthernetSubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 4),
    _UsdEthernetSubIfId_Type()
)
usdEthernetSubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdEthernetSubIfId.setStatus("current")
_UsdVlanMajorIfLayer_ObjectIdentity = ObjectIdentity
usdVlanMajorIfLayer = _UsdVlanMajorIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3)
)
_UsdVlanMajorNextIfIndex_Type = UsdNextIfIndex
_UsdVlanMajorNextIfIndex_Object = MibScalar
usdVlanMajorNextIfIndex = _UsdVlanMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 1),
    _UsdVlanMajorNextIfIndex_Type()
)
usdVlanMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdVlanMajorNextIfIndex.setStatus("current")
_UsdVlanMajorIfTable_Object = MibTable
usdVlanMajorIfTable = _UsdVlanMajorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdVlanMajorIfTable.setStatus("current")
_UsdVlanMajorIfEntry_Object = MibTableRow
usdVlanMajorIfEntry = _UsdVlanMajorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1)
)
usdVlanMajorIfEntry.setIndexNames(
    (0, "Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfIndex"),
)
if mibBuilder.loadTexts:
    usdVlanMajorIfEntry.setStatus("current")
_UsdVlanMajorIfIndex_Type = InterfaceIndex
_UsdVlanMajorIfIndex_Object = MibTableColumn
usdVlanMajorIfIndex = _UsdVlanMajorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 1),
    _UsdVlanMajorIfIndex_Type()
)
usdVlanMajorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdVlanMajorIfIndex.setStatus("current")
_UsdVlanMajorIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdVlanMajorIfLowerIfIndex_Object = MibTableColumn
usdVlanMajorIfLowerIfIndex = _UsdVlanMajorIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 2),
    _UsdVlanMajorIfLowerIfIndex_Type()
)
usdVlanMajorIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanMajorIfLowerIfIndex.setStatus("current")
_UsdVlanMajorIfRowStatus_Type = RowStatus
_UsdVlanMajorIfRowStatus_Object = MibTableColumn
usdVlanMajorIfRowStatus = _UsdVlanMajorIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 3),
    _UsdVlanMajorIfRowStatus_Type()
)
usdVlanMajorIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanMajorIfRowStatus.setStatus("current")
_UsdVlanSubIfLayer_ObjectIdentity = ObjectIdentity
usdVlanSubIfLayer = _UsdVlanSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4)
)
_UsdVlanSubNextIfIndex_Type = UsdNextIfIndex
_UsdVlanSubNextIfIndex_Object = MibScalar
usdVlanSubNextIfIndex = _UsdVlanSubNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 1),
    _UsdVlanSubNextIfIndex_Type()
)
usdVlanSubNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdVlanSubNextIfIndex.setStatus("current")
_UsdVlanSubIfTable_Object = MibTable
usdVlanSubIfTable = _UsdVlanSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdVlanSubIfTable.setStatus("current")
_UsdVlanSubIfEntry_Object = MibTableRow
usdVlanSubIfEntry = _UsdVlanSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1)
)
usdVlanSubIfEntry.setIndexNames(
    (0, "Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdVlanSubIfEntry.setStatus("current")
_UsdVlanSubIfIndex_Type = InterfaceIndex
_UsdVlanSubIfIndex_Object = MibTableColumn
usdVlanSubIfIndex = _UsdVlanSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 1),
    _UsdVlanSubIfIndex_Type()
)
usdVlanSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdVlanSubIfIndex.setStatus("current")


class _UsdVlanSubIfVlanId_Type(Integer32):
    """Custom type usdVlanSubIfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_UsdVlanSubIfVlanId_Type.__name__ = "Integer32"
_UsdVlanSubIfVlanId_Object = MibTableColumn
usdVlanSubIfVlanId = _UsdVlanSubIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 2),
    _UsdVlanSubIfVlanId_Type()
)
usdVlanSubIfVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfVlanId.setStatus("current")
_UsdVlanSubIfVlanUntagged_Type = TruthValue
_UsdVlanSubIfVlanUntagged_Object = MibTableColumn
usdVlanSubIfVlanUntagged = _UsdVlanSubIfVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 3),
    _UsdVlanSubIfVlanUntagged_Type()
)
usdVlanSubIfVlanUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfVlanUntagged.setStatus("current")
_UsdVlanSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdVlanSubIfLowerIfIndex_Object = MibTableColumn
usdVlanSubIfLowerIfIndex = _UsdVlanSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 4),
    _UsdVlanSubIfLowerIfIndex_Type()
)
usdVlanSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfLowerIfIndex.setStatus("current")
_UsdVlanSubIfRowStatus_Type = RowStatus
_UsdVlanSubIfRowStatus_Object = MibTableColumn
usdVlanSubIfRowStatus = _UsdVlanSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 5),
    _UsdVlanSubIfRowStatus_Type()
)
usdVlanSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfRowStatus.setStatus("current")


class _UsdVlanSubIfVlanStackId_Type(Integer32):
    """Custom type usdVlanSubIfVlanStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_UsdVlanSubIfVlanStackId_Type.__name__ = "Integer32"
_UsdVlanSubIfVlanStackId_Object = MibTableColumn
usdVlanSubIfVlanStackId = _UsdVlanSubIfVlanStackId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 6),
    _UsdVlanSubIfVlanStackId_Type()
)
usdVlanSubIfVlanStackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfVlanStackId.setStatus("current")


class _UsdVlanSubIfVlanStackEthertype_Type(Integer32):
    """Custom type usdVlanSubIfVlanStackEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(37120,
              37376)
        )
    )
    namedValues = NamedValues(
        *(("etherType9100h", 37120),
          ("etherType9200h", 37376))
    )


_UsdVlanSubIfVlanStackEthertype_Type.__name__ = "Integer32"
_UsdVlanSubIfVlanStackEthertype_Object = MibTableColumn
usdVlanSubIfVlanStackEthertype = _UsdVlanSubIfVlanStackEthertype_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 7),
    _UsdVlanSubIfVlanStackEthertype_Type()
)
usdVlanSubIfVlanStackEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdVlanSubIfVlanStackEthertype.setStatus("current")
_UsdEthernetConformance_ObjectIdentity = ObjectIdentity
usdEthernetConformance = _UsdEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4)
)
_UsdEthernetCompliances_ObjectIdentity = ObjectIdentity
usdEthernetCompliances = _UsdEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1)
)
_UsdEthernetGroups_ObjectIdentity = ObjectIdentity
usdEthernetGroups = _UsdEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2)
)

# Managed Objects groups

usdEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 1)
)
usdEthernetGroup.setObjects(
      *(("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfDuplexMode"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfSpeed"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfMtu"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfOperDuplexMode"))
)
if mibBuilder.loadTexts:
    usdEthernetGroup.setStatus("current")

usdEthernetSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 2)
)
usdEthernetSubIfGroup.setObjects(
      *(("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfNextIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfRowStatus"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfLowerIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfId"))
)
if mibBuilder.loadTexts:
    usdEthernetSubIfGroup.setStatus("current")

usdVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 3)
)
usdVlanGroup.setObjects(
      *(("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorNextIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfLowerIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfRowStatus"))
)
if mibBuilder.loadTexts:
    usdVlanGroup.setStatus("current")

usdVlanSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 4)
)
usdVlanSubIfGroup.setObjects(
      *(("Unisphere-Data-ETHERNET-MIB", "usdVlanSubNextIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanId"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanUntagged"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfLowerIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfRowStatus"))
)
if mibBuilder.loadTexts:
    usdVlanSubIfGroup.setStatus("obsolete")

usdVlanSubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 5)
)
usdVlanSubIfGroup2.setObjects(
      *(("Unisphere-Data-ETHERNET-MIB", "usdVlanSubNextIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanId"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanUntagged"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanStackId"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanStackEthertype"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfLowerIfIndex"),
        ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfRowStatus"))
)
if mibBuilder.loadTexts:
    usdVlanSubIfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdEthernetCompliance.setStatus(
        "obsolete"
    )

usdEthernetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdEthernetCompliance2.setStatus(
        "obsolete"
    )

usdEthernetCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdEthernetCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ETHERNET-MIB",
    **{"usdEthernetMIB": usdEthernetMIB,
       "usdEthernetObjects": usdEthernetObjects,
       "usdEthernetIfLayer": usdEthernetIfLayer,
       "usdEthernetIfTable": usdEthernetIfTable,
       "usdEthernetIfEntry": usdEthernetIfEntry,
       "usdEthernetIfIndex": usdEthernetIfIndex,
       "usdEthernetIfDuplexMode": usdEthernetIfDuplexMode,
       "usdEthernetIfSpeed": usdEthernetIfSpeed,
       "usdEthernetIfMtu": usdEthernetIfMtu,
       "usdEthernetIfOperDuplexMode": usdEthernetIfOperDuplexMode,
       "usdEthernetSubIfLayer": usdEthernetSubIfLayer,
       "usdEthernetSubIfNextIfIndex": usdEthernetSubIfNextIfIndex,
       "usdEthernetSubIfTable": usdEthernetSubIfTable,
       "usdEthernetSubIfEntry": usdEthernetSubIfEntry,
       "usdEthernetSubIfIndex": usdEthernetSubIfIndex,
       "usdEthernetSubIfRowStatus": usdEthernetSubIfRowStatus,
       "usdEthernetSubIfLowerIfIndex": usdEthernetSubIfLowerIfIndex,
       "usdEthernetSubIfId": usdEthernetSubIfId,
       "usdVlanMajorIfLayer": usdVlanMajorIfLayer,
       "usdVlanMajorNextIfIndex": usdVlanMajorNextIfIndex,
       "usdVlanMajorIfTable": usdVlanMajorIfTable,
       "usdVlanMajorIfEntry": usdVlanMajorIfEntry,
       "usdVlanMajorIfIndex": usdVlanMajorIfIndex,
       "usdVlanMajorIfLowerIfIndex": usdVlanMajorIfLowerIfIndex,
       "usdVlanMajorIfRowStatus": usdVlanMajorIfRowStatus,
       "usdVlanSubIfLayer": usdVlanSubIfLayer,
       "usdVlanSubNextIfIndex": usdVlanSubNextIfIndex,
       "usdVlanSubIfTable": usdVlanSubIfTable,
       "usdVlanSubIfEntry": usdVlanSubIfEntry,
       "usdVlanSubIfIndex": usdVlanSubIfIndex,
       "usdVlanSubIfVlanId": usdVlanSubIfVlanId,
       "usdVlanSubIfVlanUntagged": usdVlanSubIfVlanUntagged,
       "usdVlanSubIfLowerIfIndex": usdVlanSubIfLowerIfIndex,
       "usdVlanSubIfRowStatus": usdVlanSubIfRowStatus,
       "usdVlanSubIfVlanStackId": usdVlanSubIfVlanStackId,
       "usdVlanSubIfVlanStackEthertype": usdVlanSubIfVlanStackEthertype,
       "usdEthernetConformance": usdEthernetConformance,
       "usdEthernetCompliances": usdEthernetCompliances,
       "usdEthernetCompliance": usdEthernetCompliance,
       "usdEthernetCompliance2": usdEthernetCompliance2,
       "usdEthernetCompliance3": usdEthernetCompliance3,
       "usdEthernetGroups": usdEthernetGroups,
       "usdEthernetGroup": usdEthernetGroup,
       "usdEthernetSubIfGroup": usdEthernetSubIfGroup,
       "usdVlanGroup": usdVlanGroup,
       "usdVlanSubIfGroup": usdVlanSubIfGroup,
       "usdVlanSubIfGroup2": usdVlanSubIfGroup2}
)
