# SNMP MIB module (OMNI-gx2Lm1000s-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Lm1000s-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:26 2024
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

(gx2Lm1000s,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Lm1000s")

(gi,
 motproxies) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "gi",
    "motproxies")

(trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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



class Float(Counter32):
    """Custom type Float based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2Lm1000sDescriptor_ObjectIdentity = ObjectIdentity
gx2Lm1000sDescriptor = _Gx2Lm1000sDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 1)
)
_Gx2Lm1000sAnalogTable_Object = MibTable
gx2Lm1000sAnalogTable = _Gx2Lm1000sAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2)
)
if mibBuilder.loadTexts:
    gx2Lm1000sAnalogTable.setStatus("mandatory")
_Gx2Lm1000sAnalogEntry_Object = MibTableRow
gx2Lm1000sAnalogEntry = _Gx2Lm1000sAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1)
)
gx2Lm1000sAnalogEntry.setIndexNames(
    (0, "OMNI-gx2Lm1000s-MIB", "gx2Lm1000sAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Lm1000sAnalogEntry.setStatus("mandatory")


class _Gx2Lm1000sAnalogTableIndex_Type(Integer32):
    """Custom type gx2Lm1000sAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Lm1000sAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Lm1000sAnalogTableIndex_Object = MibTableColumn
gx2Lm1000sAnalogTableIndex = _Gx2Lm1000sAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 1),
    _Gx2Lm1000sAnalogTableIndex_Type()
)
gx2Lm1000sAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000sAnalogTableIndex.setStatus("mandatory")


class _Lm1000slabelOffsetNomMonitor_Type(DisplayString):
    """Custom type lm1000slabelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Lm1000slabelOffsetNomMonitor_Object = MibTableColumn
lm1000slabelOffsetNomMonitor = _Lm1000slabelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 2),
    _Lm1000slabelOffsetNomMonitor_Type()
)
lm1000slabelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelOffsetNomMonitor.setStatus("optional")


class _Lm1000suomOffsetNomMonitor_Type(DisplayString):
    """Custom type lm1000suomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Lm1000suomOffsetNomMonitor_Object = MibTableColumn
lm1000suomOffsetNomMonitor = _Lm1000suomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 3),
    _Lm1000suomOffsetNomMonitor_Type()
)
lm1000suomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomOffsetNomMonitor.setStatus("optional")
_Lm1000smajorHighOffsetNomMonitor_Type = Float
_Lm1000smajorHighOffsetNomMonitor_Object = MibTableColumn
lm1000smajorHighOffsetNomMonitor = _Lm1000smajorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 4),
    _Lm1000smajorHighOffsetNomMonitor_Type()
)
lm1000smajorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighOffsetNomMonitor.setStatus("obsolete")
_Lm1000smajorLowOffsetNomMonitor_Type = Float
_Lm1000smajorLowOffsetNomMonitor_Object = MibTableColumn
lm1000smajorLowOffsetNomMonitor = _Lm1000smajorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 5),
    _Lm1000smajorLowOffsetNomMonitor_Type()
)
lm1000smajorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowOffsetNomMonitor.setStatus("obsolete")
_Lm1000sminorHighOffsetNomMonitor_Type = Float
_Lm1000sminorHighOffsetNomMonitor_Object = MibTableColumn
lm1000sminorHighOffsetNomMonitor = _Lm1000sminorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 6),
    _Lm1000sminorHighOffsetNomMonitor_Type()
)
lm1000sminorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighOffsetNomMonitor.setStatus("obsolete")
_Lm1000sminorLowOffsetNomMonitor_Type = Float
_Lm1000sminorLowOffsetNomMonitor_Object = MibTableColumn
lm1000sminorLowOffsetNomMonitor = _Lm1000sminorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 7),
    _Lm1000sminorLowOffsetNomMonitor_Type()
)
lm1000sminorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowOffsetNomMonitor.setStatus("obsolete")
_Lm1000scurrentValueOffsetNomMonitor_Type = Float
_Lm1000scurrentValueOffsetNomMonitor_Object = MibTableColumn
lm1000scurrentValueOffsetNomMonitor = _Lm1000scurrentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 8),
    _Lm1000scurrentValueOffsetNomMonitor_Type()
)
lm1000scurrentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueOffsetNomMonitor.setStatus("mandatory")


class _Lm1000sstateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type lm1000sstateFlagOffsetNomMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Lm1000sstateFlagOffsetNomMonitor_Object = MibTableColumn
lm1000sstateFlagOffsetNomMonitor = _Lm1000sstateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 9),
    _Lm1000sstateFlagOffsetNomMonitor_Type()
)
lm1000sstateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagOffsetNomMonitor.setStatus("mandatory")
_Lm1000sminValueOffsetNomMonitor_Type = Float
_Lm1000sminValueOffsetNomMonitor_Object = MibTableColumn
lm1000sminValueOffsetNomMonitor = _Lm1000sminValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 10),
    _Lm1000sminValueOffsetNomMonitor_Type()
)
lm1000sminValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueOffsetNomMonitor.setStatus("mandatory")
_Lm1000smaxValueOffsetNomMonitor_Type = Float
_Lm1000smaxValueOffsetNomMonitor_Object = MibTableColumn
lm1000smaxValueOffsetNomMonitor = _Lm1000smaxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 11),
    _Lm1000smaxValueOffsetNomMonitor_Type()
)
lm1000smaxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueOffsetNomMonitor.setStatus("mandatory")


class _Lm1000salarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type lm1000salarmStateOffsetNomMonitor based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Lm1000salarmStateOffsetNomMonitor_Object = MibTableColumn
lm1000salarmStateOffsetNomMonitor = _Lm1000salarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 12),
    _Lm1000salarmStateOffsetNomMonitor_Type()
)
lm1000salarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateOffsetNomMonitor.setStatus("mandatory")


class _Lm1000slabelLaserPower_Type(DisplayString):
    """Custom type lm1000slabelLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelLaserPower_Type.__name__ = "DisplayString"
_Lm1000slabelLaserPower_Object = MibTableColumn
lm1000slabelLaserPower = _Lm1000slabelLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 13),
    _Lm1000slabelLaserPower_Type()
)
lm1000slabelLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelLaserPower.setStatus("optional")


class _Lm1000suomLaserPower_Type(DisplayString):
    """Custom type lm1000suomLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomLaserPower_Type.__name__ = "DisplayString"
_Lm1000suomLaserPower_Object = MibTableColumn
lm1000suomLaserPower = _Lm1000suomLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 14),
    _Lm1000suomLaserPower_Type()
)
lm1000suomLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomLaserPower.setStatus("optional")
_Lm1000smajorHighLaserPower_Type = Float
_Lm1000smajorHighLaserPower_Object = MibTableColumn
lm1000smajorHighLaserPower = _Lm1000smajorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 15),
    _Lm1000smajorHighLaserPower_Type()
)
lm1000smajorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighLaserPower.setStatus("mandatory")
_Lm1000smajorLowLaserPower_Type = Float
_Lm1000smajorLowLaserPower_Object = MibTableColumn
lm1000smajorLowLaserPower = _Lm1000smajorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 16),
    _Lm1000smajorLowLaserPower_Type()
)
lm1000smajorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowLaserPower.setStatus("mandatory")
_Lm1000sminorHighLaserPower_Type = Float
_Lm1000sminorHighLaserPower_Object = MibTableColumn
lm1000sminorHighLaserPower = _Lm1000sminorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 17),
    _Lm1000sminorHighLaserPower_Type()
)
lm1000sminorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighLaserPower.setStatus("obsolete")
_Lm1000sminorLowLaserPower_Type = Float
_Lm1000sminorLowLaserPower_Object = MibTableColumn
lm1000sminorLowLaserPower = _Lm1000sminorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 18),
    _Lm1000sminorLowLaserPower_Type()
)
lm1000sminorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowLaserPower.setStatus("obsolete")
_Lm1000scurrentValueLaserPower_Type = Float
_Lm1000scurrentValueLaserPower_Object = MibTableColumn
lm1000scurrentValueLaserPower = _Lm1000scurrentValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 19),
    _Lm1000scurrentValueLaserPower_Type()
)
lm1000scurrentValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueLaserPower.setStatus("mandatory")


class _Lm1000sstateFlagLaserPower_Type(Integer32):
    """Custom type lm1000sstateFlagLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagLaserPower_Type.__name__ = "Integer32"
_Lm1000sstateFlagLaserPower_Object = MibTableColumn
lm1000sstateFlagLaserPower = _Lm1000sstateFlagLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 20),
    _Lm1000sstateFlagLaserPower_Type()
)
lm1000sstateFlagLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagLaserPower.setStatus("mandatory")
_Lm1000sminValueLaserPower_Type = Float
_Lm1000sminValueLaserPower_Object = MibTableColumn
lm1000sminValueLaserPower = _Lm1000sminValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 21),
    _Lm1000sminValueLaserPower_Type()
)
lm1000sminValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueLaserPower.setStatus("mandatory")
_Lm1000smaxValueLaserPower_Type = Float
_Lm1000smaxValueLaserPower_Object = MibTableColumn
lm1000smaxValueLaserPower = _Lm1000smaxValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 22),
    _Lm1000smaxValueLaserPower_Type()
)
lm1000smaxValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueLaserPower.setStatus("mandatory")


class _Lm1000salarmStateLaserPower_Type(Integer32):
    """Custom type lm1000salarmStateLaserPower based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateLaserPower_Type.__name__ = "Integer32"
_Lm1000salarmStateLaserPower_Object = MibTableColumn
lm1000salarmStateLaserPower = _Lm1000salarmStateLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 23),
    _Lm1000salarmStateLaserPower_Type()
)
lm1000salarmStateLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateLaserPower.setStatus("mandatory")


class _Lm1000slabelLaserTemp_Type(DisplayString):
    """Custom type lm1000slabelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelLaserTemp_Type.__name__ = "DisplayString"
_Lm1000slabelLaserTemp_Object = MibTableColumn
lm1000slabelLaserTemp = _Lm1000slabelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 24),
    _Lm1000slabelLaserTemp_Type()
)
lm1000slabelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelLaserTemp.setStatus("optional")


class _Lm1000suomLaserTemp_Type(DisplayString):
    """Custom type lm1000suomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomLaserTemp_Type.__name__ = "DisplayString"
_Lm1000suomLaserTemp_Object = MibTableColumn
lm1000suomLaserTemp = _Lm1000suomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 25),
    _Lm1000suomLaserTemp_Type()
)
lm1000suomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomLaserTemp.setStatus("optional")
_Lm1000smajorHighLaserTemp_Type = Float
_Lm1000smajorHighLaserTemp_Object = MibTableColumn
lm1000smajorHighLaserTemp = _Lm1000smajorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 26),
    _Lm1000smajorHighLaserTemp_Type()
)
lm1000smajorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighLaserTemp.setStatus("mandatory")
_Lm1000smajorLowLaserTemp_Type = Float
_Lm1000smajorLowLaserTemp_Object = MibTableColumn
lm1000smajorLowLaserTemp = _Lm1000smajorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 27),
    _Lm1000smajorLowLaserTemp_Type()
)
lm1000smajorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowLaserTemp.setStatus("mandatory")
_Lm1000sminorHighLaserTemp_Type = Float
_Lm1000sminorHighLaserTemp_Object = MibTableColumn
lm1000sminorHighLaserTemp = _Lm1000sminorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 28),
    _Lm1000sminorHighLaserTemp_Type()
)
lm1000sminorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighLaserTemp.setStatus("obsolete")
_Lm1000sminorLowLaserTemp_Type = Float
_Lm1000sminorLowLaserTemp_Object = MibTableColumn
lm1000sminorLowLaserTemp = _Lm1000sminorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 29),
    _Lm1000sminorLowLaserTemp_Type()
)
lm1000sminorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowLaserTemp.setStatus("obsolete")
_Lm1000scurrentValueLaserTemp_Type = Float
_Lm1000scurrentValueLaserTemp_Object = MibTableColumn
lm1000scurrentValueLaserTemp = _Lm1000scurrentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 30),
    _Lm1000scurrentValueLaserTemp_Type()
)
lm1000scurrentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueLaserTemp.setStatus("mandatory")


class _Lm1000sstateFlagLaserTemp_Type(Integer32):
    """Custom type lm1000sstateFlagLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagLaserTemp_Type.__name__ = "Integer32"
_Lm1000sstateFlagLaserTemp_Object = MibTableColumn
lm1000sstateFlagLaserTemp = _Lm1000sstateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 31),
    _Lm1000sstateFlagLaserTemp_Type()
)
lm1000sstateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagLaserTemp.setStatus("mandatory")
_Lm1000sminValueLaserTemp_Type = Float
_Lm1000sminValueLaserTemp_Object = MibTableColumn
lm1000sminValueLaserTemp = _Lm1000sminValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 32),
    _Lm1000sminValueLaserTemp_Type()
)
lm1000sminValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueLaserTemp.setStatus("mandatory")
_Lm1000smaxValueLaserTemp_Type = Float
_Lm1000smaxValueLaserTemp_Object = MibTableColumn
lm1000smaxValueLaserTemp = _Lm1000smaxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 33),
    _Lm1000smaxValueLaserTemp_Type()
)
lm1000smaxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueLaserTemp.setStatus("mandatory")


class _Lm1000salarmStateLaserTemp_Type(Integer32):
    """Custom type lm1000salarmStateLaserTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateLaserTemp_Type.__name__ = "Integer32"
_Lm1000salarmStateLaserTemp_Object = MibTableColumn
lm1000salarmStateLaserTemp = _Lm1000salarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 34),
    _Lm1000salarmStateLaserTemp_Type()
)
lm1000salarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateLaserTemp.setStatus("mandatory")


class _Lm1000slabelLaserCurrent_Type(DisplayString):
    """Custom type lm1000slabelLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelLaserCurrent_Type.__name__ = "DisplayString"
_Lm1000slabelLaserCurrent_Object = MibTableColumn
lm1000slabelLaserCurrent = _Lm1000slabelLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 35),
    _Lm1000slabelLaserCurrent_Type()
)
lm1000slabelLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelLaserCurrent.setStatus("optional")


class _Lm1000suomLaserCurrent_Type(DisplayString):
    """Custom type lm1000suomLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomLaserCurrent_Type.__name__ = "DisplayString"
_Lm1000suomLaserCurrent_Object = MibTableColumn
lm1000suomLaserCurrent = _Lm1000suomLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 36),
    _Lm1000suomLaserCurrent_Type()
)
lm1000suomLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomLaserCurrent.setStatus("optional")
_Lm1000smajorHighLaserCurrent_Type = Float
_Lm1000smajorHighLaserCurrent_Object = MibTableColumn
lm1000smajorHighLaserCurrent = _Lm1000smajorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 37),
    _Lm1000smajorHighLaserCurrent_Type()
)
lm1000smajorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighLaserCurrent.setStatus("mandatory")
_Lm1000smajorLowLaserCurrent_Type = Float
_Lm1000smajorLowLaserCurrent_Object = MibTableColumn
lm1000smajorLowLaserCurrent = _Lm1000smajorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 38),
    _Lm1000smajorLowLaserCurrent_Type()
)
lm1000smajorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowLaserCurrent.setStatus("mandatory")
_Lm1000sminorHighLaserCurrent_Type = Float
_Lm1000sminorHighLaserCurrent_Object = MibTableColumn
lm1000sminorHighLaserCurrent = _Lm1000sminorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 39),
    _Lm1000sminorHighLaserCurrent_Type()
)
lm1000sminorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighLaserCurrent.setStatus("obsolete")
_Lm1000sminorLowLaserCurrent_Type = Float
_Lm1000sminorLowLaserCurrent_Object = MibTableColumn
lm1000sminorLowLaserCurrent = _Lm1000sminorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 40),
    _Lm1000sminorLowLaserCurrent_Type()
)
lm1000sminorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowLaserCurrent.setStatus("obsolete")
_Lm1000scurrentValueLaserCurrent_Type = Float
_Lm1000scurrentValueLaserCurrent_Object = MibTableColumn
lm1000scurrentValueLaserCurrent = _Lm1000scurrentValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 41),
    _Lm1000scurrentValueLaserCurrent_Type()
)
lm1000scurrentValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueLaserCurrent.setStatus("mandatory")


class _Lm1000sstateFlagLaserCurrent_Type(Integer32):
    """Custom type lm1000sstateFlagLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagLaserCurrent_Type.__name__ = "Integer32"
_Lm1000sstateFlagLaserCurrent_Object = MibTableColumn
lm1000sstateFlagLaserCurrent = _Lm1000sstateFlagLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 42),
    _Lm1000sstateFlagLaserCurrent_Type()
)
lm1000sstateFlagLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagLaserCurrent.setStatus("mandatory")
_Lm1000sminValueLaserCurrent_Type = Float
_Lm1000sminValueLaserCurrent_Object = MibTableColumn
lm1000sminValueLaserCurrent = _Lm1000sminValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 43),
    _Lm1000sminValueLaserCurrent_Type()
)
lm1000sminValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueLaserCurrent.setStatus("mandatory")
_Lm1000smaxValueLaserCurrent_Type = Float
_Lm1000smaxValueLaserCurrent_Object = MibTableColumn
lm1000smaxValueLaserCurrent = _Lm1000smaxValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 44),
    _Lm1000smaxValueLaserCurrent_Type()
)
lm1000smaxValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueLaserCurrent.setStatus("mandatory")


class _Lm1000salarmStateLaserCurrent_Type(Integer32):
    """Custom type lm1000salarmStateLaserCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateLaserCurrent_Type.__name__ = "Integer32"
_Lm1000salarmStateLaserCurrent_Object = MibTableColumn
lm1000salarmStateLaserCurrent = _Lm1000salarmStateLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 45),
    _Lm1000salarmStateLaserCurrent_Type()
)
lm1000salarmStateLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateLaserCurrent.setStatus("mandatory")


class _Lm1000slabelTecCurrent_Type(DisplayString):
    """Custom type lm1000slabelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelTecCurrent_Type.__name__ = "DisplayString"
_Lm1000slabelTecCurrent_Object = MibTableColumn
lm1000slabelTecCurrent = _Lm1000slabelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 46),
    _Lm1000slabelTecCurrent_Type()
)
lm1000slabelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelTecCurrent.setStatus("optional")


class _Lm1000suomTecCurrent_Type(DisplayString):
    """Custom type lm1000suomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomTecCurrent_Type.__name__ = "DisplayString"
_Lm1000suomTecCurrent_Object = MibTableColumn
lm1000suomTecCurrent = _Lm1000suomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 47),
    _Lm1000suomTecCurrent_Type()
)
lm1000suomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomTecCurrent.setStatus("optional")
_Lm1000smajorHighTecCurrent_Type = Float
_Lm1000smajorHighTecCurrent_Object = MibTableColumn
lm1000smajorHighTecCurrent = _Lm1000smajorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 48),
    _Lm1000smajorHighTecCurrent_Type()
)
lm1000smajorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighTecCurrent.setStatus("mandatory")
_Lm1000smajorLowTecCurrent_Type = Float
_Lm1000smajorLowTecCurrent_Object = MibTableColumn
lm1000smajorLowTecCurrent = _Lm1000smajorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 49),
    _Lm1000smajorLowTecCurrent_Type()
)
lm1000smajorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowTecCurrent.setStatus("mandatory")
_Lm1000sminorHighTecCurrent_Type = Float
_Lm1000sminorHighTecCurrent_Object = MibTableColumn
lm1000sminorHighTecCurrent = _Lm1000sminorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 50),
    _Lm1000sminorHighTecCurrent_Type()
)
lm1000sminorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighTecCurrent.setStatus("obsolete")
_Lm1000sminorLowTecCurrent_Type = Float
_Lm1000sminorLowTecCurrent_Object = MibTableColumn
lm1000sminorLowTecCurrent = _Lm1000sminorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 51),
    _Lm1000sminorLowTecCurrent_Type()
)
lm1000sminorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowTecCurrent.setStatus("obsolete")
_Lm1000scurrentValueTecCurrent_Type = Float
_Lm1000scurrentValueTecCurrent_Object = MibTableColumn
lm1000scurrentValueTecCurrent = _Lm1000scurrentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 52),
    _Lm1000scurrentValueTecCurrent_Type()
)
lm1000scurrentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueTecCurrent.setStatus("mandatory")


class _Lm1000sstateFlagTecCurrent_Type(Integer32):
    """Custom type lm1000sstateFlagTecCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagTecCurrent_Type.__name__ = "Integer32"
_Lm1000sstateFlagTecCurrent_Object = MibTableColumn
lm1000sstateFlagTecCurrent = _Lm1000sstateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 53),
    _Lm1000sstateFlagTecCurrent_Type()
)
lm1000sstateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagTecCurrent.setStatus("mandatory")
_Lm1000sminValueTecCurrent_Type = Float
_Lm1000sminValueTecCurrent_Object = MibTableColumn
lm1000sminValueTecCurrent = _Lm1000sminValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 54),
    _Lm1000sminValueTecCurrent_Type()
)
lm1000sminValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueTecCurrent.setStatus("mandatory")
_Lm1000smaxValueTecCurrent_Type = Float
_Lm1000smaxValueTecCurrent_Object = MibTableColumn
lm1000smaxValueTecCurrent = _Lm1000smaxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 55),
    _Lm1000smaxValueTecCurrent_Type()
)
lm1000smaxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueTecCurrent.setStatus("mandatory")


class _Lm1000salarmStateTecCurrent_Type(Integer32):
    """Custom type lm1000salarmStateTecCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateTecCurrent_Type.__name__ = "Integer32"
_Lm1000salarmStateTecCurrent_Object = MibTableColumn
lm1000salarmStateTecCurrent = _Lm1000salarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 56),
    _Lm1000salarmStateTecCurrent_Type()
)
lm1000salarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateTecCurrent.setStatus("mandatory")


class _Lm1000slabelModTemp_Type(DisplayString):
    """Custom type lm1000slabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelModTemp_Type.__name__ = "DisplayString"
_Lm1000slabelModTemp_Object = MibTableColumn
lm1000slabelModTemp = _Lm1000slabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 57),
    _Lm1000slabelModTemp_Type()
)
lm1000slabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelModTemp.setStatus("optional")


class _Lm1000suomModTemp_Type(DisplayString):
    """Custom type lm1000suomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomModTemp_Type.__name__ = "DisplayString"
_Lm1000suomModTemp_Object = MibTableColumn
lm1000suomModTemp = _Lm1000suomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 58),
    _Lm1000suomModTemp_Type()
)
lm1000suomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomModTemp.setStatus("optional")
_Lm1000smajorHighModTemp_Type = Float
_Lm1000smajorHighModTemp_Object = MibTableColumn
lm1000smajorHighModTemp = _Lm1000smajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 59),
    _Lm1000smajorHighModTemp_Type()
)
lm1000smajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighModTemp.setStatus("mandatory")
_Lm1000smajorLowModTemp_Type = Float
_Lm1000smajorLowModTemp_Object = MibTableColumn
lm1000smajorLowModTemp = _Lm1000smajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 60),
    _Lm1000smajorLowModTemp_Type()
)
lm1000smajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowModTemp.setStatus("mandatory")
_Lm1000sminorHighModTemp_Type = Float
_Lm1000sminorHighModTemp_Object = MibTableColumn
lm1000sminorHighModTemp = _Lm1000sminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 61),
    _Lm1000sminorHighModTemp_Type()
)
lm1000sminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighModTemp.setStatus("mandatory")
_Lm1000sminorLowModTemp_Type = Float
_Lm1000sminorLowModTemp_Object = MibTableColumn
lm1000sminorLowModTemp = _Lm1000sminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 62),
    _Lm1000sminorLowModTemp_Type()
)
lm1000sminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowModTemp.setStatus("mandatory")
_Lm1000scurrentValueModTemp_Type = Float
_Lm1000scurrentValueModTemp_Object = MibTableColumn
lm1000scurrentValueModTemp = _Lm1000scurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 63),
    _Lm1000scurrentValueModTemp_Type()
)
lm1000scurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueModTemp.setStatus("mandatory")


class _Lm1000sstateFlagModTemp_Type(Integer32):
    """Custom type lm1000sstateFlagModTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagModTemp_Type.__name__ = "Integer32"
_Lm1000sstateFlagModTemp_Object = MibTableColumn
lm1000sstateFlagModTemp = _Lm1000sstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 64),
    _Lm1000sstateFlagModTemp_Type()
)
lm1000sstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagModTemp.setStatus("mandatory")
_Lm1000sminValueModTemp_Type = Float
_Lm1000sminValueModTemp_Object = MibTableColumn
lm1000sminValueModTemp = _Lm1000sminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 65),
    _Lm1000sminValueModTemp_Type()
)
lm1000sminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueModTemp.setStatus("mandatory")
_Lm1000smaxValueModTemp_Type = Float
_Lm1000smaxValueModTemp_Object = MibTableColumn
lm1000smaxValueModTemp = _Lm1000smaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 66),
    _Lm1000smaxValueModTemp_Type()
)
lm1000smaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueModTemp.setStatus("mandatory")


class _Lm1000salarmStateModTemp_Type(Integer32):
    """Custom type lm1000salarmStateModTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateModTemp_Type.__name__ = "Integer32"
_Lm1000salarmStateModTemp_Object = MibTableColumn
lm1000salarmStateModTemp = _Lm1000salarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 67),
    _Lm1000salarmStateModTemp_Type()
)
lm1000salarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateModTemp.setStatus("mandatory")


class _Lm1000slabelFanCurrent_Type(DisplayString):
    """Custom type lm1000slabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelFanCurrent_Type.__name__ = "DisplayString"
_Lm1000slabelFanCurrent_Object = MibTableColumn
lm1000slabelFanCurrent = _Lm1000slabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 68),
    _Lm1000slabelFanCurrent_Type()
)
lm1000slabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelFanCurrent.setStatus("optional")


class _Lm1000suomFanCurrent_Type(DisplayString):
    """Custom type lm1000suomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000suomFanCurrent_Type.__name__ = "DisplayString"
_Lm1000suomFanCurrent_Object = MibTableColumn
lm1000suomFanCurrent = _Lm1000suomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 69),
    _Lm1000suomFanCurrent_Type()
)
lm1000suomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000suomFanCurrent.setStatus("optional")
_Lm1000smajorHighFanCurrent_Type = Float
_Lm1000smajorHighFanCurrent_Object = MibTableColumn
lm1000smajorHighFanCurrent = _Lm1000smajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 70),
    _Lm1000smajorHighFanCurrent_Type()
)
lm1000smajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorHighFanCurrent.setStatus("mandatory")
_Lm1000smajorLowFanCurrent_Type = Float
_Lm1000smajorLowFanCurrent_Object = MibTableColumn
lm1000smajorLowFanCurrent = _Lm1000smajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 71),
    _Lm1000smajorLowFanCurrent_Type()
)
lm1000smajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smajorLowFanCurrent.setStatus("mandatory")
_Lm1000sminorHighFanCurrent_Type = Float
_Lm1000sminorHighFanCurrent_Object = MibTableColumn
lm1000sminorHighFanCurrent = _Lm1000sminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 72),
    _Lm1000sminorHighFanCurrent_Type()
)
lm1000sminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorHighFanCurrent.setStatus("obsolete")
_Lm1000sminorLowFanCurrent_Type = Float
_Lm1000sminorLowFanCurrent_Object = MibTableColumn
lm1000sminorLowFanCurrent = _Lm1000sminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 73),
    _Lm1000sminorLowFanCurrent_Type()
)
lm1000sminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminorLowFanCurrent.setStatus("obsolete")
_Lm1000scurrentValueFanCurrent_Type = Float
_Lm1000scurrentValueFanCurrent_Object = MibTableColumn
lm1000scurrentValueFanCurrent = _Lm1000scurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 74),
    _Lm1000scurrentValueFanCurrent_Type()
)
lm1000scurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scurrentValueFanCurrent.setStatus("mandatory")


class _Lm1000sstateFlagFanCurrent_Type(Integer32):
    """Custom type lm1000sstateFlagFanCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateFlagFanCurrent_Type.__name__ = "Integer32"
_Lm1000sstateFlagFanCurrent_Object = MibTableColumn
lm1000sstateFlagFanCurrent = _Lm1000sstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 75),
    _Lm1000sstateFlagFanCurrent_Type()
)
lm1000sstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateFlagFanCurrent.setStatus("mandatory")
_Lm1000sminValueFanCurrent_Type = Float
_Lm1000sminValueFanCurrent_Object = MibTableColumn
lm1000sminValueFanCurrent = _Lm1000sminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 76),
    _Lm1000sminValueFanCurrent_Type()
)
lm1000sminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sminValueFanCurrent.setStatus("mandatory")
_Lm1000smaxValueFanCurrent_Type = Float
_Lm1000smaxValueFanCurrent_Object = MibTableColumn
lm1000smaxValueFanCurrent = _Lm1000smaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 77),
    _Lm1000smaxValueFanCurrent_Type()
)
lm1000smaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000smaxValueFanCurrent.setStatus("mandatory")


class _Lm1000salarmStateFanCurrent_Type(Integer32):
    """Custom type lm1000salarmStateFanCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Lm1000salarmStateFanCurrent_Type.__name__ = "Integer32"
_Lm1000salarmStateFanCurrent_Object = MibTableColumn
lm1000salarmStateFanCurrent = _Lm1000salarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 2, 1, 78),
    _Lm1000salarmStateFanCurrent_Type()
)
lm1000salarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000salarmStateFanCurrent.setStatus("mandatory")
_Gx2Lm1000sDigitalTable_Object = MibTable
gx2Lm1000sDigitalTable = _Gx2Lm1000sDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3)
)
if mibBuilder.loadTexts:
    gx2Lm1000sDigitalTable.setStatus("mandatory")
_Gx2Lm1000sDigitalEntry_Object = MibTableRow
gx2Lm1000sDigitalEntry = _Gx2Lm1000sDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2)
)
gx2Lm1000sDigitalEntry.setIndexNames(
    (0, "OMNI-gx2Lm1000s-MIB", "gx2Lm1000sDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Lm1000sDigitalEntry.setStatus("mandatory")


class _Gx2Lm1000sDigitalTableIndex_Type(Integer32):
    """Custom type gx2Lm1000sDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Lm1000sDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Lm1000sDigitalTableIndex_Object = MibTableColumn
gx2Lm1000sDigitalTableIndex = _Gx2Lm1000sDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 1),
    _Gx2Lm1000sDigitalTableIndex_Type()
)
gx2Lm1000sDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000sDigitalTableIndex.setStatus("mandatory")


class _Lm1000slabelRfInput_Type(DisplayString):
    """Custom type lm1000slabelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelRfInput_Type.__name__ = "DisplayString"
_Lm1000slabelRfInput_Object = MibTableColumn
lm1000slabelRfInput = _Lm1000slabelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 2),
    _Lm1000slabelRfInput_Type()
)
lm1000slabelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelRfInput.setStatus("optional")


class _Lm1000senumRfInput_Type(DisplayString):
    """Custom type lm1000senumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000senumRfInput_Type.__name__ = "DisplayString"
_Lm1000senumRfInput_Object = MibTableColumn
lm1000senumRfInput = _Lm1000senumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 3),
    _Lm1000senumRfInput_Type()
)
lm1000senumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000senumRfInput.setStatus("optional")


class _Lm1000svalueRfInput_Type(Integer32):
    """Custom type lm1000svalueRfInput based on Integer32"""
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


_Lm1000svalueRfInput_Type.__name__ = "Integer32"
_Lm1000svalueRfInput_Object = MibTableColumn
lm1000svalueRfInput = _Lm1000svalueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 4),
    _Lm1000svalueRfInput_Type()
)
lm1000svalueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm1000svalueRfInput.setStatus("mandatory")


class _Lm1000sstateflagRfInput_Type(Integer32):
    """Custom type lm1000sstateflagRfInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagRfInput_Type.__name__ = "Integer32"
_Lm1000sstateflagRfInput_Object = MibTableColumn
lm1000sstateflagRfInput = _Lm1000sstateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 5),
    _Lm1000sstateflagRfInput_Type()
)
lm1000sstateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagRfInput.setStatus("mandatory")


class _Lm1000slabelOptOutput_Type(DisplayString):
    """Custom type lm1000slabelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelOptOutput_Type.__name__ = "DisplayString"
_Lm1000slabelOptOutput_Object = MibTableColumn
lm1000slabelOptOutput = _Lm1000slabelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 6),
    _Lm1000slabelOptOutput_Type()
)
lm1000slabelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelOptOutput.setStatus("optional")


class _Lm1000senumOptOutput_Type(DisplayString):
    """Custom type lm1000senumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000senumOptOutput_Type.__name__ = "DisplayString"
_Lm1000senumOptOutput_Object = MibTableColumn
lm1000senumOptOutput = _Lm1000senumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 7),
    _Lm1000senumOptOutput_Type()
)
lm1000senumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000senumOptOutput.setStatus("optional")


class _Lm1000svalueOptOutput_Type(Integer32):
    """Custom type lm1000svalueOptOutput based on Integer32"""
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


_Lm1000svalueOptOutput_Type.__name__ = "Integer32"
_Lm1000svalueOptOutput_Object = MibTableColumn
lm1000svalueOptOutput = _Lm1000svalueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 8),
    _Lm1000svalueOptOutput_Type()
)
lm1000svalueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm1000svalueOptOutput.setStatus("mandatory")


class _Lm1000sstateflagOptOutput_Type(Integer32):
    """Custom type lm1000sstateflagOptOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagOptOutput_Type.__name__ = "Integer32"
_Lm1000sstateflagOptOutput_Object = MibTableColumn
lm1000sstateflagOptOutput = _Lm1000sstateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 9),
    _Lm1000sstateflagOptOutput_Type()
)
lm1000sstateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagOptOutput.setStatus("mandatory")


class _Lm1000slabelAttnSetting_Type(DisplayString):
    """Custom type lm1000slabelAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelAttnSetting_Type.__name__ = "DisplayString"
_Lm1000slabelAttnSetting_Object = MibTableColumn
lm1000slabelAttnSetting = _Lm1000slabelAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 10),
    _Lm1000slabelAttnSetting_Type()
)
lm1000slabelAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelAttnSetting.setStatus("optional")


class _Lm1000senumAttnSetting_Type(DisplayString):
    """Custom type lm1000senumAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000senumAttnSetting_Type.__name__ = "DisplayString"
_Lm1000senumAttnSetting_Object = MibTableColumn
lm1000senumAttnSetting = _Lm1000senumAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 11),
    _Lm1000senumAttnSetting_Type()
)
lm1000senumAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000senumAttnSetting.setStatus("optional")


class _Lm1000svalueAttnSetting_Type(Integer32):
    """Custom type lm1000svalueAttnSetting based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("dB00-0", 1),
          ("db00-5", 2),
          ("db01-0", 3),
          ("db01-5", 4),
          ("db02-0", 5),
          ("db02-5", 6),
          ("db03-0", 7),
          ("db03-5", 8),
          ("db04-0", 9),
          ("db04-5", 10),
          ("db05-0", 11),
          ("db05-5", 12),
          ("db06-0", 13),
          ("db06-5", 14),
          ("db07-0", 15),
          ("db07-5", 16),
          ("db08-0", 17),
          ("db08-5", 18),
          ("db09-0", 19),
          ("db09-5", 20),
          ("db10-0", 21),
          ("db10-5", 22),
          ("db11-0", 23),
          ("db11-5", 24),
          ("db12-0", 25),
          ("db12-5", 26),
          ("db13-0", 27),
          ("db13-5", 28),
          ("db14-0", 29),
          ("db14-5", 30),
          ("db15-0", 31))
    )


_Lm1000svalueAttnSetting_Type.__name__ = "Integer32"
_Lm1000svalueAttnSetting_Object = MibTableColumn
lm1000svalueAttnSetting = _Lm1000svalueAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 12),
    _Lm1000svalueAttnSetting_Type()
)
lm1000svalueAttnSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm1000svalueAttnSetting.setStatus("mandatory")


class _Lm1000sstateflagAttnSetting_Type(Integer32):
    """Custom type lm1000sstateflagAttnSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagAttnSetting_Type.__name__ = "Integer32"
_Lm1000sstateflagAttnSetting_Object = MibTableColumn
lm1000sstateflagAttnSetting = _Lm1000sstateflagAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 13),
    _Lm1000sstateflagAttnSetting_Type()
)
lm1000sstateflagAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagAttnSetting.setStatus("mandatory")


class _Lm1000slabelFactoryDefault_Type(DisplayString):
    """Custom type lm1000slabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelFactoryDefault_Type.__name__ = "DisplayString"
_Lm1000slabelFactoryDefault_Object = MibTableColumn
lm1000slabelFactoryDefault = _Lm1000slabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 14),
    _Lm1000slabelFactoryDefault_Type()
)
lm1000slabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelFactoryDefault.setStatus("optional")


class _Lm1000senumFactoryDefault_Type(DisplayString):
    """Custom type lm1000senumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000senumFactoryDefault_Type.__name__ = "DisplayString"
_Lm1000senumFactoryDefault_Object = MibTableColumn
lm1000senumFactoryDefault = _Lm1000senumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 15),
    _Lm1000senumFactoryDefault_Type()
)
lm1000senumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000senumFactoryDefault.setStatus("optional")


class _Lm1000svalueFactoryDefault_Type(Integer32):
    """Custom type lm1000svalueFactoryDefault based on Integer32"""
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


_Lm1000svalueFactoryDefault_Type.__name__ = "Integer32"
_Lm1000svalueFactoryDefault_Object = MibTableColumn
lm1000svalueFactoryDefault = _Lm1000svalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 16),
    _Lm1000svalueFactoryDefault_Type()
)
lm1000svalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm1000svalueFactoryDefault.setStatus("mandatory")


class _Lm1000sstateflagFactoryDefault_Type(Integer32):
    """Custom type lm1000sstateflagFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagFactoryDefault_Type.__name__ = "Integer32"
_Lm1000sstateflagFactoryDefault_Object = MibTableColumn
lm1000sstateflagFactoryDefault = _Lm1000sstateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 3, 2, 17),
    _Lm1000sstateflagFactoryDefault_Type()
)
lm1000sstateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagFactoryDefault.setStatus("mandatory")
_Gx2Lm1000sStatusTable_Object = MibTable
gx2Lm1000sStatusTable = _Gx2Lm1000sStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4)
)
if mibBuilder.loadTexts:
    gx2Lm1000sStatusTable.setStatus("mandatory")
_Gx2Lm1000sStatusEntry_Object = MibTableRow
gx2Lm1000sStatusEntry = _Gx2Lm1000sStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3)
)
gx2Lm1000sStatusEntry.setIndexNames(
    (0, "OMNI-gx2Lm1000s-MIB", "gx2Lm1000sStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Lm1000sStatusEntry.setStatus("mandatory")


class _Gx2Lm1000sStatusTableIndex_Type(Integer32):
    """Custom type gx2Lm1000sStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Lm1000sStatusTableIndex_Type.__name__ = "Integer32"
_Gx2Lm1000sStatusTableIndex_Object = MibTableColumn
gx2Lm1000sStatusTableIndex = _Gx2Lm1000sStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 1),
    _Gx2Lm1000sStatusTableIndex_Type()
)
gx2Lm1000sStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000sStatusTableIndex.setStatus("mandatory")


class _Lm1000slabelBoot_Type(DisplayString):
    """Custom type lm1000slabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelBoot_Type.__name__ = "DisplayString"
_Lm1000slabelBoot_Object = MibTableColumn
lm1000slabelBoot = _Lm1000slabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 2),
    _Lm1000slabelBoot_Type()
)
lm1000slabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelBoot.setStatus("optional")


class _Lm1000svalueBoot_Type(Integer32):
    """Custom type lm1000svalueBoot based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueBoot_Type.__name__ = "Integer32"
_Lm1000svalueBoot_Object = MibTableColumn
lm1000svalueBoot = _Lm1000svalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 3),
    _Lm1000svalueBoot_Type()
)
lm1000svalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueBoot.setStatus("mandatory")


class _Lm1000sstateflagBoot_Type(Integer32):
    """Custom type lm1000sstateflagBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagBoot_Type.__name__ = "Integer32"
_Lm1000sstateflagBoot_Object = MibTableColumn
lm1000sstateflagBoot = _Lm1000sstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 4),
    _Lm1000sstateflagBoot_Type()
)
lm1000sstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagBoot.setStatus("mandatory")


class _Lm1000slabelFlash_Type(DisplayString):
    """Custom type lm1000slabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelFlash_Type.__name__ = "DisplayString"
_Lm1000slabelFlash_Object = MibTableColumn
lm1000slabelFlash = _Lm1000slabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 5),
    _Lm1000slabelFlash_Type()
)
lm1000slabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelFlash.setStatus("optional")


class _Lm1000svalueFlash_Type(Integer32):
    """Custom type lm1000svalueFlash based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueFlash_Type.__name__ = "Integer32"
_Lm1000svalueFlash_Object = MibTableColumn
lm1000svalueFlash = _Lm1000svalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 6),
    _Lm1000svalueFlash_Type()
)
lm1000svalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueFlash.setStatus("mandatory")


class _Lm1000sstateflagFlash_Type(Integer32):
    """Custom type lm1000sstateflagFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagFlash_Type.__name__ = "Integer32"
_Lm1000sstateflagFlash_Object = MibTableColumn
lm1000sstateflagFlash = _Lm1000sstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 7),
    _Lm1000sstateflagFlash_Type()
)
lm1000sstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagFlash.setStatus("mandatory")


class _Lm1000slabelFactoryDataCRC_Type(DisplayString):
    """Custom type lm1000slabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Lm1000slabelFactoryDataCRC_Object = MibTableColumn
lm1000slabelFactoryDataCRC = _Lm1000slabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 8),
    _Lm1000slabelFactoryDataCRC_Type()
)
lm1000slabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelFactoryDataCRC.setStatus("optional")


class _Lm1000svalueFactoryDataCRC_Type(Integer32):
    """Custom type lm1000svalueFactoryDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueFactoryDataCRC_Type.__name__ = "Integer32"
_Lm1000svalueFactoryDataCRC_Object = MibTableColumn
lm1000svalueFactoryDataCRC = _Lm1000svalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 9),
    _Lm1000svalueFactoryDataCRC_Type()
)
lm1000svalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueFactoryDataCRC.setStatus("mandatory")


class _Lm1000sstateflagFactoryDataCRC_Type(Integer32):
    """Custom type lm1000sstateflagFactoryDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Lm1000sstateflagFactoryDataCRC_Object = MibTableColumn
lm1000sstateflagFactoryDataCRC = _Lm1000sstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 10),
    _Lm1000sstateflagFactoryDataCRC_Type()
)
lm1000sstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagFactoryDataCRC.setStatus("mandatory")


class _Lm1000slabelLaserDataCRC_Type(DisplayString):
    """Custom type lm1000slabelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelLaserDataCRC_Type.__name__ = "DisplayString"
_Lm1000slabelLaserDataCRC_Object = MibTableColumn
lm1000slabelLaserDataCRC = _Lm1000slabelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 11),
    _Lm1000slabelLaserDataCRC_Type()
)
lm1000slabelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelLaserDataCRC.setStatus("optional")


class _Lm1000svalueLaserDataCRC_Type(Integer32):
    """Custom type lm1000svalueLaserDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueLaserDataCRC_Type.__name__ = "Integer32"
_Lm1000svalueLaserDataCRC_Object = MibTableColumn
lm1000svalueLaserDataCRC = _Lm1000svalueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 12),
    _Lm1000svalueLaserDataCRC_Type()
)
lm1000svalueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueLaserDataCRC.setStatus("mandatory")


class _Lm1000sstateflagLaserDataCRC_Type(Integer32):
    """Custom type lm1000sstateflagLaserDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagLaserDataCRC_Type.__name__ = "Integer32"
_Lm1000sstateflagLaserDataCRC_Object = MibTableColumn
lm1000sstateflagLaserDataCRC = _Lm1000sstateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 13),
    _Lm1000sstateflagLaserDataCRC_Type()
)
lm1000sstateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagLaserDataCRC.setStatus("mandatory")


class _Lm1000slabelAlarmDataCrc_Type(DisplayString):
    """Custom type lm1000slabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelAlarmDataCrc_Type.__name__ = "DisplayString"
_Lm1000slabelAlarmDataCrc_Object = MibTableColumn
lm1000slabelAlarmDataCrc = _Lm1000slabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 14),
    _Lm1000slabelAlarmDataCrc_Type()
)
lm1000slabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelAlarmDataCrc.setStatus("optional")


class _Lm1000svalueAlarmDataCrc_Type(Integer32):
    """Custom type lm1000svalueAlarmDataCrc based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueAlarmDataCrc_Type.__name__ = "Integer32"
_Lm1000svalueAlarmDataCrc_Object = MibTableColumn
lm1000svalueAlarmDataCrc = _Lm1000svalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 15),
    _Lm1000svalueAlarmDataCrc_Type()
)
lm1000svalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueAlarmDataCrc.setStatus("mandatory")


class _Lm1000sstateflagAlarmDataCrc_Type(Integer32):
    """Custom type lm1000sstateflagAlarmDataCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Lm1000sstateflagAlarmDataCrc_Object = MibTableColumn
lm1000sstateflagAlarmDataCrc = _Lm1000sstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 16),
    _Lm1000sstateflagAlarmDataCrc_Type()
)
lm1000sstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagAlarmDataCrc.setStatus("mandatory")


class _Lm1000slabelRFInputStatus_Type(DisplayString):
    """Custom type lm1000slabelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000slabelRFInputStatus_Type.__name__ = "DisplayString"
_Lm1000slabelRFInputStatus_Object = MibTableColumn
lm1000slabelRFInputStatus = _Lm1000slabelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 17),
    _Lm1000slabelRFInputStatus_Type()
)
lm1000slabelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000slabelRFInputStatus.setStatus("optional")


class _Lm1000svalueRFInputStatus_Type(Integer32):
    """Custom type lm1000svalueRFInputStatus based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Lm1000svalueRFInputStatus_Type.__name__ = "Integer32"
_Lm1000svalueRFInputStatus_Object = MibTableColumn
lm1000svalueRFInputStatus = _Lm1000svalueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 18),
    _Lm1000svalueRFInputStatus_Type()
)
lm1000svalueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000svalueRFInputStatus.setStatus("mandatory")


class _Lm1000sstateflagRFInputStatus_Type(Integer32):
    """Custom type lm1000sstateflagRFInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Lm1000sstateflagRFInputStatus_Type.__name__ = "Integer32"
_Lm1000sstateflagRFInputStatus_Object = MibTableColumn
lm1000sstateflagRFInputStatus = _Lm1000sstateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 4, 3, 19),
    _Lm1000sstateflagRFInputStatus_Type()
)
lm1000sstateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sstateflagRFInputStatus.setStatus("mandatory")
_Gx2Lm1000sFactoryTable_Object = MibTable
gx2Lm1000sFactoryTable = _Gx2Lm1000sFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5)
)
if mibBuilder.loadTexts:
    gx2Lm1000sFactoryTable.setStatus("mandatory")
_Gx2Lm1000sFactoryEntry_Object = MibTableRow
gx2Lm1000sFactoryEntry = _Gx2Lm1000sFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4)
)
gx2Lm1000sFactoryEntry.setIndexNames(
    (0, "OMNI-gx2Lm1000s-MIB", "gx2Lm1000sFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Lm1000sFactoryEntry.setStatus("mandatory")


class _Gx2Lm1000sFactoryTableIndex_Type(Integer32):
    """Custom type gx2Lm1000sFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Lm1000sFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Lm1000sFactoryTableIndex_Object = MibTableColumn
gx2Lm1000sFactoryTableIndex = _Gx2Lm1000sFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 1),
    _Gx2Lm1000sFactoryTableIndex_Type()
)
gx2Lm1000sFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000sFactoryTableIndex.setStatus("mandatory")
_Lm1000sbootControlByte_Type = Integer32
_Lm1000sbootControlByte_Object = MibTableColumn
lm1000sbootControlByte = _Lm1000sbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 2),
    _Lm1000sbootControlByte_Type()
)
lm1000sbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sbootControlByte.setStatus("mandatory")
_Lm1000sbootStatusByte_Type = Integer32
_Lm1000sbootStatusByte_Object = MibTableColumn
lm1000sbootStatusByte = _Lm1000sbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 3),
    _Lm1000sbootStatusByte_Type()
)
lm1000sbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sbootStatusByte.setStatus("mandatory")
_Lm1000sbank1CRC_Type = Integer32
_Lm1000sbank1CRC_Object = MibTableColumn
lm1000sbank1CRC = _Lm1000sbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 4),
    _Lm1000sbank1CRC_Type()
)
lm1000sbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sbank1CRC.setStatus("mandatory")
_Lm1000sbank2CRC_Type = Integer32
_Lm1000sbank2CRC_Object = MibTableColumn
lm1000sbank2CRC = _Lm1000sbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 5),
    _Lm1000sbank2CRC_Type()
)
lm1000sbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sbank2CRC.setStatus("mandatory")
_Lm1000sprgEEPROMByte_Type = Integer32
_Lm1000sprgEEPROMByte_Object = MibTableColumn
lm1000sprgEEPROMByte = _Lm1000sprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 6),
    _Lm1000sprgEEPROMByte_Type()
)
lm1000sprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sprgEEPROMByte.setStatus("mandatory")
_Lm1000sfactoryCRC_Type = Integer32
_Lm1000sfactoryCRC_Object = MibTableColumn
lm1000sfactoryCRC = _Lm1000sfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 7),
    _Lm1000sfactoryCRC_Type()
)
lm1000sfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sfactoryCRC.setStatus("mandatory")


class _Lm1000scalculateCRC_Type(Integer32):
    """Custom type lm1000scalculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("factory", 1),
          ("na", 2))
    )


_Lm1000scalculateCRC_Type.__name__ = "Integer32"
_Lm1000scalculateCRC_Object = MibTableColumn
lm1000scalculateCRC = _Lm1000scalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 8),
    _Lm1000scalculateCRC_Type()
)
lm1000scalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000scalculateCRC.setStatus("obsolete")
_Lm1000shourMeter_Type = Integer32
_Lm1000shourMeter_Object = MibTableColumn
lm1000shourMeter = _Lm1000shourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 9),
    _Lm1000shourMeter_Type()
)
lm1000shourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000shourMeter.setStatus("mandatory")
_Lm1000sflashPrgCntA_Type = Integer32
_Lm1000sflashPrgCntA_Object = MibTableColumn
lm1000sflashPrgCntA = _Lm1000sflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 10),
    _Lm1000sflashPrgCntA_Type()
)
lm1000sflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sflashPrgCntA.setStatus("mandatory")
_Lm1000sflashPrgCntB_Type = Integer32
_Lm1000sflashPrgCntB_Object = MibTableColumn
lm1000sflashPrgCntB = _Lm1000sflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 11),
    _Lm1000sflashPrgCntB_Type()
)
lm1000sflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sflashPrgCntB.setStatus("mandatory")


class _Lm1000sflashBankARev_Type(DisplayString):
    """Custom type lm1000sflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000sflashBankARev_Type.__name__ = "DisplayString"
_Lm1000sflashBankARev_Object = MibTableColumn
lm1000sflashBankARev = _Lm1000sflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 12),
    _Lm1000sflashBankARev_Type()
)
lm1000sflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sflashBankARev.setStatus("mandatory")


class _Lm1000sflashBankBRev_Type(DisplayString):
    """Custom type lm1000sflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm1000sflashBankBRev_Type.__name__ = "DisplayString"
_Lm1000sflashBankBRev_Object = MibTableColumn
lm1000sflashBankBRev = _Lm1000sflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 5, 4, 13),
    _Lm1000sflashBankBRev_Type()
)
lm1000sflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm1000sflashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapLM1000SConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 1)
)
trapLM1000SConfigChangeInteger.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SConfigChangeInteger.setStatus(
        ""
    )

trapLM1000SConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 2)
)
trapLM1000SConfigChangeDisplayString.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueDisplayString"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SConfigChangeDisplayString.setStatus(
        ""
    )

trapLM1000SfanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 3)
)
trapLM1000SfanCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SfanCurrentAlarm.setStatus(
        ""
    )

trapLM1000SModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 4)
)
trapLM1000SModuleTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SModuleTempAlarm.setStatus(
        ""
    )

trapLM1000SomiOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 5)
)
trapLM1000SomiOffsetAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SomiOffsetAlarm.setStatus(
        ""
    )

trapLM1000StecCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 6)
)
trapLM1000StecCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000StecCurrentAlarm.setStatus(
        ""
    )

trapLM1000SLaserCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 7)
)
trapLM1000SLaserCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SLaserCurrentAlarm.setStatus(
        ""
    )

trapLM1000SLaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 8)
)
trapLM1000SLaserTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SLaserTempAlarm.setStatus(
        ""
    )

trapLM1000SLaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 9)
)
trapLM1000SLaserPowerAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SLaserPowerAlarm.setStatus(
        ""
    )

trapLM1000SFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 10)
)
trapLM1000SFlashAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SFlashAlarm.setStatus(
        ""
    )

trapLM1000SBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 11)
)
trapLM1000SBankBootAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SBankBootAlarm.setStatus(
        ""
    )

trapLM1000SAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 12)
)
trapLM1000SAlarmDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SAlarmDataCRCAlarm.setStatus(
        ""
    )

trapLM1000SFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 13)
)
trapLM1000SFactoryDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SFactoryDataCRCAlarm.setStatus(
        ""
    )

trapLM1000SCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 14)
)
trapLM1000SCalDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SCalDataCRCAlarm.setStatus(
        ""
    )

trapLM1000SResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 15)
)
trapLM1000SResetFacDefault.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SResetFacDefault.setStatus(
        ""
    )

trapLM1000SUserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 16)
)
trapLM1000SUserRFOffAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SUserRFOffAlarm.setStatus(
        ""
    )

trapLM1000SUserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 17)
)
trapLM1000SUserOpticalOffAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SUserOpticalOffAlarm.setStatus(
        ""
    )

trapLM1000SUserSBSOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 18)
)
trapLM1000SUserSBSOffAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SUserSBSOffAlarm.setStatus(
        ""
    )

trapLM1000SRFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 19)
)
trapLM1000SRFInputAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SRFInputAlarm.setStatus(
        ""
    )

trapLM1000SRFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31, 0, 20)
)
trapLM1000SRFOverloadAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLM1000SRFOverloadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Lm1000s-MIB",
    **{"Float": Float,
       "trapLM1000SConfigChangeInteger": trapLM1000SConfigChangeInteger,
       "trapLM1000SConfigChangeDisplayString": trapLM1000SConfigChangeDisplayString,
       "trapLM1000SfanCurrentAlarm": trapLM1000SfanCurrentAlarm,
       "trapLM1000SModuleTempAlarm": trapLM1000SModuleTempAlarm,
       "trapLM1000SomiOffsetAlarm": trapLM1000SomiOffsetAlarm,
       "trapLM1000StecCurrentAlarm": trapLM1000StecCurrentAlarm,
       "trapLM1000SLaserCurrentAlarm": trapLM1000SLaserCurrentAlarm,
       "trapLM1000SLaserTempAlarm": trapLM1000SLaserTempAlarm,
       "trapLM1000SLaserPowerAlarm": trapLM1000SLaserPowerAlarm,
       "trapLM1000SFlashAlarm": trapLM1000SFlashAlarm,
       "trapLM1000SBankBootAlarm": trapLM1000SBankBootAlarm,
       "trapLM1000SAlarmDataCRCAlarm": trapLM1000SAlarmDataCRCAlarm,
       "trapLM1000SFactoryDataCRCAlarm": trapLM1000SFactoryDataCRCAlarm,
       "trapLM1000SCalDataCRCAlarm": trapLM1000SCalDataCRCAlarm,
       "trapLM1000SResetFacDefault": trapLM1000SResetFacDefault,
       "trapLM1000SUserRFOffAlarm": trapLM1000SUserRFOffAlarm,
       "trapLM1000SUserOpticalOffAlarm": trapLM1000SUserOpticalOffAlarm,
       "trapLM1000SUserSBSOffAlarm": trapLM1000SUserSBSOffAlarm,
       "trapLM1000SRFInputAlarm": trapLM1000SRFInputAlarm,
       "trapLM1000SRFOverloadAlarm": trapLM1000SRFOverloadAlarm,
       "gx2Lm1000sDescriptor": gx2Lm1000sDescriptor,
       "gx2Lm1000sAnalogTable": gx2Lm1000sAnalogTable,
       "gx2Lm1000sAnalogEntry": gx2Lm1000sAnalogEntry,
       "gx2Lm1000sAnalogTableIndex": gx2Lm1000sAnalogTableIndex,
       "lm1000slabelOffsetNomMonitor": lm1000slabelOffsetNomMonitor,
       "lm1000suomOffsetNomMonitor": lm1000suomOffsetNomMonitor,
       "lm1000smajorHighOffsetNomMonitor": lm1000smajorHighOffsetNomMonitor,
       "lm1000smajorLowOffsetNomMonitor": lm1000smajorLowOffsetNomMonitor,
       "lm1000sminorHighOffsetNomMonitor": lm1000sminorHighOffsetNomMonitor,
       "lm1000sminorLowOffsetNomMonitor": lm1000sminorLowOffsetNomMonitor,
       "lm1000scurrentValueOffsetNomMonitor": lm1000scurrentValueOffsetNomMonitor,
       "lm1000sstateFlagOffsetNomMonitor": lm1000sstateFlagOffsetNomMonitor,
       "lm1000sminValueOffsetNomMonitor": lm1000sminValueOffsetNomMonitor,
       "lm1000smaxValueOffsetNomMonitor": lm1000smaxValueOffsetNomMonitor,
       "lm1000salarmStateOffsetNomMonitor": lm1000salarmStateOffsetNomMonitor,
       "lm1000slabelLaserPower": lm1000slabelLaserPower,
       "lm1000suomLaserPower": lm1000suomLaserPower,
       "lm1000smajorHighLaserPower": lm1000smajorHighLaserPower,
       "lm1000smajorLowLaserPower": lm1000smajorLowLaserPower,
       "lm1000sminorHighLaserPower": lm1000sminorHighLaserPower,
       "lm1000sminorLowLaserPower": lm1000sminorLowLaserPower,
       "lm1000scurrentValueLaserPower": lm1000scurrentValueLaserPower,
       "lm1000sstateFlagLaserPower": lm1000sstateFlagLaserPower,
       "lm1000sminValueLaserPower": lm1000sminValueLaserPower,
       "lm1000smaxValueLaserPower": lm1000smaxValueLaserPower,
       "lm1000salarmStateLaserPower": lm1000salarmStateLaserPower,
       "lm1000slabelLaserTemp": lm1000slabelLaserTemp,
       "lm1000suomLaserTemp": lm1000suomLaserTemp,
       "lm1000smajorHighLaserTemp": lm1000smajorHighLaserTemp,
       "lm1000smajorLowLaserTemp": lm1000smajorLowLaserTemp,
       "lm1000sminorHighLaserTemp": lm1000sminorHighLaserTemp,
       "lm1000sminorLowLaserTemp": lm1000sminorLowLaserTemp,
       "lm1000scurrentValueLaserTemp": lm1000scurrentValueLaserTemp,
       "lm1000sstateFlagLaserTemp": lm1000sstateFlagLaserTemp,
       "lm1000sminValueLaserTemp": lm1000sminValueLaserTemp,
       "lm1000smaxValueLaserTemp": lm1000smaxValueLaserTemp,
       "lm1000salarmStateLaserTemp": lm1000salarmStateLaserTemp,
       "lm1000slabelLaserCurrent": lm1000slabelLaserCurrent,
       "lm1000suomLaserCurrent": lm1000suomLaserCurrent,
       "lm1000smajorHighLaserCurrent": lm1000smajorHighLaserCurrent,
       "lm1000smajorLowLaserCurrent": lm1000smajorLowLaserCurrent,
       "lm1000sminorHighLaserCurrent": lm1000sminorHighLaserCurrent,
       "lm1000sminorLowLaserCurrent": lm1000sminorLowLaserCurrent,
       "lm1000scurrentValueLaserCurrent": lm1000scurrentValueLaserCurrent,
       "lm1000sstateFlagLaserCurrent": lm1000sstateFlagLaserCurrent,
       "lm1000sminValueLaserCurrent": lm1000sminValueLaserCurrent,
       "lm1000smaxValueLaserCurrent": lm1000smaxValueLaserCurrent,
       "lm1000salarmStateLaserCurrent": lm1000salarmStateLaserCurrent,
       "lm1000slabelTecCurrent": lm1000slabelTecCurrent,
       "lm1000suomTecCurrent": lm1000suomTecCurrent,
       "lm1000smajorHighTecCurrent": lm1000smajorHighTecCurrent,
       "lm1000smajorLowTecCurrent": lm1000smajorLowTecCurrent,
       "lm1000sminorHighTecCurrent": lm1000sminorHighTecCurrent,
       "lm1000sminorLowTecCurrent": lm1000sminorLowTecCurrent,
       "lm1000scurrentValueTecCurrent": lm1000scurrentValueTecCurrent,
       "lm1000sstateFlagTecCurrent": lm1000sstateFlagTecCurrent,
       "lm1000sminValueTecCurrent": lm1000sminValueTecCurrent,
       "lm1000smaxValueTecCurrent": lm1000smaxValueTecCurrent,
       "lm1000salarmStateTecCurrent": lm1000salarmStateTecCurrent,
       "lm1000slabelModTemp": lm1000slabelModTemp,
       "lm1000suomModTemp": lm1000suomModTemp,
       "lm1000smajorHighModTemp": lm1000smajorHighModTemp,
       "lm1000smajorLowModTemp": lm1000smajorLowModTemp,
       "lm1000sminorHighModTemp": lm1000sminorHighModTemp,
       "lm1000sminorLowModTemp": lm1000sminorLowModTemp,
       "lm1000scurrentValueModTemp": lm1000scurrentValueModTemp,
       "lm1000sstateFlagModTemp": lm1000sstateFlagModTemp,
       "lm1000sminValueModTemp": lm1000sminValueModTemp,
       "lm1000smaxValueModTemp": lm1000smaxValueModTemp,
       "lm1000salarmStateModTemp": lm1000salarmStateModTemp,
       "lm1000slabelFanCurrent": lm1000slabelFanCurrent,
       "lm1000suomFanCurrent": lm1000suomFanCurrent,
       "lm1000smajorHighFanCurrent": lm1000smajorHighFanCurrent,
       "lm1000smajorLowFanCurrent": lm1000smajorLowFanCurrent,
       "lm1000sminorHighFanCurrent": lm1000sminorHighFanCurrent,
       "lm1000sminorLowFanCurrent": lm1000sminorLowFanCurrent,
       "lm1000scurrentValueFanCurrent": lm1000scurrentValueFanCurrent,
       "lm1000sstateFlagFanCurrent": lm1000sstateFlagFanCurrent,
       "lm1000sminValueFanCurrent": lm1000sminValueFanCurrent,
       "lm1000smaxValueFanCurrent": lm1000smaxValueFanCurrent,
       "lm1000salarmStateFanCurrent": lm1000salarmStateFanCurrent,
       "gx2Lm1000sDigitalTable": gx2Lm1000sDigitalTable,
       "gx2Lm1000sDigitalEntry": gx2Lm1000sDigitalEntry,
       "gx2Lm1000sDigitalTableIndex": gx2Lm1000sDigitalTableIndex,
       "lm1000slabelRfInput": lm1000slabelRfInput,
       "lm1000senumRfInput": lm1000senumRfInput,
       "lm1000svalueRfInput": lm1000svalueRfInput,
       "lm1000sstateflagRfInput": lm1000sstateflagRfInput,
       "lm1000slabelOptOutput": lm1000slabelOptOutput,
       "lm1000senumOptOutput": lm1000senumOptOutput,
       "lm1000svalueOptOutput": lm1000svalueOptOutput,
       "lm1000sstateflagOptOutput": lm1000sstateflagOptOutput,
       "lm1000slabelAttnSetting": lm1000slabelAttnSetting,
       "lm1000senumAttnSetting": lm1000senumAttnSetting,
       "lm1000svalueAttnSetting": lm1000svalueAttnSetting,
       "lm1000sstateflagAttnSetting": lm1000sstateflagAttnSetting,
       "lm1000slabelFactoryDefault": lm1000slabelFactoryDefault,
       "lm1000senumFactoryDefault": lm1000senumFactoryDefault,
       "lm1000svalueFactoryDefault": lm1000svalueFactoryDefault,
       "lm1000sstateflagFactoryDefault": lm1000sstateflagFactoryDefault,
       "gx2Lm1000sStatusTable": gx2Lm1000sStatusTable,
       "gx2Lm1000sStatusEntry": gx2Lm1000sStatusEntry,
       "gx2Lm1000sStatusTableIndex": gx2Lm1000sStatusTableIndex,
       "lm1000slabelBoot": lm1000slabelBoot,
       "lm1000svalueBoot": lm1000svalueBoot,
       "lm1000sstateflagBoot": lm1000sstateflagBoot,
       "lm1000slabelFlash": lm1000slabelFlash,
       "lm1000svalueFlash": lm1000svalueFlash,
       "lm1000sstateflagFlash": lm1000sstateflagFlash,
       "lm1000slabelFactoryDataCRC": lm1000slabelFactoryDataCRC,
       "lm1000svalueFactoryDataCRC": lm1000svalueFactoryDataCRC,
       "lm1000sstateflagFactoryDataCRC": lm1000sstateflagFactoryDataCRC,
       "lm1000slabelLaserDataCRC": lm1000slabelLaserDataCRC,
       "lm1000svalueLaserDataCRC": lm1000svalueLaserDataCRC,
       "lm1000sstateflagLaserDataCRC": lm1000sstateflagLaserDataCRC,
       "lm1000slabelAlarmDataCrc": lm1000slabelAlarmDataCrc,
       "lm1000svalueAlarmDataCrc": lm1000svalueAlarmDataCrc,
       "lm1000sstateflagAlarmDataCrc": lm1000sstateflagAlarmDataCrc,
       "lm1000slabelRFInputStatus": lm1000slabelRFInputStatus,
       "lm1000svalueRFInputStatus": lm1000svalueRFInputStatus,
       "lm1000sstateflagRFInputStatus": lm1000sstateflagRFInputStatus,
       "gx2Lm1000sFactoryTable": gx2Lm1000sFactoryTable,
       "gx2Lm1000sFactoryEntry": gx2Lm1000sFactoryEntry,
       "gx2Lm1000sFactoryTableIndex": gx2Lm1000sFactoryTableIndex,
       "lm1000sbootControlByte": lm1000sbootControlByte,
       "lm1000sbootStatusByte": lm1000sbootStatusByte,
       "lm1000sbank1CRC": lm1000sbank1CRC,
       "lm1000sbank2CRC": lm1000sbank2CRC,
       "lm1000sprgEEPROMByte": lm1000sprgEEPROMByte,
       "lm1000sfactoryCRC": lm1000sfactoryCRC,
       "lm1000scalculateCRC": lm1000scalculateCRC,
       "lm1000shourMeter": lm1000shourMeter,
       "lm1000sflashPrgCntA": lm1000sflashPrgCntA,
       "lm1000sflashPrgCntB": lm1000sflashPrgCntB,
       "lm1000sflashBankARev": lm1000sflashBankARev,
       "lm1000sflashBankBRev": lm1000sflashBankBRev}
)
