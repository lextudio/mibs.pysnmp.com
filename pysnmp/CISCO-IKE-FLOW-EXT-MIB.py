# SNMP MIB module (CISCO-IKE-FLOW-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IKE-FLOW-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:20 2024
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

(cisgIpsSgProtocol,
 cisgIpsSgTunIndex) = mibBuilder.importSymbols(
    "CISCO-IPSEC-SIGNALING-MIB",
    "cisgIpsSgProtocol",
    "cisgIpsSgTunIndex")

(CIKEIsakmpDoi,
 CIPsecPhase1PeerIdentityType) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIKEIsakmpDoi",
    "CIPsecPhase1PeerIdentityType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoIkeFlowExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428)
)
ciscoIkeFlowExtMIB.setRevisions(
        ("2004-09-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIkeFlowExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIkeFlowExtMIBNotifs = _CiscoIkeFlowExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 0)
)
_CiscoIkeFlowExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIkeFlowExtMIBObjects = _CiscoIkeFlowExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1)
)
_CifeIkeGlobals_ObjectIdentity = ObjectIdentity
cifeIkeGlobals = _CifeIkeGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 1)
)


class _CifeClearAllTunnels_Type(Integer32):
    """Custom type cifeClearAllTunnels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearFCSP", 3),
          ("clearIPSec", 2),
          ("none", 1))
    )


_CifeClearAllTunnels_Type.__name__ = "Integer32"
_CifeClearAllTunnels_Object = MibScalar
cifeClearAllTunnels = _CifeClearAllTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 1, 1),
    _CifeClearAllTunnels_Type()
)
cifeClearAllTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cifeClearAllTunnels.setStatus("current")
_CifeTunnelExtTable_Object = MibTable
cifeTunnelExtTable = _CifeTunnelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2)
)
if mibBuilder.loadTexts:
    cifeTunnelExtTable.setStatus("current")
_CifeTunnelExtEntry_Object = MibTableRow
cifeTunnelExtEntry = _CifeTunnelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1)
)
cifeTunnelExtEntry.setIndexNames(
    (0, "CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtDoi"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex"),
)
if mibBuilder.loadTexts:
    cifeTunnelExtEntry.setStatus("current")
_CifeTunnelExtDoi_Type = CIKEIsakmpDoi
_CifeTunnelExtDoi_Object = MibTableColumn
cifeTunnelExtDoi = _CifeTunnelExtDoi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 1),
    _CifeTunnelExtDoi_Type()
)
cifeTunnelExtDoi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifeTunnelExtDoi.setStatus("current")
_CifeTunnelExtLocalIdenType_Type = CIPsecPhase1PeerIdentityType
_CifeTunnelExtLocalIdenType_Object = MibTableColumn
cifeTunnelExtLocalIdenType = _CifeTunnelExtLocalIdenType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 2),
    _CifeTunnelExtLocalIdenType_Type()
)
cifeTunnelExtLocalIdenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifeTunnelExtLocalIdenType.setStatus("current")


class _CifeTunnelExtLocalIdentity_Type(SnmpAdminString):
    """Custom type cifeTunnelExtLocalIdentity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CifeTunnelExtLocalIdentity_Type.__name__ = "SnmpAdminString"
_CifeTunnelExtLocalIdentity_Object = MibTableColumn
cifeTunnelExtLocalIdentity = _CifeTunnelExtLocalIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 3),
    _CifeTunnelExtLocalIdentity_Type()
)
cifeTunnelExtLocalIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifeTunnelExtLocalIdentity.setStatus("current")
_CifeTunnelExtRemoteIdenType_Type = CIPsecPhase1PeerIdentityType
_CifeTunnelExtRemoteIdenType_Object = MibTableColumn
cifeTunnelExtRemoteIdenType = _CifeTunnelExtRemoteIdenType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 4),
    _CifeTunnelExtRemoteIdenType_Type()
)
cifeTunnelExtRemoteIdenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifeTunnelExtRemoteIdenType.setStatus("current")


class _CifeTunnelExtRemoteIdentity_Type(SnmpAdminString):
    """Custom type cifeTunnelExtRemoteIdentity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CifeTunnelExtRemoteIdentity_Type.__name__ = "SnmpAdminString"
_CifeTunnelExtRemoteIdentity_Object = MibTableColumn
cifeTunnelExtRemoteIdentity = _CifeTunnelExtRemoteIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 5),
    _CifeTunnelExtRemoteIdentity_Type()
)
cifeTunnelExtRemoteIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifeTunnelExtRemoteIdentity.setStatus("current")
_CiscoIkeFlowExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoIkeFlowExtMIBConform = _CiscoIkeFlowExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2)
)
_CifeMIBConformances_ObjectIdentity = ObjectIdentity
cifeMIBConformances = _CifeMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 1)
)
_CifeMIBGroups_ObjectIdentity = ObjectIdentity
cifeMIBGroups = _CifeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2)
)

# Managed Objects groups

cifeGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2, 1)
)
cifeGlobalsGroup.setObjects(
    ("CISCO-IKE-FLOW-EXT-MIB", "cifeClearAllTunnels")
)
if mibBuilder.loadTexts:
    cifeGlobalsGroup.setStatus("current")

cifeTunnelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2, 2)
)
cifeTunnelExtGroup.setObjects(
      *(("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtLocalIdenType"),
        ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtLocalIdentity"),
        ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtRemoteIdenType"),
        ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtRemoteIdentity"))
)
if mibBuilder.loadTexts:
    cifeTunnelExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cifeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cifeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IKE-FLOW-EXT-MIB",
    **{"ciscoIkeFlowExtMIB": ciscoIkeFlowExtMIB,
       "ciscoIkeFlowExtMIBNotifs": ciscoIkeFlowExtMIBNotifs,
       "ciscoIkeFlowExtMIBObjects": ciscoIkeFlowExtMIBObjects,
       "cifeIkeGlobals": cifeIkeGlobals,
       "cifeClearAllTunnels": cifeClearAllTunnels,
       "cifeTunnelExtTable": cifeTunnelExtTable,
       "cifeTunnelExtEntry": cifeTunnelExtEntry,
       "cifeTunnelExtDoi": cifeTunnelExtDoi,
       "cifeTunnelExtLocalIdenType": cifeTunnelExtLocalIdenType,
       "cifeTunnelExtLocalIdentity": cifeTunnelExtLocalIdentity,
       "cifeTunnelExtRemoteIdenType": cifeTunnelExtRemoteIdenType,
       "cifeTunnelExtRemoteIdentity": cifeTunnelExtRemoteIdentity,
       "ciscoIkeFlowExtMIBConform": ciscoIkeFlowExtMIBConform,
       "cifeMIBConformances": cifeMIBConformances,
       "cifeMIBCompliance": cifeMIBCompliance,
       "cifeMIBGroups": cifeMIBGroups,
       "cifeGlobalsGroup": cifeGlobalsGroup,
       "cifeTunnelExtGroup": cifeTunnelExtGroup}
)
