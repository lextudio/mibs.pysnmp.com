# SNMP MIB module (JUNIPER-LSYSSP-NATDSTPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATDSTPOOL-MIB
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

(jnxLsysSpNATdstpool,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATdstpool")

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

jnxLsysSpNATdstpoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATdstpoolObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstpoolObjects = _JnxLsysSpNATdstpoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1)
)
_JnxLsysSpNATdstpoolTable_Object = MibTable
jnxLsysSpNATdstpoolTable = _JnxLsysSpNATdstpoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolTable.setStatus("current")
_JnxLsysSpNATdstpoolEntry_Object = MibTableRow
jnxLsysSpNATdstpoolEntry = _JnxLsysSpNATdstpoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1)
)
jnxLsysSpNATdstpoolEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATDSTPOOL-MIB", "jnxLsysSpNATdstpoolLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolEntry.setStatus("current")


class _JnxLsysSpNATdstpoolLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATdstpoolLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstpoolLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstpoolLsysName_Object = MibTableColumn
jnxLsysSpNATdstpoolLsysName = _JnxLsysSpNATdstpoolLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1, 1),
    _JnxLsysSpNATdstpoolLsysName_Type()
)
jnxLsysSpNATdstpoolLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolLsysName.setStatus("current")


class _JnxLsysSpNATdstpoolProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATdstpoolProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATdstpoolProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstpoolProfileName_Object = MibTableColumn
jnxLsysSpNATdstpoolProfileName = _JnxLsysSpNATdstpoolProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1, 2),
    _JnxLsysSpNATdstpoolProfileName_Type()
)
jnxLsysSpNATdstpoolProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolProfileName.setStatus("current")
_JnxLsysSpNATdstpoolUsage_Type = Unsigned32
_JnxLsysSpNATdstpoolUsage_Object = MibTableColumn
jnxLsysSpNATdstpoolUsage = _JnxLsysSpNATdstpoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1, 3),
    _JnxLsysSpNATdstpoolUsage_Type()
)
jnxLsysSpNATdstpoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolUsage.setStatus("current")
_JnxLsysSpNATdstpoolReserved_Type = Unsigned32
_JnxLsysSpNATdstpoolReserved_Object = MibTableColumn
jnxLsysSpNATdstpoolReserved = _JnxLsysSpNATdstpoolReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1, 4),
    _JnxLsysSpNATdstpoolReserved_Type()
)
jnxLsysSpNATdstpoolReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolReserved.setStatus("current")
_JnxLsysSpNATdstpoolMaximum_Type = Unsigned32
_JnxLsysSpNATdstpoolMaximum_Object = MibTableColumn
jnxLsysSpNATdstpoolMaximum = _JnxLsysSpNATdstpoolMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 1, 1, 1, 5),
    _JnxLsysSpNATdstpoolMaximum_Type()
)
jnxLsysSpNATdstpoolMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolMaximum.setStatus("current")
_JnxLsysSpNATdstpoolSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstpoolSummary = _JnxLsysSpNATdstpoolSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2)
)
_JnxLsysSpNATdstpoolUsedAmount_Type = Unsigned32
_JnxLsysSpNATdstpoolUsedAmount_Object = MibScalar
jnxLsysSpNATdstpoolUsedAmount = _JnxLsysSpNATdstpoolUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 1),
    _JnxLsysSpNATdstpoolUsedAmount_Type()
)
jnxLsysSpNATdstpoolUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolUsedAmount.setStatus("current")
_JnxLsysSpNATdstpoolMaxQuota_Type = Unsigned32
_JnxLsysSpNATdstpoolMaxQuota_Object = MibScalar
jnxLsysSpNATdstpoolMaxQuota = _JnxLsysSpNATdstpoolMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 2),
    _JnxLsysSpNATdstpoolMaxQuota_Type()
)
jnxLsysSpNATdstpoolMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolMaxQuota.setStatus("current")
_JnxLsysSpNATdstpoolAvailableAmount_Type = Unsigned32
_JnxLsysSpNATdstpoolAvailableAmount_Object = MibScalar
jnxLsysSpNATdstpoolAvailableAmount = _JnxLsysSpNATdstpoolAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 3),
    _JnxLsysSpNATdstpoolAvailableAmount_Type()
)
jnxLsysSpNATdstpoolAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolAvailableAmount.setStatus("current")
_JnxLsysSpNATdstpoolHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATdstpoolHeaviestUsage_Object = MibScalar
jnxLsysSpNATdstpoolHeaviestUsage = _JnxLsysSpNATdstpoolHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 4),
    _JnxLsysSpNATdstpoolHeaviestUsage_Type()
)
jnxLsysSpNATdstpoolHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolHeaviestUsage.setStatus("current")


class _JnxLsysSpNATdstpoolHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATdstpoolHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstpoolHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstpoolHeaviestUser_Object = MibScalar
jnxLsysSpNATdstpoolHeaviestUser = _JnxLsysSpNATdstpoolHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 5),
    _JnxLsysSpNATdstpoolHeaviestUser_Type()
)
jnxLsysSpNATdstpoolHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolHeaviestUser.setStatus("current")
_JnxLsysSpNATdstpoolLightestUsage_Type = Unsigned32
_JnxLsysSpNATdstpoolLightestUsage_Object = MibScalar
jnxLsysSpNATdstpoolLightestUsage = _JnxLsysSpNATdstpoolLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 6),
    _JnxLsysSpNATdstpoolLightestUsage_Type()
)
jnxLsysSpNATdstpoolLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolLightestUsage.setStatus("current")


class _JnxLsysSpNATdstpoolLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATdstpoolLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATdstpoolLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATdstpoolLightestUser_Object = MibScalar
jnxLsysSpNATdstpoolLightestUser = _JnxLsysSpNATdstpoolLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9, 1, 2, 7),
    _JnxLsysSpNATdstpoolLightestUser_Type()
)
jnxLsysSpNATdstpoolLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATdstpoolLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATDSTPOOL-MIB",
    **{"jnxLsysSpNATdstpoolMIB": jnxLsysSpNATdstpoolMIB,
       "jnxLsysSpNATdstpoolObjects": jnxLsysSpNATdstpoolObjects,
       "jnxLsysSpNATdstpoolTable": jnxLsysSpNATdstpoolTable,
       "jnxLsysSpNATdstpoolEntry": jnxLsysSpNATdstpoolEntry,
       "jnxLsysSpNATdstpoolLsysName": jnxLsysSpNATdstpoolLsysName,
       "jnxLsysSpNATdstpoolProfileName": jnxLsysSpNATdstpoolProfileName,
       "jnxLsysSpNATdstpoolUsage": jnxLsysSpNATdstpoolUsage,
       "jnxLsysSpNATdstpoolReserved": jnxLsysSpNATdstpoolReserved,
       "jnxLsysSpNATdstpoolMaximum": jnxLsysSpNATdstpoolMaximum,
       "jnxLsysSpNATdstpoolSummary": jnxLsysSpNATdstpoolSummary,
       "jnxLsysSpNATdstpoolUsedAmount": jnxLsysSpNATdstpoolUsedAmount,
       "jnxLsysSpNATdstpoolMaxQuota": jnxLsysSpNATdstpoolMaxQuota,
       "jnxLsysSpNATdstpoolAvailableAmount": jnxLsysSpNATdstpoolAvailableAmount,
       "jnxLsysSpNATdstpoolHeaviestUsage": jnxLsysSpNATdstpoolHeaviestUsage,
       "jnxLsysSpNATdstpoolHeaviestUser": jnxLsysSpNATdstpoolHeaviestUser,
       "jnxLsysSpNATdstpoolLightestUsage": jnxLsysSpNATdstpoolLightestUsage,
       "jnxLsysSpNATdstpoolLightestUser": jnxLsysSpNATdstpoolLightestUser}
)
