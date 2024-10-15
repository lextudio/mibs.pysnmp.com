# SNMP MIB module (OMNI-gx2Dm870-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Dm870-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:17 2024
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

(gx2Dm870,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Dm870")

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

_Gx2Dm870Descriptor_ObjectIdentity = ObjectIdentity
gx2Dm870Descriptor = _Gx2Dm870Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 1)
)
_Gx2Dm870AnalogTable_Object = MibTable
gx2Dm870AnalogTable = _Gx2Dm870AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gx2Dm870AnalogTable.setStatus("mandatory")
_Gx2Dm870AnalogEntry_Object = MibTableRow
gx2Dm870AnalogEntry = _Gx2Dm870AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1)
)
gx2Dm870AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Dm870-MIB", "gx2Dm870AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm870AnalogEntry.setStatus("mandatory")


class _Gx2Dm870AnalogTableIndex_Type(Integer32):
    """Custom type gx2Dm870AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm870AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Dm870AnalogTableIndex_Object = MibTableColumn
gx2Dm870AnalogTableIndex = _Gx2Dm870AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 1),
    _Gx2Dm870AnalogTableIndex_Type()
)
gx2Dm870AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm870AnalogTableIndex.setStatus("mandatory")


class _Dm870labelOffsetNomMonitor_Type(DisplayString):
    """Custom type dm870labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm870labelOffsetNomMonitor_Object = MibTableColumn
dm870labelOffsetNomMonitor = _Dm870labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 2),
    _Dm870labelOffsetNomMonitor_Type()
)
dm870labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelOffsetNomMonitor.setStatus("optional")


class _Dm870uomOffsetNomMonitor_Type(DisplayString):
    """Custom type dm870uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm870uomOffsetNomMonitor_Object = MibTableColumn
dm870uomOffsetNomMonitor = _Dm870uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 3),
    _Dm870uomOffsetNomMonitor_Type()
)
dm870uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomOffsetNomMonitor.setStatus("optional")
_Dm870majorHighOffsetNomMonitor_Type = Float
_Dm870majorHighOffsetNomMonitor_Object = MibTableColumn
dm870majorHighOffsetNomMonitor = _Dm870majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 4),
    _Dm870majorHighOffsetNomMonitor_Type()
)
dm870majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighOffsetNomMonitor.setStatus("mandatory")
_Dm870majorLowOffsetNomMonitor_Type = Float
_Dm870majorLowOffsetNomMonitor_Object = MibTableColumn
dm870majorLowOffsetNomMonitor = _Dm870majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 5),
    _Dm870majorLowOffsetNomMonitor_Type()
)
dm870majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowOffsetNomMonitor.setStatus("mandatory")
_Dm870minorHighOffsetNomMonitor_Type = Float
_Dm870minorHighOffsetNomMonitor_Object = MibTableColumn
dm870minorHighOffsetNomMonitor = _Dm870minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 6),
    _Dm870minorHighOffsetNomMonitor_Type()
)
dm870minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighOffsetNomMonitor.setStatus("mandatory")
_Dm870minorLowOffsetNomMonitor_Type = Float
_Dm870minorLowOffsetNomMonitor_Object = MibTableColumn
dm870minorLowOffsetNomMonitor = _Dm870minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 7),
    _Dm870minorLowOffsetNomMonitor_Type()
)
dm870minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowOffsetNomMonitor.setStatus("mandatory")
_Dm870currentValueOffsetNomMonitor_Type = Float
_Dm870currentValueOffsetNomMonitor_Object = MibTableColumn
dm870currentValueOffsetNomMonitor = _Dm870currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 8),
    _Dm870currentValueOffsetNomMonitor_Type()
)
dm870currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueOffsetNomMonitor.setStatus("mandatory")


class _Dm870stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type dm870stateFlagOffsetNomMonitor based on Integer32"""
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


_Dm870stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm870stateFlagOffsetNomMonitor_Object = MibTableColumn
dm870stateFlagOffsetNomMonitor = _Dm870stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 9),
    _Dm870stateFlagOffsetNomMonitor_Type()
)
dm870stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagOffsetNomMonitor.setStatus("mandatory")
_Dm870minValueOffsetNomMonitor_Type = Float
_Dm870minValueOffsetNomMonitor_Object = MibTableColumn
dm870minValueOffsetNomMonitor = _Dm870minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 10),
    _Dm870minValueOffsetNomMonitor_Type()
)
dm870minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueOffsetNomMonitor.setStatus("mandatory")
_Dm870maxValueOffsetNomMonitor_Type = Float
_Dm870maxValueOffsetNomMonitor_Object = MibTableColumn
dm870maxValueOffsetNomMonitor = _Dm870maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 11),
    _Dm870maxValueOffsetNomMonitor_Type()
)
dm870maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueOffsetNomMonitor.setStatus("mandatory")


class _Dm870alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type dm870alarmStateOffsetNomMonitor based on Integer32"""
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


_Dm870alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm870alarmStateOffsetNomMonitor_Object = MibTableColumn
dm870alarmStateOffsetNomMonitor = _Dm870alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 12),
    _Dm870alarmStateOffsetNomMonitor_Type()
)
dm870alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Dm870labelOffsetNomCnt_Type(DisplayString):
    """Custom type dm870labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm870labelOffsetNomCnt_Object = MibTableColumn
dm870labelOffsetNomCnt = _Dm870labelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 13),
    _Dm870labelOffsetNomCnt_Type()
)
dm870labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelOffsetNomCnt.setStatus("optional")


class _Dm870uomOffsetNomCnt_Type(DisplayString):
    """Custom type dm870uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm870uomOffsetNomCnt_Object = MibTableColumn
dm870uomOffsetNomCnt = _Dm870uomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 14),
    _Dm870uomOffsetNomCnt_Type()
)
dm870uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomOffsetNomCnt.setStatus("optional")
_Dm870majorHighOffsetNomCnt_Type = Float
_Dm870majorHighOffsetNomCnt_Object = MibTableColumn
dm870majorHighOffsetNomCnt = _Dm870majorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 15),
    _Dm870majorHighOffsetNomCnt_Type()
)
dm870majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighOffsetNomCnt.setStatus("obsolete")
_Dm870majorLowOffsetNomCnt_Type = Float
_Dm870majorLowOffsetNomCnt_Object = MibTableColumn
dm870majorLowOffsetNomCnt = _Dm870majorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 16),
    _Dm870majorLowOffsetNomCnt_Type()
)
dm870majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowOffsetNomCnt.setStatus("obsolete")
_Dm870minorHighOffsetNomCnt_Type = Float
_Dm870minorHighOffsetNomCnt_Object = MibTableColumn
dm870minorHighOffsetNomCnt = _Dm870minorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 17),
    _Dm870minorHighOffsetNomCnt_Type()
)
dm870minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighOffsetNomCnt.setStatus("obsolete")
_Dm870minorLowOffsetNomCnt_Type = Float
_Dm870minorLowOffsetNomCnt_Object = MibTableColumn
dm870minorLowOffsetNomCnt = _Dm870minorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 18),
    _Dm870minorLowOffsetNomCnt_Type()
)
dm870minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowOffsetNomCnt.setStatus("obsolete")
_Dm870currentValueOffsetNomCnt_Type = Float
_Dm870currentValueOffsetNomCnt_Object = MibTableColumn
dm870currentValueOffsetNomCnt = _Dm870currentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 19),
    _Dm870currentValueOffsetNomCnt_Type()
)
dm870currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870currentValueOffsetNomCnt.setStatus("mandatory")


class _Dm870stateFlagOffsetNomCnt_Type(Integer32):
    """Custom type dm870stateFlagOffsetNomCnt based on Integer32"""
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


_Dm870stateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_Dm870stateFlagOffsetNomCnt_Object = MibTableColumn
dm870stateFlagOffsetNomCnt = _Dm870stateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 20),
    _Dm870stateFlagOffsetNomCnt_Type()
)
dm870stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagOffsetNomCnt.setStatus("mandatory")
_Dm870minValueOffsetNomCnt_Type = Float
_Dm870minValueOffsetNomCnt_Object = MibTableColumn
dm870minValueOffsetNomCnt = _Dm870minValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 21),
    _Dm870minValueOffsetNomCnt_Type()
)
dm870minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueOffsetNomCnt.setStatus("mandatory")
_Dm870maxValueOffsetNomCnt_Type = Float
_Dm870maxValueOffsetNomCnt_Object = MibTableColumn
dm870maxValueOffsetNomCnt = _Dm870maxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 22),
    _Dm870maxValueOffsetNomCnt_Type()
)
dm870maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueOffsetNomCnt.setStatus("mandatory")


class _Dm870alarmStateOffsetNomCnt_Type(Integer32):
    """Custom type dm870alarmStateOffsetNomCnt based on Integer32"""
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


_Dm870alarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_Dm870alarmStateOffsetNomCnt_Object = MibTableColumn
dm870alarmStateOffsetNomCnt = _Dm870alarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 23),
    _Dm870alarmStateOffsetNomCnt_Type()
)
dm870alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateOffsetNomCnt.setStatus("obsolete")


class _Dm870labelAttenSetting_Type(DisplayString):
    """Custom type dm870labelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelAttenSetting_Type.__name__ = "DisplayString"
_Dm870labelAttenSetting_Object = MibTableColumn
dm870labelAttenSetting = _Dm870labelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 24),
    _Dm870labelAttenSetting_Type()
)
dm870labelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelAttenSetting.setStatus("optional")


class _Dm870uomAttenSetting_Type(DisplayString):
    """Custom type dm870uomAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomAttenSetting_Type.__name__ = "DisplayString"
_Dm870uomAttenSetting_Object = MibTableColumn
dm870uomAttenSetting = _Dm870uomAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 25),
    _Dm870uomAttenSetting_Type()
)
dm870uomAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomAttenSetting.setStatus("optional")
_Dm870majorHighAttenSetting_Type = Float
_Dm870majorHighAttenSetting_Object = MibTableColumn
dm870majorHighAttenSetting = _Dm870majorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 26),
    _Dm870majorHighAttenSetting_Type()
)
dm870majorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighAttenSetting.setStatus("obsolete")
_Dm870majorLowAttenSetting_Type = Float
_Dm870majorLowAttenSetting_Object = MibTableColumn
dm870majorLowAttenSetting = _Dm870majorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 27),
    _Dm870majorLowAttenSetting_Type()
)
dm870majorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowAttenSetting.setStatus("obsolete")
_Dm870minorHighAttenSetting_Type = Float
_Dm870minorHighAttenSetting_Object = MibTableColumn
dm870minorHighAttenSetting = _Dm870minorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 28),
    _Dm870minorHighAttenSetting_Type()
)
dm870minorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighAttenSetting.setStatus("obsolete")
_Dm870minorLowAttenSetting_Type = Float
_Dm870minorLowAttenSetting_Object = MibTableColumn
dm870minorLowAttenSetting = _Dm870minorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 29),
    _Dm870minorLowAttenSetting_Type()
)
dm870minorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowAttenSetting.setStatus("obsolete")
_Dm870currentValueAttenSetting_Type = Float
_Dm870currentValueAttenSetting_Object = MibTableColumn
dm870currentValueAttenSetting = _Dm870currentValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 30),
    _Dm870currentValueAttenSetting_Type()
)
dm870currentValueAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870currentValueAttenSetting.setStatus("mandatory")


class _Dm870stateFlagAttenSetting_Type(Integer32):
    """Custom type dm870stateFlagAttenSetting based on Integer32"""
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


_Dm870stateFlagAttenSetting_Type.__name__ = "Integer32"
_Dm870stateFlagAttenSetting_Object = MibTableColumn
dm870stateFlagAttenSetting = _Dm870stateFlagAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 31),
    _Dm870stateFlagAttenSetting_Type()
)
dm870stateFlagAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagAttenSetting.setStatus("mandatory")
_Dm870minValueAttenSetting_Type = Float
_Dm870minValueAttenSetting_Object = MibTableColumn
dm870minValueAttenSetting = _Dm870minValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 32),
    _Dm870minValueAttenSetting_Type()
)
dm870minValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueAttenSetting.setStatus("mandatory")
_Dm870maxValueAttenSetting_Type = Float
_Dm870maxValueAttenSetting_Object = MibTableColumn
dm870maxValueAttenSetting = _Dm870maxValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 33),
    _Dm870maxValueAttenSetting_Type()
)
dm870maxValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueAttenSetting.setStatus("mandatory")


class _Dm870alarmStateAttenSetting_Type(Integer32):
    """Custom type dm870alarmStateAttenSetting based on Integer32"""
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


_Dm870alarmStateAttenSetting_Type.__name__ = "Integer32"
_Dm870alarmStateAttenSetting_Object = MibTableColumn
dm870alarmStateAttenSetting = _Dm870alarmStateAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 34),
    _Dm870alarmStateAttenSetting_Type()
)
dm870alarmStateAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateAttenSetting.setStatus("mandatory")


class _Dm870labelLaserPower_Type(DisplayString):
    """Custom type dm870labelLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelLaserPower_Type.__name__ = "DisplayString"
_Dm870labelLaserPower_Object = MibTableColumn
dm870labelLaserPower = _Dm870labelLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 35),
    _Dm870labelLaserPower_Type()
)
dm870labelLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelLaserPower.setStatus("optional")


class _Dm870uomLaserPower_Type(DisplayString):
    """Custom type dm870uomLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomLaserPower_Type.__name__ = "DisplayString"
_Dm870uomLaserPower_Object = MibTableColumn
dm870uomLaserPower = _Dm870uomLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 36),
    _Dm870uomLaserPower_Type()
)
dm870uomLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomLaserPower.setStatus("optional")
_Dm870majorHighLaserPower_Type = Float
_Dm870majorHighLaserPower_Object = MibTableColumn
dm870majorHighLaserPower = _Dm870majorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 37),
    _Dm870majorHighLaserPower_Type()
)
dm870majorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighLaserPower.setStatus("mandatory")
_Dm870majorLowLaserPower_Type = Float
_Dm870majorLowLaserPower_Object = MibTableColumn
dm870majorLowLaserPower = _Dm870majorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 38),
    _Dm870majorLowLaserPower_Type()
)
dm870majorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowLaserPower.setStatus("mandatory")
_Dm870minorHighLaserPower_Type = Float
_Dm870minorHighLaserPower_Object = MibTableColumn
dm870minorHighLaserPower = _Dm870minorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 39),
    _Dm870minorHighLaserPower_Type()
)
dm870minorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighLaserPower.setStatus("obsolete")
_Dm870minorLowLaserPower_Type = Float
_Dm870minorLowLaserPower_Object = MibTableColumn
dm870minorLowLaserPower = _Dm870minorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 40),
    _Dm870minorLowLaserPower_Type()
)
dm870minorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowLaserPower.setStatus("obsolete")
_Dm870currentValueLaserPower_Type = Float
_Dm870currentValueLaserPower_Object = MibTableColumn
dm870currentValueLaserPower = _Dm870currentValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 41),
    _Dm870currentValueLaserPower_Type()
)
dm870currentValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueLaserPower.setStatus("mandatory")


class _Dm870stateFlagLaserPower_Type(Integer32):
    """Custom type dm870stateFlagLaserPower based on Integer32"""
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


_Dm870stateFlagLaserPower_Type.__name__ = "Integer32"
_Dm870stateFlagLaserPower_Object = MibTableColumn
dm870stateFlagLaserPower = _Dm870stateFlagLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 42),
    _Dm870stateFlagLaserPower_Type()
)
dm870stateFlagLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagLaserPower.setStatus("mandatory")
_Dm870minValueLaserPower_Type = Float
_Dm870minValueLaserPower_Object = MibTableColumn
dm870minValueLaserPower = _Dm870minValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 43),
    _Dm870minValueLaserPower_Type()
)
dm870minValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueLaserPower.setStatus("mandatory")
_Dm870maxValueLaserPower_Type = Float
_Dm870maxValueLaserPower_Object = MibTableColumn
dm870maxValueLaserPower = _Dm870maxValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 44),
    _Dm870maxValueLaserPower_Type()
)
dm870maxValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueLaserPower.setStatus("mandatory")


class _Dm870alarmStateLaserPower_Type(Integer32):
    """Custom type dm870alarmStateLaserPower based on Integer32"""
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


_Dm870alarmStateLaserPower_Type.__name__ = "Integer32"
_Dm870alarmStateLaserPower_Object = MibTableColumn
dm870alarmStateLaserPower = _Dm870alarmStateLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 45),
    _Dm870alarmStateLaserPower_Type()
)
dm870alarmStateLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateLaserPower.setStatus("mandatory")


class _Dm870labelLaserTemp_Type(DisplayString):
    """Custom type dm870labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelLaserTemp_Type.__name__ = "DisplayString"
_Dm870labelLaserTemp_Object = MibTableColumn
dm870labelLaserTemp = _Dm870labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 46),
    _Dm870labelLaserTemp_Type()
)
dm870labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelLaserTemp.setStatus("optional")


class _Dm870uomLaserTemp_Type(DisplayString):
    """Custom type dm870uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomLaserTemp_Type.__name__ = "DisplayString"
_Dm870uomLaserTemp_Object = MibTableColumn
dm870uomLaserTemp = _Dm870uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 47),
    _Dm870uomLaserTemp_Type()
)
dm870uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomLaserTemp.setStatus("optional")
_Dm870majorHighLaserTemp_Type = Float
_Dm870majorHighLaserTemp_Object = MibTableColumn
dm870majorHighLaserTemp = _Dm870majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 48),
    _Dm870majorHighLaserTemp_Type()
)
dm870majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighLaserTemp.setStatus("mandatory")
_Dm870majorLowLaserTemp_Type = Float
_Dm870majorLowLaserTemp_Object = MibTableColumn
dm870majorLowLaserTemp = _Dm870majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 49),
    _Dm870majorLowLaserTemp_Type()
)
dm870majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowLaserTemp.setStatus("mandatory")
_Dm870minorHighLaserTemp_Type = Float
_Dm870minorHighLaserTemp_Object = MibTableColumn
dm870minorHighLaserTemp = _Dm870minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 50),
    _Dm870minorHighLaserTemp_Type()
)
dm870minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighLaserTemp.setStatus("obsolete")
_Dm870minorLowLaserTemp_Type = Float
_Dm870minorLowLaserTemp_Object = MibTableColumn
dm870minorLowLaserTemp = _Dm870minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 51),
    _Dm870minorLowLaserTemp_Type()
)
dm870minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowLaserTemp.setStatus("obsolete")
_Dm870currentValueLaserTemp_Type = Float
_Dm870currentValueLaserTemp_Object = MibTableColumn
dm870currentValueLaserTemp = _Dm870currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 52),
    _Dm870currentValueLaserTemp_Type()
)
dm870currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueLaserTemp.setStatus("mandatory")


class _Dm870stateFlagLaserTemp_Type(Integer32):
    """Custom type dm870stateFlagLaserTemp based on Integer32"""
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


_Dm870stateFlagLaserTemp_Type.__name__ = "Integer32"
_Dm870stateFlagLaserTemp_Object = MibTableColumn
dm870stateFlagLaserTemp = _Dm870stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 53),
    _Dm870stateFlagLaserTemp_Type()
)
dm870stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagLaserTemp.setStatus("mandatory")
_Dm870minValueLaserTemp_Type = Float
_Dm870minValueLaserTemp_Object = MibTableColumn
dm870minValueLaserTemp = _Dm870minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 54),
    _Dm870minValueLaserTemp_Type()
)
dm870minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueLaserTemp.setStatus("mandatory")
_Dm870maxValueLaserTemp_Type = Float
_Dm870maxValueLaserTemp_Object = MibTableColumn
dm870maxValueLaserTemp = _Dm870maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 55),
    _Dm870maxValueLaserTemp_Type()
)
dm870maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueLaserTemp.setStatus("mandatory")


class _Dm870alarmStateLaserTemp_Type(Integer32):
    """Custom type dm870alarmStateLaserTemp based on Integer32"""
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


_Dm870alarmStateLaserTemp_Type.__name__ = "Integer32"
_Dm870alarmStateLaserTemp_Object = MibTableColumn
dm870alarmStateLaserTemp = _Dm870alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 56),
    _Dm870alarmStateLaserTemp_Type()
)
dm870alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateLaserTemp.setStatus("mandatory")


class _Dm870labelLaserCurrent_Type(DisplayString):
    """Custom type dm870labelLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelLaserCurrent_Type.__name__ = "DisplayString"
_Dm870labelLaserCurrent_Object = MibTableColumn
dm870labelLaserCurrent = _Dm870labelLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 57),
    _Dm870labelLaserCurrent_Type()
)
dm870labelLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelLaserCurrent.setStatus("optional")


class _Dm870uomLaserCurrent_Type(DisplayString):
    """Custom type dm870uomLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomLaserCurrent_Type.__name__ = "DisplayString"
_Dm870uomLaserCurrent_Object = MibTableColumn
dm870uomLaserCurrent = _Dm870uomLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 58),
    _Dm870uomLaserCurrent_Type()
)
dm870uomLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomLaserCurrent.setStatus("optional")
_Dm870majorHighLaserCurrent_Type = Float
_Dm870majorHighLaserCurrent_Object = MibTableColumn
dm870majorHighLaserCurrent = _Dm870majorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 59),
    _Dm870majorHighLaserCurrent_Type()
)
dm870majorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighLaserCurrent.setStatus("mandatory")
_Dm870majorLowLaserCurrent_Type = Float
_Dm870majorLowLaserCurrent_Object = MibTableColumn
dm870majorLowLaserCurrent = _Dm870majorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 60),
    _Dm870majorLowLaserCurrent_Type()
)
dm870majorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowLaserCurrent.setStatus("mandatory")
_Dm870minorHighLaserCurrent_Type = Float
_Dm870minorHighLaserCurrent_Object = MibTableColumn
dm870minorHighLaserCurrent = _Dm870minorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 61),
    _Dm870minorHighLaserCurrent_Type()
)
dm870minorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighLaserCurrent.setStatus("obsolete")
_Dm870minorLowLaserCurrent_Type = Float
_Dm870minorLowLaserCurrent_Object = MibTableColumn
dm870minorLowLaserCurrent = _Dm870minorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 62),
    _Dm870minorLowLaserCurrent_Type()
)
dm870minorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowLaserCurrent.setStatus("obsolete")
_Dm870currentValueLaserCurrent_Type = Float
_Dm870currentValueLaserCurrent_Object = MibTableColumn
dm870currentValueLaserCurrent = _Dm870currentValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 63),
    _Dm870currentValueLaserCurrent_Type()
)
dm870currentValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueLaserCurrent.setStatus("mandatory")


class _Dm870stateFlagLaserCurrent_Type(Integer32):
    """Custom type dm870stateFlagLaserCurrent based on Integer32"""
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


_Dm870stateFlagLaserCurrent_Type.__name__ = "Integer32"
_Dm870stateFlagLaserCurrent_Object = MibTableColumn
dm870stateFlagLaserCurrent = _Dm870stateFlagLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 64),
    _Dm870stateFlagLaserCurrent_Type()
)
dm870stateFlagLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagLaserCurrent.setStatus("mandatory")
_Dm870minValueLaserCurrent_Type = Float
_Dm870minValueLaserCurrent_Object = MibTableColumn
dm870minValueLaserCurrent = _Dm870minValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 65),
    _Dm870minValueLaserCurrent_Type()
)
dm870minValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueLaserCurrent.setStatus("mandatory")
_Dm870maxValueLaserCurrent_Type = Float
_Dm870maxValueLaserCurrent_Object = MibTableColumn
dm870maxValueLaserCurrent = _Dm870maxValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 66),
    _Dm870maxValueLaserCurrent_Type()
)
dm870maxValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueLaserCurrent.setStatus("mandatory")


class _Dm870alarmStateLaserCurrent_Type(Integer32):
    """Custom type dm870alarmStateLaserCurrent based on Integer32"""
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


_Dm870alarmStateLaserCurrent_Type.__name__ = "Integer32"
_Dm870alarmStateLaserCurrent_Object = MibTableColumn
dm870alarmStateLaserCurrent = _Dm870alarmStateLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 67),
    _Dm870alarmStateLaserCurrent_Type()
)
dm870alarmStateLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateLaserCurrent.setStatus("mandatory")


class _Dm870labelTecCurrent_Type(DisplayString):
    """Custom type dm870labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelTecCurrent_Type.__name__ = "DisplayString"
_Dm870labelTecCurrent_Object = MibTableColumn
dm870labelTecCurrent = _Dm870labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 68),
    _Dm870labelTecCurrent_Type()
)
dm870labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelTecCurrent.setStatus("optional")


class _Dm870uomTecCurrent_Type(DisplayString):
    """Custom type dm870uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomTecCurrent_Type.__name__ = "DisplayString"
_Dm870uomTecCurrent_Object = MibTableColumn
dm870uomTecCurrent = _Dm870uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 69),
    _Dm870uomTecCurrent_Type()
)
dm870uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomTecCurrent.setStatus("optional")
_Dm870majorHighTecCurrent_Type = Float
_Dm870majorHighTecCurrent_Object = MibTableColumn
dm870majorHighTecCurrent = _Dm870majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 70),
    _Dm870majorHighTecCurrent_Type()
)
dm870majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighTecCurrent.setStatus("mandatory")
_Dm870majorLowTecCurrent_Type = Float
_Dm870majorLowTecCurrent_Object = MibTableColumn
dm870majorLowTecCurrent = _Dm870majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 71),
    _Dm870majorLowTecCurrent_Type()
)
dm870majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowTecCurrent.setStatus("mandatory")
_Dm870minorHighTecCurrent_Type = Float
_Dm870minorHighTecCurrent_Object = MibTableColumn
dm870minorHighTecCurrent = _Dm870minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 72),
    _Dm870minorHighTecCurrent_Type()
)
dm870minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighTecCurrent.setStatus("obsolete")
_Dm870minorLowTecCurrent_Type = Float
_Dm870minorLowTecCurrent_Object = MibTableColumn
dm870minorLowTecCurrent = _Dm870minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 73),
    _Dm870minorLowTecCurrent_Type()
)
dm870minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowTecCurrent.setStatus("obsolete")
_Dm870currentValueTecCurrent_Type = Float
_Dm870currentValueTecCurrent_Object = MibTableColumn
dm870currentValueTecCurrent = _Dm870currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 74),
    _Dm870currentValueTecCurrent_Type()
)
dm870currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueTecCurrent.setStatus("mandatory")


class _Dm870stateFlagTecCurrent_Type(Integer32):
    """Custom type dm870stateFlagTecCurrent based on Integer32"""
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


_Dm870stateFlagTecCurrent_Type.__name__ = "Integer32"
_Dm870stateFlagTecCurrent_Object = MibTableColumn
dm870stateFlagTecCurrent = _Dm870stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 75),
    _Dm870stateFlagTecCurrent_Type()
)
dm870stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagTecCurrent.setStatus("mandatory")
_Dm870minValueTecCurrent_Type = Float
_Dm870minValueTecCurrent_Object = MibTableColumn
dm870minValueTecCurrent = _Dm870minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 76),
    _Dm870minValueTecCurrent_Type()
)
dm870minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueTecCurrent.setStatus("mandatory")
_Dm870maxValueTecCurrent_Type = Float
_Dm870maxValueTecCurrent_Object = MibTableColumn
dm870maxValueTecCurrent = _Dm870maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 77),
    _Dm870maxValueTecCurrent_Type()
)
dm870maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueTecCurrent.setStatus("mandatory")


class _Dm870alarmStateTecCurrent_Type(Integer32):
    """Custom type dm870alarmStateTecCurrent based on Integer32"""
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


_Dm870alarmStateTecCurrent_Type.__name__ = "Integer32"
_Dm870alarmStateTecCurrent_Object = MibTableColumn
dm870alarmStateTecCurrent = _Dm870alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 78),
    _Dm870alarmStateTecCurrent_Type()
)
dm870alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateTecCurrent.setStatus("mandatory")


class _Dm870labelModTemp_Type(DisplayString):
    """Custom type dm870labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelModTemp_Type.__name__ = "DisplayString"
_Dm870labelModTemp_Object = MibTableColumn
dm870labelModTemp = _Dm870labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 79),
    _Dm870labelModTemp_Type()
)
dm870labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelModTemp.setStatus("optional")


class _Dm870uomModTemp_Type(DisplayString):
    """Custom type dm870uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomModTemp_Type.__name__ = "DisplayString"
_Dm870uomModTemp_Object = MibTableColumn
dm870uomModTemp = _Dm870uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 80),
    _Dm870uomModTemp_Type()
)
dm870uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomModTemp.setStatus("optional")
_Dm870majorHighModTemp_Type = Float
_Dm870majorHighModTemp_Object = MibTableColumn
dm870majorHighModTemp = _Dm870majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 81),
    _Dm870majorHighModTemp_Type()
)
dm870majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighModTemp.setStatus("mandatory")
_Dm870majorLowModTemp_Type = Float
_Dm870majorLowModTemp_Object = MibTableColumn
dm870majorLowModTemp = _Dm870majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 82),
    _Dm870majorLowModTemp_Type()
)
dm870majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowModTemp.setStatus("mandatory")
_Dm870minorHighModTemp_Type = Float
_Dm870minorHighModTemp_Object = MibTableColumn
dm870minorHighModTemp = _Dm870minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 83),
    _Dm870minorHighModTemp_Type()
)
dm870minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighModTemp.setStatus("mandatory")
_Dm870minorLowModTemp_Type = Float
_Dm870minorLowModTemp_Object = MibTableColumn
dm870minorLowModTemp = _Dm870minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 84),
    _Dm870minorLowModTemp_Type()
)
dm870minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowModTemp.setStatus("mandatory")
_Dm870currentValueModTemp_Type = Float
_Dm870currentValueModTemp_Object = MibTableColumn
dm870currentValueModTemp = _Dm870currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 85),
    _Dm870currentValueModTemp_Type()
)
dm870currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueModTemp.setStatus("mandatory")


class _Dm870stateFlagModTemp_Type(Integer32):
    """Custom type dm870stateFlagModTemp based on Integer32"""
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


_Dm870stateFlagModTemp_Type.__name__ = "Integer32"
_Dm870stateFlagModTemp_Object = MibTableColumn
dm870stateFlagModTemp = _Dm870stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 86),
    _Dm870stateFlagModTemp_Type()
)
dm870stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagModTemp.setStatus("mandatory")
_Dm870minValueModTemp_Type = Float
_Dm870minValueModTemp_Object = MibTableColumn
dm870minValueModTemp = _Dm870minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 87),
    _Dm870minValueModTemp_Type()
)
dm870minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueModTemp.setStatus("mandatory")
_Dm870maxValueModTemp_Type = Float
_Dm870maxValueModTemp_Object = MibTableColumn
dm870maxValueModTemp = _Dm870maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 88),
    _Dm870maxValueModTemp_Type()
)
dm870maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueModTemp.setStatus("mandatory")


class _Dm870alarmStateModTemp_Type(Integer32):
    """Custom type dm870alarmStateModTemp based on Integer32"""
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


_Dm870alarmStateModTemp_Type.__name__ = "Integer32"
_Dm870alarmStateModTemp_Object = MibTableColumn
dm870alarmStateModTemp = _Dm870alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 89),
    _Dm870alarmStateModTemp_Type()
)
dm870alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateModTemp.setStatus("mandatory")


class _Dm870labelFanCurrent_Type(DisplayString):
    """Custom type dm870labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelFanCurrent_Type.__name__ = "DisplayString"
_Dm870labelFanCurrent_Object = MibTableColumn
dm870labelFanCurrent = _Dm870labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 90),
    _Dm870labelFanCurrent_Type()
)
dm870labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelFanCurrent.setStatus("optional")


class _Dm870uomFanCurrent_Type(DisplayString):
    """Custom type dm870uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870uomFanCurrent_Type.__name__ = "DisplayString"
_Dm870uomFanCurrent_Object = MibTableColumn
dm870uomFanCurrent = _Dm870uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 91),
    _Dm870uomFanCurrent_Type()
)
dm870uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870uomFanCurrent.setStatus("optional")
_Dm870majorHighFanCurrent_Type = Float
_Dm870majorHighFanCurrent_Object = MibTableColumn
dm870majorHighFanCurrent = _Dm870majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 92),
    _Dm870majorHighFanCurrent_Type()
)
dm870majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorHighFanCurrent.setStatus("mandatory")
_Dm870majorLowFanCurrent_Type = Float
_Dm870majorLowFanCurrent_Object = MibTableColumn
dm870majorLowFanCurrent = _Dm870majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 93),
    _Dm870majorLowFanCurrent_Type()
)
dm870majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870majorLowFanCurrent.setStatus("mandatory")
_Dm870minorHighFanCurrent_Type = Float
_Dm870minorHighFanCurrent_Object = MibTableColumn
dm870minorHighFanCurrent = _Dm870minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 94),
    _Dm870minorHighFanCurrent_Type()
)
dm870minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorHighFanCurrent.setStatus("obsolete")
_Dm870minorLowFanCurrent_Type = Float
_Dm870minorLowFanCurrent_Object = MibTableColumn
dm870minorLowFanCurrent = _Dm870minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 95),
    _Dm870minorLowFanCurrent_Type()
)
dm870minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minorLowFanCurrent.setStatus("obsolete")
_Dm870currentValueFanCurrent_Type = Float
_Dm870currentValueFanCurrent_Object = MibTableColumn
dm870currentValueFanCurrent = _Dm870currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 96),
    _Dm870currentValueFanCurrent_Type()
)
dm870currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870currentValueFanCurrent.setStatus("mandatory")


class _Dm870stateFlagFanCurrent_Type(Integer32):
    """Custom type dm870stateFlagFanCurrent based on Integer32"""
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


_Dm870stateFlagFanCurrent_Type.__name__ = "Integer32"
_Dm870stateFlagFanCurrent_Object = MibTableColumn
dm870stateFlagFanCurrent = _Dm870stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 97),
    _Dm870stateFlagFanCurrent_Type()
)
dm870stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateFlagFanCurrent.setStatus("mandatory")
_Dm870minValueFanCurrent_Type = Float
_Dm870minValueFanCurrent_Object = MibTableColumn
dm870minValueFanCurrent = _Dm870minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 98),
    _Dm870minValueFanCurrent_Type()
)
dm870minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870minValueFanCurrent.setStatus("mandatory")
_Dm870maxValueFanCurrent_Type = Float
_Dm870maxValueFanCurrent_Object = MibTableColumn
dm870maxValueFanCurrent = _Dm870maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 99),
    _Dm870maxValueFanCurrent_Type()
)
dm870maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870maxValueFanCurrent.setStatus("mandatory")


class _Dm870alarmStateFanCurrent_Type(Integer32):
    """Custom type dm870alarmStateFanCurrent based on Integer32"""
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


_Dm870alarmStateFanCurrent_Type.__name__ = "Integer32"
_Dm870alarmStateFanCurrent_Object = MibTableColumn
dm870alarmStateFanCurrent = _Dm870alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 2, 1, 100),
    _Dm870alarmStateFanCurrent_Type()
)
dm870alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870alarmStateFanCurrent.setStatus("mandatory")
_Gx2Dm870DigitalTable_Object = MibTable
gx2Dm870DigitalTable = _Gx2Dm870DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3)
)
if mibBuilder.loadTexts:
    gx2Dm870DigitalTable.setStatus("mandatory")
_Gx2Dm870DigitalEntry_Object = MibTableRow
gx2Dm870DigitalEntry = _Gx2Dm870DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2)
)
gx2Dm870DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Dm870-MIB", "gx2Dm870DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm870DigitalEntry.setStatus("mandatory")


class _Gx2Dm870DigitalTableIndex_Type(Integer32):
    """Custom type gx2Dm870DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm870DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Dm870DigitalTableIndex_Object = MibTableColumn
gx2Dm870DigitalTableIndex = _Gx2Dm870DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 1),
    _Gx2Dm870DigitalTableIndex_Type()
)
gx2Dm870DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm870DigitalTableIndex.setStatus("mandatory")


class _Dm870labelRfInput_Type(DisplayString):
    """Custom type dm870labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelRfInput_Type.__name__ = "DisplayString"
_Dm870labelRfInput_Object = MibTableColumn
dm870labelRfInput = _Dm870labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 2),
    _Dm870labelRfInput_Type()
)
dm870labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelRfInput.setStatus("optional")


class _Dm870enumRfInput_Type(DisplayString):
    """Custom type dm870enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870enumRfInput_Type.__name__ = "DisplayString"
_Dm870enumRfInput_Object = MibTableColumn
dm870enumRfInput = _Dm870enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 3),
    _Dm870enumRfInput_Type()
)
dm870enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870enumRfInput.setStatus("optional")


class _Dm870valueRfInput_Type(Integer32):
    """Custom type dm870valueRfInput based on Integer32"""
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


_Dm870valueRfInput_Type.__name__ = "Integer32"
_Dm870valueRfInput_Object = MibTableColumn
dm870valueRfInput = _Dm870valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 4),
    _Dm870valueRfInput_Type()
)
dm870valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870valueRfInput.setStatus("mandatory")


class _Dm870stateflagRfInput_Type(Integer32):
    """Custom type dm870stateflagRfInput based on Integer32"""
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


_Dm870stateflagRfInput_Type.__name__ = "Integer32"
_Dm870stateflagRfInput_Object = MibTableColumn
dm870stateflagRfInput = _Dm870stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 5),
    _Dm870stateflagRfInput_Type()
)
dm870stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagRfInput.setStatus("mandatory")


class _Dm870labelOptOutput_Type(DisplayString):
    """Custom type dm870labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelOptOutput_Type.__name__ = "DisplayString"
_Dm870labelOptOutput_Object = MibTableColumn
dm870labelOptOutput = _Dm870labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 6),
    _Dm870labelOptOutput_Type()
)
dm870labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelOptOutput.setStatus("optional")


class _Dm870enumOptOutput_Type(DisplayString):
    """Custom type dm870enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870enumOptOutput_Type.__name__ = "DisplayString"
_Dm870enumOptOutput_Object = MibTableColumn
dm870enumOptOutput = _Dm870enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 7),
    _Dm870enumOptOutput_Type()
)
dm870enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870enumOptOutput.setStatus("optional")


class _Dm870valueOptOutput_Type(Integer32):
    """Custom type dm870valueOptOutput based on Integer32"""
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


_Dm870valueOptOutput_Type.__name__ = "Integer32"
_Dm870valueOptOutput_Object = MibTableColumn
dm870valueOptOutput = _Dm870valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 8),
    _Dm870valueOptOutput_Type()
)
dm870valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870valueOptOutput.setStatus("mandatory")


class _Dm870stateflagOptOutput_Type(Integer32):
    """Custom type dm870stateflagOptOutput based on Integer32"""
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


_Dm870stateflagOptOutput_Type.__name__ = "Integer32"
_Dm870stateflagOptOutput_Object = MibTableColumn
dm870stateflagOptOutput = _Dm870stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 9),
    _Dm870stateflagOptOutput_Type()
)
dm870stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagOptOutput.setStatus("mandatory")


class _Dm870labelSbsControl_Type(DisplayString):
    """Custom type dm870labelSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelSbsControl_Type.__name__ = "DisplayString"
_Dm870labelSbsControl_Object = MibTableColumn
dm870labelSbsControl = _Dm870labelSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 10),
    _Dm870labelSbsControl_Type()
)
dm870labelSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelSbsControl.setStatus("optional")


class _Dm870enumSbsControl_Type(DisplayString):
    """Custom type dm870enumSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870enumSbsControl_Type.__name__ = "DisplayString"
_Dm870enumSbsControl_Object = MibTableColumn
dm870enumSbsControl = _Dm870enumSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 11),
    _Dm870enumSbsControl_Type()
)
dm870enumSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870enumSbsControl.setStatus("optional")


class _Dm870valueSbsControl_Type(Integer32):
    """Custom type dm870valueSbsControl based on Integer32"""
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


_Dm870valueSbsControl_Type.__name__ = "Integer32"
_Dm870valueSbsControl_Object = MibTableColumn
dm870valueSbsControl = _Dm870valueSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 12),
    _Dm870valueSbsControl_Type()
)
dm870valueSbsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870valueSbsControl.setStatus("mandatory")


class _Dm870stateflagSbsControl_Type(Integer32):
    """Custom type dm870stateflagSbsControl based on Integer32"""
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


_Dm870stateflagSbsControl_Type.__name__ = "Integer32"
_Dm870stateflagSbsControl_Object = MibTableColumn
dm870stateflagSbsControl = _Dm870stateflagSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 13),
    _Dm870stateflagSbsControl_Type()
)
dm870stateflagSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagSbsControl.setStatus("mandatory")


class _Dm870labelLaserMode_Type(DisplayString):
    """Custom type dm870labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelLaserMode_Type.__name__ = "DisplayString"
_Dm870labelLaserMode_Object = MibTableColumn
dm870labelLaserMode = _Dm870labelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 14),
    _Dm870labelLaserMode_Type()
)
dm870labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelLaserMode.setStatus("optional")


class _Dm870enumLaserMode_Type(DisplayString):
    """Custom type dm870enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870enumLaserMode_Type.__name__ = "DisplayString"
_Dm870enumLaserMode_Object = MibTableColumn
dm870enumLaserMode = _Dm870enumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 15),
    _Dm870enumLaserMode_Type()
)
dm870enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870enumLaserMode.setStatus("optional")


class _Dm870valueLaserMode_Type(Integer32):
    """Custom type dm870valueLaserMode based on Integer32"""
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
        *(("manual", 4),
          ("manualEquate", 5),
          ("preset", 1),
          ("set", 2),
          ("setEquate", 3))
    )


_Dm870valueLaserMode_Type.__name__ = "Integer32"
_Dm870valueLaserMode_Object = MibTableColumn
dm870valueLaserMode = _Dm870valueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 16),
    _Dm870valueLaserMode_Type()
)
dm870valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870valueLaserMode.setStatus("mandatory")


class _Dm870stateflagLaserMode_Type(Integer32):
    """Custom type dm870stateflagLaserMode based on Integer32"""
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


_Dm870stateflagLaserMode_Type.__name__ = "Integer32"
_Dm870stateflagLaserMode_Object = MibTableColumn
dm870stateflagLaserMode = _Dm870stateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 17),
    _Dm870stateflagLaserMode_Type()
)
dm870stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagLaserMode.setStatus("mandatory")


class _Dm870labelFactoryDefault_Type(DisplayString):
    """Custom type dm870labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelFactoryDefault_Type.__name__ = "DisplayString"
_Dm870labelFactoryDefault_Object = MibTableColumn
dm870labelFactoryDefault = _Dm870labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 18),
    _Dm870labelFactoryDefault_Type()
)
dm870labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelFactoryDefault.setStatus("optional")


class _Dm870enumFactoryDefault_Type(DisplayString):
    """Custom type dm870enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870enumFactoryDefault_Type.__name__ = "DisplayString"
_Dm870enumFactoryDefault_Object = MibTableColumn
dm870enumFactoryDefault = _Dm870enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 19),
    _Dm870enumFactoryDefault_Type()
)
dm870enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870enumFactoryDefault.setStatus("optional")


class _Dm870valueFactoryDefault_Type(Integer32):
    """Custom type dm870valueFactoryDefault based on Integer32"""
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


_Dm870valueFactoryDefault_Type.__name__ = "Integer32"
_Dm870valueFactoryDefault_Object = MibTableColumn
dm870valueFactoryDefault = _Dm870valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 20),
    _Dm870valueFactoryDefault_Type()
)
dm870valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm870valueFactoryDefault.setStatus("mandatory")


class _Dm870stateflagFactoryDefault_Type(Integer32):
    """Custom type dm870stateflagFactoryDefault based on Integer32"""
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


_Dm870stateflagFactoryDefault_Type.__name__ = "Integer32"
_Dm870stateflagFactoryDefault_Object = MibTableColumn
dm870stateflagFactoryDefault = _Dm870stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 3, 2, 21),
    _Dm870stateflagFactoryDefault_Type()
)
dm870stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagFactoryDefault.setStatus("mandatory")
_Gx2Dm870StatusTable_Object = MibTable
gx2Dm870StatusTable = _Gx2Dm870StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    gx2Dm870StatusTable.setStatus("mandatory")
_Gx2Dm870StatusEntry_Object = MibTableRow
gx2Dm870StatusEntry = _Gx2Dm870StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3)
)
gx2Dm870StatusEntry.setIndexNames(
    (0, "OMNI-gx2Dm870-MIB", "gx2Dm870StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm870StatusEntry.setStatus("mandatory")


class _Gx2Dm870StatusTableIndex_Type(Integer32):
    """Custom type gx2Dm870StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm870StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Dm870StatusTableIndex_Object = MibTableColumn
gx2Dm870StatusTableIndex = _Gx2Dm870StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 1),
    _Gx2Dm870StatusTableIndex_Type()
)
gx2Dm870StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm870StatusTableIndex.setStatus("mandatory")


class _Dm870labelBoot_Type(DisplayString):
    """Custom type dm870labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelBoot_Type.__name__ = "DisplayString"
_Dm870labelBoot_Object = MibTableColumn
dm870labelBoot = _Dm870labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 2),
    _Dm870labelBoot_Type()
)
dm870labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelBoot.setStatus("optional")


class _Dm870valueBoot_Type(Integer32):
    """Custom type dm870valueBoot based on Integer32"""
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


_Dm870valueBoot_Type.__name__ = "Integer32"
_Dm870valueBoot_Object = MibTableColumn
dm870valueBoot = _Dm870valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 3),
    _Dm870valueBoot_Type()
)
dm870valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueBoot.setStatus("mandatory")


class _Dm870stateflagBoot_Type(Integer32):
    """Custom type dm870stateflagBoot based on Integer32"""
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


_Dm870stateflagBoot_Type.__name__ = "Integer32"
_Dm870stateflagBoot_Object = MibTableColumn
dm870stateflagBoot = _Dm870stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 4),
    _Dm870stateflagBoot_Type()
)
dm870stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagBoot.setStatus("mandatory")


class _Dm870labelFlash_Type(DisplayString):
    """Custom type dm870labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelFlash_Type.__name__ = "DisplayString"
_Dm870labelFlash_Object = MibTableColumn
dm870labelFlash = _Dm870labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 5),
    _Dm870labelFlash_Type()
)
dm870labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelFlash.setStatus("optional")


class _Dm870valueFlash_Type(Integer32):
    """Custom type dm870valueFlash based on Integer32"""
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


_Dm870valueFlash_Type.__name__ = "Integer32"
_Dm870valueFlash_Object = MibTableColumn
dm870valueFlash = _Dm870valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 6),
    _Dm870valueFlash_Type()
)
dm870valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueFlash.setStatus("mandatory")


class _Dm870stateflagFlash_Type(Integer32):
    """Custom type dm870stateflagFlash based on Integer32"""
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


_Dm870stateflagFlash_Type.__name__ = "Integer32"
_Dm870stateflagFlash_Object = MibTableColumn
dm870stateflagFlash = _Dm870stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 7),
    _Dm870stateflagFlash_Type()
)
dm870stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagFlash.setStatus("mandatory")


class _Dm870labelFactoryDataCRC_Type(DisplayString):
    """Custom type dm870labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Dm870labelFactoryDataCRC_Object = MibTableColumn
dm870labelFactoryDataCRC = _Dm870labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 8),
    _Dm870labelFactoryDataCRC_Type()
)
dm870labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelFactoryDataCRC.setStatus("optional")


class _Dm870valueFactoryDataCRC_Type(Integer32):
    """Custom type dm870valueFactoryDataCRC based on Integer32"""
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


_Dm870valueFactoryDataCRC_Type.__name__ = "Integer32"
_Dm870valueFactoryDataCRC_Object = MibTableColumn
dm870valueFactoryDataCRC = _Dm870valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 9),
    _Dm870valueFactoryDataCRC_Type()
)
dm870valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueFactoryDataCRC.setStatus("mandatory")


class _Dm870stateflagFactoryDataCRC_Type(Integer32):
    """Custom type dm870stateflagFactoryDataCRC based on Integer32"""
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


_Dm870stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Dm870stateflagFactoryDataCRC_Object = MibTableColumn
dm870stateflagFactoryDataCRC = _Dm870stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 10),
    _Dm870stateflagFactoryDataCRC_Type()
)
dm870stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagFactoryDataCRC.setStatus("mandatory")


class _Dm870labelLaserDataCRC_Type(DisplayString):
    """Custom type dm870labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelLaserDataCRC_Type.__name__ = "DisplayString"
_Dm870labelLaserDataCRC_Object = MibTableColumn
dm870labelLaserDataCRC = _Dm870labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 11),
    _Dm870labelLaserDataCRC_Type()
)
dm870labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelLaserDataCRC.setStatus("optional")


class _Dm870valueLaserDataCRC_Type(Integer32):
    """Custom type dm870valueLaserDataCRC based on Integer32"""
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


_Dm870valueLaserDataCRC_Type.__name__ = "Integer32"
_Dm870valueLaserDataCRC_Object = MibTableColumn
dm870valueLaserDataCRC = _Dm870valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 12),
    _Dm870valueLaserDataCRC_Type()
)
dm870valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueLaserDataCRC.setStatus("mandatory")


class _Dm870stateflagLaserDataCRC_Type(Integer32):
    """Custom type dm870stateflagLaserDataCRC based on Integer32"""
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


_Dm870stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Dm870stateflagLaserDataCRC_Object = MibTableColumn
dm870stateflagLaserDataCRC = _Dm870stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 13),
    _Dm870stateflagLaserDataCRC_Type()
)
dm870stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagLaserDataCRC.setStatus("mandatory")


class _Dm870labelAlarmDataCrc_Type(DisplayString):
    """Custom type dm870labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Dm870labelAlarmDataCrc_Object = MibTableColumn
dm870labelAlarmDataCrc = _Dm870labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 14),
    _Dm870labelAlarmDataCrc_Type()
)
dm870labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelAlarmDataCrc.setStatus("optional")


class _Dm870valueAlarmDataCrc_Type(Integer32):
    """Custom type dm870valueAlarmDataCrc based on Integer32"""
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


_Dm870valueAlarmDataCrc_Type.__name__ = "Integer32"
_Dm870valueAlarmDataCrc_Object = MibTableColumn
dm870valueAlarmDataCrc = _Dm870valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 15),
    _Dm870valueAlarmDataCrc_Type()
)
dm870valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueAlarmDataCrc.setStatus("mandatory")


class _Dm870stateflagAlarmDataCrc_Type(Integer32):
    """Custom type dm870stateflagAlarmDataCrc based on Integer32"""
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


_Dm870stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Dm870stateflagAlarmDataCrc_Object = MibTableColumn
dm870stateflagAlarmDataCrc = _Dm870stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 16),
    _Dm870stateflagAlarmDataCrc_Type()
)
dm870stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagAlarmDataCrc.setStatus("mandatory")


class _Dm870labelRFInputStatus_Type(DisplayString):
    """Custom type dm870labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870labelRFInputStatus_Type.__name__ = "DisplayString"
_Dm870labelRFInputStatus_Object = MibTableColumn
dm870labelRFInputStatus = _Dm870labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 17),
    _Dm870labelRFInputStatus_Type()
)
dm870labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870labelRFInputStatus.setStatus("optional")


class _Dm870valueRFInputStatus_Type(Integer32):
    """Custom type dm870valueRFInputStatus based on Integer32"""
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


_Dm870valueRFInputStatus_Type.__name__ = "Integer32"
_Dm870valueRFInputStatus_Object = MibTableColumn
dm870valueRFInputStatus = _Dm870valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 18),
    _Dm870valueRFInputStatus_Type()
)
dm870valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870valueRFInputStatus.setStatus("mandatory")


class _Dm870stateflagRFInputStatus_Type(Integer32):
    """Custom type dm870stateflagRFInputStatus based on Integer32"""
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


_Dm870stateflagRFInputStatus_Type.__name__ = "Integer32"
_Dm870stateflagRFInputStatus_Object = MibTableColumn
dm870stateflagRFInputStatus = _Dm870stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 4, 3, 19),
    _Dm870stateflagRFInputStatus_Type()
)
dm870stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870stateflagRFInputStatus.setStatus("mandatory")
_Gx2Dm870FactoryTable_Object = MibTable
gx2Dm870FactoryTable = _Gx2Dm870FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gx2Dm870FactoryTable.setStatus("mandatory")
_Gx2Dm870FactoryEntry_Object = MibTableRow
gx2Dm870FactoryEntry = _Gx2Dm870FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4)
)
gx2Dm870FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Dm870-MIB", "gx2Dm870FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm870FactoryEntry.setStatus("mandatory")


class _Gx2Dm870FactoryTableIndex_Type(Integer32):
    """Custom type gx2Dm870FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm870FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Dm870FactoryTableIndex_Object = MibTableColumn
gx2Dm870FactoryTableIndex = _Gx2Dm870FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 1),
    _Gx2Dm870FactoryTableIndex_Type()
)
gx2Dm870FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm870FactoryTableIndex.setStatus("mandatory")
_Dm870bootControlByte_Type = Integer32
_Dm870bootControlByte_Object = MibTableColumn
dm870bootControlByte = _Dm870bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 2),
    _Dm870bootControlByte_Type()
)
dm870bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870bootControlByte.setStatus("mandatory")
_Dm870bootStatusByte_Type = Integer32
_Dm870bootStatusByte_Object = MibTableColumn
dm870bootStatusByte = _Dm870bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 3),
    _Dm870bootStatusByte_Type()
)
dm870bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870bootStatusByte.setStatus("mandatory")
_Dm870bank1CRC_Type = Integer32
_Dm870bank1CRC_Object = MibTableColumn
dm870bank1CRC = _Dm870bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 4),
    _Dm870bank1CRC_Type()
)
dm870bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870bank1CRC.setStatus("mandatory")
_Dm870bank2CRC_Type = Integer32
_Dm870bank2CRC_Object = MibTableColumn
dm870bank2CRC = _Dm870bank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 5),
    _Dm870bank2CRC_Type()
)
dm870bank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870bank2CRC.setStatus("mandatory")
_Dm870prgEEPROMByte_Type = Integer32
_Dm870prgEEPROMByte_Object = MibTableColumn
dm870prgEEPROMByte = _Dm870prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 6),
    _Dm870prgEEPROMByte_Type()
)
dm870prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870prgEEPROMByte.setStatus("mandatory")
_Dm870factoryCRC_Type = Integer32
_Dm870factoryCRC_Object = MibTableColumn
dm870factoryCRC = _Dm870factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 7),
    _Dm870factoryCRC_Type()
)
dm870factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870factoryCRC.setStatus("mandatory")


class _Dm870calculateCRC_Type(Integer32):
    """Custom type dm870calculateCRC based on Integer32"""
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


_Dm870calculateCRC_Type.__name__ = "Integer32"
_Dm870calculateCRC_Object = MibTableColumn
dm870calculateCRC = _Dm870calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 8),
    _Dm870calculateCRC_Type()
)
dm870calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870calculateCRC.setStatus("obsolete")
_Dm870hourMeter_Type = Integer32
_Dm870hourMeter_Object = MibTableColumn
dm870hourMeter = _Dm870hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 9),
    _Dm870hourMeter_Type()
)
dm870hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870hourMeter.setStatus("mandatory")
_Dm870flashPrgCntA_Type = Integer32
_Dm870flashPrgCntA_Object = MibTableColumn
dm870flashPrgCntA = _Dm870flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 10),
    _Dm870flashPrgCntA_Type()
)
dm870flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870flashPrgCntA.setStatus("mandatory")
_Dm870flashPrgCntB_Type = Integer32
_Dm870flashPrgCntB_Object = MibTableColumn
dm870flashPrgCntB = _Dm870flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 11),
    _Dm870flashPrgCntB_Type()
)
dm870flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870flashPrgCntB.setStatus("mandatory")


class _Dm870flashBankARev_Type(DisplayString):
    """Custom type dm870flashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870flashBankARev_Type.__name__ = "DisplayString"
_Dm870flashBankARev_Object = MibTableColumn
dm870flashBankARev = _Dm870flashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 12),
    _Dm870flashBankARev_Type()
)
dm870flashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870flashBankARev.setStatus("mandatory")


class _Dm870flashBankBRev_Type(DisplayString):
    """Custom type dm870flashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm870flashBankBRev_Type.__name__ = "DisplayString"
_Dm870flashBankBRev_Object = MibTableColumn
dm870flashBankBRev = _Dm870flashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 5, 4, 13),
    _Dm870flashBankBRev_Type()
)
dm870flashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm870flashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDM870ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 1)
)
trapDM870ConfigChangeInteger.setObjects(
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
    trapDM870ConfigChangeInteger.setStatus(
        ""
    )

trapDM870ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 2)
)
trapDM870ConfigChangeDisplayString.setObjects(
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
    trapDM870ConfigChangeDisplayString.setStatus(
        ""
    )

trapDM870fanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 3)
)
trapDM870fanCurrentAlarm.setObjects(
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
    trapDM870fanCurrentAlarm.setStatus(
        ""
    )

trapDM870ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 4)
)
trapDM870ModuleTempAlarm.setObjects(
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
    trapDM870ModuleTempAlarm.setStatus(
        ""
    )

trapDM870omiOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 5)
)
trapDM870omiOffsetAlarm.setObjects(
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
    trapDM870omiOffsetAlarm.setStatus(
        ""
    )

trapDM870tecCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 6)
)
trapDM870tecCurrentAlarm.setObjects(
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
    trapDM870tecCurrentAlarm.setStatus(
        ""
    )

trapDM870LaserCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 7)
)
trapDM870LaserCurrentAlarm.setObjects(
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
    trapDM870LaserCurrentAlarm.setStatus(
        ""
    )

trapDM870LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 8)
)
trapDM870LaserTempAlarm.setObjects(
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
    trapDM870LaserTempAlarm.setStatus(
        ""
    )

trapDM870LaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 9)
)
trapDM870LaserPowerAlarm.setObjects(
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
    trapDM870LaserPowerAlarm.setStatus(
        ""
    )

trapDM870FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 10)
)
trapDM870FlashAlarm.setObjects(
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
    trapDM870FlashAlarm.setStatus(
        ""
    )

trapDM870BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 11)
)
trapDM870BankBootAlarm.setObjects(
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
    trapDM870BankBootAlarm.setStatus(
        ""
    )

trapDM870AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 12)
)
trapDM870AlarmDataCRCAlarm.setObjects(
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
    trapDM870AlarmDataCRCAlarm.setStatus(
        ""
    )

trapDM870FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 13)
)
trapDM870FactoryDataCRCAlarm.setObjects(
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
    trapDM870FactoryDataCRCAlarm.setStatus(
        ""
    )

trapDM870CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 14)
)
trapDM870CalDataCRCAlarm.setObjects(
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
    trapDM870CalDataCRCAlarm.setStatus(
        ""
    )

trapDM870ResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 15)
)
trapDM870ResetFacDefault.setObjects(
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
    trapDM870ResetFacDefault.setStatus(
        ""
    )

trapDM870UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 16)
)
trapDM870UserRFOffAlarm.setObjects(
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
    trapDM870UserRFOffAlarm.setStatus(
        ""
    )

trapDM870UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 17)
)
trapDM870UserOpticalOffAlarm.setObjects(
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
    trapDM870UserOpticalOffAlarm.setStatus(
        ""
    )

trapDM870UserSBSOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 18)
)
trapDM870UserSBSOffAlarm.setObjects(
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
    trapDM870UserSBSOffAlarm.setStatus(
        ""
    )

trapDM870RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 19)
)
trapDM870RFInputAlarm.setObjects(
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
    trapDM870RFInputAlarm.setStatus(
        ""
    )

trapDM870RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16, 0, 20)
)
trapDM870RFOverloadAlarm.setObjects(
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
    trapDM870RFOverloadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Dm870-MIB",
    **{"Float": Float,
       "trapDM870ConfigChangeInteger": trapDM870ConfigChangeInteger,
       "trapDM870ConfigChangeDisplayString": trapDM870ConfigChangeDisplayString,
       "trapDM870fanCurrentAlarm": trapDM870fanCurrentAlarm,
       "trapDM870ModuleTempAlarm": trapDM870ModuleTempAlarm,
       "trapDM870omiOffsetAlarm": trapDM870omiOffsetAlarm,
       "trapDM870tecCurrentAlarm": trapDM870tecCurrentAlarm,
       "trapDM870LaserCurrentAlarm": trapDM870LaserCurrentAlarm,
       "trapDM870LaserTempAlarm": trapDM870LaserTempAlarm,
       "trapDM870LaserPowerAlarm": trapDM870LaserPowerAlarm,
       "trapDM870FlashAlarm": trapDM870FlashAlarm,
       "trapDM870BankBootAlarm": trapDM870BankBootAlarm,
       "trapDM870AlarmDataCRCAlarm": trapDM870AlarmDataCRCAlarm,
       "trapDM870FactoryDataCRCAlarm": trapDM870FactoryDataCRCAlarm,
       "trapDM870CalDataCRCAlarm": trapDM870CalDataCRCAlarm,
       "trapDM870ResetFacDefault": trapDM870ResetFacDefault,
       "trapDM870UserRFOffAlarm": trapDM870UserRFOffAlarm,
       "trapDM870UserOpticalOffAlarm": trapDM870UserOpticalOffAlarm,
       "trapDM870UserSBSOffAlarm": trapDM870UserSBSOffAlarm,
       "trapDM870RFInputAlarm": trapDM870RFInputAlarm,
       "trapDM870RFOverloadAlarm": trapDM870RFOverloadAlarm,
       "gx2Dm870Descriptor": gx2Dm870Descriptor,
       "gx2Dm870AnalogTable": gx2Dm870AnalogTable,
       "gx2Dm870AnalogEntry": gx2Dm870AnalogEntry,
       "gx2Dm870AnalogTableIndex": gx2Dm870AnalogTableIndex,
       "dm870labelOffsetNomMonitor": dm870labelOffsetNomMonitor,
       "dm870uomOffsetNomMonitor": dm870uomOffsetNomMonitor,
       "dm870majorHighOffsetNomMonitor": dm870majorHighOffsetNomMonitor,
       "dm870majorLowOffsetNomMonitor": dm870majorLowOffsetNomMonitor,
       "dm870minorHighOffsetNomMonitor": dm870minorHighOffsetNomMonitor,
       "dm870minorLowOffsetNomMonitor": dm870minorLowOffsetNomMonitor,
       "dm870currentValueOffsetNomMonitor": dm870currentValueOffsetNomMonitor,
       "dm870stateFlagOffsetNomMonitor": dm870stateFlagOffsetNomMonitor,
       "dm870minValueOffsetNomMonitor": dm870minValueOffsetNomMonitor,
       "dm870maxValueOffsetNomMonitor": dm870maxValueOffsetNomMonitor,
       "dm870alarmStateOffsetNomMonitor": dm870alarmStateOffsetNomMonitor,
       "dm870labelOffsetNomCnt": dm870labelOffsetNomCnt,
       "dm870uomOffsetNomCnt": dm870uomOffsetNomCnt,
       "dm870majorHighOffsetNomCnt": dm870majorHighOffsetNomCnt,
       "dm870majorLowOffsetNomCnt": dm870majorLowOffsetNomCnt,
       "dm870minorHighOffsetNomCnt": dm870minorHighOffsetNomCnt,
       "dm870minorLowOffsetNomCnt": dm870minorLowOffsetNomCnt,
       "dm870currentValueOffsetNomCnt": dm870currentValueOffsetNomCnt,
       "dm870stateFlagOffsetNomCnt": dm870stateFlagOffsetNomCnt,
       "dm870minValueOffsetNomCnt": dm870minValueOffsetNomCnt,
       "dm870maxValueOffsetNomCnt": dm870maxValueOffsetNomCnt,
       "dm870alarmStateOffsetNomCnt": dm870alarmStateOffsetNomCnt,
       "dm870labelAttenSetting": dm870labelAttenSetting,
       "dm870uomAttenSetting": dm870uomAttenSetting,
       "dm870majorHighAttenSetting": dm870majorHighAttenSetting,
       "dm870majorLowAttenSetting": dm870majorLowAttenSetting,
       "dm870minorHighAttenSetting": dm870minorHighAttenSetting,
       "dm870minorLowAttenSetting": dm870minorLowAttenSetting,
       "dm870currentValueAttenSetting": dm870currentValueAttenSetting,
       "dm870stateFlagAttenSetting": dm870stateFlagAttenSetting,
       "dm870minValueAttenSetting": dm870minValueAttenSetting,
       "dm870maxValueAttenSetting": dm870maxValueAttenSetting,
       "dm870alarmStateAttenSetting": dm870alarmStateAttenSetting,
       "dm870labelLaserPower": dm870labelLaserPower,
       "dm870uomLaserPower": dm870uomLaserPower,
       "dm870majorHighLaserPower": dm870majorHighLaserPower,
       "dm870majorLowLaserPower": dm870majorLowLaserPower,
       "dm870minorHighLaserPower": dm870minorHighLaserPower,
       "dm870minorLowLaserPower": dm870minorLowLaserPower,
       "dm870currentValueLaserPower": dm870currentValueLaserPower,
       "dm870stateFlagLaserPower": dm870stateFlagLaserPower,
       "dm870minValueLaserPower": dm870minValueLaserPower,
       "dm870maxValueLaserPower": dm870maxValueLaserPower,
       "dm870alarmStateLaserPower": dm870alarmStateLaserPower,
       "dm870labelLaserTemp": dm870labelLaserTemp,
       "dm870uomLaserTemp": dm870uomLaserTemp,
       "dm870majorHighLaserTemp": dm870majorHighLaserTemp,
       "dm870majorLowLaserTemp": dm870majorLowLaserTemp,
       "dm870minorHighLaserTemp": dm870minorHighLaserTemp,
       "dm870minorLowLaserTemp": dm870minorLowLaserTemp,
       "dm870currentValueLaserTemp": dm870currentValueLaserTemp,
       "dm870stateFlagLaserTemp": dm870stateFlagLaserTemp,
       "dm870minValueLaserTemp": dm870minValueLaserTemp,
       "dm870maxValueLaserTemp": dm870maxValueLaserTemp,
       "dm870alarmStateLaserTemp": dm870alarmStateLaserTemp,
       "dm870labelLaserCurrent": dm870labelLaserCurrent,
       "dm870uomLaserCurrent": dm870uomLaserCurrent,
       "dm870majorHighLaserCurrent": dm870majorHighLaserCurrent,
       "dm870majorLowLaserCurrent": dm870majorLowLaserCurrent,
       "dm870minorHighLaserCurrent": dm870minorHighLaserCurrent,
       "dm870minorLowLaserCurrent": dm870minorLowLaserCurrent,
       "dm870currentValueLaserCurrent": dm870currentValueLaserCurrent,
       "dm870stateFlagLaserCurrent": dm870stateFlagLaserCurrent,
       "dm870minValueLaserCurrent": dm870minValueLaserCurrent,
       "dm870maxValueLaserCurrent": dm870maxValueLaserCurrent,
       "dm870alarmStateLaserCurrent": dm870alarmStateLaserCurrent,
       "dm870labelTecCurrent": dm870labelTecCurrent,
       "dm870uomTecCurrent": dm870uomTecCurrent,
       "dm870majorHighTecCurrent": dm870majorHighTecCurrent,
       "dm870majorLowTecCurrent": dm870majorLowTecCurrent,
       "dm870minorHighTecCurrent": dm870minorHighTecCurrent,
       "dm870minorLowTecCurrent": dm870minorLowTecCurrent,
       "dm870currentValueTecCurrent": dm870currentValueTecCurrent,
       "dm870stateFlagTecCurrent": dm870stateFlagTecCurrent,
       "dm870minValueTecCurrent": dm870minValueTecCurrent,
       "dm870maxValueTecCurrent": dm870maxValueTecCurrent,
       "dm870alarmStateTecCurrent": dm870alarmStateTecCurrent,
       "dm870labelModTemp": dm870labelModTemp,
       "dm870uomModTemp": dm870uomModTemp,
       "dm870majorHighModTemp": dm870majorHighModTemp,
       "dm870majorLowModTemp": dm870majorLowModTemp,
       "dm870minorHighModTemp": dm870minorHighModTemp,
       "dm870minorLowModTemp": dm870minorLowModTemp,
       "dm870currentValueModTemp": dm870currentValueModTemp,
       "dm870stateFlagModTemp": dm870stateFlagModTemp,
       "dm870minValueModTemp": dm870minValueModTemp,
       "dm870maxValueModTemp": dm870maxValueModTemp,
       "dm870alarmStateModTemp": dm870alarmStateModTemp,
       "dm870labelFanCurrent": dm870labelFanCurrent,
       "dm870uomFanCurrent": dm870uomFanCurrent,
       "dm870majorHighFanCurrent": dm870majorHighFanCurrent,
       "dm870majorLowFanCurrent": dm870majorLowFanCurrent,
       "dm870minorHighFanCurrent": dm870minorHighFanCurrent,
       "dm870minorLowFanCurrent": dm870minorLowFanCurrent,
       "dm870currentValueFanCurrent": dm870currentValueFanCurrent,
       "dm870stateFlagFanCurrent": dm870stateFlagFanCurrent,
       "dm870minValueFanCurrent": dm870minValueFanCurrent,
       "dm870maxValueFanCurrent": dm870maxValueFanCurrent,
       "dm870alarmStateFanCurrent": dm870alarmStateFanCurrent,
       "gx2Dm870DigitalTable": gx2Dm870DigitalTable,
       "gx2Dm870DigitalEntry": gx2Dm870DigitalEntry,
       "gx2Dm870DigitalTableIndex": gx2Dm870DigitalTableIndex,
       "dm870labelRfInput": dm870labelRfInput,
       "dm870enumRfInput": dm870enumRfInput,
       "dm870valueRfInput": dm870valueRfInput,
       "dm870stateflagRfInput": dm870stateflagRfInput,
       "dm870labelOptOutput": dm870labelOptOutput,
       "dm870enumOptOutput": dm870enumOptOutput,
       "dm870valueOptOutput": dm870valueOptOutput,
       "dm870stateflagOptOutput": dm870stateflagOptOutput,
       "dm870labelSbsControl": dm870labelSbsControl,
       "dm870enumSbsControl": dm870enumSbsControl,
       "dm870valueSbsControl": dm870valueSbsControl,
       "dm870stateflagSbsControl": dm870stateflagSbsControl,
       "dm870labelLaserMode": dm870labelLaserMode,
       "dm870enumLaserMode": dm870enumLaserMode,
       "dm870valueLaserMode": dm870valueLaserMode,
       "dm870stateflagLaserMode": dm870stateflagLaserMode,
       "dm870labelFactoryDefault": dm870labelFactoryDefault,
       "dm870enumFactoryDefault": dm870enumFactoryDefault,
       "dm870valueFactoryDefault": dm870valueFactoryDefault,
       "dm870stateflagFactoryDefault": dm870stateflagFactoryDefault,
       "gx2Dm870StatusTable": gx2Dm870StatusTable,
       "gx2Dm870StatusEntry": gx2Dm870StatusEntry,
       "gx2Dm870StatusTableIndex": gx2Dm870StatusTableIndex,
       "dm870labelBoot": dm870labelBoot,
       "dm870valueBoot": dm870valueBoot,
       "dm870stateflagBoot": dm870stateflagBoot,
       "dm870labelFlash": dm870labelFlash,
       "dm870valueFlash": dm870valueFlash,
       "dm870stateflagFlash": dm870stateflagFlash,
       "dm870labelFactoryDataCRC": dm870labelFactoryDataCRC,
       "dm870valueFactoryDataCRC": dm870valueFactoryDataCRC,
       "dm870stateflagFactoryDataCRC": dm870stateflagFactoryDataCRC,
       "dm870labelLaserDataCRC": dm870labelLaserDataCRC,
       "dm870valueLaserDataCRC": dm870valueLaserDataCRC,
       "dm870stateflagLaserDataCRC": dm870stateflagLaserDataCRC,
       "dm870labelAlarmDataCrc": dm870labelAlarmDataCrc,
       "dm870valueAlarmDataCrc": dm870valueAlarmDataCrc,
       "dm870stateflagAlarmDataCrc": dm870stateflagAlarmDataCrc,
       "dm870labelRFInputStatus": dm870labelRFInputStatus,
       "dm870valueRFInputStatus": dm870valueRFInputStatus,
       "dm870stateflagRFInputStatus": dm870stateflagRFInputStatus,
       "gx2Dm870FactoryTable": gx2Dm870FactoryTable,
       "gx2Dm870FactoryEntry": gx2Dm870FactoryEntry,
       "gx2Dm870FactoryTableIndex": gx2Dm870FactoryTableIndex,
       "dm870bootControlByte": dm870bootControlByte,
       "dm870bootStatusByte": dm870bootStatusByte,
       "dm870bank1CRC": dm870bank1CRC,
       "dm870bank2CRC": dm870bank2CRC,
       "dm870prgEEPROMByte": dm870prgEEPROMByte,
       "dm870factoryCRC": dm870factoryCRC,
       "dm870calculateCRC": dm870calculateCRC,
       "dm870hourMeter": dm870hourMeter,
       "dm870flashPrgCntA": dm870flashPrgCntA,
       "dm870flashPrgCntB": dm870flashPrgCntB,
       "dm870flashBankARev": dm870flashBankARev,
       "dm870flashBankBRev": dm870flashBankBRev}
)
