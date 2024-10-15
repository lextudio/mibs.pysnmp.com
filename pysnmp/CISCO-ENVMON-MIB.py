# SNMP MIB module (CISCO-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:28 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13)
)
ciscoEnvMonMIB.setRevisions(
        ("2003-12-01 00:00",
         "2003-11-25 00:00",
         "2002-10-15 00:00",
         "2002-07-17 00:00",
         "2002-02-04 00:00",
         "2001-08-30 00:00",
         "2001-08-16 00:00",
         "2001-05-07 00:00",
         "2000-01-31 00:00",
         "1998-10-22 00:00",
         "1998-08-05 00:00",
         "1996-11-12 00:00",
         "1995-08-15 00:00",
         "1995-03-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoEnvMonState(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 3),
          ("normal", 1),
          ("notFunctioning", 6),
          ("notPresent", 5),
          ("shutdown", 4),
          ("warning", 2))
    )



class CiscoSignedGauge(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoEnvMonObjects_ObjectIdentity = ObjectIdentity
ciscoEnvMonObjects = _CiscoEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1)
)


class _CiscoEnvMonPresent_Type(Integer32):
    """Custom type ciscoEnvMonPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ags", 2),
          ("c10000", 10),
          ("c37xx", 13),
          ("c7000", 3),
          ("c7600", 12),
          ("cAccessMon", 6),
          ("cat4000", 9),
          ("cat6000", 7),
          ("ci", 4),
          ("oldAgs", 1),
          ("osr7600", 11),
          ("other", 14),
          ("ubr7200", 8))
    )


_CiscoEnvMonPresent_Type.__name__ = "Integer32"
_CiscoEnvMonPresent_Object = MibScalar
ciscoEnvMonPresent = _CiscoEnvMonPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 1),
    _CiscoEnvMonPresent_Type()
)
ciscoEnvMonPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonPresent.setStatus("current")
_CiscoEnvMonVoltageStatusTable_Object = MibTable
ciscoEnvMonVoltageStatusTable = _CiscoEnvMonVoltageStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusTable.setStatus("current")
_CiscoEnvMonVoltageStatusEntry_Object = MibTableRow
ciscoEnvMonVoltageStatusEntry = _CiscoEnvMonVoltageStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1)
)
ciscoEnvMonVoltageStatusEntry.setIndexNames(
    (0, "CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusIndex"),
)
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusEntry.setStatus("current")


class _CiscoEnvMonVoltageStatusIndex_Type(Integer32):
    """Custom type ciscoEnvMonVoltageStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoEnvMonVoltageStatusIndex_Type.__name__ = "Integer32"
_CiscoEnvMonVoltageStatusIndex_Object = MibTableColumn
ciscoEnvMonVoltageStatusIndex = _CiscoEnvMonVoltageStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 1),
    _CiscoEnvMonVoltageStatusIndex_Type()
)
ciscoEnvMonVoltageStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusIndex.setStatus("current")


class _CiscoEnvMonVoltageStatusDescr_Type(DisplayString):
    """Custom type ciscoEnvMonVoltageStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoEnvMonVoltageStatusDescr_Type.__name__ = "DisplayString"
_CiscoEnvMonVoltageStatusDescr_Object = MibTableColumn
ciscoEnvMonVoltageStatusDescr = _CiscoEnvMonVoltageStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 2),
    _CiscoEnvMonVoltageStatusDescr_Type()
)
ciscoEnvMonVoltageStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusDescr.setStatus("current")
_CiscoEnvMonVoltageStatusValue_Type = CiscoSignedGauge
_CiscoEnvMonVoltageStatusValue_Object = MibTableColumn
ciscoEnvMonVoltageStatusValue = _CiscoEnvMonVoltageStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 3),
    _CiscoEnvMonVoltageStatusValue_Type()
)
ciscoEnvMonVoltageStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusValue.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageStatusValue.setUnits("millivolts")
_CiscoEnvMonVoltageThresholdLow_Type = Integer32
_CiscoEnvMonVoltageThresholdLow_Object = MibTableColumn
ciscoEnvMonVoltageThresholdLow = _CiscoEnvMonVoltageThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 4),
    _CiscoEnvMonVoltageThresholdLow_Type()
)
ciscoEnvMonVoltageThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageThresholdLow.setUnits("millivolts")
_CiscoEnvMonVoltageThresholdHigh_Type = Integer32
_CiscoEnvMonVoltageThresholdHigh_Object = MibTableColumn
ciscoEnvMonVoltageThresholdHigh = _CiscoEnvMonVoltageThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 5),
    _CiscoEnvMonVoltageThresholdHigh_Type()
)
ciscoEnvMonVoltageThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageThresholdHigh.setUnits("millivolts")
_CiscoEnvMonVoltageLastShutdown_Type = Integer32
_CiscoEnvMonVoltageLastShutdown_Object = MibTableColumn
ciscoEnvMonVoltageLastShutdown = _CiscoEnvMonVoltageLastShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 6),
    _CiscoEnvMonVoltageLastShutdown_Type()
)
ciscoEnvMonVoltageLastShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageLastShutdown.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageLastShutdown.setUnits("millivolts")
_CiscoEnvMonVoltageState_Type = CiscoEnvMonState
_CiscoEnvMonVoltageState_Object = MibTableColumn
ciscoEnvMonVoltageState = _CiscoEnvMonVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 7),
    _CiscoEnvMonVoltageState_Type()
)
ciscoEnvMonVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageState.setStatus("current")
_CiscoEnvMonTemperatureStatusTable_Object = MibTable
ciscoEnvMonTemperatureStatusTable = _CiscoEnvMonTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusTable.setStatus("current")
_CiscoEnvMonTemperatureStatusEntry_Object = MibTableRow
ciscoEnvMonTemperatureStatusEntry = _CiscoEnvMonTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1)
)
ciscoEnvMonTemperatureStatusEntry.setIndexNames(
    (0, "CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusEntry.setStatus("current")


class _CiscoEnvMonTemperatureStatusIndex_Type(Integer32):
    """Custom type ciscoEnvMonTemperatureStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoEnvMonTemperatureStatusIndex_Type.__name__ = "Integer32"
_CiscoEnvMonTemperatureStatusIndex_Object = MibTableColumn
ciscoEnvMonTemperatureStatusIndex = _CiscoEnvMonTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 1),
    _CiscoEnvMonTemperatureStatusIndex_Type()
)
ciscoEnvMonTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusIndex.setStatus("current")


class _CiscoEnvMonTemperatureStatusDescr_Type(DisplayString):
    """Custom type ciscoEnvMonTemperatureStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoEnvMonTemperatureStatusDescr_Type.__name__ = "DisplayString"
_CiscoEnvMonTemperatureStatusDescr_Object = MibTableColumn
ciscoEnvMonTemperatureStatusDescr = _CiscoEnvMonTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 2),
    _CiscoEnvMonTemperatureStatusDescr_Type()
)
ciscoEnvMonTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusDescr.setStatus("current")
_CiscoEnvMonTemperatureStatusValue_Type = Gauge32
_CiscoEnvMonTemperatureStatusValue_Object = MibTableColumn
ciscoEnvMonTemperatureStatusValue = _CiscoEnvMonTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 3),
    _CiscoEnvMonTemperatureStatusValue_Type()
)
ciscoEnvMonTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusValue.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureStatusValue.setUnits("degrees Celsius")
_CiscoEnvMonTemperatureThreshold_Type = Integer32
_CiscoEnvMonTemperatureThreshold_Object = MibTableColumn
ciscoEnvMonTemperatureThreshold = _CiscoEnvMonTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 4),
    _CiscoEnvMonTemperatureThreshold_Type()
)
ciscoEnvMonTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureThreshold.setUnits("degrees Celsius")
_CiscoEnvMonTemperatureLastShutdown_Type = Integer32
_CiscoEnvMonTemperatureLastShutdown_Object = MibTableColumn
ciscoEnvMonTemperatureLastShutdown = _CiscoEnvMonTemperatureLastShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 5),
    _CiscoEnvMonTemperatureLastShutdown_Type()
)
ciscoEnvMonTemperatureLastShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureLastShutdown.setStatus("current")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureLastShutdown.setUnits("degrees Celsius")
_CiscoEnvMonTemperatureState_Type = CiscoEnvMonState
_CiscoEnvMonTemperatureState_Object = MibTableColumn
ciscoEnvMonTemperatureState = _CiscoEnvMonTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 6),
    _CiscoEnvMonTemperatureState_Type()
)
ciscoEnvMonTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureState.setStatus("current")
_CiscoEnvMonFanStatusTable_Object = MibTable
ciscoEnvMonFanStatusTable = _CiscoEnvMonFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEnvMonFanStatusTable.setStatus("current")
_CiscoEnvMonFanStatusEntry_Object = MibTableRow
ciscoEnvMonFanStatusEntry = _CiscoEnvMonFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1)
)
ciscoEnvMonFanStatusEntry.setIndexNames(
    (0, "CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    ciscoEnvMonFanStatusEntry.setStatus("current")


class _CiscoEnvMonFanStatusIndex_Type(Integer32):
    """Custom type ciscoEnvMonFanStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoEnvMonFanStatusIndex_Type.__name__ = "Integer32"
_CiscoEnvMonFanStatusIndex_Object = MibTableColumn
ciscoEnvMonFanStatusIndex = _CiscoEnvMonFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 1),
    _CiscoEnvMonFanStatusIndex_Type()
)
ciscoEnvMonFanStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoEnvMonFanStatusIndex.setStatus("current")


class _CiscoEnvMonFanStatusDescr_Type(DisplayString):
    """Custom type ciscoEnvMonFanStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoEnvMonFanStatusDescr_Type.__name__ = "DisplayString"
_CiscoEnvMonFanStatusDescr_Object = MibTableColumn
ciscoEnvMonFanStatusDescr = _CiscoEnvMonFanStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 2),
    _CiscoEnvMonFanStatusDescr_Type()
)
ciscoEnvMonFanStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonFanStatusDescr.setStatus("current")
_CiscoEnvMonFanState_Type = CiscoEnvMonState
_CiscoEnvMonFanState_Object = MibTableColumn
ciscoEnvMonFanState = _CiscoEnvMonFanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 3),
    _CiscoEnvMonFanState_Type()
)
ciscoEnvMonFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonFanState.setStatus("current")
_CiscoEnvMonSupplyStatusTable_Object = MibTable
ciscoEnvMonSupplyStatusTable = _CiscoEnvMonSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoEnvMonSupplyStatusTable.setStatus("current")
_CiscoEnvMonSupplyStatusEntry_Object = MibTableRow
ciscoEnvMonSupplyStatusEntry = _CiscoEnvMonSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1)
)
ciscoEnvMonSupplyStatusEntry.setIndexNames(
    (0, "CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    ciscoEnvMonSupplyStatusEntry.setStatus("current")


class _CiscoEnvMonSupplyStatusIndex_Type(Integer32):
    """Custom type ciscoEnvMonSupplyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoEnvMonSupplyStatusIndex_Type.__name__ = "Integer32"
_CiscoEnvMonSupplyStatusIndex_Object = MibTableColumn
ciscoEnvMonSupplyStatusIndex = _CiscoEnvMonSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 1),
    _CiscoEnvMonSupplyStatusIndex_Type()
)
ciscoEnvMonSupplyStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoEnvMonSupplyStatusIndex.setStatus("current")


class _CiscoEnvMonSupplyStatusDescr_Type(DisplayString):
    """Custom type ciscoEnvMonSupplyStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoEnvMonSupplyStatusDescr_Type.__name__ = "DisplayString"
_CiscoEnvMonSupplyStatusDescr_Object = MibTableColumn
ciscoEnvMonSupplyStatusDescr = _CiscoEnvMonSupplyStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 2),
    _CiscoEnvMonSupplyStatusDescr_Type()
)
ciscoEnvMonSupplyStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonSupplyStatusDescr.setStatus("current")
_CiscoEnvMonSupplyState_Type = CiscoEnvMonState
_CiscoEnvMonSupplyState_Object = MibTableColumn
ciscoEnvMonSupplyState = _CiscoEnvMonSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 3),
    _CiscoEnvMonSupplyState_Type()
)
ciscoEnvMonSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonSupplyState.setStatus("current")


class _CiscoEnvMonSupplySource_Type(Integer32):
    """Custom type ciscoEnvMonSupplySource based on Integer32"""
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
        *(("ac", 2),
          ("dc", 3),
          ("externalPowerSupply", 4),
          ("internalRedundant", 5),
          ("unknown", 1))
    )


_CiscoEnvMonSupplySource_Type.__name__ = "Integer32"
_CiscoEnvMonSupplySource_Object = MibTableColumn
ciscoEnvMonSupplySource = _CiscoEnvMonSupplySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 4),
    _CiscoEnvMonSupplySource_Type()
)
ciscoEnvMonSupplySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonSupplySource.setStatus("current")


class _CiscoEnvMonAlarmContacts_Type(Bits):
    """Custom type ciscoEnvMonAlarmContacts based on Bits"""
    namedValues = NamedValues(
        *(("criticalAudible", 5),
          ("criticalVisual", 2),
          ("input", 6),
          ("majorAudible", 4),
          ("majorVisual", 1),
          ("minorAudible", 3),
          ("minorVisual", 0))
    )

_CiscoEnvMonAlarmContacts_Type.__name__ = "Bits"
_CiscoEnvMonAlarmContacts_Object = MibScalar
ciscoEnvMonAlarmContacts = _CiscoEnvMonAlarmContacts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 6),
    _CiscoEnvMonAlarmContacts_Type()
)
ciscoEnvMonAlarmContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEnvMonAlarmContacts.setStatus("current")
_CiscoEnvMonMIBNotificationEnables_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBNotificationEnables = _CiscoEnvMonMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2)
)


class _CiscoEnvMonEnableShutdownNotification_Type(TruthValue):
    """Custom type ciscoEnvMonEnableShutdownNotification based on TruthValue"""


_CiscoEnvMonEnableShutdownNotification_Object = MibScalar
ciscoEnvMonEnableShutdownNotification = _CiscoEnvMonEnableShutdownNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 1),
    _CiscoEnvMonEnableShutdownNotification_Type()
)
ciscoEnvMonEnableShutdownNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableShutdownNotification.setStatus("current")


class _CiscoEnvMonEnableVoltageNotification_Type(TruthValue):
    """Custom type ciscoEnvMonEnableVoltageNotification based on TruthValue"""


_CiscoEnvMonEnableVoltageNotification_Object = MibScalar
ciscoEnvMonEnableVoltageNotification = _CiscoEnvMonEnableVoltageNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 2),
    _CiscoEnvMonEnableVoltageNotification_Type()
)
ciscoEnvMonEnableVoltageNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableVoltageNotification.setStatus("deprecated")


class _CiscoEnvMonEnableTemperatureNotification_Type(TruthValue):
    """Custom type ciscoEnvMonEnableTemperatureNotification based on TruthValue"""


_CiscoEnvMonEnableTemperatureNotification_Object = MibScalar
ciscoEnvMonEnableTemperatureNotification = _CiscoEnvMonEnableTemperatureNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 3),
    _CiscoEnvMonEnableTemperatureNotification_Type()
)
ciscoEnvMonEnableTemperatureNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableTemperatureNotification.setStatus("deprecated")


class _CiscoEnvMonEnableFanNotification_Type(TruthValue):
    """Custom type ciscoEnvMonEnableFanNotification based on TruthValue"""


_CiscoEnvMonEnableFanNotification_Object = MibScalar
ciscoEnvMonEnableFanNotification = _CiscoEnvMonEnableFanNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 4),
    _CiscoEnvMonEnableFanNotification_Type()
)
ciscoEnvMonEnableFanNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableFanNotification.setStatus("deprecated")


class _CiscoEnvMonEnableRedundantSupplyNotification_Type(TruthValue):
    """Custom type ciscoEnvMonEnableRedundantSupplyNotification based on TruthValue"""


_CiscoEnvMonEnableRedundantSupplyNotification_Object = MibScalar
ciscoEnvMonEnableRedundantSupplyNotification = _CiscoEnvMonEnableRedundantSupplyNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 5),
    _CiscoEnvMonEnableRedundantSupplyNotification_Type()
)
ciscoEnvMonEnableRedundantSupplyNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableRedundantSupplyNotification.setStatus("deprecated")


class _CiscoEnvMonEnableStatChangeNotif_Type(TruthValue):
    """Custom type ciscoEnvMonEnableStatChangeNotif based on TruthValue"""


_CiscoEnvMonEnableStatChangeNotif_Object = MibScalar
ciscoEnvMonEnableStatChangeNotif = _CiscoEnvMonEnableStatChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 6),
    _CiscoEnvMonEnableStatChangeNotif_Type()
)
ciscoEnvMonEnableStatChangeNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEnvMonEnableStatChangeNotif.setStatus("current")
_CiscoEnvMonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBNotificationPrefix = _CiscoEnvMonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3)
)
_CiscoEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBNotifications = _CiscoEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0)
)
_CiscoEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBConformance = _CiscoEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4)
)
_CiscoEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBCompliances = _CiscoEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1)
)
_CiscoEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEnvMonMIBGroups = _CiscoEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2)
)

# Managed Objects groups

ciscoEnvMonMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 1)
)
ciscoEnvMonMIBGroup.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonPresent"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdLow"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdHigh"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageLastShutdown"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureThreshold"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureLastShutdown"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplySource"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonAlarmContacts"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableShutdownNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableVoltageNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableTemperatureNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableFanNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableRedundantSupplyNotification"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBGroup.setStatus("deprecated")

ciscoEnvMonMIBGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 2)
)
ciscoEnvMonMIBGroupRev.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonPresent"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdLow"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdHigh"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageLastShutdown"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureThreshold"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureLastShutdown"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplySource"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonAlarmContacts"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableShutdownNotification"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBGroupRev.setStatus("current")

ciscoEnvMonEnableStatChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 3)
)
ciscoEnvMonEnableStatChangeGroup.setObjects(
    ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableStatChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoEnvMonEnableStatChangeGroup.setStatus("current")


# Notification objects

ciscoEnvMonShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoEnvMonShutdownNotification.setStatus(
        "current"
    )

ciscoEnvMonVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 2)
)
ciscoEnvMonVoltageNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonVoltageNotification.setStatus(
        "deprecated"
    )

ciscoEnvMonTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 3)
)
ciscoEnvMonTemperatureNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonTemperatureNotification.setStatus(
        "deprecated"
    )

ciscoEnvMonFanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 4)
)
ciscoEnvMonFanNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonFanNotification.setStatus(
        "deprecated"
    )

ciscoEnvMonRedundantSupplyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 5)
)
ciscoEnvMonRedundantSupplyNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonRedundantSupplyNotification.setStatus(
        "deprecated"
    )

ciscoEnvMonVoltStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 6)
)
ciscoEnvMonVoltStatusChangeNotif.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonVoltStatusChangeNotif.setStatus(
        "current"
    )

ciscoEnvMonTempStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 7)
)
ciscoEnvMonTempStatusChangeNotif.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonTempStatusChangeNotif.setStatus(
        "current"
    )

ciscoEnvMonFanStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 8)
)
ciscoEnvMonFanStatusChangeNotif.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonFanStatusChangeNotif.setStatus(
        "current"
    )

ciscoEnvMonSuppStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 9)
)
ciscoEnvMonSuppStatusChangeNotif.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonSuppStatusChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoEnvMonMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 4)
)
ciscoEnvMonMIBNotifGroup.setObjects(
    ("CISCO-ENVMON-MIB", "ciscoEnvMonShutdownNotification")
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBNotifGroup.setStatus(
        "current"
    )

ciscoEnvMonStatChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 5)
)
ciscoEnvMonStatChangeNotifGroup.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltStatusChangeNotif"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTempStatusChangeNotif"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusChangeNotif"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonSuppStatusChangeNotif"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonStatChangeNotifGroup.setStatus(
        "current"
    )

ciscoEnvMonMIBMiscNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 6)
)
ciscoEnvMonMIBMiscNotifGroup.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonFanNotification"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonRedundantSupplyNotification"))
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBMiscNotifGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

ciscoEnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEnvMonMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEnvMonMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENVMON-MIB",
    **{"CiscoEnvMonState": CiscoEnvMonState,
       "CiscoSignedGauge": CiscoSignedGauge,
       "ciscoEnvMonMIB": ciscoEnvMonMIB,
       "ciscoEnvMonObjects": ciscoEnvMonObjects,
       "ciscoEnvMonPresent": ciscoEnvMonPresent,
       "ciscoEnvMonVoltageStatusTable": ciscoEnvMonVoltageStatusTable,
       "ciscoEnvMonVoltageStatusEntry": ciscoEnvMonVoltageStatusEntry,
       "ciscoEnvMonVoltageStatusIndex": ciscoEnvMonVoltageStatusIndex,
       "ciscoEnvMonVoltageStatusDescr": ciscoEnvMonVoltageStatusDescr,
       "ciscoEnvMonVoltageStatusValue": ciscoEnvMonVoltageStatusValue,
       "ciscoEnvMonVoltageThresholdLow": ciscoEnvMonVoltageThresholdLow,
       "ciscoEnvMonVoltageThresholdHigh": ciscoEnvMonVoltageThresholdHigh,
       "ciscoEnvMonVoltageLastShutdown": ciscoEnvMonVoltageLastShutdown,
       "ciscoEnvMonVoltageState": ciscoEnvMonVoltageState,
       "ciscoEnvMonTemperatureStatusTable": ciscoEnvMonTemperatureStatusTable,
       "ciscoEnvMonTemperatureStatusEntry": ciscoEnvMonTemperatureStatusEntry,
       "ciscoEnvMonTemperatureStatusIndex": ciscoEnvMonTemperatureStatusIndex,
       "ciscoEnvMonTemperatureStatusDescr": ciscoEnvMonTemperatureStatusDescr,
       "ciscoEnvMonTemperatureStatusValue": ciscoEnvMonTemperatureStatusValue,
       "ciscoEnvMonTemperatureThreshold": ciscoEnvMonTemperatureThreshold,
       "ciscoEnvMonTemperatureLastShutdown": ciscoEnvMonTemperatureLastShutdown,
       "ciscoEnvMonTemperatureState": ciscoEnvMonTemperatureState,
       "ciscoEnvMonFanStatusTable": ciscoEnvMonFanStatusTable,
       "ciscoEnvMonFanStatusEntry": ciscoEnvMonFanStatusEntry,
       "ciscoEnvMonFanStatusIndex": ciscoEnvMonFanStatusIndex,
       "ciscoEnvMonFanStatusDescr": ciscoEnvMonFanStatusDescr,
       "ciscoEnvMonFanState": ciscoEnvMonFanState,
       "ciscoEnvMonSupplyStatusTable": ciscoEnvMonSupplyStatusTable,
       "ciscoEnvMonSupplyStatusEntry": ciscoEnvMonSupplyStatusEntry,
       "ciscoEnvMonSupplyStatusIndex": ciscoEnvMonSupplyStatusIndex,
       "ciscoEnvMonSupplyStatusDescr": ciscoEnvMonSupplyStatusDescr,
       "ciscoEnvMonSupplyState": ciscoEnvMonSupplyState,
       "ciscoEnvMonSupplySource": ciscoEnvMonSupplySource,
       "ciscoEnvMonAlarmContacts": ciscoEnvMonAlarmContacts,
       "ciscoEnvMonMIBNotificationEnables": ciscoEnvMonMIBNotificationEnables,
       "ciscoEnvMonEnableShutdownNotification": ciscoEnvMonEnableShutdownNotification,
       "ciscoEnvMonEnableVoltageNotification": ciscoEnvMonEnableVoltageNotification,
       "ciscoEnvMonEnableTemperatureNotification": ciscoEnvMonEnableTemperatureNotification,
       "ciscoEnvMonEnableFanNotification": ciscoEnvMonEnableFanNotification,
       "ciscoEnvMonEnableRedundantSupplyNotification": ciscoEnvMonEnableRedundantSupplyNotification,
       "ciscoEnvMonEnableStatChangeNotif": ciscoEnvMonEnableStatChangeNotif,
       "ciscoEnvMonMIBNotificationPrefix": ciscoEnvMonMIBNotificationPrefix,
       "ciscoEnvMonMIBNotifications": ciscoEnvMonMIBNotifications,
       "ciscoEnvMonShutdownNotification": ciscoEnvMonShutdownNotification,
       "ciscoEnvMonVoltageNotification": ciscoEnvMonVoltageNotification,
       "ciscoEnvMonTemperatureNotification": ciscoEnvMonTemperatureNotification,
       "ciscoEnvMonFanNotification": ciscoEnvMonFanNotification,
       "ciscoEnvMonRedundantSupplyNotification": ciscoEnvMonRedundantSupplyNotification,
       "ciscoEnvMonVoltStatusChangeNotif": ciscoEnvMonVoltStatusChangeNotif,
       "ciscoEnvMonTempStatusChangeNotif": ciscoEnvMonTempStatusChangeNotif,
       "ciscoEnvMonFanStatusChangeNotif": ciscoEnvMonFanStatusChangeNotif,
       "ciscoEnvMonSuppStatusChangeNotif": ciscoEnvMonSuppStatusChangeNotif,
       "ciscoEnvMonMIBConformance": ciscoEnvMonMIBConformance,
       "ciscoEnvMonMIBCompliances": ciscoEnvMonMIBCompliances,
       "ciscoEnvMonMIBCompliance": ciscoEnvMonMIBCompliance,
       "ciscoEnvMonMIBComplianceRev1": ciscoEnvMonMIBComplianceRev1,
       "ciscoEnvMonMIBGroups": ciscoEnvMonMIBGroups,
       "ciscoEnvMonMIBGroup": ciscoEnvMonMIBGroup,
       "ciscoEnvMonMIBGroupRev": ciscoEnvMonMIBGroupRev,
       "ciscoEnvMonEnableStatChangeGroup": ciscoEnvMonEnableStatChangeGroup,
       "ciscoEnvMonMIBNotifGroup": ciscoEnvMonMIBNotifGroup,
       "ciscoEnvMonStatChangeNotifGroup": ciscoEnvMonStatChangeNotifGroup,
       "ciscoEnvMonMIBMiscNotifGroup": ciscoEnvMonMIBMiscNotifGroup}
)
