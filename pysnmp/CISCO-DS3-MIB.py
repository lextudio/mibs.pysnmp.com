# SNMP MIB module (CISCO-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:06 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# MODULE-IDENTITY

ciscoDs3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132)
)
ciscoDs3MIB.setRevisions(
        ("2002-05-21 00:00",
         "2001-08-31 00:00",
         "2000-10-10 00:00",
         "2000-02-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDs3MIBObjects_ObjectIdentity = ObjectIdentity
ciscoDs3MIBObjects = _CiscoDs3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1)
)
_Cds3Config_ObjectIdentity = ObjectIdentity
cds3Config = _Cds3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1)
)
_Cds3ConfigTable_Object = MibTable
cds3ConfigTable = _Cds3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cds3ConfigTable.setStatus("current")
_Cds3ConfigEntry_Object = MibTableRow
cds3ConfigEntry = _Cds3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1)
)
cds3ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3ConfigEntry.setStatus("current")


class _Cds3LineType_Type(Integer32):
    """Custom type cds3LineType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("ds3cbitadm", 1),
          ("ds3cbitfrmronly", 15),
          ("ds3cbitplcp", 2),
          ("ds3m23adm", 6),
          ("ds3m23frmronly", 16),
          ("ds3m23plcp", 7),
          ("dsx3CbitParity", 11),
          ("dsx3ClearChannel", 12),
          ("dsx3M23", 9),
          ("dsx3SYNTRAN", 10),
          ("e3Framed", 13),
          ("e3Plcp", 14),
          ("e3g751adm", 4),
          ("e3g751frmronly", 18),
          ("e3g751plcp", 5),
          ("e3g832adm", 3),
          ("e3g832frmronly", 17),
          ("other", 8))
    )


_Cds3LineType_Type.__name__ = "Integer32"
_Cds3LineType_Object = MibTableColumn
cds3LineType = _Cds3LineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 1),
    _Cds3LineType_Type()
)
cds3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LineType.setStatus("current")


class _Cds3LineAIScBitsCheck_Type(Integer32):
    """Custom type cds3LineAIScBitsCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("check", 1),
          ("ignore", 2),
          ("notApplicable", 3))
    )


_Cds3LineAIScBitsCheck_Type.__name__ = "Integer32"
_Cds3LineAIScBitsCheck_Object = MibTableColumn
cds3LineAIScBitsCheck = _Cds3LineAIScBitsCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 2),
    _Cds3LineAIScBitsCheck_Type()
)
cds3LineAIScBitsCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LineAIScBitsCheck.setStatus("current")


class _Cds3LineRcvFEACValidation_Type(Integer32):
    """Custom type cds3LineRcvFEACValidation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("fEACCodes4Of5", 1),
          ("fEACCodes8Of10", 2))
    )


_Cds3LineRcvFEACValidation_Type.__name__ = "Integer32"
_Cds3LineRcvFEACValidation_Object = MibTableColumn
cds3LineRcvFEACValidation = _Cds3LineRcvFEACValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 3),
    _Cds3LineRcvFEACValidation_Type()
)
cds3LineRcvFEACValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LineRcvFEACValidation.setStatus("current")


class _Cds3LineOOFCriteria_Type(Integer32):
    """Custom type cds3LineOOFCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits3Of16", 2),
          ("bits3Of8", 1),
          ("notApplicable", 3))
    )


_Cds3LineOOFCriteria_Type.__name__ = "Integer32"
_Cds3LineOOFCriteria_Object = MibTableColumn
cds3LineOOFCriteria = _Cds3LineOOFCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 4),
    _Cds3LineOOFCriteria_Type()
)
cds3LineOOFCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LineOOFCriteria.setStatus("current")


class _Cds3TraceToTransmit_Type(DisplayString):
    """Custom type cds3TraceToTransmit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Cds3TraceToTransmit_Type.__name__ = "DisplayString"
_Cds3TraceToTransmit_Object = MibTableColumn
cds3TraceToTransmit = _Cds3TraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 5),
    _Cds3TraceToTransmit_Type()
)
cds3TraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3TraceToTransmit.setStatus("current")


class _Cds3TraceToExpect_Type(DisplayString):
    """Custom type cds3TraceToExpect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Cds3TraceToExpect_Type.__name__ = "DisplayString"
_Cds3TraceToExpect_Object = MibTableColumn
cds3TraceToExpect = _Cds3TraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 6),
    _Cds3TraceToExpect_Type()
)
cds3TraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3TraceToExpect.setStatus("current")


class _Cds3TraceAlarm_Type(Integer32):
    """Custom type cds3TraceAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("traceFailure", 2))
    )


_Cds3TraceAlarm_Type.__name__ = "Integer32"
_Cds3TraceAlarm_Object = MibTableColumn
cds3TraceAlarm = _Cds3TraceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 7),
    _Cds3TraceAlarm_Type()
)
cds3TraceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3TraceAlarm.setStatus("current")


class _Cds3InternalEqualizer_Type(Integer32):
    """Custom type cds3InternalEqualizer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byPass", 2),
          ("use", 1))
    )


_Cds3InternalEqualizer_Type.__name__ = "Integer32"
_Cds3InternalEqualizer_Object = MibTableColumn
cds3InternalEqualizer = _Cds3InternalEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 8),
    _Cds3InternalEqualizer_Type()
)
cds3InternalEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3InternalEqualizer.setStatus("current")


class _Cds3NearEndLineLoopbackStatus_Type(Unsigned32):
    """Custom type cds3NearEndLineLoopbackStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3NearEndLineLoopbackStatus_Type.__name__ = "Unsigned32"
_Cds3NearEndLineLoopbackStatus_Object = MibTableColumn
cds3NearEndLineLoopbackStatus = _Cds3NearEndLineLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 9),
    _Cds3NearEndLineLoopbackStatus_Type()
)
cds3NearEndLineLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3NearEndLineLoopbackStatus.setStatus("current")


class _Cds3FarEndLineLoopbackStatus_Type(Unsigned32):
    """Custom type cds3FarEndLineLoopbackStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3FarEndLineLoopbackStatus_Type.__name__ = "Unsigned32"
_Cds3FarEndLineLoopbackStatus_Object = MibTableColumn
cds3FarEndLineLoopbackStatus = _Cds3FarEndLineLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 1, 1, 1, 10),
    _Cds3FarEndLineLoopbackStatus_Type()
)
cds3FarEndLineLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3FarEndLineLoopbackStatus.setStatus("current")
_Cds3Alarm_ObjectIdentity = ObjectIdentity
cds3Alarm = _Cds3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2)
)
_Cds3AlarmConfig_ObjectIdentity = ObjectIdentity
cds3AlarmConfig = _Cds3AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1)
)
_Cds3AlarmConfigTable_Object = MibTable
cds3AlarmConfigTable = _Cds3AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cds3AlarmConfigTable.setStatus("current")
_Cds3AlarmConfigEntry_Object = MibTableRow
cds3AlarmConfigEntry = _Cds3AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1)
)
cds3AlarmConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3AlarmConfigEntry.setStatus("current")


class _Cds3NEAlarmUpCount_Type(Unsigned32):
    """Custom type cds3NEAlarmUpCount based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3NEAlarmUpCount_Type.__name__ = "Unsigned32"
_Cds3NEAlarmUpCount_Object = MibTableColumn
cds3NEAlarmUpCount = _Cds3NEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 1),
    _Cds3NEAlarmUpCount_Type()
)
cds3NEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3NEAlarmUpCount.setStatus("current")


class _Cds3NEAlarmDownCount_Type(Unsigned32):
    """Custom type cds3NEAlarmDownCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3NEAlarmDownCount_Type.__name__ = "Unsigned32"
_Cds3NEAlarmDownCount_Object = MibTableColumn
cds3NEAlarmDownCount = _Cds3NEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 2),
    _Cds3NEAlarmDownCount_Type()
)
cds3NEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3NEAlarmDownCount.setStatus("current")


class _Cds3NEAlarmThreshold_Type(Unsigned32):
    """Custom type cds3NEAlarmThreshold based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3NEAlarmThreshold_Type.__name__ = "Unsigned32"
_Cds3NEAlarmThreshold_Object = MibTableColumn
cds3NEAlarmThreshold = _Cds3NEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 3),
    _Cds3NEAlarmThreshold_Type()
)
cds3NEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3NEAlarmThreshold.setStatus("current")


class _Cds3FEAlarmUpCount_Type(Unsigned32):
    """Custom type cds3FEAlarmUpCount based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3FEAlarmUpCount_Type.__name__ = "Unsigned32"
_Cds3FEAlarmUpCount_Object = MibTableColumn
cds3FEAlarmUpCount = _Cds3FEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 4),
    _Cds3FEAlarmUpCount_Type()
)
cds3FEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3FEAlarmUpCount.setStatus("current")


class _Cds3FEAlarmDownCount_Type(Unsigned32):
    """Custom type cds3FEAlarmDownCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3FEAlarmDownCount_Type.__name__ = "Unsigned32"
_Cds3FEAlarmDownCount_Object = MibTableColumn
cds3FEAlarmDownCount = _Cds3FEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 5),
    _Cds3FEAlarmDownCount_Type()
)
cds3FEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3FEAlarmDownCount.setStatus("current")


class _Cds3FEAlarmThreshold_Type(Unsigned32):
    """Custom type cds3FEAlarmThreshold based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3FEAlarmThreshold_Type.__name__ = "Unsigned32"
_Cds3FEAlarmThreshold_Object = MibTableColumn
cds3FEAlarmThreshold = _Cds3FEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 6),
    _Cds3FEAlarmThreshold_Type()
)
cds3FEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3FEAlarmThreshold.setStatus("current")


class _Cds3StatisticalAlarmSeverity_Type(Integer32):
    """Custom type cds3StatisticalAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_Cds3StatisticalAlarmSeverity_Type.__name__ = "Integer32"
_Cds3StatisticalAlarmSeverity_Object = MibTableColumn
cds3StatisticalAlarmSeverity = _Cds3StatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 7),
    _Cds3StatisticalAlarmSeverity_Type()
)
cds3StatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3StatisticalAlarmSeverity.setStatus("current")


class _Cds3LCV15MinThreshold_Type(Unsigned32):
    """Custom type cds3LCV15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LCV15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3LCV15MinThreshold_Object = MibTableColumn
cds3LCV15MinThreshold = _Cds3LCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 8),
    _Cds3LCV15MinThreshold_Type()
)
cds3LCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LCV15MinThreshold.setStatus("current")


class _Cds3LCV24HrThreshold_Type(Unsigned32):
    """Custom type cds3LCV24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LCV24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3LCV24HrThreshold_Object = MibTableColumn
cds3LCV24HrThreshold = _Cds3LCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 9),
    _Cds3LCV24HrThreshold_Type()
)
cds3LCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LCV24HrThreshold.setStatus("current")


class _Cds3LES15MinThreshold_Type(Unsigned32):
    """Custom type cds3LES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3LES15MinThreshold_Object = MibTableColumn
cds3LES15MinThreshold = _Cds3LES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 10),
    _Cds3LES15MinThreshold_Type()
)
cds3LES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LES15MinThreshold.setStatus("current")


class _Cds3LES24HrThreshold_Type(Unsigned32):
    """Custom type cds3LES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3LES24HrThreshold_Object = MibTableColumn
cds3LES24HrThreshold = _Cds3LES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 11),
    _Cds3LES24HrThreshold_Type()
)
cds3LES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LES24HrThreshold.setStatus("current")


class _Cds3PCV15MinThreshold_Type(Unsigned32):
    """Custom type cds3PCV15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PCV15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PCV15MinThreshold_Object = MibTableColumn
cds3PCV15MinThreshold = _Cds3PCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 12),
    _Cds3PCV15MinThreshold_Type()
)
cds3PCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PCV15MinThreshold.setStatus("current")


class _Cds3PCV24HrThreshold_Type(Unsigned32):
    """Custom type cds3PCV24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PCV24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PCV24HrThreshold_Object = MibTableColumn
cds3PCV24HrThreshold = _Cds3PCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 13),
    _Cds3PCV24HrThreshold_Type()
)
cds3PCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PCV24HrThreshold.setStatus("current")


class _Cds3PES15MinThreshold_Type(Unsigned32):
    """Custom type cds3PES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PES15MinThreshold_Object = MibTableColumn
cds3PES15MinThreshold = _Cds3PES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 14),
    _Cds3PES15MinThreshold_Type()
)
cds3PES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PES15MinThreshold.setStatus("current")


class _Cds3PES24HrThreshold_Type(Unsigned32):
    """Custom type cds3PES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PES24HrThreshold_Object = MibTableColumn
cds3PES24HrThreshold = _Cds3PES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 15),
    _Cds3PES24HrThreshold_Type()
)
cds3PES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PES24HrThreshold.setStatus("current")


class _Cds3PSES15MinThreshold_Type(Unsigned32):
    """Custom type cds3PSES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PSES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PSES15MinThreshold_Object = MibTableColumn
cds3PSES15MinThreshold = _Cds3PSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 16),
    _Cds3PSES15MinThreshold_Type()
)
cds3PSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PSES15MinThreshold.setStatus("current")


class _Cds3PSES24HrThreshold_Type(Unsigned32):
    """Custom type cds3PSES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PSES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PSES24HrThreshold_Object = MibTableColumn
cds3PSES24HrThreshold = _Cds3PSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 17),
    _Cds3PSES24HrThreshold_Type()
)
cds3PSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PSES24HrThreshold.setStatus("current")


class _Cds3SEFS15MinThreshold_Type(Unsigned32):
    """Custom type cds3SEFS15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3SEFS15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3SEFS15MinThreshold_Object = MibTableColumn
cds3SEFS15MinThreshold = _Cds3SEFS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 18),
    _Cds3SEFS15MinThreshold_Type()
)
cds3SEFS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3SEFS15MinThreshold.setStatus("current")


class _Cds3SEFS24HrThreshold_Type(Unsigned32):
    """Custom type cds3SEFS24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3SEFS24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3SEFS24HrThreshold_Object = MibTableColumn
cds3SEFS24HrThreshold = _Cds3SEFS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 19),
    _Cds3SEFS24HrThreshold_Type()
)
cds3SEFS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3SEFS24HrThreshold.setStatus("current")


class _Cds3UAS15MinThreshold_Type(Unsigned32):
    """Custom type cds3UAS15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3UAS15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3UAS15MinThreshold_Object = MibTableColumn
cds3UAS15MinThreshold = _Cds3UAS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 20),
    _Cds3UAS15MinThreshold_Type()
)
cds3UAS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3UAS15MinThreshold.setStatus("current")


class _Cds3UAS24HrThreshold_Type(Unsigned32):
    """Custom type cds3UAS24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3UAS24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3UAS24HrThreshold_Object = MibTableColumn
cds3UAS24HrThreshold = _Cds3UAS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 21),
    _Cds3UAS24HrThreshold_Type()
)
cds3UAS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3UAS24HrThreshold.setStatus("current")


class _Cds3CCV15MinThreshold_Type(Unsigned32):
    """Custom type cds3CCV15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CCV15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3CCV15MinThreshold_Object = MibTableColumn
cds3CCV15MinThreshold = _Cds3CCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 22),
    _Cds3CCV15MinThreshold_Type()
)
cds3CCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CCV15MinThreshold.setStatus("current")


class _Cds3CCV24HrThreshold_Type(Unsigned32):
    """Custom type cds3CCV24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CCV24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3CCV24HrThreshold_Object = MibTableColumn
cds3CCV24HrThreshold = _Cds3CCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 23),
    _Cds3CCV24HrThreshold_Type()
)
cds3CCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CCV24HrThreshold.setStatus("current")


class _Cds3CES15MinThreshold_Type(Unsigned32):
    """Custom type cds3CES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3CES15MinThreshold_Object = MibTableColumn
cds3CES15MinThreshold = _Cds3CES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 24),
    _Cds3CES15MinThreshold_Type()
)
cds3CES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CES15MinThreshold.setStatus("current")


class _Cds3CES24HrThreshold_Type(Unsigned32):
    """Custom type cds3CES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3CES24HrThreshold_Object = MibTableColumn
cds3CES24HrThreshold = _Cds3CES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 25),
    _Cds3CES24HrThreshold_Type()
)
cds3CES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CES24HrThreshold.setStatus("current")


class _Cds3CSES15MinThreshold_Type(Unsigned32):
    """Custom type cds3CSES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CSES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3CSES15MinThreshold_Object = MibTableColumn
cds3CSES15MinThreshold = _Cds3CSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 26),
    _Cds3CSES15MinThreshold_Type()
)
cds3CSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CSES15MinThreshold.setStatus("current")


class _Cds3CSES24HrThreshold_Type(Unsigned32):
    """Custom type cds3CSES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3CSES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3CSES24HrThreshold_Object = MibTableColumn
cds3CSES24HrThreshold = _Cds3CSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 27),
    _Cds3CSES24HrThreshold_Type()
)
cds3CSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3CSES24HrThreshold.setStatus("current")


class _Cds3LSES15MinThreshold_Type(Unsigned32):
    """Custom type cds3LSES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LSES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3LSES15MinThreshold_Object = MibTableColumn
cds3LSES15MinThreshold = _Cds3LSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 28),
    _Cds3LSES15MinThreshold_Type()
)
cds3LSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LSES15MinThreshold.setStatus("current")


class _Cds3LSES24HrThreshold_Type(Unsigned32):
    """Custom type cds3LSES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LSES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3LSES24HrThreshold_Object = MibTableColumn
cds3LSES24HrThreshold = _Cds3LSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 29),
    _Cds3LSES24HrThreshold_Type()
)
cds3LSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3LSES24HrThreshold.setStatus("current")


class _Cds3LineStatisticalAlarmState_Type(Unsigned32):
    """Custom type cds3LineStatisticalAlarmState based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3LineStatisticalAlarmState_Type.__name__ = "Unsigned32"
_Cds3LineStatisticalAlarmState_Object = MibTableColumn
cds3LineStatisticalAlarmState = _Cds3LineStatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 1, 1, 30),
    _Cds3LineStatisticalAlarmState_Type()
)
cds3LineStatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LineStatisticalAlarmState.setStatus("current")
_Cds3AlarmConfigPlcpTable_Object = MibTable
cds3AlarmConfigPlcpTable = _Cds3AlarmConfigPlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cds3AlarmConfigPlcpTable.setStatus("current")
_Cds3AlarmConfigPlcpEntry_Object = MibTableRow
cds3AlarmConfigPlcpEntry = _Cds3AlarmConfigPlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1)
)
cds3AlarmConfigPlcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3AlarmConfigPlcpEntry.setStatus("current")


class _Cds3PlcpStatisticalAlarmSeverity_Type(Integer32):
    """Custom type cds3PlcpStatisticalAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_Cds3PlcpStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_Cds3PlcpStatisticalAlarmSeverity_Object = MibTableColumn
cds3PlcpStatisticalAlarmSeverity = _Cds3PlcpStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 1),
    _Cds3PlcpStatisticalAlarmSeverity_Type()
)
cds3PlcpStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpStatisticalAlarmSeverity.setStatus("current")


class _Cds3PlcpBip8CV15MinThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8CV15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8CV15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8CV15MinThreshold_Object = MibTableColumn
cds3PlcpBip8CV15MinThreshold = _Cds3PlcpBip8CV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 2),
    _Cds3PlcpBip8CV15MinThreshold_Type()
)
cds3PlcpBip8CV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8CV15MinThreshold.setStatus("current")


class _Cds3PlcpBip8CV24HrThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8CV24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8CV24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8CV24HrThreshold_Object = MibTableColumn
cds3PlcpBip8CV24HrThreshold = _Cds3PlcpBip8CV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 3),
    _Cds3PlcpBip8CV24HrThreshold_Type()
)
cds3PlcpBip8CV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8CV24HrThreshold.setStatus("current")


class _Cds3PlcpBip8ES15MinThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8ES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8ES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8ES15MinThreshold_Object = MibTableColumn
cds3PlcpBip8ES15MinThreshold = _Cds3PlcpBip8ES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 4),
    _Cds3PlcpBip8ES15MinThreshold_Type()
)
cds3PlcpBip8ES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8ES15MinThreshold.setStatus("current")


class _Cds3PlcpBip8ES24HrThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8ES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8ES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8ES24HrThreshold_Object = MibTableColumn
cds3PlcpBip8ES24HrThreshold = _Cds3PlcpBip8ES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 5),
    _Cds3PlcpBip8ES24HrThreshold_Type()
)
cds3PlcpBip8ES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8ES24HrThreshold.setStatus("current")


class _Cds3PlcpBip8SES15MinThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8SES15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8SES15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8SES15MinThreshold_Object = MibTableColumn
cds3PlcpBip8SES15MinThreshold = _Cds3PlcpBip8SES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 6),
    _Cds3PlcpBip8SES15MinThreshold_Type()
)
cds3PlcpBip8SES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8SES15MinThreshold.setStatus("current")


class _Cds3PlcpBip8SES24HrThreshold_Type(Unsigned32):
    """Custom type cds3PlcpBip8SES24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpBip8SES24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpBip8SES24HrThreshold_Object = MibTableColumn
cds3PlcpBip8SES24HrThreshold = _Cds3PlcpBip8SES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 7),
    _Cds3PlcpBip8SES24HrThreshold_Type()
)
cds3PlcpBip8SES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpBip8SES24HrThreshold.setStatus("current")


class _Cds3PlcpSEFS15MinThreshold_Type(Unsigned32):
    """Custom type cds3PlcpSEFS15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpSEFS15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpSEFS15MinThreshold_Object = MibTableColumn
cds3PlcpSEFS15MinThreshold = _Cds3PlcpSEFS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 8),
    _Cds3PlcpSEFS15MinThreshold_Type()
)
cds3PlcpSEFS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpSEFS15MinThreshold.setStatus("current")


class _Cds3PlcpSEFS24HrThreshold_Type(Unsigned32):
    """Custom type cds3PlcpSEFS24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpSEFS24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpSEFS24HrThreshold_Object = MibTableColumn
cds3PlcpSEFS24HrThreshold = _Cds3PlcpSEFS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 9),
    _Cds3PlcpSEFS24HrThreshold_Type()
)
cds3PlcpSEFS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpSEFS24HrThreshold.setStatus("current")


class _Cds3PlcpUAS15MinThreshold_Type(Unsigned32):
    """Custom type cds3PlcpUAS15MinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpUAS15MinThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpUAS15MinThreshold_Object = MibTableColumn
cds3PlcpUAS15MinThreshold = _Cds3PlcpUAS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 10),
    _Cds3PlcpUAS15MinThreshold_Type()
)
cds3PlcpUAS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpUAS15MinThreshold.setStatus("current")


class _Cds3PlcpUAS24HrThreshold_Type(Unsigned32):
    """Custom type cds3PlcpUAS24HrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds3PlcpUAS24HrThreshold_Type.__name__ = "Unsigned32"
_Cds3PlcpUAS24HrThreshold_Object = MibTableColumn
cds3PlcpUAS24HrThreshold = _Cds3PlcpUAS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 1, 2, 1, 11),
    _Cds3PlcpUAS24HrThreshold_Type()
)
cds3PlcpUAS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds3PlcpUAS24HrThreshold.setStatus("current")
_Cds3AlarmPlcpTable_Object = MibTable
cds3AlarmPlcpTable = _Cds3AlarmPlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cds3AlarmPlcpTable.setStatus("current")
_Cds3AlarmPlcpEntry_Object = MibTableRow
cds3AlarmPlcpEntry = _Cds3AlarmPlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1)
)
cds3AlarmPlcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3AlarmPlcpEntry.setStatus("current")
_Cds3PlcpLineAlarmState_Type = Unsigned32
_Cds3PlcpLineAlarmState_Object = MibTableColumn
cds3PlcpLineAlarmState = _Cds3PlcpLineAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 1),
    _Cds3PlcpLineAlarmState_Type()
)
cds3PlcpLineAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpLineAlarmState.setStatus("current")
_Cds3PlcpLineStatisticalAlarmState_Type = Unsigned32
_Cds3PlcpLineStatisticalAlarmState_Object = MibTableColumn
cds3PlcpLineStatisticalAlarmState = _Cds3PlcpLineStatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 2),
    _Cds3PlcpLineStatisticalAlarmState_Type()
)
cds3PlcpLineStatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpLineStatisticalAlarmState.setStatus("current")
_Cds3PlcpBip8CVCurrent_Type = Counter32
_Cds3PlcpBip8CVCurrent_Object = MibTableColumn
cds3PlcpBip8CVCurrent = _Cds3PlcpBip8CVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 3),
    _Cds3PlcpBip8CVCurrent_Type()
)
cds3PlcpBip8CVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8CVCurrent.setStatus("current")
_Cds3PlcpBip8CV24HrBucket_Type = Counter32
_Cds3PlcpBip8CV24HrBucket_Object = MibTableColumn
cds3PlcpBip8CV24HrBucket = _Cds3PlcpBip8CV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 4),
    _Cds3PlcpBip8CV24HrBucket_Type()
)
cds3PlcpBip8CV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8CV24HrBucket.setStatus("current")
_Cds3PlcpBip8ESCurrent_Type = Counter32
_Cds3PlcpBip8ESCurrent_Object = MibTableColumn
cds3PlcpBip8ESCurrent = _Cds3PlcpBip8ESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 5),
    _Cds3PlcpBip8ESCurrent_Type()
)
cds3PlcpBip8ESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8ESCurrent.setStatus("current")
_Cds3PlcpBip8ES24HrBucket_Type = Counter32
_Cds3PlcpBip8ES24HrBucket_Object = MibTableColumn
cds3PlcpBip8ES24HrBucket = _Cds3PlcpBip8ES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 6),
    _Cds3PlcpBip8ES24HrBucket_Type()
)
cds3PlcpBip8ES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8ES24HrBucket.setStatus("current")
_Cds3PlcpBip8SESCurrent_Type = Counter32
_Cds3PlcpBip8SESCurrent_Object = MibTableColumn
cds3PlcpBip8SESCurrent = _Cds3PlcpBip8SESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 7),
    _Cds3PlcpBip8SESCurrent_Type()
)
cds3PlcpBip8SESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8SESCurrent.setStatus("current")
_Cds3PlcpBip8SES24HrBucket_Type = Counter32
_Cds3PlcpBip8SES24HrBucket_Object = MibTableColumn
cds3PlcpBip8SES24HrBucket = _Cds3PlcpBip8SES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 8),
    _Cds3PlcpBip8SES24HrBucket_Type()
)
cds3PlcpBip8SES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpBip8SES24HrBucket.setStatus("current")
_Cds3PlcpSEFSCurrent_Type = Counter32
_Cds3PlcpSEFSCurrent_Object = MibTableColumn
cds3PlcpSEFSCurrent = _Cds3PlcpSEFSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 9),
    _Cds3PlcpSEFSCurrent_Type()
)
cds3PlcpSEFSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpSEFSCurrent.setStatus("current")
_Cds3PlcpSEFS24HrBucket_Type = Counter32
_Cds3PlcpSEFS24HrBucket_Object = MibTableColumn
cds3PlcpSEFS24HrBucket = _Cds3PlcpSEFS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 10),
    _Cds3PlcpSEFS24HrBucket_Type()
)
cds3PlcpSEFS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpSEFS24HrBucket.setStatus("current")
_Cds3PlcpUASCurrent_Type = Counter32
_Cds3PlcpUASCurrent_Object = MibTableColumn
cds3PlcpUASCurrent = _Cds3PlcpUASCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 11),
    _Cds3PlcpUASCurrent_Type()
)
cds3PlcpUASCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpUASCurrent.setStatus("current")
_Cds3PlcpUAS24HrBucket_Type = Counter32
_Cds3PlcpUAS24HrBucket_Object = MibTableColumn
cds3PlcpUAS24HrBucket = _Cds3PlcpUAS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 2, 2, 1, 12),
    _Cds3PlcpUAS24HrBucket_Type()
)
cds3PlcpUAS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpUAS24HrBucket.setStatus("current")
_Cds3Stats_ObjectIdentity = ObjectIdentity
cds3Stats = _Cds3Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3)
)
_Cds3StatsTable_Object = MibTable
cds3StatsTable = _Cds3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cds3StatsTable.setStatus("current")
_Cds3StatsEntry_Object = MibTableRow
cds3StatsEntry = _Cds3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1)
)
cds3StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3StatsEntry.setStatus("current")
_Cds3RcvLOSCount_Type = Counter32
_Cds3RcvLOSCount_Object = MibTableColumn
cds3RcvLOSCount = _Cds3RcvLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 1),
    _Cds3RcvLOSCount_Type()
)
cds3RcvLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3RcvLOSCount.setStatus("current")
_Cds3RcvOOFCount_Type = Counter32
_Cds3RcvOOFCount_Object = MibTableColumn
cds3RcvOOFCount = _Cds3RcvOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 2),
    _Cds3RcvOOFCount_Type()
)
cds3RcvOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3RcvOOFCount.setStatus("current")
_Cds3RAICount_Type = Counter32
_Cds3RAICount_Object = MibTableColumn
cds3RAICount = _Cds3RAICount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 3),
    _Cds3RAICount_Type()
)
cds3RAICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3RAICount.setStatus("current")
_Cds3CCVCount_Type = Counter32
_Cds3CCVCount_Object = MibTableColumn
cds3CCVCount = _Cds3CCVCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 4),
    _Cds3CCVCount_Type()
)
cds3CCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CCVCount.setStatus("current")
_Cds3FECount_Type = Counter32
_Cds3FECount_Object = MibTableColumn
cds3FECount = _Cds3FECount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 5),
    _Cds3FECount_Type()
)
cds3FECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3FECount.setStatus("current")
_Cds3EXZSCount_Type = Counter32
_Cds3EXZSCount_Object = MibTableColumn
cds3EXZSCount = _Cds3EXZSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 6),
    _Cds3EXZSCount_Type()
)
cds3EXZSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3EXZSCount.setStatus("current")
_Cds3LCVCount_Type = Counter32
_Cds3LCVCount_Object = MibTableColumn
cds3LCVCount = _Cds3LCVCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 7),
    _Cds3LCVCount_Type()
)
cds3LCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LCVCount.setStatus("current")
_Cds3PCVCount_Type = Counter32
_Cds3PCVCount_Object = MibTableColumn
cds3PCVCount = _Cds3PCVCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 8),
    _Cds3PCVCount_Type()
)
cds3PCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PCVCount.setStatus("current")
_Cds3CPECount_Type = Counter32
_Cds3CPECount_Object = MibTableColumn
cds3CPECount = _Cds3CPECount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 9),
    _Cds3CPECount_Type()
)
cds3CPECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CPECount.setStatus("current")
_Cds3FEBECount_Type = Counter32
_Cds3FEBECount_Object = MibTableColumn
cds3FEBECount = _Cds3FEBECount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 10),
    _Cds3FEBECount_Type()
)
cds3FEBECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3FEBECount.setStatus("current")
_Cds3RcvAISCount_Type = Counter32
_Cds3RcvAISCount_Object = MibTableColumn
cds3RcvAISCount = _Cds3RcvAISCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 1, 1, 11),
    _Cds3RcvAISCount_Type()
)
cds3RcvAISCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3RcvAISCount.setStatus("current")
_Cds3PlcpStatsTable_Object = MibTable
cds3PlcpStatsTable = _Cds3PlcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cds3PlcpStatsTable.setStatus("current")
_Cds3PlcpStatsEntry_Object = MibTableRow
cds3PlcpStatsEntry = _Cds3PlcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1)
)
cds3PlcpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3PlcpStatsEntry.setStatus("current")
_Cds3PlcpRcvBip8Count_Type = Counter32
_Cds3PlcpRcvBip8Count_Object = MibTableColumn
cds3PlcpRcvBip8Count = _Cds3PlcpRcvBip8Count_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 1),
    _Cds3PlcpRcvBip8Count_Type()
)
cds3PlcpRcvBip8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpRcvBip8Count.setStatus("current")
_Cds3PlcpRcvOOFCount_Type = Counter32
_Cds3PlcpRcvOOFCount_Object = MibTableColumn
cds3PlcpRcvOOFCount = _Cds3PlcpRcvOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 2),
    _Cds3PlcpRcvOOFCount_Type()
)
cds3PlcpRcvOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpRcvOOFCount.setStatus("current")
_Cds3PlcpRcvRAICount_Type = Counter32
_Cds3PlcpRcvRAICount_Object = MibTableColumn
cds3PlcpRcvRAICount = _Cds3PlcpRcvRAICount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 3),
    _Cds3PlcpRcvRAICount_Type()
)
cds3PlcpRcvRAICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpRcvRAICount.setStatus("current")
_Cds3PlcpFECount_Type = Counter32
_Cds3PlcpFECount_Object = MibTableColumn
cds3PlcpFECount = _Cds3PlcpFECount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 4),
    _Cds3PlcpFECount_Type()
)
cds3PlcpFECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpFECount.setStatus("current")
_Cds3PlcpFESecCount_Type = Counter32
_Cds3PlcpFESecCount_Object = MibTableColumn
cds3PlcpFESecCount = _Cds3PlcpFESecCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 5),
    _Cds3PlcpFESecCount_Type()
)
cds3PlcpFESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpFESecCount.setStatus("current")
_Cds3PlcpSEFSecCount_Type = Counter32
_Cds3PlcpSEFSecCount_Object = MibTableColumn
cds3PlcpSEFSecCount = _Cds3PlcpSEFSecCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 6),
    _Cds3PlcpSEFSecCount_Type()
)
cds3PlcpSEFSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpSEFSecCount.setStatus("current")
_Cds3PlcpFEBECount_Type = Counter32
_Cds3PlcpFEBECount_Object = MibTableColumn
cds3PlcpFEBECount = _Cds3PlcpFEBECount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 7),
    _Cds3PlcpFEBECount_Type()
)
cds3PlcpFEBECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpFEBECount.setStatus("current")
_Cds3PlcpFEBESecCount_Type = Counter32
_Cds3PlcpFEBESecCount_Object = MibTableColumn
cds3PlcpFEBESecCount = _Cds3PlcpFEBESecCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 8),
    _Cds3PlcpFEBESecCount_Type()
)
cds3PlcpFEBESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpFEBESecCount.setStatus("current")
_Cds3PlcpSEFEBESecCount_Type = Counter32
_Cds3PlcpSEFEBESecCount_Object = MibTableColumn
cds3PlcpSEFEBESecCount = _Cds3PlcpSEFEBESecCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 2, 1, 9),
    _Cds3PlcpSEFEBESecCount_Type()
)
cds3PlcpSEFEBESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PlcpSEFEBESecCount.setStatus("current")
_Cds3IntervalTable_Object = MibTable
cds3IntervalTable = _Cds3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cds3IntervalTable.setStatus("current")
_Cds3IntervalEntry_Object = MibTableRow
cds3IntervalEntry = _Cds3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 4, 1)
)
cds3IntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DS3-MIB", "cds3IntervalNumber"),
)
if mibBuilder.loadTexts:
    cds3IntervalEntry.setStatus("current")


class _Cds3IntervalNumber_Type(Integer32):
    """Custom type cds3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Cds3IntervalNumber_Type.__name__ = "Integer32"
_Cds3IntervalNumber_Object = MibTableColumn
cds3IntervalNumber = _Cds3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 4, 1, 1),
    _Cds3IntervalNumber_Type()
)
cds3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3IntervalNumber.setStatus("current")
_Cds3IntervalLSESs_Type = Counter32
_Cds3IntervalLSESs_Object = MibTableColumn
cds3IntervalLSESs = _Cds3IntervalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 4, 1, 2),
    _Cds3IntervalLSESs_Type()
)
cds3IntervalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3IntervalLSESs.setStatus("current")
_Cds3Current24HrTable_Object = MibTable
cds3Current24HrTable = _Cds3Current24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cds3Current24HrTable.setStatus("current")
_Cds3Current24HrEntry_Object = MibTableRow
cds3Current24HrEntry = _Cds3Current24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1)
)
cds3Current24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3Current24HrEntry.setStatus("current")
_Cds3LCVCurrent24Hr_Type = Counter32
_Cds3LCVCurrent24Hr_Object = MibTableColumn
cds3LCVCurrent24Hr = _Cds3LCVCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 1),
    _Cds3LCVCurrent24Hr_Type()
)
cds3LCVCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LCVCurrent24Hr.setStatus("current")
_Cds3LESCurrent24Hr_Type = Counter32
_Cds3LESCurrent24Hr_Object = MibTableColumn
cds3LESCurrent24Hr = _Cds3LESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 2),
    _Cds3LESCurrent24Hr_Type()
)
cds3LESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LESCurrent24Hr.setStatus("current")
_Cds3PCVCurrent24Hr_Type = Counter32
_Cds3PCVCurrent24Hr_Object = MibTableColumn
cds3PCVCurrent24Hr = _Cds3PCVCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 3),
    _Cds3PCVCurrent24Hr_Type()
)
cds3PCVCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PCVCurrent24Hr.setStatus("current")
_Cds3PESCurrent24Hr_Type = Counter32
_Cds3PESCurrent24Hr_Object = MibTableColumn
cds3PESCurrent24Hr = _Cds3PESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 4),
    _Cds3PESCurrent24Hr_Type()
)
cds3PESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PESCurrent24Hr.setStatus("current")
_Cds3PSESCurrent24Hr_Type = Counter32
_Cds3PSESCurrent24Hr_Object = MibTableColumn
cds3PSESCurrent24Hr = _Cds3PSESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 5),
    _Cds3PSESCurrent24Hr_Type()
)
cds3PSESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PSESCurrent24Hr.setStatus("current")
_Cds3SEFSCurrent24Hr_Type = Counter32
_Cds3SEFSCurrent24Hr_Object = MibTableColumn
cds3SEFSCurrent24Hr = _Cds3SEFSCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 6),
    _Cds3SEFSCurrent24Hr_Type()
)
cds3SEFSCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3SEFSCurrent24Hr.setStatus("current")
_Cds3UASCurrent24Hr_Type = Counter32
_Cds3UASCurrent24Hr_Object = MibTableColumn
cds3UASCurrent24Hr = _Cds3UASCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 7),
    _Cds3UASCurrent24Hr_Type()
)
cds3UASCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3UASCurrent24Hr.setStatus("current")
_Cds3CCVCurrent24Hr_Type = Counter32
_Cds3CCVCurrent24Hr_Object = MibTableColumn
cds3CCVCurrent24Hr = _Cds3CCVCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 8),
    _Cds3CCVCurrent24Hr_Type()
)
cds3CCVCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CCVCurrent24Hr.setStatus("current")
_Cds3CESCurrent24Hr_Type = Counter32
_Cds3CESCurrent24Hr_Object = MibTableColumn
cds3CESCurrent24Hr = _Cds3CESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 9),
    _Cds3CESCurrent24Hr_Type()
)
cds3CESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CESCurrent24Hr.setStatus("current")
_Cds3CSESCurrent24Hr_Type = Counter32
_Cds3CSESCurrent24Hr_Object = MibTableColumn
cds3CSESCurrent24Hr = _Cds3CSESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 10),
    _Cds3CSESCurrent24Hr_Type()
)
cds3CSESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CSESCurrent24Hr.setStatus("current")
_Cds3LSESCurrent24Hr_Type = Counter32
_Cds3LSESCurrent24Hr_Object = MibTableColumn
cds3LSESCurrent24Hr = _Cds3LSESCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 5, 1, 11),
    _Cds3LSESCurrent24Hr_Type()
)
cds3LSESCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LSESCurrent24Hr.setStatus("current")
_Cds3Previous24HrTable_Object = MibTable
cds3Previous24HrTable = _Cds3Previous24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cds3Previous24HrTable.setStatus("current")
_Cds3Previous24HrEntry_Object = MibTableRow
cds3Previous24HrEntry = _Cds3Previous24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1)
)
cds3Previous24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds3Previous24HrEntry.setStatus("current")
_Cds3LCVPrevious24Hr_Type = Counter32
_Cds3LCVPrevious24Hr_Object = MibTableColumn
cds3LCVPrevious24Hr = _Cds3LCVPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 1),
    _Cds3LCVPrevious24Hr_Type()
)
cds3LCVPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LCVPrevious24Hr.setStatus("current")
_Cds3LESPrevious24Hr_Type = Counter32
_Cds3LESPrevious24Hr_Object = MibTableColumn
cds3LESPrevious24Hr = _Cds3LESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 2),
    _Cds3LESPrevious24Hr_Type()
)
cds3LESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LESPrevious24Hr.setStatus("current")
_Cds3PCVPrevious24Hr_Type = Counter32
_Cds3PCVPrevious24Hr_Object = MibTableColumn
cds3PCVPrevious24Hr = _Cds3PCVPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 3),
    _Cds3PCVPrevious24Hr_Type()
)
cds3PCVPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PCVPrevious24Hr.setStatus("current")
_Cds3PESPrevious24Hr_Type = Counter32
_Cds3PESPrevious24Hr_Object = MibTableColumn
cds3PESPrevious24Hr = _Cds3PESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 4),
    _Cds3PESPrevious24Hr_Type()
)
cds3PESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PESPrevious24Hr.setStatus("current")
_Cds3PSESPrevious24Hr_Type = Counter32
_Cds3PSESPrevious24Hr_Object = MibTableColumn
cds3PSESPrevious24Hr = _Cds3PSESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 5),
    _Cds3PSESPrevious24Hr_Type()
)
cds3PSESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3PSESPrevious24Hr.setStatus("current")
_Cds3SEFSPrevious24Hr_Type = Counter32
_Cds3SEFSPrevious24Hr_Object = MibTableColumn
cds3SEFSPrevious24Hr = _Cds3SEFSPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 6),
    _Cds3SEFSPrevious24Hr_Type()
)
cds3SEFSPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3SEFSPrevious24Hr.setStatus("current")
_Cds3UASPrevious24Hr_Type = Counter32
_Cds3UASPrevious24Hr_Object = MibTableColumn
cds3UASPrevious24Hr = _Cds3UASPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 7),
    _Cds3UASPrevious24Hr_Type()
)
cds3UASPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3UASPrevious24Hr.setStatus("current")
_Cds3CCVPrevious24Hr_Type = Counter32
_Cds3CCVPrevious24Hr_Object = MibTableColumn
cds3CCVPrevious24Hr = _Cds3CCVPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 8),
    _Cds3CCVPrevious24Hr_Type()
)
cds3CCVPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CCVPrevious24Hr.setStatus("current")
_Cds3CESPrevious24Hr_Type = Counter32
_Cds3CESPrevious24Hr_Object = MibTableColumn
cds3CESPrevious24Hr = _Cds3CESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 9),
    _Cds3CESPrevious24Hr_Type()
)
cds3CESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CESPrevious24Hr.setStatus("current")
_Cds3CSESPrevious24Hr_Type = Counter32
_Cds3CSESPrevious24Hr_Object = MibTableColumn
cds3CSESPrevious24Hr = _Cds3CSESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 10),
    _Cds3CSESPrevious24Hr_Type()
)
cds3CSESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3CSESPrevious24Hr.setStatus("current")
_Cds3LSESPrevious24Hr_Type = Counter32
_Cds3LSESPrevious24Hr_Object = MibTableColumn
cds3LSESPrevious24Hr = _Cds3LSESPrevious24Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 1, 3, 6, 1, 11),
    _Cds3LSESPrevious24Hr_Type()
)
cds3LSESPrevious24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds3LSESPrevious24Hr.setStatus("current")
_CiscoDs3MIBConformance_ObjectIdentity = ObjectIdentity
ciscoDs3MIBConformance = _CiscoDs3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8)
)
_CiscoDs3MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDs3MIBCompliances = _CiscoDs3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 1)
)
_CiscoDs3MIBGroups_ObjectIdentity = ObjectIdentity
ciscoDs3MIBGroups = _CiscoDs3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2)
)

# Managed Objects groups

ciscoDs3ConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 1)
)
ciscoDs3ConfMIBGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3LineType"),
        ("CISCO-DS3-MIB", "cds3LineAIScBitsCheck"),
        ("CISCO-DS3-MIB", "cds3LineRcvFEACValidation"),
        ("CISCO-DS3-MIB", "cds3LineOOFCriteria"),
        ("CISCO-DS3-MIB", "cds3TraceToTransmit"),
        ("CISCO-DS3-MIB", "cds3TraceToExpect"),
        ("CISCO-DS3-MIB", "cds3TraceAlarm"),
        ("CISCO-DS3-MIB", "cds3InternalEqualizer"),
        ("CISCO-DS3-MIB", "cds3NearEndLineLoopbackStatus"),
        ("CISCO-DS3-MIB", "cds3FarEndLineLoopbackStatus"))
)
if mibBuilder.loadTexts:
    ciscoDs3ConfMIBGroup.setStatus("current")

cds3StatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 2)
)
cds3StatsMIBGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3RcvLOSCount"),
        ("CISCO-DS3-MIB", "cds3RcvOOFCount"),
        ("CISCO-DS3-MIB", "cds3RAICount"),
        ("CISCO-DS3-MIB", "cds3CCVCount"),
        ("CISCO-DS3-MIB", "cds3FECount"),
        ("CISCO-DS3-MIB", "cds3EXZSCount"),
        ("CISCO-DS3-MIB", "cds3LCVCount"),
        ("CISCO-DS3-MIB", "cds3PCVCount"),
        ("CISCO-DS3-MIB", "cds3CPECount"),
        ("CISCO-DS3-MIB", "cds3FEBECount"),
        ("CISCO-DS3-MIB", "cds3RcvAISCount"))
)
if mibBuilder.loadTexts:
    cds3StatsMIBGroup.setStatus("current")

ciscoDs3AlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 3)
)
ciscoDs3AlarmMIBGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3NEAlarmUpCount"),
        ("CISCO-DS3-MIB", "cds3NEAlarmDownCount"),
        ("CISCO-DS3-MIB", "cds3NEAlarmThreshold"),
        ("CISCO-DS3-MIB", "cds3FEAlarmUpCount"),
        ("CISCO-DS3-MIB", "cds3FEAlarmDownCount"),
        ("CISCO-DS3-MIB", "cds3FEAlarmThreshold"),
        ("CISCO-DS3-MIB", "cds3StatisticalAlarmSeverity"),
        ("CISCO-DS3-MIB", "cds3LCV15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3LCV24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3LES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3LES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PCV15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PCV24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PSES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PSES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3SEFS15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3SEFS24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3UAS15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3UAS24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3CCV15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3CCV24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3CES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3CES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3CSES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3CSES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3LSES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3LSES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3LineStatisticalAlarmState"),
        ("CISCO-DS3-MIB", "cds3IntervalNumber"),
        ("CISCO-DS3-MIB", "cds3IntervalLSESs"),
        ("CISCO-DS3-MIB", "cds3LCVCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3LESCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3PCVCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3PESCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3PSESCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3SEFSCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3UASCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3CCVCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3CESCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3CSESCurrent24Hr"),
        ("CISCO-DS3-MIB", "cds3LSESCurrent24Hr"))
)
if mibBuilder.loadTexts:
    ciscoDs3AlarmMIBGroup.setStatus("current")

ciscoPlcpCounterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 4)
)
ciscoPlcpCounterMIBGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3PlcpRcvBip8Count"),
        ("CISCO-DS3-MIB", "cds3PlcpRcvOOFCount"),
        ("CISCO-DS3-MIB", "cds3PlcpRcvRAICount"),
        ("CISCO-DS3-MIB", "cds3PlcpFECount"),
        ("CISCO-DS3-MIB", "cds3PlcpFESecCount"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFSecCount"),
        ("CISCO-DS3-MIB", "cds3PlcpFEBECount"),
        ("CISCO-DS3-MIB", "cds3PlcpFEBESecCount"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFEBESecCount"))
)
if mibBuilder.loadTexts:
    ciscoPlcpCounterMIBGroup.setStatus("current")

ciscoPlcpAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 5)
)
ciscoPlcpAlarmMIBGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3PlcpStatisticalAlarmSeverity"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8CV15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8CV24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8ES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8ES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8SES15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8SES24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFS15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFS24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpUAS15MinThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpUAS24HrThreshold"),
        ("CISCO-DS3-MIB", "cds3PlcpLineAlarmState"),
        ("CISCO-DS3-MIB", "cds3PlcpLineStatisticalAlarmState"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8CVCurrent"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8CV24HrBucket"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8ESCurrent"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8ES24HrBucket"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8SESCurrent"),
        ("CISCO-DS3-MIB", "cds3PlcpBip8SES24HrBucket"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFSCurrent"),
        ("CISCO-DS3-MIB", "cds3PlcpSEFS24HrBucket"),
        ("CISCO-DS3-MIB", "cds3PlcpUASCurrent"),
        ("CISCO-DS3-MIB", "cds3PlcpUAS24HrBucket"))
)
if mibBuilder.loadTexts:
    ciscoPlcpAlarmMIBGroup.setStatus("current")

ciscoDs3Previous24HrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 2, 6)
)
ciscoDs3Previous24HrGroup.setObjects(
      *(("CISCO-DS3-MIB", "cds3LCVPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3LESPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3PCVPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3PESPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3PSESPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3SEFSPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3UASPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3CCVPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3CESPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3CSESPrevious24Hr"),
        ("CISCO-DS3-MIB", "cds3LSESPrevious24Hr"))
)
if mibBuilder.loadTexts:
    ciscoDs3Previous24HrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDs3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 132, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDs3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS3-MIB",
    **{"ciscoDs3MIB": ciscoDs3MIB,
       "ciscoDs3MIBObjects": ciscoDs3MIBObjects,
       "cds3Config": cds3Config,
       "cds3ConfigTable": cds3ConfigTable,
       "cds3ConfigEntry": cds3ConfigEntry,
       "cds3LineType": cds3LineType,
       "cds3LineAIScBitsCheck": cds3LineAIScBitsCheck,
       "cds3LineRcvFEACValidation": cds3LineRcvFEACValidation,
       "cds3LineOOFCriteria": cds3LineOOFCriteria,
       "cds3TraceToTransmit": cds3TraceToTransmit,
       "cds3TraceToExpect": cds3TraceToExpect,
       "cds3TraceAlarm": cds3TraceAlarm,
       "cds3InternalEqualizer": cds3InternalEqualizer,
       "cds3NearEndLineLoopbackStatus": cds3NearEndLineLoopbackStatus,
       "cds3FarEndLineLoopbackStatus": cds3FarEndLineLoopbackStatus,
       "cds3Alarm": cds3Alarm,
       "cds3AlarmConfig": cds3AlarmConfig,
       "cds3AlarmConfigTable": cds3AlarmConfigTable,
       "cds3AlarmConfigEntry": cds3AlarmConfigEntry,
       "cds3NEAlarmUpCount": cds3NEAlarmUpCount,
       "cds3NEAlarmDownCount": cds3NEAlarmDownCount,
       "cds3NEAlarmThreshold": cds3NEAlarmThreshold,
       "cds3FEAlarmUpCount": cds3FEAlarmUpCount,
       "cds3FEAlarmDownCount": cds3FEAlarmDownCount,
       "cds3FEAlarmThreshold": cds3FEAlarmThreshold,
       "cds3StatisticalAlarmSeverity": cds3StatisticalAlarmSeverity,
       "cds3LCV15MinThreshold": cds3LCV15MinThreshold,
       "cds3LCV24HrThreshold": cds3LCV24HrThreshold,
       "cds3LES15MinThreshold": cds3LES15MinThreshold,
       "cds3LES24HrThreshold": cds3LES24HrThreshold,
       "cds3PCV15MinThreshold": cds3PCV15MinThreshold,
       "cds3PCV24HrThreshold": cds3PCV24HrThreshold,
       "cds3PES15MinThreshold": cds3PES15MinThreshold,
       "cds3PES24HrThreshold": cds3PES24HrThreshold,
       "cds3PSES15MinThreshold": cds3PSES15MinThreshold,
       "cds3PSES24HrThreshold": cds3PSES24HrThreshold,
       "cds3SEFS15MinThreshold": cds3SEFS15MinThreshold,
       "cds3SEFS24HrThreshold": cds3SEFS24HrThreshold,
       "cds3UAS15MinThreshold": cds3UAS15MinThreshold,
       "cds3UAS24HrThreshold": cds3UAS24HrThreshold,
       "cds3CCV15MinThreshold": cds3CCV15MinThreshold,
       "cds3CCV24HrThreshold": cds3CCV24HrThreshold,
       "cds3CES15MinThreshold": cds3CES15MinThreshold,
       "cds3CES24HrThreshold": cds3CES24HrThreshold,
       "cds3CSES15MinThreshold": cds3CSES15MinThreshold,
       "cds3CSES24HrThreshold": cds3CSES24HrThreshold,
       "cds3LSES15MinThreshold": cds3LSES15MinThreshold,
       "cds3LSES24HrThreshold": cds3LSES24HrThreshold,
       "cds3LineStatisticalAlarmState": cds3LineStatisticalAlarmState,
       "cds3AlarmConfigPlcpTable": cds3AlarmConfigPlcpTable,
       "cds3AlarmConfigPlcpEntry": cds3AlarmConfigPlcpEntry,
       "cds3PlcpStatisticalAlarmSeverity": cds3PlcpStatisticalAlarmSeverity,
       "cds3PlcpBip8CV15MinThreshold": cds3PlcpBip8CV15MinThreshold,
       "cds3PlcpBip8CV24HrThreshold": cds3PlcpBip8CV24HrThreshold,
       "cds3PlcpBip8ES15MinThreshold": cds3PlcpBip8ES15MinThreshold,
       "cds3PlcpBip8ES24HrThreshold": cds3PlcpBip8ES24HrThreshold,
       "cds3PlcpBip8SES15MinThreshold": cds3PlcpBip8SES15MinThreshold,
       "cds3PlcpBip8SES24HrThreshold": cds3PlcpBip8SES24HrThreshold,
       "cds3PlcpSEFS15MinThreshold": cds3PlcpSEFS15MinThreshold,
       "cds3PlcpSEFS24HrThreshold": cds3PlcpSEFS24HrThreshold,
       "cds3PlcpUAS15MinThreshold": cds3PlcpUAS15MinThreshold,
       "cds3PlcpUAS24HrThreshold": cds3PlcpUAS24HrThreshold,
       "cds3AlarmPlcpTable": cds3AlarmPlcpTable,
       "cds3AlarmPlcpEntry": cds3AlarmPlcpEntry,
       "cds3PlcpLineAlarmState": cds3PlcpLineAlarmState,
       "cds3PlcpLineStatisticalAlarmState": cds3PlcpLineStatisticalAlarmState,
       "cds3PlcpBip8CVCurrent": cds3PlcpBip8CVCurrent,
       "cds3PlcpBip8CV24HrBucket": cds3PlcpBip8CV24HrBucket,
       "cds3PlcpBip8ESCurrent": cds3PlcpBip8ESCurrent,
       "cds3PlcpBip8ES24HrBucket": cds3PlcpBip8ES24HrBucket,
       "cds3PlcpBip8SESCurrent": cds3PlcpBip8SESCurrent,
       "cds3PlcpBip8SES24HrBucket": cds3PlcpBip8SES24HrBucket,
       "cds3PlcpSEFSCurrent": cds3PlcpSEFSCurrent,
       "cds3PlcpSEFS24HrBucket": cds3PlcpSEFS24HrBucket,
       "cds3PlcpUASCurrent": cds3PlcpUASCurrent,
       "cds3PlcpUAS24HrBucket": cds3PlcpUAS24HrBucket,
       "cds3Stats": cds3Stats,
       "cds3StatsTable": cds3StatsTable,
       "cds3StatsEntry": cds3StatsEntry,
       "cds3RcvLOSCount": cds3RcvLOSCount,
       "cds3RcvOOFCount": cds3RcvOOFCount,
       "cds3RAICount": cds3RAICount,
       "cds3CCVCount": cds3CCVCount,
       "cds3FECount": cds3FECount,
       "cds3EXZSCount": cds3EXZSCount,
       "cds3LCVCount": cds3LCVCount,
       "cds3PCVCount": cds3PCVCount,
       "cds3CPECount": cds3CPECount,
       "cds3FEBECount": cds3FEBECount,
       "cds3RcvAISCount": cds3RcvAISCount,
       "cds3PlcpStatsTable": cds3PlcpStatsTable,
       "cds3PlcpStatsEntry": cds3PlcpStatsEntry,
       "cds3PlcpRcvBip8Count": cds3PlcpRcvBip8Count,
       "cds3PlcpRcvOOFCount": cds3PlcpRcvOOFCount,
       "cds3PlcpRcvRAICount": cds3PlcpRcvRAICount,
       "cds3PlcpFECount": cds3PlcpFECount,
       "cds3PlcpFESecCount": cds3PlcpFESecCount,
       "cds3PlcpSEFSecCount": cds3PlcpSEFSecCount,
       "cds3PlcpFEBECount": cds3PlcpFEBECount,
       "cds3PlcpFEBESecCount": cds3PlcpFEBESecCount,
       "cds3PlcpSEFEBESecCount": cds3PlcpSEFEBESecCount,
       "cds3IntervalTable": cds3IntervalTable,
       "cds3IntervalEntry": cds3IntervalEntry,
       "cds3IntervalNumber": cds3IntervalNumber,
       "cds3IntervalLSESs": cds3IntervalLSESs,
       "cds3Current24HrTable": cds3Current24HrTable,
       "cds3Current24HrEntry": cds3Current24HrEntry,
       "cds3LCVCurrent24Hr": cds3LCVCurrent24Hr,
       "cds3LESCurrent24Hr": cds3LESCurrent24Hr,
       "cds3PCVCurrent24Hr": cds3PCVCurrent24Hr,
       "cds3PESCurrent24Hr": cds3PESCurrent24Hr,
       "cds3PSESCurrent24Hr": cds3PSESCurrent24Hr,
       "cds3SEFSCurrent24Hr": cds3SEFSCurrent24Hr,
       "cds3UASCurrent24Hr": cds3UASCurrent24Hr,
       "cds3CCVCurrent24Hr": cds3CCVCurrent24Hr,
       "cds3CESCurrent24Hr": cds3CESCurrent24Hr,
       "cds3CSESCurrent24Hr": cds3CSESCurrent24Hr,
       "cds3LSESCurrent24Hr": cds3LSESCurrent24Hr,
       "cds3Previous24HrTable": cds3Previous24HrTable,
       "cds3Previous24HrEntry": cds3Previous24HrEntry,
       "cds3LCVPrevious24Hr": cds3LCVPrevious24Hr,
       "cds3LESPrevious24Hr": cds3LESPrevious24Hr,
       "cds3PCVPrevious24Hr": cds3PCVPrevious24Hr,
       "cds3PESPrevious24Hr": cds3PESPrevious24Hr,
       "cds3PSESPrevious24Hr": cds3PSESPrevious24Hr,
       "cds3SEFSPrevious24Hr": cds3SEFSPrevious24Hr,
       "cds3UASPrevious24Hr": cds3UASPrevious24Hr,
       "cds3CCVPrevious24Hr": cds3CCVPrevious24Hr,
       "cds3CESPrevious24Hr": cds3CESPrevious24Hr,
       "cds3CSESPrevious24Hr": cds3CSESPrevious24Hr,
       "cds3LSESPrevious24Hr": cds3LSESPrevious24Hr,
       "ciscoDs3MIBConformance": ciscoDs3MIBConformance,
       "ciscoDs3MIBCompliances": ciscoDs3MIBCompliances,
       "ciscoDs3MIBCompliance": ciscoDs3MIBCompliance,
       "ciscoDs3MIBGroups": ciscoDs3MIBGroups,
       "ciscoDs3ConfMIBGroup": ciscoDs3ConfMIBGroup,
       "cds3StatsMIBGroup": cds3StatsMIBGroup,
       "ciscoDs3AlarmMIBGroup": ciscoDs3AlarmMIBGroup,
       "ciscoPlcpCounterMIBGroup": ciscoPlcpCounterMIBGroup,
       "ciscoPlcpAlarmMIBGroup": ciscoPlcpAlarmMIBGroup,
       "ciscoDs3Previous24HrGroup": ciscoDs3Previous24HrGroup}
)
