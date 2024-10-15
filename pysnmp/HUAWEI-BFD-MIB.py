# SNMP MIB module (HUAWEI-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:52 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwBFDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdInterval(Integer32, TextualConvention):
    status = "current"


class BfdDiag(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwBfdScalarsObjects_ObjectIdentity = ObjectIdentity
hwBfdScalarsObjects = _HwBfdScalarsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1)
)


class _HwBfdVersionNumber_Type(Unsigned32):
    """Custom type hwBfdVersionNumber based on Unsigned32"""
    defaultValue = 1


_HwBfdVersionNumber_Object = MibScalar
hwBfdVersionNumber = _HwBfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 1),
    _HwBfdVersionNumber_Type()
)
hwBfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdVersionNumber.setStatus("current")


class _HwBfdAdminStatus_Type(EnabledStatus):
    """Custom type hwBfdAdminStatus based on EnabledStatus"""
    defaultValue = 2


_HwBfdAdminStatus_Object = MibScalar
hwBfdAdminStatus = _HwBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 2),
    _HwBfdAdminStatus_Type()
)
hwBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdAdminStatus.setStatus("current")


class _HwBfdSessLimitNumber_Type(Unsigned32):
    """Custom type hwBfdSessLimitNumber based on Unsigned32"""
    defaultValue = 0


_HwBfdSessLimitNumber_Object = MibScalar
hwBfdSessLimitNumber = _HwBfdSessLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 3),
    _HwBfdSessLimitNumber_Type()
)
hwBfdSessLimitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessLimitNumber.setStatus("current")


class _HwBfdSessInterfaceLimitNumber_Type(Unsigned32):
    """Custom type hwBfdSessInterfaceLimitNumber based on Unsigned32"""
    defaultValue = 0


_HwBfdSessInterfaceLimitNumber_Object = MibScalar
hwBfdSessInterfaceLimitNumber = _HwBfdSessInterfaceLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 4),
    _HwBfdSessInterfaceLimitNumber_Type()
)
hwBfdSessInterfaceLimitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessInterfaceLimitNumber.setStatus("current")
_HwBfdSessStaticNumber_Type = Unsigned32
_HwBfdSessStaticNumber_Object = MibScalar
hwBfdSessStaticNumber = _HwBfdSessStaticNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 5),
    _HwBfdSessStaticNumber_Type()
)
hwBfdSessStaticNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessStaticNumber.setStatus("current")
_HwBfdSessDynamicNumber_Type = Unsigned32
_HwBfdSessDynamicNumber_Object = MibScalar
hwBfdSessDynamicNumber = _HwBfdSessDynamicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 6),
    _HwBfdSessDynamicNumber_Type()
)
hwBfdSessDynamicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDynamicNumber.setStatus("current")
_HwBfdSessGlobalDefaultIpAddr_Type = IpAddress
_HwBfdSessGlobalDefaultIpAddr_Object = MibScalar
hwBfdSessGlobalDefaultIpAddr = _HwBfdSessGlobalDefaultIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 7),
    _HwBfdSessGlobalDefaultIpAddr_Type()
)
hwBfdSessGlobalDefaultIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdSessGlobalDefaultIpAddr.setStatus("current")


class _HwBfdEchoPassiveStatus_Type(EnabledStatus):
    """Custom type hwBfdEchoPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_HwBfdEchoPassiveStatus_Object = MibScalar
hwBfdEchoPassiveStatus = _HwBfdEchoPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 8),
    _HwBfdEchoPassiveStatus_Type()
)
hwBfdEchoPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdEchoPassiveStatus.setStatus("current")


class _HwBfdEchoAclNum_Type(Unsigned32):
    """Custom type hwBfdEchoAclNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwBfdEchoAclNum_Type.__name__ = "Unsigned32"
_HwBfdEchoAclNum_Object = MibScalar
hwBfdEchoAclNum = _HwBfdEchoAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 9),
    _HwBfdEchoAclNum_Type()
)
hwBfdEchoAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdEchoAclNum.setStatus("current")


class _HwBfdSessDynamicPingInterval_Type(Unsigned32):
    """Custom type hwBfdSessDynamicPingInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_HwBfdSessDynamicPingInterval_Type.__name__ = "Unsigned32"
_HwBfdSessDynamicPingInterval_Object = MibScalar
hwBfdSessDynamicPingInterval = _HwBfdSessDynamicPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 10),
    _HwBfdSessDynamicPingInterval_Type()
)
hwBfdSessDynamicPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdSessDynamicPingInterval.setStatus("current")


class _HwBfdSessDynamicSupportPassive_Type(EnabledStatus):
    """Custom type hwBfdSessDynamicSupportPassive based on EnabledStatus"""
    defaultValue = 2


_HwBfdSessDynamicSupportPassive_Object = MibScalar
hwBfdSessDynamicSupportPassive = _HwBfdSessDynamicSupportPassive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 11),
    _HwBfdSessDynamicSupportPassive_Type()
)
hwBfdSessDynamicSupportPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdSessDynamicSupportPassive.setStatus("current")


class _HwBfdSessDelayUpTime_Type(Unsigned32):
    """Custom type hwBfdSessDelayUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwBfdSessDelayUpTime_Type.__name__ = "Unsigned32"
_HwBfdSessDelayUpTime_Object = MibScalar
hwBfdSessDelayUpTime = _HwBfdSessDelayUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 12),
    _HwBfdSessDelayUpTime_Type()
)
hwBfdSessDelayUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdSessDelayUpTime.setStatus("current")


class _HwBfdSessMultiDstPort_Type(Integer32):
    """Custom type hwBfdSessMultiDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3784, 3784),
        ValueRangeConstraint(4784, 4784),
    )


_HwBfdSessMultiDstPort_Type.__name__ = "Integer32"
_HwBfdSessMultiDstPort_Object = MibScalar
hwBfdSessMultiDstPort = _HwBfdSessMultiDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 13),
    _HwBfdSessMultiDstPort_Type()
)
hwBfdSessMultiDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdSessMultiDstPort.setStatus("current")


class _HwBfdTrapSendInterval_Type(Integer32):
    """Custom type hwBfdTrapSendInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwBfdTrapSendInterval_Type.__name__ = "Integer32"
_HwBfdTrapSendInterval_Object = MibScalar
hwBfdTrapSendInterval = _HwBfdTrapSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 1, 14),
    _HwBfdTrapSendInterval_Type()
)
hwBfdTrapSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBfdTrapSendInterval.setStatus("current")
_HwBfdObjects_ObjectIdentity = ObjectIdentity
hwBfdObjects = _HwBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2)
)
_HwBfdIfConfTable_Object = MibTable
hwBfdIfConfTable = _HwBfdIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1)
)
if mibBuilder.loadTexts:
    hwBfdIfConfTable.setStatus("current")
_HwBfdIfConfEntry_Object = MibTableRow
hwBfdIfConfEntry = _HwBfdIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1)
)
hwBfdIfConfEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdIfConfIndex"),
)
if mibBuilder.loadTexts:
    hwBfdIfConfEntry.setStatus("current")


class _HwBfdIfConfIndex_Type(Integer32):
    """Custom type hwBfdIfConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBfdIfConfIndex_Type.__name__ = "Integer32"
_HwBfdIfConfIndex_Object = MibTableColumn
hwBfdIfConfIndex = _HwBfdIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 1),
    _HwBfdIfConfIndex_Type()
)
hwBfdIfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdIfConfIndex.setStatus("current")


class _HwBfdIfConfName_Type(OctetString):
    """Custom type hwBfdIfConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBfdIfConfName_Type.__name__ = "OctetString"
_HwBfdIfConfName_Object = MibTableColumn
hwBfdIfConfName = _HwBfdIfConfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 2),
    _HwBfdIfConfName_Type()
)
hwBfdIfConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdIfConfName.setStatus("current")


class _HwBfdIfConfEnable_Type(Integer32):
    """Custom type hwBfdIfConfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdIfConfEnable_Type.__name__ = "Integer32"
_HwBfdIfConfEnable_Object = MibTableColumn
hwBfdIfConfEnable = _HwBfdIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 3),
    _HwBfdIfConfEnable_Type()
)
hwBfdIfConfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdIfConfEnable.setStatus("obsolete")


class _HwBfdIfConfDeleting_Type(Integer32):
    """Custom type hwBfdIfConfDeleting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdIfConfDeleting_Type.__name__ = "Integer32"
_HwBfdIfConfDeleting_Object = MibTableColumn
hwBfdIfConfDeleting = _HwBfdIfConfDeleting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 4),
    _HwBfdIfConfDeleting_Type()
)
hwBfdIfConfDeleting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdIfConfDeleting.setStatus("current")


class _HwBfdIfConfAvailable_Type(Integer32):
    """Custom type hwBfdIfConfAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdIfConfAvailable_Type.__name__ = "Integer32"
_HwBfdIfConfAvailable_Object = MibTableColumn
hwBfdIfConfAvailable = _HwBfdIfConfAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 5),
    _HwBfdIfConfAvailable_Type()
)
hwBfdIfConfAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdIfConfAvailable.setStatus("current")
_HwBfdIfConfSessCnt_Type = Integer32
_HwBfdIfConfSessCnt_Object = MibTableColumn
hwBfdIfConfSessCnt = _HwBfdIfConfSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 6),
    _HwBfdIfConfSessCnt_Type()
)
hwBfdIfConfSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdIfConfSessCnt.setStatus("current")
_HwBfdIfConfRowStatus_Type = RowStatus
_HwBfdIfConfRowStatus_Object = MibTableColumn
hwBfdIfConfRowStatus = _HwBfdIfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 1, 1, 7),
    _HwBfdIfConfRowStatus_Type()
)
hwBfdIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdIfConfRowStatus.setStatus("current")
_HwBfdSessionConfTable_Object = MibTable
hwBfdSessionConfTable = _HwBfdSessionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2)
)
if mibBuilder.loadTexts:
    hwBfdSessionConfTable.setStatus("current")
_HwBfdSessionConfEntry_Object = MibTableRow
hwBfdSessionConfEntry = _HwBfdSessionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1)
)
hwBfdSessionConfEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdSessConfName"),
)
if mibBuilder.loadTexts:
    hwBfdSessionConfEntry.setStatus("current")


class _HwBfdSessConfName_Type(OctetString):
    """Custom type hwBfdSessConfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HwBfdSessConfName_Type.__name__ = "OctetString"
_HwBfdSessConfName_Object = MibTableColumn
hwBfdSessConfName = _HwBfdSessConfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 1),
    _HwBfdSessConfName_Type()
)
hwBfdSessConfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdSessConfName.setStatus("current")


class _HwBfdSessConfMIndex_Type(Unsigned32):
    """Custom type hwBfdSessConfMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwBfdSessConfMIndex_Type.__name__ = "Unsigned32"
_HwBfdSessConfMIndex_Object = MibTableColumn
hwBfdSessConfMIndex = _HwBfdSessConfMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 2),
    _HwBfdSessConfMIndex_Type()
)
hwBfdSessConfMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessConfMIndex.setStatus("current")


class _HwBfdSessConfLocalDiscr_Type(Unsigned32):
    """Custom type hwBfdSessConfLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HwBfdSessConfLocalDiscr_Type.__name__ = "Unsigned32"
_HwBfdSessConfLocalDiscr_Object = MibTableColumn
hwBfdSessConfLocalDiscr = _HwBfdSessConfLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 3),
    _HwBfdSessConfLocalDiscr_Type()
)
hwBfdSessConfLocalDiscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfLocalDiscr.setStatus("current")


class _HwBfdSessConfRemoteDiscr_Type(Unsigned32):
    """Custom type hwBfdSessConfRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HwBfdSessConfRemoteDiscr_Type.__name__ = "Unsigned32"
_HwBfdSessConfRemoteDiscr_Object = MibTableColumn
hwBfdSessConfRemoteDiscr = _HwBfdSessConfRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 4),
    _HwBfdSessConfRemoteDiscr_Type()
)
hwBfdSessConfRemoteDiscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfRemoteDiscr.setStatus("current")
_HwBfdSessConfPeerAddr_Type = IpAddress
_HwBfdSessConfPeerAddr_Object = MibTableColumn
hwBfdSessConfPeerAddr = _HwBfdSessConfPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 5),
    _HwBfdSessConfPeerAddr_Type()
)
hwBfdSessConfPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfPeerAddr.setStatus("current")


class _HwBfdSessConfBindIfIndex_Type(Unsigned32):
    """Custom type hwBfdSessConfBindIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessConfBindIfIndex_Type.__name__ = "Unsigned32"
_HwBfdSessConfBindIfIndex_Object = MibTableColumn
hwBfdSessConfBindIfIndex = _HwBfdSessConfBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 6),
    _HwBfdSessConfBindIfIndex_Type()
)
hwBfdSessConfBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessConfBindIfIndex.setStatus("current")


class _HwBfdSessConfBindIfName_Type(OctetString):
    """Custom type hwBfdSessConfBindIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBfdSessConfBindIfName_Type.__name__ = "OctetString"
_HwBfdSessConfBindIfName_Object = MibTableColumn
hwBfdSessConfBindIfName = _HwBfdSessConfBindIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 7),
    _HwBfdSessConfBindIfName_Type()
)
hwBfdSessConfBindIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfBindIfName.setStatus("current")


class _HwBfdSessConfDemandEnable_Type(Integer32):
    """Custom type hwBfdSessConfDemandEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdSessConfDemandEnable_Type.__name__ = "Integer32"
_HwBfdSessConfDemandEnable_Object = MibTableColumn
hwBfdSessConfDemandEnable = _HwBfdSessConfDemandEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 8),
    _HwBfdSessConfDemandEnable_Type()
)
hwBfdSessConfDemandEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDemandEnable.setStatus("current")


class _HwBfdSessConfDemandTimerInterval_Type(Unsigned32):
    """Custom type hwBfdSessConfDemandTimerInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 300000),
    )


_HwBfdSessConfDemandTimerInterval_Type.__name__ = "Unsigned32"
_HwBfdSessConfDemandTimerInterval_Object = MibTableColumn
hwBfdSessConfDemandTimerInterval = _HwBfdSessConfDemandTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 9),
    _HwBfdSessConfDemandTimerInterval_Type()
)
hwBfdSessConfDemandTimerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDemandTimerInterval.setStatus("current")


class _HwBfdSessConfDetectMult_Type(Unsigned32):
    """Custom type hwBfdSessConfDetectMult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_HwBfdSessConfDetectMult_Type.__name__ = "Unsigned32"
_HwBfdSessConfDetectMult_Object = MibTableColumn
hwBfdSessConfDetectMult = _HwBfdSessConfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 10),
    _HwBfdSessConfDetectMult_Type()
)
hwBfdSessConfDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDetectMult.setStatus("current")


class _HwBfdSessConfDesiredMinRxInterval_Type(BfdInterval):
    """Custom type hwBfdSessConfDesiredMinRxInterval based on BfdInterval"""
    subtypeSpec = BfdInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwBfdSessConfDesiredMinRxInterval_Type.__name__ = "BfdInterval"
_HwBfdSessConfDesiredMinRxInterval_Object = MibTableColumn
hwBfdSessConfDesiredMinRxInterval = _HwBfdSessConfDesiredMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 11),
    _HwBfdSessConfDesiredMinRxInterval_Type()
)
hwBfdSessConfDesiredMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDesiredMinRxInterval.setStatus("current")


class _HwBfdSessConfDesiredMinTxInterval_Type(BfdInterval):
    """Custom type hwBfdSessConfDesiredMinTxInterval based on BfdInterval"""
    subtypeSpec = BfdInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwBfdSessConfDesiredMinTxInterval_Type.__name__ = "BfdInterval"
_HwBfdSessConfDesiredMinTxInterval_Object = MibTableColumn
hwBfdSessConfDesiredMinTxInterval = _HwBfdSessConfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 12),
    _HwBfdSessConfDesiredMinTxInterval_Type()
)
hwBfdSessConfDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDesiredMinTxInterval.setStatus("current")


class _HwBfdSessConfWTRInterval_Type(Integer32):
    """Custom type hwBfdSessConfWTRInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwBfdSessConfWTRInterval_Type.__name__ = "Integer32"
_HwBfdSessConfWTRInterval_Object = MibTableColumn
hwBfdSessConfWTRInterval = _HwBfdSessConfWTRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 13),
    _HwBfdSessConfWTRInterval_Type()
)
hwBfdSessConfWTRInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfWTRInterval.setStatus("current")


class _HwBfdSessConfTOS_Type(Integer32):
    """Custom type hwBfdSessConfTOS based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwBfdSessConfTOS_Type.__name__ = "Integer32"
_HwBfdSessConfTOS_Object = MibTableColumn
hwBfdSessConfTOS = _HwBfdSessConfTOS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 14),
    _HwBfdSessConfTOS_Type()
)
hwBfdSessConfTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfTOS.setStatus("current")


class _HwBfdSessConfPSTFlag_Type(Integer32):
    """Custom type hwBfdSessConfPSTFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdSessConfPSTFlag_Type.__name__ = "Integer32"
_HwBfdSessConfPSTFlag_Object = MibTableColumn
hwBfdSessConfPSTFlag = _HwBfdSessConfPSTFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 15),
    _HwBfdSessConfPSTFlag_Type()
)
hwBfdSessConfPSTFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfPSTFlag.setStatus("current")


class _HwBfdSessConfCommitFlag_Type(Integer32):
    """Custom type hwBfdSessConfCommitFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdSessConfCommitFlag_Type.__name__ = "Integer32"
_HwBfdSessConfCommitFlag_Object = MibTableColumn
hwBfdSessConfCommitFlag = _HwBfdSessConfCommitFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 16),
    _HwBfdSessConfCommitFlag_Type()
)
hwBfdSessConfCommitFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfCommitFlag.setStatus("current")


class _HwBfdSessConfAdminStatus_Type(Integer32):
    """Custom type hwBfdSessConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdSessConfAdminStatus_Type.__name__ = "Integer32"
_HwBfdSessConfAdminStatus_Object = MibTableColumn
hwBfdSessConfAdminStatus = _HwBfdSessConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 17),
    _HwBfdSessConfAdminStatus_Type()
)
hwBfdSessConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfAdminStatus.setStatus("current")
_HwBfdSessConfRowStatus_Type = RowStatus
_HwBfdSessConfRowStatus_Object = MibTableColumn
hwBfdSessConfRowStatus = _HwBfdSessConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 18),
    _HwBfdSessConfRowStatus_Type()
)
hwBfdSessConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfRowStatus.setStatus("current")
_HwBfdSessConfSourceAddr_Type = IpAddress
_HwBfdSessConfSourceAddr_Object = MibTableColumn
hwBfdSessConfSourceAddr = _HwBfdSessConfSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 19),
    _HwBfdSessConfSourceAddr_Type()
)
hwBfdSessConfSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfSourceAddr.setStatus("current")


class _HwBfdSessConfVrfIndex_Type(Unsigned32):
    """Custom type hwBfdSessConfVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessConfVrfIndex_Type.__name__ = "Unsigned32"
_HwBfdSessConfVrfIndex_Object = MibTableColumn
hwBfdSessConfVrfIndex = _HwBfdSessConfVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 20),
    _HwBfdSessConfVrfIndex_Type()
)
hwBfdSessConfVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessConfVrfIndex.setStatus("current")


class _HwBfdSessConfVPNName_Type(OctetString):
    """Custom type hwBfdSessConfVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBfdSessConfVPNName_Type.__name__ = "OctetString"
_HwBfdSessConfVPNName_Object = MibTableColumn
hwBfdSessConfVPNName = _HwBfdSessConfVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 21),
    _HwBfdSessConfVPNName_Type()
)
hwBfdSessConfVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfVPNName.setStatus("current")


class _HwBfdSessConfDefaultIp_Type(Integer32):
    """Custom type hwBfdSessConfDefaultIp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HwBfdSessConfDefaultIp_Type.__name__ = "Integer32"
_HwBfdSessConfDefaultIp_Object = MibTableColumn
hwBfdSessConfDefaultIp = _HwBfdSessConfDefaultIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 22),
    _HwBfdSessConfDefaultIp_Type()
)
hwBfdSessConfDefaultIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDefaultIp.setStatus("current")


class _HwBfdSessConfPISFlag_Type(Integer32):
    """Custom type hwBfdSessConfPISFlag based on Integer32"""
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
        *(("false", 1),
          ("subif", 3),
          ("true", 2))
    )


_HwBfdSessConfPISFlag_Type.__name__ = "Integer32"
_HwBfdSessConfPISFlag_Object = MibTableColumn
hwBfdSessConfPISFlag = _HwBfdSessConfPISFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 23),
    _HwBfdSessConfPISFlag_Type()
)
hwBfdSessConfPISFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfPISFlag.setStatus("current")


class _HwBfdSessConfBindType_Type(Integer32):
    """Custom type hwBfdSessConfBindType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("fec", 5),
          ("ifAndSourceIp", 4),
          ("interfaceIp", 1),
          ("isis", 8),
          ("ldpLsp", 9),
          ("ospf", 7),
          ("peerIp", 2),
          ("pw", 13),
          ("sourceIp", 3),
          ("staticLsp", 10),
          ("teLsp", 11),
          ("teTunnel", 12),
          ("tunnelIf", 6),
          ("vsiPw", 15))
    )


_HwBfdSessConfBindType_Type.__name__ = "Integer32"
_HwBfdSessConfBindType_Object = MibTableColumn
hwBfdSessConfBindType = _HwBfdSessConfBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 24),
    _HwBfdSessConfBindType_Type()
)
hwBfdSessConfBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfBindType.setStatus("current")
_HwBfdSessConfNextHop_Type = IpAddress
_HwBfdSessConfNextHop_Object = MibTableColumn
hwBfdSessConfNextHop = _HwBfdSessConfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 25),
    _HwBfdSessConfNextHop_Type()
)
hwBfdSessConfNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfNextHop.setStatus("current")


class _HwBfdSessConfStaticLspName_Type(OctetString):
    """Custom type hwBfdSessConfStaticLspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwBfdSessConfStaticLspName_Type.__name__ = "OctetString"
_HwBfdSessConfStaticLspName_Object = MibTableColumn
hwBfdSessConfStaticLspName = _HwBfdSessConfStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 26),
    _HwBfdSessConfStaticLspName_Type()
)
hwBfdSessConfStaticLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfStaticLspName.setStatus("current")


class _HwBfdSessConfPWSecondaryFlag_Type(Integer32):
    """Custom type hwBfdSessConfPWSecondaryFlag based on Integer32"""
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
        *(("flagMasterPW", 1),
          ("flagNoPW", 3),
          ("flagSecondaryPW", 2))
    )


_HwBfdSessConfPWSecondaryFlag_Type.__name__ = "Integer32"
_HwBfdSessConfPWSecondaryFlag_Object = MibTableColumn
hwBfdSessConfPWSecondaryFlag = _HwBfdSessConfPWSecondaryFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 27),
    _HwBfdSessConfPWSecondaryFlag_Type()
)
hwBfdSessConfPWSecondaryFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfPWSecondaryFlag.setStatus("current")


class _HwBfdSessConfTunnelDetectType_Type(Integer32):
    """Custom type hwBfdSessConfTunnelDetectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flagBothDown", 1),
          ("flagNeighborDown", 2))
    )


_HwBfdSessConfTunnelDetectType_Type.__name__ = "Integer32"
_HwBfdSessConfTunnelDetectType_Object = MibTableColumn
hwBfdSessConfTunnelDetectType = _HwBfdSessConfTunnelDetectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 28),
    _HwBfdSessConfTunnelDetectType_Type()
)
hwBfdSessConfTunnelDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfTunnelDetectType.setStatus("current")


class _HwBfdSessConfVcId_Type(Unsigned32):
    """Custom type hwBfdSessConfVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessConfVcId_Type.__name__ = "Unsigned32"
_HwBfdSessConfVcId_Object = MibTableColumn
hwBfdSessConfVcId = _HwBfdSessConfVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 29),
    _HwBfdSessConfVcId_Type()
)
hwBfdSessConfVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfVcId.setStatus("current")


class _HwBfdSessConfVsiName_Type(OctetString):
    """Custom type hwBfdSessConfVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBfdSessConfVsiName_Type.__name__ = "OctetString"
_HwBfdSessConfVsiName_Object = MibTableColumn
hwBfdSessConfVsiName = _HwBfdSessConfVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 30),
    _HwBfdSessConfVsiName_Type()
)
hwBfdSessConfVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfVsiName.setStatus("current")
_HwBfdSessConfVsiPeerAddr_Type = IpAddress
_HwBfdSessConfVsiPeerAddr_Object = MibTableColumn
hwBfdSessConfVsiPeerAddr = _HwBfdSessConfVsiPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 31),
    _HwBfdSessConfVsiPeerAddr_Type()
)
hwBfdSessConfVsiPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfVsiPeerAddr.setStatus("current")


class _HwBfdSessConfDiscrAuto_Type(EnabledStatus):
    """Custom type hwBfdSessConfDiscrAuto based on EnabledStatus"""


_HwBfdSessConfDiscrAuto_Object = MibTableColumn
hwBfdSessConfDiscrAuto = _HwBfdSessConfDiscrAuto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 2, 1, 32),
    _HwBfdSessConfDiscrAuto_Type()
)
hwBfdSessConfDiscrAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSessConfDiscrAuto.setStatus("current")
_HwBfdSessionTable_Object = MibTable
hwBfdSessionTable = _HwBfdSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3)
)
if mibBuilder.loadTexts:
    hwBfdSessionTable.setStatus("current")
_HwBfdSessionEntry_Object = MibTableRow
hwBfdSessionEntry = _HwBfdSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1)
)
hwBfdSessionEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdSessIndex"),
)
if mibBuilder.loadTexts:
    hwBfdSessionEntry.setStatus("current")


class _HwBfdSessIndex_Type(Unsigned32):
    """Custom type hwBfdSessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwBfdSessIndex_Type.__name__ = "Unsigned32"
_HwBfdSessIndex_Object = MibTableColumn
hwBfdSessIndex = _HwBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 1),
    _HwBfdSessIndex_Type()
)
hwBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdSessIndex.setStatus("current")


class _HwBfdSessMIndex_Type(Unsigned32):
    """Custom type hwBfdSessMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwBfdSessMIndex_Type.__name__ = "Unsigned32"
_HwBfdSessMIndex_Object = MibTableColumn
hwBfdSessMIndex = _HwBfdSessMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 2),
    _HwBfdSessMIndex_Type()
)
hwBfdSessMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessMIndex.setStatus("current")


class _HwBfdSessBindVRRP_Type(Integer32):
    """Custom type hwBfdSessBindVRRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwBfdSessBindVRRP_Type.__name__ = "Integer32"
_HwBfdSessBindVRRP_Object = MibTableColumn
hwBfdSessBindVRRP = _HwBfdSessBindVRRP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 3),
    _HwBfdSessBindVRRP_Type()
)
hwBfdSessBindVRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessBindVRRP.setStatus("current")


class _HwBfdSessCfgName_Type(OctetString):
    """Custom type hwBfdSessCfgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HwBfdSessCfgName_Type.__name__ = "OctetString"
_HwBfdSessCfgName_Object = MibTableColumn
hwBfdSessCfgName = _HwBfdSessCfgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 4),
    _HwBfdSessCfgName_Type()
)
hwBfdSessCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessCfgName.setStatus("current")
_HwBfdSessPeerAddr_Type = IpAddress
_HwBfdSessPeerAddr_Object = MibTableColumn
hwBfdSessPeerAddr = _HwBfdSessPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 5),
    _HwBfdSessPeerAddr_Type()
)
hwBfdSessPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPeerAddr.setStatus("current")


class _HwBfdSessBindIfIndex_Type(Integer32):
    """Custom type hwBfdSessBindIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwBfdSessBindIfIndex_Type.__name__ = "Integer32"
_HwBfdSessBindIfIndex_Object = MibTableColumn
hwBfdSessBindIfIndex = _HwBfdSessBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 6),
    _HwBfdSessBindIfIndex_Type()
)
hwBfdSessBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessBindIfIndex.setStatus("current")


class _HwBfdSessBindIfName_Type(OctetString):
    """Custom type hwBfdSessBindIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBfdSessBindIfName_Type.__name__ = "OctetString"
_HwBfdSessBindIfName_Object = MibTableColumn
hwBfdSessBindIfName = _HwBfdSessBindIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 7),
    _HwBfdSessBindIfName_Type()
)
hwBfdSessBindIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessBindIfName.setStatus("current")


class _HwBfdSessLocalDiscr_Type(Unsigned32):
    """Custom type hwBfdSessLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HwBfdSessLocalDiscr_Type.__name__ = "Unsigned32"
_HwBfdSessLocalDiscr_Object = MibTableColumn
hwBfdSessLocalDiscr = _HwBfdSessLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 8),
    _HwBfdSessLocalDiscr_Type()
)
hwBfdSessLocalDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessLocalDiscr.setStatus("current")


class _HwBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type hwBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_HwBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_HwBfdSessRemoteDiscr_Object = MibTableColumn
hwBfdSessRemoteDiscr = _HwBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 9),
    _HwBfdSessRemoteDiscr_Type()
)
hwBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessRemoteDiscr.setStatus("current")


class _HwBfdSessOperMode_Type(Integer32):
    """Custom type hwBfdSessOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwBfdSessOperMode_Type.__name__ = "Integer32"
_HwBfdSessOperMode_Object = MibTableColumn
hwBfdSessOperMode = _HwBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 10),
    _HwBfdSessOperMode_Type()
)
hwBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessOperMode.setStatus("current")


class _HwBfdSessDetectMult_Type(Unsigned32):
    """Custom type hwBfdSessDetectMult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_HwBfdSessDetectMult_Type.__name__ = "Unsigned32"
_HwBfdSessDetectMult_Object = MibTableColumn
hwBfdSessDetectMult = _HwBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 11),
    _HwBfdSessDetectMult_Type()
)
hwBfdSessDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDetectMult.setStatus("current")
_HwBfdSessDemandTimerInterval_Type = BfdInterval
_HwBfdSessDemandTimerInterval_Object = MibTableColumn
hwBfdSessDemandTimerInterval = _HwBfdSessDemandTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 12),
    _HwBfdSessDemandTimerInterval_Type()
)
hwBfdSessDemandTimerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDemandTimerInterval.setStatus("current")


class _HwBfdSessActualRxInterval_Type(BfdInterval):
    """Custom type hwBfdSessActualRxInterval based on BfdInterval"""
    subtypeSpec = BfdInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30000),
    )


_HwBfdSessActualRxInterval_Type.__name__ = "BfdInterval"
_HwBfdSessActualRxInterval_Object = MibTableColumn
hwBfdSessActualRxInterval = _HwBfdSessActualRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 13),
    _HwBfdSessActualRxInterval_Type()
)
hwBfdSessActualRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessActualRxInterval.setStatus("current")


class _HwBfdSessActualTxInterval_Type(BfdInterval):
    """Custom type hwBfdSessActualTxInterval based on BfdInterval"""
    subtypeSpec = BfdInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30000),
    )


_HwBfdSessActualTxInterval_Type.__name__ = "BfdInterval"
_HwBfdSessActualTxInterval_Object = MibTableColumn
hwBfdSessActualTxInterval = _HwBfdSessActualTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 14),
    _HwBfdSessActualTxInterval_Type()
)
hwBfdSessActualTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessActualTxInterval.setStatus("current")


class _HwBfdSessWTRInterval_Type(Integer32):
    """Custom type hwBfdSessWTRInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwBfdSessWTRInterval_Type.__name__ = "Integer32"
_HwBfdSessWTRInterval_Object = MibTableColumn
hwBfdSessWTRInterval = _HwBfdSessWTRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 15),
    _HwBfdSessWTRInterval_Type()
)
hwBfdSessWTRInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessWTRInterval.setStatus("current")


class _HwBfdSessTOS_Type(Integer32):
    """Custom type hwBfdSessTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwBfdSessTOS_Type.__name__ = "Integer32"
_HwBfdSessTOS_Object = MibTableColumn
hwBfdSessTOS = _HwBfdSessTOS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 16),
    _HwBfdSessTOS_Type()
)
hwBfdSessTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessTOS.setStatus("current")


class _HwBfdSessState_Type(Integer32):
    """Custom type hwBfdSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwBfdSessState_Type.__name__ = "Integer32"
_HwBfdSessState_Object = MibTableColumn
hwBfdSessState = _HwBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 17),
    _HwBfdSessState_Type()
)
hwBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessState.setStatus("current")


class _HwBfdSessDiag_Type(Integer32):
    """Custom type hwBfdSessDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HwBfdSessDiag_Type.__name__ = "Integer32"
_HwBfdSessDiag_Object = MibTableColumn
hwBfdSessDiag = _HwBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 18),
    _HwBfdSessDiag_Type()
)
hwBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDiag.setStatus("current")
_HwBfdSessSourceAddr_Type = IpAddress
_HwBfdSessSourceAddr_Object = MibTableColumn
hwBfdSessSourceAddr = _HwBfdSessSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 19),
    _HwBfdSessSourceAddr_Type()
)
hwBfdSessSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessSourceAddr.setStatus("current")


class _HwBfdSessVrfIndex_Type(Unsigned32):
    """Custom type hwBfdSessVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessVrfIndex_Type.__name__ = "Unsigned32"
_HwBfdSessVrfIndex_Object = MibTableColumn
hwBfdSessVrfIndex = _HwBfdSessVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 20),
    _HwBfdSessVrfIndex_Type()
)
hwBfdSessVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessVrfIndex.setStatus("current")


class _HwBfdSessVPNName_Type(OctetString):
    """Custom type hwBfdSessVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBfdSessVPNName_Type.__name__ = "OctetString"
_HwBfdSessVPNName_Object = MibTableColumn
hwBfdSessVPNName = _HwBfdSessVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 21),
    _HwBfdSessVPNName_Type()
)
hwBfdSessVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessVPNName.setStatus("current")


class _HwBfdSessType_Type(Integer32):
    """Custom type hwBfdSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("entireDynamic", 3),
          ("static", 1))
    )


_HwBfdSessType_Type.__name__ = "Integer32"
_HwBfdSessType_Object = MibTableColumn
hwBfdSessType = _HwBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 22),
    _HwBfdSessType_Type()
)
hwBfdSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessType.setStatus("current")


class _HwBfdSessBindAppType_Type(Integer32):
    """Custom type hwBfdSessBindAppType based on Integer32"""
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
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 5),
          ("bgpAndOspf", 7),
          ("bgpIsis", 19),
          ("bgpIsisPim", 26),
          ("bgpIspfPim", 25),
          ("bgpOspfIsis", 24),
          ("bgpOspfIsisPim", 28),
          ("bgpPim", 20),
          ("ifnet", 3),
          ("isis", 12),
          ("isisPim", 23),
          ("lspmTnlL2vpnTnlps", 10),
          ("noApplication", 1),
          ("oamLspmL2vpn", 8),
          ("oamLspmTnlL2vpn", 9),
          ("oamMplsfwL2vpn", 11),
          ("ospf", 6),
          ("ospfIsis", 21),
          ("ospfIsisPim", 27),
          ("ospfPim", 22),
          ("pim", 18),
          ("vrrp", 2),
          ("vrrpAndIfnet", 4),
          ("vrrpLspmTnlL2vpnTnlps", 16),
          ("vrrpOamLspmL2vpn", 14),
          ("vrrpOamMplsfwL2vpn", 17),
          ("vrrpOamTnlL2vpn", 15),
          ("vsiPw", 13))
    )


_HwBfdSessBindAppType_Type.__name__ = "Integer32"
_HwBfdSessBindAppType_Object = MibTableColumn
hwBfdSessBindAppType = _HwBfdSessBindAppType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 23),
    _HwBfdSessBindAppType_Type()
)
hwBfdSessBindAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessBindAppType.setStatus("current")


class _HwBfdSessDefaultIp_Type(Integer32):
    """Custom type hwBfdSessDefaultIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HwBfdSessDefaultIp_Type.__name__ = "Integer32"
_HwBfdSessDefaultIp_Object = MibTableColumn
hwBfdSessDefaultIp = _HwBfdSessDefaultIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 24),
    _HwBfdSessDefaultIp_Type()
)
hwBfdSessDefaultIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDefaultIp.setStatus("current")


class _HwBfdSessPISFlag_Type(Integer32):
    """Custom type hwBfdSessPISFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("subif", 3),
          ("true", 2))
    )


_HwBfdSessPISFlag_Type.__name__ = "Integer32"
_HwBfdSessPISFlag_Object = MibTableColumn
hwBfdSessPISFlag = _HwBfdSessPISFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 25),
    _HwBfdSessPISFlag_Type()
)
hwBfdSessPISFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPISFlag.setStatus("current")


class _HwBfdSessBindType_Type(Integer32):
    """Custom type hwBfdSessBindType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("fec", 5),
          ("ifAndSourceIp", 4),
          ("interfaceIp", 1),
          ("isis", 8),
          ("ldpLsp", 9),
          ("ospf", 7),
          ("peerIp", 2),
          ("pw", 13),
          ("sourceIp", 3),
          ("staticLsp", 10),
          ("teLsp", 11),
          ("teTunnel", 12),
          ("tunnelIf", 6),
          ("vsiPw", 15))
    )


_HwBfdSessBindType_Type.__name__ = "Integer32"
_HwBfdSessBindType_Object = MibTableColumn
hwBfdSessBindType = _HwBfdSessBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 26),
    _HwBfdSessBindType_Type()
)
hwBfdSessBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessBindType.setStatus("current")
_HwBfdSessNextHop_Type = IpAddress
_HwBfdSessNextHop_Object = MibTableColumn
hwBfdSessNextHop = _HwBfdSessNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 27),
    _HwBfdSessNextHop_Type()
)
hwBfdSessNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessNextHop.setStatus("current")


class _HwBfdSessStaticLspName_Type(OctetString):
    """Custom type hwBfdSessStaticLspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwBfdSessStaticLspName_Type.__name__ = "OctetString"
_HwBfdSessStaticLspName_Object = MibTableColumn
hwBfdSessStaticLspName = _HwBfdSessStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 28),
    _HwBfdSessStaticLspName_Type()
)
hwBfdSessStaticLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessStaticLspName.setStatus("current")


class _HwBfdSessLspIndex_Type(Unsigned32):
    """Custom type hwBfdSessLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessLspIndex_Type.__name__ = "Unsigned32"
_HwBfdSessLspIndex_Object = MibTableColumn
hwBfdSessLspIndex = _HwBfdSessLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 29),
    _HwBfdSessLspIndex_Type()
)
hwBfdSessLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessLspIndex.setStatus("current")


class _HwBfdSessPWSecondaryFlag_Type(Integer32):
    """Custom type hwBfdSessPWSecondaryFlag based on Integer32"""
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
        *(("flagMasterPW", 1),
          ("flagNoPW", 3),
          ("flagSecondaryPW", 2))
    )


_HwBfdSessPWSecondaryFlag_Type.__name__ = "Integer32"
_HwBfdSessPWSecondaryFlag_Object = MibTableColumn
hwBfdSessPWSecondaryFlag = _HwBfdSessPWSecondaryFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 30),
    _HwBfdSessPWSecondaryFlag_Type()
)
hwBfdSessPWSecondaryFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPWSecondaryFlag.setStatus("current")


class _HwBfdSessTunnelDetectType_Type(Integer32):
    """Custom type hwBfdSessTunnelDetectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flagBothDown", 1),
          ("flagNeighborDown", 2))
    )


_HwBfdSessTunnelDetectType_Type.__name__ = "Integer32"
_HwBfdSessTunnelDetectType_Object = MibTableColumn
hwBfdSessTunnelDetectType = _HwBfdSessTunnelDetectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 31),
    _HwBfdSessTunnelDetectType_Type()
)
hwBfdSessTunnelDetectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessTunnelDetectType.setStatus("current")


class _HwBfdSessVcId_Type(Unsigned32):
    """Custom type hwBfdSessVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwBfdSessVcId_Type.__name__ = "Unsigned32"
_HwBfdSessVcId_Object = MibTableColumn
hwBfdSessVcId = _HwBfdSessVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 32),
    _HwBfdSessVcId_Type()
)
hwBfdSessVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessVcId.setStatus("current")


class _HwBfdSessVsiName_Type(OctetString):
    """Custom type hwBfdSessVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBfdSessVsiName_Type.__name__ = "OctetString"
_HwBfdSessVsiName_Object = MibTableColumn
hwBfdSessVsiName = _HwBfdSessVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 33),
    _HwBfdSessVsiName_Type()
)
hwBfdSessVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessVsiName.setStatus("current")
_HwBfdSessVsiPeerAddr_Type = IpAddress
_HwBfdSessVsiPeerAddr_Object = MibTableColumn
hwBfdSessVsiPeerAddr = _HwBfdSessVsiPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 34),
    _HwBfdSessVsiPeerAddr_Type()
)
hwBfdSessVsiPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessVsiPeerAddr.setStatus("current")


class _HwBfdSessDiscrAuto_Type(EnabledStatus):
    """Custom type hwBfdSessDiscrAuto based on EnabledStatus"""


_HwBfdSessDiscrAuto_Object = MibTableColumn
hwBfdSessDiscrAuto = _HwBfdSessDiscrAuto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 3, 1, 35),
    _HwBfdSessDiscrAuto_Type()
)
hwBfdSessDiscrAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessDiscrAuto.setStatus("current")
_HwBfdSessionPerTable_Object = MibTable
hwBfdSessionPerTable = _HwBfdSessionPerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4)
)
if mibBuilder.loadTexts:
    hwBfdSessionPerTable.setStatus("current")
_HwBfdSessionPerEntry_Object = MibTableRow
hwBfdSessionPerEntry = _HwBfdSessionPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1)
)
hwBfdSessionPerEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdSessPerIndex"),
)
if mibBuilder.loadTexts:
    hwBfdSessionPerEntry.setStatus("current")


class _HwBfdSessPerIndex_Type(Unsigned32):
    """Custom type hwBfdSessPerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBfdSessPerIndex_Type.__name__ = "Unsigned32"
_HwBfdSessPerIndex_Object = MibTableColumn
hwBfdSessPerIndex = _HwBfdSessPerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 1),
    _HwBfdSessPerIndex_Type()
)
hwBfdSessPerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdSessPerIndex.setStatus("current")
_HwBfdSessPerfPktIn_Type = Counter32
_HwBfdSessPerfPktIn_Object = MibTableColumn
hwBfdSessPerfPktIn = _HwBfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 2),
    _HwBfdSessPerfPktIn_Type()
)
hwBfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfPktIn.setStatus("current")
_HwBfdSessPerfPktInHC_Type = Counter32
_HwBfdSessPerfPktInHC_Object = MibTableColumn
hwBfdSessPerfPktInHC = _HwBfdSessPerfPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 3),
    _HwBfdSessPerfPktInHC_Type()
)
hwBfdSessPerfPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfPktInHC.setStatus("current")
_HwBfdSessPerfPktOut_Type = Counter32
_HwBfdSessPerfPktOut_Object = MibTableColumn
hwBfdSessPerfPktOut = _HwBfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 4),
    _HwBfdSessPerfPktOut_Type()
)
hwBfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfPktOut.setStatus("current")
_HwBfdSessPerfPktOutHC_Type = Counter32
_HwBfdSessPerfPktOutHC_Object = MibTableColumn
hwBfdSessPerfPktOutHC = _HwBfdSessPerfPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 5),
    _HwBfdSessPerfPktOutHC_Type()
)
hwBfdSessPerfPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfPktOutHC.setStatus("current")
_HwBfdSessPerfBadIn_Type = Counter32
_HwBfdSessPerfBadIn_Object = MibTableColumn
hwBfdSessPerfBadIn = _HwBfdSessPerfBadIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 6),
    _HwBfdSessPerfBadIn_Type()
)
hwBfdSessPerfBadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfBadIn.setStatus("current")
_HwBfdSessPerfBadInHC_Type = Counter32
_HwBfdSessPerfBadInHC_Object = MibTableColumn
hwBfdSessPerfBadInHC = _HwBfdSessPerfBadInHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 7),
    _HwBfdSessPerfBadInHC_Type()
)
hwBfdSessPerfBadInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfBadInHC.setStatus("current")
_HwBfdSessPerfBadOut_Type = Counter32
_HwBfdSessPerfBadOut_Object = MibTableColumn
hwBfdSessPerfBadOut = _HwBfdSessPerfBadOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 8),
    _HwBfdSessPerfBadOut_Type()
)
hwBfdSessPerfBadOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfBadOut.setStatus("current")
_HwBfdSessPerfBadOutHC_Type = Counter32
_HwBfdSessPerfBadOutHC_Object = MibTableColumn
hwBfdSessPerfBadOutHC = _HwBfdSessPerfBadOutHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 9),
    _HwBfdSessPerfBadOutHC_Type()
)
hwBfdSessPerfBadOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfBadOutHC.setStatus("current")
_HwBfdSessPerfLastSessDownTime_Type = OctetString
_HwBfdSessPerfLastSessDownTime_Object = MibTableColumn
hwBfdSessPerfLastSessDownTime = _HwBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 10),
    _HwBfdSessPerfLastSessDownTime_Type()
)
hwBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfLastSessDownTime.setStatus("current")
_HwBfdSessPerfSessDownCount_Type = Unsigned32
_HwBfdSessPerfSessDownCount_Object = MibTableColumn
hwBfdSessPerfSessDownCount = _HwBfdSessPerfSessDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 11),
    _HwBfdSessPerfSessDownCount_Type()
)
hwBfdSessPerfSessDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfSessDownCount.setStatus("current")
_HwBfdSessPerfSessShortBreakCount_Type = Unsigned32
_HwBfdSessPerfSessShortBreakCount_Object = MibTableColumn
hwBfdSessPerfSessShortBreakCount = _HwBfdSessPerfSessShortBreakCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 12),
    _HwBfdSessPerfSessShortBreakCount_Type()
)
hwBfdSessPerfSessShortBreakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessPerfSessShortBreakCount.setStatus("current")
_HwBfdSessionPerStartTime_Type = OctetString
_HwBfdSessionPerStartTime_Object = MibTableColumn
hwBfdSessionPerStartTime = _HwBfdSessionPerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 4, 1, 13),
    _HwBfdSessionPerStartTime_Type()
)
hwBfdSessionPerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSessionPerStartTime.setStatus("current")
_HwBfdSlotTable_Object = MibTable
hwBfdSlotTable = _HwBfdSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5)
)
if mibBuilder.loadTexts:
    hwBfdSlotTable.setStatus("current")
_HwBfdSlotEntry_Object = MibTableRow
hwBfdSlotEntry = _HwBfdSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1)
)
hwBfdSlotEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdSlotID"),
)
if mibBuilder.loadTexts:
    hwBfdSlotEntry.setStatus("current")


class _HwBfdSlotID_Type(Unsigned32):
    """Custom type hwBfdSlotID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HwBfdSlotID_Type.__name__ = "Unsigned32"
_HwBfdSlotID_Object = MibTableColumn
hwBfdSlotID = _HwBfdSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1, 1),
    _HwBfdSlotID_Type()
)
hwBfdSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdSlotID.setStatus("current")


class _HwBfdSlotReserveOneHopSessNum_Type(Unsigned32):
    """Custom type hwBfdSlotReserveOneHopSessNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HwBfdSlotReserveOneHopSessNum_Type.__name__ = "Unsigned32"
_HwBfdSlotReserveOneHopSessNum_Object = MibTableColumn
hwBfdSlotReserveOneHopSessNum = _HwBfdSlotReserveOneHopSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1, 2),
    _HwBfdSlotReserveOneHopSessNum_Type()
)
hwBfdSlotReserveOneHopSessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSlotReserveOneHopSessNum.setStatus("current")


class _HwBfdSlotOneHopSessNum_Type(Unsigned32):
    """Custom type hwBfdSlotOneHopSessNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HwBfdSlotOneHopSessNum_Type.__name__ = "Unsigned32"
_HwBfdSlotOneHopSessNum_Object = MibTableColumn
hwBfdSlotOneHopSessNum = _HwBfdSlotOneHopSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1, 3),
    _HwBfdSlotOneHopSessNum_Type()
)
hwBfdSlotOneHopSessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSlotOneHopSessNum.setStatus("obsolete")


class _HwBfdSlotCurrentSessNum_Type(Unsigned32):
    """Custom type hwBfdSlotCurrentSessNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HwBfdSlotCurrentSessNum_Type.__name__ = "Unsigned32"
_HwBfdSlotCurrentSessNum_Object = MibTableColumn
hwBfdSlotCurrentSessNum = _HwBfdSlotCurrentSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1, 4),
    _HwBfdSlotCurrentSessNum_Type()
)
hwBfdSlotCurrentSessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBfdSlotCurrentSessNum.setStatus("current")
_HwBfdSlotRowStatus_Type = RowStatus
_HwBfdSlotRowStatus_Object = MibTableColumn
hwBfdSlotRowStatus = _HwBfdSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 5, 1, 5),
    _HwBfdSlotRowStatus_Type()
)
hwBfdSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdSlotRowStatus.setStatus("current")
_HwBfdTtlConfTable_Object = MibTable
hwBfdTtlConfTable = _HwBfdTtlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6)
)
if mibBuilder.loadTexts:
    hwBfdTtlConfTable.setStatus("current")
_HwBfdTtlConfEntry_Object = MibTableRow
hwBfdTtlConfEntry = _HwBfdTtlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1)
)
hwBfdTtlConfEntry.setIndexNames(
    (0, "HUAWEI-BFD-MIB", "hwBfdTtlConfAddr"),
    (0, "HUAWEI-BFD-MIB", "hwBfdTtlConfMaskLen"),
    (0, "HUAWEI-BFD-MIB", "hwBfdTtlConfType"),
)
if mibBuilder.loadTexts:
    hwBfdTtlConfEntry.setStatus("current")
_HwBfdTtlConfAddr_Type = IpAddress
_HwBfdTtlConfAddr_Object = MibTableColumn
hwBfdTtlConfAddr = _HwBfdTtlConfAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1, 1),
    _HwBfdTtlConfAddr_Type()
)
hwBfdTtlConfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdTtlConfAddr.setStatus("current")


class _HwBfdTtlConfMaskLen_Type(Integer32):
    """Custom type hwBfdTtlConfMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_HwBfdTtlConfMaskLen_Type.__name__ = "Integer32"
_HwBfdTtlConfMaskLen_Object = MibTableColumn
hwBfdTtlConfMaskLen = _HwBfdTtlConfMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1, 2),
    _HwBfdTtlConfMaskLen_Type()
)
hwBfdTtlConfMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdTtlConfMaskLen.setStatus("current")


class _HwBfdTtlConfType_Type(Integer32):
    """Custom type hwBfdTtlConfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiHop", 2),
          ("singleHop", 1))
    )


_HwBfdTtlConfType_Type.__name__ = "Integer32"
_HwBfdTtlConfType_Object = MibTableColumn
hwBfdTtlConfType = _HwBfdTtlConfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1, 3),
    _HwBfdTtlConfType_Type()
)
hwBfdTtlConfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBfdTtlConfType.setStatus("current")


class _HwBfdTtlConfValue_Type(Integer32):
    """Custom type hwBfdTtlConfValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwBfdTtlConfValue_Type.__name__ = "Integer32"
_HwBfdTtlConfValue_Object = MibTableColumn
hwBfdTtlConfValue = _HwBfdTtlConfValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1, 4),
    _HwBfdTtlConfValue_Type()
)
hwBfdTtlConfValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdTtlConfValue.setStatus("current")
_HwBfdTtlConfRowStatus_Type = RowStatus
_HwBfdTtlConfRowStatus_Object = MibTableColumn
hwBfdTtlConfRowStatus = _HwBfdTtlConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 2, 6, 1, 50),
    _HwBfdTtlConfRowStatus_Type()
)
hwBfdTtlConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBfdTtlConfRowStatus.setStatus("current")
_HwBfdNotifications_ObjectIdentity = ObjectIdentity
hwBfdNotifications = _HwBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 3)
)
_HwBfdConformance_ObjectIdentity = ObjectIdentity
hwBfdConformance = _HwBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4)
)
_HwBfdCompliances_ObjectIdentity = ObjectIdentity
hwBfdCompliances = _HwBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 1)
)
_HwBfdGroups_ObjectIdentity = ObjectIdentity
hwBfdGroups = _HwBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 2)
)

# Managed Objects groups

hwBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 2, 1)
)
hwBfdGroup.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdVersionNumber"),
        ("HUAWEI-BFD-MIB", "hwBfdAdminStatus"),
        ("HUAWEI-BFD-MIB", "hwBfdSessLimitNumber"),
        ("HUAWEI-BFD-MIB", "hwBfdSessInterfaceLimitNumber"),
        ("HUAWEI-BFD-MIB", "hwBfdSessStaticNumber"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDynamicNumber"),
        ("HUAWEI-BFD-MIB", "hwBfdSessGlobalDefaultIpAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdEchoPassiveStatus"),
        ("HUAWEI-BFD-MIB", "hwBfdEchoAclNum"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDynamicPingInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDynamicSupportPassive"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDelayUpTime"),
        ("HUAWEI-BFD-MIB", "hwBfdSessMultiDstPort"),
        ("HUAWEI-BFD-MIB", "hwBfdTrapSendInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdIfConfName"),
        ("HUAWEI-BFD-MIB", "hwBfdIfConfDeleting"),
        ("HUAWEI-BFD-MIB", "hwBfdIfConfAvailable"),
        ("HUAWEI-BFD-MIB", "hwBfdIfConfSessCnt"),
        ("HUAWEI-BFD-MIB", "hwBfdIfConfRowStatus"),
        ("HUAWEI-BFD-MIB", "hwBfdSlotReserveOneHopSessNum"),
        ("HUAWEI-BFD-MIB", "hwBfdSlotCurrentSessNum"),
        ("HUAWEI-BFD-MIB", "hwBfdSlotRowStatus"))
)
if mibBuilder.loadTexts:
    hwBfdGroup.setStatus("current")

hwBfdSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 2, 2)
)
hwBfdSessGroup.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdSessConfMIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfLocalDiscr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfRemoteDiscr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfBindIfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfBindIfName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDemandEnable"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDemandTimerInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDetectMult"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDesiredMinRxInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDesiredMinTxInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfWTRInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfTOS"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfPSTFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfCommitFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfAdminStatus"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfRowStatus"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfSourceAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfVrfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfVPNName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDefaultIp"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfPISFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfBindType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfNextHop"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfStaticLspName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfPWSecondaryFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfTunnelDetectType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfVcId"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfVsiName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfVsiPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessConfDiscrAuto"),
        ("HUAWEI-BFD-MIB", "hwBfdSessMIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindVRRP"),
        ("HUAWEI-BFD-MIB", "hwBfdSessCfgName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessLocalDiscr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessRemoteDiscr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessOperMode"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDetectMult"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDemandTimerInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessActualRxInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessActualTxInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessWTRInterval"),
        ("HUAWEI-BFD-MIB", "hwBfdSessTOS"),
        ("HUAWEI-BFD-MIB", "hwBfdSessState"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessSourceAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVrfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVPNName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindAppType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDefaultIp"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPISFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessNextHop"),
        ("HUAWEI-BFD-MIB", "hwBfdSessStaticLspName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessLspIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPWSecondaryFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessTunnelDetectType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVcId"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiscrAuto"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfPktIn"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfPktInHC"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfPktOut"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfPktOutHC"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfBadIn"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfBadInHC"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfBadOut"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfBadOutHC"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfLastSessDownTime"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfSessDownCount"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPerfSessShortBreakCount"),
        ("HUAWEI-BFD-MIB", "hwBfdSessionPerStartTime"),
        ("HUAWEI-BFD-MIB", "hwBfdTtlConfValue"),
        ("HUAWEI-BFD-MIB", "hwBfdTtlConfRowStatus"))
)
if mibBuilder.loadTexts:
    hwBfdSessGroup.setStatus("current")

hwBfdObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 2, 3)
)
hwBfdObsoleteGroup.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdIfConfEnable"),
        ("HUAWEI-BFD-MIB", "hwBfdSlotOneHopSessNum"))
)
if mibBuilder.loadTexts:
    hwBfdObsoleteGroup.setStatus("obsolete")


# Notification objects

hwBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 3, 1)
)
hwBfdSessDown.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdSessCfgName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVrfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVPNName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDefaultIp"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessStaticLspName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPWSecondaryFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessNextHop"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVcId"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiscrAuto"))
)
if mibBuilder.loadTexts:
    hwBfdSessDown.setStatus(
        "current"
    )

hwBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 3, 2)
)
hwBfdSessUp.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdSessCfgName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindIfName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVrfIndex"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVPNName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDefaultIp"),
        ("HUAWEI-BFD-MIB", "hwBfdSessBindType"),
        ("HUAWEI-BFD-MIB", "hwBfdSessStaticLspName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessPWSecondaryFlag"),
        ("HUAWEI-BFD-MIB", "hwBfdSessNextHop"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVcId"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessVsiPeerAddr"),
        ("HUAWEI-BFD-MIB", "hwBfdSessDiscrAuto"))
)
if mibBuilder.loadTexts:
    hwBfdSessUp.setStatus(
        "current"
    )

hwBfdSessReachLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 3, 3)
)
hwBfdSessReachLimit.setObjects(
    ("HUAWEI-BFD-MIB", "hwBfdSessLimitNumber")
)
if mibBuilder.loadTexts:
    hwBfdSessReachLimit.setStatus(
        "current"
    )

hwBfdSessReachLimitBindIf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 3, 4)
)
hwBfdSessReachLimitBindIf.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdSessConfBindIfName"),
        ("HUAWEI-BFD-MIB", "hwBfdSessInterfaceLimitNumber"))
)
if mibBuilder.loadTexts:
    hwBfdSessReachLimitBindIf.setStatus(
        "current"
    )


# Notifications groups

hwBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 2, 4)
)
hwBfdNotificationGroup.setObjects(
      *(("HUAWEI-BFD-MIB", "hwBfdSessDown"),
        ("HUAWEI-BFD-MIB", "hwBfdSessUp"),
        ("HUAWEI-BFD-MIB", "hwBfdSessReachLimit"),
        ("HUAWEI-BFD-MIB", "hwBfdSessReachLimitBindIf"))
)
if mibBuilder.loadTexts:
    hwBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBfdFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 38, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwBfdFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BFD-MIB",
    **{"BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "hwBFDMIB": hwBFDMIB,
       "hwBfdScalarsObjects": hwBfdScalarsObjects,
       "hwBfdVersionNumber": hwBfdVersionNumber,
       "hwBfdAdminStatus": hwBfdAdminStatus,
       "hwBfdSessLimitNumber": hwBfdSessLimitNumber,
       "hwBfdSessInterfaceLimitNumber": hwBfdSessInterfaceLimitNumber,
       "hwBfdSessStaticNumber": hwBfdSessStaticNumber,
       "hwBfdSessDynamicNumber": hwBfdSessDynamicNumber,
       "hwBfdSessGlobalDefaultIpAddr": hwBfdSessGlobalDefaultIpAddr,
       "hwBfdEchoPassiveStatus": hwBfdEchoPassiveStatus,
       "hwBfdEchoAclNum": hwBfdEchoAclNum,
       "hwBfdSessDynamicPingInterval": hwBfdSessDynamicPingInterval,
       "hwBfdSessDynamicSupportPassive": hwBfdSessDynamicSupportPassive,
       "hwBfdSessDelayUpTime": hwBfdSessDelayUpTime,
       "hwBfdSessMultiDstPort": hwBfdSessMultiDstPort,
       "hwBfdTrapSendInterval": hwBfdTrapSendInterval,
       "hwBfdObjects": hwBfdObjects,
       "hwBfdIfConfTable": hwBfdIfConfTable,
       "hwBfdIfConfEntry": hwBfdIfConfEntry,
       "hwBfdIfConfIndex": hwBfdIfConfIndex,
       "hwBfdIfConfName": hwBfdIfConfName,
       "hwBfdIfConfEnable": hwBfdIfConfEnable,
       "hwBfdIfConfDeleting": hwBfdIfConfDeleting,
       "hwBfdIfConfAvailable": hwBfdIfConfAvailable,
       "hwBfdIfConfSessCnt": hwBfdIfConfSessCnt,
       "hwBfdIfConfRowStatus": hwBfdIfConfRowStatus,
       "hwBfdSessionConfTable": hwBfdSessionConfTable,
       "hwBfdSessionConfEntry": hwBfdSessionConfEntry,
       "hwBfdSessConfName": hwBfdSessConfName,
       "hwBfdSessConfMIndex": hwBfdSessConfMIndex,
       "hwBfdSessConfLocalDiscr": hwBfdSessConfLocalDiscr,
       "hwBfdSessConfRemoteDiscr": hwBfdSessConfRemoteDiscr,
       "hwBfdSessConfPeerAddr": hwBfdSessConfPeerAddr,
       "hwBfdSessConfBindIfIndex": hwBfdSessConfBindIfIndex,
       "hwBfdSessConfBindIfName": hwBfdSessConfBindIfName,
       "hwBfdSessConfDemandEnable": hwBfdSessConfDemandEnable,
       "hwBfdSessConfDemandTimerInterval": hwBfdSessConfDemandTimerInterval,
       "hwBfdSessConfDetectMult": hwBfdSessConfDetectMult,
       "hwBfdSessConfDesiredMinRxInterval": hwBfdSessConfDesiredMinRxInterval,
       "hwBfdSessConfDesiredMinTxInterval": hwBfdSessConfDesiredMinTxInterval,
       "hwBfdSessConfWTRInterval": hwBfdSessConfWTRInterval,
       "hwBfdSessConfTOS": hwBfdSessConfTOS,
       "hwBfdSessConfPSTFlag": hwBfdSessConfPSTFlag,
       "hwBfdSessConfCommitFlag": hwBfdSessConfCommitFlag,
       "hwBfdSessConfAdminStatus": hwBfdSessConfAdminStatus,
       "hwBfdSessConfRowStatus": hwBfdSessConfRowStatus,
       "hwBfdSessConfSourceAddr": hwBfdSessConfSourceAddr,
       "hwBfdSessConfVrfIndex": hwBfdSessConfVrfIndex,
       "hwBfdSessConfVPNName": hwBfdSessConfVPNName,
       "hwBfdSessConfDefaultIp": hwBfdSessConfDefaultIp,
       "hwBfdSessConfPISFlag": hwBfdSessConfPISFlag,
       "hwBfdSessConfBindType": hwBfdSessConfBindType,
       "hwBfdSessConfNextHop": hwBfdSessConfNextHop,
       "hwBfdSessConfStaticLspName": hwBfdSessConfStaticLspName,
       "hwBfdSessConfPWSecondaryFlag": hwBfdSessConfPWSecondaryFlag,
       "hwBfdSessConfTunnelDetectType": hwBfdSessConfTunnelDetectType,
       "hwBfdSessConfVcId": hwBfdSessConfVcId,
       "hwBfdSessConfVsiName": hwBfdSessConfVsiName,
       "hwBfdSessConfVsiPeerAddr": hwBfdSessConfVsiPeerAddr,
       "hwBfdSessConfDiscrAuto": hwBfdSessConfDiscrAuto,
       "hwBfdSessionTable": hwBfdSessionTable,
       "hwBfdSessionEntry": hwBfdSessionEntry,
       "hwBfdSessIndex": hwBfdSessIndex,
       "hwBfdSessMIndex": hwBfdSessMIndex,
       "hwBfdSessBindVRRP": hwBfdSessBindVRRP,
       "hwBfdSessCfgName": hwBfdSessCfgName,
       "hwBfdSessPeerAddr": hwBfdSessPeerAddr,
       "hwBfdSessBindIfIndex": hwBfdSessBindIfIndex,
       "hwBfdSessBindIfName": hwBfdSessBindIfName,
       "hwBfdSessLocalDiscr": hwBfdSessLocalDiscr,
       "hwBfdSessRemoteDiscr": hwBfdSessRemoteDiscr,
       "hwBfdSessOperMode": hwBfdSessOperMode,
       "hwBfdSessDetectMult": hwBfdSessDetectMult,
       "hwBfdSessDemandTimerInterval": hwBfdSessDemandTimerInterval,
       "hwBfdSessActualRxInterval": hwBfdSessActualRxInterval,
       "hwBfdSessActualTxInterval": hwBfdSessActualTxInterval,
       "hwBfdSessWTRInterval": hwBfdSessWTRInterval,
       "hwBfdSessTOS": hwBfdSessTOS,
       "hwBfdSessState": hwBfdSessState,
       "hwBfdSessDiag": hwBfdSessDiag,
       "hwBfdSessSourceAddr": hwBfdSessSourceAddr,
       "hwBfdSessVrfIndex": hwBfdSessVrfIndex,
       "hwBfdSessVPNName": hwBfdSessVPNName,
       "hwBfdSessType": hwBfdSessType,
       "hwBfdSessBindAppType": hwBfdSessBindAppType,
       "hwBfdSessDefaultIp": hwBfdSessDefaultIp,
       "hwBfdSessPISFlag": hwBfdSessPISFlag,
       "hwBfdSessBindType": hwBfdSessBindType,
       "hwBfdSessNextHop": hwBfdSessNextHop,
       "hwBfdSessStaticLspName": hwBfdSessStaticLspName,
       "hwBfdSessLspIndex": hwBfdSessLspIndex,
       "hwBfdSessPWSecondaryFlag": hwBfdSessPWSecondaryFlag,
       "hwBfdSessTunnelDetectType": hwBfdSessTunnelDetectType,
       "hwBfdSessVcId": hwBfdSessVcId,
       "hwBfdSessVsiName": hwBfdSessVsiName,
       "hwBfdSessVsiPeerAddr": hwBfdSessVsiPeerAddr,
       "hwBfdSessDiscrAuto": hwBfdSessDiscrAuto,
       "hwBfdSessionPerTable": hwBfdSessionPerTable,
       "hwBfdSessionPerEntry": hwBfdSessionPerEntry,
       "hwBfdSessPerIndex": hwBfdSessPerIndex,
       "hwBfdSessPerfPktIn": hwBfdSessPerfPktIn,
       "hwBfdSessPerfPktInHC": hwBfdSessPerfPktInHC,
       "hwBfdSessPerfPktOut": hwBfdSessPerfPktOut,
       "hwBfdSessPerfPktOutHC": hwBfdSessPerfPktOutHC,
       "hwBfdSessPerfBadIn": hwBfdSessPerfBadIn,
       "hwBfdSessPerfBadInHC": hwBfdSessPerfBadInHC,
       "hwBfdSessPerfBadOut": hwBfdSessPerfBadOut,
       "hwBfdSessPerfBadOutHC": hwBfdSessPerfBadOutHC,
       "hwBfdSessPerfLastSessDownTime": hwBfdSessPerfLastSessDownTime,
       "hwBfdSessPerfSessDownCount": hwBfdSessPerfSessDownCount,
       "hwBfdSessPerfSessShortBreakCount": hwBfdSessPerfSessShortBreakCount,
       "hwBfdSessionPerStartTime": hwBfdSessionPerStartTime,
       "hwBfdSlotTable": hwBfdSlotTable,
       "hwBfdSlotEntry": hwBfdSlotEntry,
       "hwBfdSlotID": hwBfdSlotID,
       "hwBfdSlotReserveOneHopSessNum": hwBfdSlotReserveOneHopSessNum,
       "hwBfdSlotOneHopSessNum": hwBfdSlotOneHopSessNum,
       "hwBfdSlotCurrentSessNum": hwBfdSlotCurrentSessNum,
       "hwBfdSlotRowStatus": hwBfdSlotRowStatus,
       "hwBfdTtlConfTable": hwBfdTtlConfTable,
       "hwBfdTtlConfEntry": hwBfdTtlConfEntry,
       "hwBfdTtlConfAddr": hwBfdTtlConfAddr,
       "hwBfdTtlConfMaskLen": hwBfdTtlConfMaskLen,
       "hwBfdTtlConfType": hwBfdTtlConfType,
       "hwBfdTtlConfValue": hwBfdTtlConfValue,
       "hwBfdTtlConfRowStatus": hwBfdTtlConfRowStatus,
       "hwBfdNotifications": hwBfdNotifications,
       "hwBfdSessDown": hwBfdSessDown,
       "hwBfdSessUp": hwBfdSessUp,
       "hwBfdSessReachLimit": hwBfdSessReachLimit,
       "hwBfdSessReachLimitBindIf": hwBfdSessReachLimitBindIf,
       "hwBfdConformance": hwBfdConformance,
       "hwBfdCompliances": hwBfdCompliances,
       "hwBfdFullCompliance": hwBfdFullCompliance,
       "hwBfdGroups": hwBfdGroups,
       "hwBfdGroup": hwBfdGroup,
       "hwBfdSessGroup": hwBfdSessGroup,
       "hwBfdObsoleteGroup": hwBfdObsoleteGroup,
       "hwBfdNotificationGroup": hwBfdNotificationGroup}
)
