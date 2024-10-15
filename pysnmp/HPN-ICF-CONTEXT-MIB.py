# SNMP MIB module (HPN-ICF-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-CONTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:36 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfContext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154)
)
hpnicfContext.setRevisions(
        ("2014-03-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfContextTables_ObjectIdentity = ObjectIdentity
hpnicfContextTables = _HpnicfContextTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1)
)
_HpnicfContextControl_ObjectIdentity = ObjectIdentity
hpnicfContextControl = _HpnicfContextControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1)
)
_HpnicfContextControlTable_Object = MibTable
hpnicfContextControlTable = _HpnicfContextControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfContextControlTable.setStatus("current")
_HpnicfContextControlEntry_Object = MibTableRow
hpnicfContextControlEntry = _HpnicfContextControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1)
)
hpnicfContextControlEntry.setIndexNames(
    (0, "HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"),
)
if mibBuilder.loadTexts:
    hpnicfContextControlEntry.setStatus("current")


class _HpnicfContextIndex_Type(Integer32):
    """Custom type hpnicfContextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfContextIndex_Type.__name__ = "Integer32"
_HpnicfContextIndex_Object = MibTableColumn
hpnicfContextIndex = _HpnicfContextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1, 1),
    _HpnicfContextIndex_Type()
)
hpnicfContextIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfContextIndex.setStatus("current")


class _HpnicfContextName_Type(DisplayString):
    """Custom type hpnicfContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfContextName_Type.__name__ = "DisplayString"
_HpnicfContextName_Object = MibTableColumn
hpnicfContextName = _HpnicfContextName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1, 2),
    _HpnicfContextName_Type()
)
hpnicfContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfContextName.setStatus("current")
_HpnicfContextNotification_ObjectIdentity = ObjectIdentity
hpnicfContextNotification = _HpnicfContextNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8)
)
_HpnicfContextNotificationObjects_ObjectIdentity = ObjectIdentity
hpnicfContextNotificationObjects = _HpnicfContextNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0)
)

# Managed Objects groups


# Notification objects

hpnicfContextStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0, 1)
)
hpnicfContextStateChangeToActive.setObjects(
      *(("HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"),
        ("HPN-ICF-CONTEXT-MIB", "hpnicfContextName"))
)
if mibBuilder.loadTexts:
    hpnicfContextStateChangeToActive.setStatus(
        "current"
    )

hpnicfContextStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0, 2)
)
hpnicfContextStateChangeToInactive.setObjects(
      *(("HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"),
        ("HPN-ICF-CONTEXT-MIB", "hpnicfContextName"))
)
if mibBuilder.loadTexts:
    hpnicfContextStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-CONTEXT-MIB",
    **{"hpnicfContext": hpnicfContext,
       "hpnicfContextTables": hpnicfContextTables,
       "hpnicfContextControl": hpnicfContextControl,
       "hpnicfContextControlTable": hpnicfContextControlTable,
       "hpnicfContextControlEntry": hpnicfContextControlEntry,
       "hpnicfContextIndex": hpnicfContextIndex,
       "hpnicfContextName": hpnicfContextName,
       "hpnicfContextNotification": hpnicfContextNotification,
       "hpnicfContextNotificationObjects": hpnicfContextNotificationObjects,
       "hpnicfContextStateChangeToActive": hpnicfContextStateChangeToActive,
       "hpnicfContextStateChangeToInactive": hpnicfContextStateChangeToInactive}
)
