# SNMP MIB module (BROCADE-MCT-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-MCT-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:27 2024
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

(brcdMct,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "brcdMct")

(BrcdVlanIdOrNoneTC,
 BrcdVlanIdTC) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "BrcdVlanIdOrNoneTC",
    "BrcdVlanIdTC")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

brcdMctMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1)
)
brcdMctMIB.setRevisions(
        ("2011-12-20 00:00",
         "2014-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BrcdDeployStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deploy", 1),
          ("undeploy", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BrcdMctNotifications_ObjectIdentity = ObjectIdentity
brcdMctNotifications = _BrcdMctNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 0)
)
_BrcdMctObjects_ObjectIdentity = ObjectIdentity
brcdMctObjects = _BrcdMctObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1)
)
_BrcdMctL2Forward_Type = EnabledStatus
_BrcdMctL2Forward_Object = MibScalar
brcdMctL2Forward = _BrcdMctL2Forward_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 1),
    _BrcdMctL2Forward_Type()
)
brcdMctL2Forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdMctL2Forward.setStatus("current")
_BrcdMctClusterTable_Object = MibTable
brcdMctClusterTable = _BrcdMctClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brcdMctClusterTable.setStatus("current")
_BrcdMctClusterEntry_Object = MibTableRow
brcdMctClusterEntry = _BrcdMctClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1)
)
brcdMctClusterEntry.setIndexNames(
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterId"),
)
if mibBuilder.loadTexts:
    brcdMctClusterEntry.setStatus("current")


class _BrcdMctClusterId_Type(Unsigned32):
    """Custom type brcdMctClusterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrcdMctClusterId_Type.__name__ = "Unsigned32"
_BrcdMctClusterId_Object = MibTableColumn
brcdMctClusterId = _BrcdMctClusterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 1),
    _BrcdMctClusterId_Type()
)
brcdMctClusterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMctClusterId.setStatus("current")


class _BrcdMctClusterName_Type(DisplayString):
    """Custom type brcdMctClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BrcdMctClusterName_Type.__name__ = "DisplayString"
_BrcdMctClusterName_Object = MibTableColumn
brcdMctClusterName = _BrcdMctClusterName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 2),
    _BrcdMctClusterName_Type()
)
brcdMctClusterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterName.setStatus("current")


class _BrcdMctClusterRbridgeId_Type(Unsigned32):
    """Custom type brcdMctClusterRbridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35535),
    )


_BrcdMctClusterRbridgeId_Type.__name__ = "Unsigned32"
_BrcdMctClusterRbridgeId_Object = MibTableColumn
brcdMctClusterRbridgeId = _BrcdMctClusterRbridgeId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 3),
    _BrcdMctClusterRbridgeId_Type()
)
brcdMctClusterRbridgeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterRbridgeId.setStatus("current")
_BrcdMctClusterSessionVlan_Type = BrcdVlanIdTC
_BrcdMctClusterSessionVlan_Object = MibTableColumn
brcdMctClusterSessionVlan = _BrcdMctClusterSessionVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 4),
    _BrcdMctClusterSessionVlan_Type()
)
brcdMctClusterSessionVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterSessionVlan.setStatus("current")


class _BrcdMctClusterKeepAliveVlan_Type(BrcdVlanIdOrNoneTC):
    """Custom type brcdMctClusterKeepAliveVlan based on BrcdVlanIdOrNoneTC"""
    defaultValue = 0


_BrcdMctClusterKeepAliveVlan_Object = MibTableColumn
brcdMctClusterKeepAliveVlan = _BrcdMctClusterKeepAliveVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 5),
    _BrcdMctClusterKeepAliveVlan_Type()
)
brcdMctClusterKeepAliveVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterKeepAliveVlan.setStatus("current")


class _BrcdMctClusterClientIsolationMode_Type(Integer32):
    """Custom type brcdMctClusterClientIsolationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 1),
          ("strict", 2))
    )


_BrcdMctClusterClientIsolationMode_Type.__name__ = "Integer32"
_BrcdMctClusterClientIsolationMode_Object = MibTableColumn
brcdMctClusterClientIsolationMode = _BrcdMctClusterClientIsolationMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 6),
    _BrcdMctClusterClientIsolationMode_Type()
)
brcdMctClusterClientIsolationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientIsolationMode.setStatus("current")


class _BrcdMctClusterClientShutdown_Type(TruthValue):
    """Custom type brcdMctClusterClientShutdown based on TruthValue"""


_BrcdMctClusterClientShutdown_Object = MibTableColumn
brcdMctClusterClientShutdown = _BrcdMctClusterClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 7),
    _BrcdMctClusterClientShutdown_Type()
)
brcdMctClusterClientShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientShutdown.setStatus("current")
_BrcdMctClusterMemberVlans_Type = DisplayString
_BrcdMctClusterMemberVlans_Object = MibTableColumn
brcdMctClusterMemberVlans = _BrcdMctClusterMemberVlans_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 8),
    _BrcdMctClusterMemberVlans_Type()
)
brcdMctClusterMemberVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterMemberVlans.setStatus("current")
_BrcdMctClusterActiveMemberVlans_Type = DisplayString
_BrcdMctClusterActiveMemberVlans_Object = MibTableColumn
brcdMctClusterActiveMemberVlans = _BrcdMctClusterActiveMemberVlans_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 9),
    _BrcdMctClusterActiveMemberVlans_Type()
)
brcdMctClusterActiveMemberVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterActiveMemberVlans.setStatus("current")


class _BrcdMctClusterDeploy_Type(BrcdDeployStatus):
    """Custom type brcdMctClusterDeploy based on BrcdDeployStatus"""


_BrcdMctClusterDeploy_Object = MibTableColumn
brcdMctClusterDeploy = _BrcdMctClusterDeploy_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 10),
    _BrcdMctClusterDeploy_Type()
)
brcdMctClusterDeploy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterDeploy.setStatus("current")


class _BrcdMctClusterDeployFailureReason_Type(Integer32):
    """Custom type brcdMctClusterDeployFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("clientInterfaceIsNotInMemberVlan", 19),
          ("defaultVlanConfigForSessionOrMemberVlan", 20),
          ("iclIsErpFsInterface", 10),
          ("iclIsErpMsInterface", 9),
          ("iclIsErpRplInterface", 8),
          ("iclIsMrpSecondaryInterface", 7),
          ("iclNotConfigured", 5),
          ("iclNotInMemberVlans", 12),
          ("iclNotInSessionVlan", 11),
          ("mgmtIpIsUsedInPeerOrClientConfig", 16),
          ("mgmtIpNotConfiguredInSessionVlan", 15),
          ("mgmtIpNotInSubnetOfPeerIp", 17),
          ("mgmtVeNotConfiguredInSessionVlan", 14),
          ("nonIclInterfacesInSessionVlan", 13),
          ("none", 1),
          ("peerNotConfigured", 6),
          ("rBridgeIdIsUsedInPeerOrClientConfig", 18),
          ("rBridgeIdNotConfigured", 3),
          ("sessionVlanNotConfigured", 4),
          ("unknown", 2))
    )


_BrcdMctClusterDeployFailureReason_Type.__name__ = "Integer32"
_BrcdMctClusterDeployFailureReason_Object = MibTableColumn
brcdMctClusterDeployFailureReason = _BrcdMctClusterDeployFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 11),
    _BrcdMctClusterDeployFailureReason_Type()
)
brcdMctClusterDeployFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterDeployFailureReason.setStatus("current")
_BrcdMctClusterRowStatus_Type = RowStatus
_BrcdMctClusterRowStatus_Object = MibTableColumn
brcdMctClusterRowStatus = _BrcdMctClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 2, 1, 12),
    _BrcdMctClusterRowStatus_Type()
)
brcdMctClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterRowStatus.setStatus("current")
_BrcdMctClusterIclTable_Object = MibTable
brcdMctClusterIclTable = _BrcdMctClusterIclTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    brcdMctClusterIclTable.setStatus("current")
_BrcdMctClusterIclEntry_Object = MibTableRow
brcdMctClusterIclEntry = _BrcdMctClusterIclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 3, 1)
)
brcdMctClusterIclEntry.setIndexNames(
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterId"),
    (1, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterIclName"),
)
if mibBuilder.loadTexts:
    brcdMctClusterIclEntry.setStatus("current")


class _BrcdMctClusterIclName_Type(DisplayString):
    """Custom type brcdMctClusterIclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BrcdMctClusterIclName_Type.__name__ = "DisplayString"
_BrcdMctClusterIclName_Object = MibTableColumn
brcdMctClusterIclName = _BrcdMctClusterIclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 3, 1, 1),
    _BrcdMctClusterIclName_Type()
)
brcdMctClusterIclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMctClusterIclName.setStatus("current")
_BrcdMctClusterIclIfIndex_Type = InterfaceIndex
_BrcdMctClusterIclIfIndex_Object = MibTableColumn
brcdMctClusterIclIfIndex = _BrcdMctClusterIclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 3, 1, 2),
    _BrcdMctClusterIclIfIndex_Type()
)
brcdMctClusterIclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterIclIfIndex.setStatus("current")
_BrcdMctClusterIclRowStatus_Type = RowStatus
_BrcdMctClusterIclRowStatus_Object = MibTableColumn
brcdMctClusterIclRowStatus = _BrcdMctClusterIclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 3, 1, 3),
    _BrcdMctClusterIclRowStatus_Type()
)
brcdMctClusterIclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterIclRowStatus.setStatus("current")
_BrcdMctClusterPeerTable_Object = MibTable
brcdMctClusterPeerTable = _BrcdMctClusterPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    brcdMctClusterPeerTable.setStatus("current")
_BrcdMctClusterPeerEntry_Object = MibTableRow
brcdMctClusterPeerEntry = _BrcdMctClusterPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1)
)
brcdMctClusterPeerEntry.setIndexNames(
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterId"),
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterPeerAddrType"),
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterPeerAddr"),
)
if mibBuilder.loadTexts:
    brcdMctClusterPeerEntry.setStatus("current")
_BrcdMctClusterPeerAddrType_Type = InetAddressType
_BrcdMctClusterPeerAddrType_Object = MibTableColumn
brcdMctClusterPeerAddrType = _BrcdMctClusterPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 1),
    _BrcdMctClusterPeerAddrType_Type()
)
brcdMctClusterPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMctClusterPeerAddrType.setStatus("current")
_BrcdMctClusterPeerAddr_Type = InetAddress
_BrcdMctClusterPeerAddr_Object = MibTableColumn
brcdMctClusterPeerAddr = _BrcdMctClusterPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 2),
    _BrcdMctClusterPeerAddr_Type()
)
brcdMctClusterPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMctClusterPeerAddr.setStatus("current")


class _BrcdMctClusterPeerRbridgeId_Type(Unsigned32):
    """Custom type brcdMctClusterPeerRbridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35535),
    )


_BrcdMctClusterPeerRbridgeId_Type.__name__ = "Unsigned32"
_BrcdMctClusterPeerRbridgeId_Object = MibTableColumn
brcdMctClusterPeerRbridgeId = _BrcdMctClusterPeerRbridgeId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 3),
    _BrcdMctClusterPeerRbridgeId_Type()
)
brcdMctClusterPeerRbridgeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerRbridgeId.setStatus("current")


class _BrcdMctClusterPeerIclName_Type(DisplayString):
    """Custom type brcdMctClusterPeerIclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BrcdMctClusterPeerIclName_Type.__name__ = "DisplayString"
_BrcdMctClusterPeerIclName_Object = MibTableColumn
brcdMctClusterPeerIclName = _BrcdMctClusterPeerIclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 4),
    _BrcdMctClusterPeerIclName_Type()
)
brcdMctClusterPeerIclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerIclName.setStatus("current")


class _BrcdMctClusterPeerFastFailover_Type(EnabledStatus):
    """Custom type brcdMctClusterPeerFastFailover based on EnabledStatus"""


_BrcdMctClusterPeerFastFailover_Object = MibTableColumn
brcdMctClusterPeerFastFailover = _BrcdMctClusterPeerFastFailover_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 5),
    _BrcdMctClusterPeerFastFailover_Type()
)
brcdMctClusterPeerFastFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerFastFailover.setStatus("current")
_BrcdMctClusterPeerKeepAliveTime_Type = Unsigned32
_BrcdMctClusterPeerKeepAliveTime_Object = MibTableColumn
brcdMctClusterPeerKeepAliveTime = _BrcdMctClusterPeerKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 6),
    _BrcdMctClusterPeerKeepAliveTime_Type()
)
brcdMctClusterPeerKeepAliveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerKeepAliveTime.setStatus("current")


class _BrcdMctClusterPeerHoldTime_Type(Unsigned32):
    """Custom type brcdMctClusterPeerHoldTime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_BrcdMctClusterPeerHoldTime_Type.__name__ = "Unsigned32"
_BrcdMctClusterPeerHoldTime_Object = MibTableColumn
brcdMctClusterPeerHoldTime = _BrcdMctClusterPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 7),
    _BrcdMctClusterPeerHoldTime_Type()
)
brcdMctClusterPeerHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerHoldTime.setStatus("current")
_BrcdMctClusterPeerActiveVlans_Type = DisplayString
_BrcdMctClusterPeerActiveVlans_Object = MibTableColumn
brcdMctClusterPeerActiveVlans = _BrcdMctClusterPeerActiveVlans_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 8),
    _BrcdMctClusterPeerActiveVlans_Type()
)
brcdMctClusterPeerActiveVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterPeerActiveVlans.setStatus("current")


class _BrcdMctClusterPeerOperStatus_Type(Integer32):
    """Custom type brcdMctClusterPeerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ccpDown", 5),
          ("ccpUp", 4),
          ("init", 3),
          ("noState", 2),
          ("reachable", 6),
          ("unknown", 1))
    )


_BrcdMctClusterPeerOperStatus_Type.__name__ = "Integer32"
_BrcdMctClusterPeerOperStatus_Object = MibTableColumn
brcdMctClusterPeerOperStatus = _BrcdMctClusterPeerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 9),
    _BrcdMctClusterPeerOperStatus_Type()
)
brcdMctClusterPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterPeerOperStatus.setStatus("current")


class _BrcdMctClusterPeerDownReason_Type(Integer32):
    """Custom type brcdMctClusterPeerDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("badPduLengthPktRecv", 22),
          ("badProtocolVersionPktRecv", 21),
          ("ccpTcpCommFail", 26),
          ("clusterIdMismatch", 8),
          ("fastFailoverMismatch", 11),
          ("holdTimeMismatch", 10),
          ("holdTimeoutExpired", 15),
          ("iclInterfaceDown", 3),
          ("iclVeDown", 6),
          ("initMesgSendFail", 18),
          ("internalCcpErrorRecv", 25),
          ("invalidAppMesgRecv", 20),
          ("invalidCcpPktRecv", 24),
          ("keepAliveMesgSendFail", 19),
          ("keepAliveTimeMismatch", 9),
          ("loopbackInterfaceDown", 2),
          ("none", 1),
          ("rBridgeIdMismatch", 7),
          ("recvStateTimeoutExpired", 17),
          ("routeNotAvailable", 5),
          ("sendStateTimeoutExpired", 16),
          ("shutdownMesgFromPeer", 12),
          ("tcpConnCloseMesg", 14),
          ("tcpKeepAliveTimeout", 13),
          ("unknownCcpPktRecv", 23),
          ("upgradeInProgress", 4))
    )


_BrcdMctClusterPeerDownReason_Type.__name__ = "Integer32"
_BrcdMctClusterPeerDownReason_Object = MibTableColumn
brcdMctClusterPeerDownReason = _BrcdMctClusterPeerDownReason_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 10),
    _BrcdMctClusterPeerDownReason_Type()
)
brcdMctClusterPeerDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterPeerDownReason.setStatus("current")
_BrcdMctClusterPeerUpTime_Type = TimeInterval
_BrcdMctClusterPeerUpTime_Object = MibTableColumn
brcdMctClusterPeerUpTime = _BrcdMctClusterPeerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 11),
    _BrcdMctClusterPeerUpTime_Type()
)
brcdMctClusterPeerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterPeerUpTime.setStatus("current")
_BrcdMctClusterPeerRowStatus_Type = RowStatus
_BrcdMctClusterPeerRowStatus_Object = MibTableColumn
brcdMctClusterPeerRowStatus = _BrcdMctClusterPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 4, 1, 12),
    _BrcdMctClusterPeerRowStatus_Type()
)
brcdMctClusterPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterPeerRowStatus.setStatus("current")
_BrcdMctClusterClientTable_Object = MibTable
brcdMctClusterClientTable = _BrcdMctClusterClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    brcdMctClusterClientTable.setStatus("current")
_BrcdMctClusterClientEntry_Object = MibTableRow
brcdMctClusterClientEntry = _BrcdMctClusterClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1)
)
brcdMctClusterClientEntry.setIndexNames(
    (0, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterId"),
    (1, "BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterClientName"),
)
if mibBuilder.loadTexts:
    brcdMctClusterClientEntry.setStatus("current")


class _BrcdMctClusterClientName_Type(DisplayString):
    """Custom type brcdMctClusterClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BrcdMctClusterClientName_Type.__name__ = "DisplayString"
_BrcdMctClusterClientName_Object = MibTableColumn
brcdMctClusterClientName = _BrcdMctClusterClientName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 1),
    _BrcdMctClusterClientName_Type()
)
brcdMctClusterClientName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMctClusterClientName.setStatus("current")


class _BrcdMctClusterClientRbridgeId_Type(Unsigned32):
    """Custom type brcdMctClusterClientRbridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35535),
    )


_BrcdMctClusterClientRbridgeId_Type.__name__ = "Unsigned32"
_BrcdMctClusterClientRbridgeId_Object = MibTableColumn
brcdMctClusterClientRbridgeId = _BrcdMctClusterClientRbridgeId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 2),
    _BrcdMctClusterClientRbridgeId_Type()
)
brcdMctClusterClientRbridgeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientRbridgeId.setStatus("current")
_BrcdMctClusterClientIfIndex_Type = InterfaceIndex
_BrcdMctClusterClientIfIndex_Object = MibTableColumn
brcdMctClusterClientIfIndex = _BrcdMctClusterClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 3),
    _BrcdMctClusterClientIfIndex_Type()
)
brcdMctClusterClientIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientIfIndex.setStatus("current")


class _BrcdMctClusterClientOperStatus_Type(Integer32):
    """Custom type brcdMctClusterClientOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("adminUp", 5),
          ("init", 3),
          ("localDeploy", 4),
          ("localUp", 7),
          ("master", 10),
          ("masterPeerUp", 11),
          ("noState", 2),
          ("remoteUp", 6),
          ("slave", 9),
          ("unknown", 1),
          ("up", 8))
    )


_BrcdMctClusterClientOperStatus_Type.__name__ = "Integer32"
_BrcdMctClusterClientOperStatus_Object = MibTableColumn
brcdMctClusterClientOperStatus = _BrcdMctClusterClientOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 4),
    _BrcdMctClusterClientOperStatus_Type()
)
brcdMctClusterClientOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterClientOperStatus.setStatus("current")
_BrcdMctClusterClientDeploy_Type = BrcdDeployStatus
_BrcdMctClusterClientDeploy_Object = MibTableColumn
brcdMctClusterClientDeploy = _BrcdMctClusterClientDeploy_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 5),
    _BrcdMctClusterClientDeploy_Type()
)
brcdMctClusterClientDeploy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientDeploy.setStatus("current")


class _BrcdMctClusterClientDeployFailureReason_Type(Integer32):
    """Custom type brcdMctClusterClientDeployFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clientInterfaceIsErpInterface", 8),
          ("clientInterfaceIsMrpRingInterface", 7),
          ("clientInterfaceNotConfigured", 4),
          ("clientInterfacePhysicallyNotUp", 6),
          ("iclIsNotInMemberVlan", 9),
          ("none", 1),
          ("rBridgeIdNotConfigured", 3),
          ("rBridgeIdUsedInClusterOrPeer", 5),
          ("unknown", 2))
    )


_BrcdMctClusterClientDeployFailureReason_Type.__name__ = "Integer32"
_BrcdMctClusterClientDeployFailureReason_Object = MibTableColumn
brcdMctClusterClientDeployFailureReason = _BrcdMctClusterClientDeployFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 6),
    _BrcdMctClusterClientDeployFailureReason_Type()
)
brcdMctClusterClientDeployFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdMctClusterClientDeployFailureReason.setStatus("current")
_BrcdMctClusterClientRowStatus_Type = RowStatus
_BrcdMctClusterClientRowStatus_Object = MibTableColumn
brcdMctClusterClientRowStatus = _BrcdMctClusterClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 1, 5, 1, 7),
    _BrcdMctClusterClientRowStatus_Type()
)
brcdMctClusterClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMctClusterClientRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

brcdMctClusterPeerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 0, 1)
)
brcdMctClusterPeerStatus.setObjects(
      *(("BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterPeerOperStatus"),
        ("BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterPeerDownReason"))
)
if mibBuilder.loadTexts:
    brcdMctClusterPeerStatus.setStatus(
        "current"
    )

brcdMctClusterClientStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12, 1, 0, 2)
)
brcdMctClusterClientStatus.setObjects(
    ("BROCADE-MCT-CLUSTER-MIB", "brcdMctClusterClientOperStatus")
)
if mibBuilder.loadTexts:
    brcdMctClusterClientStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-MCT-CLUSTER-MIB",
    **{"BrcdDeployStatus": BrcdDeployStatus,
       "brcdMctMIB": brcdMctMIB,
       "brcdMctNotifications": brcdMctNotifications,
       "brcdMctClusterPeerStatus": brcdMctClusterPeerStatus,
       "brcdMctClusterClientStatus": brcdMctClusterClientStatus,
       "brcdMctObjects": brcdMctObjects,
       "brcdMctL2Forward": brcdMctL2Forward,
       "brcdMctClusterTable": brcdMctClusterTable,
       "brcdMctClusterEntry": brcdMctClusterEntry,
       "brcdMctClusterId": brcdMctClusterId,
       "brcdMctClusterName": brcdMctClusterName,
       "brcdMctClusterRbridgeId": brcdMctClusterRbridgeId,
       "brcdMctClusterSessionVlan": brcdMctClusterSessionVlan,
       "brcdMctClusterKeepAliveVlan": brcdMctClusterKeepAliveVlan,
       "brcdMctClusterClientIsolationMode": brcdMctClusterClientIsolationMode,
       "brcdMctClusterClientShutdown": brcdMctClusterClientShutdown,
       "brcdMctClusterMemberVlans": brcdMctClusterMemberVlans,
       "brcdMctClusterActiveMemberVlans": brcdMctClusterActiveMemberVlans,
       "brcdMctClusterDeploy": brcdMctClusterDeploy,
       "brcdMctClusterDeployFailureReason": brcdMctClusterDeployFailureReason,
       "brcdMctClusterRowStatus": brcdMctClusterRowStatus,
       "brcdMctClusterIclTable": brcdMctClusterIclTable,
       "brcdMctClusterIclEntry": brcdMctClusterIclEntry,
       "brcdMctClusterIclName": brcdMctClusterIclName,
       "brcdMctClusterIclIfIndex": brcdMctClusterIclIfIndex,
       "brcdMctClusterIclRowStatus": brcdMctClusterIclRowStatus,
       "brcdMctClusterPeerTable": brcdMctClusterPeerTable,
       "brcdMctClusterPeerEntry": brcdMctClusterPeerEntry,
       "brcdMctClusterPeerAddrType": brcdMctClusterPeerAddrType,
       "brcdMctClusterPeerAddr": brcdMctClusterPeerAddr,
       "brcdMctClusterPeerRbridgeId": brcdMctClusterPeerRbridgeId,
       "brcdMctClusterPeerIclName": brcdMctClusterPeerIclName,
       "brcdMctClusterPeerFastFailover": brcdMctClusterPeerFastFailover,
       "brcdMctClusterPeerKeepAliveTime": brcdMctClusterPeerKeepAliveTime,
       "brcdMctClusterPeerHoldTime": brcdMctClusterPeerHoldTime,
       "brcdMctClusterPeerActiveVlans": brcdMctClusterPeerActiveVlans,
       "brcdMctClusterPeerOperStatus": brcdMctClusterPeerOperStatus,
       "brcdMctClusterPeerDownReason": brcdMctClusterPeerDownReason,
       "brcdMctClusterPeerUpTime": brcdMctClusterPeerUpTime,
       "brcdMctClusterPeerRowStatus": brcdMctClusterPeerRowStatus,
       "brcdMctClusterClientTable": brcdMctClusterClientTable,
       "brcdMctClusterClientEntry": brcdMctClusterClientEntry,
       "brcdMctClusterClientName": brcdMctClusterClientName,
       "brcdMctClusterClientRbridgeId": brcdMctClusterClientRbridgeId,
       "brcdMctClusterClientIfIndex": brcdMctClusterClientIfIndex,
       "brcdMctClusterClientOperStatus": brcdMctClusterClientOperStatus,
       "brcdMctClusterClientDeploy": brcdMctClusterClientDeploy,
       "brcdMctClusterClientDeployFailureReason": brcdMctClusterClientDeployFailureReason,
       "brcdMctClusterClientRowStatus": brcdMctClusterClientRowStatus}
)
