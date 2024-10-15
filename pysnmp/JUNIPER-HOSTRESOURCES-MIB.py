# SNMP MIB module (JUNIPER-HOSTRESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-HOSTRESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:04 2024
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

(hrStorageEntry,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrStorageEntry")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxHostResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31)
)
jnxHostResourcesMIB.setRevisions(
        ("2004-08-18 00:00",
         "2004-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxHrStorage_ObjectIdentity = ObjectIdentity
jnxHrStorage = _JnxHrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1)
)
_JnxHrStorageTable_Object = MibTable
jnxHrStorageTable = _JnxHrStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1)
)
if mibBuilder.loadTexts:
    jnxHrStorageTable.setStatus("current")
_JnxHrStorageEntry_Object = MibTableRow
jnxHrStorageEntry = _JnxHrStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxHrStorageEntry.setStatus("current")
_JnxHrStoragePercentUsed_Type = Gauge32
_JnxHrStoragePercentUsed_Object = MibTableColumn
jnxHrStoragePercentUsed = _JnxHrStoragePercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1),
    _JnxHrStoragePercentUsed_Type()
)
jnxHrStoragePercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxHrStoragePercentUsed.setStatus("current")
hrStorageEntry.registerAugmentions(
    ("JUNIPER-HOSTRESOURCES-MIB",
     "jnxHrStorageEntry")
)
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-HOSTRESOURCES-MIB",
    **{"jnxHostResourcesMIB": jnxHostResourcesMIB,
       "jnxHrStorage": jnxHrStorage,
       "jnxHrStorageTable": jnxHrStorageTable,
       "jnxHrStorageEntry": jnxHrStorageEntry,
       "jnxHrStoragePercentUsed": jnxHrStoragePercentUsed}
)
