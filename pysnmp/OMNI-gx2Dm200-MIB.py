# SNMP MIB module (OMNI-gx2Dm200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Dm200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:16 2024
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

(gx2Dm200,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Dm200")

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

_Gx2Dm200Descriptor_ObjectIdentity = ObjectIdentity
gx2Dm200Descriptor = _Gx2Dm200Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 1)
)
_Gx2Dm200AnalogTable_Object = MibTable
gx2Dm200AnalogTable = _Gx2Dm200AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gx2Dm200AnalogTable.setStatus("mandatory")
_Gx2Dm200AnalogEntry_Object = MibTableRow
gx2Dm200AnalogEntry = _Gx2Dm200AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1)
)
gx2Dm200AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Dm200-MIB", "gx2Dm200AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm200AnalogEntry.setStatus("mandatory")


class _Gx2Dm200AnalogTableIndex_Type(Integer32):
    """Custom type gx2Dm200AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Dm200AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Dm200AnalogTableIndex_Object = MibTableColumn
gx2Dm200AnalogTableIndex = _Gx2Dm200AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 1),
    _Gx2Dm200AnalogTableIndex_Type()
)
gx2Dm200AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm200AnalogTableIndex.setStatus("mandatory")


class _Dm200labelOffsetNomMonitor_Type(DisplayString):
    """Custom type dm200labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm200labelOffsetNomMonitor_Object = MibTableColumn
dm200labelOffsetNomMonitor = _Dm200labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 2),
    _Dm200labelOffsetNomMonitor_Type()
)
dm200labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelOffsetNomMonitor.setStatus("optional")


class _Dm200uomOffsetNomMonitor_Type(DisplayString):
    """Custom type dm200uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm200uomOffsetNomMonitor_Object = MibTableColumn
dm200uomOffsetNomMonitor = _Dm200uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 3),
    _Dm200uomOffsetNomMonitor_Type()
)
dm200uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomOffsetNomMonitor.setStatus("optional")
_Dm200majorHighOffsetNomMonitor_Type = Float
_Dm200majorHighOffsetNomMonitor_Object = MibTableColumn
dm200majorHighOffsetNomMonitor = _Dm200majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 4),
    _Dm200majorHighOffsetNomMonitor_Type()
)
dm200majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighOffsetNomMonitor.setStatus("obsolete")
_Dm200majorLowOffsetNomMonitor_Type = Float
_Dm200majorLowOffsetNomMonitor_Object = MibTableColumn
dm200majorLowOffsetNomMonitor = _Dm200majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 5),
    _Dm200majorLowOffsetNomMonitor_Type()
)
dm200majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowOffsetNomMonitor.setStatus("obsolete")
_Dm200minorHighOffsetNomMonitor_Type = Float
_Dm200minorHighOffsetNomMonitor_Object = MibTableColumn
dm200minorHighOffsetNomMonitor = _Dm200minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 6),
    _Dm200minorHighOffsetNomMonitor_Type()
)
dm200minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighOffsetNomMonitor.setStatus("obsolete")
_Dm200minorLowOffsetNomMonitor_Type = Float
_Dm200minorLowOffsetNomMonitor_Object = MibTableColumn
dm200minorLowOffsetNomMonitor = _Dm200minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 7),
    _Dm200minorLowOffsetNomMonitor_Type()
)
dm200minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowOffsetNomMonitor.setStatus("obsolete")
_Dm200currentValueOffsetNomMonitor_Type = Float
_Dm200currentValueOffsetNomMonitor_Object = MibTableColumn
dm200currentValueOffsetNomMonitor = _Dm200currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 8),
    _Dm200currentValueOffsetNomMonitor_Type()
)
dm200currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueOffsetNomMonitor.setStatus("mandatory")


class _Dm200stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type dm200stateFlagOffsetNomMonitor based on Integer32"""
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


_Dm200stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm200stateFlagOffsetNomMonitor_Object = MibTableColumn
dm200stateFlagOffsetNomMonitor = _Dm200stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 9),
    _Dm200stateFlagOffsetNomMonitor_Type()
)
dm200stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagOffsetNomMonitor.setStatus("mandatory")
_Dm200minValueOffsetNomMonitor_Type = Float
_Dm200minValueOffsetNomMonitor_Object = MibTableColumn
dm200minValueOffsetNomMonitor = _Dm200minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 10),
    _Dm200minValueOffsetNomMonitor_Type()
)
dm200minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueOffsetNomMonitor.setStatus("mandatory")
_Dm200maxValueOffsetNomMonitor_Type = Float
_Dm200maxValueOffsetNomMonitor_Object = MibTableColumn
dm200maxValueOffsetNomMonitor = _Dm200maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 11),
    _Dm200maxValueOffsetNomMonitor_Type()
)
dm200maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueOffsetNomMonitor.setStatus("mandatory")


class _Dm200alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type dm200alarmStateOffsetNomMonitor based on Integer32"""
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


_Dm200alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm200alarmStateOffsetNomMonitor_Object = MibTableColumn
dm200alarmStateOffsetNomMonitor = _Dm200alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 12),
    _Dm200alarmStateOffsetNomMonitor_Type()
)
dm200alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Dm200labelAttenSetting_Type(DisplayString):
    """Custom type dm200labelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelAttenSetting_Type.__name__ = "DisplayString"
_Dm200labelAttenSetting_Object = MibTableColumn
dm200labelAttenSetting = _Dm200labelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 13),
    _Dm200labelAttenSetting_Type()
)
dm200labelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelAttenSetting.setStatus("optional")


class _Dm200uomAttenSetting_Type(DisplayString):
    """Custom type dm200uomAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomAttenSetting_Type.__name__ = "DisplayString"
_Dm200uomAttenSetting_Object = MibTableColumn
dm200uomAttenSetting = _Dm200uomAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 14),
    _Dm200uomAttenSetting_Type()
)
dm200uomAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomAttenSetting.setStatus("optional")
_Dm200majorHighAttenSetting_Type = Float
_Dm200majorHighAttenSetting_Object = MibTableColumn
dm200majorHighAttenSetting = _Dm200majorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 15),
    _Dm200majorHighAttenSetting_Type()
)
dm200majorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighAttenSetting.setStatus("obsolete")
_Dm200majorLowAttenSetting_Type = Float
_Dm200majorLowAttenSetting_Object = MibTableColumn
dm200majorLowAttenSetting = _Dm200majorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 16),
    _Dm200majorLowAttenSetting_Type()
)
dm200majorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowAttenSetting.setStatus("obsolete")
_Dm200minorHighAttenSetting_Type = Float
_Dm200minorHighAttenSetting_Object = MibTableColumn
dm200minorHighAttenSetting = _Dm200minorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 17),
    _Dm200minorHighAttenSetting_Type()
)
dm200minorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighAttenSetting.setStatus("obsolete")
_Dm200minorLowAttenSetting_Type = Float
_Dm200minorLowAttenSetting_Object = MibTableColumn
dm200minorLowAttenSetting = _Dm200minorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 18),
    _Dm200minorLowAttenSetting_Type()
)
dm200minorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowAttenSetting.setStatus("obsolete")
_Dm200currentValueAttenSetting_Type = Float
_Dm200currentValueAttenSetting_Object = MibTableColumn
dm200currentValueAttenSetting = _Dm200currentValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 19),
    _Dm200currentValueAttenSetting_Type()
)
dm200currentValueAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm200currentValueAttenSetting.setStatus("mandatory")


class _Dm200stateFlagAttenSetting_Type(Integer32):
    """Custom type dm200stateFlagAttenSetting based on Integer32"""
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


_Dm200stateFlagAttenSetting_Type.__name__ = "Integer32"
_Dm200stateFlagAttenSetting_Object = MibTableColumn
dm200stateFlagAttenSetting = _Dm200stateFlagAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 20),
    _Dm200stateFlagAttenSetting_Type()
)
dm200stateFlagAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagAttenSetting.setStatus("mandatory")
_Dm200minValueAttenSetting_Type = Float
_Dm200minValueAttenSetting_Object = MibTableColumn
dm200minValueAttenSetting = _Dm200minValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 21),
    _Dm200minValueAttenSetting_Type()
)
dm200minValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueAttenSetting.setStatus("mandatory")
_Dm200maxValueAttenSetting_Type = Float
_Dm200maxValueAttenSetting_Object = MibTableColumn
dm200maxValueAttenSetting = _Dm200maxValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 22),
    _Dm200maxValueAttenSetting_Type()
)
dm200maxValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueAttenSetting.setStatus("mandatory")


class _Dm200alarmStateAttenSetting_Type(Integer32):
    """Custom type dm200alarmStateAttenSetting based on Integer32"""
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


_Dm200alarmStateAttenSetting_Type.__name__ = "Integer32"
_Dm200alarmStateAttenSetting_Object = MibTableColumn
dm200alarmStateAttenSetting = _Dm200alarmStateAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 23),
    _Dm200alarmStateAttenSetting_Type()
)
dm200alarmStateAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateAttenSetting.setStatus("mandatory")


class _Dm200labelLaserPower_Type(DisplayString):
    """Custom type dm200labelLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelLaserPower_Type.__name__ = "DisplayString"
_Dm200labelLaserPower_Object = MibTableColumn
dm200labelLaserPower = _Dm200labelLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 24),
    _Dm200labelLaserPower_Type()
)
dm200labelLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelLaserPower.setStatus("optional")


class _Dm200uomLaserPower_Type(DisplayString):
    """Custom type dm200uomLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomLaserPower_Type.__name__ = "DisplayString"
_Dm200uomLaserPower_Object = MibTableColumn
dm200uomLaserPower = _Dm200uomLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 25),
    _Dm200uomLaserPower_Type()
)
dm200uomLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomLaserPower.setStatus("optional")
_Dm200majorHighLaserPower_Type = Float
_Dm200majorHighLaserPower_Object = MibTableColumn
dm200majorHighLaserPower = _Dm200majorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 26),
    _Dm200majorHighLaserPower_Type()
)
dm200majorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighLaserPower.setStatus("mandatory")
_Dm200majorLowLaserPower_Type = Float
_Dm200majorLowLaserPower_Object = MibTableColumn
dm200majorLowLaserPower = _Dm200majorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 27),
    _Dm200majorLowLaserPower_Type()
)
dm200majorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowLaserPower.setStatus("mandatory")
_Dm200minorHighLaserPower_Type = Float
_Dm200minorHighLaserPower_Object = MibTableColumn
dm200minorHighLaserPower = _Dm200minorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 28),
    _Dm200minorHighLaserPower_Type()
)
dm200minorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighLaserPower.setStatus("obsolete")
_Dm200minorLowLaserPower_Type = Float
_Dm200minorLowLaserPower_Object = MibTableColumn
dm200minorLowLaserPower = _Dm200minorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 29),
    _Dm200minorLowLaserPower_Type()
)
dm200minorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowLaserPower.setStatus("obsolete")
_Dm200currentValueLaserPower_Type = Float
_Dm200currentValueLaserPower_Object = MibTableColumn
dm200currentValueLaserPower = _Dm200currentValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 30),
    _Dm200currentValueLaserPower_Type()
)
dm200currentValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueLaserPower.setStatus("mandatory")


class _Dm200stateFlagLaserPower_Type(Integer32):
    """Custom type dm200stateFlagLaserPower based on Integer32"""
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


_Dm200stateFlagLaserPower_Type.__name__ = "Integer32"
_Dm200stateFlagLaserPower_Object = MibTableColumn
dm200stateFlagLaserPower = _Dm200stateFlagLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 31),
    _Dm200stateFlagLaserPower_Type()
)
dm200stateFlagLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagLaserPower.setStatus("mandatory")
_Dm200minValueLaserPower_Type = Float
_Dm200minValueLaserPower_Object = MibTableColumn
dm200minValueLaserPower = _Dm200minValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 32),
    _Dm200minValueLaserPower_Type()
)
dm200minValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueLaserPower.setStatus("mandatory")
_Dm200maxValueLaserPower_Type = Float
_Dm200maxValueLaserPower_Object = MibTableColumn
dm200maxValueLaserPower = _Dm200maxValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 33),
    _Dm200maxValueLaserPower_Type()
)
dm200maxValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueLaserPower.setStatus("mandatory")


class _Dm200alarmStateLaserPower_Type(Integer32):
    """Custom type dm200alarmStateLaserPower based on Integer32"""
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


_Dm200alarmStateLaserPower_Type.__name__ = "Integer32"
_Dm200alarmStateLaserPower_Object = MibTableColumn
dm200alarmStateLaserPower = _Dm200alarmStateLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 34),
    _Dm200alarmStateLaserPower_Type()
)
dm200alarmStateLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateLaserPower.setStatus("mandatory")


class _Dm200labelLaserTemp_Type(DisplayString):
    """Custom type dm200labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelLaserTemp_Type.__name__ = "DisplayString"
_Dm200labelLaserTemp_Object = MibTableColumn
dm200labelLaserTemp = _Dm200labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 35),
    _Dm200labelLaserTemp_Type()
)
dm200labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelLaserTemp.setStatus("optional")


class _Dm200uomLaserTemp_Type(DisplayString):
    """Custom type dm200uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomLaserTemp_Type.__name__ = "DisplayString"
_Dm200uomLaserTemp_Object = MibTableColumn
dm200uomLaserTemp = _Dm200uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 36),
    _Dm200uomLaserTemp_Type()
)
dm200uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomLaserTemp.setStatus("optional")
_Dm200majorHighLaserTemp_Type = Float
_Dm200majorHighLaserTemp_Object = MibTableColumn
dm200majorHighLaserTemp = _Dm200majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 37),
    _Dm200majorHighLaserTemp_Type()
)
dm200majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighLaserTemp.setStatus("mandatory")
_Dm200majorLowLaserTemp_Type = Float
_Dm200majorLowLaserTemp_Object = MibTableColumn
dm200majorLowLaserTemp = _Dm200majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 38),
    _Dm200majorLowLaserTemp_Type()
)
dm200majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowLaserTemp.setStatus("mandatory")
_Dm200minorHighLaserTemp_Type = Float
_Dm200minorHighLaserTemp_Object = MibTableColumn
dm200minorHighLaserTemp = _Dm200minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 39),
    _Dm200minorHighLaserTemp_Type()
)
dm200minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighLaserTemp.setStatus("obsolete")
_Dm200minorLowLaserTemp_Type = Float
_Dm200minorLowLaserTemp_Object = MibTableColumn
dm200minorLowLaserTemp = _Dm200minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 40),
    _Dm200minorLowLaserTemp_Type()
)
dm200minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowLaserTemp.setStatus("obsolete")
_Dm200currentValueLaserTemp_Type = Float
_Dm200currentValueLaserTemp_Object = MibTableColumn
dm200currentValueLaserTemp = _Dm200currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 41),
    _Dm200currentValueLaserTemp_Type()
)
dm200currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueLaserTemp.setStatus("mandatory")


class _Dm200stateFlagLaserTemp_Type(Integer32):
    """Custom type dm200stateFlagLaserTemp based on Integer32"""
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


_Dm200stateFlagLaserTemp_Type.__name__ = "Integer32"
_Dm200stateFlagLaserTemp_Object = MibTableColumn
dm200stateFlagLaserTemp = _Dm200stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 42),
    _Dm200stateFlagLaserTemp_Type()
)
dm200stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagLaserTemp.setStatus("mandatory")
_Dm200minValueLaserTemp_Type = Float
_Dm200minValueLaserTemp_Object = MibTableColumn
dm200minValueLaserTemp = _Dm200minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 43),
    _Dm200minValueLaserTemp_Type()
)
dm200minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueLaserTemp.setStatus("mandatory")
_Dm200maxValueLaserTemp_Type = Float
_Dm200maxValueLaserTemp_Object = MibTableColumn
dm200maxValueLaserTemp = _Dm200maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 44),
    _Dm200maxValueLaserTemp_Type()
)
dm200maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueLaserTemp.setStatus("mandatory")


class _Dm200alarmStateLaserTemp_Type(Integer32):
    """Custom type dm200alarmStateLaserTemp based on Integer32"""
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


_Dm200alarmStateLaserTemp_Type.__name__ = "Integer32"
_Dm200alarmStateLaserTemp_Object = MibTableColumn
dm200alarmStateLaserTemp = _Dm200alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 45),
    _Dm200alarmStateLaserTemp_Type()
)
dm200alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateLaserTemp.setStatus("mandatory")


class _Dm200labelLaserCurrent_Type(DisplayString):
    """Custom type dm200labelLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelLaserCurrent_Type.__name__ = "DisplayString"
_Dm200labelLaserCurrent_Object = MibTableColumn
dm200labelLaserCurrent = _Dm200labelLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 46),
    _Dm200labelLaserCurrent_Type()
)
dm200labelLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelLaserCurrent.setStatus("optional")


class _Dm200uomLaserCurrent_Type(DisplayString):
    """Custom type dm200uomLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomLaserCurrent_Type.__name__ = "DisplayString"
_Dm200uomLaserCurrent_Object = MibTableColumn
dm200uomLaserCurrent = _Dm200uomLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 47),
    _Dm200uomLaserCurrent_Type()
)
dm200uomLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomLaserCurrent.setStatus("optional")
_Dm200majorHighLaserCurrent_Type = Float
_Dm200majorHighLaserCurrent_Object = MibTableColumn
dm200majorHighLaserCurrent = _Dm200majorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 48),
    _Dm200majorHighLaserCurrent_Type()
)
dm200majorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighLaserCurrent.setStatus("mandatory")
_Dm200majorLowLaserCurrent_Type = Float
_Dm200majorLowLaserCurrent_Object = MibTableColumn
dm200majorLowLaserCurrent = _Dm200majorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 49),
    _Dm200majorLowLaserCurrent_Type()
)
dm200majorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowLaserCurrent.setStatus("mandatory")
_Dm200minorHighLaserCurrent_Type = Float
_Dm200minorHighLaserCurrent_Object = MibTableColumn
dm200minorHighLaserCurrent = _Dm200minorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 50),
    _Dm200minorHighLaserCurrent_Type()
)
dm200minorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighLaserCurrent.setStatus("obsolete")
_Dm200minorLowLaserCurrent_Type = Float
_Dm200minorLowLaserCurrent_Object = MibTableColumn
dm200minorLowLaserCurrent = _Dm200minorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 51),
    _Dm200minorLowLaserCurrent_Type()
)
dm200minorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowLaserCurrent.setStatus("obsolete")
_Dm200currentValueLaserCurrent_Type = Float
_Dm200currentValueLaserCurrent_Object = MibTableColumn
dm200currentValueLaserCurrent = _Dm200currentValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 52),
    _Dm200currentValueLaserCurrent_Type()
)
dm200currentValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueLaserCurrent.setStatus("mandatory")


class _Dm200stateFlagLaserCurrent_Type(Integer32):
    """Custom type dm200stateFlagLaserCurrent based on Integer32"""
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


_Dm200stateFlagLaserCurrent_Type.__name__ = "Integer32"
_Dm200stateFlagLaserCurrent_Object = MibTableColumn
dm200stateFlagLaserCurrent = _Dm200stateFlagLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 53),
    _Dm200stateFlagLaserCurrent_Type()
)
dm200stateFlagLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagLaserCurrent.setStatus("mandatory")
_Dm200minValueLaserCurrent_Type = Float
_Dm200minValueLaserCurrent_Object = MibTableColumn
dm200minValueLaserCurrent = _Dm200minValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 54),
    _Dm200minValueLaserCurrent_Type()
)
dm200minValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueLaserCurrent.setStatus("mandatory")
_Dm200maxValueLaserCurrent_Type = Float
_Dm200maxValueLaserCurrent_Object = MibTableColumn
dm200maxValueLaserCurrent = _Dm200maxValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 55),
    _Dm200maxValueLaserCurrent_Type()
)
dm200maxValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueLaserCurrent.setStatus("mandatory")


class _Dm200alarmStateLaserCurrent_Type(Integer32):
    """Custom type dm200alarmStateLaserCurrent based on Integer32"""
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


_Dm200alarmStateLaserCurrent_Type.__name__ = "Integer32"
_Dm200alarmStateLaserCurrent_Object = MibTableColumn
dm200alarmStateLaserCurrent = _Dm200alarmStateLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 56),
    _Dm200alarmStateLaserCurrent_Type()
)
dm200alarmStateLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateLaserCurrent.setStatus("mandatory")


class _Dm200labelTecCurrent_Type(DisplayString):
    """Custom type dm200labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelTecCurrent_Type.__name__ = "DisplayString"
_Dm200labelTecCurrent_Object = MibTableColumn
dm200labelTecCurrent = _Dm200labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 57),
    _Dm200labelTecCurrent_Type()
)
dm200labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelTecCurrent.setStatus("optional")


class _Dm200uomTecCurrent_Type(DisplayString):
    """Custom type dm200uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomTecCurrent_Type.__name__ = "DisplayString"
_Dm200uomTecCurrent_Object = MibTableColumn
dm200uomTecCurrent = _Dm200uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 58),
    _Dm200uomTecCurrent_Type()
)
dm200uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomTecCurrent.setStatus("optional")
_Dm200majorHighTecCurrent_Type = Float
_Dm200majorHighTecCurrent_Object = MibTableColumn
dm200majorHighTecCurrent = _Dm200majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 59),
    _Dm200majorHighTecCurrent_Type()
)
dm200majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighTecCurrent.setStatus("mandatory")
_Dm200majorLowTecCurrent_Type = Float
_Dm200majorLowTecCurrent_Object = MibTableColumn
dm200majorLowTecCurrent = _Dm200majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 60),
    _Dm200majorLowTecCurrent_Type()
)
dm200majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowTecCurrent.setStatus("mandatory")
_Dm200minorHighTecCurrent_Type = Float
_Dm200minorHighTecCurrent_Object = MibTableColumn
dm200minorHighTecCurrent = _Dm200minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 61),
    _Dm200minorHighTecCurrent_Type()
)
dm200minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighTecCurrent.setStatus("obsolete")
_Dm200minorLowTecCurrent_Type = Float
_Dm200minorLowTecCurrent_Object = MibTableColumn
dm200minorLowTecCurrent = _Dm200minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 62),
    _Dm200minorLowTecCurrent_Type()
)
dm200minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowTecCurrent.setStatus("obsolete")
_Dm200currentValueTecCurrent_Type = Float
_Dm200currentValueTecCurrent_Object = MibTableColumn
dm200currentValueTecCurrent = _Dm200currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 63),
    _Dm200currentValueTecCurrent_Type()
)
dm200currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueTecCurrent.setStatus("mandatory")


class _Dm200stateFlagTecCurrent_Type(Integer32):
    """Custom type dm200stateFlagTecCurrent based on Integer32"""
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


_Dm200stateFlagTecCurrent_Type.__name__ = "Integer32"
_Dm200stateFlagTecCurrent_Object = MibTableColumn
dm200stateFlagTecCurrent = _Dm200stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 64),
    _Dm200stateFlagTecCurrent_Type()
)
dm200stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagTecCurrent.setStatus("mandatory")
_Dm200minValueTecCurrent_Type = Float
_Dm200minValueTecCurrent_Object = MibTableColumn
dm200minValueTecCurrent = _Dm200minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 65),
    _Dm200minValueTecCurrent_Type()
)
dm200minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueTecCurrent.setStatus("mandatory")
_Dm200maxValueTecCurrent_Type = Float
_Dm200maxValueTecCurrent_Object = MibTableColumn
dm200maxValueTecCurrent = _Dm200maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 66),
    _Dm200maxValueTecCurrent_Type()
)
dm200maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueTecCurrent.setStatus("mandatory")


class _Dm200alarmStateTecCurrent_Type(Integer32):
    """Custom type dm200alarmStateTecCurrent based on Integer32"""
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


_Dm200alarmStateTecCurrent_Type.__name__ = "Integer32"
_Dm200alarmStateTecCurrent_Object = MibTableColumn
dm200alarmStateTecCurrent = _Dm200alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 67),
    _Dm200alarmStateTecCurrent_Type()
)
dm200alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateTecCurrent.setStatus("mandatory")


class _Dm200labelModTemp_Type(DisplayString):
    """Custom type dm200labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelModTemp_Type.__name__ = "DisplayString"
_Dm200labelModTemp_Object = MibTableColumn
dm200labelModTemp = _Dm200labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 68),
    _Dm200labelModTemp_Type()
)
dm200labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelModTemp.setStatus("optional")


class _Dm200uomModTemp_Type(DisplayString):
    """Custom type dm200uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomModTemp_Type.__name__ = "DisplayString"
_Dm200uomModTemp_Object = MibTableColumn
dm200uomModTemp = _Dm200uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 69),
    _Dm200uomModTemp_Type()
)
dm200uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomModTemp.setStatus("optional")
_Dm200majorHighModTemp_Type = Float
_Dm200majorHighModTemp_Object = MibTableColumn
dm200majorHighModTemp = _Dm200majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 70),
    _Dm200majorHighModTemp_Type()
)
dm200majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighModTemp.setStatus("mandatory")
_Dm200majorLowModTemp_Type = Float
_Dm200majorLowModTemp_Object = MibTableColumn
dm200majorLowModTemp = _Dm200majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 71),
    _Dm200majorLowModTemp_Type()
)
dm200majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowModTemp.setStatus("mandatory")
_Dm200minorHighModTemp_Type = Float
_Dm200minorHighModTemp_Object = MibTableColumn
dm200minorHighModTemp = _Dm200minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 72),
    _Dm200minorHighModTemp_Type()
)
dm200minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighModTemp.setStatus("mandatory")
_Dm200minorLowModTemp_Type = Float
_Dm200minorLowModTemp_Object = MibTableColumn
dm200minorLowModTemp = _Dm200minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 73),
    _Dm200minorLowModTemp_Type()
)
dm200minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowModTemp.setStatus("mandatory")
_Dm200currentValueModTemp_Type = Float
_Dm200currentValueModTemp_Object = MibTableColumn
dm200currentValueModTemp = _Dm200currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 74),
    _Dm200currentValueModTemp_Type()
)
dm200currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueModTemp.setStatus("mandatory")


class _Dm200stateFlagModTemp_Type(Integer32):
    """Custom type dm200stateFlagModTemp based on Integer32"""
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


_Dm200stateFlagModTemp_Type.__name__ = "Integer32"
_Dm200stateFlagModTemp_Object = MibTableColumn
dm200stateFlagModTemp = _Dm200stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 75),
    _Dm200stateFlagModTemp_Type()
)
dm200stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagModTemp.setStatus("mandatory")
_Dm200minValueModTemp_Type = Float
_Dm200minValueModTemp_Object = MibTableColumn
dm200minValueModTemp = _Dm200minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 76),
    _Dm200minValueModTemp_Type()
)
dm200minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueModTemp.setStatus("mandatory")
_Dm200maxValueModTemp_Type = Float
_Dm200maxValueModTemp_Object = MibTableColumn
dm200maxValueModTemp = _Dm200maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 77),
    _Dm200maxValueModTemp_Type()
)
dm200maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueModTemp.setStatus("mandatory")


class _Dm200alarmStateModTemp_Type(Integer32):
    """Custom type dm200alarmStateModTemp based on Integer32"""
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


_Dm200alarmStateModTemp_Type.__name__ = "Integer32"
_Dm200alarmStateModTemp_Object = MibTableColumn
dm200alarmStateModTemp = _Dm200alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 78),
    _Dm200alarmStateModTemp_Type()
)
dm200alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateModTemp.setStatus("mandatory")


class _Dm200labelFanCurrent_Type(DisplayString):
    """Custom type dm200labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelFanCurrent_Type.__name__ = "DisplayString"
_Dm200labelFanCurrent_Object = MibTableColumn
dm200labelFanCurrent = _Dm200labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 79),
    _Dm200labelFanCurrent_Type()
)
dm200labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelFanCurrent.setStatus("optional")


class _Dm200uomFanCurrent_Type(DisplayString):
    """Custom type dm200uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200uomFanCurrent_Type.__name__ = "DisplayString"
_Dm200uomFanCurrent_Object = MibTableColumn
dm200uomFanCurrent = _Dm200uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 80),
    _Dm200uomFanCurrent_Type()
)
dm200uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200uomFanCurrent.setStatus("optional")
_Dm200majorHighFanCurrent_Type = Float
_Dm200majorHighFanCurrent_Object = MibTableColumn
dm200majorHighFanCurrent = _Dm200majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 81),
    _Dm200majorHighFanCurrent_Type()
)
dm200majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorHighFanCurrent.setStatus("mandatory")
_Dm200majorLowFanCurrent_Type = Float
_Dm200majorLowFanCurrent_Object = MibTableColumn
dm200majorLowFanCurrent = _Dm200majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 82),
    _Dm200majorLowFanCurrent_Type()
)
dm200majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200majorLowFanCurrent.setStatus("mandatory")
_Dm200minorHighFanCurrent_Type = Float
_Dm200minorHighFanCurrent_Object = MibTableColumn
dm200minorHighFanCurrent = _Dm200minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 83),
    _Dm200minorHighFanCurrent_Type()
)
dm200minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorHighFanCurrent.setStatus("obsolete")
_Dm200minorLowFanCurrent_Type = Float
_Dm200minorLowFanCurrent_Object = MibTableColumn
dm200minorLowFanCurrent = _Dm200minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 84),
    _Dm200minorLowFanCurrent_Type()
)
dm200minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minorLowFanCurrent.setStatus("obsolete")
_Dm200currentValueFanCurrent_Type = Float
_Dm200currentValueFanCurrent_Object = MibTableColumn
dm200currentValueFanCurrent = _Dm200currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 85),
    _Dm200currentValueFanCurrent_Type()
)
dm200currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200currentValueFanCurrent.setStatus("mandatory")


class _Dm200stateFlagFanCurrent_Type(Integer32):
    """Custom type dm200stateFlagFanCurrent based on Integer32"""
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


_Dm200stateFlagFanCurrent_Type.__name__ = "Integer32"
_Dm200stateFlagFanCurrent_Object = MibTableColumn
dm200stateFlagFanCurrent = _Dm200stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 86),
    _Dm200stateFlagFanCurrent_Type()
)
dm200stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateFlagFanCurrent.setStatus("mandatory")
_Dm200minValueFanCurrent_Type = Float
_Dm200minValueFanCurrent_Object = MibTableColumn
dm200minValueFanCurrent = _Dm200minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 87),
    _Dm200minValueFanCurrent_Type()
)
dm200minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200minValueFanCurrent.setStatus("mandatory")
_Dm200maxValueFanCurrent_Type = Float
_Dm200maxValueFanCurrent_Object = MibTableColumn
dm200maxValueFanCurrent = _Dm200maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 88),
    _Dm200maxValueFanCurrent_Type()
)
dm200maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200maxValueFanCurrent.setStatus("mandatory")


class _Dm200alarmStateFanCurrent_Type(Integer32):
    """Custom type dm200alarmStateFanCurrent based on Integer32"""
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


_Dm200alarmStateFanCurrent_Type.__name__ = "Integer32"
_Dm200alarmStateFanCurrent_Object = MibTableColumn
dm200alarmStateFanCurrent = _Dm200alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 2, 1, 89),
    _Dm200alarmStateFanCurrent_Type()
)
dm200alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200alarmStateFanCurrent.setStatus("mandatory")
_Gx2Dm200DigitalTable_Object = MibTable
gx2Dm200DigitalTable = _Gx2Dm200DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gx2Dm200DigitalTable.setStatus("mandatory")
_Gx2Dm200DigitalEntry_Object = MibTableRow
gx2Dm200DigitalEntry = _Gx2Dm200DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2)
)
gx2Dm200DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Dm200-MIB", "gx2Dm200DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm200DigitalEntry.setStatus("mandatory")


class _Gx2Dm200DigitalTableIndex_Type(Integer32):
    """Custom type gx2Dm200DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Dm200DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Dm200DigitalTableIndex_Object = MibTableColumn
gx2Dm200DigitalTableIndex = _Gx2Dm200DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 1),
    _Gx2Dm200DigitalTableIndex_Type()
)
gx2Dm200DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm200DigitalTableIndex.setStatus("mandatory")


class _Dm200labelRfInput_Type(DisplayString):
    """Custom type dm200labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelRfInput_Type.__name__ = "DisplayString"
_Dm200labelRfInput_Object = MibTableColumn
dm200labelRfInput = _Dm200labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 2),
    _Dm200labelRfInput_Type()
)
dm200labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelRfInput.setStatus("optional")


class _Dm200enumRfInput_Type(DisplayString):
    """Custom type dm200enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200enumRfInput_Type.__name__ = "DisplayString"
_Dm200enumRfInput_Object = MibTableColumn
dm200enumRfInput = _Dm200enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 3),
    _Dm200enumRfInput_Type()
)
dm200enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200enumRfInput.setStatus("optional")


class _Dm200valueRfInput_Type(Integer32):
    """Custom type dm200valueRfInput based on Integer32"""
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


_Dm200valueRfInput_Type.__name__ = "Integer32"
_Dm200valueRfInput_Object = MibTableColumn
dm200valueRfInput = _Dm200valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 4),
    _Dm200valueRfInput_Type()
)
dm200valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm200valueRfInput.setStatus("mandatory")


class _Dm200stateflagRfInput_Type(Integer32):
    """Custom type dm200stateflagRfInput based on Integer32"""
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


_Dm200stateflagRfInput_Type.__name__ = "Integer32"
_Dm200stateflagRfInput_Object = MibTableColumn
dm200stateflagRfInput = _Dm200stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 5),
    _Dm200stateflagRfInput_Type()
)
dm200stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagRfInput.setStatus("mandatory")


class _Dm200labelOptOutput_Type(DisplayString):
    """Custom type dm200labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelOptOutput_Type.__name__ = "DisplayString"
_Dm200labelOptOutput_Object = MibTableColumn
dm200labelOptOutput = _Dm200labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 6),
    _Dm200labelOptOutput_Type()
)
dm200labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelOptOutput.setStatus("optional")


class _Dm200enumOptOutput_Type(DisplayString):
    """Custom type dm200enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200enumOptOutput_Type.__name__ = "DisplayString"
_Dm200enumOptOutput_Object = MibTableColumn
dm200enumOptOutput = _Dm200enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 7),
    _Dm200enumOptOutput_Type()
)
dm200enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200enumOptOutput.setStatus("optional")


class _Dm200valueOptOutput_Type(Integer32):
    """Custom type dm200valueOptOutput based on Integer32"""
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


_Dm200valueOptOutput_Type.__name__ = "Integer32"
_Dm200valueOptOutput_Object = MibTableColumn
dm200valueOptOutput = _Dm200valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 8),
    _Dm200valueOptOutput_Type()
)
dm200valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm200valueOptOutput.setStatus("mandatory")


class _Dm200stateflagOptOutput_Type(Integer32):
    """Custom type dm200stateflagOptOutput based on Integer32"""
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


_Dm200stateflagOptOutput_Type.__name__ = "Integer32"
_Dm200stateflagOptOutput_Object = MibTableColumn
dm200stateflagOptOutput = _Dm200stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 9),
    _Dm200stateflagOptOutput_Type()
)
dm200stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagOptOutput.setStatus("mandatory")


class _Dm200labelSbsControl_Type(DisplayString):
    """Custom type dm200labelSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelSbsControl_Type.__name__ = "DisplayString"
_Dm200labelSbsControl_Object = MibTableColumn
dm200labelSbsControl = _Dm200labelSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 10),
    _Dm200labelSbsControl_Type()
)
dm200labelSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelSbsControl.setStatus("optional")


class _Dm200enumSbsControl_Type(DisplayString):
    """Custom type dm200enumSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200enumSbsControl_Type.__name__ = "DisplayString"
_Dm200enumSbsControl_Object = MibTableColumn
dm200enumSbsControl = _Dm200enumSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 11),
    _Dm200enumSbsControl_Type()
)
dm200enumSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200enumSbsControl.setStatus("optional")


class _Dm200valueSbsControl_Type(Integer32):
    """Custom type dm200valueSbsControl based on Integer32"""
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


_Dm200valueSbsControl_Type.__name__ = "Integer32"
_Dm200valueSbsControl_Object = MibTableColumn
dm200valueSbsControl = _Dm200valueSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 12),
    _Dm200valueSbsControl_Type()
)
dm200valueSbsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm200valueSbsControl.setStatus("mandatory")


class _Dm200stateflagSbsControl_Type(Integer32):
    """Custom type dm200stateflagSbsControl based on Integer32"""
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


_Dm200stateflagSbsControl_Type.__name__ = "Integer32"
_Dm200stateflagSbsControl_Object = MibTableColumn
dm200stateflagSbsControl = _Dm200stateflagSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 13),
    _Dm200stateflagSbsControl_Type()
)
dm200stateflagSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagSbsControl.setStatus("mandatory")


class _Dm200labelFactoryDefault_Type(DisplayString):
    """Custom type dm200labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelFactoryDefault_Type.__name__ = "DisplayString"
_Dm200labelFactoryDefault_Object = MibTableColumn
dm200labelFactoryDefault = _Dm200labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 14),
    _Dm200labelFactoryDefault_Type()
)
dm200labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelFactoryDefault.setStatus("optional")


class _Dm200enumFactoryDefault_Type(DisplayString):
    """Custom type dm200enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200enumFactoryDefault_Type.__name__ = "DisplayString"
_Dm200enumFactoryDefault_Object = MibTableColumn
dm200enumFactoryDefault = _Dm200enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 15),
    _Dm200enumFactoryDefault_Type()
)
dm200enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200enumFactoryDefault.setStatus("optional")


class _Dm200valueFactoryDefault_Type(Integer32):
    """Custom type dm200valueFactoryDefault based on Integer32"""
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


_Dm200valueFactoryDefault_Type.__name__ = "Integer32"
_Dm200valueFactoryDefault_Object = MibTableColumn
dm200valueFactoryDefault = _Dm200valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 16),
    _Dm200valueFactoryDefault_Type()
)
dm200valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm200valueFactoryDefault.setStatus("mandatory")


class _Dm200stateflagFactoryDefault_Type(Integer32):
    """Custom type dm200stateflagFactoryDefault based on Integer32"""
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


_Dm200stateflagFactoryDefault_Type.__name__ = "Integer32"
_Dm200stateflagFactoryDefault_Object = MibTableColumn
dm200stateflagFactoryDefault = _Dm200stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 3, 2, 17),
    _Dm200stateflagFactoryDefault_Type()
)
dm200stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagFactoryDefault.setStatus("mandatory")
_Gx2Dm200StatusTable_Object = MibTable
gx2Dm200StatusTable = _Gx2Dm200StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gx2Dm200StatusTable.setStatus("mandatory")
_Gx2Dm200StatusEntry_Object = MibTableRow
gx2Dm200StatusEntry = _Gx2Dm200StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3)
)
gx2Dm200StatusEntry.setIndexNames(
    (0, "OMNI-gx2Dm200-MIB", "gx2Dm200StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm200StatusEntry.setStatus("mandatory")


class _Gx2Dm200StatusTableIndex_Type(Integer32):
    """Custom type gx2Dm200StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Dm200StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Dm200StatusTableIndex_Object = MibTableColumn
gx2Dm200StatusTableIndex = _Gx2Dm200StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 1),
    _Gx2Dm200StatusTableIndex_Type()
)
gx2Dm200StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm200StatusTableIndex.setStatus("mandatory")


class _Dm200labelBoot_Type(DisplayString):
    """Custom type dm200labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelBoot_Type.__name__ = "DisplayString"
_Dm200labelBoot_Object = MibTableColumn
dm200labelBoot = _Dm200labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 2),
    _Dm200labelBoot_Type()
)
dm200labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelBoot.setStatus("optional")


class _Dm200valueBoot_Type(Integer32):
    """Custom type dm200valueBoot based on Integer32"""
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


_Dm200valueBoot_Type.__name__ = "Integer32"
_Dm200valueBoot_Object = MibTableColumn
dm200valueBoot = _Dm200valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 3),
    _Dm200valueBoot_Type()
)
dm200valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueBoot.setStatus("mandatory")


class _Dm200stateflagBoot_Type(Integer32):
    """Custom type dm200stateflagBoot based on Integer32"""
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


_Dm200stateflagBoot_Type.__name__ = "Integer32"
_Dm200stateflagBoot_Object = MibTableColumn
dm200stateflagBoot = _Dm200stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 4),
    _Dm200stateflagBoot_Type()
)
dm200stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagBoot.setStatus("mandatory")


class _Dm200labelFlash_Type(DisplayString):
    """Custom type dm200labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelFlash_Type.__name__ = "DisplayString"
_Dm200labelFlash_Object = MibTableColumn
dm200labelFlash = _Dm200labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 5),
    _Dm200labelFlash_Type()
)
dm200labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelFlash.setStatus("optional")


class _Dm200valueFlash_Type(Integer32):
    """Custom type dm200valueFlash based on Integer32"""
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


_Dm200valueFlash_Type.__name__ = "Integer32"
_Dm200valueFlash_Object = MibTableColumn
dm200valueFlash = _Dm200valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 6),
    _Dm200valueFlash_Type()
)
dm200valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueFlash.setStatus("mandatory")


class _Dm200stateflagFlash_Type(Integer32):
    """Custom type dm200stateflagFlash based on Integer32"""
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


_Dm200stateflagFlash_Type.__name__ = "Integer32"
_Dm200stateflagFlash_Object = MibTableColumn
dm200stateflagFlash = _Dm200stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 7),
    _Dm200stateflagFlash_Type()
)
dm200stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagFlash.setStatus("mandatory")


class _Dm200labelFactoryDataCRC_Type(DisplayString):
    """Custom type dm200labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Dm200labelFactoryDataCRC_Object = MibTableColumn
dm200labelFactoryDataCRC = _Dm200labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 8),
    _Dm200labelFactoryDataCRC_Type()
)
dm200labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelFactoryDataCRC.setStatus("optional")


class _Dm200valueFactoryDataCRC_Type(Integer32):
    """Custom type dm200valueFactoryDataCRC based on Integer32"""
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


_Dm200valueFactoryDataCRC_Type.__name__ = "Integer32"
_Dm200valueFactoryDataCRC_Object = MibTableColumn
dm200valueFactoryDataCRC = _Dm200valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 9),
    _Dm200valueFactoryDataCRC_Type()
)
dm200valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueFactoryDataCRC.setStatus("mandatory")


class _Dm200stateflagFactoryDataCRC_Type(Integer32):
    """Custom type dm200stateflagFactoryDataCRC based on Integer32"""
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


_Dm200stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Dm200stateflagFactoryDataCRC_Object = MibTableColumn
dm200stateflagFactoryDataCRC = _Dm200stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 10),
    _Dm200stateflagFactoryDataCRC_Type()
)
dm200stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagFactoryDataCRC.setStatus("mandatory")


class _Dm200labelLaserDataCRC_Type(DisplayString):
    """Custom type dm200labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelLaserDataCRC_Type.__name__ = "DisplayString"
_Dm200labelLaserDataCRC_Object = MibTableColumn
dm200labelLaserDataCRC = _Dm200labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 11),
    _Dm200labelLaserDataCRC_Type()
)
dm200labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelLaserDataCRC.setStatus("optional")


class _Dm200valueLaserDataCRC_Type(Integer32):
    """Custom type dm200valueLaserDataCRC based on Integer32"""
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


_Dm200valueLaserDataCRC_Type.__name__ = "Integer32"
_Dm200valueLaserDataCRC_Object = MibTableColumn
dm200valueLaserDataCRC = _Dm200valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 12),
    _Dm200valueLaserDataCRC_Type()
)
dm200valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueLaserDataCRC.setStatus("mandatory")


class _Dm200stateflagLaserDataCRC_Type(Integer32):
    """Custom type dm200stateflagLaserDataCRC based on Integer32"""
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


_Dm200stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Dm200stateflagLaserDataCRC_Object = MibTableColumn
dm200stateflagLaserDataCRC = _Dm200stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 13),
    _Dm200stateflagLaserDataCRC_Type()
)
dm200stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagLaserDataCRC.setStatus("mandatory")


class _Dm200labelAlarmDataCrc_Type(DisplayString):
    """Custom type dm200labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Dm200labelAlarmDataCrc_Object = MibTableColumn
dm200labelAlarmDataCrc = _Dm200labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 14),
    _Dm200labelAlarmDataCrc_Type()
)
dm200labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelAlarmDataCrc.setStatus("optional")


class _Dm200valueAlarmDataCrc_Type(Integer32):
    """Custom type dm200valueAlarmDataCrc based on Integer32"""
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


_Dm200valueAlarmDataCrc_Type.__name__ = "Integer32"
_Dm200valueAlarmDataCrc_Object = MibTableColumn
dm200valueAlarmDataCrc = _Dm200valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 15),
    _Dm200valueAlarmDataCrc_Type()
)
dm200valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueAlarmDataCrc.setStatus("mandatory")


class _Dm200stateflagAlarmDataCrc_Type(Integer32):
    """Custom type dm200stateflagAlarmDataCrc based on Integer32"""
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


_Dm200stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Dm200stateflagAlarmDataCrc_Object = MibTableColumn
dm200stateflagAlarmDataCrc = _Dm200stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 16),
    _Dm200stateflagAlarmDataCrc_Type()
)
dm200stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagAlarmDataCrc.setStatus("mandatory")


class _Dm200labelRFInputStatus_Type(DisplayString):
    """Custom type dm200labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200labelRFInputStatus_Type.__name__ = "DisplayString"
_Dm200labelRFInputStatus_Object = MibTableColumn
dm200labelRFInputStatus = _Dm200labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 17),
    _Dm200labelRFInputStatus_Type()
)
dm200labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200labelRFInputStatus.setStatus("optional")


class _Dm200valueRFInputStatus_Type(Integer32):
    """Custom type dm200valueRFInputStatus based on Integer32"""
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


_Dm200valueRFInputStatus_Type.__name__ = "Integer32"
_Dm200valueRFInputStatus_Object = MibTableColumn
dm200valueRFInputStatus = _Dm200valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 18),
    _Dm200valueRFInputStatus_Type()
)
dm200valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200valueRFInputStatus.setStatus("mandatory")


class _Dm200stateflagRFInputStatus_Type(Integer32):
    """Custom type dm200stateflagRFInputStatus based on Integer32"""
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


_Dm200stateflagRFInputStatus_Type.__name__ = "Integer32"
_Dm200stateflagRFInputStatus_Object = MibTableColumn
dm200stateflagRFInputStatus = _Dm200stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 4, 3, 19),
    _Dm200stateflagRFInputStatus_Type()
)
dm200stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200stateflagRFInputStatus.setStatus("mandatory")
_Gx2Dm200FactoryTable_Object = MibTable
gx2Dm200FactoryTable = _Gx2Dm200FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5)
)
if mibBuilder.loadTexts:
    gx2Dm200FactoryTable.setStatus("mandatory")
_Gx2Dm200FactoryEntry_Object = MibTableRow
gx2Dm200FactoryEntry = _Gx2Dm200FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4)
)
gx2Dm200FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Dm200-MIB", "gx2Dm200FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm200FactoryEntry.setStatus("mandatory")


class _Gx2Dm200FactoryTableIndex_Type(Integer32):
    """Custom type gx2Dm200FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Dm200FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Dm200FactoryTableIndex_Object = MibTableColumn
gx2Dm200FactoryTableIndex = _Gx2Dm200FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 1),
    _Gx2Dm200FactoryTableIndex_Type()
)
gx2Dm200FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm200FactoryTableIndex.setStatus("mandatory")
_Dm200bootControlByte_Type = Integer32
_Dm200bootControlByte_Object = MibTableColumn
dm200bootControlByte = _Dm200bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 2),
    _Dm200bootControlByte_Type()
)
dm200bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200bootControlByte.setStatus("mandatory")
_Dm200bootStatusByte_Type = Integer32
_Dm200bootStatusByte_Object = MibTableColumn
dm200bootStatusByte = _Dm200bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 3),
    _Dm200bootStatusByte_Type()
)
dm200bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200bootStatusByte.setStatus("mandatory")
_Dm200bank1CRC_Type = Integer32
_Dm200bank1CRC_Object = MibTableColumn
dm200bank1CRC = _Dm200bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 4),
    _Dm200bank1CRC_Type()
)
dm200bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200bank1CRC.setStatus("mandatory")
_Dm200bank2CRC_Type = Integer32
_Dm200bank2CRC_Object = MibTableColumn
dm200bank2CRC = _Dm200bank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 5),
    _Dm200bank2CRC_Type()
)
dm200bank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200bank2CRC.setStatus("mandatory")
_Dm200prgEEPROMByte_Type = Integer32
_Dm200prgEEPROMByte_Object = MibTableColumn
dm200prgEEPROMByte = _Dm200prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 6),
    _Dm200prgEEPROMByte_Type()
)
dm200prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200prgEEPROMByte.setStatus("mandatory")
_Dm200factoryCRC_Type = Integer32
_Dm200factoryCRC_Object = MibTableColumn
dm200factoryCRC = _Dm200factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 7),
    _Dm200factoryCRC_Type()
)
dm200factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200factoryCRC.setStatus("mandatory")


class _Dm200calculateCRC_Type(Integer32):
    """Custom type dm200calculateCRC based on Integer32"""
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


_Dm200calculateCRC_Type.__name__ = "Integer32"
_Dm200calculateCRC_Object = MibTableColumn
dm200calculateCRC = _Dm200calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 8),
    _Dm200calculateCRC_Type()
)
dm200calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200calculateCRC.setStatus("obsolete")
_Dm200hourMeter_Type = Integer32
_Dm200hourMeter_Object = MibTableColumn
dm200hourMeter = _Dm200hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 9),
    _Dm200hourMeter_Type()
)
dm200hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200hourMeter.setStatus("mandatory")
_Dm200flashPrgCntA_Type = Integer32
_Dm200flashPrgCntA_Object = MibTableColumn
dm200flashPrgCntA = _Dm200flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 10),
    _Dm200flashPrgCntA_Type()
)
dm200flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200flashPrgCntA.setStatus("mandatory")
_Dm200flashPrgCntB_Type = Integer32
_Dm200flashPrgCntB_Object = MibTableColumn
dm200flashPrgCntB = _Dm200flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 11),
    _Dm200flashPrgCntB_Type()
)
dm200flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200flashPrgCntB.setStatus("mandatory")


class _Dm200flashBankARev_Type(DisplayString):
    """Custom type dm200flashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200flashBankARev_Type.__name__ = "DisplayString"
_Dm200flashBankARev_Object = MibTableColumn
dm200flashBankARev = _Dm200flashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 12),
    _Dm200flashBankARev_Type()
)
dm200flashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200flashBankARev.setStatus("mandatory")


class _Dm200flashBankBRev_Type(DisplayString):
    """Custom type dm200flashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm200flashBankBRev_Type.__name__ = "DisplayString"
_Dm200flashBankBRev_Object = MibTableColumn
dm200flashBankBRev = _Dm200flashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 5, 4, 13),
    _Dm200flashBankBRev_Type()
)
dm200flashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm200flashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDM200ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 1)
)
trapDM200ConfigChangeInteger.setObjects(
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
    trapDM200ConfigChangeInteger.setStatus(
        ""
    )

trapDM200ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 2)
)
trapDM200ConfigChangeDisplayString.setObjects(
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
    trapDM200ConfigChangeDisplayString.setStatus(
        ""
    )

trapDM200fanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 3)
)
trapDM200fanCurrentAlarm.setObjects(
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
    trapDM200fanCurrentAlarm.setStatus(
        ""
    )

trapDM200ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 4)
)
trapDM200ModuleTempAlarm.setObjects(
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
    trapDM200ModuleTempAlarm.setStatus(
        ""
    )

trapDM200omiOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 5)
)
trapDM200omiOffsetAlarm.setObjects(
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
    trapDM200omiOffsetAlarm.setStatus(
        ""
    )

trapDM200tecCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 6)
)
trapDM200tecCurrentAlarm.setObjects(
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
    trapDM200tecCurrentAlarm.setStatus(
        ""
    )

trapDM200LaserCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 7)
)
trapDM200LaserCurrentAlarm.setObjects(
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
    trapDM200LaserCurrentAlarm.setStatus(
        ""
    )

trapDM200LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 8)
)
trapDM200LaserTempAlarm.setObjects(
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
    trapDM200LaserTempAlarm.setStatus(
        ""
    )

trapDM200LaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 9)
)
trapDM200LaserPowerAlarm.setObjects(
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
    trapDM200LaserPowerAlarm.setStatus(
        ""
    )

trapDM200FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 10)
)
trapDM200FlashAlarm.setObjects(
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
    trapDM200FlashAlarm.setStatus(
        ""
    )

trapDM200BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 11)
)
trapDM200BankBootAlarm.setObjects(
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
    trapDM200BankBootAlarm.setStatus(
        ""
    )

trapDM200AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 12)
)
trapDM200AlarmDataCRCAlarm.setObjects(
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
    trapDM200AlarmDataCRCAlarm.setStatus(
        ""
    )

trapDM200FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 13)
)
trapDM200FactoryDataCRCAlarm.setObjects(
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
    trapDM200FactoryDataCRCAlarm.setStatus(
        ""
    )

trapDM200CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 14)
)
trapDM200CalDataCRCAlarm.setObjects(
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
    trapDM200CalDataCRCAlarm.setStatus(
        ""
    )

trapDM200ResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 15)
)
trapDM200ResetFacDefault.setObjects(
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
    trapDM200ResetFacDefault.setStatus(
        ""
    )

trapDM200UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 16)
)
trapDM200UserRFOffAlarm.setObjects(
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
    trapDM200UserRFOffAlarm.setStatus(
        ""
    )

trapDM200UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 17)
)
trapDM200UserOpticalOffAlarm.setObjects(
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
    trapDM200UserOpticalOffAlarm.setStatus(
        ""
    )

trapDM200UserSBSOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 18)
)
trapDM200UserSBSOffAlarm.setObjects(
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
    trapDM200UserSBSOffAlarm.setStatus(
        ""
    )

trapDM200RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 19)
)
trapDM200RFInputAlarm.setObjects(
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
    trapDM200RFInputAlarm.setStatus(
        ""
    )

trapDM200RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19, 0, 20)
)
trapDM200RFOverloadAlarm.setObjects(
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
    trapDM200RFOverloadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Dm200-MIB",
    **{"Float": Float,
       "trapDM200ConfigChangeInteger": trapDM200ConfigChangeInteger,
       "trapDM200ConfigChangeDisplayString": trapDM200ConfigChangeDisplayString,
       "trapDM200fanCurrentAlarm": trapDM200fanCurrentAlarm,
       "trapDM200ModuleTempAlarm": trapDM200ModuleTempAlarm,
       "trapDM200omiOffsetAlarm": trapDM200omiOffsetAlarm,
       "trapDM200tecCurrentAlarm": trapDM200tecCurrentAlarm,
       "trapDM200LaserCurrentAlarm": trapDM200LaserCurrentAlarm,
       "trapDM200LaserTempAlarm": trapDM200LaserTempAlarm,
       "trapDM200LaserPowerAlarm": trapDM200LaserPowerAlarm,
       "trapDM200FlashAlarm": trapDM200FlashAlarm,
       "trapDM200BankBootAlarm": trapDM200BankBootAlarm,
       "trapDM200AlarmDataCRCAlarm": trapDM200AlarmDataCRCAlarm,
       "trapDM200FactoryDataCRCAlarm": trapDM200FactoryDataCRCAlarm,
       "trapDM200CalDataCRCAlarm": trapDM200CalDataCRCAlarm,
       "trapDM200ResetFacDefault": trapDM200ResetFacDefault,
       "trapDM200UserRFOffAlarm": trapDM200UserRFOffAlarm,
       "trapDM200UserOpticalOffAlarm": trapDM200UserOpticalOffAlarm,
       "trapDM200UserSBSOffAlarm": trapDM200UserSBSOffAlarm,
       "trapDM200RFInputAlarm": trapDM200RFInputAlarm,
       "trapDM200RFOverloadAlarm": trapDM200RFOverloadAlarm,
       "gx2Dm200Descriptor": gx2Dm200Descriptor,
       "gx2Dm200AnalogTable": gx2Dm200AnalogTable,
       "gx2Dm200AnalogEntry": gx2Dm200AnalogEntry,
       "gx2Dm200AnalogTableIndex": gx2Dm200AnalogTableIndex,
       "dm200labelOffsetNomMonitor": dm200labelOffsetNomMonitor,
       "dm200uomOffsetNomMonitor": dm200uomOffsetNomMonitor,
       "dm200majorHighOffsetNomMonitor": dm200majorHighOffsetNomMonitor,
       "dm200majorLowOffsetNomMonitor": dm200majorLowOffsetNomMonitor,
       "dm200minorHighOffsetNomMonitor": dm200minorHighOffsetNomMonitor,
       "dm200minorLowOffsetNomMonitor": dm200minorLowOffsetNomMonitor,
       "dm200currentValueOffsetNomMonitor": dm200currentValueOffsetNomMonitor,
       "dm200stateFlagOffsetNomMonitor": dm200stateFlagOffsetNomMonitor,
       "dm200minValueOffsetNomMonitor": dm200minValueOffsetNomMonitor,
       "dm200maxValueOffsetNomMonitor": dm200maxValueOffsetNomMonitor,
       "dm200alarmStateOffsetNomMonitor": dm200alarmStateOffsetNomMonitor,
       "dm200labelAttenSetting": dm200labelAttenSetting,
       "dm200uomAttenSetting": dm200uomAttenSetting,
       "dm200majorHighAttenSetting": dm200majorHighAttenSetting,
       "dm200majorLowAttenSetting": dm200majorLowAttenSetting,
       "dm200minorHighAttenSetting": dm200minorHighAttenSetting,
       "dm200minorLowAttenSetting": dm200minorLowAttenSetting,
       "dm200currentValueAttenSetting": dm200currentValueAttenSetting,
       "dm200stateFlagAttenSetting": dm200stateFlagAttenSetting,
       "dm200minValueAttenSetting": dm200minValueAttenSetting,
       "dm200maxValueAttenSetting": dm200maxValueAttenSetting,
       "dm200alarmStateAttenSetting": dm200alarmStateAttenSetting,
       "dm200labelLaserPower": dm200labelLaserPower,
       "dm200uomLaserPower": dm200uomLaserPower,
       "dm200majorHighLaserPower": dm200majorHighLaserPower,
       "dm200majorLowLaserPower": dm200majorLowLaserPower,
       "dm200minorHighLaserPower": dm200minorHighLaserPower,
       "dm200minorLowLaserPower": dm200minorLowLaserPower,
       "dm200currentValueLaserPower": dm200currentValueLaserPower,
       "dm200stateFlagLaserPower": dm200stateFlagLaserPower,
       "dm200minValueLaserPower": dm200minValueLaserPower,
       "dm200maxValueLaserPower": dm200maxValueLaserPower,
       "dm200alarmStateLaserPower": dm200alarmStateLaserPower,
       "dm200labelLaserTemp": dm200labelLaserTemp,
       "dm200uomLaserTemp": dm200uomLaserTemp,
       "dm200majorHighLaserTemp": dm200majorHighLaserTemp,
       "dm200majorLowLaserTemp": dm200majorLowLaserTemp,
       "dm200minorHighLaserTemp": dm200minorHighLaserTemp,
       "dm200minorLowLaserTemp": dm200minorLowLaserTemp,
       "dm200currentValueLaserTemp": dm200currentValueLaserTemp,
       "dm200stateFlagLaserTemp": dm200stateFlagLaserTemp,
       "dm200minValueLaserTemp": dm200minValueLaserTemp,
       "dm200maxValueLaserTemp": dm200maxValueLaserTemp,
       "dm200alarmStateLaserTemp": dm200alarmStateLaserTemp,
       "dm200labelLaserCurrent": dm200labelLaserCurrent,
       "dm200uomLaserCurrent": dm200uomLaserCurrent,
       "dm200majorHighLaserCurrent": dm200majorHighLaserCurrent,
       "dm200majorLowLaserCurrent": dm200majorLowLaserCurrent,
       "dm200minorHighLaserCurrent": dm200minorHighLaserCurrent,
       "dm200minorLowLaserCurrent": dm200minorLowLaserCurrent,
       "dm200currentValueLaserCurrent": dm200currentValueLaserCurrent,
       "dm200stateFlagLaserCurrent": dm200stateFlagLaserCurrent,
       "dm200minValueLaserCurrent": dm200minValueLaserCurrent,
       "dm200maxValueLaserCurrent": dm200maxValueLaserCurrent,
       "dm200alarmStateLaserCurrent": dm200alarmStateLaserCurrent,
       "dm200labelTecCurrent": dm200labelTecCurrent,
       "dm200uomTecCurrent": dm200uomTecCurrent,
       "dm200majorHighTecCurrent": dm200majorHighTecCurrent,
       "dm200majorLowTecCurrent": dm200majorLowTecCurrent,
       "dm200minorHighTecCurrent": dm200minorHighTecCurrent,
       "dm200minorLowTecCurrent": dm200minorLowTecCurrent,
       "dm200currentValueTecCurrent": dm200currentValueTecCurrent,
       "dm200stateFlagTecCurrent": dm200stateFlagTecCurrent,
       "dm200minValueTecCurrent": dm200minValueTecCurrent,
       "dm200maxValueTecCurrent": dm200maxValueTecCurrent,
       "dm200alarmStateTecCurrent": dm200alarmStateTecCurrent,
       "dm200labelModTemp": dm200labelModTemp,
       "dm200uomModTemp": dm200uomModTemp,
       "dm200majorHighModTemp": dm200majorHighModTemp,
       "dm200majorLowModTemp": dm200majorLowModTemp,
       "dm200minorHighModTemp": dm200minorHighModTemp,
       "dm200minorLowModTemp": dm200minorLowModTemp,
       "dm200currentValueModTemp": dm200currentValueModTemp,
       "dm200stateFlagModTemp": dm200stateFlagModTemp,
       "dm200minValueModTemp": dm200minValueModTemp,
       "dm200maxValueModTemp": dm200maxValueModTemp,
       "dm200alarmStateModTemp": dm200alarmStateModTemp,
       "dm200labelFanCurrent": dm200labelFanCurrent,
       "dm200uomFanCurrent": dm200uomFanCurrent,
       "dm200majorHighFanCurrent": dm200majorHighFanCurrent,
       "dm200majorLowFanCurrent": dm200majorLowFanCurrent,
       "dm200minorHighFanCurrent": dm200minorHighFanCurrent,
       "dm200minorLowFanCurrent": dm200minorLowFanCurrent,
       "dm200currentValueFanCurrent": dm200currentValueFanCurrent,
       "dm200stateFlagFanCurrent": dm200stateFlagFanCurrent,
       "dm200minValueFanCurrent": dm200minValueFanCurrent,
       "dm200maxValueFanCurrent": dm200maxValueFanCurrent,
       "dm200alarmStateFanCurrent": dm200alarmStateFanCurrent,
       "gx2Dm200DigitalTable": gx2Dm200DigitalTable,
       "gx2Dm200DigitalEntry": gx2Dm200DigitalEntry,
       "gx2Dm200DigitalTableIndex": gx2Dm200DigitalTableIndex,
       "dm200labelRfInput": dm200labelRfInput,
       "dm200enumRfInput": dm200enumRfInput,
       "dm200valueRfInput": dm200valueRfInput,
       "dm200stateflagRfInput": dm200stateflagRfInput,
       "dm200labelOptOutput": dm200labelOptOutput,
       "dm200enumOptOutput": dm200enumOptOutput,
       "dm200valueOptOutput": dm200valueOptOutput,
       "dm200stateflagOptOutput": dm200stateflagOptOutput,
       "dm200labelSbsControl": dm200labelSbsControl,
       "dm200enumSbsControl": dm200enumSbsControl,
       "dm200valueSbsControl": dm200valueSbsControl,
       "dm200stateflagSbsControl": dm200stateflagSbsControl,
       "dm200labelFactoryDefault": dm200labelFactoryDefault,
       "dm200enumFactoryDefault": dm200enumFactoryDefault,
       "dm200valueFactoryDefault": dm200valueFactoryDefault,
       "dm200stateflagFactoryDefault": dm200stateflagFactoryDefault,
       "gx2Dm200StatusTable": gx2Dm200StatusTable,
       "gx2Dm200StatusEntry": gx2Dm200StatusEntry,
       "gx2Dm200StatusTableIndex": gx2Dm200StatusTableIndex,
       "dm200labelBoot": dm200labelBoot,
       "dm200valueBoot": dm200valueBoot,
       "dm200stateflagBoot": dm200stateflagBoot,
       "dm200labelFlash": dm200labelFlash,
       "dm200valueFlash": dm200valueFlash,
       "dm200stateflagFlash": dm200stateflagFlash,
       "dm200labelFactoryDataCRC": dm200labelFactoryDataCRC,
       "dm200valueFactoryDataCRC": dm200valueFactoryDataCRC,
       "dm200stateflagFactoryDataCRC": dm200stateflagFactoryDataCRC,
       "dm200labelLaserDataCRC": dm200labelLaserDataCRC,
       "dm200valueLaserDataCRC": dm200valueLaserDataCRC,
       "dm200stateflagLaserDataCRC": dm200stateflagLaserDataCRC,
       "dm200labelAlarmDataCrc": dm200labelAlarmDataCrc,
       "dm200valueAlarmDataCrc": dm200valueAlarmDataCrc,
       "dm200stateflagAlarmDataCrc": dm200stateflagAlarmDataCrc,
       "dm200labelRFInputStatus": dm200labelRFInputStatus,
       "dm200valueRFInputStatus": dm200valueRFInputStatus,
       "dm200stateflagRFInputStatus": dm200stateflagRFInputStatus,
       "gx2Dm200FactoryTable": gx2Dm200FactoryTable,
       "gx2Dm200FactoryEntry": gx2Dm200FactoryEntry,
       "gx2Dm200FactoryTableIndex": gx2Dm200FactoryTableIndex,
       "dm200bootControlByte": dm200bootControlByte,
       "dm200bootStatusByte": dm200bootStatusByte,
       "dm200bank1CRC": dm200bank1CRC,
       "dm200bank2CRC": dm200bank2CRC,
       "dm200prgEEPROMByte": dm200prgEEPROMByte,
       "dm200factoryCRC": dm200factoryCRC,
       "dm200calculateCRC": dm200calculateCRC,
       "dm200hourMeter": dm200hourMeter,
       "dm200flashPrgCntA": dm200flashPrgCntA,
       "dm200flashPrgCntB": dm200flashPrgCntB,
       "dm200flashBankARev": dm200flashBankARev,
       "dm200flashBankBRev": dm200flashBankBRev}
)
