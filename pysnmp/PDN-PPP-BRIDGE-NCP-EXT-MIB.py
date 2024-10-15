# SNMP MIB module (PDN-PPP-BRIDGE-NCP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-PPP-BRIDGE-NCP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:00 2024
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

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(PdnPPPState,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "PdnPPPState",
    "SwitchState")

(pppBridgeEntry,
 pppBridgeMediaConfigEntry) = mibBuilder.importSymbols(
    "PPP-BRIDGE-NCP-MIB",
    "pppBridgeEntry",
    "pppBridgeMediaConfigEntry")

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

pdnPppBridgeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29)
)
pdnPppBridgeExtMIB.setRevisions(
        ("2004-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnPppBridgeExtNotifications_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtNotifications = _PdnPppBridgeExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 0)
)
_PdnPppBridgeExtObjects_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtObjects = _PdnPppBridgeExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1)
)
_PdnPppBridgeExtTable_Object = MibTable
pdnPppBridgeExtTable = _PdnPppBridgeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppBridgeExtTable.setStatus("current")
_PdnPppBridgeExtEntry_Object = MibTableRow
pdnPppBridgeExtEntry = _PdnPppBridgeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppBridgeExtEntry.setStatus("current")
_PdnPppBridgeBcpLinkStatusCurrState_Type = PdnPPPState
_PdnPppBridgeBcpLinkStatusCurrState_Object = MibTableColumn
pdnPppBridgeBcpLinkStatusCurrState = _PdnPppBridgeBcpLinkStatusCurrState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 1, 1, 1),
    _PdnPppBridgeBcpLinkStatusCurrState_Type()
)
pdnPppBridgeBcpLinkStatusCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppBridgeBcpLinkStatusCurrState.setStatus("current")
_PdnPppBridgeLocalToRemote802Tagged_Type = SwitchState
_PdnPppBridgeLocalToRemote802Tagged_Object = MibTableColumn
pdnPppBridgeLocalToRemote802Tagged = _PdnPppBridgeLocalToRemote802Tagged_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 1, 1, 2),
    _PdnPppBridgeLocalToRemote802Tagged_Type()
)
pdnPppBridgeLocalToRemote802Tagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppBridgeLocalToRemote802Tagged.setStatus("current")
_PdnPppBridgeRemoteToLocal802Tagged_Type = SwitchState
_PdnPppBridgeRemoteToLocal802Tagged_Object = MibTableColumn
pdnPppBridgeRemoteToLocal802Tagged = _PdnPppBridgeRemoteToLocal802Tagged_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 1, 1, 3),
    _PdnPppBridgeRemoteToLocal802Tagged_Type()
)
pdnPppBridgeRemoteToLocal802Tagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppBridgeRemoteToLocal802Tagged.setStatus("current")
_PdnPppBridgeMediaConfigExtTable_Object = MibTable
pdnPppBridgeMediaConfigExtTable = _PdnPppBridgeMediaConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 2)
)
if mibBuilder.loadTexts:
    pdnPppBridgeMediaConfigExtTable.setStatus("current")
_PdnPppBridgeMediaConfigExtEntry_Object = MibTableRow
pdnPppBridgeMediaConfigExtEntry = _PdnPppBridgeMediaConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnPppBridgeMediaConfigExtEntry.setStatus("current")
_PdnPppBridgeMediaIeee802Tagged_Type = SwitchState
_PdnPppBridgeMediaIeee802Tagged_Object = MibTableColumn
pdnPppBridgeMediaIeee802Tagged = _PdnPppBridgeMediaIeee802Tagged_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 1, 2, 1, 1),
    _PdnPppBridgeMediaIeee802Tagged_Type()
)
pdnPppBridgeMediaIeee802Tagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppBridgeMediaIeee802Tagged.setStatus("current")
_PdnPppBridgeExtAFNs_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtAFNs = _PdnPppBridgeExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 2)
)
_PdnPppBridgeExtConformance_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtConformance = _PdnPppBridgeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3)
)
_PdnPppBridgeExtCompliances_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtCompliances = _PdnPppBridgeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 1)
)
_PdnPppBridgeExtGroups_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtGroups = _PdnPppBridgeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2)
)
_PdnPppBridgeExtObjGroups_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtObjGroups = _PdnPppBridgeExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2, 1)
)
_PdnPppBridgeExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtAfnGroups = _PdnPppBridgeExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2, 2)
)
_PdnPppBridgeExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnPppBridgeExtNtfyGroups = _PdnPppBridgeExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2, 3)
)
pppBridgeEntry.registerAugmentions(
    ("PDN-PPP-BRIDGE-NCP-EXT-MIB",
     "pdnPppBridgeExtEntry")
)
pdnPppBridgeExtEntry.setIndexNames(*pppBridgeEntry.getIndexNames())
pppBridgeMediaConfigEntry.registerAugmentions(
    ("PDN-PPP-BRIDGE-NCP-EXT-MIB",
     "pdnPppBridgeMediaConfigExtEntry")
)
pdnPppBridgeMediaConfigExtEntry.setIndexNames(*pppBridgeMediaConfigEntry.getIndexNames())

# Managed Objects groups

pdnPppBridgeExtStateMachineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2, 1, 1)
)
pdnPppBridgeExtStateMachineGroup.setObjects(
    ("PDN-PPP-BRIDGE-NCP-EXT-MIB", "pdnPppBridgeBcpLinkStatusCurrState")
)
if mibBuilder.loadTexts:
    pdnPppBridgeExtStateMachineGroup.setStatus("current")

pdnPppBridgeExt802TaggedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 2, 1, 2)
)
pdnPppBridgeExt802TaggedGroup.setObjects(
      *(("PDN-PPP-BRIDGE-NCP-EXT-MIB", "pdnPppBridgeMediaIeee802Tagged"),
        ("PDN-PPP-BRIDGE-NCP-EXT-MIB", "pdnPppBridgeLocalToRemote802Tagged"),
        ("PDN-PPP-BRIDGE-NCP-EXT-MIB", "pdnPppBridgeRemoteToLocal802Tagged"))
)
if mibBuilder.loadTexts:
    pdnPppBridgeExt802TaggedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnPppBridgeExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 29, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppBridgeExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-PPP-BRIDGE-NCP-EXT-MIB",
    **{"pdnPppBridgeExtMIB": pdnPppBridgeExtMIB,
       "pdnPppBridgeExtNotifications": pdnPppBridgeExtNotifications,
       "pdnPppBridgeExtObjects": pdnPppBridgeExtObjects,
       "pdnPppBridgeExtTable": pdnPppBridgeExtTable,
       "pdnPppBridgeExtEntry": pdnPppBridgeExtEntry,
       "pdnPppBridgeBcpLinkStatusCurrState": pdnPppBridgeBcpLinkStatusCurrState,
       "pdnPppBridgeLocalToRemote802Tagged": pdnPppBridgeLocalToRemote802Tagged,
       "pdnPppBridgeRemoteToLocal802Tagged": pdnPppBridgeRemoteToLocal802Tagged,
       "pdnPppBridgeMediaConfigExtTable": pdnPppBridgeMediaConfigExtTable,
       "pdnPppBridgeMediaConfigExtEntry": pdnPppBridgeMediaConfigExtEntry,
       "pdnPppBridgeMediaIeee802Tagged": pdnPppBridgeMediaIeee802Tagged,
       "pdnPppBridgeExtAFNs": pdnPppBridgeExtAFNs,
       "pdnPppBridgeExtConformance": pdnPppBridgeExtConformance,
       "pdnPppBridgeExtCompliances": pdnPppBridgeExtCompliances,
       "pdnPppBridgeExtCompliance": pdnPppBridgeExtCompliance,
       "pdnPppBridgeExtGroups": pdnPppBridgeExtGroups,
       "pdnPppBridgeExtObjGroups": pdnPppBridgeExtObjGroups,
       "pdnPppBridgeExtStateMachineGroup": pdnPppBridgeExtStateMachineGroup,
       "pdnPppBridgeExt802TaggedGroup": pdnPppBridgeExt802TaggedGroup,
       "pdnPppBridgeExtAfnGroups": pdnPppBridgeExtAfnGroups,
       "pdnPppBridgeExtNtfyGroups": pdnPppBridgeExtNtfyGroups}
)
