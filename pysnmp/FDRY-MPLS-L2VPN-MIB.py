# SNMP MIB module (FDRY-MPLS-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-MPLS-L2VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:43 2024
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

(snMpls,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snMpls")

(PortPriorityTC,
 VlanTagMode) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "PortPriorityTC",
    "VlanTagMode")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pwEnetPwInstance,) = mibBuilder.importSymbols(
    "PW-ENET-STD-MIB",
    "pwEnetPwInstance")

(pwID,
 pwIndex,
 pwName) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwID",
    "pwIndex",
    "pwName")

(PwOperStatusTC,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwOperStatusTC")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vplsConfigEntry,
 vplsConfigIndex,
 vplsConfigName) = mibBuilder.importSymbols(
    "VPLS-GENERIC-MIB",
    "vplsConfigEntry",
    "vplsConfigIndex",
    "vplsConfigName")


# MODULE-IDENTITY

fdryMplsL2VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2)
)
fdryMplsL2VpnMIB.setRevisions(
        ("2012-04-04 00:00",
         "2010-06-02 00:00",
         "2008-02-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vll", 1),
          ("vllLocal", 2),
          ("vpls", 3))
    )



class AdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )



class ClassOfService(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



class Layer2StateTC(Integer32, TextualConvention):
    status = "current"
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 6),
          ("learning", 4),
          ("listening", 3),
          ("preforwarding", 5))
    )



class FdryPwServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vll", 1),
          ("vllLocal", 2),
          ("vpls", 3))
    )



class PwVlanCfg(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



# MIB Managed Objects in the order of their OIDs

_FdryMplsVpnNotifications_ObjectIdentity = ObjectIdentity
fdryMplsVpnNotifications = _FdryMplsVpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0)
)
_FdryMplsVllInfo_ObjectIdentity = ObjectIdentity
fdryMplsVllInfo = _FdryMplsVllInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1)
)
_FdryVllEndPointTable_Object = MibTable
fdryVllEndPointTable = _FdryVllEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fdryVllEndPointTable.setStatus("current")
_FdryVllEndPointEntry_Object = MibTableRow
fdryVllEndPointEntry = _FdryVllEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1)
)
fdryVllEndPointEntry.setIndexNames(
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVllEndPointServiceType"),
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ENET-STD-MIB", "pwEnetPwInstance"),
)
if mibBuilder.loadTexts:
    fdryVllEndPointEntry.setStatus("current")
_FdryVllEndPointServiceType_Type = MplsServiceType
_FdryVllEndPointServiceType_Object = MibTableColumn
fdryVllEndPointServiceType = _FdryVllEndPointServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 1),
    _FdryVllEndPointServiceType_Type()
)
fdryVllEndPointServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVllEndPointServiceType.setStatus("current")
_FdryVllEndPointVlanTagMode_Type = VlanTagMode
_FdryVllEndPointVlanTagMode_Object = MibTableColumn
fdryVllEndPointVlanTagMode = _FdryVllEndPointVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 2),
    _FdryVllEndPointVlanTagMode_Type()
)
fdryVllEndPointVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointVlanTagMode.setStatus("current")


class _FdryVllEndPointClassOfService_Type(ClassOfService):
    """Custom type fdryVllEndPointClassOfService based on ClassOfService"""
    defaultValue = 0


_FdryVllEndPointClassOfService_Object = MibTableColumn
fdryVllEndPointClassOfService = _FdryVllEndPointClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 3),
    _FdryVllEndPointClassOfService_Type()
)
fdryVllEndPointClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointClassOfService.setStatus("current")
_FdryVllEndPointInHCPkts_Type = Counter64
_FdryVllEndPointInHCPkts_Object = MibTableColumn
fdryVllEndPointInHCPkts = _FdryVllEndPointInHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 4),
    _FdryVllEndPointInHCPkts_Type()
)
fdryVllEndPointInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointInHCPkts.setStatus("current")
_FdryVllEndPointOutHCPkts_Type = Counter64
_FdryVllEndPointOutHCPkts_Object = MibTableColumn
fdryVllEndPointOutHCPkts = _FdryVllEndPointOutHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 5),
    _FdryVllEndPointOutHCPkts_Type()
)
fdryVllEndPointOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOutHCPkts.setStatus("current")
_FdryVllEndPointAdminStatus_Type = AdminStatus
_FdryVllEndPointAdminStatus_Object = MibTableColumn
fdryVllEndPointAdminStatus = _FdryVllEndPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 6),
    _FdryVllEndPointAdminStatus_Type()
)
fdryVllEndPointAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointAdminStatus.setStatus("current")
_FdryVllEndPointOperStatus_Type = PwOperStatusTC
_FdryVllEndPointOperStatus_Object = MibTableColumn
fdryVllEndPointOperStatus = _FdryVllEndPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 7),
    _FdryVllEndPointOperStatus_Type()
)
fdryVllEndPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOperStatus.setStatus("current")
_FdryVllEndPointRowStatus_Type = RowStatus
_FdryVllEndPointRowStatus_Object = MibTableColumn
fdryVllEndPointRowStatus = _FdryVllEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 8),
    _FdryVllEndPointRowStatus_Type()
)
fdryVllEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointRowStatus.setStatus("current")


class _FdryVllEndPointInnerVlanId_Type(PwVlanCfg):
    """Custom type fdryVllEndPointInnerVlanId based on PwVlanCfg"""
    defaultValue = 0


_FdryVllEndPointInnerVlanId_Object = MibTableColumn
fdryVllEndPointInnerVlanId = _FdryVllEndPointInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 9),
    _FdryVllEndPointInnerVlanId_Type()
)
fdryVllEndPointInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointInnerVlanId.setStatus("current")
_FdryVllEndPointInHCOctets_Type = Counter64
_FdryVllEndPointInHCOctets_Object = MibTableColumn
fdryVllEndPointInHCOctets = _FdryVllEndPointInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 10),
    _FdryVllEndPointInHCOctets_Type()
)
fdryVllEndPointInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointInHCOctets.setStatus("current")
_FdryVllEndPointOutHCOctets_Type = Counter64
_FdryVllEndPointOutHCOctets_Object = MibTableColumn
fdryVllEndPointOutHCOctets = _FdryVllEndPointOutHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 11),
    _FdryVllEndPointOutHCOctets_Type()
)
fdryVllEndPointOutHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOutHCOctets.setStatus("current")
_BrcdVllEndptVlanExtStatsTable_Object = MibTable
brcdVllEndptVlanExtStatsTable = _BrcdVllEndptVlanExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsTable.setStatus("current")
_BrcdVllEndptVlanExtStatsEntry_Object = MibTableRow
brcdVllEndptVlanExtStatsEntry = _BrcdVllEndptVlanExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1)
)
brcdVllEndptVlanExtStatsEntry.setIndexNames(
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVllEndPointServiceType"),
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ENET-STD-MIB", "pwEnetPwInstance"),
    (0, "FDRY-MPLS-L2VPN-MIB", "brcdVllEndptVlanExtStatsPriorityId"),
)
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsEntry.setStatus("current")
_BrcdVllEndptVlanExtStatsPriorityId_Type = PortPriorityTC
_BrcdVllEndptVlanExtStatsPriorityId_Object = MibTableColumn
brcdVllEndptVlanExtStatsPriorityId = _BrcdVllEndptVlanExtStatsPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 1),
    _BrcdVllEndptVlanExtStatsPriorityId_Type()
)
brcdVllEndptVlanExtStatsPriorityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsPriorityId.setStatus("current")
_BrcdVllEndptVlanExtStatsInPkts_Type = Counter64
_BrcdVllEndptVlanExtStatsInPkts_Object = MibTableColumn
brcdVllEndptVlanExtStatsInPkts = _BrcdVllEndptVlanExtStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 2),
    _BrcdVllEndptVlanExtStatsInPkts_Type()
)
brcdVllEndptVlanExtStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsInPkts.setStatus("current")
_BrcdVllEndptVlanExtStatsOutPkts_Type = Counter64
_BrcdVllEndptVlanExtStatsOutPkts_Object = MibTableColumn
brcdVllEndptVlanExtStatsOutPkts = _BrcdVllEndptVlanExtStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 3),
    _BrcdVllEndptVlanExtStatsOutPkts_Type()
)
brcdVllEndptVlanExtStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsOutPkts.setStatus("current")
_BrcdVllEndptVlanExtStatsInOctets_Type = Counter64
_BrcdVllEndptVlanExtStatsInOctets_Object = MibTableColumn
brcdVllEndptVlanExtStatsInOctets = _BrcdVllEndptVlanExtStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 4),
    _BrcdVllEndptVlanExtStatsInOctets_Type()
)
brcdVllEndptVlanExtStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsInOctets.setStatus("current")
_BrcdVllEndptVlanExtStatsOutOctets_Type = Counter64
_BrcdVllEndptVlanExtStatsOutOctets_Object = MibTableColumn
brcdVllEndptVlanExtStatsOutOctets = _BrcdVllEndptVlanExtStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 5),
    _BrcdVllEndptVlanExtStatsOutOctets_Type()
)
brcdVllEndptVlanExtStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVllEndptVlanExtStatsOutOctets.setStatus("current")
_FdryMplsVplsInfo_ObjectIdentity = ObjectIdentity
fdryMplsVplsInfo = _FdryMplsVplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2)
)
_FdryVplsEndPointTable_Object = MibTable
fdryVplsEndPointTable = _FdryVplsEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fdryVplsEndPointTable.setStatus("deprecated")
_FdryVplsEndPointEntry_Object = MibTableRow
fdryVplsEndPointEntry = _FdryVplsEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1)
)
fdryVplsEndPointEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointPortVlan"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointIfIndex"),
)
if mibBuilder.loadTexts:
    fdryVplsEndPointEntry.setStatus("deprecated")
_FdryVplsEndPointPortVlan_Type = PwVlanCfg
_FdryVplsEndPointPortVlan_Object = MibTableColumn
fdryVplsEndPointPortVlan = _FdryVplsEndPointPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 1),
    _FdryVplsEndPointPortVlan_Type()
)
fdryVplsEndPointPortVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPointPortVlan.setStatus("deprecated")
_FdryVplsEndPointIfIndex_Type = InterfaceIndex
_FdryVplsEndPointIfIndex_Object = MibTableColumn
fdryVplsEndPointIfIndex = _FdryVplsEndPointIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 2),
    _FdryVplsEndPointIfIndex_Type()
)
fdryVplsEndPointIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPointIfIndex.setStatus("deprecated")
_FdryVplsEndPointVlanTagMode_Type = VlanTagMode
_FdryVplsEndPointVlanTagMode_Object = MibTableColumn
fdryVplsEndPointVlanTagMode = _FdryVplsEndPointVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 3),
    _FdryVplsEndPointVlanTagMode_Type()
)
fdryVplsEndPointVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointVlanTagMode.setStatus("deprecated")
_FdryVplsEndPointOutHCPkts_Type = Counter64
_FdryVplsEndPointOutHCPkts_Object = MibTableColumn
fdryVplsEndPointOutHCPkts = _FdryVplsEndPointOutHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 4),
    _FdryVplsEndPointOutHCPkts_Type()
)
fdryVplsEndPointOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointOutHCPkts.setStatus("deprecated")


class _FdryVplsEndPointState_Type(Integer32):
    """Custom type fdryVplsEndPointState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5))
    )


_FdryVplsEndPointState_Type.__name__ = "Integer32"
_FdryVplsEndPointState_Object = MibTableColumn
fdryVplsEndPointState = _FdryVplsEndPointState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 5),
    _FdryVplsEndPointState_Type()
)
fdryVplsEndPointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointState.setStatus("deprecated")
_FdryVplsEndPointAdminStatus_Type = AdminStatus
_FdryVplsEndPointAdminStatus_Object = MibTableColumn
fdryVplsEndPointAdminStatus = _FdryVplsEndPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 6),
    _FdryVplsEndPointAdminStatus_Type()
)
fdryVplsEndPointAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointAdminStatus.setStatus("deprecated")
_FdryVplsEndPointOperStatus_Type = PwOperStatusTC
_FdryVplsEndPointOperStatus_Object = MibTableColumn
fdryVplsEndPointOperStatus = _FdryVplsEndPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 7),
    _FdryVplsEndPointOperStatus_Type()
)
fdryVplsEndPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointOperStatus.setStatus("deprecated")
_FdryVplsEndPointRowStatus_Type = RowStatus
_FdryVplsEndPointRowStatus_Object = MibTableColumn
fdryVplsEndPointRowStatus = _FdryVplsEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 8),
    _FdryVplsEndPointRowStatus_Type()
)
fdryVplsEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointRowStatus.setStatus("deprecated")
_FdryVplsEndPointInHCOctets_Type = Counter64
_FdryVplsEndPointInHCOctets_Object = MibTableColumn
fdryVplsEndPointInHCOctets = _FdryVplsEndPointInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 9),
    _FdryVplsEndPointInHCOctets_Type()
)
fdryVplsEndPointInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointInHCOctets.setStatus("deprecated")
_FdryVplsTable_Object = MibTable
fdryVplsTable = _FdryVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fdryVplsTable.setStatus("current")
_FdryVplsEntry_Object = MibTableRow
fdryVplsEntry = _FdryVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fdryVplsEntry.setStatus("current")


class _FdryVplsClassOfService_Type(ClassOfService):
    """Custom type fdryVplsClassOfService based on ClassOfService"""
    defaultValue = 0


_FdryVplsClassOfService_Object = MibTableColumn
fdryVplsClassOfService = _FdryVplsClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 1),
    _FdryVplsClassOfService_Type()
)
fdryVplsClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsClassOfService.setStatus("current")
_FdryVplsMaxMacLearned_Type = Unsigned32
_FdryVplsMaxMacLearned_Object = MibTableColumn
fdryVplsMaxMacLearned = _FdryVplsMaxMacLearned_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 2),
    _FdryVplsMaxMacLearned_Type()
)
fdryVplsMaxMacLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsMaxMacLearned.setStatus("current")
_FdryVplsClearMac_Type = TruthValue
_FdryVplsClearMac_Object = MibTableColumn
fdryVplsClearMac = _FdryVplsClearMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 3),
    _FdryVplsClearMac_Type()
)
fdryVplsClearMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsClearMac.setStatus("current")
_FdryVplsVcId_Type = Unsigned32
_FdryVplsVcId_Object = MibTableColumn
fdryVplsVcId = _FdryVplsVcId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 4),
    _FdryVplsVcId_Type()
)
fdryVplsVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsVcId.setStatus("current")
_FdryVplsEndPoint2Table_Object = MibTable
fdryVplsEndPoint2Table = _FdryVplsEndPoint2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3)
)
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Table.setStatus("current")
_FdryVplsEndPoint2Entry_Object = MibTableRow
fdryVplsEndPoint2Entry = _FdryVplsEndPoint2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1)
)
fdryVplsEndPoint2Entry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2VlanId"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTagType"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTag"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2IfIndex"),
)
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Entry.setStatus("current")
_FdryVplsEndPoint2VlanId_Type = PwVlanCfg
_FdryVplsEndPoint2VlanId_Object = MibTableColumn
fdryVplsEndPoint2VlanId = _FdryVplsEndPoint2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 1),
    _FdryVplsEndPoint2VlanId_Type()
)
fdryVplsEndPoint2VlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2VlanId.setStatus("current")


class _FdryVplsEndPoint2InnerTagType_Type(Integer32):
    """Custom type fdryVplsEndPoint2InnerTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("innerVlan", 2),
          ("invalid", 1),
          ("isid", 3))
    )


_FdryVplsEndPoint2InnerTagType_Type.__name__ = "Integer32"
_FdryVplsEndPoint2InnerTagType_Object = MibTableColumn
fdryVplsEndPoint2InnerTagType = _FdryVplsEndPoint2InnerTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 2),
    _FdryVplsEndPoint2InnerTagType_Type()
)
fdryVplsEndPoint2InnerTagType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InnerTagType.setStatus("current")
_FdryVplsEndPoint2InnerTag_Type = Unsigned32
_FdryVplsEndPoint2InnerTag_Object = MibTableColumn
fdryVplsEndPoint2InnerTag = _FdryVplsEndPoint2InnerTag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 3),
    _FdryVplsEndPoint2InnerTag_Type()
)
fdryVplsEndPoint2InnerTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InnerTag.setStatus("current")
_FdryVplsEndPoint2IfIndex_Type = InterfaceIndex
_FdryVplsEndPoint2IfIndex_Object = MibTableColumn
fdryVplsEndPoint2IfIndex = _FdryVplsEndPoint2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 4),
    _FdryVplsEndPoint2IfIndex_Type()
)
fdryVplsEndPoint2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2IfIndex.setStatus("current")
_FdryVplsEndPoint2VlanTagMode_Type = VlanTagMode
_FdryVplsEndPoint2VlanTagMode_Object = MibTableColumn
fdryVplsEndPoint2VlanTagMode = _FdryVplsEndPoint2VlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 5),
    _FdryVplsEndPoint2VlanTagMode_Type()
)
fdryVplsEndPoint2VlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2VlanTagMode.setStatus("current")
_FdryVplsEndPoint2InHCOctets_Type = Counter64
_FdryVplsEndPoint2InHCOctets_Object = MibTableColumn
fdryVplsEndPoint2InHCOctets = _FdryVplsEndPoint2InHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 6),
    _FdryVplsEndPoint2InHCOctets_Type()
)
fdryVplsEndPoint2InHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InHCOctets.setStatus("current")
_FdryVplsEndPoint2Layer2State_Type = Layer2StateTC
_FdryVplsEndPoint2Layer2State_Object = MibTableColumn
fdryVplsEndPoint2Layer2State = _FdryVplsEndPoint2Layer2State_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 7),
    _FdryVplsEndPoint2Layer2State_Type()
)
fdryVplsEndPoint2Layer2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Layer2State.setStatus("current")
_FdryVplsEndPoint2OperStatus_Type = PwOperStatusTC
_FdryVplsEndPoint2OperStatus_Object = MibTableColumn
fdryVplsEndPoint2OperStatus = _FdryVplsEndPoint2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 8),
    _FdryVplsEndPoint2OperStatus_Type()
)
fdryVplsEndPoint2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2OperStatus.setStatus("current")
_FdryVplsEndPoint2RowStatus_Type = RowStatus
_FdryVplsEndPoint2RowStatus_Object = MibTableColumn
fdryVplsEndPoint2RowStatus = _FdryVplsEndPoint2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 9),
    _FdryVplsEndPoint2RowStatus_Type()
)
fdryVplsEndPoint2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2RowStatus.setStatus("current")
_BrcdVplsEndptVlanExtStatsTable_Object = MibTable
brcdVplsEndptVlanExtStatsTable = _BrcdVplsEndptVlanExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4)
)
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsTable.setStatus("current")
_BrcdVplsEndptVlanExtStatsEntry_Object = MibTableRow
brcdVplsEndptVlanExtStatsEntry = _BrcdVplsEndptVlanExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1)
)
brcdVplsEndptVlanExtStatsEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2VlanId"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTagType"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTag"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2IfIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "brcdVplsEndptVlanExtStatsPriorityId"),
)
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsEntry.setStatus("current")
_BrcdVplsEndptVlanExtStatsPriorityId_Type = PortPriorityTC
_BrcdVplsEndptVlanExtStatsPriorityId_Object = MibTableColumn
brcdVplsEndptVlanExtStatsPriorityId = _BrcdVplsEndptVlanExtStatsPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 1),
    _BrcdVplsEndptVlanExtStatsPriorityId_Type()
)
brcdVplsEndptVlanExtStatsPriorityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsPriorityId.setStatus("current")
_BrcdVplsEndptVlanExtStatsInPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsInPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsInPkts = _BrcdVplsEndptVlanExtStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 2),
    _BrcdVplsEndptVlanExtStatsInPkts_Type()
)
brcdVplsEndptVlanExtStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsInPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsOutPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsOutPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsOutPkts = _BrcdVplsEndptVlanExtStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 3),
    _BrcdVplsEndptVlanExtStatsOutPkts_Type()
)
brcdVplsEndptVlanExtStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsOutPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsInOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsInOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsInOctets = _BrcdVplsEndptVlanExtStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 4),
    _BrcdVplsEndptVlanExtStatsInOctets_Type()
)
brcdVplsEndptVlanExtStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsInOctets.setStatus("current")
_BrcdVplsEndptVlanExtStatsOutOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsOutOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsOutOctets = _BrcdVplsEndptVlanExtStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 5),
    _BrcdVplsEndptVlanExtStatsOutOctets_Type()
)
brcdVplsEndptVlanExtStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsOutOctets.setStatus("current")
_BrcdVplsEndptVlanExtStatsRoutedInPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsRoutedInPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsRoutedInPkts = _BrcdVplsEndptVlanExtStatsRoutedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 6),
    _BrcdVplsEndptVlanExtStatsRoutedInPkts_Type()
)
brcdVplsEndptVlanExtStatsRoutedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsRoutedInPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsRoutedOutPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsRoutedOutPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsRoutedOutPkts = _BrcdVplsEndptVlanExtStatsRoutedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 7),
    _BrcdVplsEndptVlanExtStatsRoutedOutPkts_Type()
)
brcdVplsEndptVlanExtStatsRoutedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsRoutedOutPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsRoutedInOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsRoutedInOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsRoutedInOctets = _BrcdVplsEndptVlanExtStatsRoutedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 8),
    _BrcdVplsEndptVlanExtStatsRoutedInOctets_Type()
)
brcdVplsEndptVlanExtStatsRoutedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsRoutedInOctets.setStatus("current")
_BrcdVplsEndptVlanExtStatsRoutedOutOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsRoutedOutOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsRoutedOutOctets = _BrcdVplsEndptVlanExtStatsRoutedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 9),
    _BrcdVplsEndptVlanExtStatsRoutedOutOctets_Type()
)
brcdVplsEndptVlanExtStatsRoutedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsRoutedOutOctets.setStatus("current")
_BrcdVplsEndptVlanExtStatsSwitchedInPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsSwitchedInPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsSwitchedInPkts = _BrcdVplsEndptVlanExtStatsSwitchedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 10),
    _BrcdVplsEndptVlanExtStatsSwitchedInPkts_Type()
)
brcdVplsEndptVlanExtStatsSwitchedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsSwitchedInPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsSwitchedOutPkts_Type = Counter64
_BrcdVplsEndptVlanExtStatsSwitchedOutPkts_Object = MibTableColumn
brcdVplsEndptVlanExtStatsSwitchedOutPkts = _BrcdVplsEndptVlanExtStatsSwitchedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 11),
    _BrcdVplsEndptVlanExtStatsSwitchedOutPkts_Type()
)
brcdVplsEndptVlanExtStatsSwitchedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsSwitchedOutPkts.setStatus("current")
_BrcdVplsEndptVlanExtStatsSwitchedInOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsSwitchedInOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsSwitchedInOctets = _BrcdVplsEndptVlanExtStatsSwitchedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 12),
    _BrcdVplsEndptVlanExtStatsSwitchedInOctets_Type()
)
brcdVplsEndptVlanExtStatsSwitchedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsSwitchedInOctets.setStatus("current")
_BrcdVplsEndptVlanExtStatsSwitchedOutOctets_Type = Counter64
_BrcdVplsEndptVlanExtStatsSwitchedOutOctets_Object = MibTableColumn
brcdVplsEndptVlanExtStatsSwitchedOutOctets = _BrcdVplsEndptVlanExtStatsSwitchedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 13),
    _BrcdVplsEndptVlanExtStatsSwitchedOutOctets_Type()
)
brcdVplsEndptVlanExtStatsSwitchedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVplsEndptVlanExtStatsSwitchedOutOctets.setStatus("current")
_BrcdVplsScalarObjects_ObjectIdentity = ObjectIdentity
brcdVplsScalarObjects = _BrcdVplsScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5)
)
_BrcdVplsMacAgeTimeLocal_Type = Unsigned32
_BrcdVplsMacAgeTimeLocal_Object = MibScalar
brcdVplsMacAgeTimeLocal = _BrcdVplsMacAgeTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5, 1),
    _BrcdVplsMacAgeTimeLocal_Type()
)
brcdVplsMacAgeTimeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdVplsMacAgeTimeLocal.setStatus("current")
if mibBuilder.loadTexts:
    brcdVplsMacAgeTimeLocal.setUnits("seconds")
_BrcdVplsMacAgeTimeRemote_Type = Unsigned32
_BrcdVplsMacAgeTimeRemote_Object = MibScalar
brcdVplsMacAgeTimeRemote = _BrcdVplsMacAgeTimeRemote_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5, 2),
    _BrcdVplsMacAgeTimeRemote_Type()
)
brcdVplsMacAgeTimeRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdVplsMacAgeTimeRemote.setStatus("current")
if mibBuilder.loadTexts:
    brcdVplsMacAgeTimeRemote.setUnits("seconds")
vplsConfigEntry.registerAugmentions(
    ("FDRY-MPLS-L2VPN-MIB",
     "fdryVplsEntry")
)
fdryVplsEntry.setIndexNames(*vplsConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fdryVplsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 1)
)
fdryVplsCreated.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigName"),
        ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
)
if mibBuilder.loadTexts:
    fdryVplsCreated.setStatus(
        "current"
    )

fdryVplsDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 2)
)
fdryVplsDeleted.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigName"),
        ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
)
if mibBuilder.loadTexts:
    fdryVplsDeleted.setStatus(
        "current"
    )

fdryPwCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 3)
)
fdryPwCreated.setObjects(
      *(("FDRY-MPLS-L2VPN-MIB", "fdryPwServiceType"),
        ("PW-STD-MIB", "pwName"),
        ("PW-STD-MIB", "pwID"))
)
if mibBuilder.loadTexts:
    fdryPwCreated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-MPLS-L2VPN-MIB",
    **{"MplsServiceType": MplsServiceType,
       "AdminStatus": AdminStatus,
       "ClassOfService": ClassOfService,
       "Layer2StateTC": Layer2StateTC,
       "FdryPwServiceType": FdryPwServiceType,
       "PwVlanCfg": PwVlanCfg,
       "fdryMplsL2VpnMIB": fdryMplsL2VpnMIB,
       "fdryMplsVpnNotifications": fdryMplsVpnNotifications,
       "fdryVplsCreated": fdryVplsCreated,
       "fdryVplsDeleted": fdryVplsDeleted,
       "fdryPwCreated": fdryPwCreated,
       "fdryMplsVllInfo": fdryMplsVllInfo,
       "fdryVllEndPointTable": fdryVllEndPointTable,
       "fdryVllEndPointEntry": fdryVllEndPointEntry,
       "fdryVllEndPointServiceType": fdryVllEndPointServiceType,
       "fdryVllEndPointVlanTagMode": fdryVllEndPointVlanTagMode,
       "fdryVllEndPointClassOfService": fdryVllEndPointClassOfService,
       "fdryVllEndPointInHCPkts": fdryVllEndPointInHCPkts,
       "fdryVllEndPointOutHCPkts": fdryVllEndPointOutHCPkts,
       "fdryVllEndPointAdminStatus": fdryVllEndPointAdminStatus,
       "fdryVllEndPointOperStatus": fdryVllEndPointOperStatus,
       "fdryVllEndPointRowStatus": fdryVllEndPointRowStatus,
       "fdryVllEndPointInnerVlanId": fdryVllEndPointInnerVlanId,
       "fdryVllEndPointInHCOctets": fdryVllEndPointInHCOctets,
       "fdryVllEndPointOutHCOctets": fdryVllEndPointOutHCOctets,
       "brcdVllEndptVlanExtStatsTable": brcdVllEndptVlanExtStatsTable,
       "brcdVllEndptVlanExtStatsEntry": brcdVllEndptVlanExtStatsEntry,
       "brcdVllEndptVlanExtStatsPriorityId": brcdVllEndptVlanExtStatsPriorityId,
       "brcdVllEndptVlanExtStatsInPkts": brcdVllEndptVlanExtStatsInPkts,
       "brcdVllEndptVlanExtStatsOutPkts": brcdVllEndptVlanExtStatsOutPkts,
       "brcdVllEndptVlanExtStatsInOctets": brcdVllEndptVlanExtStatsInOctets,
       "brcdVllEndptVlanExtStatsOutOctets": brcdVllEndptVlanExtStatsOutOctets,
       "fdryMplsVplsInfo": fdryMplsVplsInfo,
       "fdryVplsEndPointTable": fdryVplsEndPointTable,
       "fdryVplsEndPointEntry": fdryVplsEndPointEntry,
       "fdryVplsEndPointPortVlan": fdryVplsEndPointPortVlan,
       "fdryVplsEndPointIfIndex": fdryVplsEndPointIfIndex,
       "fdryVplsEndPointVlanTagMode": fdryVplsEndPointVlanTagMode,
       "fdryVplsEndPointOutHCPkts": fdryVplsEndPointOutHCPkts,
       "fdryVplsEndPointState": fdryVplsEndPointState,
       "fdryVplsEndPointAdminStatus": fdryVplsEndPointAdminStatus,
       "fdryVplsEndPointOperStatus": fdryVplsEndPointOperStatus,
       "fdryVplsEndPointRowStatus": fdryVplsEndPointRowStatus,
       "fdryVplsEndPointInHCOctets": fdryVplsEndPointInHCOctets,
       "fdryVplsTable": fdryVplsTable,
       "fdryVplsEntry": fdryVplsEntry,
       "fdryVplsClassOfService": fdryVplsClassOfService,
       "fdryVplsMaxMacLearned": fdryVplsMaxMacLearned,
       "fdryVplsClearMac": fdryVplsClearMac,
       "fdryVplsVcId": fdryVplsVcId,
       "fdryVplsEndPoint2Table": fdryVplsEndPoint2Table,
       "fdryVplsEndPoint2Entry": fdryVplsEndPoint2Entry,
       "fdryVplsEndPoint2VlanId": fdryVplsEndPoint2VlanId,
       "fdryVplsEndPoint2InnerTagType": fdryVplsEndPoint2InnerTagType,
       "fdryVplsEndPoint2InnerTag": fdryVplsEndPoint2InnerTag,
       "fdryVplsEndPoint2IfIndex": fdryVplsEndPoint2IfIndex,
       "fdryVplsEndPoint2VlanTagMode": fdryVplsEndPoint2VlanTagMode,
       "fdryVplsEndPoint2InHCOctets": fdryVplsEndPoint2InHCOctets,
       "fdryVplsEndPoint2Layer2State": fdryVplsEndPoint2Layer2State,
       "fdryVplsEndPoint2OperStatus": fdryVplsEndPoint2OperStatus,
       "fdryVplsEndPoint2RowStatus": fdryVplsEndPoint2RowStatus,
       "brcdVplsEndptVlanExtStatsTable": brcdVplsEndptVlanExtStatsTable,
       "brcdVplsEndptVlanExtStatsEntry": brcdVplsEndptVlanExtStatsEntry,
       "brcdVplsEndptVlanExtStatsPriorityId": brcdVplsEndptVlanExtStatsPriorityId,
       "brcdVplsEndptVlanExtStatsInPkts": brcdVplsEndptVlanExtStatsInPkts,
       "brcdVplsEndptVlanExtStatsOutPkts": brcdVplsEndptVlanExtStatsOutPkts,
       "brcdVplsEndptVlanExtStatsInOctets": brcdVplsEndptVlanExtStatsInOctets,
       "brcdVplsEndptVlanExtStatsOutOctets": brcdVplsEndptVlanExtStatsOutOctets,
       "brcdVplsEndptVlanExtStatsRoutedInPkts": brcdVplsEndptVlanExtStatsRoutedInPkts,
       "brcdVplsEndptVlanExtStatsRoutedOutPkts": brcdVplsEndptVlanExtStatsRoutedOutPkts,
       "brcdVplsEndptVlanExtStatsRoutedInOctets": brcdVplsEndptVlanExtStatsRoutedInOctets,
       "brcdVplsEndptVlanExtStatsRoutedOutOctets": brcdVplsEndptVlanExtStatsRoutedOutOctets,
       "brcdVplsEndptVlanExtStatsSwitchedInPkts": brcdVplsEndptVlanExtStatsSwitchedInPkts,
       "brcdVplsEndptVlanExtStatsSwitchedOutPkts": brcdVplsEndptVlanExtStatsSwitchedOutPkts,
       "brcdVplsEndptVlanExtStatsSwitchedInOctets": brcdVplsEndptVlanExtStatsSwitchedInOctets,
       "brcdVplsEndptVlanExtStatsSwitchedOutOctets": brcdVplsEndptVlanExtStatsSwitchedOutOctets,
       "brcdVplsScalarObjects": brcdVplsScalarObjects,
       "brcdVplsMacAgeTimeLocal": brcdVplsMacAgeTimeLocal,
       "brcdVplsMacAgeTimeRemote": brcdVplsMacAgeTimeRemote}
)
