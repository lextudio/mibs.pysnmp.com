# SNMP MIB module (UX25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UX25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:13 2024
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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ux25_ObjectIdentity = ObjectIdentity
ux25 = _Ux25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 10)
)
_Ux25AdmnChannelTable_Object = MibTable
ux25AdmnChannelTable = _Ux25AdmnChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ux25AdmnChannelTable.setStatus("mandatory")
_Ux25AdmnChannelEntry_Object = MibTableRow
ux25AdmnChannelEntry = _Ux25AdmnChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1)
)
ux25AdmnChannelEntry.setIndexNames(
    (0, "UX25-MIB", "ux25AdmnChanneIndex"),
)
if mibBuilder.loadTexts:
    ux25AdmnChannelEntry.setStatus("mandatory")
_Ux25AdmnChanneIndex_Type = Integer32
_Ux25AdmnChanneIndex_Object = MibTableColumn
ux25AdmnChanneIndex = _Ux25AdmnChanneIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 1),
    _Ux25AdmnChanneIndex_Type()
)
ux25AdmnChanneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25AdmnChanneIndex.setStatus("mandatory")


class _Ux25AdmnNetMode_Type(Integer32):
    """Custom type ux25AdmnNetMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("accunet", 15),
          ("austpac", 6),
          ("datanet", 18),
          ("datapac", 7),
          ("datapak", 17),
          ("datexP", 12),
          ("dcs", 19),
          ("ddn", 8),
          ("ddxP", 13),
          ("fDatapac", 21),
          ("finpac", 22),
          ("itapac", 16),
          ("luxpac", 24),
          ("pacnet", 23),
          ("pss", 5),
          ("telenet", 9),
          ("telepac", 20),
          ("transpac", 10),
          ("tymnet", 11),
          ("venusP", 14),
          ("x2580", 4),
          ("x2584", 3),
          ("x2588", 2),
          ("x25Llc", 1))
    )


_Ux25AdmnNetMode_Type.__name__ = "Integer32"
_Ux25AdmnNetMode_Object = MibTableColumn
ux25AdmnNetMode = _Ux25AdmnNetMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 2),
    _Ux25AdmnNetMode_Type()
)
ux25AdmnNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnNetMode.setStatus("mandatory")


class _Ux25AdmnProtocolVersion_Type(Integer32):
    """Custom type ux25AdmnProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x25ver80", 1),
          ("x25ver84", 2),
          ("x25ver88", 3))
    )


_Ux25AdmnProtocolVersion_Type.__name__ = "Integer32"
_Ux25AdmnProtocolVersion_Object = MibTableColumn
ux25AdmnProtocolVersion = _Ux25AdmnProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 3),
    _Ux25AdmnProtocolVersion_Type()
)
ux25AdmnProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnProtocolVersion.setStatus("mandatory")


class _Ux25AdmnInterfaceMode_Type(Integer32):
    """Custom type ux25AdmnInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dceMode", 1),
          ("dteMode", 2),
          ("dxeMode", 3))
    )


_Ux25AdmnInterfaceMode_Type.__name__ = "Integer32"
_Ux25AdmnInterfaceMode_Object = MibTableColumn
ux25AdmnInterfaceMode = _Ux25AdmnInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 4),
    _Ux25AdmnInterfaceMode_Type()
)
ux25AdmnInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnInterfaceMode.setStatus("mandatory")


class _Ux25AdmnLowestPVCVal_Type(Integer32):
    """Custom type ux25AdmnLowestPVCVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnLowestPVCVal_Type.__name__ = "Integer32"
_Ux25AdmnLowestPVCVal_Object = MibTableColumn
ux25AdmnLowestPVCVal = _Ux25AdmnLowestPVCVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 5),
    _Ux25AdmnLowestPVCVal_Type()
)
ux25AdmnLowestPVCVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLowestPVCVal.setStatus("mandatory")


class _Ux25AdmnHighestPVCVal_Type(Integer32):
    """Custom type ux25AdmnHighestPVCVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnHighestPVCVal_Type.__name__ = "Integer32"
_Ux25AdmnHighestPVCVal_Object = MibTableColumn
ux25AdmnHighestPVCVal = _Ux25AdmnHighestPVCVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 6),
    _Ux25AdmnHighestPVCVal_Type()
)
ux25AdmnHighestPVCVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnHighestPVCVal.setStatus("mandatory")


class _Ux25AdmnChannelLIC_Type(Integer32):
    """Custom type ux25AdmnChannelLIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelLIC_Type.__name__ = "Integer32"
_Ux25AdmnChannelLIC_Object = MibTableColumn
ux25AdmnChannelLIC = _Ux25AdmnChannelLIC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 7),
    _Ux25AdmnChannelLIC_Type()
)
ux25AdmnChannelLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelLIC.setStatus("mandatory")


class _Ux25AdmnChannelHIC_Type(Integer32):
    """Custom type ux25AdmnChannelHIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelHIC_Type.__name__ = "Integer32"
_Ux25AdmnChannelHIC_Object = MibTableColumn
ux25AdmnChannelHIC = _Ux25AdmnChannelHIC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 8),
    _Ux25AdmnChannelHIC_Type()
)
ux25AdmnChannelHIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelHIC.setStatus("mandatory")


class _Ux25AdmnChannelLTC_Type(Integer32):
    """Custom type ux25AdmnChannelLTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelLTC_Type.__name__ = "Integer32"
_Ux25AdmnChannelLTC_Object = MibTableColumn
ux25AdmnChannelLTC = _Ux25AdmnChannelLTC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 9),
    _Ux25AdmnChannelLTC_Type()
)
ux25AdmnChannelLTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelLTC.setStatus("mandatory")


class _Ux25AdmnChannelHTC_Type(Integer32):
    """Custom type ux25AdmnChannelHTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelHTC_Type.__name__ = "Integer32"
_Ux25AdmnChannelHTC_Object = MibTableColumn
ux25AdmnChannelHTC = _Ux25AdmnChannelHTC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 10),
    _Ux25AdmnChannelHTC_Type()
)
ux25AdmnChannelHTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelHTC.setStatus("mandatory")


class _Ux25AdmnChannelLOC_Type(Integer32):
    """Custom type ux25AdmnChannelLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelLOC_Type.__name__ = "Integer32"
_Ux25AdmnChannelLOC_Object = MibTableColumn
ux25AdmnChannelLOC = _Ux25AdmnChannelLOC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 11),
    _Ux25AdmnChannelLOC_Type()
)
ux25AdmnChannelLOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelLOC.setStatus("mandatory")


class _Ux25AdmnChannelHOC_Type(Integer32):
    """Custom type ux25AdmnChannelHOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25AdmnChannelHOC_Type.__name__ = "Integer32"
_Ux25AdmnChannelHOC_Object = MibTableColumn
ux25AdmnChannelHOC = _Ux25AdmnChannelHOC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 1, 1, 12),
    _Ux25AdmnChannelHOC_Type()
)
ux25AdmnChannelHOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnChannelHOC.setStatus("mandatory")
_Ux25AdmnClassTable_Object = MibTable
ux25AdmnClassTable = _Ux25AdmnClassTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ux25AdmnClassTable.setStatus("mandatory")
_Ux25AdmnClassEntry_Object = MibTableRow
ux25AdmnClassEntry = _Ux25AdmnClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1)
)
ux25AdmnClassEntry.setIndexNames(
    (0, "UX25-MIB", "ux25AdmnClassIndex"),
)
if mibBuilder.loadTexts:
    ux25AdmnClassEntry.setStatus("mandatory")
_Ux25AdmnClassIndex_Type = Integer32
_Ux25AdmnClassIndex_Object = MibTableColumn
ux25AdmnClassIndex = _Ux25AdmnClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 1),
    _Ux25AdmnClassIndex_Type()
)
ux25AdmnClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25AdmnClassIndex.setStatus("mandatory")


class _Ux25AdmnLocMaxThruPutClass_Type(Integer32):
    """Custom type ux25AdmnLocMaxThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnLocMaxThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnLocMaxThruPutClass_Object = MibTableColumn
ux25AdmnLocMaxThruPutClass = _Ux25AdmnLocMaxThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 2),
    _Ux25AdmnLocMaxThruPutClass_Type()
)
ux25AdmnLocMaxThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocMaxThruPutClass.setStatus("mandatory")


class _Ux25AdmnRemMaxThruPutClass_Type(Integer32):
    """Custom type ux25AdmnRemMaxThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnRemMaxThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnRemMaxThruPutClass_Object = MibTableColumn
ux25AdmnRemMaxThruPutClass = _Ux25AdmnRemMaxThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 3),
    _Ux25AdmnRemMaxThruPutClass_Type()
)
ux25AdmnRemMaxThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemMaxThruPutClass.setStatus("mandatory")


class _Ux25AdmnLocDefThruPutClass_Type(Integer32):
    """Custom type ux25AdmnLocDefThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnLocDefThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnLocDefThruPutClass_Object = MibTableColumn
ux25AdmnLocDefThruPutClass = _Ux25AdmnLocDefThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 4),
    _Ux25AdmnLocDefThruPutClass_Type()
)
ux25AdmnLocDefThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocDefThruPutClass.setStatus("mandatory")


class _Ux25AdmnRemDefThruPutClass_Type(Integer32):
    """Custom type ux25AdmnRemDefThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnRemDefThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnRemDefThruPutClass_Object = MibTableColumn
ux25AdmnRemDefThruPutClass = _Ux25AdmnRemDefThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 5),
    _Ux25AdmnRemDefThruPutClass_Type()
)
ux25AdmnRemDefThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemDefThruPutClass.setStatus("mandatory")


class _Ux25AdmnLocMinThruPutClass_Type(Integer32):
    """Custom type ux25AdmnLocMinThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnLocMinThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnLocMinThruPutClass_Object = MibTableColumn
ux25AdmnLocMinThruPutClass = _Ux25AdmnLocMinThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 6),
    _Ux25AdmnLocMinThruPutClass_Type()
)
ux25AdmnLocMinThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocMinThruPutClass.setStatus("mandatory")


class _Ux25AdmnRemMinThruPutClass_Type(Integer32):
    """Custom type ux25AdmnRemMinThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25AdmnRemMinThruPutClass_Type.__name__ = "Integer32"
_Ux25AdmnRemMinThruPutClass_Object = MibTableColumn
ux25AdmnRemMinThruPutClass = _Ux25AdmnRemMinThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 7),
    _Ux25AdmnRemMinThruPutClass_Type()
)
ux25AdmnRemMinThruPutClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemMinThruPutClass.setStatus("mandatory")


class _Ux25AdmnThclassNegToDef_Type(Integer32):
    """Custom type ux25AdmnThclassNegToDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnThclassNegToDef_Type.__name__ = "Integer32"
_Ux25AdmnThclassNegToDef_Object = MibTableColumn
ux25AdmnThclassNegToDef = _Ux25AdmnThclassNegToDef_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 8),
    _Ux25AdmnThclassNegToDef_Type()
)
ux25AdmnThclassNegToDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnThclassNegToDef.setStatus("mandatory")


class _Ux25AdmnThclassType_Type(Integer32):
    """Custom type ux25AdmnThclassType based on Integer32"""
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
        *(("bothNibbles", 4),
          ("highNibble", 3),
          ("loNibble", 2),
          ("noTcType", 1))
    )


_Ux25AdmnThclassType_Type.__name__ = "Integer32"
_Ux25AdmnThclassType_Object = MibTableColumn
ux25AdmnThclassType = _Ux25AdmnThclassType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 9),
    _Ux25AdmnThclassType_Type()
)
ux25AdmnThclassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnThclassType.setStatus("mandatory")


class _Ux25AdmnThclassWinMap_Type(DisplayString):
    """Custom type ux25AdmnThclassWinMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 63),
    )


_Ux25AdmnThclassWinMap_Type.__name__ = "DisplayString"
_Ux25AdmnThclassWinMap_Object = MibTableColumn
ux25AdmnThclassWinMap = _Ux25AdmnThclassWinMap_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 10),
    _Ux25AdmnThclassWinMap_Type()
)
ux25AdmnThclassWinMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnThclassWinMap.setStatus("mandatory")


class _Ux25AdmnThclassPackMap_Type(DisplayString):
    """Custom type ux25AdmnThclassPackMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 47),
    )


_Ux25AdmnThclassPackMap_Type.__name__ = "DisplayString"
_Ux25AdmnThclassPackMap_Object = MibTableColumn
ux25AdmnThclassPackMap = _Ux25AdmnThclassPackMap_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 2, 1, 11),
    _Ux25AdmnThclassPackMap_Type()
)
ux25AdmnThclassPackMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnThclassPackMap.setStatus("mandatory")
_Ux25AdmnPacketTable_Object = MibTable
ux25AdmnPacketTable = _Ux25AdmnPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ux25AdmnPacketTable.setStatus("mandatory")
_Ux25AdmnPacketEntry_Object = MibTableRow
ux25AdmnPacketEntry = _Ux25AdmnPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1)
)
ux25AdmnPacketEntry.setIndexNames(
    (0, "UX25-MIB", "ux25AdmnPacketIndex"),
)
if mibBuilder.loadTexts:
    ux25AdmnPacketEntry.setStatus("mandatory")
_Ux25AdmnPacketIndex_Type = Integer32
_Ux25AdmnPacketIndex_Object = MibTableColumn
ux25AdmnPacketIndex = _Ux25AdmnPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 1),
    _Ux25AdmnPacketIndex_Type()
)
ux25AdmnPacketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25AdmnPacketIndex.setStatus("mandatory")


class _Ux25AdmnPktSequencing_Type(Integer32):
    """Custom type ux25AdmnPktSequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("pktSeq128", 32),
          ("pktSeq8", 16))
    )


_Ux25AdmnPktSequencing_Type.__name__ = "Integer32"
_Ux25AdmnPktSequencing_Object = MibTableColumn
ux25AdmnPktSequencing = _Ux25AdmnPktSequencing_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 2),
    _Ux25AdmnPktSequencing_Type()
)
ux25AdmnPktSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnPktSequencing.setStatus("mandatory")


class _Ux25AdmnLocMaxPktSize_Type(Integer32):
    """Custom type ux25AdmnLocMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("maxPktSz128", 7),
          ("maxPktSz256", 8),
          ("maxPktSz512", 9))
    )


_Ux25AdmnLocMaxPktSize_Type.__name__ = "Integer32"
_Ux25AdmnLocMaxPktSize_Object = MibTableColumn
ux25AdmnLocMaxPktSize = _Ux25AdmnLocMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 3),
    _Ux25AdmnLocMaxPktSize_Type()
)
ux25AdmnLocMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocMaxPktSize.setStatus("mandatory")


class _Ux25AdmnRemMaxPktSize_Type(Integer32):
    """Custom type ux25AdmnRemMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("maxPktSz128", 7),
          ("maxPktSz256", 8),
          ("maxPktSz512", 9))
    )


_Ux25AdmnRemMaxPktSize_Type.__name__ = "Integer32"
_Ux25AdmnRemMaxPktSize_Object = MibTableColumn
ux25AdmnRemMaxPktSize = _Ux25AdmnRemMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 4),
    _Ux25AdmnRemMaxPktSize_Type()
)
ux25AdmnRemMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemMaxPktSize.setStatus("mandatory")


class _Ux25AdmnLocDefPktSize_Type(Integer32):
    """Custom type ux25AdmnLocDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("defPktSz128", 7),
          ("defPktSz16", 4),
          ("defPktSz256", 8),
          ("defPktSz32", 5),
          ("defPktSz512", 9),
          ("defPktSz64", 6))
    )


_Ux25AdmnLocDefPktSize_Type.__name__ = "Integer32"
_Ux25AdmnLocDefPktSize_Object = MibTableColumn
ux25AdmnLocDefPktSize = _Ux25AdmnLocDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 5),
    _Ux25AdmnLocDefPktSize_Type()
)
ux25AdmnLocDefPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocDefPktSize.setStatus("mandatory")


class _Ux25AdmnRemDefPktSize_Type(Integer32):
    """Custom type ux25AdmnRemDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("defPktSz128", 7),
          ("defPktSz16", 4),
          ("defPktSz256", 8),
          ("defPktSz32", 5),
          ("defPktSz512", 9),
          ("defPktSz64", 6))
    )


_Ux25AdmnRemDefPktSize_Type.__name__ = "Integer32"
_Ux25AdmnRemDefPktSize_Object = MibTableColumn
ux25AdmnRemDefPktSize = _Ux25AdmnRemDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 6),
    _Ux25AdmnRemDefPktSize_Type()
)
ux25AdmnRemDefPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemDefPktSize.setStatus("mandatory")


class _Ux25AdmnLocMaxWinSize_Type(Integer32):
    """Custom type ux25AdmnLocMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Ux25AdmnLocMaxWinSize_Type.__name__ = "Integer32"
_Ux25AdmnLocMaxWinSize_Object = MibTableColumn
ux25AdmnLocMaxWinSize = _Ux25AdmnLocMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 7),
    _Ux25AdmnLocMaxWinSize_Type()
)
ux25AdmnLocMaxWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocMaxWinSize.setStatus("mandatory")


class _Ux25AdmnRemMaxWinSize_Type(Integer32):
    """Custom type ux25AdmnRemMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Ux25AdmnRemMaxWinSize_Type.__name__ = "Integer32"
_Ux25AdmnRemMaxWinSize_Object = MibTableColumn
ux25AdmnRemMaxWinSize = _Ux25AdmnRemMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 8),
    _Ux25AdmnRemMaxWinSize_Type()
)
ux25AdmnRemMaxWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemMaxWinSize.setStatus("mandatory")


class _Ux25AdmnLocDefWinSize_Type(Integer32):
    """Custom type ux25AdmnLocDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Ux25AdmnLocDefWinSize_Type.__name__ = "Integer32"
_Ux25AdmnLocDefWinSize_Object = MibTableColumn
ux25AdmnLocDefWinSize = _Ux25AdmnLocDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 9),
    _Ux25AdmnLocDefWinSize_Type()
)
ux25AdmnLocDefWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocDefWinSize.setStatus("mandatory")


class _Ux25AdmnRemDefWinSize_Type(Integer32):
    """Custom type ux25AdmnRemDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Ux25AdmnRemDefWinSize_Type.__name__ = "Integer32"
_Ux25AdmnRemDefWinSize_Object = MibTableColumn
ux25AdmnRemDefWinSize = _Ux25AdmnRemDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 10),
    _Ux25AdmnRemDefWinSize_Type()
)
ux25AdmnRemDefWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRemDefWinSize.setStatus("mandatory")


class _Ux25AdmnMaxNSDULimit_Type(Integer32):
    """Custom type ux25AdmnMaxNSDULimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnMaxNSDULimit_Type.__name__ = "Integer32"
_Ux25AdmnMaxNSDULimit_Object = MibTableColumn
ux25AdmnMaxNSDULimit = _Ux25AdmnMaxNSDULimit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 11),
    _Ux25AdmnMaxNSDULimit_Type()
)
ux25AdmnMaxNSDULimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnMaxNSDULimit.setStatus("mandatory")


class _Ux25AdmnAccNoDiagnostic_Type(Integer32):
    """Custom type ux25AdmnAccNoDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnAccNoDiagnostic_Type.__name__ = "Integer32"
_Ux25AdmnAccNoDiagnostic_Object = MibTableColumn
ux25AdmnAccNoDiagnostic = _Ux25AdmnAccNoDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 12),
    _Ux25AdmnAccNoDiagnostic_Type()
)
ux25AdmnAccNoDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnAccNoDiagnostic.setStatus("mandatory")


class _Ux25AdmnUseDiagnosticPacket_Type(Integer32):
    """Custom type ux25AdmnUseDiagnosticPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnUseDiagnosticPacket_Type.__name__ = "Integer32"
_Ux25AdmnUseDiagnosticPacket_Object = MibTableColumn
ux25AdmnUseDiagnosticPacket = _Ux25AdmnUseDiagnosticPacket_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 13),
    _Ux25AdmnUseDiagnosticPacket_Type()
)
ux25AdmnUseDiagnosticPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnUseDiagnosticPacket.setStatus("mandatory")


class _Ux25AdmnItutClearLen_Type(Integer32):
    """Custom type ux25AdmnItutClearLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnItutClearLen_Type.__name__ = "Integer32"
_Ux25AdmnItutClearLen_Object = MibTableColumn
ux25AdmnItutClearLen = _Ux25AdmnItutClearLen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 14),
    _Ux25AdmnItutClearLen_Type()
)
ux25AdmnItutClearLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnItutClearLen.setStatus("mandatory")


class _Ux25AdmnBarDiagnosticPacket_Type(Integer32):
    """Custom type ux25AdmnBarDiagnosticPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarDiagnosticPacket_Type.__name__ = "Integer32"
_Ux25AdmnBarDiagnosticPacket_Object = MibTableColumn
ux25AdmnBarDiagnosticPacket = _Ux25AdmnBarDiagnosticPacket_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 15),
    _Ux25AdmnBarDiagnosticPacket_Type()
)
ux25AdmnBarDiagnosticPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarDiagnosticPacket.setStatus("mandatory")


class _Ux25AdmnDiscNzDiagnostic_Type(Integer32):
    """Custom type ux25AdmnDiscNzDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnDiscNzDiagnostic_Type.__name__ = "Integer32"
_Ux25AdmnDiscNzDiagnostic_Object = MibTableColumn
ux25AdmnDiscNzDiagnostic = _Ux25AdmnDiscNzDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 16),
    _Ux25AdmnDiscNzDiagnostic_Type()
)
ux25AdmnDiscNzDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDiscNzDiagnostic.setStatus("mandatory")


class _Ux25AdmnAcceptHexAdd_Type(Integer32):
    """Custom type ux25AdmnAcceptHexAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnAcceptHexAdd_Type.__name__ = "Integer32"
_Ux25AdmnAcceptHexAdd_Object = MibTableColumn
ux25AdmnAcceptHexAdd = _Ux25AdmnAcceptHexAdd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 17),
    _Ux25AdmnAcceptHexAdd_Type()
)
ux25AdmnAcceptHexAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnAcceptHexAdd.setStatus("mandatory")


class _Ux25AdmnBarNonPrivilegeListen_Type(Integer32):
    """Custom type ux25AdmnBarNonPrivilegeListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarNonPrivilegeListen_Type.__name__ = "Integer32"
_Ux25AdmnBarNonPrivilegeListen_Object = MibTableColumn
ux25AdmnBarNonPrivilegeListen = _Ux25AdmnBarNonPrivilegeListen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 18),
    _Ux25AdmnBarNonPrivilegeListen_Type()
)
ux25AdmnBarNonPrivilegeListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarNonPrivilegeListen.setStatus("mandatory")


class _Ux25AdmnIntlAddrRecognition_Type(Integer32):
    """Custom type ux25AdmnIntlAddrRecognition based on Integer32"""
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
        *(("examineDnic", 2),
          ("notDistinguished", 1),
          ("prefix0", 4),
          ("prefix1", 3))
    )


_Ux25AdmnIntlAddrRecognition_Type.__name__ = "Integer32"
_Ux25AdmnIntlAddrRecognition_Object = MibTableColumn
ux25AdmnIntlAddrRecognition = _Ux25AdmnIntlAddrRecognition_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 19),
    _Ux25AdmnIntlAddrRecognition_Type()
)
ux25AdmnIntlAddrRecognition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnIntlAddrRecognition.setStatus("mandatory")


class _Ux25AdmnDnic_Type(DisplayString):
    """Custom type ux25AdmnDnic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Ux25AdmnDnic_Type.__name__ = "DisplayString"
_Ux25AdmnDnic_Object = MibTableColumn
ux25AdmnDnic = _Ux25AdmnDnic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 20),
    _Ux25AdmnDnic_Type()
)
ux25AdmnDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDnic.setStatus("mandatory")


class _Ux25AdmnIntlPrioritized_Type(Integer32):
    """Custom type ux25AdmnIntlPrioritized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnIntlPrioritized_Type.__name__ = "Integer32"
_Ux25AdmnIntlPrioritized_Object = MibTableColumn
ux25AdmnIntlPrioritized = _Ux25AdmnIntlPrioritized_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 21),
    _Ux25AdmnIntlPrioritized_Type()
)
ux25AdmnIntlPrioritized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnIntlPrioritized.setStatus("mandatory")


class _Ux25AdmnPrtyEncodeCtrl_Type(Integer32):
    """Custom type ux25AdmnPrtyEncodeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("datapacPriority76", 2),
          ("datapacTraffic80", 3),
          ("x2588", 1))
    )


_Ux25AdmnPrtyEncodeCtrl_Type.__name__ = "Integer32"
_Ux25AdmnPrtyEncodeCtrl_Object = MibTableColumn
ux25AdmnPrtyEncodeCtrl = _Ux25AdmnPrtyEncodeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 22),
    _Ux25AdmnPrtyEncodeCtrl_Type()
)
ux25AdmnPrtyEncodeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnPrtyEncodeCtrl.setStatus("mandatory")


class _Ux25AdmnPrtyPktForcedVal_Type(Integer32):
    """Custom type ux25AdmnPrtyPktForcedVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("prioPktSz0", 1),
          ("prioPktSz10", 11),
          ("prioPktSz11", 12),
          ("prioPktSz12", 13),
          ("prioPktSz4", 5),
          ("prioPktSz5", 6),
          ("prioPktSz6", 7),
          ("prioPktSz7", 8),
          ("prioPktSz8", 9),
          ("prioPktSz9", 10))
    )


_Ux25AdmnPrtyPktForcedVal_Type.__name__ = "Integer32"
_Ux25AdmnPrtyPktForcedVal_Object = MibTableColumn
ux25AdmnPrtyPktForcedVal = _Ux25AdmnPrtyPktForcedVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 23),
    _Ux25AdmnPrtyPktForcedVal_Type()
)
ux25AdmnPrtyPktForcedVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnPrtyPktForcedVal.setStatus("mandatory")


class _Ux25AdmnSrcAddrCtrl_Type(Integer32):
    """Custom type ux25AdmnSrcAddrCtrl based on Integer32"""
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
        *(("forceLocal", 4),
          ("noSaCntrl", 1),
          ("omitDte", 2),
          ("useLocal", 3))
    )


_Ux25AdmnSrcAddrCtrl_Type.__name__ = "Integer32"
_Ux25AdmnSrcAddrCtrl_Object = MibTableColumn
ux25AdmnSrcAddrCtrl = _Ux25AdmnSrcAddrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 24),
    _Ux25AdmnSrcAddrCtrl_Type()
)
ux25AdmnSrcAddrCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSrcAddrCtrl.setStatus("mandatory")


class _Ux25AdmnDbitInAccept_Type(Integer32):
    """Custom type ux25AdmnDbitInAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25AdmnDbitInAccept_Type.__name__ = "Integer32"
_Ux25AdmnDbitInAccept_Object = MibTableColumn
ux25AdmnDbitInAccept = _Ux25AdmnDbitInAccept_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 25),
    _Ux25AdmnDbitInAccept_Type()
)
ux25AdmnDbitInAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDbitInAccept.setStatus("mandatory")


class _Ux25AdmnDbitOutAccept_Type(Integer32):
    """Custom type ux25AdmnDbitOutAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25AdmnDbitOutAccept_Type.__name__ = "Integer32"
_Ux25AdmnDbitOutAccept_Object = MibTableColumn
ux25AdmnDbitOutAccept = _Ux25AdmnDbitOutAccept_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 26),
    _Ux25AdmnDbitOutAccept_Type()
)
ux25AdmnDbitOutAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDbitOutAccept.setStatus("mandatory")


class _Ux25AdmnDbitInData_Type(Integer32):
    """Custom type ux25AdmnDbitInData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25AdmnDbitInData_Type.__name__ = "Integer32"
_Ux25AdmnDbitInData_Object = MibTableColumn
ux25AdmnDbitInData = _Ux25AdmnDbitInData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 27),
    _Ux25AdmnDbitInData_Type()
)
ux25AdmnDbitInData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDbitInData.setStatus("mandatory")


class _Ux25AdmnDbitOutData_Type(Integer32):
    """Custom type ux25AdmnDbitOutData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25AdmnDbitOutData_Type.__name__ = "Integer32"
_Ux25AdmnDbitOutData_Object = MibTableColumn
ux25AdmnDbitOutData = _Ux25AdmnDbitOutData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 3, 1, 28),
    _Ux25AdmnDbitOutData_Type()
)
ux25AdmnDbitOutData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnDbitOutData.setStatus("mandatory")
_Ux25AdmnSubscriberTable_Object = MibTable
ux25AdmnSubscriberTable = _Ux25AdmnSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4)
)
if mibBuilder.loadTexts:
    ux25AdmnSubscriberTable.setStatus("mandatory")
_Ux25AdmnSubscriberEntry_Object = MibTableRow
ux25AdmnSubscriberEntry = _Ux25AdmnSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1)
)
ux25AdmnSubscriberEntry.setIndexNames(
    (0, "UX25-MIB", "ux25AdmnSubscriberIndex"),
)
if mibBuilder.loadTexts:
    ux25AdmnSubscriberEntry.setStatus("mandatory")
_Ux25AdmnSubscriberIndex_Type = Integer32
_Ux25AdmnSubscriberIndex_Object = MibTableColumn
ux25AdmnSubscriberIndex = _Ux25AdmnSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 1),
    _Ux25AdmnSubscriberIndex_Type()
)
ux25AdmnSubscriberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25AdmnSubscriberIndex.setStatus("mandatory")


class _Ux25AdmnSubCugIaoa_Type(Integer32):
    """Custom type ux25AdmnSubCugIaoa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubCugIaoa_Type.__name__ = "Integer32"
_Ux25AdmnSubCugIaoa_Object = MibTableColumn
ux25AdmnSubCugIaoa = _Ux25AdmnSubCugIaoa_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 2),
    _Ux25AdmnSubCugIaoa_Type()
)
ux25AdmnSubCugIaoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubCugIaoa.setStatus("mandatory")


class _Ux25AdmnSubCugPref_Type(Integer32):
    """Custom type ux25AdmnSubCugPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubCugPref_Type.__name__ = "Integer32"
_Ux25AdmnSubCugPref_Object = MibTableColumn
ux25AdmnSubCugPref = _Ux25AdmnSubCugPref_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 3),
    _Ux25AdmnSubCugPref_Type()
)
ux25AdmnSubCugPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubCugPref.setStatus("mandatory")


class _Ux25AdmnSubCugoa_Type(Integer32):
    """Custom type ux25AdmnSubCugoa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubCugoa_Type.__name__ = "Integer32"
_Ux25AdmnSubCugoa_Object = MibTableColumn
ux25AdmnSubCugoa = _Ux25AdmnSubCugoa_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 4),
    _Ux25AdmnSubCugoa_Type()
)
ux25AdmnSubCugoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubCugoa.setStatus("mandatory")


class _Ux25AdmnSubCugia_Type(Integer32):
    """Custom type ux25AdmnSubCugia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubCugia_Type.__name__ = "Integer32"
_Ux25AdmnSubCugia_Object = MibTableColumn
ux25AdmnSubCugia = _Ux25AdmnSubCugia_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 5),
    _Ux25AdmnSubCugia_Type()
)
ux25AdmnSubCugia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubCugia.setStatus("mandatory")


class _Ux25AdmnCugFormat_Type(Integer32):
    """Custom type ux25AdmnCugFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("extended", 2))
    )


_Ux25AdmnCugFormat_Type.__name__ = "Integer32"
_Ux25AdmnCugFormat_Object = MibTableColumn
ux25AdmnCugFormat = _Ux25AdmnCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 6),
    _Ux25AdmnCugFormat_Type()
)
ux25AdmnCugFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnCugFormat.setStatus("mandatory")


class _Ux25AdmnBarInCug_Type(Integer32):
    """Custom type ux25AdmnBarInCug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarInCug_Type.__name__ = "Integer32"
_Ux25AdmnBarInCug_Object = MibTableColumn
ux25AdmnBarInCug = _Ux25AdmnBarInCug_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 7),
    _Ux25AdmnBarInCug_Type()
)
ux25AdmnBarInCug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarInCug.setStatus("mandatory")


class _Ux25AdmnSubExtended_Type(Integer32):
    """Custom type ux25AdmnSubExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubExtended_Type.__name__ = "Integer32"
_Ux25AdmnSubExtended_Object = MibTableColumn
ux25AdmnSubExtended = _Ux25AdmnSubExtended_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 8),
    _Ux25AdmnSubExtended_Type()
)
ux25AdmnSubExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubExtended.setStatus("mandatory")


class _Ux25AdmnBarExtended_Type(Integer32):
    """Custom type ux25AdmnBarExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarExtended_Type.__name__ = "Integer32"
_Ux25AdmnBarExtended_Object = MibTableColumn
ux25AdmnBarExtended = _Ux25AdmnBarExtended_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 9),
    _Ux25AdmnBarExtended_Type()
)
ux25AdmnBarExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarExtended.setStatus("mandatory")


class _Ux25AdmnSubFstSelNoRstrct_Type(Integer32):
    """Custom type ux25AdmnSubFstSelNoRstrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubFstSelNoRstrct_Type.__name__ = "Integer32"
_Ux25AdmnSubFstSelNoRstrct_Object = MibTableColumn
ux25AdmnSubFstSelNoRstrct = _Ux25AdmnSubFstSelNoRstrct_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 10),
    _Ux25AdmnSubFstSelNoRstrct_Type()
)
ux25AdmnSubFstSelNoRstrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubFstSelNoRstrct.setStatus("mandatory")


class _Ux25AdmnSubFstSelWthRstrct_Type(Integer32):
    """Custom type ux25AdmnSubFstSelWthRstrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubFstSelWthRstrct_Type.__name__ = "Integer32"
_Ux25AdmnSubFstSelWthRstrct_Object = MibTableColumn
ux25AdmnSubFstSelWthRstrct = _Ux25AdmnSubFstSelWthRstrct_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 11),
    _Ux25AdmnSubFstSelWthRstrct_Type()
)
ux25AdmnSubFstSelWthRstrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubFstSelWthRstrct.setStatus("mandatory")


class _Ux25AdmnAccptRvsChrgng_Type(Integer32):
    """Custom type ux25AdmnAccptRvsChrgng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnAccptRvsChrgng_Type.__name__ = "Integer32"
_Ux25AdmnAccptRvsChrgng_Object = MibTableColumn
ux25AdmnAccptRvsChrgng = _Ux25AdmnAccptRvsChrgng_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 12),
    _Ux25AdmnAccptRvsChrgng_Type()
)
ux25AdmnAccptRvsChrgng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnAccptRvsChrgng.setStatus("mandatory")


class _Ux25AdmnSubLocChargePrevent_Type(Integer32):
    """Custom type ux25AdmnSubLocChargePrevent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubLocChargePrevent_Type.__name__ = "Integer32"
_Ux25AdmnSubLocChargePrevent_Object = MibTableColumn
ux25AdmnSubLocChargePrevent = _Ux25AdmnSubLocChargePrevent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 13),
    _Ux25AdmnSubLocChargePrevent_Type()
)
ux25AdmnSubLocChargePrevent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubLocChargePrevent.setStatus("mandatory")


class _Ux25AdmnSubToaNpiFormat_Type(Integer32):
    """Custom type ux25AdmnSubToaNpiFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubToaNpiFormat_Type.__name__ = "Integer32"
_Ux25AdmnSubToaNpiFormat_Object = MibTableColumn
ux25AdmnSubToaNpiFormat = _Ux25AdmnSubToaNpiFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 14),
    _Ux25AdmnSubToaNpiFormat_Type()
)
ux25AdmnSubToaNpiFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubToaNpiFormat.setStatus("mandatory")


class _Ux25AdmnBarToaNpiFormat_Type(Integer32):
    """Custom type ux25AdmnBarToaNpiFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarToaNpiFormat_Type.__name__ = "Integer32"
_Ux25AdmnBarToaNpiFormat_Object = MibTableColumn
ux25AdmnBarToaNpiFormat = _Ux25AdmnBarToaNpiFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 15),
    _Ux25AdmnBarToaNpiFormat_Type()
)
ux25AdmnBarToaNpiFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarToaNpiFormat.setStatus("mandatory")


class _Ux25AdmnSubNuiOverride_Type(Integer32):
    """Custom type ux25AdmnSubNuiOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnSubNuiOverride_Type.__name__ = "Integer32"
_Ux25AdmnSubNuiOverride_Object = MibTableColumn
ux25AdmnSubNuiOverride = _Ux25AdmnSubNuiOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 16),
    _Ux25AdmnSubNuiOverride_Type()
)
ux25AdmnSubNuiOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnSubNuiOverride.setStatus("mandatory")


class _Ux25AdmnBarInCall_Type(Integer32):
    """Custom type ux25AdmnBarInCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarInCall_Type.__name__ = "Integer32"
_Ux25AdmnBarInCall_Object = MibTableColumn
ux25AdmnBarInCall = _Ux25AdmnBarInCall_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 17),
    _Ux25AdmnBarInCall_Type()
)
ux25AdmnBarInCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarInCall.setStatus("mandatory")


class _Ux25AdmnBarOutCall_Type(Integer32):
    """Custom type ux25AdmnBarOutCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25AdmnBarOutCall_Type.__name__ = "Integer32"
_Ux25AdmnBarOutCall_Object = MibTableColumn
ux25AdmnBarOutCall = _Ux25AdmnBarOutCall_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 4, 1, 18),
    _Ux25AdmnBarOutCall_Type()
)
ux25AdmnBarOutCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnBarOutCall.setStatus("mandatory")
_Ux25AdmnTimerTable_Object = MibTable
ux25AdmnTimerTable = _Ux25AdmnTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5)
)
if mibBuilder.loadTexts:
    ux25AdmnTimerTable.setStatus("mandatory")
_Ux25AdmnTimerEntry_Object = MibTableRow
ux25AdmnTimerEntry = _Ux25AdmnTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1)
)
ux25AdmnTimerEntry.setIndexNames(
    (0, "UX25-MIB", "ux25AdmnTimerIndex"),
)
if mibBuilder.loadTexts:
    ux25AdmnTimerEntry.setStatus("mandatory")
_Ux25AdmnTimerIndex_Type = Integer32
_Ux25AdmnTimerIndex_Object = MibTableColumn
ux25AdmnTimerIndex = _Ux25AdmnTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 1),
    _Ux25AdmnTimerIndex_Type()
)
ux25AdmnTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25AdmnTimerIndex.setStatus("mandatory")


class _Ux25AdmnAckDelay_Type(Integer32):
    """Custom type ux25AdmnAckDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnAckDelay_Type.__name__ = "Integer32"
_Ux25AdmnAckDelay_Object = MibTableColumn
ux25AdmnAckDelay = _Ux25AdmnAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 2),
    _Ux25AdmnAckDelay_Type()
)
ux25AdmnAckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnAckDelay.setStatus("mandatory")


class _Ux25AdmnRstrtTime_Type(Integer32):
    """Custom type ux25AdmnRstrtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnRstrtTime_Type.__name__ = "Integer32"
_Ux25AdmnRstrtTime_Object = MibTableColumn
ux25AdmnRstrtTime = _Ux25AdmnRstrtTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 3),
    _Ux25AdmnRstrtTime_Type()
)
ux25AdmnRstrtTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRstrtTime.setStatus("mandatory")


class _Ux25AdmnCallTime_Type(Integer32):
    """Custom type ux25AdmnCallTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnCallTime_Type.__name__ = "Integer32"
_Ux25AdmnCallTime_Object = MibTableColumn
ux25AdmnCallTime = _Ux25AdmnCallTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 4),
    _Ux25AdmnCallTime_Type()
)
ux25AdmnCallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnCallTime.setStatus("mandatory")


class _Ux25AdmnRstTime_Type(Integer32):
    """Custom type ux25AdmnRstTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnRstTime_Type.__name__ = "Integer32"
_Ux25AdmnRstTime_Object = MibTableColumn
ux25AdmnRstTime = _Ux25AdmnRstTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 5),
    _Ux25AdmnRstTime_Type()
)
ux25AdmnRstTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRstTime.setStatus("mandatory")


class _Ux25AdmnClrTime_Type(Integer32):
    """Custom type ux25AdmnClrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnClrTime_Type.__name__ = "Integer32"
_Ux25AdmnClrTime_Object = MibTableColumn
ux25AdmnClrTime = _Ux25AdmnClrTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 6),
    _Ux25AdmnClrTime_Type()
)
ux25AdmnClrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnClrTime.setStatus("mandatory")


class _Ux25AdmnWinStatTime_Type(Integer32):
    """Custom type ux25AdmnWinStatTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnWinStatTime_Type.__name__ = "Integer32"
_Ux25AdmnWinStatTime_Object = MibTableColumn
ux25AdmnWinStatTime = _Ux25AdmnWinStatTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 7),
    _Ux25AdmnWinStatTime_Type()
)
ux25AdmnWinStatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnWinStatTime.setStatus("mandatory")


class _Ux25AdmnWinRotTime_Type(Integer32):
    """Custom type ux25AdmnWinRotTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnWinRotTime_Type.__name__ = "Integer32"
_Ux25AdmnWinRotTime_Object = MibTableColumn
ux25AdmnWinRotTime = _Ux25AdmnWinRotTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 8),
    _Ux25AdmnWinRotTime_Type()
)
ux25AdmnWinRotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnWinRotTime.setStatus("mandatory")


class _Ux25AdmnIntrptTime_Type(Integer32):
    """Custom type ux25AdmnIntrptTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnIntrptTime_Type.__name__ = "Integer32"
_Ux25AdmnIntrptTime_Object = MibTableColumn
ux25AdmnIntrptTime = _Ux25AdmnIntrptTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 9),
    _Ux25AdmnIntrptTime_Type()
)
ux25AdmnIntrptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnIntrptTime.setStatus("mandatory")


class _Ux25AdmnIdleValue_Type(Integer32):
    """Custom type ux25AdmnIdleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnIdleValue_Type.__name__ = "Integer32"
_Ux25AdmnIdleValue_Object = MibTableColumn
ux25AdmnIdleValue = _Ux25AdmnIdleValue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 10),
    _Ux25AdmnIdleValue_Type()
)
ux25AdmnIdleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnIdleValue.setStatus("mandatory")


class _Ux25AdmnConnectValue_Type(Integer32):
    """Custom type ux25AdmnConnectValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnConnectValue_Type.__name__ = "Integer32"
_Ux25AdmnConnectValue_Object = MibTableColumn
ux25AdmnConnectValue = _Ux25AdmnConnectValue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 11),
    _Ux25AdmnConnectValue_Type()
)
ux25AdmnConnectValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnConnectValue.setStatus("mandatory")


class _Ux25AdmnRstrtCnt_Type(Integer32):
    """Custom type ux25AdmnRstrtCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25AdmnRstrtCnt_Type.__name__ = "Integer32"
_Ux25AdmnRstrtCnt_Object = MibTableColumn
ux25AdmnRstrtCnt = _Ux25AdmnRstrtCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 12),
    _Ux25AdmnRstrtCnt_Type()
)
ux25AdmnRstrtCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRstrtCnt.setStatus("mandatory")


class _Ux25AdmnRstCnt_Type(Integer32):
    """Custom type ux25AdmnRstCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25AdmnRstCnt_Type.__name__ = "Integer32"
_Ux25AdmnRstCnt_Object = MibTableColumn
ux25AdmnRstCnt = _Ux25AdmnRstCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 13),
    _Ux25AdmnRstCnt_Type()
)
ux25AdmnRstCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnRstCnt.setStatus("mandatory")


class _Ux25AdmnClrCnt_Type(Integer32):
    """Custom type ux25AdmnClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25AdmnClrCnt_Type.__name__ = "Integer32"
_Ux25AdmnClrCnt_Object = MibTableColumn
ux25AdmnClrCnt = _Ux25AdmnClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 14),
    _Ux25AdmnClrCnt_Type()
)
ux25AdmnClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnClrCnt.setStatus("mandatory")


class _Ux25AdmnLocalDelay_Type(Integer32):
    """Custom type ux25AdmnLocalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnLocalDelay_Type.__name__ = "Integer32"
_Ux25AdmnLocalDelay_Object = MibTableColumn
ux25AdmnLocalDelay = _Ux25AdmnLocalDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 15),
    _Ux25AdmnLocalDelay_Type()
)
ux25AdmnLocalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnLocalDelay.setStatus("mandatory")


class _Ux25AdmnAccessDelay_Type(Integer32):
    """Custom type ux25AdmnAccessDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25AdmnAccessDelay_Type.__name__ = "Integer32"
_Ux25AdmnAccessDelay_Object = MibTableColumn
ux25AdmnAccessDelay = _Ux25AdmnAccessDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 5, 1, 16),
    _Ux25AdmnAccessDelay_Type()
)
ux25AdmnAccessDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25AdmnAccessDelay.setStatus("mandatory")
_Ux25OperChannelTable_Object = MibTable
ux25OperChannelTable = _Ux25OperChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6)
)
if mibBuilder.loadTexts:
    ux25OperChannelTable.setStatus("mandatory")
_Ux25OperChannelEntry_Object = MibTableRow
ux25OperChannelEntry = _Ux25OperChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1)
)
ux25OperChannelEntry.setIndexNames(
    (0, "UX25-MIB", "ux25OperChannelIndex"),
)
if mibBuilder.loadTexts:
    ux25OperChannelEntry.setStatus("mandatory")
_Ux25OperChannelIndex_Type = Integer32
_Ux25OperChannelIndex_Object = MibTableColumn
ux25OperChannelIndex = _Ux25OperChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 1),
    _Ux25OperChannelIndex_Type()
)
ux25OperChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelIndex.setStatus("mandatory")


class _Ux25OperNetMode_Type(Integer32):
    """Custom type ux25OperNetMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("accunet", 15),
          ("austpac", 6),
          ("datanet", 18),
          ("datapac", 7),
          ("datapak", 17),
          ("datexP", 12),
          ("dcs", 19),
          ("ddn", 8),
          ("ddxP", 13),
          ("fDatapac", 21),
          ("finpac", 22),
          ("itapac", 16),
          ("luxpac", 24),
          ("pacnet", 23),
          ("pss", 5),
          ("telenet", 9),
          ("telepac", 20),
          ("transpac", 10),
          ("tymnet", 11),
          ("venusP", 14),
          ("x2580", 4),
          ("x2584", 3),
          ("x2588", 2),
          ("x25Llc", 1))
    )


_Ux25OperNetMode_Type.__name__ = "Integer32"
_Ux25OperNetMode_Object = MibTableColumn
ux25OperNetMode = _Ux25OperNetMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 2),
    _Ux25OperNetMode_Type()
)
ux25OperNetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperNetMode.setStatus("mandatory")


class _Ux25OperProtocolVersion_Type(Integer32):
    """Custom type ux25OperProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x25ver80", 1),
          ("x25ver84", 2),
          ("x25ver88", 3))
    )


_Ux25OperProtocolVersion_Type.__name__ = "Integer32"
_Ux25OperProtocolVersion_Object = MibTableColumn
ux25OperProtocolVersion = _Ux25OperProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 3),
    _Ux25OperProtocolVersion_Type()
)
ux25OperProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperProtocolVersion.setStatus("mandatory")


class _Ux25OperInterfaceMode_Type(Integer32):
    """Custom type ux25OperInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dceMode", 1),
          ("dteMode", 2),
          ("dxeMode", 3))
    )


_Ux25OperInterfaceMode_Type.__name__ = "Integer32"
_Ux25OperInterfaceMode_Object = MibTableColumn
ux25OperInterfaceMode = _Ux25OperInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 4),
    _Ux25OperInterfaceMode_Type()
)
ux25OperInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperInterfaceMode.setStatus("mandatory")


class _Ux25OperLowestPVCVal_Type(Integer32):
    """Custom type ux25OperLowestPVCVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperLowestPVCVal_Type.__name__ = "Integer32"
_Ux25OperLowestPVCVal_Object = MibTableColumn
ux25OperLowestPVCVal = _Ux25OperLowestPVCVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 5),
    _Ux25OperLowestPVCVal_Type()
)
ux25OperLowestPVCVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLowestPVCVal.setStatus("mandatory")


class _Ux25OperHighestPVCVal_Type(Integer32):
    """Custom type ux25OperHighestPVCVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperHighestPVCVal_Type.__name__ = "Integer32"
_Ux25OperHighestPVCVal_Object = MibTableColumn
ux25OperHighestPVCVal = _Ux25OperHighestPVCVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 6),
    _Ux25OperHighestPVCVal_Type()
)
ux25OperHighestPVCVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperHighestPVCVal.setStatus("mandatory")


class _Ux25OperChannelLIC_Type(Integer32):
    """Custom type ux25OperChannelLIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelLIC_Type.__name__ = "Integer32"
_Ux25OperChannelLIC_Object = MibTableColumn
ux25OperChannelLIC = _Ux25OperChannelLIC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 7),
    _Ux25OperChannelLIC_Type()
)
ux25OperChannelLIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelLIC.setStatus("mandatory")


class _Ux25OperChannelHIC_Type(Integer32):
    """Custom type ux25OperChannelHIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelHIC_Type.__name__ = "Integer32"
_Ux25OperChannelHIC_Object = MibTableColumn
ux25OperChannelHIC = _Ux25OperChannelHIC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 8),
    _Ux25OperChannelHIC_Type()
)
ux25OperChannelHIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelHIC.setStatus("mandatory")


class _Ux25OperChannelLTC_Type(Integer32):
    """Custom type ux25OperChannelLTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelLTC_Type.__name__ = "Integer32"
_Ux25OperChannelLTC_Object = MibTableColumn
ux25OperChannelLTC = _Ux25OperChannelLTC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 9),
    _Ux25OperChannelLTC_Type()
)
ux25OperChannelLTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelLTC.setStatus("mandatory")


class _Ux25OperChannelHTC_Type(Integer32):
    """Custom type ux25OperChannelHTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelHTC_Type.__name__ = "Integer32"
_Ux25OperChannelHTC_Object = MibTableColumn
ux25OperChannelHTC = _Ux25OperChannelHTC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 10),
    _Ux25OperChannelHTC_Type()
)
ux25OperChannelHTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelHTC.setStatus("mandatory")


class _Ux25OperChannelLOC_Type(Integer32):
    """Custom type ux25OperChannelLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelLOC_Type.__name__ = "Integer32"
_Ux25OperChannelLOC_Object = MibTableColumn
ux25OperChannelLOC = _Ux25OperChannelLOC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 11),
    _Ux25OperChannelLOC_Type()
)
ux25OperChannelLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelLOC.setStatus("mandatory")


class _Ux25OperChannelHOC_Type(Integer32):
    """Custom type ux25OperChannelHOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ux25OperChannelHOC_Type.__name__ = "Integer32"
_Ux25OperChannelHOC_Object = MibTableColumn
ux25OperChannelHOC = _Ux25OperChannelHOC_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 6, 1, 12),
    _Ux25OperChannelHOC_Type()
)
ux25OperChannelHOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperChannelHOC.setStatus("mandatory")
_Ux25OperClassTable_Object = MibTable
ux25OperClassTable = _Ux25OperClassTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7)
)
if mibBuilder.loadTexts:
    ux25OperClassTable.setStatus("mandatory")
_Ux25OperClassEntry_Object = MibTableRow
ux25OperClassEntry = _Ux25OperClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1)
)
ux25OperClassEntry.setIndexNames(
    (0, "UX25-MIB", "ux25OperClassIndex"),
)
if mibBuilder.loadTexts:
    ux25OperClassEntry.setStatus("mandatory")
_Ux25OperClassIndex_Type = Integer32
_Ux25OperClassIndex_Object = MibTableColumn
ux25OperClassIndex = _Ux25OperClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 1),
    _Ux25OperClassIndex_Type()
)
ux25OperClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperClassIndex.setStatus("mandatory")


class _Ux25OperLocMaxThruPutClass_Type(Integer32):
    """Custom type ux25OperLocMaxThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperLocMaxThruPutClass_Type.__name__ = "Integer32"
_Ux25OperLocMaxThruPutClass_Object = MibTableColumn
ux25OperLocMaxThruPutClass = _Ux25OperLocMaxThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 2),
    _Ux25OperLocMaxThruPutClass_Type()
)
ux25OperLocMaxThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocMaxThruPutClass.setStatus("mandatory")


class _Ux25OperRemMaxThruPutClass_Type(Integer32):
    """Custom type ux25OperRemMaxThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperRemMaxThruPutClass_Type.__name__ = "Integer32"
_Ux25OperRemMaxThruPutClass_Object = MibTableColumn
ux25OperRemMaxThruPutClass = _Ux25OperRemMaxThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 3),
    _Ux25OperRemMaxThruPutClass_Type()
)
ux25OperRemMaxThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemMaxThruPutClass.setStatus("mandatory")


class _Ux25OperLocDefThruPutClass_Type(Integer32):
    """Custom type ux25OperLocDefThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperLocDefThruPutClass_Type.__name__ = "Integer32"
_Ux25OperLocDefThruPutClass_Object = MibTableColumn
ux25OperLocDefThruPutClass = _Ux25OperLocDefThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 4),
    _Ux25OperLocDefThruPutClass_Type()
)
ux25OperLocDefThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocDefThruPutClass.setStatus("mandatory")


class _Ux25OperRemDefThruPutClass_Type(Integer32):
    """Custom type ux25OperRemDefThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperRemDefThruPutClass_Type.__name__ = "Integer32"
_Ux25OperRemDefThruPutClass_Object = MibTableColumn
ux25OperRemDefThruPutClass = _Ux25OperRemDefThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 5),
    _Ux25OperRemDefThruPutClass_Type()
)
ux25OperRemDefThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemDefThruPutClass.setStatus("mandatory")


class _Ux25OperLocMinThruPutClass_Type(Integer32):
    """Custom type ux25OperLocMinThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperLocMinThruPutClass_Type.__name__ = "Integer32"
_Ux25OperLocMinThruPutClass_Object = MibTableColumn
ux25OperLocMinThruPutClass = _Ux25OperLocMinThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 6),
    _Ux25OperLocMinThruPutClass_Type()
)
ux25OperLocMinThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocMinThruPutClass.setStatus("mandatory")


class _Ux25OperRemMinThruPutClass_Type(Integer32):
    """Custom type ux25OperRemMinThruPutClass based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 8),
          ("tc150", 5),
          ("tc19200", 12),
          ("tc2400", 9),
          ("tc300", 6),
          ("tc4800", 10),
          ("tc48000", 13),
          ("tc600", 7),
          ("tc75", 4),
          ("tc9600", 11),
          ("tcReserved0", 1),
          ("tcReserved1", 2),
          ("tcReserved13", 14),
          ("tcReserved14", 15),
          ("tcReserved15", 16),
          ("tcReserved2", 3))
    )


_Ux25OperRemMinThruPutClass_Type.__name__ = "Integer32"
_Ux25OperRemMinThruPutClass_Object = MibTableColumn
ux25OperRemMinThruPutClass = _Ux25OperRemMinThruPutClass_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 7),
    _Ux25OperRemMinThruPutClass_Type()
)
ux25OperRemMinThruPutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemMinThruPutClass.setStatus("mandatory")


class _Ux25OperThclassNegToDef_Type(Integer32):
    """Custom type ux25OperThclassNegToDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperThclassNegToDef_Type.__name__ = "Integer32"
_Ux25OperThclassNegToDef_Object = MibTableColumn
ux25OperThclassNegToDef = _Ux25OperThclassNegToDef_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 8),
    _Ux25OperThclassNegToDef_Type()
)
ux25OperThclassNegToDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperThclassNegToDef.setStatus("mandatory")


class _Ux25OperThclassType_Type(Integer32):
    """Custom type ux25OperThclassType based on Integer32"""
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
        *(("bothNibbles", 4),
          ("highNibble", 3),
          ("loNibble", 2),
          ("noTcType", 1))
    )


_Ux25OperThclassType_Type.__name__ = "Integer32"
_Ux25OperThclassType_Object = MibTableColumn
ux25OperThclassType = _Ux25OperThclassType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 9),
    _Ux25OperThclassType_Type()
)
ux25OperThclassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperThclassType.setStatus("mandatory")


class _Ux25OperThclassWinMap_Type(DisplayString):
    """Custom type ux25OperThclassWinMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 63),
    )


_Ux25OperThclassWinMap_Type.__name__ = "DisplayString"
_Ux25OperThclassWinMap_Object = MibTableColumn
ux25OperThclassWinMap = _Ux25OperThclassWinMap_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 10),
    _Ux25OperThclassWinMap_Type()
)
ux25OperThclassWinMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperThclassWinMap.setStatus("mandatory")


class _Ux25OperThclassPackMap_Type(DisplayString):
    """Custom type ux25OperThclassPackMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 47),
    )


_Ux25OperThclassPackMap_Type.__name__ = "DisplayString"
_Ux25OperThclassPackMap_Object = MibTableColumn
ux25OperThclassPackMap = _Ux25OperThclassPackMap_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 7, 1, 11),
    _Ux25OperThclassPackMap_Type()
)
ux25OperThclassPackMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperThclassPackMap.setStatus("mandatory")
_Ux25OperPacketTable_Object = MibTable
ux25OperPacketTable = _Ux25OperPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8)
)
if mibBuilder.loadTexts:
    ux25OperPacketTable.setStatus("mandatory")
_Ux25OperPacketEntry_Object = MibTableRow
ux25OperPacketEntry = _Ux25OperPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1)
)
ux25OperPacketEntry.setIndexNames(
    (0, "UX25-MIB", "ux25OperPacketIndex"),
)
if mibBuilder.loadTexts:
    ux25OperPacketEntry.setStatus("mandatory")
_Ux25OperPacketIndex_Type = Integer32
_Ux25OperPacketIndex_Object = MibTableColumn
ux25OperPacketIndex = _Ux25OperPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 1),
    _Ux25OperPacketIndex_Type()
)
ux25OperPacketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperPacketIndex.setStatus("mandatory")


class _Ux25OperPktSequencing_Type(Integer32):
    """Custom type ux25OperPktSequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("pktSeq128", 32),
          ("pktSeq8", 16))
    )


_Ux25OperPktSequencing_Type.__name__ = "Integer32"
_Ux25OperPktSequencing_Object = MibTableColumn
ux25OperPktSequencing = _Ux25OperPktSequencing_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 2),
    _Ux25OperPktSequencing_Type()
)
ux25OperPktSequencing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperPktSequencing.setStatus("mandatory")


class _Ux25OperLocMaxPktSize_Type(Integer32):
    """Custom type ux25OperLocMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("maxPktSz128", 7),
          ("maxPktSz256", 8),
          ("maxPktSz512", 9))
    )


_Ux25OperLocMaxPktSize_Type.__name__ = "Integer32"
_Ux25OperLocMaxPktSize_Object = MibTableColumn
ux25OperLocMaxPktSize = _Ux25OperLocMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 3),
    _Ux25OperLocMaxPktSize_Type()
)
ux25OperLocMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocMaxPktSize.setStatus("mandatory")


class _Ux25OperRemMaxPktSize_Type(Integer32):
    """Custom type ux25OperRemMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("maxPktSz128", 7),
          ("maxPktSz256", 8),
          ("maxPktSz512", 9))
    )


_Ux25OperRemMaxPktSize_Type.__name__ = "Integer32"
_Ux25OperRemMaxPktSize_Object = MibTableColumn
ux25OperRemMaxPktSize = _Ux25OperRemMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 4),
    _Ux25OperRemMaxPktSize_Type()
)
ux25OperRemMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemMaxPktSize.setStatus("mandatory")


class _Ux25OperLocDefPktSize_Type(Integer32):
    """Custom type ux25OperLocDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("defPktSz128", 7),
          ("defPktSz16", 4),
          ("defPktSz256", 8),
          ("defPktSz32", 5),
          ("defPktSz512", 9),
          ("defPktSz64", 6))
    )


_Ux25OperLocDefPktSize_Type.__name__ = "Integer32"
_Ux25OperLocDefPktSize_Object = MibTableColumn
ux25OperLocDefPktSize = _Ux25OperLocDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 5),
    _Ux25OperLocDefPktSize_Type()
)
ux25OperLocDefPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocDefPktSize.setStatus("mandatory")


class _Ux25OperRemDefPktSize_Type(Integer32):
    """Custom type ux25OperRemDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("defPktSz128", 7),
          ("defPktSz16", 4),
          ("defPktSz256", 8),
          ("defPktSz32", 5),
          ("defPktSz512", 9),
          ("defPktSz64", 6))
    )


_Ux25OperRemDefPktSize_Type.__name__ = "Integer32"
_Ux25OperRemDefPktSize_Object = MibTableColumn
ux25OperRemDefPktSize = _Ux25OperRemDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 6),
    _Ux25OperRemDefPktSize_Type()
)
ux25OperRemDefPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemDefPktSize.setStatus("mandatory")


class _Ux25OperLocMaxWinSize_Type(Integer32):
    """Custom type ux25OperLocMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Ux25OperLocMaxWinSize_Type.__name__ = "Integer32"
_Ux25OperLocMaxWinSize_Object = MibTableColumn
ux25OperLocMaxWinSize = _Ux25OperLocMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 7),
    _Ux25OperLocMaxWinSize_Type()
)
ux25OperLocMaxWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocMaxWinSize.setStatus("mandatory")


class _Ux25OperRemMaxWinSize_Type(Integer32):
    """Custom type ux25OperRemMaxWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Ux25OperRemMaxWinSize_Type.__name__ = "Integer32"
_Ux25OperRemMaxWinSize_Object = MibTableColumn
ux25OperRemMaxWinSize = _Ux25OperRemMaxWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 8),
    _Ux25OperRemMaxWinSize_Type()
)
ux25OperRemMaxWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemMaxWinSize.setStatus("mandatory")


class _Ux25OperLocDefWinSize_Type(Integer32):
    """Custom type ux25OperLocDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Ux25OperLocDefWinSize_Type.__name__ = "Integer32"
_Ux25OperLocDefWinSize_Object = MibTableColumn
ux25OperLocDefWinSize = _Ux25OperLocDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 9),
    _Ux25OperLocDefWinSize_Type()
)
ux25OperLocDefWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocDefWinSize.setStatus("mandatory")


class _Ux25OperRemDefWinSize_Type(Integer32):
    """Custom type ux25OperRemDefWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Ux25OperRemDefWinSize_Type.__name__ = "Integer32"
_Ux25OperRemDefWinSize_Object = MibTableColumn
ux25OperRemDefWinSize = _Ux25OperRemDefWinSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 10),
    _Ux25OperRemDefWinSize_Type()
)
ux25OperRemDefWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRemDefWinSize.setStatus("mandatory")


class _Ux25OperMaxNSDULimit_Type(Integer32):
    """Custom type ux25OperMaxNSDULimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperMaxNSDULimit_Type.__name__ = "Integer32"
_Ux25OperMaxNSDULimit_Object = MibTableColumn
ux25OperMaxNSDULimit = _Ux25OperMaxNSDULimit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 11),
    _Ux25OperMaxNSDULimit_Type()
)
ux25OperMaxNSDULimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperMaxNSDULimit.setStatus("mandatory")


class _Ux25OperAccNoDiagnostic_Type(Integer32):
    """Custom type ux25OperAccNoDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperAccNoDiagnostic_Type.__name__ = "Integer32"
_Ux25OperAccNoDiagnostic_Object = MibTableColumn
ux25OperAccNoDiagnostic = _Ux25OperAccNoDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 12),
    _Ux25OperAccNoDiagnostic_Type()
)
ux25OperAccNoDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperAccNoDiagnostic.setStatus("mandatory")


class _Ux25OperUseDiagnosticPacket_Type(Integer32):
    """Custom type ux25OperUseDiagnosticPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperUseDiagnosticPacket_Type.__name__ = "Integer32"
_Ux25OperUseDiagnosticPacket_Object = MibTableColumn
ux25OperUseDiagnosticPacket = _Ux25OperUseDiagnosticPacket_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 13),
    _Ux25OperUseDiagnosticPacket_Type()
)
ux25OperUseDiagnosticPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperUseDiagnosticPacket.setStatus("mandatory")


class _Ux25OperItutClearLen_Type(Integer32):
    """Custom type ux25OperItutClearLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperItutClearLen_Type.__name__ = "Integer32"
_Ux25OperItutClearLen_Object = MibTableColumn
ux25OperItutClearLen = _Ux25OperItutClearLen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 14),
    _Ux25OperItutClearLen_Type()
)
ux25OperItutClearLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperItutClearLen.setStatus("mandatory")


class _Ux25OperBarDiagnosticPacket_Type(Integer32):
    """Custom type ux25OperBarDiagnosticPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarDiagnosticPacket_Type.__name__ = "Integer32"
_Ux25OperBarDiagnosticPacket_Object = MibTableColumn
ux25OperBarDiagnosticPacket = _Ux25OperBarDiagnosticPacket_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 15),
    _Ux25OperBarDiagnosticPacket_Type()
)
ux25OperBarDiagnosticPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarDiagnosticPacket.setStatus("mandatory")


class _Ux25OperDiscNzDiagnostic_Type(Integer32):
    """Custom type ux25OperDiscNzDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperDiscNzDiagnostic_Type.__name__ = "Integer32"
_Ux25OperDiscNzDiagnostic_Object = MibTableColumn
ux25OperDiscNzDiagnostic = _Ux25OperDiscNzDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 16),
    _Ux25OperDiscNzDiagnostic_Type()
)
ux25OperDiscNzDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDiscNzDiagnostic.setStatus("mandatory")


class _Ux25OperAcceptHexAdd_Type(Integer32):
    """Custom type ux25OperAcceptHexAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperAcceptHexAdd_Type.__name__ = "Integer32"
_Ux25OperAcceptHexAdd_Object = MibTableColumn
ux25OperAcceptHexAdd = _Ux25OperAcceptHexAdd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 17),
    _Ux25OperAcceptHexAdd_Type()
)
ux25OperAcceptHexAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperAcceptHexAdd.setStatus("mandatory")


class _Ux25OperBarNonPrivilegeListen_Type(Integer32):
    """Custom type ux25OperBarNonPrivilegeListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarNonPrivilegeListen_Type.__name__ = "Integer32"
_Ux25OperBarNonPrivilegeListen_Object = MibTableColumn
ux25OperBarNonPrivilegeListen = _Ux25OperBarNonPrivilegeListen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 18),
    _Ux25OperBarNonPrivilegeListen_Type()
)
ux25OperBarNonPrivilegeListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarNonPrivilegeListen.setStatus("mandatory")


class _Ux25OperIntlAddrRecognition_Type(Integer32):
    """Custom type ux25OperIntlAddrRecognition based on Integer32"""
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
        *(("examineDnic", 2),
          ("notDistinguished", 1),
          ("prefix0", 4),
          ("prefix1", 3))
    )


_Ux25OperIntlAddrRecognition_Type.__name__ = "Integer32"
_Ux25OperIntlAddrRecognition_Object = MibTableColumn
ux25OperIntlAddrRecognition = _Ux25OperIntlAddrRecognition_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 19),
    _Ux25OperIntlAddrRecognition_Type()
)
ux25OperIntlAddrRecognition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperIntlAddrRecognition.setStatus("mandatory")


class _Ux25OperDnic_Type(DisplayString):
    """Custom type ux25OperDnic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Ux25OperDnic_Type.__name__ = "DisplayString"
_Ux25OperDnic_Object = MibTableColumn
ux25OperDnic = _Ux25OperDnic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 20),
    _Ux25OperDnic_Type()
)
ux25OperDnic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDnic.setStatus("mandatory")


class _Ux25OperIntlPrioritized_Type(Integer32):
    """Custom type ux25OperIntlPrioritized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperIntlPrioritized_Type.__name__ = "Integer32"
_Ux25OperIntlPrioritized_Object = MibTableColumn
ux25OperIntlPrioritized = _Ux25OperIntlPrioritized_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 21),
    _Ux25OperIntlPrioritized_Type()
)
ux25OperIntlPrioritized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperIntlPrioritized.setStatus("mandatory")


class _Ux25OperPrtyEncodeCtrl_Type(Integer32):
    """Custom type ux25OperPrtyEncodeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("datapacPriority76", 2),
          ("datapacTraffic80", 3),
          ("x2588", 1))
    )


_Ux25OperPrtyEncodeCtrl_Type.__name__ = "Integer32"
_Ux25OperPrtyEncodeCtrl_Object = MibTableColumn
ux25OperPrtyEncodeCtrl = _Ux25OperPrtyEncodeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 22),
    _Ux25OperPrtyEncodeCtrl_Type()
)
ux25OperPrtyEncodeCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperPrtyEncodeCtrl.setStatus("mandatory")


class _Ux25OperPrtyPktForcedVal_Type(Integer32):
    """Custom type ux25OperPrtyPktForcedVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("prioPktSz0", 1),
          ("prioPktSz10", 11),
          ("prioPktSz11", 12),
          ("prioPktSz12", 13),
          ("prioPktSz4", 5),
          ("prioPktSz5", 6),
          ("prioPktSz6", 7),
          ("prioPktSz7", 8),
          ("prioPktSz8", 9),
          ("prioPktSz9", 10))
    )


_Ux25OperPrtyPktForcedVal_Type.__name__ = "Integer32"
_Ux25OperPrtyPktForcedVal_Object = MibTableColumn
ux25OperPrtyPktForcedVal = _Ux25OperPrtyPktForcedVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 23),
    _Ux25OperPrtyPktForcedVal_Type()
)
ux25OperPrtyPktForcedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperPrtyPktForcedVal.setStatus("mandatory")


class _Ux25OperSrcAddrCtrl_Type(Integer32):
    """Custom type ux25OperSrcAddrCtrl based on Integer32"""
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
        *(("forceLocal", 4),
          ("noSaCntrl", 1),
          ("omitDte", 2),
          ("useLocal", 3))
    )


_Ux25OperSrcAddrCtrl_Type.__name__ = "Integer32"
_Ux25OperSrcAddrCtrl_Object = MibTableColumn
ux25OperSrcAddrCtrl = _Ux25OperSrcAddrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 24),
    _Ux25OperSrcAddrCtrl_Type()
)
ux25OperSrcAddrCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSrcAddrCtrl.setStatus("mandatory")


class _Ux25OperDbitInAccept_Type(Integer32):
    """Custom type ux25OperDbitInAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25OperDbitInAccept_Type.__name__ = "Integer32"
_Ux25OperDbitInAccept_Object = MibTableColumn
ux25OperDbitInAccept = _Ux25OperDbitInAccept_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 25),
    _Ux25OperDbitInAccept_Type()
)
ux25OperDbitInAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDbitInAccept.setStatus("mandatory")


class _Ux25OperDbitOutAccept_Type(Integer32):
    """Custom type ux25OperDbitOutAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25OperDbitOutAccept_Type.__name__ = "Integer32"
_Ux25OperDbitOutAccept_Object = MibTableColumn
ux25OperDbitOutAccept = _Ux25OperDbitOutAccept_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 26),
    _Ux25OperDbitOutAccept_Type()
)
ux25OperDbitOutAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDbitOutAccept.setStatus("mandatory")


class _Ux25OperDbitInData_Type(Integer32):
    """Custom type ux25OperDbitInData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25OperDbitInData_Type.__name__ = "Integer32"
_Ux25OperDbitInData_Object = MibTableColumn
ux25OperDbitInData = _Ux25OperDbitInData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 27),
    _Ux25OperDbitInData_Type()
)
ux25OperDbitInData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDbitInData.setStatus("mandatory")


class _Ux25OperDbitOutData_Type(Integer32):
    """Custom type ux25OperDbitOutData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCall", 3),
          ("leaveDbit", 1),
          ("zeroDbit", 2))
    )


_Ux25OperDbitOutData_Type.__name__ = "Integer32"
_Ux25OperDbitOutData_Object = MibTableColumn
ux25OperDbitOutData = _Ux25OperDbitOutData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 8, 1, 28),
    _Ux25OperDbitOutData_Type()
)
ux25OperDbitOutData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperDbitOutData.setStatus("mandatory")
_Ux25OperSubscriberTable_Object = MibTable
ux25OperSubscriberTable = _Ux25OperSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9)
)
if mibBuilder.loadTexts:
    ux25OperSubscriberTable.setStatus("mandatory")
_Ux25OperSubscriberEntry_Object = MibTableRow
ux25OperSubscriberEntry = _Ux25OperSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1)
)
ux25OperSubscriberEntry.setIndexNames(
    (0, "UX25-MIB", "ux25OperSubscriberIndex"),
)
if mibBuilder.loadTexts:
    ux25OperSubscriberEntry.setStatus("mandatory")
_Ux25OperSubscriberIndex_Type = Integer32
_Ux25OperSubscriberIndex_Object = MibTableColumn
ux25OperSubscriberIndex = _Ux25OperSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 1),
    _Ux25OperSubscriberIndex_Type()
)
ux25OperSubscriberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubscriberIndex.setStatus("mandatory")


class _Ux25OperSubCugIaoa_Type(Integer32):
    """Custom type ux25OperSubCugIaoa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubCugIaoa_Type.__name__ = "Integer32"
_Ux25OperSubCugIaoa_Object = MibTableColumn
ux25OperSubCugIaoa = _Ux25OperSubCugIaoa_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 2),
    _Ux25OperSubCugIaoa_Type()
)
ux25OperSubCugIaoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubCugIaoa.setStatus("mandatory")


class _Ux25OperSubCugPref_Type(Integer32):
    """Custom type ux25OperSubCugPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubCugPref_Type.__name__ = "Integer32"
_Ux25OperSubCugPref_Object = MibTableColumn
ux25OperSubCugPref = _Ux25OperSubCugPref_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 3),
    _Ux25OperSubCugPref_Type()
)
ux25OperSubCugPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubCugPref.setStatus("mandatory")


class _Ux25OperSubCugoa_Type(Integer32):
    """Custom type ux25OperSubCugoa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubCugoa_Type.__name__ = "Integer32"
_Ux25OperSubCugoa_Object = MibTableColumn
ux25OperSubCugoa = _Ux25OperSubCugoa_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 4),
    _Ux25OperSubCugoa_Type()
)
ux25OperSubCugoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubCugoa.setStatus("mandatory")


class _Ux25OperSubCugia_Type(Integer32):
    """Custom type ux25OperSubCugia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubCugia_Type.__name__ = "Integer32"
_Ux25OperSubCugia_Object = MibTableColumn
ux25OperSubCugia = _Ux25OperSubCugia_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 5),
    _Ux25OperSubCugia_Type()
)
ux25OperSubCugia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubCugia.setStatus("mandatory")


class _Ux25OperCugFormat_Type(Integer32):
    """Custom type ux25OperCugFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("extended", 2))
    )


_Ux25OperCugFormat_Type.__name__ = "Integer32"
_Ux25OperCugFormat_Object = MibTableColumn
ux25OperCugFormat = _Ux25OperCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 6),
    _Ux25OperCugFormat_Type()
)
ux25OperCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperCugFormat.setStatus("mandatory")


class _Ux25OperBarInCug_Type(Integer32):
    """Custom type ux25OperBarInCug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarInCug_Type.__name__ = "Integer32"
_Ux25OperBarInCug_Object = MibTableColumn
ux25OperBarInCug = _Ux25OperBarInCug_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 7),
    _Ux25OperBarInCug_Type()
)
ux25OperBarInCug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarInCug.setStatus("mandatory")


class _Ux25OperSubExtended_Type(Integer32):
    """Custom type ux25OperSubExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubExtended_Type.__name__ = "Integer32"
_Ux25OperSubExtended_Object = MibTableColumn
ux25OperSubExtended = _Ux25OperSubExtended_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 8),
    _Ux25OperSubExtended_Type()
)
ux25OperSubExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubExtended.setStatus("mandatory")


class _Ux25OperBarExtended_Type(Integer32):
    """Custom type ux25OperBarExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarExtended_Type.__name__ = "Integer32"
_Ux25OperBarExtended_Object = MibTableColumn
ux25OperBarExtended = _Ux25OperBarExtended_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 9),
    _Ux25OperBarExtended_Type()
)
ux25OperBarExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarExtended.setStatus("mandatory")


class _Ux25OperSubFstSelNoRstrct_Type(Integer32):
    """Custom type ux25OperSubFstSelNoRstrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubFstSelNoRstrct_Type.__name__ = "Integer32"
_Ux25OperSubFstSelNoRstrct_Object = MibTableColumn
ux25OperSubFstSelNoRstrct = _Ux25OperSubFstSelNoRstrct_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 10),
    _Ux25OperSubFstSelNoRstrct_Type()
)
ux25OperSubFstSelNoRstrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubFstSelNoRstrct.setStatus("mandatory")


class _Ux25OperSubFstSelWthRstrct_Type(Integer32):
    """Custom type ux25OperSubFstSelWthRstrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubFstSelWthRstrct_Type.__name__ = "Integer32"
_Ux25OperSubFstSelWthRstrct_Object = MibTableColumn
ux25OperSubFstSelWthRstrct = _Ux25OperSubFstSelWthRstrct_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 11),
    _Ux25OperSubFstSelWthRstrct_Type()
)
ux25OperSubFstSelWthRstrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubFstSelWthRstrct.setStatus("mandatory")


class _Ux25OperAccptRvsChrgng_Type(Integer32):
    """Custom type ux25OperAccptRvsChrgng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperAccptRvsChrgng_Type.__name__ = "Integer32"
_Ux25OperAccptRvsChrgng_Object = MibTableColumn
ux25OperAccptRvsChrgng = _Ux25OperAccptRvsChrgng_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 12),
    _Ux25OperAccptRvsChrgng_Type()
)
ux25OperAccptRvsChrgng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperAccptRvsChrgng.setStatus("mandatory")


class _Ux25OperSubLocChargePrevent_Type(Integer32):
    """Custom type ux25OperSubLocChargePrevent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubLocChargePrevent_Type.__name__ = "Integer32"
_Ux25OperSubLocChargePrevent_Object = MibTableColumn
ux25OperSubLocChargePrevent = _Ux25OperSubLocChargePrevent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 13),
    _Ux25OperSubLocChargePrevent_Type()
)
ux25OperSubLocChargePrevent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubLocChargePrevent.setStatus("mandatory")


class _Ux25OperSubToaNpiFormat_Type(Integer32):
    """Custom type ux25OperSubToaNpiFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubToaNpiFormat_Type.__name__ = "Integer32"
_Ux25OperSubToaNpiFormat_Object = MibTableColumn
ux25OperSubToaNpiFormat = _Ux25OperSubToaNpiFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 14),
    _Ux25OperSubToaNpiFormat_Type()
)
ux25OperSubToaNpiFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubToaNpiFormat.setStatus("mandatory")


class _Ux25OperBarToaNpiFormat_Type(Integer32):
    """Custom type ux25OperBarToaNpiFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarToaNpiFormat_Type.__name__ = "Integer32"
_Ux25OperBarToaNpiFormat_Object = MibTableColumn
ux25OperBarToaNpiFormat = _Ux25OperBarToaNpiFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 15),
    _Ux25OperBarToaNpiFormat_Type()
)
ux25OperBarToaNpiFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarToaNpiFormat.setStatus("mandatory")


class _Ux25OperSubNuiOverride_Type(Integer32):
    """Custom type ux25OperSubNuiOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperSubNuiOverride_Type.__name__ = "Integer32"
_Ux25OperSubNuiOverride_Object = MibTableColumn
ux25OperSubNuiOverride = _Ux25OperSubNuiOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 16),
    _Ux25OperSubNuiOverride_Type()
)
ux25OperSubNuiOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperSubNuiOverride.setStatus("mandatory")


class _Ux25OperBarInCall_Type(Integer32):
    """Custom type ux25OperBarInCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarInCall_Type.__name__ = "Integer32"
_Ux25OperBarInCall_Object = MibTableColumn
ux25OperBarInCall = _Ux25OperBarInCall_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 17),
    _Ux25OperBarInCall_Type()
)
ux25OperBarInCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarInCall.setStatus("mandatory")


class _Ux25OperBarOutCall_Type(Integer32):
    """Custom type ux25OperBarOutCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ux25OperBarOutCall_Type.__name__ = "Integer32"
_Ux25OperBarOutCall_Object = MibTableColumn
ux25OperBarOutCall = _Ux25OperBarOutCall_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 9, 1, 18),
    _Ux25OperBarOutCall_Type()
)
ux25OperBarOutCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperBarOutCall.setStatus("mandatory")
_Ux25OperTimerTable_Object = MibTable
ux25OperTimerTable = _Ux25OperTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10)
)
if mibBuilder.loadTexts:
    ux25OperTimerTable.setStatus("mandatory")
_Ux25OperTimerEntry_Object = MibTableRow
ux25OperTimerEntry = _Ux25OperTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1)
)
ux25OperTimerEntry.setIndexNames(
    (0, "UX25-MIB", "ux25OperTimerIndex"),
)
if mibBuilder.loadTexts:
    ux25OperTimerEntry.setStatus("mandatory")
_Ux25OperTimerIndex_Type = Integer32
_Ux25OperTimerIndex_Object = MibTableColumn
ux25OperTimerIndex = _Ux25OperTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 1),
    _Ux25OperTimerIndex_Type()
)
ux25OperTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperTimerIndex.setStatus("mandatory")


class _Ux25OperAckDelay_Type(Integer32):
    """Custom type ux25OperAckDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperAckDelay_Type.__name__ = "Integer32"
_Ux25OperAckDelay_Object = MibTableColumn
ux25OperAckDelay = _Ux25OperAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 2),
    _Ux25OperAckDelay_Type()
)
ux25OperAckDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperAckDelay.setStatus("mandatory")


class _Ux25OperRstrtTime_Type(Integer32):
    """Custom type ux25OperRstrtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperRstrtTime_Type.__name__ = "Integer32"
_Ux25OperRstrtTime_Object = MibTableColumn
ux25OperRstrtTime = _Ux25OperRstrtTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 3),
    _Ux25OperRstrtTime_Type()
)
ux25OperRstrtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRstrtTime.setStatus("mandatory")


class _Ux25OperCallTime_Type(Integer32):
    """Custom type ux25OperCallTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperCallTime_Type.__name__ = "Integer32"
_Ux25OperCallTime_Object = MibTableColumn
ux25OperCallTime = _Ux25OperCallTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 4),
    _Ux25OperCallTime_Type()
)
ux25OperCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperCallTime.setStatus("mandatory")


class _Ux25OperRstTime_Type(Integer32):
    """Custom type ux25OperRstTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperRstTime_Type.__name__ = "Integer32"
_Ux25OperRstTime_Object = MibTableColumn
ux25OperRstTime = _Ux25OperRstTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 5),
    _Ux25OperRstTime_Type()
)
ux25OperRstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRstTime.setStatus("mandatory")


class _Ux25OperClrTime_Type(Integer32):
    """Custom type ux25OperClrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperClrTime_Type.__name__ = "Integer32"
_Ux25OperClrTime_Object = MibTableColumn
ux25OperClrTime = _Ux25OperClrTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 6),
    _Ux25OperClrTime_Type()
)
ux25OperClrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperClrTime.setStatus("mandatory")


class _Ux25OperWinStatTime_Type(Integer32):
    """Custom type ux25OperWinStatTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperWinStatTime_Type.__name__ = "Integer32"
_Ux25OperWinStatTime_Object = MibTableColumn
ux25OperWinStatTime = _Ux25OperWinStatTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 7),
    _Ux25OperWinStatTime_Type()
)
ux25OperWinStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperWinStatTime.setStatus("mandatory")


class _Ux25OperWinRotTime_Type(Integer32):
    """Custom type ux25OperWinRotTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperWinRotTime_Type.__name__ = "Integer32"
_Ux25OperWinRotTime_Object = MibTableColumn
ux25OperWinRotTime = _Ux25OperWinRotTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 8),
    _Ux25OperWinRotTime_Type()
)
ux25OperWinRotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperWinRotTime.setStatus("mandatory")


class _Ux25OperIntrptTime_Type(Integer32):
    """Custom type ux25OperIntrptTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperIntrptTime_Type.__name__ = "Integer32"
_Ux25OperIntrptTime_Object = MibTableColumn
ux25OperIntrptTime = _Ux25OperIntrptTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 9),
    _Ux25OperIntrptTime_Type()
)
ux25OperIntrptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperIntrptTime.setStatus("mandatory")


class _Ux25OperIdleValue_Type(Integer32):
    """Custom type ux25OperIdleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperIdleValue_Type.__name__ = "Integer32"
_Ux25OperIdleValue_Object = MibTableColumn
ux25OperIdleValue = _Ux25OperIdleValue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 10),
    _Ux25OperIdleValue_Type()
)
ux25OperIdleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperIdleValue.setStatus("mandatory")


class _Ux25OperConnectValue_Type(Integer32):
    """Custom type ux25OperConnectValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperConnectValue_Type.__name__ = "Integer32"
_Ux25OperConnectValue_Object = MibTableColumn
ux25OperConnectValue = _Ux25OperConnectValue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 11),
    _Ux25OperConnectValue_Type()
)
ux25OperConnectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperConnectValue.setStatus("mandatory")


class _Ux25OperRstrtCnt_Type(Integer32):
    """Custom type ux25OperRstrtCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25OperRstrtCnt_Type.__name__ = "Integer32"
_Ux25OperRstrtCnt_Object = MibTableColumn
ux25OperRstrtCnt = _Ux25OperRstrtCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 12),
    _Ux25OperRstrtCnt_Type()
)
ux25OperRstrtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRstrtCnt.setStatus("mandatory")


class _Ux25OperRstCnt_Type(Integer32):
    """Custom type ux25OperRstCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25OperRstCnt_Type.__name__ = "Integer32"
_Ux25OperRstCnt_Object = MibTableColumn
ux25OperRstCnt = _Ux25OperRstCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 13),
    _Ux25OperRstCnt_Type()
)
ux25OperRstCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperRstCnt.setStatus("mandatory")


class _Ux25OperClrCnt_Type(Integer32):
    """Custom type ux25OperClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ux25OperClrCnt_Type.__name__ = "Integer32"
_Ux25OperClrCnt_Object = MibTableColumn
ux25OperClrCnt = _Ux25OperClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 14),
    _Ux25OperClrCnt_Type()
)
ux25OperClrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperClrCnt.setStatus("mandatory")


class _Ux25OperLocalDelay_Type(Integer32):
    """Custom type ux25OperLocalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperLocalDelay_Type.__name__ = "Integer32"
_Ux25OperLocalDelay_Object = MibTableColumn
ux25OperLocalDelay = _Ux25OperLocalDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 15),
    _Ux25OperLocalDelay_Type()
)
ux25OperLocalDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperLocalDelay.setStatus("mandatory")


class _Ux25OperAccessDelay_Type(Integer32):
    """Custom type ux25OperAccessDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_Ux25OperAccessDelay_Type.__name__ = "Integer32"
_Ux25OperAccessDelay_Object = MibTableColumn
ux25OperAccessDelay = _Ux25OperAccessDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 10, 1, 16),
    _Ux25OperAccessDelay_Type()
)
ux25OperAccessDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25OperAccessDelay.setStatus("mandatory")
_Ux25StatTable_Object = MibTable
ux25StatTable = _Ux25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11)
)
if mibBuilder.loadTexts:
    ux25StatTable.setStatus("mandatory")
_Ux25StatEntry_Object = MibTableRow
ux25StatEntry = _Ux25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1)
)
ux25StatEntry.setIndexNames(
    (0, "UX25-MIB", "ux25StatIndex"),
)
if mibBuilder.loadTexts:
    ux25StatEntry.setStatus("mandatory")
_Ux25StatIndex_Type = Integer32
_Ux25StatIndex_Object = MibTableColumn
ux25StatIndex = _Ux25StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 1),
    _Ux25StatIndex_Type()
)
ux25StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatIndex.setStatus("mandatory")
_Ux25StatCallsRcvd_Type = Integer32
_Ux25StatCallsRcvd_Object = MibTableColumn
ux25StatCallsRcvd = _Ux25StatCallsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 2),
    _Ux25StatCallsRcvd_Type()
)
ux25StatCallsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatCallsRcvd.setStatus("mandatory")
_Ux25StatCallsSent_Type = Integer32
_Ux25StatCallsSent_Object = MibTableColumn
ux25StatCallsSent = _Ux25StatCallsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 3),
    _Ux25StatCallsSent_Type()
)
ux25StatCallsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatCallsSent.setStatus("mandatory")
_Ux25StatCallsRcvdEstab_Type = Integer32
_Ux25StatCallsRcvdEstab_Object = MibTableColumn
ux25StatCallsRcvdEstab = _Ux25StatCallsRcvdEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 4),
    _Ux25StatCallsRcvdEstab_Type()
)
ux25StatCallsRcvdEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatCallsRcvdEstab.setStatus("mandatory")
_Ux25StatCallsSentEstab_Type = Integer32
_Ux25StatCallsSentEstab_Object = MibTableColumn
ux25StatCallsSentEstab = _Ux25StatCallsSentEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 5),
    _Ux25StatCallsSentEstab_Type()
)
ux25StatCallsSentEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatCallsSentEstab.setStatus("mandatory")
_Ux25StatDataPktsRcvd_Type = Integer32
_Ux25StatDataPktsRcvd_Object = MibTableColumn
ux25StatDataPktsRcvd = _Ux25StatDataPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 6),
    _Ux25StatDataPktsRcvd_Type()
)
ux25StatDataPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatDataPktsRcvd.setStatus("mandatory")
_Ux25StatDataPktsSent_Type = Integer32
_Ux25StatDataPktsSent_Object = MibTableColumn
ux25StatDataPktsSent = _Ux25StatDataPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 7),
    _Ux25StatDataPktsSent_Type()
)
ux25StatDataPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatDataPktsSent.setStatus("mandatory")
_Ux25StatRestartsRcvd_Type = Integer32
_Ux25StatRestartsRcvd_Object = MibTableColumn
ux25StatRestartsRcvd = _Ux25StatRestartsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 8),
    _Ux25StatRestartsRcvd_Type()
)
ux25StatRestartsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRestartsRcvd.setStatus("mandatory")
_Ux25StatRestartsSent_Type = Integer32
_Ux25StatRestartsSent_Object = MibTableColumn
ux25StatRestartsSent = _Ux25StatRestartsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 9),
    _Ux25StatRestartsSent_Type()
)
ux25StatRestartsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRestartsSent.setStatus("mandatory")
_Ux25StatRcvrNotRdyRcvd_Type = Integer32
_Ux25StatRcvrNotRdyRcvd_Object = MibTableColumn
ux25StatRcvrNotRdyRcvd = _Ux25StatRcvrNotRdyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 10),
    _Ux25StatRcvrNotRdyRcvd_Type()
)
ux25StatRcvrNotRdyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRcvrNotRdyRcvd.setStatus("mandatory")
_Ux25StatRcvrNotRdySent_Type = Integer32
_Ux25StatRcvrNotRdySent_Object = MibTableColumn
ux25StatRcvrNotRdySent = _Ux25StatRcvrNotRdySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 11),
    _Ux25StatRcvrNotRdySent_Type()
)
ux25StatRcvrNotRdySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRcvrNotRdySent.setStatus("mandatory")
_Ux25StatRcvrRdyRcvd_Type = Integer32
_Ux25StatRcvrRdyRcvd_Object = MibTableColumn
ux25StatRcvrRdyRcvd = _Ux25StatRcvrRdyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 12),
    _Ux25StatRcvrRdyRcvd_Type()
)
ux25StatRcvrRdyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRcvrRdyRcvd.setStatus("mandatory")
_Ux25StatRcvrRdySent_Type = Integer32
_Ux25StatRcvrRdySent_Object = MibTableColumn
ux25StatRcvrRdySent = _Ux25StatRcvrRdySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 13),
    _Ux25StatRcvrRdySent_Type()
)
ux25StatRcvrRdySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatRcvrRdySent.setStatus("mandatory")
_Ux25StatResetsRcvd_Type = Integer32
_Ux25StatResetsRcvd_Object = MibTableColumn
ux25StatResetsRcvd = _Ux25StatResetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 14),
    _Ux25StatResetsRcvd_Type()
)
ux25StatResetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatResetsRcvd.setStatus("mandatory")
_Ux25StatResetsSent_Type = Integer32
_Ux25StatResetsSent_Object = MibTableColumn
ux25StatResetsSent = _Ux25StatResetsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 15),
    _Ux25StatResetsSent_Type()
)
ux25StatResetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatResetsSent.setStatus("mandatory")
_Ux25StatDiagPktsRcvd_Type = Integer32
_Ux25StatDiagPktsRcvd_Object = MibTableColumn
ux25StatDiagPktsRcvd = _Ux25StatDiagPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 16),
    _Ux25StatDiagPktsRcvd_Type()
)
ux25StatDiagPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatDiagPktsRcvd.setStatus("mandatory")
_Ux25StatDiagPktsSent_Type = Integer32
_Ux25StatDiagPktsSent_Object = MibTableColumn
ux25StatDiagPktsSent = _Ux25StatDiagPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 17),
    _Ux25StatDiagPktsSent_Type()
)
ux25StatDiagPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatDiagPktsSent.setStatus("mandatory")
_Ux25StatIntrptPktsRcvd_Type = Integer32
_Ux25StatIntrptPktsRcvd_Object = MibTableColumn
ux25StatIntrptPktsRcvd = _Ux25StatIntrptPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 18),
    _Ux25StatIntrptPktsRcvd_Type()
)
ux25StatIntrptPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatIntrptPktsRcvd.setStatus("mandatory")
_Ux25StatIntrptPktsSent_Type = Integer32
_Ux25StatIntrptPktsSent_Object = MibTableColumn
ux25StatIntrptPktsSent = _Ux25StatIntrptPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 19),
    _Ux25StatIntrptPktsSent_Type()
)
ux25StatIntrptPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatIntrptPktsSent.setStatus("mandatory")
_Ux25StatPVCsInDatTrnsfrState_Type = Integer32
_Ux25StatPVCsInDatTrnsfrState_Object = MibTableColumn
ux25StatPVCsInDatTrnsfrState = _Ux25StatPVCsInDatTrnsfrState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 20),
    _Ux25StatPVCsInDatTrnsfrState_Type()
)
ux25StatPVCsInDatTrnsfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatPVCsInDatTrnsfrState.setStatus("mandatory")
_Ux25StatSVCsInDatTrnsfrState_Type = Integer32
_Ux25StatSVCsInDatTrnsfrState_Object = MibTableColumn
ux25StatSVCsInDatTrnsfrState = _Ux25StatSVCsInDatTrnsfrState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 10, 11, 1, 21),
    _Ux25StatSVCsInDatTrnsfrState_Type()
)
ux25StatSVCsInDatTrnsfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ux25StatSVCsInDatTrnsfrState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UX25-MIB",
    **{"usr": usr,
       "nas": nas,
       "ux25": ux25,
       "ux25AdmnChannelTable": ux25AdmnChannelTable,
       "ux25AdmnChannelEntry": ux25AdmnChannelEntry,
       "ux25AdmnChanneIndex": ux25AdmnChanneIndex,
       "ux25AdmnNetMode": ux25AdmnNetMode,
       "ux25AdmnProtocolVersion": ux25AdmnProtocolVersion,
       "ux25AdmnInterfaceMode": ux25AdmnInterfaceMode,
       "ux25AdmnLowestPVCVal": ux25AdmnLowestPVCVal,
       "ux25AdmnHighestPVCVal": ux25AdmnHighestPVCVal,
       "ux25AdmnChannelLIC": ux25AdmnChannelLIC,
       "ux25AdmnChannelHIC": ux25AdmnChannelHIC,
       "ux25AdmnChannelLTC": ux25AdmnChannelLTC,
       "ux25AdmnChannelHTC": ux25AdmnChannelHTC,
       "ux25AdmnChannelLOC": ux25AdmnChannelLOC,
       "ux25AdmnChannelHOC": ux25AdmnChannelHOC,
       "ux25AdmnClassTable": ux25AdmnClassTable,
       "ux25AdmnClassEntry": ux25AdmnClassEntry,
       "ux25AdmnClassIndex": ux25AdmnClassIndex,
       "ux25AdmnLocMaxThruPutClass": ux25AdmnLocMaxThruPutClass,
       "ux25AdmnRemMaxThruPutClass": ux25AdmnRemMaxThruPutClass,
       "ux25AdmnLocDefThruPutClass": ux25AdmnLocDefThruPutClass,
       "ux25AdmnRemDefThruPutClass": ux25AdmnRemDefThruPutClass,
       "ux25AdmnLocMinThruPutClass": ux25AdmnLocMinThruPutClass,
       "ux25AdmnRemMinThruPutClass": ux25AdmnRemMinThruPutClass,
       "ux25AdmnThclassNegToDef": ux25AdmnThclassNegToDef,
       "ux25AdmnThclassType": ux25AdmnThclassType,
       "ux25AdmnThclassWinMap": ux25AdmnThclassWinMap,
       "ux25AdmnThclassPackMap": ux25AdmnThclassPackMap,
       "ux25AdmnPacketTable": ux25AdmnPacketTable,
       "ux25AdmnPacketEntry": ux25AdmnPacketEntry,
       "ux25AdmnPacketIndex": ux25AdmnPacketIndex,
       "ux25AdmnPktSequencing": ux25AdmnPktSequencing,
       "ux25AdmnLocMaxPktSize": ux25AdmnLocMaxPktSize,
       "ux25AdmnRemMaxPktSize": ux25AdmnRemMaxPktSize,
       "ux25AdmnLocDefPktSize": ux25AdmnLocDefPktSize,
       "ux25AdmnRemDefPktSize": ux25AdmnRemDefPktSize,
       "ux25AdmnLocMaxWinSize": ux25AdmnLocMaxWinSize,
       "ux25AdmnRemMaxWinSize": ux25AdmnRemMaxWinSize,
       "ux25AdmnLocDefWinSize": ux25AdmnLocDefWinSize,
       "ux25AdmnRemDefWinSize": ux25AdmnRemDefWinSize,
       "ux25AdmnMaxNSDULimit": ux25AdmnMaxNSDULimit,
       "ux25AdmnAccNoDiagnostic": ux25AdmnAccNoDiagnostic,
       "ux25AdmnUseDiagnosticPacket": ux25AdmnUseDiagnosticPacket,
       "ux25AdmnItutClearLen": ux25AdmnItutClearLen,
       "ux25AdmnBarDiagnosticPacket": ux25AdmnBarDiagnosticPacket,
       "ux25AdmnDiscNzDiagnostic": ux25AdmnDiscNzDiagnostic,
       "ux25AdmnAcceptHexAdd": ux25AdmnAcceptHexAdd,
       "ux25AdmnBarNonPrivilegeListen": ux25AdmnBarNonPrivilegeListen,
       "ux25AdmnIntlAddrRecognition": ux25AdmnIntlAddrRecognition,
       "ux25AdmnDnic": ux25AdmnDnic,
       "ux25AdmnIntlPrioritized": ux25AdmnIntlPrioritized,
       "ux25AdmnPrtyEncodeCtrl": ux25AdmnPrtyEncodeCtrl,
       "ux25AdmnPrtyPktForcedVal": ux25AdmnPrtyPktForcedVal,
       "ux25AdmnSrcAddrCtrl": ux25AdmnSrcAddrCtrl,
       "ux25AdmnDbitInAccept": ux25AdmnDbitInAccept,
       "ux25AdmnDbitOutAccept": ux25AdmnDbitOutAccept,
       "ux25AdmnDbitInData": ux25AdmnDbitInData,
       "ux25AdmnDbitOutData": ux25AdmnDbitOutData,
       "ux25AdmnSubscriberTable": ux25AdmnSubscriberTable,
       "ux25AdmnSubscriberEntry": ux25AdmnSubscriberEntry,
       "ux25AdmnSubscriberIndex": ux25AdmnSubscriberIndex,
       "ux25AdmnSubCugIaoa": ux25AdmnSubCugIaoa,
       "ux25AdmnSubCugPref": ux25AdmnSubCugPref,
       "ux25AdmnSubCugoa": ux25AdmnSubCugoa,
       "ux25AdmnSubCugia": ux25AdmnSubCugia,
       "ux25AdmnCugFormat": ux25AdmnCugFormat,
       "ux25AdmnBarInCug": ux25AdmnBarInCug,
       "ux25AdmnSubExtended": ux25AdmnSubExtended,
       "ux25AdmnBarExtended": ux25AdmnBarExtended,
       "ux25AdmnSubFstSelNoRstrct": ux25AdmnSubFstSelNoRstrct,
       "ux25AdmnSubFstSelWthRstrct": ux25AdmnSubFstSelWthRstrct,
       "ux25AdmnAccptRvsChrgng": ux25AdmnAccptRvsChrgng,
       "ux25AdmnSubLocChargePrevent": ux25AdmnSubLocChargePrevent,
       "ux25AdmnSubToaNpiFormat": ux25AdmnSubToaNpiFormat,
       "ux25AdmnBarToaNpiFormat": ux25AdmnBarToaNpiFormat,
       "ux25AdmnSubNuiOverride": ux25AdmnSubNuiOverride,
       "ux25AdmnBarInCall": ux25AdmnBarInCall,
       "ux25AdmnBarOutCall": ux25AdmnBarOutCall,
       "ux25AdmnTimerTable": ux25AdmnTimerTable,
       "ux25AdmnTimerEntry": ux25AdmnTimerEntry,
       "ux25AdmnTimerIndex": ux25AdmnTimerIndex,
       "ux25AdmnAckDelay": ux25AdmnAckDelay,
       "ux25AdmnRstrtTime": ux25AdmnRstrtTime,
       "ux25AdmnCallTime": ux25AdmnCallTime,
       "ux25AdmnRstTime": ux25AdmnRstTime,
       "ux25AdmnClrTime": ux25AdmnClrTime,
       "ux25AdmnWinStatTime": ux25AdmnWinStatTime,
       "ux25AdmnWinRotTime": ux25AdmnWinRotTime,
       "ux25AdmnIntrptTime": ux25AdmnIntrptTime,
       "ux25AdmnIdleValue": ux25AdmnIdleValue,
       "ux25AdmnConnectValue": ux25AdmnConnectValue,
       "ux25AdmnRstrtCnt": ux25AdmnRstrtCnt,
       "ux25AdmnRstCnt": ux25AdmnRstCnt,
       "ux25AdmnClrCnt": ux25AdmnClrCnt,
       "ux25AdmnLocalDelay": ux25AdmnLocalDelay,
       "ux25AdmnAccessDelay": ux25AdmnAccessDelay,
       "ux25OperChannelTable": ux25OperChannelTable,
       "ux25OperChannelEntry": ux25OperChannelEntry,
       "ux25OperChannelIndex": ux25OperChannelIndex,
       "ux25OperNetMode": ux25OperNetMode,
       "ux25OperProtocolVersion": ux25OperProtocolVersion,
       "ux25OperInterfaceMode": ux25OperInterfaceMode,
       "ux25OperLowestPVCVal": ux25OperLowestPVCVal,
       "ux25OperHighestPVCVal": ux25OperHighestPVCVal,
       "ux25OperChannelLIC": ux25OperChannelLIC,
       "ux25OperChannelHIC": ux25OperChannelHIC,
       "ux25OperChannelLTC": ux25OperChannelLTC,
       "ux25OperChannelHTC": ux25OperChannelHTC,
       "ux25OperChannelLOC": ux25OperChannelLOC,
       "ux25OperChannelHOC": ux25OperChannelHOC,
       "ux25OperClassTable": ux25OperClassTable,
       "ux25OperClassEntry": ux25OperClassEntry,
       "ux25OperClassIndex": ux25OperClassIndex,
       "ux25OperLocMaxThruPutClass": ux25OperLocMaxThruPutClass,
       "ux25OperRemMaxThruPutClass": ux25OperRemMaxThruPutClass,
       "ux25OperLocDefThruPutClass": ux25OperLocDefThruPutClass,
       "ux25OperRemDefThruPutClass": ux25OperRemDefThruPutClass,
       "ux25OperLocMinThruPutClass": ux25OperLocMinThruPutClass,
       "ux25OperRemMinThruPutClass": ux25OperRemMinThruPutClass,
       "ux25OperThclassNegToDef": ux25OperThclassNegToDef,
       "ux25OperThclassType": ux25OperThclassType,
       "ux25OperThclassWinMap": ux25OperThclassWinMap,
       "ux25OperThclassPackMap": ux25OperThclassPackMap,
       "ux25OperPacketTable": ux25OperPacketTable,
       "ux25OperPacketEntry": ux25OperPacketEntry,
       "ux25OperPacketIndex": ux25OperPacketIndex,
       "ux25OperPktSequencing": ux25OperPktSequencing,
       "ux25OperLocMaxPktSize": ux25OperLocMaxPktSize,
       "ux25OperRemMaxPktSize": ux25OperRemMaxPktSize,
       "ux25OperLocDefPktSize": ux25OperLocDefPktSize,
       "ux25OperRemDefPktSize": ux25OperRemDefPktSize,
       "ux25OperLocMaxWinSize": ux25OperLocMaxWinSize,
       "ux25OperRemMaxWinSize": ux25OperRemMaxWinSize,
       "ux25OperLocDefWinSize": ux25OperLocDefWinSize,
       "ux25OperRemDefWinSize": ux25OperRemDefWinSize,
       "ux25OperMaxNSDULimit": ux25OperMaxNSDULimit,
       "ux25OperAccNoDiagnostic": ux25OperAccNoDiagnostic,
       "ux25OperUseDiagnosticPacket": ux25OperUseDiagnosticPacket,
       "ux25OperItutClearLen": ux25OperItutClearLen,
       "ux25OperBarDiagnosticPacket": ux25OperBarDiagnosticPacket,
       "ux25OperDiscNzDiagnostic": ux25OperDiscNzDiagnostic,
       "ux25OperAcceptHexAdd": ux25OperAcceptHexAdd,
       "ux25OperBarNonPrivilegeListen": ux25OperBarNonPrivilegeListen,
       "ux25OperIntlAddrRecognition": ux25OperIntlAddrRecognition,
       "ux25OperDnic": ux25OperDnic,
       "ux25OperIntlPrioritized": ux25OperIntlPrioritized,
       "ux25OperPrtyEncodeCtrl": ux25OperPrtyEncodeCtrl,
       "ux25OperPrtyPktForcedVal": ux25OperPrtyPktForcedVal,
       "ux25OperSrcAddrCtrl": ux25OperSrcAddrCtrl,
       "ux25OperDbitInAccept": ux25OperDbitInAccept,
       "ux25OperDbitOutAccept": ux25OperDbitOutAccept,
       "ux25OperDbitInData": ux25OperDbitInData,
       "ux25OperDbitOutData": ux25OperDbitOutData,
       "ux25OperSubscriberTable": ux25OperSubscriberTable,
       "ux25OperSubscriberEntry": ux25OperSubscriberEntry,
       "ux25OperSubscriberIndex": ux25OperSubscriberIndex,
       "ux25OperSubCugIaoa": ux25OperSubCugIaoa,
       "ux25OperSubCugPref": ux25OperSubCugPref,
       "ux25OperSubCugoa": ux25OperSubCugoa,
       "ux25OperSubCugia": ux25OperSubCugia,
       "ux25OperCugFormat": ux25OperCugFormat,
       "ux25OperBarInCug": ux25OperBarInCug,
       "ux25OperSubExtended": ux25OperSubExtended,
       "ux25OperBarExtended": ux25OperBarExtended,
       "ux25OperSubFstSelNoRstrct": ux25OperSubFstSelNoRstrct,
       "ux25OperSubFstSelWthRstrct": ux25OperSubFstSelWthRstrct,
       "ux25OperAccptRvsChrgng": ux25OperAccptRvsChrgng,
       "ux25OperSubLocChargePrevent": ux25OperSubLocChargePrevent,
       "ux25OperSubToaNpiFormat": ux25OperSubToaNpiFormat,
       "ux25OperBarToaNpiFormat": ux25OperBarToaNpiFormat,
       "ux25OperSubNuiOverride": ux25OperSubNuiOverride,
       "ux25OperBarInCall": ux25OperBarInCall,
       "ux25OperBarOutCall": ux25OperBarOutCall,
       "ux25OperTimerTable": ux25OperTimerTable,
       "ux25OperTimerEntry": ux25OperTimerEntry,
       "ux25OperTimerIndex": ux25OperTimerIndex,
       "ux25OperAckDelay": ux25OperAckDelay,
       "ux25OperRstrtTime": ux25OperRstrtTime,
       "ux25OperCallTime": ux25OperCallTime,
       "ux25OperRstTime": ux25OperRstTime,
       "ux25OperClrTime": ux25OperClrTime,
       "ux25OperWinStatTime": ux25OperWinStatTime,
       "ux25OperWinRotTime": ux25OperWinRotTime,
       "ux25OperIntrptTime": ux25OperIntrptTime,
       "ux25OperIdleValue": ux25OperIdleValue,
       "ux25OperConnectValue": ux25OperConnectValue,
       "ux25OperRstrtCnt": ux25OperRstrtCnt,
       "ux25OperRstCnt": ux25OperRstCnt,
       "ux25OperClrCnt": ux25OperClrCnt,
       "ux25OperLocalDelay": ux25OperLocalDelay,
       "ux25OperAccessDelay": ux25OperAccessDelay,
       "ux25StatTable": ux25StatTable,
       "ux25StatEntry": ux25StatEntry,
       "ux25StatIndex": ux25StatIndex,
       "ux25StatCallsRcvd": ux25StatCallsRcvd,
       "ux25StatCallsSent": ux25StatCallsSent,
       "ux25StatCallsRcvdEstab": ux25StatCallsRcvdEstab,
       "ux25StatCallsSentEstab": ux25StatCallsSentEstab,
       "ux25StatDataPktsRcvd": ux25StatDataPktsRcvd,
       "ux25StatDataPktsSent": ux25StatDataPktsSent,
       "ux25StatRestartsRcvd": ux25StatRestartsRcvd,
       "ux25StatRestartsSent": ux25StatRestartsSent,
       "ux25StatRcvrNotRdyRcvd": ux25StatRcvrNotRdyRcvd,
       "ux25StatRcvrNotRdySent": ux25StatRcvrNotRdySent,
       "ux25StatRcvrRdyRcvd": ux25StatRcvrRdyRcvd,
       "ux25StatRcvrRdySent": ux25StatRcvrRdySent,
       "ux25StatResetsRcvd": ux25StatResetsRcvd,
       "ux25StatResetsSent": ux25StatResetsSent,
       "ux25StatDiagPktsRcvd": ux25StatDiagPktsRcvd,
       "ux25StatDiagPktsSent": ux25StatDiagPktsSent,
       "ux25StatIntrptPktsRcvd": ux25StatIntrptPktsRcvd,
       "ux25StatIntrptPktsSent": ux25StatIntrptPktsSent,
       "ux25StatPVCsInDatTrnsfrState": ux25StatPVCsInDatTrnsfrState,
       "ux25StatSVCsInDatTrnsfrState": ux25StatSVCsInDatTrnsfrState}
)
