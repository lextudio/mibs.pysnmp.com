# SNMP MIB module (JUNIPER-LSYSSP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-POLICY-MIB
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

(jnxLsysSpPolicy,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpPolicy")

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

jnxLsysSpPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpPolicyObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicyObjects = _JnxLsysSpPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1)
)
_JnxLsysSpPolicyTable_Object = MibTable
jnxLsysSpPolicyTable = _JnxLsysSpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpPolicyTable.setStatus("current")
_JnxLsysSpPolicyEntry_Object = MibTableRow
jnxLsysSpPolicyEntry = _JnxLsysSpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1)
)
jnxLsysSpPolicyEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-POLICY-MIB", "jnxLsysSpPolicyLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpPolicyEntry.setStatus("current")


class _JnxLsysSpPolicyLsysName_Type(DisplayString):
    """Custom type jnxLsysSpPolicyLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicyLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpPolicyLsysName_Object = MibTableColumn
jnxLsysSpPolicyLsysName = _JnxLsysSpPolicyLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 1),
    _JnxLsysSpPolicyLsysName_Type()
)
jnxLsysSpPolicyLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyLsysName.setStatus("current")


class _JnxLsysSpPolicyProfileName_Type(DisplayString):
    """Custom type jnxLsysSpPolicyProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpPolicyProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpPolicyProfileName_Object = MibTableColumn
jnxLsysSpPolicyProfileName = _JnxLsysSpPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 2),
    _JnxLsysSpPolicyProfileName_Type()
)
jnxLsysSpPolicyProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyProfileName.setStatus("current")
_JnxLsysSpPolicyUsage_Type = Unsigned32
_JnxLsysSpPolicyUsage_Object = MibTableColumn
jnxLsysSpPolicyUsage = _JnxLsysSpPolicyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 3),
    _JnxLsysSpPolicyUsage_Type()
)
jnxLsysSpPolicyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyUsage.setStatus("current")
_JnxLsysSpPolicyReserved_Type = Unsigned32
_JnxLsysSpPolicyReserved_Object = MibTableColumn
jnxLsysSpPolicyReserved = _JnxLsysSpPolicyReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 4),
    _JnxLsysSpPolicyReserved_Type()
)
jnxLsysSpPolicyReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyReserved.setStatus("current")
_JnxLsysSpPolicyMaximum_Type = Unsigned32
_JnxLsysSpPolicyMaximum_Object = MibTableColumn
jnxLsysSpPolicyMaximum = _JnxLsysSpPolicyMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 5),
    _JnxLsysSpPolicyMaximum_Type()
)
jnxLsysSpPolicyMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyMaximum.setStatus("current")
_JnxLsysSpPolicySummary_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicySummary = _JnxLsysSpPolicySummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2)
)
_JnxLsysSpPolicyUsedAmount_Type = Unsigned32
_JnxLsysSpPolicyUsedAmount_Object = MibScalar
jnxLsysSpPolicyUsedAmount = _JnxLsysSpPolicyUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 1),
    _JnxLsysSpPolicyUsedAmount_Type()
)
jnxLsysSpPolicyUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyUsedAmount.setStatus("current")
_JnxLsysSpPolicyMaxQuota_Type = Unsigned32
_JnxLsysSpPolicyMaxQuota_Object = MibScalar
jnxLsysSpPolicyMaxQuota = _JnxLsysSpPolicyMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 2),
    _JnxLsysSpPolicyMaxQuota_Type()
)
jnxLsysSpPolicyMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyMaxQuota.setStatus("current")
_JnxLsysSpPolicyAvailableAmount_Type = Unsigned32
_JnxLsysSpPolicyAvailableAmount_Object = MibScalar
jnxLsysSpPolicyAvailableAmount = _JnxLsysSpPolicyAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 3),
    _JnxLsysSpPolicyAvailableAmount_Type()
)
jnxLsysSpPolicyAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyAvailableAmount.setStatus("current")
_JnxLsysSpPolicyHeaviestUsage_Type = Unsigned32
_JnxLsysSpPolicyHeaviestUsage_Object = MibScalar
jnxLsysSpPolicyHeaviestUsage = _JnxLsysSpPolicyHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 4),
    _JnxLsysSpPolicyHeaviestUsage_Type()
)
jnxLsysSpPolicyHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyHeaviestUsage.setStatus("current")


class _JnxLsysSpPolicyHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpPolicyHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicyHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpPolicyHeaviestUser_Object = MibScalar
jnxLsysSpPolicyHeaviestUser = _JnxLsysSpPolicyHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 5),
    _JnxLsysSpPolicyHeaviestUser_Type()
)
jnxLsysSpPolicyHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyHeaviestUser.setStatus("current")
_JnxLsysSpPolicyLightestUsage_Type = Unsigned32
_JnxLsysSpPolicyLightestUsage_Object = MibScalar
jnxLsysSpPolicyLightestUsage = _JnxLsysSpPolicyLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 6),
    _JnxLsysSpPolicyLightestUsage_Type()
)
jnxLsysSpPolicyLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyLightestUsage.setStatus("current")


class _JnxLsysSpPolicyLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpPolicyLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicyLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpPolicyLightestUser_Object = MibScalar
jnxLsysSpPolicyLightestUser = _JnxLsysSpPolicyLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 7),
    _JnxLsysSpPolicyLightestUser_Type()
)
jnxLsysSpPolicyLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicyLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-POLICY-MIB",
    **{"jnxLsysSpPolicyMIB": jnxLsysSpPolicyMIB,
       "jnxLsysSpPolicyObjects": jnxLsysSpPolicyObjects,
       "jnxLsysSpPolicyTable": jnxLsysSpPolicyTable,
       "jnxLsysSpPolicyEntry": jnxLsysSpPolicyEntry,
       "jnxLsysSpPolicyLsysName": jnxLsysSpPolicyLsysName,
       "jnxLsysSpPolicyProfileName": jnxLsysSpPolicyProfileName,
       "jnxLsysSpPolicyUsage": jnxLsysSpPolicyUsage,
       "jnxLsysSpPolicyReserved": jnxLsysSpPolicyReserved,
       "jnxLsysSpPolicyMaximum": jnxLsysSpPolicyMaximum,
       "jnxLsysSpPolicySummary": jnxLsysSpPolicySummary,
       "jnxLsysSpPolicyUsedAmount": jnxLsysSpPolicyUsedAmount,
       "jnxLsysSpPolicyMaxQuota": jnxLsysSpPolicyMaxQuota,
       "jnxLsysSpPolicyAvailableAmount": jnxLsysSpPolicyAvailableAmount,
       "jnxLsysSpPolicyHeaviestUsage": jnxLsysSpPolicyHeaviestUsage,
       "jnxLsysSpPolicyHeaviestUser": jnxLsysSpPolicyHeaviestUser,
       "jnxLsysSpPolicyLightestUsage": jnxLsysSpPolicyLightestUsage,
       "jnxLsysSpPolicyLightestUser": jnxLsysSpPolicyLightestUser}
)
