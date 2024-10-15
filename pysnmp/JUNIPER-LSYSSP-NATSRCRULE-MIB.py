# SNMP MIB module (JUNIPER-LSYSSP-NATSRCRULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATSRCRULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:36 2024
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

(jnxLsysSpNATsrcrule,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATsrcrule")

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

jnxLsysSpNATsrcruleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATsrcruleObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcruleObjects = _JnxLsysSpNATsrcruleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1)
)
_JnxLsysSpNATsrcruleTable_Object = MibTable
jnxLsysSpNATsrcruleTable = _JnxLsysSpNATsrcruleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleTable.setStatus("current")
_JnxLsysSpNATsrcruleEntry_Object = MibTableRow
jnxLsysSpNATsrcruleEntry = _JnxLsysSpNATsrcruleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1)
)
jnxLsysSpNATsrcruleEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATSRCRULE-MIB", "jnxLsysSpNATsrcruleLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleEntry.setStatus("current")


class _JnxLsysSpNATsrcruleLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcruleLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcruleLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcruleLsysName_Object = MibTableColumn
jnxLsysSpNATsrcruleLsysName = _JnxLsysSpNATsrcruleLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 1),
    _JnxLsysSpNATsrcruleLsysName_Type()
)
jnxLsysSpNATsrcruleLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleLsysName.setStatus("current")


class _JnxLsysSpNATsrcruleProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcruleProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATsrcruleProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcruleProfileName_Object = MibTableColumn
jnxLsysSpNATsrcruleProfileName = _JnxLsysSpNATsrcruleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 2),
    _JnxLsysSpNATsrcruleProfileName_Type()
)
jnxLsysSpNATsrcruleProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleProfileName.setStatus("current")
_JnxLsysSpNATsrcruleUsage_Type = Unsigned32
_JnxLsysSpNATsrcruleUsage_Object = MibTableColumn
jnxLsysSpNATsrcruleUsage = _JnxLsysSpNATsrcruleUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 3),
    _JnxLsysSpNATsrcruleUsage_Type()
)
jnxLsysSpNATsrcruleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleUsage.setStatus("current")
_JnxLsysSpNATsrcruleReserved_Type = Unsigned32
_JnxLsysSpNATsrcruleReserved_Object = MibTableColumn
jnxLsysSpNATsrcruleReserved = _JnxLsysSpNATsrcruleReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 4),
    _JnxLsysSpNATsrcruleReserved_Type()
)
jnxLsysSpNATsrcruleReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleReserved.setStatus("current")
_JnxLsysSpNATsrcruleMaximum_Type = Unsigned32
_JnxLsysSpNATsrcruleMaximum_Object = MibTableColumn
jnxLsysSpNATsrcruleMaximum = _JnxLsysSpNATsrcruleMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 5),
    _JnxLsysSpNATsrcruleMaximum_Type()
)
jnxLsysSpNATsrcruleMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleMaximum.setStatus("current")
_JnxLsysSpNATsrcruleSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcruleSummary = _JnxLsysSpNATsrcruleSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2)
)
_JnxLsysSpNATsrcruleUsedAmount_Type = Unsigned32
_JnxLsysSpNATsrcruleUsedAmount_Object = MibScalar
jnxLsysSpNATsrcruleUsedAmount = _JnxLsysSpNATsrcruleUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 1),
    _JnxLsysSpNATsrcruleUsedAmount_Type()
)
jnxLsysSpNATsrcruleUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleUsedAmount.setStatus("current")
_JnxLsysSpNATsrcruleMaxQuota_Type = Unsigned32
_JnxLsysSpNATsrcruleMaxQuota_Object = MibScalar
jnxLsysSpNATsrcruleMaxQuota = _JnxLsysSpNATsrcruleMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 2),
    _JnxLsysSpNATsrcruleMaxQuota_Type()
)
jnxLsysSpNATsrcruleMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleMaxQuota.setStatus("current")
_JnxLsysSpNATsrcruleAvailableAmount_Type = Unsigned32
_JnxLsysSpNATsrcruleAvailableAmount_Object = MibScalar
jnxLsysSpNATsrcruleAvailableAmount = _JnxLsysSpNATsrcruleAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 3),
    _JnxLsysSpNATsrcruleAvailableAmount_Type()
)
jnxLsysSpNATsrcruleAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleAvailableAmount.setStatus("current")
_JnxLsysSpNATsrcruleHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATsrcruleHeaviestUsage_Object = MibScalar
jnxLsysSpNATsrcruleHeaviestUsage = _JnxLsysSpNATsrcruleHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 4),
    _JnxLsysSpNATsrcruleHeaviestUsage_Type()
)
jnxLsysSpNATsrcruleHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleHeaviestUsage.setStatus("current")


class _JnxLsysSpNATsrcruleHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcruleHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcruleHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcruleHeaviestUser_Object = MibScalar
jnxLsysSpNATsrcruleHeaviestUser = _JnxLsysSpNATsrcruleHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 5),
    _JnxLsysSpNATsrcruleHeaviestUser_Type()
)
jnxLsysSpNATsrcruleHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleHeaviestUser.setStatus("current")
_JnxLsysSpNATsrcruleLightestUsage_Type = Unsigned32
_JnxLsysSpNATsrcruleLightestUsage_Object = MibScalar
jnxLsysSpNATsrcruleLightestUsage = _JnxLsysSpNATsrcruleLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 6),
    _JnxLsysSpNATsrcruleLightestUsage_Type()
)
jnxLsysSpNATsrcruleLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleLightestUsage.setStatus("current")


class _JnxLsysSpNATsrcruleLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcruleLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcruleLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcruleLightestUser_Object = MibScalar
jnxLsysSpNATsrcruleLightestUser = _JnxLsysSpNATsrcruleLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 7),
    _JnxLsysSpNATsrcruleLightestUser_Type()
)
jnxLsysSpNATsrcruleLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcruleLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATSRCRULE-MIB",
    **{"jnxLsysSpNATsrcruleMIB": jnxLsysSpNATsrcruleMIB,
       "jnxLsysSpNATsrcruleObjects": jnxLsysSpNATsrcruleObjects,
       "jnxLsysSpNATsrcruleTable": jnxLsysSpNATsrcruleTable,
       "jnxLsysSpNATsrcruleEntry": jnxLsysSpNATsrcruleEntry,
       "jnxLsysSpNATsrcruleLsysName": jnxLsysSpNATsrcruleLsysName,
       "jnxLsysSpNATsrcruleProfileName": jnxLsysSpNATsrcruleProfileName,
       "jnxLsysSpNATsrcruleUsage": jnxLsysSpNATsrcruleUsage,
       "jnxLsysSpNATsrcruleReserved": jnxLsysSpNATsrcruleReserved,
       "jnxLsysSpNATsrcruleMaximum": jnxLsysSpNATsrcruleMaximum,
       "jnxLsysSpNATsrcruleSummary": jnxLsysSpNATsrcruleSummary,
       "jnxLsysSpNATsrcruleUsedAmount": jnxLsysSpNATsrcruleUsedAmount,
       "jnxLsysSpNATsrcruleMaxQuota": jnxLsysSpNATsrcruleMaxQuota,
       "jnxLsysSpNATsrcruleAvailableAmount": jnxLsysSpNATsrcruleAvailableAmount,
       "jnxLsysSpNATsrcruleHeaviestUsage": jnxLsysSpNATsrcruleHeaviestUsage,
       "jnxLsysSpNATsrcruleHeaviestUser": jnxLsysSpNATsrcruleHeaviestUser,
       "jnxLsysSpNATsrcruleLightestUsage": jnxLsysSpNATsrcruleLightestUsage,
       "jnxLsysSpNATsrcruleLightestUser": jnxLsysSpNATsrcruleLightestUser}
)
