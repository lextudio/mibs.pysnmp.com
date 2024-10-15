# SNMP MIB module (IPFIX-SELECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFIX-SELECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:51 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipfixSelectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 194)
)
ipfixSelectorMIB.setRevisions(
        ("2012-06-11 00:00",
         "2010-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpfixSelectorObjects_ObjectIdentity = ObjectIdentity
ipfixSelectorObjects = _IpfixSelectorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1)
)
_IpfixSelectorFunctions_ObjectIdentity = ObjectIdentity
ipfixSelectorFunctions = _IpfixSelectorFunctions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1)
)
_IpfixFuncSelectAll_ObjectIdentity = ObjectIdentity
ipfixFuncSelectAll = _IpfixFuncSelectAll_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 1)
)
_IpfixFuncSelectAllAvail_Type = TruthValue
_IpfixFuncSelectAllAvail_Object = MibScalar
ipfixFuncSelectAllAvail = _IpfixFuncSelectAllAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 1, 1),
    _IpfixFuncSelectAllAvail_Type()
)
ipfixFuncSelectAllAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixFuncSelectAllAvail.setStatus("current")
_IpfixSelectorConformance_ObjectIdentity = ObjectIdentity
ipfixSelectorConformance = _IpfixSelectorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2)
)
_IpfixSelectorCompliances_ObjectIdentity = ObjectIdentity
ipfixSelectorCompliances = _IpfixSelectorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2, 1)
)
_IpfixSelectorGroups_ObjectIdentity = ObjectIdentity
ipfixSelectorGroups = _IpfixSelectorGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2, 2)
)

# Managed Objects groups

ipfixSelectorBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 194, 2, 2, 1)
)
ipfixSelectorBasicGroup.setObjects(
    ("IPFIX-SELECTOR-MIB", "ipfixFuncSelectAllAvail")
)
if mibBuilder.loadTexts:
    ipfixSelectorBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipfixSelectorBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 194, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixSelectorBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-SELECTOR-MIB",
    **{"ipfixSelectorMIB": ipfixSelectorMIB,
       "ipfixSelectorObjects": ipfixSelectorObjects,
       "ipfixSelectorFunctions": ipfixSelectorFunctions,
       "ipfixFuncSelectAll": ipfixFuncSelectAll,
       "ipfixFuncSelectAllAvail": ipfixFuncSelectAllAvail,
       "ipfixSelectorConformance": ipfixSelectorConformance,
       "ipfixSelectorCompliances": ipfixSelectorCompliances,
       "ipfixSelectorBasicCompliance": ipfixSelectorBasicCompliance,
       "ipfixSelectorGroups": ipfixSelectorGroups,
       "ipfixSelectorBasicGroup": ipfixSelectorBasicGroup}
)
