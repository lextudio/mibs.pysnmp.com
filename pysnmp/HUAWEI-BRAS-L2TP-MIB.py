# SNMP MIB module (HUAWEI-BRAS-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:01 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

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


# MODULE-IDENTITY

hwBRASL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2tpMibObjects_ObjectIdentity = ObjectIdentity
hwL2tpMibObjects = _HwL2tpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1)
)
_HwL2tpConfigTable_ObjectIdentity = ObjectIdentity
hwL2tpConfigTable = _HwL2tpConfigTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1)
)
_HwL2tpEnableStatus_Type = TruthValue
_HwL2tpEnableStatus_Object = MibScalar
hwL2tpEnableStatus = _HwL2tpEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1, 1),
    _HwL2tpEnableStatus_Type()
)
hwL2tpEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpEnableStatus.setStatus("current")


class _HwL2tpTunnelClearLocalID_Type(Integer32):
    """Custom type hwL2tpTunnelClearLocalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelClearLocalID_Type.__name__ = "Integer32"
_HwL2tpTunnelClearLocalID_Object = MibScalar
hwL2tpTunnelClearLocalID = _HwL2tpTunnelClearLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1, 2),
    _HwL2tpTunnelClearLocalID_Type()
)
hwL2tpTunnelClearLocalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelClearLocalID.setStatus("current")


class _HwL2tpTunnelClearRemoteName_Type(OctetString):
    """Custom type hwL2tpTunnelClearRemoteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwL2tpTunnelClearRemoteName_Type.__name__ = "OctetString"
_HwL2tpTunnelClearRemoteName_Object = MibScalar
hwL2tpTunnelClearRemoteName = _HwL2tpTunnelClearRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1, 3),
    _HwL2tpTunnelClearRemoteName_Type()
)
hwL2tpTunnelClearRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelClearRemoteName.setStatus("current")


class _HwL2tpTunnelClearSlotID_Type(Integer32):
    """Custom type hwL2tpTunnelClearSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwL2tpTunnelClearSlotID_Type.__name__ = "Integer32"
_HwL2tpTunnelClearSlotID_Object = MibScalar
hwL2tpTunnelClearSlotID = _HwL2tpTunnelClearSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1, 4),
    _HwL2tpTunnelClearSlotID_Type()
)
hwL2tpTunnelClearSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelClearSlotID.setStatus("current")


class _HwL2tpAging_Type(Integer32):
    """Custom type hwL2tpAging based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwL2tpAging_Type.__name__ = "Integer32"
_HwL2tpAging_Object = MibScalar
hwL2tpAging = _HwL2tpAging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 1, 5),
    _HwL2tpAging_Type()
)
hwL2tpAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpAging.setStatus("current")
_HwL2tpGroupConfigTable_Object = MibTable
hwL2tpGroupConfigTable = _HwL2tpGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigTable.setStatus("current")
_HwL2tpGroupConfigEntry_Object = MibTableRow
hwL2tpGroupConfigEntry = _HwL2tpGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1)
)
hwL2tpGroupConfigEntry.setIndexNames(
    (0, "HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupindex"),
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigEntry.setStatus("current")


class _HwL2tpGroupindex_Type(Integer32):
    """Custom type hwL2tpGroupindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwL2tpGroupindex_Type.__name__ = "Integer32"
_HwL2tpGroupindex_Object = MibTableColumn
hwL2tpGroupindex = _HwL2tpGroupindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 1),
    _HwL2tpGroupindex_Type()
)
hwL2tpGroupindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpGroupindex.setStatus("current")


class _HwL2tpGroupAuthentication_Type(TruthValue):
    """Custom type hwL2tpGroupAuthentication based on TruthValue"""


_HwL2tpGroupAuthentication_Object = MibTableColumn
hwL2tpGroupAuthentication = _HwL2tpGroupAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 2),
    _HwL2tpGroupAuthentication_Type()
)
hwL2tpGroupAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupAuthentication.setStatus("current")


class _HwL2tpGroupAvpHidden_Type(TruthValue):
    """Custom type hwL2tpGroupAvpHidden based on TruthValue"""


_HwL2tpGroupAvpHidden_Object = MibTableColumn
hwL2tpGroupAvpHidden = _HwL2tpGroupAvpHidden_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 3),
    _HwL2tpGroupAvpHidden_Type()
)
hwL2tpGroupAvpHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupAvpHidden.setStatus("current")


class _HwL2tpGroupLoadShare_Type(TruthValue):
    """Custom type hwL2tpGroupLoadShare based on TruthValue"""


_HwL2tpGroupLoadShare_Object = MibTableColumn
hwL2tpGroupLoadShare = _HwL2tpGroupLoadShare_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 4),
    _HwL2tpGroupLoadShare_Type()
)
hwL2tpGroupLoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLoadShare.setStatus("current")


class _HwL2tpTunnelName_Type(OctetString):
    """Custom type hwL2tpTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwL2tpTunnelName_Type.__name__ = "OctetString"
_HwL2tpTunnelName_Object = MibTableColumn
hwL2tpTunnelName = _HwL2tpTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 5),
    _HwL2tpTunnelName_Type()
)
hwL2tpTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelName.setStatus("current")


class _HwL2tpGroupRetransmit_Type(Integer32):
    """Custom type hwL2tpGroupRetransmit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupRetransmit_Type.__name__ = "Integer32"
_HwL2tpGroupRetransmit_Object = MibTableColumn
hwL2tpGroupRetransmit = _HwL2tpGroupRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 6),
    _HwL2tpGroupRetransmit_Type()
)
hwL2tpGroupRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRetransmit.setStatus("current")


class _HwL2tpGroupTimeout_Type(Integer32):
    """Custom type hwL2tpGroupTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupTimeout_Type.__name__ = "Integer32"
_HwL2tpGroupTimeout_Object = MibTableColumn
hwL2tpGroupTimeout = _HwL2tpGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 7),
    _HwL2tpGroupTimeout_Type()
)
hwL2tpGroupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTimeout.setStatus("current")


class _HwL2tpGroupTimer_Type(Integer32):
    """Custom type hwL2tpGroupTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_HwL2tpGroupTimer_Type.__name__ = "Integer32"
_HwL2tpGroupTimer_Object = MibTableColumn
hwL2tpGroupTimer = _HwL2tpGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 8),
    _HwL2tpGroupTimer_Type()
)
hwL2tpGroupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTimer.setStatus("current")


class _HwL2tpGroupPassWord_Type(OctetString):
    """Custom type hwL2tpGroupPassWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord_Object = MibTableColumn
hwL2tpGroupPassWord = _HwL2tpGroupPassWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 9),
    _HwL2tpGroupPassWord_Type()
)
hwL2tpGroupPassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord.setStatus("current")
_HwL2tpGroupLnsIP1_Type = IpAddress
_HwL2tpGroupLnsIP1_Object = MibTableColumn
hwL2tpGroupLnsIP1 = _HwL2tpGroupLnsIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 10),
    _HwL2tpGroupLnsIP1_Type()
)
hwL2tpGroupLnsIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP1.setStatus("current")


class _HwL2tpGroupLnsWeight1_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight1 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight1_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight1_Object = MibTableColumn
hwL2tpGroupLnsWeight1 = _HwL2tpGroupLnsWeight1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 11),
    _HwL2tpGroupLnsWeight1_Type()
)
hwL2tpGroupLnsWeight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight1.setStatus("current")
_HwL2tpGroupLnsIP2_Type = IpAddress
_HwL2tpGroupLnsIP2_Object = MibTableColumn
hwL2tpGroupLnsIP2 = _HwL2tpGroupLnsIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 12),
    _HwL2tpGroupLnsIP2_Type()
)
hwL2tpGroupLnsIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP2.setStatus("current")


class _HwL2tpGroupLnsWeight2_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight2_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight2_Object = MibTableColumn
hwL2tpGroupLnsWeight2 = _HwL2tpGroupLnsWeight2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 13),
    _HwL2tpGroupLnsWeight2_Type()
)
hwL2tpGroupLnsWeight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight2.setStatus("current")
_HwL2tpGroupLnsIP3_Type = IpAddress
_HwL2tpGroupLnsIP3_Object = MibTableColumn
hwL2tpGroupLnsIP3 = _HwL2tpGroupLnsIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 14),
    _HwL2tpGroupLnsIP3_Type()
)
hwL2tpGroupLnsIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP3.setStatus("current")


class _HwL2tpGroupLnsWeight3_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight3 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight3_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight3_Object = MibTableColumn
hwL2tpGroupLnsWeight3 = _HwL2tpGroupLnsWeight3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 15),
    _HwL2tpGroupLnsWeight3_Type()
)
hwL2tpGroupLnsWeight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight3.setStatus("current")
_HwL2tpGroupLnsIP4_Type = IpAddress
_HwL2tpGroupLnsIP4_Object = MibTableColumn
hwL2tpGroupLnsIP4 = _HwL2tpGroupLnsIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 16),
    _HwL2tpGroupLnsIP4_Type()
)
hwL2tpGroupLnsIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP4.setStatus("current")


class _HwL2tpGroupLnsWeight4_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight4 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight4_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight4_Object = MibTableColumn
hwL2tpGroupLnsWeight4 = _HwL2tpGroupLnsWeight4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 17),
    _HwL2tpGroupLnsWeight4_Type()
)
hwL2tpGroupLnsWeight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight4.setStatus("current")
_HwL2tpGroupLnsIP5_Type = IpAddress
_HwL2tpGroupLnsIP5_Object = MibTableColumn
hwL2tpGroupLnsIP5 = _HwL2tpGroupLnsIP5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 18),
    _HwL2tpGroupLnsIP5_Type()
)
hwL2tpGroupLnsIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP5.setStatus("current")


class _HwL2tpGroupLnsWeight5_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight5 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight5_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight5_Object = MibTableColumn
hwL2tpGroupLnsWeight5 = _HwL2tpGroupLnsWeight5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 19),
    _HwL2tpGroupLnsWeight5_Type()
)
hwL2tpGroupLnsWeight5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight5.setStatus("current")
_HwL2tpGroupRowStatus_Type = RowStatus
_HwL2tpGroupRowStatus_Object = MibTableColumn
hwL2tpGroupRowStatus = _HwL2tpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 20),
    _HwL2tpGroupRowStatus_Type()
)
hwL2tpGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRowStatus.setStatus("current")


class _HwL2tpGroupName_Type(OctetString):
    """Custom type hwL2tpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwL2tpGroupName_Type.__name__ = "OctetString"
_HwL2tpGroupName_Object = MibTableColumn
hwL2tpGroupName = _HwL2tpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 21),
    _HwL2tpGroupName_Type()
)
hwL2tpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupName.setStatus("current")


class _HwL2tpGroupRadiusAuth_Type(TruthValue):
    """Custom type hwL2tpGroupRadiusAuth based on TruthValue"""


_HwL2tpGroupRadiusAuth_Object = MibTableColumn
hwL2tpGroupRadiusAuth = _HwL2tpGroupRadiusAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 22),
    _HwL2tpGroupRadiusAuth_Type()
)
hwL2tpGroupRadiusAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRadiusAuth.setStatus("current")


class _HwL2tpGroupAging_Type(Integer32):
    """Custom type hwL2tpGroupAging based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwL2tpGroupAging_Type.__name__ = "Integer32"
_HwL2tpGroupAging_Object = MibTableColumn
hwL2tpGroupAging = _HwL2tpGroupAging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 23),
    _HwL2tpGroupAging_Type()
)
hwL2tpGroupAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupAging.setStatus("obsolete")


class _HwL2tpGroupRemoteName_Type(OctetString):
    """Custom type hwL2tpGroupRemoteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpGroupRemoteName_Type.__name__ = "OctetString"
_HwL2tpGroupRemoteName_Object = MibTableColumn
hwL2tpGroupRemoteName = _HwL2tpGroupRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 24),
    _HwL2tpGroupRemoteName_Type()
)
hwL2tpGroupRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupRemoteName.setStatus("current")


class _HwL2tpGroupForceChap_Type(TruthValue):
    """Custom type hwL2tpGroupForceChap based on TruthValue"""


_HwL2tpGroupForceChap_Object = MibTableColumn
hwL2tpGroupForceChap = _HwL2tpGroupForceChap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 25),
    _HwL2tpGroupForceChap_Type()
)
hwL2tpGroupForceChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupForceChap.setStatus("current")


class _HwL2tpGroupForceLcp_Type(TruthValue):
    """Custom type hwL2tpGroupForceLcp based on TruthValue"""


_HwL2tpGroupForceLcp_Object = MibTableColumn
hwL2tpGroupForceLcp = _HwL2tpGroupForceLcp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 26),
    _HwL2tpGroupForceLcp_Type()
)
hwL2tpGroupForceLcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupForceLcp.setStatus("current")


class _HwL2tpGroupVt_Type(Integer32):
    """Custom type hwL2tpGroupVt based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_HwL2tpGroupVt_Type.__name__ = "Integer32"
_HwL2tpGroupVt_Object = MibTableColumn
hwL2tpGroupVt = _HwL2tpGroupVt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 27),
    _HwL2tpGroupVt_Type()
)
hwL2tpGroupVt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupVt.setStatus("current")


class _HwL2tpGroupaaaAuthentication_Type(TruthValue):
    """Custom type hwL2tpGroupaaaAuthentication based on TruthValue"""


_HwL2tpGroupaaaAuthentication_Object = MibTableColumn
hwL2tpGroupaaaAuthentication = _HwL2tpGroupaaaAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 28),
    _HwL2tpGroupaaaAuthentication_Type()
)
hwL2tpGroupaaaAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupaaaAuthentication.setStatus("current")


class _HwL2tpIdleCutTimer_Type(Integer32):
    """Custom type hwL2tpIdleCutTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_HwL2tpIdleCutTimer_Type.__name__ = "Integer32"
_HwL2tpIdleCutTimer_Object = MibTableColumn
hwL2tpIdleCutTimer = _HwL2tpIdleCutTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 29),
    _HwL2tpIdleCutTimer_Type()
)
hwL2tpIdleCutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpIdleCutTimer.setStatus("current")
_HwL2tpGroupTunnelStartLnsIP1_Type = IpAddress
_HwL2tpGroupTunnelStartLnsIP1_Object = MibTableColumn
hwL2tpGroupTunnelStartLnsIP1 = _HwL2tpGroupTunnelStartLnsIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 30),
    _HwL2tpGroupTunnelStartLnsIP1_Type()
)
hwL2tpGroupTunnelStartLnsIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTunnelStartLnsIP1.setStatus("obsolete")
_HwL2tpGroupTunnelStartLnsIP2_Type = IpAddress
_HwL2tpGroupTunnelStartLnsIP2_Object = MibTableColumn
hwL2tpGroupTunnelStartLnsIP2 = _HwL2tpGroupTunnelStartLnsIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 31),
    _HwL2tpGroupTunnelStartLnsIP2_Type()
)
hwL2tpGroupTunnelStartLnsIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTunnelStartLnsIP2.setStatus("obsolete")
_HwL2tpGroupTunnelStartLnsIP3_Type = IpAddress
_HwL2tpGroupTunnelStartLnsIP3_Object = MibTableColumn
hwL2tpGroupTunnelStartLnsIP3 = _HwL2tpGroupTunnelStartLnsIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 32),
    _HwL2tpGroupTunnelStartLnsIP3_Type()
)
hwL2tpGroupTunnelStartLnsIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTunnelStartLnsIP3.setStatus("obsolete")
_HwL2tpGroupTunnelStartLnsIP4_Type = IpAddress
_HwL2tpGroupTunnelStartLnsIP4_Object = MibTableColumn
hwL2tpGroupTunnelStartLnsIP4 = _HwL2tpGroupTunnelStartLnsIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 33),
    _HwL2tpGroupTunnelStartLnsIP4_Type()
)
hwL2tpGroupTunnelStartLnsIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTunnelStartLnsIP4.setStatus("obsolete")
_HwL2tpGroupTunnelStartLnsIP5_Type = IpAddress
_HwL2tpGroupTunnelStartLnsIP5_Object = MibTableColumn
hwL2tpGroupTunnelStartLnsIP5 = _HwL2tpGroupTunnelStartLnsIP5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 34),
    _HwL2tpGroupTunnelStartLnsIP5_Type()
)
hwL2tpGroupTunnelStartLnsIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupTunnelStartLnsIP5.setStatus("obsolete")


class _HwL2tpGroupFlag_Type(Integer32):
    """Custom type hwL2tpGroupFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwL2tpGroupFlag_Type.__name__ = "Integer32"
_HwL2tpGroupFlag_Object = MibTableColumn
hwL2tpGroupFlag = _HwL2tpGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 35),
    _HwL2tpGroupFlag_Type()
)
hwL2tpGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpGroupFlag.setStatus("current")
_HwL2tpGroupLnsIP6_Type = IpAddress
_HwL2tpGroupLnsIP6_Object = MibTableColumn
hwL2tpGroupLnsIP6 = _HwL2tpGroupLnsIP6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 36),
    _HwL2tpGroupLnsIP6_Type()
)
hwL2tpGroupLnsIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP6.setStatus("current")


class _HwL2tpGroupLnsWeight6_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight6 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight6_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight6_Object = MibTableColumn
hwL2tpGroupLnsWeight6 = _HwL2tpGroupLnsWeight6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 37),
    _HwL2tpGroupLnsWeight6_Type()
)
hwL2tpGroupLnsWeight6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight6.setStatus("current")
_HwL2tpGroupLnsIP7_Type = IpAddress
_HwL2tpGroupLnsIP7_Object = MibTableColumn
hwL2tpGroupLnsIP7 = _HwL2tpGroupLnsIP7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 38),
    _HwL2tpGroupLnsIP7_Type()
)
hwL2tpGroupLnsIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP7.setStatus("current")


class _HwL2tpGroupLnsWeight7_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight7 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight7_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight7_Object = MibTableColumn
hwL2tpGroupLnsWeight7 = _HwL2tpGroupLnsWeight7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 39),
    _HwL2tpGroupLnsWeight7_Type()
)
hwL2tpGroupLnsWeight7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight7.setStatus("current")
_HwL2tpGroupLnsIP8_Type = IpAddress
_HwL2tpGroupLnsIP8_Object = MibTableColumn
hwL2tpGroupLnsIP8 = _HwL2tpGroupLnsIP8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 40),
    _HwL2tpGroupLnsIP8_Type()
)
hwL2tpGroupLnsIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsIP8.setStatus("current")


class _HwL2tpGroupLnsWeight8_Type(Integer32):
    """Custom type hwL2tpGroupLnsWeight8 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwL2tpGroupLnsWeight8_Type.__name__ = "Integer32"
_HwL2tpGroupLnsWeight8_Object = MibTableColumn
hwL2tpGroupLnsWeight8 = _HwL2tpGroupLnsWeight8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 41),
    _HwL2tpGroupLnsWeight8_Type()
)
hwL2tpGroupLnsWeight8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupLnsWeight8.setStatus("current")


class _HwL2tpAvp46_Type(TruthValue):
    """Custom type hwL2tpAvp46 based on TruthValue"""


_HwL2tpAvp46_Object = MibTableColumn
hwL2tpAvp46 = _HwL2tpAvp46_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 42),
    _HwL2tpAvp46_Type()
)
hwL2tpAvp46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpAvp46.setStatus("current")


class _HwL2tpGroupDefaultDomain_Type(OctetString):
    """Custom type hwL2tpGroupDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_HwL2tpGroupDefaultDomain_Type.__name__ = "OctetString"
_HwL2tpGroupDefaultDomain_Object = MibTableColumn
hwL2tpGroupDefaultDomain = _HwL2tpGroupDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 43),
    _HwL2tpGroupDefaultDomain_Type()
)
hwL2tpGroupDefaultDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupDefaultDomain.setStatus("current")


class _HwL2tpGroupPassWord1_Type(OctetString):
    """Custom type hwL2tpGroupPassWord1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord1_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord1_Object = MibTableColumn
hwL2tpGroupPassWord1 = _HwL2tpGroupPassWord1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 44),
    _HwL2tpGroupPassWord1_Type()
)
hwL2tpGroupPassWord1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord1.setStatus("current")


class _HwL2tpGroupPassWord2_Type(OctetString):
    """Custom type hwL2tpGroupPassWord2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord2_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord2_Object = MibTableColumn
hwL2tpGroupPassWord2 = _HwL2tpGroupPassWord2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 45),
    _HwL2tpGroupPassWord2_Type()
)
hwL2tpGroupPassWord2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord2.setStatus("current")


class _HwL2tpGroupPassWord3_Type(OctetString):
    """Custom type hwL2tpGroupPassWord3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord3_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord3_Object = MibTableColumn
hwL2tpGroupPassWord3 = _HwL2tpGroupPassWord3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 46),
    _HwL2tpGroupPassWord3_Type()
)
hwL2tpGroupPassWord3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord3.setStatus("current")


class _HwL2tpGroupPassWord4_Type(OctetString):
    """Custom type hwL2tpGroupPassWord4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord4_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord4_Object = MibTableColumn
hwL2tpGroupPassWord4 = _HwL2tpGroupPassWord4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 47),
    _HwL2tpGroupPassWord4_Type()
)
hwL2tpGroupPassWord4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord4.setStatus("current")


class _HwL2tpGroupPassWord5_Type(OctetString):
    """Custom type hwL2tpGroupPassWord5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord5_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord5_Object = MibTableColumn
hwL2tpGroupPassWord5 = _HwL2tpGroupPassWord5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 48),
    _HwL2tpGroupPassWord5_Type()
)
hwL2tpGroupPassWord5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord5.setStatus("current")


class _HwL2tpGroupPassWord6_Type(OctetString):
    """Custom type hwL2tpGroupPassWord6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord6_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord6_Object = MibTableColumn
hwL2tpGroupPassWord6 = _HwL2tpGroupPassWord6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 49),
    _HwL2tpGroupPassWord6_Type()
)
hwL2tpGroupPassWord6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord6.setStatus("current")


class _HwL2tpGroupPassWord7_Type(OctetString):
    """Custom type hwL2tpGroupPassWord7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord7_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord7_Object = MibTableColumn
hwL2tpGroupPassWord7 = _HwL2tpGroupPassWord7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 50),
    _HwL2tpGroupPassWord7_Type()
)
hwL2tpGroupPassWord7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord7.setStatus("current")


class _HwL2tpGroupPassWord8_Type(OctetString):
    """Custom type hwL2tpGroupPassWord8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2tpGroupPassWord8_Type.__name__ = "OctetString"
_HwL2tpGroupPassWord8_Object = MibTableColumn
hwL2tpGroupPassWord8 = _HwL2tpGroupPassWord8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 51),
    _HwL2tpGroupPassWord8_Type()
)
hwL2tpGroupPassWord8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupPassWord8.setStatus("current")


class _HwL2tpGroupDomainAuthMode_Type(Integer32):
    """Custom type hwL2tpGroupDomainAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("force", 2),
          ("replace", 3))
    )


_HwL2tpGroupDomainAuthMode_Type.__name__ = "Integer32"
_HwL2tpGroupDomainAuthMode_Object = MibTableColumn
hwL2tpGroupDomainAuthMode = _HwL2tpGroupDomainAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 52),
    _HwL2tpGroupDomainAuthMode_Type()
)
hwL2tpGroupDomainAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupDomainAuthMode.setStatus("current")


class _HwL2tpGroupDescription_Type(OctetString):
    """Custom type hwL2tpGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwL2tpGroupDescription_Type.__name__ = "OctetString"
_HwL2tpGroupDescription_Object = MibTableColumn
hwL2tpGroupDescription = _HwL2tpGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 53),
    _HwL2tpGroupDescription_Type()
)
hwL2tpGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupDescription.setStatus("current")


class _HwL2tpTunnelAlarmEnable_Type(TruthValue):
    """Custom type hwL2tpTunnelAlarmEnable based on TruthValue"""


_HwL2tpTunnelAlarmEnable_Object = MibTableColumn
hwL2tpTunnelAlarmEnable = _HwL2tpTunnelAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 54),
    _HwL2tpTunnelAlarmEnable_Type()
)
hwL2tpTunnelAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpTunnelAlarmEnable.setStatus("current")


class _HwL2tpGroupQosProfileIn_Type(OctetString):
    """Custom type hwL2tpGroupQosProfileIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwL2tpGroupQosProfileIn_Type.__name__ = "OctetString"
_HwL2tpGroupQosProfileIn_Object = MibTableColumn
hwL2tpGroupQosProfileIn = _HwL2tpGroupQosProfileIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 55),
    _HwL2tpGroupQosProfileIn_Type()
)
hwL2tpGroupQosProfileIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupQosProfileIn.setStatus("current")


class _HwL2tpGroupQosProfileOut_Type(OctetString):
    """Custom type hwL2tpGroupQosProfileOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwL2tpGroupQosProfileOut_Type.__name__ = "OctetString"
_HwL2tpGroupQosProfileOut_Object = MibTableColumn
hwL2tpGroupQosProfileOut = _HwL2tpGroupQosProfileOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 56),
    _HwL2tpGroupQosProfileOut_Type()
)
hwL2tpGroupQosProfileOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupQosProfileOut.setStatus("current")


class _HwL2tpGroupQosMode_Type(Integer32):
    """Custom type hwL2tpGroupQosMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("session", 2),
          ("tunnel", 1))
    )


_HwL2tpGroupQosMode_Type.__name__ = "Integer32"
_HwL2tpGroupQosMode_Object = MibTableColumn
hwL2tpGroupQosMode = _HwL2tpGroupQosMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 2, 1, 57),
    _HwL2tpGroupQosMode_Type()
)
hwL2tpGroupQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpGroupQosMode.setStatus("current")
_HwL2tpLnsGroupConfigTable_Object = MibTable
hwL2tpLnsGroupConfigTable = _HwL2tpLnsGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupConfigTable.setStatus("current")
_HwL2tpLnsGroupConfigEntry_Object = MibTableRow
hwL2tpLnsGroupConfigEntry = _HwL2tpLnsGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1)
)
hwL2tpLnsGroupConfigEntry.setIndexNames(
    (0, "HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupName"),
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupConfigEntry.setStatus("current")


class _HwL2tpLnsGroupName_Type(OctetString):
    """Custom type hwL2tpLnsGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwL2tpLnsGroupName_Type.__name__ = "OctetString"
_HwL2tpLnsGroupName_Object = MibTableColumn
hwL2tpLnsGroupName = _HwL2tpLnsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1, 1),
    _HwL2tpLnsGroupName_Type()
)
hwL2tpLnsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupName.setStatus("current")


class _HwL2tpLnsGroupLoopBack_Type(OctetString):
    """Custom type hwL2tpLnsGroupLoopBack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpLnsGroupLoopBack_Type.__name__ = "OctetString"
_HwL2tpLnsGroupLoopBack_Object = MibTableColumn
hwL2tpLnsGroupLoopBack = _HwL2tpLnsGroupLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1, 2),
    _HwL2tpLnsGroupLoopBack_Type()
)
hwL2tpLnsGroupLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopBack.setStatus("current")


class _HwL2tpLnsGroupMasterSlot_Type(Integer32):
    """Custom type hwL2tpLnsGroupMasterSlot based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(255, 255),
    )


_HwL2tpLnsGroupMasterSlot_Type.__name__ = "Integer32"
_HwL2tpLnsGroupMasterSlot_Object = MibTableColumn
hwL2tpLnsGroupMasterSlot = _HwL2tpLnsGroupMasterSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1, 3),
    _HwL2tpLnsGroupMasterSlot_Type()
)
hwL2tpLnsGroupMasterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupMasterSlot.setStatus("current")


class _HwL2tpLnsGroupBindSlot_Type(Integer32):
    """Custom type hwL2tpLnsGroupBindSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwL2tpLnsGroupBindSlot_Type.__name__ = "Integer32"
_HwL2tpLnsGroupBindSlot_Object = MibTableColumn
hwL2tpLnsGroupBindSlot = _HwL2tpLnsGroupBindSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1, 4),
    _HwL2tpLnsGroupBindSlot_Type()
)
hwL2tpLnsGroupBindSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupBindSlot.setStatus("current")
_HwL2tpLnsGroupRowStatus_Type = RowStatus
_HwL2tpLnsGroupRowStatus_Object = MibTableColumn
hwL2tpLnsGroupRowStatus = _HwL2tpLnsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 3, 1, 5),
    _HwL2tpLnsGroupRowStatus_Type()
)
hwL2tpLnsGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupRowStatus.setStatus("current")
_HwL2tpLnsGroupLoopbackTable_Object = MibTable
hwL2tpLnsGroupLoopbackTable = _HwL2tpLnsGroupLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackTable.setStatus("current")
_HwL2tpLnsGroupLoopbackEntry_Object = MibTableRow
hwL2tpLnsGroupLoopbackEntry = _HwL2tpLnsGroupLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 4, 1)
)
hwL2tpLnsGroupLoopbackEntry.setIndexNames(
    (0, "HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupName"),
    (0, "HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupLoopbackIndex"),
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackEntry.setStatus("current")


class _HwL2tpLnsGroupLoopbackIndex_Type(Integer32):
    """Custom type hwL2tpLnsGroupLoopbackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwL2tpLnsGroupLoopbackIndex_Type.__name__ = "Integer32"
_HwL2tpLnsGroupLoopbackIndex_Object = MibTableColumn
hwL2tpLnsGroupLoopbackIndex = _HwL2tpLnsGroupLoopbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 4, 1, 1),
    _HwL2tpLnsGroupLoopbackIndex_Type()
)
hwL2tpLnsGroupLoopbackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackIndex.setStatus("current")


class _HwL2tpLnsGroupLoopbackInterface_Type(OctetString):
    """Custom type hwL2tpLnsGroupLoopbackInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpLnsGroupLoopbackInterface_Type.__name__ = "OctetString"
_HwL2tpLnsGroupLoopbackInterface_Object = MibTableColumn
hwL2tpLnsGroupLoopbackInterface = _HwL2tpLnsGroupLoopbackInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 4, 1, 2),
    _HwL2tpLnsGroupLoopbackInterface_Type()
)
hwL2tpLnsGroupLoopbackInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackInterface.setStatus("current")
_HwL2tpLnsGroupLoopbackRowStatus_Type = RowStatus
_HwL2tpLnsGroupLoopbackRowStatus_Object = MibTableColumn
hwL2tpLnsGroupLoopbackRowStatus = _HwL2tpLnsGroupLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 1, 4, 1, 3),
    _HwL2tpLnsGroupLoopbackRowStatus_Type()
)
hwL2tpLnsGroupLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackRowStatus.setStatus("current")
_HwL2tpMibTrap_ObjectIdentity = ObjectIdentity
hwL2tpMibTrap = _HwL2tpMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2)
)
_HwL2tpTrapOid_ObjectIdentity = ObjectIdentity
hwL2tpTrapOid = _HwL2tpTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 1)
)


class _HwL2tpTunnelID_Type(Integer32):
    """Custom type hwL2tpTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2tpTunnelID_Type.__name__ = "Integer32"
_HwL2tpTunnelID_Object = MibScalar
hwL2tpTunnelID = _HwL2tpTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 1, 1),
    _HwL2tpTunnelID_Type()
)
hwL2tpTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelID.setStatus("current")


class _HwL2tpPeerName_Type(OctetString):
    """Custom type hwL2tpPeerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwL2tpPeerName_Type.__name__ = "OctetString"
_HwL2tpPeerName_Object = MibScalar
hwL2tpPeerName = _HwL2tpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 1, 2),
    _HwL2tpPeerName_Type()
)
hwL2tpPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpPeerName.setStatus("current")
_HwL2tpPeerIp_Type = IpAddress
_HwL2tpPeerIp_Object = MibScalar
hwL2tpPeerIp = _HwL2tpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 1, 3),
    _HwL2tpPeerIp_Type()
)
hwL2tpPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpPeerIp.setStatus("current")


class _HwL2tpTunnelStatus_Type(OctetString):
    """Custom type hwL2tpTunnelStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwL2tpTunnelStatus_Type.__name__ = "OctetString"
_HwL2tpTunnelStatus_Object = MibScalar
hwL2tpTunnelStatus = _HwL2tpTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 1, 4),
    _HwL2tpTunnelStatus_Type()
)
hwL2tpTunnelStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2tpTunnelStatus.setStatus("current")
_HwL2tpTrapsDefine_ObjectIdentity = ObjectIdentity
hwL2tpTrapsDefine = _HwL2tpTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 2)
)
_HwL2tpTraps_ObjectIdentity = ObjectIdentity
hwL2tpTraps = _HwL2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 2, 0)
)
_HwL2tpConformance_ObjectIdentity = ObjectIdentity
hwL2tpConformance = _HwL2tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3)
)
_HwL2tpCompliances_ObjectIdentity = ObjectIdentity
hwL2tpCompliances = _HwL2tpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 1)
)
_HwL2tpObjectGroups_ObjectIdentity = ObjectIdentity
hwL2tpObjectGroups = _HwL2tpObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2)
)

# Managed Objects groups

hwL2tpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 1)
)
hwL2tpConfigGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpEnableStatus"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelClearLocalID"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelClearRemoteName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelClearSlotID"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpAging"))
)
if mibBuilder.loadTexts:
    hwL2tpConfigGroup.setStatus("current")

hwL2tpGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 2)
)
hwL2tpGroupConfigGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupindex"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupAuthentication"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupAvpHidden"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLoadShare"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupRetransmit"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTimeout"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTimer"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP1"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight1"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP2"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight2"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP3"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight3"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP4"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight4"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP5"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight5"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupRowStatus"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupRadiusAuth"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupRemoteName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupForceChap"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupForceLcp"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupVt"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupaaaAuthentication"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpIdleCutTimer"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupFlag"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP6"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight6"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP7"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight7"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsIP8"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupLnsWeight8"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpAvp46"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupDefaultDomain"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord1"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord2"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord3"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord4"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord5"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord6"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord7"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupPassWord8"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupDomainAuthMode"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupDescription"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelAlarmEnable"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupQosProfileIn"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupQosProfileOut"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupQosMode"))
)
if mibBuilder.loadTexts:
    hwL2tpGroupConfigGroup.setStatus("current")

hwL2tpLnsGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 3)
)
hwL2tpLnsGroupConfigGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupLoopBack"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupMasterSlot"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupBindSlot"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupConfigGroup.setStatus("current")

hwL2tpTrapOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 4)
)
hwL2tpTrapOidGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelID"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpPeerName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpPeerIp"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpTrapOidGroup.setStatus("current")

hwL2tpObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 5)
)
hwL2tpObsoleteGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupAging"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTunnelStartLnsIP1"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTunnelStartLnsIP2"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTunnelStartLnsIP3"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTunnelStartLnsIP4"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpGroupTunnelStartLnsIP5"))
)
if mibBuilder.loadTexts:
    hwL2tpObsoleteGroup.setStatus("obsolete")

hwL2tpLnsGroupLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 7)
)
hwL2tpLnsGroupLoopbackGroup.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupLoopbackInterface"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpLnsGroupLoopbackRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpLnsGroupLoopbackGroup.setStatus("current")


# Notification objects

hwL2tpTunnelUpOrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 2, 2, 0, 1)
)
hwL2tpTunnelUpOrDown.setObjects(
      *(("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelID"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpPeerName"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpPeerIp"),
        ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelStatus"))
)
if mibBuilder.loadTexts:
    hwL2tpTunnelUpOrDown.setStatus(
        "current"
    )


# Notifications groups

hwL2tpTrapNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 2, 6)
)
hwL2tpTrapNotificationsGroup.setObjects(
    ("HUAWEI-BRAS-L2TP-MIB", "hwL2tpTunnelUpOrDown")
)
if mibBuilder.loadTexts:
    hwL2tpTrapNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2tpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwL2tpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-L2TP-MIB",
    **{"hwBRASL2tp": hwBRASL2tp,
       "hwL2tpMibObjects": hwL2tpMibObjects,
       "hwL2tpConfigTable": hwL2tpConfigTable,
       "hwL2tpEnableStatus": hwL2tpEnableStatus,
       "hwL2tpTunnelClearLocalID": hwL2tpTunnelClearLocalID,
       "hwL2tpTunnelClearRemoteName": hwL2tpTunnelClearRemoteName,
       "hwL2tpTunnelClearSlotID": hwL2tpTunnelClearSlotID,
       "hwL2tpAging": hwL2tpAging,
       "hwL2tpGroupConfigTable": hwL2tpGroupConfigTable,
       "hwL2tpGroupConfigEntry": hwL2tpGroupConfigEntry,
       "hwL2tpGroupindex": hwL2tpGroupindex,
       "hwL2tpGroupAuthentication": hwL2tpGroupAuthentication,
       "hwL2tpGroupAvpHidden": hwL2tpGroupAvpHidden,
       "hwL2tpGroupLoadShare": hwL2tpGroupLoadShare,
       "hwL2tpTunnelName": hwL2tpTunnelName,
       "hwL2tpGroupRetransmit": hwL2tpGroupRetransmit,
       "hwL2tpGroupTimeout": hwL2tpGroupTimeout,
       "hwL2tpGroupTimer": hwL2tpGroupTimer,
       "hwL2tpGroupPassWord": hwL2tpGroupPassWord,
       "hwL2tpGroupLnsIP1": hwL2tpGroupLnsIP1,
       "hwL2tpGroupLnsWeight1": hwL2tpGroupLnsWeight1,
       "hwL2tpGroupLnsIP2": hwL2tpGroupLnsIP2,
       "hwL2tpGroupLnsWeight2": hwL2tpGroupLnsWeight2,
       "hwL2tpGroupLnsIP3": hwL2tpGroupLnsIP3,
       "hwL2tpGroupLnsWeight3": hwL2tpGroupLnsWeight3,
       "hwL2tpGroupLnsIP4": hwL2tpGroupLnsIP4,
       "hwL2tpGroupLnsWeight4": hwL2tpGroupLnsWeight4,
       "hwL2tpGroupLnsIP5": hwL2tpGroupLnsIP5,
       "hwL2tpGroupLnsWeight5": hwL2tpGroupLnsWeight5,
       "hwL2tpGroupRowStatus": hwL2tpGroupRowStatus,
       "hwL2tpGroupName": hwL2tpGroupName,
       "hwL2tpGroupRadiusAuth": hwL2tpGroupRadiusAuth,
       "hwL2tpGroupAging": hwL2tpGroupAging,
       "hwL2tpGroupRemoteName": hwL2tpGroupRemoteName,
       "hwL2tpGroupForceChap": hwL2tpGroupForceChap,
       "hwL2tpGroupForceLcp": hwL2tpGroupForceLcp,
       "hwL2tpGroupVt": hwL2tpGroupVt,
       "hwL2tpGroupaaaAuthentication": hwL2tpGroupaaaAuthentication,
       "hwL2tpIdleCutTimer": hwL2tpIdleCutTimer,
       "hwL2tpGroupTunnelStartLnsIP1": hwL2tpGroupTunnelStartLnsIP1,
       "hwL2tpGroupTunnelStartLnsIP2": hwL2tpGroupTunnelStartLnsIP2,
       "hwL2tpGroupTunnelStartLnsIP3": hwL2tpGroupTunnelStartLnsIP3,
       "hwL2tpGroupTunnelStartLnsIP4": hwL2tpGroupTunnelStartLnsIP4,
       "hwL2tpGroupTunnelStartLnsIP5": hwL2tpGroupTunnelStartLnsIP5,
       "hwL2tpGroupFlag": hwL2tpGroupFlag,
       "hwL2tpGroupLnsIP6": hwL2tpGroupLnsIP6,
       "hwL2tpGroupLnsWeight6": hwL2tpGroupLnsWeight6,
       "hwL2tpGroupLnsIP7": hwL2tpGroupLnsIP7,
       "hwL2tpGroupLnsWeight7": hwL2tpGroupLnsWeight7,
       "hwL2tpGroupLnsIP8": hwL2tpGroupLnsIP8,
       "hwL2tpGroupLnsWeight8": hwL2tpGroupLnsWeight8,
       "hwL2tpAvp46": hwL2tpAvp46,
       "hwL2tpGroupDefaultDomain": hwL2tpGroupDefaultDomain,
       "hwL2tpGroupPassWord1": hwL2tpGroupPassWord1,
       "hwL2tpGroupPassWord2": hwL2tpGroupPassWord2,
       "hwL2tpGroupPassWord3": hwL2tpGroupPassWord3,
       "hwL2tpGroupPassWord4": hwL2tpGroupPassWord4,
       "hwL2tpGroupPassWord5": hwL2tpGroupPassWord5,
       "hwL2tpGroupPassWord6": hwL2tpGroupPassWord6,
       "hwL2tpGroupPassWord7": hwL2tpGroupPassWord7,
       "hwL2tpGroupPassWord8": hwL2tpGroupPassWord8,
       "hwL2tpGroupDomainAuthMode": hwL2tpGroupDomainAuthMode,
       "hwL2tpGroupDescription": hwL2tpGroupDescription,
       "hwL2tpTunnelAlarmEnable": hwL2tpTunnelAlarmEnable,
       "hwL2tpGroupQosProfileIn": hwL2tpGroupQosProfileIn,
       "hwL2tpGroupQosProfileOut": hwL2tpGroupQosProfileOut,
       "hwL2tpGroupQosMode": hwL2tpGroupQosMode,
       "hwL2tpLnsGroupConfigTable": hwL2tpLnsGroupConfigTable,
       "hwL2tpLnsGroupConfigEntry": hwL2tpLnsGroupConfigEntry,
       "hwL2tpLnsGroupName": hwL2tpLnsGroupName,
       "hwL2tpLnsGroupLoopBack": hwL2tpLnsGroupLoopBack,
       "hwL2tpLnsGroupMasterSlot": hwL2tpLnsGroupMasterSlot,
       "hwL2tpLnsGroupBindSlot": hwL2tpLnsGroupBindSlot,
       "hwL2tpLnsGroupRowStatus": hwL2tpLnsGroupRowStatus,
       "hwL2tpLnsGroupLoopbackTable": hwL2tpLnsGroupLoopbackTable,
       "hwL2tpLnsGroupLoopbackEntry": hwL2tpLnsGroupLoopbackEntry,
       "hwL2tpLnsGroupLoopbackIndex": hwL2tpLnsGroupLoopbackIndex,
       "hwL2tpLnsGroupLoopbackInterface": hwL2tpLnsGroupLoopbackInterface,
       "hwL2tpLnsGroupLoopbackRowStatus": hwL2tpLnsGroupLoopbackRowStatus,
       "hwL2tpMibTrap": hwL2tpMibTrap,
       "hwL2tpTrapOid": hwL2tpTrapOid,
       "hwL2tpTunnelID": hwL2tpTunnelID,
       "hwL2tpPeerName": hwL2tpPeerName,
       "hwL2tpPeerIp": hwL2tpPeerIp,
       "hwL2tpTunnelStatus": hwL2tpTunnelStatus,
       "hwL2tpTrapsDefine": hwL2tpTrapsDefine,
       "hwL2tpTraps": hwL2tpTraps,
       "hwL2tpTunnelUpOrDown": hwL2tpTunnelUpOrDown,
       "hwL2tpConformance": hwL2tpConformance,
       "hwL2tpCompliances": hwL2tpCompliances,
       "hwL2tpCompliance": hwL2tpCompliance,
       "hwL2tpObjectGroups": hwL2tpObjectGroups,
       "hwL2tpConfigGroup": hwL2tpConfigGroup,
       "hwL2tpGroupConfigGroup": hwL2tpGroupConfigGroup,
       "hwL2tpLnsGroupConfigGroup": hwL2tpLnsGroupConfigGroup,
       "hwL2tpTrapOidGroup": hwL2tpTrapOidGroup,
       "hwL2tpObsoleteGroup": hwL2tpObsoleteGroup,
       "hwL2tpTrapNotificationsGroup": hwL2tpTrapNotificationsGroup,
       "hwL2tpLnsGroupLoopbackGroup": hwL2tpLnsGroupLoopbackGroup}
)
