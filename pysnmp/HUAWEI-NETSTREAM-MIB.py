# SNMP MIB module (HUAWEI-NETSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NETSTREAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:23 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleCompliance,
 ModuleIdentity,
 MibIdentifier,
 NotificationGroup,
 NotificationType,
 ObjectGroup,
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
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleCompliance",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationGroup",
    "NotificationType",
    "ObjectGroup",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwNetStreamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwNetStreamObjects_ObjectIdentity = ObjectIdentity
hwNetStreamObjects = _HwNetStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1)
)
_HwNetStreamlastchangedtime_Type = DateAndTime
_HwNetStreamlastchangedtime_Object = MibScalar
hwNetStreamlastchangedtime = _HwNetStreamlastchangedtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 1),
    _HwNetStreamlastchangedtime_Type()
)
hwNetStreamlastchangedtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetStreamlastchangedtime.setStatus("current")
_HwNetStreamIfIndexTable_Object = MibTable
hwNetStreamIfIndexTable = _HwNetStreamIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2)
)
if mibBuilder.loadTexts:
    hwNetStreamIfIndexTable.setStatus("current")
_HwNetStreamIfIndexEntry_Object = MibTableRow
hwNetStreamIfIndexEntry = _HwNetStreamIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1)
)
hwNetStreamIfIndexEntry.setIndexNames(
    (0, "HUAWEI-NETSTREAM-MIB", "hwNetStream16BitIndex"),
)
if mibBuilder.loadTexts:
    hwNetStreamIfIndexEntry.setStatus("current")


class _HwNetStream16BitIndex_Type(Integer32):
    """Custom type hwNetStream16BitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNetStream16BitIndex_Type.__name__ = "Integer32"
_HwNetStream16BitIndex_Object = MibTableColumn
hwNetStream16BitIndex = _HwNetStream16BitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1, 1),
    _HwNetStream16BitIndex_Type()
)
hwNetStream16BitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetStream16BitIndex.setStatus("current")
_HwifNet32BitIndex_Type = Integer32
_HwifNet32BitIndex_Object = MibTableColumn
hwifNet32BitIndex = _HwifNet32BitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1, 2),
    _HwifNet32BitIndex_Type()
)
hwifNet32BitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifNet32BitIndex.setStatus("current")
_HwNetStreamNotifications_ObjectIdentity = ObjectIdentity
hwNetStreamNotifications = _HwNetStreamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2)
)
_HwNetStreamTrapPrefix_ObjectIdentity = ObjectIdentity
hwNetStreamTrapPrefix = _HwNetStreamTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0)
)
_HwNetstreamConformance_ObjectIdentity = ObjectIdentity
hwNetstreamConformance = _HwNetstreamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3)
)
_HwNetstreamGroups_ObjectIdentity = ObjectIdentity
hwNetstreamGroups = _HwNetstreamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1)
)
_HwNetstreamCompliances_ObjectIdentity = ObjectIdentity
hwNetstreamCompliances = _HwNetstreamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 2)
)

# Managed Objects groups

hwNetstreamExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1, 2)
)
hwNetstreamExtGroup.setObjects(
      *(("HUAWEI-NETSTREAM-MIB", "hwNetStreamlastchangedtime"),
        ("HUAWEI-NETSTREAM-MIB", "hwNetStream16BitIndex"),
        ("HUAWEI-NETSTREAM-MIB", "hwifNet32BitIndex"))
)
if mibBuilder.loadTexts:
    hwNetstreamExtGroup.setStatus("current")


# Notification objects

hwNetStreamIndexStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 1)
)
if mibBuilder.loadTexts:
    hwNetStreamIndexStatusChanged.setStatus(
        "current"
    )

hwNetStreamIndexUsedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hwNetStreamIndexUsedUp.setStatus(
        "current"
    )

hwNetStreamSessionFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 3)
)
if mibBuilder.loadTexts:
    hwNetStreamSessionFull.setStatus(
        "current"
    )


# Notifications groups

hwNotificationExtGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1, 3)
)
hwNotificationExtGroup.setObjects(
      *(("HUAWEI-NETSTREAM-MIB", "hwNetStreamIndexUsedUp"),
        ("HUAWEI-NETSTREAM-MIB", "hwNetStreamIndexStatusChanged"))
)
if mibBuilder.loadTexts:
    hwNotificationExtGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwNetstreamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwNetstreamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NETSTREAM-MIB",
    **{"hwNetStreamMIB": hwNetStreamMIB,
       "hwNetStreamObjects": hwNetStreamObjects,
       "hwNetStreamlastchangedtime": hwNetStreamlastchangedtime,
       "hwNetStreamIfIndexTable": hwNetStreamIfIndexTable,
       "hwNetStreamIfIndexEntry": hwNetStreamIfIndexEntry,
       "hwNetStream16BitIndex": hwNetStream16BitIndex,
       "hwifNet32BitIndex": hwifNet32BitIndex,
       "hwNetStreamNotifications": hwNetStreamNotifications,
       "hwNetStreamTrapPrefix": hwNetStreamTrapPrefix,
       "hwNetStreamIndexStatusChanged": hwNetStreamIndexStatusChanged,
       "hwNetStreamIndexUsedUp": hwNetStreamIndexUsedUp,
       "hwNetStreamSessionFull": hwNetStreamSessionFull,
       "hwNetstreamConformance": hwNetstreamConformance,
       "hwNetstreamGroups": hwNetstreamGroups,
       "hwNetstreamExtGroup": hwNetstreamExtGroup,
       "hwNotificationExtGroup": hwNotificationExtGroup,
       "hwNetstreamCompliances": hwNetstreamCompliances,
       "hwNetstreamCompliance": hwNetstreamCompliance}
)
