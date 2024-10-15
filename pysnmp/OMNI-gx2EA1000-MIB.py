# SNMP MIB module (OMNI-gx2EA1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2EA1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:18 2024
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

(gx2Ea1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Ea1000")

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

_Gx2ea1000Descriptor_ObjectIdentity = ObjectIdentity
gx2ea1000Descriptor = _Gx2ea1000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 1)
)
_Gx2ea1000AnalogTable_Object = MibTable
gx2ea1000AnalogTable = _Gx2ea1000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2)
)
if mibBuilder.loadTexts:
    gx2ea1000AnalogTable.setStatus("mandatory")
_Gx2ea1000AnalogEntry_Object = MibTableRow
gx2ea1000AnalogEntry = _Gx2ea1000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1)
)
gx2ea1000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2EA1000-MIB", "gx2ea1000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2ea1000AnalogEntry.setStatus("mandatory")


class _Gx2ea1000AnalogTableIndex_Type(Integer32):
    """Custom type gx2ea1000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2ea1000AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2ea1000AnalogTableIndex_Object = MibTableColumn
gx2ea1000AnalogTableIndex = _Gx2ea1000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 1),
    _Gx2ea1000AnalogTableIndex_Type()
)
gx2ea1000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2ea1000AnalogTableIndex.setStatus("mandatory")


class _Ea1000labelOffsetNomMonitor_Type(DisplayString):
    """Custom type ea1000labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Ea1000labelOffsetNomMonitor_Object = MibTableColumn
ea1000labelOffsetNomMonitor = _Ea1000labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 2),
    _Ea1000labelOffsetNomMonitor_Type()
)
ea1000labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelOffsetNomMonitor.setStatus("optional")


class _Ea1000uomOffsetNomMonitor_Type(DisplayString):
    """Custom type ea1000uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Ea1000uomOffsetNomMonitor_Object = MibTableColumn
ea1000uomOffsetNomMonitor = _Ea1000uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 3),
    _Ea1000uomOffsetNomMonitor_Type()
)
ea1000uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomOffsetNomMonitor.setStatus("optional")
_Ea1000majorHighOffsetNomMonitor_Type = Float
_Ea1000majorHighOffsetNomMonitor_Object = MibTableColumn
ea1000majorHighOffsetNomMonitor = _Ea1000majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 4),
    _Ea1000majorHighOffsetNomMonitor_Type()
)
ea1000majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighOffsetNomMonitor.setStatus("mandatory")
_Ea1000majorLowOffsetNomMonitor_Type = Float
_Ea1000majorLowOffsetNomMonitor_Object = MibTableColumn
ea1000majorLowOffsetNomMonitor = _Ea1000majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 5),
    _Ea1000majorLowOffsetNomMonitor_Type()
)
ea1000majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowOffsetNomMonitor.setStatus("mandatory")
_Ea1000minorHighOffsetNomMonitor_Type = Float
_Ea1000minorHighOffsetNomMonitor_Object = MibTableColumn
ea1000minorHighOffsetNomMonitor = _Ea1000minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 6),
    _Ea1000minorHighOffsetNomMonitor_Type()
)
ea1000minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighOffsetNomMonitor.setStatus("mandatory")
_Ea1000minorLowOffsetNomMonitor_Type = Float
_Ea1000minorLowOffsetNomMonitor_Object = MibTableColumn
ea1000minorLowOffsetNomMonitor = _Ea1000minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 7),
    _Ea1000minorLowOffsetNomMonitor_Type()
)
ea1000minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowOffsetNomMonitor.setStatus("mandatory")
_Ea1000currentValueOffsetNomMonitor_Type = Float
_Ea1000currentValueOffsetNomMonitor_Object = MibTableColumn
ea1000currentValueOffsetNomMonitor = _Ea1000currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 8),
    _Ea1000currentValueOffsetNomMonitor_Type()
)
ea1000currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueOffsetNomMonitor.setStatus("mandatory")


class _Ea1000stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type ea1000stateFlagOffsetNomMonitor based on Integer32"""
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


_Ea1000stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Ea1000stateFlagOffsetNomMonitor_Object = MibTableColumn
ea1000stateFlagOffsetNomMonitor = _Ea1000stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 9),
    _Ea1000stateFlagOffsetNomMonitor_Type()
)
ea1000stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagOffsetNomMonitor.setStatus("mandatory")
_Ea1000minValueOffsetNomMonitor_Type = Float
_Ea1000minValueOffsetNomMonitor_Object = MibTableColumn
ea1000minValueOffsetNomMonitor = _Ea1000minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 10),
    _Ea1000minValueOffsetNomMonitor_Type()
)
ea1000minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueOffsetNomMonitor.setStatus("mandatory")
_Ea1000maxValueOffsetNomMonitor_Type = Float
_Ea1000maxValueOffsetNomMonitor_Object = MibTableColumn
ea1000maxValueOffsetNomMonitor = _Ea1000maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 11),
    _Ea1000maxValueOffsetNomMonitor_Type()
)
ea1000maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueOffsetNomMonitor.setStatus("mandatory")


class _Ea1000alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type ea1000alarmStateOffsetNomMonitor based on Integer32"""
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


_Ea1000alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Ea1000alarmStateOffsetNomMonitor_Object = MibTableColumn
ea1000alarmStateOffsetNomMonitor = _Ea1000alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 12),
    _Ea1000alarmStateOffsetNomMonitor_Type()
)
ea1000alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Ea1000labelOffsetNomCnt_Type(DisplayString):
    """Custom type ea1000labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelOffsetNomCnt_Type.__name__ = "DisplayString"
_Ea1000labelOffsetNomCnt_Object = MibTableColumn
ea1000labelOffsetNomCnt = _Ea1000labelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 13),
    _Ea1000labelOffsetNomCnt_Type()
)
ea1000labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelOffsetNomCnt.setStatus("optional")


class _Ea1000uomOffsetNomCnt_Type(DisplayString):
    """Custom type ea1000uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomOffsetNomCnt_Type.__name__ = "DisplayString"
_Ea1000uomOffsetNomCnt_Object = MibTableColumn
ea1000uomOffsetNomCnt = _Ea1000uomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 14),
    _Ea1000uomOffsetNomCnt_Type()
)
ea1000uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomOffsetNomCnt.setStatus("optional")
_Ea1000majorHighOffsetNomCnt_Type = Float
_Ea1000majorHighOffsetNomCnt_Object = MibTableColumn
ea1000majorHighOffsetNomCnt = _Ea1000majorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 15),
    _Ea1000majorHighOffsetNomCnt_Type()
)
ea1000majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighOffsetNomCnt.setStatus("optional")
_Ea1000majorLowOffsetNomCnt_Type = Float
_Ea1000majorLowOffsetNomCnt_Object = MibTableColumn
ea1000majorLowOffsetNomCnt = _Ea1000majorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 16),
    _Ea1000majorLowOffsetNomCnt_Type()
)
ea1000majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowOffsetNomCnt.setStatus("optional")
_Ea1000minorHighOffsetNomCnt_Type = Float
_Ea1000minorHighOffsetNomCnt_Object = MibTableColumn
ea1000minorHighOffsetNomCnt = _Ea1000minorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 17),
    _Ea1000minorHighOffsetNomCnt_Type()
)
ea1000minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighOffsetNomCnt.setStatus("optional")
_Ea1000minorLowOffsetNomCnt_Type = Float
_Ea1000minorLowOffsetNomCnt_Object = MibTableColumn
ea1000minorLowOffsetNomCnt = _Ea1000minorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 18),
    _Ea1000minorLowOffsetNomCnt_Type()
)
ea1000minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowOffsetNomCnt.setStatus("optional")
_Ea1000currentValueOffsetNomCnt_Type = Float
_Ea1000currentValueOffsetNomCnt_Object = MibTableColumn
ea1000currentValueOffsetNomCnt = _Ea1000currentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 19),
    _Ea1000currentValueOffsetNomCnt_Type()
)
ea1000currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000currentValueOffsetNomCnt.setStatus("mandatory")


class _Ea1000stateFlagOffsetNomCnt_Type(Integer32):
    """Custom type ea1000stateFlagOffsetNomCnt based on Integer32"""
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


_Ea1000stateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_Ea1000stateFlagOffsetNomCnt_Object = MibTableColumn
ea1000stateFlagOffsetNomCnt = _Ea1000stateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 20),
    _Ea1000stateFlagOffsetNomCnt_Type()
)
ea1000stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagOffsetNomCnt.setStatus("mandatory")
_Ea1000minValueOffsetNomCnt_Type = Float
_Ea1000minValueOffsetNomCnt_Object = MibTableColumn
ea1000minValueOffsetNomCnt = _Ea1000minValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 21),
    _Ea1000minValueOffsetNomCnt_Type()
)
ea1000minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueOffsetNomCnt.setStatus("mandatory")
_Ea1000maxValueOffsetNomCnt_Type = Float
_Ea1000maxValueOffsetNomCnt_Object = MibTableColumn
ea1000maxValueOffsetNomCnt = _Ea1000maxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 22),
    _Ea1000maxValueOffsetNomCnt_Type()
)
ea1000maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueOffsetNomCnt.setStatus("mandatory")


class _Ea1000alarmStateOffsetNomCnt_Type(Integer32):
    """Custom type ea1000alarmStateOffsetNomCnt based on Integer32"""
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


_Ea1000alarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_Ea1000alarmStateOffsetNomCnt_Object = MibTableColumn
ea1000alarmStateOffsetNomCnt = _Ea1000alarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 23),
    _Ea1000alarmStateOffsetNomCnt_Type()
)
ea1000alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateOffsetNomCnt.setStatus("mandatory")


class _Ea1000labelOptPower_Type(DisplayString):
    """Custom type ea1000labelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelOptPower_Type.__name__ = "DisplayString"
_Ea1000labelOptPower_Object = MibTableColumn
ea1000labelOptPower = _Ea1000labelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 24),
    _Ea1000labelOptPower_Type()
)
ea1000labelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelOptPower.setStatus("optional")


class _Ea1000uomOptPower_Type(DisplayString):
    """Custom type ea1000uomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomOptPower_Type.__name__ = "DisplayString"
_Ea1000uomOptPower_Object = MibTableColumn
ea1000uomOptPower = _Ea1000uomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 25),
    _Ea1000uomOptPower_Type()
)
ea1000uomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomOptPower.setStatus("optional")
_Ea1000majorHighOptPower_Type = Float
_Ea1000majorHighOptPower_Object = MibTableColumn
ea1000majorHighOptPower = _Ea1000majorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 26),
    _Ea1000majorHighOptPower_Type()
)
ea1000majorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighOptPower.setStatus("mandatory")
_Ea1000majorLowOptPower_Type = Float
_Ea1000majorLowOptPower_Object = MibTableColumn
ea1000majorLowOptPower = _Ea1000majorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 27),
    _Ea1000majorLowOptPower_Type()
)
ea1000majorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowOptPower.setStatus("mandatory")
_Ea1000minorHighOptPower_Type = Float
_Ea1000minorHighOptPower_Object = MibTableColumn
ea1000minorHighOptPower = _Ea1000minorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 28),
    _Ea1000minorHighOptPower_Type()
)
ea1000minorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighOptPower.setStatus("optional")
_Ea1000minorLowOptPower_Type = Float
_Ea1000minorLowOptPower_Object = MibTableColumn
ea1000minorLowOptPower = _Ea1000minorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 29),
    _Ea1000minorLowOptPower_Type()
)
ea1000minorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowOptPower.setStatus("optional")
_Ea1000currentValueOptPower_Type = Float
_Ea1000currentValueOptPower_Object = MibTableColumn
ea1000currentValueOptPower = _Ea1000currentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 30),
    _Ea1000currentValueOptPower_Type()
)
ea1000currentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueOptPower.setStatus("mandatory")


class _Ea1000stateFlagOptPower_Type(Integer32):
    """Custom type ea1000stateFlagOptPower based on Integer32"""
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


_Ea1000stateFlagOptPower_Type.__name__ = "Integer32"
_Ea1000stateFlagOptPower_Object = MibTableColumn
ea1000stateFlagOptPower = _Ea1000stateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 31),
    _Ea1000stateFlagOptPower_Type()
)
ea1000stateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagOptPower.setStatus("mandatory")
_Ea1000minValueOptPower_Type = Float
_Ea1000minValueOptPower_Object = MibTableColumn
ea1000minValueOptPower = _Ea1000minValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 32),
    _Ea1000minValueOptPower_Type()
)
ea1000minValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueOptPower.setStatus("mandatory")
_Ea1000maxValueOptPower_Type = Float
_Ea1000maxValueOptPower_Object = MibTableColumn
ea1000maxValueOptPower = _Ea1000maxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 33),
    _Ea1000maxValueOptPower_Type()
)
ea1000maxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueOptPower.setStatus("mandatory")


class _Ea1000alarmStateOptPower_Type(Integer32):
    """Custom type ea1000alarmStateOptPower based on Integer32"""
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


_Ea1000alarmStateOptPower_Type.__name__ = "Integer32"
_Ea1000alarmStateOptPower_Object = MibTableColumn
ea1000alarmStateOptPower = _Ea1000alarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 34),
    _Ea1000alarmStateOptPower_Type()
)
ea1000alarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateOptPower.setStatus("mandatory")


class _Ea1000labelLaserTemp_Type(DisplayString):
    """Custom type ea1000labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelLaserTemp_Type.__name__ = "DisplayString"
_Ea1000labelLaserTemp_Object = MibTableColumn
ea1000labelLaserTemp = _Ea1000labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 35),
    _Ea1000labelLaserTemp_Type()
)
ea1000labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelLaserTemp.setStatus("optional")


class _Ea1000uomLaserTemp_Type(DisplayString):
    """Custom type ea1000uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomLaserTemp_Type.__name__ = "DisplayString"
_Ea1000uomLaserTemp_Object = MibTableColumn
ea1000uomLaserTemp = _Ea1000uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 36),
    _Ea1000uomLaserTemp_Type()
)
ea1000uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomLaserTemp.setStatus("optional")
_Ea1000majorHighLaserTemp_Type = Float
_Ea1000majorHighLaserTemp_Object = MibTableColumn
ea1000majorHighLaserTemp = _Ea1000majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 37),
    _Ea1000majorHighLaserTemp_Type()
)
ea1000majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighLaserTemp.setStatus("mandatory")
_Ea1000majorLowLaserTemp_Type = Float
_Ea1000majorLowLaserTemp_Object = MibTableColumn
ea1000majorLowLaserTemp = _Ea1000majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 38),
    _Ea1000majorLowLaserTemp_Type()
)
ea1000majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowLaserTemp.setStatus("mandatory")
_Ea1000minorHighLaserTemp_Type = Float
_Ea1000minorHighLaserTemp_Object = MibTableColumn
ea1000minorHighLaserTemp = _Ea1000minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 39),
    _Ea1000minorHighLaserTemp_Type()
)
ea1000minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighLaserTemp.setStatus("mandatory")
_Ea1000minorLowLaserTemp_Type = Float
_Ea1000minorLowLaserTemp_Object = MibTableColumn
ea1000minorLowLaserTemp = _Ea1000minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 40),
    _Ea1000minorLowLaserTemp_Type()
)
ea1000minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowLaserTemp.setStatus("mandatory")
_Ea1000currentValueLaserTemp_Type = Float
_Ea1000currentValueLaserTemp_Object = MibTableColumn
ea1000currentValueLaserTemp = _Ea1000currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 41),
    _Ea1000currentValueLaserTemp_Type()
)
ea1000currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueLaserTemp.setStatus("mandatory")


class _Ea1000stateFlagLaserTemp_Type(Integer32):
    """Custom type ea1000stateFlagLaserTemp based on Integer32"""
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


_Ea1000stateFlagLaserTemp_Type.__name__ = "Integer32"
_Ea1000stateFlagLaserTemp_Object = MibTableColumn
ea1000stateFlagLaserTemp = _Ea1000stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 42),
    _Ea1000stateFlagLaserTemp_Type()
)
ea1000stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagLaserTemp.setStatus("mandatory")
_Ea1000minValueLaserTemp_Type = Float
_Ea1000minValueLaserTemp_Object = MibTableColumn
ea1000minValueLaserTemp = _Ea1000minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 43),
    _Ea1000minValueLaserTemp_Type()
)
ea1000minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueLaserTemp.setStatus("mandatory")
_Ea1000maxValueLaserTemp_Type = Float
_Ea1000maxValueLaserTemp_Object = MibTableColumn
ea1000maxValueLaserTemp = _Ea1000maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 44),
    _Ea1000maxValueLaserTemp_Type()
)
ea1000maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueLaserTemp.setStatus("mandatory")


class _Ea1000alarmStateLaserTemp_Type(Integer32):
    """Custom type ea1000alarmStateLaserTemp based on Integer32"""
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


_Ea1000alarmStateLaserTemp_Type.__name__ = "Integer32"
_Ea1000alarmStateLaserTemp_Object = MibTableColumn
ea1000alarmStateLaserTemp = _Ea1000alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 45),
    _Ea1000alarmStateLaserTemp_Type()
)
ea1000alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateLaserTemp.setStatus("mandatory")


class _Ea1000labelLaserBias_Type(DisplayString):
    """Custom type ea1000labelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelLaserBias_Type.__name__ = "DisplayString"
_Ea1000labelLaserBias_Object = MibTableColumn
ea1000labelLaserBias = _Ea1000labelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 46),
    _Ea1000labelLaserBias_Type()
)
ea1000labelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelLaserBias.setStatus("optional")


class _Ea1000uomLaserBias_Type(DisplayString):
    """Custom type ea1000uomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomLaserBias_Type.__name__ = "DisplayString"
_Ea1000uomLaserBias_Object = MibTableColumn
ea1000uomLaserBias = _Ea1000uomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 47),
    _Ea1000uomLaserBias_Type()
)
ea1000uomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomLaserBias.setStatus("optional")
_Ea1000majorHighLaserBias_Type = Float
_Ea1000majorHighLaserBias_Object = MibTableColumn
ea1000majorHighLaserBias = _Ea1000majorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 48),
    _Ea1000majorHighLaserBias_Type()
)
ea1000majorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighLaserBias.setStatus("mandatory")
_Ea1000majorLowLaserBias_Type = Float
_Ea1000majorLowLaserBias_Object = MibTableColumn
ea1000majorLowLaserBias = _Ea1000majorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 49),
    _Ea1000majorLowLaserBias_Type()
)
ea1000majorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowLaserBias.setStatus("mandatory")
_Ea1000minorHighLaserBias_Type = Float
_Ea1000minorHighLaserBias_Object = MibTableColumn
ea1000minorHighLaserBias = _Ea1000minorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 50),
    _Ea1000minorHighLaserBias_Type()
)
ea1000minorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighLaserBias.setStatus("optional")
_Ea1000minorLowLaserBias_Type = Float
_Ea1000minorLowLaserBias_Object = MibTableColumn
ea1000minorLowLaserBias = _Ea1000minorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 51),
    _Ea1000minorLowLaserBias_Type()
)
ea1000minorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowLaserBias.setStatus("optional")
_Ea1000currentValueLaserBias_Type = Float
_Ea1000currentValueLaserBias_Object = MibTableColumn
ea1000currentValueLaserBias = _Ea1000currentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 52),
    _Ea1000currentValueLaserBias_Type()
)
ea1000currentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueLaserBias.setStatus("mandatory")


class _Ea1000stateFlagLaserBias_Type(Integer32):
    """Custom type ea1000stateFlagLaserBias based on Integer32"""
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


_Ea1000stateFlagLaserBias_Type.__name__ = "Integer32"
_Ea1000stateFlagLaserBias_Object = MibTableColumn
ea1000stateFlagLaserBias = _Ea1000stateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 53),
    _Ea1000stateFlagLaserBias_Type()
)
ea1000stateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagLaserBias.setStatus("mandatory")
_Ea1000minValueLaserBias_Type = Float
_Ea1000minValueLaserBias_Object = MibTableColumn
ea1000minValueLaserBias = _Ea1000minValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 54),
    _Ea1000minValueLaserBias_Type()
)
ea1000minValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueLaserBias.setStatus("mandatory")
_Ea1000maxValueLaserBias_Type = Float
_Ea1000maxValueLaserBias_Object = MibTableColumn
ea1000maxValueLaserBias = _Ea1000maxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 55),
    _Ea1000maxValueLaserBias_Type()
)
ea1000maxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueLaserBias.setStatus("mandatory")


class _Ea1000alarmStateLaserBias_Type(Integer32):
    """Custom type ea1000alarmStateLaserBias based on Integer32"""
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


_Ea1000alarmStateLaserBias_Type.__name__ = "Integer32"
_Ea1000alarmStateLaserBias_Object = MibTableColumn
ea1000alarmStateLaserBias = _Ea1000alarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 56),
    _Ea1000alarmStateLaserBias_Type()
)
ea1000alarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateLaserBias.setStatus("mandatory")


class _Ea1000labelTecCurrent_Type(DisplayString):
    """Custom type ea1000labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelTecCurrent_Type.__name__ = "DisplayString"
_Ea1000labelTecCurrent_Object = MibTableColumn
ea1000labelTecCurrent = _Ea1000labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 57),
    _Ea1000labelTecCurrent_Type()
)
ea1000labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelTecCurrent.setStatus("optional")


class _Ea1000uomTecCurrent_Type(DisplayString):
    """Custom type ea1000uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomTecCurrent_Type.__name__ = "DisplayString"
_Ea1000uomTecCurrent_Object = MibTableColumn
ea1000uomTecCurrent = _Ea1000uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 58),
    _Ea1000uomTecCurrent_Type()
)
ea1000uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomTecCurrent.setStatus("optional")
_Ea1000majorHighTecCurrent_Type = Float
_Ea1000majorHighTecCurrent_Object = MibTableColumn
ea1000majorHighTecCurrent = _Ea1000majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 59),
    _Ea1000majorHighTecCurrent_Type()
)
ea1000majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighTecCurrent.setStatus("mandatory")
_Ea1000majorLowTecCurrent_Type = Float
_Ea1000majorLowTecCurrent_Object = MibTableColumn
ea1000majorLowTecCurrent = _Ea1000majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 60),
    _Ea1000majorLowTecCurrent_Type()
)
ea1000majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowTecCurrent.setStatus("mandatory")
_Ea1000minorHighTecCurrent_Type = Float
_Ea1000minorHighTecCurrent_Object = MibTableColumn
ea1000minorHighTecCurrent = _Ea1000minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 61),
    _Ea1000minorHighTecCurrent_Type()
)
ea1000minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighTecCurrent.setStatus("optional")
_Ea1000minorLowTecCurrent_Type = Float
_Ea1000minorLowTecCurrent_Object = MibTableColumn
ea1000minorLowTecCurrent = _Ea1000minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 62),
    _Ea1000minorLowTecCurrent_Type()
)
ea1000minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowTecCurrent.setStatus("optional")
_Ea1000currentValueTecCurrent_Type = Float
_Ea1000currentValueTecCurrent_Object = MibTableColumn
ea1000currentValueTecCurrent = _Ea1000currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 63),
    _Ea1000currentValueTecCurrent_Type()
)
ea1000currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueTecCurrent.setStatus("mandatory")


class _Ea1000stateFlagTecCurrent_Type(Integer32):
    """Custom type ea1000stateFlagTecCurrent based on Integer32"""
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


_Ea1000stateFlagTecCurrent_Type.__name__ = "Integer32"
_Ea1000stateFlagTecCurrent_Object = MibTableColumn
ea1000stateFlagTecCurrent = _Ea1000stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 64),
    _Ea1000stateFlagTecCurrent_Type()
)
ea1000stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagTecCurrent.setStatus("mandatory")
_Ea1000minValueTecCurrent_Type = Float
_Ea1000minValueTecCurrent_Object = MibTableColumn
ea1000minValueTecCurrent = _Ea1000minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 65),
    _Ea1000minValueTecCurrent_Type()
)
ea1000minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueTecCurrent.setStatus("mandatory")
_Ea1000maxValueTecCurrent_Type = Float
_Ea1000maxValueTecCurrent_Object = MibTableColumn
ea1000maxValueTecCurrent = _Ea1000maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 66),
    _Ea1000maxValueTecCurrent_Type()
)
ea1000maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueTecCurrent.setStatus("mandatory")


class _Ea1000alarmStateTecCurrent_Type(Integer32):
    """Custom type ea1000alarmStateTecCurrent based on Integer32"""
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


_Ea1000alarmStateTecCurrent_Type.__name__ = "Integer32"
_Ea1000alarmStateTecCurrent_Object = MibTableColumn
ea1000alarmStateTecCurrent = _Ea1000alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 67),
    _Ea1000alarmStateTecCurrent_Type()
)
ea1000alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateTecCurrent.setStatus("mandatory")


class _Ea1000labelModuleTemp_Type(DisplayString):
    """Custom type ea1000labelModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelModuleTemp_Type.__name__ = "DisplayString"
_Ea1000labelModuleTemp_Object = MibTableColumn
ea1000labelModuleTemp = _Ea1000labelModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 68),
    _Ea1000labelModuleTemp_Type()
)
ea1000labelModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelModuleTemp.setStatus("optional")


class _Ea1000uomModuleTemp_Type(DisplayString):
    """Custom type ea1000uomModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomModuleTemp_Type.__name__ = "DisplayString"
_Ea1000uomModuleTemp_Object = MibTableColumn
ea1000uomModuleTemp = _Ea1000uomModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 69),
    _Ea1000uomModuleTemp_Type()
)
ea1000uomModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomModuleTemp.setStatus("optional")
_Ea1000majorHighModuleTemp_Type = Float
_Ea1000majorHighModuleTemp_Object = MibTableColumn
ea1000majorHighModuleTemp = _Ea1000majorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 70),
    _Ea1000majorHighModuleTemp_Type()
)
ea1000majorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighModuleTemp.setStatus("mandatory")
_Ea1000majorLowModuleTemp_Type = Float
_Ea1000majorLowModuleTemp_Object = MibTableColumn
ea1000majorLowModuleTemp = _Ea1000majorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 71),
    _Ea1000majorLowModuleTemp_Type()
)
ea1000majorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowModuleTemp.setStatus("mandatory")
_Ea1000minorHighModuleTemp_Type = Float
_Ea1000minorHighModuleTemp_Object = MibTableColumn
ea1000minorHighModuleTemp = _Ea1000minorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 72),
    _Ea1000minorHighModuleTemp_Type()
)
ea1000minorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighModuleTemp.setStatus("mandatory")
_Ea1000minorLowModuleTemp_Type = Float
_Ea1000minorLowModuleTemp_Object = MibTableColumn
ea1000minorLowModuleTemp = _Ea1000minorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 73),
    _Ea1000minorLowModuleTemp_Type()
)
ea1000minorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowModuleTemp.setStatus("mandatory")
_Ea1000currentValueModuleTemp_Type = Float
_Ea1000currentValueModuleTemp_Object = MibTableColumn
ea1000currentValueModuleTemp = _Ea1000currentValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 74),
    _Ea1000currentValueModuleTemp_Type()
)
ea1000currentValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueModuleTemp.setStatus("mandatory")


class _Ea1000stateFlagModuleTemp_Type(Integer32):
    """Custom type ea1000stateFlagModuleTemp based on Integer32"""
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


_Ea1000stateFlagModuleTemp_Type.__name__ = "Integer32"
_Ea1000stateFlagModuleTemp_Object = MibTableColumn
ea1000stateFlagModuleTemp = _Ea1000stateFlagModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 75),
    _Ea1000stateFlagModuleTemp_Type()
)
ea1000stateFlagModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagModuleTemp.setStatus("mandatory")
_Ea1000minValueModuleTemp_Type = Float
_Ea1000minValueModuleTemp_Object = MibTableColumn
ea1000minValueModuleTemp = _Ea1000minValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 76),
    _Ea1000minValueModuleTemp_Type()
)
ea1000minValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueModuleTemp.setStatus("mandatory")
_Ea1000maxValueModuleTemp_Type = Float
_Ea1000maxValueModuleTemp_Object = MibTableColumn
ea1000maxValueModuleTemp = _Ea1000maxValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 77),
    _Ea1000maxValueModuleTemp_Type()
)
ea1000maxValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueModuleTemp.setStatus("mandatory")


class _Ea1000alarmStateModuleTemp_Type(Integer32):
    """Custom type ea1000alarmStateModuleTemp based on Integer32"""
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


_Ea1000alarmStateModuleTemp_Type.__name__ = "Integer32"
_Ea1000alarmStateModuleTemp_Object = MibTableColumn
ea1000alarmStateModuleTemp = _Ea1000alarmStateModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 78),
    _Ea1000alarmStateModuleTemp_Type()
)
ea1000alarmStateModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateModuleTemp.setStatus("mandatory")


class _Ea1000labelFan1Speed_Type(DisplayString):
    """Custom type ea1000labelFan1Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelFan1Speed_Type.__name__ = "DisplayString"
_Ea1000labelFan1Speed_Object = MibTableColumn
ea1000labelFan1Speed = _Ea1000labelFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 79),
    _Ea1000labelFan1Speed_Type()
)
ea1000labelFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelFan1Speed.setStatus("optional")


class _Ea1000uomFan1Speed_Type(DisplayString):
    """Custom type ea1000uomFan1Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomFan1Speed_Type.__name__ = "DisplayString"
_Ea1000uomFan1Speed_Object = MibTableColumn
ea1000uomFan1Speed = _Ea1000uomFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 80),
    _Ea1000uomFan1Speed_Type()
)
ea1000uomFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomFan1Speed.setStatus("optional")
_Ea1000majorHighFan1Speed_Type = Float
_Ea1000majorHighFan1Speed_Object = MibTableColumn
ea1000majorHighFan1Speed = _Ea1000majorHighFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 81),
    _Ea1000majorHighFan1Speed_Type()
)
ea1000majorHighFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighFan1Speed.setStatus("optional")
_Ea1000majorLowFan1Speed_Type = Float
_Ea1000majorLowFan1Speed_Object = MibTableColumn
ea1000majorLowFan1Speed = _Ea1000majorLowFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 82),
    _Ea1000majorLowFan1Speed_Type()
)
ea1000majorLowFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowFan1Speed.setStatus("mandatory")
_Ea1000minorHighFan1Speed_Type = Float
_Ea1000minorHighFan1Speed_Object = MibTableColumn
ea1000minorHighFan1Speed = _Ea1000minorHighFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 83),
    _Ea1000minorHighFan1Speed_Type()
)
ea1000minorHighFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighFan1Speed.setStatus("optional")
_Ea1000minorLowFan1Speed_Type = Float
_Ea1000minorLowFan1Speed_Object = MibTableColumn
ea1000minorLowFan1Speed = _Ea1000minorLowFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 84),
    _Ea1000minorLowFan1Speed_Type()
)
ea1000minorLowFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowFan1Speed.setStatus("mandatory")
_Ea1000currentValueFan1Speed_Type = Float
_Ea1000currentValueFan1Speed_Object = MibTableColumn
ea1000currentValueFan1Speed = _Ea1000currentValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 85),
    _Ea1000currentValueFan1Speed_Type()
)
ea1000currentValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueFan1Speed.setStatus("mandatory")


class _Ea1000stateFlagFan1Speed_Type(Integer32):
    """Custom type ea1000stateFlagFan1Speed based on Integer32"""
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


_Ea1000stateFlagFan1Speed_Type.__name__ = "Integer32"
_Ea1000stateFlagFan1Speed_Object = MibTableColumn
ea1000stateFlagFan1Speed = _Ea1000stateFlagFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 86),
    _Ea1000stateFlagFan1Speed_Type()
)
ea1000stateFlagFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagFan1Speed.setStatus("mandatory")
_Ea1000minValueFan1Speed_Type = Float
_Ea1000minValueFan1Speed_Object = MibTableColumn
ea1000minValueFan1Speed = _Ea1000minValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 87),
    _Ea1000minValueFan1Speed_Type()
)
ea1000minValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueFan1Speed.setStatus("mandatory")
_Ea1000maxValueFan1Speed_Type = Float
_Ea1000maxValueFan1Speed_Object = MibTableColumn
ea1000maxValueFan1Speed = _Ea1000maxValueFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 88),
    _Ea1000maxValueFan1Speed_Type()
)
ea1000maxValueFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueFan1Speed.setStatus("mandatory")


class _Ea1000alarmStateFan1Speed_Type(Integer32):
    """Custom type ea1000alarmStateFan1Speed based on Integer32"""
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


_Ea1000alarmStateFan1Speed_Type.__name__ = "Integer32"
_Ea1000alarmStateFan1Speed_Object = MibTableColumn
ea1000alarmStateFan1Speed = _Ea1000alarmStateFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 89),
    _Ea1000alarmStateFan1Speed_Type()
)
ea1000alarmStateFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateFan1Speed.setStatus("mandatory")


class _Ea1000labelFan2Speed_Type(DisplayString):
    """Custom type ea1000labelFan2Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelFan2Speed_Type.__name__ = "DisplayString"
_Ea1000labelFan2Speed_Object = MibTableColumn
ea1000labelFan2Speed = _Ea1000labelFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 90),
    _Ea1000labelFan2Speed_Type()
)
ea1000labelFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelFan2Speed.setStatus("optional")


class _Ea1000uomFan2Speed_Type(DisplayString):
    """Custom type ea1000uomFan2Speed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uomFan2Speed_Type.__name__ = "DisplayString"
_Ea1000uomFan2Speed_Object = MibTableColumn
ea1000uomFan2Speed = _Ea1000uomFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 91),
    _Ea1000uomFan2Speed_Type()
)
ea1000uomFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uomFan2Speed.setStatus("optional")
_Ea1000majorHighFan2Speed_Type = Float
_Ea1000majorHighFan2Speed_Object = MibTableColumn
ea1000majorHighFan2Speed = _Ea1000majorHighFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 92),
    _Ea1000majorHighFan2Speed_Type()
)
ea1000majorHighFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHighFan2Speed.setStatus("optional")
_Ea1000majorLowFan2Speed_Type = Float
_Ea1000majorLowFan2Speed_Object = MibTableColumn
ea1000majorLowFan2Speed = _Ea1000majorLowFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 93),
    _Ea1000majorLowFan2Speed_Type()
)
ea1000majorLowFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLowFan2Speed.setStatus("mandatory")
_Ea1000minorHighFan2Speed_Type = Float
_Ea1000minorHighFan2Speed_Object = MibTableColumn
ea1000minorHighFan2Speed = _Ea1000minorHighFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 94),
    _Ea1000minorHighFan2Speed_Type()
)
ea1000minorHighFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHighFan2Speed.setStatus("optional")
_Ea1000minorLowFan2Speed_Type = Float
_Ea1000minorLowFan2Speed_Object = MibTableColumn
ea1000minorLowFan2Speed = _Ea1000minorLowFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 95),
    _Ea1000minorLowFan2Speed_Type()
)
ea1000minorLowFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLowFan2Speed.setStatus("mandatory")
_Ea1000currentValueFan2Speed_Type = Float
_Ea1000currentValueFan2Speed_Object = MibTableColumn
ea1000currentValueFan2Speed = _Ea1000currentValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 96),
    _Ea1000currentValueFan2Speed_Type()
)
ea1000currentValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValueFan2Speed.setStatus("mandatory")


class _Ea1000stateFlagFan2Speed_Type(Integer32):
    """Custom type ea1000stateFlagFan2Speed based on Integer32"""
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


_Ea1000stateFlagFan2Speed_Type.__name__ = "Integer32"
_Ea1000stateFlagFan2Speed_Object = MibTableColumn
ea1000stateFlagFan2Speed = _Ea1000stateFlagFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 97),
    _Ea1000stateFlagFan2Speed_Type()
)
ea1000stateFlagFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlagFan2Speed.setStatus("mandatory")
_Ea1000minValueFan2Speed_Type = Float
_Ea1000minValueFan2Speed_Object = MibTableColumn
ea1000minValueFan2Speed = _Ea1000minValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 98),
    _Ea1000minValueFan2Speed_Type()
)
ea1000minValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValueFan2Speed.setStatus("mandatory")
_Ea1000maxValueFan2Speed_Type = Float
_Ea1000maxValueFan2Speed_Object = MibTableColumn
ea1000maxValueFan2Speed = _Ea1000maxValueFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 99),
    _Ea1000maxValueFan2Speed_Type()
)
ea1000maxValueFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValueFan2Speed.setStatus("mandatory")


class _Ea1000alarmStateFan2Speed_Type(Integer32):
    """Custom type ea1000alarmStateFan2Speed based on Integer32"""
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


_Ea1000alarmStateFan2Speed_Type.__name__ = "Integer32"
_Ea1000alarmStateFan2Speed_Object = MibTableColumn
ea1000alarmStateFan2Speed = _Ea1000alarmStateFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 100),
    _Ea1000alarmStateFan2Speed_Type()
)
ea1000alarmStateFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmStateFan2Speed.setStatus("mandatory")


class _Ea1000label12Volt_Type(DisplayString):
    """Custom type ea1000label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000label12Volt_Type.__name__ = "DisplayString"
_Ea1000label12Volt_Object = MibTableColumn
ea1000label12Volt = _Ea1000label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 101),
    _Ea1000label12Volt_Type()
)
ea1000label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000label12Volt.setStatus("optional")


class _Ea1000uom12Volt_Type(DisplayString):
    """Custom type ea1000uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000uom12Volt_Type.__name__ = "DisplayString"
_Ea1000uom12Volt_Object = MibTableColumn
ea1000uom12Volt = _Ea1000uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 102),
    _Ea1000uom12Volt_Type()
)
ea1000uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000uom12Volt.setStatus("optional")
_Ea1000majorHigh12Volt_Type = Float
_Ea1000majorHigh12Volt_Object = MibTableColumn
ea1000majorHigh12Volt = _Ea1000majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 103),
    _Ea1000majorHigh12Volt_Type()
)
ea1000majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorHigh12Volt.setStatus("mandatory")
_Ea1000majorLow12Volt_Type = Float
_Ea1000majorLow12Volt_Object = MibTableColumn
ea1000majorLow12Volt = _Ea1000majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 104),
    _Ea1000majorLow12Volt_Type()
)
ea1000majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000majorLow12Volt.setStatus("mandatory")
_Ea1000minorHigh12Volt_Type = Float
_Ea1000minorHigh12Volt_Object = MibTableColumn
ea1000minorHigh12Volt = _Ea1000minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 105),
    _Ea1000minorHigh12Volt_Type()
)
ea1000minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorHigh12Volt.setStatus("mandatory")
_Ea1000minorLow12Volt_Type = Float
_Ea1000minorLow12Volt_Object = MibTableColumn
ea1000minorLow12Volt = _Ea1000minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 106),
    _Ea1000minorLow12Volt_Type()
)
ea1000minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minorLow12Volt.setStatus("mandatory")
_Ea1000currentValue12Volt_Type = Float
_Ea1000currentValue12Volt_Object = MibTableColumn
ea1000currentValue12Volt = _Ea1000currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 107),
    _Ea1000currentValue12Volt_Type()
)
ea1000currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000currentValue12Volt.setStatus("mandatory")


class _Ea1000stateFlag12Volt_Type(Integer32):
    """Custom type ea1000stateFlag12Volt based on Integer32"""
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


_Ea1000stateFlag12Volt_Type.__name__ = "Integer32"
_Ea1000stateFlag12Volt_Object = MibTableColumn
ea1000stateFlag12Volt = _Ea1000stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 108),
    _Ea1000stateFlag12Volt_Type()
)
ea1000stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateFlag12Volt.setStatus("mandatory")
_Ea1000minValue12Volt_Type = Float
_Ea1000minValue12Volt_Object = MibTableColumn
ea1000minValue12Volt = _Ea1000minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 109),
    _Ea1000minValue12Volt_Type()
)
ea1000minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000minValue12Volt.setStatus("mandatory")
_Ea1000maxValue12Volt_Type = Float
_Ea1000maxValue12Volt_Object = MibTableColumn
ea1000maxValue12Volt = _Ea1000maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 110),
    _Ea1000maxValue12Volt_Type()
)
ea1000maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000maxValue12Volt.setStatus("mandatory")


class _Ea1000alarmState12Volt_Type(Integer32):
    """Custom type ea1000alarmState12Volt based on Integer32"""
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


_Ea1000alarmState12Volt_Type.__name__ = "Integer32"
_Ea1000alarmState12Volt_Object = MibTableColumn
ea1000alarmState12Volt = _Ea1000alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 2, 1, 111),
    _Ea1000alarmState12Volt_Type()
)
ea1000alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000alarmState12Volt.setStatus("mandatory")
_Gx2ea1000DigitalTable_Object = MibTable
gx2ea1000DigitalTable = _Gx2ea1000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3)
)
if mibBuilder.loadTexts:
    gx2ea1000DigitalTable.setStatus("mandatory")
_Gx2ea1000DigitalEntry_Object = MibTableRow
gx2ea1000DigitalEntry = _Gx2ea1000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2)
)
gx2ea1000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2EA1000-MIB", "gx2ea1000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2ea1000DigitalEntry.setStatus("mandatory")


class _Gx2ea1000DigitalTableIndex_Type(Integer32):
    """Custom type gx2ea1000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2ea1000DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2ea1000DigitalTableIndex_Object = MibTableColumn
gx2ea1000DigitalTableIndex = _Gx2ea1000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 1),
    _Gx2ea1000DigitalTableIndex_Type()
)
gx2ea1000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2ea1000DigitalTableIndex.setStatus("mandatory")


class _Ea1000labelRfInput_Type(DisplayString):
    """Custom type ea1000labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelRfInput_Type.__name__ = "DisplayString"
_Ea1000labelRfInput_Object = MibTableColumn
ea1000labelRfInput = _Ea1000labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 2),
    _Ea1000labelRfInput_Type()
)
ea1000labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelRfInput.setStatus("optional")


class _Ea1000enumRfInput_Type(DisplayString):
    """Custom type ea1000enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumRfInput_Type.__name__ = "DisplayString"
_Ea1000enumRfInput_Object = MibTableColumn
ea1000enumRfInput = _Ea1000enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 3),
    _Ea1000enumRfInput_Type()
)
ea1000enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumRfInput.setStatus("optional")


class _Ea1000valueRfInput_Type(Integer32):
    """Custom type ea1000valueRfInput based on Integer32"""
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


_Ea1000valueRfInput_Type.__name__ = "Integer32"
_Ea1000valueRfInput_Object = MibTableColumn
ea1000valueRfInput = _Ea1000valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 4),
    _Ea1000valueRfInput_Type()
)
ea1000valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueRfInput.setStatus("mandatory")


class _Ea1000stateflagRfInput_Type(Integer32):
    """Custom type ea1000stateflagRfInput based on Integer32"""
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


_Ea1000stateflagRfInput_Type.__name__ = "Integer32"
_Ea1000stateflagRfInput_Object = MibTableColumn
ea1000stateflagRfInput = _Ea1000stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 5),
    _Ea1000stateflagRfInput_Type()
)
ea1000stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagRfInput.setStatus("mandatory")


class _Ea1000labelOptOutput_Type(DisplayString):
    """Custom type ea1000labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelOptOutput_Type.__name__ = "DisplayString"
_Ea1000labelOptOutput_Object = MibTableColumn
ea1000labelOptOutput = _Ea1000labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 6),
    _Ea1000labelOptOutput_Type()
)
ea1000labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelOptOutput.setStatus("optional")


class _Ea1000enumOptOutput_Type(DisplayString):
    """Custom type ea1000enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumOptOutput_Type.__name__ = "DisplayString"
_Ea1000enumOptOutput_Object = MibTableColumn
ea1000enumOptOutput = _Ea1000enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 7),
    _Ea1000enumOptOutput_Type()
)
ea1000enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumOptOutput.setStatus("optional")


class _Ea1000valueOptOutput_Type(Integer32):
    """Custom type ea1000valueOptOutput based on Integer32"""
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


_Ea1000valueOptOutput_Type.__name__ = "Integer32"
_Ea1000valueOptOutput_Object = MibTableColumn
ea1000valueOptOutput = _Ea1000valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 8),
    _Ea1000valueOptOutput_Type()
)
ea1000valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueOptOutput.setStatus("mandatory")


class _Ea1000stateflagOptOutput_Type(Integer32):
    """Custom type ea1000stateflagOptOutput based on Integer32"""
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


_Ea1000stateflagOptOutput_Type.__name__ = "Integer32"
_Ea1000stateflagOptOutput_Object = MibTableColumn
ea1000stateflagOptOutput = _Ea1000stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 9),
    _Ea1000stateflagOptOutput_Type()
)
ea1000stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagOptOutput.setStatus("mandatory")


class _Ea1000labelLaserMode_Type(DisplayString):
    """Custom type ea1000labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelLaserMode_Type.__name__ = "DisplayString"
_Ea1000labelLaserMode_Object = MibTableColumn
ea1000labelLaserMode = _Ea1000labelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 10),
    _Ea1000labelLaserMode_Type()
)
ea1000labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelLaserMode.setStatus("optional")


class _Ea1000enumLaserMode_Type(DisplayString):
    """Custom type ea1000enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumLaserMode_Type.__name__ = "DisplayString"
_Ea1000enumLaserMode_Object = MibTableColumn
ea1000enumLaserMode = _Ea1000enumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 11),
    _Ea1000enumLaserMode_Type()
)
ea1000enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumLaserMode.setStatus("optional")


class _Ea1000valueLaserMode_Type(Integer32):
    """Custom type ea1000valueLaserMode based on Integer32"""
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


_Ea1000valueLaserMode_Type.__name__ = "Integer32"
_Ea1000valueLaserMode_Object = MibTableColumn
ea1000valueLaserMode = _Ea1000valueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 12),
    _Ea1000valueLaserMode_Type()
)
ea1000valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueLaserMode.setStatus("mandatory")


class _Ea1000stateflagLaserMode_Type(Integer32):
    """Custom type ea1000stateflagLaserMode based on Integer32"""
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


_Ea1000stateflagLaserMode_Type.__name__ = "Integer32"
_Ea1000stateflagLaserMode_Object = MibTableColumn
ea1000stateflagLaserMode = _Ea1000stateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 13),
    _Ea1000stateflagLaserMode_Type()
)
ea1000stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagLaserMode.setStatus("mandatory")


class _Ea1000labelAttenSetting_Type(DisplayString):
    """Custom type ea1000labelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelAttenSetting_Type.__name__ = "DisplayString"
_Ea1000labelAttenSetting_Object = MibTableColumn
ea1000labelAttenSetting = _Ea1000labelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 14),
    _Ea1000labelAttenSetting_Type()
)
ea1000labelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelAttenSetting.setStatus("optional")


class _Ea1000enumAttenSetting_Type(DisplayString):
    """Custom type ea1000enumAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumAttenSetting_Type.__name__ = "DisplayString"
_Ea1000enumAttenSetting_Object = MibTableColumn
ea1000enumAttenSetting = _Ea1000enumAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 15),
    _Ea1000enumAttenSetting_Type()
)
ea1000enumAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumAttenSetting.setStatus("optional")


class _Ea1000valueAttenSetting_Type(Integer32):
    """Custom type ea1000valueAttenSetting based on Integer32"""
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


_Ea1000valueAttenSetting_Type.__name__ = "Integer32"
_Ea1000valueAttenSetting_Object = MibTableColumn
ea1000valueAttenSetting = _Ea1000valueAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 16),
    _Ea1000valueAttenSetting_Type()
)
ea1000valueAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueAttenSetting.setStatus("mandatory")


class _Ea1000stateflagAttenSetting_Type(Integer32):
    """Custom type ea1000stateflagAttenSetting based on Integer32"""
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


_Ea1000stateflagAttenSetting_Type.__name__ = "Integer32"
_Ea1000stateflagAttenSetting_Object = MibTableColumn
ea1000stateflagAttenSetting = _Ea1000stateflagAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 17),
    _Ea1000stateflagAttenSetting_Type()
)
ea1000stateflagAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagAttenSetting.setStatus("mandatory")


class _Ea1000labelLaserSecMode_Type(DisplayString):
    """Custom type ea1000labelLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelLaserSecMode_Type.__name__ = "DisplayString"
_Ea1000labelLaserSecMode_Object = MibTableColumn
ea1000labelLaserSecMode = _Ea1000labelLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 18),
    _Ea1000labelLaserSecMode_Type()
)
ea1000labelLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelLaserSecMode.setStatus("optional")


class _Ea1000enumLaserSecMode_Type(DisplayString):
    """Custom type ea1000enumLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumLaserSecMode_Type.__name__ = "DisplayString"
_Ea1000enumLaserSecMode_Object = MibTableColumn
ea1000enumLaserSecMode = _Ea1000enumLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 19),
    _Ea1000enumLaserSecMode_Type()
)
ea1000enumLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumLaserSecMode.setStatus("optional")


class _Ea1000valueLaserSecMode_Type(Integer32):
    """Custom type ea1000valueLaserSecMode based on Integer32"""
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


_Ea1000valueLaserSecMode_Type.__name__ = "Integer32"
_Ea1000valueLaserSecMode_Object = MibTableColumn
ea1000valueLaserSecMode = _Ea1000valueLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 20),
    _Ea1000valueLaserSecMode_Type()
)
ea1000valueLaserSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueLaserSecMode.setStatus("mandatory")


class _Ea1000stateflagLaserSecMode_Type(Integer32):
    """Custom type ea1000stateflagLaserSecMode based on Integer32"""
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


_Ea1000stateflagLaserSecMode_Type.__name__ = "Integer32"
_Ea1000stateflagLaserSecMode_Object = MibTableColumn
ea1000stateflagLaserSecMode = _Ea1000stateflagLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 21),
    _Ea1000stateflagLaserSecMode_Type()
)
ea1000stateflagLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagLaserSecMode.setStatus("mandatory")


class _Ea1000labelVideoOffset_Type(DisplayString):
    """Custom type ea1000labelVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelVideoOffset_Type.__name__ = "DisplayString"
_Ea1000labelVideoOffset_Object = MibTableColumn
ea1000labelVideoOffset = _Ea1000labelVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 22),
    _Ea1000labelVideoOffset_Type()
)
ea1000labelVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelVideoOffset.setStatus("optional")


class _Ea1000enumVideoOffset_Type(DisplayString):
    """Custom type ea1000enumVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumVideoOffset_Type.__name__ = "DisplayString"
_Ea1000enumVideoOffset_Object = MibTableColumn
ea1000enumVideoOffset = _Ea1000enumVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 23),
    _Ea1000enumVideoOffset_Type()
)
ea1000enumVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumVideoOffset.setStatus("optional")


class _Ea1000valueVideoOffset_Type(Integer32):
    """Custom type ea1000valueVideoOffset based on Integer32"""
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


_Ea1000valueVideoOffset_Type.__name__ = "Integer32"
_Ea1000valueVideoOffset_Object = MibTableColumn
ea1000valueVideoOffset = _Ea1000valueVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 24),
    _Ea1000valueVideoOffset_Type()
)
ea1000valueVideoOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueVideoOffset.setStatus("mandatory")


class _Ea1000stateflagVideoOffset_Type(Integer32):
    """Custom type ea1000stateflagVideoOffset based on Integer32"""
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


_Ea1000stateflagVideoOffset_Type.__name__ = "Integer32"
_Ea1000stateflagVideoOffset_Object = MibTableColumn
ea1000stateflagVideoOffset = _Ea1000stateflagVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 25),
    _Ea1000stateflagVideoOffset_Type()
)
ea1000stateflagVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagVideoOffset.setStatus("mandatory")


class _Ea1000labelFactoryDefault_Type(DisplayString):
    """Custom type ea1000labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelFactoryDefault_Type.__name__ = "DisplayString"
_Ea1000labelFactoryDefault_Object = MibTableColumn
ea1000labelFactoryDefault = _Ea1000labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 26),
    _Ea1000labelFactoryDefault_Type()
)
ea1000labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelFactoryDefault.setStatus("optional")


class _Ea1000enumFactoryDefault_Type(DisplayString):
    """Custom type ea1000enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000enumFactoryDefault_Type.__name__ = "DisplayString"
_Ea1000enumFactoryDefault_Object = MibTableColumn
ea1000enumFactoryDefault = _Ea1000enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 27),
    _Ea1000enumFactoryDefault_Type()
)
ea1000enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000enumFactoryDefault.setStatus("optional")


class _Ea1000valueFactoryDefault_Type(Integer32):
    """Custom type ea1000valueFactoryDefault based on Integer32"""
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


_Ea1000valueFactoryDefault_Type.__name__ = "Integer32"
_Ea1000valueFactoryDefault_Object = MibTableColumn
ea1000valueFactoryDefault = _Ea1000valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 28),
    _Ea1000valueFactoryDefault_Type()
)
ea1000valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ea1000valueFactoryDefault.setStatus("mandatory")


class _Ea1000stateflagFactoryDefault_Type(Integer32):
    """Custom type ea1000stateflagFactoryDefault based on Integer32"""
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


_Ea1000stateflagFactoryDefault_Type.__name__ = "Integer32"
_Ea1000stateflagFactoryDefault_Object = MibTableColumn
ea1000stateflagFactoryDefault = _Ea1000stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 3, 2, 29),
    _Ea1000stateflagFactoryDefault_Type()
)
ea1000stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagFactoryDefault.setStatus("mandatory")
_Gx2ea1000StatusTable_Object = MibTable
gx2ea1000StatusTable = _Gx2ea1000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4)
)
if mibBuilder.loadTexts:
    gx2ea1000StatusTable.setStatus("mandatory")
_Gx2ea1000StatusEntry_Object = MibTableRow
gx2ea1000StatusEntry = _Gx2ea1000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3)
)
gx2ea1000StatusEntry.setIndexNames(
    (0, "OMNI-gx2EA1000-MIB", "gx2ea1000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2ea1000StatusEntry.setStatus("mandatory")


class _Gx2ea1000StatusTableIndex_Type(Integer32):
    """Custom type gx2ea1000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2ea1000StatusTableIndex_Type.__name__ = "Integer32"
_Gx2ea1000StatusTableIndex_Object = MibTableColumn
gx2ea1000StatusTableIndex = _Gx2ea1000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 1),
    _Gx2ea1000StatusTableIndex_Type()
)
gx2ea1000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2ea1000StatusTableIndex.setStatus("mandatory")


class _Ea1000labelBoot_Type(DisplayString):
    """Custom type ea1000labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelBoot_Type.__name__ = "DisplayString"
_Ea1000labelBoot_Object = MibTableColumn
ea1000labelBoot = _Ea1000labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 2),
    _Ea1000labelBoot_Type()
)
ea1000labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelBoot.setStatus("optional")


class _Ea1000valueBoot_Type(Integer32):
    """Custom type ea1000valueBoot based on Integer32"""
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


_Ea1000valueBoot_Type.__name__ = "Integer32"
_Ea1000valueBoot_Object = MibTableColumn
ea1000valueBoot = _Ea1000valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 3),
    _Ea1000valueBoot_Type()
)
ea1000valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueBoot.setStatus("mandatory")


class _Ea1000stateflagBoot_Type(Integer32):
    """Custom type ea1000stateflagBoot based on Integer32"""
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


_Ea1000stateflagBoot_Type.__name__ = "Integer32"
_Ea1000stateflagBoot_Object = MibTableColumn
ea1000stateflagBoot = _Ea1000stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 4),
    _Ea1000stateflagBoot_Type()
)
ea1000stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagBoot.setStatus("mandatory")


class _Ea1000labelFlash_Type(DisplayString):
    """Custom type ea1000labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelFlash_Type.__name__ = "DisplayString"
_Ea1000labelFlash_Object = MibTableColumn
ea1000labelFlash = _Ea1000labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 5),
    _Ea1000labelFlash_Type()
)
ea1000labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelFlash.setStatus("optional")


class _Ea1000valueFlash_Type(Integer32):
    """Custom type ea1000valueFlash based on Integer32"""
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


_Ea1000valueFlash_Type.__name__ = "Integer32"
_Ea1000valueFlash_Object = MibTableColumn
ea1000valueFlash = _Ea1000valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 6),
    _Ea1000valueFlash_Type()
)
ea1000valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueFlash.setStatus("mandatory")


class _Ea1000stateflagFlash_Type(Integer32):
    """Custom type ea1000stateflagFlash based on Integer32"""
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


_Ea1000stateflagFlash_Type.__name__ = "Integer32"
_Ea1000stateflagFlash_Object = MibTableColumn
ea1000stateflagFlash = _Ea1000stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 7),
    _Ea1000stateflagFlash_Type()
)
ea1000stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagFlash.setStatus("mandatory")


class _Ea1000labelFactoryDataCRC_Type(DisplayString):
    """Custom type ea1000labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Ea1000labelFactoryDataCRC_Object = MibTableColumn
ea1000labelFactoryDataCRC = _Ea1000labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 8),
    _Ea1000labelFactoryDataCRC_Type()
)
ea1000labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelFactoryDataCRC.setStatus("optional")


class _Ea1000valueFactoryDataCRC_Type(Integer32):
    """Custom type ea1000valueFactoryDataCRC based on Integer32"""
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


_Ea1000valueFactoryDataCRC_Type.__name__ = "Integer32"
_Ea1000valueFactoryDataCRC_Object = MibTableColumn
ea1000valueFactoryDataCRC = _Ea1000valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 9),
    _Ea1000valueFactoryDataCRC_Type()
)
ea1000valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueFactoryDataCRC.setStatus("mandatory")


class _Ea1000stateflagFactoryDataCRC_Type(Integer32):
    """Custom type ea1000stateflagFactoryDataCRC based on Integer32"""
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


_Ea1000stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Ea1000stateflagFactoryDataCRC_Object = MibTableColumn
ea1000stateflagFactoryDataCRC = _Ea1000stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 10),
    _Ea1000stateflagFactoryDataCRC_Type()
)
ea1000stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagFactoryDataCRC.setStatus("mandatory")


class _Ea1000labelLaserDataCRC_Type(DisplayString):
    """Custom type ea1000labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelLaserDataCRC_Type.__name__ = "DisplayString"
_Ea1000labelLaserDataCRC_Object = MibTableColumn
ea1000labelLaserDataCRC = _Ea1000labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 11),
    _Ea1000labelLaserDataCRC_Type()
)
ea1000labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelLaserDataCRC.setStatus("optional")


class _Ea1000valueLaserDataCRC_Type(Integer32):
    """Custom type ea1000valueLaserDataCRC based on Integer32"""
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


_Ea1000valueLaserDataCRC_Type.__name__ = "Integer32"
_Ea1000valueLaserDataCRC_Object = MibTableColumn
ea1000valueLaserDataCRC = _Ea1000valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 12),
    _Ea1000valueLaserDataCRC_Type()
)
ea1000valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueLaserDataCRC.setStatus("mandatory")


class _Ea1000stateflagLaserDataCRC_Type(Integer32):
    """Custom type ea1000stateflagLaserDataCRC based on Integer32"""
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


_Ea1000stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Ea1000stateflagLaserDataCRC_Object = MibTableColumn
ea1000stateflagLaserDataCRC = _Ea1000stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 13),
    _Ea1000stateflagLaserDataCRC_Type()
)
ea1000stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagLaserDataCRC.setStatus("mandatory")


class _Ea1000labelAlarmDataCrc_Type(DisplayString):
    """Custom type ea1000labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Ea1000labelAlarmDataCrc_Object = MibTableColumn
ea1000labelAlarmDataCrc = _Ea1000labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 14),
    _Ea1000labelAlarmDataCrc_Type()
)
ea1000labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelAlarmDataCrc.setStatus("optional")


class _Ea1000valueAlarmDataCrc_Type(Integer32):
    """Custom type ea1000valueAlarmDataCrc based on Integer32"""
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


_Ea1000valueAlarmDataCrc_Type.__name__ = "Integer32"
_Ea1000valueAlarmDataCrc_Object = MibTableColumn
ea1000valueAlarmDataCrc = _Ea1000valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 15),
    _Ea1000valueAlarmDataCrc_Type()
)
ea1000valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueAlarmDataCrc.setStatus("mandatory")


class _Ea1000stateflagAlarmDataCrc_Type(Integer32):
    """Custom type ea1000stateflagAlarmDataCrc based on Integer32"""
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


_Ea1000stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Ea1000stateflagAlarmDataCrc_Object = MibTableColumn
ea1000stateflagAlarmDataCrc = _Ea1000stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 16),
    _Ea1000stateflagAlarmDataCrc_Type()
)
ea1000stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagAlarmDataCrc.setStatus("mandatory")


class _Ea1000labelRFInputStatus_Type(DisplayString):
    """Custom type ea1000labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000labelRFInputStatus_Type.__name__ = "DisplayString"
_Ea1000labelRFInputStatus_Object = MibTableColumn
ea1000labelRFInputStatus = _Ea1000labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 17),
    _Ea1000labelRFInputStatus_Type()
)
ea1000labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000labelRFInputStatus.setStatus("optional")


class _Ea1000valueRFInputStatus_Type(Integer32):
    """Custom type ea1000valueRFInputStatus based on Integer32"""
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


_Ea1000valueRFInputStatus_Type.__name__ = "Integer32"
_Ea1000valueRFInputStatus_Object = MibTableColumn
ea1000valueRFInputStatus = _Ea1000valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 18),
    _Ea1000valueRFInputStatus_Type()
)
ea1000valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000valueRFInputStatus.setStatus("mandatory")


class _Ea1000stateflagRFInputStatus_Type(Integer32):
    """Custom type ea1000stateflagRFInputStatus based on Integer32"""
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


_Ea1000stateflagRFInputStatus_Type.__name__ = "Integer32"
_Ea1000stateflagRFInputStatus_Object = MibTableColumn
ea1000stateflagRFInputStatus = _Ea1000stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 4, 3, 19),
    _Ea1000stateflagRFInputStatus_Type()
)
ea1000stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000stateflagRFInputStatus.setStatus("mandatory")
_Gx2ea1000FactoryTable_Object = MibTable
gx2ea1000FactoryTable = _Gx2ea1000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5)
)
if mibBuilder.loadTexts:
    gx2ea1000FactoryTable.setStatus("mandatory")
_Gx2ea1000FactoryEntry_Object = MibTableRow
gx2ea1000FactoryEntry = _Gx2ea1000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4)
)
gx2ea1000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2EA1000-MIB", "gx2ea1000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2ea1000FactoryEntry.setStatus("mandatory")


class _Gx2ea1000FactoryTableIndex_Type(Integer32):
    """Custom type gx2ea1000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2ea1000FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2ea1000FactoryTableIndex_Object = MibTableColumn
gx2ea1000FactoryTableIndex = _Gx2ea1000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 1),
    _Gx2ea1000FactoryTableIndex_Type()
)
gx2ea1000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2ea1000FactoryTableIndex.setStatus("mandatory")
_Ea1000bootControlByteValue_Type = Integer32
_Ea1000bootControlByteValue_Object = MibTableColumn
ea1000bootControlByteValue = _Ea1000bootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 2),
    _Ea1000bootControlByteValue_Type()
)
ea1000bootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000bootControlByteValue.setStatus("mandatory")
_Ea1000bootStatusByteValue_Type = Integer32
_Ea1000bootStatusByteValue_Object = MibTableColumn
ea1000bootStatusByteValue = _Ea1000bootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 3),
    _Ea1000bootStatusByteValue_Type()
)
ea1000bootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000bootStatusByteValue.setStatus("mandatory")
_Ea1000bank1CRCValue_Type = Integer32
_Ea1000bank1CRCValue_Object = MibTableColumn
ea1000bank1CRCValue = _Ea1000bank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 4),
    _Ea1000bank1CRCValue_Type()
)
ea1000bank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000bank1CRCValue.setStatus("mandatory")
_Ea1000bank2CRCValue_Type = Integer32
_Ea1000bank2CRCValue_Object = MibTableColumn
ea1000bank2CRCValue = _Ea1000bank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 5),
    _Ea1000bank2CRCValue_Type()
)
ea1000bank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000bank2CRCValue.setStatus("mandatory")
_Ea1000prgEEPROMByteValue_Type = Integer32
_Ea1000prgEEPROMByteValue_Object = MibTableColumn
ea1000prgEEPROMByteValue = _Ea1000prgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 6),
    _Ea1000prgEEPROMByteValue_Type()
)
ea1000prgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000prgEEPROMByteValue.setStatus("mandatory")
_Ea1000factoryCRCValue_Type = Integer32
_Ea1000factoryCRCValue_Object = MibTableColumn
ea1000factoryCRCValue = _Ea1000factoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 7),
    _Ea1000factoryCRCValue_Type()
)
ea1000factoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000factoryCRCValue.setStatus("mandatory")


class _Ea1000calculateCRCValue_Type(Integer32):
    """Custom type ea1000calculateCRCValue based on Integer32"""
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


_Ea1000calculateCRCValue_Type.__name__ = "Integer32"
_Ea1000calculateCRCValue_Object = MibTableColumn
ea1000calculateCRCValue = _Ea1000calculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 8),
    _Ea1000calculateCRCValue_Type()
)
ea1000calculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000calculateCRCValue.setStatus("mandatory")
_Ea1000hourMeterValue_Type = Integer32
_Ea1000hourMeterValue_Object = MibTableColumn
ea1000hourMeterValue = _Ea1000hourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 9),
    _Ea1000hourMeterValue_Type()
)
ea1000hourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000hourMeterValue.setStatus("mandatory")
_Ea1000flashPrgCntAValue_Type = Integer32
_Ea1000flashPrgCntAValue_Object = MibTableColumn
ea1000flashPrgCntAValue = _Ea1000flashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 10),
    _Ea1000flashPrgCntAValue_Type()
)
ea1000flashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000flashPrgCntAValue.setStatus("mandatory")
_Ea1000flashPrgCntBValue_Type = Integer32
_Ea1000flashPrgCntBValue_Object = MibTableColumn
ea1000flashPrgCntBValue = _Ea1000flashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 11),
    _Ea1000flashPrgCntBValue_Type()
)
ea1000flashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000flashPrgCntBValue.setStatus("mandatory")


class _Ea1000flashBankARevValue_Type(DisplayString):
    """Custom type ea1000flashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000flashBankARevValue_Type.__name__ = "DisplayString"
_Ea1000flashBankARevValue_Object = MibTableColumn
ea1000flashBankARevValue = _Ea1000flashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 12),
    _Ea1000flashBankARevValue_Type()
)
ea1000flashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000flashBankARevValue.setStatus("mandatory")


class _Ea1000flashBankBRevValue_Type(DisplayString):
    """Custom type ea1000flashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Ea1000flashBankBRevValue_Type.__name__ = "DisplayString"
_Ea1000flashBankBRevValue_Object = MibTableColumn
ea1000flashBankBRevValue = _Ea1000flashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 5, 4, 13),
    _Ea1000flashBankBRevValue_Type()
)
ea1000flashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ea1000flashBankBRevValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapEA1000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 1)
)
trapEA1000ConfigChangeInteger.setObjects(
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
    trapEA1000ConfigChangeInteger.setStatus(
        ""
    )

trapEA1000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 2)
)
trapEA1000ConfigChangeDisplayString.setObjects(
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
    trapEA1000ConfigChangeDisplayString.setStatus(
        ""
    )

trapEA1000RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 3)
)
trapEA1000RFInputAlarm.setObjects(
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
    trapEA1000RFInputAlarm.setStatus(
        ""
    )

trapEA1000RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 4)
)
trapEA1000RFOverloadAlarm.setObjects(
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
    trapEA1000RFOverloadAlarm.setStatus(
        ""
    )

trapEA1000RFOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 5)
)
trapEA1000RFOffsetAlarm.setObjects(
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
    trapEA1000RFOffsetAlarm.setStatus(
        ""
    )

trapEA1000OpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 6)
)
trapEA1000OpticalPowerAlarm.setObjects(
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
    trapEA1000OpticalPowerAlarm.setStatus(
        ""
    )

trapEA1000LaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 7)
)
trapEA1000LaserBiasAlarm.setObjects(
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
    trapEA1000LaserBiasAlarm.setStatus(
        ""
    )

trapEA1000LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 8)
)
trapEA1000LaserTempAlarm.setObjects(
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
    trapEA1000LaserTempAlarm.setStatus(
        ""
    )

trapEA1000TECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 9)
)
trapEA1000TECCurrentAlarm.setObjects(
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
    trapEA1000TECCurrentAlarm.setStatus(
        ""
    )

trapEA1000Fan1SpeedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 10)
)
trapEA1000Fan1SpeedAlarm.setObjects(
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
    trapEA1000Fan1SpeedAlarm.setStatus(
        ""
    )

trapEA1000Fan2SpeedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 11)
)
trapEA1000Fan2SpeedAlarm.setObjects(
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
    trapEA1000Fan2SpeedAlarm.setStatus(
        ""
    )

trapEA100012vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 12)
)
trapEA100012vAlarm.setObjects(
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
    trapEA100012vAlarm.setStatus(
        ""
    )

trapEA1000ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 13)
)
trapEA1000ModuleTempAlarm.setObjects(
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
    trapEA1000ModuleTempAlarm.setStatus(
        ""
    )

trapEA1000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 14)
)
trapEA1000FlashAlarm.setObjects(
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
    trapEA1000FlashAlarm.setStatus(
        ""
    )

trapEA1000LaserBiasCntLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 15)
)
trapEA1000LaserBiasCntLoopAlarm.setObjects(
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
    trapEA1000LaserBiasCntLoopAlarm.setStatus(
        ""
    )

trapEA1000BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 16)
)
trapEA1000BankBootAlarm.setObjects(
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
    trapEA1000BankBootAlarm.setStatus(
        ""
    )

trapEA1000LaserBiasCntLoopInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 17)
)
trapEA1000LaserBiasCntLoopInitAlarm.setObjects(
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
    trapEA1000LaserBiasCntLoopInitAlarm.setStatus(
        ""
    )

trapEA1000RFParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 18)
)
trapEA1000RFParamInitAlarm.setObjects(
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
    trapEA1000RFParamInitAlarm.setStatus(
        ""
    )

trapEA1000TECParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 19)
)
trapEA1000TECParamInitAlarm.setObjects(
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
    trapEA1000TECParamInitAlarm.setStatus(
        ""
    )

trapEA1000AttnTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 20)
)
trapEA1000AttnTableInitAlarm.setObjects(
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
    trapEA1000AttnTableInitAlarm.setStatus(
        ""
    )

trapEA1000PowerMeterTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 21)
)
trapEA1000PowerMeterTableInitAlarm.setObjects(
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
    trapEA1000PowerMeterTableInitAlarm.setStatus(
        ""
    )

trapEA1000LaserDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 22)
)
trapEA1000LaserDataCRCAlarm.setObjects(
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
    trapEA1000LaserDataCRCAlarm.setStatus(
        ""
    )

trapEA1000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 23)
)
trapEA1000AlarmDataCRCAlarm.setObjects(
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
    trapEA1000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapEA1000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 24)
)
trapEA1000FactoryDataCRCAlarm.setObjects(
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
    trapEA1000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapEA1000UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 25)
)
trapEA1000UserRFOffAlarm.setObjects(
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
    trapEA1000UserRFOffAlarm.setStatus(
        ""
    )

trapEA1000UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 26)
)
trapEA1000UserOpticalOffAlarm.setObjects(
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
    trapEA1000UserOpticalOffAlarm.setStatus(
        ""
    )

trapEA1000ResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33, 0, 27)
)
trapEA1000ResetFactoryDefaultAlarm.setObjects(
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
    trapEA1000ResetFactoryDefaultAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2EA1000-MIB",
    **{"Float": Float,
       "trapEA1000ConfigChangeInteger": trapEA1000ConfigChangeInteger,
       "trapEA1000ConfigChangeDisplayString": trapEA1000ConfigChangeDisplayString,
       "trapEA1000RFInputAlarm": trapEA1000RFInputAlarm,
       "trapEA1000RFOverloadAlarm": trapEA1000RFOverloadAlarm,
       "trapEA1000RFOffsetAlarm": trapEA1000RFOffsetAlarm,
       "trapEA1000OpticalPowerAlarm": trapEA1000OpticalPowerAlarm,
       "trapEA1000LaserBiasAlarm": trapEA1000LaserBiasAlarm,
       "trapEA1000LaserTempAlarm": trapEA1000LaserTempAlarm,
       "trapEA1000TECCurrentAlarm": trapEA1000TECCurrentAlarm,
       "trapEA1000Fan1SpeedAlarm": trapEA1000Fan1SpeedAlarm,
       "trapEA1000Fan2SpeedAlarm": trapEA1000Fan2SpeedAlarm,
       "trapEA100012vAlarm": trapEA100012vAlarm,
       "trapEA1000ModuleTempAlarm": trapEA1000ModuleTempAlarm,
       "trapEA1000FlashAlarm": trapEA1000FlashAlarm,
       "trapEA1000LaserBiasCntLoopAlarm": trapEA1000LaserBiasCntLoopAlarm,
       "trapEA1000BankBootAlarm": trapEA1000BankBootAlarm,
       "trapEA1000LaserBiasCntLoopInitAlarm": trapEA1000LaserBiasCntLoopInitAlarm,
       "trapEA1000RFParamInitAlarm": trapEA1000RFParamInitAlarm,
       "trapEA1000TECParamInitAlarm": trapEA1000TECParamInitAlarm,
       "trapEA1000AttnTableInitAlarm": trapEA1000AttnTableInitAlarm,
       "trapEA1000PowerMeterTableInitAlarm": trapEA1000PowerMeterTableInitAlarm,
       "trapEA1000LaserDataCRCAlarm": trapEA1000LaserDataCRCAlarm,
       "trapEA1000AlarmDataCRCAlarm": trapEA1000AlarmDataCRCAlarm,
       "trapEA1000FactoryDataCRCAlarm": trapEA1000FactoryDataCRCAlarm,
       "trapEA1000UserRFOffAlarm": trapEA1000UserRFOffAlarm,
       "trapEA1000UserOpticalOffAlarm": trapEA1000UserOpticalOffAlarm,
       "trapEA1000ResetFactoryDefaultAlarm": trapEA1000ResetFactoryDefaultAlarm,
       "gx2ea1000Descriptor": gx2ea1000Descriptor,
       "gx2ea1000AnalogTable": gx2ea1000AnalogTable,
       "gx2ea1000AnalogEntry": gx2ea1000AnalogEntry,
       "gx2ea1000AnalogTableIndex": gx2ea1000AnalogTableIndex,
       "ea1000labelOffsetNomMonitor": ea1000labelOffsetNomMonitor,
       "ea1000uomOffsetNomMonitor": ea1000uomOffsetNomMonitor,
       "ea1000majorHighOffsetNomMonitor": ea1000majorHighOffsetNomMonitor,
       "ea1000majorLowOffsetNomMonitor": ea1000majorLowOffsetNomMonitor,
       "ea1000minorHighOffsetNomMonitor": ea1000minorHighOffsetNomMonitor,
       "ea1000minorLowOffsetNomMonitor": ea1000minorLowOffsetNomMonitor,
       "ea1000currentValueOffsetNomMonitor": ea1000currentValueOffsetNomMonitor,
       "ea1000stateFlagOffsetNomMonitor": ea1000stateFlagOffsetNomMonitor,
       "ea1000minValueOffsetNomMonitor": ea1000minValueOffsetNomMonitor,
       "ea1000maxValueOffsetNomMonitor": ea1000maxValueOffsetNomMonitor,
       "ea1000alarmStateOffsetNomMonitor": ea1000alarmStateOffsetNomMonitor,
       "ea1000labelOffsetNomCnt": ea1000labelOffsetNomCnt,
       "ea1000uomOffsetNomCnt": ea1000uomOffsetNomCnt,
       "ea1000majorHighOffsetNomCnt": ea1000majorHighOffsetNomCnt,
       "ea1000majorLowOffsetNomCnt": ea1000majorLowOffsetNomCnt,
       "ea1000minorHighOffsetNomCnt": ea1000minorHighOffsetNomCnt,
       "ea1000minorLowOffsetNomCnt": ea1000minorLowOffsetNomCnt,
       "ea1000currentValueOffsetNomCnt": ea1000currentValueOffsetNomCnt,
       "ea1000stateFlagOffsetNomCnt": ea1000stateFlagOffsetNomCnt,
       "ea1000minValueOffsetNomCnt": ea1000minValueOffsetNomCnt,
       "ea1000maxValueOffsetNomCnt": ea1000maxValueOffsetNomCnt,
       "ea1000alarmStateOffsetNomCnt": ea1000alarmStateOffsetNomCnt,
       "ea1000labelOptPower": ea1000labelOptPower,
       "ea1000uomOptPower": ea1000uomOptPower,
       "ea1000majorHighOptPower": ea1000majorHighOptPower,
       "ea1000majorLowOptPower": ea1000majorLowOptPower,
       "ea1000minorHighOptPower": ea1000minorHighOptPower,
       "ea1000minorLowOptPower": ea1000minorLowOptPower,
       "ea1000currentValueOptPower": ea1000currentValueOptPower,
       "ea1000stateFlagOptPower": ea1000stateFlagOptPower,
       "ea1000minValueOptPower": ea1000minValueOptPower,
       "ea1000maxValueOptPower": ea1000maxValueOptPower,
       "ea1000alarmStateOptPower": ea1000alarmStateOptPower,
       "ea1000labelLaserTemp": ea1000labelLaserTemp,
       "ea1000uomLaserTemp": ea1000uomLaserTemp,
       "ea1000majorHighLaserTemp": ea1000majorHighLaserTemp,
       "ea1000majorLowLaserTemp": ea1000majorLowLaserTemp,
       "ea1000minorHighLaserTemp": ea1000minorHighLaserTemp,
       "ea1000minorLowLaserTemp": ea1000minorLowLaserTemp,
       "ea1000currentValueLaserTemp": ea1000currentValueLaserTemp,
       "ea1000stateFlagLaserTemp": ea1000stateFlagLaserTemp,
       "ea1000minValueLaserTemp": ea1000minValueLaserTemp,
       "ea1000maxValueLaserTemp": ea1000maxValueLaserTemp,
       "ea1000alarmStateLaserTemp": ea1000alarmStateLaserTemp,
       "ea1000labelLaserBias": ea1000labelLaserBias,
       "ea1000uomLaserBias": ea1000uomLaserBias,
       "ea1000majorHighLaserBias": ea1000majorHighLaserBias,
       "ea1000majorLowLaserBias": ea1000majorLowLaserBias,
       "ea1000minorHighLaserBias": ea1000minorHighLaserBias,
       "ea1000minorLowLaserBias": ea1000minorLowLaserBias,
       "ea1000currentValueLaserBias": ea1000currentValueLaserBias,
       "ea1000stateFlagLaserBias": ea1000stateFlagLaserBias,
       "ea1000minValueLaserBias": ea1000minValueLaserBias,
       "ea1000maxValueLaserBias": ea1000maxValueLaserBias,
       "ea1000alarmStateLaserBias": ea1000alarmStateLaserBias,
       "ea1000labelTecCurrent": ea1000labelTecCurrent,
       "ea1000uomTecCurrent": ea1000uomTecCurrent,
       "ea1000majorHighTecCurrent": ea1000majorHighTecCurrent,
       "ea1000majorLowTecCurrent": ea1000majorLowTecCurrent,
       "ea1000minorHighTecCurrent": ea1000minorHighTecCurrent,
       "ea1000minorLowTecCurrent": ea1000minorLowTecCurrent,
       "ea1000currentValueTecCurrent": ea1000currentValueTecCurrent,
       "ea1000stateFlagTecCurrent": ea1000stateFlagTecCurrent,
       "ea1000minValueTecCurrent": ea1000minValueTecCurrent,
       "ea1000maxValueTecCurrent": ea1000maxValueTecCurrent,
       "ea1000alarmStateTecCurrent": ea1000alarmStateTecCurrent,
       "ea1000labelModuleTemp": ea1000labelModuleTemp,
       "ea1000uomModuleTemp": ea1000uomModuleTemp,
       "ea1000majorHighModuleTemp": ea1000majorHighModuleTemp,
       "ea1000majorLowModuleTemp": ea1000majorLowModuleTemp,
       "ea1000minorHighModuleTemp": ea1000minorHighModuleTemp,
       "ea1000minorLowModuleTemp": ea1000minorLowModuleTemp,
       "ea1000currentValueModuleTemp": ea1000currentValueModuleTemp,
       "ea1000stateFlagModuleTemp": ea1000stateFlagModuleTemp,
       "ea1000minValueModuleTemp": ea1000minValueModuleTemp,
       "ea1000maxValueModuleTemp": ea1000maxValueModuleTemp,
       "ea1000alarmStateModuleTemp": ea1000alarmStateModuleTemp,
       "ea1000labelFan1Speed": ea1000labelFan1Speed,
       "ea1000uomFan1Speed": ea1000uomFan1Speed,
       "ea1000majorHighFan1Speed": ea1000majorHighFan1Speed,
       "ea1000majorLowFan1Speed": ea1000majorLowFan1Speed,
       "ea1000minorHighFan1Speed": ea1000minorHighFan1Speed,
       "ea1000minorLowFan1Speed": ea1000minorLowFan1Speed,
       "ea1000currentValueFan1Speed": ea1000currentValueFan1Speed,
       "ea1000stateFlagFan1Speed": ea1000stateFlagFan1Speed,
       "ea1000minValueFan1Speed": ea1000minValueFan1Speed,
       "ea1000maxValueFan1Speed": ea1000maxValueFan1Speed,
       "ea1000alarmStateFan1Speed": ea1000alarmStateFan1Speed,
       "ea1000labelFan2Speed": ea1000labelFan2Speed,
       "ea1000uomFan2Speed": ea1000uomFan2Speed,
       "ea1000majorHighFan2Speed": ea1000majorHighFan2Speed,
       "ea1000majorLowFan2Speed": ea1000majorLowFan2Speed,
       "ea1000minorHighFan2Speed": ea1000minorHighFan2Speed,
       "ea1000minorLowFan2Speed": ea1000minorLowFan2Speed,
       "ea1000currentValueFan2Speed": ea1000currentValueFan2Speed,
       "ea1000stateFlagFan2Speed": ea1000stateFlagFan2Speed,
       "ea1000minValueFan2Speed": ea1000minValueFan2Speed,
       "ea1000maxValueFan2Speed": ea1000maxValueFan2Speed,
       "ea1000alarmStateFan2Speed": ea1000alarmStateFan2Speed,
       "ea1000label12Volt": ea1000label12Volt,
       "ea1000uom12Volt": ea1000uom12Volt,
       "ea1000majorHigh12Volt": ea1000majorHigh12Volt,
       "ea1000majorLow12Volt": ea1000majorLow12Volt,
       "ea1000minorHigh12Volt": ea1000minorHigh12Volt,
       "ea1000minorLow12Volt": ea1000minorLow12Volt,
       "ea1000currentValue12Volt": ea1000currentValue12Volt,
       "ea1000stateFlag12Volt": ea1000stateFlag12Volt,
       "ea1000minValue12Volt": ea1000minValue12Volt,
       "ea1000maxValue12Volt": ea1000maxValue12Volt,
       "ea1000alarmState12Volt": ea1000alarmState12Volt,
       "gx2ea1000DigitalTable": gx2ea1000DigitalTable,
       "gx2ea1000DigitalEntry": gx2ea1000DigitalEntry,
       "gx2ea1000DigitalTableIndex": gx2ea1000DigitalTableIndex,
       "ea1000labelRfInput": ea1000labelRfInput,
       "ea1000enumRfInput": ea1000enumRfInput,
       "ea1000valueRfInput": ea1000valueRfInput,
       "ea1000stateflagRfInput": ea1000stateflagRfInput,
       "ea1000labelOptOutput": ea1000labelOptOutput,
       "ea1000enumOptOutput": ea1000enumOptOutput,
       "ea1000valueOptOutput": ea1000valueOptOutput,
       "ea1000stateflagOptOutput": ea1000stateflagOptOutput,
       "ea1000labelLaserMode": ea1000labelLaserMode,
       "ea1000enumLaserMode": ea1000enumLaserMode,
       "ea1000valueLaserMode": ea1000valueLaserMode,
       "ea1000stateflagLaserMode": ea1000stateflagLaserMode,
       "ea1000labelAttenSetting": ea1000labelAttenSetting,
       "ea1000enumAttenSetting": ea1000enumAttenSetting,
       "ea1000valueAttenSetting": ea1000valueAttenSetting,
       "ea1000stateflagAttenSetting": ea1000stateflagAttenSetting,
       "ea1000labelLaserSecMode": ea1000labelLaserSecMode,
       "ea1000enumLaserSecMode": ea1000enumLaserSecMode,
       "ea1000valueLaserSecMode": ea1000valueLaserSecMode,
       "ea1000stateflagLaserSecMode": ea1000stateflagLaserSecMode,
       "ea1000labelVideoOffset": ea1000labelVideoOffset,
       "ea1000enumVideoOffset": ea1000enumVideoOffset,
       "ea1000valueVideoOffset": ea1000valueVideoOffset,
       "ea1000stateflagVideoOffset": ea1000stateflagVideoOffset,
       "ea1000labelFactoryDefault": ea1000labelFactoryDefault,
       "ea1000enumFactoryDefault": ea1000enumFactoryDefault,
       "ea1000valueFactoryDefault": ea1000valueFactoryDefault,
       "ea1000stateflagFactoryDefault": ea1000stateflagFactoryDefault,
       "gx2ea1000StatusTable": gx2ea1000StatusTable,
       "gx2ea1000StatusEntry": gx2ea1000StatusEntry,
       "gx2ea1000StatusTableIndex": gx2ea1000StatusTableIndex,
       "ea1000labelBoot": ea1000labelBoot,
       "ea1000valueBoot": ea1000valueBoot,
       "ea1000stateflagBoot": ea1000stateflagBoot,
       "ea1000labelFlash": ea1000labelFlash,
       "ea1000valueFlash": ea1000valueFlash,
       "ea1000stateflagFlash": ea1000stateflagFlash,
       "ea1000labelFactoryDataCRC": ea1000labelFactoryDataCRC,
       "ea1000valueFactoryDataCRC": ea1000valueFactoryDataCRC,
       "ea1000stateflagFactoryDataCRC": ea1000stateflagFactoryDataCRC,
       "ea1000labelLaserDataCRC": ea1000labelLaserDataCRC,
       "ea1000valueLaserDataCRC": ea1000valueLaserDataCRC,
       "ea1000stateflagLaserDataCRC": ea1000stateflagLaserDataCRC,
       "ea1000labelAlarmDataCrc": ea1000labelAlarmDataCrc,
       "ea1000valueAlarmDataCrc": ea1000valueAlarmDataCrc,
       "ea1000stateflagAlarmDataCrc": ea1000stateflagAlarmDataCrc,
       "ea1000labelRFInputStatus": ea1000labelRFInputStatus,
       "ea1000valueRFInputStatus": ea1000valueRFInputStatus,
       "ea1000stateflagRFInputStatus": ea1000stateflagRFInputStatus,
       "gx2ea1000FactoryTable": gx2ea1000FactoryTable,
       "gx2ea1000FactoryEntry": gx2ea1000FactoryEntry,
       "gx2ea1000FactoryTableIndex": gx2ea1000FactoryTableIndex,
       "ea1000bootControlByteValue": ea1000bootControlByteValue,
       "ea1000bootStatusByteValue": ea1000bootStatusByteValue,
       "ea1000bank1CRCValue": ea1000bank1CRCValue,
       "ea1000bank2CRCValue": ea1000bank2CRCValue,
       "ea1000prgEEPROMByteValue": ea1000prgEEPROMByteValue,
       "ea1000factoryCRCValue": ea1000factoryCRCValue,
       "ea1000calculateCRCValue": ea1000calculateCRCValue,
       "ea1000hourMeterValue": ea1000hourMeterValue,
       "ea1000flashPrgCntAValue": ea1000flashPrgCntAValue,
       "ea1000flashPrgCntBValue": ea1000flashPrgCntBValue,
       "ea1000flashBankARevValue": ea1000flashBankARevValue,
       "ea1000flashBankBRevValue": ea1000flashBankBRevValue}
)
