# SNMP MIB module (JUNIPER-LSYSSP-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYSSP-CPU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:29 2024
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

(jnxLsysSpCPU,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpCPU")

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

jnxLsysSpCPUMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpCPUObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpCPUObjects = _JnxLsysSpCPUObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1)
)
_JnxLsysSpCPUTable_Object = MibTable
jnxLsysSpCPUTable = _JnxLsysSpCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpCPUTable.setStatus("current")
_JnxLsysSpCPUEntry_Object = MibTableRow
jnxLsysSpCPUEntry = _JnxLsysSpCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1)
)
jnxLsysSpCPUEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-CPU-MIB", "jnxLsysSpCPULsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpCPUEntry.setStatus("current")


class _JnxLsysSpCPULsysName_Type(DisplayString):
    """Custom type jnxLsysSpCPULsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpCPULsysName_Type.__name__ = "DisplayString"
_JnxLsysSpCPULsysName_Object = MibTableColumn
jnxLsysSpCPULsysName = _JnxLsysSpCPULsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 1),
    _JnxLsysSpCPULsysName_Type()
)
jnxLsysSpCPULsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpCPULsysName.setStatus("current")


class _JnxLsysSpCPUProfileName_Type(DisplayString):
    """Custom type jnxLsysSpCPUProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpCPUProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpCPUProfileName_Object = MibTableColumn
jnxLsysSpCPUProfileName = _JnxLsysSpCPUProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 2),
    _JnxLsysSpCPUProfileName_Type()
)
jnxLsysSpCPUProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPUProfileName.setStatus("current")
_JnxLsysSpCPUsage_Type = Unsigned32
_JnxLsysSpCPUsage_Object = MibTableColumn
jnxLsysSpCPUsage = _JnxLsysSpCPUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 3),
    _JnxLsysSpCPUsage_Type()
)
jnxLsysSpCPUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPUsage.setUnits("0.01 percent")
_JnxLsysSpSPUUsage_Type = Unsigned32
_JnxLsysSpSPUUsage_Object = MibTableColumn
jnxLsysSpSPUUsage = _JnxLsysSpSPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 4),
    _JnxLsysSpSPUUsage_Type()
)
jnxLsysSpSPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPUUsage.setUnits("0.01 percent")
_JnxLsysSpCPUReserved_Type = Unsigned32
_JnxLsysSpCPUReserved_Object = MibTableColumn
jnxLsysSpCPUReserved = _JnxLsysSpCPUReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 5),
    _JnxLsysSpCPUReserved_Type()
)
jnxLsysSpCPUReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPUReserved.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPUReserved.setUnits("0.01 percent")
_JnxLsysSpCPUMaximum_Type = Unsigned32
_JnxLsysSpCPUMaximum_Object = MibTableColumn
jnxLsysSpCPUMaximum = _JnxLsysSpCPUMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 1, 1, 1, 6),
    _JnxLsysSpCPUMaximum_Type()
)
jnxLsysSpCPUMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPUMaximum.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPUMaximum.setUnits("0.01 percent")
_JnxLsysSpCPUSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpCPUSummary = _JnxLsysSpCPUSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2)
)
_JnxLsysSpCPSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpCPSummary = _JnxLsysSpCPSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1)
)
_JnxLsysSpCPUsedAmount_Type = Unsigned32
_JnxLsysSpCPUsedAmount_Object = MibScalar
jnxLsysSpCPUsedAmount = _JnxLsysSpCPUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 1),
    _JnxLsysSpCPUsedAmount_Type()
)
jnxLsysSpCPUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPUsedAmount.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPUsedAmount.setUnits("0.01 percent")
_JnxLsysSpCPMaxQuota_Type = Unsigned32
_JnxLsysSpCPMaxQuota_Object = MibScalar
jnxLsysSpCPMaxQuota = _JnxLsysSpCPMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 2),
    _JnxLsysSpCPMaxQuota_Type()
)
jnxLsysSpCPMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPMaxQuota.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPMaxQuota.setUnits("0.01 percent")
_JnxLsysSpCPAvailableAmount_Type = Unsigned32
_JnxLsysSpCPAvailableAmount_Object = MibScalar
jnxLsysSpCPAvailableAmount = _JnxLsysSpCPAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 3),
    _JnxLsysSpCPAvailableAmount_Type()
)
jnxLsysSpCPAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPAvailableAmount.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPAvailableAmount.setUnits("0.01 percent")
_JnxLsysSpCPHeaviestUsage_Type = Unsigned32
_JnxLsysSpCPHeaviestUsage_Object = MibScalar
jnxLsysSpCPHeaviestUsage = _JnxLsysSpCPHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 4),
    _JnxLsysSpCPHeaviestUsage_Type()
)
jnxLsysSpCPHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPHeaviestUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPHeaviestUsage.setUnits("0.01 percent")


class _JnxLsysSpCPHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpCPHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpCPHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpCPHeaviestUser_Object = MibScalar
jnxLsysSpCPHeaviestUser = _JnxLsysSpCPHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 5),
    _JnxLsysSpCPHeaviestUser_Type()
)
jnxLsysSpCPHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPHeaviestUser.setStatus("current")
_JnxLsysSpCPLightestUsage_Type = Unsigned32
_JnxLsysSpCPLightestUsage_Object = MibScalar
jnxLsysSpCPLightestUsage = _JnxLsysSpCPLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 6),
    _JnxLsysSpCPLightestUsage_Type()
)
jnxLsysSpCPLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPLightestUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpCPLightestUsage.setUnits("0.01 percent")


class _JnxLsysSpCPLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpCPLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpCPLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpCPLightestUser_Object = MibScalar
jnxLsysSpCPLightestUser = _JnxLsysSpCPLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 1, 7),
    _JnxLsysSpCPLightestUser_Type()
)
jnxLsysSpCPLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpCPLightestUser.setStatus("current")
_JnxLsysSpSPUSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpSPUSummary = _JnxLsysSpSPUSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2)
)
_JnxLsysSpSPUUsedAmount_Type = Unsigned32
_JnxLsysSpSPUUsedAmount_Object = MibScalar
jnxLsysSpSPUUsedAmount = _JnxLsysSpSPUUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 1),
    _JnxLsysSpSPUUsedAmount_Type()
)
jnxLsysSpSPUUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUUsedAmount.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPUUsedAmount.setUnits("0.01 percent")
_JnxLsysSpSPUMaxQuota_Type = Unsigned32
_JnxLsysSpSPUMaxQuota_Object = MibScalar
jnxLsysSpSPUMaxQuota = _JnxLsysSpSPUMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 2),
    _JnxLsysSpSPUMaxQuota_Type()
)
jnxLsysSpSPUMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUMaxQuota.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPUMaxQuota.setUnits("0.01 percent")
_JnxLsysSpSPUAvailableAmount_Type = Unsigned32
_JnxLsysSpSPUAvailableAmount_Object = MibScalar
jnxLsysSpSPUAvailableAmount = _JnxLsysSpSPUAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 3),
    _JnxLsysSpSPUAvailableAmount_Type()
)
jnxLsysSpSPUAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUAvailableAmount.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPUAvailableAmount.setUnits("0.01 percent")
_JnxLsysSpSPUHeaviestUsage_Type = Unsigned32
_JnxLsysSpSPUHeaviestUsage_Object = MibScalar
jnxLsysSpSPUHeaviestUsage = _JnxLsysSpSPUHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 4),
    _JnxLsysSpSPUHeaviestUsage_Type()
)
jnxLsysSpSPUHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUHeaviestUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPUHeaviestUsage.setUnits("0.01 percent")


class _JnxLsysSpSPUHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpSPUHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSPUHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSPUHeaviestUser_Object = MibScalar
jnxLsysSpSPUHeaviestUser = _JnxLsysSpSPUHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 5),
    _JnxLsysSpSPUHeaviestUser_Type()
)
jnxLsysSpSPUHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPUHeaviestUser.setStatus("current")
_JnxLsysSpSPULightestUsage_Type = Unsigned32
_JnxLsysSpSPULightestUsage_Object = MibScalar
jnxLsysSpSPULightestUsage = _JnxLsysSpSPULightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 6),
    _JnxLsysSpSPULightestUsage_Type()
)
jnxLsysSpSPULightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPULightestUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxLsysSpSPULightestUsage.setUnits("0.01 percent")


class _JnxLsysSpSPULightestUser_Type(DisplayString):
    """Custom type jnxLsysSpSPULightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSPULightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSPULightestUser_Object = MibScalar
jnxLsysSpSPULightestUser = _JnxLsysSpSPULightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18, 1, 2, 2, 7),
    _JnxLsysSpSPULightestUser_Type()
)
jnxLsysSpSPULightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSPULightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-CPU-MIB",
    **{"jnxLsysSpCPUMIB": jnxLsysSpCPUMIB,
       "jnxLsysSpCPUObjects": jnxLsysSpCPUObjects,
       "jnxLsysSpCPUTable": jnxLsysSpCPUTable,
       "jnxLsysSpCPUEntry": jnxLsysSpCPUEntry,
       "jnxLsysSpCPULsysName": jnxLsysSpCPULsysName,
       "jnxLsysSpCPUProfileName": jnxLsysSpCPUProfileName,
       "jnxLsysSpCPUsage": jnxLsysSpCPUsage,
       "jnxLsysSpSPUUsage": jnxLsysSpSPUUsage,
       "jnxLsysSpCPUReserved": jnxLsysSpCPUReserved,
       "jnxLsysSpCPUMaximum": jnxLsysSpCPUMaximum,
       "jnxLsysSpCPUSummary": jnxLsysSpCPUSummary,
       "jnxLsysSpCPSummary": jnxLsysSpCPSummary,
       "jnxLsysSpCPUsedAmount": jnxLsysSpCPUsedAmount,
       "jnxLsysSpCPMaxQuota": jnxLsysSpCPMaxQuota,
       "jnxLsysSpCPAvailableAmount": jnxLsysSpCPAvailableAmount,
       "jnxLsysSpCPHeaviestUsage": jnxLsysSpCPHeaviestUsage,
       "jnxLsysSpCPHeaviestUser": jnxLsysSpCPHeaviestUser,
       "jnxLsysSpCPLightestUsage": jnxLsysSpCPLightestUsage,
       "jnxLsysSpCPLightestUser": jnxLsysSpCPLightestUser,
       "jnxLsysSpSPUSummary": jnxLsysSpSPUSummary,
       "jnxLsysSpSPUUsedAmount": jnxLsysSpSPUUsedAmount,
       "jnxLsysSpSPUMaxQuota": jnxLsysSpSPUMaxQuota,
       "jnxLsysSpSPUAvailableAmount": jnxLsysSpSPUAvailableAmount,
       "jnxLsysSpSPUHeaviestUsage": jnxLsysSpSPUHeaviestUsage,
       "jnxLsysSpSPUHeaviestUser": jnxLsysSpSPUHeaviestUser,
       "jnxLsysSpSPULightestUsage": jnxLsysSpSPULightestUsage,
       "jnxLsysSpSPULightestUser": jnxLsysSpSPULightestUser}
)
