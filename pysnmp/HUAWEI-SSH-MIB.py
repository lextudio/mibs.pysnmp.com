# SNMP MIB module (HUAWEI-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:00 2024
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

hwSSH = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118)
)
hwSSH.setRevisions(
        ("2014-09-26 00:00",
         "2014-06-30 00:00",
         "2014-05-06 00:00",
         "2010-11-09 00:00",
         "2010-08-25 00:00",
         "2010-06-17 00:00",
         "2010-04-18 00:00",
         "2010-03-03 00:00",
         "2010-01-29 00:00",
         "2006-09-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSSHServer_ObjectIdentity = ObjectIdentity
hwSSHServer = _HwSSHServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1)
)


class _HwStelnetServerEnable_Type(Integer32):
    """Custom type hwStelnetServerEnable based on Integer32"""
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


_HwStelnetServerEnable_Type.__name__ = "Integer32"
_HwStelnetServerEnable_Object = MibScalar
hwStelnetServerEnable = _HwStelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 1),
    _HwStelnetServerEnable_Type()
)
hwStelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStelnetServerEnable.setStatus("current")


class _HwSftpServerEnable_Type(Integer32):
    """Custom type hwSftpServerEnable based on Integer32"""
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


_HwSftpServerEnable_Type.__name__ = "Integer32"
_HwSftpServerEnable_Object = MibScalar
hwSftpServerEnable = _HwSftpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 2),
    _HwSftpServerEnable_Type()
)
hwSftpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSftpServerEnable.setStatus("current")


class _HwSSHServerComp1x_Type(Integer32):
    """Custom type hwSSHServerComp1x based on Integer32"""
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


_HwSSHServerComp1x_Type.__name__ = "Integer32"
_HwSSHServerComp1x_Object = MibScalar
hwSSHServerComp1x = _HwSSHServerComp1x_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 3),
    _HwSSHServerComp1x_Type()
)
hwSSHServerComp1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerComp1x.setStatus("current")


class _HwSSHServerTimeOut_Type(Integer32):
    """Custom type hwSSHServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwSSHServerTimeOut_Type.__name__ = "Integer32"
_HwSSHServerTimeOut_Object = MibScalar
hwSSHServerTimeOut = _HwSSHServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 4),
    _HwSSHServerTimeOut_Type()
)
hwSSHServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hwSSHServerTimeOut.setUnits("second")


class _HwSSHServerRetry_Type(Integer32):
    """Custom type hwSSHServerRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwSSHServerRetry_Type.__name__ = "Integer32"
_HwSSHServerRetry_Object = MibScalar
hwSSHServerRetry = _HwSSHServerRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 5),
    _HwSSHServerRetry_Type()
)
hwSSHServerRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerRetry.setStatus("current")


class _HwSSHServerPort_Type(Integer32):
    """Custom type hwSSHServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 22),
        ValueRangeConstraint(1025, 65535),
    )


_HwSSHServerPort_Type.__name__ = "Integer32"
_HwSSHServerPort_Object = MibScalar
hwSSHServerPort = _HwSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 6),
    _HwSSHServerPort_Type()
)
hwSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerPort.setStatus("current")


class _HwSSHServerKeyTimeOut_Type(Integer32):
    """Custom type hwSSHServerKeyTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_HwSSHServerKeyTimeOut_Type.__name__ = "Integer32"
_HwSSHServerKeyTimeOut_Object = MibScalar
hwSSHServerKeyTimeOut = _HwSSHServerKeyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 7),
    _HwSSHServerKeyTimeOut_Type()
)
hwSSHServerKeyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerKeyTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hwSSHServerKeyTimeOut.setUnits("hour")


class _HwSSHServerAlarmEnable_Type(Integer32):
    """Custom type hwSSHServerAlarmEnable based on Integer32"""
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


_HwSSHServerAlarmEnable_Type.__name__ = "Integer32"
_HwSSHServerAlarmEnable_Object = MibScalar
hwSSHServerAlarmEnable = _HwSSHServerAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 8),
    _HwSSHServerAlarmEnable_Type()
)
hwSSHServerAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHServerAlarmEnable.setStatus("current")


class _HwSftpMaxUserNum_Type(Integer32):
    """Custom type hwSftpMaxUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwSftpMaxUserNum_Type.__name__ = "Integer32"
_HwSftpMaxUserNum_Object = MibScalar
hwSftpMaxUserNum = _HwSftpMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 9),
    _HwSftpMaxUserNum_Type()
)
hwSftpMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSftpMaxUserNum.setStatus("current")
_HwSftpOnLineUserNum_Type = Integer32
_HwSftpOnLineUserNum_Object = MibScalar
hwSftpOnLineUserNum = _HwSftpOnLineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 10),
    _HwSftpOnLineUserNum_Type()
)
hwSftpOnLineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSftpOnLineUserNum.setStatus("current")
_HwSSHUserTable_Object = MibTable
hwSSHUserTable = _HwSSHUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11)
)
if mibBuilder.loadTexts:
    hwSSHUserTable.setStatus("current")
_HwSSHUserEntry_Object = MibTableRow
hwSSHUserEntry = _HwSSHUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1)
)
hwSSHUserEntry.setIndexNames(
    (0, "HUAWEI-SSH-MIB", "hwSSHUserIndex"),
)
if mibBuilder.loadTexts:
    hwSSHUserEntry.setStatus("current")


class _HwSSHUserIndex_Type(Integer32):
    """Custom type hwSSHUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HwSSHUserIndex_Type.__name__ = "Integer32"
_HwSSHUserIndex_Object = MibTableColumn
hwSSHUserIndex = _HwSSHUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 1),
    _HwSSHUserIndex_Type()
)
hwSSHUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSSHUserIndex.setStatus("current")


class _HwSSHUserName_Type(OctetString):
    """Custom type hwSSHUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSSHUserName_Type.__name__ = "OctetString"
_HwSSHUserName_Object = MibTableColumn
hwSSHUserName = _HwSSHUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 2),
    _HwSSHUserName_Type()
)
hwSSHUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserName.setStatus("current")


class _HwSSHUserAssignKey_Type(OctetString):
    """Custom type hwSSHUserAssignKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSSHUserAssignKey_Type.__name__ = "OctetString"
_HwSSHUserAssignKey_Object = MibTableColumn
hwSSHUserAssignKey = _HwSSHUserAssignKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 3),
    _HwSSHUserAssignKey_Type()
)
hwSSHUserAssignKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserAssignKey.setStatus("current")


class _HwSSHUserAuthType_Type(Integer32):
    """Custom type hwSSHUserAuthType based on Integer32"""
    defaultValue = 2

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("authAny", 8),
          ("authDSA", 6),
          ("authDSAandPASSWORD", 7),
          ("authECC", 9),
          ("authECCandPASSWORD", 10),
          ("authNULL", 1),
          ("authPASSWORD", 2),
          ("authRSA", 3),
          ("authRSAandPASSWORD", 5),
          ("authRSAorPASSWORD", 4))
    )


_HwSSHUserAuthType_Type.__name__ = "Integer32"
_HwSSHUserAuthType_Object = MibTableColumn
hwSSHUserAuthType = _HwSSHUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 4),
    _HwSSHUserAuthType_Type()
)
hwSSHUserAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserAuthType.setStatus("current")


class _HwSSHUserServiceType_Type(Integer32):
    """Custom type hwSSHUserServiceType based on Integer32"""
    defaultValue = 1

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
        *(("servicetypeALL", 4),
          ("servicetypeNULL", 1),
          ("servicetypeSFTP", 3),
          ("servicetypeSNetConf", 5),
          ("servicetypeSTELNET", 2),
          ("servicetypeSTelnetSNetConf", 8),
          ("servicetypeSTelnetSftp", 7),
          ("servicetypeSftpSNetConf", 6))
    )


_HwSSHUserServiceType_Type.__name__ = "Integer32"
_HwSSHUserServiceType_Object = MibTableColumn
hwSSHUserServiceType = _HwSSHUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 5),
    _HwSSHUserServiceType_Type()
)
hwSSHUserServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserServiceType.setStatus("current")


class _HwSSHUserSftpDirectory_Type(OctetString):
    """Custom type hwSSHUserSftpDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSSHUserSftpDirectory_Type.__name__ = "OctetString"
_HwSSHUserSftpDirectory_Object = MibTableColumn
hwSSHUserSftpDirectory = _HwSSHUserSftpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 6),
    _HwSSHUserSftpDirectory_Type()
)
hwSSHUserSftpDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserSftpDirectory.setStatus("current")


class _HwSSHUserAuthorizationCMD_Type(Integer32):
    """Custom type hwSSHUserAuthorizationCMD based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorizationAAA", 2),
          ("authorizationNULL", 1))
    )


_HwSSHUserAuthorizationCMD_Type.__name__ = "Integer32"
_HwSSHUserAuthorizationCMD_Object = MibTableColumn
hwSSHUserAuthorizationCMD = _HwSSHUserAuthorizationCMD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 7),
    _HwSSHUserAuthorizationCMD_Type()
)
hwSSHUserAuthorizationCMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserAuthorizationCMD.setStatus("current")
_HwSSHUserRowStatus_Type = RowStatus
_HwSSHUserRowStatus_Object = MibTableColumn
hwSSHUserRowStatus = _HwSSHUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 8),
    _HwSSHUserRowStatus_Type()
)
hwSSHUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserRowStatus.setStatus("current")


class _HwSSHUserAssignKeyType_Type(Integer32):
    """Custom type hwSSHUserAssignKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keyTypeDSA", 2),
          ("keyTypeECC", 3),
          ("keyTypeNULL", 0),
          ("keyTypeRSA", 1))
    )


_HwSSHUserAssignKeyType_Type.__name__ = "Integer32"
_HwSSHUserAssignKeyType_Object = MibTableColumn
hwSSHUserAssignKeyType = _HwSSHUserAssignKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 9),
    _HwSSHUserAssignKeyType_Type()
)
hwSSHUserAssignKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHUserAssignKeyType.setStatus("current")
_HwSSHServerSessionTable_Object = MibTable
hwSSHServerSessionTable = _HwSSHServerSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12)
)
if mibBuilder.loadTexts:
    hwSSHServerSessionTable.setStatus("current")
_HwSSHServerSessionEntry_Object = MibTableRow
hwSSHServerSessionEntry = _HwSSHServerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1)
)
hwSSHServerSessionEntry.setIndexNames(
    (0, "HUAWEI-SSH-MIB", "hwSSHSessionIndex"),
)
if mibBuilder.loadTexts:
    hwSSHServerSessionEntry.setStatus("current")
_HwSSHSessionIndex_Type = Integer32
_HwSSHSessionIndex_Object = MibTableColumn
hwSSHSessionIndex = _HwSSHSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 1),
    _HwSSHSessionIndex_Type()
)
hwSSHSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSSHSessionIndex.setStatus("current")
_HwSSHSessionUserName_Type = DisplayString
_HwSSHSessionUserName_Object = MibTableColumn
hwSSHSessionUserName = _HwSSHSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 2),
    _HwSSHSessionUserName_Type()
)
hwSSHSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionUserName.setStatus("current")


class _HwSSHSessionConnectType_Type(Integer32):
    """Custom type hwSSHSessionConnectType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vty0", 1),
          ("vty1", 2),
          ("vty10", 11),
          ("vty11", 12),
          ("vty12", 13),
          ("vty13", 14),
          ("vty14", 15),
          ("vty15", 16),
          ("vty16", 17),
          ("vty17", 18),
          ("vty18", 19),
          ("vty19", 20),
          ("vty2", 3),
          ("vty20", 21),
          ("vty3", 4),
          ("vty4", 5),
          ("vty5", 6),
          ("vty6", 7),
          ("vty7", 8),
          ("vty8", 9),
          ("vty9", 10))
    )


_HwSSHSessionConnectType_Type.__name__ = "Integer32"
_HwSSHSessionConnectType_Object = MibTableColumn
hwSSHSessionConnectType = _HwSSHSessionConnectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 3),
    _HwSSHSessionConnectType_Type()
)
hwSSHSessionConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionConnectType.setStatus("current")
_HwSSHSessionVer_Type = DisplayString
_HwSSHSessionVer_Object = MibTableColumn
hwSSHSessionVer = _HwSSHSessionVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 4),
    _HwSSHSessionVer_Type()
)
hwSSHSessionVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionVer.setStatus("current")


class _HwSSHSessionState_Type(Integer32):
    """Custom type hwSSHSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("started", 1)
    )


_HwSSHSessionState_Type.__name__ = "Integer32"
_HwSSHSessionState_Object = MibTableColumn
hwSSHSessionState = _HwSSHSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 5),
    _HwSSHSessionState_Type()
)
hwSSHSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionState.setStatus("current")


class _HwSSHSessionRetry_Type(Integer32):
    """Custom type hwSSHSessionRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwSSHSessionRetry_Type.__name__ = "Integer32"
_HwSSHSessionRetry_Object = MibTableColumn
hwSSHSessionRetry = _HwSSHSessionRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 6),
    _HwSSHSessionRetry_Type()
)
hwSSHSessionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionRetry.setStatus("current")
_HwSSHSessionCtosCipher_Type = DisplayString
_HwSSHSessionCtosCipher_Object = MibTableColumn
hwSSHSessionCtosCipher = _HwSSHSessionCtosCipher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 7),
    _HwSSHSessionCtosCipher_Type()
)
hwSSHSessionCtosCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionCtosCipher.setStatus("current")
_HwSSHSessionStocCipher_Type = DisplayString
_HwSSHSessionStocCipher_Object = MibTableColumn
hwSSHSessionStocCipher = _HwSSHSessionStocCipher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 8),
    _HwSSHSessionStocCipher_Type()
)
hwSSHSessionStocCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionStocCipher.setStatus("current")
_HwSSHSessionCtosHmac_Type = DisplayString
_HwSSHSessionCtosHmac_Object = MibTableColumn
hwSSHSessionCtosHmac = _HwSSHSessionCtosHmac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 9),
    _HwSSHSessionCtosHmac_Type()
)
hwSSHSessionCtosHmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionCtosHmac.setStatus("current")
_HwSSHSessionStocHmac_Type = DisplayString
_HwSSHSessionStocHmac_Object = MibTableColumn
hwSSHSessionStocHmac = _HwSSHSessionStocHmac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 10),
    _HwSSHSessionStocHmac_Type()
)
hwSSHSessionStocHmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionStocHmac.setStatus("current")
_HwSSHSessionKex_Type = DisplayString
_HwSSHSessionKex_Object = MibTableColumn
hwSSHSessionKex = _HwSSHSessionKex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 11),
    _HwSSHSessionKex_Type()
)
hwSSHSessionKex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionKex.setStatus("current")
_HwSSHSessionAuthType_Type = DisplayString
_HwSSHSessionAuthType_Object = MibTableColumn
hwSSHSessionAuthType = _HwSSHSessionAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 12),
    _HwSSHSessionAuthType_Type()
)
hwSSHSessionAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionAuthType.setStatus("current")
_HwSSHSessionServiceType_Type = DisplayString
_HwSSHSessionServiceType_Object = MibTableColumn
hwSSHSessionServiceType = _HwSSHSessionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 13),
    _HwSSHSessionServiceType_Type()
)
hwSSHSessionServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionServiceType.setStatus("current")


class _HwSSHSessionKeyType_Type(Integer32):
    """Custom type hwSSHSessionKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keyTypeDSA", 2),
          ("keyTypeECC", 3),
          ("keyTypeRSA", 1))
    )


_HwSSHSessionKeyType_Type.__name__ = "Integer32"
_HwSSHSessionKeyType_Object = MibTableColumn
hwSSHSessionKeyType = _HwSSHSessionKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 14),
    _HwSSHSessionKeyType_Type()
)
hwSSHSessionKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionKeyType.setStatus("current")
_HwSSHSessionConnectionIndex_Type = Integer32
_HwSSHSessionConnectionIndex_Object = MibTableColumn
hwSSHSessionConnectionIndex = _HwSSHSessionConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 15),
    _HwSSHSessionConnectionIndex_Type()
)
hwSSHSessionConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionConnectionIndex.setStatus("current")
_HwSSHSessionCtosCompress_Type = DisplayString
_HwSSHSessionCtosCompress_Object = MibTableColumn
hwSSHSessionCtosCompress = _HwSSHSessionCtosCompress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 16),
    _HwSSHSessionCtosCompress_Type()
)
hwSSHSessionCtosCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionCtosCompress.setStatus("current")
_HwSSHSessionStocCompress_Type = DisplayString
_HwSSHSessionStocCompress_Object = MibTableColumn
hwSSHSessionStocCompress = _HwSSHSessionStocCompress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 17),
    _HwSSHSessionStocCompress_Type()
)
hwSSHSessionStocCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSSHSessionStocCompress.setStatus("current")
_HwRSAPublicKeyTable_Object = MibTable
hwRSAPublicKeyTable = _HwRSAPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13)
)
if mibBuilder.loadTexts:
    hwRSAPublicKeyTable.setStatus("current")
_HwRSAPublicKeyEntry_Object = MibTableRow
hwRSAPublicKeyEntry = _HwRSAPublicKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1)
)
hwRSAPublicKeyEntry.setIndexNames(
    (0, "HUAWEI-SSH-MIB", "hwRSAPublicKeyName"),
)
if mibBuilder.loadTexts:
    hwRSAPublicKeyEntry.setStatus("current")


class _HwRSAPublicKeyName_Type(OctetString):
    """Custom type hwRSAPublicKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwRSAPublicKeyName_Type.__name__ = "OctetString"
_HwRSAPublicKeyName_Object = MibTableColumn
hwRSAPublicKeyName = _HwRSAPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 1),
    _HwRSAPublicKeyName_Type()
)
hwRSAPublicKeyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRSAPublicKeyName.setStatus("current")


class _HwRSAPublicKeyCode_Type(OctetString):
    """Custom type hwRSAPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_HwRSAPublicKeyCode_Type.__name__ = "OctetString"
_HwRSAPublicKeyCode_Object = MibTableColumn
hwRSAPublicKeyCode = _HwRSAPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 2),
    _HwRSAPublicKeyCode_Type()
)
hwRSAPublicKeyCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRSAPublicKeyCode.setStatus("current")
_HwRSAPublicKeyRowStatus_Type = RowStatus
_HwRSAPublicKeyRowStatus_Object = MibTableColumn
hwRSAPublicKeyRowStatus = _HwRSAPublicKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 3),
    _HwRSAPublicKeyRowStatus_Type()
)
hwRSAPublicKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRSAPublicKeyRowStatus.setStatus("current")


class _HwRSAPublicKeyFingerprint_Type(OctetString):
    """Custom type hwRSAPublicKeyFingerprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_HwRSAPublicKeyFingerprint_Type.__name__ = "OctetString"
_HwRSAPublicKeyFingerprint_Object = MibTableColumn
hwRSAPublicKeyFingerprint = _HwRSAPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 4),
    _HwRSAPublicKeyFingerprint_Type()
)
hwRSAPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRSAPublicKeyFingerprint.setStatus("current")


class _HwSNetConfMaxUserNum_Type(Integer32):
    """Custom type hwSNetConfMaxUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwSNetConfMaxUserNum_Type.__name__ = "Integer32"
_HwSNetConfMaxUserNum_Object = MibScalar
hwSNetConfMaxUserNum = _HwSNetConfMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 14),
    _HwSNetConfMaxUserNum_Type()
)
hwSNetConfMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSNetConfMaxUserNum.setStatus("current")


class _HwSNetConfServerEnable_Type(Integer32):
    """Custom type hwSNetConfServerEnable based on Integer32"""
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


_HwSNetConfServerEnable_Type.__name__ = "Integer32"
_HwSNetConfServerEnable_Object = MibScalar
hwSNetConfServerEnable = _HwSNetConfServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 15),
    _HwSNetConfServerEnable_Type()
)
hwSNetConfServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSNetConfServerEnable.setStatus("current")


class _HwSSHKeepAliveEnable_Type(Integer32):
    """Custom type hwSSHKeepAliveEnable based on Integer32"""
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


_HwSSHKeepAliveEnable_Type.__name__ = "Integer32"
_HwSSHKeepAliveEnable_Object = MibScalar
hwSSHKeepAliveEnable = _HwSSHKeepAliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 16),
    _HwSSHKeepAliveEnable_Type()
)
hwSSHKeepAliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHKeepAliveEnable.setStatus("current")


class _HwSCPServerEnable_Type(Integer32):
    """Custom type hwSCPServerEnable based on Integer32"""
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


_HwSCPServerEnable_Type.__name__ = "Integer32"
_HwSCPServerEnable_Object = MibScalar
hwSCPServerEnable = _HwSCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 17),
    _HwSCPServerEnable_Type()
)
hwSCPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSCPServerEnable.setStatus("current")


class _HwSCPMaxUserNum_Type(Integer32):
    """Custom type hwSCPMaxUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwSCPMaxUserNum_Type.__name__ = "Integer32"
_HwSCPMaxUserNum_Object = MibScalar
hwSCPMaxUserNum = _HwSCPMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 18),
    _HwSCPMaxUserNum_Type()
)
hwSCPMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSCPMaxUserNum.setStatus("current")
_HwSSHClient_ObjectIdentity = ObjectIdentity
hwSSHClient = _HwSSHClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2)
)


class _HwSSHFirstTimeAuthEnable_Type(Integer32):
    """Custom type hwSSHFirstTimeAuthEnable based on Integer32"""
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


_HwSSHFirstTimeAuthEnable_Type.__name__ = "Integer32"
_HwSSHFirstTimeAuthEnable_Object = MibScalar
hwSSHFirstTimeAuthEnable = _HwSSHFirstTimeAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 1),
    _HwSSHFirstTimeAuthEnable_Type()
)
hwSSHFirstTimeAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHFirstTimeAuthEnable.setStatus("current")
_HwSSHServerInfoTable_Object = MibTable
hwSSHServerInfoTable = _HwSSHServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2)
)
if mibBuilder.loadTexts:
    hwSSHServerInfoTable.setStatus("current")
_HwSSHServerInfoEntry_Object = MibTableRow
hwSSHServerInfoEntry = _HwSSHServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1)
)
hwSSHServerInfoEntry.setIndexNames(
    (0, "HUAWEI-SSH-MIB", "hwSSHServerIndex"),
)
if mibBuilder.loadTexts:
    hwSSHServerInfoEntry.setStatus("current")


class _HwSSHServerIndex_Type(Integer32):
    """Custom type hwSSHServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwSSHServerIndex_Type.__name__ = "Integer32"
_HwSSHServerIndex_Object = MibTableColumn
hwSSHServerIndex = _HwSSHServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 1),
    _HwSSHServerIndex_Type()
)
hwSSHServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSSHServerIndex.setStatus("current")


class _HwSSHServerName_Type(OctetString):
    """Custom type hwSSHServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSSHServerName_Type.__name__ = "OctetString"
_HwSSHServerName_Object = MibTableColumn
hwSSHServerName = _HwSSHServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 2),
    _HwSSHServerName_Type()
)
hwSSHServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHServerName.setStatus("current")


class _HwSSHServerAssignKey_Type(OctetString):
    """Custom type hwSSHServerAssignKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSSHServerAssignKey_Type.__name__ = "OctetString"
_HwSSHServerAssignKey_Object = MibTableColumn
hwSSHServerAssignKey = _HwSSHServerAssignKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 3),
    _HwSSHServerAssignKey_Type()
)
hwSSHServerAssignKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHServerAssignKey.setStatus("current")
_HwSSHServerRowStatus_Type = RowStatus
_HwSSHServerRowStatus_Object = MibTableColumn
hwSSHServerRowStatus = _HwSSHServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 4),
    _HwSSHServerRowStatus_Type()
)
hwSSHServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHServerRowStatus.setStatus("current")


class _HwSSHServerAssignDSAKey_Type(OctetString):
    """Custom type hwSSHServerAssignDSAKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSSHServerAssignDSAKey_Type.__name__ = "OctetString"
_HwSSHServerAssignDSAKey_Object = MibTableColumn
hwSSHServerAssignDSAKey = _HwSSHServerAssignDSAKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 5),
    _HwSSHServerAssignDSAKey_Type()
)
hwSSHServerAssignDSAKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHServerAssignDSAKey.setStatus("current")


class _HwSSHServerAssignECCKey_Type(OctetString):
    """Custom type hwSSHServerAssignECCKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSSHServerAssignECCKey_Type.__name__ = "OctetString"
_HwSSHServerAssignECCKey_Object = MibTableColumn
hwSSHServerAssignECCKey = _HwSSHServerAssignECCKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 6),
    _HwSSHServerAssignECCKey_Type()
)
hwSSHServerAssignECCKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSSHServerAssignECCKey.setStatus("current")


class _HwSSHKeepAliveInterval_Type(Integer32):
    """Custom type hwSSHKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HwSSHKeepAliveInterval_Type.__name__ = "Integer32"
_HwSSHKeepAliveInterval_Object = MibScalar
hwSSHKeepAliveInterval = _HwSSHKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 3),
    _HwSSHKeepAliveInterval_Type()
)
hwSSHKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHKeepAliveInterval.setStatus("current")


class _HwSSHKeepAliveMaxCount_Type(Integer32):
    """Custom type hwSSHKeepAliveMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HwSSHKeepAliveMaxCount_Type.__name__ = "Integer32"
_HwSSHKeepAliveMaxCount_Object = MibScalar
hwSSHKeepAliveMaxCount = _HwSSHKeepAliveMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 4),
    _HwSSHKeepAliveMaxCount_Type()
)
hwSSHKeepAliveMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSSHKeepAliveMaxCount.setStatus("current")
_HwSSHNotifications_ObjectIdentity = ObjectIdentity
hwSSHNotifications = _HwSSHNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 3)
)
_HwSSHMIBConformance_ObjectIdentity = ObjectIdentity
hwSSHMIBConformance = _HwSSHMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4)
)
_HwSSHMIBCompliances_ObjectIdentity = ObjectIdentity
hwSSHMIBCompliances = _HwSSHMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 1)
)
_HwSSHMIBGroups_ObjectIdentity = ObjectIdentity
hwSSHMIBGroups = _HwSSHMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2)
)
_HwRSALocalKeyTable_ObjectIdentity = ObjectIdentity
hwRSALocalKeyTable = _HwRSALocalKeyTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5)
)


class _HwRSALocalHostPublicKeyCode_Type(OctetString):
    """Custom type hwRSALocalHostPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_HwRSALocalHostPublicKeyCode_Type.__name__ = "OctetString"
_HwRSALocalHostPublicKeyCode_Object = MibScalar
hwRSALocalHostPublicKeyCode = _HwRSALocalHostPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 1),
    _HwRSALocalHostPublicKeyCode_Type()
)
hwRSALocalHostPublicKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRSALocalHostPublicKeyCode.setStatus("current")


class _HwRSALocalHostPublicKeyFingerprint_Type(OctetString):
    """Custom type hwRSALocalHostPublicKeyFingerprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_HwRSALocalHostPublicKeyFingerprint_Type.__name__ = "OctetString"
_HwRSALocalHostPublicKeyFingerprint_Object = MibScalar
hwRSALocalHostPublicKeyFingerprint = _HwRSALocalHostPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 2),
    _HwRSALocalHostPublicKeyFingerprint_Type()
)
hwRSALocalHostPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRSALocalHostPublicKeyFingerprint.setStatus("current")


class _HwRSALocalServerPublicKeyCode_Type(OctetString):
    """Custom type hwRSALocalServerPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_HwRSALocalServerPublicKeyCode_Type.__name__ = "OctetString"
_HwRSALocalServerPublicKeyCode_Object = MibScalar
hwRSALocalServerPublicKeyCode = _HwRSALocalServerPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 3),
    _HwRSALocalServerPublicKeyCode_Type()
)
hwRSALocalServerPublicKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRSALocalServerPublicKeyCode.setStatus("current")


class _HwRSALocalServerPublicKeyFingerprint_Type(OctetString):
    """Custom type hwRSALocalServerPublicKeyFingerprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_HwRSALocalServerPublicKeyFingerprint_Type.__name__ = "OctetString"
_HwRSALocalServerPublicKeyFingerprint_Object = MibScalar
hwRSALocalServerPublicKeyFingerprint = _HwRSALocalServerPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 4),
    _HwRSALocalServerPublicKeyFingerprint_Type()
)
hwRSALocalServerPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRSALocalServerPublicKeyFingerprint.setStatus("current")

# Managed Objects groups

hwSSHServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 1)
)
hwSSHServerGroup.setObjects(
      *(("HUAWEI-SSH-MIB", "hwStelnetServerEnable"),
        ("HUAWEI-SSH-MIB", "hwSftpServerEnable"),
        ("HUAWEI-SSH-MIB", "hwSSHServerComp1x"),
        ("HUAWEI-SSH-MIB", "hwSSHServerTimeOut"),
        ("HUAWEI-SSH-MIB", "hwSSHServerRetry"),
        ("HUAWEI-SSH-MIB", "hwSSHServerPort"),
        ("HUAWEI-SSH-MIB", "hwSSHServerKeyTimeOut"),
        ("HUAWEI-SSH-MIB", "hwSSHServerAlarmEnable"),
        ("HUAWEI-SSH-MIB", "hwSftpMaxUserNum"),
        ("HUAWEI-SSH-MIB", "hwSftpOnLineUserNum"),
        ("HUAWEI-SSH-MIB", "hwSNetConfMaxUserNum"),
        ("HUAWEI-SSH-MIB", "hwSNetConfServerEnable"),
        ("HUAWEI-SSH-MIB", "hwSSHKeepAliveEnable"),
        ("HUAWEI-SSH-MIB", "hwSCPServerEnable"),
        ("HUAWEI-SSH-MIB", "hwSCPMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSSHServerGroup.setStatus("current")

hwSSHUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 2)
)
hwSSHUserGroup.setObjects(
      *(("HUAWEI-SSH-MIB", "hwSSHUserName"),
        ("HUAWEI-SSH-MIB", "hwSSHUserAssignKey"),
        ("HUAWEI-SSH-MIB", "hwSSHUserAuthType"),
        ("HUAWEI-SSH-MIB", "hwSSHUserServiceType"),
        ("HUAWEI-SSH-MIB", "hwSSHUserSftpDirectory"),
        ("HUAWEI-SSH-MIB", "hwSSHUserAuthorizationCMD"),
        ("HUAWEI-SSH-MIB", "hwSSHUserRowStatus"),
        ("HUAWEI-SSH-MIB", "hwSSHUserAssignKeyType"))
)
if mibBuilder.loadTexts:
    hwSSHUserGroup.setStatus("current")

hwSSHServerSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 3)
)
hwSSHServerSessionGroup.setObjects(
      *(("HUAWEI-SSH-MIB", "hwSSHSessionUserName"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionConnectType"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionVer"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionState"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionRetry"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionCtosCipher"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionStocCipher"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionCtosHmac"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionStocHmac"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionKex"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionAuthType"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionServiceType"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionKeyType"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionConnectionIndex"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionCtosCompress"),
        ("HUAWEI-SSH-MIB", "hwSSHSessionStocCompress"))
)
if mibBuilder.loadTexts:
    hwSSHServerSessionGroup.setStatus("current")

hwSSHClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 4)
)
hwSSHClientGroup.setObjects(
      *(("HUAWEI-SSH-MIB", "hwSSHFirstTimeAuthEnable"),
        ("HUAWEI-SSH-MIB", "hwSSHKeepAliveInterval"),
        ("HUAWEI-SSH-MIB", "hwSSHKeepAliveMaxCount"))
)
if mibBuilder.loadTexts:
    hwSSHClientGroup.setStatus("current")

hwSSHServerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 5)
)
hwSSHServerInfoGroup.setObjects(
      *(("HUAWEI-SSH-MIB", "hwSSHServerName"),
        ("HUAWEI-SSH-MIB", "hwSSHServerAssignKey"),
        ("HUAWEI-SSH-MIB", "hwSSHServerRowStatus"),
        ("HUAWEI-SSH-MIB", "hwSSHServerAssignDSAKey"))
)
if mibBuilder.loadTexts:
    hwSSHServerInfoGroup.setStatus("current")


# Notification objects

hwSSHSftpUserNumExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 3, 1)
)
hwSSHSftpUserNumExceedMax.setObjects(
      *(("HUAWEI-SSH-MIB", "hwSftpOnLineUserNum"),
        ("HUAWEI-SSH-MIB", "hwSftpMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSSHSftpUserNumExceedMax.setStatus(
        "current"
    )


# Notifications groups

hwSSHNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 6)
)
hwSSHNotificationGroup.setObjects(
    ("HUAWEI-SSH-MIB", "hwSSHSftpUserNumExceedMax")
)
if mibBuilder.loadTexts:
    hwSSHNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSSHMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwSSHMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SSH-MIB",
    **{"hwSSH": hwSSH,
       "hwSSHServer": hwSSHServer,
       "hwStelnetServerEnable": hwStelnetServerEnable,
       "hwSftpServerEnable": hwSftpServerEnable,
       "hwSSHServerComp1x": hwSSHServerComp1x,
       "hwSSHServerTimeOut": hwSSHServerTimeOut,
       "hwSSHServerRetry": hwSSHServerRetry,
       "hwSSHServerPort": hwSSHServerPort,
       "hwSSHServerKeyTimeOut": hwSSHServerKeyTimeOut,
       "hwSSHServerAlarmEnable": hwSSHServerAlarmEnable,
       "hwSftpMaxUserNum": hwSftpMaxUserNum,
       "hwSftpOnLineUserNum": hwSftpOnLineUserNum,
       "hwSSHUserTable": hwSSHUserTable,
       "hwSSHUserEntry": hwSSHUserEntry,
       "hwSSHUserIndex": hwSSHUserIndex,
       "hwSSHUserName": hwSSHUserName,
       "hwSSHUserAssignKey": hwSSHUserAssignKey,
       "hwSSHUserAuthType": hwSSHUserAuthType,
       "hwSSHUserServiceType": hwSSHUserServiceType,
       "hwSSHUserSftpDirectory": hwSSHUserSftpDirectory,
       "hwSSHUserAuthorizationCMD": hwSSHUserAuthorizationCMD,
       "hwSSHUserRowStatus": hwSSHUserRowStatus,
       "hwSSHUserAssignKeyType": hwSSHUserAssignKeyType,
       "hwSSHServerSessionTable": hwSSHServerSessionTable,
       "hwSSHServerSessionEntry": hwSSHServerSessionEntry,
       "hwSSHSessionIndex": hwSSHSessionIndex,
       "hwSSHSessionUserName": hwSSHSessionUserName,
       "hwSSHSessionConnectType": hwSSHSessionConnectType,
       "hwSSHSessionVer": hwSSHSessionVer,
       "hwSSHSessionState": hwSSHSessionState,
       "hwSSHSessionRetry": hwSSHSessionRetry,
       "hwSSHSessionCtosCipher": hwSSHSessionCtosCipher,
       "hwSSHSessionStocCipher": hwSSHSessionStocCipher,
       "hwSSHSessionCtosHmac": hwSSHSessionCtosHmac,
       "hwSSHSessionStocHmac": hwSSHSessionStocHmac,
       "hwSSHSessionKex": hwSSHSessionKex,
       "hwSSHSessionAuthType": hwSSHSessionAuthType,
       "hwSSHSessionServiceType": hwSSHSessionServiceType,
       "hwSSHSessionKeyType": hwSSHSessionKeyType,
       "hwSSHSessionConnectionIndex": hwSSHSessionConnectionIndex,
       "hwSSHSessionCtosCompress": hwSSHSessionCtosCompress,
       "hwSSHSessionStocCompress": hwSSHSessionStocCompress,
       "hwRSAPublicKeyTable": hwRSAPublicKeyTable,
       "hwRSAPublicKeyEntry": hwRSAPublicKeyEntry,
       "hwRSAPublicKeyName": hwRSAPublicKeyName,
       "hwRSAPublicKeyCode": hwRSAPublicKeyCode,
       "hwRSAPublicKeyRowStatus": hwRSAPublicKeyRowStatus,
       "hwRSAPublicKeyFingerprint": hwRSAPublicKeyFingerprint,
       "hwSNetConfMaxUserNum": hwSNetConfMaxUserNum,
       "hwSNetConfServerEnable": hwSNetConfServerEnable,
       "hwSSHKeepAliveEnable": hwSSHKeepAliveEnable,
       "hwSCPServerEnable": hwSCPServerEnable,
       "hwSCPMaxUserNum": hwSCPMaxUserNum,
       "hwSSHClient": hwSSHClient,
       "hwSSHFirstTimeAuthEnable": hwSSHFirstTimeAuthEnable,
       "hwSSHServerInfoTable": hwSSHServerInfoTable,
       "hwSSHServerInfoEntry": hwSSHServerInfoEntry,
       "hwSSHServerIndex": hwSSHServerIndex,
       "hwSSHServerName": hwSSHServerName,
       "hwSSHServerAssignKey": hwSSHServerAssignKey,
       "hwSSHServerRowStatus": hwSSHServerRowStatus,
       "hwSSHServerAssignDSAKey": hwSSHServerAssignDSAKey,
       "hwSSHServerAssignECCKey": hwSSHServerAssignECCKey,
       "hwSSHKeepAliveInterval": hwSSHKeepAliveInterval,
       "hwSSHKeepAliveMaxCount": hwSSHKeepAliveMaxCount,
       "hwSSHNotifications": hwSSHNotifications,
       "hwSSHSftpUserNumExceedMax": hwSSHSftpUserNumExceedMax,
       "hwSSHMIBConformance": hwSSHMIBConformance,
       "hwSSHMIBCompliances": hwSSHMIBCompliances,
       "hwSSHMIBCompliance": hwSSHMIBCompliance,
       "hwSSHMIBGroups": hwSSHMIBGroups,
       "hwSSHServerGroup": hwSSHServerGroup,
       "hwSSHUserGroup": hwSSHUserGroup,
       "hwSSHServerSessionGroup": hwSSHServerSessionGroup,
       "hwSSHClientGroup": hwSSHClientGroup,
       "hwSSHServerInfoGroup": hwSSHServerInfoGroup,
       "hwSSHNotificationGroup": hwSSHNotificationGroup,
       "hwRSALocalKeyTable": hwRSALocalKeyTable,
       "hwRSALocalHostPublicKeyCode": hwRSALocalHostPublicKeyCode,
       "hwRSALocalHostPublicKeyFingerprint": hwRSALocalHostPublicKeyFingerprint,
       "hwRSALocalServerPublicKeyCode": hwRSALocalServerPublicKeyCode,
       "hwRSALocalServerPublicKeyFingerprint": hwRSALocalServerPublicKeyFingerprint}
)
