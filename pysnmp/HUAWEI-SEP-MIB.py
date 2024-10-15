# SNMP MIB module (HUAWEI-SEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SEP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:53 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(Integer32,
 InterfaceIndex,
 ModuleIdentity,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Unsigned32,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "Integer32",
    "InterfaceIndex",
    "ModuleIdentity",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Unsigned32",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwSepMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSepObjects_ObjectIdentity = ObjectIdentity
hwSepObjects = _HwSepObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1)
)


class _HwSepResetPktCnt_Type(Integer32):
    """Custom type hwSepResetPktCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwSepResetPktCnt_Type.__name__ = "Integer32"
_HwSepResetPktCnt_Object = MibScalar
hwSepResetPktCnt = _HwSepResetPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 1),
    _HwSepResetPktCnt_Type()
)
hwSepResetPktCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSepResetPktCnt.setStatus("current")
_HwSepSegmentTable_Object = MibTable
hwSepSegmentTable = _HwSepSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2)
)
if mibBuilder.loadTexts:
    hwSepSegmentTable.setStatus("current")
_HwSepSegmentEntry_Object = MibTableRow
hwSepSegmentEntry = _HwSepSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1)
)
hwSepSegmentEntry.setIndexNames(
    (0, "HUAWEI-SEP-MIB", "hwSepSegmentId"),
)
if mibBuilder.loadTexts:
    hwSepSegmentEntry.setStatus("current")


class _HwSepSegmentId_Type(Integer32):
    """Custom type hwSepSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwSepSegmentId_Type.__name__ = "Integer32"
_HwSepSegmentId_Object = MibTableColumn
hwSepSegmentId = _HwSepSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 1),
    _HwSepSegmentId_Type()
)
hwSepSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepSegmentId.setStatus("current")


class _HwSepControlVlanId_Type(Integer32):
    """Custom type hwSepControlVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwSepControlVlanId_Type.__name__ = "Integer32"
_HwSepControlVlanId_Object = MibTableColumn
hwSepControlVlanId = _HwSepControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 2),
    _HwSepControlVlanId_Type()
)
hwSepControlVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepControlVlanId.setStatus("current")


class _HwSepPreemptManual_Type(Integer32):
    """Custom type hwSepPreemptManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSepPreemptManual_Type.__name__ = "Integer32"
_HwSepPreemptManual_Object = MibTableColumn
hwSepPreemptManual = _HwSepPreemptManual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 3),
    _HwSepPreemptManual_Type()
)
hwSepPreemptManual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepPreemptManual.setStatus("current")


class _HwSepPreemptDelay_Type(Integer32):
    """Custom type hwSepPreemptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 600),
    )


_HwSepPreemptDelay_Type.__name__ = "Integer32"
_HwSepPreemptDelay_Object = MibTableColumn
hwSepPreemptDelay = _HwSepPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 4),
    _HwSepPreemptDelay_Type()
)
hwSepPreemptDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepPreemptDelay.setStatus("current")


class _HwSepBlockPortMode_Type(Integer32):
    """Custom type hwSepBlockPortMode based on Integer32"""
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
        *(("hop", 3),
          ("middle", 2),
          ("name", 4),
          ("null", 5),
          ("optimal", 1))
    )


_HwSepBlockPortMode_Type.__name__ = "Integer32"
_HwSepBlockPortMode_Object = MibTableColumn
hwSepBlockPortMode = _HwSepBlockPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 5),
    _HwSepBlockPortMode_Type()
)
hwSepBlockPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepBlockPortMode.setStatus("current")


class _HwSepBlockPortHop_Type(Integer32):
    """Custom type hwSepBlockPortHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 512),
    )


_HwSepBlockPortHop_Type.__name__ = "Integer32"
_HwSepBlockPortHop_Object = MibTableColumn
hwSepBlockPortHop = _HwSepBlockPortHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 6),
    _HwSepBlockPortHop_Type()
)
hwSepBlockPortHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepBlockPortHop.setStatus("current")


class _HwSepBlockPortSysname_Type(OctetString):
    """Custom type hwSepBlockPortSysname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwSepBlockPortSysname_Type.__name__ = "OctetString"
_HwSepBlockPortSysname_Object = MibTableColumn
hwSepBlockPortSysname = _HwSepBlockPortSysname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 7),
    _HwSepBlockPortSysname_Type()
)
hwSepBlockPortSysname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepBlockPortSysname.setStatus("current")


class _HwSepBlockPortIfname_Type(OctetString):
    """Custom type hwSepBlockPortIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSepBlockPortIfname_Type.__name__ = "OctetString"
_HwSepBlockPortIfname_Object = MibTableColumn
hwSepBlockPortIfname = _HwSepBlockPortIfname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 8),
    _HwSepBlockPortIfname_Type()
)
hwSepBlockPortIfname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepBlockPortIfname.setStatus("current")


class _HwSepTcNotifySep_Type(OctetString):
    """Custom type hwSepTcNotifySep based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwSepTcNotifySep_Type.__name__ = "OctetString"
_HwSepTcNotifySep_Object = MibTableColumn
hwSepTcNotifySep = _HwSepTcNotifySep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 9),
    _HwSepTcNotifySep_Type()
)
hwSepTcNotifySep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifySep.setStatus("current")
_HwSepTcNotifyRrpp_Type = EnabledStatus
_HwSepTcNotifyRrpp_Object = MibTableColumn
hwSepTcNotifyRrpp = _HwSepTcNotifyRrpp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 10),
    _HwSepTcNotifyRrpp_Type()
)
hwSepTcNotifyRrpp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifyRrpp.setStatus("current")
_HwSepTcNotifyStp_Type = EnabledStatus
_HwSepTcNotifyStp_Object = MibTableColumn
hwSepTcNotifyStp = _HwSepTcNotifyStp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 11),
    _HwSepTcNotifyStp_Type()
)
hwSepTcNotifyStp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifyStp.setStatus("current")
_HwSepTcNotifyVpls_Type = EnabledStatus
_HwSepTcNotifyVpls_Object = MibTableColumn
hwSepTcNotifyVpls = _HwSepTcNotifyVpls_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 12),
    _HwSepTcNotifyVpls_Type()
)
hwSepTcNotifyVpls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifyVpls.setStatus("current")
_HwSepTcNotifyVll_Type = EnabledStatus
_HwSepTcNotifyVll_Object = MibTableColumn
hwSepTcNotifyVll = _HwSepTcNotifyVll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 13),
    _HwSepTcNotifyVll_Type()
)
hwSepTcNotifyVll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifyVll.setStatus("current")


class _HwSepTcNotifySmartLinkCtrlVlan_Type(Integer32):
    """Custom type hwSepTcNotifySmartLinkCtrlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwSepTcNotifySmartLinkCtrlVlan_Type.__name__ = "Integer32"
_HwSepTcNotifySmartLinkCtrlVlan_Object = MibTableColumn
hwSepTcNotifySmartLinkCtrlVlan = _HwSepTcNotifySmartLinkCtrlVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 14),
    _HwSepTcNotifySmartLinkCtrlVlan_Type()
)
hwSepTcNotifySmartLinkCtrlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcNotifySmartLinkCtrlVlan.setStatus("current")
_HwSepDealSmartLinkFlush_Type = EnabledStatus
_HwSepDealSmartLinkFlush_Object = MibTableColumn
hwSepDealSmartLinkFlush = _HwSepDealSmartLinkFlush_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 15),
    _HwSepDealSmartLinkFlush_Type()
)
hwSepDealSmartLinkFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepDealSmartLinkFlush.setStatus("current")


class _HwSepProtectedInstanceList_Type(OctetString):
    """Custom type hwSepProtectedInstanceList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HwSepProtectedInstanceList_Type.__name__ = "OctetString"
_HwSepProtectedInstanceList_Object = MibTableColumn
hwSepProtectedInstanceList = _HwSepProtectedInstanceList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 16),
    _HwSepProtectedInstanceList_Type()
)
hwSepProtectedInstanceList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepProtectedInstanceList.setStatus("current")


class _HwSepTcProtectionInterval_Type(Integer32):
    """Custom type hwSepTcProtectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwSepTcProtectionInterval_Type.__name__ = "Integer32"
_HwSepTcProtectionInterval_Object = MibTableColumn
hwSepTcProtectionInterval = _HwSepTcProtectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 17),
    _HwSepTcProtectionInterval_Type()
)
hwSepTcProtectionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepTcProtectionInterval.setStatus("current")
_HwSepSegmentRowStatus_Type = RowStatus
_HwSepSegmentRowStatus_Object = MibTableColumn
hwSepSegmentRowStatus = _HwSepSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 128),
    _HwSepSegmentRowStatus_Type()
)
hwSepSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepSegmentRowStatus.setStatus("current")
_HwSepTopologyTable_Object = MibTable
hwSepTopologyTable = _HwSepTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3)
)
if mibBuilder.loadTexts:
    hwSepTopologyTable.setStatus("current")
_HwSepTopologyEntry_Object = MibTableRow
hwSepTopologyEntry = _HwSepTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1)
)
hwSepTopologyEntry.setIndexNames(
    (0, "HUAWEI-SEP-MIB", "hwSepSegmentId"),
    (0, "HUAWEI-SEP-MIB", "hwSepHop"),
)
if mibBuilder.loadTexts:
    hwSepTopologyEntry.setStatus("current")


class _HwSepHop_Type(Integer32):
    """Custom type hwSepHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwSepHop_Type.__name__ = "Integer32"
_HwSepHop_Object = MibTableColumn
hwSepHop = _HwSepHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 1),
    _HwSepHop_Type()
)
hwSepHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepHop.setStatus("current")


class _HwSepPortId_Type(OctetString):
    """Custom type hwSepPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwSepPortId_Type.__name__ = "OctetString"
_HwSepPortId_Object = MibTableColumn
hwSepPortId = _HwSepPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 2),
    _HwSepPortId_Type()
)
hwSepPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepPortId.setStatus("current")


class _HwSepTopoSysname_Type(OctetString):
    """Custom type hwSepTopoSysname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwSepTopoSysname_Type.__name__ = "OctetString"
_HwSepTopoSysname_Object = MibTableColumn
hwSepTopoSysname = _HwSepTopoSysname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 3),
    _HwSepTopoSysname_Type()
)
hwSepTopoSysname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoSysname.setStatus("current")


class _HwSepTopoPortname_Type(OctetString):
    """Custom type hwSepTopoPortname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwSepTopoPortname_Type.__name__ = "OctetString"
_HwSepTopoPortname_Object = MibTableColumn
hwSepTopoPortname = _HwSepTopoPortname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 4),
    _HwSepTopoPortname_Type()
)
hwSepTopoPortname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortname.setStatus("current")


class _HwSepTopoPortConfigPriority_Type(Integer32):
    """Custom type hwSepTopoPortConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwSepTopoPortConfigPriority_Type.__name__ = "Integer32"
_HwSepTopoPortConfigPriority_Object = MibTableColumn
hwSepTopoPortConfigPriority = _HwSepTopoPortConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 5),
    _HwSepTopoPortConfigPriority_Type()
)
hwSepTopoPortConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortConfigPriority.setStatus("current")
_HwSepTopoPortActivePriority_Type = Integer32
_HwSepTopoPortActivePriority_Object = MibTableColumn
hwSepTopoPortActivePriority = _HwSepTopoPortActivePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 6),
    _HwSepTopoPortActivePriority_Type()
)
hwSepTopoPortActivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortActivePriority.setStatus("current")
_HwSepTopoConfigPortRole_Type = Integer32
_HwSepTopoConfigPortRole_Object = MibTableColumn
hwSepTopoConfigPortRole = _HwSepTopoConfigPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 7),
    _HwSepTopoConfigPortRole_Type()
)
hwSepTopoConfigPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoConfigPortRole.setStatus("current")
_HwSepTopoActivePortRole_Type = Integer32
_HwSepTopoActivePortRole_Object = MibTableColumn
hwSepTopoActivePortRole = _HwSepTopoActivePortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 8),
    _HwSepTopoActivePortRole_Type()
)
hwSepTopoActivePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoActivePortRole.setStatus("current")


class _HwSepTopoPortNbrState_Type(Integer32):
    """Custom type hwSepTopoPortNbrState based on Integer32"""
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
        *(("conflict", 5),
          ("down", 1),
          ("init", 2),
          ("preup", 3),
          ("up", 4))
    )


_HwSepTopoPortNbrState_Type.__name__ = "Integer32"
_HwSepTopoPortNbrState_Object = MibTableColumn
hwSepTopoPortNbrState = _HwSepTopoPortNbrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 9),
    _HwSepTopoPortNbrState_Type()
)
hwSepTopoPortNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortNbrState.setStatus("current")


class _HwSepTopoBrotherPortId_Type(OctetString):
    """Custom type hwSepTopoBrotherPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwSepTopoBrotherPortId_Type.__name__ = "OctetString"
_HwSepTopoBrotherPortId_Object = MibTableColumn
hwSepTopoBrotherPortId = _HwSepTopoBrotherPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 10),
    _HwSepTopoBrotherPortId_Type()
)
hwSepTopoBrotherPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoBrotherPortId.setStatus("current")


class _HwSepTopoNbrPortId_Type(OctetString):
    """Custom type hwSepTopoNbrPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwSepTopoNbrPortId_Type.__name__ = "OctetString"
_HwSepTopoNbrPortId_Object = MibTableColumn
hwSepTopoNbrPortId = _HwSepTopoNbrPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 11),
    _HwSepTopoNbrPortId_Type()
)
hwSepTopoNbrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoNbrPortId.setStatus("current")


class _HwSepTopoPortLinkState_Type(Integer32):
    """Custom type hwSepTopoPortLinkState based on Integer32"""
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


_HwSepTopoPortLinkState_Type.__name__ = "Integer32"
_HwSepTopoPortLinkState_Object = MibTableColumn
hwSepTopoPortLinkState = _HwSepTopoPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 12),
    _HwSepTopoPortLinkState_Type()
)
hwSepTopoPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortLinkState.setStatus("current")


class _HwSepTopoPortFwdState_Type(Integer32):
    """Custom type hwSepTopoPortFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 2))
    )


_HwSepTopoPortFwdState_Type.__name__ = "Integer32"
_HwSepTopoPortFwdState_Object = MibTableColumn
hwSepTopoPortFwdState = _HwSepTopoPortFwdState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 13),
    _HwSepTopoPortFwdState_Type()
)
hwSepTopoPortFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTopoPortFwdState.setStatus("current")
_HwSepPortTable_Object = MibTable
hwSepPortTable = _HwSepPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4)
)
if mibBuilder.loadTexts:
    hwSepPortTable.setStatus("current")
_HwSepPortEntry_Object = MibTableRow
hwSepPortEntry = _HwSepPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1)
)
hwSepPortEntry.setIndexNames(
    (0, "HUAWEI-SEP-MIB", "hwSepSegmentId"),
    (0, "HUAWEI-SEP-MIB", "hwSepPortType"),
    (0, "HUAWEI-SEP-MIB", "hwSepPortId1"),
    (0, "HUAWEI-SEP-MIB", "hwSepPortId2"),
    (0, "HUAWEI-SEP-MIB", "hwSepPortId3"),
    (0, "HUAWEI-SEP-MIB", "hwSepPortId4"),
)
if mibBuilder.loadTexts:
    hwSepPortEntry.setStatus("current")


class _HwSepPortType_Type(Unsigned32):
    """Custom type hwSepPortType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwSepPortType_Type.__name__ = "Unsigned32"
_HwSepPortType_Object = MibTableColumn
hwSepPortType = _HwSepPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 1),
    _HwSepPortType_Type()
)
hwSepPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepPortType.setStatus("current")


class _HwSepPortId1_Type(Unsigned32):
    """Custom type hwSepPortId1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSepPortId1_Type.__name__ = "Unsigned32"
_HwSepPortId1_Object = MibTableColumn
hwSepPortId1 = _HwSepPortId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 2),
    _HwSepPortId1_Type()
)
hwSepPortId1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepPortId1.setStatus("current")


class _HwSepPortId2_Type(Unsigned32):
    """Custom type hwSepPortId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSepPortId2_Type.__name__ = "Unsigned32"
_HwSepPortId2_Object = MibTableColumn
hwSepPortId2 = _HwSepPortId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 3),
    _HwSepPortId2_Type()
)
hwSepPortId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepPortId2.setStatus("current")


class _HwSepPortId3_Type(Unsigned32):
    """Custom type hwSepPortId3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSepPortId3_Type.__name__ = "Unsigned32"
_HwSepPortId3_Object = MibTableColumn
hwSepPortId3 = _HwSepPortId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 4),
    _HwSepPortId3_Type()
)
hwSepPortId3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepPortId3.setStatus("current")


class _HwSepPortId4_Type(Unsigned32):
    """Custom type hwSepPortId4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSepPortId4_Type.__name__ = "Unsigned32"
_HwSepPortId4_Object = MibTableColumn
hwSepPortId4 = _HwSepPortId4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 5),
    _HwSepPortId4_Type()
)
hwSepPortId4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSepPortId4.setStatus("current")


class _HwSepSysname_Type(OctetString):
    """Custom type hwSepSysname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwSepSysname_Type.__name__ = "OctetString"
_HwSepSysname_Object = MibTableColumn
hwSepSysname = _HwSepSysname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 6),
    _HwSepSysname_Type()
)
hwSepSysname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepSysname.setStatus("current")


class _HwSepPortname_Type(OctetString):
    """Custom type hwSepPortname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwSepPortname_Type.__name__ = "OctetString"
_HwSepPortname_Object = MibTableColumn
hwSepPortname = _HwSepPortname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 7),
    _HwSepPortname_Type()
)
hwSepPortname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepPortname.setStatus("current")


class _HwSepPortConfigPriority_Type(Integer32):
    """Custom type hwSepPortConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwSepPortConfigPriority_Type.__name__ = "Integer32"
_HwSepPortConfigPriority_Object = MibTableColumn
hwSepPortConfigPriority = _HwSepPortConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 8),
    _HwSepPortConfigPriority_Type()
)
hwSepPortConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepPortConfigPriority.setStatus("current")
_HwSepPortActivePriority_Type = Integer32
_HwSepPortActivePriority_Object = MibTableColumn
hwSepPortActivePriority = _HwSepPortActivePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 9),
    _HwSepPortActivePriority_Type()
)
hwSepPortActivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepPortActivePriority.setStatus("current")
_HwSepConfigPortRole_Type = Integer32
_HwSepConfigPortRole_Object = MibTableColumn
hwSepConfigPortRole = _HwSepConfigPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 10),
    _HwSepConfigPortRole_Type()
)
hwSepConfigPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepConfigPortRole.setStatus("current")
_HwSepActivePortRole_Type = Integer32
_HwSepActivePortRole_Object = MibTableColumn
hwSepActivePortRole = _HwSepActivePortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 11),
    _HwSepActivePortRole_Type()
)
hwSepActivePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepActivePortRole.setStatus("current")


class _HwSepPortNbrState_Type(Integer32):
    """Custom type hwSepPortNbrState based on Integer32"""
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
        *(("conflict", 5),
          ("down", 1),
          ("init", 2),
          ("preup", 3),
          ("up", 4))
    )


_HwSepPortNbrState_Type.__name__ = "Integer32"
_HwSepPortNbrState_Object = MibTableColumn
hwSepPortNbrState = _HwSepPortNbrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 12),
    _HwSepPortNbrState_Type()
)
hwSepPortNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepPortNbrState.setStatus("current")


class _HwSepNbrPortId_Type(OctetString):
    """Custom type hwSepNbrPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwSepNbrPortId_Type.__name__ = "OctetString"
_HwSepNbrPortId_Object = MibTableColumn
hwSepNbrPortId = _HwSepNbrPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 13),
    _HwSepNbrPortId_Type()
)
hwSepNbrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepNbrPortId.setStatus("current")


class _HwSepPortFwdState_Type(Integer32):
    """Custom type hwSepPortFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 2))
    )


_HwSepPortFwdState_Type.__name__ = "Integer32"
_HwSepPortFwdState_Object = MibTableColumn
hwSepPortFwdState = _HwSepPortFwdState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 14),
    _HwSepPortFwdState_Type()
)
hwSepPortFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepPortFwdState.setStatus("current")
_HwSepRxNbrPktCnt_Type = Integer32
_HwSepRxNbrPktCnt_Object = MibTableColumn
hwSepRxNbrPktCnt = _HwSepRxNbrPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 15),
    _HwSepRxNbrPktCnt_Type()
)
hwSepRxNbrPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxNbrPktCnt.setStatus("current")
_HwSepTxNbrPktCnt_Type = Integer32
_HwSepTxNbrPktCnt_Object = MibTableColumn
hwSepTxNbrPktCnt = _HwSepTxNbrPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 16),
    _HwSepTxNbrPktCnt_Type()
)
hwSepTxNbrPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxNbrPktCnt.setStatus("current")
_HwSepRxLsaInfoPktCnt_Type = Integer32
_HwSepRxLsaInfoPktCnt_Object = MibTableColumn
hwSepRxLsaInfoPktCnt = _HwSepRxLsaInfoPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 17),
    _HwSepRxLsaInfoPktCnt_Type()
)
hwSepRxLsaInfoPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxLsaInfoPktCnt.setStatus("current")
_HwSepTxLsaInfoPktCnt_Type = Integer32
_HwSepTxLsaInfoPktCnt_Object = MibTableColumn
hwSepTxLsaInfoPktCnt = _HwSepTxLsaInfoPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 18),
    _HwSepTxLsaInfoPktCnt_Type()
)
hwSepTxLsaInfoPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxLsaInfoPktCnt.setStatus("current")
_HwSepRxLsaAckPktCnt_Type = Integer32
_HwSepRxLsaAckPktCnt_Object = MibTableColumn
hwSepRxLsaAckPktCnt = _HwSepRxLsaAckPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 19),
    _HwSepRxLsaAckPktCnt_Type()
)
hwSepRxLsaAckPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxLsaAckPktCnt.setStatus("current")
_HwSepTxLsaAckPktCnt_Type = Integer32
_HwSepTxLsaAckPktCnt_Object = MibTableColumn
hwSepTxLsaAckPktCnt = _HwSepTxLsaAckPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 20),
    _HwSepTxLsaAckPktCnt_Type()
)
hwSepTxLsaAckPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxLsaAckPktCnt.setStatus("current")
_HwSepRxPreemptReqPktCnt_Type = Integer32
_HwSepRxPreemptReqPktCnt_Object = MibTableColumn
hwSepRxPreemptReqPktCnt = _HwSepRxPreemptReqPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 21),
    _HwSepRxPreemptReqPktCnt_Type()
)
hwSepRxPreemptReqPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxPreemptReqPktCnt.setStatus("current")
_HwSepTxPreemptReqPktCnt_Type = Integer32
_HwSepTxPreemptReqPktCnt_Object = MibTableColumn
hwSepTxPreemptReqPktCnt = _HwSepTxPreemptReqPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 22),
    _HwSepTxPreemptReqPktCnt_Type()
)
hwSepTxPreemptReqPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxPreemptReqPktCnt.setStatus("current")
_HwSepRxPreemptAckPktCnt_Type = Integer32
_HwSepRxPreemptAckPktCnt_Object = MibTableColumn
hwSepRxPreemptAckPktCnt = _HwSepRxPreemptAckPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 23),
    _HwSepRxPreemptAckPktCnt_Type()
)
hwSepRxPreemptAckPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxPreemptAckPktCnt.setStatus("current")
_HwSepTxPreemptAckPktCnt_Type = Integer32
_HwSepTxPreemptAckPktCnt_Object = MibTableColumn
hwSepTxPreemptAckPktCnt = _HwSepTxPreemptAckPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 24),
    _HwSepTxPreemptAckPktCnt_Type()
)
hwSepTxPreemptAckPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxPreemptAckPktCnt.setStatus("current")
_HwSepRxTcPktCnt_Type = Integer32
_HwSepRxTcPktCnt_Object = MibTableColumn
hwSepRxTcPktCnt = _HwSepRxTcPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 25),
    _HwSepRxTcPktCnt_Type()
)
hwSepRxTcPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxTcPktCnt.setStatus("current")
_HwSepTxTcPktCnt_Type = Integer32
_HwSepTxTcPktCnt_Object = MibTableColumn
hwSepTxTcPktCnt = _HwSepTxTcPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 26),
    _HwSepTxTcPktCnt_Type()
)
hwSepTxTcPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxTcPktCnt.setStatus("current")
_HwSepRxEpaPktCnt_Type = Integer32
_HwSepRxEpaPktCnt_Object = MibTableColumn
hwSepRxEpaPktCnt = _HwSepRxEpaPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 27),
    _HwSepRxEpaPktCnt_Type()
)
hwSepRxEpaPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepRxEpaPktCnt.setStatus("current")
_HwSepTxEpaPktCnt_Type = Integer32
_HwSepTxEpaPktCnt_Object = MibTableColumn
hwSepTxEpaPktCnt = _HwSepTxEpaPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 28),
    _HwSepTxEpaPktCnt_Type()
)
hwSepTxEpaPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSepTxEpaPktCnt.setStatus("current")


class _HwSepResetPortPktCnt_Type(Integer32):
    """Custom type hwSepResetPortPktCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwSepResetPortPktCnt_Type.__name__ = "Integer32"
_HwSepResetPortPktCnt_Object = MibTableColumn
hwSepResetPortPktCnt = _HwSepResetPortPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 29),
    _HwSepResetPortPktCnt_Type()
)
hwSepResetPortPktCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSepResetPortPktCnt.setStatus("current")
_HwSepPortRowStatus_Type = RowStatus
_HwSepPortRowStatus_Object = MibTableColumn
hwSepPortRowStatus = _HwSepPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 128),
    _HwSepPortRowStatus_Type()
)
hwSepPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSepPortRowStatus.setStatus("current")
_HwSepGroups_ObjectIdentity = ObjectIdentity
hwSepGroups = _HwSepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2)
)

# Managed Objects groups

hwSepGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 1)
)
hwSepGlobalInfoGroup.setObjects(
    ("HUAWEI-SEP-MIB", "hwSepResetPktCnt")
)
if mibBuilder.loadTexts:
    hwSepGlobalInfoGroup.setStatus("current")

hwSepSegmentInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 2)
)
hwSepSegmentInfoGroup.setObjects(
      *(("HUAWEI-SEP-MIB", "hwSepSegmentId"),
        ("HUAWEI-SEP-MIB", "hwSepControlVlanId"),
        ("HUAWEI-SEP-MIB", "hwSepPreemptManual"),
        ("HUAWEI-SEP-MIB", "hwSepPreemptDelay"),
        ("HUAWEI-SEP-MIB", "hwSepBlockPortMode"),
        ("HUAWEI-SEP-MIB", "hwSepBlockPortHop"),
        ("HUAWEI-SEP-MIB", "hwSepBlockPortSysname"),
        ("HUAWEI-SEP-MIB", "hwSepBlockPortIfname"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifySep"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifyRrpp"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifyStp"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifyVpls"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifyVll"),
        ("HUAWEI-SEP-MIB", "hwSepTcNotifySmartLinkCtrlVlan"),
        ("HUAWEI-SEP-MIB", "hwSepDealSmartLinkFlush"),
        ("HUAWEI-SEP-MIB", "hwSepProtectedInstanceList"),
        ("HUAWEI-SEP-MIB", "hwSepTcProtectionInterval"),
        ("HUAWEI-SEP-MIB", "hwSepSegmentRowStatus"))
)
if mibBuilder.loadTexts:
    hwSepSegmentInfoGroup.setStatus("current")

hwSepPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 3)
)
hwSepPortInfoGroup.setObjects(
      *(("HUAWEI-SEP-MIB", "hwSepPortType"),
        ("HUAWEI-SEP-MIB", "hwSepPortId1"),
        ("HUAWEI-SEP-MIB", "hwSepPortId2"),
        ("HUAWEI-SEP-MIB", "hwSepPortId3"),
        ("HUAWEI-SEP-MIB", "hwSepPortId4"),
        ("HUAWEI-SEP-MIB", "hwSepSysname"),
        ("HUAWEI-SEP-MIB", "hwSepPortname"),
        ("HUAWEI-SEP-MIB", "hwSepPortConfigPriority"),
        ("HUAWEI-SEP-MIB", "hwSepPortActivePriority"),
        ("HUAWEI-SEP-MIB", "hwSepConfigPortRole"),
        ("HUAWEI-SEP-MIB", "hwSepActivePortRole"),
        ("HUAWEI-SEP-MIB", "hwSepPortNbrState"),
        ("HUAWEI-SEP-MIB", "hwSepNbrPortId"),
        ("HUAWEI-SEP-MIB", "hwSepPortFwdState"),
        ("HUAWEI-SEP-MIB", "hwSepRxNbrPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxNbrPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxLsaInfoPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxLsaInfoPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxLsaAckPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxLsaAckPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxPreemptReqPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxPreemptReqPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxPreemptAckPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxPreemptAckPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxTcPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxTcPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepRxEpaPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepTxEpaPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepResetPortPktCnt"),
        ("HUAWEI-SEP-MIB", "hwSepPortRowStatus"))
)
if mibBuilder.loadTexts:
    hwSepPortInfoGroup.setStatus("current")

hwSepTopologyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 4)
)
hwSepTopologyInfoGroup.setObjects(
      *(("HUAWEI-SEP-MIB", "hwSepHop"),
        ("HUAWEI-SEP-MIB", "hwSepPortId"),
        ("HUAWEI-SEP-MIB", "hwSepTopoSysname"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortname"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortConfigPriority"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortActivePriority"),
        ("HUAWEI-SEP-MIB", "hwSepTopoConfigPortRole"),
        ("HUAWEI-SEP-MIB", "hwSepTopoActivePortRole"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortNbrState"),
        ("HUAWEI-SEP-MIB", "hwSepTopoNbrPortId"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortLinkState"),
        ("HUAWEI-SEP-MIB", "hwSepTopoPortFwdState"),
        ("HUAWEI-SEP-MIB", "hwSepTopoBrotherPortId"))
)
if mibBuilder.loadTexts:
    hwSepTopologyInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SEP-MIB",
    **{"hwSepMIB": hwSepMIB,
       "hwSepObjects": hwSepObjects,
       "hwSepResetPktCnt": hwSepResetPktCnt,
       "hwSepSegmentTable": hwSepSegmentTable,
       "hwSepSegmentEntry": hwSepSegmentEntry,
       "hwSepSegmentId": hwSepSegmentId,
       "hwSepControlVlanId": hwSepControlVlanId,
       "hwSepPreemptManual": hwSepPreemptManual,
       "hwSepPreemptDelay": hwSepPreemptDelay,
       "hwSepBlockPortMode": hwSepBlockPortMode,
       "hwSepBlockPortHop": hwSepBlockPortHop,
       "hwSepBlockPortSysname": hwSepBlockPortSysname,
       "hwSepBlockPortIfname": hwSepBlockPortIfname,
       "hwSepTcNotifySep": hwSepTcNotifySep,
       "hwSepTcNotifyRrpp": hwSepTcNotifyRrpp,
       "hwSepTcNotifyStp": hwSepTcNotifyStp,
       "hwSepTcNotifyVpls": hwSepTcNotifyVpls,
       "hwSepTcNotifyVll": hwSepTcNotifyVll,
       "hwSepTcNotifySmartLinkCtrlVlan": hwSepTcNotifySmartLinkCtrlVlan,
       "hwSepDealSmartLinkFlush": hwSepDealSmartLinkFlush,
       "hwSepProtectedInstanceList": hwSepProtectedInstanceList,
       "hwSepTcProtectionInterval": hwSepTcProtectionInterval,
       "hwSepSegmentRowStatus": hwSepSegmentRowStatus,
       "hwSepTopologyTable": hwSepTopologyTable,
       "hwSepTopologyEntry": hwSepTopologyEntry,
       "hwSepHop": hwSepHop,
       "hwSepPortId": hwSepPortId,
       "hwSepTopoSysname": hwSepTopoSysname,
       "hwSepTopoPortname": hwSepTopoPortname,
       "hwSepTopoPortConfigPriority": hwSepTopoPortConfigPriority,
       "hwSepTopoPortActivePriority": hwSepTopoPortActivePriority,
       "hwSepTopoConfigPortRole": hwSepTopoConfigPortRole,
       "hwSepTopoActivePortRole": hwSepTopoActivePortRole,
       "hwSepTopoPortNbrState": hwSepTopoPortNbrState,
       "hwSepTopoBrotherPortId": hwSepTopoBrotherPortId,
       "hwSepTopoNbrPortId": hwSepTopoNbrPortId,
       "hwSepTopoPortLinkState": hwSepTopoPortLinkState,
       "hwSepTopoPortFwdState": hwSepTopoPortFwdState,
       "hwSepPortTable": hwSepPortTable,
       "hwSepPortEntry": hwSepPortEntry,
       "hwSepPortType": hwSepPortType,
       "hwSepPortId1": hwSepPortId1,
       "hwSepPortId2": hwSepPortId2,
       "hwSepPortId3": hwSepPortId3,
       "hwSepPortId4": hwSepPortId4,
       "hwSepSysname": hwSepSysname,
       "hwSepPortname": hwSepPortname,
       "hwSepPortConfigPriority": hwSepPortConfigPriority,
       "hwSepPortActivePriority": hwSepPortActivePriority,
       "hwSepConfigPortRole": hwSepConfigPortRole,
       "hwSepActivePortRole": hwSepActivePortRole,
       "hwSepPortNbrState": hwSepPortNbrState,
       "hwSepNbrPortId": hwSepNbrPortId,
       "hwSepPortFwdState": hwSepPortFwdState,
       "hwSepRxNbrPktCnt": hwSepRxNbrPktCnt,
       "hwSepTxNbrPktCnt": hwSepTxNbrPktCnt,
       "hwSepRxLsaInfoPktCnt": hwSepRxLsaInfoPktCnt,
       "hwSepTxLsaInfoPktCnt": hwSepTxLsaInfoPktCnt,
       "hwSepRxLsaAckPktCnt": hwSepRxLsaAckPktCnt,
       "hwSepTxLsaAckPktCnt": hwSepTxLsaAckPktCnt,
       "hwSepRxPreemptReqPktCnt": hwSepRxPreemptReqPktCnt,
       "hwSepTxPreemptReqPktCnt": hwSepTxPreemptReqPktCnt,
       "hwSepRxPreemptAckPktCnt": hwSepRxPreemptAckPktCnt,
       "hwSepTxPreemptAckPktCnt": hwSepTxPreemptAckPktCnt,
       "hwSepRxTcPktCnt": hwSepRxTcPktCnt,
       "hwSepTxTcPktCnt": hwSepTxTcPktCnt,
       "hwSepRxEpaPktCnt": hwSepRxEpaPktCnt,
       "hwSepTxEpaPktCnt": hwSepTxEpaPktCnt,
       "hwSepResetPortPktCnt": hwSepResetPortPktCnt,
       "hwSepPortRowStatus": hwSepPortRowStatus,
       "hwSepGroups": hwSepGroups,
       "hwSepGlobalInfoGroup": hwSepGlobalInfoGroup,
       "hwSepSegmentInfoGroup": hwSepSegmentInfoGroup,
       "hwSepPortInfoGroup": hwSepPortInfoGroup,
       "hwSepTopologyInfoGroup": hwSepTopologyInfoGroup}
)
