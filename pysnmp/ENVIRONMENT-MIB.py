# SNMP MIB module (ENVIRONMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENVIRONMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:52 2024
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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

nnenvironmentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3)
)
nnenvironmentMib.setRevisions(
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("failed", 2),
          ("normal", 3))
    )



class EnvType(Integer32, TextualConvention):
    status = "current"
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
        *(("supply-AC-ONLY", 1),
          ("supply-AC-PoE", 2),
          ("supply-DC", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_NnenvObjects_ObjectIdentity = ObjectIdentity
nnenvObjects = _NnenvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1)
)
_NnenvTempSensorGroup_ObjectIdentity = ObjectIdentity
nnenvTempSensorGroup = _NnenvTempSensorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1)
)
_NnenvTempSensorValue_Type = Gauge32
_NnenvTempSensorValue_Object = MibScalar
nnenvTempSensorValue = _NnenvTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1, 1),
    _NnenvTempSensorValue_Type()
)
nnenvTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvTempSensorValue.setStatus("current")
_NnenvTempSensorState_Type = EnvState
_NnenvTempSensorState_Object = MibScalar
nnenvTempSensorState = _NnenvTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1, 2),
    _NnenvTempSensorState_Type()
)
nnenvTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvTempSensorState.setStatus("current")
_NnenvFanTable_Object = MibTable
nnenvFanTable = _NnenvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nnenvFanTable.setStatus("current")
_NnenvFanEntry_Object = MibTableRow
nnenvFanEntry = _NnenvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1)
)
nnenvFanEntry.setIndexNames(
    (0, "ENVIRONMENT-MIB", "nnenvFanUnitIndex"),
)
if mibBuilder.loadTexts:
    nnenvFanEntry.setStatus("current")


class _NnenvFanUnitIndex_Type(Integer32):
    """Custom type nnenvFanUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NnenvFanUnitIndex_Type.__name__ = "Integer32"
_NnenvFanUnitIndex_Object = MibTableColumn
nnenvFanUnitIndex = _NnenvFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1, 1),
    _NnenvFanUnitIndex_Type()
)
nnenvFanUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnenvFanUnitIndex.setStatus("current")
_NnenvFanState_Type = EnvState
_NnenvFanState_Object = MibTableColumn
nnenvFanState = _NnenvFanState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1, 2),
    _NnenvFanState_Type()
)
nnenvFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvFanState.setStatus("current")
_NnenvPwrsupPowerFailCount_Type = Integer32
_NnenvPwrsupPowerFailCount_Object = MibScalar
nnenvPwrsupPowerFailCount = _NnenvPwrsupPowerFailCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 3),
    _NnenvPwrsupPowerFailCount_Type()
)
nnenvPwrsupPowerFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupPowerFailCount.setStatus("current")
_NnenvPwrsupTable_Object = MibTable
nnenvPwrsupTable = _NnenvPwrsupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    nnenvPwrsupTable.setStatus("current")
_NnenvPwrsupEntry_Object = MibTableRow
nnenvPwrsupEntry = _NnenvPwrsupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1)
)
nnenvPwrsupEntry.setIndexNames(
    (0, "ENVIRONMENT-MIB", "nnenvPwrsupIndex"),
)
if mibBuilder.loadTexts:
    nnenvPwrsupEntry.setStatus("current")


class _NnenvPwrsupIndex_Type(Integer32):
    """Custom type nnenvPwrsupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NnenvPwrsupIndex_Type.__name__ = "Integer32"
_NnenvPwrsupIndex_Object = MibTableColumn
nnenvPwrsupIndex = _NnenvPwrsupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 1),
    _NnenvPwrsupIndex_Type()
)
nnenvPwrsupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnenvPwrsupIndex.setStatus("current")
_NnenvPwrsupInstalled_Type = EnvInstalled
_NnenvPwrsupInstalled_Object = MibTableColumn
nnenvPwrsupInstalled = _NnenvPwrsupInstalled_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 2),
    _NnenvPwrsupInstalled_Type()
)
nnenvPwrsupInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupInstalled.setStatus("current")
_NnenvPwrsupStatus_Type = EnvStatus
_NnenvPwrsupStatus_Object = MibTableColumn
nnenvPwrsupStatus = _NnenvPwrsupStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 3),
    _NnenvPwrsupStatus_Type()
)
nnenvPwrsupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupStatus.setStatus("current")
_NnenvPwrsupType_Type = EnvType
_NnenvPwrsupType_Object = MibTableColumn
nnenvPwrsupType = _NnenvPwrsupType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 4),
    _NnenvPwrsupType_Type()
)
nnenvPwrsupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupType.setStatus("current")
_NnenvPwrsupUptime_Type = Integer32
_NnenvPwrsupUptime_Object = MibTableColumn
nnenvPwrsupUptime = _NnenvPwrsupUptime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 5),
    _NnenvPwrsupUptime_Type()
)
nnenvPwrsupUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupUptime.setStatus("current")
_NnenvPwrsupDowntime_Type = Integer32
_NnenvPwrsupDowntime_Object = MibTableColumn
nnenvPwrsupDowntime = _NnenvPwrsupDowntime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 6),
    _NnenvPwrsupDowntime_Type()
)
nnenvPwrsupDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenvPwrsupDowntime.setStatus("current")
_NnenvNotificationEnables_ObjectIdentity = ObjectIdentity
nnenvNotificationEnables = _NnenvNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2)
)


class _NnenvEnableTemperatureNotification_Type(TruthValue):
    """Custom type nnenvEnableTemperatureNotification based on TruthValue"""


_NnenvEnableTemperatureNotification_Object = MibScalar
nnenvEnableTemperatureNotification = _NnenvEnableTemperatureNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 1),
    _NnenvEnableTemperatureNotification_Type()
)
nnenvEnableTemperatureNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenvEnableTemperatureNotification.setStatus("current")


class _NnenvEnableFanNotification_Type(TruthValue):
    """Custom type nnenvEnableFanNotification based on TruthValue"""


_NnenvEnableFanNotification_Object = MibScalar
nnenvEnableFanNotification = _NnenvEnableFanNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 2),
    _NnenvEnableFanNotification_Type()
)
nnenvEnableFanNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenvEnableFanNotification.setStatus("current")


class _NnenvEnablePowerNotification_Type(TruthValue):
    """Custom type nnenvEnablePowerNotification based on TruthValue"""


_NnenvEnablePowerNotification_Object = MibScalar
nnenvEnablePowerNotification = _NnenvEnablePowerNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 3),
    _NnenvEnablePowerNotification_Type()
)
nnenvEnablePowerNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenvEnablePowerNotification.setStatus("current")
_NnenvNotifications_ObjectIdentity = ObjectIdentity
nnenvNotifications = _NnenvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3)
)
_NnenvTraps_ObjectIdentity = ObjectIdentity
nnenvTraps = _NnenvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0)
)

# Managed Objects groups


# Notification objects

nnenvTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 1)
)
nnenvTemperatureNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvTempSensorValue"),
        ("ENVIRONMENT-MIB", "nnenvTempSensorState"))
)
if mibBuilder.loadTexts:
    nnenvTemperatureNotification.setStatus(
        "current"
    )

nnenvFanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 2)
)
nnenvFanNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvFanUnitIndex"),
        ("ENVIRONMENT-MIB", "nnenvFanState"))
)
if mibBuilder.loadTexts:
    nnenvFanNotification.setStatus(
        "current"
    )

nnenvPowerSupply1DownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 3)
)
nnenvPowerSupply1DownNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupType"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    nnenvPowerSupply1DownNotification.setStatus(
        "current"
    )

nnenvPowerSupply1UpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 4)
)
nnenvPowerSupply1UpNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupType"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    nnenvPowerSupply1UpNotification.setStatus(
        "current"
    )

nnenvPowerSupply2DownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 5)
)
nnenvPowerSupply2DownNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupType"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    nnenvPowerSupply2DownNotification.setStatus(
        "current"
    )

nnenvPowerSupply2UpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 6)
)
nnenvPowerSupply2UpNotification.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupType"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"),
        ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
)
if mibBuilder.loadTexts:
    nnenvPowerSupply2UpNotification.setStatus(
        "current"
    )


# Notifications groups

nnenvironementNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 4)
)
nnenvironementNotificationGroup.setObjects(
      *(("ENVIRONMENT-MIB", "nnenvTemperatureNotification"),
        ("ENVIRONMENT-MIB", "nnenvFanNotification"),
        ("ENVIRONMENT-MIB", "nnenvPowerSupply1DownNotification"),
        ("ENVIRONMENT-MIB", "nnenvPowerSupply1UpNotification"),
        ("ENVIRONMENT-MIB", "nnenvPowerSupply2DownNotification"),
        ("ENVIRONMENT-MIB", "nnenvPowerSupply2UpNotification"))
)
if mibBuilder.loadTexts:
    nnenvironementNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENVIRONMENT-MIB",
    **{"EnvState": EnvState,
       "EnvInstalled": EnvInstalled,
       "EnvStatus": EnvStatus,
       "EnvType": EnvType,
       "nnenvironmentMib": nnenvironmentMib,
       "nnenvObjects": nnenvObjects,
       "nnenvTempSensorGroup": nnenvTempSensorGroup,
       "nnenvTempSensorValue": nnenvTempSensorValue,
       "nnenvTempSensorState": nnenvTempSensorState,
       "nnenvFanTable": nnenvFanTable,
       "nnenvFanEntry": nnenvFanEntry,
       "nnenvFanUnitIndex": nnenvFanUnitIndex,
       "nnenvFanState": nnenvFanState,
       "nnenvPwrsupPowerFailCount": nnenvPwrsupPowerFailCount,
       "nnenvPwrsupTable": nnenvPwrsupTable,
       "nnenvPwrsupEntry": nnenvPwrsupEntry,
       "nnenvPwrsupIndex": nnenvPwrsupIndex,
       "nnenvPwrsupInstalled": nnenvPwrsupInstalled,
       "nnenvPwrsupStatus": nnenvPwrsupStatus,
       "nnenvPwrsupType": nnenvPwrsupType,
       "nnenvPwrsupUptime": nnenvPwrsupUptime,
       "nnenvPwrsupDowntime": nnenvPwrsupDowntime,
       "nnenvNotificationEnables": nnenvNotificationEnables,
       "nnenvEnableTemperatureNotification": nnenvEnableTemperatureNotification,
       "nnenvEnableFanNotification": nnenvEnableFanNotification,
       "nnenvEnablePowerNotification": nnenvEnablePowerNotification,
       "nnenvNotifications": nnenvNotifications,
       "nnenvTraps": nnenvTraps,
       "nnenvTemperatureNotification": nnenvTemperatureNotification,
       "nnenvFanNotification": nnenvFanNotification,
       "nnenvPowerSupply1DownNotification": nnenvPowerSupply1DownNotification,
       "nnenvPowerSupply1UpNotification": nnenvPowerSupply1UpNotification,
       "nnenvPowerSupply2DownNotification": nnenvPowerSupply2DownNotification,
       "nnenvPowerSupply2UpNotification": nnenvPowerSupply2UpNotification,
       "nnenvironementNotificationGroup": nnenvironementNotificationGroup}
)
