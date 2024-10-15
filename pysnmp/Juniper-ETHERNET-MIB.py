# SNMP MIB module (Juniper-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:13 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34)
)
juniEthernetMIB.setRevisions(
        ("2006-01-11 21:16",
         "2005-09-14 20:08",
         "2004-12-14 15:14",
         "2004-05-26 19:40",
         "2003-07-28 21:33",
         "2003-02-20 21:51",
         "2002-10-02 15:34",
         "2002-10-01 17:44",
         "2002-04-05 19:47",
         "2001-01-02 16:55",
         "2000-04-18 00:00",
         "2000-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniEthernetIfMauType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("mau10000BaseEr", 16),
          ("mau10000BaseLr", 15),
          ("mau10000BaseSr", 14),
          ("mau1000BaseCx", 5),
          ("mau1000BaseLx", 7),
          ("mau1000BaseSx", 6),
          ("mau1000BaseT", 4),
          ("mau1000BaseZx", 8),
          ("mau100BaseFxMm", 12),
          ("mau100BaseFxSm", 11),
          ("mau100BaseTx", 3),
          ("mau10BaseT", 2),
          ("mauNotPresent", 0),
          ("mauNotSupported", 1),
          ("mauSfpNotJnprCompliant", 13),
          ("mauSfpNotPresent", 10),
          ("mauSfpUnknown", 9),
          ("mauXfpNotJnprCompliant", 19),
          ("mauXfpNotPresent", 18),
          ("mauXfpUnknown", 17))
    )



# MIB Managed Objects in the order of their OIDs

_JuniEthernetObjects_ObjectIdentity = ObjectIdentity
juniEthernetObjects = _JuniEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1)
)
_JuniEthernetIfLayer_ObjectIdentity = ObjectIdentity
juniEthernetIfLayer = _JuniEthernetIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1)
)
_JuniEthernetIfTable_Object = MibTable
juniEthernetIfTable = _JuniEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniEthernetIfTable.setStatus("current")
_JuniEthernetIfEntry_Object = MibTableRow
juniEthernetIfEntry = _JuniEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1)
)
juniEthernetIfEntry.setIndexNames(
    (0, "Juniper-ETHERNET-MIB", "juniEthernetIfIndex"),
)
if mibBuilder.loadTexts:
    juniEthernetIfEntry.setStatus("current")
_JuniEthernetIfIndex_Type = InterfaceIndex
_JuniEthernetIfIndex_Object = MibTableColumn
juniEthernetIfIndex = _JuniEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 1),
    _JuniEthernetIfIndex_Type()
)
juniEthernetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniEthernetIfIndex.setStatus("current")


class _JuniEthernetIfDuplexMode_Type(Integer32):
    """Custom type juniEthernetIfDuplexMode based on Integer32"""
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


_JuniEthernetIfDuplexMode_Type.__name__ = "Integer32"
_JuniEthernetIfDuplexMode_Object = MibTableColumn
juniEthernetIfDuplexMode = _JuniEthernetIfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 2),
    _JuniEthernetIfDuplexMode_Type()
)
juniEthernetIfDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniEthernetIfDuplexMode.setStatus("current")


class _JuniEthernetIfSpeed_Type(Integer32):
    """Custom type juniEthernetIfSpeed based on Integer32"""
    defaultValue = 1

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
        *(("autoNegotiate", 1),
          ("speed10000Mbps", 5),
          ("speed1000Mbps", 4),
          ("speed100Mbps", 3),
          ("speed10Mbps", 2))
    )


_JuniEthernetIfSpeed_Type.__name__ = "Integer32"
_JuniEthernetIfSpeed_Object = MibTableColumn
juniEthernetIfSpeed = _JuniEthernetIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 3),
    _JuniEthernetIfSpeed_Type()
)
juniEthernetIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniEthernetIfSpeed.setStatus("current")


class _JuniEthernetIfMtu_Type(Integer32):
    """Custom type juniEthernetIfMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9188),
    )


_JuniEthernetIfMtu_Type.__name__ = "Integer32"
_JuniEthernetIfMtu_Object = MibTableColumn
juniEthernetIfMtu = _JuniEthernetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 4),
    _JuniEthernetIfMtu_Type()
)
juniEthernetIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniEthernetIfMtu.setStatus("current")


class _JuniEthernetIfOperDuplexMode_Type(Integer32):
    """Custom type juniEthernetIfOperDuplexMode based on Integer32"""
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


_JuniEthernetIfOperDuplexMode_Type.__name__ = "Integer32"
_JuniEthernetIfOperDuplexMode_Object = MibTableColumn
juniEthernetIfOperDuplexMode = _JuniEthernetIfOperDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 5),
    _JuniEthernetIfOperDuplexMode_Type()
)
juniEthernetIfOperDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfOperDuplexMode.setStatus("current")


class _JuniEthernetIfPrimaryMauType_Type(JuniEthernetIfMauType):
    """Custom type juniEthernetIfPrimaryMauType based on JuniEthernetIfMauType"""


_JuniEthernetIfPrimaryMauType_Object = MibTableColumn
juniEthernetIfPrimaryMauType = _JuniEthernetIfPrimaryMauType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 6),
    _JuniEthernetIfPrimaryMauType_Type()
)
juniEthernetIfPrimaryMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfPrimaryMauType.setStatus("current")


class _JuniEthernetIfSecondaryMauType_Type(JuniEthernetIfMauType):
    """Custom type juniEthernetIfSecondaryMauType based on JuniEthernetIfMauType"""


_JuniEthernetIfSecondaryMauType_Object = MibTableColumn
juniEthernetIfSecondaryMauType = _JuniEthernetIfSecondaryMauType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 7),
    _JuniEthernetIfSecondaryMauType_Type()
)
juniEthernetIfSecondaryMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfSecondaryMauType.setStatus("current")


class _JuniEthernetIfPrimaryLength_Type(Integer32):
    """Custom type juniEthernetIfPrimaryLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniEthernetIfPrimaryLength_Type.__name__ = "Integer32"
_JuniEthernetIfPrimaryLength_Object = MibTableColumn
juniEthernetIfPrimaryLength = _JuniEthernetIfPrimaryLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 8),
    _JuniEthernetIfPrimaryLength_Type()
)
juniEthernetIfPrimaryLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfPrimaryLength.setStatus("current")


class _JuniEthernetIfSecondaryLength_Type(Integer32):
    """Custom type juniEthernetIfSecondaryLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniEthernetIfSecondaryLength_Type.__name__ = "Integer32"
_JuniEthernetIfSecondaryLength_Object = MibTableColumn
juniEthernetIfSecondaryLength = _JuniEthernetIfSecondaryLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 9),
    _JuniEthernetIfSecondaryLength_Type()
)
juniEthernetIfSecondaryLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfSecondaryLength.setStatus("current")
_JuniEthernetSubIfLayer_ObjectIdentity = ObjectIdentity
juniEthernetSubIfLayer = _JuniEthernetSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2)
)
_JuniEthernetSubIfNextIfIndex_Type = JuniNextIfIndex
_JuniEthernetSubIfNextIfIndex_Object = MibScalar
juniEthernetSubIfNextIfIndex = _JuniEthernetSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 1),
    _JuniEthernetSubIfNextIfIndex_Type()
)
juniEthernetSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetSubIfNextIfIndex.setStatus("current")
_JuniEthernetSubIfTable_Object = MibTable
juniEthernetSubIfTable = _JuniEthernetSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniEthernetSubIfTable.setStatus("current")
_JuniEthernetSubIfEntry_Object = MibTableRow
juniEthernetSubIfEntry = _JuniEthernetSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1)
)
juniEthernetSubIfEntry.setIndexNames(
    (0, "Juniper-ETHERNET-MIB", "juniEthernetSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniEthernetSubIfEntry.setStatus("current")
_JuniEthernetSubIfIndex_Type = InterfaceIndex
_JuniEthernetSubIfIndex_Object = MibTableColumn
juniEthernetSubIfIndex = _JuniEthernetSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 1),
    _JuniEthernetSubIfIndex_Type()
)
juniEthernetSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniEthernetSubIfIndex.setStatus("current")
_JuniEthernetSubIfRowStatus_Type = RowStatus
_JuniEthernetSubIfRowStatus_Object = MibTableColumn
juniEthernetSubIfRowStatus = _JuniEthernetSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 2),
    _JuniEthernetSubIfRowStatus_Type()
)
juniEthernetSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniEthernetSubIfRowStatus.setStatus("current")
_JuniEthernetSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniEthernetSubIfLowerIfIndex_Object = MibTableColumn
juniEthernetSubIfLowerIfIndex = _JuniEthernetSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 3),
    _JuniEthernetSubIfLowerIfIndex_Type()
)
juniEthernetSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniEthernetSubIfLowerIfIndex.setStatus("current")


class _JuniEthernetSubIfId_Type(Integer32):
    """Custom type juniEthernetSubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniEthernetSubIfId_Type.__name__ = "Integer32"
_JuniEthernetSubIfId_Object = MibTableColumn
juniEthernetSubIfId = _JuniEthernetSubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 4),
    _JuniEthernetSubIfId_Type()
)
juniEthernetSubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniEthernetSubIfId.setStatus("current")
_JuniVlanMajorIfLayer_ObjectIdentity = ObjectIdentity
juniVlanMajorIfLayer = _JuniVlanMajorIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3)
)
_JuniVlanMajorNextIfIndex_Type = JuniNextIfIndex
_JuniVlanMajorNextIfIndex_Object = MibScalar
juniVlanMajorNextIfIndex = _JuniVlanMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 1),
    _JuniVlanMajorNextIfIndex_Type()
)
juniVlanMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniVlanMajorNextIfIndex.setStatus("current")
_JuniVlanMajorIfTable_Object = MibTable
juniVlanMajorIfTable = _JuniVlanMajorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniVlanMajorIfTable.setStatus("current")
_JuniVlanMajorIfEntry_Object = MibTableRow
juniVlanMajorIfEntry = _JuniVlanMajorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1)
)
juniVlanMajorIfEntry.setIndexNames(
    (0, "Juniper-ETHERNET-MIB", "juniVlanMajorIfIndex"),
)
if mibBuilder.loadTexts:
    juniVlanMajorIfEntry.setStatus("current")
_JuniVlanMajorIfIndex_Type = InterfaceIndex
_JuniVlanMajorIfIndex_Object = MibTableColumn
juniVlanMajorIfIndex = _JuniVlanMajorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 1),
    _JuniVlanMajorIfIndex_Type()
)
juniVlanMajorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniVlanMajorIfIndex.setStatus("current")
_JuniVlanMajorIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniVlanMajorIfLowerIfIndex_Object = MibTableColumn
juniVlanMajorIfLowerIfIndex = _JuniVlanMajorIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 2),
    _JuniVlanMajorIfLowerIfIndex_Type()
)
juniVlanMajorIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanMajorIfLowerIfIndex.setStatus("current")
_JuniVlanMajorIfRowStatus_Type = RowStatus
_JuniVlanMajorIfRowStatus_Object = MibTableColumn
juniVlanMajorIfRowStatus = _JuniVlanMajorIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 3),
    _JuniVlanMajorIfRowStatus_Type()
)
juniVlanMajorIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanMajorIfRowStatus.setStatus("current")
_JuniVlanSubIfLayer_ObjectIdentity = ObjectIdentity
juniVlanSubIfLayer = _JuniVlanSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4)
)
_JuniVlanSubNextIfIndex_Type = JuniNextIfIndex
_JuniVlanSubNextIfIndex_Object = MibScalar
juniVlanSubNextIfIndex = _JuniVlanSubNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 1),
    _JuniVlanSubNextIfIndex_Type()
)
juniVlanSubNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniVlanSubNextIfIndex.setStatus("current")
_JuniVlanSubIfTable_Object = MibTable
juniVlanSubIfTable = _JuniVlanSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniVlanSubIfTable.setStatus("current")
_JuniVlanSubIfEntry_Object = MibTableRow
juniVlanSubIfEntry = _JuniVlanSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1)
)
juniVlanSubIfEntry.setIndexNames(
    (0, "Juniper-ETHERNET-MIB", "juniVlanSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniVlanSubIfEntry.setStatus("current")
_JuniVlanSubIfIndex_Type = InterfaceIndex
_JuniVlanSubIfIndex_Object = MibTableColumn
juniVlanSubIfIndex = _JuniVlanSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 1),
    _JuniVlanSubIfIndex_Type()
)
juniVlanSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniVlanSubIfIndex.setStatus("current")


class _JuniVlanSubIfVlanId_Type(Integer32):
    """Custom type juniVlanSubIfVlanId based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(5000, 5000),
        ValueRangeConstraint(5001, 5001),
    )


_JuniVlanSubIfVlanId_Type.__name__ = "Integer32"
_JuniVlanSubIfVlanId_Object = MibTableColumn
juniVlanSubIfVlanId = _JuniVlanSubIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 2),
    _JuniVlanSubIfVlanId_Type()
)
juniVlanSubIfVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanId.setStatus("current")
_JuniVlanSubIfVlanUntagged_Type = TruthValue
_JuniVlanSubIfVlanUntagged_Object = MibTableColumn
juniVlanSubIfVlanUntagged = _JuniVlanSubIfVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 3),
    _JuniVlanSubIfVlanUntagged_Type()
)
juniVlanSubIfVlanUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanUntagged.setStatus("current")
_JuniVlanSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniVlanSubIfLowerIfIndex_Object = MibTableColumn
juniVlanSubIfLowerIfIndex = _JuniVlanSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 4),
    _JuniVlanSubIfLowerIfIndex_Type()
)
juniVlanSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfLowerIfIndex.setStatus("current")
_JuniVlanSubIfRowStatus_Type = RowStatus
_JuniVlanSubIfRowStatus_Object = MibTableColumn
juniVlanSubIfRowStatus = _JuniVlanSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 5),
    _JuniVlanSubIfRowStatus_Type()
)
juniVlanSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfRowStatus.setStatus("current")


class _JuniVlanSubIfVlanStackId_Type(Integer32):
    """Custom type juniVlanSubIfVlanStackId based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(5000, 5000),
    )


_JuniVlanSubIfVlanStackId_Type.__name__ = "Integer32"
_JuniVlanSubIfVlanStackId_Object = MibTableColumn
juniVlanSubIfVlanStackId = _JuniVlanSubIfVlanStackId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 6),
    _JuniVlanSubIfVlanStackId_Type()
)
juniVlanSubIfVlanStackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanStackId.setStatus("current")


class _JuniVlanSubIfVlanStackEthertype_Type(Integer32):
    """Custom type juniVlanSubIfVlanStackEthertype based on Integer32"""
    defaultValue = 37120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33024,
              34984,
              37120)
        )
    )
    namedValues = NamedValues(
        *(("etherType8100h", 33024),
          ("etherType88a8h", 34984),
          ("etherType9100h", 37120))
    )


_JuniVlanSubIfVlanStackEthertype_Type.__name__ = "Integer32"
_JuniVlanSubIfVlanStackEthertype_Object = MibTableColumn
juniVlanSubIfVlanStackEthertype = _JuniVlanSubIfVlanStackEthertype_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 7),
    _JuniVlanSubIfVlanStackEthertype_Type()
)
juniVlanSubIfVlanStackEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanStackEthertype.setStatus("current")


class _JuniVlanSubIfVlanAdvisoryRxSpeed_Type(Integer32):
    """Custom type juniVlanSubIfVlanAdvisoryRxSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniVlanSubIfVlanAdvisoryRxSpeed_Type.__name__ = "Integer32"
_JuniVlanSubIfVlanAdvisoryRxSpeed_Object = MibTableColumn
juniVlanSubIfVlanAdvisoryRxSpeed = _JuniVlanSubIfVlanAdvisoryRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 8),
    _JuniVlanSubIfVlanAdvisoryRxSpeed_Type()
)
juniVlanSubIfVlanAdvisoryRxSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanAdvisoryRxSpeed.setStatus("current")


class _JuniVlanSubIfVlanAdvisoryTxSpeed_Type(Integer32):
    """Custom type juniVlanSubIfVlanAdvisoryTxSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniVlanSubIfVlanAdvisoryTxSpeed_Type.__name__ = "Integer32"
_JuniVlanSubIfVlanAdvisoryTxSpeed_Object = MibTableColumn
juniVlanSubIfVlanAdvisoryTxSpeed = _JuniVlanSubIfVlanAdvisoryTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 9),
    _JuniVlanSubIfVlanAdvisoryTxSpeed_Type()
)
juniVlanSubIfVlanAdvisoryTxSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniVlanSubIfVlanAdvisoryTxSpeed.setStatus("current")
_JuniEthernetIfStats_ObjectIdentity = ObjectIdentity
juniEthernetIfStats = _JuniEthernetIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5)
)
_JuniEthernetIfStatsTable_Object = MibTable
juniEthernetIfStatsTable = _JuniEthernetIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniEthernetIfStatsTable.setStatus("current")
_JuniEthernetIfStatsEntry_Object = MibTableRow
juniEthernetIfStatsEntry = _JuniEthernetIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1)
)
juniEthernetIfStatsEntry.setIndexNames(
    (0, "Juniper-ETHERNET-MIB", "juniEthernetIfStatsIndex"),
)
if mibBuilder.loadTexts:
    juniEthernetIfStatsEntry.setStatus("current")
_JuniEthernetIfStatsIndex_Type = InterfaceIndex
_JuniEthernetIfStatsIndex_Object = MibTableColumn
juniEthernetIfStatsIndex = _JuniEthernetIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 1),
    _JuniEthernetIfStatsIndex_Type()
)
juniEthernetIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniEthernetIfStatsIndex.setStatus("current")


class _JuniEthernetIfIngressLineUtilization_Type(Unsigned32):
    """Custom type juniEthernetIfIngressLineUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniEthernetIfIngressLineUtilization_Type.__name__ = "Unsigned32"
_JuniEthernetIfIngressLineUtilization_Object = MibTableColumn
juniEthernetIfIngressLineUtilization = _JuniEthernetIfIngressLineUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 2),
    _JuniEthernetIfIngressLineUtilization_Type()
)
juniEthernetIfIngressLineUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfIngressLineUtilization.setStatus("current")
if mibBuilder.loadTexts:
    juniEthernetIfIngressLineUtilization.setUnits("percent")


class _JuniEthernetIfEgressLineUtilization_Type(Unsigned32):
    """Custom type juniEthernetIfEgressLineUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniEthernetIfEgressLineUtilization_Type.__name__ = "Unsigned32"
_JuniEthernetIfEgressLineUtilization_Object = MibTableColumn
juniEthernetIfEgressLineUtilization = _JuniEthernetIfEgressLineUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 3),
    _JuniEthernetIfEgressLineUtilization_Type()
)
juniEthernetIfEgressLineUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniEthernetIfEgressLineUtilization.setStatus("current")
if mibBuilder.loadTexts:
    juniEthernetIfEgressLineUtilization.setUnits("percent")
_JuniLagIfLayer_ObjectIdentity = ObjectIdentity
juniLagIfLayer = _JuniLagIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 6)
)
_JuniLagNextIfIndex_Type = JuniNextIfIndex
_JuniLagNextIfIndex_Object = MibScalar
juniLagNextIfIndex = _JuniLagNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 6, 1),
    _JuniLagNextIfIndex_Type()
)
juniLagNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLagNextIfIndex.setStatus("current")
_JuniEthernetConformance_ObjectIdentity = ObjectIdentity
juniEthernetConformance = _JuniEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4)
)
_JuniEthernetCompliances_ObjectIdentity = ObjectIdentity
juniEthernetCompliances = _JuniEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1)
)
_JuniEthernetGroups_ObjectIdentity = ObjectIdentity
juniEthernetGroups = _JuniEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2)
)

# Managed Objects groups

juniEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 1)
)
juniEthernetGroup.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniEthernetIfDuplexMode"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfSpeed"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfMtu"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfOperDuplexMode"))
)
if mibBuilder.loadTexts:
    juniEthernetGroup.setStatus("obsolete")

juniEthernetSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 2)
)
juniEthernetSubIfGroup.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniEthernetSubIfNextIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniEthernetSubIfRowStatus"),
        ("Juniper-ETHERNET-MIB", "juniEthernetSubIfLowerIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniEthernetSubIfId"))
)
if mibBuilder.loadTexts:
    juniEthernetSubIfGroup.setStatus("current")

juniVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 3)
)
juniVlanGroup.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniVlanMajorNextIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanMajorIfLowerIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanMajorIfRowStatus"))
)
if mibBuilder.loadTexts:
    juniVlanGroup.setStatus("current")

juniVlanSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 4)
)
juniVlanSubIfGroup.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniVlanSubNextIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanId"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanUntagged"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfLowerIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfRowStatus"))
)
if mibBuilder.loadTexts:
    juniVlanSubIfGroup.setStatus("obsolete")

juniVlanSubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 5)
)
juniVlanSubIfGroup2.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniVlanSubNextIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanId"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanUntagged"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanStackId"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfLowerIfIndex"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfRowStatus"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanStackEthertype"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanAdvisoryRxSpeed"),
        ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanAdvisoryTxSpeed"))
)
if mibBuilder.loadTexts:
    juniVlanSubIfGroup2.setStatus("current")

juniEthernetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 6)
)
juniEthernetGroup2.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniEthernetIfDuplexMode"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfSpeed"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfMtu"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfOperDuplexMode"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfPrimaryMauType"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfSecondaryMauType"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfPrimaryLength"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfSecondaryLength"))
)
if mibBuilder.loadTexts:
    juniEthernetGroup2.setStatus("current")

juniEthernetIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 7)
)
juniEthernetIfStatsGroup.setObjects(
      *(("Juniper-ETHERNET-MIB", "juniEthernetIfIngressLineUtilization"),
        ("Juniper-ETHERNET-MIB", "juniEthernetIfEgressLineUtilization"))
)
if mibBuilder.loadTexts:
    juniEthernetIfStatsGroup.setStatus("current")

juniLagIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 8)
)
juniLagIfGroup.setObjects(
    ("Juniper-ETHERNET-MIB", "juniLagNextIfIndex")
)
if mibBuilder.loadTexts:
    juniLagIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance.setStatus(
        "obsolete"
    )

juniEthernetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance2.setStatus(
        "obsolete"
    )

juniEthernetCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance3.setStatus(
        "obsolete"
    )

juniEthernetCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance4.setStatus(
        "obsolete"
    )

juniEthernetCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance5.setStatus(
        "obsolete"
    )

juniEthernetCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniEthernetCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ETHERNET-MIB",
    **{"JuniEthernetIfMauType": JuniEthernetIfMauType,
       "juniEthernetMIB": juniEthernetMIB,
       "juniEthernetObjects": juniEthernetObjects,
       "juniEthernetIfLayer": juniEthernetIfLayer,
       "juniEthernetIfTable": juniEthernetIfTable,
       "juniEthernetIfEntry": juniEthernetIfEntry,
       "juniEthernetIfIndex": juniEthernetIfIndex,
       "juniEthernetIfDuplexMode": juniEthernetIfDuplexMode,
       "juniEthernetIfSpeed": juniEthernetIfSpeed,
       "juniEthernetIfMtu": juniEthernetIfMtu,
       "juniEthernetIfOperDuplexMode": juniEthernetIfOperDuplexMode,
       "juniEthernetIfPrimaryMauType": juniEthernetIfPrimaryMauType,
       "juniEthernetIfSecondaryMauType": juniEthernetIfSecondaryMauType,
       "juniEthernetIfPrimaryLength": juniEthernetIfPrimaryLength,
       "juniEthernetIfSecondaryLength": juniEthernetIfSecondaryLength,
       "juniEthernetSubIfLayer": juniEthernetSubIfLayer,
       "juniEthernetSubIfNextIfIndex": juniEthernetSubIfNextIfIndex,
       "juniEthernetSubIfTable": juniEthernetSubIfTable,
       "juniEthernetSubIfEntry": juniEthernetSubIfEntry,
       "juniEthernetSubIfIndex": juniEthernetSubIfIndex,
       "juniEthernetSubIfRowStatus": juniEthernetSubIfRowStatus,
       "juniEthernetSubIfLowerIfIndex": juniEthernetSubIfLowerIfIndex,
       "juniEthernetSubIfId": juniEthernetSubIfId,
       "juniVlanMajorIfLayer": juniVlanMajorIfLayer,
       "juniVlanMajorNextIfIndex": juniVlanMajorNextIfIndex,
       "juniVlanMajorIfTable": juniVlanMajorIfTable,
       "juniVlanMajorIfEntry": juniVlanMajorIfEntry,
       "juniVlanMajorIfIndex": juniVlanMajorIfIndex,
       "juniVlanMajorIfLowerIfIndex": juniVlanMajorIfLowerIfIndex,
       "juniVlanMajorIfRowStatus": juniVlanMajorIfRowStatus,
       "juniVlanSubIfLayer": juniVlanSubIfLayer,
       "juniVlanSubNextIfIndex": juniVlanSubNextIfIndex,
       "juniVlanSubIfTable": juniVlanSubIfTable,
       "juniVlanSubIfEntry": juniVlanSubIfEntry,
       "juniVlanSubIfIndex": juniVlanSubIfIndex,
       "juniVlanSubIfVlanId": juniVlanSubIfVlanId,
       "juniVlanSubIfVlanUntagged": juniVlanSubIfVlanUntagged,
       "juniVlanSubIfLowerIfIndex": juniVlanSubIfLowerIfIndex,
       "juniVlanSubIfRowStatus": juniVlanSubIfRowStatus,
       "juniVlanSubIfVlanStackId": juniVlanSubIfVlanStackId,
       "juniVlanSubIfVlanStackEthertype": juniVlanSubIfVlanStackEthertype,
       "juniVlanSubIfVlanAdvisoryRxSpeed": juniVlanSubIfVlanAdvisoryRxSpeed,
       "juniVlanSubIfVlanAdvisoryTxSpeed": juniVlanSubIfVlanAdvisoryTxSpeed,
       "juniEthernetIfStats": juniEthernetIfStats,
       "juniEthernetIfStatsTable": juniEthernetIfStatsTable,
       "juniEthernetIfStatsEntry": juniEthernetIfStatsEntry,
       "juniEthernetIfStatsIndex": juniEthernetIfStatsIndex,
       "juniEthernetIfIngressLineUtilization": juniEthernetIfIngressLineUtilization,
       "juniEthernetIfEgressLineUtilization": juniEthernetIfEgressLineUtilization,
       "juniLagIfLayer": juniLagIfLayer,
       "juniLagNextIfIndex": juniLagNextIfIndex,
       "juniEthernetConformance": juniEthernetConformance,
       "juniEthernetCompliances": juniEthernetCompliances,
       "juniEthernetCompliance": juniEthernetCompliance,
       "juniEthernetCompliance2": juniEthernetCompliance2,
       "juniEthernetCompliance3": juniEthernetCompliance3,
       "juniEthernetCompliance4": juniEthernetCompliance4,
       "juniEthernetCompliance5": juniEthernetCompliance5,
       "juniEthernetCompliance6": juniEthernetCompliance6,
       "juniEthernetGroups": juniEthernetGroups,
       "juniEthernetGroup": juniEthernetGroup,
       "juniEthernetSubIfGroup": juniEthernetSubIfGroup,
       "juniVlanGroup": juniVlanGroup,
       "juniVlanSubIfGroup": juniVlanSubIfGroup,
       "juniVlanSubIfGroup2": juniVlanSubIfGroup2,
       "juniEthernetGroup2": juniEthernetGroup2,
       "juniEthernetIfStatsGroup": juniEthernetIfStatsGroup,
       "juniLagIfGroup": juniLagIfGroup}
)
