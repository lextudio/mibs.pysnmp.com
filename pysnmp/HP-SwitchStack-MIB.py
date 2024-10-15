# SNMP MIB module (HP-SwitchStack-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SwitchStack-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:06 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpSwitchVirtualStackMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10)
)
hpSwitchVirtualStackMib.setRevisions(
        ("2010-10-29 19:46",
         "2000-11-03 23:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchStackConfig_ObjectIdentity = ObjectIdentity
hpSwitchStackConfig = _HpSwitchStackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1)
)


class _HpSwitchStackAdminStatus_Type(Integer32):
    """Custom type hpSwitchStackAdminStatus based on Integer32"""
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
        *(("candidate", 1),
          ("command", 4),
          ("disabled", 2),
          ("member", 3),
          ("pending", 5))
    )


_HpSwitchStackAdminStatus_Type.__name__ = "Integer32"
_HpSwitchStackAdminStatus_Object = MibScalar
hpSwitchStackAdminStatus = _HpSwitchStackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 1),
    _HpSwitchStackAdminStatus_Type()
)
hpSwitchStackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackAdminStatus.setStatus("current")
_HpSwitchStackCommandAddr_Type = MacAddress
_HpSwitchStackCommandAddr_Object = MibScalar
hpSwitchStackCommandAddr = _HpSwitchStackCommandAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 2),
    _HpSwitchStackCommandAddr_Type()
)
hpSwitchStackCommandAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackCommandAddr.setStatus("current")


class _HpSwitchStackName_Type(OctetString):
    """Custom type hpSwitchStackName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpSwitchStackName_Type.__name__ = "OctetString"
_HpSwitchStackName_Object = MibScalar
hpSwitchStackName = _HpSwitchStackName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 3),
    _HpSwitchStackName_Type()
)
hpSwitchStackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackName.setStatus("current")


class _HpSwitchStackPropagate_Type(Integer32):
    """Custom type hpSwitchStackPropagate based on Integer32"""
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


_HpSwitchStackPropagate_Type.__name__ = "Integer32"
_HpSwitchStackPropagate_Object = MibScalar
hpSwitchStackPropagate = _HpSwitchStackPropagate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 4),
    _HpSwitchStackPropagate_Type()
)
hpSwitchStackPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackPropagate.setStatus("current")


class _HpSwitchStackAutoJoin_Type(Integer32):
    """Custom type hpSwitchStackAutoJoin based on Integer32"""
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


_HpSwitchStackAutoJoin_Type.__name__ = "Integer32"
_HpSwitchStackAutoJoin_Object = MibScalar
hpSwitchStackAutoJoin = _HpSwitchStackAutoJoin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 5),
    _HpSwitchStackAutoJoin_Type()
)
hpSwitchStackAutoJoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackAutoJoin.setStatus("current")


class _HpSwitchStackAutoGrab_Type(Integer32):
    """Custom type hpSwitchStackAutoGrab based on Integer32"""
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


_HpSwitchStackAutoGrab_Type.__name__ = "Integer32"
_HpSwitchStackAutoGrab_Object = MibScalar
hpSwitchStackAutoGrab = _HpSwitchStackAutoGrab_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 1, 6),
    _HpSwitchStackAutoGrab_Type()
)
hpSwitchStackAutoGrab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStackAutoGrab.setStatus("current")
_HpSwitchStackConfigMemberTable_Object = MibTable
hpSwitchStackConfigMemberTable = _HpSwitchStackConfigMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hpSwitchStackConfigMemberTable.setStatus("current")
_HpSwitchStackConfigMemberEntry_Object = MibTableRow
hpSwitchStackConfigMemberEntry = _HpSwitchStackConfigMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1)
)
hpSwitchStackConfigMemberEntry.setIndexNames(
    (0, "HP-SwitchStack-MIB", "hpSwitchStackMemberSwitchNum"),
)
if mibBuilder.loadTexts:
    hpSwitchStackConfigMemberEntry.setStatus("current")


class _HpSwitchStackMemberSwitchNum_Type(Integer32):
    """Custom type hpSwitchStackMemberSwitchNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpSwitchStackMemberSwitchNum_Type.__name__ = "Integer32"
_HpSwitchStackMemberSwitchNum_Object = MibTableColumn
hpSwitchStackMemberSwitchNum = _HpSwitchStackMemberSwitchNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1, 1),
    _HpSwitchStackMemberSwitchNum_Type()
)
hpSwitchStackMemberSwitchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStackMemberSwitchNum.setStatus("current")
_HpSwitchStackMemberMacAddr_Type = MacAddress
_HpSwitchStackMemberMacAddr_Object = MibTableColumn
hpSwitchStackMemberMacAddr = _HpSwitchStackMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1, 2),
    _HpSwitchStackMemberMacAddr_Type()
)
hpSwitchStackMemberMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchStackMemberMacAddr.setStatus("current")


class _HpSwitchStackMemberPassword_Type(OctetString):
    """Custom type hpSwitchStackMemberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_HpSwitchStackMemberPassword_Type.__name__ = "OctetString"
_HpSwitchStackMemberPassword_Object = MibTableColumn
hpSwitchStackMemberPassword = _HpSwitchStackMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1, 3),
    _HpSwitchStackMemberPassword_Type()
)
hpSwitchStackMemberPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchStackMemberPassword.setStatus("deprecated")
_HpSwitchStackMemberEntryStatus_Type = RowStatus
_HpSwitchStackMemberEntryStatus_Object = MibTableColumn
hpSwitchStackMemberEntryStatus = _HpSwitchStackMemberEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1, 4),
    _HpSwitchStackMemberEntryStatus_Type()
)
hpSwitchStackMemberEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchStackMemberEntryStatus.setStatus("current")


class _HpSwitchStackMemberPasswordLong_Type(OctetString):
    """Custom type hpSwitchStackMemberPasswordLong based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )


_HpSwitchStackMemberPasswordLong_Type.__name__ = "OctetString"
_HpSwitchStackMemberPasswordLong_Object = MibTableColumn
hpSwitchStackMemberPasswordLong = _HpSwitchStackMemberPasswordLong_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 2, 1, 5),
    _HpSwitchStackMemberPasswordLong_Type()
)
hpSwitchStackMemberPasswordLong.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchStackMemberPasswordLong.setStatus("current")
_HpStackStats_ObjectIdentity = ObjectIdentity
hpStackStats = _HpStackStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3)
)


class _HpStackStatsName_Type(OctetString):
    """Custom type hpStackStatsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpStackStatsName_Type.__name__ = "OctetString"
_HpStackStatsName_Object = MibScalar
hpStackStatsName = _HpStackStatsName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 1),
    _HpStackStatsName_Type()
)
hpStackStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsName.setStatus("current")


class _HpStackStatsMembersNum_Type(Integer32):
    """Custom type hpStackStatsMembersNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpStackStatsMembersNum_Type.__name__ = "Integer32"
_HpStackStatsMembersNum_Object = MibScalar
hpStackStatsMembersNum = _HpStackStatsMembersNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 2),
    _HpStackStatsMembersNum_Type()
)
hpStackStatsMembersNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMembersNum.setStatus("current")


class _HpStackStatsMembersUnreachable_Type(Integer32):
    """Custom type hpStackStatsMembersUnreachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpStackStatsMembersUnreachable_Type.__name__ = "Integer32"
_HpStackStatsMembersUnreachable_Object = MibScalar
hpStackStatsMembersUnreachable = _HpStackStatsMembersUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 3),
    _HpStackStatsMembersUnreachable_Type()
)
hpStackStatsMembersUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMembersUnreachable.setStatus("current")


class _HpStackStatsMemberID_Type(Integer32):
    """Custom type hpStackStatsMemberID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpStackStatsMemberID_Type.__name__ = "Integer32"
_HpStackStatsMemberID_Object = MibScalar
hpStackStatsMemberID = _HpStackStatsMemberID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 4),
    _HpStackStatsMemberID_Type()
)
hpStackStatsMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberID.setStatus("current")
_HpStackStatsMgmtIpAddr_Type = IpAddress
_HpStackStatsMgmtIpAddr_Object = MibScalar
hpStackStatsMgmtIpAddr = _HpStackStatsMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 5),
    _HpStackStatsMgmtIpAddr_Type()
)
hpStackStatsMgmtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMgmtIpAddr.setStatus("current")


class _HpStackStatsStackingStatus_Type(Integer32):
    """Custom type hpStackStatsStackingStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("commandDown", 10),
          ("commandUp", 9),
          ("evicted", 8),
          ("joined", 1),
          ("noReponse", 3),
          ("notCommand", 4),
          ("pending", 2),
          ("remoteFailure", 6),
          ("stackFull", 5),
          ("undiscovered", 12),
          ("unknownFailure", 7),
          ("unusedStatus", 11))
    )


_HpStackStatsStackingStatus_Type.__name__ = "Integer32"
_HpStackStatsStackingStatus_Object = MibScalar
hpStackStatsStackingStatus = _HpStackStatsStackingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 3, 6),
    _HpStackStatsStackingStatus_Type()
)
hpStackStatsStackingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsStackingStatus.setStatus("current")
_HpStackStatsMembersTable_Object = MibTable
hpStackStatsMembersTable = _HpStackStatsMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4)
)
if mibBuilder.loadTexts:
    hpStackStatsMembersTable.setStatus("current")
_HpStackStatsMemberEntry_Object = MibTableRow
hpStackStatsMemberEntry = _HpStackStatsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1)
)
hpStackStatsMemberEntry.setIndexNames(
    (0, "HP-SwitchStack-MIB", "hpStackStatsMemberSwitchIndx"),
)
if mibBuilder.loadTexts:
    hpStackStatsMemberEntry.setStatus("current")


class _HpStackStatsMemberSwitchIndx_Type(Integer32):
    """Custom type hpStackStatsMemberSwitchIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpStackStatsMemberSwitchIndx_Type.__name__ = "Integer32"
_HpStackStatsMemberSwitchIndx_Object = MibTableColumn
hpStackStatsMemberSwitchIndx = _HpStackStatsMemberSwitchIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1, 1),
    _HpStackStatsMemberSwitchIndx_Type()
)
hpStackStatsMemberSwitchIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberSwitchIndx.setStatus("current")
_HpStackStatsMemberMacAddr_Type = MacAddress
_HpStackStatsMemberMacAddr_Object = MibTableColumn
hpStackStatsMemberMacAddr = _HpStackStatsMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1, 2),
    _HpStackStatsMemberMacAddr_Type()
)
hpStackStatsMemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberMacAddr.setStatus("current")


class _HpStackStatsMemberSystemName_Type(OctetString):
    """Custom type hpStackStatsMemberSystemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpStackStatsMemberSystemName_Type.__name__ = "OctetString"
_HpStackStatsMemberSystemName_Object = MibTableColumn
hpStackStatsMemberSystemName = _HpStackStatsMemberSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1, 3),
    _HpStackStatsMemberSystemName_Type()
)
hpStackStatsMemberSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberSystemName.setStatus("current")


class _HpStackStatsMemberDeviceType_Type(OctetString):
    """Custom type hpStackStatsMemberDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpStackStatsMemberDeviceType_Type.__name__ = "OctetString"
_HpStackStatsMemberDeviceType_Object = MibTableColumn
hpStackStatsMemberDeviceType = _HpStackStatsMemberDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1, 4),
    _HpStackStatsMemberDeviceType_Type()
)
hpStackStatsMemberDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberDeviceType.setStatus("current")


class _HpStackStatsMemberOperStatus_Type(Integer32):
    """Custom type hpStackStatsMemberOperStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("commanderAnotherStack", 6),
          ("commanderThisStack", 12),
          ("invalidPassword", 5),
          ("joined", 2),
          ("memberDown", 11),
          ("memberUp", 10),
          ("noReponse", 3),
          ("pending", 1),
          ("rejected", 9),
          ("remoteFailure", 7),
          ("stackingDisabled", 4),
          ("undiscovered", 14),
          ("unknownFailure", 8),
          ("unusedStatus", 13))
    )


_HpStackStatsMemberOperStatus_Type.__name__ = "Integer32"
_HpStackStatsMemberOperStatus_Object = MibTableColumn
hpStackStatsMemberOperStatus = _HpStackStatsMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 4, 1, 5),
    _HpStackStatsMemberOperStatus_Type()
)
hpStackStatsMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpStackStatsMemberOperStatus.setStatus("current")
_HpSwitchDiscoveryConfig_ObjectIdentity = ObjectIdentity
hpSwitchDiscoveryConfig = _HpSwitchDiscoveryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 5)
)


class _HpSwitchDiscoveryAdminStatus_Type(Integer32):
    """Custom type hpSwitchDiscoveryAdminStatus based on Integer32"""
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


_HpSwitchDiscoveryAdminStatus_Type.__name__ = "Integer32"
_HpSwitchDiscoveryAdminStatus_Object = MibScalar
hpSwitchDiscoveryAdminStatus = _HpSwitchDiscoveryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 5, 1),
    _HpSwitchDiscoveryAdminStatus_Type()
)
hpSwitchDiscoveryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDiscoveryAdminStatus.setStatus("current")


class _HpSwitchDiscoveryTransmissionInterval_Type(Integer32):
    """Custom type hpSwitchDiscoveryTransmissionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HpSwitchDiscoveryTransmissionInterval_Type.__name__ = "Integer32"
_HpSwitchDiscoveryTransmissionInterval_Object = MibScalar
hpSwitchDiscoveryTransmissionInterval = _HpSwitchDiscoveryTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 5, 2),
    _HpSwitchDiscoveryTransmissionInterval_Type()
)
hpSwitchDiscoveryTransmissionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDiscoveryTransmissionInterval.setStatus("current")
_HpDiscoverStatsCandidatesTable_Object = MibTable
hpDiscoverStatsCandidatesTable = _HpDiscoverStatsCandidatesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 6)
)
if mibBuilder.loadTexts:
    hpDiscoverStatsCandidatesTable.setStatus("current")
_HpDiscoverStatsCandidateEntry_Object = MibTableRow
hpDiscoverStatsCandidateEntry = _HpDiscoverStatsCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 6, 1)
)
hpDiscoverStatsCandidateEntry.setIndexNames(
    (0, "HP-SwitchStack-MIB", "hpDiscoverStatsCandidateMacAddr"),
)
if mibBuilder.loadTexts:
    hpDiscoverStatsCandidateEntry.setStatus("current")
_HpDiscoverStatsCandidateMacAddr_Type = MacAddress
_HpDiscoverStatsCandidateMacAddr_Object = MibTableColumn
hpDiscoverStatsCandidateMacAddr = _HpDiscoverStatsCandidateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 6, 1, 1),
    _HpDiscoverStatsCandidateMacAddr_Type()
)
hpDiscoverStatsCandidateMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsCandidateMacAddr.setStatus("current")


class _HpDiscoverStatsCandidateSystemName_Type(OctetString):
    """Custom type hpDiscoverStatsCandidateSystemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpDiscoverStatsCandidateSystemName_Type.__name__ = "OctetString"
_HpDiscoverStatsCandidateSystemName_Object = MibTableColumn
hpDiscoverStatsCandidateSystemName = _HpDiscoverStatsCandidateSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 6, 1, 2),
    _HpDiscoverStatsCandidateSystemName_Type()
)
hpDiscoverStatsCandidateSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsCandidateSystemName.setStatus("current")


class _HpDiscoverStatsCandidateDeviceType_Type(OctetString):
    """Custom type hpDiscoverStatsCandidateDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpDiscoverStatsCandidateDeviceType_Type.__name__ = "OctetString"
_HpDiscoverStatsCandidateDeviceType_Object = MibTableColumn
hpDiscoverStatsCandidateDeviceType = _HpDiscoverStatsCandidateDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 6, 1, 3),
    _HpDiscoverStatsCandidateDeviceType_Type()
)
hpDiscoverStatsCandidateDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsCandidateDeviceType.setStatus("current")
_HpDiscoverStatsTable_Object = MibTable
hpDiscoverStatsTable = _HpDiscoverStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7)
)
if mibBuilder.loadTexts:
    hpDiscoverStatsTable.setStatus("current")
_HpDiscoverStatsEntry_Object = MibTableRow
hpDiscoverStatsEntry = _HpDiscoverStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1)
)
hpDiscoverStatsEntry.setIndexNames(
    (0, "HP-SwitchStack-MIB", "hpDiscoverStatsSwitchIndex"),
)
if mibBuilder.loadTexts:
    hpDiscoverStatsEntry.setStatus("current")


class _HpDiscoverStatsSwitchIndex_Type(Integer32):
    """Custom type hpDiscoverStatsSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpDiscoverStatsSwitchIndex_Type.__name__ = "Integer32"
_HpDiscoverStatsSwitchIndex_Object = MibTableColumn
hpDiscoverStatsSwitchIndex = _HpDiscoverStatsSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1, 1),
    _HpDiscoverStatsSwitchIndex_Type()
)
hpDiscoverStatsSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsSwitchIndex.setStatus("current")


class _HpDiscoverStatsSwitchStackName_Type(OctetString):
    """Custom type hpDiscoverStatsSwitchStackName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpDiscoverStatsSwitchStackName_Type.__name__ = "OctetString"
_HpDiscoverStatsSwitchStackName_Object = MibTableColumn
hpDiscoverStatsSwitchStackName = _HpDiscoverStatsSwitchStackName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1, 2),
    _HpDiscoverStatsSwitchStackName_Type()
)
hpDiscoverStatsSwitchStackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsSwitchStackName.setStatus("current")
_HpDiscoverStatsSwitchMacAddr_Type = MacAddress
_HpDiscoverStatsSwitchMacAddr_Object = MibTableColumn
hpDiscoverStatsSwitchMacAddr = _HpDiscoverStatsSwitchMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1, 3),
    _HpDiscoverStatsSwitchMacAddr_Type()
)
hpDiscoverStatsSwitchMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsSwitchMacAddr.setStatus("current")


class _HpDiscoverStatsSwitchSystemName_Type(OctetString):
    """Custom type hpDiscoverStatsSwitchSystemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpDiscoverStatsSwitchSystemName_Type.__name__ = "OctetString"
_HpDiscoverStatsSwitchSystemName_Object = MibTableColumn
hpDiscoverStatsSwitchSystemName = _HpDiscoverStatsSwitchSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1, 4),
    _HpDiscoverStatsSwitchSystemName_Type()
)
hpDiscoverStatsSwitchSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsSwitchSystemName.setStatus("current")


class _HpDiscoverStatsSwitchStatus_Type(OctetString):
    """Custom type hpDiscoverStatsSwitchStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_HpDiscoverStatsSwitchStatus_Type.__name__ = "OctetString"
_HpDiscoverStatsSwitchStatus_Object = MibTableColumn
hpDiscoverStatsSwitchStatus = _HpDiscoverStatsSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 7, 1, 5),
    _HpDiscoverStatsSwitchStatus_Type()
)
hpDiscoverStatsSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDiscoverStatsSwitchStatus.setStatus("current")
_HpSwitchVirtualStackMibConformance_ObjectIdentity = ObjectIdentity
hpSwitchVirtualStackMibConformance = _HpSwitchVirtualStackMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8)
)
_HpSwitchVirtualStackMibCompliances_ObjectIdentity = ObjectIdentity
hpSwitchVirtualStackMibCompliances = _HpSwitchVirtualStackMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 1)
)
_HpSwitchVirtualStackMibGroups_ObjectIdentity = ObjectIdentity
hpSwitchVirtualStackMibGroups = _HpSwitchVirtualStackMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2)
)

# Managed Objects groups

hpSwitchStackConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2, 1)
)
hpSwitchStackConfigGroup.setObjects(
      *(("HP-SwitchStack-MIB", "hpSwitchStackAdminStatus"),
        ("HP-SwitchStack-MIB", "hpSwitchStackCommandAddr"),
        ("HP-SwitchStack-MIB", "hpSwitchStackName"),
        ("HP-SwitchStack-MIB", "hpSwitchStackPropagate"),
        ("HP-SwitchStack-MIB", "hpSwitchStackAutoJoin"),
        ("HP-SwitchStack-MIB", "hpSwitchStackAutoGrab"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberSwitchNum"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberMacAddr"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberPassword"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberEntryStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchStackConfigGroup.setStatus("deprecated")

hpSwitchStackStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2, 2)
)
hpSwitchStackStatsGroup.setObjects(
      *(("HP-SwitchStack-MIB", "hpStackStatsName"),
        ("HP-SwitchStack-MIB", "hpStackStatsMembersNum"),
        ("HP-SwitchStack-MIB", "hpStackStatsMembersUnreachable"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberID"),
        ("HP-SwitchStack-MIB", "hpStackStatsMgmtIpAddr"),
        ("HP-SwitchStack-MIB", "hpStackStatsStackingStatus"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberSwitchIndx"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberMacAddr"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberSystemName"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberDeviceType"),
        ("HP-SwitchStack-MIB", "hpStackStatsMemberOperStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchStackStatsGroup.setStatus("current")

hpSwitchDiscoverConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2, 3)
)
hpSwitchDiscoverConfigGroup.setObjects(
      *(("HP-SwitchStack-MIB", "hpSwitchDiscoveryAdminStatus"),
        ("HP-SwitchStack-MIB", "hpSwitchDiscoveryTransmissionInterval"))
)
if mibBuilder.loadTexts:
    hpSwitchDiscoverConfigGroup.setStatus("current")

hpDiscoverStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2, 4)
)
hpDiscoverStatsGroup.setObjects(
      *(("HP-SwitchStack-MIB", "hpDiscoverStatsCandidateMacAddr"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsCandidateSystemName"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsCandidateDeviceType"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsSwitchIndex"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsSwitchStackName"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsSwitchMacAddr"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsSwitchSystemName"),
        ("HP-SwitchStack-MIB", "hpDiscoverStatsSwitchStatus"))
)
if mibBuilder.loadTexts:
    hpDiscoverStatsGroup.setStatus("current")

hpSwitchStackConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 2, 5)
)
hpSwitchStackConfigGroup1.setObjects(
      *(("HP-SwitchStack-MIB", "hpSwitchStackAdminStatus"),
        ("HP-SwitchStack-MIB", "hpSwitchStackCommandAddr"),
        ("HP-SwitchStack-MIB", "hpSwitchStackName"),
        ("HP-SwitchStack-MIB", "hpSwitchStackPropagate"),
        ("HP-SwitchStack-MIB", "hpSwitchStackAutoJoin"),
        ("HP-SwitchStack-MIB", "hpSwitchStackAutoGrab"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberSwitchNum"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberMacAddr"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberPasswordLong"),
        ("HP-SwitchStack-MIB", "hpSwitchStackMemberEntryStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchStackConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchVirtualStackMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchVirtualStackMibCompliance.setStatus(
        "deprecated"
    )

hpSwitchVirtualStackMibCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchVirtualStackMibCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SwitchStack-MIB",
    **{"hpSwitchVirtualStackMib": hpSwitchVirtualStackMib,
       "hpSwitchStackConfig": hpSwitchStackConfig,
       "hpSwitchStackAdminStatus": hpSwitchStackAdminStatus,
       "hpSwitchStackCommandAddr": hpSwitchStackCommandAddr,
       "hpSwitchStackName": hpSwitchStackName,
       "hpSwitchStackPropagate": hpSwitchStackPropagate,
       "hpSwitchStackAutoJoin": hpSwitchStackAutoJoin,
       "hpSwitchStackAutoGrab": hpSwitchStackAutoGrab,
       "hpSwitchStackConfigMemberTable": hpSwitchStackConfigMemberTable,
       "hpSwitchStackConfigMemberEntry": hpSwitchStackConfigMemberEntry,
       "hpSwitchStackMemberSwitchNum": hpSwitchStackMemberSwitchNum,
       "hpSwitchStackMemberMacAddr": hpSwitchStackMemberMacAddr,
       "hpSwitchStackMemberPassword": hpSwitchStackMemberPassword,
       "hpSwitchStackMemberEntryStatus": hpSwitchStackMemberEntryStatus,
       "hpSwitchStackMemberPasswordLong": hpSwitchStackMemberPasswordLong,
       "hpStackStats": hpStackStats,
       "hpStackStatsName": hpStackStatsName,
       "hpStackStatsMembersNum": hpStackStatsMembersNum,
       "hpStackStatsMembersUnreachable": hpStackStatsMembersUnreachable,
       "hpStackStatsMemberID": hpStackStatsMemberID,
       "hpStackStatsMgmtIpAddr": hpStackStatsMgmtIpAddr,
       "hpStackStatsStackingStatus": hpStackStatsStackingStatus,
       "hpStackStatsMembersTable": hpStackStatsMembersTable,
       "hpStackStatsMemberEntry": hpStackStatsMemberEntry,
       "hpStackStatsMemberSwitchIndx": hpStackStatsMemberSwitchIndx,
       "hpStackStatsMemberMacAddr": hpStackStatsMemberMacAddr,
       "hpStackStatsMemberSystemName": hpStackStatsMemberSystemName,
       "hpStackStatsMemberDeviceType": hpStackStatsMemberDeviceType,
       "hpStackStatsMemberOperStatus": hpStackStatsMemberOperStatus,
       "hpSwitchDiscoveryConfig": hpSwitchDiscoveryConfig,
       "hpSwitchDiscoveryAdminStatus": hpSwitchDiscoveryAdminStatus,
       "hpSwitchDiscoveryTransmissionInterval": hpSwitchDiscoveryTransmissionInterval,
       "hpDiscoverStatsCandidatesTable": hpDiscoverStatsCandidatesTable,
       "hpDiscoverStatsCandidateEntry": hpDiscoverStatsCandidateEntry,
       "hpDiscoverStatsCandidateMacAddr": hpDiscoverStatsCandidateMacAddr,
       "hpDiscoverStatsCandidateSystemName": hpDiscoverStatsCandidateSystemName,
       "hpDiscoverStatsCandidateDeviceType": hpDiscoverStatsCandidateDeviceType,
       "hpDiscoverStatsTable": hpDiscoverStatsTable,
       "hpDiscoverStatsEntry": hpDiscoverStatsEntry,
       "hpDiscoverStatsSwitchIndex": hpDiscoverStatsSwitchIndex,
       "hpDiscoverStatsSwitchStackName": hpDiscoverStatsSwitchStackName,
       "hpDiscoverStatsSwitchMacAddr": hpDiscoverStatsSwitchMacAddr,
       "hpDiscoverStatsSwitchSystemName": hpDiscoverStatsSwitchSystemName,
       "hpDiscoverStatsSwitchStatus": hpDiscoverStatsSwitchStatus,
       "hpSwitchVirtualStackMibConformance": hpSwitchVirtualStackMibConformance,
       "hpSwitchVirtualStackMibCompliances": hpSwitchVirtualStackMibCompliances,
       "hpSwitchVirtualStackMibCompliance": hpSwitchVirtualStackMibCompliance,
       "hpSwitchVirtualStackMibCompliance1": hpSwitchVirtualStackMibCompliance1,
       "hpSwitchVirtualStackMibGroups": hpSwitchVirtualStackMibGroups,
       "hpSwitchStackConfigGroup": hpSwitchStackConfigGroup,
       "hpSwitchStackStatsGroup": hpSwitchStackStatsGroup,
       "hpSwitchDiscoverConfigGroup": hpSwitchDiscoverConfigGroup,
       "hpDiscoverStatsGroup": hpDiscoverStatsGroup,
       "hpSwitchStackConfigGroup1": hpSwitchStackConfigGroup1}
)
