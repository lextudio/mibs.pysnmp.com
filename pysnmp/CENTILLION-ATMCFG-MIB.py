# SNMP MIB module (CENTILLION-ATMCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-ATMCFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:05 2024
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

(EnableIndicator,
 atmConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "atmConfig")

(VirtualSegmentTypeId,) = mibBuilder.importSymbols(
    "CENTILLION-VIRTUALSEGMENT-MIB",
    "VirtualSegmentTypeId")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmElanConfig_ObjectIdentity = ObjectIdentity
atmElanConfig = _AtmElanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1)
)
_AtmElanConfigTable_Object = MibTable
atmElanConfigTable = _AtmElanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmElanConfigTable.setStatus("mandatory")
_AtmElanConfigEntry_Object = MibTableRow
atmElanConfigEntry = _AtmElanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1)
)
atmElanConfigEntry.setIndexNames(
    (0, "CENTILLION-ATMCFG-MIB", "atmElanIndex"),
)
if mibBuilder.loadTexts:
    atmElanConfigEntry.setStatus("mandatory")


class _AtmElanIndex_Type(Integer32):
    """Custom type atmElanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmElanIndex_Type.__name__ = "Integer32"
_AtmElanIndex_Object = MibTableColumn
atmElanIndex = _AtmElanIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 1),
    _AtmElanIndex_Type()
)
atmElanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanIndex.setStatus("mandatory")


class _AtmElanType_Type(Integer32):
    """Custom type atmElanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atm1483Xob", 5),
          ("atmElanBe", 2),
          ("atmElanXob", 1),
          ("atmLecBe", 4),
          ("atmLecXob", 3),
          ("atmNullXob", 6))
    )


_AtmElanType_Type.__name__ = "Integer32"
_AtmElanType_Object = MibTableColumn
atmElanType = _AtmElanType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 2),
    _AtmElanType_Type()
)
atmElanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanType.setStatus("mandatory")


class _AtmElanEnable_Type(Integer32):
    """Custom type atmElanEnable based on Integer32"""
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


_AtmElanEnable_Type.__name__ = "Integer32"
_AtmElanEnable_Object = MibTableColumn
atmElanEnable = _AtmElanEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 3),
    _AtmElanEnable_Type()
)
atmElanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanEnable.setStatus("mandatory")
_AtmElanAllCkts_Type = OctetString
_AtmElanAllCkts_Object = MibTableColumn
atmElanAllCkts = _AtmElanAllCkts_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 4),
    _AtmElanAllCkts_Type()
)
atmElanAllCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanAllCkts.setStatus("mandatory")
_AtmElanVirtualCard_Type = Integer32
_AtmElanVirtualCard_Object = MibTableColumn
atmElanVirtualCard = _AtmElanVirtualCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 5),
    _AtmElanVirtualCard_Type()
)
atmElanVirtualCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanVirtualCard.setStatus("mandatory")
_AtmElanVirtualPort_Type = Integer32
_AtmElanVirtualPort_Object = MibTableColumn
atmElanVirtualPort = _AtmElanVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 6),
    _AtmElanVirtualPort_Type()
)
atmElanVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanVirtualPort.setStatus("mandatory")
_AtmElanVirtualSegmentId_Type = Integer32
_AtmElanVirtualSegmentId_Object = MibTableColumn
atmElanVirtualSegmentId = _AtmElanVirtualSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 7),
    _AtmElanVirtualSegmentId_Type()
)
atmElanVirtualSegmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanVirtualSegmentId.setStatus("mandatory")


class _AtmElanStatus_Type(Integer32):
    """Custom type atmElanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AtmElanStatus_Type.__name__ = "Integer32"
_AtmElanStatus_Object = MibTableColumn
atmElanStatus = _AtmElanStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 8),
    _AtmElanStatus_Type()
)
atmElanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanStatus.setStatus("mandatory")
_AtmElanVirtualSegmentType_Type = VirtualSegmentTypeId
_AtmElanVirtualSegmentType_Object = MibTableColumn
atmElanVirtualSegmentType = _AtmElanVirtualSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 9),
    _AtmElanVirtualSegmentType_Type()
)
atmElanVirtualSegmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanVirtualSegmentType.setStatus("mandatory")
_AtmElanBridgeGroupId_Type = Integer32
_AtmElanBridgeGroupId_Object = MibTableColumn
atmElanBridgeGroupId = _AtmElanBridgeGroupId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 10),
    _AtmElanBridgeGroupId_Type()
)
atmElanBridgeGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanBridgeGroupId.setStatus("mandatory")


class _AtmElanMaxUnknownFrameCount_Type(Integer32):
    """Custom type atmElanMaxUnknownFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmElanMaxUnknownFrameCount_Type.__name__ = "Integer32"
_AtmElanMaxUnknownFrameCount_Object = MibTableColumn
atmElanMaxUnknownFrameCount = _AtmElanMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 11),
    _AtmElanMaxUnknownFrameCount_Type()
)
atmElanMaxUnknownFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanMaxUnknownFrameCount.setStatus("mandatory")


class _AtmElanMaxUnknownFrameTime_Type(Integer32):
    """Custom type atmElanMaxUnknownFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AtmElanMaxUnknownFrameTime_Type.__name__ = "Integer32"
_AtmElanMaxUnknownFrameTime_Object = MibTableColumn
atmElanMaxUnknownFrameTime = _AtmElanMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 12),
    _AtmElanMaxUnknownFrameTime_Type()
)
atmElanMaxUnknownFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanMaxUnknownFrameTime.setStatus("mandatory")


class _AtmElanVcBridgingEnable_Type(EnableIndicator):
    """Custom type atmElanVcBridgingEnable based on EnableIndicator"""


_AtmElanVcBridgingEnable_Object = MibTableColumn
atmElanVcBridgingEnable = _AtmElanVcBridgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 13),
    _AtmElanVcBridgingEnable_Type()
)
atmElanVcBridgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmElanVcBridgingEnable.setStatus("mandatory")
_AtmCktTable_ObjectIdentity = ObjectIdentity
atmCktTable = _AtmCktTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2)
)
_AtmPktCktTable_Object = MibTable
atmPktCktTable = _AtmPktCktTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmPktCktTable.setStatus("mandatory")
_AtmPktCktEntry_Object = MibTableRow
atmPktCktEntry = _AtmPktCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1)
)
atmPktCktEntry.setIndexNames(
    (0, "CENTILLION-ATMCFG-MIB", "atmPktCktIndex"),
)
if mibBuilder.loadTexts:
    atmPktCktEntry.setStatus("mandatory")


class _AtmPktCktIndex_Type(Integer32):
    """Custom type atmPktCktIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmPktCktIndex_Type.__name__ = "Integer32"
_AtmPktCktIndex_Object = MibTableColumn
atmPktCktIndex = _AtmPktCktIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 1),
    _AtmPktCktIndex_Type()
)
atmPktCktIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktIndex.setStatus("mandatory")


class _AtmPktCktPriority_Type(Integer32):
    """Custom type atmPktCktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("normalPriority", 1))
    )


_AtmPktCktPriority_Type.__name__ = "Integer32"
_AtmPktCktPriority_Object = MibTableColumn
atmPktCktPriority = _AtmPktCktPriority_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 2),
    _AtmPktCktPriority_Type()
)
atmPktCktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktPriority.setStatus("mandatory")


class _AtmPktCktEnable_Type(Integer32):
    """Custom type atmPktCktEnable based on Integer32"""
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


_AtmPktCktEnable_Type.__name__ = "Integer32"
_AtmPktCktEnable_Object = MibTableColumn
atmPktCktEnable = _AtmPktCktEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 3),
    _AtmPktCktEnable_Type()
)
atmPktCktEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktEnable.setStatus("mandatory")


class _AtmPktCktType_Type(Integer32):
    """Custom type atmPktCktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("virtualCkt", 1),
          ("virtualPathCkt", 2))
    )


_AtmPktCktType_Type.__name__ = "Integer32"
_AtmPktCktType_Object = MibTableColumn
atmPktCktType = _AtmPktCktType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 4),
    _AtmPktCktType_Type()
)
atmPktCktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktType.setStatus("mandatory")


class _AtmPktCktCost_Type(Integer32):
    """Custom type atmPktCktCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPktCktCost_Type.__name__ = "Integer32"
_AtmPktCktCost_Object = MibTableColumn
atmPktCktCost = _AtmPktCktCost_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 5),
    _AtmPktCktCost_Type()
)
atmPktCktCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktCost.setStatus("mandatory")


class _AtmPktCktElanIndex_Type(Integer32):
    """Custom type atmPktCktElanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmPktCktElanIndex_Type.__name__ = "Integer32"
_AtmPktCktElanIndex_Object = MibTableColumn
atmPktCktElanIndex = _AtmPktCktElanIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 6),
    _AtmPktCktElanIndex_Type()
)
atmPktCktElanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktElanIndex.setStatus("mandatory")
_AtmPktCktCardPort_Type = Integer32
_AtmPktCktCardPort_Object = MibTableColumn
atmPktCktCardPort = _AtmPktCktCardPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 7),
    _AtmPktCktCardPort_Type()
)
atmPktCktCardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktCardPort.setStatus("deprecated")
_AtmPktCktVpi_Type = Integer32
_AtmPktCktVpi_Object = MibTableColumn
atmPktCktVpi = _AtmPktCktVpi_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 8),
    _AtmPktCktVpi_Type()
)
atmPktCktVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktVpi.setStatus("mandatory")
_AtmPktCktVci_Type = Integer32
_AtmPktCktVci_Object = MibTableColumn
atmPktCktVci = _AtmPktCktVci_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 9),
    _AtmPktCktVci_Type()
)
atmPktCktVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktVci.setStatus("mandatory")


class _AtmPktCktStatus_Type(Integer32):
    """Custom type atmPktCktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AtmPktCktStatus_Type.__name__ = "Integer32"
_AtmPktCktStatus_Object = MibTableColumn
atmPktCktStatus = _AtmPktCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 10),
    _AtmPktCktStatus_Type()
)
atmPktCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktStatus.setStatus("mandatory")
_AtmPktCktCardPort2_Type = Integer32
_AtmPktCktCardPort2_Object = MibTableColumn
atmPktCktCardPort2 = _AtmPktCktCardPort2_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 11),
    _AtmPktCktCardPort2_Type()
)
atmPktCktCardPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPktCktCardPort2.setStatus("mandatory")
_AtmCellCktTable_Object = MibTable
atmCellCktTable = _AtmCellCktTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    atmCellCktTable.setStatus("mandatory")
_AtmCellCktEntry_Object = MibTableRow
atmCellCktEntry = _AtmCellCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1)
)
atmCellCktEntry.setIndexNames(
    (0, "CENTILLION-ATMCFG-MIB", "atmCellCktIndex"),
)
if mibBuilder.loadTexts:
    atmCellCktEntry.setStatus("mandatory")
_AtmCellCktIndex_Type = Integer32
_AtmCellCktIndex_Object = MibTableColumn
atmCellCktIndex = _AtmCellCktIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 1),
    _AtmCellCktIndex_Type()
)
atmCellCktIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktIndex.setStatus("mandatory")


class _AtmCellCktPriority_Type(Integer32):
    """Custom type atmCellCktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("normPriority", 1))
    )


_AtmCellCktPriority_Type.__name__ = "Integer32"
_AtmCellCktPriority_Object = MibTableColumn
atmCellCktPriority = _AtmCellCktPriority_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 2),
    _AtmCellCktPriority_Type()
)
atmCellCktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktPriority.setStatus("mandatory")


class _AtmCellCktEnable_Type(Integer32):
    """Custom type atmCellCktEnable based on Integer32"""
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


_AtmCellCktEnable_Type.__name__ = "Integer32"
_AtmCellCktEnable_Object = MibTableColumn
atmCellCktEnable = _AtmCellCktEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 3),
    _AtmCellCktEnable_Type()
)
atmCellCktEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktEnable.setStatus("mandatory")


class _AtmCellCktType_Type(Integer32):
    """Custom type atmCellCktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("virtualCkt", 1),
          ("virtualPathCkt", 2))
    )


_AtmCellCktType_Type.__name__ = "Integer32"
_AtmCellCktType_Object = MibTableColumn
atmCellCktType = _AtmCellCktType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 4),
    _AtmCellCktType_Type()
)
atmCellCktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktType.setStatus("mandatory")
_AtmCellCktNumEndpt_Type = Integer32
_AtmCellCktNumEndpt_Object = MibTableColumn
atmCellCktNumEndpt = _AtmCellCktNumEndpt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 5),
    _AtmCellCktNumEndpt_Type()
)
atmCellCktNumEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktNumEndpt.setStatus("mandatory")
_AtmCellCktEndptList_Type = OctetString
_AtmCellCktEndptList_Object = MibTableColumn
atmCellCktEndptList = _AtmCellCktEndptList_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 6),
    _AtmCellCktEndptList_Type()
)
atmCellCktEndptList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktEndptList.setStatus("mandatory")


class _AtmCellCktStatus_Type(Integer32):
    """Custom type atmCellCktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AtmCellCktStatus_Type.__name__ = "Integer32"
_AtmCellCktStatus_Object = MibTableColumn
atmCellCktStatus = _AtmCellCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 7),
    _AtmCellCktStatus_Type()
)
atmCellCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCellCktStatus.setStatus("mandatory")
_AtmPortConfig_ObjectIdentity = ObjectIdentity
atmPortConfig = _AtmPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3)
)
_AtmPortConfigTable_Object = MibTable
atmPortConfigTable = _AtmPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmPortConfigTable.setStatus("mandatory")
_AtmPortConfigEntry_Object = MibTableRow
atmPortConfigEntry = _AtmPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1)
)
atmPortConfigEntry.setIndexNames(
    (0, "CENTILLION-ATMCFG-MIB", "atmPortCardIndex"),
    (0, "CENTILLION-ATMCFG-MIB", "atmPortPortIndex"),
)
if mibBuilder.loadTexts:
    atmPortConfigEntry.setStatus("mandatory")


class _AtmPortCardIndex_Type(Integer32):
    """Custom type atmPortCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtmPortCardIndex_Type.__name__ = "Integer32"
_AtmPortCardIndex_Object = MibTableColumn
atmPortCardIndex = _AtmPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 1),
    _AtmPortCardIndex_Type()
)
atmPortCardIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortCardIndex.setStatus("mandatory")


class _AtmPortPortIndex_Type(Integer32):
    """Custom type atmPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtmPortPortIndex_Type.__name__ = "Integer32"
_AtmPortPortIndex_Object = MibTableColumn
atmPortPortIndex = _AtmPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 2),
    _AtmPortPortIndex_Type()
)
atmPortPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortPortIndex.setStatus("mandatory")


class _AtmPortEnable_Type(Integer32):
    """Custom type atmPortEnable based on Integer32"""
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


_AtmPortEnable_Type.__name__ = "Integer32"
_AtmPortEnable_Object = MibTableColumn
atmPortEnable = _AtmPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 3),
    _AtmPortEnable_Type()
)
atmPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortEnable.setStatus("mandatory")


class _AtmPortLoopTimingEnable_Type(Integer32):
    """Custom type atmPortLoopTimingEnable based on Integer32"""
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


_AtmPortLoopTimingEnable_Type.__name__ = "Integer32"
_AtmPortLoopTimingEnable_Object = MibTableColumn
atmPortLoopTimingEnable = _AtmPortLoopTimingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 4),
    _AtmPortLoopTimingEnable_Type()
)
atmPortLoopTimingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLoopTimingEnable.setStatus("mandatory")


class _AtmPortHecCosetEnable_Type(Integer32):
    """Custom type atmPortHecCosetEnable based on Integer32"""
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


_AtmPortHecCosetEnable_Type.__name__ = "Integer32"
_AtmPortHecCosetEnable_Object = MibTableColumn
atmPortHecCosetEnable = _AtmPortHecCosetEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 5),
    _AtmPortHecCosetEnable_Type()
)
atmPortHecCosetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortHecCosetEnable.setStatus("mandatory")


class _AtmPortHecCorrectionEnable_Type(Integer32):
    """Custom type atmPortHecCorrectionEnable based on Integer32"""
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


_AtmPortHecCorrectionEnable_Type.__name__ = "Integer32"
_AtmPortHecCorrectionEnable_Object = MibTableColumn
atmPortHecCorrectionEnable = _AtmPortHecCorrectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 6),
    _AtmPortHecCorrectionEnable_Type()
)
atmPortHecCorrectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortHecCorrectionEnable.setStatus("mandatory")


class _AtmPortHardwareFrameMode_Type(Integer32):
    """Custom type atmPortHardwareFrameMode based on Integer32"""
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
        *(("notapply", 3),
          ("other", 4),
          ("sdh", 2),
          ("sonet", 1))
    )


_AtmPortHardwareFrameMode_Type.__name__ = "Integer32"
_AtmPortHardwareFrameMode_Object = MibTableColumn
atmPortHardwareFrameMode = _AtmPortHardwareFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 7),
    _AtmPortHardwareFrameMode_Type()
)
atmPortHardwareFrameMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortHardwareFrameMode.setStatus("mandatory")


class _AtmPortLocalLoopEnable_Type(Integer32):
    """Custom type atmPortLocalLoopEnable based on Integer32"""
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


_AtmPortLocalLoopEnable_Type.__name__ = "Integer32"
_AtmPortLocalLoopEnable_Object = MibTableColumn
atmPortLocalLoopEnable = _AtmPortLocalLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 8),
    _AtmPortLocalLoopEnable_Type()
)
atmPortLocalLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLocalLoopEnable.setStatus("mandatory")


class _AtmPortRemoteLoopEnable_Type(Integer32):
    """Custom type atmPortRemoteLoopEnable based on Integer32"""
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


_AtmPortRemoteLoopEnable_Type.__name__ = "Integer32"
_AtmPortRemoteLoopEnable_Object = MibTableColumn
atmPortRemoteLoopEnable = _AtmPortRemoteLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 9),
    _AtmPortRemoteLoopEnable_Type()
)
atmPortRemoteLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortRemoteLoopEnable.setStatus("mandatory")


class _AtmPortForceHecErrorEnable_Type(Integer32):
    """Custom type atmPortForceHecErrorEnable based on Integer32"""
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


_AtmPortForceHecErrorEnable_Type.__name__ = "Integer32"
_AtmPortForceHecErrorEnable_Object = MibTableColumn
atmPortForceHecErrorEnable = _AtmPortForceHecErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 10),
    _AtmPortForceHecErrorEnable_Type()
)
atmPortForceHecErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortForceHecErrorEnable.setStatus("mandatory")


class _AtmPortScramblingEnable_Type(Integer32):
    """Custom type atmPortScramblingEnable based on Integer32"""
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


_AtmPortScramblingEnable_Type.__name__ = "Integer32"
_AtmPortScramblingEnable_Object = MibTableColumn
atmPortScramblingEnable = _AtmPortScramblingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 11),
    _AtmPortScramblingEnable_Type()
)
atmPortScramblingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortScramblingEnable.setStatus("mandatory")


class _AtmPortSigEntityType_Type(Integer32):
    """Custom type atmPortSigEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 3),
          ("noSig", 1),
          ("uni", 2))
    )


_AtmPortSigEntityType_Type.__name__ = "Integer32"
_AtmPortSigEntityType_Object = MibTableColumn
atmPortSigEntityType = _AtmPortSigEntityType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 12),
    _AtmPortSigEntityType_Type()
)
atmPortSigEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortSigEntityType.setStatus("mandatory")


class _AtmPortSigEntityRole_Type(Integer32):
    """Custom type atmPortSigEntityRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netw", 3),
          ("other", 1),
          ("user", 2))
    )


_AtmPortSigEntityRole_Type.__name__ = "Integer32"
_AtmPortSigEntityRole_Object = MibTableColumn
atmPortSigEntityRole = _AtmPortSigEntityRole_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 13),
    _AtmPortSigEntityRole_Type()
)
atmPortSigEntityRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortSigEntityRole.setStatus("mandatory")


class _AtmPortSigVersion_Type(Integer32):
    """Custom type atmPortSigVersion based on Integer32"""
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
        *(("auto", 2),
          ("other", 1),
          ("uni30", 3),
          ("uni31", 4))
    )


_AtmPortSigVersion_Type.__name__ = "Integer32"
_AtmPortSigVersion_Object = MibTableColumn
atmPortSigVersion = _AtmPortSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 14),
    _AtmPortSigVersion_Type()
)
atmPortSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortSigVersion.setStatus("mandatory")


class _AtmPortSigIlmi_Type(Integer32):
    """Custom type atmPortSigIlmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AtmPortSigIlmi_Type.__name__ = "Integer32"
_AtmPortSigIlmi_Object = MibTableColumn
atmPortSigIlmi = _AtmPortSigIlmi_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 15),
    _AtmPortSigIlmi_Type()
)
atmPortSigIlmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortSigIlmi.setStatus("mandatory")


class _AtmPortAdminFrameMode_Type(Integer32):
    """Custom type atmPortAdminFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("sdh", 2),
          ("sonet", 1))
    )


_AtmPortAdminFrameMode_Type.__name__ = "Integer32"
_AtmPortAdminFrameMode_Object = MibTableColumn
atmPortAdminFrameMode = _AtmPortAdminFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 16),
    _AtmPortAdminFrameMode_Type()
)
atmPortAdminFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAdminFrameMode.setStatus("mandatory")


class _AtmPortSscopStatus_Type(Integer32):
    """Custom type atmPortSscopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_AtmPortSscopStatus_Type.__name__ = "Integer32"
_AtmPortSscopStatus_Object = MibTableColumn
atmPortSscopStatus = _AtmPortSscopStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 17),
    _AtmPortSscopStatus_Type()
)
atmPortSscopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSscopStatus.setStatus("mandatory")


class _AtmPortStatusEnquiryEnable_Type(EnableIndicator):
    """Custom type atmPortStatusEnquiryEnable based on EnableIndicator"""


_AtmPortStatusEnquiryEnable_Object = MibTableColumn
atmPortStatusEnquiryEnable = _AtmPortStatusEnquiryEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 18),
    _AtmPortStatusEnquiryEnable_Type()
)
atmPortStatusEnquiryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortStatusEnquiryEnable.setStatus("mandatory")


class _AtmPortTimerT309_Type(Integer32):
    """Custom type atmPortTimerT309 based on Integer32"""
    defaultValue = 10


_AtmPortTimerT309_Object = MibTableColumn
atmPortTimerT309 = _AtmPortTimerT309_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 19),
    _AtmPortTimerT309_Type()
)
atmPortTimerT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortTimerT309.setStatus("mandatory")


class _AtmPortTrafficShapingEnable_Type(Integer32):
    """Custom type atmPortTrafficShapingEnable based on Integer32"""
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


_AtmPortTrafficShapingEnable_Type.__name__ = "Integer32"
_AtmPortTrafficShapingEnable_Object = MibTableColumn
atmPortTrafficShapingEnable = _AtmPortTrafficShapingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 20),
    _AtmPortTrafficShapingEnable_Type()
)
atmPortTrafficShapingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortTrafficShapingEnable.setStatus("mandatory")
_AtmSysConfig_ObjectIdentity = ObjectIdentity
atmSysConfig = _AtmSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 4)
)


class _AtmSysSigEnable_Type(Integer32):
    """Custom type atmSysSigEnable based on Integer32"""
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


_AtmSysSigEnable_Type.__name__ = "Integer32"
_AtmSysSigEnable_Object = MibScalar
atmSysSigEnable = _AtmSysSigEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 4, 1),
    _AtmSysSigEnable_Type()
)
atmSysSigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSysSigEnable.setStatus("mandatory")
_AtmPortLogConfig_ObjectIdentity = ObjectIdentity
atmPortLogConfig = _AtmPortLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5)
)


class _AtmMaxPortLogConfig_Type(Integer32):
    """Custom type atmMaxPortLogConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmMaxPortLogConfig_Type.__name__ = "Integer32"
_AtmMaxPortLogConfig_Object = MibScalar
atmMaxPortLogConfig = _AtmMaxPortLogConfig_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 1),
    _AtmMaxPortLogConfig_Type()
)
atmMaxPortLogConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMaxPortLogConfig.setStatus("mandatory")


class _AtmCurPortLogConfig_Type(Integer32):
    """Custom type atmCurPortLogConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmCurPortLogConfig_Type.__name__ = "Integer32"
_AtmCurPortLogConfig_Object = MibScalar
atmCurPortLogConfig = _AtmCurPortLogConfig_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 2),
    _AtmCurPortLogConfig_Type()
)
atmCurPortLogConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurPortLogConfig.setStatus("mandatory")
_AtmPortLogConfigTable_Object = MibTable
atmPortLogConfigTable = _AtmPortLogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    atmPortLogConfigTable.setStatus("mandatory")
_AtmPortLogConfigEntry_Object = MibTableRow
atmPortLogConfigEntry = _AtmPortLogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1)
)
atmPortLogConfigEntry.setIndexNames(
    (0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigCardIndex"),
    (0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigPortIndex"),
    (0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigVPI"),
)
if mibBuilder.loadTexts:
    atmPortLogConfigEntry.setStatus("mandatory")


class _AtmPortLogConfigCardIndex_Type(Integer32):
    """Custom type atmPortLogConfigCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtmPortLogConfigCardIndex_Type.__name__ = "Integer32"
_AtmPortLogConfigCardIndex_Object = MibTableColumn
atmPortLogConfigCardIndex = _AtmPortLogConfigCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 1),
    _AtmPortLogConfigCardIndex_Type()
)
atmPortLogConfigCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLogConfigCardIndex.setStatus("mandatory")


class _AtmPortLogConfigPortIndex_Type(Integer32):
    """Custom type atmPortLogConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_AtmPortLogConfigPortIndex_Type.__name__ = "Integer32"
_AtmPortLogConfigPortIndex_Object = MibTableColumn
atmPortLogConfigPortIndex = _AtmPortLogConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 2),
    _AtmPortLogConfigPortIndex_Type()
)
atmPortLogConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLogConfigPortIndex.setStatus("mandatory")


class _AtmPortLogConfigVPI_Type(Integer32):
    """Custom type atmPortLogConfigVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmPortLogConfigVPI_Type.__name__ = "Integer32"
_AtmPortLogConfigVPI_Object = MibTableColumn
atmPortLogConfigVPI = _AtmPortLogConfigVPI_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 3),
    _AtmPortLogConfigVPI_Type()
)
atmPortLogConfigVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLogConfigVPI.setStatus("mandatory")


class _AtmPortLogConfigStatus_Type(Integer32):
    """Custom type atmPortLogConfigStatus based on Integer32"""
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
        *(("add", 3),
          ("modify", 4),
          ("other", 1),
          ("remove", 5),
          ("up", 2))
    )


_AtmPortLogConfigStatus_Type.__name__ = "Integer32"
_AtmPortLogConfigStatus_Object = MibTableColumn
atmPortLogConfigStatus = _AtmPortLogConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 4),
    _AtmPortLogConfigStatus_Type()
)
atmPortLogConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigStatus.setStatus("mandatory")


class _AtmPortLogConfigSigEntityType_Type(Integer32):
    """Custom type atmPortLogConfigSigEntityType based on Integer32"""
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
        *(("iisp", 3),
          ("noSig", 1),
          ("pnni", 4),
          ("uni", 2))
    )


_AtmPortLogConfigSigEntityType_Type.__name__ = "Integer32"
_AtmPortLogConfigSigEntityType_Object = MibTableColumn
atmPortLogConfigSigEntityType = _AtmPortLogConfigSigEntityType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 5),
    _AtmPortLogConfigSigEntityType_Type()
)
atmPortLogConfigSigEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigSigEntityType.setStatus("mandatory")


class _AtmPortLogConfigSigEntityRole_Type(Integer32):
    """Custom type atmPortLogConfigSigEntityRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netw", 3),
          ("other", 1),
          ("user", 2))
    )


_AtmPortLogConfigSigEntityRole_Type.__name__ = "Integer32"
_AtmPortLogConfigSigEntityRole_Object = MibTableColumn
atmPortLogConfigSigEntityRole = _AtmPortLogConfigSigEntityRole_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 6),
    _AtmPortLogConfigSigEntityRole_Type()
)
atmPortLogConfigSigEntityRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigSigEntityRole.setStatus("mandatory")


class _AtmPortLogConfigSigVersion_Type(Integer32):
    """Custom type atmPortLogConfigSigVersion based on Integer32"""
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
        *(("auto", 2),
          ("other", 1),
          ("pnni10", 5),
          ("uni30", 3),
          ("uni31", 4))
    )


_AtmPortLogConfigSigVersion_Type.__name__ = "Integer32"
_AtmPortLogConfigSigVersion_Object = MibTableColumn
atmPortLogConfigSigVersion = _AtmPortLogConfigSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 7),
    _AtmPortLogConfigSigVersion_Type()
)
atmPortLogConfigSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigSigVersion.setStatus("mandatory")


class _AtmPortLogConfigSigIlmi_Type(Integer32):
    """Custom type atmPortLogConfigSigIlmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AtmPortLogConfigSigIlmi_Type.__name__ = "Integer32"
_AtmPortLogConfigSigIlmi_Object = MibTableColumn
atmPortLogConfigSigIlmi = _AtmPortLogConfigSigIlmi_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 8),
    _AtmPortLogConfigSigIlmi_Type()
)
atmPortLogConfigSigIlmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigSigIlmi.setStatus("mandatory")


class _AtmPortLogConfigAdmWeightCbr_Type(Integer32):
    """Custom type atmPortLogConfigAdmWeightCbr based on Integer32"""
    defaultValue = 5040


_AtmPortLogConfigAdmWeightCbr_Object = MibTableColumn
atmPortLogConfigAdmWeightCbr = _AtmPortLogConfigAdmWeightCbr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 9),
    _AtmPortLogConfigAdmWeightCbr_Type()
)
atmPortLogConfigAdmWeightCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigAdmWeightCbr.setStatus("mandatory")


class _AtmPortLogConfigAdmWeightUbr_Type(Integer32):
    """Custom type atmPortLogConfigAdmWeightUbr based on Integer32"""
    defaultValue = 5040


_AtmPortLogConfigAdmWeightUbr_Object = MibTableColumn
atmPortLogConfigAdmWeightUbr = _AtmPortLogConfigAdmWeightUbr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 10),
    _AtmPortLogConfigAdmWeightUbr_Type()
)
atmPortLogConfigAdmWeightUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigAdmWeightUbr.setStatus("mandatory")


class _AtmPortLogConfigStatusEnquiryEnable_Type(EnableIndicator):
    """Custom type atmPortLogConfigStatusEnquiryEnable based on EnableIndicator"""


_AtmPortLogConfigStatusEnquiryEnable_Object = MibTableColumn
atmPortLogConfigStatusEnquiryEnable = _AtmPortLogConfigStatusEnquiryEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 11),
    _AtmPortLogConfigStatusEnquiryEnable_Type()
)
atmPortLogConfigStatusEnquiryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigStatusEnquiryEnable.setStatus("mandatory")


class _AtmPortLogConfigTimerT309_Type(Integer32):
    """Custom type atmPortLogConfigTimerT309 based on Integer32"""
    defaultValue = 10


_AtmPortLogConfigTimerT309_Object = MibTableColumn
atmPortLogConfigTimerT309 = _AtmPortLogConfigTimerT309_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 12),
    _AtmPortLogConfigTimerT309_Type()
)
atmPortLogConfigTimerT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLogConfigTimerT309.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-ATMCFG-MIB",
    **{"atmElanConfig": atmElanConfig,
       "atmElanConfigTable": atmElanConfigTable,
       "atmElanConfigEntry": atmElanConfigEntry,
       "atmElanIndex": atmElanIndex,
       "atmElanType": atmElanType,
       "atmElanEnable": atmElanEnable,
       "atmElanAllCkts": atmElanAllCkts,
       "atmElanVirtualCard": atmElanVirtualCard,
       "atmElanVirtualPort": atmElanVirtualPort,
       "atmElanVirtualSegmentId": atmElanVirtualSegmentId,
       "atmElanStatus": atmElanStatus,
       "atmElanVirtualSegmentType": atmElanVirtualSegmentType,
       "atmElanBridgeGroupId": atmElanBridgeGroupId,
       "atmElanMaxUnknownFrameCount": atmElanMaxUnknownFrameCount,
       "atmElanMaxUnknownFrameTime": atmElanMaxUnknownFrameTime,
       "atmElanVcBridgingEnable": atmElanVcBridgingEnable,
       "atmCktTable": atmCktTable,
       "atmPktCktTable": atmPktCktTable,
       "atmPktCktEntry": atmPktCktEntry,
       "atmPktCktIndex": atmPktCktIndex,
       "atmPktCktPriority": atmPktCktPriority,
       "atmPktCktEnable": atmPktCktEnable,
       "atmPktCktType": atmPktCktType,
       "atmPktCktCost": atmPktCktCost,
       "atmPktCktElanIndex": atmPktCktElanIndex,
       "atmPktCktCardPort": atmPktCktCardPort,
       "atmPktCktVpi": atmPktCktVpi,
       "atmPktCktVci": atmPktCktVci,
       "atmPktCktStatus": atmPktCktStatus,
       "atmPktCktCardPort2": atmPktCktCardPort2,
       "atmCellCktTable": atmCellCktTable,
       "atmCellCktEntry": atmCellCktEntry,
       "atmCellCktIndex": atmCellCktIndex,
       "atmCellCktPriority": atmCellCktPriority,
       "atmCellCktEnable": atmCellCktEnable,
       "atmCellCktType": atmCellCktType,
       "atmCellCktNumEndpt": atmCellCktNumEndpt,
       "atmCellCktEndptList": atmCellCktEndptList,
       "atmCellCktStatus": atmCellCktStatus,
       "atmPortConfig": atmPortConfig,
       "atmPortConfigTable": atmPortConfigTable,
       "atmPortConfigEntry": atmPortConfigEntry,
       "atmPortCardIndex": atmPortCardIndex,
       "atmPortPortIndex": atmPortPortIndex,
       "atmPortEnable": atmPortEnable,
       "atmPortLoopTimingEnable": atmPortLoopTimingEnable,
       "atmPortHecCosetEnable": atmPortHecCosetEnable,
       "atmPortHecCorrectionEnable": atmPortHecCorrectionEnable,
       "atmPortHardwareFrameMode": atmPortHardwareFrameMode,
       "atmPortLocalLoopEnable": atmPortLocalLoopEnable,
       "atmPortRemoteLoopEnable": atmPortRemoteLoopEnable,
       "atmPortForceHecErrorEnable": atmPortForceHecErrorEnable,
       "atmPortScramblingEnable": atmPortScramblingEnable,
       "atmPortSigEntityType": atmPortSigEntityType,
       "atmPortSigEntityRole": atmPortSigEntityRole,
       "atmPortSigVersion": atmPortSigVersion,
       "atmPortSigIlmi": atmPortSigIlmi,
       "atmPortAdminFrameMode": atmPortAdminFrameMode,
       "atmPortSscopStatus": atmPortSscopStatus,
       "atmPortStatusEnquiryEnable": atmPortStatusEnquiryEnable,
       "atmPortTimerT309": atmPortTimerT309,
       "atmPortTrafficShapingEnable": atmPortTrafficShapingEnable,
       "atmSysConfig": atmSysConfig,
       "atmSysSigEnable": atmSysSigEnable,
       "atmPortLogConfig": atmPortLogConfig,
       "atmMaxPortLogConfig": atmMaxPortLogConfig,
       "atmCurPortLogConfig": atmCurPortLogConfig,
       "atmPortLogConfigTable": atmPortLogConfigTable,
       "atmPortLogConfigEntry": atmPortLogConfigEntry,
       "atmPortLogConfigCardIndex": atmPortLogConfigCardIndex,
       "atmPortLogConfigPortIndex": atmPortLogConfigPortIndex,
       "atmPortLogConfigVPI": atmPortLogConfigVPI,
       "atmPortLogConfigStatus": atmPortLogConfigStatus,
       "atmPortLogConfigSigEntityType": atmPortLogConfigSigEntityType,
       "atmPortLogConfigSigEntityRole": atmPortLogConfigSigEntityRole,
       "atmPortLogConfigSigVersion": atmPortLogConfigSigVersion,
       "atmPortLogConfigSigIlmi": atmPortLogConfigSigIlmi,
       "atmPortLogConfigAdmWeightCbr": atmPortLogConfigAdmWeightCbr,
       "atmPortLogConfigAdmWeightUbr": atmPortLogConfigAdmWeightUbr,
       "atmPortLogConfigStatusEnquiryEnable": atmPortLogConfigStatusEnquiryEnable,
       "atmPortLogConfigTimerT309": atmPortLogConfigTimerT309}
)
