# SNMP MIB module (JUNIPER-LSYSSP-FLOWSESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-FLOWSESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:30 2024
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

(jnxLsysSpFlowsess,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpFlowsess")

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

jnxLsysSpFlowsessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpFlowsessObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowsessObjects = _JnxLsysSpFlowsessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1)
)
_JnxLsysSpFlowsessTable_Object = MibTable
jnxLsysSpFlowsessTable = _JnxLsysSpFlowsessTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessTable.setStatus("current")
_JnxLsysSpFlowsessEntry_Object = MibTableRow
jnxLsysSpFlowsessEntry = _JnxLsysSpFlowsessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1)
)
jnxLsysSpFlowsessEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-FLOWSESS-MIB", "jnxLsysSpFlowsessLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessEntry.setStatus("current")


class _JnxLsysSpFlowsessLsysName_Type(DisplayString):
    """Custom type jnxLsysSpFlowsessLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowsessLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpFlowsessLsysName_Object = MibTableColumn
jnxLsysSpFlowsessLsysName = _JnxLsysSpFlowsessLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1, 1),
    _JnxLsysSpFlowsessLsysName_Type()
)
jnxLsysSpFlowsessLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessLsysName.setStatus("current")


class _JnxLsysSpFlowsessProfileName_Type(DisplayString):
    """Custom type jnxLsysSpFlowsessProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpFlowsessProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpFlowsessProfileName_Object = MibTableColumn
jnxLsysSpFlowsessProfileName = _JnxLsysSpFlowsessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1, 2),
    _JnxLsysSpFlowsessProfileName_Type()
)
jnxLsysSpFlowsessProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessProfileName.setStatus("current")
_JnxLsysSpFlowsessUsage_Type = Unsigned32
_JnxLsysSpFlowsessUsage_Object = MibTableColumn
jnxLsysSpFlowsessUsage = _JnxLsysSpFlowsessUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1, 3),
    _JnxLsysSpFlowsessUsage_Type()
)
jnxLsysSpFlowsessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessUsage.setStatus("current")
_JnxLsysSpFlowsessReserved_Type = Unsigned32
_JnxLsysSpFlowsessReserved_Object = MibTableColumn
jnxLsysSpFlowsessReserved = _JnxLsysSpFlowsessReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1, 4),
    _JnxLsysSpFlowsessReserved_Type()
)
jnxLsysSpFlowsessReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessReserved.setStatus("current")
_JnxLsysSpFlowsessMaximum_Type = Unsigned32
_JnxLsysSpFlowsessMaximum_Object = MibTableColumn
jnxLsysSpFlowsessMaximum = _JnxLsysSpFlowsessMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 1, 1, 1, 5),
    _JnxLsysSpFlowsessMaximum_Type()
)
jnxLsysSpFlowsessMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessMaximum.setStatus("current")
_JnxLsysSpFlowsessSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowsessSummary = _JnxLsysSpFlowsessSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2)
)
_JnxLsysSpFlowsessUsedAmount_Type = Unsigned32
_JnxLsysSpFlowsessUsedAmount_Object = MibScalar
jnxLsysSpFlowsessUsedAmount = _JnxLsysSpFlowsessUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 1),
    _JnxLsysSpFlowsessUsedAmount_Type()
)
jnxLsysSpFlowsessUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessUsedAmount.setStatus("current")
_JnxLsysSpFlowsessMaxQuota_Type = Unsigned32
_JnxLsysSpFlowsessMaxQuota_Object = MibScalar
jnxLsysSpFlowsessMaxQuota = _JnxLsysSpFlowsessMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 2),
    _JnxLsysSpFlowsessMaxQuota_Type()
)
jnxLsysSpFlowsessMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessMaxQuota.setStatus("current")
_JnxLsysSpFlowsessAvailableAmount_Type = Unsigned32
_JnxLsysSpFlowsessAvailableAmount_Object = MibScalar
jnxLsysSpFlowsessAvailableAmount = _JnxLsysSpFlowsessAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 3),
    _JnxLsysSpFlowsessAvailableAmount_Type()
)
jnxLsysSpFlowsessAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessAvailableAmount.setStatus("current")
_JnxLsysSpFlowsessHeaviestUsage_Type = Unsigned32
_JnxLsysSpFlowsessHeaviestUsage_Object = MibScalar
jnxLsysSpFlowsessHeaviestUsage = _JnxLsysSpFlowsessHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 4),
    _JnxLsysSpFlowsessHeaviestUsage_Type()
)
jnxLsysSpFlowsessHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessHeaviestUsage.setStatus("current")


class _JnxLsysSpFlowsessHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpFlowsessHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowsessHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpFlowsessHeaviestUser_Object = MibScalar
jnxLsysSpFlowsessHeaviestUser = _JnxLsysSpFlowsessHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 5),
    _JnxLsysSpFlowsessHeaviestUser_Type()
)
jnxLsysSpFlowsessHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessHeaviestUser.setStatus("current")
_JnxLsysSpFlowsessLightestUsage_Type = Unsigned32
_JnxLsysSpFlowsessLightestUsage_Object = MibScalar
jnxLsysSpFlowsessLightestUsage = _JnxLsysSpFlowsessLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 6),
    _JnxLsysSpFlowsessLightestUsage_Type()
)
jnxLsysSpFlowsessLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessLightestUsage.setStatus("current")


class _JnxLsysSpFlowsessLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpFlowsessLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowsessLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpFlowsessLightestUser_Object = MibScalar
jnxLsysSpFlowsessLightestUser = _JnxLsysSpFlowsessLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6, 1, 2, 7),
    _JnxLsysSpFlowsessLightestUser_Type()
)
jnxLsysSpFlowsessLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowsessLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-FLOWSESS-MIB",
    **{"jnxLsysSpFlowsessMIB": jnxLsysSpFlowsessMIB,
       "jnxLsysSpFlowsessObjects": jnxLsysSpFlowsessObjects,
       "jnxLsysSpFlowsessTable": jnxLsysSpFlowsessTable,
       "jnxLsysSpFlowsessEntry": jnxLsysSpFlowsessEntry,
       "jnxLsysSpFlowsessLsysName": jnxLsysSpFlowsessLsysName,
       "jnxLsysSpFlowsessProfileName": jnxLsysSpFlowsessProfileName,
       "jnxLsysSpFlowsessUsage": jnxLsysSpFlowsessUsage,
       "jnxLsysSpFlowsessReserved": jnxLsysSpFlowsessReserved,
       "jnxLsysSpFlowsessMaximum": jnxLsysSpFlowsessMaximum,
       "jnxLsysSpFlowsessSummary": jnxLsysSpFlowsessSummary,
       "jnxLsysSpFlowsessUsedAmount": jnxLsysSpFlowsessUsedAmount,
       "jnxLsysSpFlowsessMaxQuota": jnxLsysSpFlowsessMaxQuota,
       "jnxLsysSpFlowsessAvailableAmount": jnxLsysSpFlowsessAvailableAmount,
       "jnxLsysSpFlowsessHeaviestUsage": jnxLsysSpFlowsessHeaviestUsage,
       "jnxLsysSpFlowsessHeaviestUser": jnxLsysSpFlowsessHeaviestUser,
       "jnxLsysSpFlowsessLightestUsage": jnxLsysSpFlowsessLightestUsage,
       "jnxLsysSpFlowsessLightestUser": jnxLsysSpFlowsessLightestUser}
)
