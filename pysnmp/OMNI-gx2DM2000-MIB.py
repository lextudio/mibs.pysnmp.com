# SNMP MIB module (OMNI-gx2DM2000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2DM2000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:14 2024
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

(gx2Dm2000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Dm2000")

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

_Gx2dm2000Descriptor_ObjectIdentity = ObjectIdentity
gx2dm2000Descriptor = _Gx2dm2000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 1)
)
_Gx2dm2000AnalogTable_Object = MibTable
gx2dm2000AnalogTable = _Gx2dm2000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2)
)
if mibBuilder.loadTexts:
    gx2dm2000AnalogTable.setStatus("mandatory")
_Gx2dm2000AnalogEntry_Object = MibTableRow
gx2dm2000AnalogEntry = _Gx2dm2000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1)
)
gx2dm2000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2DM2000-MIB", "gx2dm2000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dm2000AnalogEntry.setStatus("mandatory")


class _Gx2dm2000AnalogTableIndex_Type(Integer32):
    """Custom type gx2dm2000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2dm2000AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2dm2000AnalogTableIndex_Object = MibTableColumn
gx2dm2000AnalogTableIndex = _Gx2dm2000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 1),
    _Gx2dm2000AnalogTableIndex_Type()
)
gx2dm2000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dm2000AnalogTableIndex.setStatus("mandatory")


class _Dm2000labelOffsetNomMonitor_Type(DisplayString):
    """Custom type dm2000labelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm2000labelOffsetNomMonitor_Object = MibTableColumn
dm2000labelOffsetNomMonitor = _Dm2000labelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 2),
    _Dm2000labelOffsetNomMonitor_Type()
)
dm2000labelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelOffsetNomMonitor.setStatus("optional")


class _Dm2000uomOffsetNomMonitor_Type(DisplayString):
    """Custom type dm2000uomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomOffsetNomMonitor_Type.__name__ = "DisplayString"
_Dm2000uomOffsetNomMonitor_Object = MibTableColumn
dm2000uomOffsetNomMonitor = _Dm2000uomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 3),
    _Dm2000uomOffsetNomMonitor_Type()
)
dm2000uomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomOffsetNomMonitor.setStatus("optional")
_Dm2000majorHighOffsetNomMonitor_Type = Float
_Dm2000majorHighOffsetNomMonitor_Object = MibTableColumn
dm2000majorHighOffsetNomMonitor = _Dm2000majorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 4),
    _Dm2000majorHighOffsetNomMonitor_Type()
)
dm2000majorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighOffsetNomMonitor.setStatus("mandatory")
_Dm2000majorLowOffsetNomMonitor_Type = Float
_Dm2000majorLowOffsetNomMonitor_Object = MibTableColumn
dm2000majorLowOffsetNomMonitor = _Dm2000majorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 5),
    _Dm2000majorLowOffsetNomMonitor_Type()
)
dm2000majorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowOffsetNomMonitor.setStatus("mandatory")
_Dm2000minorHighOffsetNomMonitor_Type = Float
_Dm2000minorHighOffsetNomMonitor_Object = MibTableColumn
dm2000minorHighOffsetNomMonitor = _Dm2000minorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 6),
    _Dm2000minorHighOffsetNomMonitor_Type()
)
dm2000minorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighOffsetNomMonitor.setStatus("mandatory")
_Dm2000minorLowOffsetNomMonitor_Type = Float
_Dm2000minorLowOffsetNomMonitor_Object = MibTableColumn
dm2000minorLowOffsetNomMonitor = _Dm2000minorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 7),
    _Dm2000minorLowOffsetNomMonitor_Type()
)
dm2000minorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowOffsetNomMonitor.setStatus("mandatory")
_Dm2000currentValueOffsetNomMonitor_Type = Float
_Dm2000currentValueOffsetNomMonitor_Object = MibTableColumn
dm2000currentValueOffsetNomMonitor = _Dm2000currentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 8),
    _Dm2000currentValueOffsetNomMonitor_Type()
)
dm2000currentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueOffsetNomMonitor.setStatus("mandatory")


class _Dm2000stateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type dm2000stateFlagOffsetNomMonitor based on Integer32"""
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


_Dm2000stateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm2000stateFlagOffsetNomMonitor_Object = MibTableColumn
dm2000stateFlagOffsetNomMonitor = _Dm2000stateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 9),
    _Dm2000stateFlagOffsetNomMonitor_Type()
)
dm2000stateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagOffsetNomMonitor.setStatus("mandatory")
_Dm2000minValueOffsetNomMonitor_Type = Float
_Dm2000minValueOffsetNomMonitor_Object = MibTableColumn
dm2000minValueOffsetNomMonitor = _Dm2000minValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 10),
    _Dm2000minValueOffsetNomMonitor_Type()
)
dm2000minValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueOffsetNomMonitor.setStatus("mandatory")
_Dm2000maxValueOffsetNomMonitor_Type = Float
_Dm2000maxValueOffsetNomMonitor_Object = MibTableColumn
dm2000maxValueOffsetNomMonitor = _Dm2000maxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 11),
    _Dm2000maxValueOffsetNomMonitor_Type()
)
dm2000maxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueOffsetNomMonitor.setStatus("mandatory")


class _Dm2000alarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type dm2000alarmStateOffsetNomMonitor based on Integer32"""
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


_Dm2000alarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_Dm2000alarmStateOffsetNomMonitor_Object = MibTableColumn
dm2000alarmStateOffsetNomMonitor = _Dm2000alarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 12),
    _Dm2000alarmStateOffsetNomMonitor_Type()
)
dm2000alarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateOffsetNomMonitor.setStatus("mandatory")


class _Dm2000labelOffsetNomCnt_Type(DisplayString):
    """Custom type dm2000labelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm2000labelOffsetNomCnt_Object = MibTableColumn
dm2000labelOffsetNomCnt = _Dm2000labelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 13),
    _Dm2000labelOffsetNomCnt_Type()
)
dm2000labelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelOffsetNomCnt.setStatus("optional")


class _Dm2000uomOffsetNomCnt_Type(DisplayString):
    """Custom type dm2000uomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomOffsetNomCnt_Type.__name__ = "DisplayString"
_Dm2000uomOffsetNomCnt_Object = MibTableColumn
dm2000uomOffsetNomCnt = _Dm2000uomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 14),
    _Dm2000uomOffsetNomCnt_Type()
)
dm2000uomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomOffsetNomCnt.setStatus("optional")
_Dm2000majorHighOffsetNomCnt_Type = Float
_Dm2000majorHighOffsetNomCnt_Object = MibTableColumn
dm2000majorHighOffsetNomCnt = _Dm2000majorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 15),
    _Dm2000majorHighOffsetNomCnt_Type()
)
dm2000majorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighOffsetNomCnt.setStatus("mandatory")
_Dm2000majorLowOffsetNomCnt_Type = Float
_Dm2000majorLowOffsetNomCnt_Object = MibTableColumn
dm2000majorLowOffsetNomCnt = _Dm2000majorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 16),
    _Dm2000majorLowOffsetNomCnt_Type()
)
dm2000majorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowOffsetNomCnt.setStatus("mandatory")
_Dm2000minorHighOffsetNomCnt_Type = Float
_Dm2000minorHighOffsetNomCnt_Object = MibTableColumn
dm2000minorHighOffsetNomCnt = _Dm2000minorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 17),
    _Dm2000minorHighOffsetNomCnt_Type()
)
dm2000minorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighOffsetNomCnt.setStatus("mandatory")
_Dm2000minorLowOffsetNomCnt_Type = Float
_Dm2000minorLowOffsetNomCnt_Object = MibTableColumn
dm2000minorLowOffsetNomCnt = _Dm2000minorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 18),
    _Dm2000minorLowOffsetNomCnt_Type()
)
dm2000minorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowOffsetNomCnt.setStatus("mandatory")
_Dm2000currentValueOffsetNomCnt_Type = Float
_Dm2000currentValueOffsetNomCnt_Object = MibTableColumn
dm2000currentValueOffsetNomCnt = _Dm2000currentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 19),
    _Dm2000currentValueOffsetNomCnt_Type()
)
dm2000currentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000currentValueOffsetNomCnt.setStatus("mandatory")


class _Dm2000stateFlagOffsetNomCnt_Type(Integer32):
    """Custom type dm2000stateFlagOffsetNomCnt based on Integer32"""
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


_Dm2000stateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_Dm2000stateFlagOffsetNomCnt_Object = MibTableColumn
dm2000stateFlagOffsetNomCnt = _Dm2000stateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 20),
    _Dm2000stateFlagOffsetNomCnt_Type()
)
dm2000stateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagOffsetNomCnt.setStatus("mandatory")
_Dm2000minValueOffsetNomCnt_Type = Float
_Dm2000minValueOffsetNomCnt_Object = MibTableColumn
dm2000minValueOffsetNomCnt = _Dm2000minValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 21),
    _Dm2000minValueOffsetNomCnt_Type()
)
dm2000minValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueOffsetNomCnt.setStatus("mandatory")
_Dm2000maxValueOffsetNomCnt_Type = Float
_Dm2000maxValueOffsetNomCnt_Object = MibTableColumn
dm2000maxValueOffsetNomCnt = _Dm2000maxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 22),
    _Dm2000maxValueOffsetNomCnt_Type()
)
dm2000maxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueOffsetNomCnt.setStatus("mandatory")


class _Dm2000alarmStateOffsetNomCnt_Type(Integer32):
    """Custom type dm2000alarmStateOffsetNomCnt based on Integer32"""
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


_Dm2000alarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_Dm2000alarmStateOffsetNomCnt_Object = MibTableColumn
dm2000alarmStateOffsetNomCnt = _Dm2000alarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 23),
    _Dm2000alarmStateOffsetNomCnt_Type()
)
dm2000alarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateOffsetNomCnt.setStatus("mandatory")


class _Dm2000labelRelAttenSetting_Type(DisplayString):
    """Custom type dm2000labelRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelRelAttenSetting_Type.__name__ = "DisplayString"
_Dm2000labelRelAttenSetting_Object = MibTableColumn
dm2000labelRelAttenSetting = _Dm2000labelRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 24),
    _Dm2000labelRelAttenSetting_Type()
)
dm2000labelRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelRelAttenSetting.setStatus("optional")


class _Dm2000uomRelAttenSetting_Type(DisplayString):
    """Custom type dm2000uomRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomRelAttenSetting_Type.__name__ = "DisplayString"
_Dm2000uomRelAttenSetting_Object = MibTableColumn
dm2000uomRelAttenSetting = _Dm2000uomRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 25),
    _Dm2000uomRelAttenSetting_Type()
)
dm2000uomRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomRelAttenSetting.setStatus("optional")
_Dm2000majorHighRelAttenSetting_Type = Float
_Dm2000majorHighRelAttenSetting_Object = MibTableColumn
dm2000majorHighRelAttenSetting = _Dm2000majorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 26),
    _Dm2000majorHighRelAttenSetting_Type()
)
dm2000majorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighRelAttenSetting.setStatus("mandatory")
_Dm2000majorLowRelAttenSetting_Type = Float
_Dm2000majorLowRelAttenSetting_Object = MibTableColumn
dm2000majorLowRelAttenSetting = _Dm2000majorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 27),
    _Dm2000majorLowRelAttenSetting_Type()
)
dm2000majorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowRelAttenSetting.setStatus("mandatory")
_Dm2000minorHighRelAttenSetting_Type = Float
_Dm2000minorHighRelAttenSetting_Object = MibTableColumn
dm2000minorHighRelAttenSetting = _Dm2000minorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 28),
    _Dm2000minorHighRelAttenSetting_Type()
)
dm2000minorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighRelAttenSetting.setStatus("mandatory")
_Dm2000minorLowRelAttenSetting_Type = Float
_Dm2000minorLowRelAttenSetting_Object = MibTableColumn
dm2000minorLowRelAttenSetting = _Dm2000minorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 29),
    _Dm2000minorLowRelAttenSetting_Type()
)
dm2000minorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowRelAttenSetting.setStatus("mandatory")
_Dm2000currentValueRelAttenSetting_Type = Float
_Dm2000currentValueRelAttenSetting_Object = MibTableColumn
dm2000currentValueRelAttenSetting = _Dm2000currentValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 30),
    _Dm2000currentValueRelAttenSetting_Type()
)
dm2000currentValueRelAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000currentValueRelAttenSetting.setStatus("mandatory")


class _Dm2000stateFlagRelAttenSetting_Type(Integer32):
    """Custom type dm2000stateFlagRelAttenSetting based on Integer32"""
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


_Dm2000stateFlagRelAttenSetting_Type.__name__ = "Integer32"
_Dm2000stateFlagRelAttenSetting_Object = MibTableColumn
dm2000stateFlagRelAttenSetting = _Dm2000stateFlagRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 31),
    _Dm2000stateFlagRelAttenSetting_Type()
)
dm2000stateFlagRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagRelAttenSetting.setStatus("mandatory")
_Dm2000minValueRelAttenSetting_Type = Float
_Dm2000minValueRelAttenSetting_Object = MibTableColumn
dm2000minValueRelAttenSetting = _Dm2000minValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 32),
    _Dm2000minValueRelAttenSetting_Type()
)
dm2000minValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueRelAttenSetting.setStatus("mandatory")
_Dm2000maxValueRelAttenSetting_Type = Float
_Dm2000maxValueRelAttenSetting_Object = MibTableColumn
dm2000maxValueRelAttenSetting = _Dm2000maxValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 33),
    _Dm2000maxValueRelAttenSetting_Type()
)
dm2000maxValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueRelAttenSetting.setStatus("mandatory")


class _Dm2000alarmStateRelAttenSetting_Type(Integer32):
    """Custom type dm2000alarmStateRelAttenSetting based on Integer32"""
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


_Dm2000alarmStateRelAttenSetting_Type.__name__ = "Integer32"
_Dm2000alarmStateRelAttenSetting_Object = MibTableColumn
dm2000alarmStateRelAttenSetting = _Dm2000alarmStateRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 34),
    _Dm2000alarmStateRelAttenSetting_Type()
)
dm2000alarmStateRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateRelAttenSetting.setStatus("mandatory")


class _Dm2000labelOptPower_Type(DisplayString):
    """Custom type dm2000labelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelOptPower_Type.__name__ = "DisplayString"
_Dm2000labelOptPower_Object = MibTableColumn
dm2000labelOptPower = _Dm2000labelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 35),
    _Dm2000labelOptPower_Type()
)
dm2000labelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelOptPower.setStatus("optional")


class _Dm2000uomOptPower_Type(DisplayString):
    """Custom type dm2000uomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomOptPower_Type.__name__ = "DisplayString"
_Dm2000uomOptPower_Object = MibTableColumn
dm2000uomOptPower = _Dm2000uomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 36),
    _Dm2000uomOptPower_Type()
)
dm2000uomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomOptPower.setStatus("optional")
_Dm2000majorHighOptPower_Type = Float
_Dm2000majorHighOptPower_Object = MibTableColumn
dm2000majorHighOptPower = _Dm2000majorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 37),
    _Dm2000majorHighOptPower_Type()
)
dm2000majorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighOptPower.setStatus("mandatory")
_Dm2000majorLowOptPower_Type = Float
_Dm2000majorLowOptPower_Object = MibTableColumn
dm2000majorLowOptPower = _Dm2000majorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 38),
    _Dm2000majorLowOptPower_Type()
)
dm2000majorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowOptPower.setStatus("mandatory")
_Dm2000minorHighOptPower_Type = Float
_Dm2000minorHighOptPower_Object = MibTableColumn
dm2000minorHighOptPower = _Dm2000minorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 39),
    _Dm2000minorHighOptPower_Type()
)
dm2000minorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighOptPower.setStatus("mandatory")
_Dm2000minorLowOptPower_Type = Float
_Dm2000minorLowOptPower_Object = MibTableColumn
dm2000minorLowOptPower = _Dm2000minorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 40),
    _Dm2000minorLowOptPower_Type()
)
dm2000minorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowOptPower.setStatus("mandatory")
_Dm2000currentValueOptPower_Type = Float
_Dm2000currentValueOptPower_Object = MibTableColumn
dm2000currentValueOptPower = _Dm2000currentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 41),
    _Dm2000currentValueOptPower_Type()
)
dm2000currentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueOptPower.setStatus("mandatory")


class _Dm2000stateFlagOptPower_Type(Integer32):
    """Custom type dm2000stateFlagOptPower based on Integer32"""
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


_Dm2000stateFlagOptPower_Type.__name__ = "Integer32"
_Dm2000stateFlagOptPower_Object = MibTableColumn
dm2000stateFlagOptPower = _Dm2000stateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 42),
    _Dm2000stateFlagOptPower_Type()
)
dm2000stateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagOptPower.setStatus("mandatory")
_Dm2000minValueOptPower_Type = Float
_Dm2000minValueOptPower_Object = MibTableColumn
dm2000minValueOptPower = _Dm2000minValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 43),
    _Dm2000minValueOptPower_Type()
)
dm2000minValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueOptPower.setStatus("mandatory")
_Dm2000maxValueOptPower_Type = Float
_Dm2000maxValueOptPower_Object = MibTableColumn
dm2000maxValueOptPower = _Dm2000maxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 44),
    _Dm2000maxValueOptPower_Type()
)
dm2000maxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueOptPower.setStatus("mandatory")


class _Dm2000alarmStateOptPower_Type(Integer32):
    """Custom type dm2000alarmStateOptPower based on Integer32"""
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


_Dm2000alarmStateOptPower_Type.__name__ = "Integer32"
_Dm2000alarmStateOptPower_Object = MibTableColumn
dm2000alarmStateOptPower = _Dm2000alarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 45),
    _Dm2000alarmStateOptPower_Type()
)
dm2000alarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateOptPower.setStatus("mandatory")


class _Dm2000labelLaserBias_Type(DisplayString):
    """Custom type dm2000labelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelLaserBias_Type.__name__ = "DisplayString"
_Dm2000labelLaserBias_Object = MibTableColumn
dm2000labelLaserBias = _Dm2000labelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 46),
    _Dm2000labelLaserBias_Type()
)
dm2000labelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelLaserBias.setStatus("optional")


class _Dm2000uomLaserBias_Type(DisplayString):
    """Custom type dm2000uomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomLaserBias_Type.__name__ = "DisplayString"
_Dm2000uomLaserBias_Object = MibTableColumn
dm2000uomLaserBias = _Dm2000uomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 47),
    _Dm2000uomLaserBias_Type()
)
dm2000uomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomLaserBias.setStatus("optional")
_Dm2000majorHighLaserBias_Type = Float
_Dm2000majorHighLaserBias_Object = MibTableColumn
dm2000majorHighLaserBias = _Dm2000majorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 48),
    _Dm2000majorHighLaserBias_Type()
)
dm2000majorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighLaserBias.setStatus("mandatory")
_Dm2000majorLowLaserBias_Type = Float
_Dm2000majorLowLaserBias_Object = MibTableColumn
dm2000majorLowLaserBias = _Dm2000majorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 49),
    _Dm2000majorLowLaserBias_Type()
)
dm2000majorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowLaserBias.setStatus("mandatory")
_Dm2000minorHighLaserBias_Type = Float
_Dm2000minorHighLaserBias_Object = MibTableColumn
dm2000minorHighLaserBias = _Dm2000minorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 50),
    _Dm2000minorHighLaserBias_Type()
)
dm2000minorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighLaserBias.setStatus("mandatory")
_Dm2000minorLowLaserBias_Type = Float
_Dm2000minorLowLaserBias_Object = MibTableColumn
dm2000minorLowLaserBias = _Dm2000minorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 51),
    _Dm2000minorLowLaserBias_Type()
)
dm2000minorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowLaserBias.setStatus("mandatory")
_Dm2000currentValueLaserBias_Type = Float
_Dm2000currentValueLaserBias_Object = MibTableColumn
dm2000currentValueLaserBias = _Dm2000currentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 52),
    _Dm2000currentValueLaserBias_Type()
)
dm2000currentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueLaserBias.setStatus("mandatory")


class _Dm2000stateFlagLaserBias_Type(Integer32):
    """Custom type dm2000stateFlagLaserBias based on Integer32"""
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


_Dm2000stateFlagLaserBias_Type.__name__ = "Integer32"
_Dm2000stateFlagLaserBias_Object = MibTableColumn
dm2000stateFlagLaserBias = _Dm2000stateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 53),
    _Dm2000stateFlagLaserBias_Type()
)
dm2000stateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagLaserBias.setStatus("mandatory")
_Dm2000minValueLaserBias_Type = Float
_Dm2000minValueLaserBias_Object = MibTableColumn
dm2000minValueLaserBias = _Dm2000minValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 54),
    _Dm2000minValueLaserBias_Type()
)
dm2000minValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueLaserBias.setStatus("mandatory")
_Dm2000maxValueLaserBias_Type = Float
_Dm2000maxValueLaserBias_Object = MibTableColumn
dm2000maxValueLaserBias = _Dm2000maxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 55),
    _Dm2000maxValueLaserBias_Type()
)
dm2000maxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueLaserBias.setStatus("mandatory")


class _Dm2000alarmStateLaserBias_Type(Integer32):
    """Custom type dm2000alarmStateLaserBias based on Integer32"""
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


_Dm2000alarmStateLaserBias_Type.__name__ = "Integer32"
_Dm2000alarmStateLaserBias_Object = MibTableColumn
dm2000alarmStateLaserBias = _Dm2000alarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 56),
    _Dm2000alarmStateLaserBias_Type()
)
dm2000alarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateLaserBias.setStatus("mandatory")


class _Dm2000labelTecCurrent_Type(DisplayString):
    """Custom type dm2000labelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelTecCurrent_Type.__name__ = "DisplayString"
_Dm2000labelTecCurrent_Object = MibTableColumn
dm2000labelTecCurrent = _Dm2000labelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 57),
    _Dm2000labelTecCurrent_Type()
)
dm2000labelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelTecCurrent.setStatus("optional")


class _Dm2000uomTecCurrent_Type(DisplayString):
    """Custom type dm2000uomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomTecCurrent_Type.__name__ = "DisplayString"
_Dm2000uomTecCurrent_Object = MibTableColumn
dm2000uomTecCurrent = _Dm2000uomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 58),
    _Dm2000uomTecCurrent_Type()
)
dm2000uomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomTecCurrent.setStatus("optional")
_Dm2000majorHighTecCurrent_Type = Float
_Dm2000majorHighTecCurrent_Object = MibTableColumn
dm2000majorHighTecCurrent = _Dm2000majorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 59),
    _Dm2000majorHighTecCurrent_Type()
)
dm2000majorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighTecCurrent.setStatus("mandatory")
_Dm2000majorLowTecCurrent_Type = Float
_Dm2000majorLowTecCurrent_Object = MibTableColumn
dm2000majorLowTecCurrent = _Dm2000majorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 60),
    _Dm2000majorLowTecCurrent_Type()
)
dm2000majorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowTecCurrent.setStatus("mandatory")
_Dm2000minorHighTecCurrent_Type = Float
_Dm2000minorHighTecCurrent_Object = MibTableColumn
dm2000minorHighTecCurrent = _Dm2000minorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 61),
    _Dm2000minorHighTecCurrent_Type()
)
dm2000minorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighTecCurrent.setStatus("mandatory")
_Dm2000minorLowTecCurrent_Type = Float
_Dm2000minorLowTecCurrent_Object = MibTableColumn
dm2000minorLowTecCurrent = _Dm2000minorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 62),
    _Dm2000minorLowTecCurrent_Type()
)
dm2000minorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowTecCurrent.setStatus("mandatory")
_Dm2000currentValueTecCurrent_Type = Float
_Dm2000currentValueTecCurrent_Object = MibTableColumn
dm2000currentValueTecCurrent = _Dm2000currentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 63),
    _Dm2000currentValueTecCurrent_Type()
)
dm2000currentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueTecCurrent.setStatus("mandatory")


class _Dm2000stateFlagTecCurrent_Type(Integer32):
    """Custom type dm2000stateFlagTecCurrent based on Integer32"""
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


_Dm2000stateFlagTecCurrent_Type.__name__ = "Integer32"
_Dm2000stateFlagTecCurrent_Object = MibTableColumn
dm2000stateFlagTecCurrent = _Dm2000stateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 64),
    _Dm2000stateFlagTecCurrent_Type()
)
dm2000stateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagTecCurrent.setStatus("mandatory")
_Dm2000minValueTecCurrent_Type = Float
_Dm2000minValueTecCurrent_Object = MibTableColumn
dm2000minValueTecCurrent = _Dm2000minValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 65),
    _Dm2000minValueTecCurrent_Type()
)
dm2000minValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueTecCurrent.setStatus("mandatory")
_Dm2000maxValueTecCurrent_Type = Float
_Dm2000maxValueTecCurrent_Object = MibTableColumn
dm2000maxValueTecCurrent = _Dm2000maxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 66),
    _Dm2000maxValueTecCurrent_Type()
)
dm2000maxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueTecCurrent.setStatus("mandatory")


class _Dm2000alarmStateTecCurrent_Type(Integer32):
    """Custom type dm2000alarmStateTecCurrent based on Integer32"""
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


_Dm2000alarmStateTecCurrent_Type.__name__ = "Integer32"
_Dm2000alarmStateTecCurrent_Object = MibTableColumn
dm2000alarmStateTecCurrent = _Dm2000alarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 67),
    _Dm2000alarmStateTecCurrent_Type()
)
dm2000alarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateTecCurrent.setStatus("mandatory")


class _Dm2000labelLaserTemp_Type(DisplayString):
    """Custom type dm2000labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelLaserTemp_Type.__name__ = "DisplayString"
_Dm2000labelLaserTemp_Object = MibTableColumn
dm2000labelLaserTemp = _Dm2000labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 68),
    _Dm2000labelLaserTemp_Type()
)
dm2000labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelLaserTemp.setStatus("optional")


class _Dm2000uomLaserTemp_Type(DisplayString):
    """Custom type dm2000uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomLaserTemp_Type.__name__ = "DisplayString"
_Dm2000uomLaserTemp_Object = MibTableColumn
dm2000uomLaserTemp = _Dm2000uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 69),
    _Dm2000uomLaserTemp_Type()
)
dm2000uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomLaserTemp.setStatus("optional")
_Dm2000majorHighLaserTemp_Type = Float
_Dm2000majorHighLaserTemp_Object = MibTableColumn
dm2000majorHighLaserTemp = _Dm2000majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 70),
    _Dm2000majorHighLaserTemp_Type()
)
dm2000majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighLaserTemp.setStatus("mandatory")
_Dm2000majorLowLaserTemp_Type = Float
_Dm2000majorLowLaserTemp_Object = MibTableColumn
dm2000majorLowLaserTemp = _Dm2000majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 71),
    _Dm2000majorLowLaserTemp_Type()
)
dm2000majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowLaserTemp.setStatus("mandatory")
_Dm2000minorHighLaserTemp_Type = Float
_Dm2000minorHighLaserTemp_Object = MibTableColumn
dm2000minorHighLaserTemp = _Dm2000minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 72),
    _Dm2000minorHighLaserTemp_Type()
)
dm2000minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighLaserTemp.setStatus("mandatory")
_Dm2000minorLowLaserTemp_Type = Float
_Dm2000minorLowLaserTemp_Object = MibTableColumn
dm2000minorLowLaserTemp = _Dm2000minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 73),
    _Dm2000minorLowLaserTemp_Type()
)
dm2000minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowLaserTemp.setStatus("mandatory")
_Dm2000currentValueLaserTemp_Type = Float
_Dm2000currentValueLaserTemp_Object = MibTableColumn
dm2000currentValueLaserTemp = _Dm2000currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 74),
    _Dm2000currentValueLaserTemp_Type()
)
dm2000currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueLaserTemp.setStatus("mandatory")


class _Dm2000stateFlagLaserTemp_Type(Integer32):
    """Custom type dm2000stateFlagLaserTemp based on Integer32"""
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


_Dm2000stateFlagLaserTemp_Type.__name__ = "Integer32"
_Dm2000stateFlagLaserTemp_Object = MibTableColumn
dm2000stateFlagLaserTemp = _Dm2000stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 75),
    _Dm2000stateFlagLaserTemp_Type()
)
dm2000stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagLaserTemp.setStatus("mandatory")
_Dm2000minValueLaserTemp_Type = Float
_Dm2000minValueLaserTemp_Object = MibTableColumn
dm2000minValueLaserTemp = _Dm2000minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 76),
    _Dm2000minValueLaserTemp_Type()
)
dm2000minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueLaserTemp.setStatus("mandatory")
_Dm2000maxValueLaserTemp_Type = Float
_Dm2000maxValueLaserTemp_Object = MibTableColumn
dm2000maxValueLaserTemp = _Dm2000maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 77),
    _Dm2000maxValueLaserTemp_Type()
)
dm2000maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueLaserTemp.setStatus("mandatory")


class _Dm2000alarmStateLaserTemp_Type(Integer32):
    """Custom type dm2000alarmStateLaserTemp based on Integer32"""
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


_Dm2000alarmStateLaserTemp_Type.__name__ = "Integer32"
_Dm2000alarmStateLaserTemp_Object = MibTableColumn
dm2000alarmStateLaserTemp = _Dm2000alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 78),
    _Dm2000alarmStateLaserTemp_Type()
)
dm2000alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateLaserTemp.setStatus("mandatory")


class _Dm2000labelModuleTemp_Type(DisplayString):
    """Custom type dm2000labelModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelModuleTemp_Type.__name__ = "DisplayString"
_Dm2000labelModuleTemp_Object = MibTableColumn
dm2000labelModuleTemp = _Dm2000labelModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 79),
    _Dm2000labelModuleTemp_Type()
)
dm2000labelModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelModuleTemp.setStatus("optional")


class _Dm2000uomModuleTemp_Type(DisplayString):
    """Custom type dm2000uomModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomModuleTemp_Type.__name__ = "DisplayString"
_Dm2000uomModuleTemp_Object = MibTableColumn
dm2000uomModuleTemp = _Dm2000uomModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 80),
    _Dm2000uomModuleTemp_Type()
)
dm2000uomModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomModuleTemp.setStatus("optional")
_Dm2000majorHighModuleTemp_Type = Float
_Dm2000majorHighModuleTemp_Object = MibTableColumn
dm2000majorHighModuleTemp = _Dm2000majorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 81),
    _Dm2000majorHighModuleTemp_Type()
)
dm2000majorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighModuleTemp.setStatus("mandatory")
_Dm2000majorLowModuleTemp_Type = Float
_Dm2000majorLowModuleTemp_Object = MibTableColumn
dm2000majorLowModuleTemp = _Dm2000majorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 82),
    _Dm2000majorLowModuleTemp_Type()
)
dm2000majorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowModuleTemp.setStatus("mandatory")
_Dm2000minorHighModuleTemp_Type = Float
_Dm2000minorHighModuleTemp_Object = MibTableColumn
dm2000minorHighModuleTemp = _Dm2000minorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 83),
    _Dm2000minorHighModuleTemp_Type()
)
dm2000minorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighModuleTemp.setStatus("mandatory")
_Dm2000minorLowModuleTemp_Type = Float
_Dm2000minorLowModuleTemp_Object = MibTableColumn
dm2000minorLowModuleTemp = _Dm2000minorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 84),
    _Dm2000minorLowModuleTemp_Type()
)
dm2000minorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowModuleTemp.setStatus("mandatory")
_Dm2000currentValueModuleTemp_Type = Float
_Dm2000currentValueModuleTemp_Object = MibTableColumn
dm2000currentValueModuleTemp = _Dm2000currentValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 85),
    _Dm2000currentValueModuleTemp_Type()
)
dm2000currentValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueModuleTemp.setStatus("mandatory")


class _Dm2000stateFlagModuleTemp_Type(Integer32):
    """Custom type dm2000stateFlagModuleTemp based on Integer32"""
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


_Dm2000stateFlagModuleTemp_Type.__name__ = "Integer32"
_Dm2000stateFlagModuleTemp_Object = MibTableColumn
dm2000stateFlagModuleTemp = _Dm2000stateFlagModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 86),
    _Dm2000stateFlagModuleTemp_Type()
)
dm2000stateFlagModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagModuleTemp.setStatus("mandatory")
_Dm2000minValueModuleTemp_Type = Float
_Dm2000minValueModuleTemp_Object = MibTableColumn
dm2000minValueModuleTemp = _Dm2000minValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 87),
    _Dm2000minValueModuleTemp_Type()
)
dm2000minValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueModuleTemp.setStatus("mandatory")
_Dm2000maxValueModuleTemp_Type = Float
_Dm2000maxValueModuleTemp_Object = MibTableColumn
dm2000maxValueModuleTemp = _Dm2000maxValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 88),
    _Dm2000maxValueModuleTemp_Type()
)
dm2000maxValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueModuleTemp.setStatus("mandatory")


class _Dm2000alarmStateModuleTemp_Type(Integer32):
    """Custom type dm2000alarmStateModuleTemp based on Integer32"""
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


_Dm2000alarmStateModuleTemp_Type.__name__ = "Integer32"
_Dm2000alarmStateModuleTemp_Object = MibTableColumn
dm2000alarmStateModuleTemp = _Dm2000alarmStateModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 89),
    _Dm2000alarmStateModuleTemp_Type()
)
dm2000alarmStateModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateModuleTemp.setStatus("mandatory")


class _Dm2000labelFanCurrent_Type(DisplayString):
    """Custom type dm2000labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelFanCurrent_Type.__name__ = "DisplayString"
_Dm2000labelFanCurrent_Object = MibTableColumn
dm2000labelFanCurrent = _Dm2000labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 90),
    _Dm2000labelFanCurrent_Type()
)
dm2000labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelFanCurrent.setStatus("optional")


class _Dm2000uomFanCurrent_Type(DisplayString):
    """Custom type dm2000uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uomFanCurrent_Type.__name__ = "DisplayString"
_Dm2000uomFanCurrent_Object = MibTableColumn
dm2000uomFanCurrent = _Dm2000uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 91),
    _Dm2000uomFanCurrent_Type()
)
dm2000uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uomFanCurrent.setStatus("optional")
_Dm2000majorHighFanCurrent_Type = Float
_Dm2000majorHighFanCurrent_Object = MibTableColumn
dm2000majorHighFanCurrent = _Dm2000majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 92),
    _Dm2000majorHighFanCurrent_Type()
)
dm2000majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHighFanCurrent.setStatus("mandatory")
_Dm2000majorLowFanCurrent_Type = Float
_Dm2000majorLowFanCurrent_Object = MibTableColumn
dm2000majorLowFanCurrent = _Dm2000majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 93),
    _Dm2000majorLowFanCurrent_Type()
)
dm2000majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLowFanCurrent.setStatus("mandatory")
_Dm2000minorHighFanCurrent_Type = Float
_Dm2000minorHighFanCurrent_Object = MibTableColumn
dm2000minorHighFanCurrent = _Dm2000minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 94),
    _Dm2000minorHighFanCurrent_Type()
)
dm2000minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHighFanCurrent.setStatus("mandatory")
_Dm2000minorLowFanCurrent_Type = Float
_Dm2000minorLowFanCurrent_Object = MibTableColumn
dm2000minorLowFanCurrent = _Dm2000minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 95),
    _Dm2000minorLowFanCurrent_Type()
)
dm2000minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLowFanCurrent.setStatus("mandatory")
_Dm2000currentValueFanCurrent_Type = Float
_Dm2000currentValueFanCurrent_Object = MibTableColumn
dm2000currentValueFanCurrent = _Dm2000currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 96),
    _Dm2000currentValueFanCurrent_Type()
)
dm2000currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValueFanCurrent.setStatus("mandatory")


class _Dm2000stateFlagFanCurrent_Type(Integer32):
    """Custom type dm2000stateFlagFanCurrent based on Integer32"""
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


_Dm2000stateFlagFanCurrent_Type.__name__ = "Integer32"
_Dm2000stateFlagFanCurrent_Object = MibTableColumn
dm2000stateFlagFanCurrent = _Dm2000stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 97),
    _Dm2000stateFlagFanCurrent_Type()
)
dm2000stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlagFanCurrent.setStatus("mandatory")
_Dm2000minValueFanCurrent_Type = Float
_Dm2000minValueFanCurrent_Object = MibTableColumn
dm2000minValueFanCurrent = _Dm2000minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 98),
    _Dm2000minValueFanCurrent_Type()
)
dm2000minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValueFanCurrent.setStatus("mandatory")
_Dm2000maxValueFanCurrent_Type = Float
_Dm2000maxValueFanCurrent_Object = MibTableColumn
dm2000maxValueFanCurrent = _Dm2000maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 99),
    _Dm2000maxValueFanCurrent_Type()
)
dm2000maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValueFanCurrent.setStatus("mandatory")


class _Dm2000alarmStateFanCurrent_Type(Integer32):
    """Custom type dm2000alarmStateFanCurrent based on Integer32"""
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


_Dm2000alarmStateFanCurrent_Type.__name__ = "Integer32"
_Dm2000alarmStateFanCurrent_Object = MibTableColumn
dm2000alarmStateFanCurrent = _Dm2000alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 100),
    _Dm2000alarmStateFanCurrent_Type()
)
dm2000alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmStateFanCurrent.setStatus("mandatory")


class _Dm2000label12Volt_Type(DisplayString):
    """Custom type dm2000label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000label12Volt_Type.__name__ = "DisplayString"
_Dm2000label12Volt_Object = MibTableColumn
dm2000label12Volt = _Dm2000label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 101),
    _Dm2000label12Volt_Type()
)
dm2000label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000label12Volt.setStatus("optional")


class _Dm2000uom12Volt_Type(DisplayString):
    """Custom type dm2000uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000uom12Volt_Type.__name__ = "DisplayString"
_Dm2000uom12Volt_Object = MibTableColumn
dm2000uom12Volt = _Dm2000uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 102),
    _Dm2000uom12Volt_Type()
)
dm2000uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000uom12Volt.setStatus("optional")
_Dm2000majorHigh12Volt_Type = Float
_Dm2000majorHigh12Volt_Object = MibTableColumn
dm2000majorHigh12Volt = _Dm2000majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 103),
    _Dm2000majorHigh12Volt_Type()
)
dm2000majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorHigh12Volt.setStatus("mandatory")
_Dm2000majorLow12Volt_Type = Float
_Dm2000majorLow12Volt_Object = MibTableColumn
dm2000majorLow12Volt = _Dm2000majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 104),
    _Dm2000majorLow12Volt_Type()
)
dm2000majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000majorLow12Volt.setStatus("mandatory")
_Dm2000minorHigh12Volt_Type = Float
_Dm2000minorHigh12Volt_Object = MibTableColumn
dm2000minorHigh12Volt = _Dm2000minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 105),
    _Dm2000minorHigh12Volt_Type()
)
dm2000minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorHigh12Volt.setStatus("mandatory")
_Dm2000minorLow12Volt_Type = Float
_Dm2000minorLow12Volt_Object = MibTableColumn
dm2000minorLow12Volt = _Dm2000minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 106),
    _Dm2000minorLow12Volt_Type()
)
dm2000minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minorLow12Volt.setStatus("mandatory")
_Dm2000currentValue12Volt_Type = Float
_Dm2000currentValue12Volt_Object = MibTableColumn
dm2000currentValue12Volt = _Dm2000currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 107),
    _Dm2000currentValue12Volt_Type()
)
dm2000currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000currentValue12Volt.setStatus("mandatory")


class _Dm2000stateFlag12Volt_Type(Integer32):
    """Custom type dm2000stateFlag12Volt based on Integer32"""
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


_Dm2000stateFlag12Volt_Type.__name__ = "Integer32"
_Dm2000stateFlag12Volt_Object = MibTableColumn
dm2000stateFlag12Volt = _Dm2000stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 108),
    _Dm2000stateFlag12Volt_Type()
)
dm2000stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateFlag12Volt.setStatus("mandatory")
_Dm2000minValue12Volt_Type = Float
_Dm2000minValue12Volt_Object = MibTableColumn
dm2000minValue12Volt = _Dm2000minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 109),
    _Dm2000minValue12Volt_Type()
)
dm2000minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000minValue12Volt.setStatus("mandatory")
_Dm2000maxValue12Volt_Type = Float
_Dm2000maxValue12Volt_Object = MibTableColumn
dm2000maxValue12Volt = _Dm2000maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 110),
    _Dm2000maxValue12Volt_Type()
)
dm2000maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000maxValue12Volt.setStatus("mandatory")


class _Dm2000alarmState12Volt_Type(Integer32):
    """Custom type dm2000alarmState12Volt based on Integer32"""
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


_Dm2000alarmState12Volt_Type.__name__ = "Integer32"
_Dm2000alarmState12Volt_Object = MibTableColumn
dm2000alarmState12Volt = _Dm2000alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 2, 1, 111),
    _Dm2000alarmState12Volt_Type()
)
dm2000alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000alarmState12Volt.setStatus("mandatory")
_Gx2dm2000DigitalTable_Object = MibTable
gx2dm2000DigitalTable = _Gx2dm2000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3)
)
if mibBuilder.loadTexts:
    gx2dm2000DigitalTable.setStatus("mandatory")
_Gx2dm2000DigitalEntry_Object = MibTableRow
gx2dm2000DigitalEntry = _Gx2dm2000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2)
)
gx2dm2000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2DM2000-MIB", "gx2dm2000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dm2000DigitalEntry.setStatus("mandatory")


class _Gx2dm2000DigitalTableIndex_Type(Integer32):
    """Custom type gx2dm2000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2dm2000DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2dm2000DigitalTableIndex_Object = MibTableColumn
gx2dm2000DigitalTableIndex = _Gx2dm2000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 1),
    _Gx2dm2000DigitalTableIndex_Type()
)
gx2dm2000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dm2000DigitalTableIndex.setStatus("mandatory")


class _Dm2000labelRfInput_Type(DisplayString):
    """Custom type dm2000labelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelRfInput_Type.__name__ = "DisplayString"
_Dm2000labelRfInput_Object = MibTableColumn
dm2000labelRfInput = _Dm2000labelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 2),
    _Dm2000labelRfInput_Type()
)
dm2000labelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelRfInput.setStatus("optional")


class _Dm2000enumRfInput_Type(DisplayString):
    """Custom type dm2000enumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumRfInput_Type.__name__ = "DisplayString"
_Dm2000enumRfInput_Object = MibTableColumn
dm2000enumRfInput = _Dm2000enumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 3),
    _Dm2000enumRfInput_Type()
)
dm2000enumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumRfInput.setStatus("optional")


class _Dm2000valueRfInput_Type(Integer32):
    """Custom type dm2000valueRfInput based on Integer32"""
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


_Dm2000valueRfInput_Type.__name__ = "Integer32"
_Dm2000valueRfInput_Object = MibTableColumn
dm2000valueRfInput = _Dm2000valueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 4),
    _Dm2000valueRfInput_Type()
)
dm2000valueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueRfInput.setStatus("mandatory")


class _Dm2000stateflagRfInput_Type(Integer32):
    """Custom type dm2000stateflagRfInput based on Integer32"""
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


_Dm2000stateflagRfInput_Type.__name__ = "Integer32"
_Dm2000stateflagRfInput_Object = MibTableColumn
dm2000stateflagRfInput = _Dm2000stateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 5),
    _Dm2000stateflagRfInput_Type()
)
dm2000stateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagRfInput.setStatus("mandatory")


class _Dm2000labelOptOutput_Type(DisplayString):
    """Custom type dm2000labelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelOptOutput_Type.__name__ = "DisplayString"
_Dm2000labelOptOutput_Object = MibTableColumn
dm2000labelOptOutput = _Dm2000labelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 6),
    _Dm2000labelOptOutput_Type()
)
dm2000labelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelOptOutput.setStatus("optional")


class _Dm2000enumOptOutput_Type(DisplayString):
    """Custom type dm2000enumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumOptOutput_Type.__name__ = "DisplayString"
_Dm2000enumOptOutput_Object = MibTableColumn
dm2000enumOptOutput = _Dm2000enumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 7),
    _Dm2000enumOptOutput_Type()
)
dm2000enumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumOptOutput.setStatus("optional")


class _Dm2000valueOptOutput_Type(Integer32):
    """Custom type dm2000valueOptOutput based on Integer32"""
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


_Dm2000valueOptOutput_Type.__name__ = "Integer32"
_Dm2000valueOptOutput_Object = MibTableColumn
dm2000valueOptOutput = _Dm2000valueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 8),
    _Dm2000valueOptOutput_Type()
)
dm2000valueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueOptOutput.setStatus("mandatory")


class _Dm2000stateflagOptOutput_Type(Integer32):
    """Custom type dm2000stateflagOptOutput based on Integer32"""
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


_Dm2000stateflagOptOutput_Type.__name__ = "Integer32"
_Dm2000stateflagOptOutput_Object = MibTableColumn
dm2000stateflagOptOutput = _Dm2000stateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 9),
    _Dm2000stateflagOptOutput_Type()
)
dm2000stateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagOptOutput.setStatus("mandatory")


class _Dm2000labelLaserMode_Type(DisplayString):
    """Custom type dm2000labelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelLaserMode_Type.__name__ = "DisplayString"
_Dm2000labelLaserMode_Object = MibTableColumn
dm2000labelLaserMode = _Dm2000labelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 10),
    _Dm2000labelLaserMode_Type()
)
dm2000labelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelLaserMode.setStatus("optional")


class _Dm2000enumLaserMode_Type(DisplayString):
    """Custom type dm2000enumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumLaserMode_Type.__name__ = "DisplayString"
_Dm2000enumLaserMode_Object = MibTableColumn
dm2000enumLaserMode = _Dm2000enumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 11),
    _Dm2000enumLaserMode_Type()
)
dm2000enumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumLaserMode.setStatus("optional")


class _Dm2000valueLaserMode_Type(Integer32):
    """Custom type dm2000valueLaserMode based on Integer32"""
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


_Dm2000valueLaserMode_Type.__name__ = "Integer32"
_Dm2000valueLaserMode_Object = MibTableColumn
dm2000valueLaserMode = _Dm2000valueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 12),
    _Dm2000valueLaserMode_Type()
)
dm2000valueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueLaserMode.setStatus("mandatory")


class _Dm2000stateflagLaserMode_Type(Integer32):
    """Custom type dm2000stateflagLaserMode based on Integer32"""
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


_Dm2000stateflagLaserMode_Type.__name__ = "Integer32"
_Dm2000stateflagLaserMode_Object = MibTableColumn
dm2000stateflagLaserMode = _Dm2000stateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 13),
    _Dm2000stateflagLaserMode_Type()
)
dm2000stateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagLaserMode.setStatus("mandatory")


class _Dm2000labelLaserSecMode_Type(DisplayString):
    """Custom type dm2000labelLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelLaserSecMode_Type.__name__ = "DisplayString"
_Dm2000labelLaserSecMode_Object = MibTableColumn
dm2000labelLaserSecMode = _Dm2000labelLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 14),
    _Dm2000labelLaserSecMode_Type()
)
dm2000labelLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelLaserSecMode.setStatus("optional")


class _Dm2000enumLaserSecMode_Type(DisplayString):
    """Custom type dm2000enumLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumLaserSecMode_Type.__name__ = "DisplayString"
_Dm2000enumLaserSecMode_Object = MibTableColumn
dm2000enumLaserSecMode = _Dm2000enumLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 15),
    _Dm2000enumLaserSecMode_Type()
)
dm2000enumLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumLaserSecMode.setStatus("optional")


class _Dm2000valueLaserSecMode_Type(Integer32):
    """Custom type dm2000valueLaserSecMode based on Integer32"""
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


_Dm2000valueLaserSecMode_Type.__name__ = "Integer32"
_Dm2000valueLaserSecMode_Object = MibTableColumn
dm2000valueLaserSecMode = _Dm2000valueLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 16),
    _Dm2000valueLaserSecMode_Type()
)
dm2000valueLaserSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueLaserSecMode.setStatus("mandatory")


class _Dm2000stateflagLaserSecMode_Type(Integer32):
    """Custom type dm2000stateflagLaserSecMode based on Integer32"""
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


_Dm2000stateflagLaserSecMode_Type.__name__ = "Integer32"
_Dm2000stateflagLaserSecMode_Object = MibTableColumn
dm2000stateflagLaserSecMode = _Dm2000stateflagLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 17),
    _Dm2000stateflagLaserSecMode_Type()
)
dm2000stateflagLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagLaserSecMode.setStatus("mandatory")


class _Dm2000labelVideoOffset_Type(DisplayString):
    """Custom type dm2000labelVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelVideoOffset_Type.__name__ = "DisplayString"
_Dm2000labelVideoOffset_Object = MibTableColumn
dm2000labelVideoOffset = _Dm2000labelVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 18),
    _Dm2000labelVideoOffset_Type()
)
dm2000labelVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelVideoOffset.setStatus("optional")


class _Dm2000enumVideoOffset_Type(DisplayString):
    """Custom type dm2000enumVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumVideoOffset_Type.__name__ = "DisplayString"
_Dm2000enumVideoOffset_Object = MibTableColumn
dm2000enumVideoOffset = _Dm2000enumVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 19),
    _Dm2000enumVideoOffset_Type()
)
dm2000enumVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumVideoOffset.setStatus("optional")


class _Dm2000valueVideoOffset_Type(Integer32):
    """Custom type dm2000valueVideoOffset based on Integer32"""
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


_Dm2000valueVideoOffset_Type.__name__ = "Integer32"
_Dm2000valueVideoOffset_Object = MibTableColumn
dm2000valueVideoOffset = _Dm2000valueVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 20),
    _Dm2000valueVideoOffset_Type()
)
dm2000valueVideoOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueVideoOffset.setStatus("mandatory")


class _Dm2000stateflagVideoOffset_Type(Integer32):
    """Custom type dm2000stateflagVideoOffset based on Integer32"""
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


_Dm2000stateflagVideoOffset_Type.__name__ = "Integer32"
_Dm2000stateflagVideoOffset_Object = MibTableColumn
dm2000stateflagVideoOffset = _Dm2000stateflagVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 21),
    _Dm2000stateflagVideoOffset_Type()
)
dm2000stateflagVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagVideoOffset.setStatus("mandatory")


class _Dm2000labelFactoryDefault_Type(DisplayString):
    """Custom type dm2000labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelFactoryDefault_Type.__name__ = "DisplayString"
_Dm2000labelFactoryDefault_Object = MibTableColumn
dm2000labelFactoryDefault = _Dm2000labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 22),
    _Dm2000labelFactoryDefault_Type()
)
dm2000labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelFactoryDefault.setStatus("optional")


class _Dm2000enumFactoryDefault_Type(DisplayString):
    """Custom type dm2000enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumFactoryDefault_Type.__name__ = "DisplayString"
_Dm2000enumFactoryDefault_Object = MibTableColumn
dm2000enumFactoryDefault = _Dm2000enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 23),
    _Dm2000enumFactoryDefault_Type()
)
dm2000enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumFactoryDefault.setStatus("optional")


class _Dm2000valueFactoryDefault_Type(Integer32):
    """Custom type dm2000valueFactoryDefault based on Integer32"""
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


_Dm2000valueFactoryDefault_Type.__name__ = "Integer32"
_Dm2000valueFactoryDefault_Object = MibTableColumn
dm2000valueFactoryDefault = _Dm2000valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 24),
    _Dm2000valueFactoryDefault_Type()
)
dm2000valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueFactoryDefault.setStatus("mandatory")


class _Dm2000stateflagFactoryDefault_Type(Integer32):
    """Custom type dm2000stateflagFactoryDefault based on Integer32"""
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


_Dm2000stateflagFactoryDefault_Type.__name__ = "Integer32"
_Dm2000stateflagFactoryDefault_Object = MibTableColumn
dm2000stateflagFactoryDefault = _Dm2000stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 25),
    _Dm2000stateflagFactoryDefault_Type()
)
dm2000stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagFactoryDefault.setStatus("mandatory")


class _Dm2000labelFiberLength_Type(DisplayString):
    """Custom type dm2000labelFiberLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelFiberLength_Type.__name__ = "DisplayString"
_Dm2000labelFiberLength_Object = MibTableColumn
dm2000labelFiberLength = _Dm2000labelFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 26),
    _Dm2000labelFiberLength_Type()
)
dm2000labelFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelFiberLength.setStatus("optional")


class _Dm2000enumFiberLength_Type(DisplayString):
    """Custom type dm2000enumFiberLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumFiberLength_Type.__name__ = "DisplayString"
_Dm2000enumFiberLength_Object = MibTableColumn
dm2000enumFiberLength = _Dm2000enumFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 27),
    _Dm2000enumFiberLength_Type()
)
dm2000enumFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumFiberLength.setStatus("optional")
_Dm2000valueFiberLength_Type = Integer32
_Dm2000valueFiberLength_Object = MibTableColumn
dm2000valueFiberLength = _Dm2000valueFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 28),
    _Dm2000valueFiberLength_Type()
)
dm2000valueFiberLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueFiberLength.setStatus("mandatory")


class _Dm2000stateflagFiberLength_Type(Integer32):
    """Custom type dm2000stateflagFiberLength based on Integer32"""
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


_Dm2000stateflagFiberLength_Type.__name__ = "Integer32"
_Dm2000stateflagFiberLength_Object = MibTableColumn
dm2000stateflagFiberLength = _Dm2000stateflagFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 29),
    _Dm2000stateflagFiberLength_Type()
)
dm2000stateflagFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagFiberLength.setStatus("mandatory")


class _Dm2000labelWavelengthOffset_Type(DisplayString):
    """Custom type dm2000labelWavelengthOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelWavelengthOffset_Type.__name__ = "DisplayString"
_Dm2000labelWavelengthOffset_Object = MibTableColumn
dm2000labelWavelengthOffset = _Dm2000labelWavelengthOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 30),
    _Dm2000labelWavelengthOffset_Type()
)
dm2000labelWavelengthOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelWavelengthOffset.setStatus("optional")


class _Dm2000enumWavelengthOffset_Type(DisplayString):
    """Custom type dm2000enumWavelengthOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000enumWavelengthOffset_Type.__name__ = "DisplayString"
_Dm2000enumWavelengthOffset_Object = MibTableColumn
dm2000enumWavelengthOffset = _Dm2000enumWavelengthOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 31),
    _Dm2000enumWavelengthOffset_Type()
)
dm2000enumWavelengthOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000enumWavelengthOffset.setStatus("optional")


class _Dm2000valueWavelengthOffset_Type(Integer32):
    """Custom type dm2000valueWavelengthOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("FullSpectrum", 2),
          ("narrowcast", 1))
    )


_Dm2000valueWavelengthOffset_Type.__name__ = "Integer32"
_Dm2000valueWavelengthOffset_Object = MibTableColumn
dm2000valueWavelengthOffset = _Dm2000valueWavelengthOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 32),
    _Dm2000valueWavelengthOffset_Type()
)
dm2000valueWavelengthOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dm2000valueWavelengthOffset.setStatus("mandatory")


class _Dm2000stateflagWavelengthOffset_Type(Integer32):
    """Custom type dm2000stateflagWavelengthOffset based on Integer32"""
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


_Dm2000stateflagWavelengthOffset_Type.__name__ = "Integer32"
_Dm2000stateflagWavelengthOffset_Object = MibTableColumn
dm2000stateflagWavelengthOffset = _Dm2000stateflagWavelengthOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 3, 2, 33),
    _Dm2000stateflagWavelengthOffset_Type()
)
dm2000stateflagWavelengthOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagWavelengthOffset.setStatus("mandatory")
_Gx2dm2000StatusTable_Object = MibTable
gx2dm2000StatusTable = _Gx2dm2000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4)
)
if mibBuilder.loadTexts:
    gx2dm2000StatusTable.setStatus("mandatory")
_Gx2dm2000StatusEntry_Object = MibTableRow
gx2dm2000StatusEntry = _Gx2dm2000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3)
)
gx2dm2000StatusEntry.setIndexNames(
    (0, "OMNI-gx2DM2000-MIB", "gx2dm2000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dm2000StatusEntry.setStatus("mandatory")


class _Gx2dm2000StatusTableIndex_Type(Integer32):
    """Custom type gx2dm2000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2dm2000StatusTableIndex_Type.__name__ = "Integer32"
_Gx2dm2000StatusTableIndex_Object = MibTableColumn
gx2dm2000StatusTableIndex = _Gx2dm2000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 1),
    _Gx2dm2000StatusTableIndex_Type()
)
gx2dm2000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dm2000StatusTableIndex.setStatus("mandatory")


class _Dm2000labelBoot_Type(DisplayString):
    """Custom type dm2000labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelBoot_Type.__name__ = "DisplayString"
_Dm2000labelBoot_Object = MibTableColumn
dm2000labelBoot = _Dm2000labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 2),
    _Dm2000labelBoot_Type()
)
dm2000labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelBoot.setStatus("optional")


class _Dm2000valueBoot_Type(Integer32):
    """Custom type dm2000valueBoot based on Integer32"""
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


_Dm2000valueBoot_Type.__name__ = "Integer32"
_Dm2000valueBoot_Object = MibTableColumn
dm2000valueBoot = _Dm2000valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 3),
    _Dm2000valueBoot_Type()
)
dm2000valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueBoot.setStatus("mandatory")


class _Dm2000stateflagBoot_Type(Integer32):
    """Custom type dm2000stateflagBoot based on Integer32"""
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


_Dm2000stateflagBoot_Type.__name__ = "Integer32"
_Dm2000stateflagBoot_Object = MibTableColumn
dm2000stateflagBoot = _Dm2000stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 4),
    _Dm2000stateflagBoot_Type()
)
dm2000stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagBoot.setStatus("mandatory")


class _Dm2000labelFlash_Type(DisplayString):
    """Custom type dm2000labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelFlash_Type.__name__ = "DisplayString"
_Dm2000labelFlash_Object = MibTableColumn
dm2000labelFlash = _Dm2000labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 5),
    _Dm2000labelFlash_Type()
)
dm2000labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelFlash.setStatus("optional")


class _Dm2000valueFlash_Type(Integer32):
    """Custom type dm2000valueFlash based on Integer32"""
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


_Dm2000valueFlash_Type.__name__ = "Integer32"
_Dm2000valueFlash_Object = MibTableColumn
dm2000valueFlash = _Dm2000valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 6),
    _Dm2000valueFlash_Type()
)
dm2000valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueFlash.setStatus("mandatory")


class _Dm2000stateflagFlash_Type(Integer32):
    """Custom type dm2000stateflagFlash based on Integer32"""
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


_Dm2000stateflagFlash_Type.__name__ = "Integer32"
_Dm2000stateflagFlash_Object = MibTableColumn
dm2000stateflagFlash = _Dm2000stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 7),
    _Dm2000stateflagFlash_Type()
)
dm2000stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagFlash.setStatus("mandatory")


class _Dm2000labelFactoryDataCRC_Type(DisplayString):
    """Custom type dm2000labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Dm2000labelFactoryDataCRC_Object = MibTableColumn
dm2000labelFactoryDataCRC = _Dm2000labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 8),
    _Dm2000labelFactoryDataCRC_Type()
)
dm2000labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelFactoryDataCRC.setStatus("optional")


class _Dm2000valueFactoryDataCRC_Type(Integer32):
    """Custom type dm2000valueFactoryDataCRC based on Integer32"""
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


_Dm2000valueFactoryDataCRC_Type.__name__ = "Integer32"
_Dm2000valueFactoryDataCRC_Object = MibTableColumn
dm2000valueFactoryDataCRC = _Dm2000valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 9),
    _Dm2000valueFactoryDataCRC_Type()
)
dm2000valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueFactoryDataCRC.setStatus("mandatory")


class _Dm2000stateflagFactoryDataCRC_Type(Integer32):
    """Custom type dm2000stateflagFactoryDataCRC based on Integer32"""
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


_Dm2000stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Dm2000stateflagFactoryDataCRC_Object = MibTableColumn
dm2000stateflagFactoryDataCRC = _Dm2000stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 10),
    _Dm2000stateflagFactoryDataCRC_Type()
)
dm2000stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagFactoryDataCRC.setStatus("mandatory")


class _Dm2000labelLaserDataCRC_Type(DisplayString):
    """Custom type dm2000labelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelLaserDataCRC_Type.__name__ = "DisplayString"
_Dm2000labelLaserDataCRC_Object = MibTableColumn
dm2000labelLaserDataCRC = _Dm2000labelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 11),
    _Dm2000labelLaserDataCRC_Type()
)
dm2000labelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelLaserDataCRC.setStatus("optional")


class _Dm2000valueLaserDataCRC_Type(Integer32):
    """Custom type dm2000valueLaserDataCRC based on Integer32"""
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


_Dm2000valueLaserDataCRC_Type.__name__ = "Integer32"
_Dm2000valueLaserDataCRC_Object = MibTableColumn
dm2000valueLaserDataCRC = _Dm2000valueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 12),
    _Dm2000valueLaserDataCRC_Type()
)
dm2000valueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueLaserDataCRC.setStatus("mandatory")


class _Dm2000stateflagLaserDataCRC_Type(Integer32):
    """Custom type dm2000stateflagLaserDataCRC based on Integer32"""
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


_Dm2000stateflagLaserDataCRC_Type.__name__ = "Integer32"
_Dm2000stateflagLaserDataCRC_Object = MibTableColumn
dm2000stateflagLaserDataCRC = _Dm2000stateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 13),
    _Dm2000stateflagLaserDataCRC_Type()
)
dm2000stateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagLaserDataCRC.setStatus("mandatory")


class _Dm2000labelAlarmDataCrc_Type(DisplayString):
    """Custom type dm2000labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Dm2000labelAlarmDataCrc_Object = MibTableColumn
dm2000labelAlarmDataCrc = _Dm2000labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 14),
    _Dm2000labelAlarmDataCrc_Type()
)
dm2000labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelAlarmDataCrc.setStatus("optional")


class _Dm2000valueAlarmDataCrc_Type(Integer32):
    """Custom type dm2000valueAlarmDataCrc based on Integer32"""
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


_Dm2000valueAlarmDataCrc_Type.__name__ = "Integer32"
_Dm2000valueAlarmDataCrc_Object = MibTableColumn
dm2000valueAlarmDataCrc = _Dm2000valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 15),
    _Dm2000valueAlarmDataCrc_Type()
)
dm2000valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueAlarmDataCrc.setStatus("mandatory")


class _Dm2000stateflagAlarmDataCrc_Type(Integer32):
    """Custom type dm2000stateflagAlarmDataCrc based on Integer32"""
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


_Dm2000stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Dm2000stateflagAlarmDataCrc_Object = MibTableColumn
dm2000stateflagAlarmDataCrc = _Dm2000stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 16),
    _Dm2000stateflagAlarmDataCrc_Type()
)
dm2000stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagAlarmDataCrc.setStatus("mandatory")


class _Dm2000labelHWStatus_Type(DisplayString):
    """Custom type dm2000labelHWStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelHWStatus_Type.__name__ = "DisplayString"
_Dm2000labelHWStatus_Object = MibTableColumn
dm2000labelHWStatus = _Dm2000labelHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 17),
    _Dm2000labelHWStatus_Type()
)
dm2000labelHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelHWStatus.setStatus("optional")


class _Dm2000valueHWStatus_Type(Integer32):
    """Custom type dm2000valueHWStatus based on Integer32"""
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


_Dm2000valueHWStatus_Type.__name__ = "Integer32"
_Dm2000valueHWStatus_Object = MibTableColumn
dm2000valueHWStatus = _Dm2000valueHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 18),
    _Dm2000valueHWStatus_Type()
)
dm2000valueHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueHWStatus.setStatus("mandatory")


class _Dm2000stateflagHWStatus_Type(Integer32):
    """Custom type dm2000stateflagHWStatus based on Integer32"""
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


_Dm2000stateflagHWStatus_Type.__name__ = "Integer32"
_Dm2000stateflagHWStatus_Object = MibTableColumn
dm2000stateflagHWStatus = _Dm2000stateflagHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 19),
    _Dm2000stateflagHWStatus_Type()
)
dm2000stateflagHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagHWStatus.setStatus("mandatory")


class _Dm2000labelRFInputStatus_Type(DisplayString):
    """Custom type dm2000labelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000labelRFInputStatus_Type.__name__ = "DisplayString"
_Dm2000labelRFInputStatus_Object = MibTableColumn
dm2000labelRFInputStatus = _Dm2000labelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 20),
    _Dm2000labelRFInputStatus_Type()
)
dm2000labelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000labelRFInputStatus.setStatus("optional")


class _Dm2000valueRFInputStatus_Type(Integer32):
    """Custom type dm2000valueRFInputStatus based on Integer32"""
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


_Dm2000valueRFInputStatus_Type.__name__ = "Integer32"
_Dm2000valueRFInputStatus_Object = MibTableColumn
dm2000valueRFInputStatus = _Dm2000valueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 21),
    _Dm2000valueRFInputStatus_Type()
)
dm2000valueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000valueRFInputStatus.setStatus("mandatory")


class _Dm2000stateflagRFInputStatus_Type(Integer32):
    """Custom type dm2000stateflagRFInputStatus based on Integer32"""
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


_Dm2000stateflagRFInputStatus_Type.__name__ = "Integer32"
_Dm2000stateflagRFInputStatus_Object = MibTableColumn
dm2000stateflagRFInputStatus = _Dm2000stateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 4, 3, 22),
    _Dm2000stateflagRFInputStatus_Type()
)
dm2000stateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000stateflagRFInputStatus.setStatus("mandatory")
_Gx2dm2000FactoryTable_Object = MibTable
gx2dm2000FactoryTable = _Gx2dm2000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5)
)
if mibBuilder.loadTexts:
    gx2dm2000FactoryTable.setStatus("mandatory")
_Gx2dm2000FactoryEntry_Object = MibTableRow
gx2dm2000FactoryEntry = _Gx2dm2000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4)
)
gx2dm2000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2DM2000-MIB", "gx2dm2000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dm2000FactoryEntry.setStatus("mandatory")


class _Gx2dm2000FactoryTableIndex_Type(Integer32):
    """Custom type gx2dm2000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2dm2000FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2dm2000FactoryTableIndex_Object = MibTableColumn
gx2dm2000FactoryTableIndex = _Gx2dm2000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 1),
    _Gx2dm2000FactoryTableIndex_Type()
)
gx2dm2000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dm2000FactoryTableIndex.setStatus("mandatory")
_Dm2000bootControlByteValue_Type = Integer32
_Dm2000bootControlByteValue_Object = MibTableColumn
dm2000bootControlByteValue = _Dm2000bootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 2),
    _Dm2000bootControlByteValue_Type()
)
dm2000bootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000bootControlByteValue.setStatus("mandatory")
_Dm2000bootStatusByteValue_Type = Integer32
_Dm2000bootStatusByteValue_Object = MibTableColumn
dm2000bootStatusByteValue = _Dm2000bootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 3),
    _Dm2000bootStatusByteValue_Type()
)
dm2000bootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000bootStatusByteValue.setStatus("mandatory")
_Dm2000bank1CRCValue_Type = Integer32
_Dm2000bank1CRCValue_Object = MibTableColumn
dm2000bank1CRCValue = _Dm2000bank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 4),
    _Dm2000bank1CRCValue_Type()
)
dm2000bank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000bank1CRCValue.setStatus("mandatory")
_Dm2000bank2CRCValue_Type = Integer32
_Dm2000bank2CRCValue_Object = MibTableColumn
dm2000bank2CRCValue = _Dm2000bank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 5),
    _Dm2000bank2CRCValue_Type()
)
dm2000bank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000bank2CRCValue.setStatus("mandatory")
_Dm2000prgEEPROMByteValue_Type = Integer32
_Dm2000prgEEPROMByteValue_Object = MibTableColumn
dm2000prgEEPROMByteValue = _Dm2000prgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 6),
    _Dm2000prgEEPROMByteValue_Type()
)
dm2000prgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000prgEEPROMByteValue.setStatus("mandatory")
_Dm2000factoryCRCValue_Type = Integer32
_Dm2000factoryCRCValue_Object = MibTableColumn
dm2000factoryCRCValue = _Dm2000factoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 7),
    _Dm2000factoryCRCValue_Type()
)
dm2000factoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000factoryCRCValue.setStatus("mandatory")


class _Dm2000calculateCRCValue_Type(Integer32):
    """Custom type dm2000calculateCRCValue based on Integer32"""
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


_Dm2000calculateCRCValue_Type.__name__ = "Integer32"
_Dm2000calculateCRCValue_Object = MibTableColumn
dm2000calculateCRCValue = _Dm2000calculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 8),
    _Dm2000calculateCRCValue_Type()
)
dm2000calculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000calculateCRCValue.setStatus("mandatory")
_Dm2000hourMeterValue_Type = Integer32
_Dm2000hourMeterValue_Object = MibTableColumn
dm2000hourMeterValue = _Dm2000hourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 9),
    _Dm2000hourMeterValue_Type()
)
dm2000hourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000hourMeterValue.setStatus("mandatory")
_Dm2000flashPrgCntAValue_Type = Integer32
_Dm2000flashPrgCntAValue_Object = MibTableColumn
dm2000flashPrgCntAValue = _Dm2000flashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 10),
    _Dm2000flashPrgCntAValue_Type()
)
dm2000flashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000flashPrgCntAValue.setStatus("mandatory")
_Dm2000flashPrgCntBValue_Type = Integer32
_Dm2000flashPrgCntBValue_Object = MibTableColumn
dm2000flashPrgCntBValue = _Dm2000flashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 11),
    _Dm2000flashPrgCntBValue_Type()
)
dm2000flashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000flashPrgCntBValue.setStatus("mandatory")


class _Dm2000flashBankARevValue_Type(DisplayString):
    """Custom type dm2000flashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000flashBankARevValue_Type.__name__ = "DisplayString"
_Dm2000flashBankARevValue_Object = MibTableColumn
dm2000flashBankARevValue = _Dm2000flashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 12),
    _Dm2000flashBankARevValue_Type()
)
dm2000flashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000flashBankARevValue.setStatus("mandatory")


class _Dm2000flashBankBRevValue_Type(DisplayString):
    """Custom type dm2000flashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dm2000flashBankBRevValue_Type.__name__ = "DisplayString"
_Dm2000flashBankBRevValue_Object = MibTableColumn
dm2000flashBankBRevValue = _Dm2000flashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 5, 4, 13),
    _Dm2000flashBankBRevValue_Type()
)
dm2000flashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dm2000flashBankBRevValue.setStatus("mandatory")
_Gx2Dm2000HoldTimeTable_Object = MibTable
gx2Dm2000HoldTimeTable = _Gx2Dm2000HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 6)
)
if mibBuilder.loadTexts:
    gx2Dm2000HoldTimeTable.setStatus("mandatory")
_Gx2Dm2000HoldTimeEntry_Object = MibTableRow
gx2Dm2000HoldTimeEntry = _Gx2Dm2000HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 6, 5)
)
gx2Dm2000HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2DM2000-MIB", "gx2Dm2000HoldTimeTableIndex"),
    (0, "OMNI-gx2DM2000-MIB", "gx2Dm2000HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Dm2000HoldTimeEntry.setStatus("mandatory")


class _Gx2Dm2000HoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Dm2000HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm2000HoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Dm2000HoldTimeTableIndex_Object = MibTableColumn
gx2Dm2000HoldTimeTableIndex = _Gx2Dm2000HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 6, 5, 1),
    _Gx2Dm2000HoldTimeTableIndex_Type()
)
gx2Dm2000HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm2000HoldTimeTableIndex.setStatus("mandatory")


class _Gx2Dm2000HoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Dm2000HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Dm2000HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Dm2000HoldTimeSpecIndex_Object = MibTableColumn
gx2Dm2000HoldTimeSpecIndex = _Gx2Dm2000HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 6, 5, 2),
    _Gx2Dm2000HoldTimeSpecIndex_Type()
)
gx2Dm2000HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Dm2000HoldTimeSpecIndex.setStatus("mandatory")
_Gx2Dm2000HoldTimeData_Type = Integer32
_Gx2Dm2000HoldTimeData_Object = MibTableColumn
gx2Dm2000HoldTimeData = _Gx2Dm2000HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 6, 5, 3),
    _Gx2Dm2000HoldTimeData_Type()
)
gx2Dm2000HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Dm2000HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDM2000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 1)
)
trapDM2000ConfigChangeInteger.setObjects(
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
    trapDM2000ConfigChangeInteger.setStatus(
        ""
    )

trapDM2000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 2)
)
trapDM2000ConfigChangeDisplayString.setObjects(
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
    trapDM2000ConfigChangeDisplayString.setStatus(
        ""
    )

trapDM2000RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 3)
)
trapDM2000RFInputAlarm.setObjects(
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
    trapDM2000RFInputAlarm.setStatus(
        ""
    )

trapDM2000RFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 4)
)
trapDM2000RFOverloadAlarm.setObjects(
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
    trapDM2000RFOverloadAlarm.setStatus(
        ""
    )

trapDM2000RFOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 5)
)
trapDM2000RFOffsetAlarm.setObjects(
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
    trapDM2000RFOffsetAlarm.setStatus(
        ""
    )

trapDM2000OpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 6)
)
trapDM2000OpticalPowerAlarm.setObjects(
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
    trapDM2000OpticalPowerAlarm.setStatus(
        ""
    )

trapDM2000LaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 7)
)
trapDM2000LaserBiasAlarm.setObjects(
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
    trapDM2000LaserBiasAlarm.setStatus(
        ""
    )

trapDM2000LaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 8)
)
trapDM2000LaserTempAlarm.setObjects(
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
    trapDM2000LaserTempAlarm.setStatus(
        ""
    )

trapDM2000TECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 9)
)
trapDM2000TECCurrentAlarm.setObjects(
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
    trapDM2000TECCurrentAlarm.setStatus(
        ""
    )

trapDM2000FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 10)
)
trapDM2000FanCurrentAlarm.setObjects(
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
    trapDM2000FanCurrentAlarm.setStatus(
        ""
    )

trapDM200012vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 11)
)
trapDM200012vAlarm.setObjects(
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
    trapDM200012vAlarm.setStatus(
        ""
    )

trapDM2000ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 12)
)
trapDM2000ModuleTempAlarm.setObjects(
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
    trapDM2000ModuleTempAlarm.setStatus(
        ""
    )

trapDM2000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 13)
)
trapDM2000FlashAlarm.setObjects(
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
    trapDM2000FlashAlarm.setStatus(
        ""
    )

trapDM2000LaserBiasCntLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 14)
)
trapDM2000LaserBiasCntLoopAlarm.setObjects(
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
    trapDM2000LaserBiasCntLoopAlarm.setStatus(
        ""
    )

trapDM2000BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 15)
)
trapDM2000BankBootAlarm.setObjects(
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
    trapDM2000BankBootAlarm.setStatus(
        ""
    )

trapDM2000LaserBiasCntLoopInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 16)
)
trapDM2000LaserBiasCntLoopInitAlarm.setObjects(
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
    trapDM2000LaserBiasCntLoopInitAlarm.setStatus(
        ""
    )

trapDM2000RFParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 17)
)
trapDM2000RFParamInitAlarm.setObjects(
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
    trapDM2000RFParamInitAlarm.setStatus(
        ""
    )

trapDM2000TECParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 18)
)
trapDM2000TECParamInitAlarm.setObjects(
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
    trapDM2000TECParamInitAlarm.setStatus(
        ""
    )

trapDM2000AttnTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 19)
)
trapDM2000AttnTableInitAlarm.setObjects(
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
    trapDM2000AttnTableInitAlarm.setStatus(
        ""
    )

trapDM2000PowerMeterTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 20)
)
trapDM2000PowerMeterTableInitAlarm.setObjects(
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
    trapDM2000PowerMeterTableInitAlarm.setStatus(
        ""
    )

trapDM2000LaserDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 21)
)
trapDM2000LaserDataCRCAlarm.setObjects(
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
    trapDM2000LaserDataCRCAlarm.setStatus(
        ""
    )

trapDM2000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 22)
)
trapDM2000AlarmDataCRCAlarm.setObjects(
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
    trapDM2000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapDM2000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 23)
)
trapDM2000FactoryDataCRCAlarm.setObjects(
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
    trapDM2000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapDM2000UserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 24)
)
trapDM2000UserRFOffAlarm.setObjects(
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
    trapDM2000UserRFOffAlarm.setStatus(
        ""
    )

trapDM2000UserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 25)
)
trapDM2000UserOpticalOffAlarm.setObjects(
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
    trapDM2000UserOpticalOffAlarm.setStatus(
        ""
    )

trapDM2000ResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34, 0, 26)
)
trapDM2000ResetFactoryDefaultAlarm.setObjects(
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
    trapDM2000ResetFactoryDefaultAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2DM2000-MIB",
    **{"Float": Float,
       "trapDM2000ConfigChangeInteger": trapDM2000ConfigChangeInteger,
       "trapDM2000ConfigChangeDisplayString": trapDM2000ConfigChangeDisplayString,
       "trapDM2000RFInputAlarm": trapDM2000RFInputAlarm,
       "trapDM2000RFOverloadAlarm": trapDM2000RFOverloadAlarm,
       "trapDM2000RFOffsetAlarm": trapDM2000RFOffsetAlarm,
       "trapDM2000OpticalPowerAlarm": trapDM2000OpticalPowerAlarm,
       "trapDM2000LaserBiasAlarm": trapDM2000LaserBiasAlarm,
       "trapDM2000LaserTempAlarm": trapDM2000LaserTempAlarm,
       "trapDM2000TECCurrentAlarm": trapDM2000TECCurrentAlarm,
       "trapDM2000FanCurrentAlarm": trapDM2000FanCurrentAlarm,
       "trapDM200012vAlarm": trapDM200012vAlarm,
       "trapDM2000ModuleTempAlarm": trapDM2000ModuleTempAlarm,
       "trapDM2000FlashAlarm": trapDM2000FlashAlarm,
       "trapDM2000LaserBiasCntLoopAlarm": trapDM2000LaserBiasCntLoopAlarm,
       "trapDM2000BankBootAlarm": trapDM2000BankBootAlarm,
       "trapDM2000LaserBiasCntLoopInitAlarm": trapDM2000LaserBiasCntLoopInitAlarm,
       "trapDM2000RFParamInitAlarm": trapDM2000RFParamInitAlarm,
       "trapDM2000TECParamInitAlarm": trapDM2000TECParamInitAlarm,
       "trapDM2000AttnTableInitAlarm": trapDM2000AttnTableInitAlarm,
       "trapDM2000PowerMeterTableInitAlarm": trapDM2000PowerMeterTableInitAlarm,
       "trapDM2000LaserDataCRCAlarm": trapDM2000LaserDataCRCAlarm,
       "trapDM2000AlarmDataCRCAlarm": trapDM2000AlarmDataCRCAlarm,
       "trapDM2000FactoryDataCRCAlarm": trapDM2000FactoryDataCRCAlarm,
       "trapDM2000UserRFOffAlarm": trapDM2000UserRFOffAlarm,
       "trapDM2000UserOpticalOffAlarm": trapDM2000UserOpticalOffAlarm,
       "trapDM2000ResetFactoryDefaultAlarm": trapDM2000ResetFactoryDefaultAlarm,
       "gx2dm2000Descriptor": gx2dm2000Descriptor,
       "gx2dm2000AnalogTable": gx2dm2000AnalogTable,
       "gx2dm2000AnalogEntry": gx2dm2000AnalogEntry,
       "gx2dm2000AnalogTableIndex": gx2dm2000AnalogTableIndex,
       "dm2000labelOffsetNomMonitor": dm2000labelOffsetNomMonitor,
       "dm2000uomOffsetNomMonitor": dm2000uomOffsetNomMonitor,
       "dm2000majorHighOffsetNomMonitor": dm2000majorHighOffsetNomMonitor,
       "dm2000majorLowOffsetNomMonitor": dm2000majorLowOffsetNomMonitor,
       "dm2000minorHighOffsetNomMonitor": dm2000minorHighOffsetNomMonitor,
       "dm2000minorLowOffsetNomMonitor": dm2000minorLowOffsetNomMonitor,
       "dm2000currentValueOffsetNomMonitor": dm2000currentValueOffsetNomMonitor,
       "dm2000stateFlagOffsetNomMonitor": dm2000stateFlagOffsetNomMonitor,
       "dm2000minValueOffsetNomMonitor": dm2000minValueOffsetNomMonitor,
       "dm2000maxValueOffsetNomMonitor": dm2000maxValueOffsetNomMonitor,
       "dm2000alarmStateOffsetNomMonitor": dm2000alarmStateOffsetNomMonitor,
       "dm2000labelOffsetNomCnt": dm2000labelOffsetNomCnt,
       "dm2000uomOffsetNomCnt": dm2000uomOffsetNomCnt,
       "dm2000majorHighOffsetNomCnt": dm2000majorHighOffsetNomCnt,
       "dm2000majorLowOffsetNomCnt": dm2000majorLowOffsetNomCnt,
       "dm2000minorHighOffsetNomCnt": dm2000minorHighOffsetNomCnt,
       "dm2000minorLowOffsetNomCnt": dm2000minorLowOffsetNomCnt,
       "dm2000currentValueOffsetNomCnt": dm2000currentValueOffsetNomCnt,
       "dm2000stateFlagOffsetNomCnt": dm2000stateFlagOffsetNomCnt,
       "dm2000minValueOffsetNomCnt": dm2000minValueOffsetNomCnt,
       "dm2000maxValueOffsetNomCnt": dm2000maxValueOffsetNomCnt,
       "dm2000alarmStateOffsetNomCnt": dm2000alarmStateOffsetNomCnt,
       "dm2000labelRelAttenSetting": dm2000labelRelAttenSetting,
       "dm2000uomRelAttenSetting": dm2000uomRelAttenSetting,
       "dm2000majorHighRelAttenSetting": dm2000majorHighRelAttenSetting,
       "dm2000majorLowRelAttenSetting": dm2000majorLowRelAttenSetting,
       "dm2000minorHighRelAttenSetting": dm2000minorHighRelAttenSetting,
       "dm2000minorLowRelAttenSetting": dm2000minorLowRelAttenSetting,
       "dm2000currentValueRelAttenSetting": dm2000currentValueRelAttenSetting,
       "dm2000stateFlagRelAttenSetting": dm2000stateFlagRelAttenSetting,
       "dm2000minValueRelAttenSetting": dm2000minValueRelAttenSetting,
       "dm2000maxValueRelAttenSetting": dm2000maxValueRelAttenSetting,
       "dm2000alarmStateRelAttenSetting": dm2000alarmStateRelAttenSetting,
       "dm2000labelOptPower": dm2000labelOptPower,
       "dm2000uomOptPower": dm2000uomOptPower,
       "dm2000majorHighOptPower": dm2000majorHighOptPower,
       "dm2000majorLowOptPower": dm2000majorLowOptPower,
       "dm2000minorHighOptPower": dm2000minorHighOptPower,
       "dm2000minorLowOptPower": dm2000minorLowOptPower,
       "dm2000currentValueOptPower": dm2000currentValueOptPower,
       "dm2000stateFlagOptPower": dm2000stateFlagOptPower,
       "dm2000minValueOptPower": dm2000minValueOptPower,
       "dm2000maxValueOptPower": dm2000maxValueOptPower,
       "dm2000alarmStateOptPower": dm2000alarmStateOptPower,
       "dm2000labelLaserBias": dm2000labelLaserBias,
       "dm2000uomLaserBias": dm2000uomLaserBias,
       "dm2000majorHighLaserBias": dm2000majorHighLaserBias,
       "dm2000majorLowLaserBias": dm2000majorLowLaserBias,
       "dm2000minorHighLaserBias": dm2000minorHighLaserBias,
       "dm2000minorLowLaserBias": dm2000minorLowLaserBias,
       "dm2000currentValueLaserBias": dm2000currentValueLaserBias,
       "dm2000stateFlagLaserBias": dm2000stateFlagLaserBias,
       "dm2000minValueLaserBias": dm2000minValueLaserBias,
       "dm2000maxValueLaserBias": dm2000maxValueLaserBias,
       "dm2000alarmStateLaserBias": dm2000alarmStateLaserBias,
       "dm2000labelTecCurrent": dm2000labelTecCurrent,
       "dm2000uomTecCurrent": dm2000uomTecCurrent,
       "dm2000majorHighTecCurrent": dm2000majorHighTecCurrent,
       "dm2000majorLowTecCurrent": dm2000majorLowTecCurrent,
       "dm2000minorHighTecCurrent": dm2000minorHighTecCurrent,
       "dm2000minorLowTecCurrent": dm2000minorLowTecCurrent,
       "dm2000currentValueTecCurrent": dm2000currentValueTecCurrent,
       "dm2000stateFlagTecCurrent": dm2000stateFlagTecCurrent,
       "dm2000minValueTecCurrent": dm2000minValueTecCurrent,
       "dm2000maxValueTecCurrent": dm2000maxValueTecCurrent,
       "dm2000alarmStateTecCurrent": dm2000alarmStateTecCurrent,
       "dm2000labelLaserTemp": dm2000labelLaserTemp,
       "dm2000uomLaserTemp": dm2000uomLaserTemp,
       "dm2000majorHighLaserTemp": dm2000majorHighLaserTemp,
       "dm2000majorLowLaserTemp": dm2000majorLowLaserTemp,
       "dm2000minorHighLaserTemp": dm2000minorHighLaserTemp,
       "dm2000minorLowLaserTemp": dm2000minorLowLaserTemp,
       "dm2000currentValueLaserTemp": dm2000currentValueLaserTemp,
       "dm2000stateFlagLaserTemp": dm2000stateFlagLaserTemp,
       "dm2000minValueLaserTemp": dm2000minValueLaserTemp,
       "dm2000maxValueLaserTemp": dm2000maxValueLaserTemp,
       "dm2000alarmStateLaserTemp": dm2000alarmStateLaserTemp,
       "dm2000labelModuleTemp": dm2000labelModuleTemp,
       "dm2000uomModuleTemp": dm2000uomModuleTemp,
       "dm2000majorHighModuleTemp": dm2000majorHighModuleTemp,
       "dm2000majorLowModuleTemp": dm2000majorLowModuleTemp,
       "dm2000minorHighModuleTemp": dm2000minorHighModuleTemp,
       "dm2000minorLowModuleTemp": dm2000minorLowModuleTemp,
       "dm2000currentValueModuleTemp": dm2000currentValueModuleTemp,
       "dm2000stateFlagModuleTemp": dm2000stateFlagModuleTemp,
       "dm2000minValueModuleTemp": dm2000minValueModuleTemp,
       "dm2000maxValueModuleTemp": dm2000maxValueModuleTemp,
       "dm2000alarmStateModuleTemp": dm2000alarmStateModuleTemp,
       "dm2000labelFanCurrent": dm2000labelFanCurrent,
       "dm2000uomFanCurrent": dm2000uomFanCurrent,
       "dm2000majorHighFanCurrent": dm2000majorHighFanCurrent,
       "dm2000majorLowFanCurrent": dm2000majorLowFanCurrent,
       "dm2000minorHighFanCurrent": dm2000minorHighFanCurrent,
       "dm2000minorLowFanCurrent": dm2000minorLowFanCurrent,
       "dm2000currentValueFanCurrent": dm2000currentValueFanCurrent,
       "dm2000stateFlagFanCurrent": dm2000stateFlagFanCurrent,
       "dm2000minValueFanCurrent": dm2000minValueFanCurrent,
       "dm2000maxValueFanCurrent": dm2000maxValueFanCurrent,
       "dm2000alarmStateFanCurrent": dm2000alarmStateFanCurrent,
       "dm2000label12Volt": dm2000label12Volt,
       "dm2000uom12Volt": dm2000uom12Volt,
       "dm2000majorHigh12Volt": dm2000majorHigh12Volt,
       "dm2000majorLow12Volt": dm2000majorLow12Volt,
       "dm2000minorHigh12Volt": dm2000minorHigh12Volt,
       "dm2000minorLow12Volt": dm2000minorLow12Volt,
       "dm2000currentValue12Volt": dm2000currentValue12Volt,
       "dm2000stateFlag12Volt": dm2000stateFlag12Volt,
       "dm2000minValue12Volt": dm2000minValue12Volt,
       "dm2000maxValue12Volt": dm2000maxValue12Volt,
       "dm2000alarmState12Volt": dm2000alarmState12Volt,
       "gx2dm2000DigitalTable": gx2dm2000DigitalTable,
       "gx2dm2000DigitalEntry": gx2dm2000DigitalEntry,
       "gx2dm2000DigitalTableIndex": gx2dm2000DigitalTableIndex,
       "dm2000labelRfInput": dm2000labelRfInput,
       "dm2000enumRfInput": dm2000enumRfInput,
       "dm2000valueRfInput": dm2000valueRfInput,
       "dm2000stateflagRfInput": dm2000stateflagRfInput,
       "dm2000labelOptOutput": dm2000labelOptOutput,
       "dm2000enumOptOutput": dm2000enumOptOutput,
       "dm2000valueOptOutput": dm2000valueOptOutput,
       "dm2000stateflagOptOutput": dm2000stateflagOptOutput,
       "dm2000labelLaserMode": dm2000labelLaserMode,
       "dm2000enumLaserMode": dm2000enumLaserMode,
       "dm2000valueLaserMode": dm2000valueLaserMode,
       "dm2000stateflagLaserMode": dm2000stateflagLaserMode,
       "dm2000labelLaserSecMode": dm2000labelLaserSecMode,
       "dm2000enumLaserSecMode": dm2000enumLaserSecMode,
       "dm2000valueLaserSecMode": dm2000valueLaserSecMode,
       "dm2000stateflagLaserSecMode": dm2000stateflagLaserSecMode,
       "dm2000labelVideoOffset": dm2000labelVideoOffset,
       "dm2000enumVideoOffset": dm2000enumVideoOffset,
       "dm2000valueVideoOffset": dm2000valueVideoOffset,
       "dm2000stateflagVideoOffset": dm2000stateflagVideoOffset,
       "dm2000labelFactoryDefault": dm2000labelFactoryDefault,
       "dm2000enumFactoryDefault": dm2000enumFactoryDefault,
       "dm2000valueFactoryDefault": dm2000valueFactoryDefault,
       "dm2000stateflagFactoryDefault": dm2000stateflagFactoryDefault,
       "dm2000labelFiberLength": dm2000labelFiberLength,
       "dm2000enumFiberLength": dm2000enumFiberLength,
       "dm2000valueFiberLength": dm2000valueFiberLength,
       "dm2000stateflagFiberLength": dm2000stateflagFiberLength,
       "dm2000labelWavelengthOffset": dm2000labelWavelengthOffset,
       "dm2000enumWavelengthOffset": dm2000enumWavelengthOffset,
       "dm2000valueWavelengthOffset": dm2000valueWavelengthOffset,
       "dm2000stateflagWavelengthOffset": dm2000stateflagWavelengthOffset,
       "gx2dm2000StatusTable": gx2dm2000StatusTable,
       "gx2dm2000StatusEntry": gx2dm2000StatusEntry,
       "gx2dm2000StatusTableIndex": gx2dm2000StatusTableIndex,
       "dm2000labelBoot": dm2000labelBoot,
       "dm2000valueBoot": dm2000valueBoot,
       "dm2000stateflagBoot": dm2000stateflagBoot,
       "dm2000labelFlash": dm2000labelFlash,
       "dm2000valueFlash": dm2000valueFlash,
       "dm2000stateflagFlash": dm2000stateflagFlash,
       "dm2000labelFactoryDataCRC": dm2000labelFactoryDataCRC,
       "dm2000valueFactoryDataCRC": dm2000valueFactoryDataCRC,
       "dm2000stateflagFactoryDataCRC": dm2000stateflagFactoryDataCRC,
       "dm2000labelLaserDataCRC": dm2000labelLaserDataCRC,
       "dm2000valueLaserDataCRC": dm2000valueLaserDataCRC,
       "dm2000stateflagLaserDataCRC": dm2000stateflagLaserDataCRC,
       "dm2000labelAlarmDataCrc": dm2000labelAlarmDataCrc,
       "dm2000valueAlarmDataCrc": dm2000valueAlarmDataCrc,
       "dm2000stateflagAlarmDataCrc": dm2000stateflagAlarmDataCrc,
       "dm2000labelHWStatus": dm2000labelHWStatus,
       "dm2000valueHWStatus": dm2000valueHWStatus,
       "dm2000stateflagHWStatus": dm2000stateflagHWStatus,
       "dm2000labelRFInputStatus": dm2000labelRFInputStatus,
       "dm2000valueRFInputStatus": dm2000valueRFInputStatus,
       "dm2000stateflagRFInputStatus": dm2000stateflagRFInputStatus,
       "gx2dm2000FactoryTable": gx2dm2000FactoryTable,
       "gx2dm2000FactoryEntry": gx2dm2000FactoryEntry,
       "gx2dm2000FactoryTableIndex": gx2dm2000FactoryTableIndex,
       "dm2000bootControlByteValue": dm2000bootControlByteValue,
       "dm2000bootStatusByteValue": dm2000bootStatusByteValue,
       "dm2000bank1CRCValue": dm2000bank1CRCValue,
       "dm2000bank2CRCValue": dm2000bank2CRCValue,
       "dm2000prgEEPROMByteValue": dm2000prgEEPROMByteValue,
       "dm2000factoryCRCValue": dm2000factoryCRCValue,
       "dm2000calculateCRCValue": dm2000calculateCRCValue,
       "dm2000hourMeterValue": dm2000hourMeterValue,
       "dm2000flashPrgCntAValue": dm2000flashPrgCntAValue,
       "dm2000flashPrgCntBValue": dm2000flashPrgCntBValue,
       "dm2000flashBankARevValue": dm2000flashBankARevValue,
       "dm2000flashBankBRevValue": dm2000flashBankBRevValue,
       "gx2Dm2000HoldTimeTable": gx2Dm2000HoldTimeTable,
       "gx2Dm2000HoldTimeEntry": gx2Dm2000HoldTimeEntry,
       "gx2Dm2000HoldTimeTableIndex": gx2Dm2000HoldTimeTableIndex,
       "gx2Dm2000HoldTimeSpecIndex": gx2Dm2000HoldTimeSpecIndex,
       "gx2Dm2000HoldTimeData": gx2Dm2000HoldTimeData}
)
