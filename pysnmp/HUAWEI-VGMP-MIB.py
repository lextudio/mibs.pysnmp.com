# SNMP MIB module (HUAWEI-VGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:23 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hwVgmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122)
)
hwVgmpMib.setRevisions(
        ("2007-01-11 21:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VgmpGlobalCtrl_ObjectIdentity = ObjectIdentity
vgmpGlobalCtrl = _VgmpGlobalCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0)
)


class _HwVgmpTrapSnmpCtrl_Type(Integer32):
    """Custom type hwVgmpTrapSnmpCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwVgmpTrapSnmpCtrl_Type.__name__ = "Integer32"
_HwVgmpTrapSnmpCtrl_Object = MibScalar
hwVgmpTrapSnmpCtrl = _HwVgmpTrapSnmpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0, 1),
    _HwVgmpTrapSnmpCtrl_Type()
)
hwVgmpTrapSnmpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVgmpTrapSnmpCtrl.setStatus("current")


class _HwVgmpStrictCheck_Type(Integer32):
    """Custom type hwVgmpStrictCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwVgmpStrictCheck_Type.__name__ = "Integer32"
_HwVgmpStrictCheck_Object = MibScalar
hwVgmpStrictCheck = _HwVgmpStrictCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 0, 2),
    _HwVgmpStrictCheck_Type()
)
hwVgmpStrictCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVgmpStrictCheck.setStatus("current")
_VgmpNotifications_ObjectIdentity = ObjectIdentity
vgmpNotifications = _VgmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1)
)
_VgmpOperations_ObjectIdentity = ObjectIdentity
vgmpOperations = _VgmpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2)
)
_HwVgmpGroupCfgTable_Object = MibTable
hwVgmpGroupCfgTable = _HwVgmpGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1)
)
if mibBuilder.loadTexts:
    hwVgmpGroupCfgTable.setStatus("current")
_HwVgmpGroupCfgEntry_Object = MibTableRow
hwVgmpGroupCfgEntry = _HwVgmpGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1)
)
hwVgmpGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"),
)
if mibBuilder.loadTexts:
    hwVgmpGroupCfgEntry.setStatus("current")


class _HwVgmpGroupCfgID_Type(Integer32):
    """Custom type hwVgmpGroupCfgID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwVgmpGroupCfgID_Type.__name__ = "Integer32"
_HwVgmpGroupCfgID_Object = MibTableColumn
hwVgmpGroupCfgID = _HwVgmpGroupCfgID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 1),
    _HwVgmpGroupCfgID_Type()
)
hwVgmpGroupCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgID.setStatus("current")


class _HwVgmpGroupCfgEnable_Type(Integer32):
    """Custom type hwVgmpGroupCfgEnable based on Integer32"""
    defaultValue = 2

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


_HwVgmpGroupCfgEnable_Type.__name__ = "Integer32"
_HwVgmpGroupCfgEnable_Object = MibTableColumn
hwVgmpGroupCfgEnable = _HwVgmpGroupCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 2),
    _HwVgmpGroupCfgEnable_Type()
)
hwVgmpGroupCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgEnable.setStatus("current")


class _HwVgmpGroupCfgPri_Type(Integer32):
    """Custom type hwVgmpGroupCfgPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwVgmpGroupCfgPri_Type.__name__ = "Integer32"
_HwVgmpGroupCfgPri_Object = MibTableColumn
hwVgmpGroupCfgPri = _HwVgmpGroupCfgPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 3),
    _HwVgmpGroupCfgPri_Type()
)
hwVgmpGroupCfgPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPri.setStatus("current")


class _HwVgmpGroupCfgUseVrrpPri_Type(Integer32):
    """Custom type hwVgmpGroupCfgUseVrrpPri based on Integer32"""
    defaultValue = 2

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


_HwVgmpGroupCfgUseVrrpPri_Type.__name__ = "Integer32"
_HwVgmpGroupCfgUseVrrpPri_Object = MibTableColumn
hwVgmpGroupCfgUseVrrpPri = _HwVgmpGroupCfgUseVrrpPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 4),
    _HwVgmpGroupCfgUseVrrpPri_Type()
)
hwVgmpGroupCfgUseVrrpPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgUseVrrpPri.setStatus("current")


class _HwVgmpGroupCfgPriPlusValue_Type(Integer32):
    """Custom type hwVgmpGroupCfgPriPlusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwVgmpGroupCfgPriPlusValue_Type.__name__ = "Integer32"
_HwVgmpGroupCfgPriPlusValue_Object = MibTableColumn
hwVgmpGroupCfgPriPlusValue = _HwVgmpGroupCfgPriPlusValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 5),
    _HwVgmpGroupCfgPriPlusValue_Type()
)
hwVgmpGroupCfgPriPlusValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPriPlusValue.setStatus("current")


class _HwVgmpGroupCfgPreemptEnable_Type(Integer32):
    """Custom type hwVgmpGroupCfgPreemptEnable based on Integer32"""
    defaultValue = 2

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


_HwVgmpGroupCfgPreemptEnable_Type.__name__ = "Integer32"
_HwVgmpGroupCfgPreemptEnable_Object = MibTableColumn
hwVgmpGroupCfgPreemptEnable = _HwVgmpGroupCfgPreemptEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 6),
    _HwVgmpGroupCfgPreemptEnable_Type()
)
hwVgmpGroupCfgPreemptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPreemptEnable.setStatus("current")


class _HwVgmpGroupCfgPreemptDelayValue_Type(Integer32):
    """Custom type hwVgmpGroupCfgPreemptDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwVgmpGroupCfgPreemptDelayValue_Type.__name__ = "Integer32"
_HwVgmpGroupCfgPreemptDelayValue_Object = MibTableColumn
hwVgmpGroupCfgPreemptDelayValue = _HwVgmpGroupCfgPreemptDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 7),
    _HwVgmpGroupCfgPreemptDelayValue_Type()
)
hwVgmpGroupCfgPreemptDelayValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPreemptDelayValue.setStatus("current")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPreemptDelayValue.setUnits("milli-seconds")


class _HwVgmpGroupCfgHelloInterval_Type(Integer32):
    """Custom type hwVgmpGroupCfgHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 60000),
    )


_HwVgmpGroupCfgHelloInterval_Type.__name__ = "Integer32"
_HwVgmpGroupCfgHelloInterval_Object = MibTableColumn
hwVgmpGroupCfgHelloInterval = _HwVgmpGroupCfgHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 8),
    _HwVgmpGroupCfgHelloInterval_Type()
)
hwVgmpGroupCfgHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgHelloInterval.setUnits("milli-seconds")


class _HwVgmpGroupCfgSendEnable_Type(Integer32):
    """Custom type hwVgmpGroupCfgSendEnable based on Integer32"""
    defaultValue = 2

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


_HwVgmpGroupCfgSendEnable_Type.__name__ = "Integer32"
_HwVgmpGroupCfgSendEnable_Object = MibTableColumn
hwVgmpGroupCfgSendEnable = _HwVgmpGroupCfgSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 9),
    _HwVgmpGroupCfgSendEnable_Type()
)
hwVgmpGroupCfgSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgSendEnable.setStatus("current")


class _HwVgmpGroupCfgState_Type(Integer32):
    """Custom type hwVgmpGroupCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 2),
          ("master", 3),
          ("master2slave", 5),
          ("max", 7),
          ("nouse", 1),
          ("slave", 4),
          ("slave2master", 6))
    )


_HwVgmpGroupCfgState_Type.__name__ = "Integer32"
_HwVgmpGroupCfgState_Object = MibTableColumn
hwVgmpGroupCfgState = _HwVgmpGroupCfgState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 10),
    _HwVgmpGroupCfgState_Type()
)
hwVgmpGroupCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgState.setStatus("current")


class _HwVgmpGroupCfgRunPri_Type(Integer32):
    """Custom type hwVgmpGroupCfgRunPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVgmpGroupCfgRunPri_Type.__name__ = "Integer32"
_HwVgmpGroupCfgRunPri_Object = MibTableColumn
hwVgmpGroupCfgRunPri = _HwVgmpGroupCfgRunPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 11),
    _HwVgmpGroupCfgRunPri_Type()
)
hwVgmpGroupCfgRunPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgRunPri.setStatus("current")
_HwVgmpGroupCfgCreateTime_Type = Unsigned32
_HwVgmpGroupCfgCreateTime_Object = MibTableColumn
hwVgmpGroupCfgCreateTime = _HwVgmpGroupCfgCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 12),
    _HwVgmpGroupCfgCreateTime_Type()
)
hwVgmpGroupCfgCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgCreateTime.setStatus("current")
_HwVgmpGroupCfgLastChangeTime_Type = Unsigned32
_HwVgmpGroupCfgLastChangeTime_Object = MibTableColumn
hwVgmpGroupCfgLastChangeTime = _HwVgmpGroupCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 13),
    _HwVgmpGroupCfgLastChangeTime_Type()
)
hwVgmpGroupCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgLastChangeTime.setStatus("current")


class _HwVgmpGroupCfgPeerState_Type(Integer32):
    """Custom type hwVgmpGroupCfgPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HwVgmpGroupCfgPeerState_Type.__name__ = "Integer32"
_HwVgmpGroupCfgPeerState_Object = MibTableColumn
hwVgmpGroupCfgPeerState = _HwVgmpGroupCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 14),
    _HwVgmpGroupCfgPeerState_Type()
)
hwVgmpGroupCfgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgPeerState.setStatus("current")


class _HwVgmpGroupCfgVrrpNum_Type(Integer32):
    """Custom type hwVgmpGroupCfgVrrpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwVgmpGroupCfgVrrpNum_Type.__name__ = "Integer32"
_HwVgmpGroupCfgVrrpNum_Object = MibTableColumn
hwVgmpGroupCfgVrrpNum = _HwVgmpGroupCfgVrrpNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 15),
    _HwVgmpGroupCfgVrrpNum_Type()
)
hwVgmpGroupCfgVrrpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgVrrpNum.setStatus("current")


class _HwVgmpGroupCfgReset_Type(Integer32):
    """Custom type hwVgmpGroupCfgReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 2))
    )


_HwVgmpGroupCfgReset_Type.__name__ = "Integer32"
_HwVgmpGroupCfgReset_Object = MibTableColumn
hwVgmpGroupCfgReset = _HwVgmpGroupCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 16),
    _HwVgmpGroupCfgReset_Type()
)
hwVgmpGroupCfgReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgReset.setStatus("current")
_HwVgmpGroupCfgOperRowStatus_Type = RowStatus
_HwVgmpGroupCfgOperRowStatus_Object = MibTableColumn
hwVgmpGroupCfgOperRowStatus = _HwVgmpGroupCfgOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 17),
    _HwVgmpGroupCfgOperRowStatus_Type()
)
hwVgmpGroupCfgOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgOperRowStatus.setStatus("current")


class _HwVgmpGroupCfgNextState_Type(Integer32):
    """Custom type hwVgmpGroupCfgNextState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 2),
          ("master", 3),
          ("master2slave", 5),
          ("nouse", 1),
          ("slave", 4),
          ("slave2master", 6),
          ("unknown", 7))
    )


_HwVgmpGroupCfgNextState_Type.__name__ = "Integer32"
_HwVgmpGroupCfgNextState_Object = MibTableColumn
hwVgmpGroupCfgNextState = _HwVgmpGroupCfgNextState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 1, 1, 18),
    _HwVgmpGroupCfgNextState_Type()
)
hwVgmpGroupCfgNextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpGroupCfgNextState.setStatus("current")
_HwVgmpMemberTable_Object = MibTable
hwVgmpMemberTable = _HwVgmpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2)
)
if mibBuilder.loadTexts:
    hwVgmpMemberTable.setStatus("current")
_HwVgmpMemberEntry_Object = MibTableRow
hwVgmpMemberEntry = _HwVgmpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1)
)
hwVgmpMemberEntry.setIndexNames(
    (0, "HUAWEI-VGMP-MIB", "hwVgmpMemberIfIndex"),
    (0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"),
    (0, "HUAWEI-VGMP-MIB", "hwVgmpMemberVRID"),
)
if mibBuilder.loadTexts:
    hwVgmpMemberEntry.setStatus("current")
_HwVgmpMemberIfIndex_Type = InterfaceIndex
_HwVgmpMemberIfIndex_Object = MibTableColumn
hwVgmpMemberIfIndex = _HwVgmpMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 1),
    _HwVgmpMemberIfIndex_Type()
)
hwVgmpMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVgmpMemberIfIndex.setStatus("current")


class _HwVgmpMemberVRID_Type(Integer32):
    """Custom type hwVgmpMemberVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwVgmpMemberVRID_Type.__name__ = "Integer32"
_HwVgmpMemberVRID_Object = MibTableColumn
hwVgmpMemberVRID = _HwVgmpMemberVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 2),
    _HwVgmpMemberVRID_Type()
)
hwVgmpMemberVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVgmpMemberVRID.setStatus("current")


class _HwVgmpMemberData_Type(Integer32):
    """Custom type hwVgmpMemberData based on Integer32"""
    defaultValue = 2

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


_HwVgmpMemberData_Type.__name__ = "Integer32"
_HwVgmpMemberData_Object = MibTableColumn
hwVgmpMemberData = _HwVgmpMemberData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 3),
    _HwVgmpMemberData_Type()
)
hwVgmpMemberData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpMemberData.setStatus("current")


class _HwVgmpMemberTran_Type(Integer32):
    """Custom type hwVgmpMemberTran based on Integer32"""
    defaultValue = 2

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


_HwVgmpMemberTran_Type.__name__ = "Integer32"
_HwVgmpMemberTran_Object = MibTableColumn
hwVgmpMemberTran = _HwVgmpMemberTran_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 4),
    _HwVgmpMemberTran_Type()
)
hwVgmpMemberTran.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpMemberTran.setStatus("current")


class _HwVgmpMemberVrrpOnline_Type(Integer32):
    """Custom type hwVgmpMemberVrrpOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("peerDown", 2),
          ("up", 3))
    )


_HwVgmpMemberVrrpOnline_Type.__name__ = "Integer32"
_HwVgmpMemberVrrpOnline_Object = MibTableColumn
hwVgmpMemberVrrpOnline = _HwVgmpMemberVrrpOnline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 5),
    _HwVgmpMemberVrrpOnline_Type()
)
hwVgmpMemberVrrpOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpMemberVrrpOnline.setStatus("current")
_HwVgmpMemberOperRowStatus_Type = RowStatus
_HwVgmpMemberOperRowStatus_Object = MibTableColumn
hwVgmpMemberOperRowStatus = _HwVgmpMemberOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 2, 1, 6),
    _HwVgmpMemberOperRowStatus_Type()
)
hwVgmpMemberOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpMemberOperRowStatus.setStatus("current")
_HwVgmpTrackBFDTable_Object = MibTable
hwVgmpTrackBFDTable = _HwVgmpTrackBFDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3)
)
if mibBuilder.loadTexts:
    hwVgmpTrackBFDTable.setStatus("current")
_HwVgmpTrackBFDEntry_Object = MibTableRow
hwVgmpTrackBFDEntry = _HwVgmpTrackBFDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1)
)
hwVgmpTrackBFDEntry.setIndexNames(
    (0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"),
    (0, "HUAWEI-VGMP-MIB", "hwVgmpTrackBFDID"),
)
if mibBuilder.loadTexts:
    hwVgmpTrackBFDEntry.setStatus("current")


class _HwVgmpTrackBFDID_Type(Integer32):
    """Custom type hwVgmpTrackBFDID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_HwVgmpTrackBFDID_Type.__name__ = "Integer32"
_HwVgmpTrackBFDID_Object = MibTableColumn
hwVgmpTrackBFDID = _HwVgmpTrackBFDID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 1),
    _HwVgmpTrackBFDID_Type()
)
hwVgmpTrackBFDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVgmpTrackBFDID.setStatus("current")


class _HwVgmpTrackBFDReduceValue_Type(Integer32):
    """Custom type hwVgmpTrackBFDReduceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwVgmpTrackBFDReduceValue_Type.__name__ = "Integer32"
_HwVgmpTrackBFDReduceValue_Object = MibTableColumn
hwVgmpTrackBFDReduceValue = _HwVgmpTrackBFDReduceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 2),
    _HwVgmpTrackBFDReduceValue_Type()
)
hwVgmpTrackBFDReduceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpTrackBFDReduceValue.setStatus("current")


class _HwVgmpTrackBFDPreeEnable_Type(Integer32):
    """Custom type hwVgmpTrackBFDPreeEnable based on Integer32"""
    defaultValue = 2

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


_HwVgmpTrackBFDPreeEnable_Type.__name__ = "Integer32"
_HwVgmpTrackBFDPreeEnable_Object = MibTableColumn
hwVgmpTrackBFDPreeEnable = _HwVgmpTrackBFDPreeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 3),
    _HwVgmpTrackBFDPreeEnable_Type()
)
hwVgmpTrackBFDPreeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpTrackBFDPreeEnable.setStatus("current")
_HwVgmpTrackBFDOperRowStatus_Type = RowStatus
_HwVgmpTrackBFDOperRowStatus_Object = MibTableColumn
hwVgmpTrackBFDOperRowStatus = _HwVgmpTrackBFDOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 2, 3, 1, 4),
    _HwVgmpTrackBFDOperRowStatus_Type()
)
hwVgmpTrackBFDOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVgmpTrackBFDOperRowStatus.setStatus("current")
_VgmpStatistics_ObjectIdentity = ObjectIdentity
vgmpStatistics = _VgmpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3)
)
_HwVgmpStatisticTable_Object = MibTable
hwVgmpStatisticTable = _HwVgmpStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1)
)
if mibBuilder.loadTexts:
    hwVgmpStatisticTable.setStatus("current")
_HwVgmpStatisticEntry_Object = MibTableRow
hwVgmpStatisticEntry = _HwVgmpStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1)
)
hwVgmpStatisticEntry.setIndexNames(
    (0, "HUAWEI-VGMP-MIB", "hwVgmpGroupCfgID"),
)
if mibBuilder.loadTexts:
    hwVgmpStatisticEntry.setStatus("current")
_HwVgmpStatisticCheckFailDropNum_Type = Integer32
_HwVgmpStatisticCheckFailDropNum_Object = MibTableColumn
hwVgmpStatisticCheckFailDropNum = _HwVgmpStatisticCheckFailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 1),
    _HwVgmpStatisticCheckFailDropNum_Type()
)
hwVgmpStatisticCheckFailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticCheckFailDropNum.setStatus("current")
_HwVgmpStatisticDisableDropNum_Type = Integer32
_HwVgmpStatisticDisableDropNum_Object = MibTableColumn
hwVgmpStatisticDisableDropNum = _HwVgmpStatisticDisableDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 2),
    _HwVgmpStatisticDisableDropNum_Type()
)
hwVgmpStatisticDisableDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticDisableDropNum.setStatus("current")
_HwVgmpStatisticModeTypeErrDropNum_Type = Integer32
_HwVgmpStatisticModeTypeErrDropNum_Object = MibTableColumn
hwVgmpStatisticModeTypeErrDropNum = _HwVgmpStatisticModeTypeErrDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 3),
    _HwVgmpStatisticModeTypeErrDropNum_Type()
)
hwVgmpStatisticModeTypeErrDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticModeTypeErrDropNum.setStatus("current")
_HwVgmpStatisticAccHelloREQ_Type = Integer32
_HwVgmpStatisticAccHelloREQ_Object = MibTableColumn
hwVgmpStatisticAccHelloREQ = _HwVgmpStatisticAccHelloREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 4),
    _HwVgmpStatisticAccHelloREQ_Type()
)
hwVgmpStatisticAccHelloREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccHelloREQ.setStatus("current")
_HwVgmpStatisticSendHelloREQ_Type = Integer32
_HwVgmpStatisticSendHelloREQ_Object = MibTableColumn
hwVgmpStatisticSendHelloREQ = _HwVgmpStatisticSendHelloREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 5),
    _HwVgmpStatisticSendHelloREQ_Type()
)
hwVgmpStatisticSendHelloREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendHelloREQ.setStatus("current")
_HwVgmpStatisticAccHelloACK_Type = Integer32
_HwVgmpStatisticAccHelloACK_Object = MibTableColumn
hwVgmpStatisticAccHelloACK = _HwVgmpStatisticAccHelloACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 6),
    _HwVgmpStatisticAccHelloACK_Type()
)
hwVgmpStatisticAccHelloACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccHelloACK.setStatus("current")
_HwVgmpStatisticSendHelloACK_Type = Integer32
_HwVgmpStatisticSendHelloACK_Object = MibTableColumn
hwVgmpStatisticSendHelloACK = _HwVgmpStatisticSendHelloACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 7),
    _HwVgmpStatisticSendHelloACK_Type()
)
hwVgmpStatisticSendHelloACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendHelloACK.setStatus("current")
_HwVgmpStatisticAccMasterToSlaveREQ_Type = Integer32
_HwVgmpStatisticAccMasterToSlaveREQ_Object = MibTableColumn
hwVgmpStatisticAccMasterToSlaveREQ = _HwVgmpStatisticAccMasterToSlaveREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 8),
    _HwVgmpStatisticAccMasterToSlaveREQ_Type()
)
hwVgmpStatisticAccMasterToSlaveREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccMasterToSlaveREQ.setStatus("current")
_HwVgmpStatisticSendMasterToSlaveREQ_Type = Integer32
_HwVgmpStatisticSendMasterToSlaveREQ_Object = MibTableColumn
hwVgmpStatisticSendMasterToSlaveREQ = _HwVgmpStatisticSendMasterToSlaveREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 9),
    _HwVgmpStatisticSendMasterToSlaveREQ_Type()
)
hwVgmpStatisticSendMasterToSlaveREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendMasterToSlaveREQ.setStatus("current")
_HwVgmpStatisticAccMasterToSlaveACK_Type = Integer32
_HwVgmpStatisticAccMasterToSlaveACK_Object = MibTableColumn
hwVgmpStatisticAccMasterToSlaveACK = _HwVgmpStatisticAccMasterToSlaveACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 10),
    _HwVgmpStatisticAccMasterToSlaveACK_Type()
)
hwVgmpStatisticAccMasterToSlaveACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccMasterToSlaveACK.setStatus("current")
_HwVgmpStatisticSendMasterToSlaveACK_Type = Integer32
_HwVgmpStatisticSendMasterToSlaveACK_Object = MibTableColumn
hwVgmpStatisticSendMasterToSlaveACK = _HwVgmpStatisticSendMasterToSlaveACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 11),
    _HwVgmpStatisticSendMasterToSlaveACK_Type()
)
hwVgmpStatisticSendMasterToSlaveACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendMasterToSlaveACK.setStatus("current")
_HwVgmpStatisticAccMasterToSlaveNACK_Type = Integer32
_HwVgmpStatisticAccMasterToSlaveNACK_Object = MibTableColumn
hwVgmpStatisticAccMasterToSlaveNACK = _HwVgmpStatisticAccMasterToSlaveNACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 12),
    _HwVgmpStatisticAccMasterToSlaveNACK_Type()
)
hwVgmpStatisticAccMasterToSlaveNACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccMasterToSlaveNACK.setStatus("current")
_HwVgmpStatisticSendMasterToSlaveNACK_Type = Integer32
_HwVgmpStatisticSendMasterToSlaveNACK_Object = MibTableColumn
hwVgmpStatisticSendMasterToSlaveNACK = _HwVgmpStatisticSendMasterToSlaveNACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 13),
    _HwVgmpStatisticSendMasterToSlaveNACK_Type()
)
hwVgmpStatisticSendMasterToSlaveNACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendMasterToSlaveNACK.setStatus("current")
_HwVgmpStatisticAccSlaveToMasterREQ_Type = Integer32
_HwVgmpStatisticAccSlaveToMasterREQ_Object = MibTableColumn
hwVgmpStatisticAccSlaveToMasterREQ = _HwVgmpStatisticAccSlaveToMasterREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 14),
    _HwVgmpStatisticAccSlaveToMasterREQ_Type()
)
hwVgmpStatisticAccSlaveToMasterREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccSlaveToMasterREQ.setStatus("current")
_HwVgmpStatisticSendSlaveToMasterREQ_Type = Integer32
_HwVgmpStatisticSendSlaveToMasterREQ_Object = MibTableColumn
hwVgmpStatisticSendSlaveToMasterREQ = _HwVgmpStatisticSendSlaveToMasterREQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 15),
    _HwVgmpStatisticSendSlaveToMasterREQ_Type()
)
hwVgmpStatisticSendSlaveToMasterREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendSlaveToMasterREQ.setStatus("current")
_HwVgmpStatisticAccSlaveToMasterACK_Type = Integer32
_HwVgmpStatisticAccSlaveToMasterACK_Object = MibTableColumn
hwVgmpStatisticAccSlaveToMasterACK = _HwVgmpStatisticAccSlaveToMasterACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 16),
    _HwVgmpStatisticAccSlaveToMasterACK_Type()
)
hwVgmpStatisticAccSlaveToMasterACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccSlaveToMasterACK.setStatus("current")
_HwVgmpStatisticSendSlaveToMasterACK_Type = Integer32
_HwVgmpStatisticSendSlaveToMasterACK_Object = MibTableColumn
hwVgmpStatisticSendSlaveToMasterACK = _HwVgmpStatisticSendSlaveToMasterACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 17),
    _HwVgmpStatisticSendSlaveToMasterACK_Type()
)
hwVgmpStatisticSendSlaveToMasterACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendSlaveToMasterACK.setStatus("current")
_HwVgmpStatisticAccSlaveToMasterNACK_Type = Integer32
_HwVgmpStatisticAccSlaveToMasterNACK_Object = MibTableColumn
hwVgmpStatisticAccSlaveToMasterNACK = _HwVgmpStatisticAccSlaveToMasterNACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 18),
    _HwVgmpStatisticAccSlaveToMasterNACK_Type()
)
hwVgmpStatisticAccSlaveToMasterNACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticAccSlaveToMasterNACK.setStatus("current")
_HwVgmpStatisticSendSlaveToMasterNACK_Type = Integer32
_HwVgmpStatisticSendSlaveToMasterNACK_Object = MibTableColumn
hwVgmpStatisticSendSlaveToMasterNACK = _HwVgmpStatisticSendSlaveToMasterNACK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 3, 1, 1, 19),
    _HwVgmpStatisticSendSlaveToMasterNACK_Type()
)
hwVgmpStatisticSendSlaveToMasterNACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVgmpStatisticSendSlaveToMasterNACK.setStatus("current")
_VgmpConformance_ObjectIdentity = ObjectIdentity
vgmpConformance = _VgmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4)
)
_HwVGMPMIBCompliances_ObjectIdentity = ObjectIdentity
hwVGMPMIBCompliances = _HwVGMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1)
)
_HwVGMPMIBGroups_ObjectIdentity = ObjectIdentity
hwVGMPMIBGroups = _HwVGMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1)
)

# Managed Objects groups

hwVGMPGroAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 1)
)
hwVGMPGroAttrGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgEnable"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPri"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgUseVrrpPri"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPriPlusValue"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPreemptEnable"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPreemptDelayValue"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgHelloInterval"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgSendEnable"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgRunPri"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgCreateTime"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgLastChangeTime"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgPeerState"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgVrrpNum"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgReset"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgOperRowStatus"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
)
if mibBuilder.loadTexts:
    hwVGMPGroAttrGroup.setStatus("current")

hwVGMPMenAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 2)
)
hwVGMPMenAttrGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpMemberData"),
        ("HUAWEI-VGMP-MIB", "hwVgmpMemberTran"),
        ("HUAWEI-VGMP-MIB", "hwVgmpMemberVrrpOnline"),
        ("HUAWEI-VGMP-MIB", "hwVgmpMemberOperRowStatus"))
)
if mibBuilder.loadTexts:
    hwVGMPMenAttrGroup.setStatus("current")

hwVGMPBFDSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 3)
)
hwVGMPBFDSessionGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDReduceValue"),
        ("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDPreeEnable"),
        ("HUAWEI-VGMP-MIB", "hwVgmpTrackBFDOperRowStatus"))
)
if mibBuilder.loadTexts:
    hwVGMPBFDSessionGroup.setStatus("current")

hwVGMPStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 4)
)
hwVGMPStaticGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpStatisticCheckFailDropNum"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticDisableDropNum"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticModeTypeErrDropNum"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccHelloREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendHelloREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccHelloACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendHelloACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccMasterToSlaveNACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendMasterToSlaveNACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterREQ"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticAccSlaveToMasterNACK"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStatisticSendSlaveToMasterNACK"))
)
if mibBuilder.loadTexts:
    hwVGMPStaticGroup.setStatus("current")

hwVGMPGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 5)
)
hwVGMPGlobalsGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpTrapSnmpCtrl"),
        ("HUAWEI-VGMP-MIB", "hwVgmpStrictCheck"))
)
if mibBuilder.loadTexts:
    hwVGMPGlobalsGroup.setStatus("current")


# Notification objects

hwVgmpOtherStateToMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1, 1)
)
hwVgmpOtherStateToMaster.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
)
if mibBuilder.loadTexts:
    hwVgmpOtherStateToMaster.setStatus(
        "current"
    )

hwVgmpMasterToOtherState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 1, 2)
)
hwVgmpMasterToOtherState.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgState"),
        ("HUAWEI-VGMP-MIB", "hwVgmpGroupCfgNextState"))
)
if mibBuilder.loadTexts:
    hwVgmpMasterToOtherState.setStatus(
        "current"
    )


# Notifications groups

hwVGMPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 122, 4, 1, 1, 6)
)
hwVGMPNotificationGroup.setObjects(
      *(("HUAWEI-VGMP-MIB", "hwVgmpOtherStateToMaster"),
        ("HUAWEI-VGMP-MIB", "hwVgmpMasterToOtherState"))
)
if mibBuilder.loadTexts:
    hwVGMPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VGMP-MIB",
    **{"hwVgmpMib": hwVgmpMib,
       "vgmpGlobalCtrl": vgmpGlobalCtrl,
       "hwVgmpTrapSnmpCtrl": hwVgmpTrapSnmpCtrl,
       "hwVgmpStrictCheck": hwVgmpStrictCheck,
       "vgmpNotifications": vgmpNotifications,
       "hwVgmpOtherStateToMaster": hwVgmpOtherStateToMaster,
       "hwVgmpMasterToOtherState": hwVgmpMasterToOtherState,
       "vgmpOperations": vgmpOperations,
       "hwVgmpGroupCfgTable": hwVgmpGroupCfgTable,
       "hwVgmpGroupCfgEntry": hwVgmpGroupCfgEntry,
       "hwVgmpGroupCfgID": hwVgmpGroupCfgID,
       "hwVgmpGroupCfgEnable": hwVgmpGroupCfgEnable,
       "hwVgmpGroupCfgPri": hwVgmpGroupCfgPri,
       "hwVgmpGroupCfgUseVrrpPri": hwVgmpGroupCfgUseVrrpPri,
       "hwVgmpGroupCfgPriPlusValue": hwVgmpGroupCfgPriPlusValue,
       "hwVgmpGroupCfgPreemptEnable": hwVgmpGroupCfgPreemptEnable,
       "hwVgmpGroupCfgPreemptDelayValue": hwVgmpGroupCfgPreemptDelayValue,
       "hwVgmpGroupCfgHelloInterval": hwVgmpGroupCfgHelloInterval,
       "hwVgmpGroupCfgSendEnable": hwVgmpGroupCfgSendEnable,
       "hwVgmpGroupCfgState": hwVgmpGroupCfgState,
       "hwVgmpGroupCfgRunPri": hwVgmpGroupCfgRunPri,
       "hwVgmpGroupCfgCreateTime": hwVgmpGroupCfgCreateTime,
       "hwVgmpGroupCfgLastChangeTime": hwVgmpGroupCfgLastChangeTime,
       "hwVgmpGroupCfgPeerState": hwVgmpGroupCfgPeerState,
       "hwVgmpGroupCfgVrrpNum": hwVgmpGroupCfgVrrpNum,
       "hwVgmpGroupCfgReset": hwVgmpGroupCfgReset,
       "hwVgmpGroupCfgOperRowStatus": hwVgmpGroupCfgOperRowStatus,
       "hwVgmpGroupCfgNextState": hwVgmpGroupCfgNextState,
       "hwVgmpMemberTable": hwVgmpMemberTable,
       "hwVgmpMemberEntry": hwVgmpMemberEntry,
       "hwVgmpMemberIfIndex": hwVgmpMemberIfIndex,
       "hwVgmpMemberVRID": hwVgmpMemberVRID,
       "hwVgmpMemberData": hwVgmpMemberData,
       "hwVgmpMemberTran": hwVgmpMemberTran,
       "hwVgmpMemberVrrpOnline": hwVgmpMemberVrrpOnline,
       "hwVgmpMemberOperRowStatus": hwVgmpMemberOperRowStatus,
       "hwVgmpTrackBFDTable": hwVgmpTrackBFDTable,
       "hwVgmpTrackBFDEntry": hwVgmpTrackBFDEntry,
       "hwVgmpTrackBFDID": hwVgmpTrackBFDID,
       "hwVgmpTrackBFDReduceValue": hwVgmpTrackBFDReduceValue,
       "hwVgmpTrackBFDPreeEnable": hwVgmpTrackBFDPreeEnable,
       "hwVgmpTrackBFDOperRowStatus": hwVgmpTrackBFDOperRowStatus,
       "vgmpStatistics": vgmpStatistics,
       "hwVgmpStatisticTable": hwVgmpStatisticTable,
       "hwVgmpStatisticEntry": hwVgmpStatisticEntry,
       "hwVgmpStatisticCheckFailDropNum": hwVgmpStatisticCheckFailDropNum,
       "hwVgmpStatisticDisableDropNum": hwVgmpStatisticDisableDropNum,
       "hwVgmpStatisticModeTypeErrDropNum": hwVgmpStatisticModeTypeErrDropNum,
       "hwVgmpStatisticAccHelloREQ": hwVgmpStatisticAccHelloREQ,
       "hwVgmpStatisticSendHelloREQ": hwVgmpStatisticSendHelloREQ,
       "hwVgmpStatisticAccHelloACK": hwVgmpStatisticAccHelloACK,
       "hwVgmpStatisticSendHelloACK": hwVgmpStatisticSendHelloACK,
       "hwVgmpStatisticAccMasterToSlaveREQ": hwVgmpStatisticAccMasterToSlaveREQ,
       "hwVgmpStatisticSendMasterToSlaveREQ": hwVgmpStatisticSendMasterToSlaveREQ,
       "hwVgmpStatisticAccMasterToSlaveACK": hwVgmpStatisticAccMasterToSlaveACK,
       "hwVgmpStatisticSendMasterToSlaveACK": hwVgmpStatisticSendMasterToSlaveACK,
       "hwVgmpStatisticAccMasterToSlaveNACK": hwVgmpStatisticAccMasterToSlaveNACK,
       "hwVgmpStatisticSendMasterToSlaveNACK": hwVgmpStatisticSendMasterToSlaveNACK,
       "hwVgmpStatisticAccSlaveToMasterREQ": hwVgmpStatisticAccSlaveToMasterREQ,
       "hwVgmpStatisticSendSlaveToMasterREQ": hwVgmpStatisticSendSlaveToMasterREQ,
       "hwVgmpStatisticAccSlaveToMasterACK": hwVgmpStatisticAccSlaveToMasterACK,
       "hwVgmpStatisticSendSlaveToMasterACK": hwVgmpStatisticSendSlaveToMasterACK,
       "hwVgmpStatisticAccSlaveToMasterNACK": hwVgmpStatisticAccSlaveToMasterNACK,
       "hwVgmpStatisticSendSlaveToMasterNACK": hwVgmpStatisticSendSlaveToMasterNACK,
       "vgmpConformance": vgmpConformance,
       "hwVGMPMIBCompliances": hwVGMPMIBCompliances,
       "hwVGMPMIBGroups": hwVGMPMIBGroups,
       "hwVGMPGroAttrGroup": hwVGMPGroAttrGroup,
       "hwVGMPMenAttrGroup": hwVGMPMenAttrGroup,
       "hwVGMPBFDSessionGroup": hwVGMPBFDSessionGroup,
       "hwVGMPStaticGroup": hwVGMPStaticGroup,
       "hwVGMPGlobalsGroup": hwVGMPGlobalsGroup,
       "hwVGMPNotificationGroup": hwVGMPNotificationGroup}
)
