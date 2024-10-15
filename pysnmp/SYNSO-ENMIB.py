# SNMP MIB module (SYNSO-ENMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNSO-ENMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:08 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
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

_Synso_ObjectIdentity = ObjectIdentity
synso = _Synso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557)
)
_SynsoMeasure_ObjectIdentity = ObjectIdentity
synsoMeasure = _SynsoMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 2)
)
_SyupsEnvironTemperature_ObjectIdentity = ObjectIdentity
syupsEnvironTemperature = _SyupsEnvironTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1)
)
_SyupsEnvironTemperatureNumber_Type = Integer32
_SyupsEnvironTemperatureNumber_Object = MibScalar
syupsEnvironTemperatureNumber = _SyupsEnvironTemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 1),
    _SyupsEnvironTemperatureNumber_Type()
)
syupsEnvironTemperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureNumber.setStatus("mandatory")
_SyupsEnvironTemperatureTable_Object = MibTable
syupsEnvironTemperatureTable = _SyupsEnvironTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2)
)
if mibBuilder.loadTexts:
    syupsEnvironTemperatureTable.setStatus("mandatory")
_SyupsEnvironTemperatureEntry_Object = MibTableRow
syupsEnvironTemperatureEntry = _SyupsEnvironTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1)
)
syupsEnvironTemperatureEntry.setIndexNames(
    (0, "SYNSO-ENMIB", "syupsEnvironTemperatureIndex"),
)
if mibBuilder.loadTexts:
    syupsEnvironTemperatureEntry.setStatus("mandatory")
_SyupsEnvironTemperatureIndex_Type = Integer32
_SyupsEnvironTemperatureIndex_Object = MibTableColumn
syupsEnvironTemperatureIndex = _SyupsEnvironTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1, 1),
    _SyupsEnvironTemperatureIndex_Type()
)
syupsEnvironTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureIndex.setStatus("mandatory")
_SyupsEnvironTemperatureDescription_Type = DisplayString
_SyupsEnvironTemperatureDescription_Object = MibTableColumn
syupsEnvironTemperatureDescription = _SyupsEnvironTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1, 2),
    _SyupsEnvironTemperatureDescription_Type()
)
syupsEnvironTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureDescription.setStatus("mandatory")
_SyupsEnvironTemperatureLow_Type = Integer32
_SyupsEnvironTemperatureLow_Object = MibTableColumn
syupsEnvironTemperatureLow = _SyupsEnvironTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1, 3),
    _SyupsEnvironTemperatureLow_Type()
)
syupsEnvironTemperatureLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureLow.setStatus("mandatory")
_SyupsEnvironTemperatureHigh_Type = Integer32
_SyupsEnvironTemperatureHigh_Object = MibTableColumn
syupsEnvironTemperatureHigh = _SyupsEnvironTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1, 4),
    _SyupsEnvironTemperatureHigh_Type()
)
syupsEnvironTemperatureHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureHigh.setStatus("mandatory")
_SyupsEnvironTemperatureCurrent_Type = Integer32
_SyupsEnvironTemperatureCurrent_Object = MibTableColumn
syupsEnvironTemperatureCurrent = _SyupsEnvironTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 1, 2, 1, 5),
    _SyupsEnvironTemperatureCurrent_Type()
)
syupsEnvironTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironTemperatureCurrent.setStatus("mandatory")
_SyupsEnvironHumidity_ObjectIdentity = ObjectIdentity
syupsEnvironHumidity = _SyupsEnvironHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2)
)
_SyupsEnvironHumidityNumber_Type = Integer32
_SyupsEnvironHumidityNumber_Object = MibScalar
syupsEnvironHumidityNumber = _SyupsEnvironHumidityNumber_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 1),
    _SyupsEnvironHumidityNumber_Type()
)
syupsEnvironHumidityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironHumidityNumber.setStatus("mandatory")
_SyupsEnvironHumidityTable_Object = MibTable
syupsEnvironHumidityTable = _SyupsEnvironHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2)
)
if mibBuilder.loadTexts:
    syupsEnvironHumidityTable.setStatus("mandatory")
_SyupsEnvironHumidityEntry_Object = MibTableRow
syupsEnvironHumidityEntry = _SyupsEnvironHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1)
)
syupsEnvironHumidityEntry.setIndexNames(
    (0, "SYNSO-ENMIB", "syupsEnvironHumidityIndex"),
)
if mibBuilder.loadTexts:
    syupsEnvironHumidityEntry.setStatus("mandatory")
_SyupsEnvironHumidityIndex_Type = Integer32
_SyupsEnvironHumidityIndex_Object = MibTableColumn
syupsEnvironHumidityIndex = _SyupsEnvironHumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1, 1),
    _SyupsEnvironHumidityIndex_Type()
)
syupsEnvironHumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironHumidityIndex.setStatus("mandatory")
_SyupsEnvironHumidityDescription_Type = DisplayString
_SyupsEnvironHumidityDescription_Object = MibTableColumn
syupsEnvironHumidityDescription = _SyupsEnvironHumidityDescription_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1, 2),
    _SyupsEnvironHumidityDescription_Type()
)
syupsEnvironHumidityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironHumidityDescription.setStatus("mandatory")
_SyupsEnvironHumidityLow_Type = Integer32
_SyupsEnvironHumidityLow_Object = MibTableColumn
syupsEnvironHumidityLow = _SyupsEnvironHumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1, 3),
    _SyupsEnvironHumidityLow_Type()
)
syupsEnvironHumidityLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironHumidityLow.setStatus("mandatory")
_SyupsEnvironHumidityHigh_Type = Integer32
_SyupsEnvironHumidityHigh_Object = MibTableColumn
syupsEnvironHumidityHigh = _SyupsEnvironHumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1, 4),
    _SyupsEnvironHumidityHigh_Type()
)
syupsEnvironHumidityHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnvironHumidityHigh.setStatus("mandatory")
_SyupsEnvironHumidityCurrent_Type = Integer32
_SyupsEnvironHumidityCurrent_Object = MibTableColumn
syupsEnvironHumidityCurrent = _SyupsEnvironHumidityCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 2, 2, 1, 5),
    _SyupsEnvironHumidityCurrent_Type()
)
syupsEnvironHumidityCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEnvironHumidityCurrent.setStatus("mandatory")
_SyupsContact_ObjectIdentity = ObjectIdentity
syupsContact = _SyupsContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3)
)
_SyupsContactNumber_Type = Integer32
_SyupsContactNumber_Object = MibScalar
syupsContactNumber = _SyupsContactNumber_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 1),
    _SyupsContactNumber_Type()
)
syupsContactNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsContactNumber.setStatus("mandatory")
_SyupsContactTable_Object = MibTable
syupsContactTable = _SyupsContactTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2)
)
if mibBuilder.loadTexts:
    syupsContactTable.setStatus("mandatory")
_SyupsContactEntry_Object = MibTableRow
syupsContactEntry = _SyupsContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1)
)
syupsContactEntry.setIndexNames(
    (0, "SYNSO-ENMIB", "syupsContactIndex"),
)
if mibBuilder.loadTexts:
    syupsContactEntry.setStatus("mandatory")
_SyupsContactIndex_Type = Integer32
_SyupsContactIndex_Object = MibTableColumn
syupsContactIndex = _SyupsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1, 1),
    _SyupsContactIndex_Type()
)
syupsContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsContactIndex.setStatus("mandatory")
_SyupsContactDescription_Type = DisplayString
_SyupsContactDescription_Object = MibTableColumn
syupsContactDescription = _SyupsContactDescription_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1, 2),
    _SyupsContactDescription_Type()
)
syupsContactDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsContactDescription.setStatus("mandatory")


class _SyupsContactNormalState_Type(Integer32):
    """Custom type syupsContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("open", 2),
          ("unknown", 1))
    )


_SyupsContactNormalState_Type.__name__ = "Integer32"
_SyupsContactNormalState_Object = MibTableColumn
syupsContactNormalState = _SyupsContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1, 3),
    _SyupsContactNormalState_Type()
)
syupsContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsContactNormalState.setStatus("mandatory")


class _SyupsContactMonitoringStatus_Type(Integer32):
    """Custom type syupsContactMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_SyupsContactMonitoringStatus_Type.__name__ = "Integer32"
_SyupsContactMonitoringStatus_Object = MibTableColumn
syupsContactMonitoringStatus = _SyupsContactMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1, 4),
    _SyupsContactMonitoringStatus_Type()
)
syupsContactMonitoringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsContactMonitoringStatus.setStatus("mandatory")


class _SyupsContactCurrentStatus_Type(Integer32):
    """Custom type syupsContactCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("noFault", 2),
          ("unknown", 1))
    )


_SyupsContactCurrentStatus_Type.__name__ = "Integer32"
_SyupsContactCurrentStatus_Object = MibTableColumn
syupsContactCurrentStatus = _SyupsContactCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9557, 2, 3, 2, 1, 5),
    _SyupsContactCurrentStatus_Type()
)
syupsContactCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsContactCurrentStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNSO-ENMIB",
    **{"synso": synso,
       "synsoMeasure": synsoMeasure,
       "syupsEnvironTemperature": syupsEnvironTemperature,
       "syupsEnvironTemperatureNumber": syupsEnvironTemperatureNumber,
       "syupsEnvironTemperatureTable": syupsEnvironTemperatureTable,
       "syupsEnvironTemperatureEntry": syupsEnvironTemperatureEntry,
       "syupsEnvironTemperatureIndex": syupsEnvironTemperatureIndex,
       "syupsEnvironTemperatureDescription": syupsEnvironTemperatureDescription,
       "syupsEnvironTemperatureLow": syupsEnvironTemperatureLow,
       "syupsEnvironTemperatureHigh": syupsEnvironTemperatureHigh,
       "syupsEnvironTemperatureCurrent": syupsEnvironTemperatureCurrent,
       "syupsEnvironHumidity": syupsEnvironHumidity,
       "syupsEnvironHumidityNumber": syupsEnvironHumidityNumber,
       "syupsEnvironHumidityTable": syupsEnvironHumidityTable,
       "syupsEnvironHumidityEntry": syupsEnvironHumidityEntry,
       "syupsEnvironHumidityIndex": syupsEnvironHumidityIndex,
       "syupsEnvironHumidityDescription": syupsEnvironHumidityDescription,
       "syupsEnvironHumidityLow": syupsEnvironHumidityLow,
       "syupsEnvironHumidityHigh": syupsEnvironHumidityHigh,
       "syupsEnvironHumidityCurrent": syupsEnvironHumidityCurrent,
       "syupsContact": syupsContact,
       "syupsContactNumber": syupsContactNumber,
       "syupsContactTable": syupsContactTable,
       "syupsContactEntry": syupsContactEntry,
       "syupsContactIndex": syupsContactIndex,
       "syupsContactDescription": syupsContactDescription,
       "syupsContactNormalState": syupsContactNormalState,
       "syupsContactMonitoringStatus": syupsContactMonitoringStatus,
       "syupsContactCurrentStatus": syupsContactCurrentStatus}
)
