# SNMP MIB module (JUNIPER-LSYSSP-ZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-ZONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:40 2024
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

(jnxLsysSpZone,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpZone")

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

jnxLsysSpZoneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpZoneObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpZoneObjects = _JnxLsysSpZoneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1)
)
_JnxLsysSpZoneTable_Object = MibTable
jnxLsysSpZoneTable = _JnxLsysSpZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpZoneTable.setStatus("current")
_JnxLsysSpZoneEntry_Object = MibTableRow
jnxLsysSpZoneEntry = _JnxLsysSpZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1)
)
jnxLsysSpZoneEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-ZONE-MIB", "jnxLsysSpZoneLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpZoneEntry.setStatus("current")


class _JnxLsysSpZoneLsysName_Type(DisplayString):
    """Custom type jnxLsysSpZoneLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpZoneLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpZoneLsysName_Object = MibTableColumn
jnxLsysSpZoneLsysName = _JnxLsysSpZoneLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1, 1),
    _JnxLsysSpZoneLsysName_Type()
)
jnxLsysSpZoneLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpZoneLsysName.setStatus("current")


class _JnxLsysSpZoneProfileName_Type(DisplayString):
    """Custom type jnxLsysSpZoneProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpZoneProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpZoneProfileName_Object = MibTableColumn
jnxLsysSpZoneProfileName = _JnxLsysSpZoneProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1, 2),
    _JnxLsysSpZoneProfileName_Type()
)
jnxLsysSpZoneProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneProfileName.setStatus("current")
_JnxLsysSpZoneUsage_Type = Unsigned32
_JnxLsysSpZoneUsage_Object = MibTableColumn
jnxLsysSpZoneUsage = _JnxLsysSpZoneUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1, 3),
    _JnxLsysSpZoneUsage_Type()
)
jnxLsysSpZoneUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneUsage.setStatus("current")
_JnxLsysSpZoneReserved_Type = Unsigned32
_JnxLsysSpZoneReserved_Object = MibTableColumn
jnxLsysSpZoneReserved = _JnxLsysSpZoneReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1, 4),
    _JnxLsysSpZoneReserved_Type()
)
jnxLsysSpZoneReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneReserved.setStatus("current")
_JnxLsysSpZoneMaximum_Type = Unsigned32
_JnxLsysSpZoneMaximum_Object = MibTableColumn
jnxLsysSpZoneMaximum = _JnxLsysSpZoneMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 1, 1, 1, 5),
    _JnxLsysSpZoneMaximum_Type()
)
jnxLsysSpZoneMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneMaximum.setStatus("current")
_JnxLsysSpZoneSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpZoneSummary = _JnxLsysSpZoneSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2)
)
_JnxLsysSpZoneUsedAmount_Type = Unsigned32
_JnxLsysSpZoneUsedAmount_Object = MibScalar
jnxLsysSpZoneUsedAmount = _JnxLsysSpZoneUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 1),
    _JnxLsysSpZoneUsedAmount_Type()
)
jnxLsysSpZoneUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneUsedAmount.setStatus("current")
_JnxLsysSpZoneMaxQuota_Type = Unsigned32
_JnxLsysSpZoneMaxQuota_Object = MibScalar
jnxLsysSpZoneMaxQuota = _JnxLsysSpZoneMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 2),
    _JnxLsysSpZoneMaxQuota_Type()
)
jnxLsysSpZoneMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneMaxQuota.setStatus("current")
_JnxLsysSpZoneAvailableAmount_Type = Unsigned32
_JnxLsysSpZoneAvailableAmount_Object = MibScalar
jnxLsysSpZoneAvailableAmount = _JnxLsysSpZoneAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 3),
    _JnxLsysSpZoneAvailableAmount_Type()
)
jnxLsysSpZoneAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneAvailableAmount.setStatus("current")
_JnxLsysSpZoneHeaviestUsage_Type = Unsigned32
_JnxLsysSpZoneHeaviestUsage_Object = MibScalar
jnxLsysSpZoneHeaviestUsage = _JnxLsysSpZoneHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 4),
    _JnxLsysSpZoneHeaviestUsage_Type()
)
jnxLsysSpZoneHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneHeaviestUsage.setStatus("current")


class _JnxLsysSpZoneHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpZoneHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpZoneHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpZoneHeaviestUser_Object = MibScalar
jnxLsysSpZoneHeaviestUser = _JnxLsysSpZoneHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 5),
    _JnxLsysSpZoneHeaviestUser_Type()
)
jnxLsysSpZoneHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneHeaviestUser.setStatus("current")
_JnxLsysSpZoneLightestUsage_Type = Unsigned32
_JnxLsysSpZoneLightestUsage_Object = MibScalar
jnxLsysSpZoneLightestUsage = _JnxLsysSpZoneLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 6),
    _JnxLsysSpZoneLightestUsage_Type()
)
jnxLsysSpZoneLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneLightestUsage.setStatus("current")


class _JnxLsysSpZoneLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpZoneLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpZoneLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpZoneLightestUser_Object = MibScalar
jnxLsysSpZoneLightestUser = _JnxLsysSpZoneLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1, 1, 2, 7),
    _JnxLsysSpZoneLightestUser_Type()
)
jnxLsysSpZoneLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpZoneLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-ZONE-MIB",
    **{"jnxLsysSpZoneMIB": jnxLsysSpZoneMIB,
       "jnxLsysSpZoneObjects": jnxLsysSpZoneObjects,
       "jnxLsysSpZoneTable": jnxLsysSpZoneTable,
       "jnxLsysSpZoneEntry": jnxLsysSpZoneEntry,
       "jnxLsysSpZoneLsysName": jnxLsysSpZoneLsysName,
       "jnxLsysSpZoneProfileName": jnxLsysSpZoneProfileName,
       "jnxLsysSpZoneUsage": jnxLsysSpZoneUsage,
       "jnxLsysSpZoneReserved": jnxLsysSpZoneReserved,
       "jnxLsysSpZoneMaximum": jnxLsysSpZoneMaximum,
       "jnxLsysSpZoneSummary": jnxLsysSpZoneSummary,
       "jnxLsysSpZoneUsedAmount": jnxLsysSpZoneUsedAmount,
       "jnxLsysSpZoneMaxQuota": jnxLsysSpZoneMaxQuota,
       "jnxLsysSpZoneAvailableAmount": jnxLsysSpZoneAvailableAmount,
       "jnxLsysSpZoneHeaviestUsage": jnxLsysSpZoneHeaviestUsage,
       "jnxLsysSpZoneHeaviestUser": jnxLsysSpZoneHeaviestUser,
       "jnxLsysSpZoneLightestUsage": jnxLsysSpZoneLightestUsage,
       "jnxLsysSpZoneLightestUser": jnxLsysSpZoneLightestUser}
)
