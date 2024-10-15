# SNMP MIB module (SONUS-ALARM-CONTACT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ALARM-CONTACT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:50 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex")

(sonusSystemMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSystemMIBs")

(SonusAdminState,
 SonusBoolean,
 SonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusBoolean",
    "SonusShelfIndex")


# MODULE-IDENTITY

sonusAlarmManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusAlarmManagerMIBObjects_ObjectIdentity = ObjectIdentity
sonusAlarmManagerMIBObjects = _SonusAlarmManagerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1)
)
_SonusAlarmOutAdmnTable_Object = MibTable
sonusAlarmOutAdmnTable = _SonusAlarmOutAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnTable.setStatus("current")
_SonusAlarmOutAdmnEntry_Object = MibTableRow
sonusAlarmOutAdmnEntry = _SonusAlarmOutAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1)
)
sonusAlarmOutAdmnEntry.setIndexNames(
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutAdmnShelfIndex"),
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutAdmnRelayIndex"),
)
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnEntry.setStatus("current")
_SonusAlarmOutAdmnShelfIndex_Type = SonusShelfIndex
_SonusAlarmOutAdmnShelfIndex_Object = MibTableColumn
sonusAlarmOutAdmnShelfIndex = _SonusAlarmOutAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 1),
    _SonusAlarmOutAdmnShelfIndex_Type()
)
sonusAlarmOutAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnShelfIndex.setStatus("current")


class _SonusAlarmOutAdmnRelayIndex_Type(Integer32):
    """Custom type sonusAlarmOutAdmnRelayIndex based on Integer32"""
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
        *(("critical-2", 2),
          ("major-3", 3),
          ("minor-4", 4),
          ("shelfpwr-1", 1),
          ("user-5", 5))
    )


_SonusAlarmOutAdmnRelayIndex_Type.__name__ = "Integer32"
_SonusAlarmOutAdmnRelayIndex_Object = MibTableColumn
sonusAlarmOutAdmnRelayIndex = _SonusAlarmOutAdmnRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 2),
    _SonusAlarmOutAdmnRelayIndex_Type()
)
sonusAlarmOutAdmnRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnRelayIndex.setStatus("current")


class _SonusAlarmOutAdmnOperState_Type(SonusAdminState):
    """Custom type sonusAlarmOutAdmnOperState based on SonusAdminState"""


_SonusAlarmOutAdmnOperState_Object = MibTableColumn
sonusAlarmOutAdmnOperState = _SonusAlarmOutAdmnOperState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 3),
    _SonusAlarmOutAdmnOperState_Type()
)
sonusAlarmOutAdmnOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnOperState.setStatus("current")


class _SonusAlarmOutAdmnValue_Type(Integer32):
    """Custom type sonusAlarmOutAdmnValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("clear", 1))
    )


_SonusAlarmOutAdmnValue_Type.__name__ = "Integer32"
_SonusAlarmOutAdmnValue_Object = MibTableColumn
sonusAlarmOutAdmnValue = _SonusAlarmOutAdmnValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 4),
    _SonusAlarmOutAdmnValue_Type()
)
sonusAlarmOutAdmnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnValue.setStatus("current")


class _SonusAlarmOutAdmnSense_Type(Integer32):
    """Custom type sonusAlarmOutAdmnSense based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_SonusAlarmOutAdmnSense_Type.__name__ = "Integer32"
_SonusAlarmOutAdmnSense_Object = MibTableColumn
sonusAlarmOutAdmnSense = _SonusAlarmOutAdmnSense_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 5),
    _SonusAlarmOutAdmnSense_Type()
)
sonusAlarmOutAdmnSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnSense.setStatus("current")


class _SonusAlarmOutAdmnStartDelay_Type(Integer32):
    """Custom type sonusAlarmOutAdmnStartDelay based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SonusAlarmOutAdmnStartDelay_Type.__name__ = "Integer32"
_SonusAlarmOutAdmnStartDelay_Object = MibTableColumn
sonusAlarmOutAdmnStartDelay = _SonusAlarmOutAdmnStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 6),
    _SonusAlarmOutAdmnStartDelay_Type()
)
sonusAlarmOutAdmnStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnStartDelay.setStatus("current")


class _SonusAlarmOutAdmnCutoff_Type(Integer32):
    """Custom type sonusAlarmOutAdmnCutoff based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SonusAlarmOutAdmnCutoff_Type.__name__ = "Integer32"
_SonusAlarmOutAdmnCutoff_Object = MibTableColumn
sonusAlarmOutAdmnCutoff = _SonusAlarmOutAdmnCutoff_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 7),
    _SonusAlarmOutAdmnCutoff_Type()
)
sonusAlarmOutAdmnCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAlarmOutAdmnCutoff.setStatus("current")
_SonusAlarmOutStatTable_Object = MibTable
sonusAlarmOutStatTable = _SonusAlarmOutStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    sonusAlarmOutStatTable.setStatus("current")
_SonusAlarmOutStatEntry_Object = MibTableRow
sonusAlarmOutStatEntry = _SonusAlarmOutStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1)
)
sonusAlarmOutStatEntry.setIndexNames(
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutStatShelfIndex"),
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutStatRelayIndex"),
)
if mibBuilder.loadTexts:
    sonusAlarmOutStatEntry.setStatus("current")
_SonusAlarmOutStatShelfIndex_Type = SonusShelfIndex
_SonusAlarmOutStatShelfIndex_Object = MibTableColumn
sonusAlarmOutStatShelfIndex = _SonusAlarmOutStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 1),
    _SonusAlarmOutStatShelfIndex_Type()
)
sonusAlarmOutStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutStatShelfIndex.setStatus("current")


class _SonusAlarmOutStatRelayIndex_Type(Integer32):
    """Custom type sonusAlarmOutStatRelayIndex based on Integer32"""
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
        *(("critical-2", 2),
          ("major-3", 3),
          ("minor-4", 4),
          ("shelfpwr-1", 1),
          ("user-5", 5))
    )


_SonusAlarmOutStatRelayIndex_Type.__name__ = "Integer32"
_SonusAlarmOutStatRelayIndex_Object = MibTableColumn
sonusAlarmOutStatRelayIndex = _SonusAlarmOutStatRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 2),
    _SonusAlarmOutStatRelayIndex_Type()
)
sonusAlarmOutStatRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutStatRelayIndex.setStatus("current")


class _SonusAlarmOutStatStatus_Type(Integer32):
    """Custom type sonusAlarmOutStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("clear", 1))
    )


_SonusAlarmOutStatStatus_Type.__name__ = "Integer32"
_SonusAlarmOutStatStatus_Object = MibTableColumn
sonusAlarmOutStatStatus = _SonusAlarmOutStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 3),
    _SonusAlarmOutStatStatus_Type()
)
sonusAlarmOutStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutStatStatus.setStatus("current")
_SonusAlarmOutStatStartDelay_Type = SonusBoolean
_SonusAlarmOutStatStartDelay_Object = MibTableColumn
sonusAlarmOutStatStartDelay = _SonusAlarmOutStatStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 4),
    _SonusAlarmOutStatStartDelay_Type()
)
sonusAlarmOutStatStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmOutStatStartDelay.setStatus("current")
_SonusAlarmInStatTable_Object = MibTable
sonusAlarmInStatTable = _SonusAlarmInStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    sonusAlarmInStatTable.setStatus("current")
_SonusAlarmInStatEntry_Object = MibTableRow
sonusAlarmInStatEntry = _SonusAlarmInStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1)
)
sonusAlarmInStatEntry.setIndexNames(
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmInStatShelfIndex"),
    (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmInStatPort"),
)
if mibBuilder.loadTexts:
    sonusAlarmInStatEntry.setStatus("current")
_SonusAlarmInStatShelfIndex_Type = SonusShelfIndex
_SonusAlarmInStatShelfIndex_Object = MibTableColumn
sonusAlarmInStatShelfIndex = _SonusAlarmInStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 1),
    _SonusAlarmInStatShelfIndex_Type()
)
sonusAlarmInStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmInStatShelfIndex.setStatus("current")


class _SonusAlarmInStatPort_Type(Integer32):
    """Custom type sonusAlarmInStatPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SonusAlarmInStatPort_Type.__name__ = "Integer32"
_SonusAlarmInStatPort_Object = MibTableColumn
sonusAlarmInStatPort = _SonusAlarmInStatPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 2),
    _SonusAlarmInStatPort_Type()
)
sonusAlarmInStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmInStatPort.setStatus("current")


class _SonusAlarmInStatStatus_Type(Integer32):
    """Custom type sonusAlarmInStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_SonusAlarmInStatStatus_Type.__name__ = "Integer32"
_SonusAlarmInStatStatus_Object = MibTableColumn
sonusAlarmInStatStatus = _SonusAlarmInStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 3),
    _SonusAlarmInStatStatus_Type()
)
sonusAlarmInStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmInStatStatus.setStatus("current")
_SonusAlarmManagerMIBNotifications_ObjectIdentity = ObjectIdentity
sonusAlarmManagerMIBNotifications = _SonusAlarmManagerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2)
)
_SonusAlarmManagerMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusAlarmManagerMIBNotificationsPrefix = _SonusAlarmManagerMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 0)
)
_SonusAlarmManagerMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusAlarmManagerMIBNotificationsObjects = _SonusAlarmManagerMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1)
)
_SonusAlarmPortIndex_Type = Integer32
_SonusAlarmPortIndex_Object = MibScalar
sonusAlarmPortIndex = _SonusAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1, 1),
    _SonusAlarmPortIndex_Type()
)
sonusAlarmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmPortIndex.setStatus("current")


class _SonusAlarmPortState_Type(Integer32):
    """Custom type sonusAlarmPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_SonusAlarmPortState_Type.__name__ = "Integer32"
_SonusAlarmPortState_Object = MibScalar
sonusAlarmPortState = _SonusAlarmPortState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1, 2),
    _SonusAlarmPortState_Type()
)
sonusAlarmPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAlarmPortState.setStatus("current")

# Managed Objects groups


# Notification objects

sonusAlarmManagerInboundNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 0, 1)
)
sonusAlarmManagerInboundNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-ALARM-CONTACT-MIB", "sonusAlarmPortIndex"),
        ("SONUS-ALARM-CONTACT-MIB", "sonusAlarmPortState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAlarmManagerInboundNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ALARM-CONTACT-MIB",
    **{"sonusAlarmManagerMIB": sonusAlarmManagerMIB,
       "sonusAlarmManagerMIBObjects": sonusAlarmManagerMIBObjects,
       "sonusAlarmOutAdmnTable": sonusAlarmOutAdmnTable,
       "sonusAlarmOutAdmnEntry": sonusAlarmOutAdmnEntry,
       "sonusAlarmOutAdmnShelfIndex": sonusAlarmOutAdmnShelfIndex,
       "sonusAlarmOutAdmnRelayIndex": sonusAlarmOutAdmnRelayIndex,
       "sonusAlarmOutAdmnOperState": sonusAlarmOutAdmnOperState,
       "sonusAlarmOutAdmnValue": sonusAlarmOutAdmnValue,
       "sonusAlarmOutAdmnSense": sonusAlarmOutAdmnSense,
       "sonusAlarmOutAdmnStartDelay": sonusAlarmOutAdmnStartDelay,
       "sonusAlarmOutAdmnCutoff": sonusAlarmOutAdmnCutoff,
       "sonusAlarmOutStatTable": sonusAlarmOutStatTable,
       "sonusAlarmOutStatEntry": sonusAlarmOutStatEntry,
       "sonusAlarmOutStatShelfIndex": sonusAlarmOutStatShelfIndex,
       "sonusAlarmOutStatRelayIndex": sonusAlarmOutStatRelayIndex,
       "sonusAlarmOutStatStatus": sonusAlarmOutStatStatus,
       "sonusAlarmOutStatStartDelay": sonusAlarmOutStatStartDelay,
       "sonusAlarmInStatTable": sonusAlarmInStatTable,
       "sonusAlarmInStatEntry": sonusAlarmInStatEntry,
       "sonusAlarmInStatShelfIndex": sonusAlarmInStatShelfIndex,
       "sonusAlarmInStatPort": sonusAlarmInStatPort,
       "sonusAlarmInStatStatus": sonusAlarmInStatStatus,
       "sonusAlarmManagerMIBNotifications": sonusAlarmManagerMIBNotifications,
       "sonusAlarmManagerMIBNotificationsPrefix": sonusAlarmManagerMIBNotificationsPrefix,
       "sonusAlarmManagerInboundNotification": sonusAlarmManagerInboundNotification,
       "sonusAlarmManagerMIBNotificationsObjects": sonusAlarmManagerMIBNotificationsObjects,
       "sonusAlarmPortIndex": sonusAlarmPortIndex,
       "sonusAlarmPortState": sonusAlarmPortState}
)
