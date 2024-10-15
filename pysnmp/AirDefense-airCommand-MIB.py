# SNMP MIB module (AirDefense-airCommand-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AirDefense-airCommand-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:04 2024
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

_AirDefense_ObjectIdentity = ObjectIdentity
airDefense = _AirDefense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13416)
)
_AirDefenseProducts_ObjectIdentity = ObjectIdentity
airDefenseProducts = _AirDefenseProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13416, 1)
)
_AirCommand_ObjectIdentity = ObjectIdentity
airCommand = _AirCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1)
)
_AirCommandEventTable_Object = MibTable
airCommandEventTable = _AirCommandEventTable_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1)
)
if mibBuilder.loadTexts:
    airCommandEventTable.setStatus("current")
_AirCommandEventEntry_Object = MibTableRow
airCommandEventEntry = _AirCommandEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1, 1)
)
airCommandEventEntry.setIndexNames(
    (0, "AirDefense-airCommand-MIB", "airCommandEventId"),
)
if mibBuilder.loadTexts:
    airCommandEventEntry.setStatus("current")
_AirCommandEventId_Type = Integer32
_AirCommandEventId_Object = MibTableColumn
airCommandEventId = _AirCommandEventId_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1, 1, 1),
    _AirCommandEventId_Type()
)
airCommandEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airCommandEventId.setStatus("current")


class _AirCommandEventPriority_Type(Integer32):
    """Custom type airCommandEventPriority based on Integer32"""
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
          ("low", 4),
          ("major", 2),
          ("minor", 3))
    )


_AirCommandEventPriority_Type.__name__ = "Integer32"
_AirCommandEventPriority_Object = MibTableColumn
airCommandEventPriority = _AirCommandEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1, 1, 2),
    _AirCommandEventPriority_Type()
)
airCommandEventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airCommandEventPriority.setStatus("current")


class _AirCommandEventDescriptor_Type(OctetString):
    """Custom type airCommandEventDescriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AirCommandEventDescriptor_Type.__name__ = "OctetString"
_AirCommandEventDescriptor_Object = MibTableColumn
airCommandEventDescriptor = _AirCommandEventDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1, 1, 3),
    _AirCommandEventDescriptor_Type()
)
airCommandEventDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airCommandEventDescriptor.setStatus("current")
_AirCommandEventCount_Type = Integer32
_AirCommandEventCount_Object = MibTableColumn
airCommandEventCount = _AirCommandEventCount_Object(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 1, 1, 4),
    _AirCommandEventCount_Type()
)
airCommandEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airCommandEventCount.setStatus("current")

# Managed Objects groups


# Notification objects

airCommandAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13416, 1, 1, 2)
)
airCommandAlarm.setObjects(
      *(("AirDefense-airCommand-MIB", "airCommandEventPriority"),
        ("AirDefense-airCommand-MIB", "airCommandEventDescriptor"),
        ("AirDefense-airCommand-MIB", "airCommandEventCount"))
)
if mibBuilder.loadTexts:
    airCommandAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AirDefense-airCommand-MIB",
    **{"airDefense": airDefense,
       "airDefenseProducts": airDefenseProducts,
       "airCommand": airCommand,
       "airCommandEventTable": airCommandEventTable,
       "airCommandEventEntry": airCommandEventEntry,
       "airCommandEventId": airCommandEventId,
       "airCommandEventPriority": airCommandEventPriority,
       "airCommandEventDescriptor": airCommandEventDescriptor,
       "airCommandEventCount": airCommandEventCount,
       "airCommandAlarm": airCommandAlarm}
)
