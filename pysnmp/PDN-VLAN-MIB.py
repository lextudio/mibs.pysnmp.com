# SNMP MIB module (PDN-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:15 2024
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

pdnVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46)
)
pdnVlanMIB.setRevisions(
        ("2003-11-12 00:00",
         "2003-04-24 00:00",
         "2003-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnVlanNotifications_ObjectIdentity = ObjectIdentity
pdnVlanNotifications = _PdnVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 0)
)
_PdnVlanObjects_ObjectIdentity = ObjectIdentity
pdnVlanObjects = _PdnVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1)
)
_PdnVlanReservedBlockStart_Type = VlanIndex
_PdnVlanReservedBlockStart_Object = MibScalar
pdnVlanReservedBlockStart = _PdnVlanReservedBlockStart_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 1),
    _PdnVlanReservedBlockStart_Type()
)
pdnVlanReservedBlockStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnVlanReservedBlockStart.setStatus("current")
_PdnVlanInbandMgmtVlanId_Type = VlanIndex
_PdnVlanInbandMgmtVlanId_Object = MibScalar
pdnVlanInbandMgmtVlanId = _PdnVlanInbandMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 2),
    _PdnVlanInbandMgmtVlanId_Type()
)
pdnVlanInbandMgmtVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnVlanInbandMgmtVlanId.setStatus("current")
_PdnVlanInbandMgmtVlanId2_Type = VlanIndex
_PdnVlanInbandMgmtVlanId2_Object = MibScalar
pdnVlanInbandMgmtVlanId2 = _PdnVlanInbandMgmtVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 3),
    _PdnVlanInbandMgmtVlanId2_Type()
)
pdnVlanInbandMgmtVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnVlanInbandMgmtVlanId2.setStatus("current")
_PdnVlanAFNs_ObjectIdentity = ObjectIdentity
pdnVlanAFNs = _PdnVlanAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 2)
)
_PdnVlanConformance_ObjectIdentity = ObjectIdentity
pdnVlanConformance = _PdnVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3)
)
_PdnVlanCompliances_ObjectIdentity = ObjectIdentity
pdnVlanCompliances = _PdnVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1)
)
_PdnVlanGroups_ObjectIdentity = ObjectIdentity
pdnVlanGroups = _PdnVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2)
)
_PdnVlanObjGroups_ObjectIdentity = ObjectIdentity
pdnVlanObjGroups = _PdnVlanObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1)
)
_PdnVlanAfnGroups_ObjectIdentity = ObjectIdentity
pdnVlanAfnGroups = _PdnVlanAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 2)
)
_PdnVlanNtfyGroups_ObjectIdentity = ObjectIdentity
pdnVlanNtfyGroups = _PdnVlanNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 3)
)

# Managed Objects groups

pdnVlanReservedBlockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 1)
)
pdnVlanReservedBlockGroup.setObjects(
    ("PDN-VLAN-MIB", "pdnVlanReservedBlockStart")
)
if mibBuilder.loadTexts:
    pdnVlanReservedBlockGroup.setStatus("current")

pdnVlanInbandMgmtVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 2)
)
pdnVlanInbandMgmtVlanGroup.setObjects(
    ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId")
)
if mibBuilder.loadTexts:
    pdnVlanInbandMgmtVlanGroup.setStatus("current")

pdnVlanInbandMgmtVlan2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 3)
)
pdnVlanInbandMgmtVlan2Group.setObjects(
      *(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"),
        ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId2"))
)
if mibBuilder.loadTexts:
    pdnVlanInbandMgmtVlan2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-VLAN-MIB",
    **{"pdnVlanMIB": pdnVlanMIB,
       "pdnVlanNotifications": pdnVlanNotifications,
       "pdnVlanObjects": pdnVlanObjects,
       "pdnVlanReservedBlockStart": pdnVlanReservedBlockStart,
       "pdnVlanInbandMgmtVlanId": pdnVlanInbandMgmtVlanId,
       "pdnVlanInbandMgmtVlanId2": pdnVlanInbandMgmtVlanId2,
       "pdnVlanAFNs": pdnVlanAFNs,
       "pdnVlanConformance": pdnVlanConformance,
       "pdnVlanCompliances": pdnVlanCompliances,
       "pdnVlanMIBCompliance": pdnVlanMIBCompliance,
       "pdnVlanGroups": pdnVlanGroups,
       "pdnVlanObjGroups": pdnVlanObjGroups,
       "pdnVlanReservedBlockGroup": pdnVlanReservedBlockGroup,
       "pdnVlanInbandMgmtVlanGroup": pdnVlanInbandMgmtVlanGroup,
       "pdnVlanInbandMgmtVlan2Group": pdnVlanInbandMgmtVlan2Group,
       "pdnVlanAfnGroups": pdnVlanAfnGroups,
       "pdnVlanNtfyGroups": pdnVlanNtfyGroups}
)
