# SNMP MIB module (BW-BroadworksResourceAccess) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksResourceAccess
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:04 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_ResourceAccess_ObjectIdentity = ObjectIdentity
resourceAccess = _ResourceAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13)
)
_Operations_ObjectIdentity = ObjectIdentity
operations = _Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1)
)
_BwFileGets_Type = Counter32
_BwFileGets_Object = MibScalar
bwFileGets = _BwFileGets_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 1),
    _BwFileGets_Type()
)
bwFileGets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwFileGets.setStatus("current")
_BwFileDeletes_Type = Counter32
_BwFileDeletes_Object = MibScalar
bwFileDeletes = _BwFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 2),
    _BwFileDeletes_Type()
)
bwFileDeletes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwFileDeletes.setStatus("current")
_BwFilePuts_Type = Counter32
_BwFilePuts_Object = MibScalar
bwFilePuts = _BwFilePuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 3),
    _BwFilePuts_Type()
)
bwFilePuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwFilePuts.setStatus("current")
_BwResourceAccessMibConformance_ObjectIdentity = ObjectIdentity
bwResourceAccessMibConformance = _BwResourceAccessMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000)
)
_BwResourceAccessMibGroups_ObjectIdentity = ObjectIdentity
bwResourceAccessMibGroups = _BwResourceAccessMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1)
)
_BwResourceAccessMibCompliancy_ObjectIdentity = ObjectIdentity
bwResourceAccessMibCompliancy = _BwResourceAccessMibCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2)
)

# Managed Objects groups

bwResourceAccessOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1, 1)
)
bwResourceAccessOperationsGroup.setObjects(
      *(("BW-BroadworksResourceAccess", "bwFileGets"),
        ("BW-BroadworksResourceAccess", "bwFileDeletes"),
        ("BW-BroadworksResourceAccess", "bwFilePuts"))
)
if mibBuilder.loadTexts:
    bwResourceAccessOperationsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwResourceAccessBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2, 1)
)
if mibBuilder.loadTexts:
    bwResourceAccessBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksResourceAccess",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "resourceAccess": resourceAccess,
       "operations": operations,
       "bwFileGets": bwFileGets,
       "bwFileDeletes": bwFileDeletes,
       "bwFilePuts": bwFilePuts,
       "bwResourceAccessMibConformance": bwResourceAccessMibConformance,
       "bwResourceAccessMibGroups": bwResourceAccessMibGroups,
       "bwResourceAccessOperationsGroup": bwResourceAccessOperationsGroup,
       "bwResourceAccessMibCompliancy": bwResourceAccessMibCompliancy,
       "bwResourceAccessBasicCompliance": bwResourceAccessBasicCompliance}
)
