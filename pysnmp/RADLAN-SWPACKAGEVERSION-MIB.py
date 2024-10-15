# SNMP MIB module (RADLAN-SWPACKAGEVERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SWPACKAGEVERSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:35 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlSwPackageVersion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 67)
)
rlSwPackageVersion.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSwPackageVersionTable_Object = MibTable
rlSwPackageVersionTable = _RlSwPackageVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1)
)
if mibBuilder.loadTexts:
    rlSwPackageVersionTable.setStatus("current")
_RlSwPackageVersionEntry_Object = MibTableRow
rlSwPackageVersionEntry = _RlSwPackageVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1)
)
rlSwPackageVersionEntry.setIndexNames(
    (1, "RADLAN-SWPACKAGEVERSION-MIB", "rlSwPackageVersionName"),
)
if mibBuilder.loadTexts:
    rlSwPackageVersionEntry.setStatus("current")


class _RlSwPackageVersionName_Type(DisplayString):
    """Custom type rlSwPackageVersionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlSwPackageVersionName_Type.__name__ = "DisplayString"
_RlSwPackageVersionName_Object = MibTableColumn
rlSwPackageVersionName = _RlSwPackageVersionName_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 1),
    _RlSwPackageVersionName_Type()
)
rlSwPackageVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSwPackageVersionName.setStatus("current")


class _RlSwPackageVersionVesrion_Type(DisplayString):
    """Custom type rlSwPackageVersionVesrion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlSwPackageVersionVesrion_Type.__name__ = "DisplayString"
_RlSwPackageVersionVesrion_Object = MibTableColumn
rlSwPackageVersionVesrion = _RlSwPackageVersionVesrion_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 2),
    _RlSwPackageVersionVesrion_Type()
)
rlSwPackageVersionVesrion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSwPackageVersionVesrion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SWPACKAGEVERSION-MIB",
    **{"rlSwPackageVersion": rlSwPackageVersion,
       "rlSwPackageVersionTable": rlSwPackageVersionTable,
       "rlSwPackageVersionEntry": rlSwPackageVersionEntry,
       "rlSwPackageVersionName": rlSwPackageVersionName,
       "rlSwPackageVersionVesrion": rlSwPackageVersionVesrion}
)
