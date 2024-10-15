# SNMP MIB module (RDN-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-SENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:13 2024
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

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rdnSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 5)
)
rdnSensor.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnSensorTable_Object = MibTable
rdnSensorTable = _RdnSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1)
)
if mibBuilder.loadTexts:
    rdnSensorTable.setStatus("current")
_RdnSensorEntry_Object = MibTableRow
rdnSensorEntry = _RdnSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1)
)
rdnSensorEntry.setIndexNames(
    (0, "RDN-SENSOR-MIB", "rdnSensorIndex"),
)
if mibBuilder.loadTexts:
    rdnSensorEntry.setStatus("current")
_RdnSensorIndex_Type = Integer32
_RdnSensorIndex_Object = MibTableColumn
rdnSensorIndex = _RdnSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 1),
    _RdnSensorIndex_Type()
)
rdnSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSensorIndex.setStatus("current")
_RdnSensorDescr_Type = DisplayString
_RdnSensorDescr_Object = MibTableColumn
rdnSensorDescr = _RdnSensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 2),
    _RdnSensorDescr_Type()
)
rdnSensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSensorDescr.setStatus("current")
_RdnSensorObjectID_Type = ObjectIdentifier
_RdnSensorObjectID_Object = MibTableColumn
rdnSensorObjectID = _RdnSensorObjectID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 3),
    _RdnSensorObjectID_Type()
)
rdnSensorObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSensorObjectID.setStatus("current")
_RdnSensorValue_Type = Integer32
_RdnSensorValue_Object = MibTableColumn
rdnSensorValue = _RdnSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 4),
    _RdnSensorValue_Type()
)
rdnSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSensorValue.setStatus("current")
_RdnSensorThresholdHigh_Type = Integer32
_RdnSensorThresholdHigh_Object = MibTableColumn
rdnSensorThresholdHigh = _RdnSensorThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 5),
    _RdnSensorThresholdHigh_Type()
)
rdnSensorThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSensorThresholdHigh.setStatus("current")
_RdnSensorThresholdLow_Type = Integer32
_RdnSensorThresholdLow_Object = MibTableColumn
rdnSensorThresholdLow = _RdnSensorThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 6),
    _RdnSensorThresholdLow_Type()
)
rdnSensorThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSensorThresholdLow.setStatus("current")


class _RdnSensorStatus_Type(Integer32):
    """Custom type rdnSensorStatus based on Integer32"""
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
        *(("aboveMax", 4),
          ("belowMin", 3),
          ("defective", 5),
          ("notPresent", 6),
          ("ok", 2),
          ("unknown", 1))
    )


_RdnSensorStatus_Type.__name__ = "Integer32"
_RdnSensorStatus_Object = MibTableColumn
rdnSensorStatus = _RdnSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 7),
    _RdnSensorStatus_Type()
)
rdnSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSensorStatus.setStatus("current")


class _RdnSensorNotificationEnable_Type(Integer32):
    """Custom type rdnSensorNotificationEnable based on Integer32"""
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


_RdnSensorNotificationEnable_Type.__name__ = "Integer32"
_RdnSensorNotificationEnable_Object = MibTableColumn
rdnSensorNotificationEnable = _RdnSensorNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 5, 1, 1, 8),
    _RdnSensorNotificationEnable_Type()
)
rdnSensorNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSensorNotificationEnable.setStatus("current")
_RdnSensorNotifications_ObjectIdentity = ObjectIdentity
rdnSensorNotifications = _RdnSensorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 5, 2)
)
_RdnSensorNotificationsPrefix_ObjectIdentity = ObjectIdentity
rdnSensorNotificationsPrefix = _RdnSensorNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

rdnSensorThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 5, 2, 0, 1)
)
rdnSensorThresholdExceeded.setObjects(
      *(("RDN-SENSOR-MIB", "rdnSensorIndex"),
        ("RDN-SENSOR-MIB", "rdnSensorDescr"),
        ("RDN-SENSOR-MIB", "rdnSensorObjectID"),
        ("RDN-SENSOR-MIB", "rdnSensorValue"),
        ("RDN-SENSOR-MIB", "rdnSensorThresholdHigh"),
        ("RDN-SENSOR-MIB", "rdnSensorThresholdLow"),
        ("RDN-SENSOR-MIB", "rdnSensorStatus"))
)
if mibBuilder.loadTexts:
    rdnSensorThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-SENSOR-MIB",
    **{"rdnSensor": rdnSensor,
       "rdnSensorTable": rdnSensorTable,
       "rdnSensorEntry": rdnSensorEntry,
       "rdnSensorIndex": rdnSensorIndex,
       "rdnSensorDescr": rdnSensorDescr,
       "rdnSensorObjectID": rdnSensorObjectID,
       "rdnSensorValue": rdnSensorValue,
       "rdnSensorThresholdHigh": rdnSensorThresholdHigh,
       "rdnSensorThresholdLow": rdnSensorThresholdLow,
       "rdnSensorStatus": rdnSensorStatus,
       "rdnSensorNotificationEnable": rdnSensorNotificationEnable,
       "rdnSensorNotifications": rdnSensorNotifications,
       "rdnSensorNotificationsPrefix": rdnSensorNotificationsPrefix,
       "rdnSensorThresholdExceeded": rdnSensorThresholdExceeded}
)
