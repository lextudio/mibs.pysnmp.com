# SNMP MIB module (CISCO-MGX82XX-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:33 2024
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

(basisAsm,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "basisAsm")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxEnvmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 70)
)
ciscoMgx82xxEnvmonMIB.setRevisions(
        ("2003-04-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsmAlarmTable_Object = MibTable
asmAlarmTable = _AsmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    asmAlarmTable.setStatus("current")
_AsmAlarmEntry_Object = MibTableRow
asmAlarmEntry = _AsmAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1)
)
asmAlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-ENVMON-MIB", "asmAlarmNum"),
)
if mibBuilder.loadTexts:
    asmAlarmEntry.setStatus("current")


class _AsmAlarmNum_Type(Integer32):
    """Custom type asmAlarmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsmAlarmNum_Type.__name__ = "Integer32"
_AsmAlarmNum_Object = MibTableColumn
asmAlarmNum = _AsmAlarmNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 1),
    _AsmAlarmNum_Type()
)
asmAlarmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmAlarmNum.setStatus("current")


class _AsmAlarmType_Type(Integer32):
    """Custom type asmAlarmType based on Integer32"""
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
        *(("alarmDCLevel", 4),
          ("alarmFanUnit", 5),
          ("alarmOther", 1),
          ("alarmPSU", 3),
          ("alarmTemperature", 2))
    )


_AsmAlarmType_Type.__name__ = "Integer32"
_AsmAlarmType_Object = MibTableColumn
asmAlarmType = _AsmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 2),
    _AsmAlarmType_Type()
)
asmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmAlarmType.setStatus("current")


class _AsmAlarmUnitNum_Type(Integer32):
    """Custom type asmAlarmUnitNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AsmAlarmUnitNum_Type.__name__ = "Integer32"
_AsmAlarmUnitNum_Object = MibTableColumn
asmAlarmUnitNum = _AsmAlarmUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 3),
    _AsmAlarmUnitNum_Type()
)
asmAlarmUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmAlarmUnitNum.setStatus("current")


class _AsmAlarmThreshold_Type(Integer32):
    """Custom type asmAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AsmAlarmThreshold_Type.__name__ = "Integer32"
_AsmAlarmThreshold_Object = MibTableColumn
asmAlarmThreshold = _AsmAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 4),
    _AsmAlarmThreshold_Type()
)
asmAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmAlarmThreshold.setStatus("current")


class _AsmAlarmSeverity_Type(Integer32):
    """Custom type asmAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmMajor", 2),
          ("alarmMinor", 1))
    )


_AsmAlarmSeverity_Type.__name__ = "Integer32"
_AsmAlarmSeverity_Object = MibTableColumn
asmAlarmSeverity = _AsmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 5),
    _AsmAlarmSeverity_Type()
)
asmAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmAlarmSeverity.setStatus("current")


class _AsmUnitMeasurable_Type(Integer32):
    """Custom type asmUnitMeasurable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AsmUnitMeasurable_Type.__name__ = "Integer32"
_AsmUnitMeasurable_Object = MibTableColumn
asmUnitMeasurable = _AsmUnitMeasurable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 6),
    _AsmUnitMeasurable_Type()
)
asmUnitMeasurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmUnitMeasurable.setStatus("current")


class _AsmUnitMeasuredValue_Type(Integer32):
    """Custom type asmUnitMeasuredValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AsmUnitMeasuredValue_Type.__name__ = "Integer32"
_AsmUnitMeasuredValue_Object = MibTableColumn
asmUnitMeasuredValue = _AsmUnitMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 7),
    _AsmUnitMeasuredValue_Type()
)
asmUnitMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmUnitMeasuredValue.setStatus("current")


class _AsmPhysicalAlarmState_Type(Integer32):
    """Custom type asmPhysicalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AsmPhysicalAlarmState_Type.__name__ = "Integer32"
_AsmPhysicalAlarmState_Object = MibTableColumn
asmPhysicalAlarmState = _AsmPhysicalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 8),
    _AsmPhysicalAlarmState_Type()
)
asmPhysicalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmPhysicalAlarmState.setStatus("current")


class _AsmClrButton_Type(Integer32):
    """Custom type asmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asmAlarmClear", 2),
          ("asmAlarmNoAction", 1))
    )


_AsmClrButton_Type.__name__ = "Integer32"
_AsmClrButton_Object = MibTableColumn
asmClrButton = _AsmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 1, 1, 9),
    _AsmClrButton_Type()
)
asmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asmClrButton.setStatus("current")


class _AsmNumOfValidEntries_Type(Integer32):
    """Custom type asmNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AsmNumOfValidEntries_Type.__name__ = "Integer32"
_AsmNumOfValidEntries_Object = MibScalar
asmNumOfValidEntries = _AsmNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 2),
    _AsmNumOfValidEntries_Type()
)
asmNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmNumOfValidEntries.setStatus("current")


class _AsmShelfAlarmState_Type(Integer32):
    """Custom type asmShelfAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmOff", 1),
          ("alarmOn", 2))
    )


_AsmShelfAlarmState_Type.__name__ = "Integer32"
_AsmShelfAlarmState_Object = MibScalar
asmShelfAlarmState = _AsmShelfAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2, 3),
    _AsmShelfAlarmState_Type()
)
asmShelfAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmShelfAlarmState.setStatus("current")
_CmEnvmonMIBConformance_ObjectIdentity = ObjectIdentity
cmEnvmonMIBConformance = _CmEnvmonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2)
)
_CmEnvmonMIBGroups_ObjectIdentity = ObjectIdentity
cmEnvmonMIBGroups = _CmEnvmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2, 1)
)
_CmEnvmonMIBCompliances_ObjectIdentity = ObjectIdentity
cmEnvmonMIBCompliances = _CmEnvmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2, 2)
)

# Managed Objects groups

cmEnvmonInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2, 1, 1)
)
cmEnvmonInfoGroup.setObjects(
      *(("CISCO-MGX82XX-ENVMON-MIB", "asmAlarmNum"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmAlarmType"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmAlarmUnitNum"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmAlarmThreshold"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmAlarmSeverity"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmUnitMeasurable"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmUnitMeasuredValue"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmPhysicalAlarmState"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmClrButton"))
)
if mibBuilder.loadTexts:
    cmEnvmonInfoGroup.setStatus("current")

cmEnvmonGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2, 1, 2)
)
cmEnvmonGeneralGroup.setObjects(
      *(("CISCO-MGX82XX-ENVMON-MIB", "asmNumOfValidEntries"),
        ("CISCO-MGX82XX-ENVMON-MIB", "asmShelfAlarmState"))
)
if mibBuilder.loadTexts:
    cmEnvmonGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmEnvmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 70, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmEnvmonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-ENVMON-MIB",
    **{"asmAlarmTable": asmAlarmTable,
       "asmAlarmEntry": asmAlarmEntry,
       "asmAlarmNum": asmAlarmNum,
       "asmAlarmType": asmAlarmType,
       "asmAlarmUnitNum": asmAlarmUnitNum,
       "asmAlarmThreshold": asmAlarmThreshold,
       "asmAlarmSeverity": asmAlarmSeverity,
       "asmUnitMeasurable": asmUnitMeasurable,
       "asmUnitMeasuredValue": asmUnitMeasuredValue,
       "asmPhysicalAlarmState": asmPhysicalAlarmState,
       "asmClrButton": asmClrButton,
       "asmNumOfValidEntries": asmNumOfValidEntries,
       "asmShelfAlarmState": asmShelfAlarmState,
       "ciscoMgx82xxEnvmonMIB": ciscoMgx82xxEnvmonMIB,
       "cmEnvmonMIBConformance": cmEnvmonMIBConformance,
       "cmEnvmonMIBGroups": cmEnvmonMIBGroups,
       "cmEnvmonInfoGroup": cmEnvmonInfoGroup,
       "cmEnvmonGeneralGroup": cmEnvmonGeneralGroup,
       "cmEnvmonMIBCompliances": cmEnvmonMIBCompliances,
       "cmEnvmonCompliance": cmEnvmonCompliance}
)
