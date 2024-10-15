# SNMP MIB module (HH3C-ARP-RATELIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ARP-RATELIMIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:29 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hh3cARPRatelimit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110)
)
hh3cARPRatelimit.setRevisions(
        ("2013-10-14 18:00",
         "2009-12-08 19:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cARPRatelimitObjects_ObjectIdentity = ObjectIdentity
hh3cARPRatelimitObjects = _Hh3cARPRatelimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1)
)
_Hh3cARPRatelimitTrap_ObjectIdentity = ObjectIdentity
hh3cARPRatelimitTrap = _Hh3cARPRatelimitTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1)
)
_Hh3cARPRatelimitTraps_ObjectIdentity = ObjectIdentity
hh3cARPRatelimitTraps = _Hh3cARPRatelimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 0)
)
_Hh3cARPRatelimitTrapObjects_ObjectIdentity = ObjectIdentity
hh3cARPRatelimitTrapObjects = _Hh3cARPRatelimitTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 1)
)
_Hh3cARPRatelimitTrapVer_Type = Unsigned32
_Hh3cARPRatelimitTrapVer_Object = MibScalar
hh3cARPRatelimitTrapVer = _Hh3cARPRatelimitTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 1, 1),
    _Hh3cARPRatelimitTrapVer_Type()
)
hh3cARPRatelimitTrapVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cARPRatelimitTrapVer.setStatus("current")
_Hh3cARPRatelimitTrapCount_Type = Unsigned32
_Hh3cARPRatelimitTrapCount_Object = MibScalar
hh3cARPRatelimitTrapCount = _Hh3cARPRatelimitTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 1, 2),
    _Hh3cARPRatelimitTrapCount_Type()
)
hh3cARPRatelimitTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cARPRatelimitTrapCount.setStatus("current")


class _Hh3cARPRatelimitTrapMsg_Type(OctetString):
    """Custom type hh3cARPRatelimitTrapMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_Hh3cARPRatelimitTrapMsg_Type.__name__ = "OctetString"
_Hh3cARPRatelimitTrapMsg_Object = MibScalar
hh3cARPRatelimitTrapMsg = _Hh3cARPRatelimitTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 1, 3),
    _Hh3cARPRatelimitTrapMsg_Type()
)
hh3cARPRatelimitTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cARPRatelimitTrapMsg.setStatus("current")
_Hh3cARPRatelimitConfig_ObjectIdentity = ObjectIdentity
hh3cARPRatelimitConfig = _Hh3cARPRatelimitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 2)
)
_Hh3cARPRatelimitConfigTable_Object = MibTable
hh3cARPRatelimitConfigTable = _Hh3cARPRatelimitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cARPRatelimitConfigTable.setStatus("current")
_Hh3cARPRatelimitConfigEntry_Object = MibTableRow
hh3cARPRatelimitConfigEntry = _Hh3cARPRatelimitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 2, 1, 1)
)
hh3cARPRatelimitConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cARPRatelimitConfigEntry.setStatus("current")
_Hh3cARPRatelimitValue_Type = Unsigned32
_Hh3cARPRatelimitValue_Object = MibTableColumn
hh3cARPRatelimitValue = _Hh3cARPRatelimitValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 2, 1, 1, 1),
    _Hh3cARPRatelimitValue_Type()
)
hh3cARPRatelimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cARPRatelimitValue.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cARPRatelimitOverspeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110, 1, 1, 0, 1)
)
hh3cARPRatelimitOverspeedTrap.setObjects(
      *(("HH3C-ARP-RATELIMIT-MIB", "hh3cARPRatelimitTrapVer"),
        ("HH3C-ARP-RATELIMIT-MIB", "hh3cARPRatelimitTrapCount"),
        ("HH3C-ARP-RATELIMIT-MIB", "hh3cARPRatelimitTrapMsg"))
)
if mibBuilder.loadTexts:
    hh3cARPRatelimitOverspeedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ARP-RATELIMIT-MIB",
    **{"hh3cARPRatelimit": hh3cARPRatelimit,
       "hh3cARPRatelimitObjects": hh3cARPRatelimitObjects,
       "hh3cARPRatelimitTrap": hh3cARPRatelimitTrap,
       "hh3cARPRatelimitTraps": hh3cARPRatelimitTraps,
       "hh3cARPRatelimitOverspeedTrap": hh3cARPRatelimitOverspeedTrap,
       "hh3cARPRatelimitTrapObjects": hh3cARPRatelimitTrapObjects,
       "hh3cARPRatelimitTrapVer": hh3cARPRatelimitTrapVer,
       "hh3cARPRatelimitTrapCount": hh3cARPRatelimitTrapCount,
       "hh3cARPRatelimitTrapMsg": hh3cARPRatelimitTrapMsg,
       "hh3cARPRatelimitConfig": hh3cARPRatelimitConfig,
       "hh3cARPRatelimitConfigTable": hh3cARPRatelimitConfigTable,
       "hh3cARPRatelimitConfigEntry": hh3cARPRatelimitConfigEntry,
       "hh3cARPRatelimitValue": hh3cARPRatelimitValue}
)
