# SNMP MIB module (BLUEARC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUEARC-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:13 2024
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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

blueArcServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1)
)
blueArcServer.setRevisions(
        ("2010-04-08 12:00",
         "2007-11-05 12:00",
         "2006-05-12 12:00",
         "2006-04-24 12:00",
         "2005-12-13 12:00",
         "2005-12-09 12:00",
         "2005-08-29 12:00",
         "2004-03-23 12:00",
         "2003-10-14 12:00",
         "2003-09-01 12:00",
         "2003-07-24 12:00",
         "2003-07-11 12:00",
         "2003-06-10 12:00",
         "2003-03-31 12:00",
         "2003-03-27 12:00",
         "2003-01-16 14:00",
         "2003-01-16 12:00",
         "2003-01-15 10:16",
         "2003-01-07 16:21",
         "2002-11-28 16:20",
         "2002-10-25 14:52",
         "2002-10-24 14:07",
         "2002-05-31 12:00",
         "2002-05-27 12:00",
         "2002-04-04 12:00",
         "2002-03-19 12:00",
         "2001-12-21 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlueArc_ObjectIdentity = ObjectIdentity
blueArc = _BlueArc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096)
)
_BlueArcPrivate_ObjectIdentity = ObjectIdentity
blueArcPrivate = _BlueArcPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6)
)
_BlueArcServerObjs_ObjectIdentity = ObjectIdentity
blueArcServerObjs = _BlueArcServerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1)
)
_PowerUnits_ObjectIdentity = ObjectIdentity
powerUnits = _PowerUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1)
)
_PuConfigNumber_Type = Integer32
_PuConfigNumber_Object = MibScalar
puConfigNumber = _PuConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 1),
    _PuConfigNumber_Type()
)
puConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigNumber.setStatus("obsolete")
_PuConfigTable_Object = MibTable
puConfigTable = _PuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    puConfigTable.setStatus("obsolete")
_PuConfigEntry_Object = MibTableRow
puConfigEntry = _PuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1)
)
puConfigEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puConfigIndex"),
)
if mibBuilder.loadTexts:
    puConfigEntry.setStatus("obsolete")


class _PuConfigIndex_Type(Integer32):
    """Custom type puConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PuConfigIndex_Type.__name__ = "Integer32"
_PuConfigIndex_Object = MibTableColumn
puConfigIndex = _PuConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 1),
    _PuConfigIndex_Type()
)
puConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigIndex.setStatus("obsolete")


class _PuConfigShutdownEnabled_Type(Integer32):
    """Custom type puConfigShutdownEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PuConfigShutdownEnabled_Type.__name__ = "Integer32"
_PuConfigShutdownEnabled_Object = MibTableColumn
puConfigShutdownEnabled = _PuConfigShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 2),
    _PuConfigShutdownEnabled_Type()
)
puConfigShutdownEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigShutdownEnabled.setStatus("obsolete")


class _PuConfigShutdownInterval_Type(Integer32):
    """Custom type puConfigShutdownInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fiveMinutes", 6),
          ("immediately", 2),
          ("oneMinute", 3),
          ("remainingLife", 1),
          ("tenMinutes", 7),
          ("threeMinutes", 5),
          ("twoMinutes", 4))
    )


_PuConfigShutdownInterval_Type.__name__ = "Integer32"
_PuConfigShutdownInterval_Object = MibTableColumn
puConfigShutdownInterval = _PuConfigShutdownInterval_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 3),
    _PuConfigShutdownInterval_Type()
)
puConfigShutdownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigShutdownInterval.setStatus("obsolete")


class _PuConfigShutdownRemainingLife_Type(Integer32):
    """Custom type puConfigShutdownRemainingLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("fiveMinutes", 5),
          ("tenMinutes", 10))
    )


_PuConfigShutdownRemainingLife_Type.__name__ = "Integer32"
_PuConfigShutdownRemainingLife_Object = MibTableColumn
puConfigShutdownRemainingLife = _PuConfigShutdownRemainingLife_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 4),
    _PuConfigShutdownRemainingLife_Type()
)
puConfigShutdownRemainingLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigShutdownRemainingLife.setStatus("obsolete")


class _PuConfigCommsOK_Type(Integer32):
    """Custom type puConfigCommsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("communicating", 1),
          ("notCommunicating", 2))
    )


_PuConfigCommsOK_Type.__name__ = "Integer32"
_PuConfigCommsOK_Object = MibTableColumn
puConfigCommsOK = _PuConfigCommsOK_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 5),
    _PuConfigCommsOK_Type()
)
puConfigCommsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigCommsOK.setStatus("obsolete")


class _PuConfigCommsEverOK_Type(Integer32):
    """Custom type puConfigCommsEverOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("communicated", 1),
          ("neverCommunicated", 2))
    )


_PuConfigCommsEverOK_Type.__name__ = "Integer32"
_PuConfigCommsEverOK_Object = MibTableColumn
puConfigCommsEverOK = _PuConfigCommsEverOK_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 2, 1, 6),
    _PuConfigCommsEverOK_Type()
)
puConfigCommsEverOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigCommsEverOK.setStatus("obsolete")
_PuStatusNumber_Type = Integer32
_PuStatusNumber_Object = MibScalar
puStatusNumber = _PuStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 3),
    _PuStatusNumber_Type()
)
puStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusNumber.setStatus("obsolete")
_PuStatusTable_Object = MibTable
puStatusTable = _PuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    puStatusTable.setStatus("obsolete")
_PuStatusEntry_Object = MibTableRow
puStatusEntry = _PuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1)
)
puStatusEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puStatusIndex"),
)
if mibBuilder.loadTexts:
    puStatusEntry.setStatus("obsolete")


class _PuStatusIndex_Type(Integer32):
    """Custom type puStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PuStatusIndex_Type.__name__ = "Integer32"
_PuStatusIndex_Object = MibTableColumn
puStatusIndex = _PuStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 1),
    _PuStatusIndex_Type()
)
puStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusIndex.setStatus("obsolete")
_PuStatusModel_Type = DisplayString
_PuStatusModel_Object = MibTableColumn
puStatusModel = _PuStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 2),
    _PuStatusModel_Type()
)
puStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusModel.setStatus("obsolete")
_PuStatusSerialNumber_Type = DisplayString
_PuStatusSerialNumber_Object = MibTableColumn
puStatusSerialNumber = _PuStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 3),
    _PuStatusSerialNumber_Type()
)
puStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusSerialNumber.setStatus("obsolete")
_PuStatusManufactureDate_Type = DisplayString
_PuStatusManufactureDate_Object = MibTableColumn
puStatusManufactureDate = _PuStatusManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 4),
    _PuStatusManufactureDate_Type()
)
puStatusManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusManufactureDate.setStatus("obsolete")
_PuStatusBatteryReplaceDate_Type = DisplayString
_PuStatusBatteryReplaceDate_Object = MibTableColumn
puStatusBatteryReplaceDate = _PuStatusBatteryReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 5),
    _PuStatusBatteryReplaceDate_Type()
)
puStatusBatteryReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusBatteryReplaceDate.setStatus("obsolete")
_PuStatusUpperTransferVoltage_Type = Integer32
_PuStatusUpperTransferVoltage_Object = MibTableColumn
puStatusUpperTransferVoltage = _PuStatusUpperTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 6),
    _PuStatusUpperTransferVoltage_Type()
)
puStatusUpperTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusUpperTransferVoltage.setStatus("obsolete")
_PuStatusLowerTransferVoltage_Type = Integer32
_PuStatusLowerTransferVoltage_Object = MibTableColumn
puStatusLowerTransferVoltage = _PuStatusLowerTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 7),
    _PuStatusLowerTransferVoltage_Type()
)
puStatusLowerTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusLowerTransferVoltage.setStatus("obsolete")


class _PuStatusSensitivity_Type(Integer32):
    """Custom type puStatusSensitivity based on Integer32"""
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
        *(("automatic", 4),
          ("high", 1),
          ("low", 3),
          ("medium", 2),
          ("unknown", 5))
    )


_PuStatusSensitivity_Type.__name__ = "Integer32"
_PuStatusSensitivity_Object = MibTableColumn
puStatusSensitivity = _PuStatusSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 8),
    _PuStatusSensitivity_Type()
)
puStatusSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusSensitivity.setStatus("obsolete")
_PuStatusLowBatteryInterval_Type = Integer32
_PuStatusLowBatteryInterval_Object = MibTableColumn
puStatusLowBatteryInterval = _PuStatusLowBatteryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 9),
    _PuStatusLowBatteryInterval_Type()
)
puStatusLowBatteryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusLowBatteryInterval.setStatus("obsolete")


class _PuStatusAlarmSetting_Type(Integer32):
    """Custom type puStatusAlarmSetting based on Integer32"""
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
        *(("delayedUtilityFailure", 2),
          ("immediately", 1),
          ("lowBatteryOnly", 3),
          ("never", 4),
          ("unknown", 5))
    )


_PuStatusAlarmSetting_Type.__name__ = "Integer32"
_PuStatusAlarmSetting_Object = MibTableColumn
puStatusAlarmSetting = _PuStatusAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 10),
    _PuStatusAlarmSetting_Type()
)
puStatusAlarmSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusAlarmSetting.setStatus("obsolete")


class _PuStatusCalibrating_Type(Integer32):
    """Custom type puStatusCalibrating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calibrating", 1),
          ("notCalibrating", 2))
    )


_PuStatusCalibrating_Type.__name__ = "Integer32"
_PuStatusCalibrating_Object = MibTableColumn
puStatusCalibrating = _PuStatusCalibrating_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 11),
    _PuStatusCalibrating_Type()
)
puStatusCalibrating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusCalibrating.setStatus("obsolete")


class _PuStatusSleeping_Type(Integer32):
    """Custom type puStatusSleeping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSleeping", 2),
          ("sleeping", 1))
    )


_PuStatusSleeping_Type.__name__ = "Integer32"
_PuStatusSleeping_Object = MibTableColumn
puStatusSleeping = _PuStatusSleeping_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 12),
    _PuStatusSleeping_Type()
)
puStatusSleeping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusSleeping.setStatus("obsolete")


class _PuStatusOnline_Type(Integer32):
    """Custom type puStatusOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_PuStatusOnline_Type.__name__ = "Integer32"
_PuStatusOnline_Object = MibTableColumn
puStatusOnline = _PuStatusOnline_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 13),
    _PuStatusOnline_Type()
)
puStatusOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusOnline.setStatus("obsolete")


class _PuStatusOnBattery_Type(Integer32):
    """Custom type puStatusOnBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onBattery", 1),
          ("onMains", 2))
    )


_PuStatusOnBattery_Type.__name__ = "Integer32"
_PuStatusOnBattery_Object = MibTableColumn
puStatusOnBattery = _PuStatusOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 14),
    _PuStatusOnBattery_Type()
)
puStatusOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusOnBattery.setStatus("obsolete")


class _PuStatusBatteryAlmostUsedUp_Type(Integer32):
    """Custom type puStatusBatteryAlmostUsedUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryAlmostUsedUp", 1),
          ("batteryOK", 2))
    )


_PuStatusBatteryAlmostUsedUp_Type.__name__ = "Integer32"
_PuStatusBatteryAlmostUsedUp_Object = MibTableColumn
puStatusBatteryAlmostUsedUp = _PuStatusBatteryAlmostUsedUp_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 15),
    _PuStatusBatteryAlmostUsedUp_Type()
)
puStatusBatteryAlmostUsedUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusBatteryAlmostUsedUp.setStatus("obsolete")


class _PuStatusChangeBattery_Type(Integer32):
    """Custom type puStatusChangeBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryOK", 2),
          ("changeBattery", 1))
    )


_PuStatusChangeBattery_Type.__name__ = "Integer32"
_PuStatusChangeBattery_Object = MibTableColumn
puStatusChangeBattery = _PuStatusChangeBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 4, 1, 16),
    _PuStatusChangeBattery_Type()
)
puStatusChangeBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatusChangeBattery.setStatus("obsolete")
_PuStatsNumber_Type = Integer32
_PuStatsNumber_Object = MibScalar
puStatsNumber = _PuStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 5),
    _PuStatsNumber_Type()
)
puStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsNumber.setStatus("obsolete")
_PuStatsTable_Object = MibTable
puStatsTable = _PuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    puStatsTable.setStatus("obsolete")
_PuStatsEntry_Object = MibTableRow
puStatsEntry = _PuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1)
)
puStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puStatsIndex"),
)
if mibBuilder.loadTexts:
    puStatsEntry.setStatus("obsolete")


class _PuStatsIndex_Type(Integer32):
    """Custom type puStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PuStatsIndex_Type.__name__ = "Integer32"
_PuStatsIndex_Object = MibTableColumn
puStatsIndex = _PuStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 1),
    _PuStatsIndex_Type()
)
puStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsIndex.setStatus("obsolete")


class _PuStatsBatteryCharge_Type(Integer32):
    """Custom type puStatsBatteryCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PuStatsBatteryCharge_Type.__name__ = "Integer32"
_PuStatsBatteryCharge_Object = MibTableColumn
puStatsBatteryCharge = _PuStatsBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 2),
    _PuStatsBatteryCharge_Type()
)
puStatsBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsBatteryCharge.setStatus("obsolete")


class _PuStatsLoad_Type(Integer32):
    """Custom type puStatsLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PuStatsLoad_Type.__name__ = "Integer32"
_PuStatsLoad_Object = MibTableColumn
puStatsLoad = _PuStatsLoad_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 3),
    _PuStatsLoad_Type()
)
puStatsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsLoad.setStatus("obsolete")
_PuStatsFrequency_Type = Integer32
_PuStatsFrequency_Object = MibTableColumn
puStatsFrequency = _PuStatsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 4),
    _PuStatsFrequency_Type()
)
puStatsFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsFrequency.setStatus("obsolete")
_PuStatsLineVoltage_Type = Integer32
_PuStatsLineVoltage_Object = MibTableColumn
puStatsLineVoltage = _PuStatsLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 5),
    _PuStatsLineVoltage_Type()
)
puStatsLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsLineVoltage.setStatus("obsolete")
_PuStatsOutputVoltage_Type = Integer32
_PuStatsOutputVoltage_Object = MibTableColumn
puStatsOutputVoltage = _PuStatsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 6),
    _PuStatsOutputVoltage_Type()
)
puStatsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsOutputVoltage.setStatus("obsolete")
_PuStatsBatteryVoltage_Type = Integer32
_PuStatsBatteryVoltage_Object = MibTableColumn
puStatsBatteryVoltage = _PuStatsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 7),
    _PuStatsBatteryVoltage_Type()
)
puStatsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsBatteryVoltage.setStatus("obsolete")
_PuStatsTemperatureC_Type = Integer32
_PuStatsTemperatureC_Object = MibTableColumn
puStatsTemperatureC = _PuStatsTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 8),
    _PuStatsTemperatureC_Type()
)
puStatsTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsTemperatureC.setStatus("obsolete")
_PuStatsTemperatureF_Type = Integer32
_PuStatsTemperatureF_Object = MibTableColumn
puStatsTemperatureF = _PuStatsTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 9),
    _PuStatsTemperatureF_Type()
)
puStatsTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsTemperatureF.setStatus("obsolete")
_PuStatsLineMininumVoltage_Type = Integer32
_PuStatsLineMininumVoltage_Object = MibTableColumn
puStatsLineMininumVoltage = _PuStatsLineMininumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 10),
    _PuStatsLineMininumVoltage_Type()
)
puStatsLineMininumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsLineMininumVoltage.setStatus("obsolete")
_PuStatsLineMaximumVoltage_Type = Integer32
_PuStatsLineMaximumVoltage_Object = MibTableColumn
puStatsLineMaximumVoltage = _PuStatsLineMaximumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 11),
    _PuStatsLineMaximumVoltage_Type()
)
puStatsLineMaximumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsLineMaximumVoltage.setStatus("obsolete")
_PuStatsRemainingRunTime_Type = Integer32
_PuStatsRemainingRunTime_Object = MibTableColumn
puStatsRemainingRunTime = _PuStatsRemainingRunTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 6, 1, 12),
    _PuStatsRemainingRunTime_Type()
)
puStatsRemainingRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatsRemainingRunTime.setStatus("obsolete")
_PuConfigurationCount_Type = Integer32
_PuConfigurationCount_Object = MibScalar
puConfigurationCount = _PuConfigurationCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 7),
    _PuConfigurationCount_Type()
)
puConfigurationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationCount.setStatus("current")
_PuConfigurationTable_Object = MibTable
puConfigurationTable = _PuConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    puConfigurationTable.setStatus("current")
_PuConfigurationEntry_Object = MibTableRow
puConfigurationEntry = _PuConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1)
)
puConfigurationEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puConfigurationIndex"),
)
if mibBuilder.loadTexts:
    puConfigurationEntry.setStatus("current")
_PuConfigurationIndex_Type = IpAddress
_PuConfigurationIndex_Object = MibTableColumn
puConfigurationIndex = _PuConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 1),
    _PuConfigurationIndex_Type()
)
puConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationIndex.setStatus("current")
_PuConfigurationUserName_Type = DisplayString
_PuConfigurationUserName_Object = MibTableColumn
puConfigurationUserName = _PuConfigurationUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 2),
    _PuConfigurationUserName_Type()
)
puConfigurationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationUserName.setStatus("current")


class _PuConfigurationMonitoringEnabled_Type(Integer32):
    """Custom type puConfigurationMonitoringEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_PuConfigurationMonitoringEnabled_Type.__name__ = "Integer32"
_PuConfigurationMonitoringEnabled_Object = MibTableColumn
puConfigurationMonitoringEnabled = _PuConfigurationMonitoringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 3),
    _PuConfigurationMonitoringEnabled_Type()
)
puConfigurationMonitoringEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationMonitoringEnabled.setStatus("current")
_PuConfigurationShutdownOnBattery_Type = Integer32
_PuConfigurationShutdownOnBattery_Object = MibTableColumn
puConfigurationShutdownOnBattery = _PuConfigurationShutdownOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 4),
    _PuConfigurationShutdownOnBattery_Type()
)
puConfigurationShutdownOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationShutdownOnBattery.setStatus("current")
_PuConfigurationShutdownOnRuntime_Type = Integer32
_PuConfigurationShutdownOnRuntime_Object = MibTableColumn
puConfigurationShutdownOnRuntime = _PuConfigurationShutdownOnRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 5),
    _PuConfigurationShutdownOnRuntime_Type()
)
puConfigurationShutdownOnRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationShutdownOnRuntime.setStatus("current")
_PuConfigurationShutdownOnLowBattery_Type = Integer32
_PuConfigurationShutdownOnLowBattery_Object = MibTableColumn
puConfigurationShutdownOnLowBattery = _PuConfigurationShutdownOnLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 6),
    _PuConfigurationShutdownOnLowBattery_Type()
)
puConfigurationShutdownOnLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationShutdownOnLowBattery.setStatus("current")
_PuConfigurationOnBatteryTolerance_Type = Integer32
_PuConfigurationOnBatteryTolerance_Object = MibTableColumn
puConfigurationOnBatteryTolerance = _PuConfigurationOnBatteryTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 7),
    _PuConfigurationOnBatteryTolerance_Type()
)
puConfigurationOnBatteryTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationOnBatteryTolerance.setStatus("current")


class _PuConfigurationCommsOK_Type(Integer32):
    """Custom type puConfigurationCommsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("communicating", 1),
          ("notCommunicating", 2),
          ("unknown", 3))
    )


_PuConfigurationCommsOK_Type.__name__ = "Integer32"
_PuConfigurationCommsOK_Object = MibTableColumn
puConfigurationCommsOK = _PuConfigurationCommsOK_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 8),
    _PuConfigurationCommsOK_Type()
)
puConfigurationCommsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationCommsOK.setStatus("current")


class _PuConfigurationCommsEverOK_Type(Integer32):
    """Custom type puConfigurationCommsEverOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("communicated", 1),
          ("neverCommunicated", 2),
          ("unknown", 3))
    )


_PuConfigurationCommsEverOK_Type.__name__ = "Integer32"
_PuConfigurationCommsEverOK_Object = MibTableColumn
puConfigurationCommsEverOK = _PuConfigurationCommsEverOK_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 8, 1, 9),
    _PuConfigurationCommsEverOK_Type()
)
puConfigurationCommsEverOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConfigurationCommsEverOK.setStatus("current")
_PuCurrentStatusCount_Type = Integer32
_PuCurrentStatusCount_Object = MibScalar
puCurrentStatusCount = _PuCurrentStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 9),
    _PuCurrentStatusCount_Type()
)
puCurrentStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusCount.setStatus("current")
_PuCurrentStatusTable_Object = MibTable
puCurrentStatusTable = _PuCurrentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    puCurrentStatusTable.setStatus("current")
_PuCurrentStatusEntry_Object = MibTableRow
puCurrentStatusEntry = _PuCurrentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1)
)
puCurrentStatusEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puCurrentStatusIndex"),
)
if mibBuilder.loadTexts:
    puCurrentStatusEntry.setStatus("current")
_PuCurrentStatusIndex_Type = IpAddress
_PuCurrentStatusIndex_Object = MibTableColumn
puCurrentStatusIndex = _PuCurrentStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 1),
    _PuCurrentStatusIndex_Type()
)
puCurrentStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusIndex.setStatus("current")
_PuCurrentStatusModel_Type = DisplayString
_PuCurrentStatusModel_Object = MibTableColumn
puCurrentStatusModel = _PuCurrentStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 2),
    _PuCurrentStatusModel_Type()
)
puCurrentStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusModel.setStatus("current")
_PuCurrentStatusSerialNumber_Type = DisplayString
_PuCurrentStatusSerialNumber_Object = MibTableColumn
puCurrentStatusSerialNumber = _PuCurrentStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 3),
    _PuCurrentStatusSerialNumber_Type()
)
puCurrentStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusSerialNumber.setStatus("current")
_PuCurrentStatusManufactureDate_Type = DisplayString
_PuCurrentStatusManufactureDate_Object = MibTableColumn
puCurrentStatusManufactureDate = _PuCurrentStatusManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 4),
    _PuCurrentStatusManufactureDate_Type()
)
puCurrentStatusManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusManufactureDate.setStatus("current")
_PuCurrentStatusBatteryReplacedDate_Type = DisplayString
_PuCurrentStatusBatteryReplacedDate_Object = MibTableColumn
puCurrentStatusBatteryReplacedDate = _PuCurrentStatusBatteryReplacedDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 5),
    _PuCurrentStatusBatteryReplacedDate_Type()
)
puCurrentStatusBatteryReplacedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusBatteryReplacedDate.setStatus("current")
_PuCurrentStatusUpperTransferVoltage_Type = Integer32
_PuCurrentStatusUpperTransferVoltage_Object = MibTableColumn
puCurrentStatusUpperTransferVoltage = _PuCurrentStatusUpperTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 6),
    _PuCurrentStatusUpperTransferVoltage_Type()
)
puCurrentStatusUpperTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusUpperTransferVoltage.setStatus("current")
_PuCurrentStatusLowerTransferVoltage_Type = Integer32
_PuCurrentStatusLowerTransferVoltage_Object = MibTableColumn
puCurrentStatusLowerTransferVoltage = _PuCurrentStatusLowerTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 7),
    _PuCurrentStatusLowerTransferVoltage_Type()
)
puCurrentStatusLowerTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusLowerTransferVoltage.setStatus("current")


class _PuCurrentStatusSensitivity_Type(Integer32):
    """Custom type puCurrentStatusSensitivity based on Integer32"""
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
        *(("automatic", 4),
          ("high", 1),
          ("low", 3),
          ("medium", 2),
          ("unknown", 5))
    )


_PuCurrentStatusSensitivity_Type.__name__ = "Integer32"
_PuCurrentStatusSensitivity_Object = MibTableColumn
puCurrentStatusSensitivity = _PuCurrentStatusSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 8),
    _PuCurrentStatusSensitivity_Type()
)
puCurrentStatusSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusSensitivity.setStatus("current")
_PuCurrentStatusLowBatteryInterval_Type = Integer32
_PuCurrentStatusLowBatteryInterval_Object = MibTableColumn
puCurrentStatusLowBatteryInterval = _PuCurrentStatusLowBatteryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 9),
    _PuCurrentStatusLowBatteryInterval_Type()
)
puCurrentStatusLowBatteryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusLowBatteryInterval.setStatus("current")


class _PuCurrentStatusAlarmSetting_Type(Integer32):
    """Custom type puCurrentStatusAlarmSetting based on Integer32"""
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
        *(("delayedUtilityFailure", 2),
          ("immediately", 1),
          ("lowBatteryOnly", 3),
          ("never", 4),
          ("unknown", 5))
    )


_PuCurrentStatusAlarmSetting_Type.__name__ = "Integer32"
_PuCurrentStatusAlarmSetting_Object = MibTableColumn
puCurrentStatusAlarmSetting = _PuCurrentStatusAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 10),
    _PuCurrentStatusAlarmSetting_Type()
)
puCurrentStatusAlarmSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusAlarmSetting.setStatus("current")


class _PuCurrentStatusCalibrating_Type(Integer32):
    """Custom type puCurrentStatusCalibrating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calibrating", 1),
          ("notCalibrating", 2),
          ("notDefined", 0))
    )


_PuCurrentStatusCalibrating_Type.__name__ = "Integer32"
_PuCurrentStatusCalibrating_Object = MibTableColumn
puCurrentStatusCalibrating = _PuCurrentStatusCalibrating_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 11),
    _PuCurrentStatusCalibrating_Type()
)
puCurrentStatusCalibrating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusCalibrating.setStatus("current")


class _PuCurrentStatusSleeping_Type(Integer32):
    """Custom type puCurrentStatusSleeping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("notSleeping", 2),
          ("sleeping", 1))
    )


_PuCurrentStatusSleeping_Type.__name__ = "Integer32"
_PuCurrentStatusSleeping_Object = MibTableColumn
puCurrentStatusSleeping = _PuCurrentStatusSleeping_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 12),
    _PuCurrentStatusSleeping_Type()
)
puCurrentStatusSleeping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusSleeping.setStatus("current")


class _PuCurrentStatusSmartTrim_Type(Integer32):
    """Custom type puCurrentStatusSmartTrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notDefined", 0),
          ("notEnabled", 1))
    )


_PuCurrentStatusSmartTrim_Type.__name__ = "Integer32"
_PuCurrentStatusSmartTrim_Object = MibTableColumn
puCurrentStatusSmartTrim = _PuCurrentStatusSmartTrim_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 13),
    _PuCurrentStatusSmartTrim_Type()
)
puCurrentStatusSmartTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusSmartTrim.setStatus("current")


class _PuCurrentStatusSmartBoost_Type(Integer32):
    """Custom type puCurrentStatusSmartBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notDefined", 0),
          ("notEnabled", 1))
    )


_PuCurrentStatusSmartBoost_Type.__name__ = "Integer32"
_PuCurrentStatusSmartBoost_Object = MibTableColumn
puCurrentStatusSmartBoost = _PuCurrentStatusSmartBoost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 14),
    _PuCurrentStatusSmartBoost_Type()
)
puCurrentStatusSmartBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusSmartBoost.setStatus("current")


class _PuCurrentStatusOnline_Type(Integer32):
    """Custom type puCurrentStatusOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("offline", 2),
          ("online", 1))
    )


_PuCurrentStatusOnline_Type.__name__ = "Integer32"
_PuCurrentStatusOnline_Object = MibTableColumn
puCurrentStatusOnline = _PuCurrentStatusOnline_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 15),
    _PuCurrentStatusOnline_Type()
)
puCurrentStatusOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusOnline.setStatus("current")


class _PuCurrentStatusOnBattery_Type(Integer32):
    """Custom type puCurrentStatusOnBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("onBattery", 1),
          ("onMains", 2))
    )


_PuCurrentStatusOnBattery_Type.__name__ = "Integer32"
_PuCurrentStatusOnBattery_Object = MibTableColumn
puCurrentStatusOnBattery = _PuCurrentStatusOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 16),
    _PuCurrentStatusOnBattery_Type()
)
puCurrentStatusOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusOnBattery.setStatus("current")


class _PuCurrentStatusOverload_Type(Integer32):
    """Custom type puCurrentStatusOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notDefined", 0),
          ("notEnabled", 1))
    )


_PuCurrentStatusOverload_Type.__name__ = "Integer32"
_PuCurrentStatusOverload_Object = MibTableColumn
puCurrentStatusOverload = _PuCurrentStatusOverload_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 17),
    _PuCurrentStatusOverload_Type()
)
puCurrentStatusOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusOverload.setStatus("current")


class _PuCurrentStatusBatteryAlmostUsedUp_Type(Integer32):
    """Custom type puCurrentStatusBatteryAlmostUsedUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryAlmostUsedUp", 1),
          ("batteryOK", 2),
          ("notDefined", 0))
    )


_PuCurrentStatusBatteryAlmostUsedUp_Type.__name__ = "Integer32"
_PuCurrentStatusBatteryAlmostUsedUp_Object = MibTableColumn
puCurrentStatusBatteryAlmostUsedUp = _PuCurrentStatusBatteryAlmostUsedUp_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 18),
    _PuCurrentStatusBatteryAlmostUsedUp_Type()
)
puCurrentStatusBatteryAlmostUsedUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusBatteryAlmostUsedUp.setStatus("current")


class _PuCurrentStatusChangeBattery_Type(Integer32):
    """Custom type puCurrentStatusChangeBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryOK", 2),
          ("changeBattery", 1),
          ("notDefined", 0))
    )


_PuCurrentStatusChangeBattery_Type.__name__ = "Integer32"
_PuCurrentStatusChangeBattery_Object = MibTableColumn
puCurrentStatusChangeBattery = _PuCurrentStatusChangeBattery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 10, 1, 19),
    _PuCurrentStatusChangeBattery_Type()
)
puCurrentStatusChangeBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentStatusChangeBattery.setStatus("current")
_PuStatisticsCount_Type = Integer32
_PuStatisticsCount_Object = MibScalar
puStatisticsCount = _PuStatisticsCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 11),
    _PuStatisticsCount_Type()
)
puStatisticsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsCount.setStatus("current")
_PuStatisticsTable_Object = MibTable
puStatisticsTable = _PuStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    puStatisticsTable.setStatus("current")
_PuStatisticsEntry_Object = MibTableRow
puStatisticsEntry = _PuStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1)
)
puStatisticsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "puStatisticsIndex"),
)
if mibBuilder.loadTexts:
    puStatisticsEntry.setStatus("current")


class _PuStatisticsIndex_Type(Integer32):
    """Custom type puStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PuStatisticsIndex_Type.__name__ = "Integer32"
_PuStatisticsIndex_Object = MibTableColumn
puStatisticsIndex = _PuStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 1),
    _PuStatisticsIndex_Type()
)
puStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsIndex.setStatus("current")


class _PuStatisticsBatteryCharge_Type(Integer32):
    """Custom type puStatisticsBatteryCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PuStatisticsBatteryCharge_Type.__name__ = "Integer32"
_PuStatisticsBatteryCharge_Object = MibTableColumn
puStatisticsBatteryCharge = _PuStatisticsBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 2),
    _PuStatisticsBatteryCharge_Type()
)
puStatisticsBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsBatteryCharge.setStatus("current")


class _PuStatisticsLoad_Type(Integer32):
    """Custom type puStatisticsLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PuStatisticsLoad_Type.__name__ = "Integer32"
_PuStatisticsLoad_Object = MibTableColumn
puStatisticsLoad = _PuStatisticsLoad_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 3),
    _PuStatisticsLoad_Type()
)
puStatisticsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsLoad.setStatus("current")
_PuStatisticsFrequency_Type = Integer32
_PuStatisticsFrequency_Object = MibTableColumn
puStatisticsFrequency = _PuStatisticsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 4),
    _PuStatisticsFrequency_Type()
)
puStatisticsFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsFrequency.setStatus("current")
_PuStatisticsLineVoltage_Type = Integer32
_PuStatisticsLineVoltage_Object = MibTableColumn
puStatisticsLineVoltage = _PuStatisticsLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 5),
    _PuStatisticsLineVoltage_Type()
)
puStatisticsLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsLineVoltage.setStatus("current")
_PuStatisticsOutputVoltage_Type = Integer32
_PuStatisticsOutputVoltage_Object = MibTableColumn
puStatisticsOutputVoltage = _PuStatisticsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 6),
    _PuStatisticsOutputVoltage_Type()
)
puStatisticsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsOutputVoltage.setStatus("current")
_PuStatisticsBatteryVoltage_Type = Integer32
_PuStatisticsBatteryVoltage_Object = MibTableColumn
puStatisticsBatteryVoltage = _PuStatisticsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 7),
    _PuStatisticsBatteryVoltage_Type()
)
puStatisticsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsBatteryVoltage.setStatus("current")
_PuStatisticsTemperatureC_Type = Integer32
_PuStatisticsTemperatureC_Object = MibTableColumn
puStatisticsTemperatureC = _PuStatisticsTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 8),
    _PuStatisticsTemperatureC_Type()
)
puStatisticsTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsTemperatureC.setStatus("current")
_PuStatisticsTemperatureF_Type = Integer32
_PuStatisticsTemperatureF_Object = MibTableColumn
puStatisticsTemperatureF = _PuStatisticsTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 9),
    _PuStatisticsTemperatureF_Type()
)
puStatisticsTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsTemperatureF.setStatus("current")
_PuStatisticsLineMininumVoltage_Type = Integer32
_PuStatisticsLineMininumVoltage_Object = MibTableColumn
puStatisticsLineMininumVoltage = _PuStatisticsLineMininumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 10),
    _PuStatisticsLineMininumVoltage_Type()
)
puStatisticsLineMininumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsLineMininumVoltage.setStatus("current")
_PuStatisticsLineMaximumVoltage_Type = Integer32
_PuStatisticsLineMaximumVoltage_Object = MibTableColumn
puStatisticsLineMaximumVoltage = _PuStatisticsLineMaximumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 11),
    _PuStatisticsLineMaximumVoltage_Type()
)
puStatisticsLineMaximumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsLineMaximumVoltage.setStatus("current")
_PuStatisticsRemainingRunTime_Type = Integer32
_PuStatisticsRemainingRunTime_Object = MibTableColumn
puStatisticsRemainingRunTime = _PuStatisticsRemainingRunTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 1, 12, 1, 12),
    _PuStatisticsRemainingRunTime_Type()
)
puStatisticsRemainingRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puStatisticsRemainingRunTime.setStatus("current")
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2)
)
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1)
)
_SensorNumber_Type = Integer32
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("obsolete")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("obsolete")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1)
)
sensorEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("obsolete")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("obsolete")


class _SensorSpeedStatus_Type(Integer32):
    """Custom type sensorSpeedStatus based on Integer32"""
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
        *(("failed", 4),
          ("ok", 1),
          ("severe", 3),
          ("warning", 2))
    )


_SensorSpeedStatus_Type.__name__ = "Integer32"
_SensorSpeedStatus_Object = MibTableColumn
sensorSpeedStatus = _SensorSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 2),
    _SensorSpeedStatus_Type()
)
sensorSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSpeedStatus.setStatus("obsolete")
_SensorSpeedReading_Type = Unsigned32
_SensorSpeedReading_Object = MibTableColumn
sensorSpeedReading = _SensorSpeedReading_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 3),
    _SensorSpeedReading_Type()
)
sensorSpeedReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSpeedReading.setStatus("obsolete")


class _SensorTempStatus_Type(Integer32):
    """Custom type sensorTempStatus based on Integer32"""
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
        *(("failed", 4),
          ("ok", 1),
          ("severe", 3),
          ("warning", 2))
    )


_SensorTempStatus_Type.__name__ = "Integer32"
_SensorTempStatus_Object = MibTableColumn
sensorTempStatus = _SensorTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 4),
    _SensorTempStatus_Type()
)
sensorTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempStatus.setStatus("obsolete")
_SensorTempCReading_Type = Integer32
_SensorTempCReading_Object = MibTableColumn
sensorTempCReading = _SensorTempCReading_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 5),
    _SensorTempCReading_Type()
)
sensorTempCReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempCReading.setStatus("obsolete")
_SensorTempFReading_Type = Integer32
_SensorTempFReading_Object = MibTableColumn
sensorTempFReading = _SensorTempFReading_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 2, 1, 6),
    _SensorTempFReading_Type()
)
sensorTempFReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempFReading.setStatus("obsolete")


class _PsuOneStatus_Type(Integer32):
    """Custom type psuOneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_PsuOneStatus_Type.__name__ = "Integer32"
_PsuOneStatus_Object = MibScalar
psuOneStatus = _PsuOneStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 3),
    _PsuOneStatus_Type()
)
psuOneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuOneStatus.setStatus("obsolete")


class _PsuTwoStatus_Type(Integer32):
    """Custom type psuTwoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_PsuTwoStatus_Type.__name__ = "Integer32"
_PsuTwoStatus_Object = MibScalar
psuTwoStatus = _PsuTwoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 4),
    _PsuTwoStatus_Type()
)
psuTwoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuTwoStatus.setStatus("obsolete")
_OpsPerSecond_Type = Unsigned32
_OpsPerSecond_Object = MibScalar
opsPerSecond = _OpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 5),
    _OpsPerSecond_Type()
)
opsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsPerSecond.setStatus("current")
_FileSystemLoadClient_Type = Integer32
_FileSystemLoadClient_Object = MibScalar
fileSystemLoadClient = _FileSystemLoadClient_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 6),
    _FileSystemLoadClient_Type()
)
fileSystemLoadClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemLoadClient.setStatus("current")
_FileSystemLoadSystem_Type = Integer32
_FileSystemLoadSystem_Object = MibScalar
fileSystemLoadSystem = _FileSystemLoadSystem_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 7),
    _FileSystemLoadSystem_Type()
)
fileSystemLoadSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemLoadSystem.setStatus("current")
_TemperatureSensorNumber_Type = Integer32
_TemperatureSensorNumber_Object = MibScalar
temperatureSensorNumber = _TemperatureSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 8),
    _TemperatureSensorNumber_Type()
)
temperatureSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorNumber.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "temperatureSensorClusterNode"),
    (0, "BLUEARC-SERVER-MIB", "temperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")


class _TemperatureSensorClusterNode_Type(Integer32):
    """Custom type temperatureSensorClusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemperatureSensorClusterNode_Type.__name__ = "Integer32"
_TemperatureSensorClusterNode_Object = MibTableColumn
temperatureSensorClusterNode = _TemperatureSensorClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1, 1),
    _TemperatureSensorClusterNode_Type()
)
temperatureSensorClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorClusterNode.setStatus("current")


class _TemperatureSensorIndex_Type(Integer32):
    """Custom type temperatureSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemperatureSensorIndex_Type.__name__ = "Integer32"
_TemperatureSensorIndex_Object = MibTableColumn
temperatureSensorIndex = _TemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1, 2),
    _TemperatureSensorIndex_Type()
)
temperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorIndex.setStatus("current")


class _TemperatureSensorStatus_Type(Integer32):
    """Custom type temperatureSensorStatus based on Integer32"""
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
        *(("ok", 1),
          ("tempSensorFailed", 4),
          ("tempSensorWarning", 5),
          ("tempSevere", 3),
          ("tempWarning", 2),
          ("unknown", 6))
    )


_TemperatureSensorStatus_Type.__name__ = "Integer32"
_TemperatureSensorStatus_Object = MibTableColumn
temperatureSensorStatus = _TemperatureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1, 3),
    _TemperatureSensorStatus_Type()
)
temperatureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorStatus.setStatus("current")
_TemperatureSensorCReading_Type = Integer32
_TemperatureSensorCReading_Object = MibTableColumn
temperatureSensorCReading = _TemperatureSensorCReading_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1, 4),
    _TemperatureSensorCReading_Type()
)
temperatureSensorCReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorCReading.setStatus("current")
_TemperatureSensorFReading_Type = Integer32
_TemperatureSensorFReading_Object = MibTableColumn
temperatureSensorFReading = _TemperatureSensorFReading_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 9, 1, 5),
    _TemperatureSensorFReading_Type()
)
temperatureSensorFReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorFReading.setStatus("current")
_FanNumber_Type = Integer32
_FanNumber_Object = MibScalar
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 10),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1)
)
fanEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fanClusterNode"),
    (0, "BLUEARC-SERVER-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanClusterNode_Type(Integer32):
    """Custom type fanClusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FanClusterNode_Type.__name__ = "Integer32"
_FanClusterNode_Object = MibTableColumn
fanClusterNode = _FanClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1, 1),
    _FanClusterNode_Type()
)
fanClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanClusterNode.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1, 2),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanFittedStatus_Type(Integer32):
    """Custom type fanFittedStatus based on Integer32"""
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
        *(("notFitted", 3),
          ("ok", 1),
          ("okIdWrong", 2),
          ("unknown", 4))
    )


_FanFittedStatus_Type.__name__ = "Integer32"
_FanFittedStatus_Object = MibTableColumn
fanFittedStatus = _FanFittedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1, 3),
    _FanFittedStatus_Type()
)
fanFittedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFittedStatus.setStatus("current")


class _FanSpeedStatus_Type(Integer32):
    """Custom type fanSpeedStatus based on Integer32"""
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
        *(("ok", 1),
          ("severe", 3),
          ("unknown", 4),
          ("warning", 2))
    )


_FanSpeedStatus_Type.__name__ = "Integer32"
_FanSpeedStatus_Object = MibTableColumn
fanSpeedStatus = _FanSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1, 4),
    _FanSpeedStatus_Type()
)
fanSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedStatus.setStatus("current")
_FanSpeed_Type = Integer32
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 11, 1, 5),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_PsuNumber_Type = Integer32
_PsuNumber_Object = MibScalar
psuNumber = _PsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 12),
    _PsuNumber_Type()
)
psuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuNumber.setStatus("current")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 13, 1)
)
psuEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "psuClusterNode"),
    (0, "BLUEARC-SERVER-MIB", "psuIndex"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")


class _PsuClusterNode_Type(Integer32):
    """Custom type psuClusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PsuClusterNode_Type.__name__ = "Integer32"
_PsuClusterNode_Object = MibTableColumn
psuClusterNode = _PsuClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 13, 1, 1),
    _PsuClusterNode_Type()
)
psuClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuClusterNode.setStatus("current")


class _PsuIndex_Type(Integer32):
    """Custom type psuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PsuIndex_Type.__name__ = "Integer32"
_PsuIndex_Object = MibTableColumn
psuIndex = _PsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 13, 1, 2),
    _PsuIndex_Type()
)
psuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuIndex.setStatus("current")


class _PsuStatus_Type(Integer32):
    """Custom type psuStatus based on Integer32"""
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
        *(("failed", 2),
          ("notFitted", 3),
          ("ok", 1),
          ("unknown", 4))
    )


_PsuStatus_Type.__name__ = "Integer32"
_PsuStatus_Object = MibTableColumn
psuStatus = _PsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 1, 13, 1, 3),
    _PsuStatus_Type()
)
psuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuStatus.setStatus("current")
_Locale_ObjectIdentity = ObjectIdentity
locale = _Locale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2)
)
_ServerDate_Type = DisplayString
_ServerDate_Object = MibScalar
serverDate = _ServerDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 1),
    _ServerDate_Type()
)
serverDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverDate.setStatus("current")
_ServerTime_Type = DisplayString
_ServerTime_Object = MibScalar
serverTime = _ServerTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 2),
    _ServerTime_Type()
)
serverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTime.setStatus("current")
_UtcOffset_Type = Integer32
_UtcOffset_Object = MibScalar
utcOffset = _UtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 3),
    _UtcOffset_Type()
)
utcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utcOffset.setStatus("current")


class _DaylightSavings_Type(Integer32):
    """Custom type daylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daylightSavings", 1),
          ("noDaylightSavings", 2),
          ("unknown", 3))
    )


_DaylightSavings_Type.__name__ = "Integer32"
_DaylightSavings_Object = MibScalar
daylightSavings = _DaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 4),
    _DaylightSavings_Type()
)
daylightSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daylightSavings.setStatus("current")
_NtpServerNumber_Type = Integer32
_NtpServerNumber_Object = MibScalar
ntpServerNumber = _NtpServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 5),
    _NtpServerNumber_Type()
)
ntpServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerNumber.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 6, 1)
)
ntpServerEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "ntpServerHost"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerHost_Type = DisplayString
_NtpServerHost_Object = MibTableColumn
ntpServerHost = _NtpServerHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 2, 6, 1, 1),
    _NtpServerHost_Type()
)
ntpServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerHost.setStatus("current")
_Failover_ObjectIdentity = ObjectIdentity
failover = _Failover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3)
)


class _FailoverConfigStatus_Type(Integer32):
    """Custom type failoverConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("notConfigured", 2))
    )


_FailoverConfigStatus_Type.__name__ = "Integer32"
_FailoverConfigStatus_Object = MibScalar
failoverConfigStatus = _FailoverConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 1),
    _FailoverConfigStatus_Type()
)
failoverConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverConfigStatus.setStatus("obsolete")
_FailoverPrimaryName_Type = DisplayString
_FailoverPrimaryName_Object = MibScalar
failoverPrimaryName = _FailoverPrimaryName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 2),
    _FailoverPrimaryName_Type()
)
failoverPrimaryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverPrimaryName.setStatus("obsolete")
_FailoverSystemName_Type = DisplayString
_FailoverSystemName_Object = MibScalar
failoverSystemName = _FailoverSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 3),
    _FailoverSystemName_Type()
)
failoverSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSystemName.setStatus("obsolete")
_FailoverSecondaryName_Type = DisplayString
_FailoverSecondaryName_Object = MibScalar
failoverSecondaryName = _FailoverSecondaryName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 4),
    _FailoverSecondaryName_Type()
)
failoverSecondaryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSecondaryName.setStatus("obsolete")
_FailoverPrimaryIpAddr_Type = IpAddress
_FailoverPrimaryIpAddr_Object = MibScalar
failoverPrimaryIpAddr = _FailoverPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 5),
    _FailoverPrimaryIpAddr_Type()
)
failoverPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverPrimaryIpAddr.setStatus("obsolete")
_FailoverSystemIpAddr_Type = IpAddress
_FailoverSystemIpAddr_Object = MibScalar
failoverSystemIpAddr = _FailoverSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 6),
    _FailoverSystemIpAddr_Type()
)
failoverSystemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSystemIpAddr.setStatus("obsolete")
_FailoverSecondaryIpAddr_Type = IpAddress
_FailoverSecondaryIpAddr_Object = MibScalar
failoverSecondaryIpAddr = _FailoverSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 7),
    _FailoverSecondaryIpAddr_Type()
)
failoverSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSecondaryIpAddr.setStatus("obsolete")


class _FailoverPrimaryStatus_Type(Integer32):
    """Custom type failoverPrimaryStatus based on Integer32"""
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
        *(("master", 2),
          ("notConfigured", 1),
          ("notDetected", 4),
          ("standby", 3),
          ("unknown", 5))
    )


_FailoverPrimaryStatus_Type.__name__ = "Integer32"
_FailoverPrimaryStatus_Object = MibScalar
failoverPrimaryStatus = _FailoverPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 8),
    _FailoverPrimaryStatus_Type()
)
failoverPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverPrimaryStatus.setStatus("obsolete")


class _FailoverSecondaryStatus_Type(Integer32):
    """Custom type failoverSecondaryStatus based on Integer32"""
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
        *(("master", 2),
          ("notConfigured", 1),
          ("notDetected", 4),
          ("standby", 3),
          ("unknown", 5))
    )


_FailoverSecondaryStatus_Type.__name__ = "Integer32"
_FailoverSecondaryStatus_Object = MibScalar
failoverSecondaryStatus = _FailoverSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 3, 9),
    _FailoverSecondaryStatus_Type()
)
failoverSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSecondaryStatus.setStatus("obsolete")
_Cache_ObjectIdentity = ObjectIdentity
cache = _Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4)
)
_SectorCache_ObjectIdentity = ObjectIdentity
sectorCache = _SectorCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 1)
)


class _SectorCacheMode_Type(Integer32):
    """Custom type sectorCacheMode based on Integer32"""
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
        *(("disabled", 4),
          ("ramdisk", 1),
          ("unknown", 5),
          ("writeBack", 3),
          ("writeThrough", 2))
    )


_SectorCacheMode_Type.__name__ = "Integer32"
_SectorCacheMode_Object = MibScalar
sectorCacheMode = _SectorCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 1, 1),
    _SectorCacheMode_Type()
)
sectorCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheMode.setStatus("current")


class _SectorCacheDirtyPageWtmk_Type(Integer32):
    """Custom type sectorCacheDirtyPageWtmk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SectorCacheDirtyPageWtmk_Type.__name__ = "Integer32"
_SectorCacheDirtyPageWtmk_Object = MibScalar
sectorCacheDirtyPageWtmk = _SectorCacheDirtyPageWtmk_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 1, 2),
    _SectorCacheDirtyPageWtmk_Type()
)
sectorCacheDirtyPageWtmk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheDirtyPageWtmk.setStatus("obsolete")


class _SectorCacheDirtyPageTimeout_Type(Integer32):
    """Custom type sectorCacheDirtyPageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655),
    )


_SectorCacheDirtyPageTimeout_Type.__name__ = "Integer32"
_SectorCacheDirtyPageTimeout_Object = MibScalar
sectorCacheDirtyPageTimeout = _SectorCacheDirtyPageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 1, 3),
    _SectorCacheDirtyPageTimeout_Type()
)
sectorCacheDirtyPageTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheDirtyPageTimeout.setStatus("current")
_FileSysCache_ObjectIdentity = ObjectIdentity
fileSysCache = _FileSysCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 2)
)


class _FileSysCacheMode_Type(Integer32):
    """Custom type fileSysCacheMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeBack", 2),
          ("writeThrough", 1))
    )


_FileSysCacheMode_Type.__name__ = "Integer32"
_FileSysCacheMode_Object = MibScalar
fileSysCacheMode = _FileSysCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 2, 1),
    _FileSysCacheMode_Type()
)
fileSysCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSysCacheMode.setStatus("obsolete")


class _FileSysTransactionLogging_Type(Integer32):
    """Custom type fileSysTransactionLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FileSysTransactionLogging_Type.__name__ = "Integer32"
_FileSysTransactionLogging_Object = MibScalar
fileSysTransactionLogging = _FileSysTransactionLogging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 2, 2),
    _FileSysTransactionLogging_Type()
)
fileSysTransactionLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSysTransactionLogging.setStatus("obsolete")


class _FileSysCacheTimeout_Type(Integer32):
    """Custom type fileSysCacheTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_FileSysCacheTimeout_Type.__name__ = "Integer32"
_FileSysCacheTimeout_Object = MibScalar
fileSysCacheTimeout = _FileSysCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 2, 3),
    _FileSysCacheTimeout_Type()
)
fileSysCacheTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSysCacheTimeout.setStatus("obsolete")


class _FileSysUpdateLastAccess_Type(Integer32):
    """Custom type fileSysUpdateLastAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FileSysUpdateLastAccess_Type.__name__ = "Integer32"
_FileSysUpdateLastAccess_Object = MibScalar
fileSysUpdateLastAccess = _FileSysUpdateLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 4, 2, 4),
    _FileSysUpdateLastAccess_Type()
)
fileSysUpdateLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSysUpdateLastAccess.setStatus("current")
_Clustering_ObjectIdentity = ObjectIdentity
clustering = _Clustering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5)
)
_ClusterName_Type = DisplayString
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 1),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")
_ClusterUuid_Type = DisplayString
_ClusterUuid_Object = MibScalar
clusterUuid = _ClusterUuid_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 2),
    _ClusterUuid_Type()
)
clusterUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterUuid.setStatus("current")


class _ClusterConfig_Type(Integer32):
    """Custom type clusterConfig based on Integer32"""
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
        *(("activeActive", 3),
          ("activeStandby", 2),
          ("singleNode", 1),
          ("unknown", 4))
    )


_ClusterConfig_Type.__name__ = "Integer32"
_ClusterConfig_Object = MibScalar
clusterConfig = _ClusterConfig_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 3),
    _ClusterConfig_Type()
)
clusterConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConfig.setStatus("current")
_ClusterQuorumDeviceName_Type = DisplayString
_ClusterQuorumDeviceName_Object = MibScalar
clusterQuorumDeviceName = _ClusterQuorumDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 4),
    _ClusterQuorumDeviceName_Type()
)
clusterQuorumDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterQuorumDeviceName.setStatus("current")
_ClusterQuorumDeviceIpAddr_Type = IpAddress
_ClusterQuorumDeviceIpAddr_Object = MibScalar
clusterQuorumDeviceIpAddr = _ClusterQuorumDeviceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 5),
    _ClusterQuorumDeviceIpAddr_Type()
)
clusterQuorumDeviceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterQuorumDeviceIpAddr.setStatus("current")
_ClusterQuorumDeviceOwnedByPNode_Type = Integer32
_ClusterQuorumDeviceOwnedByPNode_Object = MibScalar
clusterQuorumDeviceOwnedByPNode = _ClusterQuorumDeviceOwnedByPNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 6),
    _ClusterQuorumDeviceOwnedByPNode_Type()
)
clusterQuorumDeviceOwnedByPNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterQuorumDeviceOwnedByPNode.setStatus("current")


class _ClusterQuorumDeviceStatus_Type(Integer32):
    """Custom type clusterQuorumDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clusterNodeNotUp", 6),
          ("configured", 4),
          ("granted", 5),
          ("misconfigured", 7),
          ("offLine", 2),
          ("owned", 3),
          ("unconfigured", 1),
          ("unknown", 0))
    )


_ClusterQuorumDeviceStatus_Type.__name__ = "Integer32"
_ClusterQuorumDeviceStatus_Object = MibScalar
clusterQuorumDeviceStatus = _ClusterQuorumDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 7),
    _ClusterQuorumDeviceStatus_Type()
)
clusterQuorumDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterQuorumDeviceStatus.setStatus("current")
_ClusterPNodeNumber_Type = Integer32
_ClusterPNodeNumber_Object = MibScalar
clusterPNodeNumber = _ClusterPNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 8),
    _ClusterPNodeNumber_Type()
)
clusterPNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPNodeNumber.setStatus("current")
_ClusterPNodeTable_Object = MibTable
clusterPNodeTable = _ClusterPNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9)
)
if mibBuilder.loadTexts:
    clusterPNodeTable.setStatus("current")
_ClusterPNodeEntry_Object = MibTableRow
clusterPNodeEntry = _ClusterPNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9, 1)
)
clusterPNodeEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "clusterPNodeId"),
)
if mibBuilder.loadTexts:
    clusterPNodeEntry.setStatus("current")


class _ClusterPNodeId_Type(Integer32):
    """Custom type clusterPNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterPNodeId_Type.__name__ = "Integer32"
_ClusterPNodeId_Object = MibTableColumn
clusterPNodeId = _ClusterPNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9, 1, 1),
    _ClusterPNodeId_Type()
)
clusterPNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPNodeId.setStatus("current")
_ClusterPNodeName_Type = DisplayString
_ClusterPNodeName_Object = MibTableColumn
clusterPNodeName = _ClusterPNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9, 1, 2),
    _ClusterPNodeName_Type()
)
clusterPNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPNodeName.setStatus("current")
_ClusterPNodeIpAddr_Type = IpAddress
_ClusterPNodeIpAddr_Object = MibTableColumn
clusterPNodeIpAddr = _ClusterPNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9, 1, 3),
    _ClusterPNodeIpAddr_Type()
)
clusterPNodeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPNodeIpAddr.setStatus("current")


class _ClusterPNodeStatus_Type(Integer32):
    """Custom type clusterPNodeStatus based on Integer32"""
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
        *(("dead", 5),
          ("dormant", 6),
          ("notUp", 3),
          ("onLine", 4),
          ("unknown", 1),
          ("up", 2))
    )


_ClusterPNodeStatus_Type.__name__ = "Integer32"
_ClusterPNodeStatus_Object = MibTableColumn
clusterPNodeStatus = _ClusterPNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 9, 1, 4),
    _ClusterPNodeStatus_Type()
)
clusterPNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPNodeStatus.setStatus("current")
_ClusterVNodeNumber_Type = Integer32
_ClusterVNodeNumber_Object = MibScalar
clusterVNodeNumber = _ClusterVNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 10),
    _ClusterVNodeNumber_Type()
)
clusterVNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeNumber.setStatus("current")
_ClusterVNodeTable_Object = MibTable
clusterVNodeTable = _ClusterVNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11)
)
if mibBuilder.loadTexts:
    clusterVNodeTable.setStatus("current")
_ClusterVNodeEntry_Object = MibTableRow
clusterVNodeEntry = _ClusterVNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1)
)
clusterVNodeEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "clusterVNodeId"),
)
if mibBuilder.loadTexts:
    clusterVNodeEntry.setStatus("current")


class _ClusterVNodeId_Type(Integer32):
    """Custom type clusterVNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterVNodeId_Type.__name__ = "Integer32"
_ClusterVNodeId_Object = MibTableColumn
clusterVNodeId = _ClusterVNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 1),
    _ClusterVNodeId_Type()
)
clusterVNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeId.setStatus("current")
_ClusterVNodeName_Type = DisplayString
_ClusterVNodeName_Object = MibTableColumn
clusterVNodeName = _ClusterVNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 2),
    _ClusterVNodeName_Type()
)
clusterVNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeName.setStatus("current")
_ClusterVNodeIpAddr_Type = IpAddress
_ClusterVNodeIpAddr_Object = MibTableColumn
clusterVNodeIpAddr = _ClusterVNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 3),
    _ClusterVNodeIpAddr_Type()
)
clusterVNodeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeIpAddr.setStatus("current")


class _ClusterVNodeStatus_Type(Integer32):
    """Custom type clusterVNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 3),
          ("onLine", 2),
          ("unknown", 1))
    )


_ClusterVNodeStatus_Type.__name__ = "Integer32"
_ClusterVNodeStatus_Object = MibTableColumn
clusterVNodeStatus = _ClusterVNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 4),
    _ClusterVNodeStatus_Type()
)
clusterVNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeStatus.setStatus("current")


class _ClusterVNodeAdmin_Type(Integer32):
    """Custom type clusterVNodeAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_ClusterVNodeAdmin_Type.__name__ = "Integer32"
_ClusterVNodeAdmin_Object = MibTableColumn
clusterVNodeAdmin = _ClusterVNodeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 5),
    _ClusterVNodeAdmin_Type()
)
clusterVNodeAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeAdmin.setStatus("current")
_ClusterVNodeHostedBy_Type = Integer32
_ClusterVNodeHostedBy_Object = MibTableColumn
clusterVNodeHostedBy = _ClusterVNodeHostedBy_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 5, 11, 1, 6),
    _ClusterVNodeHostedBy_Type()
)
clusterVNodeHostedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVNodeHostedBy.setStatus("current")
_SerialNumbers_ObjectIdentity = ObjectIdentity
serialNumbers = _SerialNumbers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6)
)
_SerialNumberTable_Object = MibTable
serialNumberTable = _SerialNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    serialNumberTable.setStatus("current")
_SerialNumberEntry_Object = MibTableRow
serialNumberEntry = _SerialNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1, 1)
)
serialNumberEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "componentType"),
    (0, "BLUEARC-SERVER-MIB", "subComponentType"),
    (0, "BLUEARC-SERVER-MIB", "clusterNode"),
)
if mibBuilder.loadTexts:
    serialNumberEntry.setStatus("current")


class _ComponentType_Type(Integer32):
    """Custom type componentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blade", 2),
          ("chassis", 1),
          ("psu", 3))
    )


_ComponentType_Type.__name__ = "Integer32"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1, 1, 1),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("current")


class _SubComponentType_Type(Integer32):
    """Custom type subComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 12),
          ("fsa1", 5),
          ("fsa17455", 4),
          ("fsa2", 6),
          ("fsb1", 8),
          ("fsb2", 9),
          ("fsb3", 15),
          ("fsx1", 7),
          ("mcp1", 17),
          ("mfb1", 19),
          ("mmb1", 18),
          ("nim1", 1),
          ("nim2", 2),
          ("nim3", 3),
          ("psu1", 13),
          ("psu2", 14),
          ("sim1", 10),
          ("sim2", 11),
          ("sim3", 16),
          ("unknown", 0))
    )


_SubComponentType_Type.__name__ = "Integer32"
_SubComponentType_Object = MibTableColumn
subComponentType = _SubComponentType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1, 1, 2),
    _SubComponentType_Type()
)
subComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subComponentType.setStatus("current")


class _ClusterNode_Type(Integer32):
    """Custom type clusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterNode_Type.__name__ = "Integer32"
_ClusterNode_Object = MibTableColumn
clusterNode = _ClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1, 1, 3),
    _ClusterNode_Type()
)
clusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNode.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 2, 6, 1, 1, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3)
)
_Racks_ObjectIdentity = ObjectIdentity
racks = _Racks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1)
)
_RackNumber_Type = Integer32
_RackNumber_Object = MibScalar
rackNumber = _RackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 1),
    _RackNumber_Type()
)
rackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackNumber.setStatus("obsolete")
_RackTable_Object = MibTable
rackTable = _RackTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    rackTable.setStatus("obsolete")
_RackEntry_Object = MibTableRow
rackEntry = _RackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2, 1)
)
rackEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "rackIndex"),
)
if mibBuilder.loadTexts:
    rackEntry.setStatus("obsolete")


class _RackIndex_Type(Integer32):
    """Custom type rackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RackIndex_Type.__name__ = "Integer32"
_RackIndex_Object = MibTableColumn
rackIndex = _RackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2, 1, 1),
    _RackIndex_Type()
)
rackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackIndex.setStatus("obsolete")


class _RackStatus_Type(Integer32):
    """Custom type rackStatus based on Integer32"""
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
        *(("loopFailed", 3),
          ("ok", 1),
          ("otherFailure", 4),
          ("storageFailed", 2))
    )


_RackStatus_Type.__name__ = "Integer32"
_RackStatus_Object = MibTableColumn
rackStatus = _RackStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2, 1, 2),
    _RackStatus_Type()
)
rackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackStatus.setStatus("obsolete")
_RackNumberOfEnclosures_Type = Unsigned32
_RackNumberOfEnclosures_Object = MibTableColumn
rackNumberOfEnclosures = _RackNumberOfEnclosures_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2, 1, 3),
    _RackNumberOfEnclosures_Type()
)
rackNumberOfEnclosures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackNumberOfEnclosures.setStatus("obsolete")
_RackNumberOfPhysicalDrives_Type = Unsigned32
_RackNumberOfPhysicalDrives_Object = MibTableColumn
rackNumberOfPhysicalDrives = _RackNumberOfPhysicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 1, 2, 1, 4),
    _RackNumberOfPhysicalDrives_Type()
)
rackNumberOfPhysicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackNumberOfPhysicalDrives.setStatus("obsolete")
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2)
)
_Controllers_ObjectIdentity = ObjectIdentity
controllers = _Controllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1)
)
_RaidControllerTable_Object = MibTable
raidControllerTable = _RaidControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    raidControllerTable.setStatus("obsolete")
_RaidControllerEntry_Object = MibTableRow
raidControllerEntry = _RaidControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1)
)
raidControllerEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "raidControllerRackIndex"),
)
if mibBuilder.loadTexts:
    raidControllerEntry.setStatus("obsolete")


class _RaidControllerRackIndex_Type(Integer32):
    """Custom type raidControllerRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RaidControllerRackIndex_Type.__name__ = "Integer32"
_RaidControllerRackIndex_Object = MibTableColumn
raidControllerRackIndex = _RaidControllerRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 1),
    _RaidControllerRackIndex_Type()
)
raidControllerRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerRackIndex.setStatus("obsolete")
_RaidControllerWWN_Type = DisplayString
_RaidControllerWWN_Object = MibTableColumn
raidControllerWWN = _RaidControllerWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 2),
    _RaidControllerWWN_Type()
)
raidControllerWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerWWN.setStatus("obsolete")


class _RaidControllerPrimaryStatus_Type(Integer32):
    """Custom type raidControllerPrimaryStatus based on Integer32"""
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
        *(("failed", 2),
          ("inserted", 5),
          ("notPresent", 3),
          ("offline", 6),
          ("online", 1),
          ("unknown", 4))
    )


_RaidControllerPrimaryStatus_Type.__name__ = "Integer32"
_RaidControllerPrimaryStatus_Object = MibTableColumn
raidControllerPrimaryStatus = _RaidControllerPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 3),
    _RaidControllerPrimaryStatus_Type()
)
raidControllerPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerPrimaryStatus.setStatus("obsolete")


class _RaidControllerSecondaryStatus_Type(Integer32):
    """Custom type raidControllerSecondaryStatus based on Integer32"""
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
        *(("failed", 2),
          ("notPresent", 3),
          ("online", 1),
          ("unknown", 4))
    )


_RaidControllerSecondaryStatus_Type.__name__ = "Integer32"
_RaidControllerSecondaryStatus_Object = MibTableColumn
raidControllerSecondaryStatus = _RaidControllerSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 4),
    _RaidControllerSecondaryStatus_Type()
)
raidControllerSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerSecondaryStatus.setStatus("obsolete")
_RaidControllerManufacturer_Type = DisplayString
_RaidControllerManufacturer_Object = MibTableColumn
raidControllerManufacturer = _RaidControllerManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 5),
    _RaidControllerManufacturer_Type()
)
raidControllerManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerManufacturer.setStatus("obsolete")
_RaidControllerModel_Type = DisplayString
_RaidControllerModel_Object = MibTableColumn
raidControllerModel = _RaidControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 6),
    _RaidControllerModel_Type()
)
raidControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerModel.setStatus("obsolete")
_RaidControllerCacheSize_Type = Unsigned32
_RaidControllerCacheSize_Object = MibTableColumn
raidControllerCacheSize = _RaidControllerCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 1, 1, 7),
    _RaidControllerCacheSize_Type()
)
raidControllerCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerCacheSize.setStatus("obsolete")
_RaidControllerConfigTable_Object = MibTable
raidControllerConfigTable = _RaidControllerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    raidControllerConfigTable.setStatus("obsolete")
_RaidControllerConfigEntry_Object = MibTableRow
raidControllerConfigEntry = _RaidControllerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1)
)
raidControllerConfigEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "raidControllerConfigRackIndex"),
)
if mibBuilder.loadTexts:
    raidControllerConfigEntry.setStatus("obsolete")


class _RaidControllerConfigRackIndex_Type(Integer32):
    """Custom type raidControllerConfigRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RaidControllerConfigRackIndex_Type.__name__ = "Integer32"
_RaidControllerConfigRackIndex_Object = MibTableColumn
raidControllerConfigRackIndex = _RaidControllerConfigRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 1),
    _RaidControllerConfigRackIndex_Type()
)
raidControllerConfigRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigRackIndex.setStatus("obsolete")
_RaidControllerConfigDRAMSize_Type = Unsigned32
_RaidControllerConfigDRAMSize_Object = MibTableColumn
raidControllerConfigDRAMSize = _RaidControllerConfigDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 2),
    _RaidControllerConfigDRAMSize_Type()
)
raidControllerConfigDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigDRAMSize.setStatus("obsolete")
_RaidControllerConfigFlashSize_Type = Unsigned32
_RaidControllerConfigFlashSize_Object = MibTableColumn
raidControllerConfigFlashSize = _RaidControllerConfigFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 3),
    _RaidControllerConfigFlashSize_Type()
)
raidControllerConfigFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFlashSize.setStatus("obsolete")
_RaidControllerConfigNVRSize_Type = Unsigned32
_RaidControllerConfigNVRSize_Object = MibTableColumn
raidControllerConfigNVRSize = _RaidControllerConfigNVRSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 4),
    _RaidControllerConfigNVRSize_Type()
)
raidControllerConfigNVRSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigNVRSize.setStatus("obsolete")
_RaidControllerConfigClockSpeed_Type = Unsigned32
_RaidControllerConfigClockSpeed_Object = MibTableColumn
raidControllerConfigClockSpeed = _RaidControllerConfigClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 5),
    _RaidControllerConfigClockSpeed_Type()
)
raidControllerConfigClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigClockSpeed.setStatus("obsolete")
_RaidControllerConfigMemAccess_Type = Unsigned32
_RaidControllerConfigMemAccess_Object = MibTableColumn
raidControllerConfigMemAccess = _RaidControllerConfigMemAccess_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 6),
    _RaidControllerConfigMemAccess_Type()
)
raidControllerConfigMemAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMemAccess.setStatus("obsolete")
_RaidControllerConfigMemCycle_Type = Unsigned32
_RaidControllerConfigMemCycle_Object = MibTableColumn
raidControllerConfigMemCycle = _RaidControllerConfigMemCycle_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 7),
    _RaidControllerConfigMemCycle_Type()
)
raidControllerConfigMemCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMemCycle.setStatus("obsolete")
_RaidControllerConfigPhysicalSectorSize_Type = Unsigned32
_RaidControllerConfigPhysicalSectorSize_Object = MibTableColumn
raidControllerConfigPhysicalSectorSize = _RaidControllerConfigPhysicalSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 8),
    _RaidControllerConfigPhysicalSectorSize_Type()
)
raidControllerConfigPhysicalSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigPhysicalSectorSize.setStatus("obsolete")
_RaidControllerConfigLogicalSectorSize_Type = Unsigned32
_RaidControllerConfigLogicalSectorSize_Object = MibTableColumn
raidControllerConfigLogicalSectorSize = _RaidControllerConfigLogicalSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 9),
    _RaidControllerConfigLogicalSectorSize_Type()
)
raidControllerConfigLogicalSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigLogicalSectorSize.setStatus("obsolete")
_RaidControllerConfigMaxSystemDrives_Type = Unsigned32
_RaidControllerConfigMaxSystemDrives_Object = MibTableColumn
raidControllerConfigMaxSystemDrives = _RaidControllerConfigMaxSystemDrives_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 10),
    _RaidControllerConfigMaxSystemDrives_Type()
)
raidControllerConfigMaxSystemDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMaxSystemDrives.setStatus("obsolete")
_RaidControllerConfigMaxDrivesPerSystemDrive_Type = Unsigned32
_RaidControllerConfigMaxDrivesPerSystemDrive_Object = MibTableColumn
raidControllerConfigMaxDrivesPerSystemDrive = _RaidControllerConfigMaxDrivesPerSystemDrive_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 11),
    _RaidControllerConfigMaxDrivesPerSystemDrive_Type()
)
raidControllerConfigMaxDrivesPerSystemDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMaxDrivesPerSystemDrive.setStatus("obsolete")
_RaidControllerConfigMaxSpanPerVirtualDrive_Type = Unsigned32
_RaidControllerConfigMaxSpanPerVirtualDrive_Object = MibTableColumn
raidControllerConfigMaxSpanPerVirtualDrive = _RaidControllerConfigMaxSpanPerVirtualDrive_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 12),
    _RaidControllerConfigMaxSpanPerVirtualDrive_Type()
)
raidControllerConfigMaxSpanPerVirtualDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMaxSpanPerVirtualDrive.setStatus("obsolete")
_RaidControllerConfigFirmwareVersion_Type = DisplayString
_RaidControllerConfigFirmwareVersion_Object = MibTableColumn
raidControllerConfigFirmwareVersion = _RaidControllerConfigFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 13),
    _RaidControllerConfigFirmwareVersion_Type()
)
raidControllerConfigFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFirmwareVersion.setStatus("obsolete")
_RaidControllerConfigFirmwareType_Type = Unsigned32
_RaidControllerConfigFirmwareType_Object = MibTableColumn
raidControllerConfigFirmwareType = _RaidControllerConfigFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 14),
    _RaidControllerConfigFirmwareType_Type()
)
raidControllerConfigFirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFirmwareType.setStatus("obsolete")
_RaidControllerConfigFirmwareMajor_Type = Unsigned32
_RaidControllerConfigFirmwareMajor_Object = MibTableColumn
raidControllerConfigFirmwareMajor = _RaidControllerConfigFirmwareMajor_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 15),
    _RaidControllerConfigFirmwareMajor_Type()
)
raidControllerConfigFirmwareMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFirmwareMajor.setStatus("obsolete")
_RaidControllerConfigFirmwareMinor_Type = Unsigned32
_RaidControllerConfigFirmwareMinor_Object = MibTableColumn
raidControllerConfigFirmwareMinor = _RaidControllerConfigFirmwareMinor_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 16),
    _RaidControllerConfigFirmwareMinor_Type()
)
raidControllerConfigFirmwareMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFirmwareMinor.setStatus("obsolete")
_RaidControllerConfigMaximumCommands_Type = Unsigned32
_RaidControllerConfigMaximumCommands_Object = MibTableColumn
raidControllerConfigMaximumCommands = _RaidControllerConfigMaximumCommands_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 17),
    _RaidControllerConfigMaximumCommands_Type()
)
raidControllerConfigMaximumCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigMaximumCommands.setStatus("obsolete")
_RaidControllerConfigFirmwareBuild_Type = Unsigned32
_RaidControllerConfigFirmwareBuild_Object = MibTableColumn
raidControllerConfigFirmwareBuild = _RaidControllerConfigFirmwareBuild_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 18),
    _RaidControllerConfigFirmwareBuild_Type()
)
raidControllerConfigFirmwareBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigFirmwareBuild.setStatus("obsolete")
_RaidControllerConfigRebuildRate_Type = Unsigned32
_RaidControllerConfigRebuildRate_Object = MibTableColumn
raidControllerConfigRebuildRate = _RaidControllerConfigRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 19),
    _RaidControllerConfigRebuildRate_Type()
)
raidControllerConfigRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigRebuildRate.setStatus("obsolete")
_RaidControllerConfigRebuildUnit_Type = Unsigned32
_RaidControllerConfigRebuildUnit_Object = MibTableColumn
raidControllerConfigRebuildUnit = _RaidControllerConfigRebuildUnit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 20),
    _RaidControllerConfigRebuildUnit_Type()
)
raidControllerConfigRebuildUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigRebuildUnit.setStatus("obsolete")
_RaidControllerConfigRebuildOn_Type = Unsigned32
_RaidControllerConfigRebuildOn_Object = MibTableColumn
raidControllerConfigRebuildOn = _RaidControllerConfigRebuildOn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 21),
    _RaidControllerConfigRebuildOn_Type()
)
raidControllerConfigRebuildOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigRebuildOn.setStatus("obsolete")
_RaidControllerConfigRebuildOff_Type = Unsigned32
_RaidControllerConfigRebuildOff_Object = MibTableColumn
raidControllerConfigRebuildOff = _RaidControllerConfigRebuildOff_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 2, 1, 22),
    _RaidControllerConfigRebuildOff_Type()
)
raidControllerConfigRebuildOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerConfigRebuildOff.setStatus("obsolete")
_RaidControllerBatteryBackupTable_Object = MibTable
raidControllerBatteryBackupTable = _RaidControllerBatteryBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    raidControllerBatteryBackupTable.setStatus("obsolete")
_RaidControllerBatteryBackupEntry_Object = MibTableRow
raidControllerBatteryBackupEntry = _RaidControllerBatteryBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1)
)
raidControllerBatteryBackupEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "raidControllerBatteryBackupRackIndex"),
)
if mibBuilder.loadTexts:
    raidControllerBatteryBackupEntry.setStatus("obsolete")


class _RaidControllerBatteryBackupRackIndex_Type(Integer32):
    """Custom type raidControllerBatteryBackupRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RaidControllerBatteryBackupRackIndex_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupRackIndex_Object = MibTableColumn
raidControllerBatteryBackupRackIndex = _RaidControllerBatteryBackupRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 1),
    _RaidControllerBatteryBackupRackIndex_Type()
)
raidControllerBatteryBackupRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupRackIndex.setStatus("obsolete")


class _RaidControllerBatteryBackupNoSync_Type(Integer32):
    """Custom type raidControllerBatteryBackupNoSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 1),
          ("sync", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupNoSync_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupNoSync_Object = MibTableColumn
raidControllerBatteryBackupNoSync = _RaidControllerBatteryBackupNoSync_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 2),
    _RaidControllerBatteryBackupNoSync_Type()
)
raidControllerBatteryBackupNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupNoSync.setStatus("obsolete")


class _RaidControllerBatteryBackupOutOfSync_Type(Integer32):
    """Custom type raidControllerBatteryBackupOutOfSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("outOfsync", 1),
          ("sync", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupOutOfSync_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupOutOfSync_Object = MibTableColumn
raidControllerBatteryBackupOutOfSync = _RaidControllerBatteryBackupOutOfSync_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 3),
    _RaidControllerBatteryBackupOutOfSync_Type()
)
raidControllerBatteryBackupOutOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupOutOfSync.setStatus("obsolete")


class _RaidControllerBatteryBackupFirstWarning_Type(Integer32):
    """Custom type raidControllerBatteryBackupFirstWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firstWarning", 1),
          ("noFirstWarning", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupFirstWarning_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupFirstWarning_Object = MibTableColumn
raidControllerBatteryBackupFirstWarning = _RaidControllerBatteryBackupFirstWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 4),
    _RaidControllerBatteryBackupFirstWarning_Type()
)
raidControllerBatteryBackupFirstWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupFirstWarning.setStatus("obsolete")


class _RaidControllerBatteryBackupSecondWarning_Type(Integer32):
    """Custom type raidControllerBatteryBackupSecondWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSecondWarning", 2),
          ("secondWarning", 1),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupSecondWarning_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupSecondWarning_Object = MibTableColumn
raidControllerBatteryBackupSecondWarning = _RaidControllerBatteryBackupSecondWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 5),
    _RaidControllerBatteryBackupSecondWarning_Type()
)
raidControllerBatteryBackupSecondWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupSecondWarning.setStatus("obsolete")


class _RaidControllerBatteryBackupReconditioning_Type(Integer32):
    """Custom type raidControllerBatteryBackupReconditioning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReconditioning", 2),
          ("reconditioning", 1),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupReconditioning_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupReconditioning_Object = MibTableColumn
raidControllerBatteryBackupReconditioning = _RaidControllerBatteryBackupReconditioning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 6),
    _RaidControllerBatteryBackupReconditioning_Type()
)
raidControllerBatteryBackupReconditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupReconditioning.setStatus("obsolete")


class _RaidControllerBatteryBackupDischarging_Type(Integer32):
    """Custom type raidControllerBatteryBackupDischarging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discharging", 1),
          ("notDischarging", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupDischarging_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupDischarging_Object = MibTableColumn
raidControllerBatteryBackupDischarging = _RaidControllerBatteryBackupDischarging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 7),
    _RaidControllerBatteryBackupDischarging_Type()
)
raidControllerBatteryBackupDischarging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupDischarging.setStatus("obsolete")


class _RaidControllerBatteryBackupFastCharging_Type(Integer32):
    """Custom type raidControllerBatteryBackupFastCharging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastCharging", 1),
          ("notFastCharging", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupFastCharging_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupFastCharging_Object = MibTableColumn
raidControllerBatteryBackupFastCharging = _RaidControllerBatteryBackupFastCharging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 8),
    _RaidControllerBatteryBackupFastCharging_Type()
)
raidControllerBatteryBackupFastCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupFastCharging.setStatus("obsolete")


class _RaidControllerBatteryBackupLowPower_Type(Integer32):
    """Custom type raidControllerBatteryBackupLowPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowPowerAlarm", 1),
          ("noLowPowerAlarm", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupLowPower_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupLowPower_Object = MibTableColumn
raidControllerBatteryBackupLowPower = _RaidControllerBatteryBackupLowPower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 9),
    _RaidControllerBatteryBackupLowPower_Type()
)
raidControllerBatteryBackupLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupLowPower.setStatus("obsolete")


class _RaidControllerBatteryBackupChargePercent_Type(Integer32):
    """Custom type raidControllerBatteryBackupChargePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidControllerBatteryBackupChargePercent_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupChargePercent_Object = MibTableColumn
raidControllerBatteryBackupChargePercent = _RaidControllerBatteryBackupChargePercent_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 10),
    _RaidControllerBatteryBackupChargePercent_Type()
)
raidControllerBatteryBackupChargePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupChargePercent.setStatus("obsolete")
_RaidControllerBatteryBackupHardwareVersion_Type = Unsigned32
_RaidControllerBatteryBackupHardwareVersion_Object = MibTableColumn
raidControllerBatteryBackupHardwareVersion = _RaidControllerBatteryBackupHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 11),
    _RaidControllerBatteryBackupHardwareVersion_Type()
)
raidControllerBatteryBackupHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupHardwareVersion.setStatus("obsolete")


class _RaidControllerBatteryBackupBatteryType_Type(Integer32):
    """Custom type raidControllerBatteryBackupBatteryType based on Integer32"""
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
        *(("lion", 5),
          ("niCd", 1),
          ("niMH", 4),
          ("none", 2),
          ("unknown", 3))
    )


_RaidControllerBatteryBackupBatteryType_Type.__name__ = "Integer32"
_RaidControllerBatteryBackupBatteryType_Object = MibTableColumn
raidControllerBatteryBackupBatteryType = _RaidControllerBatteryBackupBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 12),
    _RaidControllerBatteryBackupBatteryType_Type()
)
raidControllerBatteryBackupBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupBatteryType.setStatus("obsolete")
_RaidControllerBatteryBackupThreshold_Type = Unsigned32
_RaidControllerBatteryBackupThreshold_Object = MibTableColumn
raidControllerBatteryBackupThreshold = _RaidControllerBatteryBackupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 3, 1, 13),
    _RaidControllerBatteryBackupThreshold_Type()
)
raidControllerBatteryBackupThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerBatteryBackupThreshold.setStatus("obsolete")
_RaidControllerActiveTaskNumber_Type = Integer32
_RaidControllerActiveTaskNumber_Object = MibScalar
raidControllerActiveTaskNumber = _RaidControllerActiveTaskNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 4),
    _RaidControllerActiveTaskNumber_Type()
)
raidControllerActiveTaskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskNumber.setStatus("obsolete")
_RaidControllerActiveTaskTable_Object = MibTable
raidControllerActiveTaskTable = _RaidControllerActiveTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    raidControllerActiveTaskTable.setStatus("obsolete")
_RaidControllerActiveTaskEntry_Object = MibTableRow
raidControllerActiveTaskEntry = _RaidControllerActiveTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1)
)
raidControllerActiveTaskEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "raidControllerActiveTaskRackIndex"),
    (0, "BLUEARC-SERVER-MIB", "raidControllerActiveTaskIndex"),
)
if mibBuilder.loadTexts:
    raidControllerActiveTaskEntry.setStatus("obsolete")


class _RaidControllerActiveTaskRackIndex_Type(Integer32):
    """Custom type raidControllerActiveTaskRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RaidControllerActiveTaskRackIndex_Type.__name__ = "Integer32"
_RaidControllerActiveTaskRackIndex_Object = MibTableColumn
raidControllerActiveTaskRackIndex = _RaidControllerActiveTaskRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1, 1),
    _RaidControllerActiveTaskRackIndex_Type()
)
raidControllerActiveTaskRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskRackIndex.setStatus("obsolete")
_RaidControllerActiveTaskIndex_Type = Unsigned32
_RaidControllerActiveTaskIndex_Object = MibTableColumn
raidControllerActiveTaskIndex = _RaidControllerActiveTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1, 2),
    _RaidControllerActiveTaskIndex_Type()
)
raidControllerActiveTaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskIndex.setStatus("obsolete")


class _RaidControllerActiveTaskType_Type(Integer32):
    """Custom type raidControllerActiveTaskType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("backgroundInitialising", 8),
          ("chargingBattery", 6),
          ("checking", 2),
          ("checkingAndRestoring", 3),
          ("initializing", 1),
          ("migrating", 9),
          ("rebuilding", 4),
          ("reconditioningBattery", 5),
          ("unknown", 7))
    )


_RaidControllerActiveTaskType_Type.__name__ = "Integer32"
_RaidControllerActiveTaskType_Object = MibTableColumn
raidControllerActiveTaskType = _RaidControllerActiveTaskType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1, 3),
    _RaidControllerActiveTaskType_Type()
)
raidControllerActiveTaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskType.setStatus("obsolete")
_RaidControllerActiveTaskLUN_Type = Unsigned32
_RaidControllerActiveTaskLUN_Object = MibTableColumn
raidControllerActiveTaskLUN = _RaidControllerActiveTaskLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1, 4),
    _RaidControllerActiveTaskLUN_Type()
)
raidControllerActiveTaskLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskLUN.setStatus("obsolete")


class _RaidControllerActiveTaskPercentageDone_Type(Integer32):
    """Custom type raidControllerActiveTaskPercentageDone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidControllerActiveTaskPercentageDone_Type.__name__ = "Integer32"
_RaidControllerActiveTaskPercentageDone_Object = MibTableColumn
raidControllerActiveTaskPercentageDone = _RaidControllerActiveTaskPercentageDone_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 1, 5, 1, 5),
    _RaidControllerActiveTaskPercentageDone_Type()
)
raidControllerActiveTaskPercentageDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerActiveTaskPercentageDone.setStatus("obsolete")
_PhysicalDrives_ObjectIdentity = ObjectIdentity
physicalDrives = _PhysicalDrives_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2)
)
_PhysicalDriveNumber_Type = Integer32
_PhysicalDriveNumber_Object = MibScalar
physicalDriveNumber = _PhysicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 1),
    _PhysicalDriveNumber_Type()
)
physicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveNumber.setStatus("obsolete")
_PhysicalDriveTable_Object = MibTable
physicalDriveTable = _PhysicalDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    physicalDriveTable.setStatus("obsolete")
_PhysicalDriveEntry_Object = MibTableRow
physicalDriveEntry = _PhysicalDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1)
)
physicalDriveEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "physicalDriveRackIndex"),
    (0, "BLUEARC-SERVER-MIB", "physicalDriveEnclosureIndex"),
    (0, "BLUEARC-SERVER-MIB", "physicalDriveColumnIndex"),
    (0, "BLUEARC-SERVER-MIB", "physicalDriveRowIndex"),
)
if mibBuilder.loadTexts:
    physicalDriveEntry.setStatus("obsolete")


class _PhysicalDriveRackIndex_Type(Integer32):
    """Custom type physicalDriveRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PhysicalDriveRackIndex_Type.__name__ = "Integer32"
_PhysicalDriveRackIndex_Object = MibTableColumn
physicalDriveRackIndex = _PhysicalDriveRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 1),
    _PhysicalDriveRackIndex_Type()
)
physicalDriveRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveRackIndex.setStatus("obsolete")
_PhysicalDriveEnclosureIndex_Type = Unsigned32
_PhysicalDriveEnclosureIndex_Object = MibTableColumn
physicalDriveEnclosureIndex = _PhysicalDriveEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 2),
    _PhysicalDriveEnclosureIndex_Type()
)
physicalDriveEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveEnclosureIndex.setStatus("obsolete")
_PhysicalDriveColumnIndex_Type = Unsigned32
_PhysicalDriveColumnIndex_Object = MibTableColumn
physicalDriveColumnIndex = _PhysicalDriveColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 3),
    _PhysicalDriveColumnIndex_Type()
)
physicalDriveColumnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveColumnIndex.setStatus("obsolete")
_PhysicalDriveRowIndex_Type = Unsigned32
_PhysicalDriveRowIndex_Object = MibTableColumn
physicalDriveRowIndex = _PhysicalDriveRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 4),
    _PhysicalDriveRowIndex_Type()
)
physicalDriveRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveRowIndex.setStatus("obsolete")


class _PhysicalDriveStatus_Type(Integer32):
    """Custom type physicalDriveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("hotspare", 7),
          ("migrating", 9),
          ("notConfigured", 8),
          ("notPresent", 1),
          ("online", 2),
          ("rebuilding", 6),
          ("unknown", 10))
    )


_PhysicalDriveStatus_Type.__name__ = "Integer32"
_PhysicalDriveStatus_Object = MibTableColumn
physicalDriveStatus = _PhysicalDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 5),
    _PhysicalDriveStatus_Type()
)
physicalDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveStatus.setStatus("obsolete")


class _PhysicalDriveVendor_Type(Integer32):
    """Custom type physicalDriveVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seagate", 1),
          ("unknown", 2))
    )


_PhysicalDriveVendor_Type.__name__ = "Integer32"
_PhysicalDriveVendor_Object = MibTableColumn
physicalDriveVendor = _PhysicalDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 6),
    _PhysicalDriveVendor_Type()
)
physicalDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveVendor.setStatus("obsolete")
_PhysicalDriveVersion_Type = DisplayString
_PhysicalDriveVersion_Object = MibTableColumn
physicalDriveVersion = _PhysicalDriveVersion_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 7),
    _PhysicalDriveVersion_Type()
)
physicalDriveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveVersion.setStatus("obsolete")
_PhysicalDriveCapacity_Type = Counter64
_PhysicalDriveCapacity_Object = MibTableColumn
physicalDriveCapacity = _PhysicalDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 2, 2, 1, 8),
    _PhysicalDriveCapacity_Type()
)
physicalDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDriveCapacity.setStatus("obsolete")
_Enclosures_ObjectIdentity = ObjectIdentity
enclosures = _Enclosures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3)
)
_EnclosureFanNumber_Type = Integer32
_EnclosureFanNumber_Object = MibScalar
enclosureFanNumber = _EnclosureFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 1),
    _EnclosureFanNumber_Type()
)
enclosureFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanNumber.setStatus("obsolete")
_EnclosureFanTable_Object = MibTable
enclosureFanTable = _EnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    enclosureFanTable.setStatus("obsolete")
_EnclosureFanEntry_Object = MibTableRow
enclosureFanEntry = _EnclosureFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1)
)
enclosureFanEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "enclosureFanRackIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureFanEnclosureIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureFanFanIndex"),
)
if mibBuilder.loadTexts:
    enclosureFanEntry.setStatus("obsolete")


class _EnclosureFanRackIndex_Type(Integer32):
    """Custom type enclosureFanRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EnclosureFanRackIndex_Type.__name__ = "Integer32"
_EnclosureFanRackIndex_Object = MibTableColumn
enclosureFanRackIndex = _EnclosureFanRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1, 1),
    _EnclosureFanRackIndex_Type()
)
enclosureFanRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanRackIndex.setStatus("obsolete")
_EnclosureFanEnclosureIndex_Type = Unsigned32
_EnclosureFanEnclosureIndex_Object = MibTableColumn
enclosureFanEnclosureIndex = _EnclosureFanEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1, 2),
    _EnclosureFanEnclosureIndex_Type()
)
enclosureFanEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanEnclosureIndex.setStatus("obsolete")
_EnclosureFanFanIndex_Type = Unsigned32
_EnclosureFanFanIndex_Object = MibTableColumn
enclosureFanFanIndex = _EnclosureFanFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1, 3),
    _EnclosureFanFanIndex_Type()
)
enclosureFanFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanFanIndex.setStatus("obsolete")


class _EnclosureFanStatus_Type(Integer32):
    """Custom type enclosureFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_EnclosureFanStatus_Type.__name__ = "Integer32"
_EnclosureFanStatus_Object = MibTableColumn
enclosureFanStatus = _EnclosureFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1, 4),
    _EnclosureFanStatus_Type()
)
enclosureFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanStatus.setStatus("obsolete")


class _EnclosureFanSpeed_Type(Integer32):
    """Custom type enclosureFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2),
          ("stoppedOrUnknown", 3))
    )


_EnclosureFanSpeed_Type.__name__ = "Integer32"
_EnclosureFanSpeed_Object = MibTableColumn
enclosureFanSpeed = _EnclosureFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 2, 1, 5),
    _EnclosureFanSpeed_Type()
)
enclosureFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanSpeed.setStatus("obsolete")
_EnclosureTemperatureNumber_Type = Integer32
_EnclosureTemperatureNumber_Object = MibScalar
enclosureTemperatureNumber = _EnclosureTemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 3),
    _EnclosureTemperatureNumber_Type()
)
enclosureTemperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureNumber.setStatus("obsolete")
_EnclosureTemperatureTable_Object = MibTable
enclosureTemperatureTable = _EnclosureTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    enclosureTemperatureTable.setStatus("obsolete")
_EnclosureTemperatureEntry_Object = MibTableRow
enclosureTemperatureEntry = _EnclosureTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1)
)
enclosureTemperatureEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "enclosureTemperatureRackIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureTemperatureEnclosureIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureTemperatureTempIndex"),
)
if mibBuilder.loadTexts:
    enclosureTemperatureEntry.setStatus("obsolete")


class _EnclosureTemperatureRackIndex_Type(Integer32):
    """Custom type enclosureTemperatureRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EnclosureTemperatureRackIndex_Type.__name__ = "Integer32"
_EnclosureTemperatureRackIndex_Object = MibTableColumn
enclosureTemperatureRackIndex = _EnclosureTemperatureRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 1),
    _EnclosureTemperatureRackIndex_Type()
)
enclosureTemperatureRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureRackIndex.setStatus("obsolete")


class _EnclosureTemperatureEnclosureIndex_Type(Integer32):
    """Custom type enclosureTemperatureEnclosureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EnclosureTemperatureEnclosureIndex_Type.__name__ = "Integer32"
_EnclosureTemperatureEnclosureIndex_Object = MibTableColumn
enclosureTemperatureEnclosureIndex = _EnclosureTemperatureEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 2),
    _EnclosureTemperatureEnclosureIndex_Type()
)
enclosureTemperatureEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureEnclosureIndex.setStatus("obsolete")


class _EnclosureTemperatureTempIndex_Type(Integer32):
    """Custom type enclosureTemperatureTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnclosureTemperatureTempIndex_Type.__name__ = "Integer32"
_EnclosureTemperatureTempIndex_Object = MibTableColumn
enclosureTemperatureTempIndex = _EnclosureTemperatureTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 3),
    _EnclosureTemperatureTempIndex_Type()
)
enclosureTemperatureTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureTempIndex.setStatus("obsolete")


class _EnclosureTemperatureStatus_Type(Integer32):
    """Custom type enclosureTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_EnclosureTemperatureStatus_Type.__name__ = "Integer32"
_EnclosureTemperatureStatus_Object = MibTableColumn
enclosureTemperatureStatus = _EnclosureTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 4),
    _EnclosureTemperatureStatus_Type()
)
enclosureTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureStatus.setStatus("obsolete")


class _EnclosureTemperatureOverTemp_Type(Integer32):
    """Custom type enclosureTemperatureOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOverTemp", 2),
          ("overTemp", 1),
          ("unknown", 3))
    )


_EnclosureTemperatureOverTemp_Type.__name__ = "Integer32"
_EnclosureTemperatureOverTemp_Object = MibTableColumn
enclosureTemperatureOverTemp = _EnclosureTemperatureOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 5),
    _EnclosureTemperatureOverTemp_Type()
)
enclosureTemperatureOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureOverTemp.setStatus("obsolete")
_EnclosureTemperatureTempC_Type = Integer32
_EnclosureTemperatureTempC_Object = MibTableColumn
enclosureTemperatureTempC = _EnclosureTemperatureTempC_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 6),
    _EnclosureTemperatureTempC_Type()
)
enclosureTemperatureTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureTempC.setStatus("obsolete")
_EnclosureTemperatureTempF_Type = Integer32
_EnclosureTemperatureTempF_Object = MibTableColumn
enclosureTemperatureTempF = _EnclosureTemperatureTempF_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 7),
    _EnclosureTemperatureTempF_Type()
)
enclosureTemperatureTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureTempF.setStatus("obsolete")


class _EnclosureTemperatureRange_Type(Integer32):
    """Custom type enclosureTemperatureRange based on Integer32"""
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
        *(("hot", 3),
          ("normal", 1),
          ("unknown", 4),
          ("warm", 2))
    )


_EnclosureTemperatureRange_Type.__name__ = "Integer32"
_EnclosureTemperatureRange_Object = MibTableColumn
enclosureTemperatureRange = _EnclosureTemperatureRange_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 4, 1, 8),
    _EnclosureTemperatureRange_Type()
)
enclosureTemperatureRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureRange.setStatus("obsolete")
_EnclosurePSUNumber_Type = Integer32
_EnclosurePSUNumber_Object = MibScalar
enclosurePSUNumber = _EnclosurePSUNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 5),
    _EnclosurePSUNumber_Type()
)
enclosurePSUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUNumber.setStatus("obsolete")
_EnclosurePSUTable_Object = MibTable
enclosurePSUTable = _EnclosurePSUTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    enclosurePSUTable.setStatus("obsolete")
_EnclosurePSUEntry_Object = MibTableRow
enclosurePSUEntry = _EnclosurePSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6, 1)
)
enclosurePSUEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "enclosurePSURackIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosurePSUEnclosureIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosurePSUPSUIndex"),
)
if mibBuilder.loadTexts:
    enclosurePSUEntry.setStatus("obsolete")


class _EnclosurePSURackIndex_Type(Integer32):
    """Custom type enclosurePSURackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EnclosurePSURackIndex_Type.__name__ = "Integer32"
_EnclosurePSURackIndex_Object = MibTableColumn
enclosurePSURackIndex = _EnclosurePSURackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6, 1, 1),
    _EnclosurePSURackIndex_Type()
)
enclosurePSURackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSURackIndex.setStatus("obsolete")


class _EnclosurePSUEnclosureIndex_Type(Integer32):
    """Custom type enclosurePSUEnclosureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EnclosurePSUEnclosureIndex_Type.__name__ = "Integer32"
_EnclosurePSUEnclosureIndex_Object = MibTableColumn
enclosurePSUEnclosureIndex = _EnclosurePSUEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6, 1, 2),
    _EnclosurePSUEnclosureIndex_Type()
)
enclosurePSUEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUEnclosureIndex.setStatus("obsolete")


class _EnclosurePSUPSUIndex_Type(Integer32):
    """Custom type enclosurePSUPSUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnclosurePSUPSUIndex_Type.__name__ = "Integer32"
_EnclosurePSUPSUIndex_Object = MibTableColumn
enclosurePSUPSUIndex = _EnclosurePSUPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6, 1, 3),
    _EnclosurePSUPSUIndex_Type()
)
enclosurePSUPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUPSUIndex.setStatus("obsolete")


class _EnclosurePSUStatus_Type(Integer32):
    """Custom type enclosurePSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_EnclosurePSUStatus_Type.__name__ = "Integer32"
_EnclosurePSUStatus_Object = MibTableColumn
enclosurePSUStatus = _EnclosurePSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 6, 1, 4),
    _EnclosurePSUStatus_Type()
)
enclosurePSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUStatus.setStatus("obsolete")
_EnclosureAlarmNumber_Type = Integer32
_EnclosureAlarmNumber_Object = MibScalar
enclosureAlarmNumber = _EnclosureAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 7),
    _EnclosureAlarmNumber_Type()
)
enclosureAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmNumber.setStatus("obsolete")
_EnclosureAlarmTable_Object = MibTable
enclosureAlarmTable = _EnclosureAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8)
)
if mibBuilder.loadTexts:
    enclosureAlarmTable.setStatus("obsolete")
_EnclosureAlarmEntry_Object = MibTableRow
enclosureAlarmEntry = _EnclosureAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1)
)
enclosureAlarmEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "enclosureAlarmRackIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureAlarmEnclosureIndex"),
    (0, "BLUEARC-SERVER-MIB", "enclosureAlarmAlarmIndex"),
)
if mibBuilder.loadTexts:
    enclosureAlarmEntry.setStatus("obsolete")


class _EnclosureAlarmRackIndex_Type(Integer32):
    """Custom type enclosureAlarmRackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EnclosureAlarmRackIndex_Type.__name__ = "Integer32"
_EnclosureAlarmRackIndex_Object = MibTableColumn
enclosureAlarmRackIndex = _EnclosureAlarmRackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1, 1),
    _EnclosureAlarmRackIndex_Type()
)
enclosureAlarmRackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmRackIndex.setStatus("obsolete")


class _EnclosureAlarmEnclosureIndex_Type(Integer32):
    """Custom type enclosureAlarmEnclosureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnclosureAlarmEnclosureIndex_Type.__name__ = "Integer32"
_EnclosureAlarmEnclosureIndex_Object = MibTableColumn
enclosureAlarmEnclosureIndex = _EnclosureAlarmEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1, 2),
    _EnclosureAlarmEnclosureIndex_Type()
)
enclosureAlarmEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmEnclosureIndex.setStatus("obsolete")


class _EnclosureAlarmAlarmIndex_Type(Integer32):
    """Custom type enclosureAlarmAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnclosureAlarmAlarmIndex_Type.__name__ = "Integer32"
_EnclosureAlarmAlarmIndex_Object = MibTableColumn
enclosureAlarmAlarmIndex = _EnclosureAlarmAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1, 3),
    _EnclosureAlarmAlarmIndex_Type()
)
enclosureAlarmAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmAlarmIndex.setStatus("obsolete")


class _EnclosureAlarmStatus_Type(Integer32):
    """Custom type enclosureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_EnclosureAlarmStatus_Type.__name__ = "Integer32"
_EnclosureAlarmStatus_Object = MibTableColumn
enclosureAlarmStatus = _EnclosureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1, 4),
    _EnclosureAlarmStatus_Type()
)
enclosureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmStatus.setStatus("obsolete")


class _EnclosureAlarmBeeping_Type(Integer32):
    """Custom type enclosureAlarmBeeping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beeping", 1),
          ("notBeeping", 2),
          ("unknown", 3))
    )


_EnclosureAlarmBeeping_Type.__name__ = "Integer32"
_EnclosureAlarmBeeping_Object = MibTableColumn
enclosureAlarmBeeping = _EnclosureAlarmBeeping_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 2, 3, 8, 1, 5),
    _EnclosureAlarmBeeping_Type()
)
enclosureAlarmBeeping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarmBeeping.setStatus("obsolete")
_Automount_ObjectIdentity = ObjectIdentity
automount = _Automount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3)
)
_AutomountNumber_Type = Integer32
_AutomountNumber_Object = MibScalar
automountNumber = _AutomountNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 1),
    _AutomountNumber_Type()
)
automountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automountNumber.setStatus("obsolete")
_AutomountTable_Object = MibTable
automountTable = _AutomountTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    automountTable.setStatus("obsolete")
_AutomountEntry_Object = MibTableRow
automountEntry = _AutomountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2, 1)
)
automountEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "automountIndex"),
    (0, "BLUEARC-SERVER-MIB", "automountPartitionIndex"),
)
if mibBuilder.loadTexts:
    automountEntry.setStatus("obsolete")


class _AutomountIndex_Type(Integer32):
    """Custom type automountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AutomountIndex_Type.__name__ = "Integer32"
_AutomountIndex_Object = MibTableColumn
automountIndex = _AutomountIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2, 1, 1),
    _AutomountIndex_Type()
)
automountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automountIndex.setStatus("obsolete")
_AutomountPartitionIndex_Type = Unsigned32
_AutomountPartitionIndex_Object = MibTableColumn
automountPartitionIndex = _AutomountPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2, 1, 2),
    _AutomountPartitionIndex_Type()
)
automountPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automountPartitionIndex.setStatus("obsolete")
_AutomountWWN_Type = DisplayString
_AutomountWWN_Object = MibTableColumn
automountWWN = _AutomountWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2, 1, 3),
    _AutomountWWN_Type()
)
automountWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automountWWN.setStatus("obsolete")
_AutomountLUN_Type = Unsigned32
_AutomountLUN_Object = MibTableColumn
automountLUN = _AutomountLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 3, 2, 1, 4),
    _AutomountLUN_Type()
)
automountLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automountLUN.setStatus("obsolete")
_SystemDrives_ObjectIdentity = ObjectIdentity
systemDrives = _SystemDrives_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4)
)
_SysDriveNumber_Type = Integer32
_SysDriveNumber_Object = MibScalar
sysDriveNumber = _SysDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 1),
    _SysDriveNumber_Type()
)
sysDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveNumber.setStatus("current")
_SysDriveTable_Object = MibTable
sysDriveTable = _SysDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    sysDriveTable.setStatus("current")
_SysDriveEntry_Object = MibTableRow
sysDriveEntry = _SysDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1)
)
sysDriveEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "sysDriveIndex"),
)
if mibBuilder.loadTexts:
    sysDriveEntry.setStatus("current")


class _SysDriveIndex_Type(Integer32):
    """Custom type sysDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SysDriveIndex_Type.__name__ = "Integer32"
_SysDriveIndex_Object = MibTableColumn
sysDriveIndex = _SysDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 1),
    _SysDriveIndex_Type()
)
sysDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveIndex.setStatus("current")
_SysDriveWWN_Type = DisplayString
_SysDriveWWN_Object = MibTableColumn
sysDriveWWN = _SysDriveWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 2),
    _SysDriveWWN_Type()
)
sysDriveWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveWWN.setStatus("current")
_SysDriveLUN_Type = Unsigned32
_SysDriveLUN_Object = MibTableColumn
sysDriveLUN = _SysDriveLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 3),
    _SysDriveLUN_Type()
)
sysDriveLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveLUN.setStatus("current")


class _SysDriveStatus_Type(Integer32):
    """Custom type sysDriveStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("corrupt", 2),
          ("disconnected", 5),
          ("failed", 3),
          ("formatting", 8),
          ("initializing", 7),
          ("notPresent", 4),
          ("offline", 6),
          ("online", 1),
          ("unknown", 9))
    )


_SysDriveStatus_Type.__name__ = "Integer32"
_SysDriveStatus_Object = MibTableColumn
sysDriveStatus = _SysDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 4),
    _SysDriveStatus_Type()
)
sysDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveStatus.setStatus("current")
_SysDriveCapacity_Type = Counter64
_SysDriveCapacity_Object = MibTableColumn
sysDriveCapacity = _SysDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 5),
    _SysDriveCapacity_Type()
)
sysDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveCapacity.setStatus("current")


class _SysDriveRaidLevel_Type(Integer32):
    """Custom type sysDriveRaidLevel based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("jBOD", 6),
          ("raid0", 1),
          ("raid1", 2),
          ("raid10", 5),
          ("raid3", 3),
          ("raid30", 7),
          ("raid5", 4),
          ("raid50", 8),
          ("unknown", 9))
    )


_SysDriveRaidLevel_Type.__name__ = "Integer32"
_SysDriveRaidLevel_Object = MibTableColumn
sysDriveRaidLevel = _SysDriveRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 6),
    _SysDriveRaidLevel_Type()
)
sysDriveRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveRaidLevel.setStatus("current")


class _SysDriveCacheMode_Type(Integer32):
    """Custom type sysDriveCacheMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 3),
          ("writeBack", 2),
          ("writeThrough", 1))
    )


_SysDriveCacheMode_Type.__name__ = "Integer32"
_SysDriveCacheMode_Object = MibTableColumn
sysDriveCacheMode = _SysDriveCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 4, 2, 1, 7),
    _SysDriveCacheMode_Type()
)
sysDriveCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDriveCacheMode.setStatus("current")
_Volumes_ObjectIdentity = ObjectIdentity
volumes = _Volumes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5)
)
_VolumeNumber_Type = Integer32
_VolumeNumber_Object = MibScalar
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 1),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("current")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("current")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1)
)
volumeEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "volumeSysDriveIndex"),
    (0, "BLUEARC-SERVER-MIB", "volumePartitionID"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("current")


class _VolumeSysDriveIndex_Type(Integer32):
    """Custom type volumeSysDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VolumeSysDriveIndex_Type.__name__ = "Integer32"
_VolumeSysDriveIndex_Object = MibTableColumn
volumeSysDriveIndex = _VolumeSysDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 1),
    _VolumeSysDriveIndex_Type()
)
volumeSysDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSysDriveIndex.setStatus("current")
_VolumePartitionID_Type = Unsigned32
_VolumePartitionID_Object = MibTableColumn
volumePartitionID = _VolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 2),
    _VolumePartitionID_Type()
)
volumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumePartitionID.setStatus("current")
_VolumeLabel_Type = DisplayString
_VolumeLabel_Object = MibTableColumn
volumeLabel = _VolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 3),
    _VolumeLabel_Type()
)
volumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLabel.setStatus("current")


class _VolumeStatus_Type(Integer32):
    """Custom type volumeStatus based on Integer32"""
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
        *(("formatted", 3),
          ("mounted", 2),
          ("needsChecking", 4),
          ("unformatted", 1))
    )


_VolumeStatus_Type.__name__ = "Integer32"
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 4),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("current")
_VolumeCapacity_Type = Counter64
_VolumeCapacity_Object = MibTableColumn
volumeCapacity = _VolumeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 5),
    _VolumeCapacity_Type()
)
volumeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeCapacity.setStatus("current")
_VolumeFreeCapacity_Type = Counter64
_VolumeFreeCapacity_Object = MibTableColumn
volumeFreeCapacity = _VolumeFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 6),
    _VolumeFreeCapacity_Type()
)
volumeFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeCapacity.setStatus("current")
_VolumeEnterpriseVirtualServer_Type = DisplayString
_VolumeEnterpriseVirtualServer_Object = MibTableColumn
volumeEnterpriseVirtualServer = _VolumeEnterpriseVirtualServer_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 2, 1, 7),
    _VolumeEnterpriseVirtualServer_Type()
)
volumeEnterpriseVirtualServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeEnterpriseVirtualServer.setStatus("current")
_FsStatsTable_Object = MibTable
fsStatsTable = _FsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    fsStatsTable.setStatus("current")
_FsStatsEntry_Object = MibTableRow
fsStatsEntry = _FsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 3, 1)
)
fsStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fsPermId"),
)
if mibBuilder.loadTexts:
    fsStatsEntry.setStatus("current")
_FsPermId_Type = Counter64
_FsPermId_Object = MibTableColumn
fsPermId = _FsPermId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 3, 1, 1),
    _FsPermId_Type()
)
fsPermId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPermId.setStatus("current")
_FsLabel_Type = DisplayString
_FsLabel_Object = MibTableColumn
fsLabel = _FsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 3, 1, 2),
    _FsLabel_Type()
)
fsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLabel.setStatus("current")
_OpsPerSecAverage_Type = Unsigned32
_OpsPerSecAverage_Object = MibTableColumn
opsPerSecAverage = _OpsPerSecAverage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 5, 3, 1, 3),
    _OpsPerSecAverage_Type()
)
opsPerSecAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsPerSecAverage.setStatus("current")
_FcStats_ObjectIdentity = ObjectIdentity
fcStats = _FcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6)
)
_FcRequests_Type = Counter64
_FcRequests_Object = MibScalar
fcRequests = _FcRequests_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 1),
    _FcRequests_Type()
)
fcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRequests.setStatus("current")
_FcResponses_Type = Counter64
_FcResponses_Object = MibScalar
fcResponses = _FcResponses_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 2),
    _FcResponses_Type()
)
fcResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcResponses.setStatus("current")
_FcReadReqs_Type = Counter64
_FcReadReqs_Object = MibScalar
fcReadReqs = _FcReadReqs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 3),
    _FcReadReqs_Type()
)
fcReadReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcReadReqs.setStatus("current")
_FcWriteReqs_Type = Counter64
_FcWriteReqs_Object = MibScalar
fcWriteReqs = _FcWriteReqs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 4),
    _FcWriteReqs_Type()
)
fcWriteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcWriteReqs.setStatus("current")
_FcReadResps_Type = Counter64
_FcReadResps_Object = MibScalar
fcReadResps = _FcReadResps_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 5),
    _FcReadResps_Type()
)
fcReadResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcReadResps.setStatus("current")
_FcWriteResps_Type = Counter64
_FcWriteResps_Object = MibScalar
fcWriteResps = _FcWriteResps_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 6),
    _FcWriteResps_Type()
)
fcWriteResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcWriteResps.setStatus("current")
_FcInstInRate_Type = Counter32
_FcInstInRate_Object = MibScalar
fcInstInRate = _FcInstInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 7),
    _FcInstInRate_Type()
)
fcInstInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInstInRate.setStatus("obsolete")
_FcInstOutRate_Type = Counter32
_FcInstOutRate_Object = MibScalar
fcInstOutRate = _FcInstOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 8),
    _FcInstOutRate_Type()
)
fcInstOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInstOutRate.setStatus("obsolete")
_FcPkInRate_Type = Counter32
_FcPkInRate_Object = MibScalar
fcPkInRate = _FcPkInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 9),
    _FcPkInRate_Type()
)
fcPkInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPkInRate.setStatus("obsolete")
_FcPkOutRate_Type = Counter32
_FcPkOutRate_Object = MibScalar
fcPkOutRate = _FcPkOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 10),
    _FcPkOutRate_Type()
)
fcPkOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPkOutRate.setStatus("obsolete")
_FcCacheHits_Type = Counter64
_FcCacheHits_Object = MibScalar
fcCacheHits = _FcCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 11),
    _FcCacheHits_Type()
)
fcCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcCacheHits.setStatus("current")
_FcCacheMisses_Type = Counter64
_FcCacheMisses_Object = MibScalar
fcCacheMisses = _FcCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 12),
    _FcCacheMisses_Type()
)
fcCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcCacheMisses.setStatus("current")
_FcLossSignalErrs_Type = Counter32
_FcLossSignalErrs_Object = MibScalar
fcLossSignalErrs = _FcLossSignalErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 13),
    _FcLossSignalErrs_Type()
)
fcLossSignalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLossSignalErrs.setStatus("obsolete")
_FcBadRXCharErrs_Type = Counter32
_FcBadRXCharErrs_Object = MibScalar
fcBadRXCharErrs = _FcBadRXCharErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 14),
    _FcBadRXCharErrs_Type()
)
fcBadRXCharErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBadRXCharErrs.setStatus("obsolete")
_FcLossSyncErrs_Type = Counter32
_FcLossSyncErrs_Object = MibScalar
fcLossSyncErrs = _FcLossSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 15),
    _FcLossSyncErrs_Type()
)
fcLossSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLossSyncErrs.setStatus("obsolete")
_FcLinkFailErrs_Type = Counter32
_FcLinkFailErrs_Object = MibScalar
fcLinkFailErrs = _FcLinkFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 16),
    _FcLinkFailErrs_Type()
)
fcLinkFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLinkFailErrs.setStatus("obsolete")
_FcRXEOFErrs_Type = Counter32
_FcRXEOFErrs_Object = MibScalar
fcRXEOFErrs = _FcRXEOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 17),
    _FcRXEOFErrs_Type()
)
fcRXEOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRXEOFErrs.setStatus("obsolete")
_FcDiscardedFrameErrs_Type = Counter32
_FcDiscardedFrameErrs_Object = MibScalar
fcDiscardedFrameErrs = _FcDiscardedFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 18),
    _FcDiscardedFrameErrs_Type()
)
fcDiscardedFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcDiscardedFrameErrs.setStatus("obsolete")
_FcBadCRCErrs_Type = Counter32
_FcBadCRCErrs_Object = MibScalar
fcBadCRCErrs = _FcBadCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 19),
    _FcBadCRCErrs_Type()
)
fcBadCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBadCRCErrs.setStatus("obsolete")
_FcProtErrs_Type = Counter32
_FcProtErrs_Object = MibScalar
fcProtErrs = _FcProtErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 20),
    _FcProtErrs_Type()
)
fcProtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcProtErrs.setStatus("obsolete")
_FcIOStatusResubs_Type = Counter64
_FcIOStatusResubs_Object = MibScalar
fcIOStatusResubs = _FcIOStatusResubs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 21),
    _FcIOStatusResubs_Type()
)
fcIOStatusResubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIOStatusResubs.setStatus("current")
_FcIOStatusFails_Type = Counter64
_FcIOStatusFails_Object = MibScalar
fcIOStatusFails = _FcIOStatusFails_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 22),
    _FcIOStatusFails_Type()
)
fcIOStatusFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIOStatusFails.setStatus("current")


class _FibreChannelInterfaceNumber_Type(Unsigned32):
    """Custom type fibreChannelInterfaceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FibreChannelInterfaceNumber_Type.__name__ = "Unsigned32"
_FibreChannelInterfaceNumber_Object = MibScalar
fibreChannelInterfaceNumber = _FibreChannelInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 23),
    _FibreChannelInterfaceNumber_Type()
)
fibreChannelInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelInterfaceNumber.setStatus("current")
_FcStatsTable_Object = MibTable
fcStatsTable = _FcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24)
)
if mibBuilder.loadTexts:
    fcStatsTable.setStatus("obsolete")
_FcStatsEntry_Object = MibTableRow
fcStatsEntry = _FcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1)
)
fcStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fcInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fcStatsEntry.setStatus("obsolete")


class _FcInterfaceIndex_Type(Integer32):
    """Custom type fcInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FcInterfaceIndex_Type.__name__ = "Integer32"
_FcInterfaceIndex_Object = MibTableColumn
fcInterfaceIndex = _FcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 1),
    _FcInterfaceIndex_Type()
)
fcInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInterfaceIndex.setStatus("obsolete")
_FcInstantaneousInRate_Type = Counter32
_FcInstantaneousInRate_Object = MibTableColumn
fcInstantaneousInRate = _FcInstantaneousInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 2),
    _FcInstantaneousInRate_Type()
)
fcInstantaneousInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInstantaneousInRate.setStatus("obsolete")
_FcInstantaneousOutRate_Type = Counter32
_FcInstantaneousOutRate_Object = MibTableColumn
fcInstantaneousOutRate = _FcInstantaneousOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 3),
    _FcInstantaneousOutRate_Type()
)
fcInstantaneousOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInstantaneousOutRate.setStatus("obsolete")
_FcPeakInRate_Type = Counter32
_FcPeakInRate_Object = MibTableColumn
fcPeakInRate = _FcPeakInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 4),
    _FcPeakInRate_Type()
)
fcPeakInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPeakInRate.setStatus("obsolete")
_FcPeakOutRate_Type = Counter32
_FcPeakOutRate_Object = MibTableColumn
fcPeakOutRate = _FcPeakOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 5),
    _FcPeakOutRate_Type()
)
fcPeakOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPeakOutRate.setStatus("obsolete")
_FcSignalLossErrors_Type = Counter32
_FcSignalLossErrors_Object = MibTableColumn
fcSignalLossErrors = _FcSignalLossErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 6),
    _FcSignalLossErrors_Type()
)
fcSignalLossErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSignalLossErrors.setStatus("obsolete")
_FcBadRXCharErrors_Type = Counter32
_FcBadRXCharErrors_Object = MibTableColumn
fcBadRXCharErrors = _FcBadRXCharErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 7),
    _FcBadRXCharErrors_Type()
)
fcBadRXCharErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBadRXCharErrors.setStatus("obsolete")
_FcLossSyncErrors_Type = Counter32
_FcLossSyncErrors_Object = MibTableColumn
fcLossSyncErrors = _FcLossSyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 8),
    _FcLossSyncErrors_Type()
)
fcLossSyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLossSyncErrors.setStatus("obsolete")
_FcLinkFailErrors_Type = Counter32
_FcLinkFailErrors_Object = MibTableColumn
fcLinkFailErrors = _FcLinkFailErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 9),
    _FcLinkFailErrors_Type()
)
fcLinkFailErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLinkFailErrors.setStatus("obsolete")
_FcRXEOFErrors_Type = Counter32
_FcRXEOFErrors_Object = MibTableColumn
fcRXEOFErrors = _FcRXEOFErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 10),
    _FcRXEOFErrors_Type()
)
fcRXEOFErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRXEOFErrors.setStatus("obsolete")
_FcDiscardedFrameErrors_Type = Counter32
_FcDiscardedFrameErrors_Object = MibTableColumn
fcDiscardedFrameErrors = _FcDiscardedFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 11),
    _FcDiscardedFrameErrors_Type()
)
fcDiscardedFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcDiscardedFrameErrors.setStatus("obsolete")
_FcBadCRCErrors_Type = Counter32
_FcBadCRCErrors_Object = MibTableColumn
fcBadCRCErrors = _FcBadCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 12),
    _FcBadCRCErrors_Type()
)
fcBadCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBadCRCErrors.setStatus("obsolete")
_FcProtocolErrors_Type = Counter32
_FcProtocolErrors_Object = MibTableColumn
fcProtocolErrors = _FcProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 24, 1, 13),
    _FcProtocolErrors_Type()
)
fcProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcProtocolErrors.setStatus("obsolete")
_FcStatisticsTable_Object = MibTable
fcStatisticsTable = _FcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25)
)
if mibBuilder.loadTexts:
    fcStatisticsTable.setStatus("current")
_FcStatisticsEntry_Object = MibTableRow
fcStatisticsEntry = _FcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1)
)
fcStatisticsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fcStatsClusterNode"),
    (0, "BLUEARC-SERVER-MIB", "fcStatsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fcStatisticsEntry.setStatus("current")


class _FcStatsClusterNode_Type(Integer32):
    """Custom type fcStatsClusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FcStatsClusterNode_Type.__name__ = "Integer32"
_FcStatsClusterNode_Object = MibTableColumn
fcStatsClusterNode = _FcStatsClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 1),
    _FcStatsClusterNode_Type()
)
fcStatsClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsClusterNode.setStatus("current")


class _FcStatsInterfaceIndex_Type(Integer32):
    """Custom type fcStatsInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FcStatsInterfaceIndex_Type.__name__ = "Integer32"
_FcStatsInterfaceIndex_Object = MibTableColumn
fcStatsInterfaceIndex = _FcStatsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 2),
    _FcStatsInterfaceIndex_Type()
)
fcStatsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInterfaceIndex.setStatus("current")


class _FcStatsInterfaceEnabled_Type(Integer32):
    """Custom type fcStatsInterfaceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 0))
    )


_FcStatsInterfaceEnabled_Type.__name__ = "Integer32"
_FcStatsInterfaceEnabled_Object = MibTableColumn
fcStatsInterfaceEnabled = _FcStatsInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 3),
    _FcStatsInterfaceEnabled_Type()
)
fcStatsInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInterfaceEnabled.setStatus("current")


class _FcStatsInterfaceStatus_Type(Integer32):
    """Custom type fcStatsInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("isolated", 2),
          ("unknown", 0),
          ("up", 1))
    )


_FcStatsInterfaceStatus_Type.__name__ = "Integer32"
_FcStatsInterfaceStatus_Object = MibTableColumn
fcStatsInterfaceStatus = _FcStatsInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 4),
    _FcStatsInterfaceStatus_Type()
)
fcStatsInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInterfaceStatus.setStatus("current")


class _FcStatsInterfaceLinkSpeed_Type(Integer32):
    """Custom type fcStatsInterfaceLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FcStatsInterfaceLinkSpeed_Type.__name__ = "Integer32"
_FcStatsInterfaceLinkSpeed_Object = MibTableColumn
fcStatsInterfaceLinkSpeed = _FcStatsInterfaceLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 5),
    _FcStatsInterfaceLinkSpeed_Type()
)
fcStatsInterfaceLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInterfaceLinkSpeed.setStatus("current")


class _FcStatsInterfaceLinkType_Type(Integer32):
    """Custom type fcStatsInterfaceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n", 1),
          ("nl", 2),
          ("unknown", 0))
    )


_FcStatsInterfaceLinkType_Type.__name__ = "Integer32"
_FcStatsInterfaceLinkType_Object = MibTableColumn
fcStatsInterfaceLinkType = _FcStatsInterfaceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 6),
    _FcStatsInterfaceLinkType_Type()
)
fcStatsInterfaceLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInterfaceLinkType.setStatus("current")
_FcStatsInstantaneousInRate_Type = Counter32
_FcStatsInstantaneousInRate_Object = MibTableColumn
fcStatsInstantaneousInRate = _FcStatsInstantaneousInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 7),
    _FcStatsInstantaneousInRate_Type()
)
fcStatsInstantaneousInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInstantaneousInRate.setStatus("current")
_FcStatsInstantaneousOutRate_Type = Counter32
_FcStatsInstantaneousOutRate_Object = MibTableColumn
fcStatsInstantaneousOutRate = _FcStatsInstantaneousOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 8),
    _FcStatsInstantaneousOutRate_Type()
)
fcStatsInstantaneousOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsInstantaneousOutRate.setStatus("current")
_FcStatsPeakInRate_Type = Counter32
_FcStatsPeakInRate_Object = MibTableColumn
fcStatsPeakInRate = _FcStatsPeakInRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 9),
    _FcStatsPeakInRate_Type()
)
fcStatsPeakInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsPeakInRate.setStatus("current")
_FcStatsPeakOutRate_Type = Counter32
_FcStatsPeakOutRate_Object = MibTableColumn
fcStatsPeakOutRate = _FcStatsPeakOutRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 10),
    _FcStatsPeakOutRate_Type()
)
fcStatsPeakOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsPeakOutRate.setStatus("current")
_FcStatsTotalRxBytes_Type = Counter64
_FcStatsTotalRxBytes_Object = MibTableColumn
fcStatsTotalRxBytes = _FcStatsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 11),
    _FcStatsTotalRxBytes_Type()
)
fcStatsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsTotalRxBytes.setStatus("current")
_FcStatsTotalTxBytes_Type = Counter64
_FcStatsTotalTxBytes_Object = MibTableColumn
fcStatsTotalTxBytes = _FcStatsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 12),
    _FcStatsTotalTxBytes_Type()
)
fcStatsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsTotalTxBytes.setStatus("current")
_FcStatsSignalLossErrors_Type = Counter32
_FcStatsSignalLossErrors_Object = MibTableColumn
fcStatsSignalLossErrors = _FcStatsSignalLossErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 13),
    _FcStatsSignalLossErrors_Type()
)
fcStatsSignalLossErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsSignalLossErrors.setStatus("current")
_FcStatsBadRXCharErrors_Type = Counter32
_FcStatsBadRXCharErrors_Object = MibTableColumn
fcStatsBadRXCharErrors = _FcStatsBadRXCharErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 14),
    _FcStatsBadRXCharErrors_Type()
)
fcStatsBadRXCharErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsBadRXCharErrors.setStatus("current")
_FcStatsLossSyncErrors_Type = Counter32
_FcStatsLossSyncErrors_Object = MibTableColumn
fcStatsLossSyncErrors = _FcStatsLossSyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 15),
    _FcStatsLossSyncErrors_Type()
)
fcStatsLossSyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsLossSyncErrors.setStatus("current")
_FcStatsLinkFailErrors_Type = Counter32
_FcStatsLinkFailErrors_Object = MibTableColumn
fcStatsLinkFailErrors = _FcStatsLinkFailErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 16),
    _FcStatsLinkFailErrors_Type()
)
fcStatsLinkFailErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsLinkFailErrors.setStatus("current")
_FcStatsRXEOFErrors_Type = Counter32
_FcStatsRXEOFErrors_Object = MibTableColumn
fcStatsRXEOFErrors = _FcStatsRXEOFErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 17),
    _FcStatsRXEOFErrors_Type()
)
fcStatsRXEOFErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsRXEOFErrors.setStatus("current")
_FcStatsDiscardedFrameErrors_Type = Counter32
_FcStatsDiscardedFrameErrors_Object = MibTableColumn
fcStatsDiscardedFrameErrors = _FcStatsDiscardedFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 18),
    _FcStatsDiscardedFrameErrors_Type()
)
fcStatsDiscardedFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsDiscardedFrameErrors.setStatus("current")
_FcStatsBadCRCErrors_Type = Counter32
_FcStatsBadCRCErrors_Object = MibTableColumn
fcStatsBadCRCErrors = _FcStatsBadCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 19),
    _FcStatsBadCRCErrors_Type()
)
fcStatsBadCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsBadCRCErrors.setStatus("current")
_FcStatsProtocolErrors_Type = Counter32
_FcStatsProtocolErrors_Object = MibTableColumn
fcStatsProtocolErrors = _FcStatsProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 6, 25, 1, 20),
    _FcStatsProtocolErrors_Type()
)
fcStatsProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsProtocolErrors.setStatus("current")
_VirtualVolumes_ObjectIdentity = ObjectIdentity
virtualVolumes = _VirtualVolumes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7)
)
_VirtualVolumeNumber_Type = Integer32
_VirtualVolumeNumber_Object = MibScalar
virtualVolumeNumber = _VirtualVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 1),
    _VirtualVolumeNumber_Type()
)
virtualVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeNumber.setStatus("obsolete")
_VirtualVolumeTable_Object = MibTable
virtualVolumeTable = _VirtualVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    virtualVolumeTable.setStatus("obsolete")
_VirtualVolumeEntry_Object = MibTableRow
virtualVolumeEntry = _VirtualVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1)
)
virtualVolumeEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "virtualVolumeSysDriveIndex"),
    (0, "BLUEARC-SERVER-MIB", "virtualVolumePartitionID"),
    (0, "BLUEARC-SERVER-MIB", "virtualVolumeLabel"),
)
if mibBuilder.loadTexts:
    virtualVolumeEntry.setStatus("obsolete")


class _VirtualVolumeSysDriveIndex_Type(Integer32):
    """Custom type virtualVolumeSysDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_VirtualVolumeSysDriveIndex_Type.__name__ = "Integer32"
_VirtualVolumeSysDriveIndex_Object = MibTableColumn
virtualVolumeSysDriveIndex = _VirtualVolumeSysDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 1),
    _VirtualVolumeSysDriveIndex_Type()
)
virtualVolumeSysDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeSysDriveIndex.setStatus("obsolete")
_VirtualVolumePartitionID_Type = Unsigned32
_VirtualVolumePartitionID_Object = MibTableColumn
virtualVolumePartitionID = _VirtualVolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 2),
    _VirtualVolumePartitionID_Type()
)
virtualVolumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumePartitionID.setStatus("obsolete")
_VirtualVolumeLabel_Type = DisplayString
_VirtualVolumeLabel_Object = MibTableColumn
virtualVolumeLabel = _VirtualVolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 3),
    _VirtualVolumeLabel_Type()
)
virtualVolumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeLabel.setStatus("obsolete")


class _VirtualVolumeQuotaEnabled_Type(Integer32):
    """Custom type virtualVolumeQuotaEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VirtualVolumeQuotaEnabled_Type.__name__ = "Integer32"
_VirtualVolumeQuotaEnabled_Object = MibTableColumn
virtualVolumeQuotaEnabled = _VirtualVolumeQuotaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 4),
    _VirtualVolumeQuotaEnabled_Type()
)
virtualVolumeQuotaEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaEnabled.setStatus("obsolete")
_VirtualVolumeLimit_Type = Counter64
_VirtualVolumeLimit_Object = MibTableColumn
virtualVolumeLimit = _VirtualVolumeLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 5),
    _VirtualVolumeLimit_Type()
)
virtualVolumeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeLimit.setStatus("obsolete")


class _VirtualVolumeWarningAlert_Type(Integer32):
    """Custom type virtualVolumeWarningAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualVolumeWarningAlert_Type.__name__ = "Integer32"
_VirtualVolumeWarningAlert_Object = MibTableColumn
virtualVolumeWarningAlert = _VirtualVolumeWarningAlert_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 6),
    _VirtualVolumeWarningAlert_Type()
)
virtualVolumeWarningAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeWarningAlert.setStatus("obsolete")


class _VirtualVolumeCriticalAlert_Type(Integer32):
    """Custom type virtualVolumeCriticalAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualVolumeCriticalAlert_Type.__name__ = "Integer32"
_VirtualVolumeCriticalAlert_Object = MibTableColumn
virtualVolumeCriticalAlert = _VirtualVolumeCriticalAlert_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 7),
    _VirtualVolumeCriticalAlert_Type()
)
virtualVolumeCriticalAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeCriticalAlert.setStatus("obsolete")


class _VirtualVolumeHardLimitEnabled_Type(Integer32):
    """Custom type virtualVolumeHardLimitEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VirtualVolumeHardLimitEnabled_Type.__name__ = "Integer32"
_VirtualVolumeHardLimitEnabled_Object = MibTableColumn
virtualVolumeHardLimitEnabled = _VirtualVolumeHardLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 8),
    _VirtualVolumeHardLimitEnabled_Type()
)
virtualVolumeHardLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeHardLimitEnabled.setStatus("obsolete")
_VirtualVolumeQuotaBytesUsed_Type = Counter64
_VirtualVolumeQuotaBytesUsed_Object = MibTableColumn
virtualVolumeQuotaBytesUsed = _VirtualVolumeQuotaBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 9),
    _VirtualVolumeQuotaBytesUsed_Type()
)
virtualVolumeQuotaBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaBytesUsed.setStatus("obsolete")


class _VirtualVolumeQuotaPercentageUsed_Type(Integer32):
    """Custom type virtualVolumeQuotaPercentageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualVolumeQuotaPercentageUsed_Type.__name__ = "Integer32"
_VirtualVolumeQuotaPercentageUsed_Object = MibTableColumn
virtualVolumeQuotaPercentageUsed = _VirtualVolumeQuotaPercentageUsed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 2, 1, 10),
    _VirtualVolumeQuotaPercentageUsed_Type()
)
virtualVolumeQuotaPercentageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaPercentageUsed.setStatus("obsolete")
_MemberListNumber_Type = Integer32
_MemberListNumber_Object = MibScalar
memberListNumber = _MemberListNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 3),
    _MemberListNumber_Type()
)
memberListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListNumber.setStatus("obsolete")
_MemberListTable_Object = MibTable
memberListTable = _MemberListTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4)
)
if mibBuilder.loadTexts:
    memberListTable.setStatus("obsolete")
_MemberListEntry_Object = MibTableRow
memberListEntry = _MemberListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1)
)
memberListEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "memberListVolumeSysDriveIndex"),
    (0, "BLUEARC-SERVER-MIB", "memberListVolumePartitionID"),
    (0, "BLUEARC-SERVER-MIB", "memberListVirtualVolumeLabel"),
    (0, "BLUEARC-SERVER-MIB", "memberListIndex"),
)
if mibBuilder.loadTexts:
    memberListEntry.setStatus("obsolete")


class _MemberListVolumeSysDriveIndex_Type(Integer32):
    """Custom type memberListVolumeSysDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MemberListVolumeSysDriveIndex_Type.__name__ = "Integer32"
_MemberListVolumeSysDriveIndex_Object = MibTableColumn
memberListVolumeSysDriveIndex = _MemberListVolumeSysDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 1),
    _MemberListVolumeSysDriveIndex_Type()
)
memberListVolumeSysDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListVolumeSysDriveIndex.setStatus("obsolete")
_MemberListVolumePartitionID_Type = Unsigned32
_MemberListVolumePartitionID_Object = MibTableColumn
memberListVolumePartitionID = _MemberListVolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 2),
    _MemberListVolumePartitionID_Type()
)
memberListVolumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListVolumePartitionID.setStatus("obsolete")
_MemberListVirtualVolumeLabel_Type = DisplayString
_MemberListVirtualVolumeLabel_Object = MibTableColumn
memberListVirtualVolumeLabel = _MemberListVirtualVolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 3),
    _MemberListVirtualVolumeLabel_Type()
)
memberListVirtualVolumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListVirtualVolumeLabel.setStatus("obsolete")


class _MemberListIndex_Type(Integer32):
    """Custom type memberListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_MemberListIndex_Type.__name__ = "Integer32"
_MemberListIndex_Object = MibTableColumn
memberListIndex = _MemberListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 4),
    _MemberListIndex_Type()
)
memberListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListIndex.setStatus("obsolete")
_MemberListPath_Type = DisplayString
_MemberListPath_Object = MibTableColumn
memberListPath = _MemberListPath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 5),
    _MemberListPath_Type()
)
memberListPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListPath.setStatus("obsolete")


class _MemberListStatus_Type(Integer32):
    """Custom type memberListStatus based on Integer32"""
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
        *(("assigning", 3),
          ("deleting", 5),
          ("done", 1),
          ("failed", 6),
          ("pending", 2),
          ("reparenting", 4))
    )


_MemberListStatus_Type.__name__ = "Integer32"
_MemberListStatus_Object = MibTableColumn
memberListStatus = _MemberListStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 7, 4, 1, 6),
    _MemberListStatus_Type()
)
memberListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberListStatus.setStatus("obsolete")
_Snapshot_ObjectIdentity = ObjectIdentity
snapshot = _Snapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8)
)
_SnapshotRuleNumber_Type = Integer32
_SnapshotRuleNumber_Object = MibScalar
snapshotRuleNumber = _SnapshotRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 1),
    _SnapshotRuleNumber_Type()
)
snapshotRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleNumber.setStatus("current")
_SnapshotRuleTable_Object = MibTable
snapshotRuleTable = _SnapshotRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    snapshotRuleTable.setStatus("obsolete")
_SnapshotRuleEntry_Object = MibTableRow
snapshotRuleEntry = _SnapshotRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1)
)
snapshotRuleEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snapshotRuleName"),
)
if mibBuilder.loadTexts:
    snapshotRuleEntry.setStatus("obsolete")
_SnapshotRuleName_Type = DisplayString
_SnapshotRuleName_Object = MibTableColumn
snapshotRuleName = _SnapshotRuleName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 1),
    _SnapshotRuleName_Type()
)
snapshotRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleName.setStatus("obsolete")
_SnapshotRuleWWN_Type = DisplayString
_SnapshotRuleWWN_Object = MibTableColumn
snapshotRuleWWN = _SnapshotRuleWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 2),
    _SnapshotRuleWWN_Type()
)
snapshotRuleWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleWWN.setStatus("obsolete")
_SnapshotRuleLUN_Type = Unsigned32
_SnapshotRuleLUN_Object = MibTableColumn
snapshotRuleLUN = _SnapshotRuleLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 3),
    _SnapshotRuleLUN_Type()
)
snapshotRuleLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleLUN.setStatus("obsolete")
_SnapshotRulePartitionID_Type = Unsigned32
_SnapshotRulePartitionID_Object = MibTableColumn
snapshotRulePartitionID = _SnapshotRulePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 4),
    _SnapshotRulePartitionID_Type()
)
snapshotRulePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRulePartitionID.setStatus("obsolete")
_SnapshotRuleQueueSize_Type = Integer32
_SnapshotRuleQueueSize_Object = MibTableColumn
snapshotRuleQueueSize = _SnapshotRuleQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 5),
    _SnapshotRuleQueueSize_Type()
)
snapshotRuleQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleQueueSize.setStatus("obsolete")
_SnapshotRuleVolumeLabel_Type = DisplayString
_SnapshotRuleVolumeLabel_Object = MibTableColumn
snapshotRuleVolumeLabel = _SnapshotRuleVolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 2, 1, 6),
    _SnapshotRuleVolumeLabel_Type()
)
snapshotRuleVolumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRuleVolumeLabel.setStatus("obsolete")
_SnapshotScheduleNumber_Type = Integer32
_SnapshotScheduleNumber_Object = MibScalar
snapshotScheduleNumber = _SnapshotScheduleNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 3),
    _SnapshotScheduleNumber_Type()
)
snapshotScheduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleNumber.setStatus("current")
_SnapshotScheduleTable_Object = MibTable
snapshotScheduleTable = _SnapshotScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    snapshotScheduleTable.setStatus("obsolete")
_SnapshotScheduleEntry_Object = MibTableRow
snapshotScheduleEntry = _SnapshotScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 4, 1)
)
snapshotScheduleEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snapshotScheduleRuleName"),
    (0, "BLUEARC-SERVER-MIB", "snapshotScheduleIndex"),
)
if mibBuilder.loadTexts:
    snapshotScheduleEntry.setStatus("obsolete")
_SnapshotScheduleRuleName_Type = DisplayString
_SnapshotScheduleRuleName_Object = MibTableColumn
snapshotScheduleRuleName = _SnapshotScheduleRuleName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 4, 1, 1),
    _SnapshotScheduleRuleName_Type()
)
snapshotScheduleRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleRuleName.setStatus("obsolete")


class _SnapshotScheduleIndex_Type(Integer32):
    """Custom type snapshotScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnapshotScheduleIndex_Type.__name__ = "Integer32"
_SnapshotScheduleIndex_Object = MibTableColumn
snapshotScheduleIndex = _SnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 4, 1, 2),
    _SnapshotScheduleIndex_Type()
)
snapshotScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleIndex.setStatus("obsolete")
_SnapshotScheduleDateTimeSpec_Type = DisplayString
_SnapshotScheduleDateTimeSpec_Object = MibTableColumn
snapshotScheduleDateTimeSpec = _SnapshotScheduleDateTimeSpec_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 4, 1, 3),
    _SnapshotScheduleDateTimeSpec_Type()
)
snapshotScheduleDateTimeSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleDateTimeSpec.setStatus("obsolete")
_SnapshotRulesTable_Object = MibTable
snapshotRulesTable = _SnapshotRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5)
)
if mibBuilder.loadTexts:
    snapshotRulesTable.setStatus("current")
_SnapshotRulesEntry_Object = MibTableRow
snapshotRulesEntry = _SnapshotRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5, 1)
)
snapshotRulesEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snapshotRulesEVS"),
    (0, "BLUEARC-SERVER-MIB", "snapshotRulesName"),
)
if mibBuilder.loadTexts:
    snapshotRulesEntry.setStatus("current")
_SnapshotRulesEVS_Type = Unsigned32
_SnapshotRulesEVS_Object = MibTableColumn
snapshotRulesEVS = _SnapshotRulesEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5, 1, 1),
    _SnapshotRulesEVS_Type()
)
snapshotRulesEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRulesEVS.setStatus("current")
_SnapshotRulesName_Type = DisplayString
_SnapshotRulesName_Object = MibTableColumn
snapshotRulesName = _SnapshotRulesName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5, 1, 2),
    _SnapshotRulesName_Type()
)
snapshotRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRulesName.setStatus("current")
_SnapshotRulesQueueSize_Type = Integer32
_SnapshotRulesQueueSize_Object = MibTableColumn
snapshotRulesQueueSize = _SnapshotRulesQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5, 1, 3),
    _SnapshotRulesQueueSize_Type()
)
snapshotRulesQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRulesQueueSize.setStatus("current")
_SnapshotRulesVolumeLabel_Type = DisplayString
_SnapshotRulesVolumeLabel_Object = MibTableColumn
snapshotRulesVolumeLabel = _SnapshotRulesVolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 5, 1, 4),
    _SnapshotRulesVolumeLabel_Type()
)
snapshotRulesVolumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRulesVolumeLabel.setStatus("current")
_SnapshotSchedulesTable_Object = MibTable
snapshotSchedulesTable = _SnapshotSchedulesTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6)
)
if mibBuilder.loadTexts:
    snapshotSchedulesTable.setStatus("current")
_SnapshotSchedulesEntry_Object = MibTableRow
snapshotSchedulesEntry = _SnapshotSchedulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6, 1)
)
snapshotSchedulesEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snapshotSchedulesEVS"),
    (0, "BLUEARC-SERVER-MIB", "snapshotSchedulesRuleName"),
    (0, "BLUEARC-SERVER-MIB", "snapshotSchedulesIndex"),
)
if mibBuilder.loadTexts:
    snapshotSchedulesEntry.setStatus("current")
_SnapshotSchedulesEVS_Type = Unsigned32
_SnapshotSchedulesEVS_Object = MibTableColumn
snapshotSchedulesEVS = _SnapshotSchedulesEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6, 1, 1),
    _SnapshotSchedulesEVS_Type()
)
snapshotSchedulesEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSchedulesEVS.setStatus("current")
_SnapshotSchedulesRuleName_Type = DisplayString
_SnapshotSchedulesRuleName_Object = MibTableColumn
snapshotSchedulesRuleName = _SnapshotSchedulesRuleName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6, 1, 2),
    _SnapshotSchedulesRuleName_Type()
)
snapshotSchedulesRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSchedulesRuleName.setStatus("current")


class _SnapshotSchedulesIndex_Type(Integer32):
    """Custom type snapshotSchedulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnapshotSchedulesIndex_Type.__name__ = "Integer32"
_SnapshotSchedulesIndex_Object = MibTableColumn
snapshotSchedulesIndex = _SnapshotSchedulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6, 1, 3),
    _SnapshotSchedulesIndex_Type()
)
snapshotSchedulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSchedulesIndex.setStatus("current")
_SnapshotSchedulesDateTimeSpec_Type = DisplayString
_SnapshotSchedulesDateTimeSpec_Object = MibTableColumn
snapshotSchedulesDateTimeSpec = _SnapshotSchedulesDateTimeSpec_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 8, 6, 1, 4),
    _SnapshotSchedulesDateTimeSpec_Type()
)
snapshotSchedulesDateTimeSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSchedulesDateTimeSpec.setStatus("current")
_NvramStats_ObjectIdentity = ObjectIdentity
nvramStats = _NvramStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9)
)


class _NvramFsStatsNumber_Type(Unsigned32):
    """Custom type nvramFsStatsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramFsStatsNumber_Type.__name__ = "Unsigned32"
_NvramFsStatsNumber_Object = MibScalar
nvramFsStatsNumber = _NvramFsStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 1),
    _NvramFsStatsNumber_Type()
)
nvramFsStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsNumber.setStatus("current")
_NvramFsStatsTable_Object = MibTable
nvramFsStatsTable = _NvramFsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    nvramFsStatsTable.setStatus("current")
_NvramFsStatsEntry_Object = MibTableRow
nvramFsStatsEntry = _NvramFsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1)
)
nvramFsStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fsId"),
)
if mibBuilder.loadTexts:
    nvramFsStatsEntry.setStatus("current")
_FsId_Type = Unsigned32
_FsId_Object = MibTableColumn
fsId = _FsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 1),
    _FsId_Type()
)
fsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsId.setStatus("current")
_NvramFsStatsCurrentUsage_Type = Unsigned32
_NvramFsStatsCurrentUsage_Object = MibTableColumn
nvramFsStatsCurrentUsage = _NvramFsStatsCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 2),
    _NvramFsStatsCurrentUsage_Type()
)
nvramFsStatsCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsCurrentUsage.setStatus("current")
_NvramFsStatsCheckpoints_Type = Unsigned32
_NvramFsStatsCheckpoints_Object = MibTableColumn
nvramFsStatsCheckpoints = _NvramFsStatsCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 3),
    _NvramFsStatsCheckpoints_Type()
)
nvramFsStatsCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsCheckpoints.setStatus("current")
_NvramFsStatsActivityCheckpoints_Type = Unsigned32
_NvramFsStatsActivityCheckpoints_Object = MibTableColumn
nvramFsStatsActivityCheckpoints = _NvramFsStatsActivityCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 4),
    _NvramFsStatsActivityCheckpoints_Type()
)
nvramFsStatsActivityCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsActivityCheckpoints.setStatus("current")
_NvramFsStatsWaitedAllocs_Type = Unsigned32
_NvramFsStatsWaitedAllocs_Object = MibTableColumn
nvramFsStatsWaitedAllocs = _NvramFsStatsWaitedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 5),
    _NvramFsStatsWaitedAllocs_Type()
)
nvramFsStatsWaitedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsWaitedAllocs.setStatus("current")
_NvramFsStatsWaitingAllocs_Type = Unsigned32
_NvramFsStatsWaitingAllocs_Object = MibTableColumn
nvramFsStatsWaitingAllocs = _NvramFsStatsWaitingAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 2, 1, 6),
    _NvramFsStatsWaitingAllocs_Type()
)
nvramFsStatsWaitingAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramFsStatsWaitingAllocs.setStatus("current")
_NvramPoolStatsTable_Object = MibTable
nvramPoolStatsTable = _NvramPoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6)
)
if mibBuilder.loadTexts:
    nvramPoolStatsTable.setStatus("current")
_NvramPoolStatsEntry_Object = MibTableRow
nvramPoolStatsEntry = _NvramPoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1)
)
nvramPoolStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "clusterNodeId"),
)
if mibBuilder.loadTexts:
    nvramPoolStatsEntry.setStatus("current")


class _ClusterNodeId_Type(Unsigned32):
    """Custom type clusterNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterNodeId_Type.__name__ = "Unsigned32"
_ClusterNodeId_Object = MibTableColumn
clusterNodeId = _ClusterNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 1),
    _ClusterNodeId_Type()
)
clusterNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeId.setStatus("current")


class _NvramPoolStatsSize_Type(Unsigned32):
    """Custom type nvramPoolStatsSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolStatsSize_Type.__name__ = "Unsigned32"
_NvramPoolStatsSize_Object = MibTableColumn
nvramPoolStatsSize = _NvramPoolStatsSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 2),
    _NvramPoolStatsSize_Type()
)
nvramPoolStatsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolStatsSize.setStatus("current")


class _NvramPoolStatsMaximumUsed_Type(Unsigned32):
    """Custom type nvramPoolStatsMaximumUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolStatsMaximumUsed_Type.__name__ = "Unsigned32"
_NvramPoolStatsMaximumUsed_Object = MibTableColumn
nvramPoolStatsMaximumUsed = _NvramPoolStatsMaximumUsed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 3),
    _NvramPoolStatsMaximumUsed_Type()
)
nvramPoolStatsMaximumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolStatsMaximumUsed.setStatus("current")


class _NvramPoolStatsTotalCurrentUsage_Type(Unsigned32):
    """Custom type nvramPoolStatsTotalCurrentUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolStatsTotalCurrentUsage_Type.__name__ = "Unsigned32"
_NvramPoolStatsTotalCurrentUsage_Object = MibTableColumn
nvramPoolStatsTotalCurrentUsage = _NvramPoolStatsTotalCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 4),
    _NvramPoolStatsTotalCurrentUsage_Type()
)
nvramPoolStatsTotalCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolStatsTotalCurrentUsage.setStatus("current")
_NvramPoolStatsWaitedAllocs_Type = Unsigned32
_NvramPoolStatsWaitedAllocs_Object = MibTableColumn
nvramPoolStatsWaitedAllocs = _NvramPoolStatsWaitedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 5),
    _NvramPoolStatsWaitedAllocs_Type()
)
nvramPoolStatsWaitedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolStatsWaitedAllocs.setStatus("current")


class _NvramPoolStatsWaitingAllocs_Type(Unsigned32):
    """Custom type nvramPoolStatsWaitingAllocs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolStatsWaitingAllocs_Type.__name__ = "Unsigned32"
_NvramPoolStatsWaitingAllocs_Object = MibTableColumn
nvramPoolStatsWaitingAllocs = _NvramPoolStatsWaitingAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 1, 3, 9, 6, 1, 6),
    _NvramPoolStatsWaitingAllocs_Type()
)
nvramPoolStatsWaitingAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolStatsWaitingAllocs.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2)
)
_EtherStats_ObjectIdentity = ObjectIdentity
etherStats = _EtherStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1)
)
_EthOutPkts_Type = Counter64
_EthOutPkts_Object = MibScalar
ethOutPkts = _EthOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 1),
    _EthOutPkts_Type()
)
ethOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutPkts.setStatus("obsolete")
_EthInPkts_Type = Counter64
_EthInPkts_Object = MibScalar
ethInPkts = _EthInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 2),
    _EthInPkts_Type()
)
ethInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInPkts.setStatus("obsolete")
_EthInstInOctetRate_Type = Counter32
_EthInstInOctetRate_Object = MibScalar
ethInstInOctetRate = _EthInstInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 3),
    _EthInstInOctetRate_Type()
)
ethInstInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInstInOctetRate.setStatus("obsolete")
_EthInstOutOctetRate_Type = Counter32
_EthInstOutOctetRate_Object = MibScalar
ethInstOutOctetRate = _EthInstOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 4),
    _EthInstOutOctetRate_Type()
)
ethInstOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInstOutOctetRate.setStatus("obsolete")
_EthPkInOctetRate_Type = Counter32
_EthPkInOctetRate_Object = MibScalar
ethPkInOctetRate = _EthPkInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 5),
    _EthPkInOctetRate_Type()
)
ethPkInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPkInOctetRate.setStatus("obsolete")
_EthPkOutOctetRate_Type = Counter32
_EthPkOutOctetRate_Object = MibScalar
ethPkOutOctetRate = _EthPkOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 6),
    _EthPkOutOctetRate_Type()
)
ethPkOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPkOutOctetRate.setStatus("obsolete")
_EthInFIFODrops_Type = Counter64
_EthInFIFODrops_Object = MibScalar
ethInFIFODrops = _EthInFIFODrops_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 7),
    _EthInFIFODrops_Type()
)
ethInFIFODrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInFIFODrops.setStatus("obsolete")
_EthCRCErrs_Type = Counter64
_EthCRCErrs_Object = MibScalar
ethCRCErrs = _EthCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 8),
    _EthCRCErrs_Type()
)
ethCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCRCErrs.setStatus("obsolete")
_EthOutFIFOUflows_Type = Counter64
_EthOutFIFOUflows_Object = MibScalar
ethOutFIFOUflows = _EthOutFIFOUflows_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 9),
    _EthOutFIFOUflows_Type()
)
ethOutFIFOUflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutFIFOUflows.setStatus("obsolete")
_EthOutOneCollision_Type = Counter64
_EthOutOneCollision_Object = MibScalar
ethOutOneCollision = _EthOutOneCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 10),
    _EthOutOneCollision_Type()
)
ethOutOneCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutOneCollision.setStatus("obsolete")
_EthOutTwoCollision_Type = Counter64
_EthOutTwoCollision_Object = MibScalar
ethOutTwoCollision = _EthOutTwoCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 11),
    _EthOutTwoCollision_Type()
)
ethOutTwoCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutTwoCollision.setStatus("obsolete")
_EthOutFifteenCollision_Type = Counter64
_EthOutFifteenCollision_Object = MibScalar
ethOutFifteenCollision = _EthOutFifteenCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 12),
    _EthOutFifteenCollision_Type()
)
ethOutFifteenCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutFifteenCollision.setStatus("obsolete")
_EthInEvFIFOPktDrop_Type = Counter64
_EthInEvFIFOPktDrop_Object = MibScalar
ethInEvFIFOPktDrop = _EthInEvFIFOPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 13),
    _EthInEvFIFOPktDrop_Type()
)
ethInEvFIFOPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInEvFIFOPktDrop.setStatus("obsolete")
_EthEvFIFOMaxEvents_Type = Counter64
_EthEvFIFOMaxEvents_Object = MibScalar
ethEvFIFOMaxEvents = _EthEvFIFOMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 14),
    _EthEvFIFOMaxEvents_Type()
)
ethEvFIFOMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEvFIFOMaxEvents.setStatus("obsolete")
_EthOutPackets_Type = Counter64
_EthOutPackets_Object = MibScalar
ethOutPackets = _EthOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 15),
    _EthOutPackets_Type()
)
ethOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutPackets.setStatus("obsolete")
_EthInPackets_Type = Counter64
_EthInPackets_Object = MibScalar
ethInPackets = _EthInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 16),
    _EthInPackets_Type()
)
ethInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInPackets.setStatus("obsolete")
_EthTotalPackets_Type = Counter64
_EthTotalPackets_Object = MibScalar
ethTotalPackets = _EthTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 17),
    _EthTotalPackets_Type()
)
ethTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalPackets.setStatus("obsolete")
_EthOutBytes_Type = Counter64
_EthOutBytes_Object = MibScalar
ethOutBytes = _EthOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 18),
    _EthOutBytes_Type()
)
ethOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutBytes.setStatus("obsolete")
_EthInBytes_Type = Counter64
_EthInBytes_Object = MibScalar
ethInBytes = _EthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 19),
    _EthInBytes_Type()
)
ethInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInBytes.setStatus("obsolete")
_EthTotalBytes_Type = Counter64
_EthTotalBytes_Object = MibScalar
ethTotalBytes = _EthTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 20),
    _EthTotalBytes_Type()
)
ethTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalBytes.setStatus("obsolete")
_EthernetStatisticsTable_Object = MibTable
ethernetStatisticsTable = _EthernetStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    ethernetStatisticsTable.setStatus("current")
_EthernetStatisticsEntry_Object = MibTableRow
ethernetStatisticsEntry = _EthernetStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1)
)
ethernetStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetStatisticsEntry.setStatus("current")
_EthernetInstInOctetRate_Type = Counter32
_EthernetInstInOctetRate_Object = MibTableColumn
ethernetInstInOctetRate = _EthernetInstInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 1),
    _EthernetInstInOctetRate_Type()
)
ethernetInstInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInstInOctetRate.setStatus("current")
_EthernetInstOutOctetRate_Type = Counter32
_EthernetInstOutOctetRate_Object = MibTableColumn
ethernetInstOutOctetRate = _EthernetInstOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 2),
    _EthernetInstOutOctetRate_Type()
)
ethernetInstOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInstOutOctetRate.setStatus("current")
_EthernetPkInOctetRate_Type = Counter32
_EthernetPkInOctetRate_Object = MibTableColumn
ethernetPkInOctetRate = _EthernetPkInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 3),
    _EthernetPkInOctetRate_Type()
)
ethernetPkInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPkInOctetRate.setStatus("current")
_EthernetPkOutOctetRate_Type = Counter32
_EthernetPkOutOctetRate_Object = MibTableColumn
ethernetPkOutOctetRate = _EthernetPkOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 4),
    _EthernetPkOutOctetRate_Type()
)
ethernetPkOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPkOutOctetRate.setStatus("current")
_EthernetInFIFODrops_Type = Counter64
_EthernetInFIFODrops_Object = MibTableColumn
ethernetInFIFODrops = _EthernetInFIFODrops_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 5),
    _EthernetInFIFODrops_Type()
)
ethernetInFIFODrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInFIFODrops.setStatus("current")
_EthernetCRCErrs_Type = Counter64
_EthernetCRCErrs_Object = MibTableColumn
ethernetCRCErrs = _EthernetCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 6),
    _EthernetCRCErrs_Type()
)
ethernetCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetCRCErrs.setStatus("current")
_EthernetOutFIFOUflows_Type = Counter64
_EthernetOutFIFOUflows_Object = MibTableColumn
ethernetOutFIFOUflows = _EthernetOutFIFOUflows_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 7),
    _EthernetOutFIFOUflows_Type()
)
ethernetOutFIFOUflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutFIFOUflows.setStatus("current")
_EthernetOutOneCollision_Type = Counter64
_EthernetOutOneCollision_Object = MibTableColumn
ethernetOutOneCollision = _EthernetOutOneCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 8),
    _EthernetOutOneCollision_Type()
)
ethernetOutOneCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutOneCollision.setStatus("current")
_EthernetOutTwoCollision_Type = Counter64
_EthernetOutTwoCollision_Object = MibTableColumn
ethernetOutTwoCollision = _EthernetOutTwoCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 9),
    _EthernetOutTwoCollision_Type()
)
ethernetOutTwoCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutTwoCollision.setStatus("current")
_EthernetOutFifteenCollision_Type = Counter64
_EthernetOutFifteenCollision_Object = MibTableColumn
ethernetOutFifteenCollision = _EthernetOutFifteenCollision_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 10),
    _EthernetOutFifteenCollision_Type()
)
ethernetOutFifteenCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutFifteenCollision.setStatus("current")
_EthernetInEvFIFOPktDrop_Type = Counter64
_EthernetInEvFIFOPktDrop_Object = MibTableColumn
ethernetInEvFIFOPktDrop = _EthernetInEvFIFOPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 11),
    _EthernetInEvFIFOPktDrop_Type()
)
ethernetInEvFIFOPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInEvFIFOPktDrop.setStatus("current")
_EthernetEvFIFOMaxEvents_Type = Counter64
_EthernetEvFIFOMaxEvents_Object = MibTableColumn
ethernetEvFIFOMaxEvents = _EthernetEvFIFOMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 12),
    _EthernetEvFIFOMaxEvents_Type()
)
ethernetEvFIFOMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetEvFIFOMaxEvents.setStatus("current")
_EthernetOutPackets_Type = Counter64
_EthernetOutPackets_Object = MibTableColumn
ethernetOutPackets = _EthernetOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 13),
    _EthernetOutPackets_Type()
)
ethernetOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutPackets.setStatus("current")
_EthernetInPackets_Type = Counter64
_EthernetInPackets_Object = MibTableColumn
ethernetInPackets = _EthernetInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 14),
    _EthernetInPackets_Type()
)
ethernetInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInPackets.setStatus("current")
_EthernetTotalPackets_Type = Counter64
_EthernetTotalPackets_Object = MibTableColumn
ethernetTotalPackets = _EthernetTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 15),
    _EthernetTotalPackets_Type()
)
ethernetTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetTotalPackets.setStatus("current")
_EthernetOutBytes_Type = Counter64
_EthernetOutBytes_Object = MibTableColumn
ethernetOutBytes = _EthernetOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 16),
    _EthernetOutBytes_Type()
)
ethernetOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOutBytes.setStatus("current")
_EthernetInBytes_Type = Counter64
_EthernetInBytes_Object = MibTableColumn
ethernetInBytes = _EthernetInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 17),
    _EthernetInBytes_Type()
)
ethernetInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInBytes.setStatus("current")
_EthernetTotalBytes_Type = Counter64
_EthernetTotalBytes_Object = MibTableColumn
ethernetTotalBytes = _EthernetTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 18),
    _EthernetTotalBytes_Type()
)
ethernetTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetTotalBytes.setStatus("current")
_PausedOffTime_Type = Counter64
_PausedOffTime_Object = MibTableColumn
pausedOffTime = _PausedOffTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 1, 21, 1, 19),
    _PausedOffTime_Type()
)
pausedOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pausedOffTime.setStatus("current")
_TcpipStats_ObjectIdentity = ObjectIdentity
tcpipStats = _TcpipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2)
)
_TcpOpenConns_Type = Counter32
_TcpOpenConns_Object = MibScalar
tcpOpenConns = _TcpOpenConns_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 1),
    _TcpOpenConns_Type()
)
tcpOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOpenConns.setStatus("current")
_TcpMaxOpenConns_Type = Counter32
_TcpMaxOpenConns_Object = MibScalar
tcpMaxOpenConns = _TcpMaxOpenConns_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 2),
    _TcpMaxOpenConns_Type()
)
tcpMaxOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxOpenConns.setStatus("current")
_TcpTotalOpenConns_Type = Counter64
_TcpTotalOpenConns_Object = MibScalar
tcpTotalOpenConns = _TcpTotalOpenConns_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 3),
    _TcpTotalOpenConns_Type()
)
tcpTotalOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTotalOpenConns.setStatus("current")
_TcpFailedInConns_Type = Counter64
_TcpFailedInConns_Object = MibScalar
tcpFailedInConns = _TcpFailedInConns_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 4),
    _TcpFailedInConns_Type()
)
tcpFailedInConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpFailedInConns.setStatus("current")
_TcpFailedOutConns_Type = Counter64
_TcpFailedOutConns_Object = MibScalar
tcpFailedOutConns = _TcpFailedOutConns_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 5),
    _TcpFailedOutConns_Type()
)
tcpFailedOutConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpFailedOutConns.setStatus("current")
_TcpOutSegments_Type = Counter64
_TcpOutSegments_Object = MibScalar
tcpOutSegments = _TcpOutSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 6),
    _TcpOutSegments_Type()
)
tcpOutSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOutSegments.setStatus("obsolete")
_TcpInSegments_Type = Counter64
_TcpInSegments_Object = MibScalar
tcpInSegments = _TcpInSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 7),
    _TcpInSegments_Type()
)
tcpInSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInSegments.setStatus("obsolete")
_TcpReOutSegments_Type = Counter64
_TcpReOutSegments_Object = MibScalar
tcpReOutSegments = _TcpReOutSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 8),
    _TcpReOutSegments_Type()
)
tcpReOutSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpReOutSegments.setStatus("obsolete")
_TcpInvSegments_Type = Counter64
_TcpInvSegments_Object = MibScalar
tcpInvSegments = _TcpInvSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 9),
    _TcpInvSegments_Type()
)
tcpInvSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInvSegments.setStatus("obsolete")
_TcpIPInPkts_Type = Counter64
_TcpIPInPkts_Object = MibScalar
tcpIPInPkts = _TcpIPInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 10),
    _TcpIPInPkts_Type()
)
tcpIPInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInPkts.setStatus("obsolete")
_TcpIPOutPkts_Type = Counter64
_TcpIPOutPkts_Object = MibScalar
tcpIPOutPkts = _TcpIPOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 11),
    _TcpIPOutPkts_Type()
)
tcpIPOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPOutPkts.setStatus("obsolete")
_TcpIPInInvPkts_Type = Counter64
_TcpIPInInvPkts_Object = MibScalar
tcpIPInInvPkts = _TcpIPInInvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 12),
    _TcpIPInInvPkts_Type()
)
tcpIPInInvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvPkts.setStatus("obsolete")
_TcpIPInInvHdrPkts_Type = Counter64
_TcpIPInInvHdrPkts_Object = MibScalar
tcpIPInInvHdrPkts = _TcpIPInInvHdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 13),
    _TcpIPInInvHdrPkts_Type()
)
tcpIPInInvHdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvHdrPkts.setStatus("obsolete")
_TcpIPInInvChksumPkts_Type = Counter64
_TcpIPInInvChksumPkts_Object = MibScalar
tcpIPInInvChksumPkts = _TcpIPInInvChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 14),
    _TcpIPInInvChksumPkts_Type()
)
tcpIPInInvChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvChksumPkts.setStatus("obsolete")
_TcpIPInInvNUcastAddrPkts_Type = Counter64
_TcpIPInInvNUcastAddrPkts_Object = MibScalar
tcpIPInInvNUcastAddrPkts = _TcpIPInInvNUcastAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 15),
    _TcpIPInInvNUcastAddrPkts_Type()
)
tcpIPInInvNUcastAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvNUcastAddrPkts.setStatus("obsolete")
_TcpIPInInvUcastAddrPkts_Type = Counter64
_TcpIPInInvUcastAddrPkts_Object = MibScalar
tcpIPInInvUcastAddrPkts = _TcpIPInInvUcastAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 16),
    _TcpIPInInvUcastAddrPkts_Type()
)
tcpIPInInvUcastAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvUcastAddrPkts.setStatus("obsolete")
_TcpIPInInvSrcAddrPkts_Type = Counter64
_TcpIPInInvSrcAddrPkts_Object = MibScalar
tcpIPInInvSrcAddrPkts = _TcpIPInInvSrcAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 17),
    _TcpIPInInvSrcAddrPkts_Type()
)
tcpIPInInvSrcAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvSrcAddrPkts.setStatus("obsolete")
_TcpIPInInvOptionPkts_Type = Counter64
_TcpIPInInvOptionPkts_Object = MibScalar
tcpIPInInvOptionPkts = _TcpIPInInvOptionPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 18),
    _TcpIPInInvOptionPkts_Type()
)
tcpIPInInvOptionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPInInvOptionPkts.setStatus("obsolete")
_TcpInOversizeSegmentErrs_Type = Counter64
_TcpInOversizeSegmentErrs_Object = MibScalar
tcpInOversizeSegmentErrs = _TcpInOversizeSegmentErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 19),
    _TcpInOversizeSegmentErrs_Type()
)
tcpInOversizeSegmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInOversizeSegmentErrs.setStatus("obsolete")
_TcpInInvChksumPkts_Type = Counter64
_TcpInInvChksumPkts_Object = MibScalar
tcpInInvChksumPkts = _TcpInInvChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 20),
    _TcpInInvChksumPkts_Type()
)
tcpInInvChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInInvChksumPkts.setStatus("obsolete")
_TcpLinkPktDrops_Type = Counter64
_TcpLinkPktDrops_Object = MibScalar
tcpLinkPktDrops = _TcpLinkPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 21),
    _TcpLinkPktDrops_Type()
)
tcpLinkPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLinkPktDrops.setStatus("obsolete")
_TcpStatisticsTable_Object = MibTable
tcpStatisticsTable = _TcpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22)
)
if mibBuilder.loadTexts:
    tcpStatisticsTable.setStatus("current")
_TcpStatisticsEntry_Object = MibTableRow
tcpStatisticsEntry = _TcpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1)
)
tcpStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tcpStatisticsEntry.setStatus("current")
_TcpTxSegments_Type = Counter64
_TcpTxSegments_Object = MibTableColumn
tcpTxSegments = _TcpTxSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 1),
    _TcpTxSegments_Type()
)
tcpTxSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTxSegments.setStatus("current")
_TcpRxSegments_Type = Counter64
_TcpRxSegments_Object = MibTableColumn
tcpRxSegments = _TcpRxSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 2),
    _TcpRxSegments_Type()
)
tcpRxSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRxSegments.setStatus("current")
_TcpReTxSegments_Type = Counter64
_TcpReTxSegments_Object = MibTableColumn
tcpReTxSegments = _TcpReTxSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 3),
    _TcpReTxSegments_Type()
)
tcpReTxSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpReTxSegments.setStatus("current")
_TcpInvalidSegments_Type = Counter64
_TcpInvalidSegments_Object = MibTableColumn
tcpInvalidSegments = _TcpInvalidSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 4),
    _TcpInvalidSegments_Type()
)
tcpInvalidSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInvalidSegments.setStatus("current")
_TcpIPTxPkts_Type = Counter64
_TcpIPTxPkts_Object = MibTableColumn
tcpIPTxPkts = _TcpIPTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 5),
    _TcpIPTxPkts_Type()
)
tcpIPTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPTxPkts.setStatus("current")
_TcpIPRxPkts_Type = Counter64
_TcpIPRxPkts_Object = MibTableColumn
tcpIPRxPkts = _TcpIPRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 6),
    _TcpIPRxPkts_Type()
)
tcpIPRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxPkts.setStatus("current")
_TcpIPRxInvalidPkts_Type = Counter64
_TcpIPRxInvalidPkts_Object = MibTableColumn
tcpIPRxInvalidPkts = _TcpIPRxInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 7),
    _TcpIPRxInvalidPkts_Type()
)
tcpIPRxInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidPkts.setStatus("current")
_TcpIPRxInvalidHdrPkts_Type = Counter64
_TcpIPRxInvalidHdrPkts_Object = MibTableColumn
tcpIPRxInvalidHdrPkts = _TcpIPRxInvalidHdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 8),
    _TcpIPRxInvalidHdrPkts_Type()
)
tcpIPRxInvalidHdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidHdrPkts.setStatus("current")
_TcpIPRxInvalidChksumPkts_Type = Counter64
_TcpIPRxInvalidChksumPkts_Object = MibTableColumn
tcpIPRxInvalidChksumPkts = _TcpIPRxInvalidChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 9),
    _TcpIPRxInvalidChksumPkts_Type()
)
tcpIPRxInvalidChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidChksumPkts.setStatus("obsolete")
_TcpIPRxInvalidNUcastAddrPkts_Type = Counter64
_TcpIPRxInvalidNUcastAddrPkts_Object = MibTableColumn
tcpIPRxInvalidNUcastAddrPkts = _TcpIPRxInvalidNUcastAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 10),
    _TcpIPRxInvalidNUcastAddrPkts_Type()
)
tcpIPRxInvalidNUcastAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidNUcastAddrPkts.setStatus("obsolete")
_TcpIPRxInvalidUcastAddrPkts_Type = Counter64
_TcpIPRxInvalidUcastAddrPkts_Object = MibTableColumn
tcpIPRxInvalidUcastAddrPkts = _TcpIPRxInvalidUcastAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 11),
    _TcpIPRxInvalidUcastAddrPkts_Type()
)
tcpIPRxInvalidUcastAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidUcastAddrPkts.setStatus("obsolete")
_TcpIPRxInvalidSrcAddrPkts_Type = Counter64
_TcpIPRxInvalidSrcAddrPkts_Object = MibTableColumn
tcpIPRxInvalidSrcAddrPkts = _TcpIPRxInvalidSrcAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 12),
    _TcpIPRxInvalidSrcAddrPkts_Type()
)
tcpIPRxInvalidSrcAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidSrcAddrPkts.setStatus("current")
_TcpIPRxInvalidOptionPkts_Type = Counter64
_TcpIPRxInvalidOptionPkts_Object = MibTableColumn
tcpIPRxInvalidOptionPkts = _TcpIPRxInvalidOptionPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 13),
    _TcpIPRxInvalidOptionPkts_Type()
)
tcpIPRxInvalidOptionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPRxInvalidOptionPkts.setStatus("obsolete")
_TcpIPMiscBadSegments_Type = Counter64
_TcpIPMiscBadSegments_Object = MibTableColumn
tcpIPMiscBadSegments = _TcpIPMiscBadSegments_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 14),
    _TcpIPMiscBadSegments_Type()
)
tcpIPMiscBadSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIPMiscBadSegments.setStatus("current")
_TcpRxOversizeSegmentErrs_Type = Counter64
_TcpRxOversizeSegmentErrs_Object = MibTableColumn
tcpRxOversizeSegmentErrs = _TcpRxOversizeSegmentErrs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 15),
    _TcpRxOversizeSegmentErrs_Type()
)
tcpRxOversizeSegmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRxOversizeSegmentErrs.setStatus("obsolete")
_TcpRxInvalidChksumPkts_Type = Counter64
_TcpRxInvalidChksumPkts_Object = MibTableColumn
tcpRxInvalidChksumPkts = _TcpRxInvalidChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 16),
    _TcpRxInvalidChksumPkts_Type()
)
tcpRxInvalidChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRxInvalidChksumPkts.setStatus("current")
_TcpLinkPacketDrops_Type = Counter64
_TcpLinkPacketDrops_Object = MibTableColumn
tcpLinkPacketDrops = _TcpLinkPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 2, 22, 1, 17),
    _TcpLinkPacketDrops_Type()
)
tcpLinkPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLinkPacketDrops.setStatus("obsolete")
_UdpStats_ObjectIdentity = ObjectIdentity
udpStats = _UdpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3)
)
_UdpInShortPkts_Type = Counter64
_UdpInShortPkts_Object = MibScalar
udpInShortPkts = _UdpInShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 1),
    _UdpInShortPkts_Type()
)
udpInShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInShortPkts.setStatus("obsolete")
_UdpInInvChksumPkts_Type = Counter64
_UdpInInvChksumPkts_Object = MibScalar
udpInInvChksumPkts = _UdpInInvChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 2),
    _UdpInInvChksumPkts_Type()
)
udpInInvChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInInvChksumPkts.setStatus("obsolete")
_UdpStatisticsTable_Object = MibTable
udpStatisticsTable = _UdpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    udpStatisticsTable.setStatus("current")
_UdpStatisticsEntry_Object = MibTableRow
udpStatisticsEntry = _UdpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 3, 1)
)
udpStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    udpStatisticsEntry.setStatus("current")
_UdpRxShortPkts_Type = Counter64
_UdpRxShortPkts_Object = MibTableColumn
udpRxShortPkts = _UdpRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 3, 1, 1),
    _UdpRxShortPkts_Type()
)
udpRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpRxShortPkts.setStatus("current")
_UdpRxInvChksumPkts_Type = Counter64
_UdpRxInvChksumPkts_Object = MibTableColumn
udpRxInvChksumPkts = _UdpRxInvChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 3, 3, 1, 2),
    _UdpRxInvChksumPkts_Type()
)
udpRxInvChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpRxInvChksumPkts.setStatus("current")
_AdvipConfig_ObjectIdentity = ObjectIdentity
advipConfig = _AdvipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4)
)
_TcpArpCacheTimeout_Type = Unsigned32
_TcpArpCacheTimeout_Object = MibScalar
tcpArpCacheTimeout = _TcpArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 1),
    _TcpArpCacheTimeout_Type()
)
tcpArpCacheTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpArpCacheTimeout.setStatus("current")


class _TcpBroadCastUsingZero_Type(Integer32):
    """Custom type tcpBroadCastUsingZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpBroadCastUsingZero_Type.__name__ = "Integer32"
_TcpBroadCastUsingZero_Object = MibScalar
tcpBroadCastUsingZero = _TcpBroadCastUsingZero_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 2),
    _TcpBroadCastUsingZero_Type()
)
tcpBroadCastUsingZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpBroadCastUsingZero.setStatus("current")


class _TcpIgnoreICMPEcho_Type(Integer32):
    """Custom type tcpIgnoreICMPEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpIgnoreICMPEcho_Type.__name__ = "Integer32"
_TcpIgnoreICMPEcho_Object = MibScalar
tcpIgnoreICMPEcho = _TcpIgnoreICMPEcho_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 3),
    _TcpIgnoreICMPEcho_Type()
)
tcpIgnoreICMPEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIgnoreICMPEcho.setStatus("current")
_TcpOffSubnetMTU_Type = Integer32
_TcpOffSubnetMTU_Object = MibScalar
tcpOffSubnetMTU = _TcpOffSubnetMTU_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 4),
    _TcpOffSubnetMTU_Type()
)
tcpOffSubnetMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOffSubnetMTU.setStatus("current")


class _TcpAllSubnetsMTU_Type(Integer32):
    """Custom type tcpAllSubnetsMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpAllSubnetsMTU_Type.__name__ = "Integer32"
_TcpAllSubnetsMTU_Object = MibScalar
tcpAllSubnetsMTU = _TcpAllSubnetsMTU_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 5),
    _TcpAllSubnetsMTU_Type()
)
tcpAllSubnetsMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpAllSubnetsMTU.setStatus("current")


class _TcpKeepAlive_Type(Integer32):
    """Custom type tcpKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpKeepAlive_Type.__name__ = "Integer32"
_TcpKeepAlive_Object = MibScalar
tcpKeepAlive = _TcpKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 6),
    _TcpKeepAlive_Type()
)
tcpKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpKeepAlive.setStatus("current")
_TcpKeepAliveTimeout_Type = Unsigned32
_TcpKeepAliveTimeout_Object = MibScalar
tcpKeepAliveTimeout = _TcpKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 4, 7),
    _TcpKeepAliveTimeout_Type()
)
tcpKeepAliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpKeepAliveTimeout.setStatus("current")
_EngipConfig_ObjectIdentity = ObjectIdentity
engipConfig = _EngipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5)
)
_TcpDefWnd_Type = Unsigned32
_TcpDefWnd_Object = MibScalar
tcpDefWnd = _TcpDefWnd_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 1),
    _TcpDefWnd_Type()
)
tcpDefWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpDefWnd.setStatus("current")


class _TcpDelayedAcks_Type(Integer32):
    """Custom type tcpDelayedAcks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpDelayedAcks_Type.__name__ = "Integer32"
_TcpDelayedAcks_Object = MibScalar
tcpDelayedAcks = _TcpDelayedAcks_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 2),
    _TcpDelayedAcks_Type()
)
tcpDelayedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpDelayedAcks.setStatus("current")


class _TcpSlowStartCA_Type(Integer32):
    """Custom type tcpSlowStartCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpSlowStartCA_Type.__name__ = "Integer32"
_TcpSlowStartCA_Object = MibScalar
tcpSlowStartCA = _TcpSlowStartCA_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 3),
    _TcpSlowStartCA_Type()
)
tcpSlowStartCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSlowStartCA.setStatus("current")


class _TcpSSRestartDoubleMSS_Type(Integer32):
    """Custom type tcpSSRestartDoubleMSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpSSRestartDoubleMSS_Type.__name__ = "Integer32"
_TcpSSRestartDoubleMSS_Object = MibScalar
tcpSSRestartDoubleMSS = _TcpSSRestartDoubleMSS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 4),
    _TcpSSRestartDoubleMSS_Type()
)
tcpSSRestartDoubleMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSSRestartDoubleMSS.setStatus("current")


class _TcpNagle_Type(Integer32):
    """Custom type tcpNagle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpNagle_Type.__name__ = "Integer32"
_TcpNagle_Object = MibScalar
tcpNagle = _TcpNagle_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 5),
    _TcpNagle_Type()
)
tcpNagle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpNagle.setStatus("current")


class _TcpSillyWindowAvoid_Type(Integer32):
    """Custom type tcpSillyWindowAvoid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpSillyWindowAvoid_Type.__name__ = "Integer32"
_TcpSillyWindowAvoid_Object = MibScalar
tcpSillyWindowAvoid = _TcpSillyWindowAvoid_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 6),
    _TcpSillyWindowAvoid_Type()
)
tcpSillyWindowAvoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSillyWindowAvoid.setStatus("current")


class _TcpOldAckStrategy_Type(Integer32):
    """Custom type tcpOldAckStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpOldAckStrategy_Type.__name__ = "Integer32"
_TcpOldAckStrategy_Object = MibScalar
tcpOldAckStrategy = _TcpOldAckStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 7),
    _TcpOldAckStrategy_Type()
)
tcpOldAckStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOldAckStrategy.setStatus("current")


class _TcpSlowStartOnIdle_Type(Integer32):
    """Custom type tcpSlowStartOnIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpSlowStartOnIdle_Type.__name__ = "Integer32"
_TcpSlowStartOnIdle_Object = MibScalar
tcpSlowStartOnIdle = _TcpSlowStartOnIdle_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 8),
    _TcpSlowStartOnIdle_Type()
)
tcpSlowStartOnIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSlowStartOnIdle.setStatus("current")


class _TcpFastRetxFastRecovery_Type(Integer32):
    """Custom type tcpFastRetxFastRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpFastRetxFastRecovery_Type.__name__ = "Integer32"
_TcpFastRetxFastRecovery_Object = MibScalar
tcpFastRetxFastRecovery = _TcpFastRetxFastRecovery_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 9),
    _TcpFastRetxFastRecovery_Type()
)
tcpFastRetxFastRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpFastRetxFastRecovery.setStatus("current")


class _TcpOldPushStrategy_Type(Integer32):
    """Custom type tcpOldPushStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpOldPushStrategy_Type.__name__ = "Integer32"
_TcpOldPushStrategy_Object = MibScalar
tcpOldPushStrategy = _TcpOldPushStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 10),
    _TcpOldPushStrategy_Type()
)
tcpOldPushStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOldPushStrategy.setStatus("current")


class _TcpOffSubnetSlowStart_Type(Integer32):
    """Custom type tcpOffSubnetSlowStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpOffSubnetSlowStart_Type.__name__ = "Integer32"
_TcpOffSubnetSlowStart_Object = MibScalar
tcpOffSubnetSlowStart = _TcpOffSubnetSlowStart_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 11),
    _TcpOffSubnetSlowStart_Type()
)
tcpOffSubnetSlowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOffSubnetSlowStart.setStatus("current")


class _TcpUDPCheckSumGen_Type(Integer32):
    """Custom type tcpUDPCheckSumGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpUDPCheckSumGen_Type.__name__ = "Integer32"
_TcpUDPCheckSumGen_Object = MibScalar
tcpUDPCheckSumGen = _TcpUDPCheckSumGen_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 12),
    _TcpUDPCheckSumGen_Type()
)
tcpUDPCheckSumGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpUDPCheckSumGen.setStatus("current")


class _TcpIntelliSeg_Type(Integer32):
    """Custom type tcpIntelliSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TcpIntelliSeg_Type.__name__ = "Integer32"
_TcpIntelliSeg_Object = MibScalar
tcpIntelliSeg = _TcpIntelliSeg_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 5, 13),
    _TcpIntelliSeg_Type()
)
tcpIntelliSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIntelliSeg.setStatus("current")
_NameService_ObjectIdentity = ObjectIdentity
nameService = _NameService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6)
)
_Wins_ObjectIdentity = ObjectIdentity
wins = _Wins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 1)
)
_WinsPrimaryIpAddr_Type = IpAddress
_WinsPrimaryIpAddr_Object = MibScalar
winsPrimaryIpAddr = _WinsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 1, 1),
    _WinsPrimaryIpAddr_Type()
)
winsPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsPrimaryIpAddr.setStatus("current")
_WinsSecondaryIpAddr_Type = IpAddress
_WinsSecondaryIpAddr_Object = MibScalar
winsSecondaryIpAddr = _WinsSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 1, 2),
    _WinsSecondaryIpAddr_Type()
)
winsSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsSecondaryIpAddr.setStatus("current")
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2)
)
_DnsServerNumber_Type = Integer32
_DnsServerNumber_Object = MibScalar
dnsServerNumber = _DnsServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 1),
    _DnsServerNumber_Type()
)
dnsServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerNumber.setStatus("current")
_DnsServerTable_Object = MibTable
dnsServerTable = _DnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    dnsServerTable.setStatus("current")
_DnsServerEntry_Object = MibTableRow
dnsServerEntry = _DnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 2, 1)
)
dnsServerEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "dnsServerIndex"),
)
if mibBuilder.loadTexts:
    dnsServerEntry.setStatus("current")


class _DnsServerIndex_Type(Integer32):
    """Custom type dnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DnsServerIndex_Type.__name__ = "Integer32"
_DnsServerIndex_Object = MibTableColumn
dnsServerIndex = _DnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 2, 1, 1),
    _DnsServerIndex_Type()
)
dnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIndex.setStatus("current")
_DnsServerIpAddress_Type = IpAddress
_DnsServerIpAddress_Object = MibTableColumn
dnsServerIpAddress = _DnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 2, 1, 2),
    _DnsServerIpAddress_Type()
)
dnsServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIpAddress.setStatus("current")
_DnsSearchNumber_Type = Integer32
_DnsSearchNumber_Object = MibScalar
dnsSearchNumber = _DnsSearchNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 3),
    _DnsSearchNumber_Type()
)
dnsSearchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSearchNumber.setStatus("current")
_DnsSearchTable_Object = MibTable
dnsSearchTable = _DnsSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 4)
)
if mibBuilder.loadTexts:
    dnsSearchTable.setStatus("current")
_DnsSearchEntry_Object = MibTableRow
dnsSearchEntry = _DnsSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 4, 1)
)
dnsSearchEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "dnsSearchIndex"),
)
if mibBuilder.loadTexts:
    dnsSearchEntry.setStatus("current")


class _DnsSearchIndex_Type(Integer32):
    """Custom type dnsSearchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DnsSearchIndex_Type.__name__ = "Integer32"
_DnsSearchIndex_Object = MibTableColumn
dnsSearchIndex = _DnsSearchIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 4, 1, 1),
    _DnsSearchIndex_Type()
)
dnsSearchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSearchIndex.setStatus("current")
_DnsSearchString_Type = DisplayString
_DnsSearchString_Object = MibTableColumn
dnsSearchString = _DnsSearchString_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 2, 4, 1, 2),
    _DnsSearchString_Type()
)
dnsSearchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSearchString.setStatus("current")
_NsOrder_ObjectIdentity = ObjectIdentity
nsOrder = _NsOrder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3)
)
_NameServiceNumber_Type = Integer32
_NameServiceNumber_Object = MibScalar
nameServiceNumber = _NameServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3, 1),
    _NameServiceNumber_Type()
)
nameServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameServiceNumber.setStatus("current")
_NameServiceTable_Object = MibTable
nameServiceTable = _NameServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    nameServiceTable.setStatus("current")
_NameServiceEntry_Object = MibTableRow
nameServiceEntry = _NameServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3, 2, 1)
)
nameServiceEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nameServiceOrder"),
)
if mibBuilder.loadTexts:
    nameServiceEntry.setStatus("current")


class _NameServiceOrder_Type(Integer32):
    """Custom type nameServiceOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NameServiceOrder_Type.__name__ = "Integer32"
_NameServiceOrder_Object = MibTableColumn
nameServiceOrder = _NameServiceOrder_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3, 2, 1, 1),
    _NameServiceOrder_Type()
)
nameServiceOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameServiceOrder.setStatus("current")


class _NameServiceType_Type(Integer32):
    """Custom type nameServiceType based on Integer32"""
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
        *(("dns", 1),
          ("nis", 3),
          ("unknown", 4),
          ("wins", 2))
    )


_NameServiceType_Type.__name__ = "Integer32"
_NameServiceType_Object = MibTableColumn
nameServiceType = _NameServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 6, 3, 2, 1, 2),
    _NameServiceType_Type()
)
nameServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameServiceType.setStatus("current")
_Nis_ObjectIdentity = ObjectIdentity
nis = _Nis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7)
)


class _NisEnabled_Type(Integer32):
    """Custom type nisEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NisEnabled_Type.__name__ = "Integer32"
_NisEnabled_Object = MibScalar
nisEnabled = _NisEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 1),
    _NisEnabled_Type()
)
nisEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisEnabled.setStatus("current")
_NisDomain_Type = DisplayString
_NisDomain_Object = MibScalar
nisDomain = _NisDomain_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 2),
    _NisDomain_Type()
)
nisDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisDomain.setStatus("current")
_NisCurrentMaster_Type = DisplayString
_NisCurrentMaster_Object = MibScalar
nisCurrentMaster = _NisCurrentMaster_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 3),
    _NisCurrentMaster_Type()
)
nisCurrentMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisCurrentMaster.setStatus("current")


class _NisServerBroadcastEnabled_Type(Integer32):
    """Custom type nisServerBroadcastEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NisServerBroadcastEnabled_Type.__name__ = "Integer32"
_NisServerBroadcastEnabled_Object = MibScalar
nisServerBroadcastEnabled = _NisServerBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 4),
    _NisServerBroadcastEnabled_Type()
)
nisServerBroadcastEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServerBroadcastEnabled.setStatus("current")


class _NisVerificationEnabled_Type(Integer32):
    """Custom type nisVerificationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NisVerificationEnabled_Type.__name__ = "Integer32"
_NisVerificationEnabled_Object = MibScalar
nisVerificationEnabled = _NisVerificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 5),
    _NisVerificationEnabled_Type()
)
nisVerificationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisVerificationEnabled.setStatus("current")
_NisTimeout_Type = Unsigned32
_NisTimeout_Object = MibScalar
nisTimeout = _NisTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 6),
    _NisTimeout_Type()
)
nisTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisTimeout.setStatus("current")
_NisRebindInterval_Type = Unsigned32
_NisRebindInterval_Object = MibScalar
nisRebindInterval = _NisRebindInterval_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 7),
    _NisRebindInterval_Type()
)
nisRebindInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisRebindInterval.setStatus("current")
_NisUserGroupTimeout_Type = Unsigned32
_NisUserGroupTimeout_Object = MibScalar
nisUserGroupTimeout = _NisUserGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 8),
    _NisUserGroupTimeout_Type()
)
nisUserGroupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisUserGroupTimeout.setStatus("current")
_NisServerNumber_Type = Integer32
_NisServerNumber_Object = MibScalar
nisServerNumber = _NisServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 9),
    _NisServerNumber_Type()
)
nisServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServerNumber.setStatus("current")
_NisServerTable_Object = MibTable
nisServerTable = _NisServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 10)
)
if mibBuilder.loadTexts:
    nisServerTable.setStatus("current")
_NisServerEntry_Object = MibTableRow
nisServerEntry = _NisServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 10, 1)
)
nisServerEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nisServerIndex"),
)
if mibBuilder.loadTexts:
    nisServerEntry.setStatus("current")


class _NisServerIndex_Type(Integer32):
    """Custom type nisServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_NisServerIndex_Type.__name__ = "Integer32"
_NisServerIndex_Object = MibTableColumn
nisServerIndex = _NisServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 10, 1, 1),
    _NisServerIndex_Type()
)
nisServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServerIndex.setStatus("current")
_NisServerIpAddress_Type = IpAddress
_NisServerIpAddress_Object = MibTableColumn
nisServerIpAddress = _NisServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 10, 1, 2),
    _NisServerIpAddress_Type()
)
nisServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServerIpAddress.setStatus("current")
_NisServerPriority_Type = Integer32
_NisServerPriority_Object = MibTableColumn
nisServerPriority = _NisServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 2, 7, 10, 1, 3),
    _NisServerPriority_Type()
)
nisServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServerPriority.setStatus("current")
_FileProtocol_ObjectIdentity = ObjectIdentity
fileProtocol = _FileProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 1)
)


class _SecurityMode_Type(Integer32):
    """Custom type securityMode based on Integer32"""
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
        *(("mixed", 1),
          ("nosecurity", 3),
          ("unix", 2),
          ("unknown", 4))
    )


_SecurityMode_Type.__name__ = "Integer32"
_SecurityMode_Object = MibScalar
securityMode = _SecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 1, 1),
    _SecurityMode_Type()
)
securityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityMode.setStatus("current")
_SecurityDomain_Type = DisplayString
_SecurityDomain_Object = MibScalar
securityDomain = _SecurityDomain_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 1, 2),
    _SecurityDomain_Type()
)
securityDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityDomain.setStatus("current")
_Cifs_ObjectIdentity = ObjectIdentity
cifs = _Cifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2)
)
_Shares_ObjectIdentity = ObjectIdentity
shares = _Shares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1)
)
_ShareNumber_Type = Integer32
_ShareNumber_Object = MibScalar
shareNumber = _ShareNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 1),
    _ShareNumber_Type()
)
shareNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNumber.setStatus("current")
_ShareTable_Object = MibTable
shareTable = _ShareTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    shareTable.setStatus("obsolete")
_ShareEntry_Object = MibTableRow
shareEntry = _ShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1)
)
shareEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "shareName"),
)
if mibBuilder.loadTexts:
    shareEntry.setStatus("obsolete")
_ShareName_Type = DisplayString
_ShareName_Object = MibTableColumn
shareName = _ShareName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 1),
    _ShareName_Type()
)
shareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareName.setStatus("obsolete")
_SharePath_Type = DisplayString
_SharePath_Object = MibTableColumn
sharePath = _SharePath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 2),
    _SharePath_Type()
)
sharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharePath.setStatus("obsolete")
_ShareComment_Type = DisplayString
_ShareComment_Object = MibTableColumn
shareComment = _ShareComment_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 3),
    _ShareComment_Type()
)
shareComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareComment.setStatus("obsolete")
_ShareUsers_Type = Unsigned32
_ShareUsers_Object = MibTableColumn
shareUsers = _ShareUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 4),
    _ShareUsers_Type()
)
shareUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareUsers.setStatus("obsolete")
_ShareWWN_Type = DisplayString
_ShareWWN_Object = MibTableColumn
shareWWN = _ShareWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 5),
    _ShareWWN_Type()
)
shareWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareWWN.setStatus("obsolete")
_ShareLUN_Type = Unsigned32
_ShareLUN_Object = MibTableColumn
shareLUN = _ShareLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 6),
    _ShareLUN_Type()
)
shareLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareLUN.setStatus("obsolete")
_SharePartitionID_Type = Unsigned32
_SharePartitionID_Object = MibTableColumn
sharePartitionID = _SharePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 7),
    _SharePartitionID_Type()
)
sharePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharePartitionID.setStatus("obsolete")
_ShareMaxUsers_Type = Integer32
_ShareMaxUsers_Object = MibTableColumn
shareMaxUsers = _ShareMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 2, 1, 8),
    _ShareMaxUsers_Type()
)
shareMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareMaxUsers.setStatus("obsolete")
_CifsShareTable_Object = MibTable
cifsShareTable = _CifsShareTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cifsShareTable.setStatus("current")
_CifsShareEntry_Object = MibTableRow
cifsShareEntry = _CifsShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1)
)
cifsShareEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "cifsShareEvsId"),
    (0, "BLUEARC-SERVER-MIB", "cifsShareName"),
)
if mibBuilder.loadTexts:
    cifsShareEntry.setStatus("current")


class _CifsShareEvsId_Type(Integer32):
    """Custom type cifsShareEvsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CifsShareEvsId_Type.__name__ = "Integer32"
_CifsShareEvsId_Object = MibTableColumn
cifsShareEvsId = _CifsShareEvsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 1),
    _CifsShareEvsId_Type()
)
cifsShareEvsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareEvsId.setStatus("current")
_CifsShareName_Type = DisplayString
_CifsShareName_Object = MibTableColumn
cifsShareName = _CifsShareName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 2),
    _CifsShareName_Type()
)
cifsShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareName.setStatus("current")
_CifsSharePath_Type = DisplayString
_CifsSharePath_Object = MibTableColumn
cifsSharePath = _CifsSharePath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 3),
    _CifsSharePath_Type()
)
cifsSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSharePath.setStatus("current")
_CifsShareComment_Type = DisplayString
_CifsShareComment_Object = MibTableColumn
cifsShareComment = _CifsShareComment_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 4),
    _CifsShareComment_Type()
)
cifsShareComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareComment.setStatus("current")
_CifsShareUsers_Type = Unsigned32
_CifsShareUsers_Object = MibTableColumn
cifsShareUsers = _CifsShareUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 5),
    _CifsShareUsers_Type()
)
cifsShareUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareUsers.setStatus("current")
_CifsShareMaxUsers_Type = Integer32
_CifsShareMaxUsers_Object = MibTableColumn
cifsShareMaxUsers = _CifsShareMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 6),
    _CifsShareMaxUsers_Type()
)
cifsShareMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareMaxUsers.setStatus("current")
_CifsShareSpanId_Type = Integer32
_CifsShareSpanId_Object = MibTableColumn
cifsShareSpanId = _CifsShareSpanId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 1, 3, 1, 7),
    _CifsShareSpanId_Type()
)
cifsShareSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareSpanId.setStatus("current")
_ShareAccess_ObjectIdentity = ObjectIdentity
shareAccess = _ShareAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2)
)
_ShareAccessNumber_Type = Integer32
_ShareAccessNumber_Object = MibScalar
shareAccessNumber = _ShareAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 1),
    _ShareAccessNumber_Type()
)
shareAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareAccessNumber.setStatus("current")
_ShareAccessTable_Object = MibTable
shareAccessTable = _ShareAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    shareAccessTable.setStatus("current")
_ShareAccessEntry_Object = MibTableRow
shareAccessEntry = _ShareAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2, 1)
)
shareAccessEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "shareAccessIndex"),
    (0, "BLUEARC-SERVER-MIB", "shareAccessShareName"),
)
if mibBuilder.loadTexts:
    shareAccessEntry.setStatus("current")


class _ShareAccessIndex_Type(Integer32):
    """Custom type shareAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ShareAccessIndex_Type.__name__ = "Integer32"
_ShareAccessIndex_Object = MibTableColumn
shareAccessIndex = _ShareAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2, 1, 1),
    _ShareAccessIndex_Type()
)
shareAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareAccessIndex.setStatus("current")
_ShareAccessShareName_Type = DisplayString
_ShareAccessShareName_Object = MibTableColumn
shareAccessShareName = _ShareAccessShareName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2, 1, 2),
    _ShareAccessShareName_Type()
)
shareAccessShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareAccessShareName.setStatus("current")
_ShareAccessName_Type = DisplayString
_ShareAccessName_Object = MibTableColumn
shareAccessName = _ShareAccessName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2, 1, 3),
    _ShareAccessName_Type()
)
shareAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareAccessName.setStatus("current")


class _ShareAccessPerms_Type(Integer32):
    """Custom type shareAccessPerms based on Integer32"""
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
        *(("change", 3),
          ("fullControl", 4),
          ("noAccess", 1),
          ("read", 2))
    )


_ShareAccessPerms_Type.__name__ = "Integer32"
_ShareAccessPerms_Object = MibTableColumn
shareAccessPerms = _ShareAccessPerms_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 2, 2, 1, 4),
    _ShareAccessPerms_Type()
)
shareAccessPerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareAccessPerms.setStatus("current")
_CifsStats_ObjectIdentity = ObjectIdentity
cifsStats = _CifsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3)
)
_CifsClients_Type = Unsigned32
_CifsClients_Object = MibScalar
cifsClients = _CifsClients_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 1),
    _CifsClients_Type()
)
cifsClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsClients.setStatus("obsolete")
_CifsMkdirCalls_Type = Unsigned32
_CifsMkdirCalls_Object = MibScalar
cifsMkdirCalls = _CifsMkdirCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 2),
    _CifsMkdirCalls_Type()
)
cifsMkdirCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMkdirCalls.setStatus("obsolete")
_CifsRmdirCalls_Type = Unsigned32
_CifsRmdirCalls_Object = MibScalar
cifsRmdirCalls = _CifsRmdirCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 3),
    _CifsRmdirCalls_Type()
)
cifsRmdirCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsRmdirCalls.setStatus("obsolete")
_CifsOpenCalls_Type = Unsigned32
_CifsOpenCalls_Object = MibScalar
cifsOpenCalls = _CifsOpenCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 4),
    _CifsOpenCalls_Type()
)
cifsOpenCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpenCalls.setStatus("obsolete")
_CifsCreateCalls_Type = Unsigned32
_CifsCreateCalls_Object = MibScalar
cifsCreateCalls = _CifsCreateCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 5),
    _CifsCreateCalls_Type()
)
cifsCreateCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsCreateCalls.setStatus("obsolete")
_CifsCloseCalls_Type = Unsigned32
_CifsCloseCalls_Object = MibScalar
cifsCloseCalls = _CifsCloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 6),
    _CifsCloseCalls_Type()
)
cifsCloseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsCloseCalls.setStatus("obsolete")
_CifsFlushCalls_Type = Unsigned32
_CifsFlushCalls_Object = MibScalar
cifsFlushCalls = _CifsFlushCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 7),
    _CifsFlushCalls_Type()
)
cifsFlushCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsFlushCalls.setStatus("obsolete")
_CifsUnlinkCalls_Type = Unsigned32
_CifsUnlinkCalls_Object = MibScalar
cifsUnlinkCalls = _CifsUnlinkCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 8),
    _CifsUnlinkCalls_Type()
)
cifsUnlinkCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsUnlinkCalls.setStatus("obsolete")
_CifsRenameCalls_Type = Unsigned32
_CifsRenameCalls_Object = MibScalar
cifsRenameCalls = _CifsRenameCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 9),
    _CifsRenameCalls_Type()
)
cifsRenameCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsRenameCalls.setStatus("obsolete")
_CifsGetatrCalls_Type = Unsigned32
_CifsGetatrCalls_Object = MibScalar
cifsGetatrCalls = _CifsGetatrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 10),
    _CifsGetatrCalls_Type()
)
cifsGetatrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsGetatrCalls.setStatus("obsolete")
_CifsSetatrCalls_Type = Unsigned32
_CifsSetatrCalls_Object = MibScalar
cifsSetatrCalls = _CifsSetatrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 11),
    _CifsSetatrCalls_Type()
)
cifsSetatrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSetatrCalls.setStatus("obsolete")
_CifsReadCalls_Type = Unsigned32
_CifsReadCalls_Object = MibScalar
cifsReadCalls = _CifsReadCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 12),
    _CifsReadCalls_Type()
)
cifsReadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsReadCalls.setStatus("obsolete")
_CifsWriteCalls_Type = Unsigned32
_CifsWriteCalls_Object = MibScalar
cifsWriteCalls = _CifsWriteCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 13),
    _CifsWriteCalls_Type()
)
cifsWriteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWriteCalls.setStatus("obsolete")
_CifsMknewCalls_Type = Unsigned32
_CifsMknewCalls_Object = MibScalar
cifsMknewCalls = _CifsMknewCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 14),
    _CifsMknewCalls_Type()
)
cifsMknewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMknewCalls.setStatus("obsolete")
_CifsChkpthCalls_Type = Unsigned32
_CifsChkpthCalls_Object = MibScalar
cifsChkpthCalls = _CifsChkpthCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 15),
    _CifsChkpthCalls_Type()
)
cifsChkpthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsChkpthCalls.setStatus("obsolete")
_CifsLseekCalls_Type = Unsigned32
_CifsLseekCalls_Object = MibScalar
cifsLseekCalls = _CifsLseekCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 16),
    _CifsLseekCalls_Type()
)
cifsLseekCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsLseekCalls.setStatus("obsolete")
_CifsReadBrawCalls_Type = Unsigned32
_CifsReadBrawCalls_Object = MibScalar
cifsReadBrawCalls = _CifsReadBrawCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 17),
    _CifsReadBrawCalls_Type()
)
cifsReadBrawCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsReadBrawCalls.setStatus("obsolete")
_CifsWriteBrawCalls_Type = Unsigned32
_CifsWriteBrawCalls_Object = MibScalar
cifsWriteBrawCalls = _CifsWriteBrawCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 18),
    _CifsWriteBrawCalls_Type()
)
cifsWriteBrawCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWriteBrawCalls.setStatus("obsolete")
_CifsLockingXCalls_Type = Unsigned32
_CifsLockingXCalls_Object = MibScalar
cifsLockingXCalls = _CifsLockingXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 19),
    _CifsLockingXCalls_Type()
)
cifsLockingXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsLockingXCalls.setStatus("obsolete")
_CifsTransCalls_Type = Unsigned32
_CifsTransCalls_Object = MibScalar
cifsTransCalls = _CifsTransCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 20),
    _CifsTransCalls_Type()
)
cifsTransCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTransCalls.setStatus("obsolete")
_CifsEchoCalls_Type = Unsigned32
_CifsEchoCalls_Object = MibScalar
cifsEchoCalls = _CifsEchoCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 21),
    _CifsEchoCalls_Type()
)
cifsEchoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsEchoCalls.setStatus("obsolete")
_CifsWriteCloseCalls_Type = Unsigned32
_CifsWriteCloseCalls_Object = MibScalar
cifsWriteCloseCalls = _CifsWriteCloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 22),
    _CifsWriteCloseCalls_Type()
)
cifsWriteCloseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWriteCloseCalls.setStatus("obsolete")
_CifsOpenXCalls_Type = Unsigned32
_CifsOpenXCalls_Object = MibScalar
cifsOpenXCalls = _CifsOpenXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 23),
    _CifsOpenXCalls_Type()
)
cifsOpenXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpenXCalls.setStatus("obsolete")
_CifsReadXCalls_Type = Unsigned32
_CifsReadXCalls_Object = MibScalar
cifsReadXCalls = _CifsReadXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 24),
    _CifsReadXCalls_Type()
)
cifsReadXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsReadXCalls.setStatus("obsolete")
_CifsWriteXCalls_Type = Unsigned32
_CifsWriteXCalls_Object = MibScalar
cifsWriteXCalls = _CifsWriteXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 25),
    _CifsWriteXCalls_Type()
)
cifsWriteXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWriteXCalls.setStatus("obsolete")
_CifsTrans2Calls_Type = Unsigned32
_CifsTrans2Calls_Object = MibScalar
cifsTrans2Calls = _CifsTrans2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 26),
    _CifsTrans2Calls_Type()
)
cifsTrans2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTrans2Calls.setStatus("obsolete")
_CifsFindCloseCalls_Type = Unsigned32
_CifsFindCloseCalls_Object = MibScalar
cifsFindCloseCalls = _CifsFindCloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 27),
    _CifsFindCloseCalls_Type()
)
cifsFindCloseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsFindCloseCalls.setStatus("obsolete")
_CifsTdisCalls_Type = Unsigned32
_CifsTdisCalls_Object = MibScalar
cifsTdisCalls = _CifsTdisCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 28),
    _CifsTdisCalls_Type()
)
cifsTdisCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTdisCalls.setStatus("obsolete")
_CifsNegProtCalls_Type = Unsigned32
_CifsNegProtCalls_Object = MibScalar
cifsNegProtCalls = _CifsNegProtCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 29),
    _CifsNegProtCalls_Type()
)
cifsNegProtCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNegProtCalls.setStatus("obsolete")
_CifsSessSetupXCalls_Type = Unsigned32
_CifsSessSetupXCalls_Object = MibScalar
cifsSessSetupXCalls = _CifsSessSetupXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 30),
    _CifsSessSetupXCalls_Type()
)
cifsSessSetupXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSessSetupXCalls.setStatus("obsolete")
_CifsUlogoffXCalls_Type = Unsigned32
_CifsUlogoffXCalls_Object = MibScalar
cifsUlogoffXCalls = _CifsUlogoffXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 31),
    _CifsUlogoffXCalls_Type()
)
cifsUlogoffXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsUlogoffXCalls.setStatus("obsolete")
_CifsTconXCalls_Type = Unsigned32
_CifsTconXCalls_Object = MibScalar
cifsTconXCalls = _CifsTconXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 32),
    _CifsTconXCalls_Type()
)
cifsTconXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTconXCalls.setStatus("obsolete")
_CifsDskattrCalls_Type = Unsigned32
_CifsDskattrCalls_Object = MibScalar
cifsDskattrCalls = _CifsDskattrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 33),
    _CifsDskattrCalls_Type()
)
cifsDskattrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDskattrCalls.setStatus("obsolete")
_CifsSearchCalls_Type = Unsigned32
_CifsSearchCalls_Object = MibScalar
cifsSearchCalls = _CifsSearchCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 34),
    _CifsSearchCalls_Type()
)
cifsSearchCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSearchCalls.setStatus("obsolete")
_CifsNTtransCalls_Type = Unsigned32
_CifsNTtransCalls_Object = MibScalar
cifsNTtransCalls = _CifsNTtransCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 35),
    _CifsNTtransCalls_Type()
)
cifsNTtransCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNTtransCalls.setStatus("obsolete")
_CifsNTtranssCalls_Type = Unsigned32
_CifsNTtranssCalls_Object = MibScalar
cifsNTtranssCalls = _CifsNTtranssCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 36),
    _CifsNTtranssCalls_Type()
)
cifsNTtranssCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNTtranssCalls.setStatus("obsolete")
_CifsNTcreateXCalls_Type = Unsigned32
_CifsNTcreateXCalls_Object = MibScalar
cifsNTcreateXCalls = _CifsNTcreateXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 37),
    _CifsNTcreateXCalls_Type()
)
cifsNTcreateXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNTcreateXCalls.setStatus("obsolete")
_CifsNTcancelCalls_Type = Unsigned32
_CifsNTcancelCalls_Object = MibScalar
cifsNTcancelCalls = _CifsNTcancelCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 38),
    _CifsNTcancelCalls_Type()
)
cifsNTcancelCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNTcancelCalls.setStatus("obsolete")
_CifsStatsTable_Object = MibTable
cifsStatsTable = _CifsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39)
)
if mibBuilder.loadTexts:
    cifsStatsTable.setStatus("current")
_CifsStatsEntry_Object = MibTableRow
cifsStatsEntry = _CifsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1)
)
cifsStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "cifsStatsClusterNode"),
)
if mibBuilder.loadTexts:
    cifsStatsEntry.setStatus("current")
_CifsStatsClusterNode_Type = Unsigned32
_CifsStatsClusterNode_Object = MibTableColumn
cifsStatsClusterNode = _CifsStatsClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 1),
    _CifsStatsClusterNode_Type()
)
cifsStatsClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsStatsClusterNode.setStatus("current")
_Clients_Type = Unsigned32
_Clients_Object = MibTableColumn
clients = _Clients_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 2),
    _Clients_Type()
)
clients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clients.setStatus("current")
_MkdirCalls_Type = Unsigned32
_MkdirCalls_Object = MibTableColumn
mkdirCalls = _MkdirCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 3),
    _MkdirCalls_Type()
)
mkdirCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mkdirCalls.setStatus("current")
_RmdirCalls_Type = Unsigned32
_RmdirCalls_Object = MibTableColumn
rmdirCalls = _RmdirCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 4),
    _RmdirCalls_Type()
)
rmdirCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmdirCalls.setStatus("current")
_OpenCalls_Type = Unsigned32
_OpenCalls_Object = MibTableColumn
openCalls = _OpenCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 5),
    _OpenCalls_Type()
)
openCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openCalls.setStatus("current")
_CreateCalls_Type = Unsigned32
_CreateCalls_Object = MibTableColumn
createCalls = _CreateCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 6),
    _CreateCalls_Type()
)
createCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    createCalls.setStatus("current")
_CloseCalls_Type = Unsigned32
_CloseCalls_Object = MibTableColumn
closeCalls = _CloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 7),
    _CloseCalls_Type()
)
closeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    closeCalls.setStatus("current")
_FlushCalls_Type = Unsigned32
_FlushCalls_Object = MibTableColumn
flushCalls = _FlushCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 8),
    _FlushCalls_Type()
)
flushCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flushCalls.setStatus("current")
_UnlinkCalls_Type = Unsigned32
_UnlinkCalls_Object = MibTableColumn
unlinkCalls = _UnlinkCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 9),
    _UnlinkCalls_Type()
)
unlinkCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unlinkCalls.setStatus("current")
_RenameCalls_Type = Unsigned32
_RenameCalls_Object = MibTableColumn
renameCalls = _RenameCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 10),
    _RenameCalls_Type()
)
renameCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    renameCalls.setStatus("current")
_GetatrCalls_Type = Unsigned32
_GetatrCalls_Object = MibTableColumn
getatrCalls = _GetatrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 11),
    _GetatrCalls_Type()
)
getatrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getatrCalls.setStatus("current")
_SetatrCalls_Type = Unsigned32
_SetatrCalls_Object = MibTableColumn
setatrCalls = _SetatrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 12),
    _SetatrCalls_Type()
)
setatrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setatrCalls.setStatus("current")
_ReadCalls_Type = Unsigned32
_ReadCalls_Object = MibTableColumn
readCalls = _ReadCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 13),
    _ReadCalls_Type()
)
readCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCalls.setStatus("current")
_WriteCalls_Type = Unsigned32
_WriteCalls_Object = MibTableColumn
writeCalls = _WriteCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 14),
    _WriteCalls_Type()
)
writeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeCalls.setStatus("current")
_MknewCalls_Type = Unsigned32
_MknewCalls_Object = MibTableColumn
mknewCalls = _MknewCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 15),
    _MknewCalls_Type()
)
mknewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mknewCalls.setStatus("current")
_ChkpthCalls_Type = Unsigned32
_ChkpthCalls_Object = MibTableColumn
chkpthCalls = _ChkpthCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 16),
    _ChkpthCalls_Type()
)
chkpthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpthCalls.setStatus("current")
_LseekCalls_Type = Unsigned32
_LseekCalls_Object = MibTableColumn
lseekCalls = _LseekCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 17),
    _LseekCalls_Type()
)
lseekCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseekCalls.setStatus("current")
_ReadBrawCalls_Type = Unsigned32
_ReadBrawCalls_Object = MibTableColumn
readBrawCalls = _ReadBrawCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 18),
    _ReadBrawCalls_Type()
)
readBrawCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readBrawCalls.setStatus("current")
_WriteBrawCalls_Type = Unsigned32
_WriteBrawCalls_Object = MibTableColumn
writeBrawCalls = _WriteBrawCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 19),
    _WriteBrawCalls_Type()
)
writeBrawCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeBrawCalls.setStatus("current")
_LockingXCalls_Type = Unsigned32
_LockingXCalls_Object = MibTableColumn
lockingXCalls = _LockingXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 20),
    _LockingXCalls_Type()
)
lockingXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockingXCalls.setStatus("current")
_TransCalls_Type = Unsigned32
_TransCalls_Object = MibTableColumn
transCalls = _TransCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 21),
    _TransCalls_Type()
)
transCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transCalls.setStatus("current")
_EchoCalls_Type = Unsigned32
_EchoCalls_Object = MibTableColumn
echoCalls = _EchoCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 22),
    _EchoCalls_Type()
)
echoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoCalls.setStatus("current")
_WriteCloseCalls_Type = Unsigned32
_WriteCloseCalls_Object = MibTableColumn
writeCloseCalls = _WriteCloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 23),
    _WriteCloseCalls_Type()
)
writeCloseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeCloseCalls.setStatus("current")
_OpenXCalls_Type = Unsigned32
_OpenXCalls_Object = MibTableColumn
openXCalls = _OpenXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 24),
    _OpenXCalls_Type()
)
openXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openXCalls.setStatus("current")
_ReadXCalls_Type = Unsigned32
_ReadXCalls_Object = MibTableColumn
readXCalls = _ReadXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 25),
    _ReadXCalls_Type()
)
readXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readXCalls.setStatus("current")
_WriteXCalls_Type = Unsigned32
_WriteXCalls_Object = MibTableColumn
writeXCalls = _WriteXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 26),
    _WriteXCalls_Type()
)
writeXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeXCalls.setStatus("current")
_Trans2Calls_Type = Unsigned32
_Trans2Calls_Object = MibTableColumn
trans2Calls = _Trans2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 27),
    _Trans2Calls_Type()
)
trans2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trans2Calls.setStatus("current")
_FindCloseCalls_Type = Unsigned32
_FindCloseCalls_Object = MibTableColumn
findCloseCalls = _FindCloseCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 28),
    _FindCloseCalls_Type()
)
findCloseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    findCloseCalls.setStatus("current")
_TdisCalls_Type = Unsigned32
_TdisCalls_Object = MibTableColumn
tdisCalls = _TdisCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 29),
    _TdisCalls_Type()
)
tdisCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdisCalls.setStatus("current")
_NegProtCalls_Type = Unsigned32
_NegProtCalls_Object = MibTableColumn
negProtCalls = _NegProtCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 30),
    _NegProtCalls_Type()
)
negProtCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negProtCalls.setStatus("current")
_SessSetupXCalls_Type = Unsigned32
_SessSetupXCalls_Object = MibTableColumn
sessSetupXCalls = _SessSetupXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 31),
    _SessSetupXCalls_Type()
)
sessSetupXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessSetupXCalls.setStatus("current")
_UlogoffXCalls_Type = Unsigned32
_UlogoffXCalls_Object = MibTableColumn
ulogoffXCalls = _UlogoffXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 32),
    _UlogoffXCalls_Type()
)
ulogoffXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulogoffXCalls.setStatus("current")
_TconXCalls_Type = Unsigned32
_TconXCalls_Object = MibTableColumn
tconXCalls = _TconXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 33),
    _TconXCalls_Type()
)
tconXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tconXCalls.setStatus("current")
_DskattrCalls_Type = Unsigned32
_DskattrCalls_Object = MibTableColumn
dskattrCalls = _DskattrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 34),
    _DskattrCalls_Type()
)
dskattrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskattrCalls.setStatus("current")
_SearchCalls_Type = Unsigned32
_SearchCalls_Object = MibTableColumn
searchCalls = _SearchCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 35),
    _SearchCalls_Type()
)
searchCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchCalls.setStatus("current")
_NtTransCalls_Type = Unsigned32
_NtTransCalls_Object = MibTableColumn
ntTransCalls = _NtTransCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 36),
    _NtTransCalls_Type()
)
ntTransCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTransCalls.setStatus("current")
_NtTranssCalls_Type = Unsigned32
_NtTranssCalls_Object = MibTableColumn
ntTranssCalls = _NtTranssCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 37),
    _NtTranssCalls_Type()
)
ntTranssCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTranssCalls.setStatus("current")
_NtCreateXCalls_Type = Unsigned32
_NtCreateXCalls_Object = MibTableColumn
ntCreateXCalls = _NtCreateXCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 38),
    _NtCreateXCalls_Type()
)
ntCreateXCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCreateXCalls.setStatus("current")
_NtCancelCalls_Type = Unsigned32
_NtCancelCalls_Object = MibTableColumn
ntCancelCalls = _NtCancelCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 3, 39, 1, 39),
    _NtCancelCalls_Type()
)
ntCancelCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCancelCalls.setStatus("current")
_CifsService_ObjectIdentity = ObjectIdentity
cifsService = _CifsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 4)
)


class _CifsServiceEnabled_Type(Integer32):
    """Custom type cifsServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_CifsServiceEnabled_Type.__name__ = "Integer32"
_CifsServiceEnabled_Object = MibScalar
cifsServiceEnabled = _CifsServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 4, 1),
    _CifsServiceEnabled_Type()
)
cifsServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsServiceEnabled.setStatus("current")
_CifsServiceMaxUsers_Type = Unsigned32
_CifsServiceMaxUsers_Object = MibScalar
cifsServiceMaxUsers = _CifsServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 2, 4, 2),
    _CifsServiceMaxUsers_Type()
)
cifsServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsServiceMaxUsers.setStatus("current")
_Nfs_ObjectIdentity = ObjectIdentity
nfs = _Nfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3)
)
_NfsExports_ObjectIdentity = ObjectIdentity
nfsExports = _NfsExports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1)
)
_NfsExportNumber_Type = Integer32
_NfsExportNumber_Object = MibScalar
nfsExportNumber = _NfsExportNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 1),
    _NfsExportNumber_Type()
)
nfsExportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportNumber.setStatus("current")
_NfsExportTable_Object = MibTable
nfsExportTable = _NfsExportTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nfsExportTable.setStatus("obsolete")
_NfsExportEntry_Object = MibTableRow
nfsExportEntry = _NfsExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1)
)
nfsExportEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsExportIndex"),
)
if mibBuilder.loadTexts:
    nfsExportEntry.setStatus("obsolete")


class _NfsExportIndex_Type(Integer32):
    """Custom type nfsExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_NfsExportIndex_Type.__name__ = "Integer32"
_NfsExportIndex_Object = MibTableColumn
nfsExportIndex = _NfsExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 1),
    _NfsExportIndex_Type()
)
nfsExportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportIndex.setStatus("obsolete")
_NfsExportName_Type = DisplayString
_NfsExportName_Object = MibTableColumn
nfsExportName = _NfsExportName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 2),
    _NfsExportName_Type()
)
nfsExportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportName.setStatus("obsolete")
_NfsExportPath_Type = DisplayString
_NfsExportPath_Object = MibTableColumn
nfsExportPath = _NfsExportPath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 3),
    _NfsExportPath_Type()
)
nfsExportPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportPath.setStatus("obsolete")
_NfsExportNumberMounts_Type = Unsigned32
_NfsExportNumberMounts_Object = MibTableColumn
nfsExportNumberMounts = _NfsExportNumberMounts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 4),
    _NfsExportNumberMounts_Type()
)
nfsExportNumberMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportNumberMounts.setStatus("obsolete")
_NfsExportWWN_Type = DisplayString
_NfsExportWWN_Object = MibTableColumn
nfsExportWWN = _NfsExportWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 5),
    _NfsExportWWN_Type()
)
nfsExportWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportWWN.setStatus("obsolete")
_NfsExportLUN_Type = Unsigned32
_NfsExportLUN_Object = MibTableColumn
nfsExportLUN = _NfsExportLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 6),
    _NfsExportLUN_Type()
)
nfsExportLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportLUN.setStatus("obsolete")
_NfsExportPartitionID_Type = Unsigned32
_NfsExportPartitionID_Object = MibTableColumn
nfsExportPartitionID = _NfsExportPartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 2, 1, 7),
    _NfsExportPartitionID_Type()
)
nfsExportPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportPartitionID.setStatus("obsolete")
_NfsExportsTable_Object = MibTable
nfsExportsTable = _NfsExportsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    nfsExportsTable.setStatus("current")
_NfsExportsEntry_Object = MibTableRow
nfsExportsEntry = _NfsExportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3, 1)
)
nfsExportsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsExportsEvs"),
    (0, "BLUEARC-SERVER-MIB", "nfsExportsName"),
)
if mibBuilder.loadTexts:
    nfsExportsEntry.setStatus("current")


class _NfsExportsEvs_Type(Unsigned32):
    """Custom type nfsExportsEvs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NfsExportsEvs_Type.__name__ = "Unsigned32"
_NfsExportsEvs_Object = MibTableColumn
nfsExportsEvs = _NfsExportsEvs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3, 1, 1),
    _NfsExportsEvs_Type()
)
nfsExportsEvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportsEvs.setStatus("current")
_NfsExportsName_Type = DisplayString
_NfsExportsName_Object = MibTableColumn
nfsExportsName = _NfsExportsName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3, 1, 2),
    _NfsExportsName_Type()
)
nfsExportsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportsName.setStatus("current")
_NfsExportsPath_Type = DisplayString
_NfsExportsPath_Object = MibTableColumn
nfsExportsPath = _NfsExportsPath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3, 1, 3),
    _NfsExportsPath_Type()
)
nfsExportsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportsPath.setStatus("current")


class _NfsExportsDeviceId_Type(Unsigned32):
    """Custom type nfsExportsDeviceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NfsExportsDeviceId_Type.__name__ = "Unsigned32"
_NfsExportsDeviceId_Object = MibTableColumn
nfsExportsDeviceId = _NfsExportsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 1, 3, 1, 4),
    _NfsExportsDeviceId_Type()
)
nfsExportsDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsExportsDeviceId.setStatus("current")
_NfsUsers_ObjectIdentity = ObjectIdentity
nfsUsers = _NfsUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2)
)
_NfsUserNumber_Type = Integer32
_NfsUserNumber_Object = MibScalar
nfsUserNumber = _NfsUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2, 1),
    _NfsUserNumber_Type()
)
nfsUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserNumber.setStatus("obsolete")
_NfsUserTable_Object = MibTable
nfsUserTable = _NfsUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nfsUserTable.setStatus("obsolete")
_NfsUserEntry_Object = MibTableRow
nfsUserEntry = _NfsUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2, 2, 1)
)
nfsUserEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsUserName"),
)
if mibBuilder.loadTexts:
    nfsUserEntry.setStatus("obsolete")
_NfsUserName_Type = DisplayString
_NfsUserName_Object = MibTableColumn
nfsUserName = _NfsUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2, 2, 1, 1),
    _NfsUserName_Type()
)
nfsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserName.setStatus("obsolete")
_NfsUserID_Type = Unsigned32
_NfsUserID_Object = MibTableColumn
nfsUserID = _NfsUserID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 2, 2, 1, 2),
    _NfsUserID_Type()
)
nfsUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserID.setStatus("obsolete")
_NfsUserMapping_ObjectIdentity = ObjectIdentity
nfsUserMapping = _NfsUserMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3)
)
_NfsUserMappingNumber_Type = Integer32
_NfsUserMappingNumber_Object = MibScalar
nfsUserMappingNumber = _NfsUserMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 1),
    _NfsUserMappingNumber_Type()
)
nfsUserMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingNumber.setStatus("obsolete")
_NfsUserMappingTable_Object = MibTable
nfsUserMappingTable = _NfsUserMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    nfsUserMappingTable.setStatus("obsolete")
_NfsUserMappingEntry_Object = MibTableRow
nfsUserMappingEntry = _NfsUserMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1)
)
nfsUserMappingEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsUserMappingUnixUserName"),
)
if mibBuilder.loadTexts:
    nfsUserMappingEntry.setStatus("obsolete")
_NfsUserMappingUnixUserName_Type = DisplayString
_NfsUserMappingUnixUserName_Object = MibTableColumn
nfsUserMappingUnixUserName = _NfsUserMappingUnixUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1, 1),
    _NfsUserMappingUnixUserName_Type()
)
nfsUserMappingUnixUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingUnixUserName.setStatus("obsolete")


class _NfsUserMappingUnixUserIDValid_Type(Integer32):
    """Custom type nfsUserMappingUnixUserIDValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("unknown", 3),
          ("valid", 1))
    )


_NfsUserMappingUnixUserIDValid_Type.__name__ = "Integer32"
_NfsUserMappingUnixUserIDValid_Object = MibTableColumn
nfsUserMappingUnixUserIDValid = _NfsUserMappingUnixUserIDValid_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1, 2),
    _NfsUserMappingUnixUserIDValid_Type()
)
nfsUserMappingUnixUserIDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingUnixUserIDValid.setStatus("obsolete")
_NfsUserMappingUnixUserID_Type = Unsigned32
_NfsUserMappingUnixUserID_Object = MibTableColumn
nfsUserMappingUnixUserID = _NfsUserMappingUnixUserID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1, 3),
    _NfsUserMappingUnixUserID_Type()
)
nfsUserMappingUnixUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingUnixUserID.setStatus("obsolete")
_NfsUserMappingNtUserName_Type = DisplayString
_NfsUserMappingNtUserName_Object = MibTableColumn
nfsUserMappingNtUserName = _NfsUserMappingNtUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1, 4),
    _NfsUserMappingNtUserName_Type()
)
nfsUserMappingNtUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingNtUserName.setStatus("obsolete")
_NfsUserMappingNtUserDomainName_Type = DisplayString
_NfsUserMappingNtUserDomainName_Object = MibTableColumn
nfsUserMappingNtUserDomainName = _NfsUserMappingNtUserDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 3, 2, 1, 5),
    _NfsUserMappingNtUserDomainName_Type()
)
nfsUserMappingNtUserDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsUserMappingNtUserDomainName.setStatus("obsolete")
_NfsGroups_ObjectIdentity = ObjectIdentity
nfsGroups = _NfsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4)
)
_NfsGroupNumber_Type = Integer32
_NfsGroupNumber_Object = MibScalar
nfsGroupNumber = _NfsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4, 1),
    _NfsGroupNumber_Type()
)
nfsGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupNumber.setStatus("obsolete")
_NfsGroupTable_Object = MibTable
nfsGroupTable = _NfsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    nfsGroupTable.setStatus("obsolete")
_NfsGroupEntry_Object = MibTableRow
nfsGroupEntry = _NfsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4, 2, 1)
)
nfsGroupEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsGroupName"),
)
if mibBuilder.loadTexts:
    nfsGroupEntry.setStatus("obsolete")
_NfsGroupName_Type = DisplayString
_NfsGroupName_Object = MibTableColumn
nfsGroupName = _NfsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4, 2, 1, 1),
    _NfsGroupName_Type()
)
nfsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupName.setStatus("obsolete")
_NfsGroupID_Type = Unsigned32
_NfsGroupID_Object = MibTableColumn
nfsGroupID = _NfsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 4, 2, 1, 2),
    _NfsGroupID_Type()
)
nfsGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupID.setStatus("obsolete")
_NfsGroupMapping_ObjectIdentity = ObjectIdentity
nfsGroupMapping = _NfsGroupMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5)
)
_NfsGroupMappingNumber_Type = Integer32
_NfsGroupMappingNumber_Object = MibScalar
nfsGroupMappingNumber = _NfsGroupMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 1),
    _NfsGroupMappingNumber_Type()
)
nfsGroupMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingNumber.setStatus("obsolete")
_NfsGroupMappingTable_Object = MibTable
nfsGroupMappingTable = _NfsGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    nfsGroupMappingTable.setStatus("obsolete")
_NfsGroupMappingEntry_Object = MibTableRow
nfsGroupMappingEntry = _NfsGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1)
)
nfsGroupMappingEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsGroupMappingUnixGroupName"),
)
if mibBuilder.loadTexts:
    nfsGroupMappingEntry.setStatus("obsolete")
_NfsGroupMappingUnixGroupName_Type = DisplayString
_NfsGroupMappingUnixGroupName_Object = MibTableColumn
nfsGroupMappingUnixGroupName = _NfsGroupMappingUnixGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1, 1),
    _NfsGroupMappingUnixGroupName_Type()
)
nfsGroupMappingUnixGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingUnixGroupName.setStatus("obsolete")


class _NfsGroupMappingUnixGroupIDValid_Type(Integer32):
    """Custom type nfsGroupMappingUnixGroupIDValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("unknown", 3),
          ("valid", 1))
    )


_NfsGroupMappingUnixGroupIDValid_Type.__name__ = "Integer32"
_NfsGroupMappingUnixGroupIDValid_Object = MibTableColumn
nfsGroupMappingUnixGroupIDValid = _NfsGroupMappingUnixGroupIDValid_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1, 2),
    _NfsGroupMappingUnixGroupIDValid_Type()
)
nfsGroupMappingUnixGroupIDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingUnixGroupIDValid.setStatus("obsolete")
_NfsGroupMappingUnixGroupID_Type = Unsigned32
_NfsGroupMappingUnixGroupID_Object = MibTableColumn
nfsGroupMappingUnixGroupID = _NfsGroupMappingUnixGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1, 3),
    _NfsGroupMappingUnixGroupID_Type()
)
nfsGroupMappingUnixGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingUnixGroupID.setStatus("obsolete")
_NfsGroupMappingNtGroupName_Type = DisplayString
_NfsGroupMappingNtGroupName_Object = MibTableColumn
nfsGroupMappingNtGroupName = _NfsGroupMappingNtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1, 4),
    _NfsGroupMappingNtGroupName_Type()
)
nfsGroupMappingNtGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingNtGroupName.setStatus("obsolete")
_NfsGroupMappingNtGroupDomainName_Type = DisplayString
_NfsGroupMappingNtGroupDomainName_Object = MibTableColumn
nfsGroupMappingNtGroupDomainName = _NfsGroupMappingNtGroupDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 5, 2, 1, 5),
    _NfsGroupMappingNtGroupDomainName_Type()
)
nfsGroupMappingNtGroupDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsGroupMappingNtGroupDomainName.setStatus("obsolete")
_NfsStats_ObjectIdentity = ObjectIdentity
nfsStats = _NfsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6)
)
_NfsVersion2_ObjectIdentity = ObjectIdentity
nfsVersion2 = _NfsVersion2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1)
)
_Null2Calls_Type = Counter32
_Null2Calls_Object = MibScalar
null2Calls = _Null2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 1),
    _Null2Calls_Type()
)
null2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    null2Calls.setStatus("obsolete")
_GetAttr2Calls_Type = Counter32
_GetAttr2Calls_Object = MibScalar
getAttr2Calls = _GetAttr2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 2),
    _GetAttr2Calls_Type()
)
getAttr2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getAttr2Calls.setStatus("obsolete")
_SetAttr2Calls_Type = Counter32
_SetAttr2Calls_Object = MibScalar
setAttr2Calls = _SetAttr2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 3),
    _SetAttr2Calls_Type()
)
setAttr2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAttr2Calls.setStatus("obsolete")
_RootCalls_Type = Counter32
_RootCalls_Object = MibScalar
rootCalls = _RootCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 4),
    _RootCalls_Type()
)
rootCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootCalls.setStatus("obsolete")
_Lookup2Calls_Type = Counter32
_Lookup2Calls_Object = MibScalar
lookup2Calls = _Lookup2Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 5),
    _Lookup2Calls_Type()
)
lookup2Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookup2Calls.setStatus("obsolete")
_ReadLink2_Type = Counter32
_ReadLink2_Object = MibScalar
readLink2 = _ReadLink2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 6),
    _ReadLink2_Type()
)
readLink2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readLink2.setStatus("obsolete")
_Read2_Type = Counter32
_Read2_Object = MibScalar
read2 = _Read2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 7),
    _Read2_Type()
)
read2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    read2.setStatus("obsolete")
_WriteCache_Type = Counter32
_WriteCache_Object = MibScalar
writeCache = _WriteCache_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 8),
    _WriteCache_Type()
)
writeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeCache.setStatus("obsolete")
_Write2_Type = Counter32
_Write2_Object = MibScalar
write2 = _Write2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 9),
    _Write2_Type()
)
write2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    write2.setStatus("obsolete")
_Create2_Type = Counter32
_Create2_Object = MibScalar
create2 = _Create2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 10),
    _Create2_Type()
)
create2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    create2.setStatus("obsolete")
_Remove2_Type = Counter32
_Remove2_Object = MibScalar
remove2 = _Remove2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 11),
    _Remove2_Type()
)
remove2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remove2.setStatus("obsolete")
_Rename2_Type = Counter32
_Rename2_Object = MibScalar
rename2 = _Rename2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 12),
    _Rename2_Type()
)
rename2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rename2.setStatus("obsolete")
_Link2_Type = Counter32
_Link2_Object = MibScalar
link2 = _Link2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 13),
    _Link2_Type()
)
link2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    link2.setStatus("obsolete")
_SymLink2_Type = Counter32
_SymLink2_Object = MibScalar
symLink2 = _SymLink2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 14),
    _SymLink2_Type()
)
symLink2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symLink2.setStatus("obsolete")
_MkDir2_Type = Counter32
_MkDir2_Object = MibScalar
mkDir2 = _MkDir2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 15),
    _MkDir2_Type()
)
mkDir2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mkDir2.setStatus("obsolete")
_RmDir2_Type = Counter32
_RmDir2_Object = MibScalar
rmDir2 = _RmDir2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 16),
    _RmDir2_Type()
)
rmDir2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDir2.setStatus("obsolete")
_ReadDir2_Type = Counter32
_ReadDir2_Object = MibScalar
readDir2 = _ReadDir2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 17),
    _ReadDir2_Type()
)
readDir2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readDir2.setStatus("obsolete")
_StatFS2_Type = Counter32
_StatFS2_Object = MibScalar
statFS2 = _StatFS2_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 18),
    _StatFS2_Type()
)
statFS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFS2.setStatus("obsolete")
_NfsV2StatsTable_Object = MibTable
nfsV2StatsTable = _NfsV2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19)
)
if mibBuilder.loadTexts:
    nfsV2StatsTable.setStatus("current")
_NfsV2StatsEntry_Object = MibTableRow
nfsV2StatsEntry = _NfsV2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1)
)
nfsV2StatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsV2StatsClusterNode"),
)
if mibBuilder.loadTexts:
    nfsV2StatsEntry.setStatus("current")
_NfsV2StatsClusterNode_Type = Unsigned32
_NfsV2StatsClusterNode_Object = MibTableColumn
nfsV2StatsClusterNode = _NfsV2StatsClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 1),
    _NfsV2StatsClusterNode_Type()
)
nfsV2StatsClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2StatsClusterNode.setStatus("current")
_NfsV2nullCalls_Type = Counter32
_NfsV2nullCalls_Object = MibTableColumn
nfsV2nullCalls = _NfsV2nullCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 2),
    _NfsV2nullCalls_Type()
)
nfsV2nullCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2nullCalls.setStatus("current")
_NfsV2getAttrCalls_Type = Counter32
_NfsV2getAttrCalls_Object = MibTableColumn
nfsV2getAttrCalls = _NfsV2getAttrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 3),
    _NfsV2getAttrCalls_Type()
)
nfsV2getAttrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2getAttrCalls.setStatus("current")
_NfsV2setAttrCalls_Type = Counter32
_NfsV2setAttrCalls_Object = MibTableColumn
nfsV2setAttrCalls = _NfsV2setAttrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 4),
    _NfsV2setAttrCalls_Type()
)
nfsV2setAttrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2setAttrCalls.setStatus("current")
_NfsV2rootCalls_Type = Counter32
_NfsV2rootCalls_Object = MibTableColumn
nfsV2rootCalls = _NfsV2rootCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 5),
    _NfsV2rootCalls_Type()
)
nfsV2rootCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2rootCalls.setStatus("current")
_NfsV2lookupCalls_Type = Counter32
_NfsV2lookupCalls_Object = MibTableColumn
nfsV2lookupCalls = _NfsV2lookupCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 6),
    _NfsV2lookupCalls_Type()
)
nfsV2lookupCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2lookupCalls.setStatus("current")
_NfsV2readLink_Type = Counter32
_NfsV2readLink_Object = MibTableColumn
nfsV2readLink = _NfsV2readLink_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 7),
    _NfsV2readLink_Type()
)
nfsV2readLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2readLink.setStatus("current")
_NfsV2read_Type = Counter32
_NfsV2read_Object = MibTableColumn
nfsV2read = _NfsV2read_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 8),
    _NfsV2read_Type()
)
nfsV2read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2read.setStatus("current")
_NfsV2writeCache_Type = Counter32
_NfsV2writeCache_Object = MibTableColumn
nfsV2writeCache = _NfsV2writeCache_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 9),
    _NfsV2writeCache_Type()
)
nfsV2writeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2writeCache.setStatus("current")
_NfsV2write_Type = Counter32
_NfsV2write_Object = MibTableColumn
nfsV2write = _NfsV2write_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 10),
    _NfsV2write_Type()
)
nfsV2write.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2write.setStatus("current")
_NfsV2create_Type = Counter32
_NfsV2create_Object = MibTableColumn
nfsV2create = _NfsV2create_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 11),
    _NfsV2create_Type()
)
nfsV2create.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2create.setStatus("current")
_NfsV2remove_Type = Counter32
_NfsV2remove_Object = MibTableColumn
nfsV2remove = _NfsV2remove_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 12),
    _NfsV2remove_Type()
)
nfsV2remove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2remove.setStatus("current")
_NfsV2rename_Type = Counter32
_NfsV2rename_Object = MibTableColumn
nfsV2rename = _NfsV2rename_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 13),
    _NfsV2rename_Type()
)
nfsV2rename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2rename.setStatus("current")
_NfsV2link_Type = Counter32
_NfsV2link_Object = MibTableColumn
nfsV2link = _NfsV2link_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 14),
    _NfsV2link_Type()
)
nfsV2link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2link.setStatus("current")
_NfsV2symLink_Type = Counter32
_NfsV2symLink_Object = MibTableColumn
nfsV2symLink = _NfsV2symLink_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 15),
    _NfsV2symLink_Type()
)
nfsV2symLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2symLink.setStatus("current")
_NfsV2mkDir_Type = Counter32
_NfsV2mkDir_Object = MibTableColumn
nfsV2mkDir = _NfsV2mkDir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 16),
    _NfsV2mkDir_Type()
)
nfsV2mkDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2mkDir.setStatus("current")
_NfsV2rmDir_Type = Counter32
_NfsV2rmDir_Object = MibTableColumn
nfsV2rmDir = _NfsV2rmDir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 17),
    _NfsV2rmDir_Type()
)
nfsV2rmDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2rmDir.setStatus("current")
_NfsV2readDir_Type = Counter32
_NfsV2readDir_Object = MibTableColumn
nfsV2readDir = _NfsV2readDir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 18),
    _NfsV2readDir_Type()
)
nfsV2readDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2readDir.setStatus("current")
_NfsV2statFS_Type = Counter32
_NfsV2statFS_Object = MibTableColumn
nfsV2statFS = _NfsV2statFS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 1, 19, 1, 19),
    _NfsV2statFS_Type()
)
nfsV2statFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2statFS.setStatus("current")
_NfsVersion3_ObjectIdentity = ObjectIdentity
nfsVersion3 = _NfsVersion3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2)
)
_Null3Calls_Type = Counter32
_Null3Calls_Object = MibScalar
null3Calls = _Null3Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 1),
    _Null3Calls_Type()
)
null3Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    null3Calls.setStatus("obsolete")
_GetAttr3Calls_Type = Counter32
_GetAttr3Calls_Object = MibScalar
getAttr3Calls = _GetAttr3Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 2),
    _GetAttr3Calls_Type()
)
getAttr3Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getAttr3Calls.setStatus("obsolete")
_SetAttr3Calls_Type = Counter32
_SetAttr3Calls_Object = MibScalar
setAttr3Calls = _SetAttr3Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 3),
    _SetAttr3Calls_Type()
)
setAttr3Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAttr3Calls.setStatus("obsolete")
_Lookup3Calls_Type = Counter32
_Lookup3Calls_Object = MibScalar
lookup3Calls = _Lookup3Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 4),
    _Lookup3Calls_Type()
)
lookup3Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookup3Calls.setStatus("obsolete")
_Access3Calls_Type = Counter32
_Access3Calls_Object = MibScalar
access3Calls = _Access3Calls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 5),
    _Access3Calls_Type()
)
access3Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    access3Calls.setStatus("obsolete")
_ReadLink3_Type = Counter32
_ReadLink3_Object = MibScalar
readLink3 = _ReadLink3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 6),
    _ReadLink3_Type()
)
readLink3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readLink3.setStatus("obsolete")
_Read3_Type = Counter32
_Read3_Object = MibScalar
read3 = _Read3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 7),
    _Read3_Type()
)
read3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    read3.setStatus("obsolete")
_Write3_Type = Counter32
_Write3_Object = MibScalar
write3 = _Write3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 8),
    _Write3_Type()
)
write3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    write3.setStatus("obsolete")
_Create3_Type = Counter32
_Create3_Object = MibScalar
create3 = _Create3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 9),
    _Create3_Type()
)
create3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    create3.setStatus("obsolete")
_Mkdir3_Type = Counter32
_Mkdir3_Object = MibScalar
mkdir3 = _Mkdir3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 10),
    _Mkdir3_Type()
)
mkdir3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mkdir3.setStatus("obsolete")
_SymLink3_Type = Counter32
_SymLink3_Object = MibScalar
symLink3 = _SymLink3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 11),
    _SymLink3_Type()
)
symLink3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symLink3.setStatus("obsolete")
_MkNod3_Type = Counter32
_MkNod3_Object = MibScalar
mkNod3 = _MkNod3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 12),
    _MkNod3_Type()
)
mkNod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mkNod3.setStatus("obsolete")
_Remove3_Type = Counter32
_Remove3_Object = MibScalar
remove3 = _Remove3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 13),
    _Remove3_Type()
)
remove3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remove3.setStatus("obsolete")
_RmDir3_Type = Counter32
_RmDir3_Object = MibScalar
rmDir3 = _RmDir3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 14),
    _RmDir3_Type()
)
rmDir3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDir3.setStatus("obsolete")
_Rename3_Type = Counter32
_Rename3_Object = MibScalar
rename3 = _Rename3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 15),
    _Rename3_Type()
)
rename3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rename3.setStatus("obsolete")
_Link3_Type = Counter32
_Link3_Object = MibScalar
link3 = _Link3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 16),
    _Link3_Type()
)
link3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    link3.setStatus("obsolete")
_ReadDir3_Type = Counter32
_ReadDir3_Object = MibScalar
readDir3 = _ReadDir3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 17),
    _ReadDir3_Type()
)
readDir3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readDir3.setStatus("obsolete")
_ReadDirPlus3_Type = Counter32
_ReadDirPlus3_Object = MibScalar
readDirPlus3 = _ReadDirPlus3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 18),
    _ReadDirPlus3_Type()
)
readDirPlus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readDirPlus3.setStatus("obsolete")
_FsStat3_Type = Counter32
_FsStat3_Object = MibScalar
fsStat3 = _FsStat3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 19),
    _FsStat3_Type()
)
fsStat3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStat3.setStatus("obsolete")
_FsInfo3_Type = Counter32
_FsInfo3_Object = MibScalar
fsInfo3 = _FsInfo3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 20),
    _FsInfo3_Type()
)
fsInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInfo3.setStatus("obsolete")
_PathConf3_Type = Counter32
_PathConf3_Object = MibScalar
pathConf3 = _PathConf3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 21),
    _PathConf3_Type()
)
pathConf3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathConf3.setStatus("obsolete")
_Commit3_Type = Counter32
_Commit3_Object = MibScalar
commit3 = _Commit3_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 22),
    _Commit3_Type()
)
commit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commit3.setStatus("obsolete")
_NfsV3StatsTable_Object = MibTable
nfsV3StatsTable = _NfsV3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23)
)
if mibBuilder.loadTexts:
    nfsV3StatsTable.setStatus("current")
_NfsV3StatsEntry_Object = MibTableRow
nfsV3StatsEntry = _NfsV3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1)
)
nfsV3StatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "nfsV3StatsClusterNode"),
)
if mibBuilder.loadTexts:
    nfsV3StatsEntry.setStatus("current")
_NfsV3StatsClusterNode_Type = Unsigned32
_NfsV3StatsClusterNode_Object = MibTableColumn
nfsV3StatsClusterNode = _NfsV3StatsClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 1),
    _NfsV3StatsClusterNode_Type()
)
nfsV3StatsClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3StatsClusterNode.setStatus("current")
_NfsV3nullCalls_Type = Counter32
_NfsV3nullCalls_Object = MibTableColumn
nfsV3nullCalls = _NfsV3nullCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 2),
    _NfsV3nullCalls_Type()
)
nfsV3nullCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3nullCalls.setStatus("current")
_NfsV3getAttrCalls_Type = Counter32
_NfsV3getAttrCalls_Object = MibTableColumn
nfsV3getAttrCalls = _NfsV3getAttrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 3),
    _NfsV3getAttrCalls_Type()
)
nfsV3getAttrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3getAttrCalls.setStatus("current")
_NfsV3setAttrCalls_Type = Counter32
_NfsV3setAttrCalls_Object = MibTableColumn
nfsV3setAttrCalls = _NfsV3setAttrCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 4),
    _NfsV3setAttrCalls_Type()
)
nfsV3setAttrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3setAttrCalls.setStatus("current")
_NfsV3lookupCalls_Type = Counter32
_NfsV3lookupCalls_Object = MibTableColumn
nfsV3lookupCalls = _NfsV3lookupCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 5),
    _NfsV3lookupCalls_Type()
)
nfsV3lookupCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3lookupCalls.setStatus("current")
_NfsV3accessCalls_Type = Counter32
_NfsV3accessCalls_Object = MibTableColumn
nfsV3accessCalls = _NfsV3accessCalls_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 6),
    _NfsV3accessCalls_Type()
)
nfsV3accessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3accessCalls.setStatus("current")
_NfsV3readLink_Type = Counter32
_NfsV3readLink_Object = MibTableColumn
nfsV3readLink = _NfsV3readLink_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 7),
    _NfsV3readLink_Type()
)
nfsV3readLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3readLink.setStatus("current")
_NfsV3read_Type = Counter32
_NfsV3read_Object = MibTableColumn
nfsV3read = _NfsV3read_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 8),
    _NfsV3read_Type()
)
nfsV3read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3read.setStatus("current")
_NfsV3write_Type = Counter32
_NfsV3write_Object = MibTableColumn
nfsV3write = _NfsV3write_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 9),
    _NfsV3write_Type()
)
nfsV3write.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3write.setStatus("current")
_NfsV3create_Type = Counter32
_NfsV3create_Object = MibTableColumn
nfsV3create = _NfsV3create_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 10),
    _NfsV3create_Type()
)
nfsV3create.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3create.setStatus("current")
_NfsV3mkdir_Type = Counter32
_NfsV3mkdir_Object = MibTableColumn
nfsV3mkdir = _NfsV3mkdir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 11),
    _NfsV3mkdir_Type()
)
nfsV3mkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3mkdir.setStatus("current")
_NfsV3symLink_Type = Counter32
_NfsV3symLink_Object = MibTableColumn
nfsV3symLink = _NfsV3symLink_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 12),
    _NfsV3symLink_Type()
)
nfsV3symLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3symLink.setStatus("current")
_NfsV3mkNod_Type = Counter32
_NfsV3mkNod_Object = MibTableColumn
nfsV3mkNod = _NfsV3mkNod_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 13),
    _NfsV3mkNod_Type()
)
nfsV3mkNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3mkNod.setStatus("current")
_NfsV3remove_Type = Counter32
_NfsV3remove_Object = MibTableColumn
nfsV3remove = _NfsV3remove_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 14),
    _NfsV3remove_Type()
)
nfsV3remove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3remove.setStatus("current")
_NfsV3rmDir_Type = Counter32
_NfsV3rmDir_Object = MibTableColumn
nfsV3rmDir = _NfsV3rmDir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 15),
    _NfsV3rmDir_Type()
)
nfsV3rmDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3rmDir.setStatus("current")
_NfsV3rename_Type = Counter32
_NfsV3rename_Object = MibTableColumn
nfsV3rename = _NfsV3rename_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 16),
    _NfsV3rename_Type()
)
nfsV3rename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3rename.setStatus("current")
_NfsV3link_Type = Counter32
_NfsV3link_Object = MibTableColumn
nfsV3link = _NfsV3link_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 17),
    _NfsV3link_Type()
)
nfsV3link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3link.setStatus("current")
_NfsV3readDir_Type = Counter32
_NfsV3readDir_Object = MibTableColumn
nfsV3readDir = _NfsV3readDir_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 18),
    _NfsV3readDir_Type()
)
nfsV3readDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3readDir.setStatus("current")
_NfsV3readDirPlus_Type = Counter32
_NfsV3readDirPlus_Object = MibTableColumn
nfsV3readDirPlus = _NfsV3readDirPlus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 19),
    _NfsV3readDirPlus_Type()
)
nfsV3readDirPlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3readDirPlus.setStatus("current")
_NfsV3fsStat_Type = Counter32
_NfsV3fsStat_Object = MibTableColumn
nfsV3fsStat = _NfsV3fsStat_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 20),
    _NfsV3fsStat_Type()
)
nfsV3fsStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3fsStat.setStatus("current")
_NfsV3fsInfo_Type = Counter32
_NfsV3fsInfo_Object = MibTableColumn
nfsV3fsInfo = _NfsV3fsInfo_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 21),
    _NfsV3fsInfo_Type()
)
nfsV3fsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3fsInfo.setStatus("current")
_NfsV3pathConf_Type = Counter32
_NfsV3pathConf_Object = MibTableColumn
nfsV3pathConf = _NfsV3pathConf_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 22),
    _NfsV3pathConf_Type()
)
nfsV3pathConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3pathConf.setStatus("current")
_NfsV3commit_Type = Counter32
_NfsV3commit_Object = MibTableColumn
nfsV3commit = _NfsV3commit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 2, 23, 1, 23),
    _NfsV3commit_Type()
)
nfsV3commit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV3commit.setStatus("current")
_NfsMounts_Type = Counter32
_NfsMounts_Object = MibScalar
nfsMounts = _NfsMounts_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 3),
    _NfsMounts_Type()
)
nfsMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsMounts.setStatus("obsolete")
_NfsClients_Type = Counter32
_NfsClients_Object = MibScalar
nfsClients = _NfsClients_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 6, 4),
    _NfsClients_Type()
)
nfsClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClients.setStatus("obsolete")
_NfsService_ObjectIdentity = ObjectIdentity
nfsService = _NfsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 7)
)


class _NfsServiceEnabled_Type(Integer32):
    """Custom type nfsServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NfsServiceEnabled_Type.__name__ = "Integer32"
_NfsServiceEnabled_Object = MibScalar
nfsServiceEnabled = _NfsServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 7, 1),
    _NfsServiceEnabled_Type()
)
nfsServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServiceEnabled.setStatus("current")
_NfsServiceMaxUsers_Type = Unsigned32
_NfsServiceMaxUsers_Object = MibScalar
nfsServiceMaxUsers = _NfsServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 3, 7, 2),
    _NfsServiceMaxUsers_Type()
)
nfsServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServiceMaxUsers.setStatus("current")
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4)
)
_FtpTimeout_Type = Integer32
_FtpTimeout_Object = MibScalar
ftpTimeout = _FtpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 1),
    _FtpTimeout_Type()
)
ftpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTimeout.setStatus("obsolete")
_FtpMountPoints_ObjectIdentity = ObjectIdentity
ftpMountPoints = _FtpMountPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2)
)
_FtpMountNumber_Type = Integer32
_FtpMountNumber_Object = MibScalar
ftpMountNumber = _FtpMountNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 1),
    _FtpMountNumber_Type()
)
ftpMountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountNumber.setStatus("obsolete")
_FtpMountTable_Object = MibTable
ftpMountTable = _FtpMountTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ftpMountTable.setStatus("obsolete")
_FtpMountEntry_Object = MibTableRow
ftpMountEntry = _FtpMountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1)
)
ftpMountEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "ftpMountName"),
)
if mibBuilder.loadTexts:
    ftpMountEntry.setStatus("obsolete")
_FtpMountName_Type = DisplayString
_FtpMountName_Object = MibTableColumn
ftpMountName = _FtpMountName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1, 1),
    _FtpMountName_Type()
)
ftpMountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountName.setStatus("obsolete")
_FtpMountNumberUsers_Type = Unsigned32
_FtpMountNumberUsers_Object = MibTableColumn
ftpMountNumberUsers = _FtpMountNumberUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1, 2),
    _FtpMountNumberUsers_Type()
)
ftpMountNumberUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountNumberUsers.setStatus("obsolete")
_FtpMountWWN_Type = DisplayString
_FtpMountWWN_Object = MibTableColumn
ftpMountWWN = _FtpMountWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1, 3),
    _FtpMountWWN_Type()
)
ftpMountWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountWWN.setStatus("obsolete")
_FtpMountLUN_Type = Unsigned32
_FtpMountLUN_Object = MibTableColumn
ftpMountLUN = _FtpMountLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1, 4),
    _FtpMountLUN_Type()
)
ftpMountLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountLUN.setStatus("obsolete")
_FtpMountPartitionID_Type = Unsigned32
_FtpMountPartitionID_Object = MibTableColumn
ftpMountPartitionID = _FtpMountPartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 2, 2, 1, 5),
    _FtpMountPartitionID_Type()
)
ftpMountPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountPartitionID.setStatus("obsolete")
_FtpUsers_ObjectIdentity = ObjectIdentity
ftpUsers = _FtpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3)
)
_FtpUserNumber_Type = Integer32
_FtpUserNumber_Object = MibScalar
ftpUserNumber = _FtpUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 1),
    _FtpUserNumber_Type()
)
ftpUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUserNumber.setStatus("obsolete")
_FtpUserTable_Object = MibTable
ftpUserTable = _FtpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ftpUserTable.setStatus("obsolete")
_FtpUserEntry_Object = MibTableRow
ftpUserEntry = _FtpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2, 1)
)
ftpUserEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "ftpUserName"),
)
if mibBuilder.loadTexts:
    ftpUserEntry.setStatus("obsolete")
_FtpUserName_Type = DisplayString
_FtpUserName_Object = MibTableColumn
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2, 1, 1),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("obsolete")


class _FtpUserMountPointExists_Type(Integer32):
    """Custom type ftpUserMountPointExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doesnotExist", 2),
          ("exists", 1))
    )


_FtpUserMountPointExists_Type.__name__ = "Integer32"
_FtpUserMountPointExists_Object = MibTableColumn
ftpUserMountPointExists = _FtpUserMountPointExists_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2, 1, 2),
    _FtpUserMountPointExists_Type()
)
ftpUserMountPointExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUserMountPointExists.setStatus("obsolete")
_FtpUserMountPoint_Type = DisplayString
_FtpUserMountPoint_Object = MibTableColumn
ftpUserMountPoint = _FtpUserMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2, 1, 3),
    _FtpUserMountPoint_Type()
)
ftpUserMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUserMountPoint.setStatus("obsolete")
_FtpUserMountInitDirectory_Type = DisplayString
_FtpUserMountInitDirectory_Object = MibTableColumn
ftpUserMountInitDirectory = _FtpUserMountInitDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 3, 2, 1, 4),
    _FtpUserMountInitDirectory_Type()
)
ftpUserMountInitDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUserMountInitDirectory.setStatus("obsolete")
_FtpLogging_ObjectIdentity = ObjectIdentity
ftpLogging = _FtpLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4)
)


class _FtpAuditLogging_Type(Integer32):
    """Custom type ftpAuditLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FtpAuditLogging_Type.__name__ = "Integer32"
_FtpAuditLogging_Object = MibScalar
ftpAuditLogging = _FtpAuditLogging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 1),
    _FtpAuditLogging_Type()
)
ftpAuditLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogging.setStatus("obsolete")
_FtpAuditLogVolumeWWN_Type = DisplayString
_FtpAuditLogVolumeWWN_Object = MibScalar
ftpAuditLogVolumeWWN = _FtpAuditLogVolumeWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 2),
    _FtpAuditLogVolumeWWN_Type()
)
ftpAuditLogVolumeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogVolumeWWN.setStatus("obsolete")
_FtpAuditLogVolumeLUN_Type = Unsigned32
_FtpAuditLogVolumeLUN_Object = MibScalar
ftpAuditLogVolumeLUN = _FtpAuditLogVolumeLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 3),
    _FtpAuditLogVolumeLUN_Type()
)
ftpAuditLogVolumeLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogVolumeLUN.setStatus("obsolete")
_FtpAuditLogVolumePartitionID_Type = Unsigned32
_FtpAuditLogVolumePartitionID_Object = MibScalar
ftpAuditLogVolumePartitionID = _FtpAuditLogVolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 4),
    _FtpAuditLogVolumePartitionID_Type()
)
ftpAuditLogVolumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogVolumePartitionID.setStatus("obsolete")
_FtpAuditLogDirectory_Type = DisplayString
_FtpAuditLogDirectory_Object = MibScalar
ftpAuditLogDirectory = _FtpAuditLogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 5),
    _FtpAuditLogDirectory_Type()
)
ftpAuditLogDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogDirectory.setStatus("obsolete")
_FtpAuditLogRecordsPerFile_Type = Unsigned32
_FtpAuditLogRecordsPerFile_Object = MibScalar
ftpAuditLogRecordsPerFile = _FtpAuditLogRecordsPerFile_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 6),
    _FtpAuditLogRecordsPerFile_Type()
)
ftpAuditLogRecordsPerFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLogRecordsPerFile.setStatus("obsolete")
_FtpAuditMaximumLogFiles_Type = Unsigned32
_FtpAuditMaximumLogFiles_Object = MibScalar
ftpAuditMaximumLogFiles = _FtpAuditMaximumLogFiles_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 4, 7),
    _FtpAuditMaximumLogFiles_Type()
)
ftpAuditMaximumLogFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditMaximumLogFiles.setStatus("obsolete")
_FtpStats_ObjectIdentity = ObjectIdentity
ftpStats = _FtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5)
)
_FtpTotalSess_Type = Counter32
_FtpTotalSess_Object = MibScalar
ftpTotalSess = _FtpTotalSess_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 1),
    _FtpTotalSess_Type()
)
ftpTotalSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalSess.setStatus("obsolete")
_FtpTotalFtpXferIn_Type = Counter32
_FtpTotalFtpXferIn_Object = MibScalar
ftpTotalFtpXferIn = _FtpTotalFtpXferIn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 2),
    _FtpTotalFtpXferIn_Type()
)
ftpTotalFtpXferIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalFtpXferIn.setStatus("obsolete")
_FtpBytesTotalXferIn_Type = Counter64
_FtpBytesTotalXferIn_Object = MibScalar
ftpBytesTotalXferIn = _FtpBytesTotalXferIn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 3),
    _FtpBytesTotalXferIn_Type()
)
ftpBytesTotalXferIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpBytesTotalXferIn.setStatus("obsolete")
_FtpTotalFtpXferOut_Type = Counter32
_FtpTotalFtpXferOut_Object = MibScalar
ftpTotalFtpXferOut = _FtpTotalFtpXferOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 4),
    _FtpTotalFtpXferOut_Type()
)
ftpTotalFtpXferOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalFtpXferOut.setStatus("obsolete")
_FtpBytesTotalXferOut_Type = Counter64
_FtpBytesTotalXferOut_Object = MibScalar
ftpBytesTotalXferOut = _FtpBytesTotalXferOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 5),
    _FtpBytesTotalXferOut_Type()
)
ftpBytesTotalXferOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpBytesTotalXferOut.setStatus("obsolete")
_FtpTotalFtpCommands_Type = Counter32
_FtpTotalFtpCommands_Object = MibScalar
ftpTotalFtpCommands = _FtpTotalFtpCommands_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 6),
    _FtpTotalFtpCommands_Type()
)
ftpTotalFtpCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalFtpCommands.setStatus("obsolete")
_FtpTotalFtpReplies_Type = Counter32
_FtpTotalFtpReplies_Object = MibScalar
ftpTotalFtpReplies = _FtpTotalFtpReplies_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 7),
    _FtpTotalFtpReplies_Type()
)
ftpTotalFtpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalFtpReplies.setStatus("obsolete")
_FtpTotalBytesCommands_Type = Counter64
_FtpTotalBytesCommands_Object = MibScalar
ftpTotalBytesCommands = _FtpTotalBytesCommands_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 8),
    _FtpTotalBytesCommands_Type()
)
ftpTotalBytesCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalBytesCommands.setStatus("obsolete")
_FtpTotalBytesReplies_Type = Counter64
_FtpTotalBytesReplies_Object = MibScalar
ftpTotalBytesReplies = _FtpTotalBytesReplies_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 5, 9),
    _FtpTotalBytesReplies_Type()
)
ftpTotalBytesReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTotalBytesReplies.setStatus("obsolete")
_FtpService_ObjectIdentity = ObjectIdentity
ftpService = _FtpService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 6)
)


class _FtpServiceEnabled_Type(Integer32):
    """Custom type ftpServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FtpServiceEnabled_Type.__name__ = "Integer32"
_FtpServiceEnabled_Object = MibScalar
ftpServiceEnabled = _FtpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 6, 1),
    _FtpServiceEnabled_Type()
)
ftpServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpServiceEnabled.setStatus("obsolete")
_FtpServiceMaxUsers_Type = Unsigned32
_FtpServiceMaxUsers_Object = MibScalar
ftpServiceMaxUsers = _FtpServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 6, 2),
    _FtpServiceMaxUsers_Type()
)
ftpServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpServiceMaxUsers.setStatus("obsolete")
_FtpSecurity_ObjectIdentity = ObjectIdentity
ftpSecurity = _FtpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 7)
)


class _FtpNTPasswordEnabled_Type(Integer32):
    """Custom type ftpNTPasswordEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_FtpNTPasswordEnabled_Type.__name__ = "Integer32"
_FtpNTPasswordEnabled_Object = MibScalar
ftpNTPasswordEnabled = _FtpNTPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 7, 1),
    _FtpNTPasswordEnabled_Type()
)
ftpNTPasswordEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNTPasswordEnabled.setStatus("obsolete")


class _FtpNISPasswordEnabled_Type(Integer32):
    """Custom type ftpNISPasswordEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_FtpNISPasswordEnabled_Type.__name__ = "Integer32"
_FtpNISPasswordEnabled_Object = MibScalar
ftpNISPasswordEnabled = _FtpNISPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 4, 7, 2),
    _FtpNISPasswordEnabled_Type()
)
ftpNISPasswordEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNISPasswordEnabled.setStatus("obsolete")
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5)
)
_HttpConfig_ObjectIdentity = ObjectIdentity
httpConfig = _HttpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1)
)
_HttpHostVolumeWWN_Type = DisplayString
_HttpHostVolumeWWN_Object = MibScalar
httpHostVolumeWWN = _HttpHostVolumeWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 1),
    _HttpHostVolumeWWN_Type()
)
httpHostVolumeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHostVolumeWWN.setStatus("obsolete")
_HttpHostVolumeLUN_Type = Unsigned32
_HttpHostVolumeLUN_Object = MibScalar
httpHostVolumeLUN = _HttpHostVolumeLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 2),
    _HttpHostVolumeLUN_Type()
)
httpHostVolumeLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHostVolumeLUN.setStatus("obsolete")
_HttpHostVolumePartitionID_Type = Unsigned32
_HttpHostVolumePartitionID_Object = MibScalar
httpHostVolumePartitionID = _HttpHostVolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 3),
    _HttpHostVolumePartitionID_Type()
)
httpHostVolumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHostVolumePartitionID.setStatus("obsolete")
_HttpRoot_Type = DisplayString
_HttpRoot_Object = MibScalar
httpRoot = _HttpRoot_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 4),
    _HttpRoot_Type()
)
httpRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpRoot.setStatus("obsolete")
_HttpProduct_Type = DisplayString
_HttpProduct_Object = MibScalar
httpProduct = _HttpProduct_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 5),
    _HttpProduct_Type()
)
httpProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProduct.setStatus("obsolete")
_HttpMinTimeOut_Type = Unsigned32
_HttpMinTimeOut_Object = MibScalar
httpMinTimeOut = _HttpMinTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 6),
    _HttpMinTimeOut_Type()
)
httpMinTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMinTimeOut.setStatus("obsolete")
_HttpMaxTimeOut_Type = Unsigned32
_HttpMaxTimeOut_Object = MibScalar
httpMaxTimeOut = _HttpMaxTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 7),
    _HttpMaxTimeOut_Type()
)
httpMaxTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMaxTimeOut.setStatus("obsolete")
_HttpDecrTimeOut_Type = Unsigned32
_HttpDecrTimeOut_Object = MibScalar
httpDecrTimeOut = _HttpDecrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 8),
    _HttpDecrTimeOut_Type()
)
httpDecrTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpDecrTimeOut.setStatus("obsolete")
_HttpIncrTimeOut_Type = Unsigned32
_HttpIncrTimeOut_Object = MibScalar
httpIncrTimeOut = _HttpIncrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 9),
    _HttpIncrTimeOut_Type()
)
httpIncrTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpIncrTimeOut.setStatus("obsolete")
_HttpMaxConnections_Type = Unsigned32
_HttpMaxConnections_Object = MibScalar
httpMaxConnections = _HttpMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 10),
    _HttpMaxConnections_Type()
)
httpMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMaxConnections.setStatus("obsolete")


class _HttpListDirectories_Type(Integer32):
    """Custom type httpListDirectories based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HttpListDirectories_Type.__name__ = "Integer32"
_HttpListDirectories_Object = MibScalar
httpListDirectories = _HttpListDirectories_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 11),
    _HttpListDirectories_Type()
)
httpListDirectories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpListDirectories.setStatus("obsolete")


class _HttpLogging_Type(Integer32):
    """Custom type httpLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HttpLogging_Type.__name__ = "Integer32"
_HttpLogging_Object = MibScalar
httpLogging = _HttpLogging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 12),
    _HttpLogging_Type()
)
httpLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogging.setStatus("obsolete")


class _HttpMaximalLogging_Type(Integer32):
    """Custom type httpMaximalLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HttpMaximalLogging_Type.__name__ = "Integer32"
_HttpMaximalLogging_Object = MibScalar
httpMaximalLogging = _HttpMaximalLogging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 13),
    _HttpMaximalLogging_Type()
)
httpMaximalLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMaximalLogging.setStatus("obsolete")
_HttpLogVolumeWWN_Type = DisplayString
_HttpLogVolumeWWN_Object = MibScalar
httpLogVolumeWWN = _HttpLogVolumeWWN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 14),
    _HttpLogVolumeWWN_Type()
)
httpLogVolumeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogVolumeWWN.setStatus("obsolete")
_HttpLogVolumeLUN_Type = Unsigned32
_HttpLogVolumeLUN_Object = MibScalar
httpLogVolumeLUN = _HttpLogVolumeLUN_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 15),
    _HttpLogVolumeLUN_Type()
)
httpLogVolumeLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogVolumeLUN.setStatus("obsolete")
_HttpLogVolumePartitionID_Type = Unsigned32
_HttpLogVolumePartitionID_Object = MibScalar
httpLogVolumePartitionID = _HttpLogVolumePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 16),
    _HttpLogVolumePartitionID_Type()
)
httpLogVolumePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogVolumePartitionID.setStatus("obsolete")
_HttpLogDirectory_Type = DisplayString
_HttpLogDirectory_Object = MibScalar
httpLogDirectory = _HttpLogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 17),
    _HttpLogDirectory_Type()
)
httpLogDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogDirectory.setStatus("obsolete")
_HttpLogRecordsPerFile_Type = Unsigned32
_HttpLogRecordsPerFile_Object = MibScalar
httpLogRecordsPerFile = _HttpLogRecordsPerFile_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 18),
    _HttpLogRecordsPerFile_Type()
)
httpLogRecordsPerFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpLogRecordsPerFile.setStatus("obsolete")
_HttpMaximumLogFiles_Type = Unsigned32
_HttpMaximumLogFiles_Object = MibScalar
httpMaximumLogFiles = _HttpMaximumLogFiles_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 19),
    _HttpMaximumLogFiles_Type()
)
httpMaximumLogFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMaximumLogFiles.setStatus("obsolete")
_HttpMimeMapNumber_Type = Integer32
_HttpMimeMapNumber_Object = MibScalar
httpMimeMapNumber = _HttpMimeMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 20),
    _HttpMimeMapNumber_Type()
)
httpMimeMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMimeMapNumber.setStatus("obsolete")
_HttpMimeMapTable_Object = MibTable
httpMimeMapTable = _HttpMimeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 21)
)
if mibBuilder.loadTexts:
    httpMimeMapTable.setStatus("obsolete")
_HttpMimeMapEntry_Object = MibTableRow
httpMimeMapEntry = _HttpMimeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 21, 1)
)
httpMimeMapEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "httpMimeMapIndex"),
)
if mibBuilder.loadTexts:
    httpMimeMapEntry.setStatus("obsolete")


class _HttpMimeMapIndex_Type(Integer32):
    """Custom type httpMimeMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_HttpMimeMapIndex_Type.__name__ = "Integer32"
_HttpMimeMapIndex_Object = MibTableColumn
httpMimeMapIndex = _HttpMimeMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 21, 1, 1),
    _HttpMimeMapIndex_Type()
)
httpMimeMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMimeMapIndex.setStatus("obsolete")
_HttpMimeMapExtension_Type = DisplayString
_HttpMimeMapExtension_Object = MibTableColumn
httpMimeMapExtension = _HttpMimeMapExtension_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 21, 1, 2),
    _HttpMimeMapExtension_Type()
)
httpMimeMapExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMimeMapExtension.setStatus("obsolete")
_HttpMimeMapType_Type = DisplayString
_HttpMimeMapType_Object = MibTableColumn
httpMimeMapType = _HttpMimeMapType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 1, 21, 1, 3),
    _HttpMimeMapType_Type()
)
httpMimeMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMimeMapType.setStatus("obsolete")
_HttpStats_ObjectIdentity = ObjectIdentity
httpStats = _HttpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2)
)
_HttpConnsAccepted_Type = Counter64
_HttpConnsAccepted_Object = MibScalar
httpConnsAccepted = _HttpConnsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 1),
    _HttpConnsAccepted_Type()
)
httpConnsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpConnsAccepted.setStatus("obsolete")
_HttpConnsRefused_Type = Counter64
_HttpConnsRefused_Object = MibScalar
httpConnsRefused = _HttpConnsRefused_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 2),
    _HttpConnsRefused_Type()
)
httpConnsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpConnsRefused.setStatus("obsolete")
_HttpBytesXferOut_Type = Counter64
_HttpBytesXferOut_Object = MibScalar
httpBytesXferOut = _HttpBytesXferOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 3),
    _HttpBytesXferOut_Type()
)
httpBytesXferOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpBytesXferOut.setStatus("obsolete")
_HttpBytesXferIn_Type = Counter64
_HttpBytesXferIn_Object = MibScalar
httpBytesXferIn = _HttpBytesXferIn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 4),
    _HttpBytesXferIn_Type()
)
httpBytesXferIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpBytesXferIn.setStatus("obsolete")
_HttpGetRequests_Type = Counter64
_HttpGetRequests_Object = MibScalar
httpGetRequests = _HttpGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 5),
    _HttpGetRequests_Type()
)
httpGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpGetRequests.setStatus("obsolete")
_HttpHeadRequests_Type = Counter64
_HttpHeadRequests_Object = MibScalar
httpHeadRequests = _HttpHeadRequests_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 6),
    _HttpHeadRequests_Type()
)
httpHeadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHeadRequests.setStatus("obsolete")
_HttpPutRequests_Type = Counter64
_HttpPutRequests_Object = MibScalar
httpPutRequests = _HttpPutRequests_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 7),
    _HttpPutRequests_Type()
)
httpPutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPutRequests.setStatus("obsolete")
_HttpPostRequests_Type = Counter64
_HttpPostRequests_Object = MibScalar
httpPostRequests = _HttpPostRequests_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 8),
    _HttpPostRequests_Type()
)
httpPostRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPostRequests.setStatus("obsolete")
_HttpStatusOK_Type = Counter64
_HttpStatusOK_Object = MibScalar
httpStatusOK = _HttpStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 9),
    _HttpStatusOK_Type()
)
httpStatusOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusOK.setStatus("obsolete")
_HttpStatusNotModified_Type = Counter64
_HttpStatusNotModified_Object = MibScalar
httpStatusNotModified = _HttpStatusNotModified_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 10),
    _HttpStatusNotModified_Type()
)
httpStatusNotModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusNotModified.setStatus("obsolete")
_HttpStatusPreconFailed_Type = Counter64
_HttpStatusPreconFailed_Object = MibScalar
httpStatusPreconFailed = _HttpStatusPreconFailed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 11),
    _HttpStatusPreconFailed_Type()
)
httpStatusPreconFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusPreconFailed.setStatus("obsolete")
_HttpStatusBadRequest_Type = Counter64
_HttpStatusBadRequest_Object = MibScalar
httpStatusBadRequest = _HttpStatusBadRequest_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 12),
    _HttpStatusBadRequest_Type()
)
httpStatusBadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusBadRequest.setStatus("obsolete")
_HttpStatusForbidden_Type = Counter64
_HttpStatusForbidden_Object = MibScalar
httpStatusForbidden = _HttpStatusForbidden_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 13),
    _HttpStatusForbidden_Type()
)
httpStatusForbidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusForbidden.setStatus("obsolete")
_HttpStatusNotFound_Type = Counter64
_HttpStatusNotFound_Object = MibScalar
httpStatusNotFound = _HttpStatusNotFound_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 14),
    _HttpStatusNotFound_Type()
)
httpStatusNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusNotFound.setStatus("obsolete")
_HttpStatusURITooLong_Type = Counter64
_HttpStatusURITooLong_Object = MibScalar
httpStatusURITooLong = _HttpStatusURITooLong_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 15),
    _HttpStatusURITooLong_Type()
)
httpStatusURITooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusURITooLong.setStatus("obsolete")
_HttpStatusServerError_Type = Counter64
_HttpStatusServerError_Object = MibScalar
httpStatusServerError = _HttpStatusServerError_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 16),
    _HttpStatusServerError_Type()
)
httpStatusServerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusServerError.setStatus("obsolete")
_HttpStatusNotImplemented_Type = Counter64
_HttpStatusNotImplemented_Object = MibScalar
httpStatusNotImplemented = _HttpStatusNotImplemented_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 17),
    _HttpStatusNotImplemented_Type()
)
httpStatusNotImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusNotImplemented.setStatus("obsolete")
_HttpStatusServiceUnavailable_Type = Counter64
_HttpStatusServiceUnavailable_Object = MibScalar
httpStatusServiceUnavailable = _HttpStatusServiceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 18),
    _HttpStatusServiceUnavailable_Type()
)
httpStatusServiceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusServiceUnavailable.setStatus("obsolete")
_HttpStatusOtherErr_Type = Counter64
_HttpStatusOtherErr_Object = MibScalar
httpStatusOtherErr = _HttpStatusOtherErr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 19),
    _HttpStatusOtherErr_Type()
)
httpStatusOtherErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatusOtherErr.setStatus("obsolete")
_HttpTimeOut_Type = Unsigned32
_HttpTimeOut_Object = MibScalar
httpTimeOut = _HttpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 20),
    _HttpTimeOut_Type()
)
httpTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTimeOut.setStatus("obsolete")
_HttpOpenConnections_Type = Unsigned32
_HttpOpenConnections_Object = MibScalar
httpOpenConnections = _HttpOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 21),
    _HttpOpenConnections_Type()
)
httpOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOpenConnections.setStatus("obsolete")
_HttpActiveConnections_Type = Unsigned32
_HttpActiveConnections_Object = MibScalar
httpActiveConnections = _HttpActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 2, 22),
    _HttpActiveConnections_Type()
)
httpActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpActiveConnections.setStatus("obsolete")
_HttpService_ObjectIdentity = ObjectIdentity
httpService = _HttpService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 3)
)


class _HttpServiceEnabled_Type(Integer32):
    """Custom type httpServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_HttpServiceEnabled_Type.__name__ = "Integer32"
_HttpServiceEnabled_Object = MibScalar
httpServiceEnabled = _HttpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 3, 1),
    _HttpServiceEnabled_Type()
)
httpServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpServiceEnabled.setStatus("obsolete")
_HttpServiceMaxUsers_Type = Unsigned32
_HttpServiceMaxUsers_Object = MibScalar
httpServiceMaxUsers = _HttpServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 5, 3, 2),
    _HttpServiceMaxUsers_Type()
)
httpServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpServiceMaxUsers.setStatus("obsolete")
_IScsi_ObjectIdentity = ObjectIdentity
iScsi = _IScsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6)
)
_IScsiConfiguration_ObjectIdentity = ObjectIdentity
iScsiConfiguration = _IScsiConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1)
)


class _IScsiServiceEnabled_Type(Integer32):
    """Custom type iScsiServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_IScsiServiceEnabled_Type.__name__ = "Integer32"
_IScsiServiceEnabled_Object = MibScalar
iScsiServiceEnabled = _IScsiServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 1),
    _IScsiServiceEnabled_Type()
)
iScsiServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiServiceEnabled.setStatus("current")
_IScsiParameterTable_Object = MibTable
iScsiParameterTable = _IScsiParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    iScsiParameterTable.setStatus("current")
_IScsiParameterEntry_Object = MibTableRow
iScsiParameterEntry = _IScsiParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2, 1)
)
iScsiParameterEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iScsiParameterEVS"),
    (0, "BLUEARC-SERVER-MIB", "iScsiParameterName"),
)
if mibBuilder.loadTexts:
    iScsiParameterEntry.setStatus("current")


class _IScsiParameterEVS_Type(Unsigned32):
    """Custom type iScsiParameterEVS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IScsiParameterEVS_Type.__name__ = "Unsigned32"
_IScsiParameterEVS_Object = MibTableColumn
iScsiParameterEVS = _IScsiParameterEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2, 1, 1),
    _IScsiParameterEVS_Type()
)
iScsiParameterEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiParameterEVS.setStatus("current")
_IScsiParameterName_Type = DisplayString
_IScsiParameterName_Object = MibTableColumn
iScsiParameterName = _IScsiParameterName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2, 1, 2),
    _IScsiParameterName_Type()
)
iScsiParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiParameterName.setStatus("current")


class _IScsiParameterIsBoolean_Type(Integer32):
    """Custom type iScsiParameterIsBoolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boolean", 1),
          ("notBoolean", 2))
    )


_IScsiParameterIsBoolean_Type.__name__ = "Integer32"
_IScsiParameterIsBoolean_Object = MibTableColumn
iScsiParameterIsBoolean = _IScsiParameterIsBoolean_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2, 1, 3),
    _IScsiParameterIsBoolean_Type()
)
iScsiParameterIsBoolean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiParameterIsBoolean.setStatus("current")
_IScsiParameterValue_Type = Unsigned32
_IScsiParameterValue_Object = MibTableColumn
iScsiParameterValue = _IScsiParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 2, 1, 4),
    _IScsiParameterValue_Type()
)
iScsiParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiParameterValue.setStatus("current")
_IScsiTargetNumber_Type = Integer32
_IScsiTargetNumber_Object = MibScalar
iScsiTargetNumber = _IScsiTargetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 3),
    _IScsiTargetNumber_Type()
)
iScsiTargetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetNumber.setStatus("current")
_IScsiTargetTable_Object = MibTable
iScsiTargetTable = _IScsiTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4)
)
if mibBuilder.loadTexts:
    iScsiTargetTable.setStatus("current")
_IScsiTargetEntry_Object = MibTableRow
iScsiTargetEntry = _IScsiTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1)
)
iScsiTargetEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iScsiGloballyUniqueName"),
)
if mibBuilder.loadTexts:
    iScsiTargetEntry.setStatus("current")
_IScsiGloballyUniqueName_Type = DisplayString
_IScsiGloballyUniqueName_Object = MibTableColumn
iScsiGloballyUniqueName = _IScsiGloballyUniqueName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1, 1),
    _IScsiGloballyUniqueName_Type()
)
iScsiGloballyUniqueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiGloballyUniqueName.setStatus("current")
_IScsiTargetName_Type = DisplayString
_IScsiTargetName_Object = MibTableColumn
iScsiTargetName = _IScsiTargetName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1, 2),
    _IScsiTargetName_Type()
)
iScsiTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetName.setStatus("current")
_IScsiTargetComment_Type = DisplayString
_IScsiTargetComment_Object = MibTableColumn
iScsiTargetComment = _IScsiTargetComment_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1, 3),
    _IScsiTargetComment_Type()
)
iScsiTargetComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetComment.setStatus("current")
_IScsiTargetLogicalUnitNumber_Type = Unsigned32
_IScsiTargetLogicalUnitNumber_Object = MibTableColumn
iScsiTargetLogicalUnitNumber = _IScsiTargetLogicalUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1, 4),
    _IScsiTargetLogicalUnitNumber_Type()
)
iScsiTargetLogicalUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetLogicalUnitNumber.setStatus("current")


class _IScsiTargetAuthEnabled_Type(Integer32):
    """Custom type iScsiTargetAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IScsiTargetAuthEnabled_Type.__name__ = "Integer32"
_IScsiTargetAuthEnabled_Object = MibTableColumn
iScsiTargetAuthEnabled = _IScsiTargetAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 4, 1, 5),
    _IScsiTargetAuthEnabled_Type()
)
iScsiTargetAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetAuthEnabled.setStatus("current")
_IScsiLogicalUnitNumber_Type = Integer32
_IScsiLogicalUnitNumber_Object = MibScalar
iScsiLogicalUnitNumber = _IScsiLogicalUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 5),
    _IScsiLogicalUnitNumber_Type()
)
iScsiLogicalUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLogicalUnitNumber.setStatus("current")
_IScsiLogicalUnitTable_Object = MibTable
iScsiLogicalUnitTable = _IScsiLogicalUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6)
)
if mibBuilder.loadTexts:
    iScsiLogicalUnitTable.setStatus("current")
_IScsiLogicalUnitEntry_Object = MibTableRow
iScsiLogicalUnitEntry = _IScsiLogicalUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1)
)
iScsiLogicalUnitEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iScsiLUEvs"),
    (0, "BLUEARC-SERVER-MIB", "iScsiLUName"),
)
if mibBuilder.loadTexts:
    iScsiLogicalUnitEntry.setStatus("current")


class _IScsiLUEvs_Type(Unsigned32):
    """Custom type iScsiLUEvs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IScsiLUEvs_Type.__name__ = "Unsigned32"
_IScsiLUEvs_Object = MibTableColumn
iScsiLUEvs = _IScsiLUEvs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 1),
    _IScsiLUEvs_Type()
)
iScsiLUEvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUEvs.setStatus("current")
_IScsiLUName_Type = DisplayString
_IScsiLUName_Object = MibTableColumn
iScsiLUName = _IScsiLUName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 2),
    _IScsiLUName_Type()
)
iScsiLUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUName.setStatus("current")


class _IScsiLUStatus_Type(Integer32):
    """Custom type iScsiLUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unknown", 1)
    )


_IScsiLUStatus_Type.__name__ = "Integer32"
_IScsiLUStatus_Object = MibTableColumn
iScsiLUStatus = _IScsiLUStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 3),
    _IScsiLUStatus_Type()
)
iScsiLUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUStatus.setStatus("current")
_IScsiLUComment_Type = DisplayString
_IScsiLUComment_Object = MibTableColumn
iScsiLUComment = _IScsiLUComment_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 4),
    _IScsiLUComment_Type()
)
iScsiLUComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUComment.setStatus("current")


class _IScsiLUDeviceId_Type(Unsigned32):
    """Custom type iScsiLUDeviceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IScsiLUDeviceId_Type.__name__ = "Unsigned32"
_IScsiLUDeviceId_Object = MibTableColumn
iScsiLUDeviceId = _IScsiLUDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 5),
    _IScsiLUDeviceId_Type()
)
iScsiLUDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUDeviceId.setStatus("current")
_IScsiLUPath_Type = DisplayString
_IScsiLUPath_Object = MibTableColumn
iScsiLUPath = _IScsiLUPath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 6),
    _IScsiLUPath_Type()
)
iScsiLUPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUPath.setStatus("current")


class _IScsiLUInitialized_Type(Integer32):
    """Custom type iScsiLUInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("uninitialized", 2),
          ("unknown", 3))
    )


_IScsiLUInitialized_Type.__name__ = "Integer32"
_IScsiLUInitialized_Object = MibTableColumn
iScsiLUInitialized = _IScsiLUInitialized_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 7),
    _IScsiLUInitialized_Type()
)
iScsiLUInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUInitialized.setStatus("current")
_IScsiLUSize_Type = Counter64
_IScsiLUSize_Object = MibTableColumn
iScsiLUSize = _IScsiLUSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 6, 1, 8),
    _IScsiLUSize_Type()
)
iScsiLUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiLUSize.setStatus("current")
_IScsiTargetLogicalUnitTable_Object = MibTable
iScsiTargetLogicalUnitTable = _IScsiTargetLogicalUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 7)
)
if mibBuilder.loadTexts:
    iScsiTargetLogicalUnitTable.setStatus("current")
_IScsiTargetLogicalUnitEntry_Object = MibTableRow
iScsiTargetLogicalUnitEntry = _IScsiTargetLogicalUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 7, 1)
)
iScsiTargetLogicalUnitEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iScsiTargetLUTargetName"),
    (0, "BLUEARC-SERVER-MIB", "iScsiTargetLULogicalUnitName"),
)
if mibBuilder.loadTexts:
    iScsiTargetLogicalUnitEntry.setStatus("current")
_IScsiTargetLUTargetName_Type = DisplayString
_IScsiTargetLUTargetName_Object = MibTableColumn
iScsiTargetLUTargetName = _IScsiTargetLUTargetName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 7, 1, 1),
    _IScsiTargetLUTargetName_Type()
)
iScsiTargetLUTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetLUTargetName.setStatus("current")
_IScsiTargetLULogicalUnitName_Type = DisplayString
_IScsiTargetLULogicalUnitName_Object = MibTableColumn
iScsiTargetLULogicalUnitName = _IScsiTargetLULogicalUnitName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 7, 1, 2),
    _IScsiTargetLULogicalUnitName_Type()
)
iScsiTargetLULogicalUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetLULogicalUnitName.setStatus("current")
_IScsiTargetLun_Type = Integer32
_IScsiTargetLun_Object = MibTableColumn
iScsiTargetLun = _IScsiTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 7, 1, 3),
    _IScsiTargetLun_Type()
)
iScsiTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiTargetLun.setStatus("current")
_ISNSTable_Object = MibTable
iSNSTable = _ISNSTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 8)
)
if mibBuilder.loadTexts:
    iSNSTable.setStatus("current")
_ISNSEntry_Object = MibTableRow
iSNSEntry = _ISNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 8, 1)
)
iSNSEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iSNSIpAddress"),
)
if mibBuilder.loadTexts:
    iSNSEntry.setStatus("current")
_ISNSIpAddress_Type = IpAddress
_ISNSIpAddress_Object = MibTableColumn
iSNSIpAddress = _ISNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 8, 1, 1),
    _ISNSIpAddress_Type()
)
iSNSIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSNSIpAddress.setStatus("current")
_ISNSPort_Type = Unsigned32
_ISNSPort_Object = MibTableColumn
iSNSPort = _ISNSPort_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 1, 8, 1, 2),
    _ISNSPort_Type()
)
iSNSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSNSPort.setStatus("current")
_IScsiStatistics_ObjectIdentity = ObjectIdentity
iScsiStatistics = _IScsiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2)
)
_IScsiStatisticsTable_Object = MibTable
iScsiStatisticsTable = _IScsiStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    iScsiStatisticsTable.setStatus("current")
_IScsiStatisticsEntry_Object = MibTableRow
iScsiStatisticsEntry = _IScsiStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2, 1, 1)
)
iScsiStatisticsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "iScsiStatisticsNodeId"),
    (0, "BLUEARC-SERVER-MIB", "iScsiStatisticsName"),
)
if mibBuilder.loadTexts:
    iScsiStatisticsEntry.setStatus("current")
_IScsiStatisticsNodeId_Type = Unsigned32
_IScsiStatisticsNodeId_Object = MibTableColumn
iScsiStatisticsNodeId = _IScsiStatisticsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2, 1, 1, 1),
    _IScsiStatisticsNodeId_Type()
)
iScsiStatisticsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiStatisticsNodeId.setStatus("current")
_IScsiStatisticsName_Type = DisplayString
_IScsiStatisticsName_Object = MibTableColumn
iScsiStatisticsName = _IScsiStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2, 1, 1, 2),
    _IScsiStatisticsName_Type()
)
iScsiStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiStatisticsName.setStatus("current")
_IScsiStatisticsValue_Type = Counter64
_IScsiStatisticsValue_Object = MibTableColumn
iScsiStatisticsValue = _IScsiStatisticsValue_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 3, 6, 2, 1, 1, 3),
    _IScsiStatisticsValue_Type()
)
iScsiStatisticsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iScsiStatisticsValue.setStatus("current")
_Backup_ObjectIdentity = ObjectIdentity
backup = _Backup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4)
)
_NdmpStatus_ObjectIdentity = ObjectIdentity
ndmpStatus = _NdmpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 1)
)


class _NdmpCurrentStatus_Type(Integer32):
    """Custom type ndmpCurrentStatus based on Integer32"""
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
        *(("aborting", 3),
          ("started", 1),
          ("stopped", 2),
          ("unknown", 4))
    )


_NdmpCurrentStatus_Type.__name__ = "Integer32"
_NdmpCurrentStatus_Object = MibScalar
ndmpCurrentStatus = _NdmpCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 1, 1),
    _NdmpCurrentStatus_Type()
)
ndmpCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpCurrentStatus.setStatus("current")


class _NdmpEnabledOnBoot_Type(Integer32):
    """Custom type ndmpEnabledOnBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NdmpEnabledOnBoot_Type.__name__ = "Integer32"
_NdmpEnabledOnBoot_Object = MibScalar
ndmpEnabledOnBoot = _NdmpEnabledOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 1, 2),
    _NdmpEnabledOnBoot_Type()
)
ndmpEnabledOnBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpEnabledOnBoot.setStatus("current")
_NdmpDevices_ObjectIdentity = ObjectIdentity
ndmpDevices = _NdmpDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2)
)
_AutoChangerNumber_Type = Integer32
_AutoChangerNumber_Object = MibScalar
autoChangerNumber = _AutoChangerNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 1),
    _AutoChangerNumber_Type()
)
autoChangerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoChangerNumber.setStatus("current")
_AutoChangerTable_Object = MibTable
autoChangerTable = _AutoChangerTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    autoChangerTable.setStatus("current")
_AutoChangerEntry_Object = MibTableRow
autoChangerEntry = _AutoChangerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2, 1)
)
autoChangerEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "autoChangerIndex"),
)
if mibBuilder.loadTexts:
    autoChangerEntry.setStatus("current")


class _AutoChangerIndex_Type(Integer32):
    """Custom type autoChangerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AutoChangerIndex_Type.__name__ = "Integer32"
_AutoChangerIndex_Object = MibTableColumn
autoChangerIndex = _AutoChangerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2, 1, 1),
    _AutoChangerIndex_Type()
)
autoChangerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoChangerIndex.setStatus("current")
_AutoChangerDeviceName_Type = DisplayString
_AutoChangerDeviceName_Object = MibTableColumn
autoChangerDeviceName = _AutoChangerDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2, 1, 2),
    _AutoChangerDeviceName_Type()
)
autoChangerDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoChangerDeviceName.setStatus("current")
_AutoChangerSerialNumber_Type = DisplayString
_AutoChangerSerialNumber_Object = MibTableColumn
autoChangerSerialNumber = _AutoChangerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2, 1, 3),
    _AutoChangerSerialNumber_Type()
)
autoChangerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoChangerSerialNumber.setStatus("current")
_AutoChangerEVS_Type = DisplayString
_AutoChangerEVS_Object = MibTableColumn
autoChangerEVS = _AutoChangerEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 2, 1, 4),
    _AutoChangerEVS_Type()
)
autoChangerEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoChangerEVS.setStatus("current")
_TapeDriveNumber_Type = Integer32
_TapeDriveNumber_Object = MibScalar
tapeDriveNumber = _TapeDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 3),
    _TapeDriveNumber_Type()
)
tapeDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveNumber.setStatus("current")
_TapeDriveTable_Object = MibTable
tapeDriveTable = _TapeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    tapeDriveTable.setStatus("current")
_TapeDriveEntry_Object = MibTableRow
tapeDriveEntry = _TapeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1)
)
tapeDriveEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "tapeDriveIndex"),
)
if mibBuilder.loadTexts:
    tapeDriveEntry.setStatus("current")


class _TapeDriveIndex_Type(Integer32):
    """Custom type tapeDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TapeDriveIndex_Type.__name__ = "Integer32"
_TapeDriveIndex_Object = MibTableColumn
tapeDriveIndex = _TapeDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 1),
    _TapeDriveIndex_Type()
)
tapeDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveIndex.setStatus("current")
_TapeDriveAutoChangerIndex_Type = Integer32
_TapeDriveAutoChangerIndex_Object = MibTableColumn
tapeDriveAutoChangerIndex = _TapeDriveAutoChangerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 2),
    _TapeDriveAutoChangerIndex_Type()
)
tapeDriveAutoChangerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveAutoChangerIndex.setStatus("current")
_TapeDriveDeviceName_Type = DisplayString
_TapeDriveDeviceName_Object = MibTableColumn
tapeDriveDeviceName = _TapeDriveDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 3),
    _TapeDriveDeviceName_Type()
)
tapeDriveDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveDeviceName.setStatus("current")
_TapeDriveSerialNumber_Type = DisplayString
_TapeDriveSerialNumber_Object = MibTableColumn
tapeDriveSerialNumber = _TapeDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 4),
    _TapeDriveSerialNumber_Type()
)
tapeDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveSerialNumber.setStatus("current")
_TapeDriveLocation_Type = DisplayString
_TapeDriveLocation_Object = MibTableColumn
tapeDriveLocation = _TapeDriveLocation_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 5),
    _TapeDriveLocation_Type()
)
tapeDriveLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveLocation.setStatus("current")
_TapeDriveEVS_Type = DisplayString
_TapeDriveEVS_Object = MibTableColumn
tapeDriveEVS = _TapeDriveEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 2, 4, 1, 6),
    _TapeDriveEVS_Type()
)
tapeDriveEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveEVS.setStatus("current")
_NdmpSnapshotOptions_ObjectIdentity = ObjectIdentity
ndmpSnapshotOptions = _NdmpSnapshotOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 3)
)


class _NdmpAutoSnapCreateEnabled_Type(Integer32):
    """Custom type ndmpAutoSnapCreateEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_NdmpAutoSnapCreateEnabled_Type.__name__ = "Integer32"
_NdmpAutoSnapCreateEnabled_Object = MibScalar
ndmpAutoSnapCreateEnabled = _NdmpAutoSnapCreateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 3, 1),
    _NdmpAutoSnapCreateEnabled_Type()
)
ndmpAutoSnapCreateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpAutoSnapCreateEnabled.setStatus("current")


class _NdmpAutoSnapDeleteMode_Type(Integer32):
    """Custom type ndmpAutoSnapDeleteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 1),
          ("unknown", 3),
          ("whenObsolete", 2))
    )


_NdmpAutoSnapDeleteMode_Type.__name__ = "Integer32"
_NdmpAutoSnapDeleteMode_Object = MibScalar
ndmpAutoSnapDeleteMode = _NdmpAutoSnapDeleteMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 3, 2),
    _NdmpAutoSnapDeleteMode_Type()
)
ndmpAutoSnapDeleteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpAutoSnapDeleteMode.setStatus("current")
_NdmpAutoSnapMaxRetention_Type = Unsigned32
_NdmpAutoSnapMaxRetention_Object = MibScalar
ndmpAutoSnapMaxRetention = _NdmpAutoSnapMaxRetention_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 4, 3, 3),
    _NdmpAutoSnapMaxRetention_Type()
)
ndmpAutoSnapMaxRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpAutoSnapMaxRetention.setStatus("current")
_Mgmnt_ObjectIdentity = ObjectIdentity
mgmnt = _Mgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5)
)
_SystemUsers_ObjectIdentity = ObjectIdentity
systemUsers = _SystemUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1)
)
_SystemUserNumber_Type = Integer32
_SystemUserNumber_Object = MibScalar
systemUserNumber = _SystemUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1, 1),
    _SystemUserNumber_Type()
)
systemUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserNumber.setStatus("current")
_SystemUserTable_Object = MibTable
systemUserTable = _SystemUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    systemUserTable.setStatus("current")
_SystemUserEntry_Object = MibTableRow
systemUserEntry = _SystemUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1, 2, 1)
)
systemUserEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "systemUserName"),
)
if mibBuilder.loadTexts:
    systemUserEntry.setStatus("current")
_SystemUserName_Type = DisplayString
_SystemUserName_Object = MibTableColumn
systemUserName = _SystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1, 2, 1, 1),
    _SystemUserName_Type()
)
systemUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserName.setStatus("current")
_SystemUserAccessLevel_Type = DisplayString
_SystemUserAccessLevel_Object = MibTableColumn
systemUserAccessLevel = _SystemUserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 1, 2, 1, 2),
    _SystemUserAccessLevel_Type()
)
systemUserAccessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserAccessLevel.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2)
)
_LicenseKeyNumber_Type = Integer32
_LicenseKeyNumber_Object = MibScalar
licenseKeyNumber = _LicenseKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 1),
    _LicenseKeyNumber_Type()
)
licenseKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyNumber.setStatus("current")
_LicenseKeyTable_Object = MibTable
licenseKeyTable = _LicenseKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    licenseKeyTable.setStatus("obsolete")
_LicenseKeyEntry_Object = MibTableRow
licenseKeyEntry = _LicenseKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1)
)
licenseKeyEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "licenseKeyIndex"),
)
if mibBuilder.loadTexts:
    licenseKeyEntry.setStatus("obsolete")


class _LicenseKeyIndex_Type(Integer32):
    """Custom type licenseKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_LicenseKeyIndex_Type.__name__ = "Integer32"
_LicenseKeyIndex_Object = MibTableColumn
licenseKeyIndex = _LicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 1),
    _LicenseKeyIndex_Type()
)
licenseKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyIndex.setStatus("obsolete")
_LicenseKeyString_Type = DisplayString
_LicenseKeyString_Object = MibTableColumn
licenseKeyString = _LicenseKeyString_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 2),
    _LicenseKeyString_Type()
)
licenseKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyString.setStatus("obsolete")


class _LicenseKeyValid_Type(Integer32):
    """Custom type licenseKeyValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("unknown", 3),
          ("valid", 1))
    )


_LicenseKeyValid_Type.__name__ = "Integer32"
_LicenseKeyValid_Object = MibTableColumn
licenseKeyValid = _LicenseKeyValid_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 3),
    _LicenseKeyValid_Type()
)
licenseKeyValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyValid.setStatus("obsolete")


class _LicenseCIFSService_Type(Integer32):
    """Custom type licenseCIFSService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_LicenseCIFSService_Type.__name__ = "Integer32"
_LicenseCIFSService_Object = MibTableColumn
licenseCIFSService = _LicenseCIFSService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 4),
    _LicenseCIFSService_Type()
)
licenseCIFSService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCIFSService.setStatus("obsolete")


class _LicenseNFSService_Type(Integer32):
    """Custom type licenseNFSService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_LicenseNFSService_Type.__name__ = "Integer32"
_LicenseNFSService_Object = MibTableColumn
licenseNFSService = _LicenseNFSService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 5),
    _LicenseNFSService_Type()
)
licenseNFSService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseNFSService.setStatus("obsolete")


class _LicenseFTPService_Type(Integer32):
    """Custom type licenseFTPService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_LicenseFTPService_Type.__name__ = "Integer32"
_LicenseFTPService_Object = MibTableColumn
licenseFTPService = _LicenseFTPService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 6),
    _LicenseFTPService_Type()
)
licenseFTPService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFTPService.setStatus("obsolete")


class _LicenseHTTPService_Type(Integer32):
    """Custom type licenseHTTPService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_LicenseHTTPService_Type.__name__ = "Integer32"
_LicenseHTTPService_Object = MibTableColumn
licenseHTTPService = _LicenseHTTPService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 7),
    _LicenseHTTPService_Type()
)
licenseHTTPService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseHTTPService.setStatus("obsolete")


class _LicenseFailoverService_Type(Integer32):
    """Custom type licenseFailoverService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_LicenseFailoverService_Type.__name__ = "Integer32"
_LicenseFailoverService_Object = MibTableColumn
licenseFailoverService = _LicenseFailoverService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 8),
    _LicenseFailoverService_Type()
)
licenseFailoverService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFailoverService.setStatus("obsolete")


class _LicenseRAIDService_Type(Integer32):
    """Custom type licenseRAIDService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 2),
          ("single", 1),
          ("unknown", 3))
    )


_LicenseRAIDService_Type.__name__ = "Integer32"
_LicenseRAIDService_Object = MibTableColumn
licenseRAIDService = _LicenseRAIDService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 2, 1, 9),
    _LicenseRAIDService_Type()
)
licenseRAIDService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRAIDService.setStatus("obsolete")
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 3, 1)
)
licenseEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")


class _LicenseIndex_Type(Integer32):
    """Custom type licenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LicenseIndex_Type.__name__ = "Integer32"
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 3, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")
_LicenseKey_Type = DisplayString
_LicenseKey_Object = MibTableColumn
licenseKey = _LicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 3, 1, 2),
    _LicenseKey_Type()
)
licenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKey.setStatus("current")
_LicenseService_Type = DisplayString
_LicenseService_Object = MibTableColumn
licenseService = _LicenseService_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 2, 3, 1, 3),
    _LicenseService_Type()
)
licenseService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseService.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3)
)
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1)
)


class _WebAccessEnabled_Type(Integer32):
    """Custom type webAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_WebAccessEnabled_Type.__name__ = "Integer32"
_WebAccessEnabled_Object = MibScalar
webAccessEnabled = _WebAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 1),
    _WebAccessEnabled_Type()
)
webAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessEnabled.setStatus("obsolete")


class _WebAccessRestricted_Type(Integer32):
    """Custom type webAccessRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unknown", 3),
          ("unrestricted", 2))
    )


_WebAccessRestricted_Type.__name__ = "Integer32"
_WebAccessRestricted_Object = MibScalar
webAccessRestricted = _WebAccessRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 2),
    _WebAccessRestricted_Type()
)
webAccessRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessRestricted.setStatus("obsolete")
_WebAccessRestrictedNumber_Type = Integer32
_WebAccessRestrictedNumber_Object = MibScalar
webAccessRestrictedNumber = _WebAccessRestrictedNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 3),
    _WebAccessRestrictedNumber_Type()
)
webAccessRestrictedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessRestrictedNumber.setStatus("obsolete")
_WebAccessRestrictedTable_Object = MibTable
webAccessRestrictedTable = _WebAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 4)
)
if mibBuilder.loadTexts:
    webAccessRestrictedTable.setStatus("obsolete")
_WebAccessRestrictedEntry_Object = MibTableRow
webAccessRestrictedEntry = _WebAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 4, 1)
)
webAccessRestrictedEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "webAccessRestrictedHost"),
)
if mibBuilder.loadTexts:
    webAccessRestrictedEntry.setStatus("obsolete")
_WebAccessRestrictedHost_Type = DisplayString
_WebAccessRestrictedHost_Object = MibTableColumn
webAccessRestrictedHost = _WebAccessRestrictedHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 4, 1, 1),
    _WebAccessRestrictedHost_Type()
)
webAccessRestrictedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessRestrictedHost.setStatus("obsolete")
_WebAccessPortNumber_Type = Integer32
_WebAccessPortNumber_Object = MibScalar
webAccessPortNumber = _WebAccessPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 5),
    _WebAccessPortNumber_Type()
)
webAccessPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessPortNumber.setStatus("obsolete")
_WebAccessMaxConnections_Type = Integer32
_WebAccessMaxConnections_Object = MibScalar
webAccessMaxConnections = _WebAccessMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 1, 6),
    _WebAccessMaxConnections_Type()
)
webAccessMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAccessMaxConnections.setStatus("obsolete")
_Sictrl_ObjectIdentity = ObjectIdentity
sictrl = _Sictrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2)
)


class _SictrlAccessEnabled_Type(Integer32):
    """Custom type sictrlAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_SictrlAccessEnabled_Type.__name__ = "Integer32"
_SictrlAccessEnabled_Object = MibScalar
sictrlAccessEnabled = _SictrlAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 1),
    _SictrlAccessEnabled_Type()
)
sictrlAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessEnabled.setStatus("obsolete")


class _SictrlAccessRestricted_Type(Integer32):
    """Custom type sictrlAccessRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unknown", 3),
          ("unrestricted", 2))
    )


_SictrlAccessRestricted_Type.__name__ = "Integer32"
_SictrlAccessRestricted_Object = MibScalar
sictrlAccessRestricted = _SictrlAccessRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 2),
    _SictrlAccessRestricted_Type()
)
sictrlAccessRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessRestricted.setStatus("obsolete")
_SictrlAccessRestrictedNumber_Type = Integer32
_SictrlAccessRestrictedNumber_Object = MibScalar
sictrlAccessRestrictedNumber = _SictrlAccessRestrictedNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 3),
    _SictrlAccessRestrictedNumber_Type()
)
sictrlAccessRestrictedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessRestrictedNumber.setStatus("obsolete")
_SictrlAccessRestrictedTable_Object = MibTable
sictrlAccessRestrictedTable = _SictrlAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 4)
)
if mibBuilder.loadTexts:
    sictrlAccessRestrictedTable.setStatus("obsolete")
_SictrlAccessRestrictedEntry_Object = MibTableRow
sictrlAccessRestrictedEntry = _SictrlAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 4, 1)
)
sictrlAccessRestrictedEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "sictrlAccessRestrictedHost"),
)
if mibBuilder.loadTexts:
    sictrlAccessRestrictedEntry.setStatus("obsolete")
_SictrlAccessRestrictedHost_Type = DisplayString
_SictrlAccessRestrictedHost_Object = MibTableColumn
sictrlAccessRestrictedHost = _SictrlAccessRestrictedHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 4, 1, 1),
    _SictrlAccessRestrictedHost_Type()
)
sictrlAccessRestrictedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessRestrictedHost.setStatus("obsolete")
_SictrlAccessPortNumber_Type = Integer32
_SictrlAccessPortNumber_Object = MibScalar
sictrlAccessPortNumber = _SictrlAccessPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 5),
    _SictrlAccessPortNumber_Type()
)
sictrlAccessPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessPortNumber.setStatus("obsolete")
_SictrlAccessMaxConnections_Type = Integer32
_SictrlAccessMaxConnections_Object = MibScalar
sictrlAccessMaxConnections = _SictrlAccessMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 2, 6),
    _SictrlAccessMaxConnections_Type()
)
sictrlAccessMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlAccessMaxConnections.setStatus("obsolete")
_Telnet_ObjectIdentity = ObjectIdentity
telnet = _Telnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3)
)


class _TelnetAccessEnabled_Type(Integer32):
    """Custom type telnetAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_TelnetAccessEnabled_Type.__name__ = "Integer32"
_TelnetAccessEnabled_Object = MibScalar
telnetAccessEnabled = _TelnetAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 1),
    _TelnetAccessEnabled_Type()
)
telnetAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessEnabled.setStatus("current")


class _TelnetAccessRestricted_Type(Integer32):
    """Custom type telnetAccessRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unknown", 3),
          ("unrestricted", 2))
    )


_TelnetAccessRestricted_Type.__name__ = "Integer32"
_TelnetAccessRestricted_Object = MibScalar
telnetAccessRestricted = _TelnetAccessRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 2),
    _TelnetAccessRestricted_Type()
)
telnetAccessRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessRestricted.setStatus("current")
_TelnetAccessRestrictedNumber_Type = Integer32
_TelnetAccessRestrictedNumber_Object = MibScalar
telnetAccessRestrictedNumber = _TelnetAccessRestrictedNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 3),
    _TelnetAccessRestrictedNumber_Type()
)
telnetAccessRestrictedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessRestrictedNumber.setStatus("current")
_TelnetAccessRestrictedTable_Object = MibTable
telnetAccessRestrictedTable = _TelnetAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 4)
)
if mibBuilder.loadTexts:
    telnetAccessRestrictedTable.setStatus("current")
_TelnetAccessRestrictedEntry_Object = MibTableRow
telnetAccessRestrictedEntry = _TelnetAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 4, 1)
)
telnetAccessRestrictedEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "telnetAccessRestrictedHost"),
)
if mibBuilder.loadTexts:
    telnetAccessRestrictedEntry.setStatus("current")
_TelnetAccessRestrictedHost_Type = DisplayString
_TelnetAccessRestrictedHost_Object = MibTableColumn
telnetAccessRestrictedHost = _TelnetAccessRestrictedHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 4, 1, 1),
    _TelnetAccessRestrictedHost_Type()
)
telnetAccessRestrictedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessRestrictedHost.setStatus("current")
_TelnetAccessPortNumber_Type = Integer32
_TelnetAccessPortNumber_Object = MibScalar
telnetAccessPortNumber = _TelnetAccessPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 5),
    _TelnetAccessPortNumber_Type()
)
telnetAccessPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessPortNumber.setStatus("current")
_TelnetAccessMaxConnections_Type = Integer32
_TelnetAccessMaxConnections_Object = MibScalar
telnetAccessMaxConnections = _TelnetAccessMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 3, 6),
    _TelnetAccessMaxConnections_Type()
)
telnetAccessMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetAccessMaxConnections.setStatus("current")
_SecureWeb_ObjectIdentity = ObjectIdentity
secureWeb = _SecureWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4)
)


class _SecureWebAccessEnabled_Type(Integer32):
    """Custom type secureWebAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_SecureWebAccessEnabled_Type.__name__ = "Integer32"
_SecureWebAccessEnabled_Object = MibScalar
secureWebAccessEnabled = _SecureWebAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 1),
    _SecureWebAccessEnabled_Type()
)
secureWebAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessEnabled.setStatus("obsolete")


class _SecureWebAccessRestricted_Type(Integer32):
    """Custom type secureWebAccessRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unknown", 3),
          ("unrestricted", 2))
    )


_SecureWebAccessRestricted_Type.__name__ = "Integer32"
_SecureWebAccessRestricted_Object = MibScalar
secureWebAccessRestricted = _SecureWebAccessRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 2),
    _SecureWebAccessRestricted_Type()
)
secureWebAccessRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessRestricted.setStatus("obsolete")
_SecureWebAccessRestrictedNumber_Type = Integer32
_SecureWebAccessRestrictedNumber_Object = MibScalar
secureWebAccessRestrictedNumber = _SecureWebAccessRestrictedNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 3),
    _SecureWebAccessRestrictedNumber_Type()
)
secureWebAccessRestrictedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessRestrictedNumber.setStatus("obsolete")
_SecureWebAccessRestrictedTable_Object = MibTable
secureWebAccessRestrictedTable = _SecureWebAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 4)
)
if mibBuilder.loadTexts:
    secureWebAccessRestrictedTable.setStatus("obsolete")
_SecureWebAccessRestrictedEntry_Object = MibTableRow
secureWebAccessRestrictedEntry = _SecureWebAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 4, 1)
)
secureWebAccessRestrictedEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "secureWebAccessRestrictedHost"),
)
if mibBuilder.loadTexts:
    secureWebAccessRestrictedEntry.setStatus("obsolete")
_SecureWebAccessRestrictedHost_Type = DisplayString
_SecureWebAccessRestrictedHost_Object = MibTableColumn
secureWebAccessRestrictedHost = _SecureWebAccessRestrictedHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 4, 1, 1),
    _SecureWebAccessRestrictedHost_Type()
)
secureWebAccessRestrictedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessRestrictedHost.setStatus("obsolete")
_SecureWebAccessPortNumber_Type = Integer32
_SecureWebAccessPortNumber_Object = MibScalar
secureWebAccessPortNumber = _SecureWebAccessPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 5),
    _SecureWebAccessPortNumber_Type()
)
secureWebAccessPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessPortNumber.setStatus("obsolete")
_SecureWebAccessMaxConnections_Type = Integer32
_SecureWebAccessMaxConnections_Object = MibScalar
secureWebAccessMaxConnections = _SecureWebAccessMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 4, 6),
    _SecureWebAccessMaxConnections_Type()
)
secureWebAccessMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebAccessMaxConnections.setStatus("obsolete")
_Lcd_ObjectIdentity = ObjectIdentity
lcd = _Lcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 5)
)


class _LcdFrontPanelLocked_Type(Integer32):
    """Custom type lcdFrontPanelLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unLocked", 2))
    )


_LcdFrontPanelLocked_Type.__name__ = "Integer32"
_LcdFrontPanelLocked_Object = MibScalar
lcdFrontPanelLocked = _LcdFrontPanelLocked_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 3, 5, 1),
    _LcdFrontPanelLocked_Type()
)
lcdFrontPanelLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdFrontPanelLocked.setStatus("obsolete")
_Eventlog_ObjectIdentity = ObjectIdentity
eventlog = _Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4)
)
_EventLogNumber_Type = Integer32
_EventLogNumber_Object = MibScalar
eventLogNumber = _EventLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 1),
    _EventLogNumber_Type()
)
eventLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogNumber.setStatus("obsolete")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("obsolete")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 2, 1)
)
eventLogEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "eventLogTimeStamp"),
    (0, "BLUEARC-SERVER-MIB", "eventLogHandle"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("obsolete")
_EventLogTimeStamp_Type = DisplayString
_EventLogTimeStamp_Object = MibTableColumn
eventLogTimeStamp = _EventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 2, 1, 1),
    _EventLogTimeStamp_Type()
)
eventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTimeStamp.setStatus("obsolete")


class _EventLogHandle_Type(Integer32):
    """Custom type eventLogHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventLogHandle_Type.__name__ = "Integer32"
_EventLogHandle_Object = MibTableColumn
eventLogHandle = _EventLogHandle_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 2, 1, 2),
    _EventLogHandle_Type()
)
eventLogHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogHandle.setStatus("obsolete")
_EventLogText_Type = DisplayString
_EventLogText_Object = MibTableColumn
eventLogText = _EventLogText_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 4, 2, 1, 3),
    _EventLogText_Type()
)
eventLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogText.setStatus("obsolete")
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5)
)
_MailAlertConfig_ObjectIdentity = ObjectIdentity
mailAlertConfig = _MailAlertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1)
)
_SmtpAddr_Type = DisplayString
_SmtpAddr_Object = MibScalar
smtpAddr = _SmtpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 1),
    _SmtpAddr_Type()
)
smtpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpAddr.setStatus("current")


class _SmtpCritFreq_Type(Integer32):
    """Custom type smtpCritFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_SmtpCritFreq_Type.__name__ = "Integer32"
_SmtpCritFreq_Object = MibScalar
smtpCritFreq = _SmtpCritFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 2),
    _SmtpCritFreq_Type()
)
smtpCritFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpCritFreq.setStatus("current")


class _SmtpSevFreq_Type(Integer32):
    """Custom type smtpSevFreq based on Integer32"""
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
        *(("daily", 3),
          ("immediately", 2),
          ("never", 1),
          ("unknown", 4))
    )


_SmtpSevFreq_Type.__name__ = "Integer32"
_SmtpSevFreq_Object = MibScalar
smtpSevFreq = _SmtpSevFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 3),
    _SmtpSevFreq_Type()
)
smtpSevFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSevFreq.setStatus("current")


class _SmtpWarnFreq_Type(Integer32):
    """Custom type smtpWarnFreq based on Integer32"""
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
        *(("daily", 3),
          ("immediately", 2),
          ("never", 1),
          ("unknown", 4))
    )


_SmtpWarnFreq_Type.__name__ = "Integer32"
_SmtpWarnFreq_Object = MibScalar
smtpWarnFreq = _SmtpWarnFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 4),
    _SmtpWarnFreq_Type()
)
smtpWarnFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpWarnFreq.setStatus("current")


class _SmtpInfoFreq_Type(Integer32):
    """Custom type smtpInfoFreq based on Integer32"""
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
        *(("daily", 3),
          ("immediately", 2),
          ("never", 1),
          ("unknown", 4))
    )


_SmtpInfoFreq_Type.__name__ = "Integer32"
_SmtpInfoFreq_Object = MibScalar
smtpInfoFreq = _SmtpInfoFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 5),
    _SmtpInfoFreq_Type()
)
smtpInfoFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpInfoFreq.setStatus("current")
_SmtpRecipNumber_Type = Integer32
_SmtpRecipNumber_Object = MibScalar
smtpRecipNumber = _SmtpRecipNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 6),
    _SmtpRecipNumber_Type()
)
smtpRecipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipNumber.setStatus("current")
_SmtpRecipTable_Object = MibTable
smtpRecipTable = _SmtpRecipTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 7)
)
if mibBuilder.loadTexts:
    smtpRecipTable.setStatus("obsolete")
_SmtpRecipEntry_Object = MibTableRow
smtpRecipEntry = _SmtpRecipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 7, 1)
)
smtpRecipEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "smtpRecipIndex"),
)
if mibBuilder.loadTexts:
    smtpRecipEntry.setStatus("obsolete")


class _SmtpRecipIndex_Type(Integer32):
    """Custom type smtpRecipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SmtpRecipIndex_Type.__name__ = "Integer32"
_SmtpRecipIndex_Object = MibTableColumn
smtpRecipIndex = _SmtpRecipIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 7, 1, 1),
    _SmtpRecipIndex_Type()
)
smtpRecipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipIndex.setStatus("obsolete")
_SmtpRecipName_Type = DisplayString
_SmtpRecipName_Object = MibTableColumn
smtpRecipName = _SmtpRecipName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 7, 1, 2),
    _SmtpRecipName_Type()
)
smtpRecipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipName.setStatus("obsolete")


class _SmtpDiagUUencEnabled_Type(Integer32):
    """Custom type smtpDiagUUencEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_SmtpDiagUUencEnabled_Type.__name__ = "Integer32"
_SmtpDiagUUencEnabled_Object = MibScalar
smtpDiagUUencEnabled = _SmtpDiagUUencEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 8),
    _SmtpDiagUUencEnabled_Type()
)
smtpDiagUUencEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpDiagUUencEnabled.setStatus("current")
_SmtpUndisclosedRecipNumber_Type = Integer32
_SmtpUndisclosedRecipNumber_Object = MibScalar
smtpUndisclosedRecipNumber = _SmtpUndisclosedRecipNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 9),
    _SmtpUndisclosedRecipNumber_Type()
)
smtpUndisclosedRecipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpUndisclosedRecipNumber.setStatus("obsolete")
_SmtpUndisclosedRecipTable_Object = MibTable
smtpUndisclosedRecipTable = _SmtpUndisclosedRecipTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 10)
)
if mibBuilder.loadTexts:
    smtpUndisclosedRecipTable.setStatus("obsolete")
_SmtpUndisclosedRecipEntry_Object = MibTableRow
smtpUndisclosedRecipEntry = _SmtpUndisclosedRecipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 10, 1)
)
smtpUndisclosedRecipEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "smtpUndisclosedRecipIndex"),
)
if mibBuilder.loadTexts:
    smtpUndisclosedRecipEntry.setStatus("obsolete")


class _SmtpUndisclosedRecipIndex_Type(Integer32):
    """Custom type smtpUndisclosedRecipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SmtpUndisclosedRecipIndex_Type.__name__ = "Integer32"
_SmtpUndisclosedRecipIndex_Object = MibTableColumn
smtpUndisclosedRecipIndex = _SmtpUndisclosedRecipIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 10, 1, 1),
    _SmtpUndisclosedRecipIndex_Type()
)
smtpUndisclosedRecipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpUndisclosedRecipIndex.setStatus("obsolete")
_SmtpUndisclosedRecipName_Type = DisplayString
_SmtpUndisclosedRecipName_Object = MibTableColumn
smtpUndisclosedRecipName = _SmtpUndisclosedRecipName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 10, 1, 2),
    _SmtpUndisclosedRecipName_Type()
)
smtpUndisclosedRecipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpUndisclosedRecipName.setStatus("obsolete")
_SmtpRecipientTable_Object = MibTable
smtpRecipientTable = _SmtpRecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11)
)
if mibBuilder.loadTexts:
    smtpRecipientTable.setStatus("current")
_SmtpRecipientEntry_Object = MibTableRow
smtpRecipientEntry = _SmtpRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11, 1)
)
smtpRecipientEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "smtpRecipientIndex"),
)
if mibBuilder.loadTexts:
    smtpRecipientEntry.setStatus("current")


class _SmtpRecipientIndex_Type(Integer32):
    """Custom type smtpRecipientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SmtpRecipientIndex_Type.__name__ = "Integer32"
_SmtpRecipientIndex_Object = MibTableColumn
smtpRecipientIndex = _SmtpRecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11, 1, 1),
    _SmtpRecipientIndex_Type()
)
smtpRecipientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipientIndex.setStatus("current")
_SmtpRecipientName_Type = DisplayString
_SmtpRecipientName_Object = MibTableColumn
smtpRecipientName = _SmtpRecipientName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11, 1, 2),
    _SmtpRecipientName_Type()
)
smtpRecipientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipientName.setStatus("current")
_SmtpRecipientDisclose_Type = DisplayString
_SmtpRecipientDisclose_Object = MibTableColumn
smtpRecipientDisclose = _SmtpRecipientDisclose_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11, 1, 3),
    _SmtpRecipientDisclose_Type()
)
smtpRecipientDisclose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipientDisclose.setStatus("current")
_SmtpRecipientEmpty_Type = DisplayString
_SmtpRecipientEmpty_Object = MibTableColumn
smtpRecipientEmpty = _SmtpRecipientEmpty_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 1, 11, 1, 4),
    _SmtpRecipientEmpty_Type()
)
smtpRecipientEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipientEmpty.setStatus("current")
_WinAlertConfig_ObjectIdentity = ObjectIdentity
winAlertConfig = _WinAlertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2)
)


class _WinCritFreq_Type(Integer32):
    """Custom type winCritFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_WinCritFreq_Type.__name__ = "Integer32"
_WinCritFreq_Object = MibScalar
winCritFreq = _WinCritFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 1),
    _WinCritFreq_Type()
)
winCritFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winCritFreq.setStatus("obsolete")


class _WinSevFreq_Type(Integer32):
    """Custom type winSevFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_WinSevFreq_Type.__name__ = "Integer32"
_WinSevFreq_Object = MibScalar
winSevFreq = _WinSevFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 2),
    _WinSevFreq_Type()
)
winSevFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winSevFreq.setStatus("obsolete")


class _WinWarnFreq_Type(Integer32):
    """Custom type winWarnFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_WinWarnFreq_Type.__name__ = "Integer32"
_WinWarnFreq_Object = MibScalar
winWarnFreq = _WinWarnFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 3),
    _WinWarnFreq_Type()
)
winWarnFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winWarnFreq.setStatus("obsolete")


class _WinInfoFreq_Type(Integer32):
    """Custom type winInfoFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_WinInfoFreq_Type.__name__ = "Integer32"
_WinInfoFreq_Object = MibScalar
winInfoFreq = _WinInfoFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 4),
    _WinInfoFreq_Type()
)
winInfoFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winInfoFreq.setStatus("obsolete")
_WinRecipNumber_Type = Integer32
_WinRecipNumber_Object = MibScalar
winRecipNumber = _WinRecipNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 5),
    _WinRecipNumber_Type()
)
winRecipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winRecipNumber.setStatus("obsolete")
_WinRecipTable_Object = MibTable
winRecipTable = _WinRecipTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 6)
)
if mibBuilder.loadTexts:
    winRecipTable.setStatus("obsolete")
_WinRecipEntry_Object = MibTableRow
winRecipEntry = _WinRecipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 6, 1)
)
winRecipEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "winRecipIndex"),
)
if mibBuilder.loadTexts:
    winRecipEntry.setStatus("obsolete")


class _WinRecipIndex_Type(Integer32):
    """Custom type winRecipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WinRecipIndex_Type.__name__ = "Integer32"
_WinRecipIndex_Object = MibTableColumn
winRecipIndex = _WinRecipIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 6, 1, 1),
    _WinRecipIndex_Type()
)
winRecipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winRecipIndex.setStatus("obsolete")
_WinRecipName_Type = DisplayString
_WinRecipName_Object = MibTableColumn
winRecipName = _WinRecipName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 2, 6, 1, 2),
    _WinRecipName_Type()
)
winRecipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winRecipName.setStatus("obsolete")
_SnmpAlertConfig_ObjectIdentity = ObjectIdentity
snmpAlertConfig = _SnmpAlertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3)
)


class _SnmpCritFreq_Type(Integer32):
    """Custom type snmpCritFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_SnmpCritFreq_Type.__name__ = "Integer32"
_SnmpCritFreq_Object = MibScalar
snmpCritFreq = _SnmpCritFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 1),
    _SnmpCritFreq_Type()
)
snmpCritFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCritFreq.setStatus("current")


class _SnmpSevFreq_Type(Integer32):
    """Custom type snmpSevFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_SnmpSevFreq_Type.__name__ = "Integer32"
_SnmpSevFreq_Object = MibScalar
snmpSevFreq = _SnmpSevFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 2),
    _SnmpSevFreq_Type()
)
snmpSevFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSevFreq.setStatus("current")


class _SnmpWarnFreq_Type(Integer32):
    """Custom type snmpWarnFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_SnmpWarnFreq_Type.__name__ = "Integer32"
_SnmpWarnFreq_Object = MibScalar
snmpWarnFreq = _SnmpWarnFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 3),
    _SnmpWarnFreq_Type()
)
snmpWarnFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWarnFreq.setStatus("current")


class _SnmpInfoFreq_Type(Integer32):
    """Custom type snmpInfoFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1),
          ("unknown", 3))
    )


_SnmpInfoFreq_Type.__name__ = "Integer32"
_SnmpInfoFreq_Object = MibScalar
snmpInfoFreq = _SnmpInfoFreq_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 4),
    _SnmpInfoFreq_Type()
)
snmpInfoFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInfoFreq.setStatus("current")
_SnmpRecipNumber_Type = Integer32
_SnmpRecipNumber_Object = MibScalar
snmpRecipNumber = _SnmpRecipNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 5),
    _SnmpRecipNumber_Type()
)
snmpRecipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRecipNumber.setStatus("obsolete")
_SnmpRecipTable_Object = MibTable
snmpRecipTable = _SnmpRecipTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 6)
)
if mibBuilder.loadTexts:
    snmpRecipTable.setStatus("obsolete")
_SnmpRecipEntry_Object = MibTableRow
snmpRecipEntry = _SnmpRecipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 6, 1)
)
snmpRecipEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snmpRecipIndex"),
)
if mibBuilder.loadTexts:
    snmpRecipEntry.setStatus("obsolete")


class _SnmpRecipIndex_Type(Integer32):
    """Custom type snmpRecipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SnmpRecipIndex_Type.__name__ = "Integer32"
_SnmpRecipIndex_Object = MibTableColumn
snmpRecipIndex = _SnmpRecipIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 6, 1, 1),
    _SnmpRecipIndex_Type()
)
snmpRecipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRecipIndex.setStatus("obsolete")
_SnmpRecipName_Type = DisplayString
_SnmpRecipName_Object = MibTableColumn
snmpRecipName = _SnmpRecipName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 5, 3, 6, 1, 2),
    _SnmpRecipName_Type()
)
snmpRecipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRecipName.setStatus("obsolete")
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6)
)


class _SnmpProtocolMode_Type(Integer32):
    """Custom type snmpProtocolMode based on Integer32"""
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
        *(("bilingual", 1),
          ("unknown", 4),
          ("version1", 2),
          ("version2c", 3))
    )


_SnmpProtocolMode_Type.__name__ = "Integer32"
_SnmpProtocolMode_Object = MibScalar
snmpProtocolMode = _SnmpProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 1),
    _SnmpProtocolMode_Type()
)
snmpProtocolMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProtocolMode.setStatus("current")


class _SnmpAccessRestricted_Type(Integer32):
    """Custom type snmpAccessRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unknown", 3),
          ("unrestricted", 2))
    )


_SnmpAccessRestricted_Type.__name__ = "Integer32"
_SnmpAccessRestricted_Object = MibScalar
snmpAccessRestricted = _SnmpAccessRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 2),
    _SnmpAccessRestricted_Type()
)
snmpAccessRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessRestricted.setStatus("current")
_SnmpAccessRestrictedNumber_Type = Integer32
_SnmpAccessRestrictedNumber_Object = MibScalar
snmpAccessRestrictedNumber = _SnmpAccessRestrictedNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 3),
    _SnmpAccessRestrictedNumber_Type()
)
snmpAccessRestrictedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessRestrictedNumber.setStatus("current")
_SnmpAccessRestrictedTable_Object = MibTable
snmpAccessRestrictedTable = _SnmpAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    snmpAccessRestrictedTable.setStatus("current")
_SnmpAccessRestrictedEntry_Object = MibTableRow
snmpAccessRestrictedEntry = _SnmpAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 4, 1)
)
snmpAccessRestrictedEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snmpAccessRestrictedHost"),
)
if mibBuilder.loadTexts:
    snmpAccessRestrictedEntry.setStatus("current")
_SnmpAccessRestrictedHost_Type = DisplayString
_SnmpAccessRestrictedHost_Object = MibTableColumn
snmpAccessRestrictedHost = _SnmpAccessRestrictedHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 4, 1, 1),
    _SnmpAccessRestrictedHost_Type()
)
snmpAccessRestrictedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessRestrictedHost.setStatus("current")
_SnmpTrapHostNumber_Type = Integer32
_SnmpTrapHostNumber_Object = MibScalar
snmpTrapHostNumber = _SnmpTrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 5),
    _SnmpTrapHostNumber_Type()
)
snmpTrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHostNumber.setStatus("current")
_SnmpTrapHostTable_Object = MibTable
snmpTrapHostTable = _SnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    snmpTrapHostTable.setStatus("current")
_SnmpTrapHostEntry_Object = MibTableRow
snmpTrapHostEntry = _SnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 6, 1)
)
snmpTrapHostEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "snmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapHostEntry.setStatus("current")


class _SnmpTrapHostIndex_Type(Integer32):
    """Custom type snmpTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SnmpTrapHostIndex_Type.__name__ = "Integer32"
_SnmpTrapHostIndex_Object = MibTableColumn
snmpTrapHostIndex = _SnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 6, 1, 1),
    _SnmpTrapHostIndex_Type()
)
snmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHostIndex.setStatus("current")
_SnmpTrapHost_Type = DisplayString
_SnmpTrapHost_Object = MibTableColumn
snmpTrapHost = _SnmpTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 6, 6, 1, 2),
    _SnmpTrapHost_Type()
)
snmpTrapHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHost.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7)
)
_VerinfoSw_Type = DisplayString
_VerinfoSw_Object = MibScalar
verinfoSw = _VerinfoSw_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 1),
    _VerinfoSw_Type()
)
verinfoSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verinfoSw.setStatus("current")
_VerinfoHw_Type = DisplayString
_VerinfoHw_Object = MibScalar
verinfoHw = _VerinfoHw_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 2),
    _VerinfoHw_Type()
)
verinfoHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verinfoHw.setStatus("current")
_VerModNumber_Type = Integer32
_VerModNumber_Object = MibScalar
verModNumber = _VerModNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 3),
    _VerModNumber_Type()
)
verModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModNumber.setStatus("current")
_VerModTable_Object = MibTable
verModTable = _VerModTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4)
)
if mibBuilder.loadTexts:
    verModTable.setStatus("current")
_VerModEntry_Object = MibTableRow
verModEntry = _VerModEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1)
)
verModEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "verModIndex"),
)
if mibBuilder.loadTexts:
    verModEntry.setStatus("current")


class _VerModIndex_Type(Integer32):
    """Custom type verModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 3),
          ("fsb", 2),
          ("tcp", 1))
    )


_VerModIndex_Type.__name__ = "Integer32"
_VerModIndex_Object = MibTableColumn
verModIndex = _VerModIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 1),
    _VerModIndex_Type()
)
verModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModIndex.setStatus("current")
_VerModLoader_Type = DisplayString
_VerModLoader_Object = MibTableColumn
verModLoader = _VerModLoader_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 2),
    _VerModLoader_Type()
)
verModLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModLoader.setStatus("current")
_VerModKernel_Type = DisplayString
_VerModKernel_Object = MibTableColumn
verModKernel = _VerModKernel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 3),
    _VerModKernel_Type()
)
verModKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModKernel.setStatus("current")
_VerModHw_Type = DisplayString
_VerModHw_Object = MibTableColumn
verModHw = _VerModHw_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 4),
    _VerModHw_Type()
)
verModHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModHw.setStatus("current")
_VerModSerial_Type = Integer32
_VerModSerial_Object = MibTableColumn
verModSerial = _VerModSerial_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 5),
    _VerModSerial_Type()
)
verModSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModSerial.setStatus("current")
_VerModBuildState_Type = Integer32
_VerModBuildState_Object = MibTableColumn
verModBuildState = _VerModBuildState_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 6),
    _VerModBuildState_Type()
)
verModBuildState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModBuildState.setStatus("current")
_VerModUniq0_Type = DisplayString
_VerModUniq0_Object = MibTableColumn
verModUniq0 = _VerModUniq0_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 7),
    _VerModUniq0_Type()
)
verModUniq0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModUniq0.setStatus("current")
_VerModUniq1_Type = DisplayString
_VerModUniq1_Object = MibTableColumn
verModUniq1 = _VerModUniq1_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 8),
    _VerModUniq1_Type()
)
verModUniq1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModUniq1.setStatus("current")
_VerModFirstDate_Type = DisplayString
_VerModFirstDate_Object = MibTableColumn
verModFirstDate = _VerModFirstDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 9),
    _VerModFirstDate_Type()
)
verModFirstDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModFirstDate.setStatus("current")
_VerModMTDSLastFailure_Type = DisplayString
_VerModMTDSLastFailure_Object = MibTableColumn
verModMTDSLastFailure = _VerModMTDSLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 10),
    _VerModMTDSLastFailure_Type()
)
verModMTDSLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModMTDSLastFailure.setStatus("current")
_VerModMTDSFailures_Type = Integer32
_VerModMTDSFailures_Object = MibTableColumn
verModMTDSFailures = _VerModMTDSFailures_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 11),
    _VerModMTDSFailures_Type()
)
verModMTDSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModMTDSFailures.setStatus("current")
_VerModMTDSLastPass_Type = DisplayString
_VerModMTDSLastPass_Object = MibTableColumn
verModMTDSLastPass = _VerModMTDSLastPass_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 12),
    _VerModMTDSLastPass_Type()
)
verModMTDSLastPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModMTDSLastPass.setStatus("current")
_VerModMTDSPasses_Type = Integer32
_VerModMTDSPasses_Object = MibTableColumn
verModMTDSPasses = _VerModMTDSPasses_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 13),
    _VerModMTDSPasses_Type()
)
verModMTDSPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModMTDSPasses.setStatus("current")
_VerModCardID_Type = Integer32
_VerModCardID_Object = MibTableColumn
verModCardID = _VerModCardID_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 14),
    _VerModCardID_Type()
)
verModCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModCardID.setStatus("current")
_VerModCardRev_Type = Integer32
_VerModCardRev_Object = MibTableColumn
verModCardRev = _VerModCardRev_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 15),
    _VerModCardRev_Type()
)
verModCardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModCardRev.setStatus("current")
_VerModGlueRev_Type = Integer32
_VerModGlueRev_Object = MibTableColumn
verModGlueRev = _VerModGlueRev_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 7, 4, 1, 16),
    _VerModGlueRev_Type()
)
verModGlueRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verModGlueRev.setStatus("current")
_Cron_ObjectIdentity = ObjectIdentity
cron = _Cron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8)
)
_CronJobNumber_Type = Integer32
_CronJobNumber_Object = MibScalar
cronJobNumber = _CronJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 1),
    _CronJobNumber_Type()
)
cronJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobNumber.setStatus("current")
_CronJobTable_Object = MibTable
cronJobTable = _CronJobTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2)
)
if mibBuilder.loadTexts:
    cronJobTable.setStatus("current")
_CronJobEntry_Object = MibTableRow
cronJobEntry = _CronJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1)
)
cronJobEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "cronJobIndex"),
)
if mibBuilder.loadTexts:
    cronJobEntry.setStatus("current")


class _CronJobIndex_Type(Integer32):
    """Custom type cronJobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_CronJobIndex_Type.__name__ = "Integer32"
_CronJobIndex_Object = MibTableColumn
cronJobIndex = _CronJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1, 1),
    _CronJobIndex_Type()
)
cronJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobIndex.setStatus("current")
_CronJobDateSpec_Type = DisplayString
_CronJobDateSpec_Object = MibTableColumn
cronJobDateSpec = _CronJobDateSpec_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1, 2),
    _CronJobDateSpec_Type()
)
cronJobDateSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobDateSpec.setStatus("current")
_CronJobCommandList_Type = DisplayString
_CronJobCommandList_Object = MibTableColumn
cronJobCommandList = _CronJobCommandList_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1, 3),
    _CronJobCommandList_Type()
)
cronJobCommandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobCommandList.setStatus("current")
_CronJobMailList_Type = DisplayString
_CronJobMailList_Object = MibTableColumn
cronJobMailList = _CronJobMailList_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1, 4),
    _CronJobMailList_Type()
)
cronJobMailList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobMailList.setStatus("current")
_CronJobAccessLevel_Type = DisplayString
_CronJobAccessLevel_Object = MibTableColumn
cronJobAccessLevel = _CronJobAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 2, 1, 5),
    _CronJobAccessLevel_Type()
)
cronJobAccessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cronJobAccessLevel.setStatus("current")
_AtJobNumber_Type = Integer32
_AtJobNumber_Object = MibScalar
atJobNumber = _AtJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 3),
    _AtJobNumber_Type()
)
atJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobNumber.setStatus("current")
_AtJobTable_Object = MibTable
atJobTable = _AtJobTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4)
)
if mibBuilder.loadTexts:
    atJobTable.setStatus("current")
_AtJobEntry_Object = MibTableRow
atJobEntry = _AtJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1)
)
atJobEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "atJobIndex"),
)
if mibBuilder.loadTexts:
    atJobEntry.setStatus("current")


class _AtJobIndex_Type(Integer32):
    """Custom type atJobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_AtJobIndex_Type.__name__ = "Integer32"
_AtJobIndex_Object = MibTableColumn
atJobIndex = _AtJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1, 1),
    _AtJobIndex_Type()
)
atJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobIndex.setStatus("current")
_AtJobRunTime_Type = DisplayString
_AtJobRunTime_Object = MibTableColumn
atJobRunTime = _AtJobRunTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1, 2),
    _AtJobRunTime_Type()
)
atJobRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobRunTime.setStatus("current")
_AtJobCommandList_Type = DisplayString
_AtJobCommandList_Object = MibTableColumn
atJobCommandList = _AtJobCommandList_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1, 3),
    _AtJobCommandList_Type()
)
atJobCommandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobCommandList.setStatus("current")
_AtJobMailList_Type = DisplayString
_AtJobMailList_Object = MibTableColumn
atJobMailList = _AtJobMailList_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1, 4),
    _AtJobMailList_Type()
)
atJobMailList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobMailList.setStatus("current")
_AtJobAccessLevel_Type = DisplayString
_AtJobAccessLevel_Object = MibTableColumn
atJobAccessLevel = _AtJobAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 8, 4, 1, 5),
    _AtJobAccessLevel_Type()
)
atJobAccessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atJobAccessLevel.setStatus("current")
_MgmntStats_ObjectIdentity = ObjectIdentity
mgmntStats = _MgmntStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9)
)
_WebMgmntStats_ObjectIdentity = ObjectIdentity
webMgmntStats = _WebMgmntStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1)
)
_WebCurrActiveSessions_Type = Counter64
_WebCurrActiveSessions_Object = MibScalar
webCurrActiveSessions = _WebCurrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 1),
    _WebCurrActiveSessions_Type()
)
webCurrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCurrActiveSessions.setStatus("obsolete")
_WebMaxSessions_Type = Counter64
_WebMaxSessions_Object = MibScalar
webMaxSessions = _WebMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 2),
    _WebMaxSessions_Type()
)
webMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webMaxSessions.setStatus("obsolete")
_WebTotalSessions_Type = Counter64
_WebTotalSessions_Object = MibScalar
webTotalSessions = _WebTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 3),
    _WebTotalSessions_Type()
)
webTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webTotalSessions.setStatus("obsolete")
_WebRejectedSessions_Type = Counter64
_WebRejectedSessions_Object = MibScalar
webRejectedSessions = _WebRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 4),
    _WebRejectedSessions_Type()
)
webRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webRejectedSessions.setStatus("obsolete")
_WebTotalFramesTX_Type = Counter64
_WebTotalFramesTX_Object = MibScalar
webTotalFramesTX = _WebTotalFramesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 5),
    _WebTotalFramesTX_Type()
)
webTotalFramesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webTotalFramesTX.setStatus("obsolete")
_WebTotalFramesRX_Type = Counter64
_WebTotalFramesRX_Object = MibScalar
webTotalFramesRX = _WebTotalFramesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 6),
    _WebTotalFramesRX_Type()
)
webTotalFramesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webTotalFramesRX.setStatus("obsolete")
_WebTotalBytesTX_Type = Counter64
_WebTotalBytesTX_Object = MibScalar
webTotalBytesTX = _WebTotalBytesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 7),
    _WebTotalBytesTX_Type()
)
webTotalBytesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webTotalBytesTX.setStatus("obsolete")
_WebTotalBytesRX_Type = Counter64
_WebTotalBytesRX_Object = MibScalar
webTotalBytesRX = _WebTotalBytesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 1, 8),
    _WebTotalBytesRX_Type()
)
webTotalBytesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webTotalBytesRX.setStatus("obsolete")
_SictrlMgmntStats_ObjectIdentity = ObjectIdentity
sictrlMgmntStats = _SictrlMgmntStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2)
)
_SictrlCurrActiveSessions_Type = Counter64
_SictrlCurrActiveSessions_Object = MibScalar
sictrlCurrActiveSessions = _SictrlCurrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 1),
    _SictrlCurrActiveSessions_Type()
)
sictrlCurrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlCurrActiveSessions.setStatus("obsolete")
_SictrlMaxSessions_Type = Counter64
_SictrlMaxSessions_Object = MibScalar
sictrlMaxSessions = _SictrlMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 2),
    _SictrlMaxSessions_Type()
)
sictrlMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlMaxSessions.setStatus("obsolete")
_SictrlTotalSessions_Type = Counter64
_SictrlTotalSessions_Object = MibScalar
sictrlTotalSessions = _SictrlTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 3),
    _SictrlTotalSessions_Type()
)
sictrlTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlTotalSessions.setStatus("obsolete")
_SictrlRejectedSessions_Type = Counter64
_SictrlRejectedSessions_Object = MibScalar
sictrlRejectedSessions = _SictrlRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 4),
    _SictrlRejectedSessions_Type()
)
sictrlRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlRejectedSessions.setStatus("obsolete")
_SictrlTotalFramesTX_Type = Counter64
_SictrlTotalFramesTX_Object = MibScalar
sictrlTotalFramesTX = _SictrlTotalFramesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 5),
    _SictrlTotalFramesTX_Type()
)
sictrlTotalFramesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlTotalFramesTX.setStatus("obsolete")
_SictrlTotalFramesRX_Type = Counter64
_SictrlTotalFramesRX_Object = MibScalar
sictrlTotalFramesRX = _SictrlTotalFramesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 6),
    _SictrlTotalFramesRX_Type()
)
sictrlTotalFramesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlTotalFramesRX.setStatus("obsolete")
_SictrlTotalBytesTX_Type = Counter64
_SictrlTotalBytesTX_Object = MibScalar
sictrlTotalBytesTX = _SictrlTotalBytesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 7),
    _SictrlTotalBytesTX_Type()
)
sictrlTotalBytesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlTotalBytesTX.setStatus("obsolete")
_SictrlTotalBytesRX_Type = Counter64
_SictrlTotalBytesRX_Object = MibScalar
sictrlTotalBytesRX = _SictrlTotalBytesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 2, 8),
    _SictrlTotalBytesRX_Type()
)
sictrlTotalBytesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sictrlTotalBytesRX.setStatus("obsolete")
_TelnetMgmntStats_ObjectIdentity = ObjectIdentity
telnetMgmntStats = _TelnetMgmntStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3)
)
_TelnetCurrActiveSessions_Type = Counter64
_TelnetCurrActiveSessions_Object = MibScalar
telnetCurrActiveSessions = _TelnetCurrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 1),
    _TelnetCurrActiveSessions_Type()
)
telnetCurrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetCurrActiveSessions.setStatus("current")
_TelnetMaxSessions_Type = Counter64
_TelnetMaxSessions_Object = MibScalar
telnetMaxSessions = _TelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 2),
    _TelnetMaxSessions_Type()
)
telnetMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetMaxSessions.setStatus("current")
_TelnetTotalSessions_Type = Counter64
_TelnetTotalSessions_Object = MibScalar
telnetTotalSessions = _TelnetTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 3),
    _TelnetTotalSessions_Type()
)
telnetTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetTotalSessions.setStatus("current")
_TelnetRejectedSessions_Type = Counter64
_TelnetRejectedSessions_Object = MibScalar
telnetRejectedSessions = _TelnetRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 4),
    _TelnetRejectedSessions_Type()
)
telnetRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetRejectedSessions.setStatus("current")
_TelnetTotalFramesTX_Type = Counter64
_TelnetTotalFramesTX_Object = MibScalar
telnetTotalFramesTX = _TelnetTotalFramesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 5),
    _TelnetTotalFramesTX_Type()
)
telnetTotalFramesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetTotalFramesTX.setStatus("current")
_TelnetTotalFramesRX_Type = Counter64
_TelnetTotalFramesRX_Object = MibScalar
telnetTotalFramesRX = _TelnetTotalFramesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 6),
    _TelnetTotalFramesRX_Type()
)
telnetTotalFramesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetTotalFramesRX.setStatus("current")
_TelnetTotalBytesTX_Type = Counter64
_TelnetTotalBytesTX_Object = MibScalar
telnetTotalBytesTX = _TelnetTotalBytesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 7),
    _TelnetTotalBytesTX_Type()
)
telnetTotalBytesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetTotalBytesTX.setStatus("current")
_TelnetTotalBytesRX_Type = Counter64
_TelnetTotalBytesRX_Object = MibScalar
telnetTotalBytesRX = _TelnetTotalBytesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 3, 8),
    _TelnetTotalBytesRX_Type()
)
telnetTotalBytesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetTotalBytesRX.setStatus("current")
_SecureWebMgmntStats_ObjectIdentity = ObjectIdentity
secureWebMgmntStats = _SecureWebMgmntStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4)
)
_SecureWebCurrActiveSessions_Type = Counter64
_SecureWebCurrActiveSessions_Object = MibScalar
secureWebCurrActiveSessions = _SecureWebCurrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 1),
    _SecureWebCurrActiveSessions_Type()
)
secureWebCurrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebCurrActiveSessions.setStatus("obsolete")
_SecureWebMaxSessions_Type = Counter64
_SecureWebMaxSessions_Object = MibScalar
secureWebMaxSessions = _SecureWebMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 2),
    _SecureWebMaxSessions_Type()
)
secureWebMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebMaxSessions.setStatus("obsolete")
_SecureWebTotalSessions_Type = Counter64
_SecureWebTotalSessions_Object = MibScalar
secureWebTotalSessions = _SecureWebTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 3),
    _SecureWebTotalSessions_Type()
)
secureWebTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebTotalSessions.setStatus("obsolete")
_SecureWebRejectedSessions_Type = Counter64
_SecureWebRejectedSessions_Object = MibScalar
secureWebRejectedSessions = _SecureWebRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 4),
    _SecureWebRejectedSessions_Type()
)
secureWebRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebRejectedSessions.setStatus("obsolete")
_SecureWebTotalFramesTX_Type = Counter64
_SecureWebTotalFramesTX_Object = MibScalar
secureWebTotalFramesTX = _SecureWebTotalFramesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 5),
    _SecureWebTotalFramesTX_Type()
)
secureWebTotalFramesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebTotalFramesTX.setStatus("obsolete")
_SecureWebTotalFramesRX_Type = Counter64
_SecureWebTotalFramesRX_Object = MibScalar
secureWebTotalFramesRX = _SecureWebTotalFramesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 6),
    _SecureWebTotalFramesRX_Type()
)
secureWebTotalFramesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebTotalFramesRX.setStatus("obsolete")
_SecureWebTotalBytesTX_Type = Counter64
_SecureWebTotalBytesTX_Object = MibScalar
secureWebTotalBytesTX = _SecureWebTotalBytesTX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 7),
    _SecureWebTotalBytesTX_Type()
)
secureWebTotalBytesTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebTotalBytesTX.setStatus("obsolete")
_SecureWebTotalBytesRX_Type = Counter64
_SecureWebTotalBytesRX_Object = MibScalar
secureWebTotalBytesRX = _SecureWebTotalBytesRX_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 9, 4, 8),
    _SecureWebTotalBytesRX_Type()
)
secureWebTotalBytesRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureWebTotalBytesRX.setStatus("obsolete")
_HwFlowControl_ObjectIdentity = ObjectIdentity
hwFlowControl = _HwFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10)
)
_HwFlowNumber_Type = Integer32
_HwFlowNumber_Object = MibScalar
hwFlowNumber = _HwFlowNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 1),
    _HwFlowNumber_Type()
)
hwFlowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlowNumber.setStatus("obsolete")
_HwFlowTable_Object = MibTable
hwFlowTable = _HwFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    hwFlowTable.setStatus("obsolete")
_HwFlowEntry_Object = MibTableRow
hwFlowEntry = _HwFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 2, 1)
)
hwFlowEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "hwFlowIndex"),
)
if mibBuilder.loadTexts:
    hwFlowEntry.setStatus("obsolete")


class _HwFlowIndex_Type(Integer32):
    """Custom type hwFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 3),
          ("fsb", 2),
          ("tcp", 1))
    )


_HwFlowIndex_Type.__name__ = "Integer32"
_HwFlowIndex_Object = MibTableColumn
hwFlowIndex = _HwFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 2, 1, 1),
    _HwFlowIndex_Type()
)
hwFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlowIndex.setStatus("obsolete")


class _HwFlowDebug_Type(Integer32):
    """Custom type hwFlowDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwFlowDebug_Type.__name__ = "Integer32"
_HwFlowDebug_Object = MibTableColumn
hwFlowDebug = _HwFlowDebug_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 2, 1, 2),
    _HwFlowDebug_Type()
)
hwFlowDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlowDebug.setStatus("obsolete")


class _HwFlowConsole_Type(Integer32):
    """Custom type hwFlowConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwFlowConsole_Type.__name__ = "Integer32"
_HwFlowConsole_Object = MibTableColumn
hwFlowConsole = _HwFlowConsole_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 5, 10, 2, 1, 3),
    _HwFlowConsole_Type()
)
hwFlowConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlowConsole.setStatus("obsolete")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6)
)
_Utilization_ObjectIdentity = ObjectIdentity
utilization = _Utilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1)
)
_CpuUtilizationNumber_Type = Integer32
_CpuUtilizationNumber_Object = MibScalar
cpuUtilizationNumber = _CpuUtilizationNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 1),
    _CpuUtilizationNumber_Type()
)
cpuUtilizationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilizationNumber.setStatus("current")
_CpuUtilizationTable_Object = MibTable
cpuUtilizationTable = _CpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cpuUtilizationTable.setStatus("current")
_CpuUtilizationEntry_Object = MibTableRow
cpuUtilizationEntry = _CpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 2, 1)
)
cpuUtilizationEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "cpuUtilizationCnIndex"),
    (0, "BLUEARC-SERVER-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuUtilizationEntry.setStatus("current")


class _CpuUtilizationCnIndex_Type(Unsigned32):
    """Custom type cpuUtilizationCnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpuUtilizationCnIndex_Type.__name__ = "Unsigned32"
_CpuUtilizationCnIndex_Object = MibTableColumn
cpuUtilizationCnIndex = _CpuUtilizationCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 2, 1, 1),
    _CpuUtilizationCnIndex_Type()
)
cpuUtilizationCnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilizationCnIndex.setStatus("current")
_CpuIndex_Type = Unsigned32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 2, 1, 2),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuUtilization_Type = Unsigned32
_CpuUtilization_Object = MibTableColumn
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 2, 1, 3),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_FpgaUtilizationNumber_Type = Integer32
_FpgaUtilizationNumber_Object = MibScalar
fpgaUtilizationNumber = _FpgaUtilizationNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 3),
    _FpgaUtilizationNumber_Type()
)
fpgaUtilizationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaUtilizationNumber.setStatus("current")
_FpgaUtilizationTable_Object = MibTable
fpgaUtilizationTable = _FpgaUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    fpgaUtilizationTable.setStatus("current")
_FpgaUtilizationEntry_Object = MibTableRow
fpgaUtilizationEntry = _FpgaUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4, 1)
)
fpgaUtilizationEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fpgaUtilizationCnIndex"),
    (0, "BLUEARC-SERVER-MIB", "fpgaUtilizationFpgaIndex"),
)
if mibBuilder.loadTexts:
    fpgaUtilizationEntry.setStatus("current")


class _FpgaUtilizationCnIndex_Type(Unsigned32):
    """Custom type fpgaUtilizationCnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FpgaUtilizationCnIndex_Type.__name__ = "Unsigned32"
_FpgaUtilizationCnIndex_Object = MibTableColumn
fpgaUtilizationCnIndex = _FpgaUtilizationCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4, 1, 1),
    _FpgaUtilizationCnIndex_Type()
)
fpgaUtilizationCnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaUtilizationCnIndex.setStatus("current")
_FpgaUtilizationFpgaIndex_Type = Unsigned32
_FpgaUtilizationFpgaIndex_Object = MibTableColumn
fpgaUtilizationFpgaIndex = _FpgaUtilizationFpgaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4, 1, 2),
    _FpgaUtilizationFpgaIndex_Type()
)
fpgaUtilizationFpgaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaUtilizationFpgaIndex.setStatus("current")
_FpgaUtilizationFpgaName_Type = DisplayString
_FpgaUtilizationFpgaName_Object = MibTableColumn
fpgaUtilizationFpgaName = _FpgaUtilizationFpgaName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4, 1, 3),
    _FpgaUtilizationFpgaName_Type()
)
fpgaUtilizationFpgaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaUtilizationFpgaName.setStatus("current")
_FpgaUtilization_Type = Unsigned32
_FpgaUtilization_Object = MibTableColumn
fpgaUtilization = _FpgaUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 1, 4, 1, 4),
    _FpgaUtilization_Type()
)
fpgaUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaUtilization.setStatus("current")
_SystemDriveStats_ObjectIdentity = ObjectIdentity
systemDriveStats = _SystemDriveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2)
)
_SystemDriveStatsNumber_Type = Integer32
_SystemDriveStatsNumber_Object = MibScalar
systemDriveStatsNumber = _SystemDriveStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 1),
    _SystemDriveStatsNumber_Type()
)
systemDriveStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDriveStatsNumber.setStatus("current")
_SystemDriveStatsTable_Object = MibTable
systemDriveStatsTable = _SystemDriveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    systemDriveStatsTable.setStatus("current")
_SystemDriveStatsEntry_Object = MibTableRow
systemDriveStatsEntry = _SystemDriveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1)
)
systemDriveStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "systemDriveStatsCnIndex"),
    (0, "BLUEARC-SERVER-MIB", "systemDriveStatsSdId"),
)
if mibBuilder.loadTexts:
    systemDriveStatsEntry.setStatus("current")


class _SystemDriveStatsCnIndex_Type(Unsigned32):
    """Custom type systemDriveStatsCnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SystemDriveStatsCnIndex_Type.__name__ = "Unsigned32"
_SystemDriveStatsCnIndex_Object = MibTableColumn
systemDriveStatsCnIndex = _SystemDriveStatsCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 1),
    _SystemDriveStatsCnIndex_Type()
)
systemDriveStatsCnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDriveStatsCnIndex.setStatus("current")


class _SystemDriveStatsSdId_Type(Unsigned32):
    """Custom type systemDriveStatsSdId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SystemDriveStatsSdId_Type.__name__ = "Unsigned32"
_SystemDriveStatsSdId_Object = MibTableColumn
systemDriveStatsSdId = _SystemDriveStatsSdId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 2),
    _SystemDriveStatsSdId_Type()
)
systemDriveStatsSdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDriveStatsSdId.setStatus("current")
_CumNonZeroQueuedReadTime_Type = Counter64
_CumNonZeroQueuedReadTime_Object = MibTableColumn
cumNonZeroQueuedReadTime = _CumNonZeroQueuedReadTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 3),
    _CumNonZeroQueuedReadTime_Type()
)
cumNonZeroQueuedReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumNonZeroQueuedReadTime.setStatus("current")
_CumNonZeroQueuedWriteTime_Type = Counter64
_CumNonZeroQueuedWriteTime_Object = MibTableColumn
cumNonZeroQueuedWriteTime = _CumNonZeroQueuedWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 4),
    _CumNonZeroQueuedWriteTime_Type()
)
cumNonZeroQueuedWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumNonZeroQueuedWriteTime.setStatus("current")
_ReadCount_Type = Counter64
_ReadCount_Object = MibTableColumn
readCount = _ReadCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 5),
    _ReadCount_Type()
)
readCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCount.setStatus("current")
_SingleBufferWriteCount_Type = Counter64
_SingleBufferWriteCount_Object = MibTableColumn
singleBufferWriteCount = _SingleBufferWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 6),
    _SingleBufferWriteCount_Type()
)
singleBufferWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    singleBufferWriteCount.setStatus("current")
_StripeWriteCount_Type = Counter64
_StripeWriteCount_Object = MibTableColumn
stripeWriteCount = _StripeWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 7),
    _StripeWriteCount_Type()
)
stripeWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stripeWriteCount.setStatus("current")
_ReadCumLatency_Type = Counter64
_ReadCumLatency_Object = MibTableColumn
readCumLatency = _ReadCumLatency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 8),
    _ReadCumLatency_Type()
)
readCumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCumLatency.setStatus("current")
_OneWriteCumLatency_Type = Counter64
_OneWriteCumLatency_Object = MibTableColumn
oneWriteCumLatency = _OneWriteCumLatency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 9),
    _OneWriteCumLatency_Type()
)
oneWriteCumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oneWriteCumLatency.setStatus("current")
_StripeWriteCumLatency_Type = Counter64
_StripeWriteCumLatency_Object = MibTableColumn
stripeWriteCumLatency = _StripeWriteCumLatency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 2, 2, 1, 10),
    _StripeWriteCumLatency_Type()
)
stripeWriteCumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stripeWriteCumLatency.setStatus("current")
_FileSystemStats_ObjectIdentity = ObjectIdentity
fileSystemStats = _FileSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3)
)
_FileSystemStatsNumber_Type = Integer32
_FileSystemStatsNumber_Object = MibScalar
fileSystemStatsNumber = _FileSystemStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 1),
    _FileSystemStatsNumber_Type()
)
fileSystemStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemStatsNumber.setStatus("current")
_FileSystemStatsTable_Object = MibTable
fileSystemStatsTable = _FileSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    fileSystemStatsTable.setStatus("current")
_FileSystemStatsEntry_Object = MibTableRow
fileSystemStatsEntry = _FileSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1)
)
fileSystemStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fsStatsFsId"),
)
if mibBuilder.loadTexts:
    fileSystemStatsEntry.setStatus("current")


class _FsStatsFsId_Type(Integer32):
    """Custom type fsStatsFsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsStatsFsId_Type.__name__ = "Integer32"
_FsStatsFsId_Object = MibTableColumn
fsStatsFsId = _FsStatsFsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 1),
    _FsStatsFsId_Type()
)
fsStatsFsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatsFsId.setStatus("current")
_FsStatsFsLabel_Type = DisplayString
_FsStatsFsLabel_Object = MibTableColumn
fsStatsFsLabel = _FsStatsFsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 2),
    _FsStatsFsLabel_Type()
)
fsStatsFsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatsFsLabel.setStatus("current")
_FsCapacityTotalUpper_Type = Unsigned32
_FsCapacityTotalUpper_Object = MibTableColumn
fsCapacityTotalUpper = _FsCapacityTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 3),
    _FsCapacityTotalUpper_Type()
)
fsCapacityTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacityTotalUpper.setStatus("current")
_FsCapacityTotalLower_Type = Unsigned32
_FsCapacityTotalLower_Object = MibTableColumn
fsCapacityTotalLower = _FsCapacityTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 4),
    _FsCapacityTotalLower_Type()
)
fsCapacityTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacityTotalLower.setStatus("current")
_FsCapacityUsedUpper_Type = Unsigned32
_FsCapacityUsedUpper_Object = MibTableColumn
fsCapacityUsedUpper = _FsCapacityUsedUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 5),
    _FsCapacityUsedUpper_Type()
)
fsCapacityUsedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacityUsedUpper.setStatus("current")
_FsCapacityUsedLower_Type = Unsigned32
_FsCapacityUsedLower_Object = MibTableColumn
fsCapacityUsedLower = _FsCapacityUsedLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 6),
    _FsCapacityUsedLower_Type()
)
fsCapacityUsedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacityUsedLower.setStatus("current")
_FsCapacitySnapshotUpper_Type = Unsigned32
_FsCapacitySnapshotUpper_Object = MibTableColumn
fsCapacitySnapshotUpper = _FsCapacitySnapshotUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 7),
    _FsCapacitySnapshotUpper_Type()
)
fsCapacitySnapshotUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacitySnapshotUpper.setStatus("current")
_FsCapacitySnapshotLower_Type = Unsigned32
_FsCapacitySnapshotLower_Object = MibTableColumn
fsCapacitySnapshotLower = _FsCapacitySnapshotLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 8),
    _FsCapacitySnapshotLower_Type()
)
fsCapacitySnapshotLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacitySnapshotLower.setStatus("current")
_FsNvramWaitedAllocs_Type = Counter32
_FsNvramWaitedAllocs_Object = MibTableColumn
fsNvramWaitedAllocs = _FsNvramWaitedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 9),
    _FsNvramWaitedAllocs_Type()
)
fsNvramWaitedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNvramWaitedAllocs.setStatus("current")
_FsWriteSmoothing_Type = Unsigned32
_FsWriteSmoothing_Object = MibTableColumn
fsWriteSmoothing = _FsWriteSmoothing_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 2, 1, 10),
    _FsWriteSmoothing_Type()
)
fsWriteSmoothing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWriteSmoothing.setStatus("current")
_FileSystemTierStatsNumber_Type = Integer32
_FileSystemTierStatsNumber_Object = MibScalar
fileSystemTierStatsNumber = _FileSystemTierStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 3),
    _FileSystemTierStatsNumber_Type()
)
fileSystemTierStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemTierStatsNumber.setStatus("current")
_FileSystemTierStatsTable_Object = MibTable
fileSystemTierStatsTable = _FileSystemTierStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    fileSystemTierStatsTable.setStatus("current")
_FsTierStatsEntry_Object = MibTableRow
fsTierStatsEntry = _FsTierStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1)
)
fsTierStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "fsTierStatsFsId"),
    (0, "BLUEARC-SERVER-MIB", "fsTier"),
)
if mibBuilder.loadTexts:
    fsTierStatsEntry.setStatus("current")


class _FsTierStatsFsId_Type(Integer32):
    """Custom type fsTierStatsFsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsTierStatsFsId_Type.__name__ = "Integer32"
_FsTierStatsFsId_Object = MibTableColumn
fsTierStatsFsId = _FsTierStatsFsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 1),
    _FsTierStatsFsId_Type()
)
fsTierStatsFsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierStatsFsId.setStatus("current")
_FsTier_Type = Unsigned32
_FsTier_Object = MibTableColumn
fsTier = _FsTier_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 2),
    _FsTier_Type()
)
fsTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTier.setStatus("current")
_FsTierStatsFsLabel_Type = DisplayString
_FsTierStatsFsLabel_Object = MibTableColumn
fsTierStatsFsLabel = _FsTierStatsFsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 3),
    _FsTierStatsFsLabel_Type()
)
fsTierStatsFsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierStatsFsLabel.setStatus("current")
_FsTierCapacityTotalUpper_Type = Unsigned32
_FsTierCapacityTotalUpper_Object = MibTableColumn
fsTierCapacityTotalUpper = _FsTierCapacityTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 4),
    _FsTierCapacityTotalUpper_Type()
)
fsTierCapacityTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacityTotalUpper.setStatus("current")
_FsTierCapacityTotalLower_Type = Unsigned32
_FsTierCapacityTotalLower_Object = MibTableColumn
fsTierCapacityTotalLower = _FsTierCapacityTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 5),
    _FsTierCapacityTotalLower_Type()
)
fsTierCapacityTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacityTotalLower.setStatus("current")
_FsTierCapacityUsedUpper_Type = Unsigned32
_FsTierCapacityUsedUpper_Object = MibTableColumn
fsTierCapacityUsedUpper = _FsTierCapacityUsedUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 6),
    _FsTierCapacityUsedUpper_Type()
)
fsTierCapacityUsedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacityUsedUpper.setStatus("current")
_FsTierCapacityUsedLower_Type = Unsigned32
_FsTierCapacityUsedLower_Object = MibTableColumn
fsTierCapacityUsedLower = _FsTierCapacityUsedLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 7),
    _FsTierCapacityUsedLower_Type()
)
fsTierCapacityUsedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacityUsedLower.setStatus("current")
_FsTierCapacitySnapshotUpper_Type = Unsigned32
_FsTierCapacitySnapshotUpper_Object = MibTableColumn
fsTierCapacitySnapshotUpper = _FsTierCapacitySnapshotUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 8),
    _FsTierCapacitySnapshotUpper_Type()
)
fsTierCapacitySnapshotUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacitySnapshotUpper.setStatus("current")
_FsTierCapacitySnapshotLower_Type = Unsigned32
_FsTierCapacitySnapshotLower_Object = MibTableColumn
fsTierCapacitySnapshotLower = _FsTierCapacitySnapshotLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 3, 4, 1, 9),
    _FsTierCapacitySnapshotLower_Type()
)
fsTierCapacitySnapshotLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTierCapacitySnapshotLower.setStatus("current")
_SpanStats_ObjectIdentity = ObjectIdentity
spanStats = _SpanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4)
)
_SpanStatsNumber_Type = Integer32
_SpanStatsNumber_Object = MibScalar
spanStatsNumber = _SpanStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 1),
    _SpanStatsNumber_Type()
)
spanStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanStatsNumber.setStatus("current")
_SpanStatsTable_Object = MibTable
spanStatsTable = _SpanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    spanStatsTable.setStatus("current")
_SpanStatsEntry_Object = MibTableRow
spanStatsEntry = _SpanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1)
)
spanStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "spanStatsSpanId"),
)
if mibBuilder.loadTexts:
    spanStatsEntry.setStatus("current")


class _SpanStatsSpanId_Type(Integer32):
    """Custom type spanStatsSpanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanStatsSpanId_Type.__name__ = "Integer32"
_SpanStatsSpanId_Object = MibTableColumn
spanStatsSpanId = _SpanStatsSpanId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 1),
    _SpanStatsSpanId_Type()
)
spanStatsSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanStatsSpanId.setStatus("current")
_SpanLabel_Type = DisplayString
_SpanLabel_Object = MibTableColumn
spanLabel = _SpanLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 2),
    _SpanLabel_Type()
)
spanLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanLabel.setStatus("current")
_SpanCapacityTotalUpper_Type = Unsigned32
_SpanCapacityTotalUpper_Object = MibTableColumn
spanCapacityTotalUpper = _SpanCapacityTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 3),
    _SpanCapacityTotalUpper_Type()
)
spanCapacityTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanCapacityTotalUpper.setStatus("current")
_SpanCapacityTotalLower_Type = Unsigned32
_SpanCapacityTotalLower_Object = MibTableColumn
spanCapacityTotalLower = _SpanCapacityTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 4),
    _SpanCapacityTotalLower_Type()
)
spanCapacityTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanCapacityTotalLower.setStatus("current")
_SpanCapacityUsedUpper_Type = Unsigned32
_SpanCapacityUsedUpper_Object = MibTableColumn
spanCapacityUsedUpper = _SpanCapacityUsedUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 5),
    _SpanCapacityUsedUpper_Type()
)
spanCapacityUsedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanCapacityUsedUpper.setStatus("current")
_SpanCapacityUsedLower_Type = Unsigned32
_SpanCapacityUsedLower_Object = MibTableColumn
spanCapacityUsedLower = _SpanCapacityUsedLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 2, 1, 6),
    _SpanCapacityUsedLower_Type()
)
spanCapacityUsedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanCapacityUsedLower.setStatus("current")
_SpanTierStatsNumber_Type = Integer32
_SpanTierStatsNumber_Object = MibScalar
spanTierStatsNumber = _SpanTierStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 3),
    _SpanTierStatsNumber_Type()
)
spanTierStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierStatsNumber.setStatus("current")
_SpanTierStatsTable_Object = MibTable
spanTierStatsTable = _SpanTierStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4)
)
if mibBuilder.loadTexts:
    spanTierStatsTable.setStatus("current")
_SpanTierStatsEntry_Object = MibTableRow
spanTierStatsEntry = _SpanTierStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1)
)
spanTierStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "spanTierStatsSpanId"),
    (0, "BLUEARC-SERVER-MIB", "spanTier"),
)
if mibBuilder.loadTexts:
    spanTierStatsEntry.setStatus("current")


class _SpanTierStatsSpanId_Type(Integer32):
    """Custom type spanTierStatsSpanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanTierStatsSpanId_Type.__name__ = "Integer32"
_SpanTierStatsSpanId_Object = MibTableColumn
spanTierStatsSpanId = _SpanTierStatsSpanId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 1),
    _SpanTierStatsSpanId_Type()
)
spanTierStatsSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierStatsSpanId.setStatus("current")
_SpanTier_Type = Unsigned32
_SpanTier_Object = MibTableColumn
spanTier = _SpanTier_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 2),
    _SpanTier_Type()
)
spanTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTier.setStatus("current")
_SpanTierLabel_Type = DisplayString
_SpanTierLabel_Object = MibTableColumn
spanTierLabel = _SpanTierLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 3),
    _SpanTierLabel_Type()
)
spanTierLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierLabel.setStatus("current")
_SpanTierCapacityTotalUpper_Type = Unsigned32
_SpanTierCapacityTotalUpper_Object = MibTableColumn
spanTierCapacityTotalUpper = _SpanTierCapacityTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 4),
    _SpanTierCapacityTotalUpper_Type()
)
spanTierCapacityTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierCapacityTotalUpper.setStatus("current")
_SpanTierCapacityTotalLower_Type = Unsigned32
_SpanTierCapacityTotalLower_Object = MibTableColumn
spanTierCapacityTotalLower = _SpanTierCapacityTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 5),
    _SpanTierCapacityTotalLower_Type()
)
spanTierCapacityTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierCapacityTotalLower.setStatus("current")
_SpanTierCapacityUsedUpper_Type = Unsigned32
_SpanTierCapacityUsedUpper_Object = MibTableColumn
spanTierCapacityUsedUpper = _SpanTierCapacityUsedUpper_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 6),
    _SpanTierCapacityUsedUpper_Type()
)
spanTierCapacityUsedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierCapacityUsedUpper.setStatus("current")
_SpanTierCapacityUsedLower_Type = Unsigned32
_SpanTierCapacityUsedLower_Object = MibTableColumn
spanTierCapacityUsedLower = _SpanTierCapacityUsedLower_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 4, 4, 1, 7),
    _SpanTierCapacityUsedLower_Type()
)
spanTierCapacityUsedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanTierCapacityUsedLower.setStatus("current")
_CacheStats_ObjectIdentity = ObjectIdentity
cacheStats = _CacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5)
)
_MetaDataCacheStatsNumber_Type = Integer32
_MetaDataCacheStatsNumber_Object = MibScalar
metaDataCacheStatsNumber = _MetaDataCacheStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 1),
    _MetaDataCacheStatsNumber_Type()
)
metaDataCacheStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCacheStatsNumber.setStatus("current")
_MetaDataCacheStatsTable_Object = MibTable
metaDataCacheStatsTable = _MetaDataCacheStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    metaDataCacheStatsTable.setStatus("current")
_MetaDataCacheStatsEntry_Object = MibTableRow
metaDataCacheStatsEntry = _MetaDataCacheStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1)
)
metaDataCacheStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "metaDataCacheStatsFsId"),
    (0, "BLUEARC-SERVER-MIB", "metaDataCache"),
)
if mibBuilder.loadTexts:
    metaDataCacheStatsEntry.setStatus("current")


class _MetaDataCacheStatsFsId_Type(Integer32):
    """Custom type metaDataCacheStatsFsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MetaDataCacheStatsFsId_Type.__name__ = "Integer32"
_MetaDataCacheStatsFsId_Object = MibTableColumn
metaDataCacheStatsFsId = _MetaDataCacheStatsFsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1, 1),
    _MetaDataCacheStatsFsId_Type()
)
metaDataCacheStatsFsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCacheStatsFsId.setStatus("current")


class _MetaDataCache_Type(Integer32):
    """Custom type metaDataCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fsa", 7),
          ("objIndirectionObject", 6),
          ("objLeaf", 5),
          ("objRoot", 4),
          ("wdir", 2),
          ("wfile", 1),
          ("wtree", 3))
    )


_MetaDataCache_Type.__name__ = "Integer32"
_MetaDataCache_Object = MibTableColumn
metaDataCache = _MetaDataCache_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1, 2),
    _MetaDataCache_Type()
)
metaDataCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCache.setStatus("current")
_MetaDataCacheStatsFsLabel_Type = DisplayString
_MetaDataCacheStatsFsLabel_Object = MibTableColumn
metaDataCacheStatsFsLabel = _MetaDataCacheStatsFsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1, 3),
    _MetaDataCacheStatsFsLabel_Type()
)
metaDataCacheStatsFsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCacheStatsFsLabel.setStatus("current")
_MetaDataCacheStatsHits_Type = Counter32
_MetaDataCacheStatsHits_Object = MibTableColumn
metaDataCacheStatsHits = _MetaDataCacheStatsHits_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1, 4),
    _MetaDataCacheStatsHits_Type()
)
metaDataCacheStatsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCacheStatsHits.setStatus("current")
_MetaDataCacheStatsMisses_Type = Counter32
_MetaDataCacheStatsMisses_Object = MibTableColumn
metaDataCacheStatsMisses = _MetaDataCacheStatsMisses_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 2, 1, 5),
    _MetaDataCacheStatsMisses_Type()
)
metaDataCacheStatsMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaDataCacheStatsMisses.setStatus("current")
_SectorCacheStatsNumber_Type = Integer32
_SectorCacheStatsNumber_Object = MibScalar
sectorCacheStatsNumber = _SectorCacheStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 3),
    _SectorCacheStatsNumber_Type()
)
sectorCacheStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsNumber.setStatus("current")
_SectorCacheStatsTable_Object = MibTable
sectorCacheStatsTable = _SectorCacheStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    sectorCacheStatsTable.setStatus("current")
_SectorCacheStatsEntry_Object = MibTableRow
sectorCacheStatsEntry = _SectorCacheStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1)
)
sectorCacheStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "sectorCacheStatsCnIndex"),
    (0, "BLUEARC-SERVER-MIB", "sectorCacheType"),
)
if mibBuilder.loadTexts:
    sectorCacheStatsEntry.setStatus("current")


class _SectorCacheStatsCnIndex_Type(Unsigned32):
    """Custom type sectorCacheStatsCnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SectorCacheStatsCnIndex_Type.__name__ = "Unsigned32"
_SectorCacheStatsCnIndex_Object = MibTableColumn
sectorCacheStatsCnIndex = _SectorCacheStatsCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 1),
    _SectorCacheStatsCnIndex_Type()
)
sectorCacheStatsCnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsCnIndex.setStatus("current")


class _SectorCacheType_Type(Integer32):
    """Custom type sectorCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readAhead", 2),
          ("write", 3))
    )


_SectorCacheType_Type.__name__ = "Integer32"
_SectorCacheType_Object = MibTableColumn
sectorCacheType = _SectorCacheType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 2),
    _SectorCacheType_Type()
)
sectorCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheType.setStatus("current")
_SectorCacheStatsHitsPSI_Type = Counter32
_SectorCacheStatsHitsPSI_Object = MibTableColumn
sectorCacheStatsHitsPSI = _SectorCacheStatsHitsPSI_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 3),
    _SectorCacheStatsHitsPSI_Type()
)
sectorCacheStatsHitsPSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsHitsPSI.setStatus("current")
_SectorCacheStatsHitsSSI_Type = Counter32
_SectorCacheStatsHitsSSI_Object = MibTableColumn
sectorCacheStatsHitsSSI = _SectorCacheStatsHitsSSI_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 4),
    _SectorCacheStatsHitsSSI_Type()
)
sectorCacheStatsHitsSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsHitsSSI.setStatus("current")
_SectorCacheStatsHitsTotal_Type = Counter32
_SectorCacheStatsHitsTotal_Object = MibTableColumn
sectorCacheStatsHitsTotal = _SectorCacheStatsHitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 5),
    _SectorCacheStatsHitsTotal_Type()
)
sectorCacheStatsHitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsHitsTotal.setStatus("current")
_SectorCacheStatsMissesPSI_Type = Counter32
_SectorCacheStatsMissesPSI_Object = MibTableColumn
sectorCacheStatsMissesPSI = _SectorCacheStatsMissesPSI_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 6),
    _SectorCacheStatsMissesPSI_Type()
)
sectorCacheStatsMissesPSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsMissesPSI.setStatus("current")
_SectorCacheStatsMissesSSI_Type = Counter32
_SectorCacheStatsMissesSSI_Object = MibTableColumn
sectorCacheStatsMissesSSI = _SectorCacheStatsMissesSSI_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 7),
    _SectorCacheStatsMissesSSI_Type()
)
sectorCacheStatsMissesSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsMissesSSI.setStatus("current")
_SectorCacheStatsMissesTotal_Type = Counter32
_SectorCacheStatsMissesTotal_Object = MibTableColumn
sectorCacheStatsMissesTotal = _SectorCacheStatsMissesTotal_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 5, 4, 1, 8),
    _SectorCacheStatsMissesTotal_Type()
)
sectorCacheStatsMissesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectorCacheStatsMissesTotal.setStatus("current")
_ProtocolStats_ObjectIdentity = ObjectIdentity
protocolStats = _ProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6)
)
_ProtocolStatsNumber_Type = Integer32
_ProtocolStatsNumber_Object = MibScalar
protocolStatsNumber = _ProtocolStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 1),
    _ProtocolStatsNumber_Type()
)
protocolStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolStatsNumber.setStatus("current")
_ProtocolStatsTable_Object = MibTable
protocolStatsTable = _ProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    protocolStatsTable.setStatus("current")
_ProtocolStatsEntry_Object = MibTableRow
protocolStatsEntry = _ProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1)
)
protocolStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "protStatsFsId"),
    (0, "BLUEARC-SERVER-MIB", "protStatsFlavor"),
    (0, "BLUEARC-SERVER-MIB", "protStatsOpCode"),
)
if mibBuilder.loadTexts:
    protocolStatsEntry.setStatus("current")


class _ProtStatsFsId_Type(Integer32):
    """Custom type protStatsFsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ProtStatsFsId_Type.__name__ = "Integer32"
_ProtStatsFsId_Object = MibTableColumn
protStatsFsId = _ProtStatsFsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 1),
    _ProtStatsFsId_Type()
)
protStatsFsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protStatsFsId.setStatus("current")


class _ProtStatsFlavor_Type(Integer32):
    """Custom type protStatsFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("CIFS", 1),
          ("NFS", 0))
    )


_ProtStatsFlavor_Type.__name__ = "Integer32"
_ProtStatsFlavor_Object = MibTableColumn
protStatsFlavor = _ProtStatsFlavor_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 2),
    _ProtStatsFlavor_Type()
)
protStatsFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protStatsFlavor.setStatus("current")
_ProtStatsOpCode_Type = Unsigned32
_ProtStatsOpCode_Object = MibTableColumn
protStatsOpCode = _ProtStatsOpCode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 3),
    _ProtStatsOpCode_Type()
)
protStatsOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protStatsOpCode.setStatus("current")
_ProtStatsFsLabel_Type = DisplayString
_ProtStatsFsLabel_Object = MibTableColumn
protStatsFsLabel = _ProtStatsFsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 4),
    _ProtStatsFsLabel_Type()
)
protStatsFsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protStatsFsLabel.setStatus("current")
_ProtStatsOpCodeName_Type = DisplayString
_ProtStatsOpCodeName_Object = MibTableColumn
protStatsOpCodeName = _ProtStatsOpCodeName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 5),
    _ProtStatsOpCodeName_Type()
)
protStatsOpCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protStatsOpCodeName.setStatus("current")
_ProtOpCount_Type = Counter64
_ProtOpCount_Object = MibTableColumn
protOpCount = _ProtOpCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 6),
    _ProtOpCount_Type()
)
protOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protOpCount.setStatus("current")
_ProtCumulativeLatency_Type = Counter64
_ProtCumulativeLatency_Object = MibTableColumn
protCumulativeLatency = _ProtCumulativeLatency_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 2, 1, 7),
    _ProtCumulativeLatency_Type()
)
protCumulativeLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protCumulativeLatency.setStatus("current")
_ProtocolXferStatsNumber_Type = Integer32
_ProtocolXferStatsNumber_Object = MibScalar
protocolXferStatsNumber = _ProtocolXferStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 7),
    _ProtocolXferStatsNumber_Type()
)
protocolXferStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsNumber.setStatus("current")
_ProtocolXferStatsTable_Object = MibTable
protocolXferStatsTable = _ProtocolXferStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8)
)
if mibBuilder.loadTexts:
    protocolXferStatsTable.setStatus("current")
_ProtocolXferStatsEntry_Object = MibTableRow
protocolXferStatsEntry = _ProtocolXferStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1)
)
protocolXferStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "protocolXferStatsFsId"),
    (0, "BLUEARC-SERVER-MIB", "protocolXferStatsFlavor"),
)
if mibBuilder.loadTexts:
    protocolXferStatsEntry.setStatus("current")


class _ProtocolXferStatsFsId_Type(Integer32):
    """Custom type protocolXferStatsFsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ProtocolXferStatsFsId_Type.__name__ = "Integer32"
_ProtocolXferStatsFsId_Object = MibTableColumn
protocolXferStatsFsId = _ProtocolXferStatsFsId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1, 1),
    _ProtocolXferStatsFsId_Type()
)
protocolXferStatsFsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsFsId.setStatus("current")


class _ProtocolXferStatsFlavor_Type(Integer32):
    """Custom type protocolXferStatsFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("CIFS", 1),
          ("NFS", 0))
    )


_ProtocolXferStatsFlavor_Type.__name__ = "Integer32"
_ProtocolXferStatsFlavor_Object = MibTableColumn
protocolXferStatsFlavor = _ProtocolXferStatsFlavor_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1, 2),
    _ProtocolXferStatsFlavor_Type()
)
protocolXferStatsFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsFlavor.setStatus("current")
_ProtocolXferStatsFsLabel_Type = DisplayString
_ProtocolXferStatsFsLabel_Object = MibTableColumn
protocolXferStatsFsLabel = _ProtocolXferStatsFsLabel_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1, 3),
    _ProtocolXferStatsFsLabel_Type()
)
protocolXferStatsFsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsFsLabel.setStatus("current")
_ProtocolXferStatsBytesRead_Type = Counter64
_ProtocolXferStatsBytesRead_Object = MibTableColumn
protocolXferStatsBytesRead = _ProtocolXferStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1, 4),
    _ProtocolXferStatsBytesRead_Type()
)
protocolXferStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsBytesRead.setStatus("current")
_ProtocolXferStatsBytesWritten_Type = Counter64
_ProtocolXferStatsBytesWritten_Object = MibTableColumn
protocolXferStatsBytesWritten = _ProtocolXferStatsBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 6, 8, 1, 5),
    _ProtocolXferStatsBytesWritten_Type()
)
protocolXferStatsBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolXferStatsBytesWritten.setStatus("current")
_ClusterStats_ObjectIdentity = ObjectIdentity
clusterStats = _ClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7)
)
_IntraClusterPortErrorNumber_Type = Integer32
_IntraClusterPortErrorNumber_Object = MibScalar
intraClusterPortErrorNumber = _IntraClusterPortErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 1),
    _IntraClusterPortErrorNumber_Type()
)
intraClusterPortErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intraClusterPortErrorNumber.setStatus("current")
_IntraClusterPortErrorTable_Object = MibTable
intraClusterPortErrorTable = _IntraClusterPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    intraClusterPortErrorTable.setStatus("current")
_IntraClusterPortErrorEntry_Object = MibTableRow
intraClusterPortErrorEntry = _IntraClusterPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2, 1)
)
intraClusterPortErrorEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "intraClusterPortErrsCnId"),
)
if mibBuilder.loadTexts:
    intraClusterPortErrorEntry.setStatus("current")


class _IntraClusterPortErrsCnId_Type(Unsigned32):
    """Custom type intraClusterPortErrsCnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IntraClusterPortErrsCnId_Type.__name__ = "Unsigned32"
_IntraClusterPortErrsCnId_Object = MibTableColumn
intraClusterPortErrsCnId = _IntraClusterPortErrsCnId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2, 1, 1),
    _IntraClusterPortErrsCnId_Type()
)
intraClusterPortErrsCnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intraClusterPortErrsCnId.setStatus("current")
_MirroringRetransmits_Type = Counter64
_MirroringRetransmits_Object = MibTableColumn
mirroringRetransmits = _MirroringRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2, 1, 2),
    _MirroringRetransmits_Type()
)
mirroringRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirroringRetransmits.setStatus("current")
_CnsRetransmits_Type = Counter64
_CnsRetransmits_Object = MibTableColumn
cnsRetransmits = _CnsRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2, 1, 3),
    _CnsRetransmits_Type()
)
cnsRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsRetransmits.setStatus("current")
_TotalRetransmits_Type = Counter64
_TotalRetransmits_Object = MibTableColumn
totalRetransmits = _TotalRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 2, 1, 4),
    _TotalRetransmits_Type()
)
totalRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRetransmits.setStatus("current")
_ClusterNodeStatsNumber_Type = Integer32
_ClusterNodeStatsNumber_Object = MibScalar
clusterNodeStatsNumber = _ClusterNodeStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 3),
    _ClusterNodeStatsNumber_Type()
)
clusterNodeStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeStatsNumber.setStatus("current")
_ClusterNodeStatsTable_Object = MibTable
clusterNodeStatsTable = _ClusterNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 4)
)
if mibBuilder.loadTexts:
    clusterNodeStatsTable.setStatus("current")
_ClusterNodeStatsEntry_Object = MibTableRow
clusterNodeStatsEntry = _ClusterNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 4, 1)
)
clusterNodeStatsEntry.setIndexNames(
    (0, "BLUEARC-SERVER-MIB", "clusterNodeStatsCnId"),
)
if mibBuilder.loadTexts:
    clusterNodeStatsEntry.setStatus("current")


class _ClusterNodeStatsCnId_Type(Unsigned32):
    """Custom type clusterNodeStatsCnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClusterNodeStatsCnId_Type.__name__ = "Unsigned32"
_ClusterNodeStatsCnId_Object = MibTableColumn
clusterNodeStatsCnId = _ClusterNodeStatsCnId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 4, 1, 1),
    _ClusterNodeStatsCnId_Type()
)
clusterNodeStatsCnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeStatsCnId.setStatus("current")
_RunningBossockFibers_Type = Unsigned32
_RunningBossockFibers_Object = MibTableColumn
runningBossockFibers = _RunningBossockFibers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 1, 1, 6, 7, 4, 1, 2),
    _RunningBossockFibers_Type()
)
runningBossockFibers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runningBossockFibers.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUEARC-SERVER-MIB",
    **{"blueArc": blueArc,
       "blueArcPrivate": blueArcPrivate,
       "blueArcServer": blueArcServer,
       "blueArcServerObjs": blueArcServerObjs,
       "sys": sys,
       "powerUnits": powerUnits,
       "puConfigNumber": puConfigNumber,
       "puConfigTable": puConfigTable,
       "puConfigEntry": puConfigEntry,
       "puConfigIndex": puConfigIndex,
       "puConfigShutdownEnabled": puConfigShutdownEnabled,
       "puConfigShutdownInterval": puConfigShutdownInterval,
       "puConfigShutdownRemainingLife": puConfigShutdownRemainingLife,
       "puConfigCommsOK": puConfigCommsOK,
       "puConfigCommsEverOK": puConfigCommsEverOK,
       "puStatusNumber": puStatusNumber,
       "puStatusTable": puStatusTable,
       "puStatusEntry": puStatusEntry,
       "puStatusIndex": puStatusIndex,
       "puStatusModel": puStatusModel,
       "puStatusSerialNumber": puStatusSerialNumber,
       "puStatusManufactureDate": puStatusManufactureDate,
       "puStatusBatteryReplaceDate": puStatusBatteryReplaceDate,
       "puStatusUpperTransferVoltage": puStatusUpperTransferVoltage,
       "puStatusLowerTransferVoltage": puStatusLowerTransferVoltage,
       "puStatusSensitivity": puStatusSensitivity,
       "puStatusLowBatteryInterval": puStatusLowBatteryInterval,
       "puStatusAlarmSetting": puStatusAlarmSetting,
       "puStatusCalibrating": puStatusCalibrating,
       "puStatusSleeping": puStatusSleeping,
       "puStatusOnline": puStatusOnline,
       "puStatusOnBattery": puStatusOnBattery,
       "puStatusBatteryAlmostUsedUp": puStatusBatteryAlmostUsedUp,
       "puStatusChangeBattery": puStatusChangeBattery,
       "puStatsNumber": puStatsNumber,
       "puStatsTable": puStatsTable,
       "puStatsEntry": puStatsEntry,
       "puStatsIndex": puStatsIndex,
       "puStatsBatteryCharge": puStatsBatteryCharge,
       "puStatsLoad": puStatsLoad,
       "puStatsFrequency": puStatsFrequency,
       "puStatsLineVoltage": puStatsLineVoltage,
       "puStatsOutputVoltage": puStatsOutputVoltage,
       "puStatsBatteryVoltage": puStatsBatteryVoltage,
       "puStatsTemperatureC": puStatsTemperatureC,
       "puStatsTemperatureF": puStatsTemperatureF,
       "puStatsLineMininumVoltage": puStatsLineMininumVoltage,
       "puStatsLineMaximumVoltage": puStatsLineMaximumVoltage,
       "puStatsRemainingRunTime": puStatsRemainingRunTime,
       "puConfigurationCount": puConfigurationCount,
       "puConfigurationTable": puConfigurationTable,
       "puConfigurationEntry": puConfigurationEntry,
       "puConfigurationIndex": puConfigurationIndex,
       "puConfigurationUserName": puConfigurationUserName,
       "puConfigurationMonitoringEnabled": puConfigurationMonitoringEnabled,
       "puConfigurationShutdownOnBattery": puConfigurationShutdownOnBattery,
       "puConfigurationShutdownOnRuntime": puConfigurationShutdownOnRuntime,
       "puConfigurationShutdownOnLowBattery": puConfigurationShutdownOnLowBattery,
       "puConfigurationOnBatteryTolerance": puConfigurationOnBatteryTolerance,
       "puConfigurationCommsOK": puConfigurationCommsOK,
       "puConfigurationCommsEverOK": puConfigurationCommsEverOK,
       "puCurrentStatusCount": puCurrentStatusCount,
       "puCurrentStatusTable": puCurrentStatusTable,
       "puCurrentStatusEntry": puCurrentStatusEntry,
       "puCurrentStatusIndex": puCurrentStatusIndex,
       "puCurrentStatusModel": puCurrentStatusModel,
       "puCurrentStatusSerialNumber": puCurrentStatusSerialNumber,
       "puCurrentStatusManufactureDate": puCurrentStatusManufactureDate,
       "puCurrentStatusBatteryReplacedDate": puCurrentStatusBatteryReplacedDate,
       "puCurrentStatusUpperTransferVoltage": puCurrentStatusUpperTransferVoltage,
       "puCurrentStatusLowerTransferVoltage": puCurrentStatusLowerTransferVoltage,
       "puCurrentStatusSensitivity": puCurrentStatusSensitivity,
       "puCurrentStatusLowBatteryInterval": puCurrentStatusLowBatteryInterval,
       "puCurrentStatusAlarmSetting": puCurrentStatusAlarmSetting,
       "puCurrentStatusCalibrating": puCurrentStatusCalibrating,
       "puCurrentStatusSleeping": puCurrentStatusSleeping,
       "puCurrentStatusSmartTrim": puCurrentStatusSmartTrim,
       "puCurrentStatusSmartBoost": puCurrentStatusSmartBoost,
       "puCurrentStatusOnline": puCurrentStatusOnline,
       "puCurrentStatusOnBattery": puCurrentStatusOnBattery,
       "puCurrentStatusOverload": puCurrentStatusOverload,
       "puCurrentStatusBatteryAlmostUsedUp": puCurrentStatusBatteryAlmostUsedUp,
       "puCurrentStatusChangeBattery": puCurrentStatusChangeBattery,
       "puStatisticsCount": puStatisticsCount,
       "puStatisticsTable": puStatisticsTable,
       "puStatisticsEntry": puStatisticsEntry,
       "puStatisticsIndex": puStatisticsIndex,
       "puStatisticsBatteryCharge": puStatisticsBatteryCharge,
       "puStatisticsLoad": puStatisticsLoad,
       "puStatisticsFrequency": puStatisticsFrequency,
       "puStatisticsLineVoltage": puStatisticsLineVoltage,
       "puStatisticsOutputVoltage": puStatisticsOutputVoltage,
       "puStatisticsBatteryVoltage": puStatisticsBatteryVoltage,
       "puStatisticsTemperatureC": puStatisticsTemperatureC,
       "puStatisticsTemperatureF": puStatisticsTemperatureF,
       "puStatisticsLineMininumVoltage": puStatisticsLineMininumVoltage,
       "puStatisticsLineMaximumVoltage": puStatisticsLineMaximumVoltage,
       "puStatisticsRemainingRunTime": puStatisticsRemainingRunTime,
       "server": server,
       "environment": environment,
       "sensorNumber": sensorNumber,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorSpeedStatus": sensorSpeedStatus,
       "sensorSpeedReading": sensorSpeedReading,
       "sensorTempStatus": sensorTempStatus,
       "sensorTempCReading": sensorTempCReading,
       "sensorTempFReading": sensorTempFReading,
       "psuOneStatus": psuOneStatus,
       "psuTwoStatus": psuTwoStatus,
       "opsPerSecond": opsPerSecond,
       "fileSystemLoadClient": fileSystemLoadClient,
       "fileSystemLoadSystem": fileSystemLoadSystem,
       "temperatureSensorNumber": temperatureSensorNumber,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorClusterNode": temperatureSensorClusterNode,
       "temperatureSensorIndex": temperatureSensorIndex,
       "temperatureSensorStatus": temperatureSensorStatus,
       "temperatureSensorCReading": temperatureSensorCReading,
       "temperatureSensorFReading": temperatureSensorFReading,
       "fanNumber": fanNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanClusterNode": fanClusterNode,
       "fanIndex": fanIndex,
       "fanFittedStatus": fanFittedStatus,
       "fanSpeedStatus": fanSpeedStatus,
       "fanSpeed": fanSpeed,
       "psuNumber": psuNumber,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuClusterNode": psuClusterNode,
       "psuIndex": psuIndex,
       "psuStatus": psuStatus,
       "locale": locale,
       "serverDate": serverDate,
       "serverTime": serverTime,
       "utcOffset": utcOffset,
       "daylightSavings": daylightSavings,
       "ntpServerNumber": ntpServerNumber,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerHost": ntpServerHost,
       "failover": failover,
       "failoverConfigStatus": failoverConfigStatus,
       "failoverPrimaryName": failoverPrimaryName,
       "failoverSystemName": failoverSystemName,
       "failoverSecondaryName": failoverSecondaryName,
       "failoverPrimaryIpAddr": failoverPrimaryIpAddr,
       "failoverSystemIpAddr": failoverSystemIpAddr,
       "failoverSecondaryIpAddr": failoverSecondaryIpAddr,
       "failoverPrimaryStatus": failoverPrimaryStatus,
       "failoverSecondaryStatus": failoverSecondaryStatus,
       "cache": cache,
       "sectorCache": sectorCache,
       "sectorCacheMode": sectorCacheMode,
       "sectorCacheDirtyPageWtmk": sectorCacheDirtyPageWtmk,
       "sectorCacheDirtyPageTimeout": sectorCacheDirtyPageTimeout,
       "fileSysCache": fileSysCache,
       "fileSysCacheMode": fileSysCacheMode,
       "fileSysTransactionLogging": fileSysTransactionLogging,
       "fileSysCacheTimeout": fileSysCacheTimeout,
       "fileSysUpdateLastAccess": fileSysUpdateLastAccess,
       "clustering": clustering,
       "clusterName": clusterName,
       "clusterUuid": clusterUuid,
       "clusterConfig": clusterConfig,
       "clusterQuorumDeviceName": clusterQuorumDeviceName,
       "clusterQuorumDeviceIpAddr": clusterQuorumDeviceIpAddr,
       "clusterQuorumDeviceOwnedByPNode": clusterQuorumDeviceOwnedByPNode,
       "clusterQuorumDeviceStatus": clusterQuorumDeviceStatus,
       "clusterPNodeNumber": clusterPNodeNumber,
       "clusterPNodeTable": clusterPNodeTable,
       "clusterPNodeEntry": clusterPNodeEntry,
       "clusterPNodeId": clusterPNodeId,
       "clusterPNodeName": clusterPNodeName,
       "clusterPNodeIpAddr": clusterPNodeIpAddr,
       "clusterPNodeStatus": clusterPNodeStatus,
       "clusterVNodeNumber": clusterVNodeNumber,
       "clusterVNodeTable": clusterVNodeTable,
       "clusterVNodeEntry": clusterVNodeEntry,
       "clusterVNodeId": clusterVNodeId,
       "clusterVNodeName": clusterVNodeName,
       "clusterVNodeIpAddr": clusterVNodeIpAddr,
       "clusterVNodeStatus": clusterVNodeStatus,
       "clusterVNodeAdmin": clusterVNodeAdmin,
       "clusterVNodeHostedBy": clusterVNodeHostedBy,
       "serialNumbers": serialNumbers,
       "serialNumberTable": serialNumberTable,
       "serialNumberEntry": serialNumberEntry,
       "componentType": componentType,
       "subComponentType": subComponentType,
       "clusterNode": clusterNode,
       "serialNumber": serialNumber,
       "storage": storage,
       "racks": racks,
       "rackNumber": rackNumber,
       "rackTable": rackTable,
       "rackEntry": rackEntry,
       "rackIndex": rackIndex,
       "rackStatus": rackStatus,
       "rackNumberOfEnclosures": rackNumberOfEnclosures,
       "rackNumberOfPhysicalDrives": rackNumberOfPhysicalDrives,
       "raid": raid,
       "controllers": controllers,
       "raidControllerTable": raidControllerTable,
       "raidControllerEntry": raidControllerEntry,
       "raidControllerRackIndex": raidControllerRackIndex,
       "raidControllerWWN": raidControllerWWN,
       "raidControllerPrimaryStatus": raidControllerPrimaryStatus,
       "raidControllerSecondaryStatus": raidControllerSecondaryStatus,
       "raidControllerManufacturer": raidControllerManufacturer,
       "raidControllerModel": raidControllerModel,
       "raidControllerCacheSize": raidControllerCacheSize,
       "raidControllerConfigTable": raidControllerConfigTable,
       "raidControllerConfigEntry": raidControllerConfigEntry,
       "raidControllerConfigRackIndex": raidControllerConfigRackIndex,
       "raidControllerConfigDRAMSize": raidControllerConfigDRAMSize,
       "raidControllerConfigFlashSize": raidControllerConfigFlashSize,
       "raidControllerConfigNVRSize": raidControllerConfigNVRSize,
       "raidControllerConfigClockSpeed": raidControllerConfigClockSpeed,
       "raidControllerConfigMemAccess": raidControllerConfigMemAccess,
       "raidControllerConfigMemCycle": raidControllerConfigMemCycle,
       "raidControllerConfigPhysicalSectorSize": raidControllerConfigPhysicalSectorSize,
       "raidControllerConfigLogicalSectorSize": raidControllerConfigLogicalSectorSize,
       "raidControllerConfigMaxSystemDrives": raidControllerConfigMaxSystemDrives,
       "raidControllerConfigMaxDrivesPerSystemDrive": raidControllerConfigMaxDrivesPerSystemDrive,
       "raidControllerConfigMaxSpanPerVirtualDrive": raidControllerConfigMaxSpanPerVirtualDrive,
       "raidControllerConfigFirmwareVersion": raidControllerConfigFirmwareVersion,
       "raidControllerConfigFirmwareType": raidControllerConfigFirmwareType,
       "raidControllerConfigFirmwareMajor": raidControllerConfigFirmwareMajor,
       "raidControllerConfigFirmwareMinor": raidControllerConfigFirmwareMinor,
       "raidControllerConfigMaximumCommands": raidControllerConfigMaximumCommands,
       "raidControllerConfigFirmwareBuild": raidControllerConfigFirmwareBuild,
       "raidControllerConfigRebuildRate": raidControllerConfigRebuildRate,
       "raidControllerConfigRebuildUnit": raidControllerConfigRebuildUnit,
       "raidControllerConfigRebuildOn": raidControllerConfigRebuildOn,
       "raidControllerConfigRebuildOff": raidControllerConfigRebuildOff,
       "raidControllerBatteryBackupTable": raidControllerBatteryBackupTable,
       "raidControllerBatteryBackupEntry": raidControllerBatteryBackupEntry,
       "raidControllerBatteryBackupRackIndex": raidControllerBatteryBackupRackIndex,
       "raidControllerBatteryBackupNoSync": raidControllerBatteryBackupNoSync,
       "raidControllerBatteryBackupOutOfSync": raidControllerBatteryBackupOutOfSync,
       "raidControllerBatteryBackupFirstWarning": raidControllerBatteryBackupFirstWarning,
       "raidControllerBatteryBackupSecondWarning": raidControllerBatteryBackupSecondWarning,
       "raidControllerBatteryBackupReconditioning": raidControllerBatteryBackupReconditioning,
       "raidControllerBatteryBackupDischarging": raidControllerBatteryBackupDischarging,
       "raidControllerBatteryBackupFastCharging": raidControllerBatteryBackupFastCharging,
       "raidControllerBatteryBackupLowPower": raidControllerBatteryBackupLowPower,
       "raidControllerBatteryBackupChargePercent": raidControllerBatteryBackupChargePercent,
       "raidControllerBatteryBackupHardwareVersion": raidControllerBatteryBackupHardwareVersion,
       "raidControllerBatteryBackupBatteryType": raidControllerBatteryBackupBatteryType,
       "raidControllerBatteryBackupThreshold": raidControllerBatteryBackupThreshold,
       "raidControllerActiveTaskNumber": raidControllerActiveTaskNumber,
       "raidControllerActiveTaskTable": raidControllerActiveTaskTable,
       "raidControllerActiveTaskEntry": raidControllerActiveTaskEntry,
       "raidControllerActiveTaskRackIndex": raidControllerActiveTaskRackIndex,
       "raidControllerActiveTaskIndex": raidControllerActiveTaskIndex,
       "raidControllerActiveTaskType": raidControllerActiveTaskType,
       "raidControllerActiveTaskLUN": raidControllerActiveTaskLUN,
       "raidControllerActiveTaskPercentageDone": raidControllerActiveTaskPercentageDone,
       "physicalDrives": physicalDrives,
       "physicalDriveNumber": physicalDriveNumber,
       "physicalDriveTable": physicalDriveTable,
       "physicalDriveEntry": physicalDriveEntry,
       "physicalDriveRackIndex": physicalDriveRackIndex,
       "physicalDriveEnclosureIndex": physicalDriveEnclosureIndex,
       "physicalDriveColumnIndex": physicalDriveColumnIndex,
       "physicalDriveRowIndex": physicalDriveRowIndex,
       "physicalDriveStatus": physicalDriveStatus,
       "physicalDriveVendor": physicalDriveVendor,
       "physicalDriveVersion": physicalDriveVersion,
       "physicalDriveCapacity": physicalDriveCapacity,
       "enclosures": enclosures,
       "enclosureFanNumber": enclosureFanNumber,
       "enclosureFanTable": enclosureFanTable,
       "enclosureFanEntry": enclosureFanEntry,
       "enclosureFanRackIndex": enclosureFanRackIndex,
       "enclosureFanEnclosureIndex": enclosureFanEnclosureIndex,
       "enclosureFanFanIndex": enclosureFanFanIndex,
       "enclosureFanStatus": enclosureFanStatus,
       "enclosureFanSpeed": enclosureFanSpeed,
       "enclosureTemperatureNumber": enclosureTemperatureNumber,
       "enclosureTemperatureTable": enclosureTemperatureTable,
       "enclosureTemperatureEntry": enclosureTemperatureEntry,
       "enclosureTemperatureRackIndex": enclosureTemperatureRackIndex,
       "enclosureTemperatureEnclosureIndex": enclosureTemperatureEnclosureIndex,
       "enclosureTemperatureTempIndex": enclosureTemperatureTempIndex,
       "enclosureTemperatureStatus": enclosureTemperatureStatus,
       "enclosureTemperatureOverTemp": enclosureTemperatureOverTemp,
       "enclosureTemperatureTempC": enclosureTemperatureTempC,
       "enclosureTemperatureTempF": enclosureTemperatureTempF,
       "enclosureTemperatureRange": enclosureTemperatureRange,
       "enclosurePSUNumber": enclosurePSUNumber,
       "enclosurePSUTable": enclosurePSUTable,
       "enclosurePSUEntry": enclosurePSUEntry,
       "enclosurePSURackIndex": enclosurePSURackIndex,
       "enclosurePSUEnclosureIndex": enclosurePSUEnclosureIndex,
       "enclosurePSUPSUIndex": enclosurePSUPSUIndex,
       "enclosurePSUStatus": enclosurePSUStatus,
       "enclosureAlarmNumber": enclosureAlarmNumber,
       "enclosureAlarmTable": enclosureAlarmTable,
       "enclosureAlarmEntry": enclosureAlarmEntry,
       "enclosureAlarmRackIndex": enclosureAlarmRackIndex,
       "enclosureAlarmEnclosureIndex": enclosureAlarmEnclosureIndex,
       "enclosureAlarmAlarmIndex": enclosureAlarmAlarmIndex,
       "enclosureAlarmStatus": enclosureAlarmStatus,
       "enclosureAlarmBeeping": enclosureAlarmBeeping,
       "automount": automount,
       "automountNumber": automountNumber,
       "automountTable": automountTable,
       "automountEntry": automountEntry,
       "automountIndex": automountIndex,
       "automountPartitionIndex": automountPartitionIndex,
       "automountWWN": automountWWN,
       "automountLUN": automountLUN,
       "systemDrives": systemDrives,
       "sysDriveNumber": sysDriveNumber,
       "sysDriveTable": sysDriveTable,
       "sysDriveEntry": sysDriveEntry,
       "sysDriveIndex": sysDriveIndex,
       "sysDriveWWN": sysDriveWWN,
       "sysDriveLUN": sysDriveLUN,
       "sysDriveStatus": sysDriveStatus,
       "sysDriveCapacity": sysDriveCapacity,
       "sysDriveRaidLevel": sysDriveRaidLevel,
       "sysDriveCacheMode": sysDriveCacheMode,
       "volumes": volumes,
       "volumeNumber": volumeNumber,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeSysDriveIndex": volumeSysDriveIndex,
       "volumePartitionID": volumePartitionID,
       "volumeLabel": volumeLabel,
       "volumeStatus": volumeStatus,
       "volumeCapacity": volumeCapacity,
       "volumeFreeCapacity": volumeFreeCapacity,
       "volumeEnterpriseVirtualServer": volumeEnterpriseVirtualServer,
       "fsStatsTable": fsStatsTable,
       "fsStatsEntry": fsStatsEntry,
       "fsPermId": fsPermId,
       "fsLabel": fsLabel,
       "opsPerSecAverage": opsPerSecAverage,
       "fcStats": fcStats,
       "fcRequests": fcRequests,
       "fcResponses": fcResponses,
       "fcReadReqs": fcReadReqs,
       "fcWriteReqs": fcWriteReqs,
       "fcReadResps": fcReadResps,
       "fcWriteResps": fcWriteResps,
       "fcInstInRate": fcInstInRate,
       "fcInstOutRate": fcInstOutRate,
       "fcPkInRate": fcPkInRate,
       "fcPkOutRate": fcPkOutRate,
       "fcCacheHits": fcCacheHits,
       "fcCacheMisses": fcCacheMisses,
       "fcLossSignalErrs": fcLossSignalErrs,
       "fcBadRXCharErrs": fcBadRXCharErrs,
       "fcLossSyncErrs": fcLossSyncErrs,
       "fcLinkFailErrs": fcLinkFailErrs,
       "fcRXEOFErrs": fcRXEOFErrs,
       "fcDiscardedFrameErrs": fcDiscardedFrameErrs,
       "fcBadCRCErrs": fcBadCRCErrs,
       "fcProtErrs": fcProtErrs,
       "fcIOStatusResubs": fcIOStatusResubs,
       "fcIOStatusFails": fcIOStatusFails,
       "fibreChannelInterfaceNumber": fibreChannelInterfaceNumber,
       "fcStatsTable": fcStatsTable,
       "fcStatsEntry": fcStatsEntry,
       "fcInterfaceIndex": fcInterfaceIndex,
       "fcInstantaneousInRate": fcInstantaneousInRate,
       "fcInstantaneousOutRate": fcInstantaneousOutRate,
       "fcPeakInRate": fcPeakInRate,
       "fcPeakOutRate": fcPeakOutRate,
       "fcSignalLossErrors": fcSignalLossErrors,
       "fcBadRXCharErrors": fcBadRXCharErrors,
       "fcLossSyncErrors": fcLossSyncErrors,
       "fcLinkFailErrors": fcLinkFailErrors,
       "fcRXEOFErrors": fcRXEOFErrors,
       "fcDiscardedFrameErrors": fcDiscardedFrameErrors,
       "fcBadCRCErrors": fcBadCRCErrors,
       "fcProtocolErrors": fcProtocolErrors,
       "fcStatisticsTable": fcStatisticsTable,
       "fcStatisticsEntry": fcStatisticsEntry,
       "fcStatsClusterNode": fcStatsClusterNode,
       "fcStatsInterfaceIndex": fcStatsInterfaceIndex,
       "fcStatsInterfaceEnabled": fcStatsInterfaceEnabled,
       "fcStatsInterfaceStatus": fcStatsInterfaceStatus,
       "fcStatsInterfaceLinkSpeed": fcStatsInterfaceLinkSpeed,
       "fcStatsInterfaceLinkType": fcStatsInterfaceLinkType,
       "fcStatsInstantaneousInRate": fcStatsInstantaneousInRate,
       "fcStatsInstantaneousOutRate": fcStatsInstantaneousOutRate,
       "fcStatsPeakInRate": fcStatsPeakInRate,
       "fcStatsPeakOutRate": fcStatsPeakOutRate,
       "fcStatsTotalRxBytes": fcStatsTotalRxBytes,
       "fcStatsTotalTxBytes": fcStatsTotalTxBytes,
       "fcStatsSignalLossErrors": fcStatsSignalLossErrors,
       "fcStatsBadRXCharErrors": fcStatsBadRXCharErrors,
       "fcStatsLossSyncErrors": fcStatsLossSyncErrors,
       "fcStatsLinkFailErrors": fcStatsLinkFailErrors,
       "fcStatsRXEOFErrors": fcStatsRXEOFErrors,
       "fcStatsDiscardedFrameErrors": fcStatsDiscardedFrameErrors,
       "fcStatsBadCRCErrors": fcStatsBadCRCErrors,
       "fcStatsProtocolErrors": fcStatsProtocolErrors,
       "virtualVolumes": virtualVolumes,
       "virtualVolumeNumber": virtualVolumeNumber,
       "virtualVolumeTable": virtualVolumeTable,
       "virtualVolumeEntry": virtualVolumeEntry,
       "virtualVolumeSysDriveIndex": virtualVolumeSysDriveIndex,
       "virtualVolumePartitionID": virtualVolumePartitionID,
       "virtualVolumeLabel": virtualVolumeLabel,
       "virtualVolumeQuotaEnabled": virtualVolumeQuotaEnabled,
       "virtualVolumeLimit": virtualVolumeLimit,
       "virtualVolumeWarningAlert": virtualVolumeWarningAlert,
       "virtualVolumeCriticalAlert": virtualVolumeCriticalAlert,
       "virtualVolumeHardLimitEnabled": virtualVolumeHardLimitEnabled,
       "virtualVolumeQuotaBytesUsed": virtualVolumeQuotaBytesUsed,
       "virtualVolumeQuotaPercentageUsed": virtualVolumeQuotaPercentageUsed,
       "memberListNumber": memberListNumber,
       "memberListTable": memberListTable,
       "memberListEntry": memberListEntry,
       "memberListVolumeSysDriveIndex": memberListVolumeSysDriveIndex,
       "memberListVolumePartitionID": memberListVolumePartitionID,
       "memberListVirtualVolumeLabel": memberListVirtualVolumeLabel,
       "memberListIndex": memberListIndex,
       "memberListPath": memberListPath,
       "memberListStatus": memberListStatus,
       "snapshot": snapshot,
       "snapshotRuleNumber": snapshotRuleNumber,
       "snapshotRuleTable": snapshotRuleTable,
       "snapshotRuleEntry": snapshotRuleEntry,
       "snapshotRuleName": snapshotRuleName,
       "snapshotRuleWWN": snapshotRuleWWN,
       "snapshotRuleLUN": snapshotRuleLUN,
       "snapshotRulePartitionID": snapshotRulePartitionID,
       "snapshotRuleQueueSize": snapshotRuleQueueSize,
       "snapshotRuleVolumeLabel": snapshotRuleVolumeLabel,
       "snapshotScheduleNumber": snapshotScheduleNumber,
       "snapshotScheduleTable": snapshotScheduleTable,
       "snapshotScheduleEntry": snapshotScheduleEntry,
       "snapshotScheduleRuleName": snapshotScheduleRuleName,
       "snapshotScheduleIndex": snapshotScheduleIndex,
       "snapshotScheduleDateTimeSpec": snapshotScheduleDateTimeSpec,
       "snapshotRulesTable": snapshotRulesTable,
       "snapshotRulesEntry": snapshotRulesEntry,
       "snapshotRulesEVS": snapshotRulesEVS,
       "snapshotRulesName": snapshotRulesName,
       "snapshotRulesQueueSize": snapshotRulesQueueSize,
       "snapshotRulesVolumeLabel": snapshotRulesVolumeLabel,
       "snapshotSchedulesTable": snapshotSchedulesTable,
       "snapshotSchedulesEntry": snapshotSchedulesEntry,
       "snapshotSchedulesEVS": snapshotSchedulesEVS,
       "snapshotSchedulesRuleName": snapshotSchedulesRuleName,
       "snapshotSchedulesIndex": snapshotSchedulesIndex,
       "snapshotSchedulesDateTimeSpec": snapshotSchedulesDateTimeSpec,
       "nvramStats": nvramStats,
       "nvramFsStatsNumber": nvramFsStatsNumber,
       "nvramFsStatsTable": nvramFsStatsTable,
       "nvramFsStatsEntry": nvramFsStatsEntry,
       "fsId": fsId,
       "nvramFsStatsCurrentUsage": nvramFsStatsCurrentUsage,
       "nvramFsStatsCheckpoints": nvramFsStatsCheckpoints,
       "nvramFsStatsActivityCheckpoints": nvramFsStatsActivityCheckpoints,
       "nvramFsStatsWaitedAllocs": nvramFsStatsWaitedAllocs,
       "nvramFsStatsWaitingAllocs": nvramFsStatsWaitingAllocs,
       "nvramPoolStatsTable": nvramPoolStatsTable,
       "nvramPoolStatsEntry": nvramPoolStatsEntry,
       "clusterNodeId": clusterNodeId,
       "nvramPoolStatsSize": nvramPoolStatsSize,
       "nvramPoolStatsMaximumUsed": nvramPoolStatsMaximumUsed,
       "nvramPoolStatsTotalCurrentUsage": nvramPoolStatsTotalCurrentUsage,
       "nvramPoolStatsWaitedAllocs": nvramPoolStatsWaitedAllocs,
       "nvramPoolStatsWaitingAllocs": nvramPoolStatsWaitingAllocs,
       "network": network,
       "etherStats": etherStats,
       "ethOutPkts": ethOutPkts,
       "ethInPkts": ethInPkts,
       "ethInstInOctetRate": ethInstInOctetRate,
       "ethInstOutOctetRate": ethInstOutOctetRate,
       "ethPkInOctetRate": ethPkInOctetRate,
       "ethPkOutOctetRate": ethPkOutOctetRate,
       "ethInFIFODrops": ethInFIFODrops,
       "ethCRCErrs": ethCRCErrs,
       "ethOutFIFOUflows": ethOutFIFOUflows,
       "ethOutOneCollision": ethOutOneCollision,
       "ethOutTwoCollision": ethOutTwoCollision,
       "ethOutFifteenCollision": ethOutFifteenCollision,
       "ethInEvFIFOPktDrop": ethInEvFIFOPktDrop,
       "ethEvFIFOMaxEvents": ethEvFIFOMaxEvents,
       "ethOutPackets": ethOutPackets,
       "ethInPackets": ethInPackets,
       "ethTotalPackets": ethTotalPackets,
       "ethOutBytes": ethOutBytes,
       "ethInBytes": ethInBytes,
       "ethTotalBytes": ethTotalBytes,
       "ethernetStatisticsTable": ethernetStatisticsTable,
       "ethernetStatisticsEntry": ethernetStatisticsEntry,
       "ethernetInstInOctetRate": ethernetInstInOctetRate,
       "ethernetInstOutOctetRate": ethernetInstOutOctetRate,
       "ethernetPkInOctetRate": ethernetPkInOctetRate,
       "ethernetPkOutOctetRate": ethernetPkOutOctetRate,
       "ethernetInFIFODrops": ethernetInFIFODrops,
       "ethernetCRCErrs": ethernetCRCErrs,
       "ethernetOutFIFOUflows": ethernetOutFIFOUflows,
       "ethernetOutOneCollision": ethernetOutOneCollision,
       "ethernetOutTwoCollision": ethernetOutTwoCollision,
       "ethernetOutFifteenCollision": ethernetOutFifteenCollision,
       "ethernetInEvFIFOPktDrop": ethernetInEvFIFOPktDrop,
       "ethernetEvFIFOMaxEvents": ethernetEvFIFOMaxEvents,
       "ethernetOutPackets": ethernetOutPackets,
       "ethernetInPackets": ethernetInPackets,
       "ethernetTotalPackets": ethernetTotalPackets,
       "ethernetOutBytes": ethernetOutBytes,
       "ethernetInBytes": ethernetInBytes,
       "ethernetTotalBytes": ethernetTotalBytes,
       "pausedOffTime": pausedOffTime,
       "tcpipStats": tcpipStats,
       "tcpOpenConns": tcpOpenConns,
       "tcpMaxOpenConns": tcpMaxOpenConns,
       "tcpTotalOpenConns": tcpTotalOpenConns,
       "tcpFailedInConns": tcpFailedInConns,
       "tcpFailedOutConns": tcpFailedOutConns,
       "tcpOutSegments": tcpOutSegments,
       "tcpInSegments": tcpInSegments,
       "tcpReOutSegments": tcpReOutSegments,
       "tcpInvSegments": tcpInvSegments,
       "tcpIPInPkts": tcpIPInPkts,
       "tcpIPOutPkts": tcpIPOutPkts,
       "tcpIPInInvPkts": tcpIPInInvPkts,
       "tcpIPInInvHdrPkts": tcpIPInInvHdrPkts,
       "tcpIPInInvChksumPkts": tcpIPInInvChksumPkts,
       "tcpIPInInvNUcastAddrPkts": tcpIPInInvNUcastAddrPkts,
       "tcpIPInInvUcastAddrPkts": tcpIPInInvUcastAddrPkts,
       "tcpIPInInvSrcAddrPkts": tcpIPInInvSrcAddrPkts,
       "tcpIPInInvOptionPkts": tcpIPInInvOptionPkts,
       "tcpInOversizeSegmentErrs": tcpInOversizeSegmentErrs,
       "tcpInInvChksumPkts": tcpInInvChksumPkts,
       "tcpLinkPktDrops": tcpLinkPktDrops,
       "tcpStatisticsTable": tcpStatisticsTable,
       "tcpStatisticsEntry": tcpStatisticsEntry,
       "tcpTxSegments": tcpTxSegments,
       "tcpRxSegments": tcpRxSegments,
       "tcpReTxSegments": tcpReTxSegments,
       "tcpInvalidSegments": tcpInvalidSegments,
       "tcpIPTxPkts": tcpIPTxPkts,
       "tcpIPRxPkts": tcpIPRxPkts,
       "tcpIPRxInvalidPkts": tcpIPRxInvalidPkts,
       "tcpIPRxInvalidHdrPkts": tcpIPRxInvalidHdrPkts,
       "tcpIPRxInvalidChksumPkts": tcpIPRxInvalidChksumPkts,
       "tcpIPRxInvalidNUcastAddrPkts": tcpIPRxInvalidNUcastAddrPkts,
       "tcpIPRxInvalidUcastAddrPkts": tcpIPRxInvalidUcastAddrPkts,
       "tcpIPRxInvalidSrcAddrPkts": tcpIPRxInvalidSrcAddrPkts,
       "tcpIPRxInvalidOptionPkts": tcpIPRxInvalidOptionPkts,
       "tcpIPMiscBadSegments": tcpIPMiscBadSegments,
       "tcpRxOversizeSegmentErrs": tcpRxOversizeSegmentErrs,
       "tcpRxInvalidChksumPkts": tcpRxInvalidChksumPkts,
       "tcpLinkPacketDrops": tcpLinkPacketDrops,
       "udpStats": udpStats,
       "udpInShortPkts": udpInShortPkts,
       "udpInInvChksumPkts": udpInInvChksumPkts,
       "udpStatisticsTable": udpStatisticsTable,
       "udpStatisticsEntry": udpStatisticsEntry,
       "udpRxShortPkts": udpRxShortPkts,
       "udpRxInvChksumPkts": udpRxInvChksumPkts,
       "advipConfig": advipConfig,
       "tcpArpCacheTimeout": tcpArpCacheTimeout,
       "tcpBroadCastUsingZero": tcpBroadCastUsingZero,
       "tcpIgnoreICMPEcho": tcpIgnoreICMPEcho,
       "tcpOffSubnetMTU": tcpOffSubnetMTU,
       "tcpAllSubnetsMTU": tcpAllSubnetsMTU,
       "tcpKeepAlive": tcpKeepAlive,
       "tcpKeepAliveTimeout": tcpKeepAliveTimeout,
       "engipConfig": engipConfig,
       "tcpDefWnd": tcpDefWnd,
       "tcpDelayedAcks": tcpDelayedAcks,
       "tcpSlowStartCA": tcpSlowStartCA,
       "tcpSSRestartDoubleMSS": tcpSSRestartDoubleMSS,
       "tcpNagle": tcpNagle,
       "tcpSillyWindowAvoid": tcpSillyWindowAvoid,
       "tcpOldAckStrategy": tcpOldAckStrategy,
       "tcpSlowStartOnIdle": tcpSlowStartOnIdle,
       "tcpFastRetxFastRecovery": tcpFastRetxFastRecovery,
       "tcpOldPushStrategy": tcpOldPushStrategy,
       "tcpOffSubnetSlowStart": tcpOffSubnetSlowStart,
       "tcpUDPCheckSumGen": tcpUDPCheckSumGen,
       "tcpIntelliSeg": tcpIntelliSeg,
       "nameService": nameService,
       "wins": wins,
       "winsPrimaryIpAddr": winsPrimaryIpAddr,
       "winsSecondaryIpAddr": winsSecondaryIpAddr,
       "dns": dns,
       "dnsServerNumber": dnsServerNumber,
       "dnsServerTable": dnsServerTable,
       "dnsServerEntry": dnsServerEntry,
       "dnsServerIndex": dnsServerIndex,
       "dnsServerIpAddress": dnsServerIpAddress,
       "dnsSearchNumber": dnsSearchNumber,
       "dnsSearchTable": dnsSearchTable,
       "dnsSearchEntry": dnsSearchEntry,
       "dnsSearchIndex": dnsSearchIndex,
       "dnsSearchString": dnsSearchString,
       "nsOrder": nsOrder,
       "nameServiceNumber": nameServiceNumber,
       "nameServiceTable": nameServiceTable,
       "nameServiceEntry": nameServiceEntry,
       "nameServiceOrder": nameServiceOrder,
       "nameServiceType": nameServiceType,
       "nis": nis,
       "nisEnabled": nisEnabled,
       "nisDomain": nisDomain,
       "nisCurrentMaster": nisCurrentMaster,
       "nisServerBroadcastEnabled": nisServerBroadcastEnabled,
       "nisVerificationEnabled": nisVerificationEnabled,
       "nisTimeout": nisTimeout,
       "nisRebindInterval": nisRebindInterval,
       "nisUserGroupTimeout": nisUserGroupTimeout,
       "nisServerNumber": nisServerNumber,
       "nisServerTable": nisServerTable,
       "nisServerEntry": nisServerEntry,
       "nisServerIndex": nisServerIndex,
       "nisServerIpAddress": nisServerIpAddress,
       "nisServerPriority": nisServerPriority,
       "fileProtocol": fileProtocol,
       "security": security,
       "securityMode": securityMode,
       "securityDomain": securityDomain,
       "cifs": cifs,
       "shares": shares,
       "shareNumber": shareNumber,
       "shareTable": shareTable,
       "shareEntry": shareEntry,
       "shareName": shareName,
       "sharePath": sharePath,
       "shareComment": shareComment,
       "shareUsers": shareUsers,
       "shareWWN": shareWWN,
       "shareLUN": shareLUN,
       "sharePartitionID": sharePartitionID,
       "shareMaxUsers": shareMaxUsers,
       "cifsShareTable": cifsShareTable,
       "cifsShareEntry": cifsShareEntry,
       "cifsShareEvsId": cifsShareEvsId,
       "cifsShareName": cifsShareName,
       "cifsSharePath": cifsSharePath,
       "cifsShareComment": cifsShareComment,
       "cifsShareUsers": cifsShareUsers,
       "cifsShareMaxUsers": cifsShareMaxUsers,
       "cifsShareSpanId": cifsShareSpanId,
       "shareAccess": shareAccess,
       "shareAccessNumber": shareAccessNumber,
       "shareAccessTable": shareAccessTable,
       "shareAccessEntry": shareAccessEntry,
       "shareAccessIndex": shareAccessIndex,
       "shareAccessShareName": shareAccessShareName,
       "shareAccessName": shareAccessName,
       "shareAccessPerms": shareAccessPerms,
       "cifsStats": cifsStats,
       "cifsClients": cifsClients,
       "cifsMkdirCalls": cifsMkdirCalls,
       "cifsRmdirCalls": cifsRmdirCalls,
       "cifsOpenCalls": cifsOpenCalls,
       "cifsCreateCalls": cifsCreateCalls,
       "cifsCloseCalls": cifsCloseCalls,
       "cifsFlushCalls": cifsFlushCalls,
       "cifsUnlinkCalls": cifsUnlinkCalls,
       "cifsRenameCalls": cifsRenameCalls,
       "cifsGetatrCalls": cifsGetatrCalls,
       "cifsSetatrCalls": cifsSetatrCalls,
       "cifsReadCalls": cifsReadCalls,
       "cifsWriteCalls": cifsWriteCalls,
       "cifsMknewCalls": cifsMknewCalls,
       "cifsChkpthCalls": cifsChkpthCalls,
       "cifsLseekCalls": cifsLseekCalls,
       "cifsReadBrawCalls": cifsReadBrawCalls,
       "cifsWriteBrawCalls": cifsWriteBrawCalls,
       "cifsLockingXCalls": cifsLockingXCalls,
       "cifsTransCalls": cifsTransCalls,
       "cifsEchoCalls": cifsEchoCalls,
       "cifsWriteCloseCalls": cifsWriteCloseCalls,
       "cifsOpenXCalls": cifsOpenXCalls,
       "cifsReadXCalls": cifsReadXCalls,
       "cifsWriteXCalls": cifsWriteXCalls,
       "cifsTrans2Calls": cifsTrans2Calls,
       "cifsFindCloseCalls": cifsFindCloseCalls,
       "cifsTdisCalls": cifsTdisCalls,
       "cifsNegProtCalls": cifsNegProtCalls,
       "cifsSessSetupXCalls": cifsSessSetupXCalls,
       "cifsUlogoffXCalls": cifsUlogoffXCalls,
       "cifsTconXCalls": cifsTconXCalls,
       "cifsDskattrCalls": cifsDskattrCalls,
       "cifsSearchCalls": cifsSearchCalls,
       "cifsNTtransCalls": cifsNTtransCalls,
       "cifsNTtranssCalls": cifsNTtranssCalls,
       "cifsNTcreateXCalls": cifsNTcreateXCalls,
       "cifsNTcancelCalls": cifsNTcancelCalls,
       "cifsStatsTable": cifsStatsTable,
       "cifsStatsEntry": cifsStatsEntry,
       "cifsStatsClusterNode": cifsStatsClusterNode,
       "clients": clients,
       "mkdirCalls": mkdirCalls,
       "rmdirCalls": rmdirCalls,
       "openCalls": openCalls,
       "createCalls": createCalls,
       "closeCalls": closeCalls,
       "flushCalls": flushCalls,
       "unlinkCalls": unlinkCalls,
       "renameCalls": renameCalls,
       "getatrCalls": getatrCalls,
       "setatrCalls": setatrCalls,
       "readCalls": readCalls,
       "writeCalls": writeCalls,
       "mknewCalls": mknewCalls,
       "chkpthCalls": chkpthCalls,
       "lseekCalls": lseekCalls,
       "readBrawCalls": readBrawCalls,
       "writeBrawCalls": writeBrawCalls,
       "lockingXCalls": lockingXCalls,
       "transCalls": transCalls,
       "echoCalls": echoCalls,
       "writeCloseCalls": writeCloseCalls,
       "openXCalls": openXCalls,
       "readXCalls": readXCalls,
       "writeXCalls": writeXCalls,
       "trans2Calls": trans2Calls,
       "findCloseCalls": findCloseCalls,
       "tdisCalls": tdisCalls,
       "negProtCalls": negProtCalls,
       "sessSetupXCalls": sessSetupXCalls,
       "ulogoffXCalls": ulogoffXCalls,
       "tconXCalls": tconXCalls,
       "dskattrCalls": dskattrCalls,
       "searchCalls": searchCalls,
       "ntTransCalls": ntTransCalls,
       "ntTranssCalls": ntTranssCalls,
       "ntCreateXCalls": ntCreateXCalls,
       "ntCancelCalls": ntCancelCalls,
       "cifsService": cifsService,
       "cifsServiceEnabled": cifsServiceEnabled,
       "cifsServiceMaxUsers": cifsServiceMaxUsers,
       "nfs": nfs,
       "nfsExports": nfsExports,
       "nfsExportNumber": nfsExportNumber,
       "nfsExportTable": nfsExportTable,
       "nfsExportEntry": nfsExportEntry,
       "nfsExportIndex": nfsExportIndex,
       "nfsExportName": nfsExportName,
       "nfsExportPath": nfsExportPath,
       "nfsExportNumberMounts": nfsExportNumberMounts,
       "nfsExportWWN": nfsExportWWN,
       "nfsExportLUN": nfsExportLUN,
       "nfsExportPartitionID": nfsExportPartitionID,
       "nfsExportsTable": nfsExportsTable,
       "nfsExportsEntry": nfsExportsEntry,
       "nfsExportsEvs": nfsExportsEvs,
       "nfsExportsName": nfsExportsName,
       "nfsExportsPath": nfsExportsPath,
       "nfsExportsDeviceId": nfsExportsDeviceId,
       "nfsUsers": nfsUsers,
       "nfsUserNumber": nfsUserNumber,
       "nfsUserTable": nfsUserTable,
       "nfsUserEntry": nfsUserEntry,
       "nfsUserName": nfsUserName,
       "nfsUserID": nfsUserID,
       "nfsUserMapping": nfsUserMapping,
       "nfsUserMappingNumber": nfsUserMappingNumber,
       "nfsUserMappingTable": nfsUserMappingTable,
       "nfsUserMappingEntry": nfsUserMappingEntry,
       "nfsUserMappingUnixUserName": nfsUserMappingUnixUserName,
       "nfsUserMappingUnixUserIDValid": nfsUserMappingUnixUserIDValid,
       "nfsUserMappingUnixUserID": nfsUserMappingUnixUserID,
       "nfsUserMappingNtUserName": nfsUserMappingNtUserName,
       "nfsUserMappingNtUserDomainName": nfsUserMappingNtUserDomainName,
       "nfsGroups": nfsGroups,
       "nfsGroupNumber": nfsGroupNumber,
       "nfsGroupTable": nfsGroupTable,
       "nfsGroupEntry": nfsGroupEntry,
       "nfsGroupName": nfsGroupName,
       "nfsGroupID": nfsGroupID,
       "nfsGroupMapping": nfsGroupMapping,
       "nfsGroupMappingNumber": nfsGroupMappingNumber,
       "nfsGroupMappingTable": nfsGroupMappingTable,
       "nfsGroupMappingEntry": nfsGroupMappingEntry,
       "nfsGroupMappingUnixGroupName": nfsGroupMappingUnixGroupName,
       "nfsGroupMappingUnixGroupIDValid": nfsGroupMappingUnixGroupIDValid,
       "nfsGroupMappingUnixGroupID": nfsGroupMappingUnixGroupID,
       "nfsGroupMappingNtGroupName": nfsGroupMappingNtGroupName,
       "nfsGroupMappingNtGroupDomainName": nfsGroupMappingNtGroupDomainName,
       "nfsStats": nfsStats,
       "nfsVersion2": nfsVersion2,
       "null2Calls": null2Calls,
       "getAttr2Calls": getAttr2Calls,
       "setAttr2Calls": setAttr2Calls,
       "rootCalls": rootCalls,
       "lookup2Calls": lookup2Calls,
       "readLink2": readLink2,
       "read2": read2,
       "writeCache": writeCache,
       "write2": write2,
       "create2": create2,
       "remove2": remove2,
       "rename2": rename2,
       "link2": link2,
       "symLink2": symLink2,
       "mkDir2": mkDir2,
       "rmDir2": rmDir2,
       "readDir2": readDir2,
       "statFS2": statFS2,
       "nfsV2StatsTable": nfsV2StatsTable,
       "nfsV2StatsEntry": nfsV2StatsEntry,
       "nfsV2StatsClusterNode": nfsV2StatsClusterNode,
       "nfsV2nullCalls": nfsV2nullCalls,
       "nfsV2getAttrCalls": nfsV2getAttrCalls,
       "nfsV2setAttrCalls": nfsV2setAttrCalls,
       "nfsV2rootCalls": nfsV2rootCalls,
       "nfsV2lookupCalls": nfsV2lookupCalls,
       "nfsV2readLink": nfsV2readLink,
       "nfsV2read": nfsV2read,
       "nfsV2writeCache": nfsV2writeCache,
       "nfsV2write": nfsV2write,
       "nfsV2create": nfsV2create,
       "nfsV2remove": nfsV2remove,
       "nfsV2rename": nfsV2rename,
       "nfsV2link": nfsV2link,
       "nfsV2symLink": nfsV2symLink,
       "nfsV2mkDir": nfsV2mkDir,
       "nfsV2rmDir": nfsV2rmDir,
       "nfsV2readDir": nfsV2readDir,
       "nfsV2statFS": nfsV2statFS,
       "nfsVersion3": nfsVersion3,
       "null3Calls": null3Calls,
       "getAttr3Calls": getAttr3Calls,
       "setAttr3Calls": setAttr3Calls,
       "lookup3Calls": lookup3Calls,
       "access3Calls": access3Calls,
       "readLink3": readLink3,
       "read3": read3,
       "write3": write3,
       "create3": create3,
       "mkdir3": mkdir3,
       "symLink3": symLink3,
       "mkNod3": mkNod3,
       "remove3": remove3,
       "rmDir3": rmDir3,
       "rename3": rename3,
       "link3": link3,
       "readDir3": readDir3,
       "readDirPlus3": readDirPlus3,
       "fsStat3": fsStat3,
       "fsInfo3": fsInfo3,
       "pathConf3": pathConf3,
       "commit3": commit3,
       "nfsV3StatsTable": nfsV3StatsTable,
       "nfsV3StatsEntry": nfsV3StatsEntry,
       "nfsV3StatsClusterNode": nfsV3StatsClusterNode,
       "nfsV3nullCalls": nfsV3nullCalls,
       "nfsV3getAttrCalls": nfsV3getAttrCalls,
       "nfsV3setAttrCalls": nfsV3setAttrCalls,
       "nfsV3lookupCalls": nfsV3lookupCalls,
       "nfsV3accessCalls": nfsV3accessCalls,
       "nfsV3readLink": nfsV3readLink,
       "nfsV3read": nfsV3read,
       "nfsV3write": nfsV3write,
       "nfsV3create": nfsV3create,
       "nfsV3mkdir": nfsV3mkdir,
       "nfsV3symLink": nfsV3symLink,
       "nfsV3mkNod": nfsV3mkNod,
       "nfsV3remove": nfsV3remove,
       "nfsV3rmDir": nfsV3rmDir,
       "nfsV3rename": nfsV3rename,
       "nfsV3link": nfsV3link,
       "nfsV3readDir": nfsV3readDir,
       "nfsV3readDirPlus": nfsV3readDirPlus,
       "nfsV3fsStat": nfsV3fsStat,
       "nfsV3fsInfo": nfsV3fsInfo,
       "nfsV3pathConf": nfsV3pathConf,
       "nfsV3commit": nfsV3commit,
       "nfsMounts": nfsMounts,
       "nfsClients": nfsClients,
       "nfsService": nfsService,
       "nfsServiceEnabled": nfsServiceEnabled,
       "nfsServiceMaxUsers": nfsServiceMaxUsers,
       "ftp": ftp,
       "ftpTimeout": ftpTimeout,
       "ftpMountPoints": ftpMountPoints,
       "ftpMountNumber": ftpMountNumber,
       "ftpMountTable": ftpMountTable,
       "ftpMountEntry": ftpMountEntry,
       "ftpMountName": ftpMountName,
       "ftpMountNumberUsers": ftpMountNumberUsers,
       "ftpMountWWN": ftpMountWWN,
       "ftpMountLUN": ftpMountLUN,
       "ftpMountPartitionID": ftpMountPartitionID,
       "ftpUsers": ftpUsers,
       "ftpUserNumber": ftpUserNumber,
       "ftpUserTable": ftpUserTable,
       "ftpUserEntry": ftpUserEntry,
       "ftpUserName": ftpUserName,
       "ftpUserMountPointExists": ftpUserMountPointExists,
       "ftpUserMountPoint": ftpUserMountPoint,
       "ftpUserMountInitDirectory": ftpUserMountInitDirectory,
       "ftpLogging": ftpLogging,
       "ftpAuditLogging": ftpAuditLogging,
       "ftpAuditLogVolumeWWN": ftpAuditLogVolumeWWN,
       "ftpAuditLogVolumeLUN": ftpAuditLogVolumeLUN,
       "ftpAuditLogVolumePartitionID": ftpAuditLogVolumePartitionID,
       "ftpAuditLogDirectory": ftpAuditLogDirectory,
       "ftpAuditLogRecordsPerFile": ftpAuditLogRecordsPerFile,
       "ftpAuditMaximumLogFiles": ftpAuditMaximumLogFiles,
       "ftpStats": ftpStats,
       "ftpTotalSess": ftpTotalSess,
       "ftpTotalFtpXferIn": ftpTotalFtpXferIn,
       "ftpBytesTotalXferIn": ftpBytesTotalXferIn,
       "ftpTotalFtpXferOut": ftpTotalFtpXferOut,
       "ftpBytesTotalXferOut": ftpBytesTotalXferOut,
       "ftpTotalFtpCommands": ftpTotalFtpCommands,
       "ftpTotalFtpReplies": ftpTotalFtpReplies,
       "ftpTotalBytesCommands": ftpTotalBytesCommands,
       "ftpTotalBytesReplies": ftpTotalBytesReplies,
       "ftpService": ftpService,
       "ftpServiceEnabled": ftpServiceEnabled,
       "ftpServiceMaxUsers": ftpServiceMaxUsers,
       "ftpSecurity": ftpSecurity,
       "ftpNTPasswordEnabled": ftpNTPasswordEnabled,
       "ftpNISPasswordEnabled": ftpNISPasswordEnabled,
       "http": http,
       "httpConfig": httpConfig,
       "httpHostVolumeWWN": httpHostVolumeWWN,
       "httpHostVolumeLUN": httpHostVolumeLUN,
       "httpHostVolumePartitionID": httpHostVolumePartitionID,
       "httpRoot": httpRoot,
       "httpProduct": httpProduct,
       "httpMinTimeOut": httpMinTimeOut,
       "httpMaxTimeOut": httpMaxTimeOut,
       "httpDecrTimeOut": httpDecrTimeOut,
       "httpIncrTimeOut": httpIncrTimeOut,
       "httpMaxConnections": httpMaxConnections,
       "httpListDirectories": httpListDirectories,
       "httpLogging": httpLogging,
       "httpMaximalLogging": httpMaximalLogging,
       "httpLogVolumeWWN": httpLogVolumeWWN,
       "httpLogVolumeLUN": httpLogVolumeLUN,
       "httpLogVolumePartitionID": httpLogVolumePartitionID,
       "httpLogDirectory": httpLogDirectory,
       "httpLogRecordsPerFile": httpLogRecordsPerFile,
       "httpMaximumLogFiles": httpMaximumLogFiles,
       "httpMimeMapNumber": httpMimeMapNumber,
       "httpMimeMapTable": httpMimeMapTable,
       "httpMimeMapEntry": httpMimeMapEntry,
       "httpMimeMapIndex": httpMimeMapIndex,
       "httpMimeMapExtension": httpMimeMapExtension,
       "httpMimeMapType": httpMimeMapType,
       "httpStats": httpStats,
       "httpConnsAccepted": httpConnsAccepted,
       "httpConnsRefused": httpConnsRefused,
       "httpBytesXferOut": httpBytesXferOut,
       "httpBytesXferIn": httpBytesXferIn,
       "httpGetRequests": httpGetRequests,
       "httpHeadRequests": httpHeadRequests,
       "httpPutRequests": httpPutRequests,
       "httpPostRequests": httpPostRequests,
       "httpStatusOK": httpStatusOK,
       "httpStatusNotModified": httpStatusNotModified,
       "httpStatusPreconFailed": httpStatusPreconFailed,
       "httpStatusBadRequest": httpStatusBadRequest,
       "httpStatusForbidden": httpStatusForbidden,
       "httpStatusNotFound": httpStatusNotFound,
       "httpStatusURITooLong": httpStatusURITooLong,
       "httpStatusServerError": httpStatusServerError,
       "httpStatusNotImplemented": httpStatusNotImplemented,
       "httpStatusServiceUnavailable": httpStatusServiceUnavailable,
       "httpStatusOtherErr": httpStatusOtherErr,
       "httpTimeOut": httpTimeOut,
       "httpOpenConnections": httpOpenConnections,
       "httpActiveConnections": httpActiveConnections,
       "httpService": httpService,
       "httpServiceEnabled": httpServiceEnabled,
       "httpServiceMaxUsers": httpServiceMaxUsers,
       "iScsi": iScsi,
       "iScsiConfiguration": iScsiConfiguration,
       "iScsiServiceEnabled": iScsiServiceEnabled,
       "iScsiParameterTable": iScsiParameterTable,
       "iScsiParameterEntry": iScsiParameterEntry,
       "iScsiParameterEVS": iScsiParameterEVS,
       "iScsiParameterName": iScsiParameterName,
       "iScsiParameterIsBoolean": iScsiParameterIsBoolean,
       "iScsiParameterValue": iScsiParameterValue,
       "iScsiTargetNumber": iScsiTargetNumber,
       "iScsiTargetTable": iScsiTargetTable,
       "iScsiTargetEntry": iScsiTargetEntry,
       "iScsiGloballyUniqueName": iScsiGloballyUniqueName,
       "iScsiTargetName": iScsiTargetName,
       "iScsiTargetComment": iScsiTargetComment,
       "iScsiTargetLogicalUnitNumber": iScsiTargetLogicalUnitNumber,
       "iScsiTargetAuthEnabled": iScsiTargetAuthEnabled,
       "iScsiLogicalUnitNumber": iScsiLogicalUnitNumber,
       "iScsiLogicalUnitTable": iScsiLogicalUnitTable,
       "iScsiLogicalUnitEntry": iScsiLogicalUnitEntry,
       "iScsiLUEvs": iScsiLUEvs,
       "iScsiLUName": iScsiLUName,
       "iScsiLUStatus": iScsiLUStatus,
       "iScsiLUComment": iScsiLUComment,
       "iScsiLUDeviceId": iScsiLUDeviceId,
       "iScsiLUPath": iScsiLUPath,
       "iScsiLUInitialized": iScsiLUInitialized,
       "iScsiLUSize": iScsiLUSize,
       "iScsiTargetLogicalUnitTable": iScsiTargetLogicalUnitTable,
       "iScsiTargetLogicalUnitEntry": iScsiTargetLogicalUnitEntry,
       "iScsiTargetLUTargetName": iScsiTargetLUTargetName,
       "iScsiTargetLULogicalUnitName": iScsiTargetLULogicalUnitName,
       "iScsiTargetLun": iScsiTargetLun,
       "iSNSTable": iSNSTable,
       "iSNSEntry": iSNSEntry,
       "iSNSIpAddress": iSNSIpAddress,
       "iSNSPort": iSNSPort,
       "iScsiStatistics": iScsiStatistics,
       "iScsiStatisticsTable": iScsiStatisticsTable,
       "iScsiStatisticsEntry": iScsiStatisticsEntry,
       "iScsiStatisticsNodeId": iScsiStatisticsNodeId,
       "iScsiStatisticsName": iScsiStatisticsName,
       "iScsiStatisticsValue": iScsiStatisticsValue,
       "backup": backup,
       "ndmpStatus": ndmpStatus,
       "ndmpCurrentStatus": ndmpCurrentStatus,
       "ndmpEnabledOnBoot": ndmpEnabledOnBoot,
       "ndmpDevices": ndmpDevices,
       "autoChangerNumber": autoChangerNumber,
       "autoChangerTable": autoChangerTable,
       "autoChangerEntry": autoChangerEntry,
       "autoChangerIndex": autoChangerIndex,
       "autoChangerDeviceName": autoChangerDeviceName,
       "autoChangerSerialNumber": autoChangerSerialNumber,
       "autoChangerEVS": autoChangerEVS,
       "tapeDriveNumber": tapeDriveNumber,
       "tapeDriveTable": tapeDriveTable,
       "tapeDriveEntry": tapeDriveEntry,
       "tapeDriveIndex": tapeDriveIndex,
       "tapeDriveAutoChangerIndex": tapeDriveAutoChangerIndex,
       "tapeDriveDeviceName": tapeDriveDeviceName,
       "tapeDriveSerialNumber": tapeDriveSerialNumber,
       "tapeDriveLocation": tapeDriveLocation,
       "tapeDriveEVS": tapeDriveEVS,
       "ndmpSnapshotOptions": ndmpSnapshotOptions,
       "ndmpAutoSnapCreateEnabled": ndmpAutoSnapCreateEnabled,
       "ndmpAutoSnapDeleteMode": ndmpAutoSnapDeleteMode,
       "ndmpAutoSnapMaxRetention": ndmpAutoSnapMaxRetention,
       "mgmnt": mgmnt,
       "systemUsers": systemUsers,
       "systemUserNumber": systemUserNumber,
       "systemUserTable": systemUserTable,
       "systemUserEntry": systemUserEntry,
       "systemUserName": systemUserName,
       "systemUserAccessLevel": systemUserAccessLevel,
       "license": license,
       "licenseKeyNumber": licenseKeyNumber,
       "licenseKeyTable": licenseKeyTable,
       "licenseKeyEntry": licenseKeyEntry,
       "licenseKeyIndex": licenseKeyIndex,
       "licenseKeyString": licenseKeyString,
       "licenseKeyValid": licenseKeyValid,
       "licenseCIFSService": licenseCIFSService,
       "licenseNFSService": licenseNFSService,
       "licenseFTPService": licenseFTPService,
       "licenseHTTPService": licenseHTTPService,
       "licenseFailoverService": licenseFailoverService,
       "licenseRAIDService": licenseRAIDService,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseIndex": licenseIndex,
       "licenseKey": licenseKey,
       "licenseService": licenseService,
       "access": access,
       "web": web,
       "webAccessEnabled": webAccessEnabled,
       "webAccessRestricted": webAccessRestricted,
       "webAccessRestrictedNumber": webAccessRestrictedNumber,
       "webAccessRestrictedTable": webAccessRestrictedTable,
       "webAccessRestrictedEntry": webAccessRestrictedEntry,
       "webAccessRestrictedHost": webAccessRestrictedHost,
       "webAccessPortNumber": webAccessPortNumber,
       "webAccessMaxConnections": webAccessMaxConnections,
       "sictrl": sictrl,
       "sictrlAccessEnabled": sictrlAccessEnabled,
       "sictrlAccessRestricted": sictrlAccessRestricted,
       "sictrlAccessRestrictedNumber": sictrlAccessRestrictedNumber,
       "sictrlAccessRestrictedTable": sictrlAccessRestrictedTable,
       "sictrlAccessRestrictedEntry": sictrlAccessRestrictedEntry,
       "sictrlAccessRestrictedHost": sictrlAccessRestrictedHost,
       "sictrlAccessPortNumber": sictrlAccessPortNumber,
       "sictrlAccessMaxConnections": sictrlAccessMaxConnections,
       "telnet": telnet,
       "telnetAccessEnabled": telnetAccessEnabled,
       "telnetAccessRestricted": telnetAccessRestricted,
       "telnetAccessRestrictedNumber": telnetAccessRestrictedNumber,
       "telnetAccessRestrictedTable": telnetAccessRestrictedTable,
       "telnetAccessRestrictedEntry": telnetAccessRestrictedEntry,
       "telnetAccessRestrictedHost": telnetAccessRestrictedHost,
       "telnetAccessPortNumber": telnetAccessPortNumber,
       "telnetAccessMaxConnections": telnetAccessMaxConnections,
       "secureWeb": secureWeb,
       "secureWebAccessEnabled": secureWebAccessEnabled,
       "secureWebAccessRestricted": secureWebAccessRestricted,
       "secureWebAccessRestrictedNumber": secureWebAccessRestrictedNumber,
       "secureWebAccessRestrictedTable": secureWebAccessRestrictedTable,
       "secureWebAccessRestrictedEntry": secureWebAccessRestrictedEntry,
       "secureWebAccessRestrictedHost": secureWebAccessRestrictedHost,
       "secureWebAccessPortNumber": secureWebAccessPortNumber,
       "secureWebAccessMaxConnections": secureWebAccessMaxConnections,
       "lcd": lcd,
       "lcdFrontPanelLocked": lcdFrontPanelLocked,
       "eventlog": eventlog,
       "eventLogNumber": eventLogNumber,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogTimeStamp": eventLogTimeStamp,
       "eventLogHandle": eventLogHandle,
       "eventLogText": eventLogText,
       "alerts": alerts,
       "mailAlertConfig": mailAlertConfig,
       "smtpAddr": smtpAddr,
       "smtpCritFreq": smtpCritFreq,
       "smtpSevFreq": smtpSevFreq,
       "smtpWarnFreq": smtpWarnFreq,
       "smtpInfoFreq": smtpInfoFreq,
       "smtpRecipNumber": smtpRecipNumber,
       "smtpRecipTable": smtpRecipTable,
       "smtpRecipEntry": smtpRecipEntry,
       "smtpRecipIndex": smtpRecipIndex,
       "smtpRecipName": smtpRecipName,
       "smtpDiagUUencEnabled": smtpDiagUUencEnabled,
       "smtpUndisclosedRecipNumber": smtpUndisclosedRecipNumber,
       "smtpUndisclosedRecipTable": smtpUndisclosedRecipTable,
       "smtpUndisclosedRecipEntry": smtpUndisclosedRecipEntry,
       "smtpUndisclosedRecipIndex": smtpUndisclosedRecipIndex,
       "smtpUndisclosedRecipName": smtpUndisclosedRecipName,
       "smtpRecipientTable": smtpRecipientTable,
       "smtpRecipientEntry": smtpRecipientEntry,
       "smtpRecipientIndex": smtpRecipientIndex,
       "smtpRecipientName": smtpRecipientName,
       "smtpRecipientDisclose": smtpRecipientDisclose,
       "smtpRecipientEmpty": smtpRecipientEmpty,
       "winAlertConfig": winAlertConfig,
       "winCritFreq": winCritFreq,
       "winSevFreq": winSevFreq,
       "winWarnFreq": winWarnFreq,
       "winInfoFreq": winInfoFreq,
       "winRecipNumber": winRecipNumber,
       "winRecipTable": winRecipTable,
       "winRecipEntry": winRecipEntry,
       "winRecipIndex": winRecipIndex,
       "winRecipName": winRecipName,
       "snmpAlertConfig": snmpAlertConfig,
       "snmpCritFreq": snmpCritFreq,
       "snmpSevFreq": snmpSevFreq,
       "snmpWarnFreq": snmpWarnFreq,
       "snmpInfoFreq": snmpInfoFreq,
       "snmpRecipNumber": snmpRecipNumber,
       "snmpRecipTable": snmpRecipTable,
       "snmpRecipEntry": snmpRecipEntry,
       "snmpRecipIndex": snmpRecipIndex,
       "snmpRecipName": snmpRecipName,
       "snmpAgent": snmpAgent,
       "snmpProtocolMode": snmpProtocolMode,
       "snmpAccessRestricted": snmpAccessRestricted,
       "snmpAccessRestrictedNumber": snmpAccessRestrictedNumber,
       "snmpAccessRestrictedTable": snmpAccessRestrictedTable,
       "snmpAccessRestrictedEntry": snmpAccessRestrictedEntry,
       "snmpAccessRestrictedHost": snmpAccessRestrictedHost,
       "snmpTrapHostNumber": snmpTrapHostNumber,
       "snmpTrapHostTable": snmpTrapHostTable,
       "snmpTrapHostEntry": snmpTrapHostEntry,
       "snmpTrapHostIndex": snmpTrapHostIndex,
       "snmpTrapHost": snmpTrapHost,
       "versions": versions,
       "verinfoSw": verinfoSw,
       "verinfoHw": verinfoHw,
       "verModNumber": verModNumber,
       "verModTable": verModTable,
       "verModEntry": verModEntry,
       "verModIndex": verModIndex,
       "verModLoader": verModLoader,
       "verModKernel": verModKernel,
       "verModHw": verModHw,
       "verModSerial": verModSerial,
       "verModBuildState": verModBuildState,
       "verModUniq0": verModUniq0,
       "verModUniq1": verModUniq1,
       "verModFirstDate": verModFirstDate,
       "verModMTDSLastFailure": verModMTDSLastFailure,
       "verModMTDSFailures": verModMTDSFailures,
       "verModMTDSLastPass": verModMTDSLastPass,
       "verModMTDSPasses": verModMTDSPasses,
       "verModCardID": verModCardID,
       "verModCardRev": verModCardRev,
       "verModGlueRev": verModGlueRev,
       "cron": cron,
       "cronJobNumber": cronJobNumber,
       "cronJobTable": cronJobTable,
       "cronJobEntry": cronJobEntry,
       "cronJobIndex": cronJobIndex,
       "cronJobDateSpec": cronJobDateSpec,
       "cronJobCommandList": cronJobCommandList,
       "cronJobMailList": cronJobMailList,
       "cronJobAccessLevel": cronJobAccessLevel,
       "atJobNumber": atJobNumber,
       "atJobTable": atJobTable,
       "atJobEntry": atJobEntry,
       "atJobIndex": atJobIndex,
       "atJobRunTime": atJobRunTime,
       "atJobCommandList": atJobCommandList,
       "atJobMailList": atJobMailList,
       "atJobAccessLevel": atJobAccessLevel,
       "mgmntStats": mgmntStats,
       "webMgmntStats": webMgmntStats,
       "webCurrActiveSessions": webCurrActiveSessions,
       "webMaxSessions": webMaxSessions,
       "webTotalSessions": webTotalSessions,
       "webRejectedSessions": webRejectedSessions,
       "webTotalFramesTX": webTotalFramesTX,
       "webTotalFramesRX": webTotalFramesRX,
       "webTotalBytesTX": webTotalBytesTX,
       "webTotalBytesRX": webTotalBytesRX,
       "sictrlMgmntStats": sictrlMgmntStats,
       "sictrlCurrActiveSessions": sictrlCurrActiveSessions,
       "sictrlMaxSessions": sictrlMaxSessions,
       "sictrlTotalSessions": sictrlTotalSessions,
       "sictrlRejectedSessions": sictrlRejectedSessions,
       "sictrlTotalFramesTX": sictrlTotalFramesTX,
       "sictrlTotalFramesRX": sictrlTotalFramesRX,
       "sictrlTotalBytesTX": sictrlTotalBytesTX,
       "sictrlTotalBytesRX": sictrlTotalBytesRX,
       "telnetMgmntStats": telnetMgmntStats,
       "telnetCurrActiveSessions": telnetCurrActiveSessions,
       "telnetMaxSessions": telnetMaxSessions,
       "telnetTotalSessions": telnetTotalSessions,
       "telnetRejectedSessions": telnetRejectedSessions,
       "telnetTotalFramesTX": telnetTotalFramesTX,
       "telnetTotalFramesRX": telnetTotalFramesRX,
       "telnetTotalBytesTX": telnetTotalBytesTX,
       "telnetTotalBytesRX": telnetTotalBytesRX,
       "secureWebMgmntStats": secureWebMgmntStats,
       "secureWebCurrActiveSessions": secureWebCurrActiveSessions,
       "secureWebMaxSessions": secureWebMaxSessions,
       "secureWebTotalSessions": secureWebTotalSessions,
       "secureWebRejectedSessions": secureWebRejectedSessions,
       "secureWebTotalFramesTX": secureWebTotalFramesTX,
       "secureWebTotalFramesRX": secureWebTotalFramesRX,
       "secureWebTotalBytesTX": secureWebTotalBytesTX,
       "secureWebTotalBytesRX": secureWebTotalBytesRX,
       "hwFlowControl": hwFlowControl,
       "hwFlowNumber": hwFlowNumber,
       "hwFlowTable": hwFlowTable,
       "hwFlowEntry": hwFlowEntry,
       "hwFlowIndex": hwFlowIndex,
       "hwFlowDebug": hwFlowDebug,
       "hwFlowConsole": hwFlowConsole,
       "performance": performance,
       "utilization": utilization,
       "cpuUtilizationNumber": cpuUtilizationNumber,
       "cpuUtilizationTable": cpuUtilizationTable,
       "cpuUtilizationEntry": cpuUtilizationEntry,
       "cpuUtilizationCnIndex": cpuUtilizationCnIndex,
       "cpuIndex": cpuIndex,
       "cpuUtilization": cpuUtilization,
       "fpgaUtilizationNumber": fpgaUtilizationNumber,
       "fpgaUtilizationTable": fpgaUtilizationTable,
       "fpgaUtilizationEntry": fpgaUtilizationEntry,
       "fpgaUtilizationCnIndex": fpgaUtilizationCnIndex,
       "fpgaUtilizationFpgaIndex": fpgaUtilizationFpgaIndex,
       "fpgaUtilizationFpgaName": fpgaUtilizationFpgaName,
       "fpgaUtilization": fpgaUtilization,
       "systemDriveStats": systemDriveStats,
       "systemDriveStatsNumber": systemDriveStatsNumber,
       "systemDriveStatsTable": systemDriveStatsTable,
       "systemDriveStatsEntry": systemDriveStatsEntry,
       "systemDriveStatsCnIndex": systemDriveStatsCnIndex,
       "systemDriveStatsSdId": systemDriveStatsSdId,
       "cumNonZeroQueuedReadTime": cumNonZeroQueuedReadTime,
       "cumNonZeroQueuedWriteTime": cumNonZeroQueuedWriteTime,
       "readCount": readCount,
       "singleBufferWriteCount": singleBufferWriteCount,
       "stripeWriteCount": stripeWriteCount,
       "readCumLatency": readCumLatency,
       "oneWriteCumLatency": oneWriteCumLatency,
       "stripeWriteCumLatency": stripeWriteCumLatency,
       "fileSystemStats": fileSystemStats,
       "fileSystemStatsNumber": fileSystemStatsNumber,
       "fileSystemStatsTable": fileSystemStatsTable,
       "fileSystemStatsEntry": fileSystemStatsEntry,
       "fsStatsFsId": fsStatsFsId,
       "fsStatsFsLabel": fsStatsFsLabel,
       "fsCapacityTotalUpper": fsCapacityTotalUpper,
       "fsCapacityTotalLower": fsCapacityTotalLower,
       "fsCapacityUsedUpper": fsCapacityUsedUpper,
       "fsCapacityUsedLower": fsCapacityUsedLower,
       "fsCapacitySnapshotUpper": fsCapacitySnapshotUpper,
       "fsCapacitySnapshotLower": fsCapacitySnapshotLower,
       "fsNvramWaitedAllocs": fsNvramWaitedAllocs,
       "fsWriteSmoothing": fsWriteSmoothing,
       "fileSystemTierStatsNumber": fileSystemTierStatsNumber,
       "fileSystemTierStatsTable": fileSystemTierStatsTable,
       "fsTierStatsEntry": fsTierStatsEntry,
       "fsTierStatsFsId": fsTierStatsFsId,
       "fsTier": fsTier,
       "fsTierStatsFsLabel": fsTierStatsFsLabel,
       "fsTierCapacityTotalUpper": fsTierCapacityTotalUpper,
       "fsTierCapacityTotalLower": fsTierCapacityTotalLower,
       "fsTierCapacityUsedUpper": fsTierCapacityUsedUpper,
       "fsTierCapacityUsedLower": fsTierCapacityUsedLower,
       "fsTierCapacitySnapshotUpper": fsTierCapacitySnapshotUpper,
       "fsTierCapacitySnapshotLower": fsTierCapacitySnapshotLower,
       "spanStats": spanStats,
       "spanStatsNumber": spanStatsNumber,
       "spanStatsTable": spanStatsTable,
       "spanStatsEntry": spanStatsEntry,
       "spanStatsSpanId": spanStatsSpanId,
       "spanLabel": spanLabel,
       "spanCapacityTotalUpper": spanCapacityTotalUpper,
       "spanCapacityTotalLower": spanCapacityTotalLower,
       "spanCapacityUsedUpper": spanCapacityUsedUpper,
       "spanCapacityUsedLower": spanCapacityUsedLower,
       "spanTierStatsNumber": spanTierStatsNumber,
       "spanTierStatsTable": spanTierStatsTable,
       "spanTierStatsEntry": spanTierStatsEntry,
       "spanTierStatsSpanId": spanTierStatsSpanId,
       "spanTier": spanTier,
       "spanTierLabel": spanTierLabel,
       "spanTierCapacityTotalUpper": spanTierCapacityTotalUpper,
       "spanTierCapacityTotalLower": spanTierCapacityTotalLower,
       "spanTierCapacityUsedUpper": spanTierCapacityUsedUpper,
       "spanTierCapacityUsedLower": spanTierCapacityUsedLower,
       "cacheStats": cacheStats,
       "metaDataCacheStatsNumber": metaDataCacheStatsNumber,
       "metaDataCacheStatsTable": metaDataCacheStatsTable,
       "metaDataCacheStatsEntry": metaDataCacheStatsEntry,
       "metaDataCacheStatsFsId": metaDataCacheStatsFsId,
       "metaDataCache": metaDataCache,
       "metaDataCacheStatsFsLabel": metaDataCacheStatsFsLabel,
       "metaDataCacheStatsHits": metaDataCacheStatsHits,
       "metaDataCacheStatsMisses": metaDataCacheStatsMisses,
       "sectorCacheStatsNumber": sectorCacheStatsNumber,
       "sectorCacheStatsTable": sectorCacheStatsTable,
       "sectorCacheStatsEntry": sectorCacheStatsEntry,
       "sectorCacheStatsCnIndex": sectorCacheStatsCnIndex,
       "sectorCacheType": sectorCacheType,
       "sectorCacheStatsHitsPSI": sectorCacheStatsHitsPSI,
       "sectorCacheStatsHitsSSI": sectorCacheStatsHitsSSI,
       "sectorCacheStatsHitsTotal": sectorCacheStatsHitsTotal,
       "sectorCacheStatsMissesPSI": sectorCacheStatsMissesPSI,
       "sectorCacheStatsMissesSSI": sectorCacheStatsMissesSSI,
       "sectorCacheStatsMissesTotal": sectorCacheStatsMissesTotal,
       "protocolStats": protocolStats,
       "protocolStatsNumber": protocolStatsNumber,
       "protocolStatsTable": protocolStatsTable,
       "protocolStatsEntry": protocolStatsEntry,
       "protStatsFsId": protStatsFsId,
       "protStatsFlavor": protStatsFlavor,
       "protStatsOpCode": protStatsOpCode,
       "protStatsFsLabel": protStatsFsLabel,
       "protStatsOpCodeName": protStatsOpCodeName,
       "protOpCount": protOpCount,
       "protCumulativeLatency": protCumulativeLatency,
       "protocolXferStatsNumber": protocolXferStatsNumber,
       "protocolXferStatsTable": protocolXferStatsTable,
       "protocolXferStatsEntry": protocolXferStatsEntry,
       "protocolXferStatsFsId": protocolXferStatsFsId,
       "protocolXferStatsFlavor": protocolXferStatsFlavor,
       "protocolXferStatsFsLabel": protocolXferStatsFsLabel,
       "protocolXferStatsBytesRead": protocolXferStatsBytesRead,
       "protocolXferStatsBytesWritten": protocolXferStatsBytesWritten,
       "clusterStats": clusterStats,
       "intraClusterPortErrorNumber": intraClusterPortErrorNumber,
       "intraClusterPortErrorTable": intraClusterPortErrorTable,
       "intraClusterPortErrorEntry": intraClusterPortErrorEntry,
       "intraClusterPortErrsCnId": intraClusterPortErrsCnId,
       "mirroringRetransmits": mirroringRetransmits,
       "cnsRetransmits": cnsRetransmits,
       "totalRetransmits": totalRetransmits,
       "clusterNodeStatsNumber": clusterNodeStatsNumber,
       "clusterNodeStatsTable": clusterNodeStatsTable,
       "clusterNodeStatsEntry": clusterNodeStatsEntry,
       "clusterNodeStatsCnId": clusterNodeStatsCnId,
       "runningBossockFibers": runningBossockFibers}
)
