# SNMP MIB module (CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanPersistentXgcpEventsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18)
)
ciscoWanPersistentXgcpEventsMIB.setRevisions(
        ("2003-10-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanPersistentXgcpEventsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanPersistentXgcpEventsMIBObjects = _CiscoWanPersistentXgcpEventsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1)
)
_PersistentXgcpEvents_ObjectIdentity = ObjectIdentity
persistentXgcpEvents = _PersistentXgcpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1)
)
_PersistentXgcpEventsTable_Object = MibTable
persistentXgcpEventsTable = _PersistentXgcpEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    persistentXgcpEventsTable.setStatus("current")
_PersistentXgcpEventsEntry_Object = MibTableRow
persistentXgcpEventsEntry = _PersistentXgcpEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1)
)
persistentXgcpEventsEntry.setIndexNames(
    (0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"),
)
if mibBuilder.loadTexts:
    persistentXgcpEventsEntry.setStatus("current")


class _PersistentXgcpEventNum_Type(Integer32):
    """Custom type persistentXgcpEventNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PersistentXgcpEventNum_Type.__name__ = "Integer32"
_PersistentXgcpEventNum_Object = MibTableColumn
persistentXgcpEventNum = _PersistentXgcpEventNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1),
    _PersistentXgcpEventNum_Type()
)
persistentXgcpEventNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    persistentXgcpEventNum.setStatus("current")


class _PersistentXgcpEventName_Type(SnmpAdminString):
    """Custom type persistentXgcpEventName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PersistentXgcpEventName_Type.__name__ = "SnmpAdminString"
_PersistentXgcpEventName_Object = MibTableColumn
persistentXgcpEventName = _PersistentXgcpEventName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2),
    _PersistentXgcpEventName_Type()
)
persistentXgcpEventName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    persistentXgcpEventName.setStatus("current")
_PersistentXgcpEventRowStatus_Type = RowStatus
_PersistentXgcpEventRowStatus_Object = MibTableColumn
persistentXgcpEventRowStatus = _PersistentXgcpEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3),
    _PersistentXgcpEventRowStatus_Type()
)
persistentXgcpEventRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    persistentXgcpEventRowStatus.setStatus("current")
_PersistentXgcpEventsMIBConformance_ObjectIdentity = ObjectIdentity
persistentXgcpEventsMIBConformance = _PersistentXgcpEventsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 2)
)
_PersistentXgcpEventsMIBCompliances_ObjectIdentity = ObjectIdentity
persistentXgcpEventsMIBCompliances = _PersistentXgcpEventsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1)
)
_PersistentXgcpEventsMIBGroups_ObjectIdentity = ObjectIdentity
persistentXgcpEventsMIBGroups = _PersistentXgcpEventsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2)
)

# Managed Objects groups

persistentXgcpEventsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)
)
persistentXgcpEventsMIBGroup.setObjects(
      *(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"),
        ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
)
if mibBuilder.loadTexts:
    persistentXgcpEventsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

persistentXgcpEventsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    persistentXgcpEventsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB",
    **{"ciscoWanPersistentXgcpEventsMIB": ciscoWanPersistentXgcpEventsMIB,
       "ciscoWanPersistentXgcpEventsMIBObjects": ciscoWanPersistentXgcpEventsMIBObjects,
       "persistentXgcpEvents": persistentXgcpEvents,
       "persistentXgcpEventsTable": persistentXgcpEventsTable,
       "persistentXgcpEventsEntry": persistentXgcpEventsEntry,
       "persistentXgcpEventNum": persistentXgcpEventNum,
       "persistentXgcpEventName": persistentXgcpEventName,
       "persistentXgcpEventRowStatus": persistentXgcpEventRowStatus,
       "persistentXgcpEventsMIBConformance": persistentXgcpEventsMIBConformance,
       "persistentXgcpEventsMIBCompliances": persistentXgcpEventsMIBCompliances,
       "persistentXgcpEventsMIBCompliance": persistentXgcpEventsMIBCompliance,
       "persistentXgcpEventsMIBGroups": persistentXgcpEventsMIBGroups,
       "persistentXgcpEventsMIBGroup": persistentXgcpEventsMIBGroup}
)
