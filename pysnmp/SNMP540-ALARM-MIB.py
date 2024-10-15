# SNMP MIB module (SNMP540-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP540-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:12 2024
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

(snmp540,) = mibBuilder.importSymbols(
    "SNMP540-MGMT-MIB",
    "snmp540")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snmp540Alarm_ObjectIdentity = ObjectIdentity
snmp540Alarm = _Snmp540Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10)
)


class _Snmp540AlarmMIBversion_Type(DisplayString):
    """Custom type snmp540AlarmMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Snmp540AlarmMIBversion_Type.__name__ = "DisplayString"
_Snmp540AlarmMIBversion_Object = MibScalar
snmp540AlarmMIBversion = _Snmp540AlarmMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 1),
    _Snmp540AlarmMIBversion_Type()
)
snmp540AlarmMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540AlarmMIBversion.setStatus("mandatory")


class _Snmp540AlarmStructure_Type(Integer32):
    """Custom type snmp540AlarmStructure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gdcProprietarySCMStandard", 1),
          ("generalAlarmStructure", 2))
    )


_Snmp540AlarmStructure_Type.__name__ = "Integer32"
_Snmp540AlarmStructure_Object = MibScalar
snmp540AlarmStructure = _Snmp540AlarmStructure_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 2),
    _Snmp540AlarmStructure_Type()
)
snmp540AlarmStructure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540AlarmStructure.setStatus("mandatory")
_Snmp540AlarmNumber_Type = Integer32
_Snmp540AlarmNumber_Object = MibScalar
snmp540AlarmNumber = _Snmp540AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 3),
    _Snmp540AlarmNumber_Type()
)
snmp540AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540AlarmNumber.setStatus("mandatory")


class _Snmp540GeneralIntegrationTime_Type(Integer32):
    """Custom type snmp540GeneralIntegrationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Snmp540GeneralIntegrationTime_Type.__name__ = "Integer32"
_Snmp540GeneralIntegrationTime_Object = MibScalar
snmp540GeneralIntegrationTime = _Snmp540GeneralIntegrationTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 4),
    _Snmp540GeneralIntegrationTime_Type()
)
snmp540GeneralIntegrationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540GeneralIntegrationTime.setStatus("mandatory")
_Snmp540AlarmTable_Object = MibTable
snmp540AlarmTable = _Snmp540AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5)
)
if mibBuilder.loadTexts:
    snmp540AlarmTable.setStatus("mandatory")
_Snmp540AlarmEntry_Object = MibTableRow
snmp540AlarmEntry = _Snmp540AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1)
)
snmp540AlarmEntry.setIndexNames(
    (0, "SNMP540-ALARM-MIB", "alarmNumber"),
)
if mibBuilder.loadTexts:
    snmp540AlarmEntry.setStatus("mandatory")
_AlarmNumber_Type = Integer32
_AlarmNumber_Object = MibTableColumn
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("mandatory")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")


class _SeverityLevel_Type(Integer32):
    """Custom type severityLevel based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_SeverityLevel_Type.__name__ = "Integer32"
_SeverityLevel_Object = MibTableColumn
severityLevel = _SeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 3),
    _SeverityLevel_Type()
)
severityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityLevel.setStatus("mandatory")


class __pysmi_class_Type(Integer32):
    """Custom type _pysmi_class based on Integer32"""
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
        *(("countWindow", 3),
          ("general", 1),
          ("threshold", 2),
          ("thresholdInterval", 4))
    )


__pysmi_class_Type.__name__ = "Integer32"
__pysmi_class_Object = MibScalar
_pysmi_class = __pysmi_class_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 4),
    __pysmi_class_Type()
)
_pysmi_class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    _pysmi_class.setStatus("mandatory")


class _Mask_Type(Integer32):
    """Custom type mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_Mask_Type.__name__ = "Integer32"
_Mask_Object = MibTableColumn
mask = _Mask_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 5),
    _Mask_Type()
)
mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mask.setStatus("mandatory")


class _Threshold_Type(Integer32):
    """Custom type threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 99),
    )


_Threshold_Type.__name__ = "Integer32"
_Threshold_Object = MibTableColumn
threshold = _Threshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 6),
    _Threshold_Type()
)
threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshold.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 7),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")

# Managed Objects groups


# Notification objects

snmp540AlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 0, 1)
)
snmp540AlarmTrap.setObjects(
      *(("SNMP540-ALARM-MIB", "description"),
        ("SNMP540-ALARM-MIB", "severityLevel"),
        ("SNMP540-ALARM-MIB", "status"))
)
if mibBuilder.loadTexts:
    snmp540AlarmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP540-ALARM-MIB",
    **{"snmp540AlarmTrap": snmp540AlarmTrap,
       "snmp540Alarm": snmp540Alarm,
       "snmp540AlarmMIBversion": snmp540AlarmMIBversion,
       "snmp540AlarmStructure": snmp540AlarmStructure,
       "snmp540AlarmNumber": snmp540AlarmNumber,
       "snmp540GeneralIntegrationTime": snmp540GeneralIntegrationTime,
       "snmp540AlarmTable": snmp540AlarmTable,
       "snmp540AlarmEntry": snmp540AlarmEntry,
       "alarmNumber": alarmNumber,
       "description": description,
       "severityLevel": severityLevel,
       "class": _pysmi_class,
       "mask": mask,
       "threshold": threshold,
       "status": status}
)
