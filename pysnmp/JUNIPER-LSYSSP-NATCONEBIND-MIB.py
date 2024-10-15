# SNMP MIB module (JUNIPER-LSYSSP-NATCONEBIND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATCONEBIND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:31 2024
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

(jnxLsysSpNATconebind,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATconebind")

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

jnxLsysSpNATconebindMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATconebindObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATconebindObjects = _JnxLsysSpNATconebindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1)
)
_JnxLsysSpNATconebindTable_Object = MibTable
jnxLsysSpNATconebindTable = _JnxLsysSpNATconebindTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindTable.setStatus("current")
_JnxLsysSpNATconebindEntry_Object = MibTableRow
jnxLsysSpNATconebindEntry = _JnxLsysSpNATconebindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1)
)
jnxLsysSpNATconebindEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATCONEBIND-MIB", "jnxLsysSpNATconebindLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindEntry.setStatus("current")


class _JnxLsysSpNATconebindLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATconebindLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATconebindLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATconebindLsysName_Object = MibTableColumn
jnxLsysSpNATconebindLsysName = _JnxLsysSpNATconebindLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 1),
    _JnxLsysSpNATconebindLsysName_Type()
)
jnxLsysSpNATconebindLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindLsysName.setStatus("current")


class _JnxLsysSpNATconebindProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATconebindProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATconebindProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATconebindProfileName_Object = MibTableColumn
jnxLsysSpNATconebindProfileName = _JnxLsysSpNATconebindProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 2),
    _JnxLsysSpNATconebindProfileName_Type()
)
jnxLsysSpNATconebindProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindProfileName.setStatus("current")
_JnxLsysSpNATconebindUsage_Type = Unsigned32
_JnxLsysSpNATconebindUsage_Object = MibTableColumn
jnxLsysSpNATconebindUsage = _JnxLsysSpNATconebindUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 3),
    _JnxLsysSpNATconebindUsage_Type()
)
jnxLsysSpNATconebindUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindUsage.setStatus("current")
_JnxLsysSpNATconebindReserved_Type = Unsigned32
_JnxLsysSpNATconebindReserved_Object = MibTableColumn
jnxLsysSpNATconebindReserved = _JnxLsysSpNATconebindReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 4),
    _JnxLsysSpNATconebindReserved_Type()
)
jnxLsysSpNATconebindReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindReserved.setStatus("current")
_JnxLsysSpNATconebindMaximum_Type = Unsigned32
_JnxLsysSpNATconebindMaximum_Object = MibTableColumn
jnxLsysSpNATconebindMaximum = _JnxLsysSpNATconebindMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 5),
    _JnxLsysSpNATconebindMaximum_Type()
)
jnxLsysSpNATconebindMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindMaximum.setStatus("current")
_JnxLsysSpNATconebindSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATconebindSummary = _JnxLsysSpNATconebindSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2)
)
_JnxLsysSpNATconebindUsedAmount_Type = Unsigned32
_JnxLsysSpNATconebindUsedAmount_Object = MibScalar
jnxLsysSpNATconebindUsedAmount = _JnxLsysSpNATconebindUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 1),
    _JnxLsysSpNATconebindUsedAmount_Type()
)
jnxLsysSpNATconebindUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindUsedAmount.setStatus("current")
_JnxLsysSpNATconebindMaxQuota_Type = Unsigned32
_JnxLsysSpNATconebindMaxQuota_Object = MibScalar
jnxLsysSpNATconebindMaxQuota = _JnxLsysSpNATconebindMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 2),
    _JnxLsysSpNATconebindMaxQuota_Type()
)
jnxLsysSpNATconebindMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindMaxQuota.setStatus("current")
_JnxLsysSpNATconebindAvailableAmount_Type = Unsigned32
_JnxLsysSpNATconebindAvailableAmount_Object = MibScalar
jnxLsysSpNATconebindAvailableAmount = _JnxLsysSpNATconebindAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 3),
    _JnxLsysSpNATconebindAvailableAmount_Type()
)
jnxLsysSpNATconebindAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindAvailableAmount.setStatus("current")
_JnxLsysSpNATconebindHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATconebindHeaviestUsage_Object = MibScalar
jnxLsysSpNATconebindHeaviestUsage = _JnxLsysSpNATconebindHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 4),
    _JnxLsysSpNATconebindHeaviestUsage_Type()
)
jnxLsysSpNATconebindHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindHeaviestUsage.setStatus("current")


class _JnxLsysSpNATconebindHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATconebindHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATconebindHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATconebindHeaviestUser_Object = MibScalar
jnxLsysSpNATconebindHeaviestUser = _JnxLsysSpNATconebindHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 5),
    _JnxLsysSpNATconebindHeaviestUser_Type()
)
jnxLsysSpNATconebindHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindHeaviestUser.setStatus("current")
_JnxLsysSpNATconebindLightestUsage_Type = Unsigned32
_JnxLsysSpNATconebindLightestUsage_Object = MibScalar
jnxLsysSpNATconebindLightestUsage = _JnxLsysSpNATconebindLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 6),
    _JnxLsysSpNATconebindLightestUsage_Type()
)
jnxLsysSpNATconebindLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindLightestUsage.setStatus("current")


class _JnxLsysSpNATconebindLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATconebindLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATconebindLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATconebindLightestUser_Object = MibScalar
jnxLsysSpNATconebindLightestUser = _JnxLsysSpNATconebindLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 7),
    _JnxLsysSpNATconebindLightestUser_Type()
)
jnxLsysSpNATconebindLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATconebindLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATCONEBIND-MIB",
    **{"jnxLsysSpNATconebindMIB": jnxLsysSpNATconebindMIB,
       "jnxLsysSpNATconebindObjects": jnxLsysSpNATconebindObjects,
       "jnxLsysSpNATconebindTable": jnxLsysSpNATconebindTable,
       "jnxLsysSpNATconebindEntry": jnxLsysSpNATconebindEntry,
       "jnxLsysSpNATconebindLsysName": jnxLsysSpNATconebindLsysName,
       "jnxLsysSpNATconebindProfileName": jnxLsysSpNATconebindProfileName,
       "jnxLsysSpNATconebindUsage": jnxLsysSpNATconebindUsage,
       "jnxLsysSpNATconebindReserved": jnxLsysSpNATconebindReserved,
       "jnxLsysSpNATconebindMaximum": jnxLsysSpNATconebindMaximum,
       "jnxLsysSpNATconebindSummary": jnxLsysSpNATconebindSummary,
       "jnxLsysSpNATconebindUsedAmount": jnxLsysSpNATconebindUsedAmount,
       "jnxLsysSpNATconebindMaxQuota": jnxLsysSpNATconebindMaxQuota,
       "jnxLsysSpNATconebindAvailableAmount": jnxLsysSpNATconebindAvailableAmount,
       "jnxLsysSpNATconebindHeaviestUsage": jnxLsysSpNATconebindHeaviestUsage,
       "jnxLsysSpNATconebindHeaviestUser": jnxLsysSpNATconebindHeaviestUser,
       "jnxLsysSpNATconebindLightestUsage": jnxLsysSpNATconebindLightestUsage,
       "jnxLsysSpNATconebindLightestUser": jnxLsysSpNATconebindLightestUser}
)
