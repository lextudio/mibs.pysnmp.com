# SNMP MIB module (OMNI-gx2Dm1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Dm1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:15 2024
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

(gx2Dm1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Dm1000")

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

_Gx2Dm1000Descriptor_ObjectIdentity = ObjectIdentity
gx2Dm1000Descriptor = _Gx2Dm1000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 1)
)
_Gx2Dm1000AnalogTable_Object = MibTable
gx2Dm1000AnalogTable = _Gx2Dm1000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2)
)
if mibBuilder.loadTexts:
    gx2Dm1000AnalogTable.setStatus("mandatory")
_Gx2Dm1000AnalogEntry_Object = MibTableRow
gx2Dm1000AnalogEntry = _Gx2Dm1000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1)
)
gx2Dm1000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Dm1000-MIB", "gx2Dm1000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm1000AnalogEntry.setStatus("mandatory")


class _Gx2Dm1000AnalogTableIndex_Type(Integer32):
    """Custom type gx2Dm1000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm1000AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Dm1000AnalogTableIndex_Object = MibTableColumn
gx2Dm1000AnalogTableIndex = _Gx2Dm1000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 1),
    _Gx2Dm1000AnalogTableIndex_Type()
)
gx2Dm1000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm1000AnalogTableIndex.setStatus("mandatory")


class _Dm1000labelOffsetNomMonitor_Type(DisplayString):
    """Custom type dm1000labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm1000labelOffsetNomMonitor_Object = MibTableColumn
dm1000labelOffsetNomMonitor = _Dm1000labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 2),
    _Dm1000labelOffsetNomMonitor_Type()
)
dm1000labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelOffsetNomMonitor.setStatus("optional")


class _Dm1000uomOffsetNomMonitor_Type(DisplayString):
    """Custom type dm1000uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm1000uomOffsetNomMonitor_Object = MibTableColumn
dm1000uomOffsetNomMonitor = _Dm1000uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 3),
    _Dm1000uomOffsetNomMonitor_Type()
)
dm1000uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomOffsetNomMonitor.setStatus("optional")
_Dm1000majorHighOffsetNomMonitor_Type = Float
_Dm1000majorHighOffsetNomMonitor_Object = MibTableColumn
dm1000majorHighOffsetNomMonitor = _Dm1000majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 4),
    _Dm1000majorHighOffsetNomMonitor_Type()
)
dm1000majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighOffsetNomMonitor.setStatus("mandatory")
_Dm1000majorLowOffsetNomMonitor_Type = Float
_Dm1000majorLowOffsetNomMonitor_Object = MibTableColumn
dm1000majorLowOffsetNomMonitor = _Dm1000majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 5),
    _Dm1000majorLowOffsetNomMonitor_Type()
)
dm1000majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowOffsetNomMonitor.setStatus("mandatory")
_Dm1000minorHighOffsetNomMonitor_Type = Float
_Dm1000minorHighOffsetNomMonitor_Object = MibTableColumn
dm1000minorHighOffsetNomMonitor = _Dm1000minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 6),
    _Dm1000minorHighOffsetNomMonitor_Type()
)
dm1000minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighOffsetNomMonitor.setStatus("mandatory")
_Dm1000minorLowOffsetNomMonitor_Type = Float
_Dm1000minorLowOffsetNomMonitor_Object = MibTableColumn
dm1000minorLowOffsetNomMonitor = _Dm1000minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 7),
    _Dm1000minorLowOffsetNomMonitor_Type()
)
dm1000minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowOffsetNomMonitor.setStatus("mandatory")
_Dm1000currentValueOffsetNomMonitor_Type = Float
_Dm1000currentValueOffsetNomMonitor_Object = MibTableColumn
dm1000currentValueOffsetNomMonitor = _Dm1000currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 8),
    _Dm1000currentValueOffsetNomMonitor_Type()
)
dm1000currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueOffsetNomMonitor.setStatus("mandatory")


class _Dm1000stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type dm1000stateFlagOffsetNomMonitor based on Integer32"""
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


_Dm1000stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm1000stateFlagOffsetNomMonitor_Object = MibTableColumn
dm1000stateFlagOffsetNomMonitor = _Dm1000stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 9),
    _Dm1000stateFlagOffsetNomMonitor_Type()
)
dm1000stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagOffsetNomMonitor.setStatus("mandatory")
_Dm1000minValueOffsetNomMonitor_Type = Float
_Dm1000minValueOffsetNomMonitor_Object = MibTableColumn
dm1000minValueOffsetNomMonitor = _Dm1000minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 10),
    _Dm1000minValueOffsetNomMonitor_Type()
)
dm1000minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueOffsetNomMonitor.setStatus("mandatory")
_Dm1000maxValueOffsetNomMonitor_Type = Float
_Dm1000maxValueOffsetNomMonitor_Object = MibTableColumn
dm1000maxValueOffsetNomMonitor = _Dm1000maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 11),
    _Dm1000maxValueOffsetNomMonitor_Type()
)
dm1000maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueOffsetNomMonitor.setStatus("mandatory")


class _Dm1000alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type dm1000alarmStateOffsetNomMonitor based on Integer32"""
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


_Dm1000alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm1000alarmStateOffsetNomMonitor_Object = MibTableColumn
dm1000alarmStateOffsetNomMonitor = _Dm1000alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 12),
    _Dm1000alarmStateOffsetNomMonitor_Type()
)
dm1000alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Dm1000labelOffsetNomCnt_Type(DisplayString):
    """Custom type dm1000labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm1000labelOffsetNomCnt_Object = MibTableColumn
dm1000labelOffsetNomCnt = _Dm1000labelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 13),
    _Dm1000labelOffsetNomCnt_Type()
)
dm1000labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelOffsetNomCnt.setStatus("optional")


class _Dm1000uomOffsetNomCnt_Type(DisplayString):
    """Custom type dm1000uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm1000uomOffsetNomCnt_Object = MibTableColumn
dm1000uomOffsetNomCnt = _Dm1000uomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 14),
    _Dm1000uomOffsetNomCnt_Type()
)
dm1000uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomOffsetNomCnt.setStatus("optional")
_Dm1000majorHighOffsetNomCnt_Type = Float
_Dm1000majorHighOffsetNomCnt_Object = MibTableColumn
dm1000majorHighOffsetNomCnt = _Dm1000majorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 15),
    _Dm1000majorHighOffsetNomCnt_Type()
)
dm1000majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighOffsetNomCnt.setStatus("obsolete")
_Dm1000majorLowOffsetNomCnt_Type = Float
_Dm1000majorLowOffsetNomCnt_Object = MibTableColumn
dm1000majorLowOffsetNomCnt = _Dm1000majorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 16),
    _Dm1000majorLowOffsetNomCnt_Type()
)
dm1000majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowOffsetNomCnt.setStatus("obsolete")
_Dm1000minorHighOffsetNomCnt_Type = Float
_Dm1000minorHighOffsetNomCnt_Object = MibTableColumn
dm1000minorHighOffsetNomCnt = _Dm1000minorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 17),
    _Dm1000minorHighOffsetNomCnt_Type()
)
dm1000minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighOffsetNomCnt.setStatus("obsolete")
_Dm1000minorLowOffsetNomCnt_Type = Float
_Dm1000minorLowOffsetNomCnt_Object = MibTableColumn
dm1000minorLowOffsetNomCnt = _Dm1000minorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 18),
    _Dm1000minorLowOffsetNomCnt_Type()
)
dm1000minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowOffsetNomCnt.setStatus("obsolete")
_Dm1000currentValueOffsetNomCnt_Type = Float
_Dm1000currentValueOffsetNomCnt_Object = MibTableColumn
dm1000currentValueOffsetNomCnt = _Dm1000currentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 19),
    _Dm1000currentValueOffsetNomCnt_Type()
)
dm1000currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000currentValueOffsetNomCnt.setStatus("mandatory")


class _Dm1000stateFlagOffsetNomCnt_Type(Integer32):
    """Custom type dm1000stateFlagOffsetNomCnt based on Integer32"""
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


_Dm1000stateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_Dm1000stateFlagOffsetNomCnt_Object = MibTableColumn
dm1000stateFlagOffsetNomCnt = _Dm1000stateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 20),
    _Dm1000stateFlagOffsetNomCnt_Type()
)
dm1000stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagOffsetNomCnt.setStatus("mandatory")
_Dm1000minValueOffsetNomCnt_Type = Float
_Dm1000minValueOffsetNomCnt_Object = MibTableColumn
dm1000minValueOffsetNomCnt = _Dm1000minValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 21),
    _Dm1000minValueOffsetNomCnt_Type()
)
dm1000minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueOffsetNomCnt.setStatus("mandatory")
_Dm1000maxValueOffsetNomCnt_Type = Float
_Dm1000maxValueOffsetNomCnt_Object = MibTableColumn
dm1000maxValueOffsetNomCnt = _Dm1000maxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 22),
    _Dm1000maxValueOffsetNomCnt_Type()
)
dm1000maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueOffsetNomCnt.setStatus("mandatory")


class _Dm1000alarmStateOffsetNomCnt_Type(Integer32):
    """Custom type dm1000alarmStateOffsetNomCnt based on Integer32"""
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


_Dm1000alarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_Dm1000alarmStateOffsetNomCnt_Object = MibTableColumn
dm1000alarmStateOffsetNomCnt = _Dm1000alarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 23),
    _Dm1000alarmStateOffsetNomCnt_Type()
)
dm1000alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateOffsetNomCnt.setStatus("obsolete")


class _Dm1000labelAttenSetting_Type(DisplayString):
    """Custom type dm1000labelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelAttenSetting_Type.__name__ = "DisplayString"
_Dm1000labelAttenSetting_Object = MibTableColumn
dm1000labelAttenSetting = _Dm1000labelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 24),
    _Dm1000labelAttenSetting_Type()
)
dm1000labelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelAttenSetting.setStatus("optional")


class _Dm1000uomAttenSetting_Type(DisplayString):
    """Custom type dm1000uomAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomAttenSetting_Type.__name__ = "DisplayString"
_Dm1000uomAttenSetting_Object = MibTableColumn
dm1000uomAttenSetting = _Dm1000uomAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 25),
    _Dm1000uomAttenSetting_Type()
)
dm1000uomAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomAttenSetting.setStatus("optional")
_Dm1000majorHighAttenSetting_Type = Float
_Dm1000majorHighAttenSetting_Object = MibTableColumn
dm1000majorHighAttenSetting = _Dm1000majorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 26),
    _Dm1000majorHighAttenSetting_Type()
)
dm1000majorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighAttenSetting.setStatus("obsolete")
_Dm1000majorLowAttenSetting_Type = Float
_Dm1000majorLowAttenSetting_Object = MibTableColumn
dm1000majorLowAttenSetting = _Dm1000majorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 27),
    _Dm1000majorLowAttenSetting_Type()
)
dm1000majorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowAttenSetting.setStatus("obsolete")
_Dm1000minorHighAttenSetting_Type = Float
_Dm1000minorHighAttenSetting_Object = MibTableColumn
dm1000minorHighAttenSetting = _Dm1000minorHighAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 28),
    _Dm1000minorHighAttenSetting_Type()
)
dm1000minorHighAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighAttenSetting.setStatus("obsolete")
_Dm1000minorLowAttenSetting_Type = Float
_Dm1000minorLowAttenSetting_Object = MibTableColumn
dm1000minorLowAttenSetting = _Dm1000minorLowAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 29),
    _Dm1000minorLowAttenSetting_Type()
)
dm1000minorLowAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowAttenSetting.setStatus("obsolete")
_Dm1000currentValueAttenSetting_Type = Float
_Dm1000currentValueAttenSetting_Object = MibTableColumn
dm1000currentValueAttenSetting = _Dm1000currentValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 30),
    _Dm1000currentValueAttenSetting_Type()
)
dm1000currentValueAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000currentValueAttenSetting.setStatus("mandatory")


class _Dm1000stateFlagAttenSetting_Type(Integer32):
    """Custom type dm1000stateFlagAttenSetting based on Integer32"""
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


_Dm1000stateFlagAttenSetting_Type.__name__ = "Integer32"
_Dm1000stateFlagAttenSetting_Object = MibTableColumn
dm1000stateFlagAttenSetting = _Dm1000stateFlagAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 31),
    _Dm1000stateFlagAttenSetting_Type()
)
dm1000stateFlagAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagAttenSetting.setStatus("mandatory")
_Dm1000minValueAttenSetting_Type = Float
_Dm1000minValueAttenSetting_Object = MibTableColumn
dm1000minValueAttenSetting = _Dm1000minValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 32),
    _Dm1000minValueAttenSetting_Type()
)
dm1000minValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueAttenSetting.setStatus("mandatory")
_Dm1000maxValueAttenSetting_Type = Float
_Dm1000maxValueAttenSetting_Object = MibTableColumn
dm1000maxValueAttenSetting = _Dm1000maxValueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 33),
    _Dm1000maxValueAttenSetting_Type()
)
dm1000maxValueAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueAttenSetting.setStatus("mandatory")


class _Dm1000alarmStateAttenSetting_Type(Integer32):
    """Custom type dm1000alarmStateAttenSetting based on Integer32"""
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


_Dm1000alarmStateAttenSetting_Type.__name__ = "Integer32"
_Dm1000alarmStateAttenSetting_Object = MibTableColumn
dm1000alarmStateAttenSetting = _Dm1000alarmStateAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 34),
    _Dm1000alarmStateAttenSetting_Type()
)
dm1000alarmStateAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateAttenSetting.setStatus("mandatory")


class _Dm1000labelLaserPower_Type(DisplayString):
    """Custom type dm1000labelLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelLaserPower_Type.__name__ = "DisplayString"
_Dm1000labelLaserPower_Object = MibTableColumn
dm1000labelLaserPower = _Dm1000labelLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 35),
    _Dm1000labelLaserPower_Type()
)
dm1000labelLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelLaserPower.setStatus("optional")


class _Dm1000uomLaserPower_Type(DisplayString):
    """Custom type dm1000uomLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomLaserPower_Type.__name__ = "DisplayString"
_Dm1000uomLaserPower_Object = MibTableColumn
dm1000uomLaserPower = _Dm1000uomLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 36),
    _Dm1000uomLaserPower_Type()
)
dm1000uomLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomLaserPower.setStatus("optional")
_Dm1000majorHighLaserPower_Type = Float
_Dm1000majorHighLaserPower_Object = MibTableColumn
dm1000majorHighLaserPower = _Dm1000majorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 37),
    _Dm1000majorHighLaserPower_Type()
)
dm1000majorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighLaserPower.setStatus("mandatory")
_Dm1000majorLowLaserPower_Type = Float
_Dm1000majorLowLaserPower_Object = MibTableColumn
dm1000majorLowLaserPower = _Dm1000majorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 38),
    _Dm1000majorLowLaserPower_Type()
)
dm1000majorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowLaserPower.setStatus("mandatory")
_Dm1000minorHighLaserPower_Type = Float
_Dm1000minorHighLaserPower_Object = MibTableColumn
dm1000minorHighLaserPower = _Dm1000minorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 39),
    _Dm1000minorHighLaserPower_Type()
)
dm1000minorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighLaserPower.setStatus("obsolete")
_Dm1000minorLowLaserPower_Type = Float
_Dm1000minorLowLaserPower_Object = MibTableColumn
dm1000minorLowLaserPower = _Dm1000minorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 40),
    _Dm1000minorLowLaserPower_Type()
)
dm1000minorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowLaserPower.setStatus("obsolete")
_Dm1000currentValueLaserPower_Type = Float
_Dm1000currentValueLaserPower_Object = MibTableColumn
dm1000currentValueLaserPower = _Dm1000currentValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 41),
    _Dm1000currentValueLaserPower_Type()
)
dm1000currentValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueLaserPower.setStatus("mandatory")


class _Dm1000stateFlagLaserPower_Type(Integer32):
    """Custom type dm1000stateFlagLaserPower based on Integer32"""
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


_Dm1000stateFlagLaserPower_Type.__name__ = "Integer32"
_Dm1000stateFlagLaserPower_Object = MibTableColumn
dm1000stateFlagLaserPower = _Dm1000stateFlagLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 42),
    _Dm1000stateFlagLaserPower_Type()
)
dm1000stateFlagLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagLaserPower.setStatus("mandatory")
_Dm1000minValueLaserPower_Type = Float
_Dm1000minValueLaserPower_Object = MibTableColumn
dm1000minValueLaserPower = _Dm1000minValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 43),
    _Dm1000minValueLaserPower_Type()
)
dm1000minValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueLaserPower.setStatus("mandatory")
_Dm1000maxValueLaserPower_Type = Float
_Dm1000maxValueLaserPower_Object = MibTableColumn
dm1000maxValueLaserPower = _Dm1000maxValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 44),
    _Dm1000maxValueLaserPower_Type()
)
dm1000maxValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueLaserPower.setStatus("mandatory")


class _Dm1000alarmStateLaserPower_Type(Integer32):
    """Custom type dm1000alarmStateLaserPower based on Integer32"""
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


_Dm1000alarmStateLaserPower_Type.__name__ = "Integer32"
_Dm1000alarmStateLaserPower_Object = MibTableColumn
dm1000alarmStateLaserPower = _Dm1000alarmStateLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 45),
    _Dm1000alarmStateLaserPower_Type()
)
dm1000alarmStateLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateLaserPower.setStatus("mandatory")


class _Dm1000labelLaserTemp_Type(DisplayString):
    """Custom type dm1000labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelLaserTemp_Type.__name__ = "DisplayString"
_Dm1000labelLaserTemp_Object = MibTableColumn
dm1000labelLaserTemp = _Dm1000labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 46),
    _Dm1000labelLaserTemp_Type()
)
dm1000labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelLaserTemp.setStatus("optional")


class _Dm1000uomLaserTemp_Type(DisplayString):
    """Custom type dm1000uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomLaserTemp_Type.__name__ = "DisplayString"
_Dm1000uomLaserTemp_Object = MibTableColumn
dm1000uomLaserTemp = _Dm1000uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 47),
    _Dm1000uomLaserTemp_Type()
)
dm1000uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomLaserTemp.setStatus("optional")
_Dm1000majorHighLaserTemp_Type = Float
_Dm1000majorHighLaserTemp_Object = MibTableColumn
dm1000majorHighLaserTemp = _Dm1000majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 48),
    _Dm1000majorHighLaserTemp_Type()
)
dm1000majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighLaserTemp.setStatus("mandatory")
_Dm1000majorLowLaserTemp_Type = Float
_Dm1000majorLowLaserTemp_Object = MibTableColumn
dm1000majorLowLaserTemp = _Dm1000majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 49),
    _Dm1000majorLowLaserTemp_Type()
)
dm1000majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowLaserTemp.setStatus("mandatory")
_Dm1000minorHighLaserTemp_Type = Float
_Dm1000minorHighLaserTemp_Object = MibTableColumn
dm1000minorHighLaserTemp = _Dm1000minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 50),
    _Dm1000minorHighLaserTemp_Type()
)
dm1000minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighLaserTemp.setStatus("obsolete")
_Dm1000minorLowLaserTemp_Type = Float
_Dm1000minorLowLaserTemp_Object = MibTableColumn
dm1000minorLowLaserTemp = _Dm1000minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 51),
    _Dm1000minorLowLaserTemp_Type()
)
dm1000minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowLaserTemp.setStatus("obsolete")
_Dm1000currentValueLaserTemp_Type = Float
_Dm1000currentValueLaserTemp_Object = MibTableColumn
dm1000currentValueLaserTemp = _Dm1000currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 52),
    _Dm1000currentValueLaserTemp_Type()
)
dm1000currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueLaserTemp.setStatus("mandatory")


class _Dm1000stateFlagLaserTemp_Type(Integer32):
    """Custom type dm1000stateFlagLaserTemp based on Integer32"""
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


_Dm1000stateFlagLaserTemp_Type.__name__ = "Integer32"
_Dm1000stateFlagLaserTemp_Object = MibTableColumn
dm1000stateFlagLaserTemp = _Dm1000stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 53),
    _Dm1000stateFlagLaserTemp_Type()
)
dm1000stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagLaserTemp.setStatus("mandatory")
_Dm1000minValueLaserTemp_Type = Float
_Dm1000minValueLaserTemp_Object = MibTableColumn
dm1000minValueLaserTemp = _Dm1000minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 54),
    _Dm1000minValueLaserTemp_Type()
)
dm1000minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueLaserTemp.setStatus("mandatory")
_Dm1000maxValueLaserTemp_Type = Float
_Dm1000maxValueLaserTemp_Object = MibTableColumn
dm1000maxValueLaserTemp = _Dm1000maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 55),
    _Dm1000maxValueLaserTemp_Type()
)
dm1000maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueLaserTemp.setStatus("mandatory")


class _Dm1000alarmStateLaserTemp_Type(Integer32):
    """Custom type dm1000alarmStateLaserTemp based on Integer32"""
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


_Dm1000alarmStateLaserTemp_Type.__name__ = "Integer32"
_Dm1000alarmStateLaserTemp_Object = MibTableColumn
dm1000alarmStateLaserTemp = _Dm1000alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 56),
    _Dm1000alarmStateLaserTemp_Type()
)
dm1000alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateLaserTemp.setStatus("mandatory")


class _Dm1000labelLaserCurrent_Type(DisplayString):
    """Custom type dm1000labelLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelLaserCurrent_Type.__name__ = "DisplayString"
_Dm1000labelLaserCurrent_Object = MibTableColumn
dm1000labelLaserCurrent = _Dm1000labelLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 57),
    _Dm1000labelLaserCurrent_Type()
)
dm1000labelLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelLaserCurrent.setStatus("optional")


class _Dm1000uomLaserCurrent_Type(DisplayString):
    """Custom type dm1000uomLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomLaserCurrent_Type.__name__ = "DisplayString"
_Dm1000uomLaserCurrent_Object = MibTableColumn
dm1000uomLaserCurrent = _Dm1000uomLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 58),
    _Dm1000uomLaserCurrent_Type()
)
dm1000uomLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomLaserCurrent.setStatus("optional")
_Dm1000majorHighLaserCurrent_Type = Float
_Dm1000majorHighLaserCurrent_Object = MibTableColumn
dm1000majorHighLaserCurrent = _Dm1000majorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 59),
    _Dm1000majorHighLaserCurrent_Type()
)
dm1000majorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighLaserCurrent.setStatus("mandatory")
_Dm1000majorLowLaserCurrent_Type = Float
_Dm1000majorLowLaserCurrent_Object = MibTableColumn
dm1000majorLowLaserCurrent = _Dm1000majorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 60),
    _Dm1000majorLowLaserCurrent_Type()
)
dm1000majorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowLaserCurrent.setStatus("mandatory")
_Dm1000minorHighLaserCurrent_Type = Float
_Dm1000minorHighLaserCurrent_Object = MibTableColumn
dm1000minorHighLaserCurrent = _Dm1000minorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 61),
    _Dm1000minorHighLaserCurrent_Type()
)
dm1000minorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighLaserCurrent.setStatus("obsolete")
_Dm1000minorLowLaserCurrent_Type = Float
_Dm1000minorLowLaserCurrent_Object = MibTableColumn
dm1000minorLowLaserCurrent = _Dm1000minorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 62),
    _Dm1000minorLowLaserCurrent_Type()
)
dm1000minorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowLaserCurrent.setStatus("obsolete")
_Dm1000currentValueLaserCurrent_Type = Float
_Dm1000currentValueLaserCurrent_Object = MibTableColumn
dm1000currentValueLaserCurrent = _Dm1000currentValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 63),
    _Dm1000currentValueLaserCurrent_Type()
)
dm1000currentValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueLaserCurrent.setStatus("mandatory")


class _Dm1000stateFlagLaserCurrent_Type(Integer32):
    """Custom type dm1000stateFlagLaserCurrent based on Integer32"""
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


_Dm1000stateFlagLaserCurrent_Type.__name__ = "Integer32"
_Dm1000stateFlagLaserCurrent_Object = MibTableColumn
dm1000stateFlagLaserCurrent = _Dm1000stateFlagLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 64),
    _Dm1000stateFlagLaserCurrent_Type()
)
dm1000stateFlagLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagLaserCurrent.setStatus("mandatory")
_Dm1000minValueLaserCurrent_Type = Float
_Dm1000minValueLaserCurrent_Object = MibTableColumn
dm1000minValueLaserCurrent = _Dm1000minValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 65),
    _Dm1000minValueLaserCurrent_Type()
)
dm1000minValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueLaserCurrent.setStatus("mandatory")
_Dm1000maxValueLaserCurrent_Type = Float
_Dm1000maxValueLaserCurrent_Object = MibTableColumn
dm1000maxValueLaserCurrent = _Dm1000maxValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 66),
    _Dm1000maxValueLaserCurrent_Type()
)
dm1000maxValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueLaserCurrent.setStatus("mandatory")


class _Dm1000alarmStateLaserCurrent_Type(Integer32):
    """Custom type dm1000alarmStateLaserCurrent based on Integer32"""
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


_Dm1000alarmStateLaserCurrent_Type.__name__ = "Integer32"
_Dm1000alarmStateLaserCurrent_Object = MibTableColumn
dm1000alarmStateLaserCurrent = _Dm1000alarmStateLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 67),
    _Dm1000alarmStateLaserCurrent_Type()
)
dm1000alarmStateLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateLaserCurrent.setStatus("mandatory")


class _Dm1000labelTecCurrent_Type(DisplayString):
    """Custom type dm1000labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelTecCurrent_Type.__name__ = "DisplayString"
_Dm1000labelTecCurrent_Object = MibTableColumn
dm1000labelTecCurrent = _Dm1000labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 68),
    _Dm1000labelTecCurrent_Type()
)
dm1000labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelTecCurrent.setStatus("optional")


class _Dm1000uomTecCurrent_Type(DisplayString):
    """Custom type dm1000uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomTecCurrent_Type.__name__ = "DisplayString"
_Dm1000uomTecCurrent_Object = MibTableColumn
dm1000uomTecCurrent = _Dm1000uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 69),
    _Dm1000uomTecCurrent_Type()
)
dm1000uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomTecCurrent.setStatus("optional")
_Dm1000majorHighTecCurrent_Type = Float
_Dm1000majorHighTecCurrent_Object = MibTableColumn
dm1000majorHighTecCurrent = _Dm1000majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 70),
    _Dm1000majorHighTecCurrent_Type()
)
dm1000majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighTecCurrent.setStatus("mandatory")
_Dm1000majorLowTecCurrent_Type = Float
_Dm1000majorLowTecCurrent_Object = MibTableColumn
dm1000majorLowTecCurrent = _Dm1000majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 71),
    _Dm1000majorLowTecCurrent_Type()
)
dm1000majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowTecCurrent.setStatus("mandatory")
_Dm1000minorHighTecCurrent_Type = Float
_Dm1000minorHighTecCurrent_Object = MibTableColumn
dm1000minorHighTecCurrent = _Dm1000minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 72),
    _Dm1000minorHighTecCurrent_Type()
)
dm1000minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighTecCurrent.setStatus("obsolete")
_Dm1000minorLowTecCurrent_Type = Float
_Dm1000minorLowTecCurrent_Object = MibTableColumn
dm1000minorLowTecCurrent = _Dm1000minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 73),
    _Dm1000minorLowTecCurrent_Type()
)
dm1000minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowTecCurrent.setStatus("obsolete")
_Dm1000currentValueTecCurrent_Type = Float
_Dm1000currentValueTecCurrent_Object = MibTableColumn
dm1000currentValueTecCurrent = _Dm1000currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 74),
    _Dm1000currentValueTecCurrent_Type()
)
dm1000currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueTecCurrent.setStatus("mandatory")


class _Dm1000stateFlagTecCurrent_Type(Integer32):
    """Custom type dm1000stateFlagTecCurrent based on Integer32"""
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


_Dm1000stateFlagTecCurrent_Type.__name__ = "Integer32"
_Dm1000stateFlagTecCurrent_Object = MibTableColumn
dm1000stateFlagTecCurrent = _Dm1000stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 75),
    _Dm1000stateFlagTecCurrent_Type()
)
dm1000stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagTecCurrent.setStatus("mandatory")
_Dm1000minValueTecCurrent_Type = Float
_Dm1000minValueTecCurrent_Object = MibTableColumn
dm1000minValueTecCurrent = _Dm1000minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 76),
    _Dm1000minValueTecCurrent_Type()
)
dm1000minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueTecCurrent.setStatus("mandatory")
_Dm1000maxValueTecCurrent_Type = Float
_Dm1000maxValueTecCurrent_Object = MibTableColumn
dm1000maxValueTecCurrent = _Dm1000maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 77),
    _Dm1000maxValueTecCurrent_Type()
)
dm1000maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueTecCurrent.setStatus("mandatory")


class _Dm1000alarmStateTecCurrent_Type(Integer32):
    """Custom type dm1000alarmStateTecCurrent based on Integer32"""
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


_Dm1000alarmStateTecCurrent_Type.__name__ = "Integer32"
_Dm1000alarmStateTecCurrent_Object = MibTableColumn
dm1000alarmStateTecCurrent = _Dm1000alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 78),
    _Dm1000alarmStateTecCurrent_Type()
)
dm1000alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateTecCurrent.setStatus("mandatory")


class _Dm1000labelModTemp_Type(DisplayString):
    """Custom type dm1000labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelModTemp_Type.__name__ = "DisplayString"
_Dm1000labelModTemp_Object = MibTableColumn
dm1000labelModTemp = _Dm1000labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 79),
    _Dm1000labelModTemp_Type()
)
dm1000labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelModTemp.setStatus("optional")


class _Dm1000uomModTemp_Type(DisplayString):
    """Custom type dm1000uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomModTemp_Type.__name__ = "DisplayString"
_Dm1000uomModTemp_Object = MibTableColumn
dm1000uomModTemp = _Dm1000uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 80),
    _Dm1000uomModTemp_Type()
)
dm1000uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomModTemp.setStatus("optional")
_Dm1000majorHighModTemp_Type = Float
_Dm1000majorHighModTemp_Object = MibTableColumn
dm1000majorHighModTemp = _Dm1000majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 81),
    _Dm1000majorHighModTemp_Type()
)
dm1000majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighModTemp.setStatus("mandatory")
_Dm1000majorLowModTemp_Type = Float
_Dm1000majorLowModTemp_Object = MibTableColumn
dm1000majorLowModTemp = _Dm1000majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 82),
    _Dm1000majorLowModTemp_Type()
)
dm1000majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowModTemp.setStatus("mandatory")
_Dm1000minorHighModTemp_Type = Float
_Dm1000minorHighModTemp_Object = MibTableColumn
dm1000minorHighModTemp = _Dm1000minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 83),
    _Dm1000minorHighModTemp_Type()
)
dm1000minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighModTemp.setStatus("mandatory")
_Dm1000minorLowModTemp_Type = Float
_Dm1000minorLowModTemp_Object = MibTableColumn
dm1000minorLowModTemp = _Dm1000minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 84),
    _Dm1000minorLowModTemp_Type()
)
dm1000minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowModTemp.setStatus("mandatory")
_Dm1000currentValueModTemp_Type = Float
_Dm1000currentValueModTemp_Object = MibTableColumn
dm1000currentValueModTemp = _Dm1000currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 85),
    _Dm1000currentValueModTemp_Type()
)
dm1000currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueModTemp.setStatus("mandatory")


class _Dm1000stateFlagModTemp_Type(Integer32):
    """Custom type dm1000stateFlagModTemp based on Integer32"""
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


_Dm1000stateFlagModTemp_Type.__name__ = "Integer32"
_Dm1000stateFlagModTemp_Object = MibTableColumn
dm1000stateFlagModTemp = _Dm1000stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 86),
    _Dm1000stateFlagModTemp_Type()
)
dm1000stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagModTemp.setStatus("mandatory")
_Dm1000minValueModTemp_Type = Float
_Dm1000minValueModTemp_Object = MibTableColumn
dm1000minValueModTemp = _Dm1000minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 87),
    _Dm1000minValueModTemp_Type()
)
dm1000minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueModTemp.setStatus("mandatory")
_Dm1000maxValueModTemp_Type = Float
_Dm1000maxValueModTemp_Object = MibTableColumn
dm1000maxValueModTemp = _Dm1000maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 88),
    _Dm1000maxValueModTemp_Type()
)
dm1000maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueModTemp.setStatus("mandatory")


class _Dm1000alarmStateModTemp_Type(Integer32):
    """Custom type dm1000alarmStateModTemp based on Integer32"""
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


_Dm1000alarmStateModTemp_Type.__name__ = "Integer32"
_Dm1000alarmStateModTemp_Object = MibTableColumn
dm1000alarmStateModTemp = _Dm1000alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 89),
    _Dm1000alarmStateModTemp_Type()
)
dm1000alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateModTemp.setStatus("mandatory")


class _Dm1000labelFanCurrent_Type(DisplayString):
    """Custom type dm1000labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelFanCurrent_Type.__name__ = "DisplayString"
_Dm1000labelFanCurrent_Object = MibTableColumn
dm1000labelFanCurrent = _Dm1000labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 90),
    _Dm1000labelFanCurrent_Type()
)
dm1000labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelFanCurrent.setStatus("optional")


class _Dm1000uomFanCurrent_Type(DisplayString):
    """Custom type dm1000uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000uomFanCurrent_Type.__name__ = "DisplayString"
_Dm1000uomFanCurrent_Object = MibTableColumn
dm1000uomFanCurrent = _Dm1000uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 91),
    _Dm1000uomFanCurrent_Type()
)
dm1000uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000uomFanCurrent.setStatus("optional")
_Dm1000majorHighFanCurrent_Type = Float
_Dm1000majorHighFanCurrent_Object = MibTableColumn
dm1000majorHighFanCurrent = _Dm1000majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 92),
    _Dm1000majorHighFanCurrent_Type()
)
dm1000majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorHighFanCurrent.setStatus("mandatory")
_Dm1000majorLowFanCurrent_Type = Float
_Dm1000majorLowFanCurrent_Object = MibTableColumn
dm1000majorLowFanCurrent = _Dm1000majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 93),
    _Dm1000majorLowFanCurrent_Type()
)
dm1000majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000majorLowFanCurrent.setStatus("mandatory")
_Dm1000minorHighFanCurrent_Type = Float
_Dm1000minorHighFanCurrent_Object = MibTableColumn
dm1000minorHighFanCurrent = _Dm1000minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 94),
    _Dm1000minorHighFanCurrent_Type()
)
dm1000minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorHighFanCurrent.setStatus("obsolete")
_Dm1000minorLowFanCurrent_Type = Float
_Dm1000minorLowFanCurrent_Object = MibTableColumn
dm1000minorLowFanCurrent = _Dm1000minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 95),
    _Dm1000minorLowFanCurrent_Type()
)
dm1000minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minorLowFanCurrent.setStatus("obsolete")
_Dm1000currentValueFanCurrent_Type = Float
_Dm1000currentValueFanCurrent_Object = MibTableColumn
dm1000currentValueFanCurrent = _Dm1000currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 96),
    _Dm1000currentValueFanCurrent_Type()
)
dm1000currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000currentValueFanCurrent.setStatus("mandatory")


class _Dm1000stateFlagFanCurrent_Type(Integer32):
    """Custom type dm1000stateFlagFanCurrent based on Integer32"""
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


_Dm1000stateFlagFanCurrent_Type.__name__ = "Integer32"
_Dm1000stateFlagFanCurrent_Object = MibTableColumn
dm1000stateFlagFanCurrent = _Dm1000stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 97),
    _Dm1000stateFlagFanCurrent_Type()
)
dm1000stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateFlagFanCurrent.setStatus("mandatory")
_Dm1000minValueFanCurrent_Type = Float
_Dm1000minValueFanCurrent_Object = MibTableColumn
dm1000minValueFanCurrent = _Dm1000minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 98),
    _Dm1000minValueFanCurrent_Type()
)
dm1000minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000minValueFanCurrent.setStatus("mandatory")
_Dm1000maxValueFanCurrent_Type = Float
_Dm1000maxValueFanCurrent_Object = MibTableColumn
dm1000maxValueFanCurrent = _Dm1000maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 99),
    _Dm1000maxValueFanCurrent_Type()
)
dm1000maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000maxValueFanCurrent.setStatus("mandatory")


class _Dm1000alarmStateFanCurrent_Type(Integer32):
    """Custom type dm1000alarmStateFanCurrent based on Integer32"""
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


_Dm1000alarmStateFanCurrent_Type.__name__ = "Integer32"
_Dm1000alarmStateFanCurrent_Object = MibTableColumn
dm1000alarmStateFanCurrent = _Dm1000alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 2, 1, 100),
    _Dm1000alarmStateFanCurrent_Type()
)
dm1000alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000alarmStateFanCurrent.setStatus("mandatory")
_Gx2Dm1000DigitalTable_Object = MibTable
gx2Dm1000DigitalTable = _Gx2Dm1000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3)
)
if mibBuilder.loadTexts:
    gx2Dm1000DigitalTable.setStatus("mandatory")
_Gx2Dm1000DigitalEntry_Object = MibTableRow
gx2Dm1000DigitalEntry = _Gx2Dm1000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2)
)
gx2Dm1000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Dm1000-MIB", "gx2Dm1000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm1000DigitalEntry.setStatus("mandatory")


class _Gx2Dm1000DigitalTableIndex_Type(Integer32):
    """Custom type gx2Dm1000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm1000DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Dm1000DigitalTableIndex_Object = MibTableColumn
gx2Dm1000DigitalTableIndex = _Gx2Dm1000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 1),
    _Gx2Dm1000DigitalTableIndex_Type()
)
gx2Dm1000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm1000DigitalTableIndex.setStatus("mandatory")


class _Dm1000labelRfInput_Type(DisplayString):
    """Custom type dm1000labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelRfInput_Type.__name__ = "DisplayString"
_Dm1000labelRfInput_Object = MibTableColumn
dm1000labelRfInput = _Dm1000labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 2),
    _Dm1000labelRfInput_Type()
)
dm1000labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelRfInput.setStatus("optional")


class _Dm1000enumRfInput_Type(DisplayString):
    """Custom type dm1000enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000enumRfInput_Type.__name__ = "DisplayString"
_Dm1000enumRfInput_Object = MibTableColumn
dm1000enumRfInput = _Dm1000enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 3),
    _Dm1000enumRfInput_Type()
)
dm1000enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000enumRfInput.setStatus("optional")


class _Dm1000valueRfInput_Type(Integer32):
    """Custom type dm1000valueRfInput based on Integer32"""
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


_Dm1000valueRfInput_Type.__name__ = "Integer32"
_Dm1000valueRfInput_Object = MibTableColumn
dm1000valueRfInput = _Dm1000valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 4),
    _Dm1000valueRfInput_Type()
)
dm1000valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000valueRfInput.setStatus("mandatory")


class _Dm1000stateflagRfInput_Type(Integer32):
    """Custom type dm1000stateflagRfInput based on Integer32"""
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


_Dm1000stateflagRfInput_Type.__name__ = "Integer32"
_Dm1000stateflagRfInput_Object = MibTableColumn
dm1000stateflagRfInput = _Dm1000stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 5),
    _Dm1000stateflagRfInput_Type()
)
dm1000stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagRfInput.setStatus("mandatory")


class _Dm1000labelOptOutput_Type(DisplayString):
    """Custom type dm1000labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelOptOutput_Type.__name__ = "DisplayString"
_Dm1000labelOptOutput_Object = MibTableColumn
dm1000labelOptOutput = _Dm1000labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 6),
    _Dm1000labelOptOutput_Type()
)
dm1000labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelOptOutput.setStatus("optional")


class _Dm1000enumOptOutput_Type(DisplayString):
    """Custom type dm1000enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000enumOptOutput_Type.__name__ = "DisplayString"
_Dm1000enumOptOutput_Object = MibTableColumn
dm1000enumOptOutput = _Dm1000enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 7),
    _Dm1000enumOptOutput_Type()
)
dm1000enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000enumOptOutput.setStatus("optional")


class _Dm1000valueOptOutput_Type(Integer32):
    """Custom type dm1000valueOptOutput based on Integer32"""
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


_Dm1000valueOptOutput_Type.__name__ = "Integer32"
_Dm1000valueOptOutput_Object = MibTableColumn
dm1000valueOptOutput = _Dm1000valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 8),
    _Dm1000valueOptOutput_Type()
)
dm1000valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000valueOptOutput.setStatus("mandatory")


class _Dm1000stateflagOptOutput_Type(Integer32):
    """Custom type dm1000stateflagOptOutput based on Integer32"""
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


_Dm1000stateflagOptOutput_Type.__name__ = "Integer32"
_Dm1000stateflagOptOutput_Object = MibTableColumn
dm1000stateflagOptOutput = _Dm1000stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 9),
    _Dm1000stateflagOptOutput_Type()
)
dm1000stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagOptOutput.setStatus("mandatory")


class _Dm1000labelSbsControl_Type(DisplayString):
    """Custom type dm1000labelSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelSbsControl_Type.__name__ = "DisplayString"
_Dm1000labelSbsControl_Object = MibTableColumn
dm1000labelSbsControl = _Dm1000labelSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 10),
    _Dm1000labelSbsControl_Type()
)
dm1000labelSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelSbsControl.setStatus("optional")


class _Dm1000enumSbsControl_Type(DisplayString):
    """Custom type dm1000enumSbsControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000enumSbsControl_Type.__name__ = "DisplayString"
_Dm1000enumSbsControl_Object = MibTableColumn
dm1000enumSbsControl = _Dm1000enumSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 11),
    _Dm1000enumSbsControl_Type()
)
dm1000enumSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000enumSbsControl.setStatus("optional")


class _Dm1000valueSbsControl_Type(Integer32):
    """Custom type dm1000valueSbsControl based on Integer32"""
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


_Dm1000valueSbsControl_Type.__name__ = "Integer32"
_Dm1000valueSbsControl_Object = MibTableColumn
dm1000valueSbsControl = _Dm1000valueSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 12),
    _Dm1000valueSbsControl_Type()
)
dm1000valueSbsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000valueSbsControl.setStatus("mandatory")


class _Dm1000stateflagSbsControl_Type(Integer32):
    """Custom type dm1000stateflagSbsControl based on Integer32"""
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


_Dm1000stateflagSbsControl_Type.__name__ = "Integer32"
_Dm1000stateflagSbsControl_Object = MibTableColumn
dm1000stateflagSbsControl = _Dm1000stateflagSbsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 13),
    _Dm1000stateflagSbsControl_Type()
)
dm1000stateflagSbsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagSbsControl.setStatus("mandatory")


class _Dm1000labelLaserMode_Type(DisplayString):
    """Custom type dm1000labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelLaserMode_Type.__name__ = "DisplayString"
_Dm1000labelLaserMode_Object = MibTableColumn
dm1000labelLaserMode = _Dm1000labelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 14),
    _Dm1000labelLaserMode_Type()
)
dm1000labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelLaserMode.setStatus("optional")


class _Dm1000enumLaserMode_Type(DisplayString):
    """Custom type dm1000enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000enumLaserMode_Type.__name__ = "DisplayString"
_Dm1000enumLaserMode_Object = MibTableColumn
dm1000enumLaserMode = _Dm1000enumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 15),
    _Dm1000enumLaserMode_Type()
)
dm1000enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000enumLaserMode.setStatus("optional")


class _Dm1000valueLaserMode_Type(Integer32):
    """Custom type dm1000valueLaserMode based on Integer32"""
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


_Dm1000valueLaserMode_Type.__name__ = "Integer32"
_Dm1000valueLaserMode_Object = MibTableColumn
dm1000valueLaserMode = _Dm1000valueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 16),
    _Dm1000valueLaserMode_Type()
)
dm1000valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000valueLaserMode.setStatus("mandatory")


class _Dm1000stateflagLaserMode_Type(Integer32):
    """Custom type dm1000stateflagLaserMode based on Integer32"""
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


_Dm1000stateflagLaserMode_Type.__name__ = "Integer32"
_Dm1000stateflagLaserMode_Object = MibTableColumn
dm1000stateflagLaserMode = _Dm1000stateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 17),
    _Dm1000stateflagLaserMode_Type()
)
dm1000stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagLaserMode.setStatus("mandatory")


class _Dm1000labelFactoryDefault_Type(DisplayString):
    """Custom type dm1000labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelFactoryDefault_Type.__name__ = "DisplayString"
_Dm1000labelFactoryDefault_Object = MibTableColumn
dm1000labelFactoryDefault = _Dm1000labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 18),
    _Dm1000labelFactoryDefault_Type()
)
dm1000labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelFactoryDefault.setStatus("optional")


class _Dm1000enumFactoryDefault_Type(DisplayString):
    """Custom type dm1000enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000enumFactoryDefault_Type.__name__ = "DisplayString"
_Dm1000enumFactoryDefault_Object = MibTableColumn
dm1000enumFactoryDefault = _Dm1000enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 19),
    _Dm1000enumFactoryDefault_Type()
)
dm1000enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000enumFactoryDefault.setStatus("optional")


class _Dm1000valueFactoryDefault_Type(Integer32):
    """Custom type dm1000valueFactoryDefault based on Integer32"""
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


_Dm1000valueFactoryDefault_Type.__name__ = "Integer32"
_Dm1000valueFactoryDefault_Object = MibTableColumn
dm1000valueFactoryDefault = _Dm1000valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 20),
    _Dm1000valueFactoryDefault_Type()
)
dm1000valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm1000valueFactoryDefault.setStatus("mandatory")


class _Dm1000stateflagFactoryDefault_Type(Integer32):
    """Custom type dm1000stateflagFactoryDefault based on Integer32"""
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


_Dm1000stateflagFactoryDefault_Type.__name__ = "Integer32"
_Dm1000stateflagFactoryDefault_Object = MibTableColumn
dm1000stateflagFactoryDefault = _Dm1000stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 3, 2, 21),
    _Dm1000stateflagFactoryDefault_Type()
)
dm1000stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagFactoryDefault.setStatus("mandatory")
_Gx2Dm1000StatusTable_Object = MibTable
gx2Dm1000StatusTable = _Gx2Dm1000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4)
)
if mibBuilder.loadTexts:
    gx2Dm1000StatusTable.setStatus("mandatory")
_Gx2Dm1000StatusEntry_Object = MibTableRow
gx2Dm1000StatusEntry = _Gx2Dm1000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3)
)
gx2Dm1000StatusEntry.setIndexNames(
    (0, "OMNI-gx2Dm1000-MIB", "gx2Dm1000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm1000StatusEntry.setStatus("mandatory")


class _Gx2Dm1000StatusTableIndex_Type(Integer32):
    """Custom type gx2Dm1000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm1000StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Dm1000StatusTableIndex_Object = MibTableColumn
gx2Dm1000StatusTableIndex = _Gx2Dm1000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 1),
    _Gx2Dm1000StatusTableIndex_Type()
)
gx2Dm1000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm1000StatusTableIndex.setStatus("mandatory")


class _Dm1000labelBoot_Type(DisplayString):
    """Custom type dm1000labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelBoot_Type.__name__ = "DisplayString"
_Dm1000labelBoot_Object = MibTableColumn
dm1000labelBoot = _Dm1000labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 2),
    _Dm1000labelBoot_Type()
)
dm1000labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelBoot.setStatus("optional")


class _Dm1000valueBoot_Type(Integer32):
    """Custom type dm1000valueBoot based on Integer32"""
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


_Dm1000valueBoot_Type.__name__ = "Integer32"
_Dm1000valueBoot_Object = MibTableColumn
dm1000valueBoot = _Dm1000valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 3),
    _Dm1000valueBoot_Type()
)
dm1000valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueBoot.setStatus("mandatory")


class _Dm1000stateflagBoot_Type(Integer32):
    """Custom type dm1000stateflagBoot based on Integer32"""
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


_Dm1000stateflagBoot_Type.__name__ = "Integer32"
_Dm1000stateflagBoot_Object = MibTableColumn
dm1000stateflagBoot = _Dm1000stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 4),
    _Dm1000stateflagBoot_Type()
)
dm1000stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagBoot.setStatus("mandatory")


class _Dm1000labelFlash_Type(DisplayString):
    """Custom type dm1000labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelFlash_Type.__name__ = "DisplayString"
_Dm1000labelFlash_Object = MibTableColumn
dm1000labelFlash = _Dm1000labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 5),
    _Dm1000labelFlash_Type()
)
dm1000labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelFlash.setStatus("optional")


class _Dm1000valueFlash_Type(Integer32):
    """Custom type dm1000valueFlash based on Integer32"""
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


_Dm1000valueFlash_Type.__name__ = "Integer32"
_Dm1000valueFlash_Object = MibTableColumn
dm1000valueFlash = _Dm1000valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 6),
    _Dm1000valueFlash_Type()
)
dm1000valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueFlash.setStatus("mandatory")


class _Dm1000stateflagFlash_Type(Integer32):
    """Custom type dm1000stateflagFlash based on Integer32"""
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


_Dm1000stateflagFlash_Type.__name__ = "Integer32"
_Dm1000stateflagFlash_Object = MibTableColumn
dm1000stateflagFlash = _Dm1000stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 7),
    _Dm1000stateflagFlash_Type()
)
dm1000stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagFlash.setStatus("mandatory")


class _Dm1000labelFactoryDataCRC_Type(DisplayString):
    """Custom type dm1000labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Dm1000labelFactoryDataCRC_Object = MibTableColumn
dm1000labelFactoryDataCRC = _Dm1000labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 8),
    _Dm1000labelFactoryDataCRC_Type()
)
dm1000labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelFactoryDataCRC.setStatus("optional")


class _Dm1000valueFactoryDataCRC_Type(Integer32):
    """Custom type dm1000valueFactoryDataCRC based on Integer32"""
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


_Dm1000valueFactoryDataCRC_Type.__name__ = "Integer32"
_Dm1000valueFactoryDataCRC_Object = MibTableColumn
dm1000valueFactoryDataCRC = _Dm1000valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 9),
    _Dm1000valueFactoryDataCRC_Type()
)
dm1000valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueFactoryDataCRC.setStatus("mandatory")


class _Dm1000stateflagFactoryDataCRC_Type(Integer32):
    """Custom type dm1000stateflagFactoryDataCRC based on Integer32"""
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


_Dm1000stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Dm1000stateflagFactoryDataCRC_Object = MibTableColumn
dm1000stateflagFactoryDataCRC = _Dm1000stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 10),
    _Dm1000stateflagFactoryDataCRC_Type()
)
dm1000stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagFactoryDataCRC.setStatus("mandatory")


class _Dm1000labelLaserDataCRC_Type(DisplayString):
    """Custom type dm1000labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelLaserDataCRC_Type.__name__ = "DisplayString"
_Dm1000labelLaserDataCRC_Object = MibTableColumn
dm1000labelLaserDataCRC = _Dm1000labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 11),
    _Dm1000labelLaserDataCRC_Type()
)
dm1000labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelLaserDataCRC.setStatus("optional")


class _Dm1000valueLaserDataCRC_Type(Integer32):
    """Custom type dm1000valueLaserDataCRC based on Integer32"""
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


_Dm1000valueLaserDataCRC_Type.__name__ = "Integer32"
_Dm1000valueLaserDataCRC_Object = MibTableColumn
dm1000valueLaserDataCRC = _Dm1000valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 12),
    _Dm1000valueLaserDataCRC_Type()
)
dm1000valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueLaserDataCRC.setStatus("mandatory")


class _Dm1000stateflagLaserDataCRC_Type(Integer32):
    """Custom type dm1000stateflagLaserDataCRC based on Integer32"""
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


_Dm1000stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Dm1000stateflagLaserDataCRC_Object = MibTableColumn
dm1000stateflagLaserDataCRC = _Dm1000stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 13),
    _Dm1000stateflagLaserDataCRC_Type()
)
dm1000stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagLaserDataCRC.setStatus("mandatory")


class _Dm1000labelAlarmDataCrc_Type(DisplayString):
    """Custom type dm1000labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Dm1000labelAlarmDataCrc_Object = MibTableColumn
dm1000labelAlarmDataCrc = _Dm1000labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 14),
    _Dm1000labelAlarmDataCrc_Type()
)
dm1000labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelAlarmDataCrc.setStatus("optional")


class _Dm1000valueAlarmDataCrc_Type(Integer32):
    """Custom type dm1000valueAlarmDataCrc based on Integer32"""
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


_Dm1000valueAlarmDataCrc_Type.__name__ = "Integer32"
_Dm1000valueAlarmDataCrc_Object = MibTableColumn
dm1000valueAlarmDataCrc = _Dm1000valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 15),
    _Dm1000valueAlarmDataCrc_Type()
)
dm1000valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueAlarmDataCrc.setStatus("mandatory")


class _Dm1000stateflagAlarmDataCrc_Type(Integer32):
    """Custom type dm1000stateflagAlarmDataCrc based on Integer32"""
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


_Dm1000stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Dm1000stateflagAlarmDataCrc_Object = MibTableColumn
dm1000stateflagAlarmDataCrc = _Dm1000stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 16),
    _Dm1000stateflagAlarmDataCrc_Type()
)
dm1000stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagAlarmDataCrc.setStatus("mandatory")


class _Dm1000labelRFInputStatus_Type(DisplayString):
    """Custom type dm1000labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000labelRFInputStatus_Type.__name__ = "DisplayString"
_Dm1000labelRFInputStatus_Object = MibTableColumn
dm1000labelRFInputStatus = _Dm1000labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 17),
    _Dm1000labelRFInputStatus_Type()
)
dm1000labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000labelRFInputStatus.setStatus("optional")


class _Dm1000valueRFInputStatus_Type(Integer32):
    """Custom type dm1000valueRFInputStatus based on Integer32"""
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


_Dm1000valueRFInputStatus_Type.__name__ = "Integer32"
_Dm1000valueRFInputStatus_Object = MibTableColumn
dm1000valueRFInputStatus = _Dm1000valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 18),
    _Dm1000valueRFInputStatus_Type()
)
dm1000valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000valueRFInputStatus.setStatus("mandatory")


class _Dm1000stateflagRFInputStatus_Type(Integer32):
    """Custom type dm1000stateflagRFInputStatus based on Integer32"""
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


_Dm1000stateflagRFInputStatus_Type.__name__ = "Integer32"
_Dm1000stateflagRFInputStatus_Object = MibTableColumn
dm1000stateflagRFInputStatus = _Dm1000stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 4, 3, 19),
    _Dm1000stateflagRFInputStatus_Type()
)
dm1000stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000stateflagRFInputStatus.setStatus("mandatory")
_Gx2Dm1000FactoryTable_Object = MibTable
gx2Dm1000FactoryTable = _Gx2Dm1000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5)
)
if mibBuilder.loadTexts:
    gx2Dm1000FactoryTable.setStatus("mandatory")
_Gx2Dm1000FactoryEntry_Object = MibTableRow
gx2Dm1000FactoryEntry = _Gx2Dm1000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4)
)
gx2Dm1000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Dm1000-MIB", "gx2Dm1000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm1000FactoryEntry.setStatus("mandatory")


class _Gx2Dm1000FactoryTableIndex_Type(Integer32):
    """Custom type gx2Dm1000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm1000FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Dm1000FactoryTableIndex_Object = MibTableColumn
gx2Dm1000FactoryTableIndex = _Gx2Dm1000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 1),
    _Gx2Dm1000FactoryTableIndex_Type()
)
gx2Dm1000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm1000FactoryTableIndex.setStatus("mandatory")
_Dm1000bootControlByte_Type = Integer32
_Dm1000bootControlByte_Object = MibTableColumn
dm1000bootControlByte = _Dm1000bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 2),
    _Dm1000bootControlByte_Type()
)
dm1000bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000bootControlByte.setStatus("mandatory")
_Dm1000bootStatusByte_Type = Integer32
_Dm1000bootStatusByte_Object = MibTableColumn
dm1000bootStatusByte = _Dm1000bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 3),
    _Dm1000bootStatusByte_Type()
)
dm1000bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000bootStatusByte.setStatus("mandatory")
_Dm1000bank1CRC_Type = Integer32
_Dm1000bank1CRC_Object = MibTableColumn
dm1000bank1CRC = _Dm1000bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 4),
    _Dm1000bank1CRC_Type()
)
dm1000bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000bank1CRC.setStatus("mandatory")
_Dm1000bank2CRC_Type = Integer32
_Dm1000bank2CRC_Object = MibTableColumn
dm1000bank2CRC = _Dm1000bank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 5),
    _Dm1000bank2CRC_Type()
)
dm1000bank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000bank2CRC.setStatus("mandatory")
_Dm1000prgEEPROMByte_Type = Integer32
_Dm1000prgEEPROMByte_Object = MibTableColumn
dm1000prgEEPROMByte = _Dm1000prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 6),
    _Dm1000prgEEPROMByte_Type()
)
dm1000prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000prgEEPROMByte.setStatus("mandatory")
_Dm1000factoryCRC_Type = Integer32
_Dm1000factoryCRC_Object = MibTableColumn
dm1000factoryCRC = _Dm1000factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 7),
    _Dm1000factoryCRC_Type()
)
dm1000factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000factoryCRC.setStatus("mandatory")


class _Dm1000calculateCRC_Type(Integer32):
    """Custom type dm1000calculateCRC based on Integer32"""
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


_Dm1000calculateCRC_Type.__name__ = "Integer32"
_Dm1000calculateCRC_Object = MibTableColumn
dm1000calculateCRC = _Dm1000calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 8),
    _Dm1000calculateCRC_Type()
)
dm1000calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000calculateCRC.setStatus("obsolete")
_Dm1000hourMeter_Type = Integer32
_Dm1000hourMeter_Object = MibTableColumn
dm1000hourMeter = _Dm1000hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 9),
    _Dm1000hourMeter_Type()
)
dm1000hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000hourMeter.setStatus("mandatory")
_Dm1000flashPrgCntA_Type = Integer32
_Dm1000flashPrgCntA_Object = MibTableColumn
dm1000flashPrgCntA = _Dm1000flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 10),
    _Dm1000flashPrgCntA_Type()
)
dm1000flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000flashPrgCntA.setStatus("mandatory")
_Dm1000flashPrgCntB_Type = Integer32
_Dm1000flashPrgCntB_Object = MibTableColumn
dm1000flashPrgCntB = _Dm1000flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 11),
    _Dm1000flashPrgCntB_Type()
)
dm1000flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000flashPrgCntB.setStatus("mandatory")


class _Dm1000flashBankARev_Type(DisplayString):
    """Custom type dm1000flashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000flashBankARev_Type.__name__ = "DisplayString"
_Dm1000flashBankARev_Object = MibTableColumn
dm1000flashBankARev = _Dm1000flashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 12),
    _Dm1000flashBankARev_Type()
)
dm1000flashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000flashBankARev.setStatus("mandatory")


class _Dm1000flashBankBRev_Type(DisplayString):
    """Custom type dm1000flashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm1000flashBankBRev_Type.__name__ = "DisplayString"
_Dm1000flashBankBRev_Object = MibTableColumn
dm1000flashBankBRev = _Dm1000flashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 5, 4, 13),
    _Dm1000flashBankBRev_Type()
)
dm1000flashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm1000flashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDM1000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 1)
)
trapDM1000ConfigChangeInteger.setObjects(
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
    trapDM1000ConfigChangeInteger.setStatus(
        ""
    )

trapDM1000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 2)
)
trapDM1000ConfigChangeDisplayString.setObjects(
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
    trapDM1000ConfigChangeDisplayString.setStatus(
        ""
    )

trapDM1000fanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 3)
)
trapDM1000fanCurrentAlarm.setObjects(
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
    trapDM1000fanCurrentAlarm.setStatus(
        ""
    )

trapDM1000ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 4)
)
trapDM1000ModuleTempAlarm.setObjects(
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
    trapDM1000ModuleTempAlarm.setStatus(
        ""
    )

trapDM1000omiOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 5)
)
trapDM1000omiOffsetAlarm.setObjects(
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
    trapDM1000omiOffsetAlarm.setStatus(
        ""
    )

trapDM1000tecCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 6)
)
trapDM1000tecCurrentAlarm.setObjects(
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
    trapDM1000tecCurrentAlarm.setStatus(
        ""
    )

trapDM1000LaserCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 7)
)
trapDM1000LaserCurrentAlarm.setObjects(
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
    trapDM1000LaserCurrentAlarm.setStatus(
        ""
    )

trapDM1000LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 8)
)
trapDM1000LaserTempAlarm.setObjects(
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
    trapDM1000LaserTempAlarm.setStatus(
        ""
    )

trapDM1000LaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 9)
)
trapDM1000LaserPowerAlarm.setObjects(
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
    trapDM1000LaserPowerAlarm.setStatus(
        ""
    )

trapDM1000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 10)
)
trapDM1000FlashAlarm.setObjects(
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
    trapDM1000FlashAlarm.setStatus(
        ""
    )

trapDM1000BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 11)
)
trapDM1000BankBootAlarm.setObjects(
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
    trapDM1000BankBootAlarm.setStatus(
        ""
    )

trapDM1000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 12)
)
trapDM1000AlarmDataCRCAlarm.setObjects(
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
    trapDM1000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapDM1000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 13)
)
trapDM1000FactoryDataCRCAlarm.setObjects(
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
    trapDM1000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapDM1000CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 14)
)
trapDM1000CalDataCRCAlarm.setObjects(
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
    trapDM1000CalDataCRCAlarm.setStatus(
        ""
    )

trapDM1000ResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 15)
)
trapDM1000ResetFacDefault.setObjects(
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
    trapDM1000ResetFacDefault.setStatus(
        ""
    )

trapDM1000UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 16)
)
trapDM1000UserRFOffAlarm.setObjects(
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
    trapDM1000UserRFOffAlarm.setStatus(
        ""
    )

trapDM1000UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 17)
)
trapDM1000UserOpticalOffAlarm.setObjects(
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
    trapDM1000UserOpticalOffAlarm.setStatus(
        ""
    )

trapDM1000UserSBSOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 18)
)
trapDM1000UserSBSOffAlarm.setObjects(
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
    trapDM1000UserSBSOffAlarm.setStatus(
        ""
    )

trapDM1000RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 19)
)
trapDM1000RFInputAlarm.setObjects(
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
    trapDM1000RFInputAlarm.setStatus(
        ""
    )

trapDM1000RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28, 0, 20)
)
trapDM1000RFOverloadAlarm.setObjects(
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
    trapDM1000RFOverloadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Dm1000-MIB",
    **{"Float": Float,
       "trapDM1000ConfigChangeInteger": trapDM1000ConfigChangeInteger,
       "trapDM1000ConfigChangeDisplayString": trapDM1000ConfigChangeDisplayString,
       "trapDM1000fanCurrentAlarm": trapDM1000fanCurrentAlarm,
       "trapDM1000ModuleTempAlarm": trapDM1000ModuleTempAlarm,
       "trapDM1000omiOffsetAlarm": trapDM1000omiOffsetAlarm,
       "trapDM1000tecCurrentAlarm": trapDM1000tecCurrentAlarm,
       "trapDM1000LaserCurrentAlarm": trapDM1000LaserCurrentAlarm,
       "trapDM1000LaserTempAlarm": trapDM1000LaserTempAlarm,
       "trapDM1000LaserPowerAlarm": trapDM1000LaserPowerAlarm,
       "trapDM1000FlashAlarm": trapDM1000FlashAlarm,
       "trapDM1000BankBootAlarm": trapDM1000BankBootAlarm,
       "trapDM1000AlarmDataCRCAlarm": trapDM1000AlarmDataCRCAlarm,
       "trapDM1000FactoryDataCRCAlarm": trapDM1000FactoryDataCRCAlarm,
       "trapDM1000CalDataCRCAlarm": trapDM1000CalDataCRCAlarm,
       "trapDM1000ResetFacDefault": trapDM1000ResetFacDefault,
       "trapDM1000UserRFOffAlarm": trapDM1000UserRFOffAlarm,
       "trapDM1000UserOpticalOffAlarm": trapDM1000UserOpticalOffAlarm,
       "trapDM1000UserSBSOffAlarm": trapDM1000UserSBSOffAlarm,
       "trapDM1000RFInputAlarm": trapDM1000RFInputAlarm,
       "trapDM1000RFOverloadAlarm": trapDM1000RFOverloadAlarm,
       "gx2Dm1000Descriptor": gx2Dm1000Descriptor,
       "gx2Dm1000AnalogTable": gx2Dm1000AnalogTable,
       "gx2Dm1000AnalogEntry": gx2Dm1000AnalogEntry,
       "gx2Dm1000AnalogTableIndex": gx2Dm1000AnalogTableIndex,
       "dm1000labelOffsetNomMonitor": dm1000labelOffsetNomMonitor,
       "dm1000uomOffsetNomMonitor": dm1000uomOffsetNomMonitor,
       "dm1000majorHighOffsetNomMonitor": dm1000majorHighOffsetNomMonitor,
       "dm1000majorLowOffsetNomMonitor": dm1000majorLowOffsetNomMonitor,
       "dm1000minorHighOffsetNomMonitor": dm1000minorHighOffsetNomMonitor,
       "dm1000minorLowOffsetNomMonitor": dm1000minorLowOffsetNomMonitor,
       "dm1000currentValueOffsetNomMonitor": dm1000currentValueOffsetNomMonitor,
       "dm1000stateFlagOffsetNomMonitor": dm1000stateFlagOffsetNomMonitor,
       "dm1000minValueOffsetNomMonitor": dm1000minValueOffsetNomMonitor,
       "dm1000maxValueOffsetNomMonitor": dm1000maxValueOffsetNomMonitor,
       "dm1000alarmStateOffsetNomMonitor": dm1000alarmStateOffsetNomMonitor,
       "dm1000labelOffsetNomCnt": dm1000labelOffsetNomCnt,
       "dm1000uomOffsetNomCnt": dm1000uomOffsetNomCnt,
       "dm1000majorHighOffsetNomCnt": dm1000majorHighOffsetNomCnt,
       "dm1000majorLowOffsetNomCnt": dm1000majorLowOffsetNomCnt,
       "dm1000minorHighOffsetNomCnt": dm1000minorHighOffsetNomCnt,
       "dm1000minorLowOffsetNomCnt": dm1000minorLowOffsetNomCnt,
       "dm1000currentValueOffsetNomCnt": dm1000currentValueOffsetNomCnt,
       "dm1000stateFlagOffsetNomCnt": dm1000stateFlagOffsetNomCnt,
       "dm1000minValueOffsetNomCnt": dm1000minValueOffsetNomCnt,
       "dm1000maxValueOffsetNomCnt": dm1000maxValueOffsetNomCnt,
       "dm1000alarmStateOffsetNomCnt": dm1000alarmStateOffsetNomCnt,
       "dm1000labelAttenSetting": dm1000labelAttenSetting,
       "dm1000uomAttenSetting": dm1000uomAttenSetting,
       "dm1000majorHighAttenSetting": dm1000majorHighAttenSetting,
       "dm1000majorLowAttenSetting": dm1000majorLowAttenSetting,
       "dm1000minorHighAttenSetting": dm1000minorHighAttenSetting,
       "dm1000minorLowAttenSetting": dm1000minorLowAttenSetting,
       "dm1000currentValueAttenSetting": dm1000currentValueAttenSetting,
       "dm1000stateFlagAttenSetting": dm1000stateFlagAttenSetting,
       "dm1000minValueAttenSetting": dm1000minValueAttenSetting,
       "dm1000maxValueAttenSetting": dm1000maxValueAttenSetting,
       "dm1000alarmStateAttenSetting": dm1000alarmStateAttenSetting,
       "dm1000labelLaserPower": dm1000labelLaserPower,
       "dm1000uomLaserPower": dm1000uomLaserPower,
       "dm1000majorHighLaserPower": dm1000majorHighLaserPower,
       "dm1000majorLowLaserPower": dm1000majorLowLaserPower,
       "dm1000minorHighLaserPower": dm1000minorHighLaserPower,
       "dm1000minorLowLaserPower": dm1000minorLowLaserPower,
       "dm1000currentValueLaserPower": dm1000currentValueLaserPower,
       "dm1000stateFlagLaserPower": dm1000stateFlagLaserPower,
       "dm1000minValueLaserPower": dm1000minValueLaserPower,
       "dm1000maxValueLaserPower": dm1000maxValueLaserPower,
       "dm1000alarmStateLaserPower": dm1000alarmStateLaserPower,
       "dm1000labelLaserTemp": dm1000labelLaserTemp,
       "dm1000uomLaserTemp": dm1000uomLaserTemp,
       "dm1000majorHighLaserTemp": dm1000majorHighLaserTemp,
       "dm1000majorLowLaserTemp": dm1000majorLowLaserTemp,
       "dm1000minorHighLaserTemp": dm1000minorHighLaserTemp,
       "dm1000minorLowLaserTemp": dm1000minorLowLaserTemp,
       "dm1000currentValueLaserTemp": dm1000currentValueLaserTemp,
       "dm1000stateFlagLaserTemp": dm1000stateFlagLaserTemp,
       "dm1000minValueLaserTemp": dm1000minValueLaserTemp,
       "dm1000maxValueLaserTemp": dm1000maxValueLaserTemp,
       "dm1000alarmStateLaserTemp": dm1000alarmStateLaserTemp,
       "dm1000labelLaserCurrent": dm1000labelLaserCurrent,
       "dm1000uomLaserCurrent": dm1000uomLaserCurrent,
       "dm1000majorHighLaserCurrent": dm1000majorHighLaserCurrent,
       "dm1000majorLowLaserCurrent": dm1000majorLowLaserCurrent,
       "dm1000minorHighLaserCurrent": dm1000minorHighLaserCurrent,
       "dm1000minorLowLaserCurrent": dm1000minorLowLaserCurrent,
       "dm1000currentValueLaserCurrent": dm1000currentValueLaserCurrent,
       "dm1000stateFlagLaserCurrent": dm1000stateFlagLaserCurrent,
       "dm1000minValueLaserCurrent": dm1000minValueLaserCurrent,
       "dm1000maxValueLaserCurrent": dm1000maxValueLaserCurrent,
       "dm1000alarmStateLaserCurrent": dm1000alarmStateLaserCurrent,
       "dm1000labelTecCurrent": dm1000labelTecCurrent,
       "dm1000uomTecCurrent": dm1000uomTecCurrent,
       "dm1000majorHighTecCurrent": dm1000majorHighTecCurrent,
       "dm1000majorLowTecCurrent": dm1000majorLowTecCurrent,
       "dm1000minorHighTecCurrent": dm1000minorHighTecCurrent,
       "dm1000minorLowTecCurrent": dm1000minorLowTecCurrent,
       "dm1000currentValueTecCurrent": dm1000currentValueTecCurrent,
       "dm1000stateFlagTecCurrent": dm1000stateFlagTecCurrent,
       "dm1000minValueTecCurrent": dm1000minValueTecCurrent,
       "dm1000maxValueTecCurrent": dm1000maxValueTecCurrent,
       "dm1000alarmStateTecCurrent": dm1000alarmStateTecCurrent,
       "dm1000labelModTemp": dm1000labelModTemp,
       "dm1000uomModTemp": dm1000uomModTemp,
       "dm1000majorHighModTemp": dm1000majorHighModTemp,
       "dm1000majorLowModTemp": dm1000majorLowModTemp,
       "dm1000minorHighModTemp": dm1000minorHighModTemp,
       "dm1000minorLowModTemp": dm1000minorLowModTemp,
       "dm1000currentValueModTemp": dm1000currentValueModTemp,
       "dm1000stateFlagModTemp": dm1000stateFlagModTemp,
       "dm1000minValueModTemp": dm1000minValueModTemp,
       "dm1000maxValueModTemp": dm1000maxValueModTemp,
       "dm1000alarmStateModTemp": dm1000alarmStateModTemp,
       "dm1000labelFanCurrent": dm1000labelFanCurrent,
       "dm1000uomFanCurrent": dm1000uomFanCurrent,
       "dm1000majorHighFanCurrent": dm1000majorHighFanCurrent,
       "dm1000majorLowFanCurrent": dm1000majorLowFanCurrent,
       "dm1000minorHighFanCurrent": dm1000minorHighFanCurrent,
       "dm1000minorLowFanCurrent": dm1000minorLowFanCurrent,
       "dm1000currentValueFanCurrent": dm1000currentValueFanCurrent,
       "dm1000stateFlagFanCurrent": dm1000stateFlagFanCurrent,
       "dm1000minValueFanCurrent": dm1000minValueFanCurrent,
       "dm1000maxValueFanCurrent": dm1000maxValueFanCurrent,
       "dm1000alarmStateFanCurrent": dm1000alarmStateFanCurrent,
       "gx2Dm1000DigitalTable": gx2Dm1000DigitalTable,
       "gx2Dm1000DigitalEntry": gx2Dm1000DigitalEntry,
       "gx2Dm1000DigitalTableIndex": gx2Dm1000DigitalTableIndex,
       "dm1000labelRfInput": dm1000labelRfInput,
       "dm1000enumRfInput": dm1000enumRfInput,
       "dm1000valueRfInput": dm1000valueRfInput,
       "dm1000stateflagRfInput": dm1000stateflagRfInput,
       "dm1000labelOptOutput": dm1000labelOptOutput,
       "dm1000enumOptOutput": dm1000enumOptOutput,
       "dm1000valueOptOutput": dm1000valueOptOutput,
       "dm1000stateflagOptOutput": dm1000stateflagOptOutput,
       "dm1000labelSbsControl": dm1000labelSbsControl,
       "dm1000enumSbsControl": dm1000enumSbsControl,
       "dm1000valueSbsControl": dm1000valueSbsControl,
       "dm1000stateflagSbsControl": dm1000stateflagSbsControl,
       "dm1000labelLaserMode": dm1000labelLaserMode,
       "dm1000enumLaserMode": dm1000enumLaserMode,
       "dm1000valueLaserMode": dm1000valueLaserMode,
       "dm1000stateflagLaserMode": dm1000stateflagLaserMode,
       "dm1000labelFactoryDefault": dm1000labelFactoryDefault,
       "dm1000enumFactoryDefault": dm1000enumFactoryDefault,
       "dm1000valueFactoryDefault": dm1000valueFactoryDefault,
       "dm1000stateflagFactoryDefault": dm1000stateflagFactoryDefault,
       "gx2Dm1000StatusTable": gx2Dm1000StatusTable,
       "gx2Dm1000StatusEntry": gx2Dm1000StatusEntry,
       "gx2Dm1000StatusTableIndex": gx2Dm1000StatusTableIndex,
       "dm1000labelBoot": dm1000labelBoot,
       "dm1000valueBoot": dm1000valueBoot,
       "dm1000stateflagBoot": dm1000stateflagBoot,
       "dm1000labelFlash": dm1000labelFlash,
       "dm1000valueFlash": dm1000valueFlash,
       "dm1000stateflagFlash": dm1000stateflagFlash,
       "dm1000labelFactoryDataCRC": dm1000labelFactoryDataCRC,
       "dm1000valueFactoryDataCRC": dm1000valueFactoryDataCRC,
       "dm1000stateflagFactoryDataCRC": dm1000stateflagFactoryDataCRC,
       "dm1000labelLaserDataCRC": dm1000labelLaserDataCRC,
       "dm1000valueLaserDataCRC": dm1000valueLaserDataCRC,
       "dm1000stateflagLaserDataCRC": dm1000stateflagLaserDataCRC,
       "dm1000labelAlarmDataCrc": dm1000labelAlarmDataCrc,
       "dm1000valueAlarmDataCrc": dm1000valueAlarmDataCrc,
       "dm1000stateflagAlarmDataCrc": dm1000stateflagAlarmDataCrc,
       "dm1000labelRFInputStatus": dm1000labelRFInputStatus,
       "dm1000valueRFInputStatus": dm1000valueRFInputStatus,
       "dm1000stateflagRFInputStatus": dm1000stateflagRFInputStatus,
       "gx2Dm1000FactoryTable": gx2Dm1000FactoryTable,
       "gx2Dm1000FactoryEntry": gx2Dm1000FactoryEntry,
       "gx2Dm1000FactoryTableIndex": gx2Dm1000FactoryTableIndex,
       "dm1000bootControlByte": dm1000bootControlByte,
       "dm1000bootStatusByte": dm1000bootStatusByte,
       "dm1000bank1CRC": dm1000bank1CRC,
       "dm1000bank2CRC": dm1000bank2CRC,
       "dm1000prgEEPROMByte": dm1000prgEEPROMByte,
       "dm1000factoryCRC": dm1000factoryCRC,
       "dm1000calculateCRC": dm1000calculateCRC,
       "dm1000hourMeter": dm1000hourMeter,
       "dm1000flashPrgCntA": dm1000flashPrgCntA,
       "dm1000flashPrgCntB": dm1000flashPrgCntB,
       "dm1000flashBankARev": dm1000flashBankARev,
       "dm1000flashBankBRev": dm1000flashBankBRev}
)
