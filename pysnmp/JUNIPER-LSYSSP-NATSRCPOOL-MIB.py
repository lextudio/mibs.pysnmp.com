# SNMP MIB module (JUNIPER-LSYSSP-NATSRCPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATSRCPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:35 2024
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

(jnxLsysSpNATsrcpool,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATsrcpool")

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

jnxLsysSpNATsrcpoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATsrcpoolObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpoolObjects = _JnxLsysSpNATsrcpoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1)
)
_JnxLsysSpNATsrcpoolTable_Object = MibTable
jnxLsysSpNATsrcpoolTable = _JnxLsysSpNATsrcpoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolTable.setStatus("current")
_JnxLsysSpNATsrcpoolEntry_Object = MibTableRow
jnxLsysSpNATsrcpoolEntry = _JnxLsysSpNATsrcpoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1)
)
jnxLsysSpNATsrcpoolEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATSRCPOOL-MIB", "jnxLsysSpNATsrcpoolLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolEntry.setStatus("current")


class _JnxLsysSpNATsrcpoolLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpoolLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpoolLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpoolLsysName_Object = MibTableColumn
jnxLsysSpNATsrcpoolLsysName = _JnxLsysSpNATsrcpoolLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 1),
    _JnxLsysSpNATsrcpoolLsysName_Type()
)
jnxLsysSpNATsrcpoolLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolLsysName.setStatus("current")


class _JnxLsysSpNATsrcpoolProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpoolProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATsrcpoolProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpoolProfileName_Object = MibTableColumn
jnxLsysSpNATsrcpoolProfileName = _JnxLsysSpNATsrcpoolProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 2),
    _JnxLsysSpNATsrcpoolProfileName_Type()
)
jnxLsysSpNATsrcpoolProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolProfileName.setStatus("current")
_JnxLsysSpNATsrcpoolUsage_Type = Unsigned32
_JnxLsysSpNATsrcpoolUsage_Object = MibTableColumn
jnxLsysSpNATsrcpoolUsage = _JnxLsysSpNATsrcpoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 3),
    _JnxLsysSpNATsrcpoolUsage_Type()
)
jnxLsysSpNATsrcpoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolUsage.setStatus("current")
_JnxLsysSpNATsrcpoolReserved_Type = Unsigned32
_JnxLsysSpNATsrcpoolReserved_Object = MibTableColumn
jnxLsysSpNATsrcpoolReserved = _JnxLsysSpNATsrcpoolReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 4),
    _JnxLsysSpNATsrcpoolReserved_Type()
)
jnxLsysSpNATsrcpoolReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolReserved.setStatus("current")
_JnxLsysSpNATsrcpoolMaximum_Type = Unsigned32
_JnxLsysSpNATsrcpoolMaximum_Object = MibTableColumn
jnxLsysSpNATsrcpoolMaximum = _JnxLsysSpNATsrcpoolMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 5),
    _JnxLsysSpNATsrcpoolMaximum_Type()
)
jnxLsysSpNATsrcpoolMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolMaximum.setStatus("current")
_JnxLsysSpNATsrcpoolSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpoolSummary = _JnxLsysSpNATsrcpoolSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2)
)
_JnxLsysSpNATsrcpoolUsedAmount_Type = Unsigned32
_JnxLsysSpNATsrcpoolUsedAmount_Object = MibScalar
jnxLsysSpNATsrcpoolUsedAmount = _JnxLsysSpNATsrcpoolUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 1),
    _JnxLsysSpNATsrcpoolUsedAmount_Type()
)
jnxLsysSpNATsrcpoolUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolUsedAmount.setStatus("current")
_JnxLsysSpNATsrcpoolMaxQuota_Type = Unsigned32
_JnxLsysSpNATsrcpoolMaxQuota_Object = MibScalar
jnxLsysSpNATsrcpoolMaxQuota = _JnxLsysSpNATsrcpoolMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 2),
    _JnxLsysSpNATsrcpoolMaxQuota_Type()
)
jnxLsysSpNATsrcpoolMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolMaxQuota.setStatus("current")
_JnxLsysSpNATsrcpoolAvailableAmount_Type = Unsigned32
_JnxLsysSpNATsrcpoolAvailableAmount_Object = MibScalar
jnxLsysSpNATsrcpoolAvailableAmount = _JnxLsysSpNATsrcpoolAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 3),
    _JnxLsysSpNATsrcpoolAvailableAmount_Type()
)
jnxLsysSpNATsrcpoolAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolAvailableAmount.setStatus("current")
_JnxLsysSpNATsrcpoolHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATsrcpoolHeaviestUsage_Object = MibScalar
jnxLsysSpNATsrcpoolHeaviestUsage = _JnxLsysSpNATsrcpoolHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 4),
    _JnxLsysSpNATsrcpoolHeaviestUsage_Type()
)
jnxLsysSpNATsrcpoolHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolHeaviestUsage.setStatus("current")


class _JnxLsysSpNATsrcpoolHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpoolHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpoolHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpoolHeaviestUser_Object = MibScalar
jnxLsysSpNATsrcpoolHeaviestUser = _JnxLsysSpNATsrcpoolHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 5),
    _JnxLsysSpNATsrcpoolHeaviestUser_Type()
)
jnxLsysSpNATsrcpoolHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolHeaviestUser.setStatus("current")
_JnxLsysSpNATsrcpoolLightestUsage_Type = Unsigned32
_JnxLsysSpNATsrcpoolLightestUsage_Object = MibScalar
jnxLsysSpNATsrcpoolLightestUsage = _JnxLsysSpNATsrcpoolLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 6),
    _JnxLsysSpNATsrcpoolLightestUsage_Type()
)
jnxLsysSpNATsrcpoolLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolLightestUsage.setStatus("current")


class _JnxLsysSpNATsrcpoolLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpoolLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpoolLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpoolLightestUser_Object = MibScalar
jnxLsysSpNATsrcpoolLightestUser = _JnxLsysSpNATsrcpoolLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 7),
    _JnxLsysSpNATsrcpoolLightestUser_Type()
)
jnxLsysSpNATsrcpoolLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpoolLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATSRCPOOL-MIB",
    **{"jnxLsysSpNATsrcpoolMIB": jnxLsysSpNATsrcpoolMIB,
       "jnxLsysSpNATsrcpoolObjects": jnxLsysSpNATsrcpoolObjects,
       "jnxLsysSpNATsrcpoolTable": jnxLsysSpNATsrcpoolTable,
       "jnxLsysSpNATsrcpoolEntry": jnxLsysSpNATsrcpoolEntry,
       "jnxLsysSpNATsrcpoolLsysName": jnxLsysSpNATsrcpoolLsysName,
       "jnxLsysSpNATsrcpoolProfileName": jnxLsysSpNATsrcpoolProfileName,
       "jnxLsysSpNATsrcpoolUsage": jnxLsysSpNATsrcpoolUsage,
       "jnxLsysSpNATsrcpoolReserved": jnxLsysSpNATsrcpoolReserved,
       "jnxLsysSpNATsrcpoolMaximum": jnxLsysSpNATsrcpoolMaximum,
       "jnxLsysSpNATsrcpoolSummary": jnxLsysSpNATsrcpoolSummary,
       "jnxLsysSpNATsrcpoolUsedAmount": jnxLsysSpNATsrcpoolUsedAmount,
       "jnxLsysSpNATsrcpoolMaxQuota": jnxLsysSpNATsrcpoolMaxQuota,
       "jnxLsysSpNATsrcpoolAvailableAmount": jnxLsysSpNATsrcpoolAvailableAmount,
       "jnxLsysSpNATsrcpoolHeaviestUsage": jnxLsysSpNATsrcpoolHeaviestUsage,
       "jnxLsysSpNATsrcpoolHeaviestUser": jnxLsysSpNATsrcpoolHeaviestUser,
       "jnxLsysSpNATsrcpoolLightestUsage": jnxLsysSpNATsrcpoolLightestUsage,
       "jnxLsysSpNATsrcpoolLightestUser": jnxLsysSpNATsrcpoolLightestUser}
)
