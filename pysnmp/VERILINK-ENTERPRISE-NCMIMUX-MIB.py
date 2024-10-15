# SNMP MIB module (VERILINK-ENTERPRISE-NCMIMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMIMUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(ncm_imux,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-imux")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmimuxConfigTable_Object = MibTable
ncmimuxConfigTable = _NcmimuxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000)
)
if mibBuilder.loadTexts:
    ncmimuxConfigTable.setStatus("mandatory")
_NcmimuxConfigEntry_Object = MibTableRow
ncmimuxConfigEntry = _NcmimuxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1)
)
ncmimuxConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxLineIndex"),
)
if mibBuilder.loadTexts:
    ncmimuxConfigEntry.setStatus("mandatory")


class _NcmimuxNIDConfigIndex_Type(Integer32):
    """Custom type ncmimuxNIDConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxNIDConfigIndex_Type.__name__ = "Integer32"
_NcmimuxNIDConfigIndex_Object = MibTableColumn
ncmimuxNIDConfigIndex = _NcmimuxNIDConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 1),
    _NcmimuxNIDConfigIndex_Type()
)
ncmimuxNIDConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxNIDConfigIndex.setStatus("mandatory")


class _NcmimuxLineIndex_Type(Integer32):
    """Custom type ncmimuxLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxLineIndex_Type.__name__ = "Integer32"
_NcmimuxLineIndex_Object = MibTableColumn
ncmimuxLineIndex = _NcmimuxLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 2),
    _NcmimuxLineIndex_Type()
)
ncmimuxLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxLineIndex.setStatus("mandatory")


class _NcmimuxEndId_Type(Integer32):
    """Custom type ncmimuxEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmimuxEndId_Type.__name__ = "Integer32"
_NcmimuxEndId_Object = MibTableColumn
ncmimuxEndId = _NcmimuxEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 3),
    _NcmimuxEndId_Type()
)
ncmimuxEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxEndId.setStatus("mandatory")


class _NcmimuxIfIndex_Type(Integer32):
    """Custom type ncmimuxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxIfIndex_Type.__name__ = "Integer32"
_NcmimuxIfIndex_Object = MibTableColumn
ncmimuxIfIndex = _NcmimuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 4),
    _NcmimuxIfIndex_Type()
)
ncmimuxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxIfIndex.setStatus("mandatory")


class _NcmimuxBkplaneBusSelect_Type(Integer32):
    """Custom type ncmimuxBkplaneBusSelect based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bus-AAAAAAAA", 1),
          ("bus-AABBAABB", 2),
          ("bus-AACCAACC", 3),
          ("bus-AADDAADD", 4),
          ("bus-BBAABBAA", 5),
          ("bus-BBBBBBBB", 6),
          ("bus-BBCCBBCC", 7),
          ("bus-BBDDBBDD", 8),
          ("bus-CCAACCAA", 9),
          ("bus-CCBBCCBB", 10),
          ("bus-CCCCCCCC", 11),
          ("bus-CCDDCCDD", 12),
          ("bus-DDAADDAA", 13),
          ("bus-DDBBDDBB", 14),
          ("bus-DDCCDDCC", 15),
          ("bus-DDDDDDDD", 16),
          ("bus-EEXXEEXX", 18),
          ("bus-XXEEXXEE", 17))
    )


_NcmimuxBkplaneBusSelect_Type.__name__ = "Integer32"
_NcmimuxBkplaneBusSelect_Object = MibTableColumn
ncmimuxBkplaneBusSelect = _NcmimuxBkplaneBusSelect_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 5),
    _NcmimuxBkplaneBusSelect_Type()
)
ncmimuxBkplaneBusSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxBkplaneBusSelect.setStatus("mandatory")


class _NcmimuxCarrierLineRate_Type(Integer32):
    """Custom type ncmimuxCarrierLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1-rate", 2),
          ("t1-rate", 1))
    )


_NcmimuxCarrierLineRate_Type.__name__ = "Integer32"
_NcmimuxCarrierLineRate_Object = MibTableColumn
ncmimuxCarrierLineRate = _NcmimuxCarrierLineRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 6),
    _NcmimuxCarrierLineRate_Type()
)
ncmimuxCarrierLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxCarrierLineRate.setStatus("mandatory")


class _NcmimuxCarrierLinesEqp_Type(DisplayString):
    """Custom type ncmimuxCarrierLinesEqp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxCarrierLinesEqp_Type.__name__ = "DisplayString"
_NcmimuxCarrierLinesEqp_Object = MibTableColumn
ncmimuxCarrierLinesEqp = _NcmimuxCarrierLinesEqp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 7),
    _NcmimuxCarrierLinesEqp_Type()
)
ncmimuxCarrierLinesEqp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxCarrierLinesEqp.setStatus("mandatory")


class _NcmimuxChanneling_Type(Integer32):
    """Custom type ncmimuxChanneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode-56k", 2),
          ("mode-64k", 1))
    )


_NcmimuxChanneling_Type.__name__ = "Integer32"
_NcmimuxChanneling_Object = MibTableColumn
ncmimuxChanneling = _NcmimuxChanneling_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 8),
    _NcmimuxChanneling_Type()
)
ncmimuxChanneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxChanneling.setStatus("mandatory")


class _NcmimuxDTEClkTransmit_Type(Integer32):
    """Custom type ncmimuxDTEClkTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_NcmimuxDTEClkTransmit_Type.__name__ = "Integer32"
_NcmimuxDTEClkTransmit_Object = MibTableColumn
ncmimuxDTEClkTransmit = _NcmimuxDTEClkTransmit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 9),
    _NcmimuxDTEClkTransmit_Type()
)
ncmimuxDTEClkTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDTEClkTransmit.setStatus("mandatory")


class _NcmimuxDTEClkRecv_Type(Integer32):
    """Custom type ncmimuxDTEClkRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_NcmimuxDTEClkRecv_Type.__name__ = "Integer32"
_NcmimuxDTEClkRecv_Object = MibTableColumn
ncmimuxDTEClkRecv = _NcmimuxDTEClkRecv_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 10),
    _NcmimuxDTEClkRecv_Type()
)
ncmimuxDTEClkRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDTEClkRecv.setStatus("mandatory")


class _NcmimuxDTEClkRefern_Type(Integer32):
    """Custom type ncmimuxDTEClkRefern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_NcmimuxDTEClkRefern_Type.__name__ = "Integer32"
_NcmimuxDTEClkRefern_Object = MibTableColumn
ncmimuxDTEClkRefern = _NcmimuxDTEClkRefern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 11),
    _NcmimuxDTEClkRefern_Type()
)
ncmimuxDTEClkRefern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDTEClkRefern.setStatus("mandatory")


class _NcmimuxDTEMode_Type(Integer32):
    """Custom type ncmimuxDTEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_NcmimuxDTEMode_Type.__name__ = "Integer32"
_NcmimuxDTEMode_Object = MibTableColumn
ncmimuxDTEMode = _NcmimuxDTEMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 12),
    _NcmimuxDTEMode_Type()
)
ncmimuxDTEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDTEMode.setStatus("mandatory")


class _NcmimuxDSR_Type(Integer32):
    """Custom type ncmimuxDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NcmimuxDSR_Type.__name__ = "Integer32"
_NcmimuxDSR_Object = MibTableColumn
ncmimuxDSR = _NcmimuxDSR_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 13),
    _NcmimuxDSR_Type()
)
ncmimuxDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDSR.setStatus("mandatory")


class _NcmimuxTM_Type(Integer32):
    """Custom type ncmimuxTM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NcmimuxTM_Type.__name__ = "Integer32"
_NcmimuxTM_Object = MibTableColumn
ncmimuxTM = _NcmimuxTM_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 14),
    _NcmimuxTM_Type()
)
ncmimuxTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxTM.setStatus("mandatory")


class _NcmimuxCTS_Type(Integer32):
    """Custom type ncmimuxCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NcmimuxCTS_Type.__name__ = "Integer32"
_NcmimuxCTS_Object = MibTableColumn
ncmimuxCTS = _NcmimuxCTS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 15),
    _NcmimuxCTS_Type()
)
ncmimuxCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxCTS.setStatus("mandatory")


class _NcmimuxDCD_Type(Integer32):
    """Custom type ncmimuxDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NcmimuxDCD_Type.__name__ = "Integer32"
_NcmimuxDCD_Object = MibTableColumn
ncmimuxDCD = _NcmimuxDCD_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 16),
    _NcmimuxDCD_Type()
)
ncmimuxDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxDCD.setStatus("mandatory")


class _NcmimuxRI_Type(Integer32):
    """Custom type ncmimuxRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NcmimuxRI_Type.__name__ = "Integer32"
_NcmimuxRI_Object = MibTableColumn
ncmimuxRI = _NcmimuxRI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 17),
    _NcmimuxRI_Type()
)
ncmimuxRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxRI.setStatus("mandatory")


class _NcmimuxSnapType_Type(Integer32):
    """Custom type ncmimuxSnapType based on Integer32"""
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
        *(("eia530", 5),
          ("eia530a", 4),
          ("hssi", 2),
          ("rs449", 6),
          ("unknown", 1),
          ("v35", 3))
    )


_NcmimuxSnapType_Type.__name__ = "Integer32"
_NcmimuxSnapType_Object = MibTableColumn
ncmimuxSnapType = _NcmimuxSnapType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 18),
    _NcmimuxSnapType_Type()
)
ncmimuxSnapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxSnapType.setStatus("mandatory")
_NcmimuxQuadSlot_Type = Integer32
_NcmimuxQuadSlot_Object = MibTableColumn
ncmimuxQuadSlot = _NcmimuxQuadSlot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 19),
    _NcmimuxQuadSlot_Type()
)
ncmimuxQuadSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxQuadSlot.setStatus("mandatory")
_NcmimuxStatusTable_Object = MibTable
ncmimuxStatusTable = _NcmimuxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001)
)
if mibBuilder.loadTexts:
    ncmimuxStatusTable.setStatus("mandatory")
_NcmimuxStatusEntry_Object = MibTableRow
ncmimuxStatusEntry = _NcmimuxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1)
)
ncmimuxStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDStatusIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmimuxStatusEntry.setStatus("mandatory")


class _NcmimuxNIDStatusIndex_Type(Integer32):
    """Custom type ncmimuxNIDStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxNIDStatusIndex_Type.__name__ = "Integer32"
_NcmimuxNIDStatusIndex_Object = MibTableColumn
ncmimuxNIDStatusIndex = _NcmimuxNIDStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 1),
    _NcmimuxNIDStatusIndex_Type()
)
ncmimuxNIDStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxNIDStatusIndex.setStatus("mandatory")


class _NcmimuxStatusIndex_Type(Integer32):
    """Custom type ncmimuxStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxStatusIndex_Type.__name__ = "Integer32"
_NcmimuxStatusIndex_Object = MibTableColumn
ncmimuxStatusIndex = _NcmimuxStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 2),
    _NcmimuxStatusIndex_Type()
)
ncmimuxStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxStatusIndex.setStatus("mandatory")


class _NcmimuxStatEndId_Type(Integer32):
    """Custom type ncmimuxStatEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmimuxStatEndId_Type.__name__ = "Integer32"
_NcmimuxStatEndId_Object = MibTableColumn
ncmimuxStatEndId = _NcmimuxStatEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 3),
    _NcmimuxStatEndId_Type()
)
ncmimuxStatEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxStatEndId.setStatus("mandatory")


class _NcmimuxLinesEqp_Type(DisplayString):
    """Custom type ncmimuxLinesEqp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxLinesEqp_Type.__name__ = "DisplayString"
_NcmimuxLinesEqp_Object = MibTableColumn
ncmimuxLinesEqp = _NcmimuxLinesEqp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 4),
    _NcmimuxLinesEqp_Type()
)
ncmimuxLinesEqp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxLinesEqp.setStatus("mandatory")


class _NcmimuxLinesStat_Type(DisplayString):
    """Custom type ncmimuxLinesStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxLinesStat_Type.__name__ = "DisplayString"
_NcmimuxLinesStat_Object = MibTableColumn
ncmimuxLinesStat = _NcmimuxLinesStat_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 5),
    _NcmimuxLinesStat_Type()
)
ncmimuxLinesStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxLinesStat.setStatus("mandatory")


class _NcmimuxFrameStatus_Type(DisplayString):
    """Custom type ncmimuxFrameStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxFrameStatus_Type.__name__ = "DisplayString"
_NcmimuxFrameStatus_Object = MibTableColumn
ncmimuxFrameStatus = _NcmimuxFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 6),
    _NcmimuxFrameStatus_Type()
)
ncmimuxFrameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxFrameStatus.setStatus("mandatory")


class _NcmimuxCTSStatus_Type(DisplayString):
    """Custom type ncmimuxCTSStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxCTSStatus_Type.__name__ = "DisplayString"
_NcmimuxCTSStatus_Object = MibTableColumn
ncmimuxCTSStatus = _NcmimuxCTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 7),
    _NcmimuxCTSStatus_Type()
)
ncmimuxCTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxCTSStatus.setStatus("mandatory")


class _NcmimuxCRCStatus_Type(DisplayString):
    """Custom type ncmimuxCRCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxCRCStatus_Type.__name__ = "DisplayString"
_NcmimuxCRCStatus_Object = MibTableColumn
ncmimuxCRCStatus = _NcmimuxCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 8),
    _NcmimuxCRCStatus_Type()
)
ncmimuxCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxCRCStatus.setStatus("mandatory")


class _NcmimuxFarEndCRCStatus_Type(DisplayString):
    """Custom type ncmimuxFarEndCRCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmimuxFarEndCRCStatus_Type.__name__ = "DisplayString"
_NcmimuxFarEndCRCStatus_Object = MibTableColumn
ncmimuxFarEndCRCStatus = _NcmimuxFarEndCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 9),
    _NcmimuxFarEndCRCStatus_Type()
)
ncmimuxFarEndCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxFarEndCRCStatus.setStatus("mandatory")
_NcmimuxDataValidStatus_Type = Integer32
_NcmimuxDataValidStatus_Object = MibTableColumn
ncmimuxDataValidStatus = _NcmimuxDataValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 10),
    _NcmimuxDataValidStatus_Type()
)
ncmimuxDataValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxDataValidStatus.setStatus("mandatory")


class _NcmimuxNetworkAlarm_Type(Integer32):
    """Custom type ncmimuxNetworkAlarm based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("flashing-Green", 6),
          ("flashing-Green-Yellow", 9),
          ("flashing-Red", 5),
          ("flashing-Red-Green", 8),
          ("flashing-Yellow", 7),
          ("flashing-Yellow-Red", 10),
          ("green", 3),
          ("off", 1),
          ("red", 2),
          ("yellow", 4))
    )


_NcmimuxNetworkAlarm_Type.__name__ = "Integer32"
_NcmimuxNetworkAlarm_Object = MibTableColumn
ncmimuxNetworkAlarm = _NcmimuxNetworkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 11),
    _NcmimuxNetworkAlarm_Type()
)
ncmimuxNetworkAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxNetworkAlarm.setStatus("mandatory")


class _NcmimuxAlarmLED_Type(Integer32):
    """Custom type ncmimuxAlarmLED based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("flashing-Green", 6),
          ("flashing-Green-Yellow", 9),
          ("flashing-Red", 5),
          ("flashing-Red-Green", 8),
          ("flashing-Yellow", 7),
          ("flashing-Yellow-Red", 10),
          ("green", 3),
          ("off", 1),
          ("red", 2),
          ("yellow", 4))
    )


_NcmimuxAlarmLED_Type.__name__ = "Integer32"
_NcmimuxAlarmLED_Object = MibTableColumn
ncmimuxAlarmLED = _NcmimuxAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 12),
    _NcmimuxAlarmLED_Type()
)
ncmimuxAlarmLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxAlarmLED.setStatus("mandatory")


class _NcmimuxEventMessages_Type(Integer32):
    """Custom type ncmimuxEventMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxEventMessages_Type.__name__ = "Integer32"
_NcmimuxEventMessages_Object = MibTableColumn
ncmimuxEventMessages = _NcmimuxEventMessages_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 13),
    _NcmimuxEventMessages_Type()
)
ncmimuxEventMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxEventMessages.setStatus("mandatory")
_NcmimuxControlTable_Object = MibTable
ncmimuxControlTable = _NcmimuxControlTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002)
)
if mibBuilder.loadTexts:
    ncmimuxControlTable.setStatus("mandatory")
_NcmimuxControlEntry_Object = MibTableRow
ncmimuxControlEntry = _NcmimuxControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1)
)
ncmimuxControlEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDControlIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxControlIndex"),
)
if mibBuilder.loadTexts:
    ncmimuxControlEntry.setStatus("mandatory")


class _NcmimuxNIDControlIndex_Type(Integer32):
    """Custom type ncmimuxNIDControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxNIDControlIndex_Type.__name__ = "Integer32"
_NcmimuxNIDControlIndex_Object = MibTableColumn
ncmimuxNIDControlIndex = _NcmimuxNIDControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 1),
    _NcmimuxNIDControlIndex_Type()
)
ncmimuxNIDControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxNIDControlIndex.setStatus("mandatory")


class _NcmimuxControlIndex_Type(Integer32):
    """Custom type ncmimuxControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxControlIndex_Type.__name__ = "Integer32"
_NcmimuxControlIndex_Object = MibTableColumn
ncmimuxControlIndex = _NcmimuxControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 2),
    _NcmimuxControlIndex_Type()
)
ncmimuxControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxControlIndex.setStatus("mandatory")


class _NcmimuxCntEndId_Type(Integer32):
    """Custom type ncmimuxCntEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmimuxCntEndId_Type.__name__ = "Integer32"
_NcmimuxCntEndId_Object = MibTableColumn
ncmimuxCntEndId = _NcmimuxCntEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 3),
    _NcmimuxCntEndId_Type()
)
ncmimuxCntEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxCntEndId.setStatus("mandatory")


class _NcmimuxLoopback_Type(Integer32):
    """Custom type ncmimuxLoopback based on Integer32"""
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
        *(("actv-ELB", 2),
          ("actv-ELB-AND-PLB", 4),
          ("actv-PLB", 3),
          ("deactv-ELB", 5),
          ("deactv-PLB", 6),
          ("no-ELB-AND-PLB", 1))
    )


_NcmimuxLoopback_Type.__name__ = "Integer32"
_NcmimuxLoopback_Object = MibTableColumn
ncmimuxLoopback = _NcmimuxLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 4),
    _NcmimuxLoopback_Type()
)
ncmimuxLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxLoopback.setStatus("mandatory")


class _NcmimuxAISPattern_Type(Integer32):
    """Custom type ncmimuxAISPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all-Ones", 2),
          ("all-Zeros", 3),
          ("disable", 1))
    )


_NcmimuxAISPattern_Type.__name__ = "Integer32"
_NcmimuxAISPattern_Object = MibTableColumn
ncmimuxAISPattern = _NcmimuxAISPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 5),
    _NcmimuxAISPattern_Type()
)
ncmimuxAISPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmimuxAISPattern.setStatus("mandatory")


class _NcmimuxTestPattern_Type(Integer32):
    """Custom type ncmimuxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("inv-Pat-127", 3),
          ("pat-127", 2))
    )


_NcmimuxTestPattern_Type.__name__ = "Integer32"
_NcmimuxTestPattern_Object = MibTableColumn
ncmimuxTestPattern = _NcmimuxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 6),
    _NcmimuxTestPattern_Type()
)
ncmimuxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxTestPattern.setStatus("mandatory")
_NcmimuxDTEStatTable_Object = MibTable
ncmimuxDTEStatTable = _NcmimuxDTEStatTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003)
)
if mibBuilder.loadTexts:
    ncmimuxDTEStatTable.setStatus("mandatory")
_NcmimuxDTEStatEntry_Object = MibTableRow
ncmimuxDTEStatEntry = _NcmimuxDTEStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1)
)
ncmimuxDTEStatEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDDTEStatIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxDTEStatIndex"),
)
if mibBuilder.loadTexts:
    ncmimuxDTEStatEntry.setStatus("mandatory")


class _NcmimuxNIDDTEStatIndex_Type(Integer32):
    """Custom type ncmimuxNIDDTEStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxNIDDTEStatIndex_Type.__name__ = "Integer32"
_NcmimuxNIDDTEStatIndex_Object = MibTableColumn
ncmimuxNIDDTEStatIndex = _NcmimuxNIDDTEStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 1),
    _NcmimuxNIDDTEStatIndex_Type()
)
ncmimuxNIDDTEStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxNIDDTEStatIndex.setStatus("mandatory")


class _NcmimuxDTEStatIndex_Type(Integer32):
    """Custom type ncmimuxDTEStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmimuxDTEStatIndex_Type.__name__ = "Integer32"
_NcmimuxDTEStatIndex_Object = MibTableColumn
ncmimuxDTEStatIndex = _NcmimuxDTEStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 2),
    _NcmimuxDTEStatIndex_Type()
)
ncmimuxDTEStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxDTEStatIndex.setStatus("mandatory")


class _NcmimuxDTEStatReg_Type(Integer32):
    """Custom type ncmimuxDTEStatReg based on Integer32"""
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
        *(("hSSI-DTR", 1),
          ("hSSI-Loopback-A", 2),
          ("hSSI-Loopback-B", 3),
          ("v35-RTS", 4),
          ("v54-LL", 6),
          ("v54-RL", 5))
    )


_NcmimuxDTEStatReg_Type.__name__ = "Integer32"
_NcmimuxDTEStatReg_Object = MibTableColumn
ncmimuxDTEStatReg = _NcmimuxDTEStatReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 3),
    _NcmimuxDTEStatReg_Type()
)
ncmimuxDTEStatReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxDTEStatReg.setStatus("mandatory")


class _NcmimuxDTEStatLPBK_Type(Integer32):
    """Custom type ncmimuxDTEStatLPBK based on Integer32"""
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
        *(("pRBS", 5),
          ("v35-LoopDown-Errors", 4),
          ("v54-LoopDown", 3),
          ("v54-LoopUp", 1),
          ("v54-Ptrn-Loop-Errors", 2))
    )


_NcmimuxDTEStatLPBK_Type.__name__ = "Integer32"
_NcmimuxDTEStatLPBK_Object = MibTableColumn
ncmimuxDTEStatLPBK = _NcmimuxDTEStatLPBK_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 4),
    _NcmimuxDTEStatLPBK_Type()
)
ncmimuxDTEStatLPBK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxDTEStatLPBK.setStatus("mandatory")


class _NcmimuxDTEStatAlarm_Type(Integer32):
    """Custom type ncmimuxDTEStatAlarm based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("flashing-Green", 6),
          ("flashing-Green-Yellow", 9),
          ("flashing-Red", 5),
          ("flashing-Red-Green", 8),
          ("flashing-Yellow", 7),
          ("flashing-Yellow-Red", 10),
          ("green", 3),
          ("off", 1),
          ("red", 2),
          ("yellow", 4))
    )


_NcmimuxDTEStatAlarm_Type.__name__ = "Integer32"
_NcmimuxDTEStatAlarm_Object = MibTableColumn
ncmimuxDTEStatAlarm = _NcmimuxDTEStatAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 5),
    _NcmimuxDTEStatAlarm_Type()
)
ncmimuxDTEStatAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmimuxDTEStatAlarm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMIMUX-MIB",
    **{"ncmimuxConfigTable": ncmimuxConfigTable,
       "ncmimuxConfigEntry": ncmimuxConfigEntry,
       "ncmimuxNIDConfigIndex": ncmimuxNIDConfigIndex,
       "ncmimuxLineIndex": ncmimuxLineIndex,
       "ncmimuxEndId": ncmimuxEndId,
       "ncmimuxIfIndex": ncmimuxIfIndex,
       "ncmimuxBkplaneBusSelect": ncmimuxBkplaneBusSelect,
       "ncmimuxCarrierLineRate": ncmimuxCarrierLineRate,
       "ncmimuxCarrierLinesEqp": ncmimuxCarrierLinesEqp,
       "ncmimuxChanneling": ncmimuxChanneling,
       "ncmimuxDTEClkTransmit": ncmimuxDTEClkTransmit,
       "ncmimuxDTEClkRecv": ncmimuxDTEClkRecv,
       "ncmimuxDTEClkRefern": ncmimuxDTEClkRefern,
       "ncmimuxDTEMode": ncmimuxDTEMode,
       "ncmimuxDSR": ncmimuxDSR,
       "ncmimuxTM": ncmimuxTM,
       "ncmimuxCTS": ncmimuxCTS,
       "ncmimuxDCD": ncmimuxDCD,
       "ncmimuxRI": ncmimuxRI,
       "ncmimuxSnapType": ncmimuxSnapType,
       "ncmimuxQuadSlot": ncmimuxQuadSlot,
       "ncmimuxStatusTable": ncmimuxStatusTable,
       "ncmimuxStatusEntry": ncmimuxStatusEntry,
       "ncmimuxNIDStatusIndex": ncmimuxNIDStatusIndex,
       "ncmimuxStatusIndex": ncmimuxStatusIndex,
       "ncmimuxStatEndId": ncmimuxStatEndId,
       "ncmimuxLinesEqp": ncmimuxLinesEqp,
       "ncmimuxLinesStat": ncmimuxLinesStat,
       "ncmimuxFrameStatus": ncmimuxFrameStatus,
       "ncmimuxCTSStatus": ncmimuxCTSStatus,
       "ncmimuxCRCStatus": ncmimuxCRCStatus,
       "ncmimuxFarEndCRCStatus": ncmimuxFarEndCRCStatus,
       "ncmimuxDataValidStatus": ncmimuxDataValidStatus,
       "ncmimuxNetworkAlarm": ncmimuxNetworkAlarm,
       "ncmimuxAlarmLED": ncmimuxAlarmLED,
       "ncmimuxEventMessages": ncmimuxEventMessages,
       "ncmimuxControlTable": ncmimuxControlTable,
       "ncmimuxControlEntry": ncmimuxControlEntry,
       "ncmimuxNIDControlIndex": ncmimuxNIDControlIndex,
       "ncmimuxControlIndex": ncmimuxControlIndex,
       "ncmimuxCntEndId": ncmimuxCntEndId,
       "ncmimuxLoopback": ncmimuxLoopback,
       "ncmimuxAISPattern": ncmimuxAISPattern,
       "ncmimuxTestPattern": ncmimuxTestPattern,
       "ncmimuxDTEStatTable": ncmimuxDTEStatTable,
       "ncmimuxDTEStatEntry": ncmimuxDTEStatEntry,
       "ncmimuxNIDDTEStatIndex": ncmimuxNIDDTEStatIndex,
       "ncmimuxDTEStatIndex": ncmimuxDTEStatIndex,
       "ncmimuxDTEStatReg": ncmimuxDTEStatReg,
       "ncmimuxDTEStatLPBK": ncmimuxDTEStatLPBK,
       "ncmimuxDTEStatAlarm": ncmimuxDTEStatAlarm}
)
