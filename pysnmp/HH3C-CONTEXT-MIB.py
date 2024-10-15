# SNMP MIB module (HH3C-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-CONTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:37 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cContext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154)
)
hh3cContext.setRevisions(
        ("2014-03-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cContextTables_ObjectIdentity = ObjectIdentity
hh3cContextTables = _Hh3cContextTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1)
)
_Hh3cContextControl_ObjectIdentity = ObjectIdentity
hh3cContextControl = _Hh3cContextControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1, 1)
)
_Hh3cContextControlTable_Object = MibTable
hh3cContextControlTable = _Hh3cContextControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cContextControlTable.setStatus("current")
_Hh3cContextControlEntry_Object = MibTableRow
hh3cContextControlEntry = _Hh3cContextControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1, 1, 1, 1)
)
hh3cContextControlEntry.setIndexNames(
    (0, "HH3C-CONTEXT-MIB", "hh3cContextIndex"),
)
if mibBuilder.loadTexts:
    hh3cContextControlEntry.setStatus("current")


class _Hh3cContextIndex_Type(Integer32):
    """Custom type hh3cContextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cContextIndex_Type.__name__ = "Integer32"
_Hh3cContextIndex_Object = MibTableColumn
hh3cContextIndex = _Hh3cContextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1, 1, 1, 1, 1),
    _Hh3cContextIndex_Type()
)
hh3cContextIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cContextIndex.setStatus("current")


class _Hh3cContextName_Type(DisplayString):
    """Custom type hh3cContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cContextName_Type.__name__ = "DisplayString"
_Hh3cContextName_Object = MibTableColumn
hh3cContextName = _Hh3cContextName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 1, 1, 1, 1, 2),
    _Hh3cContextName_Type()
)
hh3cContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cContextName.setStatus("current")
_Hh3cContextNotification_ObjectIdentity = ObjectIdentity
hh3cContextNotification = _Hh3cContextNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 8)
)
_Hh3cContextNotificationObjects_ObjectIdentity = ObjectIdentity
hh3cContextNotificationObjects = _Hh3cContextNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 8, 0)
)

# Managed Objects groups


# Notification objects

hh3cContextStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 8, 0, 1)
)
hh3cContextStateChangeToActive.setObjects(
      *(("HH3C-CONTEXT-MIB", "hh3cContextIndex"),
        ("HH3C-CONTEXT-MIB", "hh3cContextName"))
)
if mibBuilder.loadTexts:
    hh3cContextStateChangeToActive.setStatus(
        "current"
    )

hh3cContextStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154, 8, 0, 2)
)
hh3cContextStateChangeToInactive.setObjects(
      *(("HH3C-CONTEXT-MIB", "hh3cContextIndex"),
        ("HH3C-CONTEXT-MIB", "hh3cContextName"))
)
if mibBuilder.loadTexts:
    hh3cContextStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CONTEXT-MIB",
    **{"hh3cContext": hh3cContext,
       "hh3cContextTables": hh3cContextTables,
       "hh3cContextControl": hh3cContextControl,
       "hh3cContextControlTable": hh3cContextControlTable,
       "hh3cContextControlEntry": hh3cContextControlEntry,
       "hh3cContextIndex": hh3cContextIndex,
       "hh3cContextName": hh3cContextName,
       "hh3cContextNotification": hh3cContextNotification,
       "hh3cContextNotificationObjects": hh3cContextNotificationObjects,
       "hh3cContextStateChangeToActive": hh3cContextStateChangeToActive,
       "hh3cContextStateChangeToInactive": hh3cContextStateChangeToInactive}
)
