# SNMP MIB module (JUNIPER-LSYSSPAUTHENTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSPAUTHENTRY-MIB
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

(jnxLsysSpAuthentry,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpAuthentry")

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

jnxLsysSpAuthentryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpAuthentryObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpAuthentryObjects = _JnxLsysSpAuthentryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1)
)
_JnxLsysSpAuthentryTable_Object = MibTable
jnxLsysSpAuthentryTable = _JnxLsysSpAuthentryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryTable.setStatus("current")
_JnxLsysSpAuthentryEntry_Object = MibTableRow
jnxLsysSpAuthentryEntry = _JnxLsysSpAuthentryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1)
)
jnxLsysSpAuthentryEntry.setIndexNames(
    (1, "JUNIPER-LSYSSPAUTHENTRY-MIB", "jnxLsysSpAuthentryLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryEntry.setStatus("current")


class _JnxLsysSpAuthentryLsysName_Type(DisplayString):
    """Custom type jnxLsysSpAuthentryLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpAuthentryLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpAuthentryLsysName_Object = MibTableColumn
jnxLsysSpAuthentryLsysName = _JnxLsysSpAuthentryLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 1),
    _JnxLsysSpAuthentryLsysName_Type()
)
jnxLsysSpAuthentryLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryLsysName.setStatus("current")


class _JnxLsysSpAuthentryProfileName_Type(DisplayString):
    """Custom type jnxLsysSpAuthentryProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpAuthentryProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpAuthentryProfileName_Object = MibTableColumn
jnxLsysSpAuthentryProfileName = _JnxLsysSpAuthentryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 2),
    _JnxLsysSpAuthentryProfileName_Type()
)
jnxLsysSpAuthentryProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryProfileName.setStatus("current")
_JnxLsysSpAuthentryUsage_Type = Unsigned32
_JnxLsysSpAuthentryUsage_Object = MibTableColumn
jnxLsysSpAuthentryUsage = _JnxLsysSpAuthentryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 3),
    _JnxLsysSpAuthentryUsage_Type()
)
jnxLsysSpAuthentryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryUsage.setStatus("current")
_JnxLsysSpAuthentryReserved_Type = Unsigned32
_JnxLsysSpAuthentryReserved_Object = MibTableColumn
jnxLsysSpAuthentryReserved = _JnxLsysSpAuthentryReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 4),
    _JnxLsysSpAuthentryReserved_Type()
)
jnxLsysSpAuthentryReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryReserved.setStatus("current")
_JnxLsysSpAuthentryMaximum_Type = Unsigned32
_JnxLsysSpAuthentryMaximum_Object = MibTableColumn
jnxLsysSpAuthentryMaximum = _JnxLsysSpAuthentryMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 5),
    _JnxLsysSpAuthentryMaximum_Type()
)
jnxLsysSpAuthentryMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryMaximum.setStatus("current")
_JnxLsysSpAuthentrySummary_ObjectIdentity = ObjectIdentity
jnxLsysSpAuthentrySummary = _JnxLsysSpAuthentrySummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2)
)
_JnxLsysSpAuthentryUsedAmount_Type = Unsigned32
_JnxLsysSpAuthentryUsedAmount_Object = MibScalar
jnxLsysSpAuthentryUsedAmount = _JnxLsysSpAuthentryUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 1),
    _JnxLsysSpAuthentryUsedAmount_Type()
)
jnxLsysSpAuthentryUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryUsedAmount.setStatus("current")
_JnxLsysSpAuthentryMaxQuota_Type = Unsigned32
_JnxLsysSpAuthentryMaxQuota_Object = MibScalar
jnxLsysSpAuthentryMaxQuota = _JnxLsysSpAuthentryMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 2),
    _JnxLsysSpAuthentryMaxQuota_Type()
)
jnxLsysSpAuthentryMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryMaxQuota.setStatus("current")
_JnxLsysSpAuthentryAvailableAmount_Type = Unsigned32
_JnxLsysSpAuthentryAvailableAmount_Object = MibScalar
jnxLsysSpAuthentryAvailableAmount = _JnxLsysSpAuthentryAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 3),
    _JnxLsysSpAuthentryAvailableAmount_Type()
)
jnxLsysSpAuthentryAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryAvailableAmount.setStatus("current")
_JnxLsysSpAuthentryHeaviestUsage_Type = Unsigned32
_JnxLsysSpAuthentryHeaviestUsage_Object = MibScalar
jnxLsysSpAuthentryHeaviestUsage = _JnxLsysSpAuthentryHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 4),
    _JnxLsysSpAuthentryHeaviestUsage_Type()
)
jnxLsysSpAuthentryHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryHeaviestUsage.setStatus("current")


class _JnxLsysSpAuthentryHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpAuthentryHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpAuthentryHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpAuthentryHeaviestUser_Object = MibScalar
jnxLsysSpAuthentryHeaviestUser = _JnxLsysSpAuthentryHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 5),
    _JnxLsysSpAuthentryHeaviestUser_Type()
)
jnxLsysSpAuthentryHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryHeaviestUser.setStatus("current")
_JnxLsysSpAuthentryLightestUsage_Type = Unsigned32
_JnxLsysSpAuthentryLightestUsage_Object = MibScalar
jnxLsysSpAuthentryLightestUsage = _JnxLsysSpAuthentryLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 6),
    _JnxLsysSpAuthentryLightestUsage_Type()
)
jnxLsysSpAuthentryLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryLightestUsage.setStatus("current")


class _JnxLsysSpAuthentryLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpAuthentryLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpAuthentryLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpAuthentryLightestUser_Object = MibScalar
jnxLsysSpAuthentryLightestUser = _JnxLsysSpAuthentryLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 7),
    _JnxLsysSpAuthentryLightestUser_Type()
)
jnxLsysSpAuthentryLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpAuthentryLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSPAUTHENTRY-MIB",
    **{"jnxLsysSpAuthentryMIB": jnxLsysSpAuthentryMIB,
       "jnxLsysSpAuthentryObjects": jnxLsysSpAuthentryObjects,
       "jnxLsysSpAuthentryTable": jnxLsysSpAuthentryTable,
       "jnxLsysSpAuthentryEntry": jnxLsysSpAuthentryEntry,
       "jnxLsysSpAuthentryLsysName": jnxLsysSpAuthentryLsysName,
       "jnxLsysSpAuthentryProfileName": jnxLsysSpAuthentryProfileName,
       "jnxLsysSpAuthentryUsage": jnxLsysSpAuthentryUsage,
       "jnxLsysSpAuthentryReserved": jnxLsysSpAuthentryReserved,
       "jnxLsysSpAuthentryMaximum": jnxLsysSpAuthentryMaximum,
       "jnxLsysSpAuthentrySummary": jnxLsysSpAuthentrySummary,
       "jnxLsysSpAuthentryUsedAmount": jnxLsysSpAuthentryUsedAmount,
       "jnxLsysSpAuthentryMaxQuota": jnxLsysSpAuthentryMaxQuota,
       "jnxLsysSpAuthentryAvailableAmount": jnxLsysSpAuthentryAvailableAmount,
       "jnxLsysSpAuthentryHeaviestUsage": jnxLsysSpAuthentryHeaviestUsage,
       "jnxLsysSpAuthentryHeaviestUser": jnxLsysSpAuthentryHeaviestUser,
       "jnxLsysSpAuthentryLightestUsage": jnxLsysSpAuthentryLightestUsage,
       "jnxLsysSpAuthentryLightestUser": jnxLsysSpAuthentryLightestUser}
)
