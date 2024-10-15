# SNMP MIB module (OMNI-gx2EM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2EM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:20 2024
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

(gx2Em1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Em1000")

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

_Gx2emDescriptor_ObjectIdentity = ObjectIdentity
gx2emDescriptor = _Gx2emDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 1)
)
_Gx2emAnalogTable_Object = MibTable
gx2emAnalogTable = _Gx2emAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2)
)
if mibBuilder.loadTexts:
    gx2emAnalogTable.setStatus("mandatory")
_Gx2emAnalogEntry_Object = MibTableRow
gx2emAnalogEntry = _Gx2emAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1)
)
gx2emAnalogEntry.setIndexNames(
    (0, "OMNI-gx2EM-MIB", "gx2emAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2emAnalogEntry.setStatus("mandatory")


class _Gx2emAnalogTableIndex_Type(Integer32):
    """Custom type gx2emAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2emAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2emAnalogTableIndex_Object = MibTableColumn
gx2emAnalogTableIndex = _Gx2emAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 1),
    _Gx2emAnalogTableIndex_Type()
)
gx2emAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2emAnalogTableIndex.setStatus("mandatory")


class _LabelOffsetNomMonitor_Type(DisplayString):
    """Custom type labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelOffsetNomMonitor_Type.__name__ = "DisplayString"
_LabelOffsetNomMonitor_Object = MibTableColumn
labelOffsetNomMonitor = _LabelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 2),
    _LabelOffsetNomMonitor_Type()
)
labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelOffsetNomMonitor.setStatus("optional")


class _UomOffsetNomMonitor_Type(DisplayString):
    """Custom type uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomOffsetNomMonitor_Type.__name__ = "DisplayString"
_UomOffsetNomMonitor_Object = MibTableColumn
uomOffsetNomMonitor = _UomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 3),
    _UomOffsetNomMonitor_Type()
)
uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomOffsetNomMonitor.setStatus("optional")
_MajorHighOffsetNomMonitor_Type = Float
_MajorHighOffsetNomMonitor_Object = MibTableColumn
majorHighOffsetNomMonitor = _MajorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 4),
    _MajorHighOffsetNomMonitor_Type()
)
majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighOffsetNomMonitor.setStatus("mandatory")
_MajorLowOffsetNomMonitor_Type = Float
_MajorLowOffsetNomMonitor_Object = MibTableColumn
majorLowOffsetNomMonitor = _MajorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 5),
    _MajorLowOffsetNomMonitor_Type()
)
majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowOffsetNomMonitor.setStatus("mandatory")
_MinorHighOffsetNomMonitor_Type = Float
_MinorHighOffsetNomMonitor_Object = MibTableColumn
minorHighOffsetNomMonitor = _MinorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 6),
    _MinorHighOffsetNomMonitor_Type()
)
minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighOffsetNomMonitor.setStatus("mandatory")
_MinorLowOffsetNomMonitor_Type = Float
_MinorLowOffsetNomMonitor_Object = MibTableColumn
minorLowOffsetNomMonitor = _MinorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 7),
    _MinorLowOffsetNomMonitor_Type()
)
minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowOffsetNomMonitor.setStatus("mandatory")
_CurrentValueOffsetNomMonitor_Type = Float
_CurrentValueOffsetNomMonitor_Object = MibTableColumn
currentValueOffsetNomMonitor = _CurrentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 8),
    _CurrentValueOffsetNomMonitor_Type()
)
currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueOffsetNomMonitor.setStatus("mandatory")


class _StateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type stateFlagOffsetNomMonitor based on Integer32"""
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


_StateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_StateFlagOffsetNomMonitor_Object = MibTableColumn
stateFlagOffsetNomMonitor = _StateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 9),
    _StateFlagOffsetNomMonitor_Type()
)
stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagOffsetNomMonitor.setStatus("mandatory")
_MinValueOffsetNomMonitor_Type = Float
_MinValueOffsetNomMonitor_Object = MibTableColumn
minValueOffsetNomMonitor = _MinValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 10),
    _MinValueOffsetNomMonitor_Type()
)
minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueOffsetNomMonitor.setStatus("mandatory")
_MaxValueOffsetNomMonitor_Type = Float
_MaxValueOffsetNomMonitor_Object = MibTableColumn
maxValueOffsetNomMonitor = _MaxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 11),
    _MaxValueOffsetNomMonitor_Type()
)
maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueOffsetNomMonitor.setStatus("mandatory")


class _AlarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type alarmStateOffsetNomMonitor based on Integer32"""
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


_AlarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_AlarmStateOffsetNomMonitor_Object = MibTableColumn
alarmStateOffsetNomMonitor = _AlarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 12),
    _AlarmStateOffsetNomMonitor_Type()
)
alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateOffsetNomMonitor.setStatus("mandatory")


class _LabelOffsetNomCnt_Type(DisplayString):
    """Custom type labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelOffsetNomCnt_Type.__name__ = "DisplayString"
_LabelOffsetNomCnt_Object = MibTableColumn
labelOffsetNomCnt = _LabelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 13),
    _LabelOffsetNomCnt_Type()
)
labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelOffsetNomCnt.setStatus("optional")


class _UomOffsetNomCnt_Type(DisplayString):
    """Custom type uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomOffsetNomCnt_Type.__name__ = "DisplayString"
_UomOffsetNomCnt_Object = MibTableColumn
uomOffsetNomCnt = _UomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 14),
    _UomOffsetNomCnt_Type()
)
uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomOffsetNomCnt.setStatus("optional")
_MajorHighOffsetNomCnt_Type = Float
_MajorHighOffsetNomCnt_Object = MibTableColumn
majorHighOffsetNomCnt = _MajorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 15),
    _MajorHighOffsetNomCnt_Type()
)
majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighOffsetNomCnt.setStatus("mandatory")
_MajorLowOffsetNomCnt_Type = Float
_MajorLowOffsetNomCnt_Object = MibTableColumn
majorLowOffsetNomCnt = _MajorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 16),
    _MajorLowOffsetNomCnt_Type()
)
majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowOffsetNomCnt.setStatus("mandatory")
_MinorHighOffsetNomCnt_Type = Float
_MinorHighOffsetNomCnt_Object = MibTableColumn
minorHighOffsetNomCnt = _MinorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 17),
    _MinorHighOffsetNomCnt_Type()
)
minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighOffsetNomCnt.setStatus("mandatory")
_MinorLowOffsetNomCnt_Type = Float
_MinorLowOffsetNomCnt_Object = MibTableColumn
minorLowOffsetNomCnt = _MinorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 18),
    _MinorLowOffsetNomCnt_Type()
)
minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowOffsetNomCnt.setStatus("mandatory")
_CurrentValueOffsetNomCnt_Type = Float
_CurrentValueOffsetNomCnt_Object = MibTableColumn
currentValueOffsetNomCnt = _CurrentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 19),
    _CurrentValueOffsetNomCnt_Type()
)
currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentValueOffsetNomCnt.setStatus("mandatory")


class _StateFlagOffsetNomCnt_Type(Integer32):
    """Custom type stateFlagOffsetNomCnt based on Integer32"""
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


_StateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_StateFlagOffsetNomCnt_Object = MibTableColumn
stateFlagOffsetNomCnt = _StateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 20),
    _StateFlagOffsetNomCnt_Type()
)
stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagOffsetNomCnt.setStatus("mandatory")
_MinValueOffsetNomCnt_Type = Float
_MinValueOffsetNomCnt_Object = MibTableColumn
minValueOffsetNomCnt = _MinValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 21),
    _MinValueOffsetNomCnt_Type()
)
minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueOffsetNomCnt.setStatus("mandatory")
_MaxValueOffsetNomCnt_Type = Float
_MaxValueOffsetNomCnt_Object = MibTableColumn
maxValueOffsetNomCnt = _MaxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 22),
    _MaxValueOffsetNomCnt_Type()
)
maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueOffsetNomCnt.setStatus("mandatory")


class _AlarmStateOffsetNomCnt_Type(Integer32):
    """Custom type alarmStateOffsetNomCnt based on Integer32"""
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


_AlarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_AlarmStateOffsetNomCnt_Object = MibTableColumn
alarmStateOffsetNomCnt = _AlarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 23),
    _AlarmStateOffsetNomCnt_Type()
)
alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateOffsetNomCnt.setStatus("mandatory")


class _LabelRelAttenSetting_Type(DisplayString):
    """Custom type labelRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelRelAttenSetting_Type.__name__ = "DisplayString"
_LabelRelAttenSetting_Object = MibTableColumn
labelRelAttenSetting = _LabelRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 24),
    _LabelRelAttenSetting_Type()
)
labelRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelRelAttenSetting.setStatus("optional")


class _UomRelAttenSetting_Type(DisplayString):
    """Custom type uomRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomRelAttenSetting_Type.__name__ = "DisplayString"
_UomRelAttenSetting_Object = MibTableColumn
uomRelAttenSetting = _UomRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 25),
    _UomRelAttenSetting_Type()
)
uomRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomRelAttenSetting.setStatus("optional")
_MajorHighRelAttenSetting_Type = Float
_MajorHighRelAttenSetting_Object = MibTableColumn
majorHighRelAttenSetting = _MajorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 26),
    _MajorHighRelAttenSetting_Type()
)
majorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighRelAttenSetting.setStatus("mandatory")
_MajorLowRelAttenSetting_Type = Float
_MajorLowRelAttenSetting_Object = MibTableColumn
majorLowRelAttenSetting = _MajorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 27),
    _MajorLowRelAttenSetting_Type()
)
majorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowRelAttenSetting.setStatus("mandatory")
_MinorHighRelAttenSetting_Type = Float
_MinorHighRelAttenSetting_Object = MibTableColumn
minorHighRelAttenSetting = _MinorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 28),
    _MinorHighRelAttenSetting_Type()
)
minorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighRelAttenSetting.setStatus("mandatory")
_MinorLowRelAttenSetting_Type = Float
_MinorLowRelAttenSetting_Object = MibTableColumn
minorLowRelAttenSetting = _MinorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 29),
    _MinorLowRelAttenSetting_Type()
)
minorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowRelAttenSetting.setStatus("mandatory")
_CurrentValueRelAttenSetting_Type = Float
_CurrentValueRelAttenSetting_Object = MibTableColumn
currentValueRelAttenSetting = _CurrentValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 30),
    _CurrentValueRelAttenSetting_Type()
)
currentValueRelAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentValueRelAttenSetting.setStatus("mandatory")


class _StateFlagRelAttenSetting_Type(Integer32):
    """Custom type stateFlagRelAttenSetting based on Integer32"""
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


_StateFlagRelAttenSetting_Type.__name__ = "Integer32"
_StateFlagRelAttenSetting_Object = MibTableColumn
stateFlagRelAttenSetting = _StateFlagRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 31),
    _StateFlagRelAttenSetting_Type()
)
stateFlagRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagRelAttenSetting.setStatus("mandatory")
_MinValueRelAttenSetting_Type = Float
_MinValueRelAttenSetting_Object = MibTableColumn
minValueRelAttenSetting = _MinValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 32),
    _MinValueRelAttenSetting_Type()
)
minValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueRelAttenSetting.setStatus("mandatory")
_MaxValueRelAttenSetting_Type = Float
_MaxValueRelAttenSetting_Object = MibTableColumn
maxValueRelAttenSetting = _MaxValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 33),
    _MaxValueRelAttenSetting_Type()
)
maxValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueRelAttenSetting.setStatus("mandatory")


class _AlarmStateRelAttenSetting_Type(Integer32):
    """Custom type alarmStateRelAttenSetting based on Integer32"""
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


_AlarmStateRelAttenSetting_Type.__name__ = "Integer32"
_AlarmStateRelAttenSetting_Object = MibTableColumn
alarmStateRelAttenSetting = _AlarmStateRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 34),
    _AlarmStateRelAttenSetting_Type()
)
alarmStateRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateRelAttenSetting.setStatus("mandatory")


class _LabelOptPower_Type(DisplayString):
    """Custom type labelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelOptPower_Type.__name__ = "DisplayString"
_LabelOptPower_Object = MibTableColumn
labelOptPower = _LabelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 35),
    _LabelOptPower_Type()
)
labelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelOptPower.setStatus("optional")


class _UomOptPower_Type(DisplayString):
    """Custom type uomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomOptPower_Type.__name__ = "DisplayString"
_UomOptPower_Object = MibTableColumn
uomOptPower = _UomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 36),
    _UomOptPower_Type()
)
uomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomOptPower.setStatus("optional")
_MajorHighOptPower_Type = Float
_MajorHighOptPower_Object = MibTableColumn
majorHighOptPower = _MajorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 37),
    _MajorHighOptPower_Type()
)
majorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighOptPower.setStatus("mandatory")
_MajorLowOptPower_Type = Float
_MajorLowOptPower_Object = MibTableColumn
majorLowOptPower = _MajorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 38),
    _MajorLowOptPower_Type()
)
majorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowOptPower.setStatus("mandatory")
_MinorHighOptPower_Type = Float
_MinorHighOptPower_Object = MibTableColumn
minorHighOptPower = _MinorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 39),
    _MinorHighOptPower_Type()
)
minorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighOptPower.setStatus("mandatory")
_MinorLowOptPower_Type = Float
_MinorLowOptPower_Object = MibTableColumn
minorLowOptPower = _MinorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 40),
    _MinorLowOptPower_Type()
)
minorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowOptPower.setStatus("mandatory")
_CurrentValueOptPower_Type = Float
_CurrentValueOptPower_Object = MibTableColumn
currentValueOptPower = _CurrentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 41),
    _CurrentValueOptPower_Type()
)
currentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueOptPower.setStatus("mandatory")


class _StateFlagOptPower_Type(Integer32):
    """Custom type stateFlagOptPower based on Integer32"""
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


_StateFlagOptPower_Type.__name__ = "Integer32"
_StateFlagOptPower_Object = MibTableColumn
stateFlagOptPower = _StateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 42),
    _StateFlagOptPower_Type()
)
stateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagOptPower.setStatus("mandatory")
_MinValueOptPower_Type = Float
_MinValueOptPower_Object = MibTableColumn
minValueOptPower = _MinValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 43),
    _MinValueOptPower_Type()
)
minValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueOptPower.setStatus("mandatory")
_MaxValueOptPower_Type = Float
_MaxValueOptPower_Object = MibTableColumn
maxValueOptPower = _MaxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 44),
    _MaxValueOptPower_Type()
)
maxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueOptPower.setStatus("mandatory")


class _AlarmStateOptPower_Type(Integer32):
    """Custom type alarmStateOptPower based on Integer32"""
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


_AlarmStateOptPower_Type.__name__ = "Integer32"
_AlarmStateOptPower_Object = MibTableColumn
alarmStateOptPower = _AlarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 45),
    _AlarmStateOptPower_Type()
)
alarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateOptPower.setStatus("mandatory")


class _LabelLaserBias_Type(DisplayString):
    """Custom type labelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLaserBias_Type.__name__ = "DisplayString"
_LabelLaserBias_Object = MibTableColumn
labelLaserBias = _LabelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 46),
    _LabelLaserBias_Type()
)
labelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLaserBias.setStatus("optional")


class _UomLaserBias_Type(DisplayString):
    """Custom type uomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomLaserBias_Type.__name__ = "DisplayString"
_UomLaserBias_Object = MibTableColumn
uomLaserBias = _UomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 47),
    _UomLaserBias_Type()
)
uomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomLaserBias.setStatus("optional")
_MajorHighLaserBias_Type = Float
_MajorHighLaserBias_Object = MibTableColumn
majorHighLaserBias = _MajorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 48),
    _MajorHighLaserBias_Type()
)
majorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighLaserBias.setStatus("mandatory")
_MajorLowLaserBias_Type = Float
_MajorLowLaserBias_Object = MibTableColumn
majorLowLaserBias = _MajorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 49),
    _MajorLowLaserBias_Type()
)
majorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowLaserBias.setStatus("mandatory")
_MinorHighLaserBias_Type = Float
_MinorHighLaserBias_Object = MibTableColumn
minorHighLaserBias = _MinorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 50),
    _MinorHighLaserBias_Type()
)
minorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighLaserBias.setStatus("mandatory")
_MinorLowLaserBias_Type = Float
_MinorLowLaserBias_Object = MibTableColumn
minorLowLaserBias = _MinorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 51),
    _MinorLowLaserBias_Type()
)
minorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowLaserBias.setStatus("mandatory")
_CurrentValueLaserBias_Type = Float
_CurrentValueLaserBias_Object = MibTableColumn
currentValueLaserBias = _CurrentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 52),
    _CurrentValueLaserBias_Type()
)
currentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueLaserBias.setStatus("mandatory")


class _StateFlagLaserBias_Type(Integer32):
    """Custom type stateFlagLaserBias based on Integer32"""
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


_StateFlagLaserBias_Type.__name__ = "Integer32"
_StateFlagLaserBias_Object = MibTableColumn
stateFlagLaserBias = _StateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 53),
    _StateFlagLaserBias_Type()
)
stateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagLaserBias.setStatus("mandatory")
_MinValueLaserBias_Type = Float
_MinValueLaserBias_Object = MibTableColumn
minValueLaserBias = _MinValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 54),
    _MinValueLaserBias_Type()
)
minValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueLaserBias.setStatus("mandatory")
_MaxValueLaserBias_Type = Float
_MaxValueLaserBias_Object = MibTableColumn
maxValueLaserBias = _MaxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 55),
    _MaxValueLaserBias_Type()
)
maxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueLaserBias.setStatus("mandatory")


class _AlarmStateLaserBias_Type(Integer32):
    """Custom type alarmStateLaserBias based on Integer32"""
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


_AlarmStateLaserBias_Type.__name__ = "Integer32"
_AlarmStateLaserBias_Object = MibTableColumn
alarmStateLaserBias = _AlarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 56),
    _AlarmStateLaserBias_Type()
)
alarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateLaserBias.setStatus("mandatory")


class _LabelTecCurrent_Type(DisplayString):
    """Custom type labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTecCurrent_Type.__name__ = "DisplayString"
_LabelTecCurrent_Object = MibTableColumn
labelTecCurrent = _LabelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 57),
    _LabelTecCurrent_Type()
)
labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTecCurrent.setStatus("optional")


class _UomTecCurrent_Type(DisplayString):
    """Custom type uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomTecCurrent_Type.__name__ = "DisplayString"
_UomTecCurrent_Object = MibTableColumn
uomTecCurrent = _UomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 58),
    _UomTecCurrent_Type()
)
uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomTecCurrent.setStatus("optional")
_MajorHighTecCurrent_Type = Float
_MajorHighTecCurrent_Object = MibTableColumn
majorHighTecCurrent = _MajorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 59),
    _MajorHighTecCurrent_Type()
)
majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighTecCurrent.setStatus("mandatory")
_MajorLowTecCurrent_Type = Float
_MajorLowTecCurrent_Object = MibTableColumn
majorLowTecCurrent = _MajorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 60),
    _MajorLowTecCurrent_Type()
)
majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowTecCurrent.setStatus("mandatory")
_MinorHighTecCurrent_Type = Float
_MinorHighTecCurrent_Object = MibTableColumn
minorHighTecCurrent = _MinorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 61),
    _MinorHighTecCurrent_Type()
)
minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighTecCurrent.setStatus("mandatory")
_MinorLowTecCurrent_Type = Float
_MinorLowTecCurrent_Object = MibTableColumn
minorLowTecCurrent = _MinorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 62),
    _MinorLowTecCurrent_Type()
)
minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowTecCurrent.setStatus("mandatory")
_CurrentValueTecCurrent_Type = Float
_CurrentValueTecCurrent_Object = MibTableColumn
currentValueTecCurrent = _CurrentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 63),
    _CurrentValueTecCurrent_Type()
)
currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueTecCurrent.setStatus("mandatory")


class _StateFlagTecCurrent_Type(Integer32):
    """Custom type stateFlagTecCurrent based on Integer32"""
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


_StateFlagTecCurrent_Type.__name__ = "Integer32"
_StateFlagTecCurrent_Object = MibTableColumn
stateFlagTecCurrent = _StateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 64),
    _StateFlagTecCurrent_Type()
)
stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagTecCurrent.setStatus("mandatory")
_MinValueTecCurrent_Type = Float
_MinValueTecCurrent_Object = MibTableColumn
minValueTecCurrent = _MinValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 65),
    _MinValueTecCurrent_Type()
)
minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueTecCurrent.setStatus("mandatory")
_MaxValueTecCurrent_Type = Float
_MaxValueTecCurrent_Object = MibTableColumn
maxValueTecCurrent = _MaxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 66),
    _MaxValueTecCurrent_Type()
)
maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueTecCurrent.setStatus("mandatory")


class _AlarmStateTecCurrent_Type(Integer32):
    """Custom type alarmStateTecCurrent based on Integer32"""
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


_AlarmStateTecCurrent_Type.__name__ = "Integer32"
_AlarmStateTecCurrent_Object = MibTableColumn
alarmStateTecCurrent = _AlarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 67),
    _AlarmStateTecCurrent_Type()
)
alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateTecCurrent.setStatus("mandatory")


class _LabelLaserTemp_Type(DisplayString):
    """Custom type labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLaserTemp_Type.__name__ = "DisplayString"
_LabelLaserTemp_Object = MibTableColumn
labelLaserTemp = _LabelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 68),
    _LabelLaserTemp_Type()
)
labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLaserTemp.setStatus("optional")


class _UomLaserTemp_Type(DisplayString):
    """Custom type uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomLaserTemp_Type.__name__ = "DisplayString"
_UomLaserTemp_Object = MibTableColumn
uomLaserTemp = _UomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 69),
    _UomLaserTemp_Type()
)
uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomLaserTemp.setStatus("optional")
_MajorHighLaserTemp_Type = Float
_MajorHighLaserTemp_Object = MibTableColumn
majorHighLaserTemp = _MajorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 70),
    _MajorHighLaserTemp_Type()
)
majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighLaserTemp.setStatus("mandatory")
_MajorLowLaserTemp_Type = Float
_MajorLowLaserTemp_Object = MibTableColumn
majorLowLaserTemp = _MajorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 71),
    _MajorLowLaserTemp_Type()
)
majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowLaserTemp.setStatus("mandatory")
_MinorHighLaserTemp_Type = Float
_MinorHighLaserTemp_Object = MibTableColumn
minorHighLaserTemp = _MinorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 72),
    _MinorHighLaserTemp_Type()
)
minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighLaserTemp.setStatus("mandatory")
_MinorLowLaserTemp_Type = Float
_MinorLowLaserTemp_Object = MibTableColumn
minorLowLaserTemp = _MinorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 73),
    _MinorLowLaserTemp_Type()
)
minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowLaserTemp.setStatus("mandatory")
_CurrentValueLaserTemp_Type = Float
_CurrentValueLaserTemp_Object = MibTableColumn
currentValueLaserTemp = _CurrentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 74),
    _CurrentValueLaserTemp_Type()
)
currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueLaserTemp.setStatus("mandatory")


class _StateFlagLaserTemp_Type(Integer32):
    """Custom type stateFlagLaserTemp based on Integer32"""
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


_StateFlagLaserTemp_Type.__name__ = "Integer32"
_StateFlagLaserTemp_Object = MibTableColumn
stateFlagLaserTemp = _StateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 75),
    _StateFlagLaserTemp_Type()
)
stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagLaserTemp.setStatus("mandatory")
_MinValueLaserTemp_Type = Float
_MinValueLaserTemp_Object = MibTableColumn
minValueLaserTemp = _MinValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 76),
    _MinValueLaserTemp_Type()
)
minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueLaserTemp.setStatus("mandatory")
_MaxValueLaserTemp_Type = Float
_MaxValueLaserTemp_Object = MibTableColumn
maxValueLaserTemp = _MaxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 77),
    _MaxValueLaserTemp_Type()
)
maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueLaserTemp.setStatus("mandatory")


class _AlarmStateLaserTemp_Type(Integer32):
    """Custom type alarmStateLaserTemp based on Integer32"""
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


_AlarmStateLaserTemp_Type.__name__ = "Integer32"
_AlarmStateLaserTemp_Object = MibTableColumn
alarmStateLaserTemp = _AlarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 78),
    _AlarmStateLaserTemp_Type()
)
alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateLaserTemp.setStatus("mandatory")


class _LabelModuleTemp_Type(DisplayString):
    """Custom type labelModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelModuleTemp_Type.__name__ = "DisplayString"
_LabelModuleTemp_Object = MibTableColumn
labelModuleTemp = _LabelModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 79),
    _LabelModuleTemp_Type()
)
labelModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelModuleTemp.setStatus("optional")


class _UomModuleTemp_Type(DisplayString):
    """Custom type uomModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomModuleTemp_Type.__name__ = "DisplayString"
_UomModuleTemp_Object = MibTableColumn
uomModuleTemp = _UomModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 80),
    _UomModuleTemp_Type()
)
uomModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomModuleTemp.setStatus("optional")
_MajorHighModuleTemp_Type = Float
_MajorHighModuleTemp_Object = MibTableColumn
majorHighModuleTemp = _MajorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 81),
    _MajorHighModuleTemp_Type()
)
majorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighModuleTemp.setStatus("mandatory")
_MajorLowModuleTemp_Type = Float
_MajorLowModuleTemp_Object = MibTableColumn
majorLowModuleTemp = _MajorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 82),
    _MajorLowModuleTemp_Type()
)
majorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowModuleTemp.setStatus("mandatory")
_MinorHighModuleTemp_Type = Float
_MinorHighModuleTemp_Object = MibTableColumn
minorHighModuleTemp = _MinorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 83),
    _MinorHighModuleTemp_Type()
)
minorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighModuleTemp.setStatus("mandatory")
_MinorLowModuleTemp_Type = Float
_MinorLowModuleTemp_Object = MibTableColumn
minorLowModuleTemp = _MinorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 84),
    _MinorLowModuleTemp_Type()
)
minorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowModuleTemp.setStatus("mandatory")
_CurrentValueModuleTemp_Type = Float
_CurrentValueModuleTemp_Object = MibTableColumn
currentValueModuleTemp = _CurrentValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 85),
    _CurrentValueModuleTemp_Type()
)
currentValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueModuleTemp.setStatus("mandatory")


class _StateFlagModuleTemp_Type(Integer32):
    """Custom type stateFlagModuleTemp based on Integer32"""
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


_StateFlagModuleTemp_Type.__name__ = "Integer32"
_StateFlagModuleTemp_Object = MibTableColumn
stateFlagModuleTemp = _StateFlagModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 86),
    _StateFlagModuleTemp_Type()
)
stateFlagModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagModuleTemp.setStatus("mandatory")
_MinValueModuleTemp_Type = Float
_MinValueModuleTemp_Object = MibTableColumn
minValueModuleTemp = _MinValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 87),
    _MinValueModuleTemp_Type()
)
minValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueModuleTemp.setStatus("mandatory")
_MaxValueModuleTemp_Type = Float
_MaxValueModuleTemp_Object = MibTableColumn
maxValueModuleTemp = _MaxValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 88),
    _MaxValueModuleTemp_Type()
)
maxValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueModuleTemp.setStatus("mandatory")


class _AlarmStateModuleTemp_Type(Integer32):
    """Custom type alarmStateModuleTemp based on Integer32"""
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


_AlarmStateModuleTemp_Type.__name__ = "Integer32"
_AlarmStateModuleTemp_Object = MibTableColumn
alarmStateModuleTemp = _AlarmStateModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 89),
    _AlarmStateModuleTemp_Type()
)
alarmStateModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateModuleTemp.setStatus("mandatory")


class _LabelFanCurrent_Type(DisplayString):
    """Custom type labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFanCurrent_Type.__name__ = "DisplayString"
_LabelFanCurrent_Object = MibTableColumn
labelFanCurrent = _LabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 90),
    _LabelFanCurrent_Type()
)
labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFanCurrent.setStatus("optional")


class _UomFanCurrent_Type(DisplayString):
    """Custom type uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomFanCurrent_Type.__name__ = "DisplayString"
_UomFanCurrent_Object = MibTableColumn
uomFanCurrent = _UomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 91),
    _UomFanCurrent_Type()
)
uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomFanCurrent.setStatus("optional")
_MajorHighFanCurrent_Type = Float
_MajorHighFanCurrent_Object = MibTableColumn
majorHighFanCurrent = _MajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 92),
    _MajorHighFanCurrent_Type()
)
majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighFanCurrent.setStatus("mandatory")
_MajorLowFanCurrent_Type = Float
_MajorLowFanCurrent_Object = MibTableColumn
majorLowFanCurrent = _MajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 93),
    _MajorLowFanCurrent_Type()
)
majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowFanCurrent.setStatus("mandatory")
_MinorHighFanCurrent_Type = Float
_MinorHighFanCurrent_Object = MibTableColumn
minorHighFanCurrent = _MinorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 94),
    _MinorHighFanCurrent_Type()
)
minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighFanCurrent.setStatus("mandatory")
_MinorLowFanCurrent_Type = Float
_MinorLowFanCurrent_Object = MibTableColumn
minorLowFanCurrent = _MinorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 95),
    _MinorLowFanCurrent_Type()
)
minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowFanCurrent.setStatus("mandatory")
_CurrentValueFanCurrent_Type = Float
_CurrentValueFanCurrent_Object = MibTableColumn
currentValueFanCurrent = _CurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 96),
    _CurrentValueFanCurrent_Type()
)
currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueFanCurrent.setStatus("mandatory")


class _StateFlagFanCurrent_Type(Integer32):
    """Custom type stateFlagFanCurrent based on Integer32"""
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


_StateFlagFanCurrent_Type.__name__ = "Integer32"
_StateFlagFanCurrent_Object = MibTableColumn
stateFlagFanCurrent = _StateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 97),
    _StateFlagFanCurrent_Type()
)
stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagFanCurrent.setStatus("mandatory")
_MinValueFanCurrent_Type = Float
_MinValueFanCurrent_Object = MibTableColumn
minValueFanCurrent = _MinValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 98),
    _MinValueFanCurrent_Type()
)
minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueFanCurrent.setStatus("mandatory")
_MaxValueFanCurrent_Type = Float
_MaxValueFanCurrent_Object = MibTableColumn
maxValueFanCurrent = _MaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 99),
    _MaxValueFanCurrent_Type()
)
maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueFanCurrent.setStatus("mandatory")


class _AlarmStateFanCurrent_Type(Integer32):
    """Custom type alarmStateFanCurrent based on Integer32"""
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


_AlarmStateFanCurrent_Type.__name__ = "Integer32"
_AlarmStateFanCurrent_Object = MibTableColumn
alarmStateFanCurrent = _AlarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 100),
    _AlarmStateFanCurrent_Type()
)
alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateFanCurrent.setStatus("mandatory")


class _Label12Volt_Type(DisplayString):
    """Custom type label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Label12Volt_Type.__name__ = "DisplayString"
_Label12Volt_Object = MibTableColumn
label12Volt = _Label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 101),
    _Label12Volt_Type()
)
label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    label12Volt.setStatus("optional")


class _Uom12Volt_Type(DisplayString):
    """Custom type uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Uom12Volt_Type.__name__ = "DisplayString"
_Uom12Volt_Object = MibTableColumn
uom12Volt = _Uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 102),
    _Uom12Volt_Type()
)
uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uom12Volt.setStatus("optional")
_MajorHigh12Volt_Type = Float
_MajorHigh12Volt_Object = MibTableColumn
majorHigh12Volt = _MajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 103),
    _MajorHigh12Volt_Type()
)
majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHigh12Volt.setStatus("mandatory")
_MajorLow12Volt_Type = Float
_MajorLow12Volt_Object = MibTableColumn
majorLow12Volt = _MajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 104),
    _MajorLow12Volt_Type()
)
majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLow12Volt.setStatus("mandatory")
_MinorHigh12Volt_Type = Float
_MinorHigh12Volt_Object = MibTableColumn
minorHigh12Volt = _MinorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 105),
    _MinorHigh12Volt_Type()
)
minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHigh12Volt.setStatus("mandatory")
_MinorLow12Volt_Type = Float
_MinorLow12Volt_Object = MibTableColumn
minorLow12Volt = _MinorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 106),
    _MinorLow12Volt_Type()
)
minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLow12Volt.setStatus("mandatory")
_CurrentValue12Volt_Type = Float
_CurrentValue12Volt_Object = MibTableColumn
currentValue12Volt = _CurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 107),
    _CurrentValue12Volt_Type()
)
currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValue12Volt.setStatus("mandatory")


class _StateFlag12Volt_Type(Integer32):
    """Custom type stateFlag12Volt based on Integer32"""
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


_StateFlag12Volt_Type.__name__ = "Integer32"
_StateFlag12Volt_Object = MibTableColumn
stateFlag12Volt = _StateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 108),
    _StateFlag12Volt_Type()
)
stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlag12Volt.setStatus("mandatory")
_MinValue12Volt_Type = Float
_MinValue12Volt_Object = MibTableColumn
minValue12Volt = _MinValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 109),
    _MinValue12Volt_Type()
)
minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValue12Volt.setStatus("mandatory")
_MaxValue12Volt_Type = Float
_MaxValue12Volt_Object = MibTableColumn
maxValue12Volt = _MaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 110),
    _MaxValue12Volt_Type()
)
maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValue12Volt.setStatus("mandatory")


class _AlarmState12Volt_Type(Integer32):
    """Custom type alarmState12Volt based on Integer32"""
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


_AlarmState12Volt_Type.__name__ = "Integer32"
_AlarmState12Volt_Object = MibTableColumn
alarmState12Volt = _AlarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 2, 1, 111),
    _AlarmState12Volt_Type()
)
alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState12Volt.setStatus("mandatory")
_Gx2emDigitalTable_Object = MibTable
gx2emDigitalTable = _Gx2emDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3)
)
if mibBuilder.loadTexts:
    gx2emDigitalTable.setStatus("mandatory")
_Gx2emDigitalEntry_Object = MibTableRow
gx2emDigitalEntry = _Gx2emDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2)
)
gx2emDigitalEntry.setIndexNames(
    (0, "OMNI-gx2EM-MIB", "gx2emDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2emDigitalEntry.setStatus("mandatory")


class _Gx2emDigitalTableIndex_Type(Integer32):
    """Custom type gx2emDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2emDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2emDigitalTableIndex_Object = MibTableColumn
gx2emDigitalTableIndex = _Gx2emDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 1),
    _Gx2emDigitalTableIndex_Type()
)
gx2emDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2emDigitalTableIndex.setStatus("mandatory")


class _LabelRfInput_Type(DisplayString):
    """Custom type labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelRfInput_Type.__name__ = "DisplayString"
_LabelRfInput_Object = MibTableColumn
labelRfInput = _LabelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 2),
    _LabelRfInput_Type()
)
labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelRfInput.setStatus("optional")


class _EnumRfInput_Type(DisplayString):
    """Custom type enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumRfInput_Type.__name__ = "DisplayString"
_EnumRfInput_Object = MibTableColumn
enumRfInput = _EnumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 3),
    _EnumRfInput_Type()
)
enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumRfInput.setStatus("optional")


class _ValueRfInput_Type(Integer32):
    """Custom type valueRfInput based on Integer32"""
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


_ValueRfInput_Type.__name__ = "Integer32"
_ValueRfInput_Object = MibTableColumn
valueRfInput = _ValueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 4),
    _ValueRfInput_Type()
)
valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueRfInput.setStatus("mandatory")


class _StateflagRfInput_Type(Integer32):
    """Custom type stateflagRfInput based on Integer32"""
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


_StateflagRfInput_Type.__name__ = "Integer32"
_StateflagRfInput_Object = MibTableColumn
stateflagRfInput = _StateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 5),
    _StateflagRfInput_Type()
)
stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagRfInput.setStatus("mandatory")


class _LabelOptOutput_Type(DisplayString):
    """Custom type labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelOptOutput_Type.__name__ = "DisplayString"
_LabelOptOutput_Object = MibTableColumn
labelOptOutput = _LabelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 6),
    _LabelOptOutput_Type()
)
labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelOptOutput.setStatus("optional")


class _EnumOptOutput_Type(DisplayString):
    """Custom type enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumOptOutput_Type.__name__ = "DisplayString"
_EnumOptOutput_Object = MibTableColumn
enumOptOutput = _EnumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 7),
    _EnumOptOutput_Type()
)
enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumOptOutput.setStatus("optional")


class _ValueOptOutput_Type(Integer32):
    """Custom type valueOptOutput based on Integer32"""
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


_ValueOptOutput_Type.__name__ = "Integer32"
_ValueOptOutput_Object = MibTableColumn
valueOptOutput = _ValueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 8),
    _ValueOptOutput_Type()
)
valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueOptOutput.setStatus("mandatory")


class _StateflagOptOutput_Type(Integer32):
    """Custom type stateflagOptOutput based on Integer32"""
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


_StateflagOptOutput_Type.__name__ = "Integer32"
_StateflagOptOutput_Object = MibTableColumn
stateflagOptOutput = _StateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 9),
    _StateflagOptOutput_Type()
)
stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagOptOutput.setStatus("mandatory")


class _LabelLaserMode_Type(DisplayString):
    """Custom type labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLaserMode_Type.__name__ = "DisplayString"
_LabelLaserMode_Object = MibTableColumn
labelLaserMode = _LabelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 10),
    _LabelLaserMode_Type()
)
labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLaserMode.setStatus("optional")


class _EnumLaserMode_Type(DisplayString):
    """Custom type enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumLaserMode_Type.__name__ = "DisplayString"
_EnumLaserMode_Object = MibTableColumn
enumLaserMode = _EnumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 11),
    _EnumLaserMode_Type()
)
enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumLaserMode.setStatus("optional")


class _ValueLaserMode_Type(Integer32):
    """Custom type valueLaserMode based on Integer32"""
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


_ValueLaserMode_Type.__name__ = "Integer32"
_ValueLaserMode_Object = MibTableColumn
valueLaserMode = _ValueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 12),
    _ValueLaserMode_Type()
)
valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueLaserMode.setStatus("mandatory")


class _StateflagLaserMode_Type(Integer32):
    """Custom type stateflagLaserMode based on Integer32"""
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


_StateflagLaserMode_Type.__name__ = "Integer32"
_StateflagLaserMode_Object = MibTableColumn
stateflagLaserMode = _StateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 13),
    _StateflagLaserMode_Type()
)
stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagLaserMode.setStatus("mandatory")


class _LabelLaserSecMode_Type(DisplayString):
    """Custom type labelLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLaserSecMode_Type.__name__ = "DisplayString"
_LabelLaserSecMode_Object = MibTableColumn
labelLaserSecMode = _LabelLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 14),
    _LabelLaserSecMode_Type()
)
labelLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLaserSecMode.setStatus("optional")


class _EnumLaserSecMode_Type(DisplayString):
    """Custom type enumLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumLaserSecMode_Type.__name__ = "DisplayString"
_EnumLaserSecMode_Object = MibTableColumn
enumLaserSecMode = _EnumLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 15),
    _EnumLaserSecMode_Type()
)
enumLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumLaserSecMode.setStatus("optional")


class _ValueLaserSecMode_Type(Integer32):
    """Custom type valueLaserSecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw", 1),
          ("video", 2))
    )


_ValueLaserSecMode_Type.__name__ = "Integer32"
_ValueLaserSecMode_Object = MibTableColumn
valueLaserSecMode = _ValueLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 16),
    _ValueLaserSecMode_Type()
)
valueLaserSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueLaserSecMode.setStatus("mandatory")


class _StateflagLaserSecMode_Type(Integer32):
    """Custom type stateflagLaserSecMode based on Integer32"""
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


_StateflagLaserSecMode_Type.__name__ = "Integer32"
_StateflagLaserSecMode_Object = MibTableColumn
stateflagLaserSecMode = _StateflagLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 17),
    _StateflagLaserSecMode_Type()
)
stateflagLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagLaserSecMode.setStatus("mandatory")


class _LabelVideoOffset_Type(DisplayString):
    """Custom type labelVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelVideoOffset_Type.__name__ = "DisplayString"
_LabelVideoOffset_Object = MibTableColumn
labelVideoOffset = _LabelVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 18),
    _LabelVideoOffset_Type()
)
labelVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelVideoOffset.setStatus("optional")


class _EnumVideoOffset_Type(DisplayString):
    """Custom type enumVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumVideoOffset_Type.__name__ = "DisplayString"
_EnumVideoOffset_Object = MibTableColumn
enumVideoOffset = _EnumVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 19),
    _EnumVideoOffset_Type()
)
enumVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumVideoOffset.setStatus("optional")


class _ValueVideoOffset_Type(Integer32):
    """Custom type valueVideoOffset based on Integer32"""
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
        *(("minus2dB", 1),
          ("minus3dB", 2),
          ("minus4dB", 3),
          ("minus5dB", 4))
    )


_ValueVideoOffset_Type.__name__ = "Integer32"
_ValueVideoOffset_Object = MibTableColumn
valueVideoOffset = _ValueVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 20),
    _ValueVideoOffset_Type()
)
valueVideoOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueVideoOffset.setStatus("mandatory")


class _StateflagVideoOffset_Type(Integer32):
    """Custom type stateflagVideoOffset based on Integer32"""
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


_StateflagVideoOffset_Type.__name__ = "Integer32"
_StateflagVideoOffset_Object = MibTableColumn
stateflagVideoOffset = _StateflagVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 21),
    _StateflagVideoOffset_Type()
)
stateflagVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagVideoOffset.setStatus("mandatory")


class _LabelFactoryDefault_Type(DisplayString):
    """Custom type labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFactoryDefault_Type.__name__ = "DisplayString"
_LabelFactoryDefault_Object = MibTableColumn
labelFactoryDefault = _LabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 22),
    _LabelFactoryDefault_Type()
)
labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFactoryDefault.setStatus("optional")


class _EnumFactoryDefault_Type(DisplayString):
    """Custom type enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumFactoryDefault_Type.__name__ = "DisplayString"
_EnumFactoryDefault_Object = MibTableColumn
enumFactoryDefault = _EnumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 23),
    _EnumFactoryDefault_Type()
)
enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumFactoryDefault.setStatus("optional")


class _ValueFactoryDefault_Type(Integer32):
    """Custom type valueFactoryDefault based on Integer32"""
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


_ValueFactoryDefault_Type.__name__ = "Integer32"
_ValueFactoryDefault_Object = MibTableColumn
valueFactoryDefault = _ValueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 24),
    _ValueFactoryDefault_Type()
)
valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueFactoryDefault.setStatus("mandatory")


class _StateflagFactoryDefault_Type(Integer32):
    """Custom type stateflagFactoryDefault based on Integer32"""
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


_StateflagFactoryDefault_Type.__name__ = "Integer32"
_StateflagFactoryDefault_Object = MibTableColumn
stateflagFactoryDefault = _StateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 3, 2, 25),
    _StateflagFactoryDefault_Type()
)
stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagFactoryDefault.setStatus("mandatory")
_Gx2emStatusTable_Object = MibTable
gx2emStatusTable = _Gx2emStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4)
)
if mibBuilder.loadTexts:
    gx2emStatusTable.setStatus("mandatory")
_Gx2emStatusEntry_Object = MibTableRow
gx2emStatusEntry = _Gx2emStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3)
)
gx2emStatusEntry.setIndexNames(
    (0, "OMNI-gx2EM-MIB", "gx2emStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2emStatusEntry.setStatus("mandatory")


class _Gx2emStatusTableIndex_Type(Integer32):
    """Custom type gx2emStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2emStatusTableIndex_Type.__name__ = "Integer32"
_Gx2emStatusTableIndex_Object = MibTableColumn
gx2emStatusTableIndex = _Gx2emStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 1),
    _Gx2emStatusTableIndex_Type()
)
gx2emStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2emStatusTableIndex.setStatus("mandatory")


class _LabelBoot_Type(DisplayString):
    """Custom type labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelBoot_Type.__name__ = "DisplayString"
_LabelBoot_Object = MibTableColumn
labelBoot = _LabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 2),
    _LabelBoot_Type()
)
labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelBoot.setStatus("optional")


class _ValueBoot_Type(Integer32):
    """Custom type valueBoot based on Integer32"""
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


_ValueBoot_Type.__name__ = "Integer32"
_ValueBoot_Object = MibTableColumn
valueBoot = _ValueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 3),
    _ValueBoot_Type()
)
valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueBoot.setStatus("mandatory")


class _StateflagBoot_Type(Integer32):
    """Custom type stateflagBoot based on Integer32"""
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


_StateflagBoot_Type.__name__ = "Integer32"
_StateflagBoot_Object = MibTableColumn
stateflagBoot = _StateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 4),
    _StateflagBoot_Type()
)
stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagBoot.setStatus("mandatory")


class _LabelFlash_Type(DisplayString):
    """Custom type labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFlash_Type.__name__ = "DisplayString"
_LabelFlash_Object = MibTableColumn
labelFlash = _LabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 5),
    _LabelFlash_Type()
)
labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFlash.setStatus("optional")


class _ValueFlash_Type(Integer32):
    """Custom type valueFlash based on Integer32"""
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


_ValueFlash_Type.__name__ = "Integer32"
_ValueFlash_Object = MibTableColumn
valueFlash = _ValueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 6),
    _ValueFlash_Type()
)
valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueFlash.setStatus("mandatory")


class _StateflagFlash_Type(Integer32):
    """Custom type stateflagFlash based on Integer32"""
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


_StateflagFlash_Type.__name__ = "Integer32"
_StateflagFlash_Object = MibTableColumn
stateflagFlash = _StateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 7),
    _StateflagFlash_Type()
)
stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagFlash.setStatus("mandatory")


class _LabelFactoryDataCRC_Type(DisplayString):
    """Custom type labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFactoryDataCRC_Type.__name__ = "DisplayString"
_LabelFactoryDataCRC_Object = MibTableColumn
labelFactoryDataCRC = _LabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 8),
    _LabelFactoryDataCRC_Type()
)
labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFactoryDataCRC.setStatus("optional")


class _ValueFactoryDataCRC_Type(Integer32):
    """Custom type valueFactoryDataCRC based on Integer32"""
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


_ValueFactoryDataCRC_Type.__name__ = "Integer32"
_ValueFactoryDataCRC_Object = MibTableColumn
valueFactoryDataCRC = _ValueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 9),
    _ValueFactoryDataCRC_Type()
)
valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueFactoryDataCRC.setStatus("mandatory")


class _StateflagFactoryDataCRC_Type(Integer32):
    """Custom type stateflagFactoryDataCRC based on Integer32"""
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


_StateflagFactoryDataCRC_Type.__name__ = "Integer32"
_StateflagFactoryDataCRC_Object = MibTableColumn
stateflagFactoryDataCRC = _StateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 10),
    _StateflagFactoryDataCRC_Type()
)
stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagFactoryDataCRC.setStatus("mandatory")


class _LabelLaserDataCRC_Type(DisplayString):
    """Custom type labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLaserDataCRC_Type.__name__ = "DisplayString"
_LabelLaserDataCRC_Object = MibTableColumn
labelLaserDataCRC = _LabelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 11),
    _LabelLaserDataCRC_Type()
)
labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLaserDataCRC.setStatus("optional")


class _ValueLaserDataCRC_Type(Integer32):
    """Custom type valueLaserDataCRC based on Integer32"""
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


_ValueLaserDataCRC_Type.__name__ = "Integer32"
_ValueLaserDataCRC_Object = MibTableColumn
valueLaserDataCRC = _ValueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 12),
    _ValueLaserDataCRC_Type()
)
valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueLaserDataCRC.setStatus("mandatory")


class _StateflagLaserDataCRC_Type(Integer32):
    """Custom type stateflagLaserDataCRC based on Integer32"""
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


_StateflagLaserDataCRC_Type.__name__ = "Integer32"
_StateflagLaserDataCRC_Object = MibTableColumn
stateflagLaserDataCRC = _StateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 13),
    _StateflagLaserDataCRC_Type()
)
stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagLaserDataCRC.setStatus("mandatory")


class _LabelAlarmDataCrc_Type(DisplayString):
    """Custom type labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelAlarmDataCrc_Type.__name__ = "DisplayString"
_LabelAlarmDataCrc_Object = MibTableColumn
labelAlarmDataCrc = _LabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 14),
    _LabelAlarmDataCrc_Type()
)
labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelAlarmDataCrc.setStatus("optional")


class _ValueAlarmDataCrc_Type(Integer32):
    """Custom type valueAlarmDataCrc based on Integer32"""
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


_ValueAlarmDataCrc_Type.__name__ = "Integer32"
_ValueAlarmDataCrc_Object = MibTableColumn
valueAlarmDataCrc = _ValueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 15),
    _ValueAlarmDataCrc_Type()
)
valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueAlarmDataCrc.setStatus("mandatory")


class _StateflagAlarmDataCrc_Type(Integer32):
    """Custom type stateflagAlarmDataCrc based on Integer32"""
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


_StateflagAlarmDataCrc_Type.__name__ = "Integer32"
_StateflagAlarmDataCrc_Object = MibTableColumn
stateflagAlarmDataCrc = _StateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 16),
    _StateflagAlarmDataCrc_Type()
)
stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagAlarmDataCrc.setStatus("mandatory")


class _LabelHWStatus_Type(DisplayString):
    """Custom type labelHWStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelHWStatus_Type.__name__ = "DisplayString"
_LabelHWStatus_Object = MibTableColumn
labelHWStatus = _LabelHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 17),
    _LabelHWStatus_Type()
)
labelHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelHWStatus.setStatus("optional")


class _ValueHWStatus_Type(Integer32):
    """Custom type valueHWStatus based on Integer32"""
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


_ValueHWStatus_Type.__name__ = "Integer32"
_ValueHWStatus_Object = MibTableColumn
valueHWStatus = _ValueHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 18),
    _ValueHWStatus_Type()
)
valueHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueHWStatus.setStatus("mandatory")


class _StateflagHWStatus_Type(Integer32):
    """Custom type stateflagHWStatus based on Integer32"""
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


_StateflagHWStatus_Type.__name__ = "Integer32"
_StateflagHWStatus_Object = MibTableColumn
stateflagHWStatus = _StateflagHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 19),
    _StateflagHWStatus_Type()
)
stateflagHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagHWStatus.setStatus("mandatory")


class _LabelRFInputStatus_Type(DisplayString):
    """Custom type labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelRFInputStatus_Type.__name__ = "DisplayString"
_LabelRFInputStatus_Object = MibTableColumn
labelRFInputStatus = _LabelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 20),
    _LabelRFInputStatus_Type()
)
labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelRFInputStatus.setStatus("optional")


class _ValueRFInputStatus_Type(Integer32):
    """Custom type valueRFInputStatus based on Integer32"""
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


_ValueRFInputStatus_Type.__name__ = "Integer32"
_ValueRFInputStatus_Object = MibTableColumn
valueRFInputStatus = _ValueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 21),
    _ValueRFInputStatus_Type()
)
valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueRFInputStatus.setStatus("mandatory")


class _StateflagRFInputStatus_Type(Integer32):
    """Custom type stateflagRFInputStatus based on Integer32"""
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


_StateflagRFInputStatus_Type.__name__ = "Integer32"
_StateflagRFInputStatus_Object = MibTableColumn
stateflagRFInputStatus = _StateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 4, 3, 22),
    _StateflagRFInputStatus_Type()
)
stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateflagRFInputStatus.setStatus("mandatory")
_Gx2emFactoryTable_Object = MibTable
gx2emFactoryTable = _Gx2emFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5)
)
if mibBuilder.loadTexts:
    gx2emFactoryTable.setStatus("mandatory")
_Gx2emFactoryEntry_Object = MibTableRow
gx2emFactoryEntry = _Gx2emFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4)
)
gx2emFactoryEntry.setIndexNames(
    (0, "OMNI-gx2EM-MIB", "gx2emFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2emFactoryEntry.setStatus("mandatory")


class _Gx2emFactoryTableIndex_Type(Integer32):
    """Custom type gx2emFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2emFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2emFactoryTableIndex_Object = MibTableColumn
gx2emFactoryTableIndex = _Gx2emFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 1),
    _Gx2emFactoryTableIndex_Type()
)
gx2emFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2emFactoryTableIndex.setStatus("mandatory")
_BootControlByteValue_Type = Integer32
_BootControlByteValue_Object = MibTableColumn
bootControlByteValue = _BootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 2),
    _BootControlByteValue_Type()
)
bootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootControlByteValue.setStatus("mandatory")
_BootStatusByteValue_Type = Integer32
_BootStatusByteValue_Object = MibTableColumn
bootStatusByteValue = _BootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 3),
    _BootStatusByteValue_Type()
)
bootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootStatusByteValue.setStatus("mandatory")
_Bank1CRCValue_Type = Integer32
_Bank1CRCValue_Object = MibTableColumn
bank1CRCValue = _Bank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 4),
    _Bank1CRCValue_Type()
)
bank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bank1CRCValue.setStatus("mandatory")
_Bank2CRCValue_Type = Integer32
_Bank2CRCValue_Object = MibTableColumn
bank2CRCValue = _Bank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 5),
    _Bank2CRCValue_Type()
)
bank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bank2CRCValue.setStatus("mandatory")
_PrgEEPROMByteValue_Type = Integer32
_PrgEEPROMByteValue_Object = MibTableColumn
prgEEPROMByteValue = _PrgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 6),
    _PrgEEPROMByteValue_Type()
)
prgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prgEEPROMByteValue.setStatus("mandatory")
_FactoryCRCValue_Type = Integer32
_FactoryCRCValue_Object = MibTableColumn
factoryCRCValue = _FactoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 7),
    _FactoryCRCValue_Type()
)
factoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryCRCValue.setStatus("mandatory")


class _CalculateCRCValue_Type(Integer32):
    """Custom type calculateCRCValue based on Integer32"""
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
          ("laserData", 2))
    )


_CalculateCRCValue_Type.__name__ = "Integer32"
_CalculateCRCValue_Object = MibTableColumn
calculateCRCValue = _CalculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 8),
    _CalculateCRCValue_Type()
)
calculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calculateCRCValue.setStatus("mandatory")
_HourMeterValue_Type = Integer32
_HourMeterValue_Object = MibTableColumn
hourMeterValue = _HourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 9),
    _HourMeterValue_Type()
)
hourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourMeterValue.setStatus("mandatory")
_FlashPrgCntAValue_Type = Integer32
_FlashPrgCntAValue_Object = MibTableColumn
flashPrgCntAValue = _FlashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 10),
    _FlashPrgCntAValue_Type()
)
flashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPrgCntAValue.setStatus("mandatory")
_FlashPrgCntBValue_Type = Integer32
_FlashPrgCntBValue_Object = MibTableColumn
flashPrgCntBValue = _FlashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 11),
    _FlashPrgCntBValue_Type()
)
flashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPrgCntBValue.setStatus("mandatory")


class _FlashBankARevValue_Type(DisplayString):
    """Custom type flashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FlashBankARevValue_Type.__name__ = "DisplayString"
_FlashBankARevValue_Object = MibTableColumn
flashBankARevValue = _FlashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 12),
    _FlashBankARevValue_Type()
)
flashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashBankARevValue.setStatus("mandatory")


class _FlashBankBRevValue_Type(DisplayString):
    """Custom type flashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FlashBankBRevValue_Type.__name__ = "DisplayString"
_FlashBankBRevValue_Object = MibTableColumn
flashBankBRevValue = _FlashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 5, 4, 13),
    _FlashBankBRevValue_Type()
)
flashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashBankBRevValue.setStatus("mandatory")
_Gx2Em1000HoldTimeTable_Object = MibTable
gx2Em1000HoldTimeTable = _Gx2Em1000HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 6)
)
if mibBuilder.loadTexts:
    gx2Em1000HoldTimeTable.setStatus("mandatory")
_Gx2Em1000HoldTimeEntry_Object = MibTableRow
gx2Em1000HoldTimeEntry = _Gx2Em1000HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 6, 5)
)
gx2Em1000HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2EM-MIB", "gx2Em1000HoldTimeTableIndex"),
    (0, "OMNI-gx2EM-MIB", "gx2Em1000HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Em1000HoldTimeEntry.setStatus("mandatory")


class _Gx2Em1000HoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Em1000HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em1000HoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Em1000HoldTimeTableIndex_Object = MibTableColumn
gx2Em1000HoldTimeTableIndex = _Gx2Em1000HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 6, 5, 1),
    _Gx2Em1000HoldTimeTableIndex_Type()
)
gx2Em1000HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em1000HoldTimeTableIndex.setStatus("mandatory")


class _Gx2Em1000HoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Em1000HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em1000HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Em1000HoldTimeSpecIndex_Object = MibTableColumn
gx2Em1000HoldTimeSpecIndex = _Gx2Em1000HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 6, 5, 2),
    _Gx2Em1000HoldTimeSpecIndex_Type()
)
gx2Em1000HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em1000HoldTimeSpecIndex.setStatus("mandatory")
_Gx2Em1000HoldTimeData_Type = Integer32
_Gx2Em1000HoldTimeData_Object = MibTableColumn
gx2Em1000HoldTimeData = _Gx2Em1000HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 6, 5, 3),
    _Gx2Em1000HoldTimeData_Type()
)
gx2Em1000HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Em1000HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapEMConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 1)
)
trapEMConfigChangeInteger.setObjects(
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
    trapEMConfigChangeInteger.setStatus(
        ""
    )

trapEMConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 2)
)
trapEMConfigChangeDisplayString.setObjects(
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
    trapEMConfigChangeDisplayString.setStatus(
        ""
    )

trapEMRFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 3)
)
trapEMRFInputAlarm.setObjects(
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
    trapEMRFInputAlarm.setStatus(
        ""
    )

trapEMRFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 4)
)
trapEMRFOverloadAlarm.setObjects(
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
    trapEMRFOverloadAlarm.setStatus(
        ""
    )

trapEMRFOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 5)
)
trapEMRFOffsetAlarm.setObjects(
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
    trapEMRFOffsetAlarm.setStatus(
        ""
    )

trapEMOpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 6)
)
trapEMOpticalPowerAlarm.setObjects(
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
    trapEMOpticalPowerAlarm.setStatus(
        ""
    )

trapEMLaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 7)
)
trapEMLaserBiasAlarm.setObjects(
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
    trapEMLaserBiasAlarm.setStatus(
        ""
    )

trapEMLaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 8)
)
trapEMLaserTempAlarm.setObjects(
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
    trapEMLaserTempAlarm.setStatus(
        ""
    )

trapEMTECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 9)
)
trapEMTECCurrentAlarm.setObjects(
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
    trapEMTECCurrentAlarm.setStatus(
        ""
    )

trapEMFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 10)
)
trapEMFanCurrentAlarm.setObjects(
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
    trapEMFanCurrentAlarm.setStatus(
        ""
    )

trapEM12vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 11)
)
trapEM12vAlarm.setObjects(
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
    trapEM12vAlarm.setStatus(
        ""
    )

trapEMModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 12)
)
trapEMModuleTempAlarm.setObjects(
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
    trapEMModuleTempAlarm.setStatus(
        ""
    )

trapEMFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 13)
)
trapEMFlashAlarm.setObjects(
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
    trapEMFlashAlarm.setStatus(
        ""
    )

trapEMLaserBiasCntLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 14)
)
trapEMLaserBiasCntLoopAlarm.setObjects(
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
    trapEMLaserBiasCntLoopAlarm.setStatus(
        ""
    )

trapEMBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 15)
)
trapEMBankBootAlarm.setObjects(
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
    trapEMBankBootAlarm.setStatus(
        ""
    )

trapEMLaserBiasCntLoopInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 16)
)
trapEMLaserBiasCntLoopInitAlarm.setObjects(
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
    trapEMLaserBiasCntLoopInitAlarm.setStatus(
        ""
    )

trapEMRFParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 17)
)
trapEMRFParamInitAlarm.setObjects(
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
    trapEMRFParamInitAlarm.setStatus(
        ""
    )

trapEMTECParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 18)
)
trapEMTECParamInitAlarm.setObjects(
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
    trapEMTECParamInitAlarm.setStatus(
        ""
    )

trapEMAttnTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 19)
)
trapEMAttnTableInitAlarm.setObjects(
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
    trapEMAttnTableInitAlarm.setStatus(
        ""
    )

trapEMPowerMeterTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 20)
)
trapEMPowerMeterTableInitAlarm.setObjects(
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
    trapEMPowerMeterTableInitAlarm.setStatus(
        ""
    )

trapEMLaserDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 21)
)
trapEMLaserDataCRCAlarm.setObjects(
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
    trapEMLaserDataCRCAlarm.setStatus(
        ""
    )

trapEMAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 22)
)
trapEMAlarmDataCRCAlarm.setObjects(
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
    trapEMAlarmDataCRCAlarm.setStatus(
        ""
    )

trapEMFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 23)
)
trapEMFactoryDataCRCAlarm.setObjects(
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
    trapEMFactoryDataCRCAlarm.setStatus(
        ""
    )

trapEMUserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 24)
)
trapEMUserRFOffAlarm.setObjects(
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
    trapEMUserRFOffAlarm.setStatus(
        ""
    )

trapEMUserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 25)
)
trapEMUserOpticalOffAlarm.setObjects(
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
    trapEMUserOpticalOffAlarm.setStatus(
        ""
    )

trapEMResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30, 0, 26)
)
trapEMResetFactoryDefaultAlarm.setObjects(
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
    trapEMResetFactoryDefaultAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2EM-MIB",
    **{"Float": Float,
       "trapEMConfigChangeInteger": trapEMConfigChangeInteger,
       "trapEMConfigChangeDisplayString": trapEMConfigChangeDisplayString,
       "trapEMRFInputAlarm": trapEMRFInputAlarm,
       "trapEMRFOverloadAlarm": trapEMRFOverloadAlarm,
       "trapEMRFOffsetAlarm": trapEMRFOffsetAlarm,
       "trapEMOpticalPowerAlarm": trapEMOpticalPowerAlarm,
       "trapEMLaserBiasAlarm": trapEMLaserBiasAlarm,
       "trapEMLaserTempAlarm": trapEMLaserTempAlarm,
       "trapEMTECCurrentAlarm": trapEMTECCurrentAlarm,
       "trapEMFanCurrentAlarm": trapEMFanCurrentAlarm,
       "trapEM12vAlarm": trapEM12vAlarm,
       "trapEMModuleTempAlarm": trapEMModuleTempAlarm,
       "trapEMFlashAlarm": trapEMFlashAlarm,
       "trapEMLaserBiasCntLoopAlarm": trapEMLaserBiasCntLoopAlarm,
       "trapEMBankBootAlarm": trapEMBankBootAlarm,
       "trapEMLaserBiasCntLoopInitAlarm": trapEMLaserBiasCntLoopInitAlarm,
       "trapEMRFParamInitAlarm": trapEMRFParamInitAlarm,
       "trapEMTECParamInitAlarm": trapEMTECParamInitAlarm,
       "trapEMAttnTableInitAlarm": trapEMAttnTableInitAlarm,
       "trapEMPowerMeterTableInitAlarm": trapEMPowerMeterTableInitAlarm,
       "trapEMLaserDataCRCAlarm": trapEMLaserDataCRCAlarm,
       "trapEMAlarmDataCRCAlarm": trapEMAlarmDataCRCAlarm,
       "trapEMFactoryDataCRCAlarm": trapEMFactoryDataCRCAlarm,
       "trapEMUserRFOffAlarm": trapEMUserRFOffAlarm,
       "trapEMUserOpticalOffAlarm": trapEMUserOpticalOffAlarm,
       "trapEMResetFactoryDefaultAlarm": trapEMResetFactoryDefaultAlarm,
       "gx2emDescriptor": gx2emDescriptor,
       "gx2emAnalogTable": gx2emAnalogTable,
       "gx2emAnalogEntry": gx2emAnalogEntry,
       "gx2emAnalogTableIndex": gx2emAnalogTableIndex,
       "labelOffsetNomMonitor": labelOffsetNomMonitor,
       "uomOffsetNomMonitor": uomOffsetNomMonitor,
       "majorHighOffsetNomMonitor": majorHighOffsetNomMonitor,
       "majorLowOffsetNomMonitor": majorLowOffsetNomMonitor,
       "minorHighOffsetNomMonitor": minorHighOffsetNomMonitor,
       "minorLowOffsetNomMonitor": minorLowOffsetNomMonitor,
       "currentValueOffsetNomMonitor": currentValueOffsetNomMonitor,
       "stateFlagOffsetNomMonitor": stateFlagOffsetNomMonitor,
       "minValueOffsetNomMonitor": minValueOffsetNomMonitor,
       "maxValueOffsetNomMonitor": maxValueOffsetNomMonitor,
       "alarmStateOffsetNomMonitor": alarmStateOffsetNomMonitor,
       "labelOffsetNomCnt": labelOffsetNomCnt,
       "uomOffsetNomCnt": uomOffsetNomCnt,
       "majorHighOffsetNomCnt": majorHighOffsetNomCnt,
       "majorLowOffsetNomCnt": majorLowOffsetNomCnt,
       "minorHighOffsetNomCnt": minorHighOffsetNomCnt,
       "minorLowOffsetNomCnt": minorLowOffsetNomCnt,
       "currentValueOffsetNomCnt": currentValueOffsetNomCnt,
       "stateFlagOffsetNomCnt": stateFlagOffsetNomCnt,
       "minValueOffsetNomCnt": minValueOffsetNomCnt,
       "maxValueOffsetNomCnt": maxValueOffsetNomCnt,
       "alarmStateOffsetNomCnt": alarmStateOffsetNomCnt,
       "labelRelAttenSetting": labelRelAttenSetting,
       "uomRelAttenSetting": uomRelAttenSetting,
       "majorHighRelAttenSetting": majorHighRelAttenSetting,
       "majorLowRelAttenSetting": majorLowRelAttenSetting,
       "minorHighRelAttenSetting": minorHighRelAttenSetting,
       "minorLowRelAttenSetting": minorLowRelAttenSetting,
       "currentValueRelAttenSetting": currentValueRelAttenSetting,
       "stateFlagRelAttenSetting": stateFlagRelAttenSetting,
       "minValueRelAttenSetting": minValueRelAttenSetting,
       "maxValueRelAttenSetting": maxValueRelAttenSetting,
       "alarmStateRelAttenSetting": alarmStateRelAttenSetting,
       "labelOptPower": labelOptPower,
       "uomOptPower": uomOptPower,
       "majorHighOptPower": majorHighOptPower,
       "majorLowOptPower": majorLowOptPower,
       "minorHighOptPower": minorHighOptPower,
       "minorLowOptPower": minorLowOptPower,
       "currentValueOptPower": currentValueOptPower,
       "stateFlagOptPower": stateFlagOptPower,
       "minValueOptPower": minValueOptPower,
       "maxValueOptPower": maxValueOptPower,
       "alarmStateOptPower": alarmStateOptPower,
       "labelLaserBias": labelLaserBias,
       "uomLaserBias": uomLaserBias,
       "majorHighLaserBias": majorHighLaserBias,
       "majorLowLaserBias": majorLowLaserBias,
       "minorHighLaserBias": minorHighLaserBias,
       "minorLowLaserBias": minorLowLaserBias,
       "currentValueLaserBias": currentValueLaserBias,
       "stateFlagLaserBias": stateFlagLaserBias,
       "minValueLaserBias": minValueLaserBias,
       "maxValueLaserBias": maxValueLaserBias,
       "alarmStateLaserBias": alarmStateLaserBias,
       "labelTecCurrent": labelTecCurrent,
       "uomTecCurrent": uomTecCurrent,
       "majorHighTecCurrent": majorHighTecCurrent,
       "majorLowTecCurrent": majorLowTecCurrent,
       "minorHighTecCurrent": minorHighTecCurrent,
       "minorLowTecCurrent": minorLowTecCurrent,
       "currentValueTecCurrent": currentValueTecCurrent,
       "stateFlagTecCurrent": stateFlagTecCurrent,
       "minValueTecCurrent": minValueTecCurrent,
       "maxValueTecCurrent": maxValueTecCurrent,
       "alarmStateTecCurrent": alarmStateTecCurrent,
       "labelLaserTemp": labelLaserTemp,
       "uomLaserTemp": uomLaserTemp,
       "majorHighLaserTemp": majorHighLaserTemp,
       "majorLowLaserTemp": majorLowLaserTemp,
       "minorHighLaserTemp": minorHighLaserTemp,
       "minorLowLaserTemp": minorLowLaserTemp,
       "currentValueLaserTemp": currentValueLaserTemp,
       "stateFlagLaserTemp": stateFlagLaserTemp,
       "minValueLaserTemp": minValueLaserTemp,
       "maxValueLaserTemp": maxValueLaserTemp,
       "alarmStateLaserTemp": alarmStateLaserTemp,
       "labelModuleTemp": labelModuleTemp,
       "uomModuleTemp": uomModuleTemp,
       "majorHighModuleTemp": majorHighModuleTemp,
       "majorLowModuleTemp": majorLowModuleTemp,
       "minorHighModuleTemp": minorHighModuleTemp,
       "minorLowModuleTemp": minorLowModuleTemp,
       "currentValueModuleTemp": currentValueModuleTemp,
       "stateFlagModuleTemp": stateFlagModuleTemp,
       "minValueModuleTemp": minValueModuleTemp,
       "maxValueModuleTemp": maxValueModuleTemp,
       "alarmStateModuleTemp": alarmStateModuleTemp,
       "labelFanCurrent": labelFanCurrent,
       "uomFanCurrent": uomFanCurrent,
       "majorHighFanCurrent": majorHighFanCurrent,
       "majorLowFanCurrent": majorLowFanCurrent,
       "minorHighFanCurrent": minorHighFanCurrent,
       "minorLowFanCurrent": minorLowFanCurrent,
       "currentValueFanCurrent": currentValueFanCurrent,
       "stateFlagFanCurrent": stateFlagFanCurrent,
       "minValueFanCurrent": minValueFanCurrent,
       "maxValueFanCurrent": maxValueFanCurrent,
       "alarmStateFanCurrent": alarmStateFanCurrent,
       "label12Volt": label12Volt,
       "uom12Volt": uom12Volt,
       "majorHigh12Volt": majorHigh12Volt,
       "majorLow12Volt": majorLow12Volt,
       "minorHigh12Volt": minorHigh12Volt,
       "minorLow12Volt": minorLow12Volt,
       "currentValue12Volt": currentValue12Volt,
       "stateFlag12Volt": stateFlag12Volt,
       "minValue12Volt": minValue12Volt,
       "maxValue12Volt": maxValue12Volt,
       "alarmState12Volt": alarmState12Volt,
       "gx2emDigitalTable": gx2emDigitalTable,
       "gx2emDigitalEntry": gx2emDigitalEntry,
       "gx2emDigitalTableIndex": gx2emDigitalTableIndex,
       "labelRfInput": labelRfInput,
       "enumRfInput": enumRfInput,
       "valueRfInput": valueRfInput,
       "stateflagRfInput": stateflagRfInput,
       "labelOptOutput": labelOptOutput,
       "enumOptOutput": enumOptOutput,
       "valueOptOutput": valueOptOutput,
       "stateflagOptOutput": stateflagOptOutput,
       "labelLaserMode": labelLaserMode,
       "enumLaserMode": enumLaserMode,
       "valueLaserMode": valueLaserMode,
       "stateflagLaserMode": stateflagLaserMode,
       "labelLaserSecMode": labelLaserSecMode,
       "enumLaserSecMode": enumLaserSecMode,
       "valueLaserSecMode": valueLaserSecMode,
       "stateflagLaserSecMode": stateflagLaserSecMode,
       "labelVideoOffset": labelVideoOffset,
       "enumVideoOffset": enumVideoOffset,
       "valueVideoOffset": valueVideoOffset,
       "stateflagVideoOffset": stateflagVideoOffset,
       "labelFactoryDefault": labelFactoryDefault,
       "enumFactoryDefault": enumFactoryDefault,
       "valueFactoryDefault": valueFactoryDefault,
       "stateflagFactoryDefault": stateflagFactoryDefault,
       "gx2emStatusTable": gx2emStatusTable,
       "gx2emStatusEntry": gx2emStatusEntry,
       "gx2emStatusTableIndex": gx2emStatusTableIndex,
       "labelBoot": labelBoot,
       "valueBoot": valueBoot,
       "stateflagBoot": stateflagBoot,
       "labelFlash": labelFlash,
       "valueFlash": valueFlash,
       "stateflagFlash": stateflagFlash,
       "labelFactoryDataCRC": labelFactoryDataCRC,
       "valueFactoryDataCRC": valueFactoryDataCRC,
       "stateflagFactoryDataCRC": stateflagFactoryDataCRC,
       "labelLaserDataCRC": labelLaserDataCRC,
       "valueLaserDataCRC": valueLaserDataCRC,
       "stateflagLaserDataCRC": stateflagLaserDataCRC,
       "labelAlarmDataCrc": labelAlarmDataCrc,
       "valueAlarmDataCrc": valueAlarmDataCrc,
       "stateflagAlarmDataCrc": stateflagAlarmDataCrc,
       "labelHWStatus": labelHWStatus,
       "valueHWStatus": valueHWStatus,
       "stateflagHWStatus": stateflagHWStatus,
       "labelRFInputStatus": labelRFInputStatus,
       "valueRFInputStatus": valueRFInputStatus,
       "stateflagRFInputStatus": stateflagRFInputStatus,
       "gx2emFactoryTable": gx2emFactoryTable,
       "gx2emFactoryEntry": gx2emFactoryEntry,
       "gx2emFactoryTableIndex": gx2emFactoryTableIndex,
       "bootControlByteValue": bootControlByteValue,
       "bootStatusByteValue": bootStatusByteValue,
       "bank1CRCValue": bank1CRCValue,
       "bank2CRCValue": bank2CRCValue,
       "prgEEPROMByteValue": prgEEPROMByteValue,
       "factoryCRCValue": factoryCRCValue,
       "calculateCRCValue": calculateCRCValue,
       "hourMeterValue": hourMeterValue,
       "flashPrgCntAValue": flashPrgCntAValue,
       "flashPrgCntBValue": flashPrgCntBValue,
       "flashBankARevValue": flashBankARevValue,
       "flashBankBRevValue": flashBankBRevValue,
       "gx2Em1000HoldTimeTable": gx2Em1000HoldTimeTable,
       "gx2Em1000HoldTimeEntry": gx2Em1000HoldTimeEntry,
       "gx2Em1000HoldTimeTableIndex": gx2Em1000HoldTimeTableIndex,
       "gx2Em1000HoldTimeSpecIndex": gx2Em1000HoldTimeSpecIndex,
       "gx2Em1000HoldTimeData": gx2Em1000HoldTimeData}
)
