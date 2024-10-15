# SNMP MIB module (HUAWEI-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TACACS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:09 2024
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

(huawei,
 huaweiDatacomm,
 huaweiMgmt) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "huaweiDatacomm",
    "huaweiMgmt")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTACACS_ObjectIdentity = ObjectIdentity
hwTACACS = _HwTACACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20)
)
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
_HwTACACSServerGroupTableEntry_Object = MibTableRow
hwTACACSServerGroupTableEntry = _HwTACACSServerGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1)
)
hwTACACSServerGroupTableEntry.setIndexNames(
    (0, "HUAWEI-TACACS-MIB", "hwTACACSServerGroupName"),
)
if mibBuilder.loadTexts:
    hwTACACSServerGroupTableEntry.setStatus("current")


class _HwTACACSServerGroupName_Type(OctetString):
    """Custom type hwTACACSServerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwTACACSServerGroupName_Type.__name__ = "OctetString"
_HwTACACSServerGroupName_Object = MibTableColumn
hwTACACSServerGroupName = _HwTACACSServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 1),
    _HwTACACSServerGroupName_Type()
)
hwTACACSServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupName.setStatus("current")
_HwTACACSServerGroupSourceIP_Type = IpAddress
_HwTACACSServerGroupSourceIP_Object = MibTableColumn
hwTACACSServerGroupSourceIP = _HwTACACSServerGroupSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 2),
    _HwTACACSServerGroupSourceIP_Type()
)
hwTACACSServerGroupSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupSourceIP.setStatus("current")


class _HwTACACSServerGroupKey_Type(OctetString):
    """Custom type hwTACACSServerGroupKey based on OctetString"""
    defaultValue = 5

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTACACSServerGroupKey_Type.__name__ = "OctetString"
_HwTACACSServerGroupKey_Object = MibTableColumn
hwTACACSServerGroupKey = _HwTACACSServerGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 3),
    _HwTACACSServerGroupKey_Type()
)
hwTACACSServerGroupKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupKey.setStatus("current")


class _HwTACACSServerGroupTimer_Type(Integer32):
    """Custom type hwTACACSServerGroupTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwTACACSServerGroupTimer_Type.__name__ = "Integer32"
_HwTACACSServerGroupTimer_Object = MibTableColumn
hwTACACSServerGroupTimer = _HwTACACSServerGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 4),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_HwTACACSServerGroupDomain_Type.__name__ = "Integer32"
_HwTACACSServerGroupDomain_Object = MibTableColumn
hwTACACSServerGroupDomain = _HwTACACSServerGroupDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 5),
    _HwTACACSServerGroupDomain_Type()
)
hwTACACSServerGroupDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupDomain.setStatus("current")
_HwTACACSServerGroupPriAuthen_Type = IpAddress
_HwTACACSServerGroupPriAuthen_Object = MibTableColumn
hwTACACSServerGroupPriAuthen = _HwTACACSServerGroupPriAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 6),
    _HwTACACSServerGroupPriAuthen_Type()
)
hwTACACSServerGroupPriAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthen.setStatus("current")
_HwTACACSServerGroupPriAuthor_Type = IpAddress
_HwTACACSServerGroupPriAuthor_Object = MibTableColumn
hwTACACSServerGroupPriAuthor = _HwTACACSServerGroupPriAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 7),
    _HwTACACSServerGroupPriAuthor_Type()
)
hwTACACSServerGroupPriAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAuthor.setStatus("current")
_HwTACACSServerGroupPriAccout_Type = IpAddress
_HwTACACSServerGroupPriAccout_Object = MibTableColumn
hwTACACSServerGroupPriAccout = _HwTACACSServerGroupPriAccout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 8),
    _HwTACACSServerGroupPriAccout_Type()
)
hwTACACSServerGroupPriAccout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupPriAccout.setStatus("current")
_HwTACACSServerGroupCurAuthen_Type = IpAddress
_HwTACACSServerGroupCurAuthen_Object = MibTableColumn
hwTACACSServerGroupCurAuthen = _HwTACACSServerGroupCurAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 9),
    _HwTACACSServerGroupCurAuthen_Type()
)
hwTACACSServerGroupCurAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAuthen.setStatus("current")
_HwTACACSServerGroupCurAuthor_Type = IpAddress
_HwTACACSServerGroupCurAuthor_Object = MibTableColumn
hwTACACSServerGroupCurAuthor = _HwTACACSServerGroupCurAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 10),
    _HwTACACSServerGroupCurAuthor_Type()
)
hwTACACSServerGroupCurAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAuthor.setStatus("current")
_HwTACACSServerGroupCurAccout_Type = IpAddress
_HwTACACSServerGroupCurAccout_Object = MibTableColumn
hwTACACSServerGroupCurAccout = _HwTACACSServerGroupCurAccout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 11),
    _HwTACACSServerGroupCurAccout_Type()
)
hwTACACSServerGroupCurAccout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerGroupCurAccout.setStatus("current")
_HwTACACSServerGroupRowStatus_Type = RowStatus
_HwTACACSServerGroupRowStatus_Object = MibTableColumn
hwTACACSServerGroupRowStatus = _HwTACACSServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 1, 1, 12),
    _HwTACACSServerGroupRowStatus_Type()
)
hwTACACSServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerGroupRowStatus.setStatus("current")
_HwTACACSServerTable_Object = MibTable
hwTACACSServerTable = _HwTACACSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hwTACACSServerTable.setStatus("current")
_HwTACACSServerTableEntry_Object = MibTableRow
hwTACACSServerTableEntry = _HwTACACSServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1)
)
hwTACACSServerTableEntry.setIndexNames(
    (0, "HUAWEI-TACACS-MIB", "hwTACACSGroupName"),
    (0, "HUAWEI-TACACS-MIB", "hwTACACSServerAddr"),
)
if mibBuilder.loadTexts:
    hwTACACSServerTableEntry.setStatus("current")


class _HwTACACSGroupName_Type(OctetString):
    """Custom type hwTACACSGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwTACACSGroupName_Type.__name__ = "OctetString"
_HwTACACSGroupName_Object = MibTableColumn
hwTACACSGroupName = _HwTACACSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 1),
    _HwTACACSGroupName_Type()
)
hwTACACSGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSGroupName.setStatus("current")
_HwTACACSServerAddr_Type = IpAddress
_HwTACACSServerAddr_Object = MibTableColumn
hwTACACSServerAddr = _HwTACACSServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 2),
    _HwTACACSServerAddr_Type()
)
hwTACACSServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSServerAddr.setStatus("current")


class _HwTACACSServerPort_Type(Integer32):
    """Custom type hwTACACSServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTACACSServerPort_Type.__name__ = "Integer32"
_HwTACACSServerPort_Object = MibTableColumn
hwTACACSServerPort = _HwTACACSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 3),
    _HwTACACSServerPort_Type()
)
hwTACACSServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerPort.setStatus("current")


class _HwTACACSTimeout_Type(Integer32):
    """Custom type hwTACACSTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwTACACSTimeout_Type.__name__ = "Integer32"
_HwTACACSTimeout_Object = MibTableColumn
hwTACACSTimeout = _HwTACACSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 4),
    _HwTACACSTimeout_Type()
)
hwTACACSTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSTimeout.setStatus("current")


class _HwTACACSServerKey_Type(OctetString):
    """Custom type hwTACACSServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTACACSServerKey_Type.__name__ = "OctetString"
_HwTACACSServerKey_Object = MibTableColumn
hwTACACSServerKey = _HwTACACSServerKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 5),
    _HwTACACSServerKey_Type()
)
hwTACACSServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerKey.setStatus("current")


class _HwTACACSServerPriAuthen_Type(Integer32):
    """Custom type hwTACACSServerPriAuthen based on Integer32"""
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


_HwTACACSServerPriAuthen_Type.__name__ = "Integer32"
_HwTACACSServerPriAuthen_Object = MibTableColumn
hwTACACSServerPriAuthen = _HwTACACSServerPriAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 6),
    _HwTACACSServerPriAuthen_Type()
)
hwTACACSServerPriAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerPriAuthen.setStatus("current")


class _HwTACACSServerPriAuthor_Type(Integer32):
    """Custom type hwTACACSServerPriAuthor based on Integer32"""
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


_HwTACACSServerPriAuthor_Type.__name__ = "Integer32"
_HwTACACSServerPriAuthor_Object = MibTableColumn
hwTACACSServerPriAuthor = _HwTACACSServerPriAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 7),
    _HwTACACSServerPriAuthor_Type()
)
hwTACACSServerPriAuthor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerPriAuthor.setStatus("current")


class _HwTACACSServerPriAcct_Type(Integer32):
    """Custom type hwTACACSServerPriAcct based on Integer32"""
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


_HwTACACSServerPriAcct_Type.__name__ = "Integer32"
_HwTACACSServerPriAcct_Object = MibTableColumn
hwTACACSServerPriAcct = _HwTACACSServerPriAcct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 8),
    _HwTACACSServerPriAcct_Type()
)
hwTACACSServerPriAcct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerPriAcct.setStatus("current")
_HwTACACSAuthenClientRoundTripTime_Type = Integer32
_HwTACACSAuthenClientRoundTripTime_Object = MibTableColumn
hwTACACSAuthenClientRoundTripTime = _HwTACACSAuthenClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 9),
    _HwTACACSAuthenClientRoundTripTime_Type()
)
hwTACACSAuthenClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientRoundTripTime.setStatus("current")
_HwTACACSAuthenClientAccessReqPacket_Type = Counter32
_HwTACACSAuthenClientAccessReqPacket_Object = MibTableColumn
hwTACACSAuthenClientAccessReqPacket = _HwTACACSAuthenClientAccessReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 10),
    _HwTACACSAuthenClientAccessReqPacket_Type()
)
hwTACACSAuthenClientAccessReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessReqPacket.setStatus("current")
_HwTACACSAuthenClientAccessReqLogin_Type = Counter32
_HwTACACSAuthenClientAccessReqLogin_Object = MibTableColumn
hwTACACSAuthenClientAccessReqLogin = _HwTACACSAuthenClientAccessReqLogin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 11),
    _HwTACACSAuthenClientAccessReqLogin_Type()
)
hwTACACSAuthenClientAccessReqLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessReqLogin.setStatus("current")
_HwTACACSAuthenClientAccessReqChaPass_Type = Counter32
_HwTACACSAuthenClientAccessReqChaPass_Object = MibTableColumn
hwTACACSAuthenClientAccessReqChaPass = _HwTACACSAuthenClientAccessReqChaPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 12),
    _HwTACACSAuthenClientAccessReqChaPass_Type()
)
hwTACACSAuthenClientAccessReqChaPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessReqChaPass.setStatus("current")
_HwTACACSAuthenClientAccessReqSendPass_Type = Counter32
_HwTACACSAuthenClientAccessReqSendPass_Object = MibTableColumn
hwTACACSAuthenClientAccessReqSendPass = _HwTACACSAuthenClientAccessReqSendPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 13),
    _HwTACACSAuthenClientAccessReqSendPass_Type()
)
hwTACACSAuthenClientAccessReqSendPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessReqSendPass.setStatus("current")
_HwTACACSAuthenClientAccessReqSendAuth_Type = Counter32
_HwTACACSAuthenClientAccessReqSendAuth_Object = MibTableColumn
hwTACACSAuthenClientAccessReqSendAuth = _HwTACACSAuthenClientAccessReqSendAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 14),
    _HwTACACSAuthenClientAccessReqSendAuth_Type()
)
hwTACACSAuthenClientAccessReqSendAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessReqSendAuth.setStatus("current")
_HwTACACSAuthenClientAccessResPack_Type = Counter32
_HwTACACSAuthenClientAccessResPack_Object = MibTableColumn
hwTACACSAuthenClientAccessResPack = _HwTACACSAuthenClientAccessResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 15),
    _HwTACACSAuthenClientAccessResPack_Type()
)
hwTACACSAuthenClientAccessResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResPack.setStatus("current")
_HwTACACSAuthenClientAccessResPass_Type = Counter32
_HwTACACSAuthenClientAccessResPass_Object = MibTableColumn
hwTACACSAuthenClientAccessResPass = _HwTACACSAuthenClientAccessResPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 16),
    _HwTACACSAuthenClientAccessResPass_Type()
)
hwTACACSAuthenClientAccessResPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResPass.setStatus("current")
_HwTACACSAuthenClientAccessResFail_Type = Counter32
_HwTACACSAuthenClientAccessResFail_Object = MibTableColumn
hwTACACSAuthenClientAccessResFail = _HwTACACSAuthenClientAccessResFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 17),
    _HwTACACSAuthenClientAccessResFail_Type()
)
hwTACACSAuthenClientAccessResFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResFail.setStatus("current")
_HwTACACSAuthenClientAccessResGetData_Type = Counter32
_HwTACACSAuthenClientAccessResGetData_Object = MibTableColumn
hwTACACSAuthenClientAccessResGetData = _HwTACACSAuthenClientAccessResGetData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 18),
    _HwTACACSAuthenClientAccessResGetData_Type()
)
hwTACACSAuthenClientAccessResGetData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResGetData.setStatus("current")
_HwTACACSAuthenClientAccessResGetUser_Type = Counter32
_HwTACACSAuthenClientAccessResGetUser_Object = MibTableColumn
hwTACACSAuthenClientAccessResGetUser = _HwTACACSAuthenClientAccessResGetUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 19),
    _HwTACACSAuthenClientAccessResGetUser_Type()
)
hwTACACSAuthenClientAccessResGetUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResGetUser.setStatus("current")
_HwTACACSAuthenClientAccessResGetPass_Type = Counter32
_HwTACACSAuthenClientAccessResGetPass_Object = MibTableColumn
hwTACACSAuthenClientAccessResGetPass = _HwTACACSAuthenClientAccessResGetPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 20),
    _HwTACACSAuthenClientAccessResGetPass_Type()
)
hwTACACSAuthenClientAccessResGetPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResGetPass.setStatus("current")
_HwTACACSAuthenClientAccessResRestart_Type = Counter32
_HwTACACSAuthenClientAccessResRestart_Object = MibTableColumn
hwTACACSAuthenClientAccessResRestart = _HwTACACSAuthenClientAccessResRestart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 21),
    _HwTACACSAuthenClientAccessResRestart_Type()
)
hwTACACSAuthenClientAccessResRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResRestart.setStatus("current")
_HwTACACSAuthenClientAccessResError_Type = Counter32
_HwTACACSAuthenClientAccessResError_Object = MibTableColumn
hwTACACSAuthenClientAccessResError = _HwTACACSAuthenClientAccessResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 22),
    _HwTACACSAuthenClientAccessResError_Type()
)
hwTACACSAuthenClientAccessResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResError.setStatus("current")
_HwTACACSAuthenClientAccessResFollow_Type = Counter32
_HwTACACSAuthenClientAccessResFollow_Object = MibTableColumn
hwTACACSAuthenClientAccessResFollow = _HwTACACSAuthenClientAccessResFollow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 23),
    _HwTACACSAuthenClientAccessResFollow_Type()
)
hwTACACSAuthenClientAccessResFollow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessResFollow.setStatus("current")
_HwTACACSAuthenClientMalformedAccessResponses_Type = Counter32
_HwTACACSAuthenClientMalformedAccessResponses_Object = MibTableColumn
hwTACACSAuthenClientMalformedAccessResponses = _HwTACACSAuthenClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 24),
    _HwTACACSAuthenClientMalformedAccessResponses_Type()
)
hwTACACSAuthenClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientMalformedAccessResponses.setStatus("current")
_HwTACACSAuthenClientAccessConPack_Type = Counter32
_HwTACACSAuthenClientAccessConPack_Object = MibTableColumn
hwTACACSAuthenClientAccessConPack = _HwTACACSAuthenClientAccessConPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 25),
    _HwTACACSAuthenClientAccessConPack_Type()
)
hwTACACSAuthenClientAccessConPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessConPack.setStatus("current")
_HwTACACSAuthenClientAccessConAbort_Type = Counter32
_HwTACACSAuthenClientAccessConAbort_Object = MibTableColumn
hwTACACSAuthenClientAccessConAbort = _HwTACACSAuthenClientAccessConAbort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 26),
    _HwTACACSAuthenClientAccessConAbort_Type()
)
hwTACACSAuthenClientAccessConAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientAccessConAbort.setStatus("current")
_HwTACACSAuthenClientPendingRequests_Type = Counter32
_HwTACACSAuthenClientPendingRequests_Object = MibTableColumn
hwTACACSAuthenClientPendingRequests = _HwTACACSAuthenClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 27),
    _HwTACACSAuthenClientPendingRequests_Type()
)
hwTACACSAuthenClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientPendingRequests.setStatus("current")
_HwTACACSAuthenClientTimeouts_Type = Counter32
_HwTACACSAuthenClientTimeouts_Object = MibTableColumn
hwTACACSAuthenClientTimeouts = _HwTACACSAuthenClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 28),
    _HwTACACSAuthenClientTimeouts_Type()
)
hwTACACSAuthenClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientTimeouts.setStatus("current")
_HwTACACSAuthenClientUnknownTypes_Type = Counter32
_HwTACACSAuthenClientUnknownTypes_Object = MibTableColumn
hwTACACSAuthenClientUnknownTypes = _HwTACACSAuthenClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 29),
    _HwTACACSAuthenClientUnknownTypes_Type()
)
hwTACACSAuthenClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientUnknownTypes.setStatus("current")
_HwTACACSAuthenClientPacketsDropped_Type = Counter32
_HwTACACSAuthenClientPacketsDropped_Object = MibTableColumn
hwTACACSAuthenClientPacketsDropped = _HwTACACSAuthenClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 30),
    _HwTACACSAuthenClientPacketsDropped_Type()
)
hwTACACSAuthenClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthenClientPacketsDropped.setStatus("current")
_HwTACACSAuthorClientRoundTripTime_Type = Integer32
_HwTACACSAuthorClientRoundTripTime_Object = MibTableColumn
hwTACACSAuthorClientRoundTripTime = _HwTACACSAuthorClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 31),
    _HwTACACSAuthorClientRoundTripTime_Type()
)
hwTACACSAuthorClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientRoundTripTime.setStatus("current")
_HwTACACSAuthorClientReqPacket_Type = Counter32
_HwTACACSAuthorClientReqPacket_Object = MibTableColumn
hwTACACSAuthorClientReqPacket = _HwTACACSAuthorClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 32),
    _HwTACACSAuthorClientReqPacket_Type()
)
hwTACACSAuthorClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqPacket.setStatus("current")
_HwTACACSAuthorClientReqEXEC_Type = Counter32
_HwTACACSAuthorClientReqEXEC_Object = MibTableColumn
hwTACACSAuthorClientReqEXEC = _HwTACACSAuthorClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 33),
    _HwTACACSAuthorClientReqEXEC_Type()
)
hwTACACSAuthorClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqEXEC.setStatus("current")
_HwTACACSAuthorClientReqLCP_Type = Counter32
_HwTACACSAuthorClientReqLCP_Object = MibTableColumn
hwTACACSAuthorClientReqLCP = _HwTACACSAuthorClientReqLCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 34),
    _HwTACACSAuthorClientReqLCP_Type()
)
hwTACACSAuthorClientReqLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqLCP.setStatus("current")
_HwTACACSAuthorClientReqIPCP_Type = Counter32
_HwTACACSAuthorClientReqIPCP_Object = MibTableColumn
hwTACACSAuthorClientReqIPCP = _HwTACACSAuthorClientReqIPCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 35),
    _HwTACACSAuthorClientReqIPCP_Type()
)
hwTACACSAuthorClientReqIPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqIPCP.setStatus("current")
_HwTACACSAuthorClientReqVPDN_Type = Counter32
_HwTACACSAuthorClientReqVPDN_Object = MibTableColumn
hwTACACSAuthorClientReqVPDN = _HwTACACSAuthorClientReqVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 36),
    _HwTACACSAuthorClientReqVPDN_Type()
)
hwTACACSAuthorClientReqVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqVPDN.setStatus("current")
_HwTACACSAuthorClientReqCommandLevel_Type = Counter32
_HwTACACSAuthorClientReqCommandLevel_Object = MibTableColumn
hwTACACSAuthorClientReqCommandLevel = _HwTACACSAuthorClientReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 37),
    _HwTACACSAuthorClientReqCommandLevel_Type()
)
hwTACACSAuthorClientReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqCommandLevel.setStatus("current")
_HwTACACSAuthorClientResPack_Type = Counter32
_HwTACACSAuthorClientResPack_Object = MibTableColumn
hwTACACSAuthorClientResPack = _HwTACACSAuthorClientResPack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 38),
    _HwTACACSAuthorClientResPack_Type()
)
hwTACACSAuthorClientResPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResPack.setStatus("current")
_HwTACACSAuthorClientResEXEC_Type = Counter32
_HwTACACSAuthorClientResEXEC_Object = MibTableColumn
hwTACACSAuthorClientResEXEC = _HwTACACSAuthorClientResEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 39),
    _HwTACACSAuthorClientResEXEC_Type()
)
hwTACACSAuthorClientResEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResEXEC.setStatus("current")
_HwTACACSAuthorClientResLCP_Type = Counter32
_HwTACACSAuthorClientResLCP_Object = MibTableColumn
hwTACACSAuthorClientResLCP = _HwTACACSAuthorClientResLCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 40),
    _HwTACACSAuthorClientResLCP_Type()
)
hwTACACSAuthorClientResLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResLCP.setStatus("current")
_HwTACACSAuthorClientResIPCP_Type = Counter32
_HwTACACSAuthorClientResIPCP_Object = MibTableColumn
hwTACACSAuthorClientResIPCP = _HwTACACSAuthorClientResIPCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 41),
    _HwTACACSAuthorClientResIPCP_Type()
)
hwTACACSAuthorClientResIPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResIPCP.setStatus("current")
_HwTACACSAuthorClientResVPDN_Type = Counter32
_HwTACACSAuthorClientResVPDN_Object = MibTableColumn
hwTACACSAuthorClientResVPDN = _HwTACACSAuthorClientResVPDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 42),
    _HwTACACSAuthorClientResVPDN_Type()
)
hwTACACSAuthorClientResVPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResVPDN.setStatus("current")
_HwTACACSAuthorClientResCommandLevel_Type = Counter32
_HwTACACSAuthorClientResCommandLevel_Object = MibTableColumn
hwTACACSAuthorClientResCommandLevel = _HwTACACSAuthorClientResCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 43),
    _HwTACACSAuthorClientResCommandLevel_Type()
)
hwTACACSAuthorClientResCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResCommandLevel.setStatus("current")
_HwTACACSAuthorClientResError_Type = Counter32
_HwTACACSAuthorClientResError_Object = MibTableColumn
hwTACACSAuthorClientResError = _HwTACACSAuthorClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 44),
    _HwTACACSAuthorClientResError_Type()
)
hwTACACSAuthorClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientResError.setStatus("current")
_HwTACACSAuthorClientReqPending_Type = Counter32
_HwTACACSAuthorClientReqPending_Object = MibTableColumn
hwTACACSAuthorClientReqPending = _HwTACACSAuthorClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 45),
    _HwTACACSAuthorClientReqPending_Type()
)
hwTACACSAuthorClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientReqPending.setStatus("current")
_HwTACACSAuthorClientTimeouts_Type = Counter32
_HwTACACSAuthorClientTimeouts_Object = MibTableColumn
hwTACACSAuthorClientTimeouts = _HwTACACSAuthorClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 46),
    _HwTACACSAuthorClientTimeouts_Type()
)
hwTACACSAuthorClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientTimeouts.setStatus("current")
_HwTACACSAuthorClientUnknownTypes_Type = Counter32
_HwTACACSAuthorClientUnknownTypes_Object = MibTableColumn
hwTACACSAuthorClientUnknownTypes = _HwTACACSAuthorClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 47),
    _HwTACACSAuthorClientUnknownTypes_Type()
)
hwTACACSAuthorClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientUnknownTypes.setStatus("current")
_HwTACACSAuthorClientPacketsDropped_Type = Counter32
_HwTACACSAuthorClientPacketsDropped_Object = MibTableColumn
hwTACACSAuthorClientPacketsDropped = _HwTACACSAuthorClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 48),
    _HwTACACSAuthorClientPacketsDropped_Type()
)
hwTACACSAuthorClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAuthorClientPacketsDropped.setStatus("current")
_HwTACACSAccClientRoundTripTime_Type = Integer32
_HwTACACSAccClientRoundTripTime_Object = MibTableColumn
hwTACACSAccClientRoundTripTime = _HwTACACSAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 49),
    _HwTACACSAccClientRoundTripTime_Type()
)
hwTACACSAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientRoundTripTime.setStatus("current")
_HwTACACSAccClientReqPacket_Type = Counter32
_HwTACACSAccClientReqPacket_Object = MibTableColumn
hwTACACSAccClientReqPacket = _HwTACACSAccClientReqPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 50),
    _HwTACACSAccClientReqPacket_Type()
)
hwTACACSAccClientReqPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqPacket.setStatus("current")
_HwTACACSAccClientReqNetwork_Type = Counter32
_HwTACACSAccClientReqNetwork_Object = MibTableColumn
hwTACACSAccClientReqNetwork = _HwTACACSAccClientReqNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 51),
    _HwTACACSAccClientReqNetwork_Type()
)
hwTACACSAccClientReqNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqNetwork.setStatus("current")
_HwTACACSAccClientReqConnection_Type = Counter32
_HwTACACSAccClientReqConnection_Object = MibTableColumn
hwTACACSAccClientReqConnection = _HwTACACSAccClientReqConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 52),
    _HwTACACSAccClientReqConnection_Type()
)
hwTACACSAccClientReqConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqConnection.setStatus("current")
_HwTACACSAccClientReqEXEC_Type = Counter32
_HwTACACSAccClientReqEXEC_Object = MibTableColumn
hwTACACSAccClientReqEXEC = _HwTACACSAccClientReqEXEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 53),
    _HwTACACSAccClientReqEXEC_Type()
)
hwTACACSAccClientReqEXEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqEXEC.setStatus("current")
_HwTACACSAccClientReqSysEvent_Type = Counter32
_HwTACACSAccClientReqSysEvent_Object = MibTableColumn
hwTACACSAccClientReqSysEvent = _HwTACACSAccClientReqSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 54),
    _HwTACACSAccClientReqSysEvent_Type()
)
hwTACACSAccClientReqSysEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqSysEvent.setStatus("current")
_HwTACACSAccClientReqCommandLevel_Type = Counter32
_HwTACACSAccClientReqCommandLevel_Object = MibTableColumn
hwTACACSAccClientReqCommandLevel = _HwTACACSAccClientReqCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 55),
    _HwTACACSAccClientReqCommandLevel_Type()
)
hwTACACSAccClientReqCommandLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqCommandLevel.setStatus("current")
_HwTACACSAccClientReqUpdate_Type = Counter32
_HwTACACSAccClientReqUpdate_Object = MibTableColumn
hwTACACSAccClientReqUpdate = _HwTACACSAccClientReqUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 56),
    _HwTACACSAccClientReqUpdate_Type()
)
hwTACACSAccClientReqUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqUpdate.setStatus("current")
_HwTACACSAccClientResPacket_Type = Counter32
_HwTACACSAccClientResPacket_Object = MibTableColumn
hwTACACSAccClientResPacket = _HwTACACSAccClientResPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 57),
    _HwTACACSAccClientResPacket_Type()
)
hwTACACSAccClientResPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientResPacket.setStatus("current")
_HwTACACSAccClientResError_Type = Counter32
_HwTACACSAccClientResError_Object = MibTableColumn
hwTACACSAccClientResError = _HwTACACSAccClientResError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 58),
    _HwTACACSAccClientResError_Type()
)
hwTACACSAccClientResError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientResError.setStatus("current")
_HwTACACSAccClientReqPending_Type = Counter32
_HwTACACSAccClientReqPending_Object = MibTableColumn
hwTACACSAccClientReqPending = _HwTACACSAccClientReqPending_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 59),
    _HwTACACSAccClientReqPending_Type()
)
hwTACACSAccClientReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientReqPending.setStatus("current")
_HwTACACSAccClientTimeouts_Type = Counter32
_HwTACACSAccClientTimeouts_Object = MibTableColumn
hwTACACSAccClientTimeouts = _HwTACACSAccClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 60),
    _HwTACACSAccClientTimeouts_Type()
)
hwTACACSAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientTimeouts.setStatus("current")
_HwTACACSAccClientUnknownTypes_Type = Counter32
_HwTACACSAccClientUnknownTypes_Object = MibTableColumn
hwTACACSAccClientUnknownTypes = _HwTACACSAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 61),
    _HwTACACSAccClientUnknownTypes_Type()
)
hwTACACSAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientUnknownTypes.setStatus("current")
_HwTACACSAccClientPacketsDropped_Type = Counter32
_HwTACACSAccClientPacketsDropped_Object = MibTableColumn
hwTACACSAccClientPacketsDropped = _HwTACACSAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 62),
    _HwTACACSAccClientPacketsDropped_Type()
)
hwTACACSAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTACACSAccClientPacketsDropped.setStatus("current")
_HwTACACSServerRowStatus_Type = RowStatus
_HwTACACSServerRowStatus_Object = MibTableColumn
hwTACACSServerRowStatus = _HwTACACSServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 20, 1, 2, 1, 63),
    _HwTACACSServerRowStatus_Type()
)
hwTACACSServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTACACSServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TACACS-MIB",
    **{"hwTACACS": hwTACACS,
       "hwTACACSServerConfig": hwTACACSServerConfig,
       "hwTACACSServerGroupTable": hwTACACSServerGroupTable,
       "hwTACACSServerGroupTableEntry": hwTACACSServerGroupTableEntry,
       "hwTACACSServerGroupName": hwTACACSServerGroupName,
       "hwTACACSServerGroupSourceIP": hwTACACSServerGroupSourceIP,
       "hwTACACSServerGroupKey": hwTACACSServerGroupKey,
       "hwTACACSServerGroupTimer": hwTACACSServerGroupTimer,
       "hwTACACSServerGroupDomain": hwTACACSServerGroupDomain,
       "hwTACACSServerGroupPriAuthen": hwTACACSServerGroupPriAuthen,
       "hwTACACSServerGroupPriAuthor": hwTACACSServerGroupPriAuthor,
       "hwTACACSServerGroupPriAccout": hwTACACSServerGroupPriAccout,
       "hwTACACSServerGroupCurAuthen": hwTACACSServerGroupCurAuthen,
       "hwTACACSServerGroupCurAuthor": hwTACACSServerGroupCurAuthor,
       "hwTACACSServerGroupCurAccout": hwTACACSServerGroupCurAccout,
       "hwTACACSServerGroupRowStatus": hwTACACSServerGroupRowStatus,
       "hwTACACSServerTable": hwTACACSServerTable,
       "hwTACACSServerTableEntry": hwTACACSServerTableEntry,
       "hwTACACSGroupName": hwTACACSGroupName,
       "hwTACACSServerAddr": hwTACACSServerAddr,
       "hwTACACSServerPort": hwTACACSServerPort,
       "hwTACACSTimeout": hwTACACSTimeout,
       "hwTACACSServerKey": hwTACACSServerKey,
       "hwTACACSServerPriAuthen": hwTACACSServerPriAuthen,
       "hwTACACSServerPriAuthor": hwTACACSServerPriAuthor,
       "hwTACACSServerPriAcct": hwTACACSServerPriAcct,
       "hwTACACSAuthenClientRoundTripTime": hwTACACSAuthenClientRoundTripTime,
       "hwTACACSAuthenClientAccessReqPacket": hwTACACSAuthenClientAccessReqPacket,
       "hwTACACSAuthenClientAccessReqLogin": hwTACACSAuthenClientAccessReqLogin,
       "hwTACACSAuthenClientAccessReqChaPass": hwTACACSAuthenClientAccessReqChaPass,
       "hwTACACSAuthenClientAccessReqSendPass": hwTACACSAuthenClientAccessReqSendPass,
       "hwTACACSAuthenClientAccessReqSendAuth": hwTACACSAuthenClientAccessReqSendAuth,
       "hwTACACSAuthenClientAccessResPack": hwTACACSAuthenClientAccessResPack,
       "hwTACACSAuthenClientAccessResPass": hwTACACSAuthenClientAccessResPass,
       "hwTACACSAuthenClientAccessResFail": hwTACACSAuthenClientAccessResFail,
       "hwTACACSAuthenClientAccessResGetData": hwTACACSAuthenClientAccessResGetData,
       "hwTACACSAuthenClientAccessResGetUser": hwTACACSAuthenClientAccessResGetUser,
       "hwTACACSAuthenClientAccessResGetPass": hwTACACSAuthenClientAccessResGetPass,
       "hwTACACSAuthenClientAccessResRestart": hwTACACSAuthenClientAccessResRestart,
       "hwTACACSAuthenClientAccessResError": hwTACACSAuthenClientAccessResError,
       "hwTACACSAuthenClientAccessResFollow": hwTACACSAuthenClientAccessResFollow,
       "hwTACACSAuthenClientMalformedAccessResponses": hwTACACSAuthenClientMalformedAccessResponses,
       "hwTACACSAuthenClientAccessConPack": hwTACACSAuthenClientAccessConPack,
       "hwTACACSAuthenClientAccessConAbort": hwTACACSAuthenClientAccessConAbort,
       "hwTACACSAuthenClientPendingRequests": hwTACACSAuthenClientPendingRequests,
       "hwTACACSAuthenClientTimeouts": hwTACACSAuthenClientTimeouts,
       "hwTACACSAuthenClientUnknownTypes": hwTACACSAuthenClientUnknownTypes,
       "hwTACACSAuthenClientPacketsDropped": hwTACACSAuthenClientPacketsDropped,
       "hwTACACSAuthorClientRoundTripTime": hwTACACSAuthorClientRoundTripTime,
       "hwTACACSAuthorClientReqPacket": hwTACACSAuthorClientReqPacket,
       "hwTACACSAuthorClientReqEXEC": hwTACACSAuthorClientReqEXEC,
       "hwTACACSAuthorClientReqLCP": hwTACACSAuthorClientReqLCP,
       "hwTACACSAuthorClientReqIPCP": hwTACACSAuthorClientReqIPCP,
       "hwTACACSAuthorClientReqVPDN": hwTACACSAuthorClientReqVPDN,
       "hwTACACSAuthorClientReqCommandLevel": hwTACACSAuthorClientReqCommandLevel,
       "hwTACACSAuthorClientResPack": hwTACACSAuthorClientResPack,
       "hwTACACSAuthorClientResEXEC": hwTACACSAuthorClientResEXEC,
       "hwTACACSAuthorClientResLCP": hwTACACSAuthorClientResLCP,
       "hwTACACSAuthorClientResIPCP": hwTACACSAuthorClientResIPCP,
       "hwTACACSAuthorClientResVPDN": hwTACACSAuthorClientResVPDN,
       "hwTACACSAuthorClientResCommandLevel": hwTACACSAuthorClientResCommandLevel,
       "hwTACACSAuthorClientResError": hwTACACSAuthorClientResError,
       "hwTACACSAuthorClientReqPending": hwTACACSAuthorClientReqPending,
       "hwTACACSAuthorClientTimeouts": hwTACACSAuthorClientTimeouts,
       "hwTACACSAuthorClientUnknownTypes": hwTACACSAuthorClientUnknownTypes,
       "hwTACACSAuthorClientPacketsDropped": hwTACACSAuthorClientPacketsDropped,
       "hwTACACSAccClientRoundTripTime": hwTACACSAccClientRoundTripTime,
       "hwTACACSAccClientReqPacket": hwTACACSAccClientReqPacket,
       "hwTACACSAccClientReqNetwork": hwTACACSAccClientReqNetwork,
       "hwTACACSAccClientReqConnection": hwTACACSAccClientReqConnection,
       "hwTACACSAccClientReqEXEC": hwTACACSAccClientReqEXEC,
       "hwTACACSAccClientReqSysEvent": hwTACACSAccClientReqSysEvent,
       "hwTACACSAccClientReqCommandLevel": hwTACACSAccClientReqCommandLevel,
       "hwTACACSAccClientReqUpdate": hwTACACSAccClientReqUpdate,
       "hwTACACSAccClientResPacket": hwTACACSAccClientResPacket,
       "hwTACACSAccClientResError": hwTACACSAccClientResError,
       "hwTACACSAccClientReqPending": hwTACACSAccClientReqPending,
       "hwTACACSAccClientTimeouts": hwTACACSAccClientTimeouts,
       "hwTACACSAccClientUnknownTypes": hwTACACSAccClientUnknownTypes,
       "hwTACACSAccClientPacketsDropped": hwTACACSAccClientPacketsDropped,
       "hwTACACSServerRowStatus": hwTACACSServerRowStatus}
)
