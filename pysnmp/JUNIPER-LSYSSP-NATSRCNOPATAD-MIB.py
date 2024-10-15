# SNMP MIB module (JUNIPER-LSYSSP-NATSRCNOPATAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-NATSRCNOPATAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:34 2024
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

(jnxLsysSpNATsrcnopatad,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATsrcnopatad")

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

jnxLsysSpNATsrcnopatadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATsrcnopatadObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcnopatadObjects = _JnxLsysSpNATsrcnopatadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1)
)
_JnxLsysSpNATsrcnopatadTable_Object = MibTable
jnxLsysSpNATsrcnopatadTable = _JnxLsysSpNATsrcnopatadTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadTable.setStatus("current")
_JnxLsysSpNATsrcnopatadEntry_Object = MibTableRow
jnxLsysSpNATsrcnopatadEntry = _JnxLsysSpNATsrcnopatadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1)
)
jnxLsysSpNATsrcnopatadEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", "jnxLsysSpNATsrcnopatadLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadEntry.setStatus("current")


class _JnxLsysSpNATsrcnopatadLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcnopatadLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcnopatadLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcnopatadLsysName_Object = MibTableColumn
jnxLsysSpNATsrcnopatadLsysName = _JnxLsysSpNATsrcnopatadLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 1),
    _JnxLsysSpNATsrcnopatadLsysName_Type()
)
jnxLsysSpNATsrcnopatadLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadLsysName.setStatus("current")


class _JnxLsysSpNATsrcnopatadProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcnopatadProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATsrcnopatadProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcnopatadProfileName_Object = MibTableColumn
jnxLsysSpNATsrcnopatadProfileName = _JnxLsysSpNATsrcnopatadProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 2),
    _JnxLsysSpNATsrcnopatadProfileName_Type()
)
jnxLsysSpNATsrcnopatadProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadProfileName.setStatus("current")
_JnxLsysSpNATsrcnopatadUsage_Type = Unsigned32
_JnxLsysSpNATsrcnopatadUsage_Object = MibTableColumn
jnxLsysSpNATsrcnopatadUsage = _JnxLsysSpNATsrcnopatadUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 3),
    _JnxLsysSpNATsrcnopatadUsage_Type()
)
jnxLsysSpNATsrcnopatadUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadUsage.setStatus("current")
_JnxLsysSpNATsrcnopatadReserved_Type = Unsigned32
_JnxLsysSpNATsrcnopatadReserved_Object = MibTableColumn
jnxLsysSpNATsrcnopatadReserved = _JnxLsysSpNATsrcnopatadReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 4),
    _JnxLsysSpNATsrcnopatadReserved_Type()
)
jnxLsysSpNATsrcnopatadReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadReserved.setStatus("current")
_JnxLsysSpNATsrcnopatadMaximum_Type = Unsigned32
_JnxLsysSpNATsrcnopatadMaximum_Object = MibTableColumn
jnxLsysSpNATsrcnopatadMaximum = _JnxLsysSpNATsrcnopatadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 5),
    _JnxLsysSpNATsrcnopatadMaximum_Type()
)
jnxLsysSpNATsrcnopatadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadMaximum.setStatus("current")
_JnxLsysSpNATsrcnopatadSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcnopatadSummary = _JnxLsysSpNATsrcnopatadSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2)
)
_JnxLsysSpNATsrcnopatadUsedAmount_Type = Unsigned32
_JnxLsysSpNATsrcnopatadUsedAmount_Object = MibScalar
jnxLsysSpNATsrcnopatadUsedAmount = _JnxLsysSpNATsrcnopatadUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 1),
    _JnxLsysSpNATsrcnopatadUsedAmount_Type()
)
jnxLsysSpNATsrcnopatadUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadUsedAmount.setStatus("current")
_JnxLsysSpNATsrcnopatadMaxQuota_Type = Unsigned32
_JnxLsysSpNATsrcnopatadMaxQuota_Object = MibScalar
jnxLsysSpNATsrcnopatadMaxQuota = _JnxLsysSpNATsrcnopatadMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 2),
    _JnxLsysSpNATsrcnopatadMaxQuota_Type()
)
jnxLsysSpNATsrcnopatadMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadMaxQuota.setStatus("current")
_JnxLsysSpNATsrcnopatadAvailableAmount_Type = Unsigned32
_JnxLsysSpNATsrcnopatadAvailableAmount_Object = MibScalar
jnxLsysSpNATsrcnopatadAvailableAmount = _JnxLsysSpNATsrcnopatadAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 3),
    _JnxLsysSpNATsrcnopatadAvailableAmount_Type()
)
jnxLsysSpNATsrcnopatadAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadAvailableAmount.setStatus("current")
_JnxLsysSpNATsrcnopatadHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATsrcnopatadHeaviestUsage_Object = MibScalar
jnxLsysSpNATsrcnopatadHeaviestUsage = _JnxLsysSpNATsrcnopatadHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 4),
    _JnxLsysSpNATsrcnopatadHeaviestUsage_Type()
)
jnxLsysSpNATsrcnopatadHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadHeaviestUsage.setStatus("current")


class _JnxLsysSpNATsrcnopatadHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcnopatadHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcnopatadHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcnopatadHeaviestUser_Object = MibScalar
jnxLsysSpNATsrcnopatadHeaviestUser = _JnxLsysSpNATsrcnopatadHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 5),
    _JnxLsysSpNATsrcnopatadHeaviestUser_Type()
)
jnxLsysSpNATsrcnopatadHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadHeaviestUser.setStatus("current")
_JnxLsysSpNATsrcnopatadLightestUsage_Type = Unsigned32
_JnxLsysSpNATsrcnopatadLightestUsage_Object = MibScalar
jnxLsysSpNATsrcnopatadLightestUsage = _JnxLsysSpNATsrcnopatadLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 6),
    _JnxLsysSpNATsrcnopatadLightestUsage_Type()
)
jnxLsysSpNATsrcnopatadLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadLightestUsage.setStatus("current")


class _JnxLsysSpNATsrcnopatadLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATsrcnopatadLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATsrcnopatadLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATsrcnopatadLightestUser_Object = MibScalar
jnxLsysSpNATsrcnopatadLightestUser = _JnxLsysSpNATsrcnopatadLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 7),
    _JnxLsysSpNATsrcnopatadLightestUser_Type()
)
jnxLsysSpNATsrcnopatadLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATsrcnopatadLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATSRCNOPATAD-MIB",
    **{"jnxLsysSpNATsrcnopatadMIB": jnxLsysSpNATsrcnopatadMIB,
       "jnxLsysSpNATsrcnopatadObjects": jnxLsysSpNATsrcnopatadObjects,
       "jnxLsysSpNATsrcnopatadTable": jnxLsysSpNATsrcnopatadTable,
       "jnxLsysSpNATsrcnopatadEntry": jnxLsysSpNATsrcnopatadEntry,
       "jnxLsysSpNATsrcnopatadLsysName": jnxLsysSpNATsrcnopatadLsysName,
       "jnxLsysSpNATsrcnopatadProfileName": jnxLsysSpNATsrcnopatadProfileName,
       "jnxLsysSpNATsrcnopatadUsage": jnxLsysSpNATsrcnopatadUsage,
       "jnxLsysSpNATsrcnopatadReserved": jnxLsysSpNATsrcnopatadReserved,
       "jnxLsysSpNATsrcnopatadMaximum": jnxLsysSpNATsrcnopatadMaximum,
       "jnxLsysSpNATsrcnopatadSummary": jnxLsysSpNATsrcnopatadSummary,
       "jnxLsysSpNATsrcnopatadUsedAmount": jnxLsysSpNATsrcnopatadUsedAmount,
       "jnxLsysSpNATsrcnopatadMaxQuota": jnxLsysSpNATsrcnopatadMaxQuota,
       "jnxLsysSpNATsrcnopatadAvailableAmount": jnxLsysSpNATsrcnopatadAvailableAmount,
       "jnxLsysSpNATsrcnopatadHeaviestUsage": jnxLsysSpNATsrcnopatadHeaviestUsage,
       "jnxLsysSpNATsrcnopatadHeaviestUser": jnxLsysSpNATsrcnopatadHeaviestUser,
       "jnxLsysSpNATsrcnopatadLightestUsage": jnxLsysSpNATsrcnopatadLightestUsage,
       "jnxLsysSpNATsrcnopatadLightestUser": jnxLsysSpNATsrcnopatadLightestUser}
)
