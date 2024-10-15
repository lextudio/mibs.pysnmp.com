# SNMP MIB module (TIARA-NETWORKS-ENVIRONMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-ENVIRONMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:40 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraEnvironmentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3)
)
tiaraEnvironmentMib.setRevisions(
        ("1900-08-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnvState(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 3),
          ("fail", 4),
          ("normal", 1),
          ("turned-off", 5),
          ("warning", 2))
    )



class EnvInstalled(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("not-installed", 1))
    )



class EnvStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class EnvType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minus48VDC", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EnvObjects_ObjectIdentity = ObjectIdentity
envObjects = _EnvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1)
)
_EnvTempSensorTable_Object = MibTable
envTempSensorTable = _EnvTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    envTempSensorTable.setStatus("current")
_EnvTempSensorEntry_Object = MibTableRow
envTempSensorEntry = _EnvTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1)
)
envTempSensorEntry.setIndexNames(
    (0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorUnitIndex"),
)
if mibBuilder.loadTexts:
    envTempSensorEntry.setStatus("current")


class _EnvTempSensorUnitIndex_Type(Integer32):
    """Custom type envTempSensorUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnvTempSensorUnitIndex_Type.__name__ = "Integer32"
_EnvTempSensorUnitIndex_Object = MibTableColumn
envTempSensorUnitIndex = _EnvTempSensorUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 1),
    _EnvTempSensorUnitIndex_Type()
)
envTempSensorUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envTempSensorUnitIndex.setStatus("current")
_EnvTempSensorValue_Type = Gauge32
_EnvTempSensorValue_Object = MibTableColumn
envTempSensorValue = _EnvTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 2),
    _EnvTempSensorValue_Type()
)
envTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTempSensorValue.setStatus("current")
_EnvTempSensorState_Type = EnvState
_EnvTempSensorState_Object = MibTableColumn
envTempSensorState = _EnvTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 1, 1, 3),
    _EnvTempSensorState_Type()
)
envTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTempSensorState.setStatus("current")
_EnvFanTable_Object = MibTable
envFanTable = _EnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    envFanTable.setStatus("current")
_EnvFanEntry_Object = MibTableRow
envFanEntry = _EnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1)
)
envFanEntry.setIndexNames(
    (0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanUnitIndex"),
)
if mibBuilder.loadTexts:
    envFanEntry.setStatus("current")


class _EnvFanUnitIndex_Type(Integer32):
    """Custom type envFanUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnvFanUnitIndex_Type.__name__ = "Integer32"
_EnvFanUnitIndex_Object = MibTableColumn
envFanUnitIndex = _EnvFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1, 1),
    _EnvFanUnitIndex_Type()
)
envFanUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envFanUnitIndex.setStatus("current")
_EnvFanState_Type = EnvState
_EnvFanState_Object = MibTableColumn
envFanState = _EnvFanState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 2, 1, 2),
    _EnvFanState_Type()
)
envFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanState.setStatus("current")
_EnvPwrsupPowerFailCount_Type = Integer32
_EnvPwrsupPowerFailCount_Object = MibScalar
envPwrsupPowerFailCount = _EnvPwrsupPowerFailCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 3),
    _EnvPwrsupPowerFailCount_Type()
)
envPwrsupPowerFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupPowerFailCount.setStatus("current")
_EnvPwrsupTable_Object = MibTable
envPwrsupTable = _EnvPwrsupTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    envPwrsupTable.setStatus("current")
_EnvPwrsupEntry_Object = MibTableRow
envPwrsupEntry = _EnvPwrsupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1)
)
envPwrsupEntry.setIndexNames(
    (0, "TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"),
)
if mibBuilder.loadTexts:
    envPwrsupEntry.setStatus("current")


class _EnvPwrsupIndex_Type(Integer32):
    """Custom type envPwrsupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EnvPwrsupIndex_Type.__name__ = "Integer32"
_EnvPwrsupIndex_Object = MibTableColumn
envPwrsupIndex = _EnvPwrsupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 1),
    _EnvPwrsupIndex_Type()
)
envPwrsupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envPwrsupIndex.setStatus("current")
_EnvPwrsupInstalled_Type = EnvInstalled
_EnvPwrsupInstalled_Object = MibTableColumn
envPwrsupInstalled = _EnvPwrsupInstalled_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 2),
    _EnvPwrsupInstalled_Type()
)
envPwrsupInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupInstalled.setStatus("current")
_EnvPwrsupStatus_Type = EnvStatus
_EnvPwrsupStatus_Object = MibTableColumn
envPwrsupStatus = _EnvPwrsupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 3),
    _EnvPwrsupStatus_Type()
)
envPwrsupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupStatus.setStatus("current")
_EnvPwrsupType_Type = EnvType
_EnvPwrsupType_Object = MibTableColumn
envPwrsupType = _EnvPwrsupType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 4),
    _EnvPwrsupType_Type()
)
envPwrsupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupType.setStatus("current")
_EnvPwrsupUptime_Type = Integer32
_EnvPwrsupUptime_Object = MibTableColumn
envPwrsupUptime = _EnvPwrsupUptime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 5),
    _EnvPwrsupUptime_Type()
)
envPwrsupUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupUptime.setStatus("current")
_EnvPwrsupDowntime_Type = Integer32
_EnvPwrsupDowntime_Object = MibTableColumn
envPwrsupDowntime = _EnvPwrsupDowntime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 1, 4, 1, 6),
    _EnvPwrsupDowntime_Type()
)
envPwrsupDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPwrsupDowntime.setStatus("current")
_EnvNotificationEnables_ObjectIdentity = ObjectIdentity
envNotificationEnables = _EnvNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 2)
)


class _EnvEnableTemperatureNotification_Type(TruthValue):
    """Custom type envEnableTemperatureNotification based on TruthValue"""


_EnvEnableTemperatureNotification_Object = MibScalar
envEnableTemperatureNotification = _EnvEnableTemperatureNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 1),
    _EnvEnableTemperatureNotification_Type()
)
envEnableTemperatureNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envEnableTemperatureNotification.setStatus("current")


class _EnvEnableFanNotification_Type(TruthValue):
    """Custom type envEnableFanNotification based on TruthValue"""


_EnvEnableFanNotification_Object = MibScalar
envEnableFanNotification = _EnvEnableFanNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 2),
    _EnvEnableFanNotification_Type()
)
envEnableFanNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envEnableFanNotification.setStatus("current")


class _EnvEnablePowerNotification_Type(TruthValue):
    """Custom type envEnablePowerNotification based on TruthValue"""


_EnvEnablePowerNotification_Object = MibScalar
envEnablePowerNotification = _EnvEnablePowerNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 2, 3),
    _EnvEnablePowerNotification_Type()
)
envEnablePowerNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envEnablePowerNotification.setStatus("current")
_EnvNotifications_ObjectIdentity = ObjectIdentity
envNotifications = _EnvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3)
)

# Managed Objects groups


# Notification objects

envTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 1)
)
envTemperatureNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorUnitIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorValue"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envTempSensorState"))
)
if mibBuilder.loadTexts:
    envTemperatureNotification.setStatus(
        ""
    )

envFanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 2)
)
envFanNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanUnitIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envFanState"))
)
if mibBuilder.loadTexts:
    envFanNotification.setStatus(
        ""
    )

envPowerSupply1DownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 3)
)
envPowerSupply1DownNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    envPowerSupply1DownNotification.setStatus(
        ""
    )

envPowerSupply1UpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 4)
)
envPowerSupply1UpNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    envPowerSupply1UpNotification.setStatus(
        ""
    )

envPowerSupply2DownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 5)
)
envPowerSupply2DownNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    envPowerSupply2DownNotification.setStatus(
        ""
    )

envPowerSupply2UpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 3, 3, 0, 6)
)
envPowerSupply2UpNotification.setObjects(
      *(("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupPowerFailCount"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupIndex"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupInstalled"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupStatus"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupType"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupUptime"),
        ("TIARA-NETWORKS-ENVIRONMENT-MIB", "envPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    envPowerSupply2UpNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-ENVIRONMENT-MIB",
    **{"EnvState": EnvState,
       "EnvInstalled": EnvInstalled,
       "EnvStatus": EnvStatus,
       "EnvType": EnvType,
       "tiaraEnvironmentMib": tiaraEnvironmentMib,
       "envObjects": envObjects,
       "envTempSensorTable": envTempSensorTable,
       "envTempSensorEntry": envTempSensorEntry,
       "envTempSensorUnitIndex": envTempSensorUnitIndex,
       "envTempSensorValue": envTempSensorValue,
       "envTempSensorState": envTempSensorState,
       "envFanTable": envFanTable,
       "envFanEntry": envFanEntry,
       "envFanUnitIndex": envFanUnitIndex,
       "envFanState": envFanState,
       "envPwrsupPowerFailCount": envPwrsupPowerFailCount,
       "envPwrsupTable": envPwrsupTable,
       "envPwrsupEntry": envPwrsupEntry,
       "envPwrsupIndex": envPwrsupIndex,
       "envPwrsupInstalled": envPwrsupInstalled,
       "envPwrsupStatus": envPwrsupStatus,
       "envPwrsupType": envPwrsupType,
       "envPwrsupUptime": envPwrsupUptime,
       "envPwrsupDowntime": envPwrsupDowntime,
       "envNotificationEnables": envNotificationEnables,
       "envEnableTemperatureNotification": envEnableTemperatureNotification,
       "envEnableFanNotification": envEnableFanNotification,
       "envEnablePowerNotification": envEnablePowerNotification,
       "envNotifications": envNotifications,
       "envTemperatureNotification": envTemperatureNotification,
       "envFanNotification": envFanNotification,
       "envPowerSupply1DownNotification": envPowerSupply1DownNotification,
       "envPowerSupply1UpNotification": envPowerSupply1UpNotification,
       "envPowerSupply2DownNotification": envPowerSupply2DownNotification,
       "envPowerSupply2UpNotification": envPowerSupply2UpNotification}
)
