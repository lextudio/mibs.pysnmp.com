# SNMP MIB module (HUAWEI-HWTACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-HWTACACS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:58 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwTACACS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20)
)
hwTACACS.setRevisions(
        ("2015-07-29 19:15",
         "2015-05-06 16:00",
         "2013-08-24 11:00",
         "2013-07-05 11:00",
         "2013-03-08 16:00",
         "2014-02-25 16:00",
         "2015-04-01 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTACACSServerConfig_ObjectIdentity = ObjectIdentity
hwTACACSServerConfig = _HwTACACSServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1)
)
_HwTACACSServerGroupTable_Object = MibTable
hwTACACSServerGroupTable = _HwTACACSServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1)
)
if mibBuilder.loadTexts:
    hwTACACSServerGroupTable.setStatus("current")
_HwTACACSServerGroupEntry_Object = MibTableRow
hwTACACSServerGroupEntry = _HwTACACSServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1)
)
hwTACACSServerGroupEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupIndex"),
)
if mibBuilder.loadTexts:
    hwTACACSServerGroupEntry.setStatus("current")


class _HwTACACSServerGroupIndex_Type(Integer32):
    """Custom type hwTACACSServerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwTACACSServerGroupIndex_Type.__name__ = "Integer32"
_HwTACACSServerGroupIndex_Object = MibTableColumn
hwTACACSServerGroupIndex = _HwTACACSServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 1),
    _HwTACACSServerGroupIndex_Type()
)
hwTACACSServerGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupIndex.setStatus("current")


class _HwTACACSServerGroupName_Type(OctetString):
    """Custom type hwTACACSServerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwTACACSServerGroupName_Type.__name__ = "OctetString"
_HwTACACSServerGroupName_Object = MibTableColumn
hwTACACSServerGroupName = _HwTACACSServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 2),
    _HwTACACSServerGroupName_Type()
)
hwTACACSServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupName.setStatus("current")
_HwTACACSServerGroupSourceIP_Type = IpAddress
_HwTACACSServerGroupSourceIP_Object = MibTableColumn
hwTACACSServerGroupSourceIP = _HwTACACSServerGroupSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 3),
    _HwTACACSServerGroupSourceIP_Type()
)
hwTACACSServerGroupSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSourceIP.setStatus("current")


class _HwTACACSServerGroupKey_Type(OctetString):
    """Custom type hwTACACSServerGroupKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwTACACSServerGroupKey_Type.__name__ = "OctetString"
_HwTACACSServerGroupKey_Object = MibTableColumn
hwTACACSServerGroupKey = _HwTACACSServerGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 4),
    _HwTACACSServerGroupKey_Type()
)
hwTACACSServerGroupKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupKey.setStatus("current")


class _HwTACACSServerGroupTimer_Type(Integer32):
    """Custom type hwTACACSServerGroupTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwTACACSServerGroupTimer_Type.__name__ = "Integer32"
_HwTACACSServerGroupTimer_Object = MibTableColumn
hwTACACSServerGroupTimer = _HwTACACSServerGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 5),
    _HwTACACSServerGroupTimer_Type()
)
hwTACACSServerGroupTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupTimer.setStatus("current")


class _HwTACACSServerGroupDomain_Type(Integer32):
    """Custom type hwTACACSServerGroupDomain based on Integer32"""
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
        *(("close", 2),
          ("open", 1),
          ("original", 3))
    )


_HwTACACSServerGroupDomain_Type.__name__ = "Integer32"
_HwTACACSServerGroupDomain_Object = MibTableColumn
hwTACACSServerGroupDomain = _HwTACACSServerGroupDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 6),
    _HwTACACSServerGroupDomain_Type()
)
hwTACACSServerGroupDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupDomain.setStatus("current")


class _HwTACACSServerGroupOctFmt_Type(Integer32):
    """Custom type hwTACACSServerGroupOctFmt based on Integer32"""
    defaultValue = 1

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
        *(("byte", 1),
          ("gbyte", 4),
          ("kbyte", 2),
          ("mbyte", 3))
    )


_HwTACACSServerGroupOctFmt_Type.__name__ = "Integer32"
_HwTACACSServerGroupOctFmt_Object = MibTableColumn
hwTACACSServerGroupOctFmt = _HwTACACSServerGroupOctFmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 7),
    _HwTACACSServerGroupOctFmt_Type()
)
hwTACACSServerGroupOctFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupOctFmt.setStatus("current")


class _HwTACACSServerGroupTimeout_Type(Integer32):
    """Custom type hwTACACSServerGroupTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwTACACSServerGroupTimeout_Type.__name__ = "Integer32"
_HwTACACSServerGroupTimeout_Object = MibTableColumn
hwTACACSServerGroupTimeout = _HwTACACSServerGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 8),
    _HwTACACSServerGroupTimeout_Type()
)
hwTACACSServerGroupTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupTimeout.setStatus("current")
_HwTACACSServerGroupPriAuthenAddr_Type = IpAddress
_HwTACACSServerGroupPriAuthenAddr_Object = MibTableColumn
hwTACACSServerGroupPriAuthenAddr = _HwTACACSServerGroupPriAuthenAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 9),
    _HwTACACSServerGroupPriAuthenAddr_Type()
)
hwTACACSServerGroupPriAuthenAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthenAddr.setStatus("current")


class _HwTACACSServerGroupPriAuthenPort_Type(Integer32):
    """Custom type hwTACACSServerGroupPriAuthenPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupPriAuthenPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupPriAuthenPort_Object = MibTableColumn
hwTACACSServerGroupPriAuthenPort = _HwTACACSServerGroupPriAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 10),
    _HwTACACSServerGroupPriAuthenPort_Type()
)
hwTACACSServerGroupPriAuthenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthenPort.setStatus("current")
_HwTACACSServerGroupPriAuthorAddr_Type = IpAddress
_HwTACACSServerGroupPriAuthorAddr_Object = MibTableColumn
hwTACACSServerGroupPriAuthorAddr = _HwTACACSServerGroupPriAuthorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 11),
    _HwTACACSServerGroupPriAuthorAddr_Type()
)
hwTACACSServerGroupPriAuthorAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthorAddr.setStatus("current")


class _HwTACACSServerGroupPriAuthorPort_Type(Integer32):
    """Custom type hwTACACSServerGroupPriAuthorPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupPriAuthorPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupPriAuthorPort_Object = MibTableColumn
hwTACACSServerGroupPriAuthorPort = _HwTACACSServerGroupPriAuthorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 12),
    _HwTACACSServerGroupPriAuthorPort_Type()
)
hwTACACSServerGroupPriAuthorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthorPort.setStatus("current")
_HwTACACSServerGroupPriAccoutAddr_Type = IpAddress
_HwTACACSServerGroupPriAccoutAddr_Object = MibTableColumn
hwTACACSServerGroupPriAccoutAddr = _HwTACACSServerGroupPriAccoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 13),
    _HwTACACSServerGroupPriAccoutAddr_Type()
)
hwTACACSServerGroupPriAccoutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAccoutAddr.setStatus("current")


class _HwTACACSServerGroupPriAccoutPort_Type(Integer32):
    """Custom type hwTACACSServerGroupPriAccoutPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupPriAccoutPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupPriAccoutPort_Object = MibTableColumn
hwTACACSServerGroupPriAccoutPort = _HwTACACSServerGroupPriAccoutPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 14),
    _HwTACACSServerGroupPriAccoutPort_Type()
)
hwTACACSServerGroupPriAccoutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAccoutPort.setStatus("current")
_HwTACACSServerGroupSecAuthenAddr_Type = IpAddress
_HwTACACSServerGroupSecAuthenAddr_Object = MibTableColumn
hwTACACSServerGroupSecAuthenAddr = _HwTACACSServerGroupSecAuthenAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 15),
    _HwTACACSServerGroupSecAuthenAddr_Type()
)
hwTACACSServerGroupSecAuthenAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAuthenAddr.setStatus("current")


class _HwTACACSServerGroupSecAuthenPort_Type(Integer32):
    """Custom type hwTACACSServerGroupSecAuthenPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupSecAuthenPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupSecAuthenPort_Object = MibTableColumn
hwTACACSServerGroupSecAuthenPort = _HwTACACSServerGroupSecAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 16),
    _HwTACACSServerGroupSecAuthenPort_Type()
)
hwTACACSServerGroupSecAuthenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAuthenPort.setStatus("current")
_HwTACACSServerGroupSecAuthorAddr_Type = IpAddress
_HwTACACSServerGroupSecAuthorAddr_Object = MibTableColumn
hwTACACSServerGroupSecAuthorAddr = _HwTACACSServerGroupSecAuthorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 17),
    _HwTACACSServerGroupSecAuthorAddr_Type()
)
hwTACACSServerGroupSecAuthorAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAuthorAddr.setStatus("current")


class _HwTACACSServerGroupSecAuthorPort_Type(Integer32):
    """Custom type hwTACACSServerGroupSecAuthorPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupSecAuthorPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupSecAuthorPort_Object = MibTableColumn
hwTACACSServerGroupSecAuthorPort = _HwTACACSServerGroupSecAuthorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 18),
    _HwTACACSServerGroupSecAuthorPort_Type()
)
hwTACACSServerGroupSecAuthorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAuthorPort.setStatus("current")
_HwTACACSServerGroupSecAccoutAddr_Type = IpAddress
_HwTACACSServerGroupSecAccoutAddr_Object = MibTableColumn
hwTACACSServerGroupSecAccoutAddr = _HwTACACSServerGroupSecAccoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 19),
    _HwTACACSServerGroupSecAccoutAddr_Type()
)
hwTACACSServerGroupSecAccoutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAccoutAddr.setStatus("current")


class _HwTACACSServerGroupSecAccoutPort_Type(Integer32):
    """Custom type hwTACACSServerGroupSecAccoutPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerGroupSecAccoutPort_Type.__name__ = "Integer32"
_HwTACACSServerGroupSecAccoutPort_Object = MibTableColumn
hwTACACSServerGroupSecAccoutPort = _HwTACACSServerGroupSecAccoutPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 20),
    _HwTACACSServerGroupSecAccoutPort_Type()
)
hwTACACSServerGroupSecAccoutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSecAccoutPort.setStatus("current")
_HwTACACSServerGroupCurAuthenAddr_Type = IpAddress
_HwTACACSServerGroupCurAuthenAddr_Object = MibTableColumn
hwTACACSServerGroupCurAuthenAddr = _HwTACACSServerGroupCurAuthenAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 21),
    _HwTACACSServerGroupCurAuthenAddr_Type()
)
hwTACACSServerGroupCurAuthenAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAuthenAddr.setStatus("current")
_HwTACACSServerGroupCurAuthorAddr_Type = IpAddress
_HwTACACSServerGroupCurAuthorAddr_Object = MibTableColumn
hwTACACSServerGroupCurAuthorAddr = _HwTACACSServerGroupCurAuthorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 22),
    _HwTACACSServerGroupCurAuthorAddr_Type()
)
hwTACACSServerGroupCurAuthorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAuthorAddr.setStatus("current")
_HwTACACSServerGroupCurAccoutAddr_Type = IpAddress
_HwTACACSServerGroupCurAccoutAddr_Object = MibTableColumn
hwTACACSServerGroupCurAccoutAddr = _HwTACACSServerGroupCurAccoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 23),
    _HwTACACSServerGroupCurAccoutAddr_Type()
)
hwTACACSServerGroupCurAccoutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAccoutAddr.setStatus("current")
_HwTACACSPriAuthenClientRoundTripTime_Type = Integer32
_HwTACACSPriAuthenClientRoundTripTime_Object = MibTableColumn
hwTACACSPriAuthenClientRoundTripTime = _HwTACACSPriAuthenClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 24),
    _HwTACACSPriAuthenClientRoundTripTime_Type()
)
hwTACACSPriAuthenClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientRoundTripTime.setStatus("current")
_HwTACACSPriAuthenClientAccessReqPacket_Type = Counter32
_HwTACACSPriAuthenClientAccessReqPacket_Object = MibTableColumn
hwTACACSPriAuthenClientAccessReqPacket = _HwTACACSPriAuthenClientAccessReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 25),
    _HwTACACSPriAuthenClientAccessReqPacket_Type()
)
hwTACACSPriAuthenClientAccessReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessReqPacket.setStatus("current")
_HwTACACSPriAuthenClientAccessReqLogin_Type = Counter32
_HwTACACSPriAuthenClientAccessReqLogin_Object = MibTableColumn
hwTACACSPriAuthenClientAccessReqLogin = _HwTACACSPriAuthenClientAccessReqLogin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 26),
    _HwTACACSPriAuthenClientAccessReqLogin_Type()
)
hwTACACSPriAuthenClientAccessReqLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessReqLogin.setStatus("current")
_HwTACACSPriAuthenClientAccessReqChaPass_Type = Counter32
_HwTACACSPriAuthenClientAccessReqChaPass_Object = MibTableColumn
hwTACACSPriAuthenClientAccessReqChaPass = _HwTACACSPriAuthenClientAccessReqChaPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 27),
    _HwTACACSPriAuthenClientAccessReqChaPass_Type()
)
hwTACACSPriAuthenClientAccessReqChaPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessReqChaPass.setStatus("current")
_HwTACACSPriAuthenClientAccessReqSendPass_Type = Counter32
_HwTACACSPriAuthenClientAccessReqSendPass_Object = MibTableColumn
hwTACACSPriAuthenClientAccessReqSendPass = _HwTACACSPriAuthenClientAccessReqSendPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 28),
    _HwTACACSPriAuthenClientAccessReqSendPass_Type()
)
hwTACACSPriAuthenClientAccessReqSendPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessReqSendPass.setStatus("current")
_HwTACACSPriAuthenClientAccessReqSendAuth_Type = Counter32
_HwTACACSPriAuthenClientAccessReqSendAuth_Object = MibTableColumn
hwTACACSPriAuthenClientAccessReqSendAuth = _HwTACACSPriAuthenClientAccessReqSendAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 29),
    _HwTACACSPriAuthenClientAccessReqSendAuth_Type()
)
hwTACACSPriAuthenClientAccessReqSendAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessReqSendAuth.setStatus("current")
_HwTACACSPriAuthenClientAccessResPack_Type = Counter32
_HwTACACSPriAuthenClientAccessResPack_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResPack = _HwTACACSPriAuthenClientAccessResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 30),
    _HwTACACSPriAuthenClientAccessResPack_Type()
)
hwTACACSPriAuthenClientAccessResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResPack.setStatus("current")
_HwTACACSPriAuthenClientAccessResPass_Type = Counter32
_HwTACACSPriAuthenClientAccessResPass_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResPass = _HwTACACSPriAuthenClientAccessResPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 31),
    _HwTACACSPriAuthenClientAccessResPass_Type()
)
hwTACACSPriAuthenClientAccessResPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResPass.setStatus("current")
_HwTACACSPriAuthenClientAccessResFail_Type = Counter32
_HwTACACSPriAuthenClientAccessResFail_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResFail = _HwTACACSPriAuthenClientAccessResFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 32),
    _HwTACACSPriAuthenClientAccessResFail_Type()
)
hwTACACSPriAuthenClientAccessResFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResFail.setStatus("current")
_HwTACACSPriAuthenClientAccessResGetData_Type = Counter32
_HwTACACSPriAuthenClientAccessResGetData_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResGetData = _HwTACACSPriAuthenClientAccessResGetData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 33),
    _HwTACACSPriAuthenClientAccessResGetData_Type()
)
hwTACACSPriAuthenClientAccessResGetData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResGetData.setStatus("current")
_HwTACACSPriAuthenClientAccessResGetUser_Type = Counter32
_HwTACACSPriAuthenClientAccessResGetUser_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResGetUser = _HwTACACSPriAuthenClientAccessResGetUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 34),
    _HwTACACSPriAuthenClientAccessResGetUser_Type()
)
hwTACACSPriAuthenClientAccessResGetUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResGetUser.setStatus("current")
_HwTACACSPriAuthenClientAccessResGetPass_Type = Counter32
_HwTACACSPriAuthenClientAccessResGetPass_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResGetPass = _HwTACACSPriAuthenClientAccessResGetPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 35),
    _HwTACACSPriAuthenClientAccessResGetPass_Type()
)
hwTACACSPriAuthenClientAccessResGetPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResGetPass.setStatus("current")
_HwTACACSPriAuthenClientAccessResRestart_Type = Counter32
_HwTACACSPriAuthenClientAccessResRestart_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResRestart = _HwTACACSPriAuthenClientAccessResRestart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 36),
    _HwTACACSPriAuthenClientAccessResRestart_Type()
)
hwTACACSPriAuthenClientAccessResRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResRestart.setStatus("current")
_HwTACACSPriAuthenClientAccessResError_Type = Counter32
_HwTACACSPriAuthenClientAccessResError_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResError = _HwTACACSPriAuthenClientAccessResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 37),
    _HwTACACSPriAuthenClientAccessResError_Type()
)
hwTACACSPriAuthenClientAccessResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResError.setStatus("current")
_HwTACACSPriAuthenClientAccessResFollow_Type = Counter32
_HwTACACSPriAuthenClientAccessResFollow_Object = MibTableColumn
hwTACACSPriAuthenClientAccessResFollow = _HwTACACSPriAuthenClientAccessResFollow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 38),
    _HwTACACSPriAuthenClientAccessResFollow_Type()
)
hwTACACSPriAuthenClientAccessResFollow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessResFollow.setStatus("current")
_HwTACACSPriAuthenClientMalformedAccessResponses_Type = Counter32
_HwTACACSPriAuthenClientMalformedAccessResponses_Object = MibTableColumn
hwTACACSPriAuthenClientMalformedAccessResponses = _HwTACACSPriAuthenClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 39),
    _HwTACACSPriAuthenClientMalformedAccessResponses_Type()
)
hwTACACSPriAuthenClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientMalformedAccessResponses.setStatus("current")
_HwTACACSPriAuthenClientAccessConPack_Type = Counter32
_HwTACACSPriAuthenClientAccessConPack_Object = MibTableColumn
hwTACACSPriAuthenClientAccessConPack = _HwTACACSPriAuthenClientAccessConPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 40),
    _HwTACACSPriAuthenClientAccessConPack_Type()
)
hwTACACSPriAuthenClientAccessConPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessConPack.setStatus("current")
_HwTACACSPriAuthenClientAccessConAbort_Type = Counter32
_HwTACACSPriAuthenClientAccessConAbort_Object = MibTableColumn
hwTACACSPriAuthenClientAccessConAbort = _HwTACACSPriAuthenClientAccessConAbort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 41),
    _HwTACACSPriAuthenClientAccessConAbort_Type()
)
hwTACACSPriAuthenClientAccessConAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientAccessConAbort.setStatus("current")
_HwTACACSPriAuthenClientPendingRequests_Type = Counter32
_HwTACACSPriAuthenClientPendingRequests_Object = MibTableColumn
hwTACACSPriAuthenClientPendingRequests = _HwTACACSPriAuthenClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 42),
    _HwTACACSPriAuthenClientPendingRequests_Type()
)
hwTACACSPriAuthenClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientPendingRequests.setStatus("current")
_HwTACACSPriAuthenClientTimeouts_Type = Counter32
_HwTACACSPriAuthenClientTimeouts_Object = MibTableColumn
hwTACACSPriAuthenClientTimeouts = _HwTACACSPriAuthenClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 43),
    _HwTACACSPriAuthenClientTimeouts_Type()
)
hwTACACSPriAuthenClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientTimeouts.setStatus("current")
_HwTACACSPriAuthenClientUnknownTypes_Type = Counter32
_HwTACACSPriAuthenClientUnknownTypes_Object = MibTableColumn
hwTACACSPriAuthenClientUnknownTypes = _HwTACACSPriAuthenClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 44),
    _HwTACACSPriAuthenClientUnknownTypes_Type()
)
hwTACACSPriAuthenClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientUnknownTypes.setStatus("current")
_HwTACACSPriAuthenClientPacketsDropped_Type = Counter32
_HwTACACSPriAuthenClientPacketsDropped_Object = MibTableColumn
hwTACACSPriAuthenClientPacketsDropped = _HwTACACSPriAuthenClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 45),
    _HwTACACSPriAuthenClientPacketsDropped_Type()
)
hwTACACSPriAuthenClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthenClientPacketsDropped.setStatus("current")
_HwTACACSPriAuthorClientRoundTripTime_Type = Integer32
_HwTACACSPriAuthorClientRoundTripTime_Object = MibTableColumn
hwTACACSPriAuthorClientRoundTripTime = _HwTACACSPriAuthorClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 46),
    _HwTACACSPriAuthorClientRoundTripTime_Type()
)
hwTACACSPriAuthorClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientRoundTripTime.setStatus("current")
_HwTACACSPriAuthorClientReqPacket_Type = Counter32
_HwTACACSPriAuthorClientReqPacket_Object = MibTableColumn
hwTACACSPriAuthorClientReqPacket = _HwTACACSPriAuthorClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 47),
    _HwTACACSPriAuthorClientReqPacket_Type()
)
hwTACACSPriAuthorClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientReqPacket.setStatus("current")
_HwTACACSPriAuthorClientReqEXEC_Type = Counter32
_HwTACACSPriAuthorClientReqEXEC_Object = MibTableColumn
hwTACACSPriAuthorClientReqEXEC = _HwTACACSPriAuthorClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 48),
    _HwTACACSPriAuthorClientReqEXEC_Type()
)
hwTACACSPriAuthorClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientReqEXEC.setStatus("current")
_HwTACACSPriAuthorClientReqVPDN_Type = Counter32
_HwTACACSPriAuthorClientReqVPDN_Object = MibTableColumn
hwTACACSPriAuthorClientReqVPDN = _HwTACACSPriAuthorClientReqVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 49),
    _HwTACACSPriAuthorClientReqVPDN_Type()
)
hwTACACSPriAuthorClientReqVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientReqVPDN.setStatus("current")
_HwTACACSPriAuthorClientResPack_Type = Counter32
_HwTACACSPriAuthorClientResPack_Object = MibTableColumn
hwTACACSPriAuthorClientResPack = _HwTACACSPriAuthorClientResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 50),
    _HwTACACSPriAuthorClientResPack_Type()
)
hwTACACSPriAuthorClientResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientResPack.setStatus("current")
_HwTACACSPriAuthorClientResEXEC_Type = Counter32
_HwTACACSPriAuthorClientResEXEC_Object = MibTableColumn
hwTACACSPriAuthorClientResEXEC = _HwTACACSPriAuthorClientResEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 51),
    _HwTACACSPriAuthorClientResEXEC_Type()
)
hwTACACSPriAuthorClientResEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientResEXEC.setStatus("current")
_HwTACACSPriAuthorClientResVPDN_Type = Counter32
_HwTACACSPriAuthorClientResVPDN_Object = MibTableColumn
hwTACACSPriAuthorClientResVPDN = _HwTACACSPriAuthorClientResVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 52),
    _HwTACACSPriAuthorClientResVPDN_Type()
)
hwTACACSPriAuthorClientResVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientResVPDN.setStatus("current")
_HwTACACSPriAuthorClientResError_Type = Counter32
_HwTACACSPriAuthorClientResError_Object = MibTableColumn
hwTACACSPriAuthorClientResError = _HwTACACSPriAuthorClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 53),
    _HwTACACSPriAuthorClientResError_Type()
)
hwTACACSPriAuthorClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientResError.setStatus("current")
_HwTACACSPriAuthorClientReqPending_Type = Counter32
_HwTACACSPriAuthorClientReqPending_Object = MibTableColumn
hwTACACSPriAuthorClientReqPending = _HwTACACSPriAuthorClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 54),
    _HwTACACSPriAuthorClientReqPending_Type()
)
hwTACACSPriAuthorClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientReqPending.setStatus("current")
_HwTACACSPriAuthorClientTimeouts_Type = Counter32
_HwTACACSPriAuthorClientTimeouts_Object = MibTableColumn
hwTACACSPriAuthorClientTimeouts = _HwTACACSPriAuthorClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 55),
    _HwTACACSPriAuthorClientTimeouts_Type()
)
hwTACACSPriAuthorClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientTimeouts.setStatus("current")
_HwTACACSPriAuthorClientUnknownTypes_Type = Counter32
_HwTACACSPriAuthorClientUnknownTypes_Object = MibTableColumn
hwTACACSPriAuthorClientUnknownTypes = _HwTACACSPriAuthorClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 56),
    _HwTACACSPriAuthorClientUnknownTypes_Type()
)
hwTACACSPriAuthorClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientUnknownTypes.setStatus("current")
_HwTACACSPriAuthorClientPacketsDropped_Type = Counter32
_HwTACACSPriAuthorClientPacketsDropped_Object = MibTableColumn
hwTACACSPriAuthorClientPacketsDropped = _HwTACACSPriAuthorClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 57),
    _HwTACACSPriAuthorClientPacketsDropped_Type()
)
hwTACACSPriAuthorClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAuthorClientPacketsDropped.setStatus("current")
_HwTACACSPriAccClientRoundTripTime_Type = Integer32
_HwTACACSPriAccClientRoundTripTime_Object = MibTableColumn
hwTACACSPriAccClientRoundTripTime = _HwTACACSPriAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 58),
    _HwTACACSPriAccClientRoundTripTime_Type()
)
hwTACACSPriAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientRoundTripTime.setStatus("current")
_HwTACACSPriAccClientReqPacket_Type = Counter32
_HwTACACSPriAccClientReqPacket_Object = MibTableColumn
hwTACACSPriAccClientReqPacket = _HwTACACSPriAccClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 59),
    _HwTACACSPriAccClientReqPacket_Type()
)
hwTACACSPriAccClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqPacket.setStatus("current")
_HwTACACSPriAccClientReqNetwork_Type = Counter32
_HwTACACSPriAccClientReqNetwork_Object = MibTableColumn
hwTACACSPriAccClientReqNetwork = _HwTACACSPriAccClientReqNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 60),
    _HwTACACSPriAccClientReqNetwork_Type()
)
hwTACACSPriAccClientReqNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqNetwork.setStatus("current")
_HwTACACSPriAccClientReqConnection_Type = Counter32
_HwTACACSPriAccClientReqConnection_Object = MibTableColumn
hwTACACSPriAccClientReqConnection = _HwTACACSPriAccClientReqConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 61),
    _HwTACACSPriAccClientReqConnection_Type()
)
hwTACACSPriAccClientReqConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqConnection.setStatus("current")
_HwTACACSPriAccClientReqEXEC_Type = Counter32
_HwTACACSPriAccClientReqEXEC_Object = MibTableColumn
hwTACACSPriAccClientReqEXEC = _HwTACACSPriAccClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 62),
    _HwTACACSPriAccClientReqEXEC_Type()
)
hwTACACSPriAccClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqEXEC.setStatus("current")
_HwTACACSPriAccClientReqSysEvent_Type = Counter32
_HwTACACSPriAccClientReqSysEvent_Object = MibTableColumn
hwTACACSPriAccClientReqSysEvent = _HwTACACSPriAccClientReqSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 63),
    _HwTACACSPriAccClientReqSysEvent_Type()
)
hwTACACSPriAccClientReqSysEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqSysEvent.setStatus("current")
_HwTACACSPriAccClientReqCommandLevel_Type = Counter32
_HwTACACSPriAccClientReqCommandLevel_Object = MibTableColumn
hwTACACSPriAccClientReqCommandLevel = _HwTACACSPriAccClientReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 64),
    _HwTACACSPriAccClientReqCommandLevel_Type()
)
hwTACACSPriAccClientReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqCommandLevel.setStatus("current")
_HwTACACSPriAccClientReqUpdate_Type = Counter32
_HwTACACSPriAccClientReqUpdate_Object = MibTableColumn
hwTACACSPriAccClientReqUpdate = _HwTACACSPriAccClientReqUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 65),
    _HwTACACSPriAccClientReqUpdate_Type()
)
hwTACACSPriAccClientReqUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqUpdate.setStatus("current")
_HwTACACSPriAccClientResPacket_Type = Counter32
_HwTACACSPriAccClientResPacket_Object = MibTableColumn
hwTACACSPriAccClientResPacket = _HwTACACSPriAccClientResPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 66),
    _HwTACACSPriAccClientResPacket_Type()
)
hwTACACSPriAccClientResPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientResPacket.setStatus("current")
_HwTACACSPriAccClientResError_Type = Counter32
_HwTACACSPriAccClientResError_Object = MibTableColumn
hwTACACSPriAccClientResError = _HwTACACSPriAccClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 67),
    _HwTACACSPriAccClientResError_Type()
)
hwTACACSPriAccClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientResError.setStatus("current")
_HwTACACSPriAccClientReqPending_Type = Counter32
_HwTACACSPriAccClientReqPending_Object = MibTableColumn
hwTACACSPriAccClientReqPending = _HwTACACSPriAccClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 68),
    _HwTACACSPriAccClientReqPending_Type()
)
hwTACACSPriAccClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientReqPending.setStatus("current")
_HwTACACSPriAccClientTimeouts_Type = Counter32
_HwTACACSPriAccClientTimeouts_Object = MibTableColumn
hwTACACSPriAccClientTimeouts = _HwTACACSPriAccClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 69),
    _HwTACACSPriAccClientTimeouts_Type()
)
hwTACACSPriAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientTimeouts.setStatus("current")
_HwTACACSPriAccClientUnknownTypes_Type = Counter32
_HwTACACSPriAccClientUnknownTypes_Object = MibTableColumn
hwTACACSPriAccClientUnknownTypes = _HwTACACSPriAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 70),
    _HwTACACSPriAccClientUnknownTypes_Type()
)
hwTACACSPriAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientUnknownTypes.setStatus("current")
_HwTACACSPriAccClientPacketsDropped_Type = Counter32
_HwTACACSPriAccClientPacketsDropped_Object = MibTableColumn
hwTACACSPriAccClientPacketsDropped = _HwTACACSPriAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 71),
    _HwTACACSPriAccClientPacketsDropped_Type()
)
hwTACACSPriAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSPriAccClientPacketsDropped.setStatus("current")
_HwTACACSSecAuthenClientRoundTripTime_Type = Integer32
_HwTACACSSecAuthenClientRoundTripTime_Object = MibTableColumn
hwTACACSSecAuthenClientRoundTripTime = _HwTACACSSecAuthenClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 72),
    _HwTACACSSecAuthenClientRoundTripTime_Type()
)
hwTACACSSecAuthenClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientRoundTripTime.setStatus("current")
_HwTACACSSecAuthenClientAccessReqPacket_Type = Counter32
_HwTACACSSecAuthenClientAccessReqPacket_Object = MibTableColumn
hwTACACSSecAuthenClientAccessReqPacket = _HwTACACSSecAuthenClientAccessReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 73),
    _HwTACACSSecAuthenClientAccessReqPacket_Type()
)
hwTACACSSecAuthenClientAccessReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessReqPacket.setStatus("current")
_HwTACACSSecAuthenClientAccessReqLogin_Type = Counter32
_HwTACACSSecAuthenClientAccessReqLogin_Object = MibTableColumn
hwTACACSSecAuthenClientAccessReqLogin = _HwTACACSSecAuthenClientAccessReqLogin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 74),
    _HwTACACSSecAuthenClientAccessReqLogin_Type()
)
hwTACACSSecAuthenClientAccessReqLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessReqLogin.setStatus("current")
_HwTACACSSecAuthenClientAccessReqChaPass_Type = Counter32
_HwTACACSSecAuthenClientAccessReqChaPass_Object = MibTableColumn
hwTACACSSecAuthenClientAccessReqChaPass = _HwTACACSSecAuthenClientAccessReqChaPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 75),
    _HwTACACSSecAuthenClientAccessReqChaPass_Type()
)
hwTACACSSecAuthenClientAccessReqChaPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessReqChaPass.setStatus("current")
_HwTACACSSecAuthenClientAccessReqSendPass_Type = Counter32
_HwTACACSSecAuthenClientAccessReqSendPass_Object = MibTableColumn
hwTACACSSecAuthenClientAccessReqSendPass = _HwTACACSSecAuthenClientAccessReqSendPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 76),
    _HwTACACSSecAuthenClientAccessReqSendPass_Type()
)
hwTACACSSecAuthenClientAccessReqSendPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessReqSendPass.setStatus("current")
_HwTACACSSecAuthenClientAccessReqSendAuth_Type = Counter32
_HwTACACSSecAuthenClientAccessReqSendAuth_Object = MibTableColumn
hwTACACSSecAuthenClientAccessReqSendAuth = _HwTACACSSecAuthenClientAccessReqSendAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 77),
    _HwTACACSSecAuthenClientAccessReqSendAuth_Type()
)
hwTACACSSecAuthenClientAccessReqSendAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessReqSendAuth.setStatus("current")
_HwTACACSSecAuthenClientAccessResPack_Type = Counter32
_HwTACACSSecAuthenClientAccessResPack_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResPack = _HwTACACSSecAuthenClientAccessResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 78),
    _HwTACACSSecAuthenClientAccessResPack_Type()
)
hwTACACSSecAuthenClientAccessResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResPack.setStatus("current")
_HwTACACSSecAuthenClientAccessResPass_Type = Counter32
_HwTACACSSecAuthenClientAccessResPass_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResPass = _HwTACACSSecAuthenClientAccessResPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 79),
    _HwTACACSSecAuthenClientAccessResPass_Type()
)
hwTACACSSecAuthenClientAccessResPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResPass.setStatus("current")
_HwTACACSSecAuthenClientAccessResFail_Type = Counter32
_HwTACACSSecAuthenClientAccessResFail_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResFail = _HwTACACSSecAuthenClientAccessResFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 80),
    _HwTACACSSecAuthenClientAccessResFail_Type()
)
hwTACACSSecAuthenClientAccessResFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResFail.setStatus("current")
_HwTACACSSecAuthenClientAccessResGetData_Type = Counter32
_HwTACACSSecAuthenClientAccessResGetData_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResGetData = _HwTACACSSecAuthenClientAccessResGetData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 81),
    _HwTACACSSecAuthenClientAccessResGetData_Type()
)
hwTACACSSecAuthenClientAccessResGetData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResGetData.setStatus("current")
_HwTACACSSecAuthenClientAccessResGetUser_Type = Counter32
_HwTACACSSecAuthenClientAccessResGetUser_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResGetUser = _HwTACACSSecAuthenClientAccessResGetUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 82),
    _HwTACACSSecAuthenClientAccessResGetUser_Type()
)
hwTACACSSecAuthenClientAccessResGetUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResGetUser.setStatus("current")
_HwTACACSSecAuthenClientAccessResGetPass_Type = Counter32
_HwTACACSSecAuthenClientAccessResGetPass_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResGetPass = _HwTACACSSecAuthenClientAccessResGetPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 83),
    _HwTACACSSecAuthenClientAccessResGetPass_Type()
)
hwTACACSSecAuthenClientAccessResGetPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResGetPass.setStatus("current")
_HwTACACSSecAuthenClientAccessResRestart_Type = Counter32
_HwTACACSSecAuthenClientAccessResRestart_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResRestart = _HwTACACSSecAuthenClientAccessResRestart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 84),
    _HwTACACSSecAuthenClientAccessResRestart_Type()
)
hwTACACSSecAuthenClientAccessResRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResRestart.setStatus("current")
_HwTACACSSecAuthenClientAccessResError_Type = Counter32
_HwTACACSSecAuthenClientAccessResError_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResError = _HwTACACSSecAuthenClientAccessResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 85),
    _HwTACACSSecAuthenClientAccessResError_Type()
)
hwTACACSSecAuthenClientAccessResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResError.setStatus("current")
_HwTACACSSecAuthenClientAccessResFollow_Type = Counter32
_HwTACACSSecAuthenClientAccessResFollow_Object = MibTableColumn
hwTACACSSecAuthenClientAccessResFollow = _HwTACACSSecAuthenClientAccessResFollow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 86),
    _HwTACACSSecAuthenClientAccessResFollow_Type()
)
hwTACACSSecAuthenClientAccessResFollow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessResFollow.setStatus("current")
_HwTACACSSecAuthenClientMalformedAccessResponses_Type = Counter32
_HwTACACSSecAuthenClientMalformedAccessResponses_Object = MibTableColumn
hwTACACSSecAuthenClientMalformedAccessResponses = _HwTACACSSecAuthenClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 87),
    _HwTACACSSecAuthenClientMalformedAccessResponses_Type()
)
hwTACACSSecAuthenClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientMalformedAccessResponses.setStatus("current")
_HwTACACSSecAuthenClientAccessConPack_Type = Counter32
_HwTACACSSecAuthenClientAccessConPack_Object = MibTableColumn
hwTACACSSecAuthenClientAccessConPack = _HwTACACSSecAuthenClientAccessConPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 88),
    _HwTACACSSecAuthenClientAccessConPack_Type()
)
hwTACACSSecAuthenClientAccessConPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessConPack.setStatus("current")
_HwTACACSSecAuthenClientAccessConAbort_Type = Counter32
_HwTACACSSecAuthenClientAccessConAbort_Object = MibTableColumn
hwTACACSSecAuthenClientAccessConAbort = _HwTACACSSecAuthenClientAccessConAbort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 89),
    _HwTACACSSecAuthenClientAccessConAbort_Type()
)
hwTACACSSecAuthenClientAccessConAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientAccessConAbort.setStatus("current")
_HwTACACSSecAuthenClientPendingRequests_Type = Counter32
_HwTACACSSecAuthenClientPendingRequests_Object = MibTableColumn
hwTACACSSecAuthenClientPendingRequests = _HwTACACSSecAuthenClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 90),
    _HwTACACSSecAuthenClientPendingRequests_Type()
)
hwTACACSSecAuthenClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientPendingRequests.setStatus("current")
_HwTACACSSecAuthenClientTimeouts_Type = Counter32
_HwTACACSSecAuthenClientTimeouts_Object = MibTableColumn
hwTACACSSecAuthenClientTimeouts = _HwTACACSSecAuthenClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 91),
    _HwTACACSSecAuthenClientTimeouts_Type()
)
hwTACACSSecAuthenClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientTimeouts.setStatus("current")
_HwTACACSSecAuthenClientUnknownTypes_Type = Counter32
_HwTACACSSecAuthenClientUnknownTypes_Object = MibTableColumn
hwTACACSSecAuthenClientUnknownTypes = _HwTACACSSecAuthenClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 92),
    _HwTACACSSecAuthenClientUnknownTypes_Type()
)
hwTACACSSecAuthenClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientUnknownTypes.setStatus("current")
_HwTACACSSecAuthenClientPacketsDropped_Type = Counter32
_HwTACACSSecAuthenClientPacketsDropped_Object = MibTableColumn
hwTACACSSecAuthenClientPacketsDropped = _HwTACACSSecAuthenClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 93),
    _HwTACACSSecAuthenClientPacketsDropped_Type()
)
hwTACACSSecAuthenClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthenClientPacketsDropped.setStatus("current")
_HwTACACSSecAuthorClientRoundTripTime_Type = Integer32
_HwTACACSSecAuthorClientRoundTripTime_Object = MibTableColumn
hwTACACSSecAuthorClientRoundTripTime = _HwTACACSSecAuthorClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 94),
    _HwTACACSSecAuthorClientRoundTripTime_Type()
)
hwTACACSSecAuthorClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientRoundTripTime.setStatus("current")
_HwTACACSSecAuthorClientReqPacket_Type = Counter32
_HwTACACSSecAuthorClientReqPacket_Object = MibTableColumn
hwTACACSSecAuthorClientReqPacket = _HwTACACSSecAuthorClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 95),
    _HwTACACSSecAuthorClientReqPacket_Type()
)
hwTACACSSecAuthorClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientReqPacket.setStatus("current")
_HwTACACSSecAuthorClientReqEXEC_Type = Counter32
_HwTACACSSecAuthorClientReqEXEC_Object = MibTableColumn
hwTACACSSecAuthorClientReqEXEC = _HwTACACSSecAuthorClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 96),
    _HwTACACSSecAuthorClientReqEXEC_Type()
)
hwTACACSSecAuthorClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientReqEXEC.setStatus("current")
_HwTACACSSecAuthorClientReqVPDN_Type = Counter32
_HwTACACSSecAuthorClientReqVPDN_Object = MibTableColumn
hwTACACSSecAuthorClientReqVPDN = _HwTACACSSecAuthorClientReqVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 97),
    _HwTACACSSecAuthorClientReqVPDN_Type()
)
hwTACACSSecAuthorClientReqVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientReqVPDN.setStatus("current")
_HwTACACSSecAuthorClientResPack_Type = Counter32
_HwTACACSSecAuthorClientResPack_Object = MibTableColumn
hwTACACSSecAuthorClientResPack = _HwTACACSSecAuthorClientResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 98),
    _HwTACACSSecAuthorClientResPack_Type()
)
hwTACACSSecAuthorClientResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientResPack.setStatus("current")
_HwTACACSSecAuthorClientResEXEC_Type = Counter32
_HwTACACSSecAuthorClientResEXEC_Object = MibTableColumn
hwTACACSSecAuthorClientResEXEC = _HwTACACSSecAuthorClientResEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 99),
    _HwTACACSSecAuthorClientResEXEC_Type()
)
hwTACACSSecAuthorClientResEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientResEXEC.setStatus("current")
_HwTACACSSecAuthorClientResVPDN_Type = Counter32
_HwTACACSSecAuthorClientResVPDN_Object = MibTableColumn
hwTACACSSecAuthorClientResVPDN = _HwTACACSSecAuthorClientResVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 100),
    _HwTACACSSecAuthorClientResVPDN_Type()
)
hwTACACSSecAuthorClientResVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientResVPDN.setStatus("current")
_HwTACACSSecAuthorClientResError_Type = Counter32
_HwTACACSSecAuthorClientResError_Object = MibTableColumn
hwTACACSSecAuthorClientResError = _HwTACACSSecAuthorClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 101),
    _HwTACACSSecAuthorClientResError_Type()
)
hwTACACSSecAuthorClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientResError.setStatus("current")
_HwTACACSSecAuthorClientReqPending_Type = Counter32
_HwTACACSSecAuthorClientReqPending_Object = MibTableColumn
hwTACACSSecAuthorClientReqPending = _HwTACACSSecAuthorClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 102),
    _HwTACACSSecAuthorClientReqPending_Type()
)
hwTACACSSecAuthorClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientReqPending.setStatus("current")
_HwTACACSSecAuthorClientTimeouts_Type = Counter32
_HwTACACSSecAuthorClientTimeouts_Object = MibTableColumn
hwTACACSSecAuthorClientTimeouts = _HwTACACSSecAuthorClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 103),
    _HwTACACSSecAuthorClientTimeouts_Type()
)
hwTACACSSecAuthorClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientTimeouts.setStatus("current")
_HwTACACSSecAuthorClientUnknownTypes_Type = Counter32
_HwTACACSSecAuthorClientUnknownTypes_Object = MibTableColumn
hwTACACSSecAuthorClientUnknownTypes = _HwTACACSSecAuthorClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 104),
    _HwTACACSSecAuthorClientUnknownTypes_Type()
)
hwTACACSSecAuthorClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientUnknownTypes.setStatus("current")
_HwTACACSSecAuthorClientPacketsDropped_Type = Counter32
_HwTACACSSecAuthorClientPacketsDropped_Object = MibTableColumn
hwTACACSSecAuthorClientPacketsDropped = _HwTACACSSecAuthorClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 105),
    _HwTACACSSecAuthorClientPacketsDropped_Type()
)
hwTACACSSecAuthorClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAuthorClientPacketsDropped.setStatus("current")
_HwTACACSSecAccClientRoundTripTime_Type = Integer32
_HwTACACSSecAccClientRoundTripTime_Object = MibTableColumn
hwTACACSSecAccClientRoundTripTime = _HwTACACSSecAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 106),
    _HwTACACSSecAccClientRoundTripTime_Type()
)
hwTACACSSecAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientRoundTripTime.setStatus("current")
_HwTACACSSecAccClientReqPacket_Type = Counter32
_HwTACACSSecAccClientReqPacket_Object = MibTableColumn
hwTACACSSecAccClientReqPacket = _HwTACACSSecAccClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 107),
    _HwTACACSSecAccClientReqPacket_Type()
)
hwTACACSSecAccClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqPacket.setStatus("current")
_HwTACACSSecAccClientReqNetwork_Type = Counter32
_HwTACACSSecAccClientReqNetwork_Object = MibTableColumn
hwTACACSSecAccClientReqNetwork = _HwTACACSSecAccClientReqNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 108),
    _HwTACACSSecAccClientReqNetwork_Type()
)
hwTACACSSecAccClientReqNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqNetwork.setStatus("current")
_HwTACACSSecAccClientReqConnection_Type = Counter32
_HwTACACSSecAccClientReqConnection_Object = MibTableColumn
hwTACACSSecAccClientReqConnection = _HwTACACSSecAccClientReqConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 109),
    _HwTACACSSecAccClientReqConnection_Type()
)
hwTACACSSecAccClientReqConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqConnection.setStatus("current")
_HwTACACSSecAccClientReqEXEC_Type = Counter32
_HwTACACSSecAccClientReqEXEC_Object = MibTableColumn
hwTACACSSecAccClientReqEXEC = _HwTACACSSecAccClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 110),
    _HwTACACSSecAccClientReqEXEC_Type()
)
hwTACACSSecAccClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqEXEC.setStatus("current")
_HwTACACSSecAccClientReqSysEvent_Type = Counter32
_HwTACACSSecAccClientReqSysEvent_Object = MibTableColumn
hwTACACSSecAccClientReqSysEvent = _HwTACACSSecAccClientReqSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 111),
    _HwTACACSSecAccClientReqSysEvent_Type()
)
hwTACACSSecAccClientReqSysEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqSysEvent.setStatus("current")
_HwTACACSSecAccClientReqCommandLevel_Type = Counter32
_HwTACACSSecAccClientReqCommandLevel_Object = MibTableColumn
hwTACACSSecAccClientReqCommandLevel = _HwTACACSSecAccClientReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 112),
    _HwTACACSSecAccClientReqCommandLevel_Type()
)
hwTACACSSecAccClientReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqCommandLevel.setStatus("current")
_HwTACACSSecAccClientReqUpdate_Type = Counter32
_HwTACACSSecAccClientReqUpdate_Object = MibTableColumn
hwTACACSSecAccClientReqUpdate = _HwTACACSSecAccClientReqUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 113),
    _HwTACACSSecAccClientReqUpdate_Type()
)
hwTACACSSecAccClientReqUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqUpdate.setStatus("current")
_HwTACACSSecAccClientResPacket_Type = Counter32
_HwTACACSSecAccClientResPacket_Object = MibTableColumn
hwTACACSSecAccClientResPacket = _HwTACACSSecAccClientResPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 114),
    _HwTACACSSecAccClientResPacket_Type()
)
hwTACACSSecAccClientResPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientResPacket.setStatus("current")
_HwTACACSSecAccClientResError_Type = Counter32
_HwTACACSSecAccClientResError_Object = MibTableColumn
hwTACACSSecAccClientResError = _HwTACACSSecAccClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 115),
    _HwTACACSSecAccClientResError_Type()
)
hwTACACSSecAccClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientResError.setStatus("current")
_HwTACACSSecAccClientReqPending_Type = Counter32
_HwTACACSSecAccClientReqPending_Object = MibTableColumn
hwTACACSSecAccClientReqPending = _HwTACACSSecAccClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 116),
    _HwTACACSSecAccClientReqPending_Type()
)
hwTACACSSecAccClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientReqPending.setStatus("current")
_HwTACACSSecAccClientTimeouts_Type = Counter32
_HwTACACSSecAccClientTimeouts_Object = MibTableColumn
hwTACACSSecAccClientTimeouts = _HwTACACSSecAccClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 117),
    _HwTACACSSecAccClientTimeouts_Type()
)
hwTACACSSecAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientTimeouts.setStatus("current")
_HwTACACSSecAccClientUnknownTypes_Type = Counter32
_HwTACACSSecAccClientUnknownTypes_Object = MibTableColumn
hwTACACSSecAccClientUnknownTypes = _HwTACACSSecAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 118),
    _HwTACACSSecAccClientUnknownTypes_Type()
)
hwTACACSSecAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientUnknownTypes.setStatus("current")
_HwTACACSSecAccClientPacketsDropped_Type = Counter32
_HwTACACSSecAccClientPacketsDropped_Object = MibTableColumn
hwTACACSSecAccClientPacketsDropped = _HwTACACSSecAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 119),
    _HwTACACSSecAccClientPacketsDropped_Type()
)
hwTACACSSecAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSSecAccClientPacketsDropped.setStatus("current")
_HwTACACSServerGroupRowStatus_Type = RowStatus
_HwTACACSServerGroupRowStatus_Object = MibTableColumn
hwTACACSServerGroupRowStatus = _HwTACACSServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 120),
    _HwTACACSServerGroupRowStatus_Type()
)
hwTACACSServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupRowStatus.setStatus("current")
_HwTacacsConformance_ObjectIdentity = ObjectIdentity
hwTacacsConformance = _HwTacacsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2)
)
_HwTacacsCompliances_ObjectIdentity = ObjectIdentity
hwTacacsCompliances = _HwTacacsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2, 1)
)
_HwTacacsObjectGroups_ObjectIdentity = ObjectIdentity
hwTacacsObjectGroups = _HwTacacsObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2, 2)
)
_HwtacacsClientMng_ObjectIdentity = ObjectIdentity
hwtacacsClientMng = _HwtacacsClientMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3)
)
_HwtacacsClient_ObjectIdentity = ObjectIdentity
hwtacacsClient = _HwtacacsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1)
)
_HwtacacsClientAuthenRequestPackets_Type = Counter32
_HwtacacsClientAuthenRequestPackets_Object = MibScalar
hwtacacsClientAuthenRequestPackets = _HwtacacsClientAuthenRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 1),
    _HwtacacsClientAuthenRequestPackets_Type()
)
hwtacacsClientAuthenRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenRequestPackets.setStatus("current")
_HwtacacsClientAuthenAcceptPackets_Type = Counter32
_HwtacacsClientAuthenAcceptPackets_Object = MibScalar
hwtacacsClientAuthenAcceptPackets = _HwtacacsClientAuthenAcceptPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 2),
    _HwtacacsClientAuthenAcceptPackets_Type()
)
hwtacacsClientAuthenAcceptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenAcceptPackets.setStatus("current")
_HwtacacsClientAuthenRejectPackets_Type = Counter32
_HwtacacsClientAuthenRejectPackets_Object = MibScalar
hwtacacsClientAuthenRejectPackets = _HwtacacsClientAuthenRejectPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 3),
    _HwtacacsClientAuthenRejectPackets_Type()
)
hwtacacsClientAuthenRejectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenRejectPackets.setStatus("current")
_HwtacacsClientAuthenPendRequests_Type = Gauge32
_HwtacacsClientAuthenPendRequests_Object = MibScalar
hwtacacsClientAuthenPendRequests = _HwtacacsClientAuthenPendRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 4),
    _HwtacacsClientAuthenPendRequests_Type()
)
hwtacacsClientAuthenPendRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenPendRequests.setStatus("current")
_HwtacacsClientAuthorReqPackets_Type = Counter32
_HwtacacsClientAuthorReqPackets_Object = MibScalar
hwtacacsClientAuthorReqPackets = _HwtacacsClientAuthorReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 5),
    _HwtacacsClientAuthorReqPackets_Type()
)
hwtacacsClientAuthorReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorReqPackets.setStatus("current")
_HwtacacsClientAuthorAcceptPackets_Type = Counter32
_HwtacacsClientAuthorAcceptPackets_Object = MibScalar
hwtacacsClientAuthorAcceptPackets = _HwtacacsClientAuthorAcceptPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 6),
    _HwtacacsClientAuthorAcceptPackets_Type()
)
hwtacacsClientAuthorAcceptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorAcceptPackets.setStatus("current")
_HwtacacsClientAuthorRejectPackets_Type = Counter32
_HwtacacsClientAuthorRejectPackets_Object = MibScalar
hwtacacsClientAuthorRejectPackets = _HwtacacsClientAuthorRejectPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 7),
    _HwtacacsClientAuthorRejectPackets_Type()
)
hwtacacsClientAuthorRejectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorRejectPackets.setStatus("current")
_HwtacacsClientAuthorPendRequests_Type = Gauge32
_HwtacacsClientAuthorPendRequests_Object = MibScalar
hwtacacsClientAuthorPendRequests = _HwtacacsClientAuthorPendRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 8),
    _HwtacacsClientAuthorPendRequests_Type()
)
hwtacacsClientAuthorPendRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorPendRequests.setStatus("current")
_HwtacacsClientDroppedPackets_Type = Counter32
_HwtacacsClientDroppedPackets_Object = MibScalar
hwtacacsClientDroppedPackets = _HwtacacsClientDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 9),
    _HwtacacsClientDroppedPackets_Type()
)
hwtacacsClientDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientDroppedPackets.setStatus("current")
_HwtacacsClientAcctRequestPackets_Type = Counter32
_HwtacacsClientAcctRequestPackets_Object = MibScalar
hwtacacsClientAcctRequestPackets = _HwtacacsClientAcctRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 10),
    _HwtacacsClientAcctRequestPackets_Type()
)
hwtacacsClientAcctRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAcctRequestPackets.setStatus("current")
_HwtacacsClientAcctResponsePackets_Type = Counter32
_HwtacacsClientAcctResponsePackets_Object = MibScalar
hwtacacsClientAcctResponsePackets = _HwtacacsClientAcctResponsePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 11),
    _HwtacacsClientAcctResponsePackets_Type()
)
hwtacacsClientAcctResponsePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAcctResponsePackets.setStatus("current")
_HwtacacsClientAcctErrorPackets_Type = Counter32
_HwtacacsClientAcctErrorPackets_Object = MibScalar
hwtacacsClientAcctErrorPackets = _HwtacacsClientAcctErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 12),
    _HwtacacsClientAcctErrorPackets_Type()
)
hwtacacsClientAcctErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAcctErrorPackets.setStatus("current")
_HwtacacsClientAcctPendingPackets_Type = Counter32
_HwtacacsClientAcctPendingPackets_Object = MibScalar
hwtacacsClientAcctPendingPackets = _HwtacacsClientAcctPendingPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 13),
    _HwtacacsClientAcctPendingPackets_Type()
)
hwtacacsClientAcctPendingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAcctPendingPackets.setStatus("current")
_HwtacacsTemplateTable_Object = MibTable
hwtacacsTemplateTable = _HwtacacsTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14)
)
if mibBuilder.loadTexts:
    hwtacacsTemplateTable.setStatus("current")
_HwtacacsTemplateEntry_Object = MibTableRow
hwtacacsTemplateEntry = _HwtacacsTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1)
)
hwtacacsTemplateEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientTemplateIndex"),
)
if mibBuilder.loadTexts:
    hwtacacsTemplateEntry.setStatus("current")


class _HwtacacsClientTemplateIndex_Type(Unsigned32):
    """Custom type hwtacacsClientTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwtacacsClientTemplateIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientTemplateIndex_Object = MibTableColumn
hwtacacsClientTemplateIndex = _HwtacacsClientTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 1),
    _HwtacacsClientTemplateIndex_Type()
)
hwtacacsClientTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientTemplateIndex.setStatus("current")


class _HwtacacsClientTemplateName_Type(OctetString):
    """Custom type hwtacacsClientTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwtacacsClientTemplateName_Type.__name__ = "OctetString"
_HwtacacsClientTemplateName_Object = MibTableColumn
hwtacacsClientTemplateName = _HwtacacsClientTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 2),
    _HwtacacsClientTemplateName_Type()
)
hwtacacsClientTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientTemplateName.setStatus("current")


class _HwtacacsClientSharedKey_Type(OctetString):
    """Custom type hwtacacsClientSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwtacacsClientSharedKey_Type.__name__ = "OctetString"
_HwtacacsClientSharedKey_Object = MibTableColumn
hwtacacsClientSharedKey = _HwtacacsClientSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 3),
    _HwtacacsClientSharedKey_Type()
)
hwtacacsClientSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientSharedKey.setStatus("current")
_HwtacacsClientSourceIP_Type = IpAddress
_HwtacacsClientSourceIP_Object = MibTableColumn
hwtacacsClientSourceIP = _HwtacacsClientSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 4),
    _HwtacacsClientSourceIP_Type()
)
hwtacacsClientSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientSourceIP.setStatus("current")


class _HwtacacsClientQuietTimer_Type(Unsigned32):
    """Custom type hwtacacsClientQuietTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwtacacsClientQuietTimer_Type.__name__ = "Unsigned32"
_HwtacacsClientQuietTimer_Object = MibTableColumn
hwtacacsClientQuietTimer = _HwtacacsClientQuietTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 5),
    _HwtacacsClientQuietTimer_Type()
)
hwtacacsClientQuietTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientQuietTimer.setStatus("current")


class _HwtacacsClientResponseTimeout_Type(Unsigned32):
    """Custom type hwtacacsClientResponseTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwtacacsClientResponseTimeout_Type.__name__ = "Unsigned32"
_HwtacacsClientResponseTimeout_Object = MibTableColumn
hwtacacsClientResponseTimeout = _HwtacacsClientResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 6),
    _HwtacacsClientResponseTimeout_Type()
)
hwtacacsClientResponseTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientResponseTimeout.setStatus("current")


class _HwtacacsClientDomainNameIncluded_Type(Integer32):
    """Custom type hwtacacsClientDomainNameIncluded based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientDomainNameIncluded_Type.__name__ = "Integer32"
_HwtacacsClientDomainNameIncluded_Object = MibTableColumn
hwtacacsClientDomainNameIncluded = _HwtacacsClientDomainNameIncluded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 7),
    _HwtacacsClientDomainNameIncluded_Type()
)
hwtacacsClientDomainNameIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientDomainNameIncluded.setStatus("current")
_HwtacacsClientRowStatus_Type = RowStatus
_HwtacacsClientRowStatus_Object = MibTableColumn
hwtacacsClientRowStatus = _HwtacacsClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 14, 1, 8),
    _HwtacacsClientRowStatus_Type()
)
hwtacacsClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientRowStatus.setStatus("current")
_HwtacacsClientAuthenServerTable_Object = MibTable
hwtacacsClientAuthenServerTable = _HwtacacsClientAuthenServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15)
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerTable.setStatus("current")
_HwtacacsClientAuthenServerEntry_Object = MibTableRow
hwtacacsClientAuthenServerEntry = _HwtacacsClientAuthenServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1)
)
hwtacacsClientAuthenServerEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenTemplateIndex"),
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerIndex"),
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerEntry.setStatus("current")


class _HwtacacsClientAuthenTemplateIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAuthenTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwtacacsClientAuthenTemplateIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAuthenTemplateIndex_Object = MibTableColumn
hwtacacsClientAuthenTemplateIndex = _HwtacacsClientAuthenTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 1),
    _HwtacacsClientAuthenTemplateIndex_Type()
)
hwtacacsClientAuthenTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenTemplateIndex.setStatus("current")


class _HwtacacsClientAuthenServerIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAuthenServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwtacacsClientAuthenServerIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAuthenServerIndex_Object = MibTableColumn
hwtacacsClientAuthenServerIndex = _HwtacacsClientAuthenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 2),
    _HwtacacsClientAuthenServerIndex_Type()
)
hwtacacsClientAuthenServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerIndex.setStatus("current")
_HwtacacsClientAuthenServerAddress_Type = IpAddress
_HwtacacsClientAuthenServerAddress_Object = MibTableColumn
hwtacacsClientAuthenServerAddress = _HwtacacsClientAuthenServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 3),
    _HwtacacsClientAuthenServerAddress_Type()
)
hwtacacsClientAuthenServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerAddress.setStatus("current")


class _HwtacacsClientAuthenServerPort_Type(Integer32):
    """Custom type hwtacacsClientAuthenServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwtacacsClientAuthenServerPort_Type.__name__ = "Integer32"
_HwtacacsClientAuthenServerPort_Object = MibTableColumn
hwtacacsClientAuthenServerPort = _HwtacacsClientAuthenServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 4),
    _HwtacacsClientAuthenServerPort_Type()
)
hwtacacsClientAuthenServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerPort.setStatus("current")


class _HwtacacsClientAuthenServerType_Type(Integer32):
    """Custom type hwtacacsClientAuthenServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthenServerType_Type.__name__ = "Integer32"
_HwtacacsClientAuthenServerType_Object = MibTableColumn
hwtacacsClientAuthenServerType = _HwtacacsClientAuthenServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 5),
    _HwtacacsClientAuthenServerType_Type()
)
hwtacacsClientAuthenServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerType.setStatus("current")


class _HwtacacsClientAuthenServerState_Type(Integer32):
    """Custom type hwtacacsClientAuthenServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthenServerState_Type.__name__ = "Integer32"
_HwtacacsClientAuthenServerState_Object = MibTableColumn
hwtacacsClientAuthenServerState = _HwtacacsClientAuthenServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 6),
    _HwtacacsClientAuthenServerState_Type()
)
hwtacacsClientAuthenServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerState.setStatus("current")


class _HwtacacsClientAuthenServerMode_Type(Integer32):
    """Custom type hwtacacsClientAuthenServerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthenServerMode_Type.__name__ = "Integer32"
_HwtacacsClientAuthenServerMode_Object = MibTableColumn
hwtacacsClientAuthenServerMode = _HwtacacsClientAuthenServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 7),
    _HwtacacsClientAuthenServerMode_Type()
)
hwtacacsClientAuthenServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerMode.setStatus("current")
_HwtacacsClientAuthenRoundTripTime_Type = TimeTicks
_HwtacacsClientAuthenRoundTripTime_Object = MibTableColumn
hwtacacsClientAuthenRoundTripTime = _HwtacacsClientAuthenRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 8),
    _HwtacacsClientAuthenRoundTripTime_Type()
)
hwtacacsClientAuthenRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenRoundTripTime.setStatus("current")
_HwtacacsClientAuthenAccessReqPackets_Type = Counter32
_HwtacacsClientAuthenAccessReqPackets_Object = MibTableColumn
hwtacacsClientAuthenAccessReqPackets = _HwtacacsClientAuthenAccessReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 9),
    _HwtacacsClientAuthenAccessReqPackets_Type()
)
hwtacacsClientAuthenAccessReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenAccessReqPackets.setStatus("current")
_HwtacacsClientAuthenAccessChngPassRequests_Type = Counter32
_HwtacacsClientAuthenAccessChngPassRequests_Object = MibTableColumn
hwtacacsClientAuthenAccessChngPassRequests = _HwtacacsClientAuthenAccessChngPassRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 10),
    _HwtacacsClientAuthenAccessChngPassRequests_Type()
)
hwtacacsClientAuthenAccessChngPassRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenAccessChngPassRequests.setStatus("current")
_HwtacacsClientAuthenAccessSendPassPackets_Type = Counter32
_HwtacacsClientAuthenAccessSendPassPackets_Object = MibTableColumn
hwtacacsClientAuthenAccessSendPassPackets = _HwtacacsClientAuthenAccessSendPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 11),
    _HwtacacsClientAuthenAccessSendPassPackets_Type()
)
hwtacacsClientAuthenAccessSendPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenAccessSendPassPackets.setStatus("current")
_HwtacacsClientAuthenAccessSendAuthenPackets_Type = Counter32
_HwtacacsClientAuthenAccessSendAuthenPackets_Object = MibTableColumn
hwtacacsClientAuthenAccessSendAuthenPackets = _HwtacacsClientAuthenAccessSendAuthenPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 12),
    _HwtacacsClientAuthenAccessSendAuthenPackets_Type()
)
hwtacacsClientAuthenAccessSendAuthenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenAccessSendAuthenPackets.setStatus("current")
_HwtacacsClientAuthenStartPackets_Type = Counter32
_HwtacacsClientAuthenStartPackets_Object = MibTableColumn
hwtacacsClientAuthenStartPackets = _HwtacacsClientAuthenStartPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 13),
    _HwtacacsClientAuthenStartPackets_Type()
)
hwtacacsClientAuthenStartPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenStartPackets.setStatus("current")
_HwtacacsClientAuthenContinuePackets_Type = Counter32
_HwtacacsClientAuthenContinuePackets_Object = MibTableColumn
hwtacacsClientAuthenContinuePackets = _HwtacacsClientAuthenContinuePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 14),
    _HwtacacsClientAuthenContinuePackets_Type()
)
hwtacacsClientAuthenContinuePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenContinuePackets.setStatus("current")
_HwtacacsClientAuthenContinueAbortPackets_Type = Counter32
_HwtacacsClientAuthenContinueAbortPackets_Object = MibTableColumn
hwtacacsClientAuthenContinueAbortPackets = _HwtacacsClientAuthenContinueAbortPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 15),
    _HwtacacsClientAuthenContinueAbortPackets_Type()
)
hwtacacsClientAuthenContinueAbortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenContinueAbortPackets.setStatus("current")
_HwtacacsClientAuthenReplyPackets_Type = Counter32
_HwtacacsClientAuthenReplyPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyPackets = _HwtacacsClientAuthenReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 16),
    _HwtacacsClientAuthenReplyPackets_Type()
)
hwtacacsClientAuthenReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyPackets.setStatus("current")
_HwtacacsClientAuthenReplyPassPackets_Type = Counter32
_HwtacacsClientAuthenReplyPassPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyPassPackets = _HwtacacsClientAuthenReplyPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 17),
    _HwtacacsClientAuthenReplyPassPackets_Type()
)
hwtacacsClientAuthenReplyPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyPassPackets.setStatus("current")
_HwtacacsClientAuthenReplyFailPackets_Type = Counter32
_HwtacacsClientAuthenReplyFailPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyFailPackets = _HwtacacsClientAuthenReplyFailPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 18),
    _HwtacacsClientAuthenReplyFailPackets_Type()
)
hwtacacsClientAuthenReplyFailPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyFailPackets.setStatus("current")
_HwtacacsClientAuthenReplyGetDataPackets_Type = Counter32
_HwtacacsClientAuthenReplyGetDataPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyGetDataPackets = _HwtacacsClientAuthenReplyGetDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 19),
    _HwtacacsClientAuthenReplyGetDataPackets_Type()
)
hwtacacsClientAuthenReplyGetDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyGetDataPackets.setStatus("current")
_HwtacacsClientAuthenReplyGetUserPackets_Type = Counter32
_HwtacacsClientAuthenReplyGetUserPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyGetUserPackets = _HwtacacsClientAuthenReplyGetUserPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 20),
    _HwtacacsClientAuthenReplyGetUserPackets_Type()
)
hwtacacsClientAuthenReplyGetUserPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyGetUserPackets.setStatus("current")
_HwtacacsClientAuthenReplyGetPassPackets_Type = Counter32
_HwtacacsClientAuthenReplyGetPassPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyGetPassPackets = _HwtacacsClientAuthenReplyGetPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 21),
    _HwtacacsClientAuthenReplyGetPassPackets_Type()
)
hwtacacsClientAuthenReplyGetPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyGetPassPackets.setStatus("current")
_HwtacacsClientAuthenReplyErrorPackets_Type = Counter32
_HwtacacsClientAuthenReplyErrorPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyErrorPackets = _HwtacacsClientAuthenReplyErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 22),
    _HwtacacsClientAuthenReplyErrorPackets_Type()
)
hwtacacsClientAuthenReplyErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyErrorPackets.setStatus("current")
_HwtacacsClientAuthenReplyRestartPackets_Type = Counter32
_HwtacacsClientAuthenReplyRestartPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyRestartPackets = _HwtacacsClientAuthenReplyRestartPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 23),
    _HwtacacsClientAuthenReplyRestartPackets_Type()
)
hwtacacsClientAuthenReplyRestartPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyRestartPackets.setStatus("current")
_HwtacacsClientAuthenReplyFollowPackets_Type = Counter32
_HwtacacsClientAuthenReplyFollowPackets_Object = MibTableColumn
hwtacacsClientAuthenReplyFollowPackets = _HwtacacsClientAuthenReplyFollowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 24),
    _HwtacacsClientAuthenReplyFollowPackets_Type()
)
hwtacacsClientAuthenReplyFollowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenReplyFollowPackets.setStatus("current")
_HwtacacsClientAuthenPendingRequests_Type = Gauge32
_HwtacacsClientAuthenPendingRequests_Object = MibTableColumn
hwtacacsClientAuthenPendingRequests = _HwtacacsClientAuthenPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 25),
    _HwtacacsClientAuthenPendingRequests_Type()
)
hwtacacsClientAuthenPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenPendingRequests.setStatus("current")
_HwtacacsClientAuthenTimeouts_Type = Counter32
_HwtacacsClientAuthenTimeouts_Object = MibTableColumn
hwtacacsClientAuthenTimeouts = _HwtacacsClientAuthenTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 26),
    _HwtacacsClientAuthenTimeouts_Type()
)
hwtacacsClientAuthenTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenTimeouts.setStatus("current")
_HwtacacsClientAuthenUnknownTypePackets_Type = Counter32
_HwtacacsClientAuthenUnknownTypePackets_Object = MibTableColumn
hwtacacsClientAuthenUnknownTypePackets = _HwtacacsClientAuthenUnknownTypePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 27),
    _HwtacacsClientAuthenUnknownTypePackets_Type()
)
hwtacacsClientAuthenUnknownTypePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenUnknownTypePackets.setStatus("current")
_HwtacacsClientAuthenDroppedPackets_Type = Counter32
_HwtacacsClientAuthenDroppedPackets_Object = MibTableColumn
hwtacacsClientAuthenDroppedPackets = _HwtacacsClientAuthenDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 28),
    _HwtacacsClientAuthenDroppedPackets_Type()
)
hwtacacsClientAuthenDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenDroppedPackets.setStatus("current")


class _HwtacacsClientAuthenVPNName_Type(OctetString):
    """Custom type hwtacacsClientAuthenVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwtacacsClientAuthenVPNName_Type.__name__ = "OctetString"
_HwtacacsClientAuthenVPNName_Object = MibTableColumn
hwtacacsClientAuthenVPNName = _HwtacacsClientAuthenVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 29),
    _HwtacacsClientAuthenVPNName_Type()
)
hwtacacsClientAuthenVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenVPNName.setStatus("current")
_HwtacacsClientAuthenRowStatus_Type = RowStatus
_HwtacacsClientAuthenRowStatus_Object = MibTableColumn
hwtacacsClientAuthenRowStatus = _HwtacacsClientAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 15, 1, 30),
    _HwtacacsClientAuthenRowStatus_Type()
)
hwtacacsClientAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthenRowStatus.setStatus("current")
_HwtacacsClientAuthorServerTable_Object = MibTable
hwtacacsClientAuthorServerTable = _HwtacacsClientAuthorServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16)
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerTable.setStatus("current")
_HwtacacsClientAuthorServerEntry_Object = MibTableRow
hwtacacsClientAuthorServerEntry = _HwtacacsClientAuthorServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1)
)
hwtacacsClientAuthorServerEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorTemplateIndex"),
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerIndex"),
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerEntry.setStatus("current")


class _HwtacacsClientAuthorTemplateIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAuthorTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwtacacsClientAuthorTemplateIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAuthorTemplateIndex_Object = MibTableColumn
hwtacacsClientAuthorTemplateIndex = _HwtacacsClientAuthorTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 1),
    _HwtacacsClientAuthorTemplateIndex_Type()
)
hwtacacsClientAuthorTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorTemplateIndex.setStatus("current")


class _HwtacacsClientAuthorServerIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAuthorServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_HwtacacsClientAuthorServerIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAuthorServerIndex_Object = MibTableColumn
hwtacacsClientAuthorServerIndex = _HwtacacsClientAuthorServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 2),
    _HwtacacsClientAuthorServerIndex_Type()
)
hwtacacsClientAuthorServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerIndex.setStatus("current")
_HwtacacsClientAuthorServerAddress_Type = IpAddress
_HwtacacsClientAuthorServerAddress_Object = MibTableColumn
hwtacacsClientAuthorServerAddress = _HwtacacsClientAuthorServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 3),
    _HwtacacsClientAuthorServerAddress_Type()
)
hwtacacsClientAuthorServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerAddress.setStatus("current")


class _HwtacacsClientAuthorServerPort_Type(Integer32):
    """Custom type hwtacacsClientAuthorServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwtacacsClientAuthorServerPort_Type.__name__ = "Integer32"
_HwtacacsClientAuthorServerPort_Object = MibTableColumn
hwtacacsClientAuthorServerPort = _HwtacacsClientAuthorServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 4),
    _HwtacacsClientAuthorServerPort_Type()
)
hwtacacsClientAuthorServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerPort.setStatus("current")


class _HwtacacsClientAuthorServerType_Type(Integer32):
    """Custom type hwtacacsClientAuthorServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthorServerType_Type.__name__ = "Integer32"
_HwtacacsClientAuthorServerType_Object = MibTableColumn
hwtacacsClientAuthorServerType = _HwtacacsClientAuthorServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 5),
    _HwtacacsClientAuthorServerType_Type()
)
hwtacacsClientAuthorServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerType.setStatus("current")


class _HwtacacsClientAuthorServerState_Type(Integer32):
    """Custom type hwtacacsClientAuthorServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthorServerState_Type.__name__ = "Integer32"
_HwtacacsClientAuthorServerState_Object = MibTableColumn
hwtacacsClientAuthorServerState = _HwtacacsClientAuthorServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 6),
    _HwtacacsClientAuthorServerState_Type()
)
hwtacacsClientAuthorServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerState.setStatus("current")


class _HwtacacsClientAuthorServerMode_Type(Integer32):
    """Custom type hwtacacsClientAuthorServerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAuthorServerMode_Type.__name__ = "Integer32"
_HwtacacsClientAuthorServerMode_Object = MibTableColumn
hwtacacsClientAuthorServerMode = _HwtacacsClientAuthorServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 7),
    _HwtacacsClientAuthorServerMode_Type()
)
hwtacacsClientAuthorServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerMode.setStatus("current")
_HwtacacsClientAuthorRoundTripTime_Type = TimeTicks
_HwtacacsClientAuthorRoundTripTime_Object = MibTableColumn
hwtacacsClientAuthorRoundTripTime = _HwtacacsClientAuthorRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 8),
    _HwtacacsClientAuthorRoundTripTime_Type()
)
hwtacacsClientAuthorRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorRoundTripTime.setStatus("current")
_HwtacacsClientAuthorRequestPackets_Type = Counter32
_HwtacacsClientAuthorRequestPackets_Object = MibTableColumn
hwtacacsClientAuthorRequestPackets = _HwtacacsClientAuthorRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 9),
    _HwtacacsClientAuthorRequestPackets_Type()
)
hwtacacsClientAuthorRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorRequestPackets.setStatus("current")
_HwtacacsClientAuthorResponseAcceptPackets_Type = Counter32
_HwtacacsClientAuthorResponseAcceptPackets_Object = MibTableColumn
hwtacacsClientAuthorResponseAcceptPackets = _HwtacacsClientAuthorResponseAcceptPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 10),
    _HwtacacsClientAuthorResponseAcceptPackets_Type()
)
hwtacacsClientAuthorResponseAcceptPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorResponseAcceptPackets.setStatus("current")
_HwtacacsClientAuthorResponseRejectPackets_Type = Counter32
_HwtacacsClientAuthorResponseRejectPackets_Object = MibTableColumn
hwtacacsClientAuthorResponseRejectPackets = _HwtacacsClientAuthorResponseRejectPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 11),
    _HwtacacsClientAuthorResponseRejectPackets_Type()
)
hwtacacsClientAuthorResponseRejectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorResponseRejectPackets.setStatus("current")
_HwtacacsClientAuthorResponseErrorPackets_Type = Counter32
_HwtacacsClientAuthorResponseErrorPackets_Object = MibTableColumn
hwtacacsClientAuthorResponseErrorPackets = _HwtacacsClientAuthorResponseErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 12),
    _HwtacacsClientAuthorResponseErrorPackets_Type()
)
hwtacacsClientAuthorResponseErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorResponseErrorPackets.setStatus("current")
_HwtacacsClientAuthorPendingRequests_Type = Gauge32
_HwtacacsClientAuthorPendingRequests_Object = MibTableColumn
hwtacacsClientAuthorPendingRequests = _HwtacacsClientAuthorPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 13),
    _HwtacacsClientAuthorPendingRequests_Type()
)
hwtacacsClientAuthorPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorPendingRequests.setStatus("current")
_HwtacacsClientAuthorTimeouts_Type = Counter32
_HwtacacsClientAuthorTimeouts_Object = MibTableColumn
hwtacacsClientAuthorTimeouts = _HwtacacsClientAuthorTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 14),
    _HwtacacsClientAuthorTimeouts_Type()
)
hwtacacsClientAuthorTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorTimeouts.setStatus("current")
_HwtacacsClientAuthorUnknownTypePackets_Type = Counter32
_HwtacacsClientAuthorUnknownTypePackets_Object = MibTableColumn
hwtacacsClientAuthorUnknownTypePackets = _HwtacacsClientAuthorUnknownTypePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 15),
    _HwtacacsClientAuthorUnknownTypePackets_Type()
)
hwtacacsClientAuthorUnknownTypePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorUnknownTypePackets.setStatus("current")
_HwtacacsClientAuthorDroppedPackets_Type = Counter32
_HwtacacsClientAuthorDroppedPackets_Object = MibTableColumn
hwtacacsClientAuthorDroppedPackets = _HwtacacsClientAuthorDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 16),
    _HwtacacsClientAuthorDroppedPackets_Type()
)
hwtacacsClientAuthorDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorDroppedPackets.setStatus("current")


class _HwtacacsClientAuthorVPNName_Type(OctetString):
    """Custom type hwtacacsClientAuthorVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwtacacsClientAuthorVPNName_Type.__name__ = "OctetString"
_HwtacacsClientAuthorVPNName_Object = MibTableColumn
hwtacacsClientAuthorVPNName = _HwtacacsClientAuthorVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 17),
    _HwtacacsClientAuthorVPNName_Type()
)
hwtacacsClientAuthorVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorVPNName.setStatus("current")
_HwtacacsClientAuthorRowStatus_Type = RowStatus
_HwtacacsClientAuthorRowStatus_Object = MibTableColumn
hwtacacsClientAuthorRowStatus = _HwtacacsClientAuthorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 16, 1, 18),
    _HwtacacsClientAuthorRowStatus_Type()
)
hwtacacsClientAuthorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAuthorRowStatus.setStatus("current")
_HwtacacsClientAccountServerTable_Object = MibTable
hwtacacsClientAccountServerTable = _HwtacacsClientAccountServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17)
)
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerTable.setStatus("current")
_HwtacacsClientAccountServerEntry_Object = MibTableRow
hwtacacsClientAccountServerEntry = _HwtacacsClientAccountServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1)
)
hwtacacsClientAccountServerEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountTemplateIndex"),
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerIndex"),
)
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerEntry.setStatus("current")


class _HwtacacsClientAccountTemplateIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAccountTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwtacacsClientAccountTemplateIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAccountTemplateIndex_Object = MibTableColumn
hwtacacsClientAccountTemplateIndex = _HwtacacsClientAccountTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 1),
    _HwtacacsClientAccountTemplateIndex_Type()
)
hwtacacsClientAccountTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAccountTemplateIndex.setStatus("current")


class _HwtacacsClientAccountServerIndex_Type(Unsigned32):
    """Custom type hwtacacsClientAccountServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwtacacsClientAccountServerIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientAccountServerIndex_Object = MibTableColumn
hwtacacsClientAccountServerIndex = _HwtacacsClientAccountServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 2),
    _HwtacacsClientAccountServerIndex_Type()
)
hwtacacsClientAccountServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerIndex.setStatus("current")
_HwtacacsClientAccountServerAddress_Type = IpAddress
_HwtacacsClientAccountServerAddress_Object = MibTableColumn
hwtacacsClientAccountServerAddress = _HwtacacsClientAccountServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 3),
    _HwtacacsClientAccountServerAddress_Type()
)
hwtacacsClientAccountServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerAddress.setStatus("current")


class _HwtacacsClientAccountServerPort_Type(Integer32):
    """Custom type hwtacacsClientAccountServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwtacacsClientAccountServerPort_Type.__name__ = "Integer32"
_HwtacacsClientAccountServerPort_Object = MibTableColumn
hwtacacsClientAccountServerPort = _HwtacacsClientAccountServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 4),
    _HwtacacsClientAccountServerPort_Type()
)
hwtacacsClientAccountServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerPort.setStatus("current")


class _HwtacacsClientAccountServerType_Type(Integer32):
    """Custom type hwtacacsClientAccountServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAccountServerType_Type.__name__ = "Integer32"
_HwtacacsClientAccountServerType_Object = MibTableColumn
hwtacacsClientAccountServerType = _HwtacacsClientAccountServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 5),
    _HwtacacsClientAccountServerType_Type()
)
hwtacacsClientAccountServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerType.setStatus("current")


class _HwtacacsClientAccountServerState_Type(Integer32):
    """Custom type hwtacacsClientAccountServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAccountServerState_Type.__name__ = "Integer32"
_HwtacacsClientAccountServerState_Object = MibTableColumn
hwtacacsClientAccountServerState = _HwtacacsClientAccountServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 6),
    _HwtacacsClientAccountServerState_Type()
)
hwtacacsClientAccountServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerState.setStatus("current")


class _HwtacacsClientAccountServerMode_Type(Integer32):
    """Custom type hwtacacsClientAccountServerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientAccountServerMode_Type.__name__ = "Integer32"
_HwtacacsClientAccountServerMode_Object = MibTableColumn
hwtacacsClientAccountServerMode = _HwtacacsClientAccountServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 7),
    _HwtacacsClientAccountServerMode_Type()
)
hwtacacsClientAccountServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerMode.setStatus("current")
_HwtacacsClientAccountRoundTripTime_Type = TimeTicks
_HwtacacsClientAccountRoundTripTime_Object = MibTableColumn
hwtacacsClientAccountRoundTripTime = _HwtacacsClientAccountRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 8),
    _HwtacacsClientAccountRoundTripTime_Type()
)
hwtacacsClientAccountRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountRoundTripTime.setStatus("current")
_HwtacacsClientAccountRequestPackets_Type = Counter32
_HwtacacsClientAccountRequestPackets_Object = MibTableColumn
hwtacacsClientAccountRequestPackets = _HwtacacsClientAccountRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 9),
    _HwtacacsClientAccountRequestPackets_Type()
)
hwtacacsClientAccountRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountRequestPackets.setStatus("current")
_HwtacacsClientAccountReqNetwork_Type = Counter32
_HwtacacsClientAccountReqNetwork_Object = MibTableColumn
hwtacacsClientAccountReqNetwork = _HwtacacsClientAccountReqNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 10),
    _HwtacacsClientAccountReqNetwork_Type()
)
hwtacacsClientAccountReqNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqNetwork.setStatus("current")
_HwtacacsClientAccountReqConnection_Type = Counter32
_HwtacacsClientAccountReqConnection_Object = MibTableColumn
hwtacacsClientAccountReqConnection = _HwtacacsClientAccountReqConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 11),
    _HwtacacsClientAccountReqConnection_Type()
)
hwtacacsClientAccountReqConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqConnection.setStatus("current")
_HwtacacsClientAccountReqEXEC_Type = Counter32
_HwtacacsClientAccountReqEXEC_Object = MibTableColumn
hwtacacsClientAccountReqEXEC = _HwtacacsClientAccountReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 12),
    _HwtacacsClientAccountReqEXEC_Type()
)
hwtacacsClientAccountReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqEXEC.setStatus("current")
_HwtacacsClientAccountReqSysEvent_Type = Counter32
_HwtacacsClientAccountReqSysEvent_Object = MibTableColumn
hwtacacsClientAccountReqSysEvent = _HwtacacsClientAccountReqSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 13),
    _HwtacacsClientAccountReqSysEvent_Type()
)
hwtacacsClientAccountReqSysEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqSysEvent.setStatus("current")
_HwtacacsClientAccountReqCommandLevel_Type = Counter32
_HwtacacsClientAccountReqCommandLevel_Object = MibTableColumn
hwtacacsClientAccountReqCommandLevel = _HwtacacsClientAccountReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 14),
    _HwtacacsClientAccountReqCommandLevel_Type()
)
hwtacacsClientAccountReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqCommandLevel.setStatus("current")
_HwtacacsClientAccountReqUpdate_Type = Counter32
_HwtacacsClientAccountReqUpdate_Object = MibTableColumn
hwtacacsClientAccountReqUpdate = _HwtacacsClientAccountReqUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 15),
    _HwtacacsClientAccountReqUpdate_Type()
)
hwtacacsClientAccountReqUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqUpdate.setStatus("current")
_HwtacacsClientAccountResponsePackets_Type = Counter32
_HwtacacsClientAccountResponsePackets_Object = MibTableColumn
hwtacacsClientAccountResponsePackets = _HwtacacsClientAccountResponsePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 16),
    _HwtacacsClientAccountResponsePackets_Type()
)
hwtacacsClientAccountResponsePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountResponsePackets.setStatus("current")
_HwtacacsClientAccountResponseErrorPackets_Type = Counter32
_HwtacacsClientAccountResponseErrorPackets_Object = MibTableColumn
hwtacacsClientAccountResponseErrorPackets = _HwtacacsClientAccountResponseErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 17),
    _HwtacacsClientAccountResponseErrorPackets_Type()
)
hwtacacsClientAccountResponseErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountResponseErrorPackets.setStatus("current")
_HwtacacsClientAccountReqPending_Type = Counter32
_HwtacacsClientAccountReqPending_Object = MibTableColumn
hwtacacsClientAccountReqPending = _HwtacacsClientAccountReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 18),
    _HwtacacsClientAccountReqPending_Type()
)
hwtacacsClientAccountReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountReqPending.setStatus("current")
_HwtacacsClientAccountTimeouts_Type = Counter32
_HwtacacsClientAccountTimeouts_Object = MibTableColumn
hwtacacsClientAccountTimeouts = _HwtacacsClientAccountTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 19),
    _HwtacacsClientAccountTimeouts_Type()
)
hwtacacsClientAccountTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountTimeouts.setStatus("current")
_HwtacacsClientAccountUnKnownTypes_Type = Counter32
_HwtacacsClientAccountUnKnownTypes_Object = MibTableColumn
hwtacacsClientAccountUnKnownTypes = _HwtacacsClientAccountUnKnownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 20),
    _HwtacacsClientAccountUnKnownTypes_Type()
)
hwtacacsClientAccountUnKnownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountUnKnownTypes.setStatus("current")
_HwtacacsClientAccountPacketsDropped_Type = Counter32
_HwtacacsClientAccountPacketsDropped_Object = MibTableColumn
hwtacacsClientAccountPacketsDropped = _HwtacacsClientAccountPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 21),
    _HwtacacsClientAccountPacketsDropped_Type()
)
hwtacacsClientAccountPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountPacketsDropped.setStatus("current")


class _HwtacacsClientAccountVPNName_Type(OctetString):
    """Custom type hwtacacsClientAccountVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwtacacsClientAccountVPNName_Type.__name__ = "OctetString"
_HwtacacsClientAccountVPNName_Object = MibTableColumn
hwtacacsClientAccountVPNName = _HwtacacsClientAccountVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 22),
    _HwtacacsClientAccountVPNName_Type()
)
hwtacacsClientAccountVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientAccountVPNName.setStatus("current")
_HwtacacsClientAccountRowStatus_Type = RowStatus
_HwtacacsClientAccountRowStatus_Object = MibTableColumn
hwtacacsClientAccountRowStatus = _HwtacacsClientAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 17, 1, 23),
    _HwtacacsClientAccountRowStatus_Type()
)
hwtacacsClientAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientAccountRowStatus.setStatus("current")
_HwtacacsClientCommonServerTable_Object = MibTable
hwtacacsClientCommonServerTable = _HwtacacsClientCommonServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18)
)
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerTable.setStatus("current")
_HwtacacsClientCommonServerEntry_Object = MibTableRow
hwtacacsClientCommonServerEntry = _HwtacacsClientCommonServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1)
)
hwtacacsClientCommonServerEntry.setIndexNames(
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonTemplateIndex"),
    (0, "HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerIndex"),
)
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerEntry.setStatus("current")


class _HwtacacsClientCommonTemplateIndex_Type(Unsigned32):
    """Custom type hwtacacsClientCommonTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwtacacsClientCommonTemplateIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientCommonTemplateIndex_Object = MibTableColumn
hwtacacsClientCommonTemplateIndex = _HwtacacsClientCommonTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 1),
    _HwtacacsClientCommonTemplateIndex_Type()
)
hwtacacsClientCommonTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientCommonTemplateIndex.setStatus("current")


class _HwtacacsClientCommonServerIndex_Type(Unsigned32):
    """Custom type hwtacacsClientCommonServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwtacacsClientCommonServerIndex_Type.__name__ = "Unsigned32"
_HwtacacsClientCommonServerIndex_Object = MibTableColumn
hwtacacsClientCommonServerIndex = _HwtacacsClientCommonServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 2),
    _HwtacacsClientCommonServerIndex_Type()
)
hwtacacsClientCommonServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerIndex.setStatus("current")
_HwtacacsClientCommonServerAddress_Type = IpAddress
_HwtacacsClientCommonServerAddress_Object = MibTableColumn
hwtacacsClientCommonServerAddress = _HwtacacsClientCommonServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 3),
    _HwtacacsClientCommonServerAddress_Type()
)
hwtacacsClientCommonServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerAddress.setStatus("current")


class _HwtacacsClientCommonServerPort_Type(Integer32):
    """Custom type hwtacacsClientCommonServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwtacacsClientCommonServerPort_Type.__name__ = "Integer32"
_HwtacacsClientCommonServerPort_Object = MibTableColumn
hwtacacsClientCommonServerPort = _HwtacacsClientCommonServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 4),
    _HwtacacsClientCommonServerPort_Type()
)
hwtacacsClientCommonServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerPort.setStatus("current")


class _HwtacacsClientCommonServerType_Type(Integer32):
    """Custom type hwtacacsClientCommonServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientCommonServerType_Type.__name__ = "Integer32"
_HwtacacsClientCommonServerType_Object = MibTableColumn
hwtacacsClientCommonServerType = _HwtacacsClientCommonServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 5),
    _HwtacacsClientCommonServerType_Type()
)
hwtacacsClientCommonServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerType.setStatus("current")


class _HwtacacsClientCommonServerState_Type(Integer32):
    """Custom type hwtacacsClientCommonServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientCommonServerState_Type.__name__ = "Integer32"
_HwtacacsClientCommonServerState_Object = MibTableColumn
hwtacacsClientCommonServerState = _HwtacacsClientCommonServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 6),
    _HwtacacsClientCommonServerState_Type()
)
hwtacacsClientCommonServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerState.setStatus("current")


class _HwtacacsClientCommonServerMode_Type(Integer32):
    """Custom type hwtacacsClientCommonServerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwtacacsClientCommonServerMode_Type.__name__ = "Integer32"
_HwtacacsClientCommonServerMode_Object = MibTableColumn
hwtacacsClientCommonServerMode = _HwtacacsClientCommonServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 7),
    _HwtacacsClientCommonServerMode_Type()
)
hwtacacsClientCommonServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerMode.setStatus("current")
_HwtacacsClientCommonRoundTripTime_Type = TimeTicks
_HwtacacsClientCommonRoundTripTime_Object = MibTableColumn
hwtacacsClientCommonRoundTripTime = _HwtacacsClientCommonRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 8),
    _HwtacacsClientCommonRoundTripTime_Type()
)
hwtacacsClientCommonRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonRoundTripTime.setStatus("current")
_HwtacacsClientCommonRequestPackets_Type = Counter32
_HwtacacsClientCommonRequestPackets_Object = MibTableColumn
hwtacacsClientCommonRequestPackets = _HwtacacsClientCommonRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 9),
    _HwtacacsClientCommonRequestPackets_Type()
)
hwtacacsClientCommonRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonRequestPackets.setStatus("current")
_HwtacacsClientCommonAccessChngPassRequests_Type = Counter32
_HwtacacsClientCommonAccessChngPassRequests_Object = MibTableColumn
hwtacacsClientCommonAccessChngPassRequests = _HwtacacsClientCommonAccessChngPassRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 10),
    _HwtacacsClientCommonAccessChngPassRequests_Type()
)
hwtacacsClientCommonAccessChngPassRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonAccessChngPassRequests.setStatus("current")
_HwtacacsClientCommonAccessSendPassPackets_Type = Counter32
_HwtacacsClientCommonAccessSendPassPackets_Object = MibTableColumn
hwtacacsClientCommonAccessSendPassPackets = _HwtacacsClientCommonAccessSendPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 11),
    _HwtacacsClientCommonAccessSendPassPackets_Type()
)
hwtacacsClientCommonAccessSendPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonAccessSendPassPackets.setStatus("current")
_HwtacacsClientCommonAccessSendAuthenPackets_Type = Counter32
_HwtacacsClientCommonAccessSendAuthenPackets_Object = MibTableColumn
hwtacacsClientCommonAccessSendAuthenPackets = _HwtacacsClientCommonAccessSendAuthenPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 12),
    _HwtacacsClientCommonAccessSendAuthenPackets_Type()
)
hwtacacsClientCommonAccessSendAuthenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonAccessSendAuthenPackets.setStatus("current")
_HwtacacsClientCommonStartPackets_Type = Counter32
_HwtacacsClientCommonStartPackets_Object = MibTableColumn
hwtacacsClientCommonStartPackets = _HwtacacsClientCommonStartPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 13),
    _HwtacacsClientCommonStartPackets_Type()
)
hwtacacsClientCommonStartPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonStartPackets.setStatus("current")
_HwtacacsClientCommonContinuePackets_Type = Counter32
_HwtacacsClientCommonContinuePackets_Object = MibTableColumn
hwtacacsClientCommonContinuePackets = _HwtacacsClientCommonContinuePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 14),
    _HwtacacsClientCommonContinuePackets_Type()
)
hwtacacsClientCommonContinuePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonContinuePackets.setStatus("current")
_HwtacacsClientCommomContinueAbortPackets_Type = Counter32
_HwtacacsClientCommomContinueAbortPackets_Object = MibTableColumn
hwtacacsClientCommomContinueAbortPackets = _HwtacacsClientCommomContinueAbortPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 15),
    _HwtacacsClientCommomContinueAbortPackets_Type()
)
hwtacacsClientCommomContinueAbortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommomContinueAbortPackets.setStatus("current")
_HwtacacsClientCommonReplyPackets_Type = Counter32
_HwtacacsClientCommonReplyPackets_Object = MibTableColumn
hwtacacsClientCommonReplyPackets = _HwtacacsClientCommonReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 16),
    _HwtacacsClientCommonReplyPackets_Type()
)
hwtacacsClientCommonReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyPackets.setStatus("current")
_HwtacacsClientCommonReplyPassPackets_Type = Counter32
_HwtacacsClientCommonReplyPassPackets_Object = MibTableColumn
hwtacacsClientCommonReplyPassPackets = _HwtacacsClientCommonReplyPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 17),
    _HwtacacsClientCommonReplyPassPackets_Type()
)
hwtacacsClientCommonReplyPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyPassPackets.setStatus("current")
_HwtacacsClientCommonReplyFailPackets_Type = Counter32
_HwtacacsClientCommonReplyFailPackets_Object = MibTableColumn
hwtacacsClientCommonReplyFailPackets = _HwtacacsClientCommonReplyFailPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 18),
    _HwtacacsClientCommonReplyFailPackets_Type()
)
hwtacacsClientCommonReplyFailPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyFailPackets.setStatus("current")
_HwtacacsClientCommonReplyGetDataPackets_Type = Counter32
_HwtacacsClientCommonReplyGetDataPackets_Object = MibTableColumn
hwtacacsClientCommonReplyGetDataPackets = _HwtacacsClientCommonReplyGetDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 19),
    _HwtacacsClientCommonReplyGetDataPackets_Type()
)
hwtacacsClientCommonReplyGetDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyGetDataPackets.setStatus("current")
_HwtacacsClientCommonReplyGetUserPackets_Type = Counter32
_HwtacacsClientCommonReplyGetUserPackets_Object = MibTableColumn
hwtacacsClientCommonReplyGetUserPackets = _HwtacacsClientCommonReplyGetUserPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 20),
    _HwtacacsClientCommonReplyGetUserPackets_Type()
)
hwtacacsClientCommonReplyGetUserPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyGetUserPackets.setStatus("current")
_HwtacacsClientCommonReplyGetPassPackets_Type = Counter32
_HwtacacsClientCommonReplyGetPassPackets_Object = MibTableColumn
hwtacacsClientCommonReplyGetPassPackets = _HwtacacsClientCommonReplyGetPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 21),
    _HwtacacsClientCommonReplyGetPassPackets_Type()
)
hwtacacsClientCommonReplyGetPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyGetPassPackets.setStatus("current")
_HwtacacsClientCommonReplyErrorPackets_Type = Counter32
_HwtacacsClientCommonReplyErrorPackets_Object = MibTableColumn
hwtacacsClientCommonReplyErrorPackets = _HwtacacsClientCommonReplyErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 22),
    _HwtacacsClientCommonReplyErrorPackets_Type()
)
hwtacacsClientCommonReplyErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyErrorPackets.setStatus("current")
_HwtacacsClientCommonReplyRestartPackets_Type = Counter32
_HwtacacsClientCommonReplyRestartPackets_Object = MibTableColumn
hwtacacsClientCommonReplyRestartPackets = _HwtacacsClientCommonReplyRestartPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 23),
    _HwtacacsClientCommonReplyRestartPackets_Type()
)
hwtacacsClientCommonReplyRestartPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyRestartPackets.setStatus("current")
_HwtacacsClientCommonReplyFollowPackets_Type = Counter32
_HwtacacsClientCommonReplyFollowPackets_Object = MibTableColumn
hwtacacsClientCommonReplyFollowPackets = _HwtacacsClientCommonReplyFollowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 24),
    _HwtacacsClientCommonReplyFollowPackets_Type()
)
hwtacacsClientCommonReplyFollowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReplyFollowPackets.setStatus("current")
_HwtacacsClientCommonReqNetwork_Type = Counter32
_HwtacacsClientCommonReqNetwork_Object = MibTableColumn
hwtacacsClientCommonReqNetwork = _HwtacacsClientCommonReqNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 25),
    _HwtacacsClientCommonReqNetwork_Type()
)
hwtacacsClientCommonReqNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqNetwork.setStatus("current")
_HwtacacsClientCommonReqConnection_Type = Counter32
_HwtacacsClientCommonReqConnection_Object = MibTableColumn
hwtacacsClientCommonReqConnection = _HwtacacsClientCommonReqConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 26),
    _HwtacacsClientCommonReqConnection_Type()
)
hwtacacsClientCommonReqConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqConnection.setStatus("current")
_HwtacacsClientCommonReqEXEC_Type = Counter32
_HwtacacsClientCommonReqEXEC_Object = MibTableColumn
hwtacacsClientCommonReqEXEC = _HwtacacsClientCommonReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 27),
    _HwtacacsClientCommonReqEXEC_Type()
)
hwtacacsClientCommonReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqEXEC.setStatus("current")
_HwtacacsClientCommonReqSysEvent_Type = Counter32
_HwtacacsClientCommonReqSysEvent_Object = MibTableColumn
hwtacacsClientCommonReqSysEvent = _HwtacacsClientCommonReqSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 28),
    _HwtacacsClientCommonReqSysEvent_Type()
)
hwtacacsClientCommonReqSysEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqSysEvent.setStatus("current")
_HwtacacsClientCommonReqCommandLevel_Type = Counter32
_HwtacacsClientCommonReqCommandLevel_Object = MibTableColumn
hwtacacsClientCommonReqCommandLevel = _HwtacacsClientCommonReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 29),
    _HwtacacsClientCommonReqCommandLevel_Type()
)
hwtacacsClientCommonReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqCommandLevel.setStatus("current")
_HwtacacsClientCommonReqUpdate_Type = Counter32
_HwtacacsClientCommonReqUpdate_Object = MibTableColumn
hwtacacsClientCommonReqUpdate = _HwtacacsClientCommonReqUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 30),
    _HwtacacsClientCommonReqUpdate_Type()
)
hwtacacsClientCommonReqUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonReqUpdate.setStatus("current")
_HwtacacsClientCommonPendingRequests_Type = Gauge32
_HwtacacsClientCommonPendingRequests_Object = MibTableColumn
hwtacacsClientCommonPendingRequests = _HwtacacsClientCommonPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 31),
    _HwtacacsClientCommonPendingRequests_Type()
)
hwtacacsClientCommonPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonPendingRequests.setStatus("current")
_HwtacacsClientCommonTimeouts_Type = Counter32
_HwtacacsClientCommonTimeouts_Object = MibTableColumn
hwtacacsClientCommonTimeouts = _HwtacacsClientCommonTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 32),
    _HwtacacsClientCommonTimeouts_Type()
)
hwtacacsClientCommonTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonTimeouts.setStatus("current")
_HwtacacsClientCommonUnknownTypePackets_Type = Counter32
_HwtacacsClientCommonUnknownTypePackets_Object = MibTableColumn
hwtacacsClientCommonUnknownTypePackets = _HwtacacsClientCommonUnknownTypePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 33),
    _HwtacacsClientCommonUnknownTypePackets_Type()
)
hwtacacsClientCommonUnknownTypePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonUnknownTypePackets.setStatus("current")
_HwtacacsClientCommonDroppedPackets_Type = Counter32
_HwtacacsClientCommonDroppedPackets_Object = MibTableColumn
hwtacacsClientCommonDroppedPackets = _HwtacacsClientCommonDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 34),
    _HwtacacsClientCommonDroppedPackets_Type()
)
hwtacacsClientCommonDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonDroppedPackets.setStatus("current")


class _HwtacacsClientCommonVPNName_Type(OctetString):
    """Custom type hwtacacsClientCommonVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwtacacsClientCommonVPNName_Type.__name__ = "OctetString"
_HwtacacsClientCommonVPNName_Object = MibTableColumn
hwtacacsClientCommonVPNName = _HwtacacsClientCommonVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 35),
    _HwtacacsClientCommonVPNName_Type()
)
hwtacacsClientCommonVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwtacacsClientCommonVPNName.setStatus("current")
_HwtacacsClientCommonRowStatus_Type = RowStatus
_HwtacacsClientCommonRowStatus_Object = MibTableColumn
hwtacacsClientCommonRowStatus = _HwtacacsClientCommonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 1, 18, 1, 36),
    _HwtacacsClientCommonRowStatus_Type()
)
hwtacacsClientCommonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwtacacsClientCommonRowStatus.setStatus("current")
_HwtacacsClientConformance_ObjectIdentity = ObjectIdentity
hwtacacsClientConformance = _HwtacacsClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2)
)
_HwtacacsClientCompliances_ObjectIdentity = ObjectIdentity
hwtacacsClientCompliances = _HwtacacsClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 1)
)
_HwtacacsClientObjectGroups_ObjectIdentity = ObjectIdentity
hwtacacsClientObjectGroups = _HwtacacsClientObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2)
)
_HwTacacsSetting_ObjectIdentity = ObjectIdentity
hwTacacsSetting = _HwTacacsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 4)
)
_HwTacacsSettingEntry_ObjectIdentity = ObjectIdentity
hwTacacsSettingEntry = _HwTacacsSettingEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 4, 1)
)


class _HwTACACSEnable_Type(Integer32):
    """Custom type hwTACACSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwTACACSEnable_Type.__name__ = "Integer32"
_HwTACACSEnable_Object = MibScalar
hwTACACSEnable = _HwTACACSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 4, 1, 1),
    _HwTACACSEnable_Type()
)
hwTACACSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSEnable.setStatus("current")


class _HwTACACSAcctStopResendDisable_Type(Integer32):
    """Custom type hwTACACSAcctStopResendDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwTACACSAcctStopResendDisable_Type.__name__ = "Integer32"
_HwTACACSAcctStopResendDisable_Object = MibScalar
hwTACACSAcctStopResendDisable = _HwTACACSAcctStopResendDisable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 4, 1, 2),
    _HwTACACSAcctStopResendDisable_Type()
)
hwTACACSAcctStopResendDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSAcctStopResendDisable.setStatus("current")


class _HwTACACSAcctStopResendNumber_Type(Integer32):
    """Custom type hwTACACSAcctStopResendNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwTACACSAcctStopResendNumber_Type.__name__ = "Integer32"
_HwTACACSAcctStopResendNumber_Object = MibScalar
hwTACACSAcctStopResendNumber = _HwTACACSAcctStopResendNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 4, 1, 3),
    _HwTACACSAcctStopResendNumber_Type()
)
hwTACACSAcctStopResendNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSAcctStopResendNumber.setStatus("current")

# Managed Objects groups

hwTacacsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2, 2, 1)
)
hwTacacsTableGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupIndex"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupName"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSourceIP"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupKey"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupTimer"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupDomain"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupOctFmt"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupTimeout"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAuthenAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAuthenPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAuthorAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAuthorPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAccoutAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupPriAccoutPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAuthenAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAuthenPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAuthorAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAuthorPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAccoutAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupSecAccoutPort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupCurAuthenAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupCurAuthorAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupCurAccoutAddr"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessReqLogin"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessReqChaPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessReqSendPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessReqSendAuth"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResFail"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResGetData"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResGetUser"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResGetPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResRestart"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessResFollow"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientMalformedAccessResponses"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessConPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientAccessConAbort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientPendingRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthenClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientReqEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientReqVPDN"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientResPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientResEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientResVPDN"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientReqPending"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAuthorClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqNetwork"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqConnection"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqSysEvent"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqCommandLevel"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqUpdate"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientResPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientReqPending"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSPriAccClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessReqLogin"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessReqChaPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessReqSendPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessReqSendAuth"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResFail"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResGetData"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResGetUser"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResGetPass"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResRestart"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessResFollow"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientMalformedAccessResponses"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessConPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientAccessConAbort"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientPendingRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthenClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientReqEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientReqVPDN"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientResPack"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientResEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientResVPDN"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientReqPending"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAuthorClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqNetwork"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqConnection"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqSysEvent"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqCommandLevel"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqUpdate"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientResPacket"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientResError"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientReqPending"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientUnknownTypes"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSSecAccClientPacketsDropped"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSServerGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwTacacsTableGroup.setStatus("current")

hwTacacsSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2, 2, 2)
)
hwTacacsSettingGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwTACACSEnable"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSAcctStopResendDisable"),
        ("HUAWEI-HWTACACS-MIB", "hwTACACSAcctStopResendNumber"))
)
if mibBuilder.loadTexts:
    hwTacacsSettingGroup.setStatus("current")

hwtacacsClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 1)
)
hwtacacsClientGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenRequestPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenAcceptPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenRejectPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenPendRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorReqPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorAcceptPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorRejectPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorPendRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientDroppedPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAcctRequestPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAcctResponsePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAcctErrorPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAcctPendingPackets"))
)
if mibBuilder.loadTexts:
    hwtacacsClientGroup.setStatus("current")

hwtacacsClientTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 2)
)
hwtacacsClientTemplateGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientTemplateName"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientSharedKey"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientSourceIP"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientResponseTimeout"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientDomainNameIncluded"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientQuietTimer"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientRowStatus"))
)
if mibBuilder.loadTexts:
    hwtacacsClientTemplateGroup.setStatus("current")

hwtacacsClientAuthenServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 3)
)
hwtacacsClientAuthenServerGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerAddress"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerPort"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerType"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerState"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenServerMode"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenAccessReqPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenAccessChngPassRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenAccessSendPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenAccessSendAuthenPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenStartPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenContinuePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenContinueAbortPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyFailPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyGetDataPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyGetUserPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyGetPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyErrorPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyRestartPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenReplyFollowPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenPendingRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenUnknownTypePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenDroppedPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenVPNName"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthenRowStatus"))
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthenServerGroup.setStatus("current")

hwtacacsClientAuthorServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 4)
)
hwtacacsClientAuthorServerGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerAddress"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerPort"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerType"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerState"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorServerMode"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorRequestPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorResponseAcceptPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorResponseRejectPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorResponseErrorPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorPendingRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorUnknownTypePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorDroppedPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorVPNName"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorRowStatus"))
)
if mibBuilder.loadTexts:
    hwtacacsClientAuthorServerGroup.setStatus("current")

hwtacacsClientAccountServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 5)
)
hwtacacsClientAccountServerGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerAddress"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerPort"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerType"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerState"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountServerMode"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountRequestPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountResponsePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountResponseErrorPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAccountVPNName"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientAuthorRowStatus"))
)
if mibBuilder.loadTexts:
    hwtacacsClientAccountServerGroup.setStatus("current")

hwtacacsClientCommonServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 2, 6)
)
hwtacacsClientCommonServerGroup.setObjects(
      *(("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerAddress"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerPort"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerType"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerState"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonServerMode"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonRoundTripTime"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonRequestPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonAccessChngPassRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonAccessSendPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonAccessSendAuthenPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonStartPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonContinuePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommomContinueAbortPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyFailPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyGetDataPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyGetUserPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyGetPassPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyErrorPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyRestartPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReplyFollowPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqNetwork"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqConnection"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqEXEC"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqSysEvent"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqCommandLevel"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonReqUpdate"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonPendingRequests"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonTimeouts"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonUnknownTypePackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonDroppedPackets"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonVPNName"),
        ("HUAWEI-HWTACACS-MIB", "hwtacacsClientCommonRowStatus"))
)
if mibBuilder.loadTexts:
    hwtacacsClientCommonServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwTacacsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwTacacsCompliance.setStatus(
        "current"
    )

hwtacacsClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwtacacsClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-HWTACACS-MIB",
    **{"hwTACACS": hwTACACS,
       "hwTACACSServerConfig": hwTACACSServerConfig,
       "hwTACACSServerGroupTable": hwTACACSServerGroupTable,
       "hwTACACSServerGroupEntry": hwTACACSServerGroupEntry,
       "hwTACACSServerGroupIndex": hwTACACSServerGroupIndex,
       "hwTACACSServerGroupName": hwTACACSServerGroupName,
       "hwTACACSServerGroupSourceIP": hwTACACSServerGroupSourceIP,
       "hwTACACSServerGroupKey": hwTACACSServerGroupKey,
       "hwTACACSServerGroupTimer": hwTACACSServerGroupTimer,
       "hwTACACSServerGroupDomain": hwTACACSServerGroupDomain,
       "hwTACACSServerGroupOctFmt": hwTACACSServerGroupOctFmt,
       "hwTACACSServerGroupTimeout": hwTACACSServerGroupTimeout,
       "hwTACACSServerGroupPriAuthenAddr": hwTACACSServerGroupPriAuthenAddr,
       "hwTACACSServerGroupPriAuthenPort": hwTACACSServerGroupPriAuthenPort,
       "hwTACACSServerGroupPriAuthorAddr": hwTACACSServerGroupPriAuthorAddr,
       "hwTACACSServerGroupPriAuthorPort": hwTACACSServerGroupPriAuthorPort,
       "hwTACACSServerGroupPriAccoutAddr": hwTACACSServerGroupPriAccoutAddr,
       "hwTACACSServerGroupPriAccoutPort": hwTACACSServerGroupPriAccoutPort,
       "hwTACACSServerGroupSecAuthenAddr": hwTACACSServerGroupSecAuthenAddr,
       "hwTACACSServerGroupSecAuthenPort": hwTACACSServerGroupSecAuthenPort,
       "hwTACACSServerGroupSecAuthorAddr": hwTACACSServerGroupSecAuthorAddr,
       "hwTACACSServerGroupSecAuthorPort": hwTACACSServerGroupSecAuthorPort,
       "hwTACACSServerGroupSecAccoutAddr": hwTACACSServerGroupSecAccoutAddr,
       "hwTACACSServerGroupSecAccoutPort": hwTACACSServerGroupSecAccoutPort,
       "hwTACACSServerGroupCurAuthenAddr": hwTACACSServerGroupCurAuthenAddr,
       "hwTACACSServerGroupCurAuthorAddr": hwTACACSServerGroupCurAuthorAddr,
       "hwTACACSServerGroupCurAccoutAddr": hwTACACSServerGroupCurAccoutAddr,
       "hwTACACSPriAuthenClientRoundTripTime": hwTACACSPriAuthenClientRoundTripTime,
       "hwTACACSPriAuthenClientAccessReqPacket": hwTACACSPriAuthenClientAccessReqPacket,
       "hwTACACSPriAuthenClientAccessReqLogin": hwTACACSPriAuthenClientAccessReqLogin,
       "hwTACACSPriAuthenClientAccessReqChaPass": hwTACACSPriAuthenClientAccessReqChaPass,
       "hwTACACSPriAuthenClientAccessReqSendPass": hwTACACSPriAuthenClientAccessReqSendPass,
       "hwTACACSPriAuthenClientAccessReqSendAuth": hwTACACSPriAuthenClientAccessReqSendAuth,
       "hwTACACSPriAuthenClientAccessResPack": hwTACACSPriAuthenClientAccessResPack,
       "hwTACACSPriAuthenClientAccessResPass": hwTACACSPriAuthenClientAccessResPass,
       "hwTACACSPriAuthenClientAccessResFail": hwTACACSPriAuthenClientAccessResFail,
       "hwTACACSPriAuthenClientAccessResGetData": hwTACACSPriAuthenClientAccessResGetData,
       "hwTACACSPriAuthenClientAccessResGetUser": hwTACACSPriAuthenClientAccessResGetUser,
       "hwTACACSPriAuthenClientAccessResGetPass": hwTACACSPriAuthenClientAccessResGetPass,
       "hwTACACSPriAuthenClientAccessResRestart": hwTACACSPriAuthenClientAccessResRestart,
       "hwTACACSPriAuthenClientAccessResError": hwTACACSPriAuthenClientAccessResError,
       "hwTACACSPriAuthenClientAccessResFollow": hwTACACSPriAuthenClientAccessResFollow,
       "hwTACACSPriAuthenClientMalformedAccessResponses": hwTACACSPriAuthenClientMalformedAccessResponses,
       "hwTACACSPriAuthenClientAccessConPack": hwTACACSPriAuthenClientAccessConPack,
       "hwTACACSPriAuthenClientAccessConAbort": hwTACACSPriAuthenClientAccessConAbort,
       "hwTACACSPriAuthenClientPendingRequests": hwTACACSPriAuthenClientPendingRequests,
       "hwTACACSPriAuthenClientTimeouts": hwTACACSPriAuthenClientTimeouts,
       "hwTACACSPriAuthenClientUnknownTypes": hwTACACSPriAuthenClientUnknownTypes,
       "hwTACACSPriAuthenClientPacketsDropped": hwTACACSPriAuthenClientPacketsDropped,
       "hwTACACSPriAuthorClientRoundTripTime": hwTACACSPriAuthorClientRoundTripTime,
       "hwTACACSPriAuthorClientReqPacket": hwTACACSPriAuthorClientReqPacket,
       "hwTACACSPriAuthorClientReqEXEC": hwTACACSPriAuthorClientReqEXEC,
       "hwTACACSPriAuthorClientReqVPDN": hwTACACSPriAuthorClientReqVPDN,
       "hwTACACSPriAuthorClientResPack": hwTACACSPriAuthorClientResPack,
       "hwTACACSPriAuthorClientResEXEC": hwTACACSPriAuthorClientResEXEC,
       "hwTACACSPriAuthorClientResVPDN": hwTACACSPriAuthorClientResVPDN,
       "hwTACACSPriAuthorClientResError": hwTACACSPriAuthorClientResError,
       "hwTACACSPriAuthorClientReqPending": hwTACACSPriAuthorClientReqPending,
       "hwTACACSPriAuthorClientTimeouts": hwTACACSPriAuthorClientTimeouts,
       "hwTACACSPriAuthorClientUnknownTypes": hwTACACSPriAuthorClientUnknownTypes,
       "hwTACACSPriAuthorClientPacketsDropped": hwTACACSPriAuthorClientPacketsDropped,
       "hwTACACSPriAccClientRoundTripTime": hwTACACSPriAccClientRoundTripTime,
       "hwTACACSPriAccClientReqPacket": hwTACACSPriAccClientReqPacket,
       "hwTACACSPriAccClientReqNetwork": hwTACACSPriAccClientReqNetwork,
       "hwTACACSPriAccClientReqConnection": hwTACACSPriAccClientReqConnection,
       "hwTACACSPriAccClientReqEXEC": hwTACACSPriAccClientReqEXEC,
       "hwTACACSPriAccClientReqSysEvent": hwTACACSPriAccClientReqSysEvent,
       "hwTACACSPriAccClientReqCommandLevel": hwTACACSPriAccClientReqCommandLevel,
       "hwTACACSPriAccClientReqUpdate": hwTACACSPriAccClientReqUpdate,
       "hwTACACSPriAccClientResPacket": hwTACACSPriAccClientResPacket,
       "hwTACACSPriAccClientResError": hwTACACSPriAccClientResError,
       "hwTACACSPriAccClientReqPending": hwTACACSPriAccClientReqPending,
       "hwTACACSPriAccClientTimeouts": hwTACACSPriAccClientTimeouts,
       "hwTACACSPriAccClientUnknownTypes": hwTACACSPriAccClientUnknownTypes,
       "hwTACACSPriAccClientPacketsDropped": hwTACACSPriAccClientPacketsDropped,
       "hwTACACSSecAuthenClientRoundTripTime": hwTACACSSecAuthenClientRoundTripTime,
       "hwTACACSSecAuthenClientAccessReqPacket": hwTACACSSecAuthenClientAccessReqPacket,
       "hwTACACSSecAuthenClientAccessReqLogin": hwTACACSSecAuthenClientAccessReqLogin,
       "hwTACACSSecAuthenClientAccessReqChaPass": hwTACACSSecAuthenClientAccessReqChaPass,
       "hwTACACSSecAuthenClientAccessReqSendPass": hwTACACSSecAuthenClientAccessReqSendPass,
       "hwTACACSSecAuthenClientAccessReqSendAuth": hwTACACSSecAuthenClientAccessReqSendAuth,
       "hwTACACSSecAuthenClientAccessResPack": hwTACACSSecAuthenClientAccessResPack,
       "hwTACACSSecAuthenClientAccessResPass": hwTACACSSecAuthenClientAccessResPass,
       "hwTACACSSecAuthenClientAccessResFail": hwTACACSSecAuthenClientAccessResFail,
       "hwTACACSSecAuthenClientAccessResGetData": hwTACACSSecAuthenClientAccessResGetData,
       "hwTACACSSecAuthenClientAccessResGetUser": hwTACACSSecAuthenClientAccessResGetUser,
       "hwTACACSSecAuthenClientAccessResGetPass": hwTACACSSecAuthenClientAccessResGetPass,
       "hwTACACSSecAuthenClientAccessResRestart": hwTACACSSecAuthenClientAccessResRestart,
       "hwTACACSSecAuthenClientAccessResError": hwTACACSSecAuthenClientAccessResError,
       "hwTACACSSecAuthenClientAccessResFollow": hwTACACSSecAuthenClientAccessResFollow,
       "hwTACACSSecAuthenClientMalformedAccessResponses": hwTACACSSecAuthenClientMalformedAccessResponses,
       "hwTACACSSecAuthenClientAccessConPack": hwTACACSSecAuthenClientAccessConPack,
       "hwTACACSSecAuthenClientAccessConAbort": hwTACACSSecAuthenClientAccessConAbort,
       "hwTACACSSecAuthenClientPendingRequests": hwTACACSSecAuthenClientPendingRequests,
       "hwTACACSSecAuthenClientTimeouts": hwTACACSSecAuthenClientTimeouts,
       "hwTACACSSecAuthenClientUnknownTypes": hwTACACSSecAuthenClientUnknownTypes,
       "hwTACACSSecAuthenClientPacketsDropped": hwTACACSSecAuthenClientPacketsDropped,
       "hwTACACSSecAuthorClientRoundTripTime": hwTACACSSecAuthorClientRoundTripTime,
       "hwTACACSSecAuthorClientReqPacket": hwTACACSSecAuthorClientReqPacket,
       "hwTACACSSecAuthorClientReqEXEC": hwTACACSSecAuthorClientReqEXEC,
       "hwTACACSSecAuthorClientReqVPDN": hwTACACSSecAuthorClientReqVPDN,
       "hwTACACSSecAuthorClientResPack": hwTACACSSecAuthorClientResPack,
       "hwTACACSSecAuthorClientResEXEC": hwTACACSSecAuthorClientResEXEC,
       "hwTACACSSecAuthorClientResVPDN": hwTACACSSecAuthorClientResVPDN,
       "hwTACACSSecAuthorClientResError": hwTACACSSecAuthorClientResError,
       "hwTACACSSecAuthorClientReqPending": hwTACACSSecAuthorClientReqPending,
       "hwTACACSSecAuthorClientTimeouts": hwTACACSSecAuthorClientTimeouts,
       "hwTACACSSecAuthorClientUnknownTypes": hwTACACSSecAuthorClientUnknownTypes,
       "hwTACACSSecAuthorClientPacketsDropped": hwTACACSSecAuthorClientPacketsDropped,
       "hwTACACSSecAccClientRoundTripTime": hwTACACSSecAccClientRoundTripTime,
       "hwTACACSSecAccClientReqPacket": hwTACACSSecAccClientReqPacket,
       "hwTACACSSecAccClientReqNetwork": hwTACACSSecAccClientReqNetwork,
       "hwTACACSSecAccClientReqConnection": hwTACACSSecAccClientReqConnection,
       "hwTACACSSecAccClientReqEXEC": hwTACACSSecAccClientReqEXEC,
       "hwTACACSSecAccClientReqSysEvent": hwTACACSSecAccClientReqSysEvent,
       "hwTACACSSecAccClientReqCommandLevel": hwTACACSSecAccClientReqCommandLevel,
       "hwTACACSSecAccClientReqUpdate": hwTACACSSecAccClientReqUpdate,
       "hwTACACSSecAccClientResPacket": hwTACACSSecAccClientResPacket,
       "hwTACACSSecAccClientResError": hwTACACSSecAccClientResError,
       "hwTACACSSecAccClientReqPending": hwTACACSSecAccClientReqPending,
       "hwTACACSSecAccClientTimeouts": hwTACACSSecAccClientTimeouts,
       "hwTACACSSecAccClientUnknownTypes": hwTACACSSecAccClientUnknownTypes,
       "hwTACACSSecAccClientPacketsDropped": hwTACACSSecAccClientPacketsDropped,
       "hwTACACSServerGroupRowStatus": hwTACACSServerGroupRowStatus,
       "hwTacacsConformance": hwTacacsConformance,
       "hwTacacsCompliances": hwTacacsCompliances,
       "hwTacacsCompliance": hwTacacsCompliance,
       "hwTacacsObjectGroups": hwTacacsObjectGroups,
       "hwTacacsTableGroup": hwTacacsTableGroup,
       "hwTacacsSettingGroup": hwTacacsSettingGroup,
       "hwtacacsClientMng": hwtacacsClientMng,
       "hwtacacsClient": hwtacacsClient,
       "hwtacacsClientAuthenRequestPackets": hwtacacsClientAuthenRequestPackets,
       "hwtacacsClientAuthenAcceptPackets": hwtacacsClientAuthenAcceptPackets,
       "hwtacacsClientAuthenRejectPackets": hwtacacsClientAuthenRejectPackets,
       "hwtacacsClientAuthenPendRequests": hwtacacsClientAuthenPendRequests,
       "hwtacacsClientAuthorReqPackets": hwtacacsClientAuthorReqPackets,
       "hwtacacsClientAuthorAcceptPackets": hwtacacsClientAuthorAcceptPackets,
       "hwtacacsClientAuthorRejectPackets": hwtacacsClientAuthorRejectPackets,
       "hwtacacsClientAuthorPendRequests": hwtacacsClientAuthorPendRequests,
       "hwtacacsClientDroppedPackets": hwtacacsClientDroppedPackets,
       "hwtacacsClientAcctRequestPackets": hwtacacsClientAcctRequestPackets,
       "hwtacacsClientAcctResponsePackets": hwtacacsClientAcctResponsePackets,
       "hwtacacsClientAcctErrorPackets": hwtacacsClientAcctErrorPackets,
       "hwtacacsClientAcctPendingPackets": hwtacacsClientAcctPendingPackets,
       "hwtacacsTemplateTable": hwtacacsTemplateTable,
       "hwtacacsTemplateEntry": hwtacacsTemplateEntry,
       "hwtacacsClientTemplateIndex": hwtacacsClientTemplateIndex,
       "hwtacacsClientTemplateName": hwtacacsClientTemplateName,
       "hwtacacsClientSharedKey": hwtacacsClientSharedKey,
       "hwtacacsClientSourceIP": hwtacacsClientSourceIP,
       "hwtacacsClientQuietTimer": hwtacacsClientQuietTimer,
       "hwtacacsClientResponseTimeout": hwtacacsClientResponseTimeout,
       "hwtacacsClientDomainNameIncluded": hwtacacsClientDomainNameIncluded,
       "hwtacacsClientRowStatus": hwtacacsClientRowStatus,
       "hwtacacsClientAuthenServerTable": hwtacacsClientAuthenServerTable,
       "hwtacacsClientAuthenServerEntry": hwtacacsClientAuthenServerEntry,
       "hwtacacsClientAuthenTemplateIndex": hwtacacsClientAuthenTemplateIndex,
       "hwtacacsClientAuthenServerIndex": hwtacacsClientAuthenServerIndex,
       "hwtacacsClientAuthenServerAddress": hwtacacsClientAuthenServerAddress,
       "hwtacacsClientAuthenServerPort": hwtacacsClientAuthenServerPort,
       "hwtacacsClientAuthenServerType": hwtacacsClientAuthenServerType,
       "hwtacacsClientAuthenServerState": hwtacacsClientAuthenServerState,
       "hwtacacsClientAuthenServerMode": hwtacacsClientAuthenServerMode,
       "hwtacacsClientAuthenRoundTripTime": hwtacacsClientAuthenRoundTripTime,
       "hwtacacsClientAuthenAccessReqPackets": hwtacacsClientAuthenAccessReqPackets,
       "hwtacacsClientAuthenAccessChngPassRequests": hwtacacsClientAuthenAccessChngPassRequests,
       "hwtacacsClientAuthenAccessSendPassPackets": hwtacacsClientAuthenAccessSendPassPackets,
       "hwtacacsClientAuthenAccessSendAuthenPackets": hwtacacsClientAuthenAccessSendAuthenPackets,
       "hwtacacsClientAuthenStartPackets": hwtacacsClientAuthenStartPackets,
       "hwtacacsClientAuthenContinuePackets": hwtacacsClientAuthenContinuePackets,
       "hwtacacsClientAuthenContinueAbortPackets": hwtacacsClientAuthenContinueAbortPackets,
       "hwtacacsClientAuthenReplyPackets": hwtacacsClientAuthenReplyPackets,
       "hwtacacsClientAuthenReplyPassPackets": hwtacacsClientAuthenReplyPassPackets,
       "hwtacacsClientAuthenReplyFailPackets": hwtacacsClientAuthenReplyFailPackets,
       "hwtacacsClientAuthenReplyGetDataPackets": hwtacacsClientAuthenReplyGetDataPackets,
       "hwtacacsClientAuthenReplyGetUserPackets": hwtacacsClientAuthenReplyGetUserPackets,
       "hwtacacsClientAuthenReplyGetPassPackets": hwtacacsClientAuthenReplyGetPassPackets,
       "hwtacacsClientAuthenReplyErrorPackets": hwtacacsClientAuthenReplyErrorPackets,
       "hwtacacsClientAuthenReplyRestartPackets": hwtacacsClientAuthenReplyRestartPackets,
       "hwtacacsClientAuthenReplyFollowPackets": hwtacacsClientAuthenReplyFollowPackets,
       "hwtacacsClientAuthenPendingRequests": hwtacacsClientAuthenPendingRequests,
       "hwtacacsClientAuthenTimeouts": hwtacacsClientAuthenTimeouts,
       "hwtacacsClientAuthenUnknownTypePackets": hwtacacsClientAuthenUnknownTypePackets,
       "hwtacacsClientAuthenDroppedPackets": hwtacacsClientAuthenDroppedPackets,
       "hwtacacsClientAuthenVPNName": hwtacacsClientAuthenVPNName,
       "hwtacacsClientAuthenRowStatus": hwtacacsClientAuthenRowStatus,
       "hwtacacsClientAuthorServerTable": hwtacacsClientAuthorServerTable,
       "hwtacacsClientAuthorServerEntry": hwtacacsClientAuthorServerEntry,
       "hwtacacsClientAuthorTemplateIndex": hwtacacsClientAuthorTemplateIndex,
       "hwtacacsClientAuthorServerIndex": hwtacacsClientAuthorServerIndex,
       "hwtacacsClientAuthorServerAddress": hwtacacsClientAuthorServerAddress,
       "hwtacacsClientAuthorServerPort": hwtacacsClientAuthorServerPort,
       "hwtacacsClientAuthorServerType": hwtacacsClientAuthorServerType,
       "hwtacacsClientAuthorServerState": hwtacacsClientAuthorServerState,
       "hwtacacsClientAuthorServerMode": hwtacacsClientAuthorServerMode,
       "hwtacacsClientAuthorRoundTripTime": hwtacacsClientAuthorRoundTripTime,
       "hwtacacsClientAuthorRequestPackets": hwtacacsClientAuthorRequestPackets,
       "hwtacacsClientAuthorResponseAcceptPackets": hwtacacsClientAuthorResponseAcceptPackets,
       "hwtacacsClientAuthorResponseRejectPackets": hwtacacsClientAuthorResponseRejectPackets,
       "hwtacacsClientAuthorResponseErrorPackets": hwtacacsClientAuthorResponseErrorPackets,
       "hwtacacsClientAuthorPendingRequests": hwtacacsClientAuthorPendingRequests,
       "hwtacacsClientAuthorTimeouts": hwtacacsClientAuthorTimeouts,
       "hwtacacsClientAuthorUnknownTypePackets": hwtacacsClientAuthorUnknownTypePackets,
       "hwtacacsClientAuthorDroppedPackets": hwtacacsClientAuthorDroppedPackets,
       "hwtacacsClientAuthorVPNName": hwtacacsClientAuthorVPNName,
       "hwtacacsClientAuthorRowStatus": hwtacacsClientAuthorRowStatus,
       "hwtacacsClientAccountServerTable": hwtacacsClientAccountServerTable,
       "hwtacacsClientAccountServerEntry": hwtacacsClientAccountServerEntry,
       "hwtacacsClientAccountTemplateIndex": hwtacacsClientAccountTemplateIndex,
       "hwtacacsClientAccountServerIndex": hwtacacsClientAccountServerIndex,
       "hwtacacsClientAccountServerAddress": hwtacacsClientAccountServerAddress,
       "hwtacacsClientAccountServerPort": hwtacacsClientAccountServerPort,
       "hwtacacsClientAccountServerType": hwtacacsClientAccountServerType,
       "hwtacacsClientAccountServerState": hwtacacsClientAccountServerState,
       "hwtacacsClientAccountServerMode": hwtacacsClientAccountServerMode,
       "hwtacacsClientAccountRoundTripTime": hwtacacsClientAccountRoundTripTime,
       "hwtacacsClientAccountRequestPackets": hwtacacsClientAccountRequestPackets,
       "hwtacacsClientAccountReqNetwork": hwtacacsClientAccountReqNetwork,
       "hwtacacsClientAccountReqConnection": hwtacacsClientAccountReqConnection,
       "hwtacacsClientAccountReqEXEC": hwtacacsClientAccountReqEXEC,
       "hwtacacsClientAccountReqSysEvent": hwtacacsClientAccountReqSysEvent,
       "hwtacacsClientAccountReqCommandLevel": hwtacacsClientAccountReqCommandLevel,
       "hwtacacsClientAccountReqUpdate": hwtacacsClientAccountReqUpdate,
       "hwtacacsClientAccountResponsePackets": hwtacacsClientAccountResponsePackets,
       "hwtacacsClientAccountResponseErrorPackets": hwtacacsClientAccountResponseErrorPackets,
       "hwtacacsClientAccountReqPending": hwtacacsClientAccountReqPending,
       "hwtacacsClientAccountTimeouts": hwtacacsClientAccountTimeouts,
       "hwtacacsClientAccountUnKnownTypes": hwtacacsClientAccountUnKnownTypes,
       "hwtacacsClientAccountPacketsDropped": hwtacacsClientAccountPacketsDropped,
       "hwtacacsClientAccountVPNName": hwtacacsClientAccountVPNName,
       "hwtacacsClientAccountRowStatus": hwtacacsClientAccountRowStatus,
       "hwtacacsClientCommonServerTable": hwtacacsClientCommonServerTable,
       "hwtacacsClientCommonServerEntry": hwtacacsClientCommonServerEntry,
       "hwtacacsClientCommonTemplateIndex": hwtacacsClientCommonTemplateIndex,
       "hwtacacsClientCommonServerIndex": hwtacacsClientCommonServerIndex,
       "hwtacacsClientCommonServerAddress": hwtacacsClientCommonServerAddress,
       "hwtacacsClientCommonServerPort": hwtacacsClientCommonServerPort,
       "hwtacacsClientCommonServerType": hwtacacsClientCommonServerType,
       "hwtacacsClientCommonServerState": hwtacacsClientCommonServerState,
       "hwtacacsClientCommonServerMode": hwtacacsClientCommonServerMode,
       "hwtacacsClientCommonRoundTripTime": hwtacacsClientCommonRoundTripTime,
       "hwtacacsClientCommonRequestPackets": hwtacacsClientCommonRequestPackets,
       "hwtacacsClientCommonAccessChngPassRequests": hwtacacsClientCommonAccessChngPassRequests,
       "hwtacacsClientCommonAccessSendPassPackets": hwtacacsClientCommonAccessSendPassPackets,
       "hwtacacsClientCommonAccessSendAuthenPackets": hwtacacsClientCommonAccessSendAuthenPackets,
       "hwtacacsClientCommonStartPackets": hwtacacsClientCommonStartPackets,
       "hwtacacsClientCommonContinuePackets": hwtacacsClientCommonContinuePackets,
       "hwtacacsClientCommomContinueAbortPackets": hwtacacsClientCommomContinueAbortPackets,
       "hwtacacsClientCommonReplyPackets": hwtacacsClientCommonReplyPackets,
       "hwtacacsClientCommonReplyPassPackets": hwtacacsClientCommonReplyPassPackets,
       "hwtacacsClientCommonReplyFailPackets": hwtacacsClientCommonReplyFailPackets,
       "hwtacacsClientCommonReplyGetDataPackets": hwtacacsClientCommonReplyGetDataPackets,
       "hwtacacsClientCommonReplyGetUserPackets": hwtacacsClientCommonReplyGetUserPackets,
       "hwtacacsClientCommonReplyGetPassPackets": hwtacacsClientCommonReplyGetPassPackets,
       "hwtacacsClientCommonReplyErrorPackets": hwtacacsClientCommonReplyErrorPackets,
       "hwtacacsClientCommonReplyRestartPackets": hwtacacsClientCommonReplyRestartPackets,
       "hwtacacsClientCommonReplyFollowPackets": hwtacacsClientCommonReplyFollowPackets,
       "hwtacacsClientCommonReqNetwork": hwtacacsClientCommonReqNetwork,
       "hwtacacsClientCommonReqConnection": hwtacacsClientCommonReqConnection,
       "hwtacacsClientCommonReqEXEC": hwtacacsClientCommonReqEXEC,
       "hwtacacsClientCommonReqSysEvent": hwtacacsClientCommonReqSysEvent,
       "hwtacacsClientCommonReqCommandLevel": hwtacacsClientCommonReqCommandLevel,
       "hwtacacsClientCommonReqUpdate": hwtacacsClientCommonReqUpdate,
       "hwtacacsClientCommonPendingRequests": hwtacacsClientCommonPendingRequests,
       "hwtacacsClientCommonTimeouts": hwtacacsClientCommonTimeouts,
       "hwtacacsClientCommonUnknownTypePackets": hwtacacsClientCommonUnknownTypePackets,
       "hwtacacsClientCommonDroppedPackets": hwtacacsClientCommonDroppedPackets,
       "hwtacacsClientCommonVPNName": hwtacacsClientCommonVPNName,
       "hwtacacsClientCommonRowStatus": hwtacacsClientCommonRowStatus,
       "hwtacacsClientConformance": hwtacacsClientConformance,
       "hwtacacsClientCompliances": hwtacacsClientCompliances,
       "hwtacacsClientCompliance": hwtacacsClientCompliance,
       "hwtacacsClientObjectGroups": hwtacacsClientObjectGroups,
       "hwtacacsClientGroup": hwtacacsClientGroup,
       "hwtacacsClientTemplateGroup": hwtacacsClientTemplateGroup,
       "hwtacacsClientAuthenServerGroup": hwtacacsClientAuthenServerGroup,
       "hwtacacsClientAuthorServerGroup": hwtacacsClientAuthorServerGroup,
       "hwtacacsClientAccountServerGroup": hwtacacsClientAccountServerGroup,
       "hwtacacsClientCommonServerGroup": hwtacacsClientCommonServerGroup,
       "hwTacacsSetting": hwTacacsSetting,
       "hwTacacsSettingEntry": hwTacacsSettingEntry,
       "hwTACACSEnable": hwTACACSEnable,
       "hwTACACSAcctStopResendDisable": hwTACACSAcctStopResendDisable,
       "hwTACACSAcctStopResendNumber": hwTACACSAcctStopResendNumber}
)
