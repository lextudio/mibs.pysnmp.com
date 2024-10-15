# SNMP MIB module (OMNI-gx2GS1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2GS1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:22 2024
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

(gx2Gs1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Gs1000")

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

_Gx2gs1000Descriptor_ObjectIdentity = ObjectIdentity
gx2gs1000Descriptor = _Gx2gs1000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 1)
)
_Gx2gs1000AnalogTable_Object = MibTable
gx2gs1000AnalogTable = _Gx2gs1000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2)
)
if mibBuilder.loadTexts:
    gx2gs1000AnalogTable.setStatus("mandatory")
_Gx2gs1000AnalogEntry_Object = MibTableRow
gx2gs1000AnalogEntry = _Gx2gs1000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1)
)
gx2gs1000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2GS1000-MIB", "gx2gs1000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2gs1000AnalogEntry.setStatus("mandatory")


class _Gx2gs1000AnalogTableIndex_Type(Integer32):
    """Custom type gx2gs1000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2gs1000AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2gs1000AnalogTableIndex_Object = MibTableColumn
gx2gs1000AnalogTableIndex = _Gx2gs1000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 1),
    _Gx2gs1000AnalogTableIndex_Type()
)
gx2gs1000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2gs1000AnalogTableIndex.setStatus("mandatory")


class _Gs1000labelOffsetNomMonitor_Type(DisplayString):
    """Custom type gs1000labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Gs1000labelOffsetNomMonitor_Object = MibTableColumn
gs1000labelOffsetNomMonitor = _Gs1000labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 2),
    _Gs1000labelOffsetNomMonitor_Type()
)
gs1000labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelOffsetNomMonitor.setStatus("optional")


class _Gs1000uomOffsetNomMonitor_Type(DisplayString):
    """Custom type gs1000uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Gs1000uomOffsetNomMonitor_Object = MibTableColumn
gs1000uomOffsetNomMonitor = _Gs1000uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 3),
    _Gs1000uomOffsetNomMonitor_Type()
)
gs1000uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomOffsetNomMonitor.setStatus("optional")
_Gs1000majorHighOffsetNomMonitor_Type = Float
_Gs1000majorHighOffsetNomMonitor_Object = MibTableColumn
gs1000majorHighOffsetNomMonitor = _Gs1000majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 4),
    _Gs1000majorHighOffsetNomMonitor_Type()
)
gs1000majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighOffsetNomMonitor.setStatus("mandatory")
_Gs1000majorLowOffsetNomMonitor_Type = Float
_Gs1000majorLowOffsetNomMonitor_Object = MibTableColumn
gs1000majorLowOffsetNomMonitor = _Gs1000majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 5),
    _Gs1000majorLowOffsetNomMonitor_Type()
)
gs1000majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowOffsetNomMonitor.setStatus("mandatory")
_Gs1000minorHighOffsetNomMonitor_Type = Float
_Gs1000minorHighOffsetNomMonitor_Object = MibTableColumn
gs1000minorHighOffsetNomMonitor = _Gs1000minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 6),
    _Gs1000minorHighOffsetNomMonitor_Type()
)
gs1000minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighOffsetNomMonitor.setStatus("mandatory")
_Gs1000minorLowOffsetNomMonitor_Type = Float
_Gs1000minorLowOffsetNomMonitor_Object = MibTableColumn
gs1000minorLowOffsetNomMonitor = _Gs1000minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 7),
    _Gs1000minorLowOffsetNomMonitor_Type()
)
gs1000minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowOffsetNomMonitor.setStatus("mandatory")
_Gs1000currentValueOffsetNomMonitor_Type = Float
_Gs1000currentValueOffsetNomMonitor_Object = MibTableColumn
gs1000currentValueOffsetNomMonitor = _Gs1000currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 8),
    _Gs1000currentValueOffsetNomMonitor_Type()
)
gs1000currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueOffsetNomMonitor.setStatus("mandatory")


class _Gs1000stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type gs1000stateFlagOffsetNomMonitor based on Integer32"""
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


_Gs1000stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Gs1000stateFlagOffsetNomMonitor_Object = MibTableColumn
gs1000stateFlagOffsetNomMonitor = _Gs1000stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 9),
    _Gs1000stateFlagOffsetNomMonitor_Type()
)
gs1000stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagOffsetNomMonitor.setStatus("mandatory")
_Gs1000minValueOffsetNomMonitor_Type = Float
_Gs1000minValueOffsetNomMonitor_Object = MibTableColumn
gs1000minValueOffsetNomMonitor = _Gs1000minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 10),
    _Gs1000minValueOffsetNomMonitor_Type()
)
gs1000minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueOffsetNomMonitor.setStatus("mandatory")
_Gs1000maxValueOffsetNomMonitor_Type = Float
_Gs1000maxValueOffsetNomMonitor_Object = MibTableColumn
gs1000maxValueOffsetNomMonitor = _Gs1000maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 11),
    _Gs1000maxValueOffsetNomMonitor_Type()
)
gs1000maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueOffsetNomMonitor.setStatus("mandatory")


class _Gs1000alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type gs1000alarmStateOffsetNomMonitor based on Integer32"""
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


_Gs1000alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Gs1000alarmStateOffsetNomMonitor_Object = MibTableColumn
gs1000alarmStateOffsetNomMonitor = _Gs1000alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 12),
    _Gs1000alarmStateOffsetNomMonitor_Type()
)
gs1000alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Gs1000labelOffsetNomCnt_Type(DisplayString):
    """Custom type gs1000labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelOffsetNomCnt_Type.__name__ = "DisplayString"
_Gs1000labelOffsetNomCnt_Object = MibTableColumn
gs1000labelOffsetNomCnt = _Gs1000labelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 13),
    _Gs1000labelOffsetNomCnt_Type()
)
gs1000labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelOffsetNomCnt.setStatus("optional")


class _Gs1000uomOffsetNomCnt_Type(DisplayString):
    """Custom type gs1000uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomOffsetNomCnt_Type.__name__ = "DisplayString"
_Gs1000uomOffsetNomCnt_Object = MibTableColumn
gs1000uomOffsetNomCnt = _Gs1000uomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 14),
    _Gs1000uomOffsetNomCnt_Type()
)
gs1000uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomOffsetNomCnt.setStatus("optional")
_Gs1000majorHighOffsetNomCnt_Type = Float
_Gs1000majorHighOffsetNomCnt_Object = MibTableColumn
gs1000majorHighOffsetNomCnt = _Gs1000majorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 15),
    _Gs1000majorHighOffsetNomCnt_Type()
)
gs1000majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighOffsetNomCnt.setStatus("optional")
_Gs1000majorLowOffsetNomCnt_Type = Float
_Gs1000majorLowOffsetNomCnt_Object = MibTableColumn
gs1000majorLowOffsetNomCnt = _Gs1000majorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 16),
    _Gs1000majorLowOffsetNomCnt_Type()
)
gs1000majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowOffsetNomCnt.setStatus("optional")
_Gs1000minorHighOffsetNomCnt_Type = Float
_Gs1000minorHighOffsetNomCnt_Object = MibTableColumn
gs1000minorHighOffsetNomCnt = _Gs1000minorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 17),
    _Gs1000minorHighOffsetNomCnt_Type()
)
gs1000minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighOffsetNomCnt.setStatus("optional")
_Gs1000minorLowOffsetNomCnt_Type = Float
_Gs1000minorLowOffsetNomCnt_Object = MibTableColumn
gs1000minorLowOffsetNomCnt = _Gs1000minorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 18),
    _Gs1000minorLowOffsetNomCnt_Type()
)
gs1000minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowOffsetNomCnt.setStatus("optional")
_Gs1000currentValueOffsetNomCnt_Type = Float
_Gs1000currentValueOffsetNomCnt_Object = MibTableColumn
gs1000currentValueOffsetNomCnt = _Gs1000currentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 19),
    _Gs1000currentValueOffsetNomCnt_Type()
)
gs1000currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000currentValueOffsetNomCnt.setStatus("mandatory")


class _Gs1000stateFlagOffsetNomCnt_Type(Integer32):
    """Custom type gs1000stateFlagOffsetNomCnt based on Integer32"""
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


_Gs1000stateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_Gs1000stateFlagOffsetNomCnt_Object = MibTableColumn
gs1000stateFlagOffsetNomCnt = _Gs1000stateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 20),
    _Gs1000stateFlagOffsetNomCnt_Type()
)
gs1000stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagOffsetNomCnt.setStatus("mandatory")
_Gs1000minValueOffsetNomCnt_Type = Float
_Gs1000minValueOffsetNomCnt_Object = MibTableColumn
gs1000minValueOffsetNomCnt = _Gs1000minValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 21),
    _Gs1000minValueOffsetNomCnt_Type()
)
gs1000minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueOffsetNomCnt.setStatus("mandatory")
_Gs1000maxValueOffsetNomCnt_Type = Float
_Gs1000maxValueOffsetNomCnt_Object = MibTableColumn
gs1000maxValueOffsetNomCnt = _Gs1000maxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 22),
    _Gs1000maxValueOffsetNomCnt_Type()
)
gs1000maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueOffsetNomCnt.setStatus("mandatory")


class _Gs1000alarmStateOffsetNomCnt_Type(Integer32):
    """Custom type gs1000alarmStateOffsetNomCnt based on Integer32"""
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


_Gs1000alarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_Gs1000alarmStateOffsetNomCnt_Object = MibTableColumn
gs1000alarmStateOffsetNomCnt = _Gs1000alarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 23),
    _Gs1000alarmStateOffsetNomCnt_Type()
)
gs1000alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateOffsetNomCnt.setStatus("mandatory")


class _Gs1000labelOptPower_Type(DisplayString):
    """Custom type gs1000labelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelOptPower_Type.__name__ = "DisplayString"
_Gs1000labelOptPower_Object = MibTableColumn
gs1000labelOptPower = _Gs1000labelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 24),
    _Gs1000labelOptPower_Type()
)
gs1000labelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelOptPower.setStatus("optional")


class _Gs1000uomOptPower_Type(DisplayString):
    """Custom type gs1000uomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomOptPower_Type.__name__ = "DisplayString"
_Gs1000uomOptPower_Object = MibTableColumn
gs1000uomOptPower = _Gs1000uomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 25),
    _Gs1000uomOptPower_Type()
)
gs1000uomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomOptPower.setStatus("optional")
_Gs1000majorHighOptPower_Type = Float
_Gs1000majorHighOptPower_Object = MibTableColumn
gs1000majorHighOptPower = _Gs1000majorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 26),
    _Gs1000majorHighOptPower_Type()
)
gs1000majorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighOptPower.setStatus("mandatory")
_Gs1000majorLowOptPower_Type = Float
_Gs1000majorLowOptPower_Object = MibTableColumn
gs1000majorLowOptPower = _Gs1000majorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 27),
    _Gs1000majorLowOptPower_Type()
)
gs1000majorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowOptPower.setStatus("mandatory")
_Gs1000minorHighOptPower_Type = Float
_Gs1000minorHighOptPower_Object = MibTableColumn
gs1000minorHighOptPower = _Gs1000minorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 28),
    _Gs1000minorHighOptPower_Type()
)
gs1000minorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighOptPower.setStatus("optional")
_Gs1000minorLowOptPower_Type = Float
_Gs1000minorLowOptPower_Object = MibTableColumn
gs1000minorLowOptPower = _Gs1000minorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 29),
    _Gs1000minorLowOptPower_Type()
)
gs1000minorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowOptPower.setStatus("optional")
_Gs1000currentValueOptPower_Type = Float
_Gs1000currentValueOptPower_Object = MibTableColumn
gs1000currentValueOptPower = _Gs1000currentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 30),
    _Gs1000currentValueOptPower_Type()
)
gs1000currentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueOptPower.setStatus("mandatory")


class _Gs1000stateFlagOptPower_Type(Integer32):
    """Custom type gs1000stateFlagOptPower based on Integer32"""
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


_Gs1000stateFlagOptPower_Type.__name__ = "Integer32"
_Gs1000stateFlagOptPower_Object = MibTableColumn
gs1000stateFlagOptPower = _Gs1000stateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 31),
    _Gs1000stateFlagOptPower_Type()
)
gs1000stateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagOptPower.setStatus("mandatory")
_Gs1000minValueOptPower_Type = Float
_Gs1000minValueOptPower_Object = MibTableColumn
gs1000minValueOptPower = _Gs1000minValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 32),
    _Gs1000minValueOptPower_Type()
)
gs1000minValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueOptPower.setStatus("mandatory")
_Gs1000maxValueOptPower_Type = Float
_Gs1000maxValueOptPower_Object = MibTableColumn
gs1000maxValueOptPower = _Gs1000maxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 33),
    _Gs1000maxValueOptPower_Type()
)
gs1000maxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueOptPower.setStatus("mandatory")


class _Gs1000alarmStateOptPower_Type(Integer32):
    """Custom type gs1000alarmStateOptPower based on Integer32"""
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


_Gs1000alarmStateOptPower_Type.__name__ = "Integer32"
_Gs1000alarmStateOptPower_Object = MibTableColumn
gs1000alarmStateOptPower = _Gs1000alarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 34),
    _Gs1000alarmStateOptPower_Type()
)
gs1000alarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateOptPower.setStatus("mandatory")


class _Gs1000labelLaserTemp_Type(DisplayString):
    """Custom type gs1000labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelLaserTemp_Type.__name__ = "DisplayString"
_Gs1000labelLaserTemp_Object = MibTableColumn
gs1000labelLaserTemp = _Gs1000labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 35),
    _Gs1000labelLaserTemp_Type()
)
gs1000labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelLaserTemp.setStatus("optional")


class _Gs1000uomLaserTemp_Type(DisplayString):
    """Custom type gs1000uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomLaserTemp_Type.__name__ = "DisplayString"
_Gs1000uomLaserTemp_Object = MibTableColumn
gs1000uomLaserTemp = _Gs1000uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 36),
    _Gs1000uomLaserTemp_Type()
)
gs1000uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomLaserTemp.setStatus("optional")
_Gs1000majorHighLaserTemp_Type = Float
_Gs1000majorHighLaserTemp_Object = MibTableColumn
gs1000majorHighLaserTemp = _Gs1000majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 37),
    _Gs1000majorHighLaserTemp_Type()
)
gs1000majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighLaserTemp.setStatus("mandatory")
_Gs1000majorLowLaserTemp_Type = Float
_Gs1000majorLowLaserTemp_Object = MibTableColumn
gs1000majorLowLaserTemp = _Gs1000majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 38),
    _Gs1000majorLowLaserTemp_Type()
)
gs1000majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowLaserTemp.setStatus("mandatory")
_Gs1000minorHighLaserTemp_Type = Float
_Gs1000minorHighLaserTemp_Object = MibTableColumn
gs1000minorHighLaserTemp = _Gs1000minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 39),
    _Gs1000minorHighLaserTemp_Type()
)
gs1000minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighLaserTemp.setStatus("mandatory")
_Gs1000minorLowLaserTemp_Type = Float
_Gs1000minorLowLaserTemp_Object = MibTableColumn
gs1000minorLowLaserTemp = _Gs1000minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 40),
    _Gs1000minorLowLaserTemp_Type()
)
gs1000minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowLaserTemp.setStatus("mandatory")
_Gs1000currentValueLaserTemp_Type = Float
_Gs1000currentValueLaserTemp_Object = MibTableColumn
gs1000currentValueLaserTemp = _Gs1000currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 41),
    _Gs1000currentValueLaserTemp_Type()
)
gs1000currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueLaserTemp.setStatus("mandatory")


class _Gs1000stateFlagLaserTemp_Type(Integer32):
    """Custom type gs1000stateFlagLaserTemp based on Integer32"""
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


_Gs1000stateFlagLaserTemp_Type.__name__ = "Integer32"
_Gs1000stateFlagLaserTemp_Object = MibTableColumn
gs1000stateFlagLaserTemp = _Gs1000stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 42),
    _Gs1000stateFlagLaserTemp_Type()
)
gs1000stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagLaserTemp.setStatus("mandatory")
_Gs1000minValueLaserTemp_Type = Float
_Gs1000minValueLaserTemp_Object = MibTableColumn
gs1000minValueLaserTemp = _Gs1000minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 43),
    _Gs1000minValueLaserTemp_Type()
)
gs1000minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueLaserTemp.setStatus("mandatory")
_Gs1000maxValueLaserTemp_Type = Float
_Gs1000maxValueLaserTemp_Object = MibTableColumn
gs1000maxValueLaserTemp = _Gs1000maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 44),
    _Gs1000maxValueLaserTemp_Type()
)
gs1000maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueLaserTemp.setStatus("mandatory")


class _Gs1000alarmStateLaserTemp_Type(Integer32):
    """Custom type gs1000alarmStateLaserTemp based on Integer32"""
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


_Gs1000alarmStateLaserTemp_Type.__name__ = "Integer32"
_Gs1000alarmStateLaserTemp_Object = MibTableColumn
gs1000alarmStateLaserTemp = _Gs1000alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 45),
    _Gs1000alarmStateLaserTemp_Type()
)
gs1000alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateLaserTemp.setStatus("mandatory")


class _Gs1000labelLaserBias_Type(DisplayString):
    """Custom type gs1000labelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelLaserBias_Type.__name__ = "DisplayString"
_Gs1000labelLaserBias_Object = MibTableColumn
gs1000labelLaserBias = _Gs1000labelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 46),
    _Gs1000labelLaserBias_Type()
)
gs1000labelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelLaserBias.setStatus("optional")


class _Gs1000uomLaserBias_Type(DisplayString):
    """Custom type gs1000uomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomLaserBias_Type.__name__ = "DisplayString"
_Gs1000uomLaserBias_Object = MibTableColumn
gs1000uomLaserBias = _Gs1000uomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 47),
    _Gs1000uomLaserBias_Type()
)
gs1000uomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomLaserBias.setStatus("optional")
_Gs1000majorHighLaserBias_Type = Float
_Gs1000majorHighLaserBias_Object = MibTableColumn
gs1000majorHighLaserBias = _Gs1000majorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 48),
    _Gs1000majorHighLaserBias_Type()
)
gs1000majorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighLaserBias.setStatus("mandatory")
_Gs1000majorLowLaserBias_Type = Float
_Gs1000majorLowLaserBias_Object = MibTableColumn
gs1000majorLowLaserBias = _Gs1000majorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 49),
    _Gs1000majorLowLaserBias_Type()
)
gs1000majorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowLaserBias.setStatus("mandatory")
_Gs1000minorHighLaserBias_Type = Float
_Gs1000minorHighLaserBias_Object = MibTableColumn
gs1000minorHighLaserBias = _Gs1000minorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 50),
    _Gs1000minorHighLaserBias_Type()
)
gs1000minorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighLaserBias.setStatus("optional")
_Gs1000minorLowLaserBias_Type = Float
_Gs1000minorLowLaserBias_Object = MibTableColumn
gs1000minorLowLaserBias = _Gs1000minorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 51),
    _Gs1000minorLowLaserBias_Type()
)
gs1000minorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowLaserBias.setStatus("optional")
_Gs1000currentValueLaserBias_Type = Float
_Gs1000currentValueLaserBias_Object = MibTableColumn
gs1000currentValueLaserBias = _Gs1000currentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 52),
    _Gs1000currentValueLaserBias_Type()
)
gs1000currentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueLaserBias.setStatus("mandatory")


class _Gs1000stateFlagLaserBias_Type(Integer32):
    """Custom type gs1000stateFlagLaserBias based on Integer32"""
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


_Gs1000stateFlagLaserBias_Type.__name__ = "Integer32"
_Gs1000stateFlagLaserBias_Object = MibTableColumn
gs1000stateFlagLaserBias = _Gs1000stateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 53),
    _Gs1000stateFlagLaserBias_Type()
)
gs1000stateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagLaserBias.setStatus("mandatory")
_Gs1000minValueLaserBias_Type = Float
_Gs1000minValueLaserBias_Object = MibTableColumn
gs1000minValueLaserBias = _Gs1000minValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 54),
    _Gs1000minValueLaserBias_Type()
)
gs1000minValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueLaserBias.setStatus("mandatory")
_Gs1000maxValueLaserBias_Type = Float
_Gs1000maxValueLaserBias_Object = MibTableColumn
gs1000maxValueLaserBias = _Gs1000maxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 55),
    _Gs1000maxValueLaserBias_Type()
)
gs1000maxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueLaserBias.setStatus("mandatory")


class _Gs1000alarmStateLaserBias_Type(Integer32):
    """Custom type gs1000alarmStateLaserBias based on Integer32"""
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


_Gs1000alarmStateLaserBias_Type.__name__ = "Integer32"
_Gs1000alarmStateLaserBias_Object = MibTableColumn
gs1000alarmStateLaserBias = _Gs1000alarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 56),
    _Gs1000alarmStateLaserBias_Type()
)
gs1000alarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateLaserBias.setStatus("mandatory")


class _Gs1000labelTecCurrent_Type(DisplayString):
    """Custom type gs1000labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelTecCurrent_Type.__name__ = "DisplayString"
_Gs1000labelTecCurrent_Object = MibTableColumn
gs1000labelTecCurrent = _Gs1000labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 57),
    _Gs1000labelTecCurrent_Type()
)
gs1000labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelTecCurrent.setStatus("optional")


class _Gs1000uomTecCurrent_Type(DisplayString):
    """Custom type gs1000uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomTecCurrent_Type.__name__ = "DisplayString"
_Gs1000uomTecCurrent_Object = MibTableColumn
gs1000uomTecCurrent = _Gs1000uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 58),
    _Gs1000uomTecCurrent_Type()
)
gs1000uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomTecCurrent.setStatus("optional")
_Gs1000majorHighTecCurrent_Type = Float
_Gs1000majorHighTecCurrent_Object = MibTableColumn
gs1000majorHighTecCurrent = _Gs1000majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 59),
    _Gs1000majorHighTecCurrent_Type()
)
gs1000majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighTecCurrent.setStatus("mandatory")
_Gs1000majorLowTecCurrent_Type = Float
_Gs1000majorLowTecCurrent_Object = MibTableColumn
gs1000majorLowTecCurrent = _Gs1000majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 60),
    _Gs1000majorLowTecCurrent_Type()
)
gs1000majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowTecCurrent.setStatus("mandatory")
_Gs1000minorHighTecCurrent_Type = Float
_Gs1000minorHighTecCurrent_Object = MibTableColumn
gs1000minorHighTecCurrent = _Gs1000minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 61),
    _Gs1000minorHighTecCurrent_Type()
)
gs1000minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighTecCurrent.setStatus("optional")
_Gs1000minorLowTecCurrent_Type = Float
_Gs1000minorLowTecCurrent_Object = MibTableColumn
gs1000minorLowTecCurrent = _Gs1000minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 62),
    _Gs1000minorLowTecCurrent_Type()
)
gs1000minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowTecCurrent.setStatus("optional")
_Gs1000currentValueTecCurrent_Type = Float
_Gs1000currentValueTecCurrent_Object = MibTableColumn
gs1000currentValueTecCurrent = _Gs1000currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 63),
    _Gs1000currentValueTecCurrent_Type()
)
gs1000currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueTecCurrent.setStatus("mandatory")


class _Gs1000stateFlagTecCurrent_Type(Integer32):
    """Custom type gs1000stateFlagTecCurrent based on Integer32"""
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


_Gs1000stateFlagTecCurrent_Type.__name__ = "Integer32"
_Gs1000stateFlagTecCurrent_Object = MibTableColumn
gs1000stateFlagTecCurrent = _Gs1000stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 64),
    _Gs1000stateFlagTecCurrent_Type()
)
gs1000stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagTecCurrent.setStatus("mandatory")
_Gs1000minValueTecCurrent_Type = Float
_Gs1000minValueTecCurrent_Object = MibTableColumn
gs1000minValueTecCurrent = _Gs1000minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 65),
    _Gs1000minValueTecCurrent_Type()
)
gs1000minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueTecCurrent.setStatus("mandatory")
_Gs1000maxValueTecCurrent_Type = Float
_Gs1000maxValueTecCurrent_Object = MibTableColumn
gs1000maxValueTecCurrent = _Gs1000maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 66),
    _Gs1000maxValueTecCurrent_Type()
)
gs1000maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueTecCurrent.setStatus("mandatory")


class _Gs1000alarmStateTecCurrent_Type(Integer32):
    """Custom type gs1000alarmStateTecCurrent based on Integer32"""
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


_Gs1000alarmStateTecCurrent_Type.__name__ = "Integer32"
_Gs1000alarmStateTecCurrent_Object = MibTableColumn
gs1000alarmStateTecCurrent = _Gs1000alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 67),
    _Gs1000alarmStateTecCurrent_Type()
)
gs1000alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateTecCurrent.setStatus("mandatory")


class _Gs1000labelModuleTemp_Type(DisplayString):
    """Custom type gs1000labelModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelModuleTemp_Type.__name__ = "DisplayString"
_Gs1000labelModuleTemp_Object = MibTableColumn
gs1000labelModuleTemp = _Gs1000labelModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 68),
    _Gs1000labelModuleTemp_Type()
)
gs1000labelModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelModuleTemp.setStatus("optional")


class _Gs1000uomModuleTemp_Type(DisplayString):
    """Custom type gs1000uomModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomModuleTemp_Type.__name__ = "DisplayString"
_Gs1000uomModuleTemp_Object = MibTableColumn
gs1000uomModuleTemp = _Gs1000uomModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 69),
    _Gs1000uomModuleTemp_Type()
)
gs1000uomModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomModuleTemp.setStatus("optional")
_Gs1000majorHighModuleTemp_Type = Float
_Gs1000majorHighModuleTemp_Object = MibTableColumn
gs1000majorHighModuleTemp = _Gs1000majorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 70),
    _Gs1000majorHighModuleTemp_Type()
)
gs1000majorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighModuleTemp.setStatus("mandatory")
_Gs1000majorLowModuleTemp_Type = Float
_Gs1000majorLowModuleTemp_Object = MibTableColumn
gs1000majorLowModuleTemp = _Gs1000majorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 71),
    _Gs1000majorLowModuleTemp_Type()
)
gs1000majorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowModuleTemp.setStatus("mandatory")
_Gs1000minorHighModuleTemp_Type = Float
_Gs1000minorHighModuleTemp_Object = MibTableColumn
gs1000minorHighModuleTemp = _Gs1000minorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 72),
    _Gs1000minorHighModuleTemp_Type()
)
gs1000minorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighModuleTemp.setStatus("mandatory")
_Gs1000minorLowModuleTemp_Type = Float
_Gs1000minorLowModuleTemp_Object = MibTableColumn
gs1000minorLowModuleTemp = _Gs1000minorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 73),
    _Gs1000minorLowModuleTemp_Type()
)
gs1000minorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowModuleTemp.setStatus("mandatory")
_Gs1000currentValueModuleTemp_Type = Float
_Gs1000currentValueModuleTemp_Object = MibTableColumn
gs1000currentValueModuleTemp = _Gs1000currentValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 74),
    _Gs1000currentValueModuleTemp_Type()
)
gs1000currentValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueModuleTemp.setStatus("mandatory")


class _Gs1000stateFlagModuleTemp_Type(Integer32):
    """Custom type gs1000stateFlagModuleTemp based on Integer32"""
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


_Gs1000stateFlagModuleTemp_Type.__name__ = "Integer32"
_Gs1000stateFlagModuleTemp_Object = MibTableColumn
gs1000stateFlagModuleTemp = _Gs1000stateFlagModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 75),
    _Gs1000stateFlagModuleTemp_Type()
)
gs1000stateFlagModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagModuleTemp.setStatus("mandatory")
_Gs1000minValueModuleTemp_Type = Float
_Gs1000minValueModuleTemp_Object = MibTableColumn
gs1000minValueModuleTemp = _Gs1000minValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 76),
    _Gs1000minValueModuleTemp_Type()
)
gs1000minValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueModuleTemp.setStatus("mandatory")
_Gs1000maxValueModuleTemp_Type = Float
_Gs1000maxValueModuleTemp_Object = MibTableColumn
gs1000maxValueModuleTemp = _Gs1000maxValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 77),
    _Gs1000maxValueModuleTemp_Type()
)
gs1000maxValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueModuleTemp.setStatus("mandatory")


class _Gs1000alarmStateModuleTemp_Type(Integer32):
    """Custom type gs1000alarmStateModuleTemp based on Integer32"""
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


_Gs1000alarmStateModuleTemp_Type.__name__ = "Integer32"
_Gs1000alarmStateModuleTemp_Object = MibTableColumn
gs1000alarmStateModuleTemp = _Gs1000alarmStateModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 78),
    _Gs1000alarmStateModuleTemp_Type()
)
gs1000alarmStateModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateModuleTemp.setStatus("mandatory")


class _Gs1000labelFan1Speed_Type(DisplayString):
    """Custom type gs1000labelFan1Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelFan1Speed_Type.__name__ = "DisplayString"
_Gs1000labelFan1Speed_Object = MibTableColumn
gs1000labelFan1Speed = _Gs1000labelFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 79),
    _Gs1000labelFan1Speed_Type()
)
gs1000labelFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelFan1Speed.setStatus("optional")


class _Gs1000uomFan1Speed_Type(DisplayString):
    """Custom type gs1000uomFan1Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomFan1Speed_Type.__name__ = "DisplayString"
_Gs1000uomFan1Speed_Object = MibTableColumn
gs1000uomFan1Speed = _Gs1000uomFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 80),
    _Gs1000uomFan1Speed_Type()
)
gs1000uomFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomFan1Speed.setStatus("optional")
_Gs1000majorHighFan1Speed_Type = Float
_Gs1000majorHighFan1Speed_Object = MibTableColumn
gs1000majorHighFan1Speed = _Gs1000majorHighFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 81),
    _Gs1000majorHighFan1Speed_Type()
)
gs1000majorHighFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighFan1Speed.setStatus("optional")
_Gs1000majorLowFan1Speed_Type = Float
_Gs1000majorLowFan1Speed_Object = MibTableColumn
gs1000majorLowFan1Speed = _Gs1000majorLowFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 82),
    _Gs1000majorLowFan1Speed_Type()
)
gs1000majorLowFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowFan1Speed.setStatus("mandatory")
_Gs1000minorHighFan1Speed_Type = Float
_Gs1000minorHighFan1Speed_Object = MibTableColumn
gs1000minorHighFan1Speed = _Gs1000minorHighFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 83),
    _Gs1000minorHighFan1Speed_Type()
)
gs1000minorHighFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighFan1Speed.setStatus("optional")
_Gs1000minorLowFan1Speed_Type = Float
_Gs1000minorLowFan1Speed_Object = MibTableColumn
gs1000minorLowFan1Speed = _Gs1000minorLowFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 84),
    _Gs1000minorLowFan1Speed_Type()
)
gs1000minorLowFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowFan1Speed.setStatus("mandatory")
_Gs1000currentValueFan1Speed_Type = Float
_Gs1000currentValueFan1Speed_Object = MibTableColumn
gs1000currentValueFan1Speed = _Gs1000currentValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 85),
    _Gs1000currentValueFan1Speed_Type()
)
gs1000currentValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueFan1Speed.setStatus("mandatory")


class _Gs1000stateFlagFan1Speed_Type(Integer32):
    """Custom type gs1000stateFlagFan1Speed based on Integer32"""
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


_Gs1000stateFlagFan1Speed_Type.__name__ = "Integer32"
_Gs1000stateFlagFan1Speed_Object = MibTableColumn
gs1000stateFlagFan1Speed = _Gs1000stateFlagFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 86),
    _Gs1000stateFlagFan1Speed_Type()
)
gs1000stateFlagFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagFan1Speed.setStatus("mandatory")
_Gs1000minValueFan1Speed_Type = Float
_Gs1000minValueFan1Speed_Object = MibTableColumn
gs1000minValueFan1Speed = _Gs1000minValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 87),
    _Gs1000minValueFan1Speed_Type()
)
gs1000minValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueFan1Speed.setStatus("mandatory")
_Gs1000maxValueFan1Speed_Type = Float
_Gs1000maxValueFan1Speed_Object = MibTableColumn
gs1000maxValueFan1Speed = _Gs1000maxValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 88),
    _Gs1000maxValueFan1Speed_Type()
)
gs1000maxValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueFan1Speed.setStatus("mandatory")


class _Gs1000alarmStateFan1Speed_Type(Integer32):
    """Custom type gs1000alarmStateFan1Speed based on Integer32"""
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


_Gs1000alarmStateFan1Speed_Type.__name__ = "Integer32"
_Gs1000alarmStateFan1Speed_Object = MibTableColumn
gs1000alarmStateFan1Speed = _Gs1000alarmStateFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 89),
    _Gs1000alarmStateFan1Speed_Type()
)
gs1000alarmStateFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateFan1Speed.setStatus("mandatory")


class _Gs1000labelFan2Speed_Type(DisplayString):
    """Custom type gs1000labelFan2Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelFan2Speed_Type.__name__ = "DisplayString"
_Gs1000labelFan2Speed_Object = MibTableColumn
gs1000labelFan2Speed = _Gs1000labelFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 90),
    _Gs1000labelFan2Speed_Type()
)
gs1000labelFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelFan2Speed.setStatus("optional")


class _Gs1000uomFan2Speed_Type(DisplayString):
    """Custom type gs1000uomFan2Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uomFan2Speed_Type.__name__ = "DisplayString"
_Gs1000uomFan2Speed_Object = MibTableColumn
gs1000uomFan2Speed = _Gs1000uomFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 91),
    _Gs1000uomFan2Speed_Type()
)
gs1000uomFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uomFan2Speed.setStatus("optional")
_Gs1000majorHighFan2Speed_Type = Float
_Gs1000majorHighFan2Speed_Object = MibTableColumn
gs1000majorHighFan2Speed = _Gs1000majorHighFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 92),
    _Gs1000majorHighFan2Speed_Type()
)
gs1000majorHighFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHighFan2Speed.setStatus("optional")
_Gs1000majorLowFan2Speed_Type = Float
_Gs1000majorLowFan2Speed_Object = MibTableColumn
gs1000majorLowFan2Speed = _Gs1000majorLowFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 93),
    _Gs1000majorLowFan2Speed_Type()
)
gs1000majorLowFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLowFan2Speed.setStatus("mandatory")
_Gs1000minorHighFan2Speed_Type = Float
_Gs1000minorHighFan2Speed_Object = MibTableColumn
gs1000minorHighFan2Speed = _Gs1000minorHighFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 94),
    _Gs1000minorHighFan2Speed_Type()
)
gs1000minorHighFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHighFan2Speed.setStatus("optional")
_Gs1000minorLowFan2Speed_Type = Float
_Gs1000minorLowFan2Speed_Object = MibTableColumn
gs1000minorLowFan2Speed = _Gs1000minorLowFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 95),
    _Gs1000minorLowFan2Speed_Type()
)
gs1000minorLowFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLowFan2Speed.setStatus("mandatory")
_Gs1000currentValueFan2Speed_Type = Float
_Gs1000currentValueFan2Speed_Object = MibTableColumn
gs1000currentValueFan2Speed = _Gs1000currentValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 96),
    _Gs1000currentValueFan2Speed_Type()
)
gs1000currentValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValueFan2Speed.setStatus("mandatory")


class _Gs1000stateFlagFan2Speed_Type(Integer32):
    """Custom type gs1000stateFlagFan2Speed based on Integer32"""
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


_Gs1000stateFlagFan2Speed_Type.__name__ = "Integer32"
_Gs1000stateFlagFan2Speed_Object = MibTableColumn
gs1000stateFlagFan2Speed = _Gs1000stateFlagFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 97),
    _Gs1000stateFlagFan2Speed_Type()
)
gs1000stateFlagFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlagFan2Speed.setStatus("mandatory")
_Gs1000minValueFan2Speed_Type = Float
_Gs1000minValueFan2Speed_Object = MibTableColumn
gs1000minValueFan2Speed = _Gs1000minValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 98),
    _Gs1000minValueFan2Speed_Type()
)
gs1000minValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValueFan2Speed.setStatus("mandatory")
_Gs1000maxValueFan2Speed_Type = Float
_Gs1000maxValueFan2Speed_Object = MibTableColumn
gs1000maxValueFan2Speed = _Gs1000maxValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 99),
    _Gs1000maxValueFan2Speed_Type()
)
gs1000maxValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValueFan2Speed.setStatus("mandatory")


class _Gs1000alarmStateFan2Speed_Type(Integer32):
    """Custom type gs1000alarmStateFan2Speed based on Integer32"""
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


_Gs1000alarmStateFan2Speed_Type.__name__ = "Integer32"
_Gs1000alarmStateFan2Speed_Object = MibTableColumn
gs1000alarmStateFan2Speed = _Gs1000alarmStateFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 100),
    _Gs1000alarmStateFan2Speed_Type()
)
gs1000alarmStateFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmStateFan2Speed.setStatus("mandatory")


class _Gs1000label12Volt_Type(DisplayString):
    """Custom type gs1000label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000label12Volt_Type.__name__ = "DisplayString"
_Gs1000label12Volt_Object = MibTableColumn
gs1000label12Volt = _Gs1000label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 101),
    _Gs1000label12Volt_Type()
)
gs1000label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000label12Volt.setStatus("optional")


class _Gs1000uom12Volt_Type(DisplayString):
    """Custom type gs1000uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000uom12Volt_Type.__name__ = "DisplayString"
_Gs1000uom12Volt_Object = MibTableColumn
gs1000uom12Volt = _Gs1000uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 102),
    _Gs1000uom12Volt_Type()
)
gs1000uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000uom12Volt.setStatus("optional")
_Gs1000majorHigh12Volt_Type = Float
_Gs1000majorHigh12Volt_Object = MibTableColumn
gs1000majorHigh12Volt = _Gs1000majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 103),
    _Gs1000majorHigh12Volt_Type()
)
gs1000majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorHigh12Volt.setStatus("mandatory")
_Gs1000majorLow12Volt_Type = Float
_Gs1000majorLow12Volt_Object = MibTableColumn
gs1000majorLow12Volt = _Gs1000majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 104),
    _Gs1000majorLow12Volt_Type()
)
gs1000majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000majorLow12Volt.setStatus("mandatory")
_Gs1000minorHigh12Volt_Type = Float
_Gs1000minorHigh12Volt_Object = MibTableColumn
gs1000minorHigh12Volt = _Gs1000minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 105),
    _Gs1000minorHigh12Volt_Type()
)
gs1000minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorHigh12Volt.setStatus("mandatory")
_Gs1000minorLow12Volt_Type = Float
_Gs1000minorLow12Volt_Object = MibTableColumn
gs1000minorLow12Volt = _Gs1000minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 106),
    _Gs1000minorLow12Volt_Type()
)
gs1000minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minorLow12Volt.setStatus("mandatory")
_Gs1000currentValue12Volt_Type = Float
_Gs1000currentValue12Volt_Object = MibTableColumn
gs1000currentValue12Volt = _Gs1000currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 107),
    _Gs1000currentValue12Volt_Type()
)
gs1000currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000currentValue12Volt.setStatus("mandatory")


class _Gs1000stateFlag12Volt_Type(Integer32):
    """Custom type gs1000stateFlag12Volt based on Integer32"""
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


_Gs1000stateFlag12Volt_Type.__name__ = "Integer32"
_Gs1000stateFlag12Volt_Object = MibTableColumn
gs1000stateFlag12Volt = _Gs1000stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 108),
    _Gs1000stateFlag12Volt_Type()
)
gs1000stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateFlag12Volt.setStatus("mandatory")
_Gs1000minValue12Volt_Type = Float
_Gs1000minValue12Volt_Object = MibTableColumn
gs1000minValue12Volt = _Gs1000minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 109),
    _Gs1000minValue12Volt_Type()
)
gs1000minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000minValue12Volt.setStatus("mandatory")
_Gs1000maxValue12Volt_Type = Float
_Gs1000maxValue12Volt_Object = MibTableColumn
gs1000maxValue12Volt = _Gs1000maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 110),
    _Gs1000maxValue12Volt_Type()
)
gs1000maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000maxValue12Volt.setStatus("mandatory")


class _Gs1000alarmState12Volt_Type(Integer32):
    """Custom type gs1000alarmState12Volt based on Integer32"""
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


_Gs1000alarmState12Volt_Type.__name__ = "Integer32"
_Gs1000alarmState12Volt_Object = MibTableColumn
gs1000alarmState12Volt = _Gs1000alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 2, 1, 111),
    _Gs1000alarmState12Volt_Type()
)
gs1000alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000alarmState12Volt.setStatus("mandatory")
_Gx2gs1000DigitalTable_Object = MibTable
gx2gs1000DigitalTable = _Gx2gs1000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3)
)
if mibBuilder.loadTexts:
    gx2gs1000DigitalTable.setStatus("mandatory")
_Gx2gs1000DigitalEntry_Object = MibTableRow
gx2gs1000DigitalEntry = _Gx2gs1000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2)
)
gx2gs1000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2GS1000-MIB", "gx2gs1000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2gs1000DigitalEntry.setStatus("mandatory")


class _Gx2gs1000DigitalTableIndex_Type(Integer32):
    """Custom type gx2gs1000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2gs1000DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2gs1000DigitalTableIndex_Object = MibTableColumn
gx2gs1000DigitalTableIndex = _Gx2gs1000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 1),
    _Gx2gs1000DigitalTableIndex_Type()
)
gx2gs1000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2gs1000DigitalTableIndex.setStatus("mandatory")


class _Gs1000labelRfInput_Type(DisplayString):
    """Custom type gs1000labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelRfInput_Type.__name__ = "DisplayString"
_Gs1000labelRfInput_Object = MibTableColumn
gs1000labelRfInput = _Gs1000labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 2),
    _Gs1000labelRfInput_Type()
)
gs1000labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelRfInput.setStatus("optional")


class _Gs1000enumRfInput_Type(DisplayString):
    """Custom type gs1000enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumRfInput_Type.__name__ = "DisplayString"
_Gs1000enumRfInput_Object = MibTableColumn
gs1000enumRfInput = _Gs1000enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 3),
    _Gs1000enumRfInput_Type()
)
gs1000enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumRfInput.setStatus("optional")


class _Gs1000valueRfInput_Type(Integer32):
    """Custom type gs1000valueRfInput based on Integer32"""
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


_Gs1000valueRfInput_Type.__name__ = "Integer32"
_Gs1000valueRfInput_Object = MibTableColumn
gs1000valueRfInput = _Gs1000valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 4),
    _Gs1000valueRfInput_Type()
)
gs1000valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueRfInput.setStatus("mandatory")


class _Gs1000stateflagRfInput_Type(Integer32):
    """Custom type gs1000stateflagRfInput based on Integer32"""
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


_Gs1000stateflagRfInput_Type.__name__ = "Integer32"
_Gs1000stateflagRfInput_Object = MibTableColumn
gs1000stateflagRfInput = _Gs1000stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 5),
    _Gs1000stateflagRfInput_Type()
)
gs1000stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagRfInput.setStatus("mandatory")


class _Gs1000labelOptOutput_Type(DisplayString):
    """Custom type gs1000labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelOptOutput_Type.__name__ = "DisplayString"
_Gs1000labelOptOutput_Object = MibTableColumn
gs1000labelOptOutput = _Gs1000labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 6),
    _Gs1000labelOptOutput_Type()
)
gs1000labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelOptOutput.setStatus("optional")


class _Gs1000enumOptOutput_Type(DisplayString):
    """Custom type gs1000enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumOptOutput_Type.__name__ = "DisplayString"
_Gs1000enumOptOutput_Object = MibTableColumn
gs1000enumOptOutput = _Gs1000enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 7),
    _Gs1000enumOptOutput_Type()
)
gs1000enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumOptOutput.setStatus("optional")


class _Gs1000valueOptOutput_Type(Integer32):
    """Custom type gs1000valueOptOutput based on Integer32"""
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


_Gs1000valueOptOutput_Type.__name__ = "Integer32"
_Gs1000valueOptOutput_Object = MibTableColumn
gs1000valueOptOutput = _Gs1000valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 8),
    _Gs1000valueOptOutput_Type()
)
gs1000valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueOptOutput.setStatus("mandatory")


class _Gs1000stateflagOptOutput_Type(Integer32):
    """Custom type gs1000stateflagOptOutput based on Integer32"""
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


_Gs1000stateflagOptOutput_Type.__name__ = "Integer32"
_Gs1000stateflagOptOutput_Object = MibTableColumn
gs1000stateflagOptOutput = _Gs1000stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 9),
    _Gs1000stateflagOptOutput_Type()
)
gs1000stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagOptOutput.setStatus("mandatory")


class _Gs1000labelLaserMode_Type(DisplayString):
    """Custom type gs1000labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelLaserMode_Type.__name__ = "DisplayString"
_Gs1000labelLaserMode_Object = MibTableColumn
gs1000labelLaserMode = _Gs1000labelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 10),
    _Gs1000labelLaserMode_Type()
)
gs1000labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelLaserMode.setStatus("optional")


class _Gs1000enumLaserMode_Type(DisplayString):
    """Custom type gs1000enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumLaserMode_Type.__name__ = "DisplayString"
_Gs1000enumLaserMode_Object = MibTableColumn
gs1000enumLaserMode = _Gs1000enumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 11),
    _Gs1000enumLaserMode_Type()
)
gs1000enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumLaserMode.setStatus("optional")


class _Gs1000valueLaserMode_Type(Integer32):
    """Custom type gs1000valueLaserMode based on Integer32"""
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


_Gs1000valueLaserMode_Type.__name__ = "Integer32"
_Gs1000valueLaserMode_Object = MibTableColumn
gs1000valueLaserMode = _Gs1000valueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 12),
    _Gs1000valueLaserMode_Type()
)
gs1000valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueLaserMode.setStatus("mandatory")


class _Gs1000stateflagLaserMode_Type(Integer32):
    """Custom type gs1000stateflagLaserMode based on Integer32"""
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


_Gs1000stateflagLaserMode_Type.__name__ = "Integer32"
_Gs1000stateflagLaserMode_Object = MibTableColumn
gs1000stateflagLaserMode = _Gs1000stateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 13),
    _Gs1000stateflagLaserMode_Type()
)
gs1000stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagLaserMode.setStatus("mandatory")


class _Gs1000labelAttenSetting_Type(DisplayString):
    """Custom type gs1000labelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelAttenSetting_Type.__name__ = "DisplayString"
_Gs1000labelAttenSetting_Object = MibTableColumn
gs1000labelAttenSetting = _Gs1000labelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 14),
    _Gs1000labelAttenSetting_Type()
)
gs1000labelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelAttenSetting.setStatus("optional")


class _Gs1000enumAttenSetting_Type(DisplayString):
    """Custom type gs1000enumAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumAttenSetting_Type.__name__ = "DisplayString"
_Gs1000enumAttenSetting_Object = MibTableColumn
gs1000enumAttenSetting = _Gs1000enumAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 15),
    _Gs1000enumAttenSetting_Type()
)
gs1000enumAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumAttenSetting.setStatus("optional")


class _Gs1000valueAttenSetting_Type(Integer32):
    """Custom type gs1000valueAttenSetting based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("attn0pt0", 1),
          ("attn0pt5", 2),
          ("attn10pt0", 21),
          ("attn10pt5", 22),
          ("attn11pt0", 23),
          ("attn11pt5", 24),
          ("attn12pt0", 25),
          ("attn1pt0", 3),
          ("attn1pt5", 4),
          ("attn2pt0", 5),
          ("attn2pt5", 6),
          ("attn3pt0", 7),
          ("attn3pt5", 8),
          ("attn4pt0", 9),
          ("attn4pt5", 10),
          ("attn5pt0", 11),
          ("attn5pt5", 12),
          ("attn6pt0", 13),
          ("attn6pt5", 14),
          ("attn7pt0", 15),
          ("attn7pt5", 16),
          ("attn8pt0", 17),
          ("attn8pt5", 18),
          ("attn9pt0", 19),
          ("attn9pt5", 20))
    )


_Gs1000valueAttenSetting_Type.__name__ = "Integer32"
_Gs1000valueAttenSetting_Object = MibTableColumn
gs1000valueAttenSetting = _Gs1000valueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 16),
    _Gs1000valueAttenSetting_Type()
)
gs1000valueAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueAttenSetting.setStatus("mandatory")


class _Gs1000stateflagAttenSetting_Type(Integer32):
    """Custom type gs1000stateflagAttenSetting based on Integer32"""
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


_Gs1000stateflagAttenSetting_Type.__name__ = "Integer32"
_Gs1000stateflagAttenSetting_Object = MibTableColumn
gs1000stateflagAttenSetting = _Gs1000stateflagAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 17),
    _Gs1000stateflagAttenSetting_Type()
)
gs1000stateflagAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagAttenSetting.setStatus("mandatory")


class _Gs1000labelLaserSecMode_Type(DisplayString):
    """Custom type gs1000labelLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelLaserSecMode_Type.__name__ = "DisplayString"
_Gs1000labelLaserSecMode_Object = MibTableColumn
gs1000labelLaserSecMode = _Gs1000labelLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 18),
    _Gs1000labelLaserSecMode_Type()
)
gs1000labelLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelLaserSecMode.setStatus("optional")


class _Gs1000enumLaserSecMode_Type(DisplayString):
    """Custom type gs1000enumLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumLaserSecMode_Type.__name__ = "DisplayString"
_Gs1000enumLaserSecMode_Object = MibTableColumn
gs1000enumLaserSecMode = _Gs1000enumLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 19),
    _Gs1000enumLaserSecMode_Type()
)
gs1000enumLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumLaserSecMode.setStatus("optional")


class _Gs1000valueLaserSecMode_Type(Integer32):
    """Custom type gs1000valueLaserSecMode based on Integer32"""
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


_Gs1000valueLaserSecMode_Type.__name__ = "Integer32"
_Gs1000valueLaserSecMode_Object = MibTableColumn
gs1000valueLaserSecMode = _Gs1000valueLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 20),
    _Gs1000valueLaserSecMode_Type()
)
gs1000valueLaserSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueLaserSecMode.setStatus("mandatory")


class _Gs1000stateflagLaserSecMode_Type(Integer32):
    """Custom type gs1000stateflagLaserSecMode based on Integer32"""
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


_Gs1000stateflagLaserSecMode_Type.__name__ = "Integer32"
_Gs1000stateflagLaserSecMode_Object = MibTableColumn
gs1000stateflagLaserSecMode = _Gs1000stateflagLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 21),
    _Gs1000stateflagLaserSecMode_Type()
)
gs1000stateflagLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagLaserSecMode.setStatus("mandatory")


class _Gs1000labelVideoOffset_Type(DisplayString):
    """Custom type gs1000labelVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelVideoOffset_Type.__name__ = "DisplayString"
_Gs1000labelVideoOffset_Object = MibTableColumn
gs1000labelVideoOffset = _Gs1000labelVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 22),
    _Gs1000labelVideoOffset_Type()
)
gs1000labelVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelVideoOffset.setStatus("optional")


class _Gs1000enumVideoOffset_Type(DisplayString):
    """Custom type gs1000enumVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumVideoOffset_Type.__name__ = "DisplayString"
_Gs1000enumVideoOffset_Object = MibTableColumn
gs1000enumVideoOffset = _Gs1000enumVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 23),
    _Gs1000enumVideoOffset_Type()
)
gs1000enumVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumVideoOffset.setStatus("optional")


class _Gs1000valueVideoOffset_Type(Integer32):
    """Custom type gs1000valueVideoOffset based on Integer32"""
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
        *(("minus1dB", 1),
          ("minus2dB", 2),
          ("minus3dB", 3),
          ("minus4dB", 4),
          ("minus5dB", 5))
    )


_Gs1000valueVideoOffset_Type.__name__ = "Integer32"
_Gs1000valueVideoOffset_Object = MibTableColumn
gs1000valueVideoOffset = _Gs1000valueVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 24),
    _Gs1000valueVideoOffset_Type()
)
gs1000valueVideoOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueVideoOffset.setStatus("mandatory")


class _Gs1000stateflagVideoOffset_Type(Integer32):
    """Custom type gs1000stateflagVideoOffset based on Integer32"""
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


_Gs1000stateflagVideoOffset_Type.__name__ = "Integer32"
_Gs1000stateflagVideoOffset_Object = MibTableColumn
gs1000stateflagVideoOffset = _Gs1000stateflagVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 25),
    _Gs1000stateflagVideoOffset_Type()
)
gs1000stateflagVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagVideoOffset.setStatus("mandatory")


class _Gs1000labelFactoryDefault_Type(DisplayString):
    """Custom type gs1000labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelFactoryDefault_Type.__name__ = "DisplayString"
_Gs1000labelFactoryDefault_Object = MibTableColumn
gs1000labelFactoryDefault = _Gs1000labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 26),
    _Gs1000labelFactoryDefault_Type()
)
gs1000labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelFactoryDefault.setStatus("optional")


class _Gs1000enumFactoryDefault_Type(DisplayString):
    """Custom type gs1000enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000enumFactoryDefault_Type.__name__ = "DisplayString"
_Gs1000enumFactoryDefault_Object = MibTableColumn
gs1000enumFactoryDefault = _Gs1000enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 27),
    _Gs1000enumFactoryDefault_Type()
)
gs1000enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000enumFactoryDefault.setStatus("optional")


class _Gs1000valueFactoryDefault_Type(Integer32):
    """Custom type gs1000valueFactoryDefault based on Integer32"""
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


_Gs1000valueFactoryDefault_Type.__name__ = "Integer32"
_Gs1000valueFactoryDefault_Object = MibTableColumn
gs1000valueFactoryDefault = _Gs1000valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 28),
    _Gs1000valueFactoryDefault_Type()
)
gs1000valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs1000valueFactoryDefault.setStatus("mandatory")


class _Gs1000stateflagFactoryDefault_Type(Integer32):
    """Custom type gs1000stateflagFactoryDefault based on Integer32"""
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


_Gs1000stateflagFactoryDefault_Type.__name__ = "Integer32"
_Gs1000stateflagFactoryDefault_Object = MibTableColumn
gs1000stateflagFactoryDefault = _Gs1000stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 3, 2, 29),
    _Gs1000stateflagFactoryDefault_Type()
)
gs1000stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagFactoryDefault.setStatus("mandatory")
_Gx2gs1000StatusTable_Object = MibTable
gx2gs1000StatusTable = _Gx2gs1000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4)
)
if mibBuilder.loadTexts:
    gx2gs1000StatusTable.setStatus("mandatory")
_Gx2gs1000StatusEntry_Object = MibTableRow
gx2gs1000StatusEntry = _Gx2gs1000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3)
)
gx2gs1000StatusEntry.setIndexNames(
    (0, "OMNI-gx2GS1000-MIB", "gx2gs1000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2gs1000StatusEntry.setStatus("mandatory")


class _Gx2gs1000StatusTableIndex_Type(Integer32):
    """Custom type gx2gs1000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2gs1000StatusTableIndex_Type.__name__ = "Integer32"
_Gx2gs1000StatusTableIndex_Object = MibTableColumn
gx2gs1000StatusTableIndex = _Gx2gs1000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 1),
    _Gx2gs1000StatusTableIndex_Type()
)
gx2gs1000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2gs1000StatusTableIndex.setStatus("mandatory")


class _Gs1000labelBoot_Type(DisplayString):
    """Custom type gs1000labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelBoot_Type.__name__ = "DisplayString"
_Gs1000labelBoot_Object = MibTableColumn
gs1000labelBoot = _Gs1000labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 2),
    _Gs1000labelBoot_Type()
)
gs1000labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelBoot.setStatus("optional")


class _Gs1000valueBoot_Type(Integer32):
    """Custom type gs1000valueBoot based on Integer32"""
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


_Gs1000valueBoot_Type.__name__ = "Integer32"
_Gs1000valueBoot_Object = MibTableColumn
gs1000valueBoot = _Gs1000valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 3),
    _Gs1000valueBoot_Type()
)
gs1000valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueBoot.setStatus("mandatory")


class _Gs1000stateflagBoot_Type(Integer32):
    """Custom type gs1000stateflagBoot based on Integer32"""
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


_Gs1000stateflagBoot_Type.__name__ = "Integer32"
_Gs1000stateflagBoot_Object = MibTableColumn
gs1000stateflagBoot = _Gs1000stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 4),
    _Gs1000stateflagBoot_Type()
)
gs1000stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagBoot.setStatus("mandatory")


class _Gs1000labelFlash_Type(DisplayString):
    """Custom type gs1000labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelFlash_Type.__name__ = "DisplayString"
_Gs1000labelFlash_Object = MibTableColumn
gs1000labelFlash = _Gs1000labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 5),
    _Gs1000labelFlash_Type()
)
gs1000labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelFlash.setStatus("optional")


class _Gs1000valueFlash_Type(Integer32):
    """Custom type gs1000valueFlash based on Integer32"""
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


_Gs1000valueFlash_Type.__name__ = "Integer32"
_Gs1000valueFlash_Object = MibTableColumn
gs1000valueFlash = _Gs1000valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 6),
    _Gs1000valueFlash_Type()
)
gs1000valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueFlash.setStatus("mandatory")


class _Gs1000stateflagFlash_Type(Integer32):
    """Custom type gs1000stateflagFlash based on Integer32"""
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


_Gs1000stateflagFlash_Type.__name__ = "Integer32"
_Gs1000stateflagFlash_Object = MibTableColumn
gs1000stateflagFlash = _Gs1000stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 7),
    _Gs1000stateflagFlash_Type()
)
gs1000stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagFlash.setStatus("mandatory")


class _Gs1000labelFactoryDataCRC_Type(DisplayString):
    """Custom type gs1000labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Gs1000labelFactoryDataCRC_Object = MibTableColumn
gs1000labelFactoryDataCRC = _Gs1000labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 8),
    _Gs1000labelFactoryDataCRC_Type()
)
gs1000labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelFactoryDataCRC.setStatus("optional")


class _Gs1000valueFactoryDataCRC_Type(Integer32):
    """Custom type gs1000valueFactoryDataCRC based on Integer32"""
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


_Gs1000valueFactoryDataCRC_Type.__name__ = "Integer32"
_Gs1000valueFactoryDataCRC_Object = MibTableColumn
gs1000valueFactoryDataCRC = _Gs1000valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 9),
    _Gs1000valueFactoryDataCRC_Type()
)
gs1000valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueFactoryDataCRC.setStatus("mandatory")


class _Gs1000stateflagFactoryDataCRC_Type(Integer32):
    """Custom type gs1000stateflagFactoryDataCRC based on Integer32"""
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


_Gs1000stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Gs1000stateflagFactoryDataCRC_Object = MibTableColumn
gs1000stateflagFactoryDataCRC = _Gs1000stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 10),
    _Gs1000stateflagFactoryDataCRC_Type()
)
gs1000stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagFactoryDataCRC.setStatus("mandatory")


class _Gs1000labelLaserDataCRC_Type(DisplayString):
    """Custom type gs1000labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelLaserDataCRC_Type.__name__ = "DisplayString"
_Gs1000labelLaserDataCRC_Object = MibTableColumn
gs1000labelLaserDataCRC = _Gs1000labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 11),
    _Gs1000labelLaserDataCRC_Type()
)
gs1000labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelLaserDataCRC.setStatus("optional")


class _Gs1000valueLaserDataCRC_Type(Integer32):
    """Custom type gs1000valueLaserDataCRC based on Integer32"""
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


_Gs1000valueLaserDataCRC_Type.__name__ = "Integer32"
_Gs1000valueLaserDataCRC_Object = MibTableColumn
gs1000valueLaserDataCRC = _Gs1000valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 12),
    _Gs1000valueLaserDataCRC_Type()
)
gs1000valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueLaserDataCRC.setStatus("mandatory")


class _Gs1000stateflagLaserDataCRC_Type(Integer32):
    """Custom type gs1000stateflagLaserDataCRC based on Integer32"""
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


_Gs1000stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Gs1000stateflagLaserDataCRC_Object = MibTableColumn
gs1000stateflagLaserDataCRC = _Gs1000stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 13),
    _Gs1000stateflagLaserDataCRC_Type()
)
gs1000stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagLaserDataCRC.setStatus("mandatory")


class _Gs1000labelAlarmDataCrc_Type(DisplayString):
    """Custom type gs1000labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Gs1000labelAlarmDataCrc_Object = MibTableColumn
gs1000labelAlarmDataCrc = _Gs1000labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 14),
    _Gs1000labelAlarmDataCrc_Type()
)
gs1000labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelAlarmDataCrc.setStatus("optional")


class _Gs1000valueAlarmDataCrc_Type(Integer32):
    """Custom type gs1000valueAlarmDataCrc based on Integer32"""
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


_Gs1000valueAlarmDataCrc_Type.__name__ = "Integer32"
_Gs1000valueAlarmDataCrc_Object = MibTableColumn
gs1000valueAlarmDataCrc = _Gs1000valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 15),
    _Gs1000valueAlarmDataCrc_Type()
)
gs1000valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueAlarmDataCrc.setStatus("mandatory")


class _Gs1000stateflagAlarmDataCrc_Type(Integer32):
    """Custom type gs1000stateflagAlarmDataCrc based on Integer32"""
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


_Gs1000stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Gs1000stateflagAlarmDataCrc_Object = MibTableColumn
gs1000stateflagAlarmDataCrc = _Gs1000stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 16),
    _Gs1000stateflagAlarmDataCrc_Type()
)
gs1000stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagAlarmDataCrc.setStatus("mandatory")


class _Gs1000labelRFInputStatus_Type(DisplayString):
    """Custom type gs1000labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000labelRFInputStatus_Type.__name__ = "DisplayString"
_Gs1000labelRFInputStatus_Object = MibTableColumn
gs1000labelRFInputStatus = _Gs1000labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 17),
    _Gs1000labelRFInputStatus_Type()
)
gs1000labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000labelRFInputStatus.setStatus("optional")


class _Gs1000valueRFInputStatus_Type(Integer32):
    """Custom type gs1000valueRFInputStatus based on Integer32"""
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


_Gs1000valueRFInputStatus_Type.__name__ = "Integer32"
_Gs1000valueRFInputStatus_Object = MibTableColumn
gs1000valueRFInputStatus = _Gs1000valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 18),
    _Gs1000valueRFInputStatus_Type()
)
gs1000valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000valueRFInputStatus.setStatus("mandatory")


class _Gs1000stateflagRFInputStatus_Type(Integer32):
    """Custom type gs1000stateflagRFInputStatus based on Integer32"""
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


_Gs1000stateflagRFInputStatus_Type.__name__ = "Integer32"
_Gs1000stateflagRFInputStatus_Object = MibTableColumn
gs1000stateflagRFInputStatus = _Gs1000stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 4, 3, 19),
    _Gs1000stateflagRFInputStatus_Type()
)
gs1000stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000stateflagRFInputStatus.setStatus("mandatory")
_Gx2gs1000FactoryTable_Object = MibTable
gx2gs1000FactoryTable = _Gx2gs1000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5)
)
if mibBuilder.loadTexts:
    gx2gs1000FactoryTable.setStatus("mandatory")
_Gx2gs1000FactoryEntry_Object = MibTableRow
gx2gs1000FactoryEntry = _Gx2gs1000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4)
)
gx2gs1000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2GS1000-MIB", "gx2gs1000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2gs1000FactoryEntry.setStatus("mandatory")


class _Gx2gs1000FactoryTableIndex_Type(Integer32):
    """Custom type gx2gs1000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2gs1000FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2gs1000FactoryTableIndex_Object = MibTableColumn
gx2gs1000FactoryTableIndex = _Gx2gs1000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 1),
    _Gx2gs1000FactoryTableIndex_Type()
)
gx2gs1000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2gs1000FactoryTableIndex.setStatus("mandatory")
_Gs1000bootControlByteValue_Type = Integer32
_Gs1000bootControlByteValue_Object = MibTableColumn
gs1000bootControlByteValue = _Gs1000bootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 2),
    _Gs1000bootControlByteValue_Type()
)
gs1000bootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000bootControlByteValue.setStatus("mandatory")
_Gs1000bootStatusByteValue_Type = Integer32
_Gs1000bootStatusByteValue_Object = MibTableColumn
gs1000bootStatusByteValue = _Gs1000bootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 3),
    _Gs1000bootStatusByteValue_Type()
)
gs1000bootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000bootStatusByteValue.setStatus("mandatory")
_Gs1000bank1CRCValue_Type = Integer32
_Gs1000bank1CRCValue_Object = MibTableColumn
gs1000bank1CRCValue = _Gs1000bank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 4),
    _Gs1000bank1CRCValue_Type()
)
gs1000bank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000bank1CRCValue.setStatus("mandatory")
_Gs1000bank2CRCValue_Type = Integer32
_Gs1000bank2CRCValue_Object = MibTableColumn
gs1000bank2CRCValue = _Gs1000bank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 5),
    _Gs1000bank2CRCValue_Type()
)
gs1000bank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000bank2CRCValue.setStatus("mandatory")
_Gs1000prgEEPROMByteValue_Type = Integer32
_Gs1000prgEEPROMByteValue_Object = MibTableColumn
gs1000prgEEPROMByteValue = _Gs1000prgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 6),
    _Gs1000prgEEPROMByteValue_Type()
)
gs1000prgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000prgEEPROMByteValue.setStatus("mandatory")
_Gs1000factoryCRCValue_Type = Integer32
_Gs1000factoryCRCValue_Object = MibTableColumn
gs1000factoryCRCValue = _Gs1000factoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 7),
    _Gs1000factoryCRCValue_Type()
)
gs1000factoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000factoryCRCValue.setStatus("mandatory")


class _Gs1000calculateCRCValue_Type(Integer32):
    """Custom type gs1000calculateCRCValue based on Integer32"""
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


_Gs1000calculateCRCValue_Type.__name__ = "Integer32"
_Gs1000calculateCRCValue_Object = MibTableColumn
gs1000calculateCRCValue = _Gs1000calculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 8),
    _Gs1000calculateCRCValue_Type()
)
gs1000calculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000calculateCRCValue.setStatus("mandatory")
_Gs1000hourMeterValue_Type = Integer32
_Gs1000hourMeterValue_Object = MibTableColumn
gs1000hourMeterValue = _Gs1000hourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 9),
    _Gs1000hourMeterValue_Type()
)
gs1000hourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000hourMeterValue.setStatus("mandatory")
_Gs1000flashPrgCntAValue_Type = Integer32
_Gs1000flashPrgCntAValue_Object = MibTableColumn
gs1000flashPrgCntAValue = _Gs1000flashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 10),
    _Gs1000flashPrgCntAValue_Type()
)
gs1000flashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000flashPrgCntAValue.setStatus("mandatory")
_Gs1000flashPrgCntBValue_Type = Integer32
_Gs1000flashPrgCntBValue_Object = MibTableColumn
gs1000flashPrgCntBValue = _Gs1000flashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 11),
    _Gs1000flashPrgCntBValue_Type()
)
gs1000flashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000flashPrgCntBValue.setStatus("mandatory")


class _Gs1000flashBankARevValue_Type(DisplayString):
    """Custom type gs1000flashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000flashBankARevValue_Type.__name__ = "DisplayString"
_Gs1000flashBankARevValue_Object = MibTableColumn
gs1000flashBankARevValue = _Gs1000flashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 12),
    _Gs1000flashBankARevValue_Type()
)
gs1000flashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000flashBankARevValue.setStatus("mandatory")


class _Gs1000flashBankBRevValue_Type(DisplayString):
    """Custom type gs1000flashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Gs1000flashBankBRevValue_Type.__name__ = "DisplayString"
_Gs1000flashBankBRevValue_Object = MibTableColumn
gs1000flashBankBRevValue = _Gs1000flashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 5, 4, 13),
    _Gs1000flashBankBRevValue_Type()
)
gs1000flashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs1000flashBankBRevValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapGS1000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 1)
)
trapGS1000ConfigChangeInteger.setObjects(
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
    trapGS1000ConfigChangeInteger.setStatus(
        ""
    )

trapGS1000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 2)
)
trapGS1000ConfigChangeDisplayString.setObjects(
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
    trapGS1000ConfigChangeDisplayString.setStatus(
        ""
    )

trapGS1000RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 3)
)
trapGS1000RFInputAlarm.setObjects(
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
    trapGS1000RFInputAlarm.setStatus(
        ""
    )

trapGS1000RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 4)
)
trapGS1000RFOverloadAlarm.setObjects(
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
    trapGS1000RFOverloadAlarm.setStatus(
        ""
    )

trapGS1000RFOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 5)
)
trapGS1000RFOffsetAlarm.setObjects(
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
    trapGS1000RFOffsetAlarm.setStatus(
        ""
    )

trapGS1000OpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 6)
)
trapGS1000OpticalPowerAlarm.setObjects(
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
    trapGS1000OpticalPowerAlarm.setStatus(
        ""
    )

trapGS1000LaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 7)
)
trapGS1000LaserBiasAlarm.setObjects(
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
    trapGS1000LaserBiasAlarm.setStatus(
        ""
    )

trapGS1000LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 8)
)
trapGS1000LaserTempAlarm.setObjects(
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
    trapGS1000LaserTempAlarm.setStatus(
        ""
    )

trapGS1000TECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 9)
)
trapGS1000TECCurrentAlarm.setObjects(
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
    trapGS1000TECCurrentAlarm.setStatus(
        ""
    )

trapGS1000Fan1SpeedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 10)
)
trapGS1000Fan1SpeedAlarm.setObjects(
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
    trapGS1000Fan1SpeedAlarm.setStatus(
        ""
    )

trapGS1000Fan2SpeedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 11)
)
trapGS1000Fan2SpeedAlarm.setObjects(
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
    trapGS1000Fan2SpeedAlarm.setStatus(
        ""
    )

trapGS100012vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 12)
)
trapGS100012vAlarm.setObjects(
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
    trapGS100012vAlarm.setStatus(
        ""
    )

trapGS1000ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 13)
)
trapGS1000ModuleTempAlarm.setObjects(
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
    trapGS1000ModuleTempAlarm.setStatus(
        ""
    )

trapGS1000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 14)
)
trapGS1000FlashAlarm.setObjects(
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
    trapGS1000FlashAlarm.setStatus(
        ""
    )

trapGS1000LaserBiasCntLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 15)
)
trapGS1000LaserBiasCntLoopAlarm.setObjects(
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
    trapGS1000LaserBiasCntLoopAlarm.setStatus(
        ""
    )

trapGS1000BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 16)
)
trapGS1000BankBootAlarm.setObjects(
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
    trapGS1000BankBootAlarm.setStatus(
        ""
    )

trapGS1000LaserBiasCntLoopInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 17)
)
trapGS1000LaserBiasCntLoopInitAlarm.setObjects(
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
    trapGS1000LaserBiasCntLoopInitAlarm.setStatus(
        ""
    )

trapGS1000RFParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 18)
)
trapGS1000RFParamInitAlarm.setObjects(
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
    trapGS1000RFParamInitAlarm.setStatus(
        ""
    )

trapGS1000TECParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 19)
)
trapGS1000TECParamInitAlarm.setObjects(
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
    trapGS1000TECParamInitAlarm.setStatus(
        ""
    )

trapGS1000AttnTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 20)
)
trapGS1000AttnTableInitAlarm.setObjects(
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
    trapGS1000AttnTableInitAlarm.setStatus(
        ""
    )

trapGS1000PowerMeterTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 21)
)
trapGS1000PowerMeterTableInitAlarm.setObjects(
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
    trapGS1000PowerMeterTableInitAlarm.setStatus(
        ""
    )

trapGS1000LaserDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 22)
)
trapGS1000LaserDataCRCAlarm.setObjects(
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
    trapGS1000LaserDataCRCAlarm.setStatus(
        ""
    )

trapGS1000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 23)
)
trapGS1000AlarmDataCRCAlarm.setObjects(
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
    trapGS1000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapGS1000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 24)
)
trapGS1000FactoryDataCRCAlarm.setObjects(
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
    trapGS1000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapGS1000UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 25)
)
trapGS1000UserRFOffAlarm.setObjects(
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
    trapGS1000UserRFOffAlarm.setStatus(
        ""
    )

trapGS1000UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 26)
)
trapGS1000UserOpticalOffAlarm.setObjects(
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
    trapGS1000UserOpticalOffAlarm.setStatus(
        ""
    )

trapGS1000ResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36, 0, 27)
)
trapGS1000ResetFactoryDefaultAlarm.setObjects(
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
    trapGS1000ResetFactoryDefaultAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2GS1000-MIB",
    **{"Float": Float,
       "trapGS1000ConfigChangeInteger": trapGS1000ConfigChangeInteger,
       "trapGS1000ConfigChangeDisplayString": trapGS1000ConfigChangeDisplayString,
       "trapGS1000RFInputAlarm": trapGS1000RFInputAlarm,
       "trapGS1000RFOverloadAlarm": trapGS1000RFOverloadAlarm,
       "trapGS1000RFOffsetAlarm": trapGS1000RFOffsetAlarm,
       "trapGS1000OpticalPowerAlarm": trapGS1000OpticalPowerAlarm,
       "trapGS1000LaserBiasAlarm": trapGS1000LaserBiasAlarm,
       "trapGS1000LaserTempAlarm": trapGS1000LaserTempAlarm,
       "trapGS1000TECCurrentAlarm": trapGS1000TECCurrentAlarm,
       "trapGS1000Fan1SpeedAlarm": trapGS1000Fan1SpeedAlarm,
       "trapGS1000Fan2SpeedAlarm": trapGS1000Fan2SpeedAlarm,
       "trapGS100012vAlarm": trapGS100012vAlarm,
       "trapGS1000ModuleTempAlarm": trapGS1000ModuleTempAlarm,
       "trapGS1000FlashAlarm": trapGS1000FlashAlarm,
       "trapGS1000LaserBiasCntLoopAlarm": trapGS1000LaserBiasCntLoopAlarm,
       "trapGS1000BankBootAlarm": trapGS1000BankBootAlarm,
       "trapGS1000LaserBiasCntLoopInitAlarm": trapGS1000LaserBiasCntLoopInitAlarm,
       "trapGS1000RFParamInitAlarm": trapGS1000RFParamInitAlarm,
       "trapGS1000TECParamInitAlarm": trapGS1000TECParamInitAlarm,
       "trapGS1000AttnTableInitAlarm": trapGS1000AttnTableInitAlarm,
       "trapGS1000PowerMeterTableInitAlarm": trapGS1000PowerMeterTableInitAlarm,
       "trapGS1000LaserDataCRCAlarm": trapGS1000LaserDataCRCAlarm,
       "trapGS1000AlarmDataCRCAlarm": trapGS1000AlarmDataCRCAlarm,
       "trapGS1000FactoryDataCRCAlarm": trapGS1000FactoryDataCRCAlarm,
       "trapGS1000UserRFOffAlarm": trapGS1000UserRFOffAlarm,
       "trapGS1000UserOpticalOffAlarm": trapGS1000UserOpticalOffAlarm,
       "trapGS1000ResetFactoryDefaultAlarm": trapGS1000ResetFactoryDefaultAlarm,
       "gx2gs1000Descriptor": gx2gs1000Descriptor,
       "gx2gs1000AnalogTable": gx2gs1000AnalogTable,
       "gx2gs1000AnalogEntry": gx2gs1000AnalogEntry,
       "gx2gs1000AnalogTableIndex": gx2gs1000AnalogTableIndex,
       "gs1000labelOffsetNomMonitor": gs1000labelOffsetNomMonitor,
       "gs1000uomOffsetNomMonitor": gs1000uomOffsetNomMonitor,
       "gs1000majorHighOffsetNomMonitor": gs1000majorHighOffsetNomMonitor,
       "gs1000majorLowOffsetNomMonitor": gs1000majorLowOffsetNomMonitor,
       "gs1000minorHighOffsetNomMonitor": gs1000minorHighOffsetNomMonitor,
       "gs1000minorLowOffsetNomMonitor": gs1000minorLowOffsetNomMonitor,
       "gs1000currentValueOffsetNomMonitor": gs1000currentValueOffsetNomMonitor,
       "gs1000stateFlagOffsetNomMonitor": gs1000stateFlagOffsetNomMonitor,
       "gs1000minValueOffsetNomMonitor": gs1000minValueOffsetNomMonitor,
       "gs1000maxValueOffsetNomMonitor": gs1000maxValueOffsetNomMonitor,
       "gs1000alarmStateOffsetNomMonitor": gs1000alarmStateOffsetNomMonitor,
       "gs1000labelOffsetNomCnt": gs1000labelOffsetNomCnt,
       "gs1000uomOffsetNomCnt": gs1000uomOffsetNomCnt,
       "gs1000majorHighOffsetNomCnt": gs1000majorHighOffsetNomCnt,
       "gs1000majorLowOffsetNomCnt": gs1000majorLowOffsetNomCnt,
       "gs1000minorHighOffsetNomCnt": gs1000minorHighOffsetNomCnt,
       "gs1000minorLowOffsetNomCnt": gs1000minorLowOffsetNomCnt,
       "gs1000currentValueOffsetNomCnt": gs1000currentValueOffsetNomCnt,
       "gs1000stateFlagOffsetNomCnt": gs1000stateFlagOffsetNomCnt,
       "gs1000minValueOffsetNomCnt": gs1000minValueOffsetNomCnt,
       "gs1000maxValueOffsetNomCnt": gs1000maxValueOffsetNomCnt,
       "gs1000alarmStateOffsetNomCnt": gs1000alarmStateOffsetNomCnt,
       "gs1000labelOptPower": gs1000labelOptPower,
       "gs1000uomOptPower": gs1000uomOptPower,
       "gs1000majorHighOptPower": gs1000majorHighOptPower,
       "gs1000majorLowOptPower": gs1000majorLowOptPower,
       "gs1000minorHighOptPower": gs1000minorHighOptPower,
       "gs1000minorLowOptPower": gs1000minorLowOptPower,
       "gs1000currentValueOptPower": gs1000currentValueOptPower,
       "gs1000stateFlagOptPower": gs1000stateFlagOptPower,
       "gs1000minValueOptPower": gs1000minValueOptPower,
       "gs1000maxValueOptPower": gs1000maxValueOptPower,
       "gs1000alarmStateOptPower": gs1000alarmStateOptPower,
       "gs1000labelLaserTemp": gs1000labelLaserTemp,
       "gs1000uomLaserTemp": gs1000uomLaserTemp,
       "gs1000majorHighLaserTemp": gs1000majorHighLaserTemp,
       "gs1000majorLowLaserTemp": gs1000majorLowLaserTemp,
       "gs1000minorHighLaserTemp": gs1000minorHighLaserTemp,
       "gs1000minorLowLaserTemp": gs1000minorLowLaserTemp,
       "gs1000currentValueLaserTemp": gs1000currentValueLaserTemp,
       "gs1000stateFlagLaserTemp": gs1000stateFlagLaserTemp,
       "gs1000minValueLaserTemp": gs1000minValueLaserTemp,
       "gs1000maxValueLaserTemp": gs1000maxValueLaserTemp,
       "gs1000alarmStateLaserTemp": gs1000alarmStateLaserTemp,
       "gs1000labelLaserBias": gs1000labelLaserBias,
       "gs1000uomLaserBias": gs1000uomLaserBias,
       "gs1000majorHighLaserBias": gs1000majorHighLaserBias,
       "gs1000majorLowLaserBias": gs1000majorLowLaserBias,
       "gs1000minorHighLaserBias": gs1000minorHighLaserBias,
       "gs1000minorLowLaserBias": gs1000minorLowLaserBias,
       "gs1000currentValueLaserBias": gs1000currentValueLaserBias,
       "gs1000stateFlagLaserBias": gs1000stateFlagLaserBias,
       "gs1000minValueLaserBias": gs1000minValueLaserBias,
       "gs1000maxValueLaserBias": gs1000maxValueLaserBias,
       "gs1000alarmStateLaserBias": gs1000alarmStateLaserBias,
       "gs1000labelTecCurrent": gs1000labelTecCurrent,
       "gs1000uomTecCurrent": gs1000uomTecCurrent,
       "gs1000majorHighTecCurrent": gs1000majorHighTecCurrent,
       "gs1000majorLowTecCurrent": gs1000majorLowTecCurrent,
       "gs1000minorHighTecCurrent": gs1000minorHighTecCurrent,
       "gs1000minorLowTecCurrent": gs1000minorLowTecCurrent,
       "gs1000currentValueTecCurrent": gs1000currentValueTecCurrent,
       "gs1000stateFlagTecCurrent": gs1000stateFlagTecCurrent,
       "gs1000minValueTecCurrent": gs1000minValueTecCurrent,
       "gs1000maxValueTecCurrent": gs1000maxValueTecCurrent,
       "gs1000alarmStateTecCurrent": gs1000alarmStateTecCurrent,
       "gs1000labelModuleTemp": gs1000labelModuleTemp,
       "gs1000uomModuleTemp": gs1000uomModuleTemp,
       "gs1000majorHighModuleTemp": gs1000majorHighModuleTemp,
       "gs1000majorLowModuleTemp": gs1000majorLowModuleTemp,
       "gs1000minorHighModuleTemp": gs1000minorHighModuleTemp,
       "gs1000minorLowModuleTemp": gs1000minorLowModuleTemp,
       "gs1000currentValueModuleTemp": gs1000currentValueModuleTemp,
       "gs1000stateFlagModuleTemp": gs1000stateFlagModuleTemp,
       "gs1000minValueModuleTemp": gs1000minValueModuleTemp,
       "gs1000maxValueModuleTemp": gs1000maxValueModuleTemp,
       "gs1000alarmStateModuleTemp": gs1000alarmStateModuleTemp,
       "gs1000labelFan1Speed": gs1000labelFan1Speed,
       "gs1000uomFan1Speed": gs1000uomFan1Speed,
       "gs1000majorHighFan1Speed": gs1000majorHighFan1Speed,
       "gs1000majorLowFan1Speed": gs1000majorLowFan1Speed,
       "gs1000minorHighFan1Speed": gs1000minorHighFan1Speed,
       "gs1000minorLowFan1Speed": gs1000minorLowFan1Speed,
       "gs1000currentValueFan1Speed": gs1000currentValueFan1Speed,
       "gs1000stateFlagFan1Speed": gs1000stateFlagFan1Speed,
       "gs1000minValueFan1Speed": gs1000minValueFan1Speed,
       "gs1000maxValueFan1Speed": gs1000maxValueFan1Speed,
       "gs1000alarmStateFan1Speed": gs1000alarmStateFan1Speed,
       "gs1000labelFan2Speed": gs1000labelFan2Speed,
       "gs1000uomFan2Speed": gs1000uomFan2Speed,
       "gs1000majorHighFan2Speed": gs1000majorHighFan2Speed,
       "gs1000majorLowFan2Speed": gs1000majorLowFan2Speed,
       "gs1000minorHighFan2Speed": gs1000minorHighFan2Speed,
       "gs1000minorLowFan2Speed": gs1000minorLowFan2Speed,
       "gs1000currentValueFan2Speed": gs1000currentValueFan2Speed,
       "gs1000stateFlagFan2Speed": gs1000stateFlagFan2Speed,
       "gs1000minValueFan2Speed": gs1000minValueFan2Speed,
       "gs1000maxValueFan2Speed": gs1000maxValueFan2Speed,
       "gs1000alarmStateFan2Speed": gs1000alarmStateFan2Speed,
       "gs1000label12Volt": gs1000label12Volt,
       "gs1000uom12Volt": gs1000uom12Volt,
       "gs1000majorHigh12Volt": gs1000majorHigh12Volt,
       "gs1000majorLow12Volt": gs1000majorLow12Volt,
       "gs1000minorHigh12Volt": gs1000minorHigh12Volt,
       "gs1000minorLow12Volt": gs1000minorLow12Volt,
       "gs1000currentValue12Volt": gs1000currentValue12Volt,
       "gs1000stateFlag12Volt": gs1000stateFlag12Volt,
       "gs1000minValue12Volt": gs1000minValue12Volt,
       "gs1000maxValue12Volt": gs1000maxValue12Volt,
       "gs1000alarmState12Volt": gs1000alarmState12Volt,
       "gx2gs1000DigitalTable": gx2gs1000DigitalTable,
       "gx2gs1000DigitalEntry": gx2gs1000DigitalEntry,
       "gx2gs1000DigitalTableIndex": gx2gs1000DigitalTableIndex,
       "gs1000labelRfInput": gs1000labelRfInput,
       "gs1000enumRfInput": gs1000enumRfInput,
       "gs1000valueRfInput": gs1000valueRfInput,
       "gs1000stateflagRfInput": gs1000stateflagRfInput,
       "gs1000labelOptOutput": gs1000labelOptOutput,
       "gs1000enumOptOutput": gs1000enumOptOutput,
       "gs1000valueOptOutput": gs1000valueOptOutput,
       "gs1000stateflagOptOutput": gs1000stateflagOptOutput,
       "gs1000labelLaserMode": gs1000labelLaserMode,
       "gs1000enumLaserMode": gs1000enumLaserMode,
       "gs1000valueLaserMode": gs1000valueLaserMode,
       "gs1000stateflagLaserMode": gs1000stateflagLaserMode,
       "gs1000labelAttenSetting": gs1000labelAttenSetting,
       "gs1000enumAttenSetting": gs1000enumAttenSetting,
       "gs1000valueAttenSetting": gs1000valueAttenSetting,
       "gs1000stateflagAttenSetting": gs1000stateflagAttenSetting,
       "gs1000labelLaserSecMode": gs1000labelLaserSecMode,
       "gs1000enumLaserSecMode": gs1000enumLaserSecMode,
       "gs1000valueLaserSecMode": gs1000valueLaserSecMode,
       "gs1000stateflagLaserSecMode": gs1000stateflagLaserSecMode,
       "gs1000labelVideoOffset": gs1000labelVideoOffset,
       "gs1000enumVideoOffset": gs1000enumVideoOffset,
       "gs1000valueVideoOffset": gs1000valueVideoOffset,
       "gs1000stateflagVideoOffset": gs1000stateflagVideoOffset,
       "gs1000labelFactoryDefault": gs1000labelFactoryDefault,
       "gs1000enumFactoryDefault": gs1000enumFactoryDefault,
       "gs1000valueFactoryDefault": gs1000valueFactoryDefault,
       "gs1000stateflagFactoryDefault": gs1000stateflagFactoryDefault,
       "gx2gs1000StatusTable": gx2gs1000StatusTable,
       "gx2gs1000StatusEntry": gx2gs1000StatusEntry,
       "gx2gs1000StatusTableIndex": gx2gs1000StatusTableIndex,
       "gs1000labelBoot": gs1000labelBoot,
       "gs1000valueBoot": gs1000valueBoot,
       "gs1000stateflagBoot": gs1000stateflagBoot,
       "gs1000labelFlash": gs1000labelFlash,
       "gs1000valueFlash": gs1000valueFlash,
       "gs1000stateflagFlash": gs1000stateflagFlash,
       "gs1000labelFactoryDataCRC": gs1000labelFactoryDataCRC,
       "gs1000valueFactoryDataCRC": gs1000valueFactoryDataCRC,
       "gs1000stateflagFactoryDataCRC": gs1000stateflagFactoryDataCRC,
       "gs1000labelLaserDataCRC": gs1000labelLaserDataCRC,
       "gs1000valueLaserDataCRC": gs1000valueLaserDataCRC,
       "gs1000stateflagLaserDataCRC": gs1000stateflagLaserDataCRC,
       "gs1000labelAlarmDataCrc": gs1000labelAlarmDataCrc,
       "gs1000valueAlarmDataCrc": gs1000valueAlarmDataCrc,
       "gs1000stateflagAlarmDataCrc": gs1000stateflagAlarmDataCrc,
       "gs1000labelRFInputStatus": gs1000labelRFInputStatus,
       "gs1000valueRFInputStatus": gs1000valueRFInputStatus,
       "gs1000stateflagRFInputStatus": gs1000stateflagRFInputStatus,
       "gx2gs1000FactoryTable": gx2gs1000FactoryTable,
       "gx2gs1000FactoryEntry": gx2gs1000FactoryEntry,
       "gx2gs1000FactoryTableIndex": gx2gs1000FactoryTableIndex,
       "gs1000bootControlByteValue": gs1000bootControlByteValue,
       "gs1000bootStatusByteValue": gs1000bootStatusByteValue,
       "gs1000bank1CRCValue": gs1000bank1CRCValue,
       "gs1000bank2CRCValue": gs1000bank2CRCValue,
       "gs1000prgEEPROMByteValue": gs1000prgEEPROMByteValue,
       "gs1000factoryCRCValue": gs1000factoryCRCValue,
       "gs1000calculateCRCValue": gs1000calculateCRCValue,
       "gs1000hourMeterValue": gs1000hourMeterValue,
       "gs1000flashPrgCntAValue": gs1000flashPrgCntAValue,
       "gs1000flashPrgCntBValue": gs1000flashPrgCntBValue,
       "gs1000flashBankARevValue": gs1000flashBankARevValue,
       "gs1000flashBankBRevValue": gs1000flashBankBRevValue}
)
