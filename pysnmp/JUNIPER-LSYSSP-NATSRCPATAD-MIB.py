# SNMP MIB module (JUNIPER-LSYSSP-NATSRCPATAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATSRCPATAD-MIB
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

(jnxLsysSpNATsrcpatad,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATsrcpatad")

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

jnxLsysSpNATsrcpatadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATsrcpatadObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpatadObjects = _JnxLsysSpNATsrcpatadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1)
)
_JnxLsysSpNATsrcpatadTable_Object = MibTable
jnxLsysSpNATsrcpatadTable = _JnxLsysSpNATsrcpatadTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadTable.setStatus("current")
_JnxLsysSpNATsrcpatadEntry_Object = MibTableRow
jnxLsysSpNATsrcpatadEntry = _JnxLsysSpNATsrcpatadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1)
)
jnxLsysSpNATsrcpatadEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATSRCPATAD-MIB", "jnxLsysSpNATsrcpatadLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadEntry.setStatus("current")


class _JnxLsysSpNATsrcpatadLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpatadLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpatadLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpatadLsysName_Object = MibTableColumn
jnxLsysSpNATsrcpatadLsysName = _JnxLsysSpNATsrcpatadLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 1),
    _JnxLsysSpNATsrcpatadLsysName_Type()
)
jnxLsysSpNATsrcpatadLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadLsysName.setStatus("current")


class _JnxLsysSpNATsrcpatadProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpatadProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATsrcpatadProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpatadProfileName_Object = MibTableColumn
jnxLsysSpNATsrcpatadProfileName = _JnxLsysSpNATsrcpatadProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 2),
    _JnxLsysSpNATsrcpatadProfileName_Type()
)
jnxLsysSpNATsrcpatadProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadProfileName.setStatus("current")
_JnxLsysSpNATsrcpatadUsage_Type = Unsigned32
_JnxLsysSpNATsrcpatadUsage_Object = MibTableColumn
jnxLsysSpNATsrcpatadUsage = _JnxLsysSpNATsrcpatadUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 3),
    _JnxLsysSpNATsrcpatadUsage_Type()
)
jnxLsysSpNATsrcpatadUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadUsage.setStatus("current")
_JnxLsysSpNATsrcpatadReserved_Type = Unsigned32
_JnxLsysSpNATsrcpatadReserved_Object = MibTableColumn
jnxLsysSpNATsrcpatadReserved = _JnxLsysSpNATsrcpatadReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 4),
    _JnxLsysSpNATsrcpatadReserved_Type()
)
jnxLsysSpNATsrcpatadReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadReserved.setStatus("current")
_JnxLsysSpNATsrcpatadMaximum_Type = Unsigned32
_JnxLsysSpNATsrcpatadMaximum_Object = MibTableColumn
jnxLsysSpNATsrcpatadMaximum = _JnxLsysSpNATsrcpatadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 5),
    _JnxLsysSpNATsrcpatadMaximum_Type()
)
jnxLsysSpNATsrcpatadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadMaximum.setStatus("current")
_JnxLsysSpNATsrcpatadSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpatadSummary = _JnxLsysSpNATsrcpatadSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2)
)
_JnxLsysSpNATsrcpatadUsedAmount_Type = Unsigned32
_JnxLsysSpNATsrcpatadUsedAmount_Object = MibScalar
jnxLsysSpNATsrcpatadUsedAmount = _JnxLsysSpNATsrcpatadUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 1),
    _JnxLsysSpNATsrcpatadUsedAmount_Type()
)
jnxLsysSpNATsrcpatadUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadUsedAmount.setStatus("current")
_JnxLsysSpNATsrcpatadMaxQuota_Type = Unsigned32
_JnxLsysSpNATsrcpatadMaxQuota_Object = MibScalar
jnxLsysSpNATsrcpatadMaxQuota = _JnxLsysSpNATsrcpatadMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 2),
    _JnxLsysSpNATsrcpatadMaxQuota_Type()
)
jnxLsysSpNATsrcpatadMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadMaxQuota.setStatus("current")
_JnxLsysSpNATsrcpatadAvailableAmount_Type = Unsigned32
_JnxLsysSpNATsrcpatadAvailableAmount_Object = MibScalar
jnxLsysSpNATsrcpatadAvailableAmount = _JnxLsysSpNATsrcpatadAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 3),
    _JnxLsysSpNATsrcpatadAvailableAmount_Type()
)
jnxLsysSpNATsrcpatadAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadAvailableAmount.setStatus("current")
_JnxLsysSpNATsrcpatadHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATsrcpatadHeaviestUsage_Object = MibScalar
jnxLsysSpNATsrcpatadHeaviestUsage = _JnxLsysSpNATsrcpatadHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 4),
    _JnxLsysSpNATsrcpatadHeaviestUsage_Type()
)
jnxLsysSpNATsrcpatadHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadHeaviestUsage.setStatus("current")


class _JnxLsysSpNATsrcpatadHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpatadHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpatadHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpatadHeaviestUser_Object = MibScalar
jnxLsysSpNATsrcpatadHeaviestUser = _JnxLsysSpNATsrcpatadHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 5),
    _JnxLsysSpNATsrcpatadHeaviestUser_Type()
)
jnxLsysSpNATsrcpatadHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadHeaviestUser.setStatus("current")
_JnxLsysSpNATsrcpatadLightestUsage_Type = Unsigned32
_JnxLsysSpNATsrcpatadLightestUsage_Object = MibScalar
jnxLsysSpNATsrcpatadLightestUsage = _JnxLsysSpNATsrcpatadLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 6),
    _JnxLsysSpNATsrcpatadLightestUsage_Type()
)
jnxLsysSpNATsrcpatadLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadLightestUsage.setStatus("current")


class _JnxLsysSpNATsrcpatadLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcpatadLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcpatadLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcpatadLightestUser_Object = MibScalar
jnxLsysSpNATsrcpatadLightestUser = _JnxLsysSpNATsrcpatadLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 7),
    _JnxLsysSpNATsrcpatadLightestUser_Type()
)
jnxLsysSpNATsrcpatadLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcpatadLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATSRCPATAD-MIB",
    **{"jnxLsysSpNATsrcpatadMIB": jnxLsysSpNATsrcpatadMIB,
       "jnxLsysSpNATsrcpatadObjects": jnxLsysSpNATsrcpatadObjects,
       "jnxLsysSpNATsrcpatadTable": jnxLsysSpNATsrcpatadTable,
       "jnxLsysSpNATsrcpatadEntry": jnxLsysSpNATsrcpatadEntry,
       "jnxLsysSpNATsrcpatadLsysName": jnxLsysSpNATsrcpatadLsysName,
       "jnxLsysSpNATsrcpatadProfileName": jnxLsysSpNATsrcpatadProfileName,
       "jnxLsysSpNATsrcpatadUsage": jnxLsysSpNATsrcpatadUsage,
       "jnxLsysSpNATsrcpatadReserved": jnxLsysSpNATsrcpatadReserved,
       "jnxLsysSpNATsrcpatadMaximum": jnxLsysSpNATsrcpatadMaximum,
       "jnxLsysSpNATsrcpatadSummary": jnxLsysSpNATsrcpatadSummary,
       "jnxLsysSpNATsrcpatadUsedAmount": jnxLsysSpNATsrcpatadUsedAmount,
       "jnxLsysSpNATsrcpatadMaxQuota": jnxLsysSpNATsrcpatadMaxQuota,
       "jnxLsysSpNATsrcpatadAvailableAmount": jnxLsysSpNATsrcpatadAvailableAmount,
       "jnxLsysSpNATsrcpatadHeaviestUsage": jnxLsysSpNATsrcpatadHeaviestUsage,
       "jnxLsysSpNATsrcpatadHeaviestUser": jnxLsysSpNATsrcpatadHeaviestUser,
       "jnxLsysSpNATsrcpatadLightestUsage": jnxLsysSpNATsrcpatadLightestUsage,
       "jnxLsysSpNATsrcpatadLightestUser": jnxLsysSpNATsrcpatadLightestUser}
)
