# SNMP MIB module (VERILINK-ENTERPRISE-NCMM13-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMM13-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:18 2024
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

(ncm_m13,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-m13")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ncmm13DS3PortTable_Object = MibTable
ncmm13DS3PortTable = _Ncmm13DS3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000)
)
if mibBuilder.loadTexts:
    ncmm13DS3PortTable.setStatus("mandatory")
_Ncmm13DS3PortEntry_Object = MibTableRow
ncmm13DS3PortEntry = _Ncmm13DS3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1)
)
ncmm13DS3PortEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13DS3PortNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13DS3PortIndex"),
)
if mibBuilder.loadTexts:
    ncmm13DS3PortEntry.setStatus("mandatory")


class _Ncmm13DS3PortNIDIndex_Type(Integer32):
    """Custom type ncmm13DS3PortNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13DS3PortNIDIndex_Type.__name__ = "Integer32"
_Ncmm13DS3PortNIDIndex_Object = MibTableColumn
ncmm13DS3PortNIDIndex = _Ncmm13DS3PortNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 1),
    _Ncmm13DS3PortNIDIndex_Type()
)
ncmm13DS3PortNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3PortNIDIndex.setStatus("mandatory")


class _Ncmm13DS3PortIndex_Type(Integer32):
    """Custom type ncmm13DS3PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13DS3PortIndex_Type.__name__ = "Integer32"
_Ncmm13DS3PortIndex_Object = MibTableColumn
ncmm13DS3PortIndex = _Ncmm13DS3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 2),
    _Ncmm13DS3PortIndex_Type()
)
ncmm13DS3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3PortIndex.setStatus("mandatory")


class _Ncmm13DS3ModeControl_Type(Integer32):
    """Custom type ncmm13DS3ModeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c-bit", 1),
          ("m23-bit", 2))
    )


_Ncmm13DS3ModeControl_Type.__name__ = "Integer32"
_Ncmm13DS3ModeControl_Object = MibTableColumn
ncmm13DS3ModeControl = _Ncmm13DS3ModeControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 3),
    _Ncmm13DS3ModeControl_Type()
)
ncmm13DS3ModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3ModeControl.setStatus("mandatory")


class _Ncmm13DS3LineType_Type(Integer32):
    """Custom type ncmm13DS3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi-polar", 1),
          ("uni-polar", 2))
    )


_Ncmm13DS3LineType_Type.__name__ = "Integer32"
_Ncmm13DS3LineType_Object = MibTableColumn
ncmm13DS3LineType = _Ncmm13DS3LineType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 4),
    _Ncmm13DS3LineType_Type()
)
ncmm13DS3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3LineType.setStatus("mandatory")


class _Ncmm13DS3PerfControl_Type(Integer32):
    """Custom type ncmm13DS3PerfControl based on Integer32"""
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


_Ncmm13DS3PerfControl_Type.__name__ = "Integer32"
_Ncmm13DS3PerfControl_Object = MibTableColumn
ncmm13DS3PerfControl = _Ncmm13DS3PerfControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 5),
    _Ncmm13DS3PerfControl_Type()
)
ncmm13DS3PerfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3PerfControl.setStatus("mandatory")


class _Ncmm13DS3AlarmControl_Type(Integer32):
    """Custom type ncmm13DS3AlarmControl based on Integer32"""
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


_Ncmm13DS3AlarmControl_Type.__name__ = "Integer32"
_Ncmm13DS3AlarmControl_Object = MibTableColumn
ncmm13DS3AlarmControl = _Ncmm13DS3AlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 6),
    _Ncmm13DS3AlarmControl_Type()
)
ncmm13DS3AlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3AlarmControl.setStatus("mandatory")


class _Ncmm13DS3FarEndControl_Type(Integer32):
    """Custom type ncmm13DS3FarEndControl based on Integer32"""
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


_Ncmm13DS3FarEndControl_Type.__name__ = "Integer32"
_Ncmm13DS3FarEndControl_Object = MibTableColumn
ncmm13DS3FarEndControl = _Ncmm13DS3FarEndControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 7),
    _Ncmm13DS3FarEndControl_Type()
)
ncmm13DS3FarEndControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3FarEndControl.setStatus("mandatory")


class _Ncmm13DS3BusType_Type(Integer32):
    """Custom type ncmm13DS3BusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-bus", 2),
          ("c-bus", 1))
    )


_Ncmm13DS3BusType_Type.__name__ = "Integer32"
_Ncmm13DS3BusType_Object = MibTableColumn
ncmm13DS3BusType = _Ncmm13DS3BusType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 8),
    _Ncmm13DS3BusType_Type()
)
ncmm13DS3BusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3BusType.setStatus("mandatory")


class _Ncmm13DS3InbandControl_Type(Integer32):
    """Custom type ncmm13DS3InbandControl based on Integer32"""
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


_Ncmm13DS3InbandControl_Type.__name__ = "Integer32"
_Ncmm13DS3InbandControl_Object = MibTableColumn
ncmm13DS3InbandControl = _Ncmm13DS3InbandControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 9),
    _Ncmm13DS3InbandControl_Type()
)
ncmm13DS3InbandControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3InbandControl.setStatus("mandatory")


class _Ncmm13DS3CableLength_Type(Integer32):
    """Custom type ncmm13DS3CableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_Ncmm13DS3CableLength_Type.__name__ = "Integer32"
_Ncmm13DS3CableLength_Object = MibTableColumn
ncmm13DS3CableLength = _Ncmm13DS3CableLength_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 10),
    _Ncmm13DS3CableLength_Type()
)
ncmm13DS3CableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3CableLength.setStatus("mandatory")


class _Ncmm13DS3EquipCode_Type(DisplayString):
    """Custom type ncmm13DS3EquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ncmm13DS3EquipCode_Type.__name__ = "DisplayString"
_Ncmm13DS3EquipCode_Object = MibTableColumn
ncmm13DS3EquipCode = _Ncmm13DS3EquipCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 11),
    _Ncmm13DS3EquipCode_Type()
)
ncmm13DS3EquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3EquipCode.setStatus("mandatory")


class _Ncmm13DS3LocationIDCode_Type(DisplayString):
    """Custom type ncmm13DS3LocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Ncmm13DS3LocationIDCode_Type.__name__ = "DisplayString"
_Ncmm13DS3LocationIDCode_Object = MibTableColumn
ncmm13DS3LocationIDCode = _Ncmm13DS3LocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 12),
    _Ncmm13DS3LocationIDCode_Type()
)
ncmm13DS3LocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3LocationIDCode.setStatus("mandatory")


class _Ncmm13DS3FrameIDCode_Type(DisplayString):
    """Custom type ncmm13DS3FrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ncmm13DS3FrameIDCode_Type.__name__ = "DisplayString"
_Ncmm13DS3FrameIDCode_Object = MibTableColumn
ncmm13DS3FrameIDCode = _Ncmm13DS3FrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 13),
    _Ncmm13DS3FrameIDCode_Type()
)
ncmm13DS3FrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3FrameIDCode.setStatus("mandatory")


class _Ncmm13DS3UnitCode_Type(DisplayString):
    """Custom type ncmm13DS3UnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ncmm13DS3UnitCode_Type.__name__ = "DisplayString"
_Ncmm13DS3UnitCode_Object = MibTableColumn
ncmm13DS3UnitCode = _Ncmm13DS3UnitCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 14),
    _Ncmm13DS3UnitCode_Type()
)
ncmm13DS3UnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3UnitCode.setStatus("mandatory")


class _Ncmm13DS3FacilityIDCode_Type(DisplayString):
    """Custom type ncmm13DS3FacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_Ncmm13DS3FacilityIDCode_Type.__name__ = "DisplayString"
_Ncmm13DS3FacilityIDCode_Object = MibTableColumn
ncmm13DS3FacilityIDCode = _Ncmm13DS3FacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 15),
    _Ncmm13DS3FacilityIDCode_Type()
)
ncmm13DS3FacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3FacilityIDCode.setStatus("mandatory")


class _Ncmm13DS3PortIdCode_Type(DisplayString):
    """Custom type ncmm13DS3PortIdCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_Ncmm13DS3PortIdCode_Type.__name__ = "DisplayString"
_Ncmm13DS3PortIdCode_Object = MibTableColumn
ncmm13DS3PortIdCode = _Ncmm13DS3PortIdCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 16),
    _Ncmm13DS3PortIdCode_Type()
)
ncmm13DS3PortIdCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3PortIdCode.setStatus("mandatory")


class _Ncmm13DS3GenIDCode_Type(DisplayString):
    """Custom type ncmm13DS3GenIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_Ncmm13DS3GenIDCode_Type.__name__ = "DisplayString"
_Ncmm13DS3GenIDCode_Object = MibTableColumn
ncmm13DS3GenIDCode = _Ncmm13DS3GenIDCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14000, 1, 17),
    _Ncmm13DS3GenIDCode_Type()
)
ncmm13DS3GenIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3GenIDCode.setStatus("mandatory")
_Ncmm13StatTable_Object = MibTable
ncmm13StatTable = _Ncmm13StatTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001)
)
if mibBuilder.loadTexts:
    ncmm13StatTable.setStatus("mandatory")
_Ncmm13StatEntry_Object = MibTableRow
ncmm13StatEntry = _Ncmm13StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1)
)
ncmm13StatEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13StatNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13StatIndex"),
)
if mibBuilder.loadTexts:
    ncmm13StatEntry.setStatus("mandatory")


class _Ncmm13StatNIDIndex_Type(Integer32):
    """Custom type ncmm13StatNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13StatNIDIndex_Type.__name__ = "Integer32"
_Ncmm13StatNIDIndex_Object = MibTableColumn
ncmm13StatNIDIndex = _Ncmm13StatNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 1),
    _Ncmm13StatNIDIndex_Type()
)
ncmm13StatNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatNIDIndex.setStatus("mandatory")


class _Ncmm13StatIndex_Type(Integer32):
    """Custom type ncmm13StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13StatIndex_Type.__name__ = "Integer32"
_Ncmm13StatIndex_Object = MibTableColumn
ncmm13StatIndex = _Ncmm13StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 2),
    _Ncmm13StatIndex_Type()
)
ncmm13StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatIndex.setStatus("mandatory")


class _Ncmm13StatAIS_Type(Integer32):
    """Custom type ncmm13StatAIS based on Integer32"""
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


_Ncmm13StatAIS_Type.__name__ = "Integer32"
_Ncmm13StatAIS_Object = MibTableColumn
ncmm13StatAIS = _Ncmm13StatAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 3),
    _Ncmm13StatAIS_Type()
)
ncmm13StatAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatAIS.setStatus("mandatory")


class _Ncmm13StatIdle_Type(Integer32):
    """Custom type ncmm13StatIdle based on Integer32"""
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


_Ncmm13StatIdle_Type.__name__ = "Integer32"
_Ncmm13StatIdle_Object = MibTableColumn
ncmm13StatIdle = _Ncmm13StatIdle_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 4),
    _Ncmm13StatIdle_Type()
)
ncmm13StatIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatIdle.setStatus("mandatory")


class _Ncmm13StatYellowAlm_Type(Integer32):
    """Custom type ncmm13StatYellowAlm based on Integer32"""
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


_Ncmm13StatYellowAlm_Type.__name__ = "Integer32"
_Ncmm13StatYellowAlm_Object = MibTableColumn
ncmm13StatYellowAlm = _Ncmm13StatYellowAlm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 5),
    _Ncmm13StatYellowAlm_Type()
)
ncmm13StatYellowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatYellowAlm.setStatus("mandatory")


class _Ncmm13StatOOF_Type(Integer32):
    """Custom type ncmm13StatOOF based on Integer32"""
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


_Ncmm13StatOOF_Type.__name__ = "Integer32"
_Ncmm13StatOOF_Object = MibTableColumn
ncmm13StatOOF = _Ncmm13StatOOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 6),
    _Ncmm13StatOOF_Type()
)
ncmm13StatOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatOOF.setStatus("mandatory")


class _Ncmm13StatLOS_Type(Integer32):
    """Custom type ncmm13StatLOS based on Integer32"""
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


_Ncmm13StatLOS_Type.__name__ = "Integer32"
_Ncmm13StatLOS_Object = MibTableColumn
ncmm13StatLOS = _Ncmm13StatLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 7),
    _Ncmm13StatLOS_Type()
)
ncmm13StatLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13StatLOS.setStatus("mandatory")


class _Ncmm13DS3NearEndLocalLoopback_Type(Integer32):
    """Custom type ncmm13DS3NearEndLocalLoopback based on Integer32"""
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


_Ncmm13DS3NearEndLocalLoopback_Type.__name__ = "Integer32"
_Ncmm13DS3NearEndLocalLoopback_Object = MibTableColumn
ncmm13DS3NearEndLocalLoopback = _Ncmm13DS3NearEndLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 8),
    _Ncmm13DS3NearEndLocalLoopback_Type()
)
ncmm13DS3NearEndLocalLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3NearEndLocalLoopback.setStatus("mandatory")


class _Ncmm13DS3NearEndLineLoopback_Type(Integer32):
    """Custom type ncmm13DS3NearEndLineLoopback based on Integer32"""
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


_Ncmm13DS3NearEndLineLoopback_Type.__name__ = "Integer32"
_Ncmm13DS3NearEndLineLoopback_Object = MibTableColumn
ncmm13DS3NearEndLineLoopback = _Ncmm13DS3NearEndLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 9),
    _Ncmm13DS3NearEndLineLoopback_Type()
)
ncmm13DS3NearEndLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3NearEndLineLoopback.setStatus("mandatory")


class _Ncmm13DS3FarEndLineLoopback_Type(Integer32):
    """Custom type ncmm13DS3FarEndLineLoopback based on Integer32"""
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


_Ncmm13DS3FarEndLineLoopback_Type.__name__ = "Integer32"
_Ncmm13DS3FarEndLineLoopback_Object = MibTableColumn
ncmm13DS3FarEndLineLoopback = _Ncmm13DS3FarEndLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 10),
    _Ncmm13DS3FarEndLineLoopback_Type()
)
ncmm13DS3FarEndLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3FarEndLineLoopback.setStatus("mandatory")
_Ncmm13T1NearEndLineLoopback_Type = DisplayString
_Ncmm13T1NearEndLineLoopback_Object = MibTableColumn
ncmm13T1NearEndLineLoopback = _Ncmm13T1NearEndLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 11),
    _Ncmm13T1NearEndLineLoopback_Type()
)
ncmm13T1NearEndLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1NearEndLineLoopback.setStatus("mandatory")
_Ncmm13T1FarEndLineLoopback_Type = DisplayString
_Ncmm13T1FarEndLineLoopback_Object = MibTableColumn
ncmm13T1FarEndLineLoopback = _Ncmm13T1FarEndLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 12),
    _Ncmm13T1FarEndLineLoopback_Type()
)
ncmm13T1FarEndLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1FarEndLineLoopback.setStatus("mandatory")


class _Ncmm13FarEndAllT1LineLoopback_Type(Integer32):
    """Custom type ncmm13FarEndAllT1LineLoopback based on Integer32"""
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


_Ncmm13FarEndAllT1LineLoopback_Type.__name__ = "Integer32"
_Ncmm13FarEndAllT1LineLoopback_Object = MibTableColumn
ncmm13FarEndAllT1LineLoopback = _Ncmm13FarEndAllT1LineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 13),
    _Ncmm13FarEndAllT1LineLoopback_Type()
)
ncmm13FarEndAllT1LineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13FarEndAllT1LineLoopback.setStatus("mandatory")
_Ncmm13T1LocalLoopback_Type = DisplayString
_Ncmm13T1LocalLoopback_Object = MibTableColumn
ncmm13T1LocalLoopback = _Ncmm13T1LocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14001, 1, 14),
    _Ncmm13T1LocalLoopback_Type()
)
ncmm13T1LocalLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1LocalLoopback.setStatus("mandatory")
_Ncmm13CurrentTable_Object = MibTable
ncmm13CurrentTable = _Ncmm13CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002)
)
if mibBuilder.loadTexts:
    ncmm13CurrentTable.setStatus("mandatory")
_Ncmm13CurrentEntry_Object = MibTableRow
ncmm13CurrentEntry = _Ncmm13CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1)
)
ncmm13CurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13CurrentNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13CurrentIndex"),
)
if mibBuilder.loadTexts:
    ncmm13CurrentEntry.setStatus("mandatory")


class _Ncmm13CurrentNIDIndex_Type(Integer32):
    """Custom type ncmm13CurrentNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13CurrentNIDIndex_Type.__name__ = "Integer32"
_Ncmm13CurrentNIDIndex_Object = MibTableColumn
ncmm13CurrentNIDIndex = _Ncmm13CurrentNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 1),
    _Ncmm13CurrentNIDIndex_Type()
)
ncmm13CurrentNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentNIDIndex.setStatus("mandatory")


class _Ncmm13CurrentIndex_Type(Integer32):
    """Custom type ncmm13CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13CurrentIndex_Type.__name__ = "Integer32"
_Ncmm13CurrentIndex_Object = MibTableColumn
ncmm13CurrentIndex = _Ncmm13CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 2),
    _Ncmm13CurrentIndex_Type()
)
ncmm13CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentIndex.setStatus("mandatory")


class _Ncmm13CurrentCRCStatus_Type(Integer32):
    """Custom type ncmm13CurrentCRCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_Ncmm13CurrentCRCStatus_Type.__name__ = "Integer32"
_Ncmm13CurrentCRCStatus_Object = MibTableColumn
ncmm13CurrentCRCStatus = _Ncmm13CurrentCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 3),
    _Ncmm13CurrentCRCStatus_Type()
)
ncmm13CurrentCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentCRCStatus.setStatus("mandatory")


class _Ncmm13CurrentTimeStampSecs_Type(Integer32):
    """Custom type ncmm13CurrentTimeStampSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13CurrentTimeStampSecs_Type.__name__ = "Integer32"
_Ncmm13CurrentTimeStampSecs_Object = MibTableColumn
ncmm13CurrentTimeStampSecs = _Ncmm13CurrentTimeStampSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 4),
    _Ncmm13CurrentTimeStampSecs_Type()
)
ncmm13CurrentTimeStampSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentTimeStampSecs.setStatus("mandatory")


class _Ncmm13CurrentTimeStampMSecs_Type(Integer32):
    """Custom type ncmm13CurrentTimeStampMSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13CurrentTimeStampMSecs_Type.__name__ = "Integer32"
_Ncmm13CurrentTimeStampMSecs_Object = MibTableColumn
ncmm13CurrentTimeStampMSecs = _Ncmm13CurrentTimeStampMSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 5),
    _Ncmm13CurrentTimeStampMSecs_Type()
)
ncmm13CurrentTimeStampMSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentTimeStampMSecs.setStatus("mandatory")


class _Ncmm13CurrentIntervalSecsElaps_Type(Integer32):
    """Custom type ncmm13CurrentIntervalSecsElaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13CurrentIntervalSecsElaps_Type.__name__ = "Integer32"
_Ncmm13CurrentIntervalSecsElaps_Object = MibTableColumn
ncmm13CurrentIntervalSecsElaps = _Ncmm13CurrentIntervalSecsElaps_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 6),
    _Ncmm13CurrentIntervalSecsElaps_Type()
)
ncmm13CurrentIntervalSecsElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentIntervalSecsElaps.setStatus("mandatory")
_Ncmm13CurrentFarEndCCV_Type = Gauge32
_Ncmm13CurrentFarEndCCV_Object = MibTableColumn
ncmm13CurrentFarEndCCV = _Ncmm13CurrentFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 7),
    _Ncmm13CurrentFarEndCCV_Type()
)
ncmm13CurrentFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentFarEndCCV.setStatus("mandatory")
_Ncmm13CurrentFarEndCES_Type = Gauge32
_Ncmm13CurrentFarEndCES_Object = MibTableColumn
ncmm13CurrentFarEndCES = _Ncmm13CurrentFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 8),
    _Ncmm13CurrentFarEndCES_Type()
)
ncmm13CurrentFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentFarEndCES.setStatus("mandatory")
_Ncmm13CurrentFarEndCSES_Type = Gauge32
_Ncmm13CurrentFarEndCSES_Object = MibTableColumn
ncmm13CurrentFarEndCSES = _Ncmm13CurrentFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 9),
    _Ncmm13CurrentFarEndCSES_Type()
)
ncmm13CurrentFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentFarEndCSES.setStatus("mandatory")
_Ncmm13CurrentFarEndLUAS_Type = Gauge32
_Ncmm13CurrentFarEndLUAS_Object = MibTableColumn
ncmm13CurrentFarEndLUAS = _Ncmm13CurrentFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 10),
    _Ncmm13CurrentFarEndLUAS_Type()
)
ncmm13CurrentFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentFarEndLUAS.setStatus("mandatory")
_Ncmm13CurrentLCV_Type = Gauge32
_Ncmm13CurrentLCV_Object = MibTableColumn
ncmm13CurrentLCV = _Ncmm13CurrentLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 11),
    _Ncmm13CurrentLCV_Type()
)
ncmm13CurrentLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLCV.setStatus("mandatory")
_Ncmm13CurrentLES_Type = Gauge32
_Ncmm13CurrentLES_Object = MibTableColumn
ncmm13CurrentLES = _Ncmm13CurrentLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 12),
    _Ncmm13CurrentLES_Type()
)
ncmm13CurrentLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLES.setStatus("mandatory")
_Ncmm13CurrentLSES_Type = Gauge32
_Ncmm13CurrentLSES_Object = MibTableColumn
ncmm13CurrentLSES = _Ncmm13CurrentLSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 13),
    _Ncmm13CurrentLSES_Type()
)
ncmm13CurrentLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLSES.setStatus("mandatory")
_Ncmm13CurrentPCV_Type = Gauge32
_Ncmm13CurrentPCV_Object = MibTableColumn
ncmm13CurrentPCV = _Ncmm13CurrentPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 14),
    _Ncmm13CurrentPCV_Type()
)
ncmm13CurrentPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentPCV.setStatus("mandatory")
_Ncmm13CurrentPES_Type = Gauge32
_Ncmm13CurrentPES_Object = MibTableColumn
ncmm13CurrentPES = _Ncmm13CurrentPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 15),
    _Ncmm13CurrentPES_Type()
)
ncmm13CurrentPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentPES.setStatus("mandatory")
_Ncmm13CurrentPSES_Type = Gauge32
_Ncmm13CurrentPSES_Object = MibTableColumn
ncmm13CurrentPSES = _Ncmm13CurrentPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 16),
    _Ncmm13CurrentPSES_Type()
)
ncmm13CurrentPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentPSES.setStatus("mandatory")
_Ncmm13CurrentCCV_Type = Gauge32
_Ncmm13CurrentCCV_Object = MibTableColumn
ncmm13CurrentCCV = _Ncmm13CurrentCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 17),
    _Ncmm13CurrentCCV_Type()
)
ncmm13CurrentCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentCCV.setStatus("mandatory")
_Ncmm13CurrentCES_Type = Gauge32
_Ncmm13CurrentCES_Object = MibTableColumn
ncmm13CurrentCES = _Ncmm13CurrentCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 18),
    _Ncmm13CurrentCES_Type()
)
ncmm13CurrentCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentCES.setStatus("mandatory")
_Ncmm13CurrentCSES_Type = Gauge32
_Ncmm13CurrentCSES_Object = MibTableColumn
ncmm13CurrentCSES = _Ncmm13CurrentCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 19),
    _Ncmm13CurrentCSES_Type()
)
ncmm13CurrentCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentCSES.setStatus("mandatory")
_Ncmm13CurrentSEFS_Type = Gauge32
_Ncmm13CurrentSEFS_Object = MibTableColumn
ncmm13CurrentSEFS = _Ncmm13CurrentSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 20),
    _Ncmm13CurrentSEFS_Type()
)
ncmm13CurrentSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentSEFS.setStatus("mandatory")
_Ncmm13CurrentAISS_Type = Gauge32
_Ncmm13CurrentAISS_Object = MibTableColumn
ncmm13CurrentAISS = _Ncmm13CurrentAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 21),
    _Ncmm13CurrentAISS_Type()
)
ncmm13CurrentAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentAISS.setStatus("mandatory")
_Ncmm13CurrentLUAS_Type = Gauge32
_Ncmm13CurrentLUAS_Object = MibTableColumn
ncmm13CurrentLUAS = _Ncmm13CurrentLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 22),
    _Ncmm13CurrentLUAS_Type()
)
ncmm13CurrentLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLUAS.setStatus("mandatory")
_Ncmm13CurrentLOOS_Type = Gauge32
_Ncmm13CurrentLOOS_Object = MibTableColumn
ncmm13CurrentLOOS = _Ncmm13CurrentLOOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 23),
    _Ncmm13CurrentLOOS_Type()
)
ncmm13CurrentLOOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLOOS.setStatus("mandatory")
_Ncmm13CurrentLOFS_Type = Gauge32
_Ncmm13CurrentLOFS_Object = MibTableColumn
ncmm13CurrentLOFS = _Ncmm13CurrentLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14002, 1, 24),
    _Ncmm13CurrentLOFS_Type()
)
ncmm13CurrentLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13CurrentLOFS.setStatus("mandatory")
_Ncmm13IntervalTable_Object = MibTable
ncmm13IntervalTable = _Ncmm13IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003)
)
if mibBuilder.loadTexts:
    ncmm13IntervalTable.setStatus("mandatory")
_Ncmm13IntervalEntry_Object = MibTableRow
ncmm13IntervalEntry = _Ncmm13IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1)
)
ncmm13IntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13IntervalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13IntervalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13IntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmm13IntervalEntry.setStatus("mandatory")


class _Ncmm13IntervalNIDIndex_Type(Integer32):
    """Custom type ncmm13IntervalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13IntervalNIDIndex_Type.__name__ = "Integer32"
_Ncmm13IntervalNIDIndex_Object = MibTableColumn
ncmm13IntervalNIDIndex = _Ncmm13IntervalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 1),
    _Ncmm13IntervalNIDIndex_Type()
)
ncmm13IntervalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalNIDIndex.setStatus("mandatory")


class _Ncmm13IntervalIndex_Type(Integer32):
    """Custom type ncmm13IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13IntervalIndex_Type.__name__ = "Integer32"
_Ncmm13IntervalIndex_Object = MibTableColumn
ncmm13IntervalIndex = _Ncmm13IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 2),
    _Ncmm13IntervalIndex_Type()
)
ncmm13IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalIndex.setStatus("mandatory")


class _Ncmm13IntervalNumber_Type(Integer32):
    """Custom type ncmm13IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ncmm13IntervalNumber_Type.__name__ = "Integer32"
_Ncmm13IntervalNumber_Object = MibTableColumn
ncmm13IntervalNumber = _Ncmm13IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 3),
    _Ncmm13IntervalNumber_Type()
)
ncmm13IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalNumber.setStatus("mandatory")
_Ncmm13IntervalFarEndCCV_Type = Gauge32
_Ncmm13IntervalFarEndCCV_Object = MibTableColumn
ncmm13IntervalFarEndCCV = _Ncmm13IntervalFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 4),
    _Ncmm13IntervalFarEndCCV_Type()
)
ncmm13IntervalFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalFarEndCCV.setStatus("mandatory")
_Ncmm13IntervalFarEndCES_Type = Gauge32
_Ncmm13IntervalFarEndCES_Object = MibTableColumn
ncmm13IntervalFarEndCES = _Ncmm13IntervalFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 5),
    _Ncmm13IntervalFarEndCES_Type()
)
ncmm13IntervalFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalFarEndCES.setStatus("mandatory")
_Ncmm13IntervalFarEndCSES_Type = Gauge32
_Ncmm13IntervalFarEndCSES_Object = MibTableColumn
ncmm13IntervalFarEndCSES = _Ncmm13IntervalFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 6),
    _Ncmm13IntervalFarEndCSES_Type()
)
ncmm13IntervalFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalFarEndCSES.setStatus("mandatory")
_Ncmm13IntervalFarEndLUAS_Type = Gauge32
_Ncmm13IntervalFarEndLUAS_Object = MibTableColumn
ncmm13IntervalFarEndLUAS = _Ncmm13IntervalFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 7),
    _Ncmm13IntervalFarEndLUAS_Type()
)
ncmm13IntervalFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalFarEndLUAS.setStatus("mandatory")
_Ncmm13IntervalLCV_Type = Gauge32
_Ncmm13IntervalLCV_Object = MibTableColumn
ncmm13IntervalLCV = _Ncmm13IntervalLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 8),
    _Ncmm13IntervalLCV_Type()
)
ncmm13IntervalLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLCV.setStatus("mandatory")
_Ncmm13IntervalLES_Type = Gauge32
_Ncmm13IntervalLES_Object = MibTableColumn
ncmm13IntervalLES = _Ncmm13IntervalLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 9),
    _Ncmm13IntervalLES_Type()
)
ncmm13IntervalLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLES.setStatus("mandatory")
_Ncmm13IntervalLSES_Type = Gauge32
_Ncmm13IntervalLSES_Object = MibTableColumn
ncmm13IntervalLSES = _Ncmm13IntervalLSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 10),
    _Ncmm13IntervalLSES_Type()
)
ncmm13IntervalLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLSES.setStatus("mandatory")
_Ncmm13IntervalPCV_Type = Gauge32
_Ncmm13IntervalPCV_Object = MibTableColumn
ncmm13IntervalPCV = _Ncmm13IntervalPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 11),
    _Ncmm13IntervalPCV_Type()
)
ncmm13IntervalPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalPCV.setStatus("mandatory")
_Ncmm13IntervalPES_Type = Gauge32
_Ncmm13IntervalPES_Object = MibTableColumn
ncmm13IntervalPES = _Ncmm13IntervalPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 12),
    _Ncmm13IntervalPES_Type()
)
ncmm13IntervalPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalPES.setStatus("mandatory")
_Ncmm13IntervalPSES_Type = Gauge32
_Ncmm13IntervalPSES_Object = MibTableColumn
ncmm13IntervalPSES = _Ncmm13IntervalPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 13),
    _Ncmm13IntervalPSES_Type()
)
ncmm13IntervalPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalPSES.setStatus("mandatory")
_Ncmm13IntervalCCV_Type = Gauge32
_Ncmm13IntervalCCV_Object = MibTableColumn
ncmm13IntervalCCV = _Ncmm13IntervalCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 14),
    _Ncmm13IntervalCCV_Type()
)
ncmm13IntervalCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalCCV.setStatus("mandatory")
_Ncmm13IntervalCES_Type = Gauge32
_Ncmm13IntervalCES_Object = MibTableColumn
ncmm13IntervalCES = _Ncmm13IntervalCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 15),
    _Ncmm13IntervalCES_Type()
)
ncmm13IntervalCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalCES.setStatus("mandatory")
_Ncmm13IntervalCSES_Type = Gauge32
_Ncmm13IntervalCSES_Object = MibTableColumn
ncmm13IntervalCSES = _Ncmm13IntervalCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 16),
    _Ncmm13IntervalCSES_Type()
)
ncmm13IntervalCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalCSES.setStatus("mandatory")
_Ncmm13IntervalSEFS_Type = Gauge32
_Ncmm13IntervalSEFS_Object = MibTableColumn
ncmm13IntervalSEFS = _Ncmm13IntervalSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 17),
    _Ncmm13IntervalSEFS_Type()
)
ncmm13IntervalSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalSEFS.setStatus("mandatory")
_Ncmm13IntervalAISS_Type = Gauge32
_Ncmm13IntervalAISS_Object = MibTableColumn
ncmm13IntervalAISS = _Ncmm13IntervalAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 18),
    _Ncmm13IntervalAISS_Type()
)
ncmm13IntervalAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalAISS.setStatus("mandatory")
_Ncmm13IntervalLUAS_Type = Gauge32
_Ncmm13IntervalLUAS_Object = MibTableColumn
ncmm13IntervalLUAS = _Ncmm13IntervalLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 19),
    _Ncmm13IntervalLUAS_Type()
)
ncmm13IntervalLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLUAS.setStatus("mandatory")
_Ncmm13IntervalLOSS_Type = Gauge32
_Ncmm13IntervalLOSS_Object = MibTableColumn
ncmm13IntervalLOSS = _Ncmm13IntervalLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 20),
    _Ncmm13IntervalLOSS_Type()
)
ncmm13IntervalLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLOSS.setStatus("mandatory")
_Ncmm13IntervalLOFS_Type = Gauge32
_Ncmm13IntervalLOFS_Object = MibTableColumn
ncmm13IntervalLOFS = _Ncmm13IntervalLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14003, 1, 21),
    _Ncmm13IntervalLOFS_Type()
)
ncmm13IntervalLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13IntervalLOFS.setStatus("mandatory")
_Ncmm13TotalTable_Object = MibTable
ncmm13TotalTable = _Ncmm13TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004)
)
if mibBuilder.loadTexts:
    ncmm13TotalTable.setStatus("mandatory")
_Ncmm13TotalEntry_Object = MibTableRow
ncmm13TotalEntry = _Ncmm13TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1)
)
ncmm13TotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TotalIndex"),
)
if mibBuilder.loadTexts:
    ncmm13TotalEntry.setStatus("mandatory")


class _Ncmm13TotalNIDIndex_Type(Integer32):
    """Custom type ncmm13TotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13TotalNIDIndex_Type.__name__ = "Integer32"
_Ncmm13TotalNIDIndex_Object = MibTableColumn
ncmm13TotalNIDIndex = _Ncmm13TotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 1),
    _Ncmm13TotalNIDIndex_Type()
)
ncmm13TotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalNIDIndex.setStatus("mandatory")


class _Ncmm13TotalIndex_Type(Integer32):
    """Custom type ncmm13TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TotalIndex_Type.__name__ = "Integer32"
_Ncmm13TotalIndex_Object = MibTableColumn
ncmm13TotalIndex = _Ncmm13TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 2),
    _Ncmm13TotalIndex_Type()
)
ncmm13TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalIndex.setStatus("mandatory")


class _Ncmm13TotalCRCStatus_Type(Integer32):
    """Custom type ncmm13TotalCRCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_Ncmm13TotalCRCStatus_Type.__name__ = "Integer32"
_Ncmm13TotalCRCStatus_Object = MibTableColumn
ncmm13TotalCRCStatus = _Ncmm13TotalCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 3),
    _Ncmm13TotalCRCStatus_Type()
)
ncmm13TotalCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalCRCStatus.setStatus("mandatory")


class _Ncmm13TotalValidInterv_Type(Integer32):
    """Custom type ncmm13TotalValidInterv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TotalValidInterv_Type.__name__ = "Integer32"
_Ncmm13TotalValidInterv_Object = MibTableColumn
ncmm13TotalValidInterv = _Ncmm13TotalValidInterv_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 4),
    _Ncmm13TotalValidInterv_Type()
)
ncmm13TotalValidInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalValidInterv.setStatus("mandatory")
_Ncmm13TotalFarEndCCV_Type = Gauge32
_Ncmm13TotalFarEndCCV_Object = MibTableColumn
ncmm13TotalFarEndCCV = _Ncmm13TotalFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 5),
    _Ncmm13TotalFarEndCCV_Type()
)
ncmm13TotalFarEndCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalFarEndCCV.setStatus("mandatory")
_Ncmm13TotalFarEndCES_Type = Gauge32
_Ncmm13TotalFarEndCES_Object = MibTableColumn
ncmm13TotalFarEndCES = _Ncmm13TotalFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 6),
    _Ncmm13TotalFarEndCES_Type()
)
ncmm13TotalFarEndCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalFarEndCES.setStatus("mandatory")
_Ncmm13TotalFarEndCSES_Type = Gauge32
_Ncmm13TotalFarEndCSES_Object = MibTableColumn
ncmm13TotalFarEndCSES = _Ncmm13TotalFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 7),
    _Ncmm13TotalFarEndCSES_Type()
)
ncmm13TotalFarEndCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalFarEndCSES.setStatus("mandatory")
_Ncmm13TotalFarEndLUAS_Type = Gauge32
_Ncmm13TotalFarEndLUAS_Object = MibTableColumn
ncmm13TotalFarEndLUAS = _Ncmm13TotalFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 8),
    _Ncmm13TotalFarEndLUAS_Type()
)
ncmm13TotalFarEndLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalFarEndLUAS.setStatus("mandatory")
_Ncmm13TotalLCV_Type = Gauge32
_Ncmm13TotalLCV_Object = MibTableColumn
ncmm13TotalLCV = _Ncmm13TotalLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 9),
    _Ncmm13TotalLCV_Type()
)
ncmm13TotalLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLCV.setStatus("mandatory")
_Ncmm13TotalLES_Type = Gauge32
_Ncmm13TotalLES_Object = MibTableColumn
ncmm13TotalLES = _Ncmm13TotalLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 10),
    _Ncmm13TotalLES_Type()
)
ncmm13TotalLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLES.setStatus("mandatory")
_Ncmm13TotalLSES_Type = Gauge32
_Ncmm13TotalLSES_Object = MibTableColumn
ncmm13TotalLSES = _Ncmm13TotalLSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 11),
    _Ncmm13TotalLSES_Type()
)
ncmm13TotalLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLSES.setStatus("mandatory")
_Ncmm13TotalPCV_Type = Gauge32
_Ncmm13TotalPCV_Object = MibTableColumn
ncmm13TotalPCV = _Ncmm13TotalPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 12),
    _Ncmm13TotalPCV_Type()
)
ncmm13TotalPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalPCV.setStatus("mandatory")
_Ncmm13TotalPES_Type = Gauge32
_Ncmm13TotalPES_Object = MibTableColumn
ncmm13TotalPES = _Ncmm13TotalPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 13),
    _Ncmm13TotalPES_Type()
)
ncmm13TotalPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalPES.setStatus("mandatory")
_Ncmm13TotalPSES_Type = Gauge32
_Ncmm13TotalPSES_Object = MibTableColumn
ncmm13TotalPSES = _Ncmm13TotalPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 14),
    _Ncmm13TotalPSES_Type()
)
ncmm13TotalPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalPSES.setStatus("mandatory")
_Ncmm13TotalCCV_Type = Gauge32
_Ncmm13TotalCCV_Object = MibTableColumn
ncmm13TotalCCV = _Ncmm13TotalCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 15),
    _Ncmm13TotalCCV_Type()
)
ncmm13TotalCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalCCV.setStatus("mandatory")
_Ncmm13TotalCES_Type = Gauge32
_Ncmm13TotalCES_Object = MibTableColumn
ncmm13TotalCES = _Ncmm13TotalCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 16),
    _Ncmm13TotalCES_Type()
)
ncmm13TotalCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalCES.setStatus("mandatory")
_Ncmm13TotalCSES_Type = Gauge32
_Ncmm13TotalCSES_Object = MibTableColumn
ncmm13TotalCSES = _Ncmm13TotalCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 17),
    _Ncmm13TotalCSES_Type()
)
ncmm13TotalCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalCSES.setStatus("mandatory")
_Ncmm13TotalSEFS_Type = Gauge32
_Ncmm13TotalSEFS_Object = MibTableColumn
ncmm13TotalSEFS = _Ncmm13TotalSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 18),
    _Ncmm13TotalSEFS_Type()
)
ncmm13TotalSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalSEFS.setStatus("mandatory")
_Ncmm13TotalAISS_Type = Gauge32
_Ncmm13TotalAISS_Object = MibTableColumn
ncmm13TotalAISS = _Ncmm13TotalAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 19),
    _Ncmm13TotalAISS_Type()
)
ncmm13TotalAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalAISS.setStatus("mandatory")
_Ncmm13TotalLUAS_Type = Gauge32
_Ncmm13TotalLUAS_Object = MibTableColumn
ncmm13TotalLUAS = _Ncmm13TotalLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 20),
    _Ncmm13TotalLUAS_Type()
)
ncmm13TotalLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLUAS.setStatus("mandatory")
_Ncmm13TotalLOSS_Type = Gauge32
_Ncmm13TotalLOSS_Object = MibTableColumn
ncmm13TotalLOSS = _Ncmm13TotalLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 21),
    _Ncmm13TotalLOSS_Type()
)
ncmm13TotalLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLOSS.setStatus("mandatory")
_Ncmm13TotalLOFS_Type = Gauge32
_Ncmm13TotalLOFS_Object = MibTableColumn
ncmm13TotalLOFS = _Ncmm13TotalLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14004, 1, 22),
    _Ncmm13TotalLOFS_Type()
)
ncmm13TotalLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TotalLOFS.setStatus("mandatory")
_Ncmm13PerformanceSnapShotTable_Object = MibTable
ncmm13PerformanceSnapShotTable = _Ncmm13PerformanceSnapShotTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005)
)
if mibBuilder.loadTexts:
    ncmm13PerformanceSnapShotTable.setStatus("mandatory")
_Ncmm13PerformanceSnapShotEntry_Object = MibTableRow
ncmm13PerformanceSnapShotEntry = _Ncmm13PerformanceSnapShotEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1)
)
ncmm13PerformanceSnapShotEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13SnapShotNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13SnapShotIndex"),
)
if mibBuilder.loadTexts:
    ncmm13PerformanceSnapShotEntry.setStatus("mandatory")


class _Ncmm13SnapShotNIDIndex_Type(Integer32):
    """Custom type ncmm13SnapShotNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13SnapShotNIDIndex_Type.__name__ = "Integer32"
_Ncmm13SnapShotNIDIndex_Object = MibTableColumn
ncmm13SnapShotNIDIndex = _Ncmm13SnapShotNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 1),
    _Ncmm13SnapShotNIDIndex_Type()
)
ncmm13SnapShotNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13SnapShotNIDIndex.setStatus("mandatory")


class _Ncmm13SnapShotIndex_Type(Integer32):
    """Custom type ncmm13SnapShotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13SnapShotIndex_Type.__name__ = "Integer32"
_Ncmm13SnapShotIndex_Object = MibTableColumn
ncmm13SnapShotIndex = _Ncmm13SnapShotIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 2),
    _Ncmm13SnapShotIndex_Type()
)
ncmm13SnapShotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13SnapShotIndex.setStatus("mandatory")


class _Ncmm13SnapShotCRCStatus_Type(Integer32):
    """Custom type ncmm13SnapShotCRCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_Ncmm13SnapShotCRCStatus_Type.__name__ = "Integer32"
_Ncmm13SnapShotCRCStatus_Object = MibTableColumn
ncmm13SnapShotCRCStatus = _Ncmm13SnapShotCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 3),
    _Ncmm13SnapShotCRCStatus_Type()
)
ncmm13SnapShotCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13SnapShotCRCStatus.setStatus("mandatory")


class _Ncmm13SnapShot_Type(Integer32):
    """Custom type ncmm13SnapShot based on Integer32"""
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


_Ncmm13SnapShot_Type.__name__ = "Integer32"
_Ncmm13SnapShot_Object = MibTableColumn
ncmm13SnapShot = _Ncmm13SnapShot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 4),
    _Ncmm13SnapShot_Type()
)
ncmm13SnapShot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13SnapShot.setStatus("mandatory")


class _Ncmm13TimeStampSec_Type(Integer32):
    """Custom type ncmm13TimeStampSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13TimeStampSec_Type.__name__ = "Integer32"
_Ncmm13TimeStampSec_Object = MibTableColumn
ncmm13TimeStampSec = _Ncmm13TimeStampSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 5),
    _Ncmm13TimeStampSec_Type()
)
ncmm13TimeStampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TimeStampSec.setStatus("mandatory")


class _Ncmm13TimeStampMilliSec_Type(Integer32):
    """Custom type ncmm13TimeStampMilliSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TimeStampMilliSec_Type.__name__ = "Integer32"
_Ncmm13TimeStampMilliSec_Object = MibTableColumn
ncmm13TimeStampMilliSec = _Ncmm13TimeStampMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 6),
    _Ncmm13TimeStampMilliSec_Type()
)
ncmm13TimeStampMilliSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TimeStampMilliSec.setStatus("mandatory")


class _Ncmm13SnapShotSecs_Type(Integer32):
    """Custom type ncmm13SnapShotSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13SnapShotSecs_Type.__name__ = "Integer32"
_Ncmm13SnapShotSecs_Object = MibTableColumn
ncmm13SnapShotSecs = _Ncmm13SnapShotSecs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 7),
    _Ncmm13SnapShotSecs_Type()
)
ncmm13SnapShotSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13SnapShotSecs.setStatus("mandatory")


class _Ncmm13ResetPerfReg_Type(Integer32):
    """Custom type ncmm13ResetPerfReg based on Integer32"""
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


_Ncmm13ResetPerfReg_Type.__name__ = "Integer32"
_Ncmm13ResetPerfReg_Object = MibTableColumn
ncmm13ResetPerfReg = _Ncmm13ResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14005, 1, 8),
    _Ncmm13ResetPerfReg_Type()
)
ncmm13ResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13ResetPerfReg.setStatus("mandatory")
_Ncmm13TCAQtrTable_Object = MibTable
ncmm13TCAQtrTable = _Ncmm13TCAQtrTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006)
)
if mibBuilder.loadTexts:
    ncmm13TCAQtrTable.setStatus("mandatory")
_Ncmm13TCAQtrEntry_Object = MibTableRow
ncmm13TCAQtrEntry = _Ncmm13TCAQtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1)
)
ncmm13TCAQtrEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TCAQtrNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TCAQtrIndex"),
)
if mibBuilder.loadTexts:
    ncmm13TCAQtrEntry.setStatus("mandatory")


class _Ncmm13TCAQtrNIDIndex_Type(Integer32):
    """Custom type ncmm13TCAQtrNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13TCAQtrNIDIndex_Type.__name__ = "Integer32"
_Ncmm13TCAQtrNIDIndex_Object = MibTableColumn
ncmm13TCAQtrNIDIndex = _Ncmm13TCAQtrNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 1),
    _Ncmm13TCAQtrNIDIndex_Type()
)
ncmm13TCAQtrNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TCAQtrNIDIndex.setStatus("mandatory")


class _Ncmm13TCAQtrIndex_Type(Integer32):
    """Custom type ncmm13TCAQtrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TCAQtrIndex_Type.__name__ = "Integer32"
_Ncmm13TCAQtrIndex_Object = MibTableColumn
ncmm13TCAQtrIndex = _Ncmm13TCAQtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 2),
    _Ncmm13TCAQtrIndex_Type()
)
ncmm13TCAQtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TCAQtrIndex.setStatus("mandatory")


class _Ncmm13TCAQtrFarEndCCV_Type(Integer32):
    """Custom type ncmm13TCAQtrFarEndCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrFarEndCCV_Type.__name__ = "Integer32"
_Ncmm13TCAQtrFarEndCCV_Object = MibTableColumn
ncmm13TCAQtrFarEndCCV = _Ncmm13TCAQtrFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 3),
    _Ncmm13TCAQtrFarEndCCV_Type()
)
ncmm13TCAQtrFarEndCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrFarEndCCV.setStatus("mandatory")


class _Ncmm13TCAQtrFarEndCES_Type(Integer32):
    """Custom type ncmm13TCAQtrFarEndCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrFarEndCES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrFarEndCES_Object = MibTableColumn
ncmm13TCAQtrFarEndCES = _Ncmm13TCAQtrFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 4),
    _Ncmm13TCAQtrFarEndCES_Type()
)
ncmm13TCAQtrFarEndCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrFarEndCES.setStatus("mandatory")


class _Ncmm13TCAQtrFarEndCSES_Type(Integer32):
    """Custom type ncmm13TCAQtrFarEndCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrFarEndCSES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrFarEndCSES_Object = MibTableColumn
ncmm13TCAQtrFarEndCSES = _Ncmm13TCAQtrFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 5),
    _Ncmm13TCAQtrFarEndCSES_Type()
)
ncmm13TCAQtrFarEndCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrFarEndCSES.setStatus("mandatory")


class _Ncmm13TCAQtrFarEndLUAS_Type(Integer32):
    """Custom type ncmm13TCAQtrFarEndLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrFarEndLUAS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrFarEndLUAS_Object = MibTableColumn
ncmm13TCAQtrFarEndLUAS = _Ncmm13TCAQtrFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 6),
    _Ncmm13TCAQtrFarEndLUAS_Type()
)
ncmm13TCAQtrFarEndLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrFarEndLUAS.setStatus("mandatory")


class _Ncmm13TCAQtrLCV_Type(Integer32):
    """Custom type ncmm13TCAQtrLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLCV_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLCV_Object = MibTableColumn
ncmm13TCAQtrLCV = _Ncmm13TCAQtrLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 7),
    _Ncmm13TCAQtrLCV_Type()
)
ncmm13TCAQtrLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLCV.setStatus("mandatory")


class _Ncmm13TCAQtrLES_Type(Integer32):
    """Custom type ncmm13TCAQtrLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLES_Object = MibTableColumn
ncmm13TCAQtrLES = _Ncmm13TCAQtrLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 8),
    _Ncmm13TCAQtrLES_Type()
)
ncmm13TCAQtrLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLES.setStatus("mandatory")


class _Ncmm13TCAQtrLSES_Type(Integer32):
    """Custom type ncmm13TCAQtrLSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLSES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLSES_Object = MibTableColumn
ncmm13TCAQtrLSES = _Ncmm13TCAQtrLSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 9),
    _Ncmm13TCAQtrLSES_Type()
)
ncmm13TCAQtrLSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLSES.setStatus("mandatory")


class _Ncmm13TCAQtrPCV_Type(Integer32):
    """Custom type ncmm13TCAQtrPCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrPCV_Type.__name__ = "Integer32"
_Ncmm13TCAQtrPCV_Object = MibTableColumn
ncmm13TCAQtrPCV = _Ncmm13TCAQtrPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 10),
    _Ncmm13TCAQtrPCV_Type()
)
ncmm13TCAQtrPCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrPCV.setStatus("mandatory")


class _Ncmm13TCAQtrPES_Type(Integer32):
    """Custom type ncmm13TCAQtrPES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrPES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrPES_Object = MibTableColumn
ncmm13TCAQtrPES = _Ncmm13TCAQtrPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 11),
    _Ncmm13TCAQtrPES_Type()
)
ncmm13TCAQtrPES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrPES.setStatus("mandatory")


class _Ncmm13TCAQtrPSES_Type(Integer32):
    """Custom type ncmm13TCAQtrPSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrPSES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrPSES_Object = MibTableColumn
ncmm13TCAQtrPSES = _Ncmm13TCAQtrPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 12),
    _Ncmm13TCAQtrPSES_Type()
)
ncmm13TCAQtrPSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrPSES.setStatus("mandatory")


class _Ncmm13TCAQtrCCV_Type(Integer32):
    """Custom type ncmm13TCAQtrCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrCCV_Type.__name__ = "Integer32"
_Ncmm13TCAQtrCCV_Object = MibTableColumn
ncmm13TCAQtrCCV = _Ncmm13TCAQtrCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 13),
    _Ncmm13TCAQtrCCV_Type()
)
ncmm13TCAQtrCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrCCV.setStatus("mandatory")


class _Ncmm13TCAQtrCES_Type(Integer32):
    """Custom type ncmm13TCAQtrCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrCES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrCES_Object = MibTableColumn
ncmm13TCAQtrCES = _Ncmm13TCAQtrCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 14),
    _Ncmm13TCAQtrCES_Type()
)
ncmm13TCAQtrCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrCES.setStatus("mandatory")


class _Ncmm13TCAQtrCSES_Type(Integer32):
    """Custom type ncmm13TCAQtrCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrCSES_Type.__name__ = "Integer32"
_Ncmm13TCAQtrCSES_Object = MibTableColumn
ncmm13TCAQtrCSES = _Ncmm13TCAQtrCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 15),
    _Ncmm13TCAQtrCSES_Type()
)
ncmm13TCAQtrCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrCSES.setStatus("mandatory")


class _Ncmm13TCAQtrSEFS_Type(Integer32):
    """Custom type ncmm13TCAQtrSEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrSEFS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrSEFS_Object = MibTableColumn
ncmm13TCAQtrSEFS = _Ncmm13TCAQtrSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 16),
    _Ncmm13TCAQtrSEFS_Type()
)
ncmm13TCAQtrSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrSEFS.setStatus("mandatory")


class _Ncmm13TCAQtrAISS_Type(Integer32):
    """Custom type ncmm13TCAQtrAISS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrAISS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrAISS_Object = MibTableColumn
ncmm13TCAQtrAISS = _Ncmm13TCAQtrAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 17),
    _Ncmm13TCAQtrAISS_Type()
)
ncmm13TCAQtrAISS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrAISS.setStatus("mandatory")


class _Ncmm13TCAQtrLUAS_Type(Integer32):
    """Custom type ncmm13TCAQtrLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLUAS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLUAS_Object = MibTableColumn
ncmm13TCAQtrLUAS = _Ncmm13TCAQtrLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 18),
    _Ncmm13TCAQtrLUAS_Type()
)
ncmm13TCAQtrLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLUAS.setStatus("mandatory")


class _Ncmm13TCAQtrLOSS_Type(Integer32):
    """Custom type ncmm13TCAQtrLOSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLOSS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLOSS_Object = MibTableColumn
ncmm13TCAQtrLOSS = _Ncmm13TCAQtrLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 19),
    _Ncmm13TCAQtrLOSS_Type()
)
ncmm13TCAQtrLOSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLOSS.setStatus("mandatory")


class _Ncmm13TCAQtrLOFS_Type(Integer32):
    """Custom type ncmm13TCAQtrLOFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCAQtrLOFS_Type.__name__ = "Integer32"
_Ncmm13TCAQtrLOFS_Object = MibTableColumn
ncmm13TCAQtrLOFS = _Ncmm13TCAQtrLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14006, 1, 20),
    _Ncmm13TCAQtrLOFS_Type()
)
ncmm13TCAQtrLOFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCAQtrLOFS.setStatus("mandatory")
_Ncmm13TCADayTable_Object = MibTable
ncmm13TCADayTable = _Ncmm13TCADayTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007)
)
if mibBuilder.loadTexts:
    ncmm13TCADayTable.setStatus("mandatory")
_Ncmm13TCADayEntry_Object = MibTableRow
ncmm13TCADayEntry = _Ncmm13TCADayEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1)
)
ncmm13TCADayEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TCADayNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TCADayIndex"),
)
if mibBuilder.loadTexts:
    ncmm13TCADayEntry.setStatus("mandatory")


class _Ncmm13TCADayNIDIndex_Type(Integer32):
    """Custom type ncmm13TCADayNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13TCADayNIDIndex_Type.__name__ = "Integer32"
_Ncmm13TCADayNIDIndex_Object = MibTableColumn
ncmm13TCADayNIDIndex = _Ncmm13TCADayNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 1),
    _Ncmm13TCADayNIDIndex_Type()
)
ncmm13TCADayNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TCADayNIDIndex.setStatus("mandatory")


class _Ncmm13TCADayIndex_Type(Integer32):
    """Custom type ncmm13TCADayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TCADayIndex_Type.__name__ = "Integer32"
_Ncmm13TCADayIndex_Object = MibTableColumn
ncmm13TCADayIndex = _Ncmm13TCADayIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 2),
    _Ncmm13TCADayIndex_Type()
)
ncmm13TCADayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TCADayIndex.setStatus("mandatory")


class _Ncmm13TCADayFarEndCCV_Type(Integer32):
    """Custom type ncmm13TCADayFarEndCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayFarEndCCV_Type.__name__ = "Integer32"
_Ncmm13TCADayFarEndCCV_Object = MibTableColumn
ncmm13TCADayFarEndCCV = _Ncmm13TCADayFarEndCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 3),
    _Ncmm13TCADayFarEndCCV_Type()
)
ncmm13TCADayFarEndCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayFarEndCCV.setStatus("mandatory")


class _Ncmm13TCADayFarEndCES_Type(Integer32):
    """Custom type ncmm13TCADayFarEndCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayFarEndCES_Type.__name__ = "Integer32"
_Ncmm13TCADayFarEndCES_Object = MibTableColumn
ncmm13TCADayFarEndCES = _Ncmm13TCADayFarEndCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 4),
    _Ncmm13TCADayFarEndCES_Type()
)
ncmm13TCADayFarEndCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayFarEndCES.setStatus("mandatory")


class _Ncmm13TCADayFarEndCSES_Type(Integer32):
    """Custom type ncmm13TCADayFarEndCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayFarEndCSES_Type.__name__ = "Integer32"
_Ncmm13TCADayFarEndCSES_Object = MibTableColumn
ncmm13TCADayFarEndCSES = _Ncmm13TCADayFarEndCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 5),
    _Ncmm13TCADayFarEndCSES_Type()
)
ncmm13TCADayFarEndCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayFarEndCSES.setStatus("mandatory")


class _Ncmm13TCADayFarEndLUAS_Type(Integer32):
    """Custom type ncmm13TCADayFarEndLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayFarEndLUAS_Type.__name__ = "Integer32"
_Ncmm13TCADayFarEndLUAS_Object = MibTableColumn
ncmm13TCADayFarEndLUAS = _Ncmm13TCADayFarEndLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 6),
    _Ncmm13TCADayFarEndLUAS_Type()
)
ncmm13TCADayFarEndLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayFarEndLUAS.setStatus("mandatory")


class _Ncmm13TCADayLCV_Type(Integer32):
    """Custom type ncmm13TCADayLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLCV_Type.__name__ = "Integer32"
_Ncmm13TCADayLCV_Object = MibTableColumn
ncmm13TCADayLCV = _Ncmm13TCADayLCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 7),
    _Ncmm13TCADayLCV_Type()
)
ncmm13TCADayLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLCV.setStatus("mandatory")


class _Ncmm13TCADayLES_Type(Integer32):
    """Custom type ncmm13TCADayLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLES_Type.__name__ = "Integer32"
_Ncmm13TCADayLES_Object = MibTableColumn
ncmm13TCADayLES = _Ncmm13TCADayLES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 8),
    _Ncmm13TCADayLES_Type()
)
ncmm13TCADayLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLES.setStatus("mandatory")


class _Ncmm13TCADayLSES_Type(Integer32):
    """Custom type ncmm13TCADayLSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLSES_Type.__name__ = "Integer32"
_Ncmm13TCADayLSES_Object = MibTableColumn
ncmm13TCADayLSES = _Ncmm13TCADayLSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 9),
    _Ncmm13TCADayLSES_Type()
)
ncmm13TCADayLSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLSES.setStatus("mandatory")


class _Ncmm13TCADayPCV_Type(Integer32):
    """Custom type ncmm13TCADayPCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayPCV_Type.__name__ = "Integer32"
_Ncmm13TCADayPCV_Object = MibTableColumn
ncmm13TCADayPCV = _Ncmm13TCADayPCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 10),
    _Ncmm13TCADayPCV_Type()
)
ncmm13TCADayPCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayPCV.setStatus("mandatory")


class _Ncmm13TCADayPES_Type(Integer32):
    """Custom type ncmm13TCADayPES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayPES_Type.__name__ = "Integer32"
_Ncmm13TCADayPES_Object = MibTableColumn
ncmm13TCADayPES = _Ncmm13TCADayPES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 11),
    _Ncmm13TCADayPES_Type()
)
ncmm13TCADayPES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayPES.setStatus("mandatory")


class _Ncmm13TCADayPSES_Type(Integer32):
    """Custom type ncmm13TCADayPSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayPSES_Type.__name__ = "Integer32"
_Ncmm13TCADayPSES_Object = MibTableColumn
ncmm13TCADayPSES = _Ncmm13TCADayPSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 12),
    _Ncmm13TCADayPSES_Type()
)
ncmm13TCADayPSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayPSES.setStatus("mandatory")


class _Ncmm13TCADayCCV_Type(Integer32):
    """Custom type ncmm13TCADayCCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayCCV_Type.__name__ = "Integer32"
_Ncmm13TCADayCCV_Object = MibTableColumn
ncmm13TCADayCCV = _Ncmm13TCADayCCV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 13),
    _Ncmm13TCADayCCV_Type()
)
ncmm13TCADayCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayCCV.setStatus("mandatory")


class _Ncmm13TCADayCES_Type(Integer32):
    """Custom type ncmm13TCADayCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayCES_Type.__name__ = "Integer32"
_Ncmm13TCADayCES_Object = MibTableColumn
ncmm13TCADayCES = _Ncmm13TCADayCES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 14),
    _Ncmm13TCADayCES_Type()
)
ncmm13TCADayCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayCES.setStatus("mandatory")


class _Ncmm13TCADayCSES_Type(Integer32):
    """Custom type ncmm13TCADayCSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayCSES_Type.__name__ = "Integer32"
_Ncmm13TCADayCSES_Object = MibTableColumn
ncmm13TCADayCSES = _Ncmm13TCADayCSES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 15),
    _Ncmm13TCADayCSES_Type()
)
ncmm13TCADayCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayCSES.setStatus("mandatory")


class _Ncmm13TCADaySEFS_Type(Integer32):
    """Custom type ncmm13TCADaySEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADaySEFS_Type.__name__ = "Integer32"
_Ncmm13TCADaySEFS_Object = MibTableColumn
ncmm13TCADaySEFS = _Ncmm13TCADaySEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 16),
    _Ncmm13TCADaySEFS_Type()
)
ncmm13TCADaySEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADaySEFS.setStatus("mandatory")


class _Ncmm13TCADayAISS_Type(Integer32):
    """Custom type ncmm13TCADayAISS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayAISS_Type.__name__ = "Integer32"
_Ncmm13TCADayAISS_Object = MibTableColumn
ncmm13TCADayAISS = _Ncmm13TCADayAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 17),
    _Ncmm13TCADayAISS_Type()
)
ncmm13TCADayAISS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayAISS.setStatus("mandatory")


class _Ncmm13TCADayLUAS_Type(Integer32):
    """Custom type ncmm13TCADayLUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLUAS_Type.__name__ = "Integer32"
_Ncmm13TCADayLUAS_Object = MibTableColumn
ncmm13TCADayLUAS = _Ncmm13TCADayLUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 18),
    _Ncmm13TCADayLUAS_Type()
)
ncmm13TCADayLUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLUAS.setStatus("mandatory")


class _Ncmm13TCADayLOSS_Type(Integer32):
    """Custom type ncmm13TCADayLOSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLOSS_Type.__name__ = "Integer32"
_Ncmm13TCADayLOSS_Object = MibTableColumn
ncmm13TCADayLOSS = _Ncmm13TCADayLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 19),
    _Ncmm13TCADayLOSS_Type()
)
ncmm13TCADayLOSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLOSS.setStatus("mandatory")


class _Ncmm13TCADayLOFS_Type(Integer32):
    """Custom type ncmm13TCADayLOFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ncmm13TCADayLOFS_Type.__name__ = "Integer32"
_Ncmm13TCADayLOFS_Object = MibTableColumn
ncmm13TCADayLOFS = _Ncmm13TCADayLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14007, 1, 20),
    _Ncmm13TCADayLOFS_Type()
)
ncmm13TCADayLOFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TCADayLOFS.setStatus("mandatory")
_Ncmm13TxAlarmTable_Object = MibTable
ncmm13TxAlarmTable = _Ncmm13TxAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008)
)
if mibBuilder.loadTexts:
    ncmm13TxAlarmTable.setStatus("mandatory")
_Ncmm13TxAlarmEntry_Object = MibTableRow
ncmm13TxAlarmEntry = _Ncmm13TxAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1)
)
ncmm13TxAlarmEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TxAlarmNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13TxAlarmIndex"),
)
if mibBuilder.loadTexts:
    ncmm13TxAlarmEntry.setStatus("mandatory")


class _Ncmm13TxAlarmNIDIndex_Type(Integer32):
    """Custom type ncmm13TxAlarmNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13TxAlarmNIDIndex_Type.__name__ = "Integer32"
_Ncmm13TxAlarmNIDIndex_Object = MibTableColumn
ncmm13TxAlarmNIDIndex = _Ncmm13TxAlarmNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 1),
    _Ncmm13TxAlarmNIDIndex_Type()
)
ncmm13TxAlarmNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TxAlarmNIDIndex.setStatus("mandatory")


class _Ncmm13TxAlarmIndex_Type(Integer32):
    """Custom type ncmm13TxAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13TxAlarmIndex_Type.__name__ = "Integer32"
_Ncmm13TxAlarmIndex_Object = MibTableColumn
ncmm13TxAlarmIndex = _Ncmm13TxAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 2),
    _Ncmm13TxAlarmIndex_Type()
)
ncmm13TxAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13TxAlarmIndex.setStatus("mandatory")


class _Ncmm13TxYellowAlarm_Type(Integer32):
    """Custom type ncmm13TxYellowAlarm based on Integer32"""
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


_Ncmm13TxYellowAlarm_Type.__name__ = "Integer32"
_Ncmm13TxYellowAlarm_Object = MibTableColumn
ncmm13TxYellowAlarm = _Ncmm13TxYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 3),
    _Ncmm13TxYellowAlarm_Type()
)
ncmm13TxYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TxYellowAlarm.setStatus("mandatory")


class _Ncmm13TxAIS_Type(Integer32):
    """Custom type ncmm13TxAIS based on Integer32"""
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


_Ncmm13TxAIS_Type.__name__ = "Integer32"
_Ncmm13TxAIS_Object = MibTableColumn
ncmm13TxAIS = _Ncmm13TxAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 4),
    _Ncmm13TxAIS_Type()
)
ncmm13TxAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TxAIS.setStatus("mandatory")


class _Ncmm13TxIdleSignal_Type(Integer32):
    """Custom type ncmm13TxIdleSignal based on Integer32"""
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


_Ncmm13TxIdleSignal_Type.__name__ = "Integer32"
_Ncmm13TxIdleSignal_Object = MibTableColumn
ncmm13TxIdleSignal = _Ncmm13TxIdleSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 5),
    _Ncmm13TxIdleSignal_Type()
)
ncmm13TxIdleSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TxIdleSignal.setStatus("mandatory")


class _Ncmm13TxFEBE_Type(Integer32):
    """Custom type ncmm13TxFEBE based on Integer32"""
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


_Ncmm13TxFEBE_Type.__name__ = "Integer32"
_Ncmm13TxFEBE_Object = MibTableColumn
ncmm13TxFEBE = _Ncmm13TxFEBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 6),
    _Ncmm13TxFEBE_Type()
)
ncmm13TxFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TxFEBE.setStatus("mandatory")


class _Ncmm13TxFEACAlarm_Type(Integer32):
    """Custom type ncmm13TxFEACAlarm based on Integer32"""
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
        *(("ais-Received-Alarm", 5),
          ("common-Eqpt-NSA-Alarm", 8),
          ("eqpt-FailureSA-Alarm", 2),
          ("eqpt-NSA-Alarm", 7),
          ("idle-Received-Alarm", 6),
          ("los-HBER-Alarm", 3),
          ("no-FEAC-Alarm-enabled", 1),
          ("oof-Alarm", 4))
    )


_Ncmm13TxFEACAlarm_Type.__name__ = "Integer32"
_Ncmm13TxFEACAlarm_Object = MibTableColumn
ncmm13TxFEACAlarm = _Ncmm13TxFEACAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14008, 1, 7),
    _Ncmm13TxFEACAlarm_Type()
)
ncmm13TxFEACAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13TxFEACAlarm.setStatus("mandatory")
_Ncmm13DS3LPBKTable_Object = MibTable
ncmm13DS3LPBKTable = _Ncmm13DS3LPBKTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14009)
)
if mibBuilder.loadTexts:
    ncmm13DS3LPBKTable.setStatus("mandatory")
_Ncmm13DS3LPBKEntry_Object = MibTableRow
ncmm13DS3LPBKEntry = _Ncmm13DS3LPBKEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14009, 1)
)
ncmm13DS3LPBKEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13DS3LPBKNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13DS3LPBKIndex"),
)
if mibBuilder.loadTexts:
    ncmm13DS3LPBKEntry.setStatus("mandatory")


class _Ncmm13DS3LPBKNIDIndex_Type(Integer32):
    """Custom type ncmm13DS3LPBKNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13DS3LPBKNIDIndex_Type.__name__ = "Integer32"
_Ncmm13DS3LPBKNIDIndex_Object = MibTableColumn
ncmm13DS3LPBKNIDIndex = _Ncmm13DS3LPBKNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14009, 1, 1),
    _Ncmm13DS3LPBKNIDIndex_Type()
)
ncmm13DS3LPBKNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3LPBKNIDIndex.setStatus("mandatory")


class _Ncmm13DS3LPBKIndex_Type(Integer32):
    """Custom type ncmm13DS3LPBKIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13DS3LPBKIndex_Type.__name__ = "Integer32"
_Ncmm13DS3LPBKIndex_Object = MibTableColumn
ncmm13DS3LPBKIndex = _Ncmm13DS3LPBKIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14009, 1, 2),
    _Ncmm13DS3LPBKIndex_Type()
)
ncmm13DS3LPBKIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13DS3LPBKIndex.setStatus("mandatory")


class _Ncmm13DS3LPBKAction_Type(Integer32):
    """Custom type ncmm13DS3LPBKAction based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("m13-DS3-Activate-FEAC-Far-End", 4),
          ("m13-DS3-Activate-Inband-Far-End", 5),
          ("m13-DS3-Activate-Line", 3),
          ("m13-DS3-Activate-Local", 2),
          ("m13-DS3-DeActivate-FEAC-Far-End", 8),
          ("m13-DS3-DeActivate-Inband-Far-End", 9),
          ("m13-DS3-DeActivate-Line", 7),
          ("m13-DS3-DeActivate-Local", 6),
          ("no-Loopback", 1))
    )


_Ncmm13DS3LPBKAction_Type.__name__ = "Integer32"
_Ncmm13DS3LPBKAction_Object = MibTableColumn
ncmm13DS3LPBKAction = _Ncmm13DS3LPBKAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14009, 1, 3),
    _Ncmm13DS3LPBKAction_Type()
)
ncmm13DS3LPBKAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13DS3LPBKAction.setStatus("mandatory")
_Ncmm13T1LPBKTable_Object = MibTable
ncmm13T1LPBKTable = _Ncmm13T1LPBKTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14010)
)
if mibBuilder.loadTexts:
    ncmm13T1LPBKTable.setStatus("mandatory")
_Ncmm13T1LPBKEntry_Object = MibTableRow
ncmm13T1LPBKEntry = _Ncmm13T1LPBKEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14010, 1)
)
ncmm13T1LPBKEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13T1LPBKNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13T1LPBKIndex"),
)
if mibBuilder.loadTexts:
    ncmm13T1LPBKEntry.setStatus("mandatory")


class _Ncmm13T1LPBKNIDIndex_Type(Integer32):
    """Custom type ncmm13T1LPBKNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13T1LPBKNIDIndex_Type.__name__ = "Integer32"
_Ncmm13T1LPBKNIDIndex_Object = MibTableColumn
ncmm13T1LPBKNIDIndex = _Ncmm13T1LPBKNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14010, 1, 1),
    _Ncmm13T1LPBKNIDIndex_Type()
)
ncmm13T1LPBKNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1LPBKNIDIndex.setStatus("mandatory")


class _Ncmm13T1LPBKIndex_Type(Integer32):
    """Custom type ncmm13T1LPBKIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ncmm13T1LPBKIndex_Type.__name__ = "Integer32"
_Ncmm13T1LPBKIndex_Object = MibTableColumn
ncmm13T1LPBKIndex = _Ncmm13T1LPBKIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14010, 1, 2),
    _Ncmm13T1LPBKIndex_Type()
)
ncmm13T1LPBKIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1LPBKIndex.setStatus("mandatory")


class _Ncmm13T1LPBKAction_Type(Integer32):
    """Custom type ncmm13T1LPBKAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("m13-Activate-1-28-T1-Far-End", 12),
          ("m13-Activate-1-28-T1-Line", 10),
          ("m13-Activate-1-28-T1-Local", 14),
          ("m13-Activate-All-T1-Far-End", 13),
          ("m13-Activate-All-T1-Line", 11),
          ("m13-Activate-All-T1-Local", 15),
          ("m13-DeActivate-1-28-T1-Far-End", 18),
          ("m13-DeActivate-1-28-T1-Line", 16),
          ("m13-DeActivate-1-28-T1-Local", 20),
          ("m13-DeActivate-All-T1-Far-End", 19),
          ("m13-DeActivate-All-T1-Line", 17),
          ("m13-DeActivate-All-T1-Local", 21),
          ("no-Loopback", 1))
    )


_Ncmm13T1LPBKAction_Type.__name__ = "Integer32"
_Ncmm13T1LPBKAction_Object = MibTableColumn
ncmm13T1LPBKAction = _Ncmm13T1LPBKAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14010, 1, 3),
    _Ncmm13T1LPBKAction_Type()
)
ncmm13T1LPBKAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1LPBKAction.setStatus("mandatory")
_Ncmm13T1ConfigTable_Object = MibTable
ncmm13T1ConfigTable = _Ncmm13T1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011)
)
if mibBuilder.loadTexts:
    ncmm13T1ConfigTable.setStatus("mandatory")
_Ncmm13T1ConfigEntry_Object = MibTableRow
ncmm13T1ConfigEntry = _Ncmm13T1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1)
)
ncmm13T1ConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13T1ConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMM13-MIB", "ncmm13T1LineIndex"),
)
if mibBuilder.loadTexts:
    ncmm13T1ConfigEntry.setStatus("mandatory")


class _Ncmm13T1ConfigNIDIndex_Type(Integer32):
    """Custom type ncmm13T1ConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13T1ConfigNIDIndex_Type.__name__ = "Integer32"
_Ncmm13T1ConfigNIDIndex_Object = MibTableColumn
ncmm13T1ConfigNIDIndex = _Ncmm13T1ConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 1),
    _Ncmm13T1ConfigNIDIndex_Type()
)
ncmm13T1ConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1ConfigNIDIndex.setStatus("mandatory")


class _Ncmm13T1LineIndex_Type(Integer32):
    """Custom type ncmm13T1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmm13T1LineIndex_Type.__name__ = "Integer32"
_Ncmm13T1LineIndex_Object = MibTableColumn
ncmm13T1LineIndex = _Ncmm13T1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 2),
    _Ncmm13T1LineIndex_Type()
)
ncmm13T1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmm13T1LineIndex.setStatus("mandatory")


class _Ncmm13T1FramingFormat_Type(Integer32):
    """Custom type ncmm13T1FramingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eSF", 2),
          ("sF", 1))
    )


_Ncmm13T1FramingFormat_Type.__name__ = "Integer32"
_Ncmm13T1FramingFormat_Object = MibTableColumn
ncmm13T1FramingFormat = _Ncmm13T1FramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 3),
    _Ncmm13T1FramingFormat_Type()
)
ncmm13T1FramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1FramingFormat.setStatus("mandatory")


class _Ncmm13T1LineCoding_Type(Integer32):
    """Custom type ncmm13T1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("b8ZS", 2))
    )


_Ncmm13T1LineCoding_Type.__name__ = "Integer32"
_Ncmm13T1LineCoding_Object = MibTableColumn
ncmm13T1LineCoding = _Ncmm13T1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 4),
    _Ncmm13T1LineCoding_Type()
)
ncmm13T1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1LineCoding.setStatus("mandatory")


class _Ncmm13T1EnableNetOnesDensity_Type(Integer32):
    """Custom type ncmm13T1EnableNetOnesDensity based on Integer32"""
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


_Ncmm13T1EnableNetOnesDensity_Type.__name__ = "Integer32"
_Ncmm13T1EnableNetOnesDensity_Object = MibTableColumn
ncmm13T1EnableNetOnesDensity = _Ncmm13T1EnableNetOnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 5),
    _Ncmm13T1EnableNetOnesDensity_Type()
)
ncmm13T1EnableNetOnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1EnableNetOnesDensity.setStatus("mandatory")


class _Ncmm13T1DensityPattern_Type(Integer32):
    """Custom type ncmm13T1DensityPattern based on Integer32"""
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
        *(("d12d5c80Zero", 3),
          ("d15Zeros", 2),
          ("d80Zeros", 1),
          ("tR-62411", 4))
    )


_Ncmm13T1DensityPattern_Type.__name__ = "Integer32"
_Ncmm13T1DensityPattern_Object = MibTableColumn
ncmm13T1DensityPattern = _Ncmm13T1DensityPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 6),
    _Ncmm13T1DensityPattern_Type()
)
ncmm13T1DensityPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1DensityPattern.setStatus("mandatory")


class _Ncmm13T1PortService_Type(Integer32):
    """Custom type ncmm13T1PortService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 2),
          ("out-of-service", 1))
    )


_Ncmm13T1PortService_Type.__name__ = "Integer32"
_Ncmm13T1PortService_Object = MibTableColumn
ncmm13T1PortService = _Ncmm13T1PortService_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037, 14011, 1, 7),
    _Ncmm13T1PortService_Type()
)
ncmm13T1PortService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmm13T1PortService.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMM13-MIB",
    **{"ncmm13DS3PortTable": ncmm13DS3PortTable,
       "ncmm13DS3PortEntry": ncmm13DS3PortEntry,
       "ncmm13DS3PortNIDIndex": ncmm13DS3PortNIDIndex,
       "ncmm13DS3PortIndex": ncmm13DS3PortIndex,
       "ncmm13DS3ModeControl": ncmm13DS3ModeControl,
       "ncmm13DS3LineType": ncmm13DS3LineType,
       "ncmm13DS3PerfControl": ncmm13DS3PerfControl,
       "ncmm13DS3AlarmControl": ncmm13DS3AlarmControl,
       "ncmm13DS3FarEndControl": ncmm13DS3FarEndControl,
       "ncmm13DS3BusType": ncmm13DS3BusType,
       "ncmm13DS3InbandControl": ncmm13DS3InbandControl,
       "ncmm13DS3CableLength": ncmm13DS3CableLength,
       "ncmm13DS3EquipCode": ncmm13DS3EquipCode,
       "ncmm13DS3LocationIDCode": ncmm13DS3LocationIDCode,
       "ncmm13DS3FrameIDCode": ncmm13DS3FrameIDCode,
       "ncmm13DS3UnitCode": ncmm13DS3UnitCode,
       "ncmm13DS3FacilityIDCode": ncmm13DS3FacilityIDCode,
       "ncmm13DS3PortIdCode": ncmm13DS3PortIdCode,
       "ncmm13DS3GenIDCode": ncmm13DS3GenIDCode,
       "ncmm13StatTable": ncmm13StatTable,
       "ncmm13StatEntry": ncmm13StatEntry,
       "ncmm13StatNIDIndex": ncmm13StatNIDIndex,
       "ncmm13StatIndex": ncmm13StatIndex,
       "ncmm13StatAIS": ncmm13StatAIS,
       "ncmm13StatIdle": ncmm13StatIdle,
       "ncmm13StatYellowAlm": ncmm13StatYellowAlm,
       "ncmm13StatOOF": ncmm13StatOOF,
       "ncmm13StatLOS": ncmm13StatLOS,
       "ncmm13DS3NearEndLocalLoopback": ncmm13DS3NearEndLocalLoopback,
       "ncmm13DS3NearEndLineLoopback": ncmm13DS3NearEndLineLoopback,
       "ncmm13DS3FarEndLineLoopback": ncmm13DS3FarEndLineLoopback,
       "ncmm13T1NearEndLineLoopback": ncmm13T1NearEndLineLoopback,
       "ncmm13T1FarEndLineLoopback": ncmm13T1FarEndLineLoopback,
       "ncmm13FarEndAllT1LineLoopback": ncmm13FarEndAllT1LineLoopback,
       "ncmm13T1LocalLoopback": ncmm13T1LocalLoopback,
       "ncmm13CurrentTable": ncmm13CurrentTable,
       "ncmm13CurrentEntry": ncmm13CurrentEntry,
       "ncmm13CurrentNIDIndex": ncmm13CurrentNIDIndex,
       "ncmm13CurrentIndex": ncmm13CurrentIndex,
       "ncmm13CurrentCRCStatus": ncmm13CurrentCRCStatus,
       "ncmm13CurrentTimeStampSecs": ncmm13CurrentTimeStampSecs,
       "ncmm13CurrentTimeStampMSecs": ncmm13CurrentTimeStampMSecs,
       "ncmm13CurrentIntervalSecsElaps": ncmm13CurrentIntervalSecsElaps,
       "ncmm13CurrentFarEndCCV": ncmm13CurrentFarEndCCV,
       "ncmm13CurrentFarEndCES": ncmm13CurrentFarEndCES,
       "ncmm13CurrentFarEndCSES": ncmm13CurrentFarEndCSES,
       "ncmm13CurrentFarEndLUAS": ncmm13CurrentFarEndLUAS,
       "ncmm13CurrentLCV": ncmm13CurrentLCV,
       "ncmm13CurrentLES": ncmm13CurrentLES,
       "ncmm13CurrentLSES": ncmm13CurrentLSES,
       "ncmm13CurrentPCV": ncmm13CurrentPCV,
       "ncmm13CurrentPES": ncmm13CurrentPES,
       "ncmm13CurrentPSES": ncmm13CurrentPSES,
       "ncmm13CurrentCCV": ncmm13CurrentCCV,
       "ncmm13CurrentCES": ncmm13CurrentCES,
       "ncmm13CurrentCSES": ncmm13CurrentCSES,
       "ncmm13CurrentSEFS": ncmm13CurrentSEFS,
       "ncmm13CurrentAISS": ncmm13CurrentAISS,
       "ncmm13CurrentLUAS": ncmm13CurrentLUAS,
       "ncmm13CurrentLOOS": ncmm13CurrentLOOS,
       "ncmm13CurrentLOFS": ncmm13CurrentLOFS,
       "ncmm13IntervalTable": ncmm13IntervalTable,
       "ncmm13IntervalEntry": ncmm13IntervalEntry,
       "ncmm13IntervalNIDIndex": ncmm13IntervalNIDIndex,
       "ncmm13IntervalIndex": ncmm13IntervalIndex,
       "ncmm13IntervalNumber": ncmm13IntervalNumber,
       "ncmm13IntervalFarEndCCV": ncmm13IntervalFarEndCCV,
       "ncmm13IntervalFarEndCES": ncmm13IntervalFarEndCES,
       "ncmm13IntervalFarEndCSES": ncmm13IntervalFarEndCSES,
       "ncmm13IntervalFarEndLUAS": ncmm13IntervalFarEndLUAS,
       "ncmm13IntervalLCV": ncmm13IntervalLCV,
       "ncmm13IntervalLES": ncmm13IntervalLES,
       "ncmm13IntervalLSES": ncmm13IntervalLSES,
       "ncmm13IntervalPCV": ncmm13IntervalPCV,
       "ncmm13IntervalPES": ncmm13IntervalPES,
       "ncmm13IntervalPSES": ncmm13IntervalPSES,
       "ncmm13IntervalCCV": ncmm13IntervalCCV,
       "ncmm13IntervalCES": ncmm13IntervalCES,
       "ncmm13IntervalCSES": ncmm13IntervalCSES,
       "ncmm13IntervalSEFS": ncmm13IntervalSEFS,
       "ncmm13IntervalAISS": ncmm13IntervalAISS,
       "ncmm13IntervalLUAS": ncmm13IntervalLUAS,
       "ncmm13IntervalLOSS": ncmm13IntervalLOSS,
       "ncmm13IntervalLOFS": ncmm13IntervalLOFS,
       "ncmm13TotalTable": ncmm13TotalTable,
       "ncmm13TotalEntry": ncmm13TotalEntry,
       "ncmm13TotalNIDIndex": ncmm13TotalNIDIndex,
       "ncmm13TotalIndex": ncmm13TotalIndex,
       "ncmm13TotalCRCStatus": ncmm13TotalCRCStatus,
       "ncmm13TotalValidInterv": ncmm13TotalValidInterv,
       "ncmm13TotalFarEndCCV": ncmm13TotalFarEndCCV,
       "ncmm13TotalFarEndCES": ncmm13TotalFarEndCES,
       "ncmm13TotalFarEndCSES": ncmm13TotalFarEndCSES,
       "ncmm13TotalFarEndLUAS": ncmm13TotalFarEndLUAS,
       "ncmm13TotalLCV": ncmm13TotalLCV,
       "ncmm13TotalLES": ncmm13TotalLES,
       "ncmm13TotalLSES": ncmm13TotalLSES,
       "ncmm13TotalPCV": ncmm13TotalPCV,
       "ncmm13TotalPES": ncmm13TotalPES,
       "ncmm13TotalPSES": ncmm13TotalPSES,
       "ncmm13TotalCCV": ncmm13TotalCCV,
       "ncmm13TotalCES": ncmm13TotalCES,
       "ncmm13TotalCSES": ncmm13TotalCSES,
       "ncmm13TotalSEFS": ncmm13TotalSEFS,
       "ncmm13TotalAISS": ncmm13TotalAISS,
       "ncmm13TotalLUAS": ncmm13TotalLUAS,
       "ncmm13TotalLOSS": ncmm13TotalLOSS,
       "ncmm13TotalLOFS": ncmm13TotalLOFS,
       "ncmm13PerformanceSnapShotTable": ncmm13PerformanceSnapShotTable,
       "ncmm13PerformanceSnapShotEntry": ncmm13PerformanceSnapShotEntry,
       "ncmm13SnapShotNIDIndex": ncmm13SnapShotNIDIndex,
       "ncmm13SnapShotIndex": ncmm13SnapShotIndex,
       "ncmm13SnapShotCRCStatus": ncmm13SnapShotCRCStatus,
       "ncmm13SnapShot": ncmm13SnapShot,
       "ncmm13TimeStampSec": ncmm13TimeStampSec,
       "ncmm13TimeStampMilliSec": ncmm13TimeStampMilliSec,
       "ncmm13SnapShotSecs": ncmm13SnapShotSecs,
       "ncmm13ResetPerfReg": ncmm13ResetPerfReg,
       "ncmm13TCAQtrTable": ncmm13TCAQtrTable,
       "ncmm13TCAQtrEntry": ncmm13TCAQtrEntry,
       "ncmm13TCAQtrNIDIndex": ncmm13TCAQtrNIDIndex,
       "ncmm13TCAQtrIndex": ncmm13TCAQtrIndex,
       "ncmm13TCAQtrFarEndCCV": ncmm13TCAQtrFarEndCCV,
       "ncmm13TCAQtrFarEndCES": ncmm13TCAQtrFarEndCES,
       "ncmm13TCAQtrFarEndCSES": ncmm13TCAQtrFarEndCSES,
       "ncmm13TCAQtrFarEndLUAS": ncmm13TCAQtrFarEndLUAS,
       "ncmm13TCAQtrLCV": ncmm13TCAQtrLCV,
       "ncmm13TCAQtrLES": ncmm13TCAQtrLES,
       "ncmm13TCAQtrLSES": ncmm13TCAQtrLSES,
       "ncmm13TCAQtrPCV": ncmm13TCAQtrPCV,
       "ncmm13TCAQtrPES": ncmm13TCAQtrPES,
       "ncmm13TCAQtrPSES": ncmm13TCAQtrPSES,
       "ncmm13TCAQtrCCV": ncmm13TCAQtrCCV,
       "ncmm13TCAQtrCES": ncmm13TCAQtrCES,
       "ncmm13TCAQtrCSES": ncmm13TCAQtrCSES,
       "ncmm13TCAQtrSEFS": ncmm13TCAQtrSEFS,
       "ncmm13TCAQtrAISS": ncmm13TCAQtrAISS,
       "ncmm13TCAQtrLUAS": ncmm13TCAQtrLUAS,
       "ncmm13TCAQtrLOSS": ncmm13TCAQtrLOSS,
       "ncmm13TCAQtrLOFS": ncmm13TCAQtrLOFS,
       "ncmm13TCADayTable": ncmm13TCADayTable,
       "ncmm13TCADayEntry": ncmm13TCADayEntry,
       "ncmm13TCADayNIDIndex": ncmm13TCADayNIDIndex,
       "ncmm13TCADayIndex": ncmm13TCADayIndex,
       "ncmm13TCADayFarEndCCV": ncmm13TCADayFarEndCCV,
       "ncmm13TCADayFarEndCES": ncmm13TCADayFarEndCES,
       "ncmm13TCADayFarEndCSES": ncmm13TCADayFarEndCSES,
       "ncmm13TCADayFarEndLUAS": ncmm13TCADayFarEndLUAS,
       "ncmm13TCADayLCV": ncmm13TCADayLCV,
       "ncmm13TCADayLES": ncmm13TCADayLES,
       "ncmm13TCADayLSES": ncmm13TCADayLSES,
       "ncmm13TCADayPCV": ncmm13TCADayPCV,
       "ncmm13TCADayPES": ncmm13TCADayPES,
       "ncmm13TCADayPSES": ncmm13TCADayPSES,
       "ncmm13TCADayCCV": ncmm13TCADayCCV,
       "ncmm13TCADayCES": ncmm13TCADayCES,
       "ncmm13TCADayCSES": ncmm13TCADayCSES,
       "ncmm13TCADaySEFS": ncmm13TCADaySEFS,
       "ncmm13TCADayAISS": ncmm13TCADayAISS,
       "ncmm13TCADayLUAS": ncmm13TCADayLUAS,
       "ncmm13TCADayLOSS": ncmm13TCADayLOSS,
       "ncmm13TCADayLOFS": ncmm13TCADayLOFS,
       "ncmm13TxAlarmTable": ncmm13TxAlarmTable,
       "ncmm13TxAlarmEntry": ncmm13TxAlarmEntry,
       "ncmm13TxAlarmNIDIndex": ncmm13TxAlarmNIDIndex,
       "ncmm13TxAlarmIndex": ncmm13TxAlarmIndex,
       "ncmm13TxYellowAlarm": ncmm13TxYellowAlarm,
       "ncmm13TxAIS": ncmm13TxAIS,
       "ncmm13TxIdleSignal": ncmm13TxIdleSignal,
       "ncmm13TxFEBE": ncmm13TxFEBE,
       "ncmm13TxFEACAlarm": ncmm13TxFEACAlarm,
       "ncmm13DS3LPBKTable": ncmm13DS3LPBKTable,
       "ncmm13DS3LPBKEntry": ncmm13DS3LPBKEntry,
       "ncmm13DS3LPBKNIDIndex": ncmm13DS3LPBKNIDIndex,
       "ncmm13DS3LPBKIndex": ncmm13DS3LPBKIndex,
       "ncmm13DS3LPBKAction": ncmm13DS3LPBKAction,
       "ncmm13T1LPBKTable": ncmm13T1LPBKTable,
       "ncmm13T1LPBKEntry": ncmm13T1LPBKEntry,
       "ncmm13T1LPBKNIDIndex": ncmm13T1LPBKNIDIndex,
       "ncmm13T1LPBKIndex": ncmm13T1LPBKIndex,
       "ncmm13T1LPBKAction": ncmm13T1LPBKAction,
       "ncmm13T1ConfigTable": ncmm13T1ConfigTable,
       "ncmm13T1ConfigEntry": ncmm13T1ConfigEntry,
       "ncmm13T1ConfigNIDIndex": ncmm13T1ConfigNIDIndex,
       "ncmm13T1LineIndex": ncmm13T1LineIndex,
       "ncmm13T1FramingFormat": ncmm13T1FramingFormat,
       "ncmm13T1LineCoding": ncmm13T1LineCoding,
       "ncmm13T1EnableNetOnesDensity": ncmm13T1EnableNetOnesDensity,
       "ncmm13T1DensityPattern": ncmm13T1DensityPattern,
       "ncmm13T1PortService": ncmm13T1PortService}
)
