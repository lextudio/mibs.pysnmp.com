# SNMP MIB module (JUNIPER-LSYSSP-NATDSTRULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATDSTRULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:32 2024
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

(jnxLsysSpNATdstrule,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATdstrule")

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

jnxLsysSpNATdstruleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATdstruleObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstruleObjects = _JnxLsysSpNATdstruleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1)
)
_JnxLsysSpNATdstruleTable_Object = MibTable
jnxLsysSpNATdstruleTable = _JnxLsysSpNATdstruleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleTable.setStatus("current")
_JnxLsysSpNATdstruleEntry_Object = MibTableRow
jnxLsysSpNATdstruleEntry = _JnxLsysSpNATdstruleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1)
)
jnxLsysSpNATdstruleEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATDSTRULE-MIB", "jnxLsysSpNATdstruleLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleEntry.setStatus("current")


class _JnxLsysSpNATdstruleLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATdstruleLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstruleLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstruleLsysName_Object = MibTableColumn
jnxLsysSpNATdstruleLsysName = _JnxLsysSpNATdstruleLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1, 1),
    _JnxLsysSpNATdstruleLsysName_Type()
)
jnxLsysSpNATdstruleLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleLsysName.setStatus("current")


class _JnxLsysSpNATdstruleProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATdstruleProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATdstruleProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstruleProfileName_Object = MibTableColumn
jnxLsysSpNATdstruleProfileName = _JnxLsysSpNATdstruleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1, 2),
    _JnxLsysSpNATdstruleProfileName_Type()
)
jnxLsysSpNATdstruleProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleProfileName.setStatus("current")
_JnxLsysSpNATdstruleUsage_Type = Unsigned32
_JnxLsysSpNATdstruleUsage_Object = MibTableColumn
jnxLsysSpNATdstruleUsage = _JnxLsysSpNATdstruleUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1, 3),
    _JnxLsysSpNATdstruleUsage_Type()
)
jnxLsysSpNATdstruleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleUsage.setStatus("current")
_JnxLsysSpNATdstruleReserved_Type = Unsigned32
_JnxLsysSpNATdstruleReserved_Object = MibTableColumn
jnxLsysSpNATdstruleReserved = _JnxLsysSpNATdstruleReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1, 4),
    _JnxLsysSpNATdstruleReserved_Type()
)
jnxLsysSpNATdstruleReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleReserved.setStatus("current")
_JnxLsysSpNATdstruleMaximum_Type = Unsigned32
_JnxLsysSpNATdstruleMaximum_Object = MibTableColumn
jnxLsysSpNATdstruleMaximum = _JnxLsysSpNATdstruleMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 1, 1, 1, 5),
    _JnxLsysSpNATdstruleMaximum_Type()
)
jnxLsysSpNATdstruleMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleMaximum.setStatus("current")
_JnxLsysSpNATdstruleSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstruleSummary = _JnxLsysSpNATdstruleSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2)
)
_JnxLsysSpNATdstruleUsedAmount_Type = Unsigned32
_JnxLsysSpNATdstruleUsedAmount_Object = MibScalar
jnxLsysSpNATdstruleUsedAmount = _JnxLsysSpNATdstruleUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 1),
    _JnxLsysSpNATdstruleUsedAmount_Type()
)
jnxLsysSpNATdstruleUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleUsedAmount.setStatus("current")
_JnxLsysSpNATdstruleMaxQuota_Type = Unsigned32
_JnxLsysSpNATdstruleMaxQuota_Object = MibScalar
jnxLsysSpNATdstruleMaxQuota = _JnxLsysSpNATdstruleMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 2),
    _JnxLsysSpNATdstruleMaxQuota_Type()
)
jnxLsysSpNATdstruleMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleMaxQuota.setStatus("current")
_JnxLsysSpNATdstruleAvailableAmount_Type = Unsigned32
_JnxLsysSpNATdstruleAvailableAmount_Object = MibScalar
jnxLsysSpNATdstruleAvailableAmount = _JnxLsysSpNATdstruleAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 3),
    _JnxLsysSpNATdstruleAvailableAmount_Type()
)
jnxLsysSpNATdstruleAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleAvailableAmount.setStatus("current")
_JnxLsysSpNATdstruleHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATdstruleHeaviestUsage_Object = MibScalar
jnxLsysSpNATdstruleHeaviestUsage = _JnxLsysSpNATdstruleHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 4),
    _JnxLsysSpNATdstruleHeaviestUsage_Type()
)
jnxLsysSpNATdstruleHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleHeaviestUsage.setStatus("current")


class _JnxLsysSpNATdstruleHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATdstruleHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstruleHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstruleHeaviestUser_Object = MibScalar
jnxLsysSpNATdstruleHeaviestUser = _JnxLsysSpNATdstruleHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 5),
    _JnxLsysSpNATdstruleHeaviestUser_Type()
)
jnxLsysSpNATdstruleHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleHeaviestUser.setStatus("current")
_JnxLsysSpNATdstruleLightestUsage_Type = Unsigned32
_JnxLsysSpNATdstruleLightestUsage_Object = MibScalar
jnxLsysSpNATdstruleLightestUsage = _JnxLsysSpNATdstruleLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 6),
    _JnxLsysSpNATdstruleLightestUsage_Type()
)
jnxLsysSpNATdstruleLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleLightestUsage.setStatus("current")


class _JnxLsysSpNATdstruleLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATdstruleLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstruleLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstruleLightestUser_Object = MibScalar
jnxLsysSpNATdstruleLightestUser = _JnxLsysSpNATdstruleLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13, 1, 2, 7),
    _JnxLsysSpNATdstruleLightestUser_Type()
)
jnxLsysSpNATdstruleLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstruleLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATDSTRULE-MIB",
    **{"jnxLsysSpNATdstruleMIB": jnxLsysSpNATdstruleMIB,
       "jnxLsysSpNATdstruleObjects": jnxLsysSpNATdstruleObjects,
       "jnxLsysSpNATdstruleTable": jnxLsysSpNATdstruleTable,
       "jnxLsysSpNATdstruleEntry": jnxLsysSpNATdstruleEntry,
       "jnxLsysSpNATdstruleLsysName": jnxLsysSpNATdstruleLsysName,
       "jnxLsysSpNATdstruleProfileName": jnxLsysSpNATdstruleProfileName,
       "jnxLsysSpNATdstruleUsage": jnxLsysSpNATdstruleUsage,
       "jnxLsysSpNATdstruleReserved": jnxLsysSpNATdstruleReserved,
       "jnxLsysSpNATdstruleMaximum": jnxLsysSpNATdstruleMaximum,
       "jnxLsysSpNATdstruleSummary": jnxLsysSpNATdstruleSummary,
       "jnxLsysSpNATdstruleUsedAmount": jnxLsysSpNATdstruleUsedAmount,
       "jnxLsysSpNATdstruleMaxQuota": jnxLsysSpNATdstruleMaxQuota,
       "jnxLsysSpNATdstruleAvailableAmount": jnxLsysSpNATdstruleAvailableAmount,
       "jnxLsysSpNATdstruleHeaviestUsage": jnxLsysSpNATdstruleHeaviestUsage,
       "jnxLsysSpNATdstruleHeaviestUser": jnxLsysSpNATdstruleHeaviestUser,
       "jnxLsysSpNATdstruleLightestUsage": jnxLsysSpNATdstruleLightestUsage,
       "jnxLsysSpNATdstruleLightestUser": jnxLsysSpNATdstruleLightestUser}
)
