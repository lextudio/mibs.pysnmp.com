# SNMP MIB module (JUNIPER-LSYSSP-POLICYWCNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-POLICYWCNT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:38 2024
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

(jnxLsysSpPolicywcnt,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpPolicywcnt")

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

jnxLsysSpPolicywcntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpPolicywcntObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicywcntObjects = _JnxLsysSpPolicywcntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1)
)
_JnxLsysSpPolicywcntTable_Object = MibTable
jnxLsysSpPolicywcntTable = _JnxLsysSpPolicywcntTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntTable.setStatus("current")
_JnxLsysSpPolicywcntEntry_Object = MibTableRow
jnxLsysSpPolicywcntEntry = _JnxLsysSpPolicywcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1)
)
jnxLsysSpPolicywcntEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-POLICYWCNT-MIB", "jnxLsysSpPolicywcntLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntEntry.setStatus("current")


class _JnxLsysSpPolicywcntLsysName_Type(DisplayString):
    """Custom type jnxLsysSpPolicywcntLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicywcntLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpPolicywcntLsysName_Object = MibTableColumn
jnxLsysSpPolicywcntLsysName = _JnxLsysSpPolicywcntLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1, 1),
    _JnxLsysSpPolicywcntLsysName_Type()
)
jnxLsysSpPolicywcntLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntLsysName.setStatus("current")


class _JnxLsysSpPolicywcntProfileName_Type(DisplayString):
    """Custom type jnxLsysSpPolicywcntProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpPolicywcntProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpPolicywcntProfileName_Object = MibTableColumn
jnxLsysSpPolicywcntProfileName = _JnxLsysSpPolicywcntProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1, 2),
    _JnxLsysSpPolicywcntProfileName_Type()
)
jnxLsysSpPolicywcntProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntProfileName.setStatus("current")
_JnxLsysSpPolicywcntUsage_Type = Unsigned32
_JnxLsysSpPolicywcntUsage_Object = MibTableColumn
jnxLsysSpPolicywcntUsage = _JnxLsysSpPolicywcntUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1, 3),
    _JnxLsysSpPolicywcntUsage_Type()
)
jnxLsysSpPolicywcntUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntUsage.setStatus("current")
_JnxLsysSpPolicywcntReserved_Type = Unsigned32
_JnxLsysSpPolicywcntReserved_Object = MibTableColumn
jnxLsysSpPolicywcntReserved = _JnxLsysSpPolicywcntReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1, 4),
    _JnxLsysSpPolicywcntReserved_Type()
)
jnxLsysSpPolicywcntReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntReserved.setStatus("current")
_JnxLsysSpPolicywcntMaximum_Type = Unsigned32
_JnxLsysSpPolicywcntMaximum_Object = MibTableColumn
jnxLsysSpPolicywcntMaximum = _JnxLsysSpPolicywcntMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 1, 1, 1, 5),
    _JnxLsysSpPolicywcntMaximum_Type()
)
jnxLsysSpPolicywcntMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntMaximum.setStatus("current")
_JnxLsysSpPolicywcntSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicywcntSummary = _JnxLsysSpPolicywcntSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2)
)
_JnxLsysSpPolicywcntUsedAmount_Type = Unsigned32
_JnxLsysSpPolicywcntUsedAmount_Object = MibScalar
jnxLsysSpPolicywcntUsedAmount = _JnxLsysSpPolicywcntUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 1),
    _JnxLsysSpPolicywcntUsedAmount_Type()
)
jnxLsysSpPolicywcntUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntUsedAmount.setStatus("current")
_JnxLsysSpPolicywcntMaxQuota_Type = Unsigned32
_JnxLsysSpPolicywcntMaxQuota_Object = MibScalar
jnxLsysSpPolicywcntMaxQuota = _JnxLsysSpPolicywcntMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 2),
    _JnxLsysSpPolicywcntMaxQuota_Type()
)
jnxLsysSpPolicywcntMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntMaxQuota.setStatus("current")
_JnxLsysSpPolicywcntAvailableAmount_Type = Unsigned32
_JnxLsysSpPolicywcntAvailableAmount_Object = MibScalar
jnxLsysSpPolicywcntAvailableAmount = _JnxLsysSpPolicywcntAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 3),
    _JnxLsysSpPolicywcntAvailableAmount_Type()
)
jnxLsysSpPolicywcntAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntAvailableAmount.setStatus("current")
_JnxLsysSpPolicywcntHeaviestUsage_Type = Unsigned32
_JnxLsysSpPolicywcntHeaviestUsage_Object = MibScalar
jnxLsysSpPolicywcntHeaviestUsage = _JnxLsysSpPolicywcntHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 4),
    _JnxLsysSpPolicywcntHeaviestUsage_Type()
)
jnxLsysSpPolicywcntHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntHeaviestUsage.setStatus("current")


class _JnxLsysSpPolicywcntHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpPolicywcntHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicywcntHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpPolicywcntHeaviestUser_Object = MibScalar
jnxLsysSpPolicywcntHeaviestUser = _JnxLsysSpPolicywcntHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 5),
    _JnxLsysSpPolicywcntHeaviestUser_Type()
)
jnxLsysSpPolicywcntHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntHeaviestUser.setStatus("current")
_JnxLsysSpPolicywcntLightestUsage_Type = Unsigned32
_JnxLsysSpPolicywcntLightestUsage_Object = MibScalar
jnxLsysSpPolicywcntLightestUsage = _JnxLsysSpPolicywcntLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 6),
    _JnxLsysSpPolicywcntLightestUsage_Type()
)
jnxLsysSpPolicywcntLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntLightestUsage.setStatus("current")


class _JnxLsysSpPolicywcntLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpPolicywcntLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpPolicywcntLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpPolicywcntLightestUser_Object = MibScalar
jnxLsysSpPolicywcntLightestUser = _JnxLsysSpPolicywcntLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4, 1, 2, 7),
    _JnxLsysSpPolicywcntLightestUser_Type()
)
jnxLsysSpPolicywcntLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpPolicywcntLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-POLICYWCNT-MIB",
    **{"jnxLsysSpPolicywcntMIB": jnxLsysSpPolicywcntMIB,
       "jnxLsysSpPolicywcntObjects": jnxLsysSpPolicywcntObjects,
       "jnxLsysSpPolicywcntTable": jnxLsysSpPolicywcntTable,
       "jnxLsysSpPolicywcntEntry": jnxLsysSpPolicywcntEntry,
       "jnxLsysSpPolicywcntLsysName": jnxLsysSpPolicywcntLsysName,
       "jnxLsysSpPolicywcntProfileName": jnxLsysSpPolicywcntProfileName,
       "jnxLsysSpPolicywcntUsage": jnxLsysSpPolicywcntUsage,
       "jnxLsysSpPolicywcntReserved": jnxLsysSpPolicywcntReserved,
       "jnxLsysSpPolicywcntMaximum": jnxLsysSpPolicywcntMaximum,
       "jnxLsysSpPolicywcntSummary": jnxLsysSpPolicywcntSummary,
       "jnxLsysSpPolicywcntUsedAmount": jnxLsysSpPolicywcntUsedAmount,
       "jnxLsysSpPolicywcntMaxQuota": jnxLsysSpPolicywcntMaxQuota,
       "jnxLsysSpPolicywcntAvailableAmount": jnxLsysSpPolicywcntAvailableAmount,
       "jnxLsysSpPolicywcntHeaviestUsage": jnxLsysSpPolicywcntHeaviestUsage,
       "jnxLsysSpPolicywcntHeaviestUser": jnxLsysSpPolicywcntHeaviestUser,
       "jnxLsysSpPolicywcntLightestUsage": jnxLsysSpPolicywcntLightestUsage,
       "jnxLsysSpPolicywcntLightestUser": jnxLsysSpPolicywcntLightestUser}
)
