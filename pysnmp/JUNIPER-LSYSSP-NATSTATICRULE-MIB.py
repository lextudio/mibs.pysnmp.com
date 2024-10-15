# SNMP MIB module (JUNIPER-LSYSSP-NATSTATICRULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATSTATICRULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:37 2024
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

(jnxLsysSpNATstaticrule,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATstaticrule")

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

jnxLsysSpNATstaticruleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATstaticruleObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATstaticruleObjects = _JnxLsysSpNATstaticruleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1)
)
_JnxLsysSpNATstaticruleTable_Object = MibTable
jnxLsysSpNATstaticruleTable = _JnxLsysSpNATstaticruleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleTable.setStatus("current")
_JnxLsysSpNATstaticruleEntry_Object = MibTableRow
jnxLsysSpNATstaticruleEntry = _JnxLsysSpNATstaticruleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1)
)
jnxLsysSpNATstaticruleEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATSTATICRULE-MIB", "jnxLsysSpNATstaticruleLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleEntry.setStatus("current")


class _JnxLsysSpNATstaticruleLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATstaticruleLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATstaticruleLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATstaticruleLsysName_Object = MibTableColumn
jnxLsysSpNATstaticruleLsysName = _JnxLsysSpNATstaticruleLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1, 1),
    _JnxLsysSpNATstaticruleLsysName_Type()
)
jnxLsysSpNATstaticruleLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleLsysName.setStatus("current")


class _JnxLsysSpNATstaticruleProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATstaticruleProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATstaticruleProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATstaticruleProfileName_Object = MibTableColumn
jnxLsysSpNATstaticruleProfileName = _JnxLsysSpNATstaticruleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1, 2),
    _JnxLsysSpNATstaticruleProfileName_Type()
)
jnxLsysSpNATstaticruleProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleProfileName.setStatus("current")
_JnxLsysSpNATstaticruleUsage_Type = Unsigned32
_JnxLsysSpNATstaticruleUsage_Object = MibTableColumn
jnxLsysSpNATstaticruleUsage = _JnxLsysSpNATstaticruleUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1, 3),
    _JnxLsysSpNATstaticruleUsage_Type()
)
jnxLsysSpNATstaticruleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleUsage.setStatus("current")
_JnxLsysSpNATstaticruleReserved_Type = Unsigned32
_JnxLsysSpNATstaticruleReserved_Object = MibTableColumn
jnxLsysSpNATstaticruleReserved = _JnxLsysSpNATstaticruleReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1, 4),
    _JnxLsysSpNATstaticruleReserved_Type()
)
jnxLsysSpNATstaticruleReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleReserved.setStatus("current")
_JnxLsysSpNATstaticruleMaximum_Type = Unsigned32
_JnxLsysSpNATstaticruleMaximum_Object = MibTableColumn
jnxLsysSpNATstaticruleMaximum = _JnxLsysSpNATstaticruleMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 1, 1, 1, 5),
    _JnxLsysSpNATstaticruleMaximum_Type()
)
jnxLsysSpNATstaticruleMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleMaximum.setStatus("current")
_JnxLsysSpNATstaticruleSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATstaticruleSummary = _JnxLsysSpNATstaticruleSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2)
)
_JnxLsysSpNATstaticruleUsedAmount_Type = Unsigned32
_JnxLsysSpNATstaticruleUsedAmount_Object = MibScalar
jnxLsysSpNATstaticruleUsedAmount = _JnxLsysSpNATstaticruleUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 1),
    _JnxLsysSpNATstaticruleUsedAmount_Type()
)
jnxLsysSpNATstaticruleUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleUsedAmount.setStatus("current")
_JnxLsysSpNATstaticruleMaxQuota_Type = Unsigned32
_JnxLsysSpNATstaticruleMaxQuota_Object = MibScalar
jnxLsysSpNATstaticruleMaxQuota = _JnxLsysSpNATstaticruleMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 2),
    _JnxLsysSpNATstaticruleMaxQuota_Type()
)
jnxLsysSpNATstaticruleMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleMaxQuota.setStatus("current")
_JnxLsysSpNATstaticruleAvailableAmount_Type = Unsigned32
_JnxLsysSpNATstaticruleAvailableAmount_Object = MibScalar
jnxLsysSpNATstaticruleAvailableAmount = _JnxLsysSpNATstaticruleAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 3),
    _JnxLsysSpNATstaticruleAvailableAmount_Type()
)
jnxLsysSpNATstaticruleAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleAvailableAmount.setStatus("current")
_JnxLsysSpNATstaticruleHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATstaticruleHeaviestUsage_Object = MibScalar
jnxLsysSpNATstaticruleHeaviestUsage = _JnxLsysSpNATstaticruleHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 4),
    _JnxLsysSpNATstaticruleHeaviestUsage_Type()
)
jnxLsysSpNATstaticruleHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleHeaviestUsage.setStatus("current")


class _JnxLsysSpNATstaticruleHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATstaticruleHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATstaticruleHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATstaticruleHeaviestUser_Object = MibScalar
jnxLsysSpNATstaticruleHeaviestUser = _JnxLsysSpNATstaticruleHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 5),
    _JnxLsysSpNATstaticruleHeaviestUser_Type()
)
jnxLsysSpNATstaticruleHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleHeaviestUser.setStatus("current")
_JnxLsysSpNATstaticruleLightestUsage_Type = Unsigned32
_JnxLsysSpNATstaticruleLightestUsage_Object = MibScalar
jnxLsysSpNATstaticruleLightestUsage = _JnxLsysSpNATstaticruleLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 6),
    _JnxLsysSpNATstaticruleLightestUsage_Type()
)
jnxLsysSpNATstaticruleLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleLightestUsage.setStatus("current")


class _JnxLsysSpNATstaticruleLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATstaticruleLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATstaticruleLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATstaticruleLightestUser_Object = MibScalar
jnxLsysSpNATstaticruleLightestUser = _JnxLsysSpNATstaticruleLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14, 1, 2, 7),
    _JnxLsysSpNATstaticruleLightestUser_Type()
)
jnxLsysSpNATstaticruleLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATstaticruleLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATSTATICRULE-MIB",
    **{"jnxLsysSpNATstaticruleMIB": jnxLsysSpNATstaticruleMIB,
       "jnxLsysSpNATstaticruleObjects": jnxLsysSpNATstaticruleObjects,
       "jnxLsysSpNATstaticruleTable": jnxLsysSpNATstaticruleTable,
       "jnxLsysSpNATstaticruleEntry": jnxLsysSpNATstaticruleEntry,
       "jnxLsysSpNATstaticruleLsysName": jnxLsysSpNATstaticruleLsysName,
       "jnxLsysSpNATstaticruleProfileName": jnxLsysSpNATstaticruleProfileName,
       "jnxLsysSpNATstaticruleUsage": jnxLsysSpNATstaticruleUsage,
       "jnxLsysSpNATstaticruleReserved": jnxLsysSpNATstaticruleReserved,
       "jnxLsysSpNATstaticruleMaximum": jnxLsysSpNATstaticruleMaximum,
       "jnxLsysSpNATstaticruleSummary": jnxLsysSpNATstaticruleSummary,
       "jnxLsysSpNATstaticruleUsedAmount": jnxLsysSpNATstaticruleUsedAmount,
       "jnxLsysSpNATstaticruleMaxQuota": jnxLsysSpNATstaticruleMaxQuota,
       "jnxLsysSpNATstaticruleAvailableAmount": jnxLsysSpNATstaticruleAvailableAmount,
       "jnxLsysSpNATstaticruleHeaviestUsage": jnxLsysSpNATstaticruleHeaviestUsage,
       "jnxLsysSpNATstaticruleHeaviestUser": jnxLsysSpNATstaticruleHeaviestUser,
       "jnxLsysSpNATstaticruleLightestUsage": jnxLsysSpNATstaticruleLightestUsage,
       "jnxLsysSpNATstaticruleLightestUser": jnxLsysSpNATstaticruleLightestUser}
)
