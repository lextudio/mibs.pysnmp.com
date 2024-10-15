# SNMP MIB module (RBN-MPLS-L3VPN-STD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-MPLS-L3VPN-STD-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:16 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(MplsL3VpnRouteDistinguisher,
 MplsL3VpnRtType,
 mplsL3VpnVrfName) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "MplsL3VpnRouteDistinguisher",
    "MplsL3VpnRtType",
    "mplsL3VpnVrfName")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rbnMplsL3VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51)
)
rbnMplsL3VpnMIB.setRevisions(
        ("2009-05-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnMplsL3VpnObjects_ObjectIdentity = ObjectIdentity
rbnMplsL3VpnObjects = _RbnMplsL3VpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1)
)
_RbnMplsL3VpnConf_ObjectIdentity = ObjectIdentity
rbnMplsL3VpnConf = _RbnMplsL3VpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1)
)
_RbnMplsL3VpnVrfRTTable_Object = MibTable
rbnMplsL3VpnVrfRTTable = _RbnMplsL3VpnVrfRTTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTTable.setStatus("current")
_RbnMplsL3VpnVrfRTEntry_Object = MibTableRow
rbnMplsL3VpnVrfRTEntry = _RbnMplsL3VpnVrfRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1)
)
rbnMplsL3VpnVrfRTEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTAddrFamily"),
    (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTType"),
    (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTIndex"),
)
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTEntry.setStatus("current")
_RbnMplsL3VpnVrfRTAddrFamily_Type = AddressFamilyNumbers
_RbnMplsL3VpnVrfRTAddrFamily_Object = MibTableColumn
rbnMplsL3VpnVrfRTAddrFamily = _RbnMplsL3VpnVrfRTAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 1),
    _RbnMplsL3VpnVrfRTAddrFamily_Type()
)
rbnMplsL3VpnVrfRTAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTAddrFamily.setStatus("current")
_RbnMplsL3VpnVrfRTType_Type = MplsL3VpnRtType
_RbnMplsL3VpnVrfRTType_Object = MibTableColumn
rbnMplsL3VpnVrfRTType = _RbnMplsL3VpnVrfRTType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 2),
    _RbnMplsL3VpnVrfRTType_Type()
)
rbnMplsL3VpnVrfRTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTType.setStatus("current")


class _RbnMplsL3VpnVrfRTIndex_Type(Unsigned32):
    """Custom type rbnMplsL3VpnVrfRTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnMplsL3VpnVrfRTIndex_Type.__name__ = "Unsigned32"
_RbnMplsL3VpnVrfRTIndex_Object = MibTableColumn
rbnMplsL3VpnVrfRTIndex = _RbnMplsL3VpnVrfRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 3),
    _RbnMplsL3VpnVrfRTIndex_Type()
)
rbnMplsL3VpnVrfRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTIndex.setStatus("current")
_RbnMplsL3VpnVrfRT_Type = MplsL3VpnRouteDistinguisher
_RbnMplsL3VpnVrfRT_Object = MibTableColumn
rbnMplsL3VpnVrfRT = _RbnMplsL3VpnVrfRT_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 4),
    _RbnMplsL3VpnVrfRT_Type()
)
rbnMplsL3VpnVrfRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRT.setStatus("current")
_RbnMplsL3VpnVrfRTDescr_Type = SnmpAdminString
_RbnMplsL3VpnVrfRTDescr_Object = MibTableColumn
rbnMplsL3VpnVrfRTDescr = _RbnMplsL3VpnVrfRTDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 5),
    _RbnMplsL3VpnVrfRTDescr_Type()
)
rbnMplsL3VpnVrfRTDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL3VpnVrfRTDescr.setStatus("current")
_RbnMplsL3VpnConformance_ObjectIdentity = ObjectIdentity
rbnMplsL3VpnConformance = _RbnMplsL3VpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 2)
)
_RbnMplsL3VpnGroups_ObjectIdentity = ObjectIdentity
rbnMplsL3VpnGroups = _RbnMplsL3VpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 1)
)
_RbnMplsL3VpnCompliances_ObjectIdentity = ObjectIdentity
rbnMplsL3VpnCompliances = _RbnMplsL3VpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 2)
)

# Managed Objects groups

rbnMplsL3VpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 1, 1)
)
rbnMplsL3VpnGroup.setObjects(
      *(("RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRT"),
        ("RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTDescr"))
)
if mibBuilder.loadTexts:
    rbnMplsL3VpnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnMplsL3VpnModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnMplsL3VpnModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-MPLS-L3VPN-STD-EXT-MIB",
    **{"rbnMplsL3VpnMIB": rbnMplsL3VpnMIB,
       "rbnMplsL3VpnObjects": rbnMplsL3VpnObjects,
       "rbnMplsL3VpnConf": rbnMplsL3VpnConf,
       "rbnMplsL3VpnVrfRTTable": rbnMplsL3VpnVrfRTTable,
       "rbnMplsL3VpnVrfRTEntry": rbnMplsL3VpnVrfRTEntry,
       "rbnMplsL3VpnVrfRTAddrFamily": rbnMplsL3VpnVrfRTAddrFamily,
       "rbnMplsL3VpnVrfRTType": rbnMplsL3VpnVrfRTType,
       "rbnMplsL3VpnVrfRTIndex": rbnMplsL3VpnVrfRTIndex,
       "rbnMplsL3VpnVrfRT": rbnMplsL3VpnVrfRT,
       "rbnMplsL3VpnVrfRTDescr": rbnMplsL3VpnVrfRTDescr,
       "rbnMplsL3VpnConformance": rbnMplsL3VpnConformance,
       "rbnMplsL3VpnGroups": rbnMplsL3VpnGroups,
       "rbnMplsL3VpnGroup": rbnMplsL3VpnGroup,
       "rbnMplsL3VpnCompliances": rbnMplsL3VpnCompliances,
       "rbnMplsL3VpnModuleCompliance": rbnMplsL3VpnModuleCompliance}
)
