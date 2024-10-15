# SNMP MIB module (FD-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:29 2024
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

(epon,) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "epon")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

coreSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SniPortList(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ge1", 1),
          ("ge2", 2),
          ("ge3", 3),
          ("ge4", 4),
          ("ge5", 5),
          ("ge6", 6),
          ("ge7", 7),
          ("ge8", 8))
    )



class SwPortList(Integer32, TextualConvention):
    status = "current"
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ge1", 1),
          ("ge10", 10),
          ("ge11", 11),
          ("ge12", 12),
          ("ge13", 13),
          ("ge14", 14),
          ("ge15", 15),
          ("ge16", 16),
          ("ge2", 2),
          ("ge3", 3),
          ("ge4", 4),
          ("ge5", 5),
          ("ge6", 6),
          ("ge7", 7),
          ("ge8", 8),
          ("ge9", 9))
    )



class OperSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )



class PortList(OctetString, TextualConvention):
    status = "current"


class DeviceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 5),
          ("normal", 4),
          ("notPresent", 1),
          ("offline", 2),
          ("online", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SwitchConfig_ObjectIdentity = ObjectIdentity
switchConfig = _SwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 1)
)


class _SwitchMode_Type(Integer32):
    """Custom type switchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("sniDestinated", 1),
          ("transparent", 2))
    )


_SwitchMode_Type.__name__ = "Integer32"
_SwitchMode_Object = MibScalar
switchMode = _SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 1, 1),
    _SwitchMode_Type()
)
switchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchMode.setStatus("current")
_DestinedSNIPort_Type = SniPortList
_DestinedSNIPort_Object = MibScalar
destinedSNIPort = _DestinedSNIPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 1, 2),
    _DestinedSNIPort_Type()
)
destinedSNIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinedSNIPort.setStatus("current")
_InBandInterface_ObjectIdentity = ObjectIdentity
inBandInterface = _InBandInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2)
)
_NetInterfaceTable_Object = MibTable
netInterfaceTable = _NetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    netInterfaceTable.setStatus("current")
_NetInterfaceEntry_Object = MibTableRow
netInterfaceEntry = _NetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1)
)
netInterfaceEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    netInterfaceEntry.setStatus("current")


class _IfIndex_Type(Integer32):
    """Custom type ifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IfIndex_Type.__name__ = "Integer32"
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 2),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
_IfIpAddr_Type = IpAddress
_IfIpAddr_Object = MibTableColumn
ifIpAddr = _IfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 3),
    _IfIpAddr_Type()
)
ifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddr.setStatus("current")
_IfNetMask_Type = IpAddress
_IfNetMask_Object = MibTableColumn
ifNetMask = _IfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 4),
    _IfNetMask_Type()
)
ifNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifNetMask.setStatus("current")
_IfDefautGateway_Type = IpAddress
_IfDefautGateway_Object = MibTableColumn
ifDefautGateway = _IfDefautGateway_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 5),
    _IfDefautGateway_Type()
)
ifDefautGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifDefautGateway.setStatus("current")


class _IfVlan_Type(Integer32):
    """Custom type ifVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IfVlan_Type.__name__ = "Integer32"
_IfVlan_Object = MibTableColumn
ifVlan = _IfVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 6),
    _IfVlan_Type()
)
ifVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifVlan.setStatus("current")


class _IfShutDown_Type(Integer32):
    """Custom type ifShutDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("shutdown", 2))
    )


_IfShutDown_Type.__name__ = "Integer32"
_IfShutDown_Object = MibTableColumn
ifShutDown = _IfShutDown_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 7),
    _IfShutDown_Type()
)
ifShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifShutDown.setStatus("current")


class _IfStatus_Type(Integer32):
    """Custom type ifStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_IfStatus_Type.__name__ = "Integer32"
_IfStatus_Object = MibTableColumn
ifStatus = _IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 2, 1, 1, 8),
    _IfStatus_Type()
)
ifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStatus.setStatus("current")
_SwitchPort_ObjectIdentity = ObjectIdentity
switchPort = _SwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3)
)
_SwPortStatusTable_Object = MibTable
swPortStatusTable = _SwPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swPortStatusTable.setStatus("current")
_SwPortStatusEntry_Object = MibTableRow
swPortStatusEntry = _SwPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1)
)
swPortStatusEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
)
if mibBuilder.loadTexts:
    swPortStatusEntry.setStatus("current")
_SwSniPortId_Type = SniPortList
_SwSniPortId_Object = MibTableColumn
swSniPortId = _SwSniPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 1),
    _SwSniPortId_Type()
)
swSniPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSniPortId.setStatus("current")


class _SfpPlugStauts_Type(Integer32):
    """Custom type sfpPlugStauts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plugIn", 1),
          ("plugOut", 2))
    )


_SfpPlugStauts_Type.__name__ = "Integer32"
_SfpPlugStauts_Object = MibTableColumn
sfpPlugStauts = _SfpPlugStauts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 2),
    _SfpPlugStauts_Type()
)
sfpPlugStauts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPlugStauts.setStatus("current")
_TrsPower_Type = Integer32
_TrsPower_Object = MibTableColumn
trsPower = _TrsPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 3),
    _TrsPower_Type()
)
trsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trsPower.setStatus("current")
_ResPower_Type = Integer32
_ResPower_Object = MibTableColumn
resPower = _ResPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 4),
    _ResPower_Type()
)
resPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resPower.setStatus("current")


class _SwPortLinkState_Type(Integer32):
    """Custom type swPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_SwPortLinkState_Type.__name__ = "Integer32"
_SwPortLinkState_Object = MibTableColumn
swPortLinkState = _SwPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 5),
    _SwPortLinkState_Type()
)
swPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortLinkState.setStatus("current")


class _SwPortProtStatus_Type(Integer32):
    """Custom type swPortProtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_SwPortProtStatus_Type.__name__ = "Integer32"
_SwPortProtStatus_Object = MibTableColumn
swPortProtStatus = _SwPortProtStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 6),
    _SwPortProtStatus_Type()
)
swPortProtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortProtStatus.setStatus("current")


class _SwPortWorkSpd_Type(Integer32):
    """Custom type swPortWorkSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 1),
          ("mbps100", 2),
          ("mbps1G", 3))
    )


_SwPortWorkSpd_Type.__name__ = "Integer32"
_SwPortWorkSpd_Object = MibTableColumn
swPortWorkSpd = _SwPortWorkSpd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 7),
    _SwPortWorkSpd_Type()
)
swPortWorkSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortWorkSpd.setStatus("current")


class _SwPortWorkDup_Type(Integer32):
    """Custom type swPortWorkDup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDup", 1),
          ("halfDup", 2))
    )


_SwPortWorkDup_Type.__name__ = "Integer32"
_SwPortWorkDup_Object = MibTableColumn
swPortWorkDup = _SwPortWorkDup_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 8),
    _SwPortWorkDup_Type()
)
swPortWorkDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortWorkDup.setStatus("current")


class _SwPortWorkFlowCtr_Type(Integer32):
    """Custom type swPortWorkFlowCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SwPortWorkFlowCtr_Type.__name__ = "Integer32"
_SwPortWorkFlowCtr_Object = MibTableColumn
swPortWorkFlowCtr = _SwPortWorkFlowCtr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 1, 1, 9),
    _SwPortWorkFlowCtr_Type()
)
swPortWorkFlowCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortWorkFlowCtr.setStatus("current")
_SwPortCfgTable_Object = MibTable
swPortCfgTable = _SwPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swPortCfgTable.setStatus("current")
_SwPortCfgEntry_Object = MibTableRow
swPortCfgEntry = _SwPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1)
)
swPortCfgEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swPortId"),
)
if mibBuilder.loadTexts:
    swPortCfgEntry.setStatus("current")
_SwPortId_Type = SwPortList
_SwPortId_Object = MibTableColumn
swPortId = _SwPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 2),
    _SwPortId_Type()
)
swPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortId.setStatus("current")


class _SfpModeCfg_Type(Integer32):
    """Custom type sfpModeCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_SfpModeCfg_Type.__name__ = "Integer32"
_SfpModeCfg_Object = MibTableColumn
sfpModeCfg = _SfpModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 3),
    _SfpModeCfg_Type()
)
sfpModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpModeCfg.setStatus("current")


class _SwPortCfgSpd_Type(Integer32):
    """Custom type swPortCfgSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 5),
          ("mbps10", 1),
          ("mbps100", 2),
          ("mbps10G", 4),
          ("mbps1G", 3))
    )


_SwPortCfgSpd_Type.__name__ = "Integer32"
_SwPortCfgSpd_Object = MibTableColumn
swPortCfgSpd = _SwPortCfgSpd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 4),
    _SwPortCfgSpd_Type()
)
swPortCfgSpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCfgSpd.setStatus("current")


class _SwPortCfgDup_Type(Integer32):
    """Custom type swPortCfgDup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_SwPortCfgDup_Type.__name__ = "Integer32"
_SwPortCfgDup_Object = MibTableColumn
swPortCfgDup = _SwPortCfgDup_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 5),
    _SwPortCfgDup_Type()
)
swPortCfgDup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCfgDup.setStatus("current")


class _SwPortRstAuto_Type(Integer32):
    """Custom type swPortRstAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_SwPortRstAuto_Type.__name__ = "Integer32"
_SwPortRstAuto_Object = MibTableColumn
swPortRstAuto = _SwPortRstAuto_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 6),
    _SwPortRstAuto_Type()
)
swPortRstAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortRstAuto.setStatus("current")


class _SwPortFlowCtl_Type(Integer32):
    """Custom type swPortFlowCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disable", 2),
          ("enable", 1))
    )


_SwPortFlowCtl_Type.__name__ = "Integer32"
_SwPortFlowCtl_Object = MibTableColumn
swPortFlowCtl = _SwPortFlowCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 7),
    _SwPortFlowCtl_Type()
)
swPortFlowCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortFlowCtl.setStatus("current")


class _SwPortDftPri_Type(Integer32):
    """Custom type swPortDftPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwPortDftPri_Type.__name__ = "Integer32"
_SwPortDftPri_Object = MibTableColumn
swPortDftPri = _SwPortDftPri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 8),
    _SwPortDftPri_Type()
)
swPortDftPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortDftPri.setStatus("current")


class _SwPortDftVid_Type(Integer32):
    """Custom type swPortDftVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwPortDftVid_Type.__name__ = "Integer32"
_SwPortDftVid_Object = MibTableColumn
swPortDftVid = _SwPortDftVid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 9),
    _SwPortDftVid_Type()
)
swPortDftVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortDftVid.setStatus("current")


class _SwPortForceLinkDown_Type(Integer32):
    """Custom type swPortForceLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("forceDown", 1)
    )


_SwPortForceLinkDown_Type.__name__ = "Integer32"
_SwPortForceLinkDown_Object = MibTableColumn
swPortForceLinkDown = _SwPortForceLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 10),
    _SwPortForceLinkDown_Type()
)
swPortForceLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortForceLinkDown.setStatus("current")
_SwPortEnable_Type = OperSwitch
_SwPortEnable_Object = MibTableColumn
swPortEnable = _SwPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 11),
    _SwPortEnable_Type()
)
swPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortEnable.setStatus("current")
_SwPortIngressFilter_Type = OperSwitch
_SwPortIngressFilter_Object = MibTableColumn
swPortIngressFilter = _SwPortIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 12),
    _SwPortIngressFilter_Type()
)
swPortIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortIngressFilter.setStatus("current")


class _SwPortPermitFrameType_Type(Integer32):
    """Custom type swPortPermitFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allType", 2),
          ("tagged", 1),
          ("unTagged", 3))
    )


_SwPortPermitFrameType_Type.__name__ = "Integer32"
_SwPortPermitFrameType_Object = MibTableColumn
swPortPermitFrameType = _SwPortPermitFrameType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 13),
    _SwPortPermitFrameType_Type()
)
swPortPermitFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortPermitFrameType.setStatus("current")
_SwPortNestVlanEnable_Type = OperSwitch
_SwPortNestVlanEnable_Object = MibTableColumn
swPortNestVlanEnable = _SwPortNestVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 14),
    _SwPortNestVlanEnable_Type()
)
swPortNestVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortNestVlanEnable.setStatus("current")
_SwPortProtVlan_Type = OperSwitch
_SwPortProtVlan_Object = MibTableColumn
swPortProtVlan = _SwPortProtVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 15),
    _SwPortProtVlan_Type()
)
swPortProtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortProtVlan.setStatus("current")
_SwPortBroadCastRateCtl_Type = OperSwitch
_SwPortBroadCastRateCtl_Object = MibTableColumn
swPortBroadCastRateCtl = _SwPortBroadCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 16),
    _SwPortBroadCastRateCtl_Type()
)
swPortBroadCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBroadCastRateCtl.setStatus("current")
_SwPortMultiCastRateCtl_Type = OperSwitch
_SwPortMultiCastRateCtl_Object = MibTableColumn
swPortMultiCastRateCtl = _SwPortMultiCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 17),
    _SwPortMultiCastRateCtl_Type()
)
swPortMultiCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMultiCastRateCtl.setStatus("current")
_SwPortUnkUcCastRateCtl_Type = OperSwitch
_SwPortUnkUcCastRateCtl_Object = MibTableColumn
swPortUnkUcCastRateCtl = _SwPortUnkUcCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 18),
    _SwPortUnkUcCastRateCtl_Type()
)
swPortUnkUcCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortUnkUcCastRateCtl.setStatus("current")


class _SwPortBroadCastRate_Type(Integer32):
    """Custom type swPortBroadCastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwPortBroadCastRate_Type.__name__ = "Integer32"
_SwPortBroadCastRate_Object = MibTableColumn
swPortBroadCastRate = _SwPortBroadCastRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 2, 1, 19),
    _SwPortBroadCastRate_Type()
)
swPortBroadCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBroadCastRate.setStatus("current")


class _SwPortRateCtlMode_Type(Integer32):
    """Custom type swPortRateCtlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kBps", 1),
          ("kpps", 2))
    )


_SwPortRateCtlMode_Type.__name__ = "Integer32"
_SwPortRateCtlMode_Object = MibScalar
swPortRateCtlMode = _SwPortRateCtlMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 3, 3),
    _SwPortRateCtlMode_Type()
)
swPortRateCtlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortRateCtlMode.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4)
)
_ProSupportedTable_Object = MibTable
proSupportedTable = _ProSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    proSupportedTable.setStatus("current")
_ProSupportedEntry_Object = MibTableRow
proSupportedEntry = _ProSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 1, 1)
)
proSupportedEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "proSupportedId"),
)
if mibBuilder.loadTexts:
    proSupportedEntry.setStatus("current")


class _ProSupportedId_Type(Integer32):
    """Custom type proSupportedId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ProSupportedId_Type.__name__ = "Integer32"
_ProSupportedId_Object = MibTableColumn
proSupportedId = _ProSupportedId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 1, 1, 1),
    _ProSupportedId_Type()
)
proSupportedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proSupportedId.setStatus("current")


class _ProSupported_Type(Integer32):
    """Custom type proSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_ProSupported_Type.__name__ = "Integer32"
_ProSupported_Object = MibTableColumn
proSupported = _ProSupported_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 1, 1, 2),
    _ProSupported_Type()
)
proSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proSupported.setStatus("current")
_ProSupportedRowStatus_Type = RowStatus
_ProSupportedRowStatus_Object = MibTableColumn
proSupportedRowStatus = _ProSupportedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 1, 1, 3),
    _ProSupportedRowStatus_Type()
)
proSupportedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proSupportedRowStatus.setStatus("current")
_ProVlanTable_Object = MibTable
proVlanTable = _ProVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    proVlanTable.setStatus("current")
_ProVlanEntry_Object = MibTableRow
proVlanEntry = _ProVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2, 1)
)
proVlanEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swPortId"),
    (0, "FD-SWITCH-MIB", "proVlanIdx"),
)
if mibBuilder.loadTexts:
    proVlanEntry.setStatus("current")


class _ProVlanIdx_Type(Integer32):
    """Custom type proVlanIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ProVlanIdx_Type.__name__ = "Integer32"
_ProVlanIdx_Object = MibTableColumn
proVlanIdx = _ProVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2, 1, 1),
    _ProVlanIdx_Type()
)
proVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proVlanIdx.setStatus("current")


class _ProVlanProtocol_Type(Integer32):
    """Custom type proVlanProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_ProVlanProtocol_Type.__name__ = "Integer32"
_ProVlanProtocol_Object = MibTableColumn
proVlanProtocol = _ProVlanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2, 1, 2),
    _ProVlanProtocol_Type()
)
proVlanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proVlanProtocol.setStatus("current")


class _ProVlanId_Type(Integer32):
    """Custom type proVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ProVlanId_Type.__name__ = "Integer32"
_ProVlanId_Object = MibTableColumn
proVlanId = _ProVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2, 1, 3),
    _ProVlanId_Type()
)
proVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proVlanId.setStatus("current")
_ProVlanRowStatus_Type = RowStatus
_ProVlanRowStatus_Object = MibTableColumn
proVlanRowStatus = _ProVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 2, 1, 4),
    _ProVlanRowStatus_Type()
)
proVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proVlanRowStatus.setStatus("current")
_QVlanTable_Object = MibTable
qVlanTable = _QVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    qVlanTable.setStatus("current")
_QVlanEntry_Object = MibTableRow
qVlanEntry = _QVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3, 1)
)
qVlanEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "qVlanId"),
)
if mibBuilder.loadTexts:
    qVlanEntry.setStatus("current")
_QVlanId_Type = Unsigned32
_QVlanId_Object = MibTableColumn
qVlanId = _QVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3, 1, 1),
    _QVlanId_Type()
)
qVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qVlanId.setStatus("current")
_QVlanStaticEgressPorts_Type = PortList
_QVlanStaticEgressPorts_Object = MibTableColumn
qVlanStaticEgressPorts = _QVlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3, 1, 2),
    _QVlanStaticEgressPorts_Type()
)
qVlanStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qVlanStaticEgressPorts.setStatus("current")
_QVlanStaticUntaggedPorts_Type = PortList
_QVlanStaticUntaggedPorts_Object = MibTableColumn
qVlanStaticUntaggedPorts = _QVlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3, 1, 3),
    _QVlanStaticUntaggedPorts_Type()
)
qVlanStaticUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qVlanStaticUntaggedPorts.setStatus("current")
_QVlanRowStatus_Type = RowStatus
_QVlanRowStatus_Object = MibTableColumn
qVlanRowStatus = _QVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 3, 1, 4),
    _QVlanRowStatus_Type()
)
qVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qVlanRowStatus.setStatus("current")
_QVlanCfg_ObjectIdentity = ObjectIdentity
qVlanCfg = _QVlanCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 4)
)
_VlanMode_Type = OperSwitch
_VlanMode_Object = MibScalar
vlanMode = _VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 4, 4, 1),
    _VlanMode_Type()
)
vlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMode.setStatus("current")
_Trunk_ObjectIdentity = ObjectIdentity
trunk = _Trunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5)
)
_TrunkConfig_ObjectIdentity = ObjectIdentity
trunkConfig = _TrunkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 1)
)


class _TrunkBlance_Type(Integer32):
    """Custom type trunkBlance based on Integer32"""
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
        *(("balanceInL2If", 6),
          ("balanceIp", 2),
          ("balanceIpMac", 4),
          ("balanceL4Port", 3),
          ("balanceL4PortMac", 5),
          ("balanceMac", 1))
    )


_TrunkBlance_Type.__name__ = "Integer32"
_TrunkBlance_Object = MibScalar
trunkBlance = _TrunkBlance_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 1, 1),
    _TrunkBlance_Type()
)
trunkBlance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkBlance.setStatus("current")
_TrunkGroupTable_Object = MibTable
trunkGroupTable = _TrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    trunkGroupTable.setStatus("current")
_TrunkGroupEntry_Object = MibTableRow
trunkGroupEntry = _TrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 2, 1)
)
trunkGroupEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "trunkGroupId"),
)
if mibBuilder.loadTexts:
    trunkGroupEntry.setStatus("current")


class _TrunkGroupId_Type(Integer32):
    """Custom type trunkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TrunkGroupId_Type.__name__ = "Integer32"
_TrunkGroupId_Object = MibTableColumn
trunkGroupId = _TrunkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 2, 1, 1),
    _TrunkGroupId_Type()
)
trunkGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkGroupId.setStatus("current")
_TrunkGroupMembers_Type = PortList
_TrunkGroupMembers_Object = MibTableColumn
trunkGroupMembers = _TrunkGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 2, 1, 2),
    _TrunkGroupMembers_Type()
)
trunkGroupMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupMembers.setStatus("current")
_TrunkGroupRowStatus_Type = RowStatus
_TrunkGroupRowStatus_Object = MibTableColumn
trunkGroupRowStatus = _TrunkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 5, 2, 1, 3),
    _TrunkGroupRowStatus_Type()
)
trunkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupRowStatus.setStatus("current")
_Rstp_ObjectIdentity = ObjectIdentity
rstp = _Rstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6)
)
_RstpConfig_ObjectIdentity = ObjectIdentity
rstpConfig = _RstpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1)
)
_RstpEnable_Type = OperSwitch
_RstpEnable_Object = MibScalar
rstpEnable = _RstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 1),
    _RstpEnable_Type()
)
rstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpEnable.setStatus("current")


class _BridgePri_Type(Integer32):
    """Custom type bridgePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4096,
              8192,
              12288,
              16384,
              20480,
              24576,
              28672,
              32768,
              36864,
              40960,
              45056,
              49152,
              53248,
              57344,
              61440)
        )
    )
    namedValues = NamedValues(
        *(("p0", 1),
          ("p12288", 12288),
          ("p16384", 16384),
          ("p20480", 20480),
          ("p24576", 24576),
          ("p28672", 28672),
          ("p32768", 32768),
          ("p36864", 36864),
          ("p4096", 4096),
          ("p40960", 40960),
          ("p45056", 45056),
          ("p49152", 49152),
          ("p53248", 53248),
          ("p57344", 57344),
          ("p61440", 61440),
          ("p8192", 8192))
    )


_BridgePri_Type.__name__ = "Integer32"
_BridgePri_Object = MibScalar
bridgePri = _BridgePri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 2),
    _BridgePri_Type()
)
bridgePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePri.setStatus("current")


class _BridgeMaxAge_Type(Integer32):
    """Custom type bridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_BridgeMaxAge_Type.__name__ = "Integer32"
_BridgeMaxAge_Object = MibScalar
bridgeMaxAge = _BridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 3),
    _BridgeMaxAge_Type()
)
bridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMaxAge.setStatus("current")


class _BridgeForwardDelay_Type(Integer32):
    """Custom type bridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_BridgeForwardDelay_Type.__name__ = "Integer32"
_BridgeForwardDelay_Object = MibScalar
bridgeForwardDelay = _BridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 4),
    _BridgeForwardDelay_Type()
)
bridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeForwardDelay.setStatus("current")


class _TransmitHoldCount_Type(Integer32):
    """Custom type transmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TransmitHoldCount_Type.__name__ = "Integer32"
_TransmitHoldCount_Object = MibScalar
transmitHoldCount = _TransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 5),
    _TransmitHoldCount_Type()
)
transmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitHoldCount.setStatus("current")
_BridgeIdAddr_Type = MacAddress
_BridgeIdAddr_Object = MibScalar
bridgeIdAddr = _BridgeIdAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 6),
    _BridgeIdAddr_Type()
)
bridgeIdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeIdAddr.setStatus("current")
_BridgeHelloTime_Type = Integer32
_BridgeHelloTime_Object = MibScalar
bridgeHelloTime = _BridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 7),
    _BridgeHelloTime_Type()
)
bridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeHelloTime.setStatus("current")
_RootPri_Type = Integer32
_RootPri_Object = MibScalar
rootPri = _RootPri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 8),
    _RootPri_Type()
)
rootPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootPri.setStatus("current")
_RootAddr_Type = MacAddress
_RootAddr_Object = MibScalar
rootAddr = _RootAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 9),
    _RootAddr_Type()
)
rootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootAddr.setStatus("current")


class _RootPathCost_Type(Integer32):
    """Custom type rootPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_RootPathCost_Type.__name__ = "Integer32"
_RootPathCost_Object = MibScalar
rootPathCost = _RootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 1, 10),
    _RootPathCost_Type()
)
rootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootPathCost.setStatus("current")
_RstpPortTable_Object = MibTable
rstpPortTable = _RstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    rstpPortTable.setStatus("current")
_RstpPortEntry_Object = MibTableRow
rstpPortEntry = _RstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1)
)
rstpPortEntry.setIndexNames(
    (0, "FD-SWITCH-MIB", "swSniPortId"),
)
if mibBuilder.loadTexts:
    rstpPortEntry.setStatus("current")


class _RstpMode_Type(Integer32):
    """Custom type rstpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stp", 1))
    )


_RstpMode_Type.__name__ = "Integer32"
_RstpMode_Object = MibTableColumn
rstpMode = _RstpMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 1),
    _RstpMode_Type()
)
rstpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpMode.setStatus("current")


class _RstpPri_Type(Integer32):
    """Custom type rstpPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144,
              160,
              176,
              192,
              208,
              224,
              240)
        )
    )
    namedValues = NamedValues(
        *(("p0", 1),
          ("p112", 112),
          ("p128", 128),
          ("p144", 144),
          ("p16", 16),
          ("p160", 160),
          ("p176", 176),
          ("p192", 192),
          ("p208", 208),
          ("p224", 224),
          ("p240", 240),
          ("p32", 32),
          ("p48", 48),
          ("p64", 64),
          ("p80", 80),
          ("p96", 96))
    )


_RstpPri_Type.__name__ = "Integer32"
_RstpPri_Object = MibTableColumn
rstpPri = _RstpPri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 2),
    _RstpPri_Type()
)
rstpPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPri.setStatus("current")


class _RstpPathCost_Type(Integer32):
    """Custom type rstpPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_RstpPathCost_Type.__name__ = "Integer32"
_RstpPathCost_Object = MibTableColumn
rstpPathCost = _RstpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 3),
    _RstpPathCost_Type()
)
rstpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPathCost.setStatus("current")
_RstpMCheck_Type = OperSwitch
_RstpMCheck_Object = MibTableColumn
rstpMCheck = _RstpMCheck_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 4),
    _RstpMCheck_Type()
)
rstpMCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpMCheck.setStatus("current")


class _RstpEdgeConfig_Type(Integer32):
    """Custom type rstpEdgeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("edge", 2),
          ("nonEdge", 1))
    )


_RstpEdgeConfig_Type.__name__ = "Integer32"
_RstpEdgeConfig_Object = MibTableColumn
rstpEdgeConfig = _RstpEdgeConfig_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 5),
    _RstpEdgeConfig_Type()
)
rstpEdgeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpEdgeConfig.setStatus("current")


class _RstpOperEdge_Type(Integer32):
    """Custom type rstpOperEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edge", 1),
          ("nonEdge", 2))
    )


_RstpOperEdge_Type.__name__ = "Integer32"
_RstpOperEdge_Object = MibTableColumn
rstpOperEdge = _RstpOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 6),
    _RstpOperEdge_Type()
)
rstpOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpOperEdge.setStatus("current")


class _RstpP2PCfg_Type(Integer32):
    """Custom type rstpP2PCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("p2p", 2),
          ("share", 1))
    )


_RstpP2PCfg_Type.__name__ = "Integer32"
_RstpP2PCfg_Object = MibTableColumn
rstpP2PCfg = _RstpP2PCfg_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 7),
    _RstpP2PCfg_Type()
)
rstpP2PCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpP2PCfg.setStatus("current")


class _RstpOperP2P_Type(Integer32):
    """Custom type rstpOperP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 2),
          ("share", 1))
    )


_RstpOperP2P_Type.__name__ = "Integer32"
_RstpOperP2P_Object = MibTableColumn
rstpOperP2P = _RstpOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 8),
    _RstpOperP2P_Type()
)
rstpOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpOperP2P.setStatus("current")


class _RstpPortState_Type(Integer32):
    """Custom type rstpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 2),
          ("forwarding", 4),
          ("learning", 3),
          ("linkdown", 1))
    )


_RstpPortState_Type.__name__ = "Integer32"
_RstpPortState_Object = MibTableColumn
rstpPortState = _RstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 6, 2, 1, 9),
    _RstpPortState_Type()
)
rstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPortState.setStatus("current")
_Mirror_ObjectIdentity = ObjectIdentity
mirror = _Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7)
)


class _DestinationPort_Type(Integer32):
    """Custom type destinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ge1", 1),
          ("ge2", 2),
          ("ge3", 3),
          ("ge4", 4),
          ("ge5", 5),
          ("ge6", 6),
          ("ge7", 7),
          ("ge8", 8),
          ("none", 0))
    )


_DestinationPort_Type.__name__ = "Integer32"
_DestinationPort_Object = MibScalar
destinationPort = _DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7, 1),
    _DestinationPort_Type()
)
destinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationPort.setStatus("current")
_SourceIngressPorts_Type = PortList
_SourceIngressPorts_Object = MibScalar
sourceIngressPorts = _SourceIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7, 2),
    _SourceIngressPorts_Type()
)
sourceIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIngressPorts.setStatus("current")
_SourceEgressPorts_Type = PortList
_SourceEgressPorts_Object = MibScalar
sourceEgressPorts = _SourceEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7, 3),
    _SourceEgressPorts_Type()
)
sourceEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceEgressPorts.setStatus("current")


class _SourceVlan_Type(OctetString):
    """Custom type sourceVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 18),
    )


_SourceVlan_Type.__name__ = "OctetString"
_SourceVlan_Object = MibScalar
sourceVlan = _SourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7, 4),
    _SourceVlan_Type()
)
sourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceVlan.setStatus("current")


class _Operation_Type(Integer32):
    """Custom type operation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("none", 0))
    )


_Operation_Type.__name__ = "Integer32"
_Operation_Object = MibScalar
operation = _Operation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 7, 5),
    _Operation_Type()
)
operation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operation.setStatus("current")
_Igmpsnooping_ObjectIdentity = ObjectIdentity
igmpsnooping = _Igmpsnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8)
)


class _IgmpsnoopingAdmin_Type(Integer32):
    """Custom type igmpsnoopingAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IgmpsnoopingAdmin_Type.__name__ = "Integer32"
_IgmpsnoopingAdmin_Object = MibScalar
igmpsnoopingAdmin = _IgmpsnoopingAdmin_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8, 1),
    _IgmpsnoopingAdmin_Type()
)
igmpsnoopingAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnoopingAdmin.setStatus("current")


class _IgmpsnoopingRouterAgingTime_Type(Integer32):
    """Custom type igmpsnoopingRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IgmpsnoopingRouterAgingTime_Type.__name__ = "Integer32"
_IgmpsnoopingRouterAgingTime_Object = MibScalar
igmpsnoopingRouterAgingTime = _IgmpsnoopingRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8, 2),
    _IgmpsnoopingRouterAgingTime_Type()
)
igmpsnoopingRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnoopingRouterAgingTime.setStatus("current")


class _IgmpsnoopingHostAgingTime_Type(Integer32):
    """Custom type igmpsnoopingHostAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_IgmpsnoopingHostAgingTime_Type.__name__ = "Integer32"
_IgmpsnoopingHostAgingTime_Object = MibScalar
igmpsnoopingHostAgingTime = _IgmpsnoopingHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8, 3),
    _IgmpsnoopingHostAgingTime_Type()
)
igmpsnoopingHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnoopingHostAgingTime.setStatus("current")
_IgmpsnoopingVlanData_Type = OctetString
_IgmpsnoopingVlanData_Object = MibScalar
igmpsnoopingVlanData = _IgmpsnoopingVlanData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8, 4),
    _IgmpsnoopingVlanData_Type()
)
igmpsnoopingVlanData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnoopingVlanData.setStatus("current")


class _IgmpsnoopingQueryProxy_Type(Integer32):
    """Custom type igmpsnoopingQueryProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IgmpsnoopingQueryProxy_Type.__name__ = "Integer32"
_IgmpsnoopingQueryProxy_Object = MibScalar
igmpsnoopingQueryProxy = _IgmpsnoopingQueryProxy_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 8, 5),
    _IgmpsnoopingQueryProxy_Type()
)
igmpsnoopingQueryProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnoopingQueryProxy.setStatus("current")
_CoreSwitchConformance_ObjectIdentity = ObjectIdentity
coreSwitchConformance = _CoreSwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10)
)
_CoreSwitchGroups_ObjectIdentity = ObjectIdentity
coreSwitchGroups = _CoreSwitchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1)
)
_CoreSwitchCompliances_ObjectIdentity = ObjectIdentity
coreSwitchCompliances = _CoreSwitchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 2)
)

# Managed Objects groups

inbandNetIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 1)
)
inbandNetIfGroup.setObjects(
      *(("FD-SWITCH-MIB", "ifName"),
        ("FD-SWITCH-MIB", "ifIpAddr"),
        ("FD-SWITCH-MIB", "ifNetMask"),
        ("FD-SWITCH-MIB", "ifDefautGateway"),
        ("FD-SWITCH-MIB", "ifVlan"),
        ("FD-SWITCH-MIB", "ifShutDown"),
        ("FD-SWITCH-MIB", "ifStatus"))
)
if mibBuilder.loadTexts:
    inbandNetIfGroup.setStatus("current")

switchCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 2)
)
switchCfgGroup.setObjects(
      *(("FD-SWITCH-MIB", "switchMode"),
        ("FD-SWITCH-MIB", "destinedSNIPort"))
)
if mibBuilder.loadTexts:
    switchCfgGroup.setStatus("current")

swPortManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 3)
)
swPortManageGroup.setObjects(
      *(("FD-SWITCH-MIB", "sfpPlugStauts"),
        ("FD-SWITCH-MIB", "trsPower"),
        ("FD-SWITCH-MIB", "resPower"),
        ("FD-SWITCH-MIB", "swPortLinkState"),
        ("FD-SWITCH-MIB", "swPortProtStatus"),
        ("FD-SWITCH-MIB", "swPortWorkSpd"),
        ("FD-SWITCH-MIB", "swPortWorkDup"),
        ("FD-SWITCH-MIB", "swPortWorkFlowCtr"),
        ("FD-SWITCH-MIB", "sfpModeCfg"),
        ("FD-SWITCH-MIB", "swPortCfgSpd"),
        ("FD-SWITCH-MIB", "swPortCfgDup"),
        ("FD-SWITCH-MIB", "swPortRstAuto"),
        ("FD-SWITCH-MIB", "swPortFlowCtl"),
        ("FD-SWITCH-MIB", "swPortDftPri"),
        ("FD-SWITCH-MIB", "swPortDftVid"),
        ("FD-SWITCH-MIB", "swPortForceLinkDown"),
        ("FD-SWITCH-MIB", "swPortEnable"),
        ("FD-SWITCH-MIB", "swPortIngressFilter"),
        ("FD-SWITCH-MIB", "swPortPermitFrameType"),
        ("FD-SWITCH-MIB", "swPortNestVlanEnable"),
        ("FD-SWITCH-MIB", "swPortProtVlan"),
        ("FD-SWITCH-MIB", "swPortBroadCastRateCtl"),
        ("FD-SWITCH-MIB", "swPortBroadCastRate"),
        ("FD-SWITCH-MIB", "swPortMultiCastRateCtl"),
        ("FD-SWITCH-MIB", "swPortUnkUcCastRateCtl"),
        ("FD-SWITCH-MIB", "swPortRateCtlMode"))
)
if mibBuilder.loadTexts:
    swPortManageGroup.setStatus("current")

swVlanGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 4)
)
swVlanGroups.setObjects(
      *(("FD-SWITCH-MIB", "proSupportedRowStatus"),
        ("FD-SWITCH-MIB", "proVlanRowStatus"),
        ("FD-SWITCH-MIB", "proSupported"),
        ("FD-SWITCH-MIB", "proVlanProtocol"),
        ("FD-SWITCH-MIB", "proVlanId"),
        ("FD-SWITCH-MIB", "qVlanStaticEgressPorts"),
        ("FD-SWITCH-MIB", "qVlanStaticUntaggedPorts"),
        ("FD-SWITCH-MIB", "qVlanRowStatus"),
        ("FD-SWITCH-MIB", "vlanMode"))
)
if mibBuilder.loadTexts:
    swVlanGroups.setStatus("current")

swTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 5)
)
swTrunkGroup.setObjects(
      *(("FD-SWITCH-MIB", "trunkBlance"),
        ("FD-SWITCH-MIB", "trunkGroupMembers"),
        ("FD-SWITCH-MIB", "trunkGroupRowStatus"))
)
if mibBuilder.loadTexts:
    swTrunkGroup.setStatus("current")

swRstpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 6)
)
swRstpGroup.setObjects(
      *(("FD-SWITCH-MIB", "rstpEnable"),
        ("FD-SWITCH-MIB", "bridgePri"),
        ("FD-SWITCH-MIB", "bridgeMaxAge"),
        ("FD-SWITCH-MIB", "bridgeForwardDelay"),
        ("FD-SWITCH-MIB", "transmitHoldCount"),
        ("FD-SWITCH-MIB", "bridgeIdAddr"),
        ("FD-SWITCH-MIB", "bridgeHelloTime"),
        ("FD-SWITCH-MIB", "rootPri"),
        ("FD-SWITCH-MIB", "rootAddr"),
        ("FD-SWITCH-MIB", "rootPathCost"),
        ("FD-SWITCH-MIB", "rstpMode"),
        ("FD-SWITCH-MIB", "rstpPri"),
        ("FD-SWITCH-MIB", "rstpPathCost"),
        ("FD-SWITCH-MIB", "rstpMCheck"),
        ("FD-SWITCH-MIB", "rstpEdgeConfig"),
        ("FD-SWITCH-MIB", "rstpOperEdge"),
        ("FD-SWITCH-MIB", "rstpP2PCfg"),
        ("FD-SWITCH-MIB", "rstpOperP2P"),
        ("FD-SWITCH-MIB", "rstpPortState"))
)
if mibBuilder.loadTexts:
    swRstpGroup.setStatus("current")

mirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 1, 7)
)
mirrorGroup.setObjects(
      *(("FD-SWITCH-MIB", "destinationPort"),
        ("FD-SWITCH-MIB", "sourceIngressPorts"),
        ("FD-SWITCH-MIB", "sourceEgressPorts"),
        ("FD-SWITCH-MIB", "sourceVlan"),
        ("FD-SWITCH-MIB", "operation"))
)
if mibBuilder.loadTexts:
    mirrorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    coreSwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-SWITCH-MIB",
    **{"SniPortList": SniPortList,
       "SwPortList": SwPortList,
       "OperSwitch": OperSwitch,
       "PortList": PortList,
       "DeviceStatus": DeviceStatus,
       "coreSwitch": coreSwitch,
       "switchConfig": switchConfig,
       "switchMode": switchMode,
       "destinedSNIPort": destinedSNIPort,
       "inBandInterface": inBandInterface,
       "netInterfaceTable": netInterfaceTable,
       "netInterfaceEntry": netInterfaceEntry,
       "ifIndex": ifIndex,
       "ifName": ifName,
       "ifIpAddr": ifIpAddr,
       "ifNetMask": ifNetMask,
       "ifDefautGateway": ifDefautGateway,
       "ifVlan": ifVlan,
       "ifShutDown": ifShutDown,
       "ifStatus": ifStatus,
       "switchPort": switchPort,
       "swPortStatusTable": swPortStatusTable,
       "swPortStatusEntry": swPortStatusEntry,
       "swSniPortId": swSniPortId,
       "sfpPlugStauts": sfpPlugStauts,
       "trsPower": trsPower,
       "resPower": resPower,
       "swPortLinkState": swPortLinkState,
       "swPortProtStatus": swPortProtStatus,
       "swPortWorkSpd": swPortWorkSpd,
       "swPortWorkDup": swPortWorkDup,
       "swPortWorkFlowCtr": swPortWorkFlowCtr,
       "swPortCfgTable": swPortCfgTable,
       "swPortCfgEntry": swPortCfgEntry,
       "swPortId": swPortId,
       "sfpModeCfg": sfpModeCfg,
       "swPortCfgSpd": swPortCfgSpd,
       "swPortCfgDup": swPortCfgDup,
       "swPortRstAuto": swPortRstAuto,
       "swPortFlowCtl": swPortFlowCtl,
       "swPortDftPri": swPortDftPri,
       "swPortDftVid": swPortDftVid,
       "swPortForceLinkDown": swPortForceLinkDown,
       "swPortEnable": swPortEnable,
       "swPortIngressFilter": swPortIngressFilter,
       "swPortPermitFrameType": swPortPermitFrameType,
       "swPortNestVlanEnable": swPortNestVlanEnable,
       "swPortProtVlan": swPortProtVlan,
       "swPortBroadCastRateCtl": swPortBroadCastRateCtl,
       "swPortMultiCastRateCtl": swPortMultiCastRateCtl,
       "swPortUnkUcCastRateCtl": swPortUnkUcCastRateCtl,
       "swPortBroadCastRate": swPortBroadCastRate,
       "swPortRateCtlMode": swPortRateCtlMode,
       "vlan": vlan,
       "proSupportedTable": proSupportedTable,
       "proSupportedEntry": proSupportedEntry,
       "proSupportedId": proSupportedId,
       "proSupported": proSupported,
       "proSupportedRowStatus": proSupportedRowStatus,
       "proVlanTable": proVlanTable,
       "proVlanEntry": proVlanEntry,
       "proVlanIdx": proVlanIdx,
       "proVlanProtocol": proVlanProtocol,
       "proVlanId": proVlanId,
       "proVlanRowStatus": proVlanRowStatus,
       "qVlanTable": qVlanTable,
       "qVlanEntry": qVlanEntry,
       "qVlanId": qVlanId,
       "qVlanStaticEgressPorts": qVlanStaticEgressPorts,
       "qVlanStaticUntaggedPorts": qVlanStaticUntaggedPorts,
       "qVlanRowStatus": qVlanRowStatus,
       "qVlanCfg": qVlanCfg,
       "vlanMode": vlanMode,
       "trunk": trunk,
       "trunkConfig": trunkConfig,
       "trunkBlance": trunkBlance,
       "trunkGroupTable": trunkGroupTable,
       "trunkGroupEntry": trunkGroupEntry,
       "trunkGroupId": trunkGroupId,
       "trunkGroupMembers": trunkGroupMembers,
       "trunkGroupRowStatus": trunkGroupRowStatus,
       "rstp": rstp,
       "rstpConfig": rstpConfig,
       "rstpEnable": rstpEnable,
       "bridgePri": bridgePri,
       "bridgeMaxAge": bridgeMaxAge,
       "bridgeForwardDelay": bridgeForwardDelay,
       "transmitHoldCount": transmitHoldCount,
       "bridgeIdAddr": bridgeIdAddr,
       "bridgeHelloTime": bridgeHelloTime,
       "rootPri": rootPri,
       "rootAddr": rootAddr,
       "rootPathCost": rootPathCost,
       "rstpPortTable": rstpPortTable,
       "rstpPortEntry": rstpPortEntry,
       "rstpMode": rstpMode,
       "rstpPri": rstpPri,
       "rstpPathCost": rstpPathCost,
       "rstpMCheck": rstpMCheck,
       "rstpEdgeConfig": rstpEdgeConfig,
       "rstpOperEdge": rstpOperEdge,
       "rstpP2PCfg": rstpP2PCfg,
       "rstpOperP2P": rstpOperP2P,
       "rstpPortState": rstpPortState,
       "mirror": mirror,
       "destinationPort": destinationPort,
       "sourceIngressPorts": sourceIngressPorts,
       "sourceEgressPorts": sourceEgressPorts,
       "sourceVlan": sourceVlan,
       "operation": operation,
       "igmpsnooping": igmpsnooping,
       "igmpsnoopingAdmin": igmpsnoopingAdmin,
       "igmpsnoopingRouterAgingTime": igmpsnoopingRouterAgingTime,
       "igmpsnoopingHostAgingTime": igmpsnoopingHostAgingTime,
       "igmpsnoopingVlanData": igmpsnoopingVlanData,
       "igmpsnoopingQueryProxy": igmpsnoopingQueryProxy,
       "coreSwitchConformance": coreSwitchConformance,
       "coreSwitchGroups": coreSwitchGroups,
       "inbandNetIfGroup": inbandNetIfGroup,
       "switchCfgGroup": switchCfgGroup,
       "swPortManageGroup": swPortManageGroup,
       "swVlanGroups": swVlanGroups,
       "swTrunkGroup": swTrunkGroup,
       "swRstpGroup": swRstpGroup,
       "mirrorGroup": mirrorGroup,
       "coreSwitchCompliances": coreSwitchCompliances,
       "coreSwitchCompliance": coreSwitchCompliance}
)
