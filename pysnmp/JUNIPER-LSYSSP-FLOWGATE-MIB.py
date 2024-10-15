# SNMP MIB module (JUNIPER-LSYSSP-FLOWGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-FLOWGATE-MIB
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

(jnxLsysSpFlowgate,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpFlowgate")

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

jnxLsysSpFlowgateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpFlowgateObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowgateObjects = _JnxLsysSpFlowgateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1)
)
_JnxLsysSpFlowgateTable_Object = MibTable
jnxLsysSpFlowgateTable = _JnxLsysSpFlowgateTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateTable.setStatus("current")
_JnxLsysSpFlowgateEntry_Object = MibTableRow
jnxLsysSpFlowgateEntry = _JnxLsysSpFlowgateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1)
)
jnxLsysSpFlowgateEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-FLOWGATE-MIB", "jnxLsysSpFlowgateLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateEntry.setStatus("current")


class _JnxLsysSpFlowgateLsysName_Type(DisplayString):
    """Custom type jnxLsysSpFlowgateLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowgateLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpFlowgateLsysName_Object = MibTableColumn
jnxLsysSpFlowgateLsysName = _JnxLsysSpFlowgateLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1, 1),
    _JnxLsysSpFlowgateLsysName_Type()
)
jnxLsysSpFlowgateLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateLsysName.setStatus("current")


class _JnxLsysSpFlowgateProfileName_Type(DisplayString):
    """Custom type jnxLsysSpFlowgateProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpFlowgateProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpFlowgateProfileName_Object = MibTableColumn
jnxLsysSpFlowgateProfileName = _JnxLsysSpFlowgateProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1, 2),
    _JnxLsysSpFlowgateProfileName_Type()
)
jnxLsysSpFlowgateProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateProfileName.setStatus("current")
_JnxLsysSpFlowgateUsage_Type = Unsigned32
_JnxLsysSpFlowgateUsage_Object = MibTableColumn
jnxLsysSpFlowgateUsage = _JnxLsysSpFlowgateUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1, 3),
    _JnxLsysSpFlowgateUsage_Type()
)
jnxLsysSpFlowgateUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateUsage.setStatus("current")
_JnxLsysSpFlowgateReserved_Type = Unsigned32
_JnxLsysSpFlowgateReserved_Object = MibTableColumn
jnxLsysSpFlowgateReserved = _JnxLsysSpFlowgateReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1, 4),
    _JnxLsysSpFlowgateReserved_Type()
)
jnxLsysSpFlowgateReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateReserved.setStatus("current")
_JnxLsysSpFlowgateMaximum_Type = Unsigned32
_JnxLsysSpFlowgateMaximum_Object = MibTableColumn
jnxLsysSpFlowgateMaximum = _JnxLsysSpFlowgateMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 1, 1, 1, 5),
    _JnxLsysSpFlowgateMaximum_Type()
)
jnxLsysSpFlowgateMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateMaximum.setStatus("current")
_JnxLsysSpFlowgateSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowgateSummary = _JnxLsysSpFlowgateSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2)
)
_JnxLsysSpFlowgateUsedAmount_Type = Unsigned32
_JnxLsysSpFlowgateUsedAmount_Object = MibScalar
jnxLsysSpFlowgateUsedAmount = _JnxLsysSpFlowgateUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 1),
    _JnxLsysSpFlowgateUsedAmount_Type()
)
jnxLsysSpFlowgateUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateUsedAmount.setStatus("current")
_JnxLsysSpFlowgateMaxQuota_Type = Unsigned32
_JnxLsysSpFlowgateMaxQuota_Object = MibScalar
jnxLsysSpFlowgateMaxQuota = _JnxLsysSpFlowgateMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 2),
    _JnxLsysSpFlowgateMaxQuota_Type()
)
jnxLsysSpFlowgateMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateMaxQuota.setStatus("current")
_JnxLsysSpFlowgateAvailableAmount_Type = Unsigned32
_JnxLsysSpFlowgateAvailableAmount_Object = MibScalar
jnxLsysSpFlowgateAvailableAmount = _JnxLsysSpFlowgateAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 3),
    _JnxLsysSpFlowgateAvailableAmount_Type()
)
jnxLsysSpFlowgateAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateAvailableAmount.setStatus("current")
_JnxLsysSpFlowgateHeaviestUsage_Type = Unsigned32
_JnxLsysSpFlowgateHeaviestUsage_Object = MibScalar
jnxLsysSpFlowgateHeaviestUsage = _JnxLsysSpFlowgateHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 4),
    _JnxLsysSpFlowgateHeaviestUsage_Type()
)
jnxLsysSpFlowgateHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateHeaviestUsage.setStatus("current")


class _JnxLsysSpFlowgateHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpFlowgateHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowgateHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpFlowgateHeaviestUser_Object = MibScalar
jnxLsysSpFlowgateHeaviestUser = _JnxLsysSpFlowgateHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 5),
    _JnxLsysSpFlowgateHeaviestUser_Type()
)
jnxLsysSpFlowgateHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateHeaviestUser.setStatus("current")
_JnxLsysSpFlowgateLightestUsage_Type = Unsigned32
_JnxLsysSpFlowgateLightestUsage_Object = MibScalar
jnxLsysSpFlowgateLightestUsage = _JnxLsysSpFlowgateLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 6),
    _JnxLsysSpFlowgateLightestUsage_Type()
)
jnxLsysSpFlowgateLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateLightestUsage.setStatus("current")


class _JnxLsysSpFlowgateLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpFlowgateLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpFlowgateLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpFlowgateLightestUser_Object = MibScalar
jnxLsysSpFlowgateLightestUser = _JnxLsysSpFlowgateLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5, 1, 2, 7),
    _JnxLsysSpFlowgateLightestUser_Type()
)
jnxLsysSpFlowgateLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpFlowgateLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-FLOWGATE-MIB",
    **{"jnxLsysSpFlowgateMIB": jnxLsysSpFlowgateMIB,
       "jnxLsysSpFlowgateObjects": jnxLsysSpFlowgateObjects,
       "jnxLsysSpFlowgateTable": jnxLsysSpFlowgateTable,
       "jnxLsysSpFlowgateEntry": jnxLsysSpFlowgateEntry,
       "jnxLsysSpFlowgateLsysName": jnxLsysSpFlowgateLsysName,
       "jnxLsysSpFlowgateProfileName": jnxLsysSpFlowgateProfileName,
       "jnxLsysSpFlowgateUsage": jnxLsysSpFlowgateUsage,
       "jnxLsysSpFlowgateReserved": jnxLsysSpFlowgateReserved,
       "jnxLsysSpFlowgateMaximum": jnxLsysSpFlowgateMaximum,
       "jnxLsysSpFlowgateSummary": jnxLsysSpFlowgateSummary,
       "jnxLsysSpFlowgateUsedAmount": jnxLsysSpFlowgateUsedAmount,
       "jnxLsysSpFlowgateMaxQuota": jnxLsysSpFlowgateMaxQuota,
       "jnxLsysSpFlowgateAvailableAmount": jnxLsysSpFlowgateAvailableAmount,
       "jnxLsysSpFlowgateHeaviestUsage": jnxLsysSpFlowgateHeaviestUsage,
       "jnxLsysSpFlowgateHeaviestUser": jnxLsysSpFlowgateHeaviestUser,
       "jnxLsysSpFlowgateLightestUsage": jnxLsysSpFlowgateLightestUsage,
       "jnxLsysSpFlowgateLightestUser": jnxLsysSpFlowgateLightestUser}
)
