# SNMP MIB module (MY-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:21 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

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
 Gauge,
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
    "Gauge",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10)
)
myInterfaceMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyIfConfigMIBObjects_ObjectIdentity = ObjectIdentity
myIfConfigMIBObjects = _MyIfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1)
)
_MyIfTable_Object = MibTable
myIfTable = _MyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    myIfTable.setStatus("current")
_MyIfEntry_Object = MibTableRow
myIfEntry = _MyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1)
)
myIfEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myIfIndex"),
)
if mibBuilder.loadTexts:
    myIfEntry.setStatus("current")
_MyIfIndex_Type = IfIndex
_MyIfIndex_Object = MibTableColumn
myIfIndex = _MyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 1),
    _MyIfIndex_Type()
)
myIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfIndex.setStatus("current")


class _MyIfPortType_Type(Integer32):
    """Custom type myIfPortType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("port1000MBASEFX", 10),
          ("port1000MBASELX", 6),
          ("port1000MBASESX", 5),
          ("port1000MBASETX", 7),
          ("port100MBASEFX", 9),
          ("port100MBASEFXL", 3),
          ("port100MBASEFXS", 4),
          ("port10GBASE", 19),
          ("port10GBASEER", 14),
          ("port10GBASEEW", 18),
          ("port10GBASELR", 13),
          ("port10GBASELW", 17),
          ("port10GBASELX4", 15),
          ("port10GBASESR", 12),
          ("port10GBASESW", 16),
          ("port10M100MBASETX", 2),
          ("portGBIC", 8),
          ("portSFP", 11),
          ("unknown", 1))
    )


_MyIfPortType_Type.__name__ = "Integer32"
_MyIfPortType_Object = MibTableColumn
myIfPortType = _MyIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 2),
    _MyIfPortType_Type()
)
myIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfPortType.setStatus("current")


class _MyIfFlowControlAdminStatus_Type(Integer32):
    """Custom type myIfFlowControlAdminStatus based on Integer32"""
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
        *(("autonego", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("unknown", 4))
    )


_MyIfFlowControlAdminStatus_Type.__name__ = "Integer32"
_MyIfFlowControlAdminStatus_Object = MibTableColumn
myIfFlowControlAdminStatus = _MyIfFlowControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 3),
    _MyIfFlowControlAdminStatus_Type()
)
myIfFlowControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfFlowControlAdminStatus.setStatus("current")
_MyIfFlowControlOperStatus_Type = EnabledStatus
_MyIfFlowControlOperStatus_Object = MibTableColumn
myIfFlowControlOperStatus = _MyIfFlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 4),
    _MyIfFlowControlOperStatus_Type()
)
myIfFlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfFlowControlOperStatus.setStatus("current")


class _MyIfAdminSpeed_Type(Integer32):
    """Custom type myIfAdminSpeed based on Integer32"""
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
        *(("autonego", 4),
          ("speed1000Mb", 3),
          ("speed100Mb", 2),
          ("speed10Gb", 5),
          ("speed10Mb", 1),
          ("unknown", 6))
    )


_MyIfAdminSpeed_Type.__name__ = "Integer32"
_MyIfAdminSpeed_Object = MibTableColumn
myIfAdminSpeed = _MyIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 5),
    _MyIfAdminSpeed_Type()
)
myIfAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfAdminSpeed.setStatus("current")


class _MyIfAdminDuplex_Type(Integer32):
    """Custom type myIfAdminDuplex based on Integer32"""
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
        *(("autonego", 3),
          ("full", 1),
          ("half", 2),
          ("unknown", 4))
    )


_MyIfAdminDuplex_Type.__name__ = "Integer32"
_MyIfAdminDuplex_Object = MibTableColumn
myIfAdminDuplex = _MyIfAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 6),
    _MyIfAdminDuplex_Type()
)
myIfAdminDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfAdminDuplex.setStatus("current")


class _MyIfOperSpeed_Type(Integer32):
    """Custom type myIfOperSpeed based on Integer32"""
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
        *(("speed1000Mb", 3),
          ("speed100Mb", 2),
          ("speed10Gb", 5),
          ("speed10Mb", 1),
          ("unknown", 4))
    )


_MyIfOperSpeed_Type.__name__ = "Integer32"
_MyIfOperSpeed_Object = MibTableColumn
myIfOperSpeed = _MyIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 7),
    _MyIfOperSpeed_Type()
)
myIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfOperSpeed.setStatus("current")


class _MyIfOperDuplex_Type(Integer32):
    """Custom type myIfOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_MyIfOperDuplex_Type.__name__ = "Integer32"
_MyIfOperDuplex_Object = MibTableColumn
myIfOperDuplex = _MyIfOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 8),
    _MyIfOperDuplex_Type()
)
myIfOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfOperDuplex.setStatus("current")


class _MyIfManageStatus_Type(EnabledStatus):
    """Custom type myIfManageStatus based on EnabledStatus"""


_MyIfManageStatus_Object = MibTableColumn
myIfManageStatus = _MyIfManageStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 9),
    _MyIfManageStatus_Type()
)
myIfManageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfManageStatus.setStatus("current")
_MyIfIpBroadcast_Type = IpAddress
_MyIfIpBroadcast_Object = MibTableColumn
myIfIpBroadcast = _MyIfIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 10),
    _MyIfIpBroadcast_Type()
)
myIfIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfIpBroadcast.setStatus("current")


class _MyIfLayer_Type(Integer32):
    """Custom type myIfLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer-2", 1),
          ("layer-3", 2))
    )


_MyIfLayer_Type.__name__ = "Integer32"
_MyIfLayer_Object = MibTableColumn
myIfLayer = _MyIfLayer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 11),
    _MyIfLayer_Type()
)
myIfLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfLayer.setStatus("current")


class _MyIfMode_Type(Integer32):
    """Custom type myIfMode based on Integer32"""
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
        *(("access", 1),
          ("dot1q-tunnel", 3),
          ("host", 7),
          ("hybrid", 4),
          ("other", 5),
          ("promiscuous", 8),
          ("trunk", 2),
          ("uplink", 6))
    )


_MyIfMode_Type.__name__ = "Integer32"
_MyIfMode_Object = MibTableColumn
myIfMode = _MyIfMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 12),
    _MyIfMode_Type()
)
myIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfMode.setStatus("current")
_MyIfCounterClear_Type = Integer32
_MyIfCounterClear_Object = MibTableColumn
myIfCounterClear = _MyIfCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 13),
    _MyIfCounterClear_Type()
)
myIfCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfCounterClear.setStatus("current")
_MyIfEntryStatus_Type = ConfigStatus
_MyIfEntryStatus_Object = MibTableColumn
myIfEntryStatus = _MyIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 14),
    _MyIfEntryStatus_Type()
)
myIfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myIfEntryStatus.setStatus("current")


class _MyIfMediumType_Type(Integer32):
    """Custom type myIfMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("unknown", 0))
    )


_MyIfMediumType_Type.__name__ = "Integer32"
_MyIfMediumType_Object = MibTableColumn
myIfMediumType = _MyIfMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 1, 1, 15),
    _MyIfMediumType_Type()
)
myIfMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfMediumType.setStatus("current")
_MyIfIpTable_Object = MibTable
myIfIpTable = _MyIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    myIfIpTable.setStatus("current")
_MyIfIpEntry_Object = MibTableRow
myIfIpEntry = _MyIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1)
)
myIfIpEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myIfIpIfIndex"),
    (0, "MY-INTERFACE-MIB", "myIfIpId"),
    (0, "MY-INTERFACE-MIB", "myIfIp"),
)
if mibBuilder.loadTexts:
    myIfIpEntry.setStatus("current")
_MyIfIpIfIndex_Type = IfIndex
_MyIfIpIfIndex_Object = MibTableColumn
myIfIpIfIndex = _MyIfIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1, 1),
    _MyIfIpIfIndex_Type()
)
myIfIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfIpIfIndex.setStatus("current")


class _MyIfIpId_Type(Integer32):
    """Custom type myIfIpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MyIfIpId_Type.__name__ = "Integer32"
_MyIfIpId_Object = MibTableColumn
myIfIpId = _MyIfIpId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1, 2),
    _MyIfIpId_Type()
)
myIfIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfIpId.setStatus("current")
_MyIfIp_Type = IpAddress
_MyIfIp_Object = MibTableColumn
myIfIp = _MyIfIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1, 3),
    _MyIfIp_Type()
)
myIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfIp.setStatus("current")
_MyIfIpMask_Type = IpAddress
_MyIfIpMask_Object = MibTableColumn
myIfIpMask = _MyIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1, 4),
    _MyIfIpMask_Type()
)
myIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfIpMask.setStatus("current")
_MyIfIpEntryStatus_Type = RowStatus
_MyIfIpEntryStatus_Object = MibTableColumn
myIfIpEntryStatus = _MyIfIpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 2, 1, 5),
    _MyIfIpEntryStatus_Type()
)
myIfIpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myIfIpEntryStatus.setStatus("current")
_MyIfStatusTable_Object = MibTable
myIfStatusTable = _MyIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    myIfStatusTable.setStatus("current")
_MyIfStatusEntry_Object = MibTableRow
myIfStatusEntry = _MyIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3, 1)
)
myIfStatusEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myIfStatusIndex"),
)
if mibBuilder.loadTexts:
    myIfStatusEntry.setStatus("current")
_MyIfStatusIndex_Type = IfIndex
_MyIfStatusIndex_Object = MibTableColumn
myIfStatusIndex = _MyIfStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3, 1, 1),
    _MyIfStatusIndex_Type()
)
myIfStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfStatusIndex.setStatus("current")
_MyIfStatusLoopBackExamine_Type = Integer32
_MyIfStatusLoopBackExamine_Object = MibTableColumn
myIfStatusLoopBackExamine = _MyIfStatusLoopBackExamine_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3, 1, 2),
    _MyIfStatusLoopBackExamine_Type()
)
myIfStatusLoopBackExamine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfStatusLoopBackExamine.setStatus("current")


class _MyIfErrorStatus_Type(Integer32):
    """Custom type myIfErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("err-disable-bpduguard", 2),
          ("err-disable-ptsecurity", 3),
          ("no-error", 1))
    )


_MyIfErrorStatus_Type.__name__ = "Integer32"
_MyIfErrorStatus_Object = MibTableColumn
myIfErrorStatus = _MyIfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3, 1, 3),
    _MyIfErrorStatus_Type()
)
myIfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfErrorStatus.setStatus("current")
_MyIfLineDetect_Type = Integer32
_MyIfLineDetect_Object = MibTableColumn
myIfLineDetect = _MyIfLineDetect_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 3, 1, 4),
    _MyIfLineDetect_Type()
)
myIfLineDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfLineDetect.setStatus("current")
_MyGlobalIfDisableRecovery_Type = Integer32
_MyGlobalIfDisableRecovery_Object = MibScalar
myGlobalIfDisableRecovery = _MyGlobalIfDisableRecovery_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 4),
    _MyGlobalIfDisableRecovery_Type()
)
myGlobalIfDisableRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGlobalIfDisableRecovery.setStatus("current")
_MyPortTypeChooseTable_Object = MibTable
myPortTypeChooseTable = _MyPortTypeChooseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    myPortTypeChooseTable.setStatus("current")
_MyPortTypeChooseEntry_Object = MibTableRow
myPortTypeChooseEntry = _MyPortTypeChooseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 5, 1)
)
myPortTypeChooseEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myPortTypeChooseIndex"),
)
if mibBuilder.loadTexts:
    myPortTypeChooseEntry.setStatus("current")
_MyPortTypeChooseIndex_Type = IfIndex
_MyPortTypeChooseIndex_Object = MibTableColumn
myPortTypeChooseIndex = _MyPortTypeChooseIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 5, 1, 1),
    _MyPortTypeChooseIndex_Type()
)
myPortTypeChooseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortTypeChooseIndex.setStatus("current")


class _MyPortTypeChooseType_Type(Integer32):
    """Custom type myPortTypeChooseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1))
    )


_MyPortTypeChooseType_Type.__name__ = "Integer32"
_MyPortTypeChooseType_Object = MibTableColumn
myPortTypeChooseType = _MyPortTypeChooseType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 5, 1, 2),
    _MyPortTypeChooseType_Type()
)
myPortTypeChooseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortTypeChooseType.setStatus("current")
_MyIfMTUTable_Object = MibTable
myIfMTUTable = _MyIfMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    myIfMTUTable.setStatus("current")
_MyIfMTUEntry_Object = MibTableRow
myIfMTUEntry = _MyIfMTUEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 6, 1)
)
myIfMTUEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myIfMTUIndex"),
)
if mibBuilder.loadTexts:
    myIfMTUEntry.setStatus("current")
_MyIfMTUIndex_Type = IfIndex
_MyIfMTUIndex_Object = MibTableColumn
myIfMTUIndex = _MyIfMTUIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 6, 1, 1),
    _MyIfMTUIndex_Type()
)
myIfMTUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfMTUIndex.setStatus("current")
_MyIfMTU_Type = Integer32
_MyIfMTU_Object = MibTableColumn
myIfMTU = _MyIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 6, 1, 2),
    _MyIfMTU_Type()
)
myIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfMTU.setStatus("current")
_MyIfAvailableBWTable_Object = MibTable
myIfAvailableBWTable = _MyIfAvailableBWTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 7)
)
if mibBuilder.loadTexts:
    myIfAvailableBWTable.setStatus("current")
_MyIfAvailableBWEntry_Object = MibTableRow
myIfAvailableBWEntry = _MyIfAvailableBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 7, 1)
)
myIfAvailableBWEntry.setIndexNames(
    (0, "MY-INTERFACE-MIB", "myIfAvailableBWIfIndex"),
)
if mibBuilder.loadTexts:
    myIfAvailableBWEntry.setStatus("current")
_MyIfAvailableBWIfIndex_Type = IfIndex
_MyIfAvailableBWIfIndex_Object = MibTableColumn
myIfAvailableBWIfIndex = _MyIfAvailableBWIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 7, 1, 1),
    _MyIfAvailableBWIfIndex_Type()
)
myIfAvailableBWIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfAvailableBWIfIndex.setStatus("current")
_MyIfAvailableBWIfBW_Type = Gauge32
_MyIfAvailableBWIfBW_Object = MibTableColumn
myIfAvailableBWIfBW = _MyIfAvailableBWIfBW_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 1, 7, 1, 2),
    _MyIfAvailableBWIfBW_Type()
)
myIfAvailableBWIfBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfAvailableBWIfBW.setStatus("current")
_MyInterfaceTraps_ObjectIdentity = ObjectIdentity
myInterfaceTraps = _MyInterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 2)
)


class _LineDetectStatus_Type(Integer32):
    """Custom type lineDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("open", 2),
          ("short", 3))
    )


_LineDetectStatus_Type.__name__ = "Integer32"
_LineDetectStatus_Object = MibScalar
lineDetectStatus = _LineDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 2, 1),
    _LineDetectStatus_Type()
)
lineDetectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectStatus.setStatus("current")
_LineDetectPosition_Type = Integer32
_LineDetectPosition_Object = MibScalar
lineDetectPosition = _LineDetectPosition_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 2, 2),
    _LineDetectPosition_Type()
)
lineDetectPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectPosition.setStatus("current")
_MyInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
myInterfaceMIBConformance = _MyInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3)
)
_MyInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
myInterfaceMIBCompliances = _MyInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 1)
)
_MyInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
myInterfaceMIBGroups = _MyInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2)
)

# Managed Objects groups

myInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2, 1)
)
myInterfaceMIBGroup.setObjects(
      *(("MY-INTERFACE-MIB", "myIfIndex"),
        ("MY-INTERFACE-MIB", "myIfPortType"),
        ("MY-INTERFACE-MIB", "myIfFlowControlAdminStatus"),
        ("MY-INTERFACE-MIB", "myIfFlowControlOperStatus"),
        ("MY-INTERFACE-MIB", "myIfAdminSpeed"),
        ("MY-INTERFACE-MIB", "myIfAdminDuplex"),
        ("MY-INTERFACE-MIB", "myIfOperSpeed"),
        ("MY-INTERFACE-MIB", "myIfOperDuplex"),
        ("MY-INTERFACE-MIB", "myIfManageStatus"),
        ("MY-INTERFACE-MIB", "myIfIpBroadcast"),
        ("MY-INTERFACE-MIB", "myIfLayer"),
        ("MY-INTERFACE-MIB", "myIfMode"),
        ("MY-INTERFACE-MIB", "myIfCounterClear"),
        ("MY-INTERFACE-MIB", "myIfEntryStatus"),
        ("MY-INTERFACE-MIB", "myIfMediumType"),
        ("MY-INTERFACE-MIB", "myIfIpIfIndex"),
        ("MY-INTERFACE-MIB", "myIfIpId"),
        ("MY-INTERFACE-MIB", "myIfIp"),
        ("MY-INTERFACE-MIB", "myIfIpMask"),
        ("MY-INTERFACE-MIB", "myIfIpEntryStatus"),
        ("MY-INTERFACE-MIB", "myIfStatusIndex"),
        ("MY-INTERFACE-MIB", "myIfStatusLoopBackExamine"),
        ("MY-INTERFACE-MIB", "myIfErrorStatus"),
        ("MY-INTERFACE-MIB", "myGlobalIfDisableRecovery"))
)
if mibBuilder.loadTexts:
    myInterfaceMIBGroup.setStatus("current")

myPortTypeChooseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2, 2)
)
myPortTypeChooseMibGroup.setObjects(
      *(("MY-INTERFACE-MIB", "myPortTypeChooseIndex"),
        ("MY-INTERFACE-MIB", "myPortTypeChooseType"))
)
if mibBuilder.loadTexts:
    myPortTypeChooseMibGroup.setStatus("current")

myIfMTUMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2, 3)
)
myIfMTUMibGroup.setObjects(
      *(("MY-INTERFACE-MIB", "myIfMTUIndex"),
        ("MY-INTERFACE-MIB", "myIfMTU"))
)
if mibBuilder.loadTexts:
    myIfMTUMibGroup.setStatus("current")

myIfLineDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2, 4)
)
myIfLineDetectGroup.setObjects(
    ("MY-INTERFACE-MIB", "myIfLineDetect")
)
if mibBuilder.loadTexts:
    myIfLineDetectGroup.setStatus("current")

myIfAvailableBWMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 2, 5)
)
myIfAvailableBWMibGroup.setObjects(
      *(("MY-INTERFACE-MIB", "myIfAvailableBWIfIndex"),
        ("MY-INTERFACE-MIB", "myIfAvailableBWIfBW"))
)
if mibBuilder.loadTexts:
    myIfAvailableBWMibGroup.setStatus("current")


# Notification objects

lineQualityDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 2, 3)
)
lineQualityDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MY-INTERFACE-MIB", "lineDetectStatus"),
        ("MY-INTERFACE-MIB", "lineDetectPosition"))
)
if mibBuilder.loadTexts:
    lineQualityDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    myInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-INTERFACE-MIB",
    **{"myInterfaceMIB": myInterfaceMIB,
       "myIfConfigMIBObjects": myIfConfigMIBObjects,
       "myIfTable": myIfTable,
       "myIfEntry": myIfEntry,
       "myIfIndex": myIfIndex,
       "myIfPortType": myIfPortType,
       "myIfFlowControlAdminStatus": myIfFlowControlAdminStatus,
       "myIfFlowControlOperStatus": myIfFlowControlOperStatus,
       "myIfAdminSpeed": myIfAdminSpeed,
       "myIfAdminDuplex": myIfAdminDuplex,
       "myIfOperSpeed": myIfOperSpeed,
       "myIfOperDuplex": myIfOperDuplex,
       "myIfManageStatus": myIfManageStatus,
       "myIfIpBroadcast": myIfIpBroadcast,
       "myIfLayer": myIfLayer,
       "myIfMode": myIfMode,
       "myIfCounterClear": myIfCounterClear,
       "myIfEntryStatus": myIfEntryStatus,
       "myIfMediumType": myIfMediumType,
       "myIfIpTable": myIfIpTable,
       "myIfIpEntry": myIfIpEntry,
       "myIfIpIfIndex": myIfIpIfIndex,
       "myIfIpId": myIfIpId,
       "myIfIp": myIfIp,
       "myIfIpMask": myIfIpMask,
       "myIfIpEntryStatus": myIfIpEntryStatus,
       "myIfStatusTable": myIfStatusTable,
       "myIfStatusEntry": myIfStatusEntry,
       "myIfStatusIndex": myIfStatusIndex,
       "myIfStatusLoopBackExamine": myIfStatusLoopBackExamine,
       "myIfErrorStatus": myIfErrorStatus,
       "myIfLineDetect": myIfLineDetect,
       "myGlobalIfDisableRecovery": myGlobalIfDisableRecovery,
       "myPortTypeChooseTable": myPortTypeChooseTable,
       "myPortTypeChooseEntry": myPortTypeChooseEntry,
       "myPortTypeChooseIndex": myPortTypeChooseIndex,
       "myPortTypeChooseType": myPortTypeChooseType,
       "myIfMTUTable": myIfMTUTable,
       "myIfMTUEntry": myIfMTUEntry,
       "myIfMTUIndex": myIfMTUIndex,
       "myIfMTU": myIfMTU,
       "myIfAvailableBWTable": myIfAvailableBWTable,
       "myIfAvailableBWEntry": myIfAvailableBWEntry,
       "myIfAvailableBWIfIndex": myIfAvailableBWIfIndex,
       "myIfAvailableBWIfBW": myIfAvailableBWIfBW,
       "myInterfaceTraps": myInterfaceTraps,
       "lineDetectStatus": lineDetectStatus,
       "lineDetectPosition": lineDetectPosition,
       "lineQualityDetect": lineQualityDetect,
       "myInterfaceMIBConformance": myInterfaceMIBConformance,
       "myInterfaceMIBCompliances": myInterfaceMIBCompliances,
       "myInterfaceMIBCompliance": myInterfaceMIBCompliance,
       "myInterfaceMIBGroups": myInterfaceMIBGroups,
       "myInterfaceMIBGroup": myInterfaceMIBGroup,
       "myPortTypeChooseMibGroup": myPortTypeChooseMibGroup,
       "myIfMTUMibGroup": myIfMTUMibGroup,
       "myIfLineDetectGroup": myIfLineDetectGroup,
       "myIfAvailableBWMibGroup": myIfAvailableBWMibGroup}
)
