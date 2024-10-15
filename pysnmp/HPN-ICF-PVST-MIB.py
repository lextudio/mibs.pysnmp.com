# SNMP MIB module (HPN-ICF-PVST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PVST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:34 2024
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

hpnicfPvst = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131)
)
hpnicfPvst.setRevisions(
        ("2014-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPvstObjects_ObjectIdentity = ObjectIdentity
hpnicfPvstObjects = _HpnicfPvstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1)
)
_HpnicfPvstVlanConfigTable_Object = MibTable
hpnicfPvstVlanConfigTable = _HpnicfPvstVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanConfigTable.setStatus("current")
_HpnicfPvstVlanConfigEntry_Object = MibTableRow
hpnicfPvstVlanConfigEntry = _HpnicfPvstVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 1, 1)
)
hpnicfPvstVlanConfigEntry.setIndexNames(
    (0, "HPN-ICF-PVST-MIB", "hpnicfPvstVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanConfigEntry.setStatus("current")


class _HpnicfPvstVlanID_Type(Integer32):
    """Custom type hpnicfPvstVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfPvstVlanID_Type.__name__ = "Integer32"
_HpnicfPvstVlanID_Object = MibTableColumn
hpnicfPvstVlanID = _HpnicfPvstVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 1, 1, 1),
    _HpnicfPvstVlanID_Type()
)
hpnicfPvstVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPvstVlanID.setStatus("current")
_HpnicfPvstVlanPortConfigTable_Object = MibTable
hpnicfPvstVlanPortConfigTable = _HpnicfPvstVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanPortConfigTable.setStatus("current")
_HpnicfPvstVlanPortConfigEntry_Object = MibTableRow
hpnicfPvstVlanPortConfigEntry = _HpnicfPvstVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 2, 1)
)
hpnicfPvstVlanPortConfigEntry.setIndexNames(
    (0, "HPN-ICF-PVST-MIB", "hpnicfPvstPortVlanID"),
    (0, "HPN-ICF-PVST-MIB", "hpnicfPvstPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanPortConfigEntry.setStatus("current")


class _HpnicfPvstPortVlanID_Type(Integer32):
    """Custom type hpnicfPvstPortVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfPvstPortVlanID_Type.__name__ = "Integer32"
_HpnicfPvstPortVlanID_Object = MibTableColumn
hpnicfPvstPortVlanID = _HpnicfPvstPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 2, 1, 1),
    _HpnicfPvstPortVlanID_Type()
)
hpnicfPvstPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPvstPortVlanID.setStatus("current")


class _HpnicfPvstPortIndex_Type(Integer32):
    """Custom type hpnicfPvstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPvstPortIndex_Type.__name__ = "Integer32"
_HpnicfPvstPortIndex_Object = MibTableColumn
hpnicfPvstPortIndex = _HpnicfPvstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 1, 2, 1, 2),
    _HpnicfPvstPortIndex_Type()
)
hpnicfPvstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPvstPortIndex.setStatus("current")
_HpnicfPvstNotifications_ObjectIdentity = ObjectIdentity
hpnicfPvstNotifications = _HpnicfPvstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 2)
)
_HpnicfPvstEvents_ObjectIdentity = ObjectIdentity
hpnicfPvstEvents = _HpnicfPvstEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfPvstVlanPortDetectedTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 2, 0, 1)
)
hpnicfPvstVlanPortDetectedTc.setObjects(
      *(("HPN-ICF-PVST-MIB", "hpnicfPvstPortVlanID"),
        ("HPN-ICF-PVST-MIB", "hpnicfPvstPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanPortDetectedTc.setStatus(
        "current"
    )

hpnicfPvstVlanPortRcvdTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 131, 2, 0, 2)
)
hpnicfPvstVlanPortRcvdTc.setObjects(
      *(("HPN-ICF-PVST-MIB", "hpnicfPvstPortVlanID"),
        ("HPN-ICF-PVST-MIB", "hpnicfPvstPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPvstVlanPortRcvdTc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PVST-MIB",
    **{"hpnicfPvst": hpnicfPvst,
       "hpnicfPvstObjects": hpnicfPvstObjects,
       "hpnicfPvstVlanConfigTable": hpnicfPvstVlanConfigTable,
       "hpnicfPvstVlanConfigEntry": hpnicfPvstVlanConfigEntry,
       "hpnicfPvstVlanID": hpnicfPvstVlanID,
       "hpnicfPvstVlanPortConfigTable": hpnicfPvstVlanPortConfigTable,
       "hpnicfPvstVlanPortConfigEntry": hpnicfPvstVlanPortConfigEntry,
       "hpnicfPvstPortVlanID": hpnicfPvstPortVlanID,
       "hpnicfPvstPortIndex": hpnicfPvstPortIndex,
       "hpnicfPvstNotifications": hpnicfPvstNotifications,
       "hpnicfPvstEvents": hpnicfPvstEvents,
       "hpnicfPvstVlanPortDetectedTc": hpnicfPvstVlanPortDetectedTc,
       "hpnicfPvstVlanPortRcvdTc": hpnicfPvstVlanPortRcvdTc}
)
