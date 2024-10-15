# SNMP MIB module (VERILINK-ENTERPRISE-NCMDS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMDS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:12 2024
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

(ncm_ds3,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-ds3")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmhdmDs3PortTable_Object = MibTable
ncmhdmDs3PortTable = _NcmhdmDs3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000)
)
if mibBuilder.loadTexts:
    ncmhdmDs3PortTable.setStatus("mandatory")
_NcmhdmDs3PortEntry_Object = MibTableRow
ncmhdmDs3PortEntry = _NcmhdmDs3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1)
)
ncmhdmDs3PortEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmDs3PortNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmDs3PortIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmDs3PortEntry.setStatus("mandatory")


class _NcmhdmDs3PortNIDIndex_Type(Integer32):
    """Custom type ncmhdmDs3PortNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmDs3PortNIDIndex_Type.__name__ = "Integer32"
_NcmhdmDs3PortNIDIndex_Object = MibTableColumn
ncmhdmDs3PortNIDIndex = _NcmhdmDs3PortNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 1),
    _NcmhdmDs3PortNIDIndex_Type()
)
ncmhdmDs3PortNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3PortNIDIndex.setStatus("mandatory")


class _NcmhdmDs3PortIndex_Type(Integer32):
    """Custom type ncmhdmDs3PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmDs3PortIndex_Type.__name__ = "Integer32"
_NcmhdmDs3PortIndex_Object = MibTableColumn
ncmhdmDs3PortIndex = _NcmhdmDs3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 2),
    _NcmhdmDs3PortIndex_Type()
)
ncmhdmDs3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3PortIndex.setStatus("mandatory")


class _NcmhdmDs3PerfControl_Type(Integer32):
    """Custom type ncmhdmDs3PerfControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3PerfControl_Type.__name__ = "Integer32"
_NcmhdmDs3PerfControl_Object = MibTableColumn
ncmhdmDs3PerfControl = _NcmhdmDs3PerfControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 3),
    _NcmhdmDs3PerfControl_Type()
)
ncmhdmDs3PerfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3PerfControl.setStatus("mandatory")


class _NcmhdmDs3LBOSelection_Type(Integer32):
    """Custom type ncmhdmDs3LBOSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lONG-CABLE", 2),
          ("nORMAL-CABLE", 1))
    )


_NcmhdmDs3LBOSelection_Type.__name__ = "Integer32"
_NcmhdmDs3LBOSelection_Object = MibTableColumn
ncmhdmDs3LBOSelection = _NcmhdmDs3LBOSelection_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 4),
    _NcmhdmDs3LBOSelection_Type()
)
ncmhdmDs3LBOSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3LBOSelection.setStatus("mandatory")


class _NcmhdmDs3DataRateMode_Type(Integer32):
    """Custom type ncmhdmDs3DataRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both-NearEndORFarEnd", 2),
          ("not-applicable", 3),
          ("only-NearEnd", 1))
    )


_NcmhdmDs3DataRateMode_Type.__name__ = "Integer32"
_NcmhdmDs3DataRateMode_Object = MibTableColumn
ncmhdmDs3DataRateMode = _NcmhdmDs3DataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 5),
    _NcmhdmDs3DataRateMode_Type()
)
ncmhdmDs3DataRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3DataRateMode.setStatus("mandatory")
_NcmhdmDs3Rate_Type = Integer32
_NcmhdmDs3Rate_Object = MibTableColumn
ncmhdmDs3Rate = _NcmhdmDs3Rate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 6),
    _NcmhdmDs3Rate_Type()
)
ncmhdmDs3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3Rate.setStatus("mandatory")


class _NcmhdmDs3LineType_Type(Integer32):
    """Custom type ncmhdmDs3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dSX3CBitParity", 4),
          ("dsx3M13", 2))
    )


_NcmhdmDs3LineType_Type.__name__ = "Integer32"
_NcmhdmDs3LineType_Object = MibTableColumn
ncmhdmDs3LineType = _NcmhdmDs3LineType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 7),
    _NcmhdmDs3LineType_Type()
)
ncmhdmDs3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3LineType.setStatus("mandatory")


class _NcmhdmDs3LineCode_Type(Integer32):
    """Custom type ncmhdmDs3LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dSX3CB3ZS", 2)
    )


_NcmhdmDs3LineCode_Type.__name__ = "Integer32"
_NcmhdmDs3LineCode_Object = MibTableColumn
ncmhdmDs3LineCode = _NcmhdmDs3LineCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 8),
    _NcmhdmDs3LineCode_Type()
)
ncmhdmDs3LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3LineCode.setStatus("mandatory")


class _NcmhdmDs3AISCBit_Type(Integer32):
    """Custom type ncmhdmDs3AISCBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("aISCBit", 1)
    )


_NcmhdmDs3AISCBit_Type.__name__ = "Integer32"
_NcmhdmDs3AISCBit_Object = MibTableColumn
ncmhdmDs3AISCBit = _NcmhdmDs3AISCBit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 9),
    _NcmhdmDs3AISCBit_Type()
)
ncmhdmDs3AISCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3AISCBit.setStatus("mandatory")


class _NcmhdmDs3EquipCode_Type(DisplayString):
    """Custom type ncmhdmDs3EquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NcmhdmDs3EquipCode_Type.__name__ = "DisplayString"
_NcmhdmDs3EquipCode_Object = MibTableColumn
ncmhdmDs3EquipCode = _NcmhdmDs3EquipCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 10),
    _NcmhdmDs3EquipCode_Type()
)
ncmhdmDs3EquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3EquipCode.setStatus("mandatory")


class _NcmhdmDs3LocationIDCode_Type(DisplayString):
    """Custom type ncmhdmDs3LocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_NcmhdmDs3LocationIDCode_Type.__name__ = "DisplayString"
_NcmhdmDs3LocationIDCode_Object = MibTableColumn
ncmhdmDs3LocationIDCode = _NcmhdmDs3LocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 11),
    _NcmhdmDs3LocationIDCode_Type()
)
ncmhdmDs3LocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3LocationIDCode.setStatus("mandatory")


class _NcmhdmDs3FrameIDCode_Type(DisplayString):
    """Custom type ncmhdmDs3FrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NcmhdmDs3FrameIDCode_Type.__name__ = "DisplayString"
_NcmhdmDs3FrameIDCode_Object = MibTableColumn
ncmhdmDs3FrameIDCode = _NcmhdmDs3FrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 12),
    _NcmhdmDs3FrameIDCode_Type()
)
ncmhdmDs3FrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3FrameIDCode.setStatus("mandatory")


class _NcmhdmDs3UnitCode_Type(DisplayString):
    """Custom type ncmhdmDs3UnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_NcmhdmDs3UnitCode_Type.__name__ = "DisplayString"
_NcmhdmDs3UnitCode_Object = MibTableColumn
ncmhdmDs3UnitCode = _NcmhdmDs3UnitCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 13),
    _NcmhdmDs3UnitCode_Type()
)
ncmhdmDs3UnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3UnitCode.setStatus("mandatory")


class _NcmhdmDs3FacilityIDCode_Type(DisplayString):
    """Custom type ncmhdmDs3FacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_NcmhdmDs3FacilityIDCode_Type.__name__ = "DisplayString"
_NcmhdmDs3FacilityIDCode_Object = MibTableColumn
ncmhdmDs3FacilityIDCode = _NcmhdmDs3FacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 14),
    _NcmhdmDs3FacilityIDCode_Type()
)
ncmhdmDs3FacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3FacilityIDCode.setStatus("mandatory")


class _NcmhdmDs3PortIdCode_Type(DisplayString):
    """Custom type ncmhdmDs3PortIdCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_NcmhdmDs3PortIdCode_Type.__name__ = "DisplayString"
_NcmhdmDs3PortIdCode_Object = MibTableColumn
ncmhdmDs3PortIdCode = _NcmhdmDs3PortIdCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 15),
    _NcmhdmDs3PortIdCode_Type()
)
ncmhdmDs3PortIdCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3PortIdCode.setStatus("mandatory")


class _NcmhdmDs3CircuitID_Type(DisplayString):
    """Custom type ncmhdmDs3CircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_NcmhdmDs3CircuitID_Type.__name__ = "DisplayString"
_NcmhdmDs3CircuitID_Object = MibTableColumn
ncmhdmDs3CircuitID = _NcmhdmDs3CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 16),
    _NcmhdmDs3CircuitID_Type()
)
ncmhdmDs3CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3CircuitID.setStatus("mandatory")


class _NcmhdmDs3GenIDCode_Type(DisplayString):
    """Custom type ncmhdmDs3GenIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_NcmhdmDs3GenIDCode_Type.__name__ = "DisplayString"
_NcmhdmDs3GenIDCode_Object = MibTableColumn
ncmhdmDs3GenIDCode = _NcmhdmDs3GenIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 17),
    _NcmhdmDs3GenIDCode_Type()
)
ncmhdmDs3GenIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3GenIDCode.setStatus("mandatory")


class _NcmhdmDs3Inband_Type(Integer32):
    """Custom type ncmhdmDs3Inband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3Inband_Type.__name__ = "Integer32"
_NcmhdmDs3Inband_Object = MibTableColumn
ncmhdmDs3Inband = _NcmhdmDs3Inband_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9000, 1, 18),
    _NcmhdmDs3Inband_Type()
)
ncmhdmDs3Inband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3Inband.setStatus("mandatory")
_NcmhdmHssi1PortTable_Object = MibTable
ncmhdmHssi1PortTable = _NcmhdmHssi1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001)
)
if mibBuilder.loadTexts:
    ncmhdmHssi1PortTable.setStatus("mandatory")
_NcmhdmHssi1PortEntry_Object = MibTableRow
ncmhdmHssi1PortEntry = _NcmhdmHssi1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1)
)
ncmhdmHssi1PortEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmDs3Hssi1NIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmHssi1PortIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmHssi1PortEntry.setStatus("mandatory")


class _NcmhdmDs3Hssi1NIDIndex_Type(Integer32):
    """Custom type ncmhdmDs3Hssi1NIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmDs3Hssi1NIDIndex_Type.__name__ = "Integer32"
_NcmhdmDs3Hssi1NIDIndex_Object = MibTableColumn
ncmhdmDs3Hssi1NIDIndex = _NcmhdmDs3Hssi1NIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 1),
    _NcmhdmDs3Hssi1NIDIndex_Type()
)
ncmhdmDs3Hssi1NIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3Hssi1NIDIndex.setStatus("mandatory")


class _NcmhdmHssi1PortIndex_Type(Integer32):
    """Custom type ncmhdmHssi1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmHssi1PortIndex_Type.__name__ = "Integer32"
_NcmhdmHssi1PortIndex_Object = MibTableColumn
ncmhdmHssi1PortIndex = _NcmhdmHssi1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 2),
    _NcmhdmHssi1PortIndex_Type()
)
ncmhdmHssi1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmHssi1PortIndex.setStatus("mandatory")


class _NcmhdmHssi1ConfigMode_Type(Integer32):
    """Custom type ncmhdmHssi1ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aUTOMATIC", 1),
          ("mANUAL", 2))
    )


_NcmhdmHssi1ConfigMode_Type.__name__ = "Integer32"
_NcmhdmHssi1ConfigMode_Object = MibTableColumn
ncmhdmHssi1ConfigMode = _NcmhdmHssi1ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 3),
    _NcmhdmHssi1ConfigMode_Type()
)
ncmhdmHssi1ConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmHssi1ConfigMode.setStatus("mandatory")


class _NcmhdmHssi1PortConfig_Type(Integer32):
    """Custom type ncmhdmHssi1PortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iN-SERVICE", 2),
          ("oUT-OF-SERVICE", 1))
    )


_NcmhdmHssi1PortConfig_Type.__name__ = "Integer32"
_NcmhdmHssi1PortConfig_Object = MibTableColumn
ncmhdmHssi1PortConfig = _NcmhdmHssi1PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 4),
    _NcmhdmHssi1PortConfig_Type()
)
ncmhdmHssi1PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmHssi1PortConfig.setStatus("mandatory")


class _NcmhdmHssi1TestMode_Type(Integer32):
    """Custom type ncmhdmHssi1TestMode based on Integer32"""
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


_NcmhdmHssi1TestMode_Type.__name__ = "Integer32"
_NcmhdmHssi1TestMode_Object = MibTableColumn
ncmhdmHssi1TestMode = _NcmhdmHssi1TestMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 5),
    _NcmhdmHssi1TestMode_Type()
)
ncmhdmHssi1TestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmHssi1TestMode.setStatus("mandatory")


class _NcmhdmHssi1DataRateMode_Type(Integer32):
    """Custom type ncmhdmHssi1DataRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both-NearEndORFarEnd", 2),
          ("not-applicable", 3),
          ("only-NearEnd", 1))
    )


_NcmhdmHssi1DataRateMode_Type.__name__ = "Integer32"
_NcmhdmHssi1DataRateMode_Object = MibTableColumn
ncmhdmHssi1DataRateMode = _NcmhdmHssi1DataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 6),
    _NcmhdmHssi1DataRateMode_Type()
)
ncmhdmHssi1DataRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmHssi1DataRateMode.setStatus("mandatory")


class _NcmhdmHssi1HssiRate_Type(Integer32):
    """Custom type ncmhdmHssi1HssiRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_NcmhdmHssi1HssiRate_Type.__name__ = "Integer32"
_NcmhdmHssi1HssiRate_Object = MibTableColumn
ncmhdmHssi1HssiRate = _NcmhdmHssi1HssiRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 7),
    _NcmhdmHssi1HssiRate_Type()
)
ncmhdmHssi1HssiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmHssi1HssiRate.setStatus("mandatory")


class _NcmhdmHssi1CircuitID_Type(DisplayString):
    """Custom type ncmhdmHssi1CircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NcmhdmHssi1CircuitID_Type.__name__ = "DisplayString"
_NcmhdmHssi1CircuitID_Object = MibTableColumn
ncmhdmHssi1CircuitID = _NcmhdmHssi1CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9001, 1, 8),
    _NcmhdmHssi1CircuitID_Type()
)
ncmhdmHssi1CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmHssi1CircuitID.setStatus("mandatory")
_NcmhdmHssiStatTable_Object = MibTable
ncmhdmHssiStatTable = _NcmhdmHssiStatTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002)
)
if mibBuilder.loadTexts:
    ncmhdmHssiStatTable.setStatus("mandatory")
_NcmhdmHssiStatEntry_Object = MibTableRow
ncmhdmHssiStatEntry = _NcmhdmHssiStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1)
)
ncmhdmHssiStatEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmHssiStatNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmHssiStatIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmHssiStatEntry.setStatus("mandatory")


class _NcmhdmHssiStatNIDIndex_Type(Integer32):
    """Custom type ncmhdmHssiStatNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmHssiStatNIDIndex_Type.__name__ = "Integer32"
_NcmhdmHssiStatNIDIndex_Object = MibTableColumn
ncmhdmHssiStatNIDIndex = _NcmhdmHssiStatNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 1),
    _NcmhdmHssiStatNIDIndex_Type()
)
ncmhdmHssiStatNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmHssiStatNIDIndex.setStatus("mandatory")


class _NcmhdmHssiStatIndex_Type(Integer32):
    """Custom type ncmhdmHssiStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmHssiStatIndex_Type.__name__ = "Integer32"
_NcmhdmHssiStatIndex_Object = MibTableColumn
ncmhdmHssiStatIndex = _NcmhdmHssiStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 2),
    _NcmhdmHssiStatIndex_Type()
)
ncmhdmHssiStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmHssiStatIndex.setStatus("mandatory")


class _NcmhdmStatDCEReady_Type(Integer32):
    """Custom type ncmhdmStatDCEReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatDCEReady_Type.__name__ = "Integer32"
_NcmhdmStatDCEReady_Object = MibTableColumn
ncmhdmStatDCEReady = _NcmhdmStatDCEReady_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 3),
    _NcmhdmStatDCEReady_Type()
)
ncmhdmStatDCEReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatDCEReady.setStatus("mandatory")


class _NcmhdmStatDTEReady_Type(Integer32):
    """Custom type ncmhdmStatDTEReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatDTEReady_Type.__name__ = "Integer32"
_NcmhdmStatDTEReady_Object = MibTableColumn
ncmhdmStatDTEReady = _NcmhdmStatDTEReady_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 4),
    _NcmhdmStatDTEReady_Type()
)
ncmhdmStatDTEReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatDTEReady.setStatus("mandatory")


class _NcmhdmStatLpbkA_Type(Integer32):
    """Custom type ncmhdmStatLpbkA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatLpbkA_Type.__name__ = "Integer32"
_NcmhdmStatLpbkA_Object = MibTableColumn
ncmhdmStatLpbkA = _NcmhdmStatLpbkA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 5),
    _NcmhdmStatLpbkA_Type()
)
ncmhdmStatLpbkA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatLpbkA.setStatus("mandatory")


class _NcmhdmStatLpbkB_Type(Integer32):
    """Custom type ncmhdmStatLpbkB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatLpbkB_Type.__name__ = "Integer32"
_NcmhdmStatLpbkB_Object = MibTableColumn
ncmhdmStatLpbkB = _NcmhdmStatLpbkB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 6),
    _NcmhdmStatLpbkB_Type()
)
ncmhdmStatLpbkB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatLpbkB.setStatus("mandatory")


class _NcmhdmStatTestMode_Type(Integer32):
    """Custom type ncmhdmStatTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatTestMode_Type.__name__ = "Integer32"
_NcmhdmStatTestMode_Object = MibTableColumn
ncmhdmStatTestMode = _NcmhdmStatTestMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 7),
    _NcmhdmStatTestMode_Type()
)
ncmhdmStatTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatTestMode.setStatus("mandatory")


class _NcmhdmStatPortState_Type(Integer32):
    """Custom type ncmhdmStatPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iN-SERVICE", 2),
          ("oUT-OF-SERVICE", 1))
    )


_NcmhdmStatPortState_Type.__name__ = "Integer32"
_NcmhdmStatPortState_Object = MibTableColumn
ncmhdmStatPortState = _NcmhdmStatPortState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 8),
    _NcmhdmStatPortState_Type()
)
ncmhdmStatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatPortState.setStatus("mandatory")


class _NcmhdmStatCIMType_Type(Integer32):
    """Custom type ncmhdmStatCIMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(44,
              59,
              63)
        )
    )
    namedValues = NamedValues(
        *(("cdm-2080", 59),
          ("cdm-2182", 63),
          ("cim-2080", 44))
    )


_NcmhdmStatCIMType_Type.__name__ = "Integer32"
_NcmhdmStatCIMType_Object = MibTableColumn
ncmhdmStatCIMType = _NcmhdmStatCIMType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 9),
    _NcmhdmStatCIMType_Type()
)
ncmhdmStatCIMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatCIMType.setStatus("mandatory")


class _NcmhdmStatDiagStatus_Type(Integer32):
    """Custom type ncmhdmStatDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmStatDiagStatus_Type.__name__ = "Integer32"
_NcmhdmStatDiagStatus_Object = MibTableColumn
ncmhdmStatDiagStatus = _NcmhdmStatDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9002, 1, 10),
    _NcmhdmStatDiagStatus_Type()
)
ncmhdmStatDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmStatDiagStatus.setStatus("mandatory")
_NcmhdmCurrentTable_Object = MibTable
ncmhdmCurrentTable = _NcmhdmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003)
)
if mibBuilder.loadTexts:
    ncmhdmCurrentTable.setStatus("mandatory")
_NcmhdmCurrentEntry_Object = MibTableRow
ncmhdmCurrentEntry = _NcmhdmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1)
)
ncmhdmCurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmCurrentNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmCurrentIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmCurrentEntry.setStatus("mandatory")


class _NcmhdmCurrentNIDIndex_Type(Integer32):
    """Custom type ncmhdmCurrentNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmCurrentNIDIndex_Type.__name__ = "Integer32"
_NcmhdmCurrentNIDIndex_Object = MibTableColumn
ncmhdmCurrentNIDIndex = _NcmhdmCurrentNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 1),
    _NcmhdmCurrentNIDIndex_Type()
)
ncmhdmCurrentNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentNIDIndex.setStatus("mandatory")


class _NcmhdmCurrentIndex_Type(Integer32):
    """Custom type ncmhdmCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmCurrentIndex_Type.__name__ = "Integer32"
_NcmhdmCurrentIndex_Object = MibTableColumn
ncmhdmCurrentIndex = _NcmhdmCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 2),
    _NcmhdmCurrentIndex_Type()
)
ncmhdmCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentIndex.setStatus("mandatory")


class _NcmhdmCurrentCRC4Status_Type(Integer32):
    """Custom type ncmhdmCurrentCRC4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_NcmhdmCurrentCRC4Status_Type.__name__ = "Integer32"
_NcmhdmCurrentCRC4Status_Object = MibTableColumn
ncmhdmCurrentCRC4Status = _NcmhdmCurrentCRC4Status_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 3),
    _NcmhdmCurrentCRC4Status_Type()
)
ncmhdmCurrentCRC4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentCRC4Status.setStatus("mandatory")


class _NcmhdmCurrentTimeStampSecs_Type(Integer32):
    """Custom type ncmhdmCurrentTimeStampSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmCurrentTimeStampSecs_Type.__name__ = "Integer32"
_NcmhdmCurrentTimeStampSecs_Object = MibTableColumn
ncmhdmCurrentTimeStampSecs = _NcmhdmCurrentTimeStampSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 4),
    _NcmhdmCurrentTimeStampSecs_Type()
)
ncmhdmCurrentTimeStampSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentTimeStampSecs.setStatus("mandatory")


class _NcmhdmCurrentTimeStampMSecs_Type(Integer32):
    """Custom type ncmhdmCurrentTimeStampMSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmCurrentTimeStampMSecs_Type.__name__ = "Integer32"
_NcmhdmCurrentTimeStampMSecs_Object = MibTableColumn
ncmhdmCurrentTimeStampMSecs = _NcmhdmCurrentTimeStampMSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 5),
    _NcmhdmCurrentTimeStampMSecs_Type()
)
ncmhdmCurrentTimeStampMSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentTimeStampMSecs.setStatus("mandatory")


class _NcmhdmCurrentSecsElaps_Type(Integer32):
    """Custom type ncmhdmCurrentSecsElaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmCurrentSecsElaps_Type.__name__ = "Integer32"
_NcmhdmCurrentSecsElaps_Object = MibTableColumn
ncmhdmCurrentSecsElaps = _NcmhdmCurrentSecsElaps_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 6),
    _NcmhdmCurrentSecsElaps_Type()
)
ncmhdmCurrentSecsElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentSecsElaps.setStatus("mandatory")
_NcmhdmCurrentFarEndCCV_Type = Gauge32
_NcmhdmCurrentFarEndCCV_Object = MibTableColumn
ncmhdmCurrentFarEndCCV = _NcmhdmCurrentFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 7),
    _NcmhdmCurrentFarEndCCV_Type()
)
ncmhdmCurrentFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentFarEndCCV.setStatus("mandatory")
_NcmhdmCurrentFarEndCES_Type = Gauge32
_NcmhdmCurrentFarEndCES_Object = MibTableColumn
ncmhdmCurrentFarEndCES = _NcmhdmCurrentFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 8),
    _NcmhdmCurrentFarEndCES_Type()
)
ncmhdmCurrentFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentFarEndCES.setStatus("mandatory")
_NcmhdmCurrentFarEndCSES_Type = Gauge32
_NcmhdmCurrentFarEndCSES_Object = MibTableColumn
ncmhdmCurrentFarEndCSES = _NcmhdmCurrentFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 9),
    _NcmhdmCurrentFarEndCSES_Type()
)
ncmhdmCurrentFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentFarEndCSES.setStatus("mandatory")
_NcmhdmCurrentFarEndLUAS_Type = Gauge32
_NcmhdmCurrentFarEndLUAS_Object = MibTableColumn
ncmhdmCurrentFarEndLUAS = _NcmhdmCurrentFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 10),
    _NcmhdmCurrentFarEndLUAS_Type()
)
ncmhdmCurrentFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentFarEndLUAS.setStatus("mandatory")
_NcmhdmCurrentLCV_Type = Gauge32
_NcmhdmCurrentLCV_Object = MibTableColumn
ncmhdmCurrentLCV = _NcmhdmCurrentLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 11),
    _NcmhdmCurrentLCV_Type()
)
ncmhdmCurrentLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentLCV.setStatus("mandatory")
_NcmhdmCurrentLES_Type = Gauge32
_NcmhdmCurrentLES_Object = MibTableColumn
ncmhdmCurrentLES = _NcmhdmCurrentLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 12),
    _NcmhdmCurrentLES_Type()
)
ncmhdmCurrentLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentLES.setStatus("mandatory")
_NcmhdmCurrentLSESs_Type = Gauge32
_NcmhdmCurrentLSESs_Object = MibTableColumn
ncmhdmCurrentLSESs = _NcmhdmCurrentLSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 13),
    _NcmhdmCurrentLSESs_Type()
)
ncmhdmCurrentLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentLSESs.setStatus("mandatory")
_NcmhdmCurrentPCV_Type = Gauge32
_NcmhdmCurrentPCV_Object = MibTableColumn
ncmhdmCurrentPCV = _NcmhdmCurrentPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 14),
    _NcmhdmCurrentPCV_Type()
)
ncmhdmCurrentPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentPCV.setStatus("mandatory")
_NcmhdmCurrentPES_Type = Gauge32
_NcmhdmCurrentPES_Object = MibTableColumn
ncmhdmCurrentPES = _NcmhdmCurrentPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 15),
    _NcmhdmCurrentPES_Type()
)
ncmhdmCurrentPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentPES.setStatus("mandatory")
_NcmhdmCurrentPSES_Type = Gauge32
_NcmhdmCurrentPSES_Object = MibTableColumn
ncmhdmCurrentPSES = _NcmhdmCurrentPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 16),
    _NcmhdmCurrentPSES_Type()
)
ncmhdmCurrentPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentPSES.setStatus("mandatory")
_NcmhdmCurrentCCV_Type = Gauge32
_NcmhdmCurrentCCV_Object = MibTableColumn
ncmhdmCurrentCCV = _NcmhdmCurrentCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 17),
    _NcmhdmCurrentCCV_Type()
)
ncmhdmCurrentCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentCCV.setStatus("mandatory")
_NcmhdmCurrentCES_Type = Gauge32
_NcmhdmCurrentCES_Object = MibTableColumn
ncmhdmCurrentCES = _NcmhdmCurrentCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 18),
    _NcmhdmCurrentCES_Type()
)
ncmhdmCurrentCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentCES.setStatus("mandatory")
_NcmhdmCurrentCSES_Type = Gauge32
_NcmhdmCurrentCSES_Object = MibTableColumn
ncmhdmCurrentCSES = _NcmhdmCurrentCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 19),
    _NcmhdmCurrentCSES_Type()
)
ncmhdmCurrentCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentCSES.setStatus("mandatory")
_NcmhdmCurrentSEFS_Type = Gauge32
_NcmhdmCurrentSEFS_Object = MibTableColumn
ncmhdmCurrentSEFS = _NcmhdmCurrentSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 20),
    _NcmhdmCurrentSEFS_Type()
)
ncmhdmCurrentSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentSEFS.setStatus("mandatory")
_NcmhdmCurrentAISS_Type = Gauge32
_NcmhdmCurrentAISS_Object = MibTableColumn
ncmhdmCurrentAISS = _NcmhdmCurrentAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 21),
    _NcmhdmCurrentAISS_Type()
)
ncmhdmCurrentAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentAISS.setStatus("mandatory")
_NcmhdmCurrentOOSSs_Type = Gauge32
_NcmhdmCurrentOOSSs_Object = MibTableColumn
ncmhdmCurrentOOSSs = _NcmhdmCurrentOOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 22),
    _NcmhdmCurrentOOSSs_Type()
)
ncmhdmCurrentOOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentOOSSs.setStatus("mandatory")
_NcmhdmCurrentLOSSs_Type = Gauge32
_NcmhdmCurrentLOSSs_Object = MibTableColumn
ncmhdmCurrentLOSSs = _NcmhdmCurrentLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 23),
    _NcmhdmCurrentLOSSs_Type()
)
ncmhdmCurrentLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentLOSSs.setStatus("mandatory")
_NcmhdmCurrentLOFSs_Type = Gauge32
_NcmhdmCurrentLOFSs_Object = MibTableColumn
ncmhdmCurrentLOFSs = _NcmhdmCurrentLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9003, 1, 24),
    _NcmhdmCurrentLOFSs_Type()
)
ncmhdmCurrentLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmCurrentLOFSs.setStatus("mandatory")
_NcmhdmIntervalTable_Object = MibTable
ncmhdmIntervalTable = _NcmhdmIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004)
)
if mibBuilder.loadTexts:
    ncmhdmIntervalTable.setStatus("mandatory")
_NcmhdmIntervalEntry_Object = MibTableRow
ncmhdmIntervalEntry = _NcmhdmIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1)
)
ncmhdmIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmIntervalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmIntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmhdmIntervalEntry.setStatus("mandatory")


class _NcmhdmIntervalNIDIndex_Type(Integer32):
    """Custom type ncmhdmIntervalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmIntervalNIDIndex_Type.__name__ = "Integer32"
_NcmhdmIntervalNIDIndex_Object = MibTableColumn
ncmhdmIntervalNIDIndex = _NcmhdmIntervalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 1),
    _NcmhdmIntervalNIDIndex_Type()
)
ncmhdmIntervalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalNIDIndex.setStatus("mandatory")


class _NcmhdmIntervalIndex_Type(Integer32):
    """Custom type ncmhdmIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmIntervalIndex_Type.__name__ = "Integer32"
_NcmhdmIntervalIndex_Object = MibTableColumn
ncmhdmIntervalIndex = _NcmhdmIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 2),
    _NcmhdmIntervalIndex_Type()
)
ncmhdmIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalIndex.setStatus("mandatory")


class _NcmhdmIntervalNumber_Type(Integer32):
    """Custom type ncmhdmIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmhdmIntervalNumber_Type.__name__ = "Integer32"
_NcmhdmIntervalNumber_Object = MibTableColumn
ncmhdmIntervalNumber = _NcmhdmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 3),
    _NcmhdmIntervalNumber_Type()
)
ncmhdmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalNumber.setStatus("mandatory")
_NcmhdmIntervalFarEndCCV_Type = Gauge32
_NcmhdmIntervalFarEndCCV_Object = MibTableColumn
ncmhdmIntervalFarEndCCV = _NcmhdmIntervalFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 4),
    _NcmhdmIntervalFarEndCCV_Type()
)
ncmhdmIntervalFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalFarEndCCV.setStatus("mandatory")
_NcmhdmIntervalFarEndCES_Type = Gauge32
_NcmhdmIntervalFarEndCES_Object = MibTableColumn
ncmhdmIntervalFarEndCES = _NcmhdmIntervalFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 5),
    _NcmhdmIntervalFarEndCES_Type()
)
ncmhdmIntervalFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalFarEndCES.setStatus("mandatory")
_NcmhdmIntervalFarEndCSES_Type = Gauge32
_NcmhdmIntervalFarEndCSES_Object = MibTableColumn
ncmhdmIntervalFarEndCSES = _NcmhdmIntervalFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 6),
    _NcmhdmIntervalFarEndCSES_Type()
)
ncmhdmIntervalFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalFarEndCSES.setStatus("mandatory")
_NcmhdmIntervalFarEndLUAS_Type = Gauge32
_NcmhdmIntervalFarEndLUAS_Object = MibTableColumn
ncmhdmIntervalFarEndLUAS = _NcmhdmIntervalFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 7),
    _NcmhdmIntervalFarEndLUAS_Type()
)
ncmhdmIntervalFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalFarEndLUAS.setStatus("mandatory")
_NcmhdmIntervalLCV_Type = Gauge32
_NcmhdmIntervalLCV_Object = MibTableColumn
ncmhdmIntervalLCV = _NcmhdmIntervalLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 8),
    _NcmhdmIntervalLCV_Type()
)
ncmhdmIntervalLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalLCV.setStatus("mandatory")
_NcmhdmIntervalLES_Type = Gauge32
_NcmhdmIntervalLES_Object = MibTableColumn
ncmhdmIntervalLES = _NcmhdmIntervalLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 9),
    _NcmhdmIntervalLES_Type()
)
ncmhdmIntervalLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalLES.setStatus("mandatory")
_NcmhdmIntervalLSESs_Type = Gauge32
_NcmhdmIntervalLSESs_Object = MibTableColumn
ncmhdmIntervalLSESs = _NcmhdmIntervalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 10),
    _NcmhdmIntervalLSESs_Type()
)
ncmhdmIntervalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalLSESs.setStatus("mandatory")
_NcmhdmIntervalPCV_Type = Gauge32
_NcmhdmIntervalPCV_Object = MibTableColumn
ncmhdmIntervalPCV = _NcmhdmIntervalPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 11),
    _NcmhdmIntervalPCV_Type()
)
ncmhdmIntervalPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalPCV.setStatus("mandatory")
_NcmhdmIntervalPES_Type = Gauge32
_NcmhdmIntervalPES_Object = MibTableColumn
ncmhdmIntervalPES = _NcmhdmIntervalPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 12),
    _NcmhdmIntervalPES_Type()
)
ncmhdmIntervalPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalPES.setStatus("mandatory")
_NcmhdmIntervalPSES_Type = Gauge32
_NcmhdmIntervalPSES_Object = MibTableColumn
ncmhdmIntervalPSES = _NcmhdmIntervalPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 13),
    _NcmhdmIntervalPSES_Type()
)
ncmhdmIntervalPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalPSES.setStatus("mandatory")
_NcmhdmIntervalCCV_Type = Gauge32
_NcmhdmIntervalCCV_Object = MibTableColumn
ncmhdmIntervalCCV = _NcmhdmIntervalCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 14),
    _NcmhdmIntervalCCV_Type()
)
ncmhdmIntervalCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalCCV.setStatus("mandatory")
_NcmhdmIntervalCES_Type = Gauge32
_NcmhdmIntervalCES_Object = MibTableColumn
ncmhdmIntervalCES = _NcmhdmIntervalCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 15),
    _NcmhdmIntervalCES_Type()
)
ncmhdmIntervalCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalCES.setStatus("mandatory")
_NcmhdmIntervalCSES_Type = Gauge32
_NcmhdmIntervalCSES_Object = MibTableColumn
ncmhdmIntervalCSES = _NcmhdmIntervalCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 16),
    _NcmhdmIntervalCSES_Type()
)
ncmhdmIntervalCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalCSES.setStatus("mandatory")
_NcmhdmIntervalSEFS_Type = Gauge32
_NcmhdmIntervalSEFS_Object = MibTableColumn
ncmhdmIntervalSEFS = _NcmhdmIntervalSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 17),
    _NcmhdmIntervalSEFS_Type()
)
ncmhdmIntervalSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalSEFS.setStatus("mandatory")
_NcmhdmIntervalAISS_Type = Gauge32
_NcmhdmIntervalAISS_Object = MibTableColumn
ncmhdmIntervalAISS = _NcmhdmIntervalAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 18),
    _NcmhdmIntervalAISS_Type()
)
ncmhdmIntervalAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalAISS.setStatus("mandatory")
_NcmhdmIntervalOOSSs_Type = Gauge32
_NcmhdmIntervalOOSSs_Object = MibTableColumn
ncmhdmIntervalOOSSs = _NcmhdmIntervalOOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 19),
    _NcmhdmIntervalOOSSs_Type()
)
ncmhdmIntervalOOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalOOSSs.setStatus("mandatory")
_NcmhdmIntervalLOSSs_Type = Gauge32
_NcmhdmIntervalLOSSs_Object = MibTableColumn
ncmhdmIntervalLOSSs = _NcmhdmIntervalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 20),
    _NcmhdmIntervalLOSSs_Type()
)
ncmhdmIntervalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalLOSSs.setStatus("mandatory")
_NcmhdmIntervalLOFSs_Type = Gauge32
_NcmhdmIntervalLOFSs_Object = MibTableColumn
ncmhdmIntervalLOFSs = _NcmhdmIntervalLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9004, 1, 21),
    _NcmhdmIntervalLOFSs_Type()
)
ncmhdmIntervalLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmIntervalLOFSs.setStatus("mandatory")
_NcmhdmTotalTable_Object = MibTable
ncmhdmTotalTable = _NcmhdmTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005)
)
if mibBuilder.loadTexts:
    ncmhdmTotalTable.setStatus("mandatory")
_NcmhdmTotalEntry_Object = MibTableRow
ncmhdmTotalEntry = _NcmhdmTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1)
)
ncmhdmTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTotalIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmTotalEntry.setStatus("mandatory")


class _NcmhdmTotalNIDIndex_Type(Integer32):
    """Custom type ncmhdmTotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmTotalNIDIndex_Type.__name__ = "Integer32"
_NcmhdmTotalNIDIndex_Object = MibTableColumn
ncmhdmTotalNIDIndex = _NcmhdmTotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 1),
    _NcmhdmTotalNIDIndex_Type()
)
ncmhdmTotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalNIDIndex.setStatus("mandatory")


class _NcmhdmTotalIndex_Type(Integer32):
    """Custom type ncmhdmTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmTotalIndex_Type.__name__ = "Integer32"
_NcmhdmTotalIndex_Object = MibTableColumn
ncmhdmTotalIndex = _NcmhdmTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 2),
    _NcmhdmTotalIndex_Type()
)
ncmhdmTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalIndex.setStatus("mandatory")


class _NcmhdmTotalCRC4Status_Type(Integer32):
    """Custom type ncmhdmTotalCRC4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_NcmhdmTotalCRC4Status_Type.__name__ = "Integer32"
_NcmhdmTotalCRC4Status_Object = MibTableColumn
ncmhdmTotalCRC4Status = _NcmhdmTotalCRC4Status_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 3),
    _NcmhdmTotalCRC4Status_Type()
)
ncmhdmTotalCRC4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalCRC4Status.setStatus("mandatory")


class _NcmhdmTotalValidInterv_Type(Integer32):
    """Custom type ncmhdmTotalValidInterv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmTotalValidInterv_Type.__name__ = "Integer32"
_NcmhdmTotalValidInterv_Object = MibTableColumn
ncmhdmTotalValidInterv = _NcmhdmTotalValidInterv_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 4),
    _NcmhdmTotalValidInterv_Type()
)
ncmhdmTotalValidInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalValidInterv.setStatus("mandatory")
_NcmhdmTotalFarEndCCV_Type = Gauge32
_NcmhdmTotalFarEndCCV_Object = MibTableColumn
ncmhdmTotalFarEndCCV = _NcmhdmTotalFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 5),
    _NcmhdmTotalFarEndCCV_Type()
)
ncmhdmTotalFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalFarEndCCV.setStatus("mandatory")
_NcmhdmTotalFarEndCES_Type = Gauge32
_NcmhdmTotalFarEndCES_Object = MibTableColumn
ncmhdmTotalFarEndCES = _NcmhdmTotalFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 6),
    _NcmhdmTotalFarEndCES_Type()
)
ncmhdmTotalFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalFarEndCES.setStatus("mandatory")
_NcmhdmTotalFarEndCSES_Type = Gauge32
_NcmhdmTotalFarEndCSES_Object = MibTableColumn
ncmhdmTotalFarEndCSES = _NcmhdmTotalFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 7),
    _NcmhdmTotalFarEndCSES_Type()
)
ncmhdmTotalFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalFarEndCSES.setStatus("mandatory")
_NcmhdmTotalFarEndLUAS_Type = Gauge32
_NcmhdmTotalFarEndLUAS_Object = MibTableColumn
ncmhdmTotalFarEndLUAS = _NcmhdmTotalFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 8),
    _NcmhdmTotalFarEndLUAS_Type()
)
ncmhdmTotalFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalFarEndLUAS.setStatus("mandatory")
_NcmhdmTotalLCV_Type = Gauge32
_NcmhdmTotalLCV_Object = MibTableColumn
ncmhdmTotalLCV = _NcmhdmTotalLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 9),
    _NcmhdmTotalLCV_Type()
)
ncmhdmTotalLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalLCV.setStatus("mandatory")
_NcmhdmTotalLES_Type = Gauge32
_NcmhdmTotalLES_Object = MibTableColumn
ncmhdmTotalLES = _NcmhdmTotalLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 10),
    _NcmhdmTotalLES_Type()
)
ncmhdmTotalLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalLES.setStatus("mandatory")
_NcmhdmTotalLSESs_Type = Gauge32
_NcmhdmTotalLSESs_Object = MibTableColumn
ncmhdmTotalLSESs = _NcmhdmTotalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 11),
    _NcmhdmTotalLSESs_Type()
)
ncmhdmTotalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalLSESs.setStatus("mandatory")
_NcmhdmTotalPCV_Type = Gauge32
_NcmhdmTotalPCV_Object = MibTableColumn
ncmhdmTotalPCV = _NcmhdmTotalPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 12),
    _NcmhdmTotalPCV_Type()
)
ncmhdmTotalPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalPCV.setStatus("mandatory")
_NcmhdmTotalPES_Type = Gauge32
_NcmhdmTotalPES_Object = MibTableColumn
ncmhdmTotalPES = _NcmhdmTotalPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 13),
    _NcmhdmTotalPES_Type()
)
ncmhdmTotalPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalPES.setStatus("mandatory")
_NcmhdmTotalPSES_Type = Gauge32
_NcmhdmTotalPSES_Object = MibTableColumn
ncmhdmTotalPSES = _NcmhdmTotalPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 14),
    _NcmhdmTotalPSES_Type()
)
ncmhdmTotalPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalPSES.setStatus("mandatory")
_NcmhdmTotalCCV_Type = Gauge32
_NcmhdmTotalCCV_Object = MibTableColumn
ncmhdmTotalCCV = _NcmhdmTotalCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 15),
    _NcmhdmTotalCCV_Type()
)
ncmhdmTotalCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalCCV.setStatus("mandatory")
_NcmhdmTotalCES_Type = Gauge32
_NcmhdmTotalCES_Object = MibTableColumn
ncmhdmTotalCES = _NcmhdmTotalCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 16),
    _NcmhdmTotalCES_Type()
)
ncmhdmTotalCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalCES.setStatus("mandatory")
_NcmhdmTotalCSES_Type = Gauge32
_NcmhdmTotalCSES_Object = MibTableColumn
ncmhdmTotalCSES = _NcmhdmTotalCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 17),
    _NcmhdmTotalCSES_Type()
)
ncmhdmTotalCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalCSES.setStatus("mandatory")
_NcmhdmTotalSEFS_Type = Gauge32
_NcmhdmTotalSEFS_Object = MibTableColumn
ncmhdmTotalSEFS = _NcmhdmTotalSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 18),
    _NcmhdmTotalSEFS_Type()
)
ncmhdmTotalSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalSEFS.setStatus("mandatory")
_NcmhdmTotalAISS_Type = Gauge32
_NcmhdmTotalAISS_Object = MibTableColumn
ncmhdmTotalAISS = _NcmhdmTotalAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 19),
    _NcmhdmTotalAISS_Type()
)
ncmhdmTotalAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalAISS.setStatus("mandatory")
_NcmhdmTotalOOSSs_Type = Gauge32
_NcmhdmTotalOOSSs_Object = MibTableColumn
ncmhdmTotalOOSSs = _NcmhdmTotalOOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 20),
    _NcmhdmTotalOOSSs_Type()
)
ncmhdmTotalOOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalOOSSs.setStatus("mandatory")
_NcmhdmTotalLOSSs_Type = Gauge32
_NcmhdmTotalLOSSs_Object = MibTableColumn
ncmhdmTotalLOSSs = _NcmhdmTotalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 21),
    _NcmhdmTotalLOSSs_Type()
)
ncmhdmTotalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalLOSSs.setStatus("mandatory")
_NcmhdmTotalLOFSs_Type = Gauge32
_NcmhdmTotalLOFSs_Object = MibTableColumn
ncmhdmTotalLOFSs = _NcmhdmTotalLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9005, 1, 22),
    _NcmhdmTotalLOFSs_Type()
)
ncmhdmTotalLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTotalLOFSs.setStatus("mandatory")
_NcmDs3PerformanceSnapShotTable_Object = MibTable
ncmDs3PerformanceSnapShotTable = _NcmDs3PerformanceSnapShotTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006)
)
if mibBuilder.loadTexts:
    ncmDs3PerformanceSnapShotTable.setStatus("mandatory")
_NcmDs3PerformanceSnapShotEntry_Object = MibTableRow
ncmDs3PerformanceSnapShotEntry = _NcmDs3PerformanceSnapShotEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1)
)
ncmDs3PerformanceSnapShotEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmDs3SnapShotNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmDs3SnapShotIndex"),
)
if mibBuilder.loadTexts:
    ncmDs3PerformanceSnapShotEntry.setStatus("mandatory")


class _NcmDs3SnapShotNIDIndex_Type(Integer32):
    """Custom type ncmDs3SnapShotNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDs3SnapShotNIDIndex_Type.__name__ = "Integer32"
_NcmDs3SnapShotNIDIndex_Object = MibTableColumn
ncmDs3SnapShotNIDIndex = _NcmDs3SnapShotNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 1),
    _NcmDs3SnapShotNIDIndex_Type()
)
ncmDs3SnapShotNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3SnapShotNIDIndex.setStatus("mandatory")


class _NcmDs3SnapShotIndex_Type(Integer32):
    """Custom type ncmDs3SnapShotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDs3SnapShotIndex_Type.__name__ = "Integer32"
_NcmDs3SnapShotIndex_Object = MibTableColumn
ncmDs3SnapShotIndex = _NcmDs3SnapShotIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 2),
    _NcmDs3SnapShotIndex_Type()
)
ncmDs3SnapShotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3SnapShotIndex.setStatus("mandatory")


class _NcmDs3SnapShotCRC4Status_Type(Integer32):
    """Custom type ncmDs3SnapShotCRC4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_NcmDs3SnapShotCRC4Status_Type.__name__ = "Integer32"
_NcmDs3SnapShotCRC4Status_Object = MibTableColumn
ncmDs3SnapShotCRC4Status = _NcmDs3SnapShotCRC4Status_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 3),
    _NcmDs3SnapShotCRC4Status_Type()
)
ncmDs3SnapShotCRC4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3SnapShotCRC4Status.setStatus("mandatory")


class _NcmDs3SnapShot_Type(Integer32):
    """Custom type ncmDs3SnapShot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmDs3SnapShot_Type.__name__ = "Integer32"
_NcmDs3SnapShot_Object = MibTableColumn
ncmDs3SnapShot = _NcmDs3SnapShot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 4),
    _NcmDs3SnapShot_Type()
)
ncmDs3SnapShot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDs3SnapShot.setStatus("mandatory")


class _NcmDs3TimeStampSec_Type(Integer32):
    """Custom type ncmDs3TimeStampSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDs3TimeStampSec_Type.__name__ = "Integer32"
_NcmDs3TimeStampSec_Object = MibTableColumn
ncmDs3TimeStampSec = _NcmDs3TimeStampSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 5),
    _NcmDs3TimeStampSec_Type()
)
ncmDs3TimeStampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3TimeStampSec.setStatus("mandatory")


class _NcmDs3TimeStampMilliSec_Type(Integer32):
    """Custom type ncmDs3TimeStampMilliSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmDs3TimeStampMilliSec_Type.__name__ = "Integer32"
_NcmDs3TimeStampMilliSec_Object = MibTableColumn
ncmDs3TimeStampMilliSec = _NcmDs3TimeStampMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 6),
    _NcmDs3TimeStampMilliSec_Type()
)
ncmDs3TimeStampMilliSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3TimeStampMilliSec.setStatus("mandatory")


class _NcmDs3SnapShotSecs_Type(Integer32):
    """Custom type ncmDs3SnapShotSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmDs3SnapShotSecs_Type.__name__ = "Integer32"
_NcmDs3SnapShotSecs_Object = MibTableColumn
ncmDs3SnapShotSecs = _NcmDs3SnapShotSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 7),
    _NcmDs3SnapShotSecs_Type()
)
ncmDs3SnapShotSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDs3SnapShotSecs.setStatus("mandatory")


class _NcmDs3ResetPerfReg_Type(Integer32):
    """Custom type ncmDs3ResetPerfReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmDs3ResetPerfReg_Type.__name__ = "Integer32"
_NcmDs3ResetPerfReg_Object = MibTableColumn
ncmDs3ResetPerfReg = _NcmDs3ResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9006, 1, 8),
    _NcmDs3ResetPerfReg_Type()
)
ncmDs3ResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDs3ResetPerfReg.setStatus("mandatory")
_NcmhdmTCAQtrTable_Object = MibTable
ncmhdmTCAQtrTable = _NcmhdmTCAQtrTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007)
)
if mibBuilder.loadTexts:
    ncmhdmTCAQtrTable.setStatus("mandatory")
_NcmhdmTCAQtrEntry_Object = MibTableRow
ncmhdmTCAQtrEntry = _NcmhdmTCAQtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1)
)
ncmhdmTCAQtrEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTCAQtrNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTCAQtrIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmTCAQtrEntry.setStatus("mandatory")


class _NcmhdmTCAQtrNIDIndex_Type(Integer32):
    """Custom type ncmhdmTCAQtrNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmTCAQtrNIDIndex_Type.__name__ = "Integer32"
_NcmhdmTCAQtrNIDIndex_Object = MibTableColumn
ncmhdmTCAQtrNIDIndex = _NcmhdmTCAQtrNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 1),
    _NcmhdmTCAQtrNIDIndex_Type()
)
ncmhdmTCAQtrNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrNIDIndex.setStatus("mandatory")


class _NcmhdmTCAQtrIndex_Type(Integer32):
    """Custom type ncmhdmTCAQtrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmTCAQtrIndex_Type.__name__ = "Integer32"
_NcmhdmTCAQtrIndex_Object = MibTableColumn
ncmhdmTCAQtrIndex = _NcmhdmTCAQtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 2),
    _NcmhdmTCAQtrIndex_Type()
)
ncmhdmTCAQtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrIndex.setStatus("mandatory")


class _NcmhdmTCAQtrDs3FarEndCCV_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3FarEndCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3FarEndCCV_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3FarEndCCV_Object = MibTableColumn
ncmhdmTCAQtrDs3FarEndCCV = _NcmhdmTCAQtrDs3FarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 3),
    _NcmhdmTCAQtrDs3FarEndCCV_Type()
)
ncmhdmTCAQtrDs3FarEndCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3FarEndCCV.setStatus("mandatory")


class _NcmhdmTCAQtrDs3FarEndCES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3FarEndCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3FarEndCES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3FarEndCES_Object = MibTableColumn
ncmhdmTCAQtrDs3FarEndCES = _NcmhdmTCAQtrDs3FarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 4),
    _NcmhdmTCAQtrDs3FarEndCES_Type()
)
ncmhdmTCAQtrDs3FarEndCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3FarEndCES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3FarEndCSES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3FarEndCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3FarEndCSES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3FarEndCSES_Object = MibTableColumn
ncmhdmTCAQtrDs3FarEndCSES = _NcmhdmTCAQtrDs3FarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 5),
    _NcmhdmTCAQtrDs3FarEndCSES_Type()
)
ncmhdmTCAQtrDs3FarEndCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3FarEndCSES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3FarEndLUAS_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3FarEndLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3FarEndLUAS_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3FarEndLUAS_Object = MibTableColumn
ncmhdmTCAQtrDs3FarEndLUAS = _NcmhdmTCAQtrDs3FarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 6),
    _NcmhdmTCAQtrDs3FarEndLUAS_Type()
)
ncmhdmTCAQtrDs3FarEndLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3FarEndLUAS.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LCV_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LCV_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LCV_Object = MibTableColumn
ncmhdmTCAQtrDs3LCV = _NcmhdmTCAQtrDs3LCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 7),
    _NcmhdmTCAQtrDs3LCV_Type()
)
ncmhdmTCAQtrDs3LCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LCV.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LES_Object = MibTableColumn
ncmhdmTCAQtrDs3LES = _NcmhdmTCAQtrDs3LES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 8),
    _NcmhdmTCAQtrDs3LES_Type()
)
ncmhdmTCAQtrDs3LES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LSESs_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LSESs_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LSESs_Object = MibTableColumn
ncmhdmTCAQtrDs3LSESs = _NcmhdmTCAQtrDs3LSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 9),
    _NcmhdmTCAQtrDs3LSESs_Type()
)
ncmhdmTCAQtrDs3LSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LSESs.setStatus("mandatory")


class _NcmhdmTCAQtrDs3PCV_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3PCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3PCV_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3PCV_Object = MibTableColumn
ncmhdmTCAQtrDs3PCV = _NcmhdmTCAQtrDs3PCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 10),
    _NcmhdmTCAQtrDs3PCV_Type()
)
ncmhdmTCAQtrDs3PCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3PCV.setStatus("mandatory")


class _NcmhdmTCAQtrDs3PES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3PES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3PES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3PES_Object = MibTableColumn
ncmhdmTCAQtrDs3PES = _NcmhdmTCAQtrDs3PES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 11),
    _NcmhdmTCAQtrDs3PES_Type()
)
ncmhdmTCAQtrDs3PES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3PES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3PSES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3PSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3PSES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3PSES_Object = MibTableColumn
ncmhdmTCAQtrDs3PSES = _NcmhdmTCAQtrDs3PSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 12),
    _NcmhdmTCAQtrDs3PSES_Type()
)
ncmhdmTCAQtrDs3PSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3PSES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3CCV_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3CCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3CCV_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3CCV_Object = MibTableColumn
ncmhdmTCAQtrDs3CCV = _NcmhdmTCAQtrDs3CCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 13),
    _NcmhdmTCAQtrDs3CCV_Type()
)
ncmhdmTCAQtrDs3CCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3CCV.setStatus("mandatory")


class _NcmhdmTCAQtrDs3CES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3CES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3CES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3CES_Object = MibTableColumn
ncmhdmTCAQtrDs3CES = _NcmhdmTCAQtrDs3CES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 14),
    _NcmhdmTCAQtrDs3CES_Type()
)
ncmhdmTCAQtrDs3CES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3CES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3CSES_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3CSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3CSES_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3CSES_Object = MibTableColumn
ncmhdmTCAQtrDs3CSES = _NcmhdmTCAQtrDs3CSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 15),
    _NcmhdmTCAQtrDs3CSES_Type()
)
ncmhdmTCAQtrDs3CSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3CSES.setStatus("mandatory")


class _NcmhdmTCAQtrDs3SEFS_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3SEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3SEFS_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3SEFS_Object = MibTableColumn
ncmhdmTCAQtrDs3SEFS = _NcmhdmTCAQtrDs3SEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 16),
    _NcmhdmTCAQtrDs3SEFS_Type()
)
ncmhdmTCAQtrDs3SEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3SEFS.setStatus("mandatory")


class _NcmhdmTCAQtrDs3AISS_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3AISS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3AISS_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3AISS_Object = MibTableColumn
ncmhdmTCAQtrDs3AISS = _NcmhdmTCAQtrDs3AISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 17),
    _NcmhdmTCAQtrDs3AISS_Type()
)
ncmhdmTCAQtrDs3AISS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3AISS.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LUASs_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LUASs_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LUASs_Object = MibTableColumn
ncmhdmTCAQtrDs3LUASs = _NcmhdmTCAQtrDs3LUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 18),
    _NcmhdmTCAQtrDs3LUASs_Type()
)
ncmhdmTCAQtrDs3LUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LUASs.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LOSSs_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LOSSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LOSSs_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LOSSs_Object = MibTableColumn
ncmhdmTCAQtrDs3LOSSs = _NcmhdmTCAQtrDs3LOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 19),
    _NcmhdmTCAQtrDs3LOSSs_Type()
)
ncmhdmTCAQtrDs3LOSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LOSSs.setStatus("mandatory")


class _NcmhdmTCAQtrDs3LOFSs_Type(Integer32):
    """Custom type ncmhdmTCAQtrDs3LOFSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCAQtrDs3LOFSs_Type.__name__ = "Integer32"
_NcmhdmTCAQtrDs3LOFSs_Object = MibTableColumn
ncmhdmTCAQtrDs3LOFSs = _NcmhdmTCAQtrDs3LOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9007, 1, 20),
    _NcmhdmTCAQtrDs3LOFSs_Type()
)
ncmhdmTCAQtrDs3LOFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCAQtrDs3LOFSs.setStatus("mandatory")
_NcmhdmTCADayTable_Object = MibTable
ncmhdmTCADayTable = _NcmhdmTCADayTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008)
)
if mibBuilder.loadTexts:
    ncmhdmTCADayTable.setStatus("mandatory")
_NcmhdmTCADayEntry_Object = MibTableRow
ncmhdmTCADayEntry = _NcmhdmTCADayEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1)
)
ncmhdmTCADayEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTCADayNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTCADayIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmTCADayEntry.setStatus("mandatory")


class _NcmhdmTCADayNIDIndex_Type(Integer32):
    """Custom type ncmhdmTCADayNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmTCADayNIDIndex_Type.__name__ = "Integer32"
_NcmhdmTCADayNIDIndex_Object = MibTableColumn
ncmhdmTCADayNIDIndex = _NcmhdmTCADayNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 1),
    _NcmhdmTCADayNIDIndex_Type()
)
ncmhdmTCADayNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTCADayNIDIndex.setStatus("mandatory")


class _NcmhdmTCADayIndex_Type(Integer32):
    """Custom type ncmhdmTCADayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmTCADayIndex_Type.__name__ = "Integer32"
_NcmhdmTCADayIndex_Object = MibTableColumn
ncmhdmTCADayIndex = _NcmhdmTCADayIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 2),
    _NcmhdmTCADayIndex_Type()
)
ncmhdmTCADayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTCADayIndex.setStatus("mandatory")


class _NcmhdmTCADayDs3FarEndCCV_Type(Integer32):
    """Custom type ncmhdmTCADayDs3FarEndCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3FarEndCCV_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3FarEndCCV_Object = MibTableColumn
ncmhdmTCADayDs3FarEndCCV = _NcmhdmTCADayDs3FarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 3),
    _NcmhdmTCADayDs3FarEndCCV_Type()
)
ncmhdmTCADayDs3FarEndCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3FarEndCCV.setStatus("mandatory")


class _NcmhdmTCADayDs3FarEndCES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3FarEndCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3FarEndCES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3FarEndCES_Object = MibTableColumn
ncmhdmTCADayDs3FarEndCES = _NcmhdmTCADayDs3FarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 4),
    _NcmhdmTCADayDs3FarEndCES_Type()
)
ncmhdmTCADayDs3FarEndCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3FarEndCES.setStatus("mandatory")


class _NcmhdmTCADayDs3FarEndCSES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3FarEndCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3FarEndCSES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3FarEndCSES_Object = MibTableColumn
ncmhdmTCADayDs3FarEndCSES = _NcmhdmTCADayDs3FarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 5),
    _NcmhdmTCADayDs3FarEndCSES_Type()
)
ncmhdmTCADayDs3FarEndCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3FarEndCSES.setStatus("mandatory")


class _NcmhdmTCADayDs3FarEndLUAS_Type(Integer32):
    """Custom type ncmhdmTCADayDs3FarEndLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3FarEndLUAS_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3FarEndLUAS_Object = MibTableColumn
ncmhdmTCADayDs3FarEndLUAS = _NcmhdmTCADayDs3FarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 6),
    _NcmhdmTCADayDs3FarEndLUAS_Type()
)
ncmhdmTCADayDs3FarEndLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3FarEndLUAS.setStatus("mandatory")


class _NcmhdmTCADayDs3LCV_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LCV_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LCV_Object = MibTableColumn
ncmhdmTCADayDs3LCV = _NcmhdmTCADayDs3LCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 7),
    _NcmhdmTCADayDs3LCV_Type()
)
ncmhdmTCADayDs3LCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LCV.setStatus("mandatory")


class _NcmhdmTCADayDs3LES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LES_Object = MibTableColumn
ncmhdmTCADayDs3LES = _NcmhdmTCADayDs3LES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 8),
    _NcmhdmTCADayDs3LES_Type()
)
ncmhdmTCADayDs3LES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LES.setStatus("mandatory")


class _NcmhdmTCADayDs3LSESs_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LSESs_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LSESs_Object = MibTableColumn
ncmhdmTCADayDs3LSESs = _NcmhdmTCADayDs3LSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 9),
    _NcmhdmTCADayDs3LSESs_Type()
)
ncmhdmTCADayDs3LSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LSESs.setStatus("mandatory")


class _NcmhdmTCADayDs3PCV_Type(Integer32):
    """Custom type ncmhdmTCADayDs3PCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3PCV_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3PCV_Object = MibTableColumn
ncmhdmTCADayDs3PCV = _NcmhdmTCADayDs3PCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 10),
    _NcmhdmTCADayDs3PCV_Type()
)
ncmhdmTCADayDs3PCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3PCV.setStatus("mandatory")


class _NcmhdmTCADayDs3PES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3PES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3PES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3PES_Object = MibTableColumn
ncmhdmTCADayDs3PES = _NcmhdmTCADayDs3PES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 11),
    _NcmhdmTCADayDs3PES_Type()
)
ncmhdmTCADayDs3PES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3PES.setStatus("mandatory")


class _NcmhdmTCADayDs3PSES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3PSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3PSES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3PSES_Object = MibTableColumn
ncmhdmTCADayDs3PSES = _NcmhdmTCADayDs3PSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 12),
    _NcmhdmTCADayDs3PSES_Type()
)
ncmhdmTCADayDs3PSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3PSES.setStatus("mandatory")


class _NcmhdmTCADayDs3CCV_Type(Integer32):
    """Custom type ncmhdmTCADayDs3CCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3CCV_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3CCV_Object = MibTableColumn
ncmhdmTCADayDs3CCV = _NcmhdmTCADayDs3CCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 13),
    _NcmhdmTCADayDs3CCV_Type()
)
ncmhdmTCADayDs3CCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3CCV.setStatus("mandatory")


class _NcmhdmTCADayDs3CES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3CES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3CES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3CES_Object = MibTableColumn
ncmhdmTCADayDs3CES = _NcmhdmTCADayDs3CES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 14),
    _NcmhdmTCADayDs3CES_Type()
)
ncmhdmTCADayDs3CES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3CES.setStatus("mandatory")


class _NcmhdmTCADayDs3CSES_Type(Integer32):
    """Custom type ncmhdmTCADayDs3CSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3CSES_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3CSES_Object = MibTableColumn
ncmhdmTCADayDs3CSES = _NcmhdmTCADayDs3CSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 15),
    _NcmhdmTCADayDs3CSES_Type()
)
ncmhdmTCADayDs3CSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3CSES.setStatus("mandatory")


class _NcmhdmTCADayDs3SEFS_Type(Integer32):
    """Custom type ncmhdmTCADayDs3SEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3SEFS_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3SEFS_Object = MibTableColumn
ncmhdmTCADayDs3SEFS = _NcmhdmTCADayDs3SEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 16),
    _NcmhdmTCADayDs3SEFS_Type()
)
ncmhdmTCADayDs3SEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3SEFS.setStatus("mandatory")


class _NcmhdmTCADayDs3AISS_Type(Integer32):
    """Custom type ncmhdmTCADayDs3AISS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3AISS_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3AISS_Object = MibTableColumn
ncmhdmTCADayDs3AISS = _NcmhdmTCADayDs3AISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 17),
    _NcmhdmTCADayDs3AISS_Type()
)
ncmhdmTCADayDs3AISS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3AISS.setStatus("mandatory")


class _NcmhdmTCADayDs3LUASs_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LUASs_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LUASs_Object = MibTableColumn
ncmhdmTCADayDs3LUASs = _NcmhdmTCADayDs3LUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 18),
    _NcmhdmTCADayDs3LUASs_Type()
)
ncmhdmTCADayDs3LUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LUASs.setStatus("mandatory")


class _NcmhdmTCADayDs3LOSSs_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LOSSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LOSSs_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LOSSs_Object = MibTableColumn
ncmhdmTCADayDs3LOSSs = _NcmhdmTCADayDs3LOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 19),
    _NcmhdmTCADayDs3LOSSs_Type()
)
ncmhdmTCADayDs3LOSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LOSSs.setStatus("mandatory")


class _NcmhdmTCADayDs3LOFSs_Type(Integer32):
    """Custom type ncmhdmTCADayDs3LOFSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NcmhdmTCADayDs3LOFSs_Type.__name__ = "Integer32"
_NcmhdmTCADayDs3LOFSs_Object = MibTableColumn
ncmhdmTCADayDs3LOFSs = _NcmhdmTCADayDs3LOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9008, 1, 20),
    _NcmhdmTCADayDs3LOFSs_Type()
)
ncmhdmTCADayDs3LOFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTCADayDs3LOFSs.setStatus("mandatory")
_NcmhdmTxAlarmTable_Object = MibTable
ncmhdmTxAlarmTable = _NcmhdmTxAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009)
)
if mibBuilder.loadTexts:
    ncmhdmTxAlarmTable.setStatus("mandatory")
_NcmhdmTxAlarmEntry_Object = MibTableRow
ncmhdmTxAlarmEntry = _NcmhdmTxAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1)
)
ncmhdmTxAlarmEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTxAlarmNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmTxAlarmIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmTxAlarmEntry.setStatus("mandatory")


class _NcmhdmTxAlarmNIDIndex_Type(Integer32):
    """Custom type ncmhdmTxAlarmNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmTxAlarmNIDIndex_Type.__name__ = "Integer32"
_NcmhdmTxAlarmNIDIndex_Object = MibTableColumn
ncmhdmTxAlarmNIDIndex = _NcmhdmTxAlarmNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 1),
    _NcmhdmTxAlarmNIDIndex_Type()
)
ncmhdmTxAlarmNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTxAlarmNIDIndex.setStatus("mandatory")


class _NcmhdmTxAlarmIndex_Type(Integer32):
    """Custom type ncmhdmTxAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmTxAlarmIndex_Type.__name__ = "Integer32"
_NcmhdmTxAlarmIndex_Object = MibTableColumn
ncmhdmTxAlarmIndex = _NcmhdmTxAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 2),
    _NcmhdmTxAlarmIndex_Type()
)
ncmhdmTxAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmTxAlarmIndex.setStatus("mandatory")


class _NcmhdmTxYellowAlarm_Type(Integer32):
    """Custom type ncmhdmTxYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dISABLE", 2),
          ("eNABLE", 1))
    )


_NcmhdmTxYellowAlarm_Type.__name__ = "Integer32"
_NcmhdmTxYellowAlarm_Object = MibTableColumn
ncmhdmTxYellowAlarm = _NcmhdmTxYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 3),
    _NcmhdmTxYellowAlarm_Type()
)
ncmhdmTxYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTxYellowAlarm.setStatus("mandatory")


class _NcmhdmTxAIS_Type(Integer32):
    """Custom type ncmhdmTxAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dISABLE", 2),
          ("eNABLE", 1))
    )


_NcmhdmTxAIS_Type.__name__ = "Integer32"
_NcmhdmTxAIS_Object = MibTableColumn
ncmhdmTxAIS = _NcmhdmTxAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 4),
    _NcmhdmTxAIS_Type()
)
ncmhdmTxAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTxAIS.setStatus("mandatory")


class _NcmhdmTxIdleSignal_Type(Integer32):
    """Custom type ncmhdmTxIdleSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dISABLE", 2),
          ("eNABLE", 1))
    )


_NcmhdmTxIdleSignal_Type.__name__ = "Integer32"
_NcmhdmTxIdleSignal_Object = MibTableColumn
ncmhdmTxIdleSignal = _NcmhdmTxIdleSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 5),
    _NcmhdmTxIdleSignal_Type()
)
ncmhdmTxIdleSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTxIdleSignal.setStatus("mandatory")


class _NcmhdmTxFEBE_Type(Integer32):
    """Custom type ncmhdmTxFEBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dISABLE", 2),
          ("eNABLE", 1))
    )


_NcmhdmTxFEBE_Type.__name__ = "Integer32"
_NcmhdmTxFEBE_Object = MibTableColumn
ncmhdmTxFEBE = _NcmhdmTxFEBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 6),
    _NcmhdmTxFEBE_Type()
)
ncmhdmTxFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTxFEBE.setStatus("mandatory")


class _NcmhdmTxFEACAlarm_Type(Integer32):
    """Custom type ncmhdmTxFEACAlarm based on Integer32"""
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
        *(("aISReceived-Alarm", 5),
          ("commonEqptFailureNSA-Alarm", 8),
          ("eqptFailureNSA-Alarm", 7),
          ("eqptFailureSA-Alarm", 2),
          ("idleReceived-Alarm", 6),
          ("lOSHBER-Alarm", 3),
          ("nO-FEAC-Alarm-enabled", 1),
          ("oOF-Alarm", 4))
    )


_NcmhdmTxFEACAlarm_Type.__name__ = "Integer32"
_NcmhdmTxFEACAlarm_Object = MibTableColumn
ncmhdmTxFEACAlarm = _NcmhdmTxFEACAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9009, 1, 7),
    _NcmhdmTxFEACAlarm_Type()
)
ncmhdmTxFEACAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmTxFEACAlarm.setStatus("mandatory")
_NcmhdmDs3StatTable_Object = MibTable
ncmhdmDs3StatTable = _NcmhdmDs3StatTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010)
)
if mibBuilder.loadTexts:
    ncmhdmDs3StatTable.setStatus("mandatory")
_NcmhdmDs3StatEntry_Object = MibTableRow
ncmhdmDs3StatEntry = _NcmhdmDs3StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1)
)
ncmhdmDs3StatEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmDs3StatNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmDs3StatIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmDs3StatEntry.setStatus("mandatory")


class _NcmhdmDs3StatNIDIndex_Type(Integer32):
    """Custom type ncmhdmDs3StatNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmDs3StatNIDIndex_Type.__name__ = "Integer32"
_NcmhdmDs3StatNIDIndex_Object = MibTableColumn
ncmhdmDs3StatNIDIndex = _NcmhdmDs3StatNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 1),
    _NcmhdmDs3StatNIDIndex_Type()
)
ncmhdmDs3StatNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatNIDIndex.setStatus("mandatory")


class _NcmhdmDs3StatIndex_Type(Integer32):
    """Custom type ncmhdmDs3StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NcmhdmDs3StatIndex_Type.__name__ = "Integer32"
_NcmhdmDs3StatIndex_Object = MibTableColumn
ncmhdmDs3StatIndex = _NcmhdmDs3StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 2),
    _NcmhdmDs3StatIndex_Type()
)
ncmhdmDs3StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatIndex.setStatus("mandatory")


class _NcmhdmDs3StatAIS_Type(Integer32):
    """Custom type ncmhdmDs3StatAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatAIS_Type.__name__ = "Integer32"
_NcmhdmDs3StatAIS_Object = MibTableColumn
ncmhdmDs3StatAIS = _NcmhdmDs3StatAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 3),
    _NcmhdmDs3StatAIS_Type()
)
ncmhdmDs3StatAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatAIS.setStatus("mandatory")


class _NcmhdmDs3StatIdle_Type(Integer32):
    """Custom type ncmhdmDs3StatIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatIdle_Type.__name__ = "Integer32"
_NcmhdmDs3StatIdle_Object = MibTableColumn
ncmhdmDs3StatIdle = _NcmhdmDs3StatIdle_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 4),
    _NcmhdmDs3StatIdle_Type()
)
ncmhdmDs3StatIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatIdle.setStatus("mandatory")


class _NcmhdmDs3StatYellowAlm_Type(Integer32):
    """Custom type ncmhdmDs3StatYellowAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatYellowAlm_Type.__name__ = "Integer32"
_NcmhdmDs3StatYellowAlm_Object = MibTableColumn
ncmhdmDs3StatYellowAlm = _NcmhdmDs3StatYellowAlm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 5),
    _NcmhdmDs3StatYellowAlm_Type()
)
ncmhdmDs3StatYellowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatYellowAlm.setStatus("mandatory")


class _NcmhdmDs3StatFrameLoss_Type(Integer32):
    """Custom type ncmhdmDs3StatFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatFrameLoss_Type.__name__ = "Integer32"
_NcmhdmDs3StatFrameLoss_Object = MibTableColumn
ncmhdmDs3StatFrameLoss = _NcmhdmDs3StatFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 6),
    _NcmhdmDs3StatFrameLoss_Type()
)
ncmhdmDs3StatFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatFrameLoss.setStatus("mandatory")


class _NcmhdmDs3StatSigLoss_Type(Integer32):
    """Custom type ncmhdmDs3StatSigLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatSigLoss_Type.__name__ = "Integer32"
_NcmhdmDs3StatSigLoss_Object = MibTableColumn
ncmhdmDs3StatSigLoss = _NcmhdmDs3StatSigLoss_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 7),
    _NcmhdmDs3StatSigLoss_Type()
)
ncmhdmDs3StatSigLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatSigLoss.setStatus("mandatory")


class _NcmhdmDs3StatPLCPYellow_Type(Integer32):
    """Custom type ncmhdmDs3StatPLCPYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatPLCPYellow_Type.__name__ = "Integer32"
_NcmhdmDs3StatPLCPYellow_Object = MibTableColumn
ncmhdmDs3StatPLCPYellow = _NcmhdmDs3StatPLCPYellow_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 8),
    _NcmhdmDs3StatPLCPYellow_Type()
)
ncmhdmDs3StatPLCPYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatPLCPYellow.setStatus("mandatory")


class _NcmhdmDs3StatPLCPFrmLoss_Type(Integer32):
    """Custom type ncmhdmDs3StatPLCPFrmLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatPLCPFrmLoss_Type.__name__ = "Integer32"
_NcmhdmDs3StatPLCPFrmLoss_Object = MibTableColumn
ncmhdmDs3StatPLCPFrmLoss = _NcmhdmDs3StatPLCPFrmLoss_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 9),
    _NcmhdmDs3StatPLCPFrmLoss_Type()
)
ncmhdmDs3StatPLCPFrmLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatPLCPFrmLoss.setStatus("mandatory")


class _NcmhdmDs3StatPLCPOOF_Type(Integer32):
    """Custom type ncmhdmDs3StatPLCPOOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_NcmhdmDs3StatPLCPOOF_Type.__name__ = "Integer32"
_NcmhdmDs3StatPLCPOOF_Object = MibTableColumn
ncmhdmDs3StatPLCPOOF = _NcmhdmDs3StatPLCPOOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 10),
    _NcmhdmDs3StatPLCPOOF_Type()
)
ncmhdmDs3StatPLCPOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3StatPLCPOOF.setStatus("mandatory")


class _NcmhdmDs3LpbkLocal_Type(Integer32):
    """Custom type ncmhdmDs3LpbkLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3LpbkLocal_Type.__name__ = "Integer32"
_NcmhdmDs3LpbkLocal_Object = MibTableColumn
ncmhdmDs3LpbkLocal = _NcmhdmDs3LpbkLocal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 11),
    _NcmhdmDs3LpbkLocal_Type()
)
ncmhdmDs3LpbkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3LpbkLocal.setStatus("mandatory")


class _NcmhdmDs3LpbkPayload_Type(Integer32):
    """Custom type ncmhdmDs3LpbkPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3LpbkPayload_Type.__name__ = "Integer32"
_NcmhdmDs3LpbkPayload_Object = MibTableColumn
ncmhdmDs3LpbkPayload = _NcmhdmDs3LpbkPayload_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 12),
    _NcmhdmDs3LpbkPayload_Type()
)
ncmhdmDs3LpbkPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3LpbkPayload.setStatus("mandatory")


class _NcmhdmDs3LpbkFEAC_Type(Integer32):
    """Custom type ncmhdmDs3LpbkFEAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3LpbkFEAC_Type.__name__ = "Integer32"
_NcmhdmDs3LpbkFEAC_Object = MibTableColumn
ncmhdmDs3LpbkFEAC = _NcmhdmDs3LpbkFEAC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 13),
    _NcmhdmDs3LpbkFEAC_Type()
)
ncmhdmDs3LpbkFEAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3LpbkFEAC.setStatus("mandatory")


class _NcmhdmDs3LpbkFarEnd_Type(Integer32):
    """Custom type ncmhdmDs3LpbkFarEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmhdmDs3LpbkFarEnd_Type.__name__ = "Integer32"
_NcmhdmDs3LpbkFarEnd_Object = MibTableColumn
ncmhdmDs3LpbkFarEnd = _NcmhdmDs3LpbkFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9010, 1, 14),
    _NcmhdmDs3LpbkFarEnd_Type()
)
ncmhdmDs3LpbkFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmDs3LpbkFarEnd.setStatus("mandatory")
_Ncmhdmds3LPBKTable_Object = MibTable
ncmhdmds3LPBKTable = _Ncmhdmds3LPBKTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9011)
)
if mibBuilder.loadTexts:
    ncmhdmds3LPBKTable.setStatus("mandatory")
_Ncmhdmds3LPBKEntry_Object = MibTableRow
ncmhdmds3LPBKEntry = _Ncmhdmds3LPBKEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9011, 1)
)
ncmhdmds3LPBKEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmLPBKNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDS3-MIB", "ncmhdmds3LPBKIndex"),
)
if mibBuilder.loadTexts:
    ncmhdmds3LPBKEntry.setStatus("mandatory")


class _NcmhdmLPBKNIDIndex_Type(Integer32):
    """Custom type ncmhdmLPBKNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmhdmLPBKNIDIndex_Type.__name__ = "Integer32"
_NcmhdmLPBKNIDIndex_Object = MibTableColumn
ncmhdmLPBKNIDIndex = _NcmhdmLPBKNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9011, 1, 1),
    _NcmhdmLPBKNIDIndex_Type()
)
ncmhdmLPBKNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmLPBKNIDIndex.setStatus("mandatory")


class _Ncmhdmds3LPBKIndex_Type(Integer32):
    """Custom type ncmhdmds3LPBKIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmhdmds3LPBKIndex_Type.__name__ = "Integer32"
_Ncmhdmds3LPBKIndex_Object = MibTableColumn
ncmhdmds3LPBKIndex = _Ncmhdmds3LPBKIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9011, 1, 2),
    _Ncmhdmds3LPBKIndex_Type()
)
ncmhdmds3LPBKIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmhdmds3LPBKIndex.setStatus("mandatory")


class _NcmhdmDs3LPBKActivation_Type(Integer32):
    """Custom type ncmhdmDs3LPBKActivation based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dS3-Internal-Activate", 2),
          ("dS3-Internal-De-activate", 3),
          ("dS3-Payload-Activate", 4),
          ("dS3-Payload-De-activate", 5),
          ("fEAC-Activate", 10),
          ("fEAC-De-activate", 11),
          ("far-End-Lpbk-Activate", 12),
          ("far-End-Lpbk-De-activate", 13),
          ("hSSI-A-Activate", 6),
          ("hSSI-A-De-activate", 7),
          ("hSSI-B-Activate", 8),
          ("hSSI-B-De-activate", 9),
          ("no-Loopback", 1))
    )


_NcmhdmDs3LPBKActivation_Type.__name__ = "Integer32"
_NcmhdmDs3LPBKActivation_Object = MibTableColumn
ncmhdmDs3LPBKActivation = _NcmhdmDs3LPBKActivation_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036, 9011, 1, 3),
    _NcmhdmDs3LPBKActivation_Type()
)
ncmhdmDs3LPBKActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmhdmDs3LPBKActivation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMDS3-MIB",
    **{"ncmhdmDs3PortTable": ncmhdmDs3PortTable,
       "ncmhdmDs3PortEntry": ncmhdmDs3PortEntry,
       "ncmhdmDs3PortNIDIndex": ncmhdmDs3PortNIDIndex,
       "ncmhdmDs3PortIndex": ncmhdmDs3PortIndex,
       "ncmhdmDs3PerfControl": ncmhdmDs3PerfControl,
       "ncmhdmDs3LBOSelection": ncmhdmDs3LBOSelection,
       "ncmhdmDs3DataRateMode": ncmhdmDs3DataRateMode,
       "ncmhdmDs3Rate": ncmhdmDs3Rate,
       "ncmhdmDs3LineType": ncmhdmDs3LineType,
       "ncmhdmDs3LineCode": ncmhdmDs3LineCode,
       "ncmhdmDs3AISCBit": ncmhdmDs3AISCBit,
       "ncmhdmDs3EquipCode": ncmhdmDs3EquipCode,
       "ncmhdmDs3LocationIDCode": ncmhdmDs3LocationIDCode,
       "ncmhdmDs3FrameIDCode": ncmhdmDs3FrameIDCode,
       "ncmhdmDs3UnitCode": ncmhdmDs3UnitCode,
       "ncmhdmDs3FacilityIDCode": ncmhdmDs3FacilityIDCode,
       "ncmhdmDs3PortIdCode": ncmhdmDs3PortIdCode,
       "ncmhdmDs3CircuitID": ncmhdmDs3CircuitID,
       "ncmhdmDs3GenIDCode": ncmhdmDs3GenIDCode,
       "ncmhdmDs3Inband": ncmhdmDs3Inband,
       "ncmhdmHssi1PortTable": ncmhdmHssi1PortTable,
       "ncmhdmHssi1PortEntry": ncmhdmHssi1PortEntry,
       "ncmhdmDs3Hssi1NIDIndex": ncmhdmDs3Hssi1NIDIndex,
       "ncmhdmHssi1PortIndex": ncmhdmHssi1PortIndex,
       "ncmhdmHssi1ConfigMode": ncmhdmHssi1ConfigMode,
       "ncmhdmHssi1PortConfig": ncmhdmHssi1PortConfig,
       "ncmhdmHssi1TestMode": ncmhdmHssi1TestMode,
       "ncmhdmHssi1DataRateMode": ncmhdmHssi1DataRateMode,
       "ncmhdmHssi1HssiRate": ncmhdmHssi1HssiRate,
       "ncmhdmHssi1CircuitID": ncmhdmHssi1CircuitID,
       "ncmhdmHssiStatTable": ncmhdmHssiStatTable,
       "ncmhdmHssiStatEntry": ncmhdmHssiStatEntry,
       "ncmhdmHssiStatNIDIndex": ncmhdmHssiStatNIDIndex,
       "ncmhdmHssiStatIndex": ncmhdmHssiStatIndex,
       "ncmhdmStatDCEReady": ncmhdmStatDCEReady,
       "ncmhdmStatDTEReady": ncmhdmStatDTEReady,
       "ncmhdmStatLpbkA": ncmhdmStatLpbkA,
       "ncmhdmStatLpbkB": ncmhdmStatLpbkB,
       "ncmhdmStatTestMode": ncmhdmStatTestMode,
       "ncmhdmStatPortState": ncmhdmStatPortState,
       "ncmhdmStatCIMType": ncmhdmStatCIMType,
       "ncmhdmStatDiagStatus": ncmhdmStatDiagStatus,
       "ncmhdmCurrentTable": ncmhdmCurrentTable,
       "ncmhdmCurrentEntry": ncmhdmCurrentEntry,
       "ncmhdmCurrentNIDIndex": ncmhdmCurrentNIDIndex,
       "ncmhdmCurrentIndex": ncmhdmCurrentIndex,
       "ncmhdmCurrentCRC4Status": ncmhdmCurrentCRC4Status,
       "ncmhdmCurrentTimeStampSecs": ncmhdmCurrentTimeStampSecs,
       "ncmhdmCurrentTimeStampMSecs": ncmhdmCurrentTimeStampMSecs,
       "ncmhdmCurrentSecsElaps": ncmhdmCurrentSecsElaps,
       "ncmhdmCurrentFarEndCCV": ncmhdmCurrentFarEndCCV,
       "ncmhdmCurrentFarEndCES": ncmhdmCurrentFarEndCES,
       "ncmhdmCurrentFarEndCSES": ncmhdmCurrentFarEndCSES,
       "ncmhdmCurrentFarEndLUAS": ncmhdmCurrentFarEndLUAS,
       "ncmhdmCurrentLCV": ncmhdmCurrentLCV,
       "ncmhdmCurrentLES": ncmhdmCurrentLES,
       "ncmhdmCurrentLSESs": ncmhdmCurrentLSESs,
       "ncmhdmCurrentPCV": ncmhdmCurrentPCV,
       "ncmhdmCurrentPES": ncmhdmCurrentPES,
       "ncmhdmCurrentPSES": ncmhdmCurrentPSES,
       "ncmhdmCurrentCCV": ncmhdmCurrentCCV,
       "ncmhdmCurrentCES": ncmhdmCurrentCES,
       "ncmhdmCurrentCSES": ncmhdmCurrentCSES,
       "ncmhdmCurrentSEFS": ncmhdmCurrentSEFS,
       "ncmhdmCurrentAISS": ncmhdmCurrentAISS,
       "ncmhdmCurrentOOSSs": ncmhdmCurrentOOSSs,
       "ncmhdmCurrentLOSSs": ncmhdmCurrentLOSSs,
       "ncmhdmCurrentLOFSs": ncmhdmCurrentLOFSs,
       "ncmhdmIntervalTable": ncmhdmIntervalTable,
       "ncmhdmIntervalEntry": ncmhdmIntervalEntry,
       "ncmhdmIntervalNIDIndex": ncmhdmIntervalNIDIndex,
       "ncmhdmIntervalIndex": ncmhdmIntervalIndex,
       "ncmhdmIntervalNumber": ncmhdmIntervalNumber,
       "ncmhdmIntervalFarEndCCV": ncmhdmIntervalFarEndCCV,
       "ncmhdmIntervalFarEndCES": ncmhdmIntervalFarEndCES,
       "ncmhdmIntervalFarEndCSES": ncmhdmIntervalFarEndCSES,
       "ncmhdmIntervalFarEndLUAS": ncmhdmIntervalFarEndLUAS,
       "ncmhdmIntervalLCV": ncmhdmIntervalLCV,
       "ncmhdmIntervalLES": ncmhdmIntervalLES,
       "ncmhdmIntervalLSESs": ncmhdmIntervalLSESs,
       "ncmhdmIntervalPCV": ncmhdmIntervalPCV,
       "ncmhdmIntervalPES": ncmhdmIntervalPES,
       "ncmhdmIntervalPSES": ncmhdmIntervalPSES,
       "ncmhdmIntervalCCV": ncmhdmIntervalCCV,
       "ncmhdmIntervalCES": ncmhdmIntervalCES,
       "ncmhdmIntervalCSES": ncmhdmIntervalCSES,
       "ncmhdmIntervalSEFS": ncmhdmIntervalSEFS,
       "ncmhdmIntervalAISS": ncmhdmIntervalAISS,
       "ncmhdmIntervalOOSSs": ncmhdmIntervalOOSSs,
       "ncmhdmIntervalLOSSs": ncmhdmIntervalLOSSs,
       "ncmhdmIntervalLOFSs": ncmhdmIntervalLOFSs,
       "ncmhdmTotalTable": ncmhdmTotalTable,
       "ncmhdmTotalEntry": ncmhdmTotalEntry,
       "ncmhdmTotalNIDIndex": ncmhdmTotalNIDIndex,
       "ncmhdmTotalIndex": ncmhdmTotalIndex,
       "ncmhdmTotalCRC4Status": ncmhdmTotalCRC4Status,
       "ncmhdmTotalValidInterv": ncmhdmTotalValidInterv,
       "ncmhdmTotalFarEndCCV": ncmhdmTotalFarEndCCV,
       "ncmhdmTotalFarEndCES": ncmhdmTotalFarEndCES,
       "ncmhdmTotalFarEndCSES": ncmhdmTotalFarEndCSES,
       "ncmhdmTotalFarEndLUAS": ncmhdmTotalFarEndLUAS,
       "ncmhdmTotalLCV": ncmhdmTotalLCV,
       "ncmhdmTotalLES": ncmhdmTotalLES,
       "ncmhdmTotalLSESs": ncmhdmTotalLSESs,
       "ncmhdmTotalPCV": ncmhdmTotalPCV,
       "ncmhdmTotalPES": ncmhdmTotalPES,
       "ncmhdmTotalPSES": ncmhdmTotalPSES,
       "ncmhdmTotalCCV": ncmhdmTotalCCV,
       "ncmhdmTotalCES": ncmhdmTotalCES,
       "ncmhdmTotalCSES": ncmhdmTotalCSES,
       "ncmhdmTotalSEFS": ncmhdmTotalSEFS,
       "ncmhdmTotalAISS": ncmhdmTotalAISS,
       "ncmhdmTotalOOSSs": ncmhdmTotalOOSSs,
       "ncmhdmTotalLOSSs": ncmhdmTotalLOSSs,
       "ncmhdmTotalLOFSs": ncmhdmTotalLOFSs,
       "ncmDs3PerformanceSnapShotTable": ncmDs3PerformanceSnapShotTable,
       "ncmDs3PerformanceSnapShotEntry": ncmDs3PerformanceSnapShotEntry,
       "ncmDs3SnapShotNIDIndex": ncmDs3SnapShotNIDIndex,
       "ncmDs3SnapShotIndex": ncmDs3SnapShotIndex,
       "ncmDs3SnapShotCRC4Status": ncmDs3SnapShotCRC4Status,
       "ncmDs3SnapShot": ncmDs3SnapShot,
       "ncmDs3TimeStampSec": ncmDs3TimeStampSec,
       "ncmDs3TimeStampMilliSec": ncmDs3TimeStampMilliSec,
       "ncmDs3SnapShotSecs": ncmDs3SnapShotSecs,
       "ncmDs3ResetPerfReg": ncmDs3ResetPerfReg,
       "ncmhdmTCAQtrTable": ncmhdmTCAQtrTable,
       "ncmhdmTCAQtrEntry": ncmhdmTCAQtrEntry,
       "ncmhdmTCAQtrNIDIndex": ncmhdmTCAQtrNIDIndex,
       "ncmhdmTCAQtrIndex": ncmhdmTCAQtrIndex,
       "ncmhdmTCAQtrDs3FarEndCCV": ncmhdmTCAQtrDs3FarEndCCV,
       "ncmhdmTCAQtrDs3FarEndCES": ncmhdmTCAQtrDs3FarEndCES,
       "ncmhdmTCAQtrDs3FarEndCSES": ncmhdmTCAQtrDs3FarEndCSES,
       "ncmhdmTCAQtrDs3FarEndLUAS": ncmhdmTCAQtrDs3FarEndLUAS,
       "ncmhdmTCAQtrDs3LCV": ncmhdmTCAQtrDs3LCV,
       "ncmhdmTCAQtrDs3LES": ncmhdmTCAQtrDs3LES,
       "ncmhdmTCAQtrDs3LSESs": ncmhdmTCAQtrDs3LSESs,
       "ncmhdmTCAQtrDs3PCV": ncmhdmTCAQtrDs3PCV,
       "ncmhdmTCAQtrDs3PES": ncmhdmTCAQtrDs3PES,
       "ncmhdmTCAQtrDs3PSES": ncmhdmTCAQtrDs3PSES,
       "ncmhdmTCAQtrDs3CCV": ncmhdmTCAQtrDs3CCV,
       "ncmhdmTCAQtrDs3CES": ncmhdmTCAQtrDs3CES,
       "ncmhdmTCAQtrDs3CSES": ncmhdmTCAQtrDs3CSES,
       "ncmhdmTCAQtrDs3SEFS": ncmhdmTCAQtrDs3SEFS,
       "ncmhdmTCAQtrDs3AISS": ncmhdmTCAQtrDs3AISS,
       "ncmhdmTCAQtrDs3LUASs": ncmhdmTCAQtrDs3LUASs,
       "ncmhdmTCAQtrDs3LOSSs": ncmhdmTCAQtrDs3LOSSs,
       "ncmhdmTCAQtrDs3LOFSs": ncmhdmTCAQtrDs3LOFSs,
       "ncmhdmTCADayTable": ncmhdmTCADayTable,
       "ncmhdmTCADayEntry": ncmhdmTCADayEntry,
       "ncmhdmTCADayNIDIndex": ncmhdmTCADayNIDIndex,
       "ncmhdmTCADayIndex": ncmhdmTCADayIndex,
       "ncmhdmTCADayDs3FarEndCCV": ncmhdmTCADayDs3FarEndCCV,
       "ncmhdmTCADayDs3FarEndCES": ncmhdmTCADayDs3FarEndCES,
       "ncmhdmTCADayDs3FarEndCSES": ncmhdmTCADayDs3FarEndCSES,
       "ncmhdmTCADayDs3FarEndLUAS": ncmhdmTCADayDs3FarEndLUAS,
       "ncmhdmTCADayDs3LCV": ncmhdmTCADayDs3LCV,
       "ncmhdmTCADayDs3LES": ncmhdmTCADayDs3LES,
       "ncmhdmTCADayDs3LSESs": ncmhdmTCADayDs3LSESs,
       "ncmhdmTCADayDs3PCV": ncmhdmTCADayDs3PCV,
       "ncmhdmTCADayDs3PES": ncmhdmTCADayDs3PES,
       "ncmhdmTCADayDs3PSES": ncmhdmTCADayDs3PSES,
       "ncmhdmTCADayDs3CCV": ncmhdmTCADayDs3CCV,
       "ncmhdmTCADayDs3CES": ncmhdmTCADayDs3CES,
       "ncmhdmTCADayDs3CSES": ncmhdmTCADayDs3CSES,
       "ncmhdmTCADayDs3SEFS": ncmhdmTCADayDs3SEFS,
       "ncmhdmTCADayDs3AISS": ncmhdmTCADayDs3AISS,
       "ncmhdmTCADayDs3LUASs": ncmhdmTCADayDs3LUASs,
       "ncmhdmTCADayDs3LOSSs": ncmhdmTCADayDs3LOSSs,
       "ncmhdmTCADayDs3LOFSs": ncmhdmTCADayDs3LOFSs,
       "ncmhdmTxAlarmTable": ncmhdmTxAlarmTable,
       "ncmhdmTxAlarmEntry": ncmhdmTxAlarmEntry,
       "ncmhdmTxAlarmNIDIndex": ncmhdmTxAlarmNIDIndex,
       "ncmhdmTxAlarmIndex": ncmhdmTxAlarmIndex,
       "ncmhdmTxYellowAlarm": ncmhdmTxYellowAlarm,
       "ncmhdmTxAIS": ncmhdmTxAIS,
       "ncmhdmTxIdleSignal": ncmhdmTxIdleSignal,
       "ncmhdmTxFEBE": ncmhdmTxFEBE,
       "ncmhdmTxFEACAlarm": ncmhdmTxFEACAlarm,
       "ncmhdmDs3StatTable": ncmhdmDs3StatTable,
       "ncmhdmDs3StatEntry": ncmhdmDs3StatEntry,
       "ncmhdmDs3StatNIDIndex": ncmhdmDs3StatNIDIndex,
       "ncmhdmDs3StatIndex": ncmhdmDs3StatIndex,
       "ncmhdmDs3StatAIS": ncmhdmDs3StatAIS,
       "ncmhdmDs3StatIdle": ncmhdmDs3StatIdle,
       "ncmhdmDs3StatYellowAlm": ncmhdmDs3StatYellowAlm,
       "ncmhdmDs3StatFrameLoss": ncmhdmDs3StatFrameLoss,
       "ncmhdmDs3StatSigLoss": ncmhdmDs3StatSigLoss,
       "ncmhdmDs3StatPLCPYellow": ncmhdmDs3StatPLCPYellow,
       "ncmhdmDs3StatPLCPFrmLoss": ncmhdmDs3StatPLCPFrmLoss,
       "ncmhdmDs3StatPLCPOOF": ncmhdmDs3StatPLCPOOF,
       "ncmhdmDs3LpbkLocal": ncmhdmDs3LpbkLocal,
       "ncmhdmDs3LpbkPayload": ncmhdmDs3LpbkPayload,
       "ncmhdmDs3LpbkFEAC": ncmhdmDs3LpbkFEAC,
       "ncmhdmDs3LpbkFarEnd": ncmhdmDs3LpbkFarEnd,
       "ncmhdmds3LPBKTable": ncmhdmds3LPBKTable,
       "ncmhdmds3LPBKEntry": ncmhdmds3LPBKEntry,
       "ncmhdmLPBKNIDIndex": ncmhdmLPBKNIDIndex,
       "ncmhdmds3LPBKIndex": ncmhdmds3LPBKIndex,
       "ncmhdmDs3LPBKActivation": ncmhdmDs3LPBKActivation}
)
