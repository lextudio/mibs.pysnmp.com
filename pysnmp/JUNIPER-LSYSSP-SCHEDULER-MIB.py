# SNMP MIB module (JUNIPER-LSYSSP-SCHEDULER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-SCHEDULER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:39 2024
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

(jnxLsysSpScheduler,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpScheduler")

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

jnxLsysSpSchedulerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpSchedulerObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpSchedulerObjects = _JnxLsysSpSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1)
)
_JnxLsysSpSchedulerTable_Object = MibTable
jnxLsysSpSchedulerTable = _JnxLsysSpSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerTable.setStatus("current")
_JnxLsysSpSchedulerEntry_Object = MibTableRow
jnxLsysSpSchedulerEntry = _JnxLsysSpSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1)
)
jnxLsysSpSchedulerEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-SCHEDULER-MIB", "jnxLsysSpSchedulerLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerEntry.setStatus("current")


class _JnxLsysSpSchedulerLsysName_Type(DisplayString):
    """Custom type jnxLsysSpSchedulerLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSchedulerLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpSchedulerLsysName_Object = MibTableColumn
jnxLsysSpSchedulerLsysName = _JnxLsysSpSchedulerLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 1),
    _JnxLsysSpSchedulerLsysName_Type()
)
jnxLsysSpSchedulerLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerLsysName.setStatus("current")


class _JnxLsysSpSchedulerProfileName_Type(DisplayString):
    """Custom type jnxLsysSpSchedulerProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpSchedulerProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpSchedulerProfileName_Object = MibTableColumn
jnxLsysSpSchedulerProfileName = _JnxLsysSpSchedulerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 2),
    _JnxLsysSpSchedulerProfileName_Type()
)
jnxLsysSpSchedulerProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerProfileName.setStatus("current")
_JnxLsysSpSchedulerUsage_Type = Unsigned32
_JnxLsysSpSchedulerUsage_Object = MibTableColumn
jnxLsysSpSchedulerUsage = _JnxLsysSpSchedulerUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 3),
    _JnxLsysSpSchedulerUsage_Type()
)
jnxLsysSpSchedulerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerUsage.setStatus("current")
_JnxLsysSpSchedulerReserved_Type = Unsigned32
_JnxLsysSpSchedulerReserved_Object = MibTableColumn
jnxLsysSpSchedulerReserved = _JnxLsysSpSchedulerReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 4),
    _JnxLsysSpSchedulerReserved_Type()
)
jnxLsysSpSchedulerReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerReserved.setStatus("current")
_JnxLsysSpSchedulerMaximum_Type = Unsigned32
_JnxLsysSpSchedulerMaximum_Object = MibTableColumn
jnxLsysSpSchedulerMaximum = _JnxLsysSpSchedulerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 5),
    _JnxLsysSpSchedulerMaximum_Type()
)
jnxLsysSpSchedulerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerMaximum.setStatus("current")
_JnxLsysSpSchedulerSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpSchedulerSummary = _JnxLsysSpSchedulerSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2)
)
_JnxLsysSpSchedulerUsedAmount_Type = Unsigned32
_JnxLsysSpSchedulerUsedAmount_Object = MibScalar
jnxLsysSpSchedulerUsedAmount = _JnxLsysSpSchedulerUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 1),
    _JnxLsysSpSchedulerUsedAmount_Type()
)
jnxLsysSpSchedulerUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerUsedAmount.setStatus("current")
_JnxLsysSpSchedulerMaxQuota_Type = Unsigned32
_JnxLsysSpSchedulerMaxQuota_Object = MibScalar
jnxLsysSpSchedulerMaxQuota = _JnxLsysSpSchedulerMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 2),
    _JnxLsysSpSchedulerMaxQuota_Type()
)
jnxLsysSpSchedulerMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerMaxQuota.setStatus("current")
_JnxLsysSpSchedulerAvailableAmount_Type = Unsigned32
_JnxLsysSpSchedulerAvailableAmount_Object = MibScalar
jnxLsysSpSchedulerAvailableAmount = _JnxLsysSpSchedulerAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 3),
    _JnxLsysSpSchedulerAvailableAmount_Type()
)
jnxLsysSpSchedulerAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerAvailableAmount.setStatus("current")
_JnxLsysSpSchedulerHeaviestUsage_Type = Unsigned32
_JnxLsysSpSchedulerHeaviestUsage_Object = MibScalar
jnxLsysSpSchedulerHeaviestUsage = _JnxLsysSpSchedulerHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 4),
    _JnxLsysSpSchedulerHeaviestUsage_Type()
)
jnxLsysSpSchedulerHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerHeaviestUsage.setStatus("current")


class _JnxLsysSpSchedulerHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpSchedulerHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSchedulerHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSchedulerHeaviestUser_Object = MibScalar
jnxLsysSpSchedulerHeaviestUser = _JnxLsysSpSchedulerHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 5),
    _JnxLsysSpSchedulerHeaviestUser_Type()
)
jnxLsysSpSchedulerHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerHeaviestUser.setStatus("current")
_JnxLsysSpSchedulerLightestUsage_Type = Unsigned32
_JnxLsysSpSchedulerLightestUsage_Object = MibScalar
jnxLsysSpSchedulerLightestUsage = _JnxLsysSpSchedulerLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 6),
    _JnxLsysSpSchedulerLightestUsage_Type()
)
jnxLsysSpSchedulerLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerLightestUsage.setStatus("current")


class _JnxLsysSpSchedulerLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpSchedulerLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSchedulerLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSchedulerLightestUser_Object = MibScalar
jnxLsysSpSchedulerLightestUser = _JnxLsysSpSchedulerLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 7),
    _JnxLsysSpSchedulerLightestUser_Type()
)
jnxLsysSpSchedulerLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSchedulerLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-SCHEDULER-MIB",
    **{"jnxLsysSpSchedulerMIB": jnxLsysSpSchedulerMIB,
       "jnxLsysSpSchedulerObjects": jnxLsysSpSchedulerObjects,
       "jnxLsysSpSchedulerTable": jnxLsysSpSchedulerTable,
       "jnxLsysSpSchedulerEntry": jnxLsysSpSchedulerEntry,
       "jnxLsysSpSchedulerLsysName": jnxLsysSpSchedulerLsysName,
       "jnxLsysSpSchedulerProfileName": jnxLsysSpSchedulerProfileName,
       "jnxLsysSpSchedulerUsage": jnxLsysSpSchedulerUsage,
       "jnxLsysSpSchedulerReserved": jnxLsysSpSchedulerReserved,
       "jnxLsysSpSchedulerMaximum": jnxLsysSpSchedulerMaximum,
       "jnxLsysSpSchedulerSummary": jnxLsysSpSchedulerSummary,
       "jnxLsysSpSchedulerUsedAmount": jnxLsysSpSchedulerUsedAmount,
       "jnxLsysSpSchedulerMaxQuota": jnxLsysSpSchedulerMaxQuota,
       "jnxLsysSpSchedulerAvailableAmount": jnxLsysSpSchedulerAvailableAmount,
       "jnxLsysSpSchedulerHeaviestUsage": jnxLsysSpSchedulerHeaviestUsage,
       "jnxLsysSpSchedulerHeaviestUser": jnxLsysSpSchedulerHeaviestUser,
       "jnxLsysSpSchedulerLightestUsage": jnxLsysSpSchedulerLightestUsage,
       "jnxLsysSpSchedulerLightestUser": jnxLsysSpSchedulerLightestUser}
)
