# SNMP MIB module (HUAWEI-HGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-HGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:55 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwCluster = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7)
)
hwCluster.setRevisions(
        ("2015-04-11 15:31",
         "2015-04-07 15:25",
         "2013-09-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwClusterObject_ObjectIdentity = ObjectIdentity
hwClusterObject = _HwClusterObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1)
)
_HgmpEventsV2_ObjectIdentity = ObjectIdentity
hgmpEventsV2 = _HgmpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0)
)


class _HgmpSetVLANSecurity_Type(Integer32):
    """Custom type hgmpSetVLANSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noSecurity", 0),
          ("security", 1))
    )


_HgmpSetVLANSecurity_Type.__name__ = "Integer32"
_HgmpSetVLANSecurity_Object = MibScalar
hgmpSetVLANSecurity = _HgmpSetVLANSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 1),
    _HgmpSetVLANSecurity_Type()
)
hgmpSetVLANSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpSetVLANSecurity.setStatus("current")


class _HgmpHandShakeInterval_Type(Integer32):
    """Custom type hgmpHandShakeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HgmpHandShakeInterval_Type.__name__ = "Integer32"
_HgmpHandShakeInterval_Object = MibScalar
hgmpHandShakeInterval = _HgmpHandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 2),
    _HgmpHandShakeInterval_Type()
)
hgmpHandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpHandShakeInterval.setStatus("current")


class _HgmpHandShakeHoldtime_Type(Integer32):
    """Custom type hgmpHandShakeHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HgmpHandShakeHoldtime_Type.__name__ = "Integer32"
_HgmpHandShakeHoldtime_Object = MibScalar
hgmpHandShakeHoldtime = _HgmpHandShakeHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 3),
    _HgmpHandShakeHoldtime_Type()
)
hgmpHandShakeHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpHandShakeHoldtime.setStatus("current")


class _HgmpGrpMemberTableChange_Type(Integer32):
    """Custom type hgmpGrpMemberTableChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpGrpMemberTableChange_Type.__name__ = "Integer32"
_HgmpGrpMemberTableChange_Object = MibScalar
hgmpGrpMemberTableChange = _HgmpGrpMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 4),
    _HgmpGrpMemberTableChange_Type()
)
hgmpGrpMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberTableChange.setStatus("current")
_HgmpMemberDisconRate_Type = Integer32
_HgmpMemberDisconRate_Object = MibScalar
hgmpMemberDisconRate = _HgmpMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 5),
    _HgmpMemberDisconRate_Type()
)
hgmpMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberDisconRate.setStatus("current")


class _HgmpCmdLanswitchFlag_Type(Integer32):
    """Custom type hgmpCmdLanswitchFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpCmdLanswitchFlag_Type.__name__ = "Integer32"
_HgmpCmdLanswitchFlag_Object = MibScalar
hgmpCmdLanswitchFlag = _HgmpCmdLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 6),
    _HgmpCmdLanswitchFlag_Type()
)
hgmpCmdLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpCmdLanswitchFlag.setStatus("current")


class _HgmpCmdClusterName_Type(OctetString):
    """Custom type hgmpCmdClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HgmpCmdClusterName_Type.__name__ = "OctetString"
_HgmpCmdClusterName_Object = MibScalar
hgmpCmdClusterName = _HgmpCmdClusterName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 7),
    _HgmpCmdClusterName_Type()
)
hgmpCmdClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpCmdClusterName.setStatus("current")
_HgmpMngPriIpSegCMIP_Type = IpAddress
_HgmpMngPriIpSegCMIP_Object = MibScalar
hgmpMngPriIpSegCMIP = _HgmpMngPriIpSegCMIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 8),
    _HgmpMngPriIpSegCMIP_Type()
)
hgmpMngPriIpSegCMIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMngPriIpSegCMIP.setStatus("current")
_HgmpMngPriIpMask_Type = IpAddress
_HgmpMngPriIpMask_Object = MibScalar
hgmpMngPriIpMask = _HgmpMngPriIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 9),
    _HgmpMngPriIpMask_Type()
)
hgmpMngPriIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMngPriIpMask.setStatus("current")
_HgmpFtpServer_Type = IpAddress
_HgmpFtpServer_Object = MibScalar
hgmpFtpServer = _HgmpFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 10),
    _HgmpFtpServer_Type()
)
hgmpFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpFtpServer.setStatus("current")
_HgmpTftpServer_Type = IpAddress
_HgmpTftpServer_Object = MibScalar
hgmpTftpServer = _HgmpTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 11),
    _HgmpTftpServer_Type()
)
hgmpTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpTftpServer.setStatus("current")
_HgmpSnmpHost_Type = IpAddress
_HgmpSnmpHost_Object = MibScalar
hgmpSnmpHost = _HgmpSnmpHost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 12),
    _HgmpSnmpHost_Type()
)
hgmpSnmpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpSnmpHost.setStatus("current")
_HgmpLogHost_Type = IpAddress
_HgmpLogHost_Object = MibScalar
hgmpLogHost = _HgmpLogHost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 13),
    _HgmpLogHost_Type()
)
hgmpLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpLogHost.setStatus("current")
_HgmpGrpMemberTable_Object = MibTable
hgmpGrpMemberTable = _HgmpGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14)
)
if mibBuilder.loadTexts:
    hgmpGrpMemberTable.setStatus("current")
_HgmpGrpMemberEntry_Object = MibTableRow
hgmpGrpMemberEntry = _HgmpGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1)
)
hgmpGrpMemberEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hgmpGrpMemberEntry.setStatus("current")


class _HgmpGrpMemberDeviceId_Type(OctetString):
    """Custom type hgmpGrpMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpGrpMemberDeviceId_Type.__name__ = "OctetString"
_HgmpGrpMemberDeviceId_Object = MibTableColumn
hgmpGrpMemberDeviceId = _HgmpGrpMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 1),
    _HgmpGrpMemberDeviceId_Type()
)
hgmpGrpMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberDeviceId.setStatus("current")


class _HgmpGrpMemberSerial_Type(Integer32):
    """Custom type hgmpGrpMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpGrpMemberSerial_Type.__name__ = "Integer32"
_HgmpGrpMemberSerial_Object = MibTableColumn
hgmpGrpMemberSerial = _HgmpGrpMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 2),
    _HgmpGrpMemberSerial_Type()
)
hgmpGrpMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberSerial.setStatus("current")
_HgmpGrpMemberIpAddr_Type = IpAddress
_HgmpGrpMemberIpAddr_Object = MibTableColumn
hgmpGrpMemberIpAddr = _HgmpGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 3),
    _HgmpGrpMemberIpAddr_Type()
)
hgmpGrpMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberIpAddr.setStatus("current")


class _HgmpGrpMemberName_Type(OctetString):
    """Custom type hgmpGrpMemberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HgmpGrpMemberName_Type.__name__ = "OctetString"
_HgmpGrpMemberName_Object = MibTableColumn
hgmpGrpMemberName = _HgmpGrpMemberName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 4),
    _HgmpGrpMemberName_Type()
)
hgmpGrpMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberName.setStatus("current")


class _HgmpGrpMemberPassword_Type(OctetString):
    """Custom type hgmpGrpMemberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HgmpGrpMemberPassword_Type.__name__ = "OctetString"
_HgmpGrpMemberPassword_Object = MibTableColumn
hgmpGrpMemberPassword = _HgmpGrpMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 5),
    _HgmpGrpMemberPassword_Type()
)
hgmpGrpMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpGrpMemberPassword.setStatus("current")
_HgmpGrpMemberPlatform_Type = OctetString
_HgmpGrpMemberPlatform_Object = MibTableColumn
hgmpGrpMemberPlatform = _HgmpGrpMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 6),
    _HgmpGrpMemberPlatform_Type()
)
hgmpGrpMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberPlatform.setStatus("current")


class _HgmpGrpMemberStatus_Type(Integer32):
    """Custom type hgmpGrpMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("normal", 0))
    )


_HgmpGrpMemberStatus_Type.__name__ = "Integer32"
_HgmpGrpMemberStatus_Object = MibTableColumn
hgmpGrpMemberStatus = _HgmpGrpMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 7),
    _HgmpGrpMemberStatus_Type()
)
hgmpGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberStatus.setStatus("current")
_HgmpGrpMemberDisconCount_Type = Integer32
_HgmpGrpMemberDisconCount_Object = MibTableColumn
hgmpGrpMemberDisconCount = _HgmpGrpMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 8),
    _HgmpGrpMemberDisconCount_Type()
)
hgmpGrpMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberDisconCount.setStatus("current")
_HgmpGrpMemberEnrollTime_Type = Integer32
_HgmpGrpMemberEnrollTime_Object = MibTableColumn
hgmpGrpMemberEnrollTime = _HgmpGrpMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 9),
    _HgmpGrpMemberEnrollTime_Type()
)
hgmpGrpMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberEnrollTime.setStatus("current")
_HgmpGrpMemberOperate_Type = RowStatus
_HgmpGrpMemberOperate_Object = MibTableColumn
hgmpGrpMemberOperate = _HgmpGrpMemberOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 14, 1, 10),
    _HgmpGrpMemberOperate_Type()
)
hgmpGrpMemberOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpGrpMemberOperate.setStatus("current")
_HgmpMemberResetTable_Object = MibTable
hgmpMemberResetTable = _HgmpMemberResetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 15)
)
if mibBuilder.loadTexts:
    hgmpMemberResetTable.setStatus("current")
_HgmpMemberResetEntry_Object = MibTableRow
hgmpMemberResetEntry = _HgmpMemberResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 15, 1)
)
hgmpMemberResetEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpMemberResetMAC"),
)
if mibBuilder.loadTexts:
    hgmpMemberResetEntry.setStatus("current")
_HgmpMemberResetMAC_Type = MacAddress
_HgmpMemberResetMAC_Object = MibTableColumn
hgmpMemberResetMAC = _HgmpMemberResetMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 15, 1, 1),
    _HgmpMemberResetMAC_Type()
)
hgmpMemberResetMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberResetMAC.setStatus("current")


class _HgmpMemberEraseflash_Type(Integer32):
    """Custom type hgmpMemberEraseflash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("cannotget", 65535),
          ("erase", 1),
          ("noErase", 0))
    )


_HgmpMemberEraseflash_Type.__name__ = "Integer32"
_HgmpMemberEraseflash_Object = MibTableColumn
hgmpMemberEraseflash = _HgmpMemberEraseflash_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 15, 1, 2),
    _HgmpMemberEraseflash_Type()
)
hgmpMemberEraseflash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMemberEraseflash.setStatus("current")


class _HgmpClusterRole_Type(Integer32):
    """Custom type hgmpClusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("roleBAKSW", 3),
          ("roleCASW", 16),
          ("roleCMDSW", 1),
          ("roleMEMBERSW", 2),
          ("roleUNISW", 17))
    )


_HgmpClusterRole_Type.__name__ = "Integer32"
_HgmpClusterRole_Object = MibScalar
hgmpClusterRole = _HgmpClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 16),
    _HgmpClusterRole_Type()
)
hgmpClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterRole.setStatus("current")
_HgmpClusterMaxPoolNum_Type = Integer32
_HgmpClusterMaxPoolNum_Object = MibScalar
hgmpClusterMaxPoolNum = _HgmpClusterMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 17),
    _HgmpClusterMaxPoolNum_Type()
)
hgmpClusterMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterMaxPoolNum.setStatus("current")
_HgmpClusterCmdSwMac_Type = MacAddress
_HgmpClusterCmdSwMac_Object = MibScalar
hgmpClusterCmdSwMac = _HgmpClusterCmdSwMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 18),
    _HgmpClusterCmdSwMac_Type()
)
hgmpClusterCmdSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterCmdSwMac.setStatus("current")


class _HgmpRun_Type(Integer32):
    """Custom type hgmpRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpRun_Type.__name__ = "Integer32"
_HgmpRun_Object = MibScalar
hgmpRun = _HgmpRun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 19),
    _HgmpRun_Type()
)
hgmpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpRun.setStatus("current")


class _HgmpClusterAutojoin_Type(Integer32):
    """Custom type hgmpClusterAutojoin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpClusterAutojoin_Type.__name__ = "Integer32"
_HgmpClusterAutojoin_Object = MibScalar
hgmpClusterAutojoin = _HgmpClusterAutojoin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 20),
    _HgmpClusterAutojoin_Type()
)
hgmpClusterAutojoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpClusterAutojoin.setStatus("current")


class _HgmpClusterDiscAgingTime_Type(Integer32):
    """Custom type hgmpClusterDiscAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_HgmpClusterDiscAgingTime_Type.__name__ = "Integer32"
_HgmpClusterDiscAgingTime_Object = MibScalar
hgmpClusterDiscAgingTime = _HgmpClusterDiscAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 21),
    _HgmpClusterDiscAgingTime_Type()
)
hgmpClusterDiscAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpClusterDiscAgingTime.setStatus("current")
_HgmpPlugAndPlayStatus_Type = EnabledStatus
_HgmpPlugAndPlayStatus_Object = MibScalar
hgmpPlugAndPlayStatus = _HgmpPlugAndPlayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 22),
    _HgmpPlugAndPlayStatus_Type()
)
hgmpPlugAndPlayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpPlugAndPlayStatus.setStatus("current")
_HgmpMultiMacAddress_Type = MacAddress
_HgmpMultiMacAddress_Object = MibScalar
hgmpMultiMacAddress = _HgmpMultiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 23),
    _HgmpMultiMacAddress_Type()
)
hgmpMultiMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMultiMacAddress.setStatus("current")


class _HgmpManageVlan_Type(Integer32):
    """Custom type hgmpManageVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HgmpManageVlan_Type.__name__ = "Integer32"
_HgmpManageVlan_Object = MibScalar
hgmpManageVlan = _HgmpManageVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 24),
    _HgmpManageVlan_Type()
)
hgmpManageVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpManageVlan.setStatus("current")
_HgmpSftpServer_Type = IpAddress
_HgmpSftpServer_Object = MibScalar
hgmpSftpServer = _HgmpSftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 25),
    _HgmpSftpServer_Type()
)
hgmpSftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpSftpServer.setStatus("current")
_HgmpUnrelatedPortNdpAdminTable_Object = MibTable
hgmpUnrelatedPortNdpAdminTable = _HgmpUnrelatedPortNdpAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26)
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminTable.setStatus("current")
_HgmpUnrelatedPortNdpAdminEntry_Object = MibTableRow
hgmpUnrelatedPortNdpAdminEntry = _HgmpUnrelatedPortNdpAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1)
)
hgmpUnrelatedPortNdpAdminEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminCmdId"),
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminEntry.setStatus("current")


class _HgmpUnrelatedPortNdpAdminCmdId_Type(Integer32):
    """Custom type hgmpUnrelatedPortNdpAdminCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpUnrelatedPortNdpAdminCmdId_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNdpAdminCmdId_Object = MibTableColumn
hgmpUnrelatedPortNdpAdminCmdId = _HgmpUnrelatedPortNdpAdminCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1, 1),
    _HgmpUnrelatedPortNdpAdminCmdId_Type()
)
hgmpUnrelatedPortNdpAdminCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminCmdId.setStatus("current")


class _HgmpUnrelatedPortNdpAdminGroupType_Type(Integer32):
    """Custom type hgmpUnrelatedPortNdpAdminGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpUnrelatedPortNdpAdminGroupType_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNdpAdminGroupType_Object = MibTableColumn
hgmpUnrelatedPortNdpAdminGroupType = _HgmpUnrelatedPortNdpAdminGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1, 2),
    _HgmpUnrelatedPortNdpAdminGroupType_Type()
)
hgmpUnrelatedPortNdpAdminGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminGroupType.setStatus("current")


class _HgmpUnrelatedPortNdpAdminGroupValue_Type(OctetString):
    """Custom type hgmpUnrelatedPortNdpAdminGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpUnrelatedPortNdpAdminGroupValue_Type.__name__ = "OctetString"
_HgmpUnrelatedPortNdpAdminGroupValue_Object = MibTableColumn
hgmpUnrelatedPortNdpAdminGroupValue = _HgmpUnrelatedPortNdpAdminGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1, 3),
    _HgmpUnrelatedPortNdpAdminGroupValue_Type()
)
hgmpUnrelatedPortNdpAdminGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminGroupValue.setStatus("current")
_HgmpUnrelatedPortNdpAdminStatus_Type = EnabledStatus
_HgmpUnrelatedPortNdpAdminStatus_Object = MibTableColumn
hgmpUnrelatedPortNdpAdminStatus = _HgmpUnrelatedPortNdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1, 4),
    _HgmpUnrelatedPortNdpAdminStatus_Type()
)
hgmpUnrelatedPortNdpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminStatus.setStatus("current")
_HgmpUnrelatedPortNdpAdminRowStatus_Type = RowStatus
_HgmpUnrelatedPortNdpAdminRowStatus_Object = MibTableColumn
hgmpUnrelatedPortNdpAdminRowStatus = _HgmpUnrelatedPortNdpAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 26, 1, 5),
    _HgmpUnrelatedPortNdpAdminRowStatus_Type()
)
hgmpUnrelatedPortNdpAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpAdminRowStatus.setStatus("current")
_HgmpUnrelatedPortNdpResultTable_Object = MibTable
hgmpUnrelatedPortNdpResultTable = _HgmpUnrelatedPortNdpResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 27)
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpResultTable.setStatus("current")
_HgmpUnrelatedPortNdpResultEntry_Object = MibTableRow
hgmpUnrelatedPortNdpResultEntry = _HgmpUnrelatedPortNdpResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 27, 1)
)
hgmpUnrelatedPortNdpResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpResultEntry.setStatus("current")
_HgmpUnrelatedPortNdpResultMemberMac_Type = MacAddress
_HgmpUnrelatedPortNdpResultMemberMac_Object = MibTableColumn
hgmpUnrelatedPortNdpResultMemberMac = _HgmpUnrelatedPortNdpResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 27, 1, 1),
    _HgmpUnrelatedPortNdpResultMemberMac_Type()
)
hgmpUnrelatedPortNdpResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpResultMemberMac.setStatus("current")


class _HgmpUnrelatedPortNdpResultMemberId_Type(Integer32):
    """Custom type hgmpUnrelatedPortNdpResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpUnrelatedPortNdpResultMemberId_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNdpResultMemberId_Object = MibTableColumn
hgmpUnrelatedPortNdpResultMemberId = _HgmpUnrelatedPortNdpResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 27, 1, 2),
    _HgmpUnrelatedPortNdpResultMemberId_Type()
)
hgmpUnrelatedPortNdpResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpResultMemberId.setStatus("current")


class _HgmpUnrelatedPortNdpResult_Type(Integer32):
    """Custom type hgmpUnrelatedPortNdpResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpUnrelatedPortNdpResult_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNdpResult_Object = MibTableColumn
hgmpUnrelatedPortNdpResult = _HgmpUnrelatedPortNdpResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 27, 1, 3),
    _HgmpUnrelatedPortNdpResult_Type()
)
hgmpUnrelatedPortNdpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNdpResult.setStatus("current")
_HgmpUnrelatedPortNtdpAdminTable_Object = MibTable
hgmpUnrelatedPortNtdpAdminTable = _HgmpUnrelatedPortNtdpAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28)
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminTable.setStatus("current")
_HgmpUnrelatedPortNtdpAdminEntry_Object = MibTableRow
hgmpUnrelatedPortNtdpAdminEntry = _HgmpUnrelatedPortNtdpAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1)
)
hgmpUnrelatedPortNtdpAdminEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminCmdId"),
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminEntry.setStatus("current")


class _HgmpUnrelatedPortNtdpAdminCmdId_Type(Integer32):
    """Custom type hgmpUnrelatedPortNtdpAdminCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpUnrelatedPortNtdpAdminCmdId_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNtdpAdminCmdId_Object = MibTableColumn
hgmpUnrelatedPortNtdpAdminCmdId = _HgmpUnrelatedPortNtdpAdminCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1, 1),
    _HgmpUnrelatedPortNtdpAdminCmdId_Type()
)
hgmpUnrelatedPortNtdpAdminCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminCmdId.setStatus("current")


class _HgmpUnrelatedPortNtdpAdminGroupType_Type(Integer32):
    """Custom type hgmpUnrelatedPortNtdpAdminGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpUnrelatedPortNtdpAdminGroupType_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNtdpAdminGroupType_Object = MibTableColumn
hgmpUnrelatedPortNtdpAdminGroupType = _HgmpUnrelatedPortNtdpAdminGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1, 2),
    _HgmpUnrelatedPortNtdpAdminGroupType_Type()
)
hgmpUnrelatedPortNtdpAdminGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminGroupType.setStatus("current")


class _HgmpUnrelatedPortNtdpAdminGroupValue_Type(OctetString):
    """Custom type hgmpUnrelatedPortNtdpAdminGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpUnrelatedPortNtdpAdminGroupValue_Type.__name__ = "OctetString"
_HgmpUnrelatedPortNtdpAdminGroupValue_Object = MibTableColumn
hgmpUnrelatedPortNtdpAdminGroupValue = _HgmpUnrelatedPortNtdpAdminGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1, 3),
    _HgmpUnrelatedPortNtdpAdminGroupValue_Type()
)
hgmpUnrelatedPortNtdpAdminGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminGroupValue.setStatus("current")
_HgmpUnrelatedPortNtdpAdminStatus_Type = EnabledStatus
_HgmpUnrelatedPortNtdpAdminStatus_Object = MibTableColumn
hgmpUnrelatedPortNtdpAdminStatus = _HgmpUnrelatedPortNtdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1, 4),
    _HgmpUnrelatedPortNtdpAdminStatus_Type()
)
hgmpUnrelatedPortNtdpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminStatus.setStatus("current")
_HgmpUnrelatedPortNtdpAdminRowStatus_Type = RowStatus
_HgmpUnrelatedPortNtdpAdminRowStatus_Object = MibTableColumn
hgmpUnrelatedPortNtdpAdminRowStatus = _HgmpUnrelatedPortNtdpAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 28, 1, 5),
    _HgmpUnrelatedPortNtdpAdminRowStatus_Type()
)
hgmpUnrelatedPortNtdpAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpAdminRowStatus.setStatus("current")
_HgmpUnrelatedPortNtdpResultTable_Object = MibTable
hgmpUnrelatedPortNtdpResultTable = _HgmpUnrelatedPortNtdpResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 29)
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpResultTable.setStatus("current")
_HgmpUnrelatedPortNtdpResultEntry_Object = MibTableRow
hgmpUnrelatedPortNtdpResultEntry = _HgmpUnrelatedPortNtdpResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 29, 1)
)
hgmpUnrelatedPortNtdpResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpResultEntry.setStatus("current")
_HgmpUnrelatedPortNtdpResultMemberMac_Type = MacAddress
_HgmpUnrelatedPortNtdpResultMemberMac_Object = MibTableColumn
hgmpUnrelatedPortNtdpResultMemberMac = _HgmpUnrelatedPortNtdpResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 29, 1, 1),
    _HgmpUnrelatedPortNtdpResultMemberMac_Type()
)
hgmpUnrelatedPortNtdpResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpResultMemberMac.setStatus("current")


class _HgmpUnrelatedPortNtdpResultMemberId_Type(Integer32):
    """Custom type hgmpUnrelatedPortNtdpResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpUnrelatedPortNtdpResultMemberId_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNtdpResultMemberId_Object = MibTableColumn
hgmpUnrelatedPortNtdpResultMemberId = _HgmpUnrelatedPortNtdpResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 29, 1, 2),
    _HgmpUnrelatedPortNtdpResultMemberId_Type()
)
hgmpUnrelatedPortNtdpResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpResultMemberId.setStatus("current")


class _HgmpUnrelatedPortNtdpResult_Type(Integer32):
    """Custom type hgmpUnrelatedPortNtdpResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpUnrelatedPortNtdpResult_Type.__name__ = "Integer32"
_HgmpUnrelatedPortNtdpResult_Object = MibTableColumn
hgmpUnrelatedPortNtdpResult = _HgmpUnrelatedPortNtdpResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 29, 1, 3),
    _HgmpUnrelatedPortNtdpResult_Type()
)
hgmpUnrelatedPortNtdpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpUnrelatedPortNtdpResult.setStatus("current")
_HgmpBatchUpgradeTable_Object = MibTable
hgmpBatchUpgradeTable = _HgmpBatchUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30)
)
if mibBuilder.loadTexts:
    hgmpBatchUpgradeTable.setStatus("current")
_HgmpBatchUpgradeEntry_Object = MibTableRow
hgmpBatchUpgradeEntry = _HgmpBatchUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1)
)
hgmpBatchUpgradeEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchUpgradeCmdId"),
)
if mibBuilder.loadTexts:
    hgmpBatchUpgradeEntry.setStatus("current")


class _HgmpBatchUpgradeCmdId_Type(Integer32):
    """Custom type hgmpBatchUpgradeCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpBatchUpgradeCmdId_Type.__name__ = "Integer32"
_HgmpBatchUpgradeCmdId_Object = MibTableColumn
hgmpBatchUpgradeCmdId = _HgmpBatchUpgradeCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 1),
    _HgmpBatchUpgradeCmdId_Type()
)
hgmpBatchUpgradeCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeCmdId.setStatus("current")


class _HgmpBatchUpgradeGroupType_Type(Integer32):
    """Custom type hgmpBatchUpgradeGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpBatchUpgradeGroupType_Type.__name__ = "Integer32"
_HgmpBatchUpgradeGroupType_Object = MibTableColumn
hgmpBatchUpgradeGroupType = _HgmpBatchUpgradeGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 2),
    _HgmpBatchUpgradeGroupType_Type()
)
hgmpBatchUpgradeGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeGroupType.setStatus("current")


class _HgmpBatchUpgradeGroupValue_Type(OctetString):
    """Custom type hgmpBatchUpgradeGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpBatchUpgradeGroupValue_Type.__name__ = "OctetString"
_HgmpBatchUpgradeGroupValue_Object = MibTableColumn
hgmpBatchUpgradeGroupValue = _HgmpBatchUpgradeGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 3),
    _HgmpBatchUpgradeGroupValue_Type()
)
hgmpBatchUpgradeGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeGroupValue.setStatus("current")


class _HgmpBatchUpgradeFileType_Type(Integer32):
    """Custom type hgmpBatchUpgradeFileType based on Integer32"""
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
        *(("configFile", 3),
          ("licenseFile", 5),
          ("pafFile", 4),
          ("patchFile", 2),
          ("versionFile", 1))
    )


_HgmpBatchUpgradeFileType_Type.__name__ = "Integer32"
_HgmpBatchUpgradeFileType_Object = MibTableColumn
hgmpBatchUpgradeFileType = _HgmpBatchUpgradeFileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 4),
    _HgmpBatchUpgradeFileType_Type()
)
hgmpBatchUpgradeFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeFileType.setStatus("current")
_HgmpBatchUpgradeFileName_Type = OctetString
_HgmpBatchUpgradeFileName_Object = MibTableColumn
hgmpBatchUpgradeFileName = _HgmpBatchUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 5),
    _HgmpBatchUpgradeFileName_Type()
)
hgmpBatchUpgradeFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeFileName.setStatus("current")
_HgmpBatchUpgradeRowStatus_Type = RowStatus
_HgmpBatchUpgradeRowStatus_Object = MibTableColumn
hgmpBatchUpgradeRowStatus = _HgmpBatchUpgradeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 30, 1, 6),
    _HgmpBatchUpgradeRowStatus_Type()
)
hgmpBatchUpgradeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeRowStatus.setStatus("current")
_HgmpBatchUpgradeResultTable_Object = MibTable
hgmpBatchUpgradeResultTable = _HgmpBatchUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 31)
)
if mibBuilder.loadTexts:
    hgmpBatchUpgradeResultTable.setStatus("current")
_HgmpBatchUpgradeResultEntry_Object = MibTableRow
hgmpBatchUpgradeResultEntry = _HgmpBatchUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 31, 1)
)
hgmpBatchUpgradeResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchUpgradeCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchUpgradeResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpBatchUpgradeResultEntry.setStatus("current")
_HgmpBatchUpgradeResultMemberMac_Type = MacAddress
_HgmpBatchUpgradeResultMemberMac_Object = MibTableColumn
hgmpBatchUpgradeResultMemberMac = _HgmpBatchUpgradeResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 31, 1, 1),
    _HgmpBatchUpgradeResultMemberMac_Type()
)
hgmpBatchUpgradeResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeResultMemberMac.setStatus("current")


class _HgmpBatchUpgradeResultMemberId_Type(Integer32):
    """Custom type hgmpBatchUpgradeResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpBatchUpgradeResultMemberId_Type.__name__ = "Integer32"
_HgmpBatchUpgradeResultMemberId_Object = MibTableColumn
hgmpBatchUpgradeResultMemberId = _HgmpBatchUpgradeResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 31, 1, 2),
    _HgmpBatchUpgradeResultMemberId_Type()
)
hgmpBatchUpgradeResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeResultMemberId.setStatus("current")


class _HgmpBatchUpgradeResult_Type(Integer32):
    """Custom type hgmpBatchUpgradeResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpBatchUpgradeResult_Type.__name__ = "Integer32"
_HgmpBatchUpgradeResult_Object = MibTableColumn
hgmpBatchUpgradeResult = _HgmpBatchUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 31, 1, 3),
    _HgmpBatchUpgradeResult_Type()
)
hgmpBatchUpgradeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchUpgradeResult.setStatus("current")
_HgmpBatchRebootTable_Object = MibTable
hgmpBatchRebootTable = _HgmpBatchRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32)
)
if mibBuilder.loadTexts:
    hgmpBatchRebootTable.setStatus("current")
_HgmpBatchRebootEntry_Object = MibTableRow
hgmpBatchRebootEntry = _HgmpBatchRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32, 1)
)
hgmpBatchRebootEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchRebootCmdId"),
)
if mibBuilder.loadTexts:
    hgmpBatchRebootEntry.setStatus("current")


class _HgmpBatchRebootCmdId_Type(Integer32):
    """Custom type hgmpBatchRebootCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpBatchRebootCmdId_Type.__name__ = "Integer32"
_HgmpBatchRebootCmdId_Object = MibTableColumn
hgmpBatchRebootCmdId = _HgmpBatchRebootCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32, 1, 1),
    _HgmpBatchRebootCmdId_Type()
)
hgmpBatchRebootCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchRebootCmdId.setStatus("current")


class _HgmpBatchRebootGroupType_Type(Integer32):
    """Custom type hgmpBatchRebootGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpBatchRebootGroupType_Type.__name__ = "Integer32"
_HgmpBatchRebootGroupType_Object = MibTableColumn
hgmpBatchRebootGroupType = _HgmpBatchRebootGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32, 1, 2),
    _HgmpBatchRebootGroupType_Type()
)
hgmpBatchRebootGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchRebootGroupType.setStatus("current")


class _HgmpBatchRebootGroupValue_Type(OctetString):
    """Custom type hgmpBatchRebootGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpBatchRebootGroupValue_Type.__name__ = "OctetString"
_HgmpBatchRebootGroupValue_Object = MibTableColumn
hgmpBatchRebootGroupValue = _HgmpBatchRebootGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32, 1, 3),
    _HgmpBatchRebootGroupValue_Type()
)
hgmpBatchRebootGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchRebootGroupValue.setStatus("current")
_HgmpBatchRebootRowStatus_Type = RowStatus
_HgmpBatchRebootRowStatus_Object = MibTableColumn
hgmpBatchRebootRowStatus = _HgmpBatchRebootRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 32, 1, 4),
    _HgmpBatchRebootRowStatus_Type()
)
hgmpBatchRebootRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchRebootRowStatus.setStatus("current")
_HgmpBatchRebootResultTable_Object = MibTable
hgmpBatchRebootResultTable = _HgmpBatchRebootResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 33)
)
if mibBuilder.loadTexts:
    hgmpBatchRebootResultTable.setStatus("current")
_HgmpBatchRebootResultEntry_Object = MibTableRow
hgmpBatchRebootResultEntry = _HgmpBatchRebootResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 33, 1)
)
hgmpBatchRebootResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchRebootCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchRebootResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpBatchRebootResultEntry.setStatus("current")
_HgmpBatchRebootResultMemberMac_Type = MacAddress
_HgmpBatchRebootResultMemberMac_Object = MibTableColumn
hgmpBatchRebootResultMemberMac = _HgmpBatchRebootResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 33, 1, 1),
    _HgmpBatchRebootResultMemberMac_Type()
)
hgmpBatchRebootResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchRebootResultMemberMac.setStatus("current")


class _HgmpBatchRebootResultMemberId_Type(Integer32):
    """Custom type hgmpBatchRebootResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpBatchRebootResultMemberId_Type.__name__ = "Integer32"
_HgmpBatchRebootResultMemberId_Object = MibTableColumn
hgmpBatchRebootResultMemberId = _HgmpBatchRebootResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 33, 1, 2),
    _HgmpBatchRebootResultMemberId_Type()
)
hgmpBatchRebootResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchRebootResultMemberId.setStatus("current")


class _HgmpBatchRebootResult_Type(Integer32):
    """Custom type hgmpBatchRebootResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpBatchRebootResult_Type.__name__ = "Integer32"
_HgmpBatchRebootResult_Object = MibTableColumn
hgmpBatchRebootResult = _HgmpBatchRebootResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 33, 1, 3),
    _HgmpBatchRebootResult_Type()
)
hgmpBatchRebootResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchRebootResult.setStatus("current")
_HgmpBatchSaveTable_Object = MibTable
hgmpBatchSaveTable = _HgmpBatchSaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34)
)
if mibBuilder.loadTexts:
    hgmpBatchSaveTable.setStatus("current")
_HgmpBatchSaveEntry_Object = MibTableRow
hgmpBatchSaveEntry = _HgmpBatchSaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34, 1)
)
hgmpBatchSaveEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSaveCmdId"),
)
if mibBuilder.loadTexts:
    hgmpBatchSaveEntry.setStatus("current")


class _HgmpBatchSaveCmdId_Type(Integer32):
    """Custom type hgmpBatchSaveCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpBatchSaveCmdId_Type.__name__ = "Integer32"
_HgmpBatchSaveCmdId_Object = MibTableColumn
hgmpBatchSaveCmdId = _HgmpBatchSaveCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34, 1, 1),
    _HgmpBatchSaveCmdId_Type()
)
hgmpBatchSaveCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchSaveCmdId.setStatus("current")


class _HgmpBatchSaveGroupType_Type(Integer32):
    """Custom type hgmpBatchSaveGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpBatchSaveGroupType_Type.__name__ = "Integer32"
_HgmpBatchSaveGroupType_Object = MibTableColumn
hgmpBatchSaveGroupType = _HgmpBatchSaveGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34, 1, 2),
    _HgmpBatchSaveGroupType_Type()
)
hgmpBatchSaveGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSaveGroupType.setStatus("current")


class _HgmpBatchSaveGroupValue_Type(OctetString):
    """Custom type hgmpBatchSaveGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpBatchSaveGroupValue_Type.__name__ = "OctetString"
_HgmpBatchSaveGroupValue_Object = MibTableColumn
hgmpBatchSaveGroupValue = _HgmpBatchSaveGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34, 1, 3),
    _HgmpBatchSaveGroupValue_Type()
)
hgmpBatchSaveGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSaveGroupValue.setStatus("current")
_HgmpBatchSaveRowStatus_Type = RowStatus
_HgmpBatchSaveRowStatus_Object = MibTableColumn
hgmpBatchSaveRowStatus = _HgmpBatchSaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 34, 1, 4),
    _HgmpBatchSaveRowStatus_Type()
)
hgmpBatchSaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSaveRowStatus.setStatus("current")
_HgmpBatchSaveResultTable_Object = MibTable
hgmpBatchSaveResultTable = _HgmpBatchSaveResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 35)
)
if mibBuilder.loadTexts:
    hgmpBatchSaveResultTable.setStatus("current")
_HgmpBatchSaveResultEntry_Object = MibTableRow
hgmpBatchSaveResultEntry = _HgmpBatchSaveResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 35, 1)
)
hgmpBatchSaveResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSaveCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSaveResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpBatchSaveResultEntry.setStatus("current")
_HgmpBatchSaveResultMemberMac_Type = MacAddress
_HgmpBatchSaveResultMemberMac_Object = MibTableColumn
hgmpBatchSaveResultMemberMac = _HgmpBatchSaveResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 35, 1, 1),
    _HgmpBatchSaveResultMemberMac_Type()
)
hgmpBatchSaveResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchSaveResultMemberMac.setStatus("current")


class _HgmpBatchSaveResultMemberId_Type(Integer32):
    """Custom type hgmpBatchSaveResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpBatchSaveResultMemberId_Type.__name__ = "Integer32"
_HgmpBatchSaveResultMemberId_Object = MibTableColumn
hgmpBatchSaveResultMemberId = _HgmpBatchSaveResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 35, 1, 2),
    _HgmpBatchSaveResultMemberId_Type()
)
hgmpBatchSaveResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchSaveResultMemberId.setStatus("current")


class _HgmpBatchSaveResult_Type(Integer32):
    """Custom type hgmpBatchSaveResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpBatchSaveResult_Type.__name__ = "Integer32"
_HgmpBatchSaveResult_Object = MibTableColumn
hgmpBatchSaveResult = _HgmpBatchSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 35, 1, 3),
    _HgmpBatchSaveResult_Type()
)
hgmpBatchSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchSaveResult.setStatus("current")
_HgmpBatchSynchronizeCfgFileTable_Object = MibTable
hgmpBatchSynchronizeCfgFileTable = _HgmpBatchSynchronizeCfgFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36)
)
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileTable.setStatus("current")
_HgmpBatchSynchronizeCfgFileEntry_Object = MibTableRow
hgmpBatchSynchronizeCfgFileEntry = _HgmpBatchSynchronizeCfgFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36, 1)
)
hgmpBatchSynchronizeCfgFileEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileCmdId"),
)
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileEntry.setStatus("current")


class _HgmpBatchSynchronizeCfgFileCmdId_Type(Integer32):
    """Custom type hgmpBatchSynchronizeCfgFileCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HgmpBatchSynchronizeCfgFileCmdId_Type.__name__ = "Integer32"
_HgmpBatchSynchronizeCfgFileCmdId_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileCmdId = _HgmpBatchSynchronizeCfgFileCmdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36, 1, 1),
    _HgmpBatchSynchronizeCfgFileCmdId_Type()
)
hgmpBatchSynchronizeCfgFileCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileCmdId.setStatus("current")


class _HgmpBatchSynchronizeCfgFileGroupType_Type(Integer32):
    """Custom type hgmpBatchSynchronizeCfgFileGroupType based on Integer32"""
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
        *(("allMembers", 1),
          ("deviceType", 2),
          ("memberIdList", 3))
    )


_HgmpBatchSynchronizeCfgFileGroupType_Type.__name__ = "Integer32"
_HgmpBatchSynchronizeCfgFileGroupType_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileGroupType = _HgmpBatchSynchronizeCfgFileGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36, 1, 2),
    _HgmpBatchSynchronizeCfgFileGroupType_Type()
)
hgmpBatchSynchronizeCfgFileGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileGroupType.setStatus("current")


class _HgmpBatchSynchronizeCfgFileGroupValue_Type(OctetString):
    """Custom type hgmpBatchSynchronizeCfgFileGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HgmpBatchSynchronizeCfgFileGroupValue_Type.__name__ = "OctetString"
_HgmpBatchSynchronizeCfgFileGroupValue_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileGroupValue = _HgmpBatchSynchronizeCfgFileGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36, 1, 3),
    _HgmpBatchSynchronizeCfgFileGroupValue_Type()
)
hgmpBatchSynchronizeCfgFileGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileGroupValue.setStatus("current")
_HgmpBatchSynchronizeCfgFileRowStatus_Type = RowStatus
_HgmpBatchSynchronizeCfgFileRowStatus_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileRowStatus = _HgmpBatchSynchronizeCfgFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 36, 1, 4),
    _HgmpBatchSynchronizeCfgFileRowStatus_Type()
)
hgmpBatchSynchronizeCfgFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileRowStatus.setStatus("current")
_HgmpBatchSynchronizeCfgFileResultTable_Object = MibTable
hgmpBatchSynchronizeCfgFileResultTable = _HgmpBatchSynchronizeCfgFileResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 37)
)
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileResultTable.setStatus("current")
_HgmpBatchSynchronizeCfgFileResultEntry_Object = MibTableRow
hgmpBatchSynchronizeCfgFileResultEntry = _HgmpBatchSynchronizeCfgFileResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 37, 1)
)
hgmpBatchSynchronizeCfgFileResultEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileCmdId"),
    (0, "HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileResultMemberMac"),
)
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileResultEntry.setStatus("current")
_HgmpBatchSynchronizeCfgFileResultMemberMac_Type = MacAddress
_HgmpBatchSynchronizeCfgFileResultMemberMac_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileResultMemberMac = _HgmpBatchSynchronizeCfgFileResultMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 37, 1, 1),
    _HgmpBatchSynchronizeCfgFileResultMemberMac_Type()
)
hgmpBatchSynchronizeCfgFileResultMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileResultMemberMac.setStatus("current")


class _HgmpBatchSynchronizeCfgFileResultMemberId_Type(Integer32):
    """Custom type hgmpBatchSynchronizeCfgFileResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpBatchSynchronizeCfgFileResultMemberId_Type.__name__ = "Integer32"
_HgmpBatchSynchronizeCfgFileResultMemberId_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileResultMemberId = _HgmpBatchSynchronizeCfgFileResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 37, 1, 2),
    _HgmpBatchSynchronizeCfgFileResultMemberId_Type()
)
hgmpBatchSynchronizeCfgFileResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileResultMemberId.setStatus("current")


class _HgmpBatchSynchronizeCfgFileResult_Type(Integer32):
    """Custom type hgmpBatchSynchronizeCfgFileResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HgmpBatchSynchronizeCfgFileResult_Type.__name__ = "Integer32"
_HgmpBatchSynchronizeCfgFileResult_Object = MibTableColumn
hgmpBatchSynchronizeCfgFileResult = _HgmpBatchSynchronizeCfgFileResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 37, 1, 3),
    _HgmpBatchSynchronizeCfgFileResult_Type()
)
hgmpBatchSynchronizeCfgFileResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBatchSynchronizeCfgFileResult.setStatus("current")


class _HgmpMemberRebootTimeoutValue_Type(Integer32):
    """Custom type hgmpMemberRebootTimeoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HgmpMemberRebootTimeoutValue_Type.__name__ = "Integer32"
_HgmpMemberRebootTimeoutValue_Object = MibScalar
hgmpMemberRebootTimeoutValue = _HgmpMemberRebootTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 38),
    _HgmpMemberRebootTimeoutValue_Type()
)
hgmpMemberRebootTimeoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMemberRebootTimeoutValue.setStatus("current")


class _HgmpClusterVersion_Type(Integer32):
    """Custom type hgmpClusterVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_HgmpClusterVersion_Type.__name__ = "Integer32"
_HgmpClusterVersion_Object = MibScalar
hgmpClusterVersion = _HgmpClusterVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 39),
    _HgmpClusterVersion_Type()
)
hgmpClusterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpClusterVersion.setStatus("current")
_HwStackObject_ObjectIdentity = ObjectIdentity
hwStackObject = _HwStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2)
)
_HgmpStackEventsV2_ObjectIdentity = ObjectIdentity
hgmpStackEventsV2 = _HgmpStackEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 0)
)


class _HgmpStackMemberTableChange_Type(Integer32):
    """Custom type hgmpStackMemberTableChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpStackMemberTableChange_Type.__name__ = "Integer32"
_HgmpStackMemberTableChange_Object = MibScalar
hgmpStackMemberTableChange = _HgmpStackMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 1),
    _HgmpStackMemberTableChange_Type()
)
hgmpStackMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberTableChange.setStatus("current")
_HgmpStackMemberDisconRate_Type = Integer32
_HgmpStackMemberDisconRate_Object = MibScalar
hgmpStackMemberDisconRate = _HgmpStackMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 2),
    _HgmpStackMemberDisconRate_Type()
)
hgmpStackMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberDisconRate.setStatus("current")


class _HgmpMainLanswitchFlag_Type(Integer32):
    """Custom type hgmpMainLanswitchFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpMainLanswitchFlag_Type.__name__ = "Integer32"
_HgmpMainLanswitchFlag_Object = MibScalar
hgmpMainLanswitchFlag = _HgmpMainLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 3),
    _HgmpMainLanswitchFlag_Type()
)
hgmpMainLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMainLanswitchFlag.setStatus("current")
_HgmpStackIpPoolStartIP_Type = IpAddress
_HgmpStackIpPoolStartIP_Object = MibScalar
hgmpStackIpPoolStartIP = _HgmpStackIpPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 4),
    _HgmpStackIpPoolStartIP_Type()
)
hgmpStackIpPoolStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpStackIpPoolStartIP.setStatus("current")


class _HgmpStackIpPoolLength_Type(Integer32):
    """Custom type hgmpStackIpPoolLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HgmpStackIpPoolLength_Type.__name__ = "Integer32"
_HgmpStackIpPoolLength_Object = MibScalar
hgmpStackIpPoolLength = _HgmpStackIpPoolLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 5),
    _HgmpStackIpPoolLength_Type()
)
hgmpStackIpPoolLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpStackIpPoolLength.setStatus("current")
_HgmpStackMemberTable_Object = MibTable
hgmpStackMemberTable = _HgmpStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hgmpStackMemberTable.setStatus("current")
_HgmpStackMemberEntry_Object = MibTableRow
hgmpStackMemberEntry = _HgmpStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1)
)
hgmpStackMemberEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hgmpStackMemberEntry.setStatus("current")


class _HgmpStackMemberDeviceId_Type(OctetString):
    """Custom type hgmpStackMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpStackMemberDeviceId_Type.__name__ = "OctetString"
_HgmpStackMemberDeviceId_Object = MibTableColumn
hgmpStackMemberDeviceId = _HgmpStackMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 1),
    _HgmpStackMemberDeviceId_Type()
)
hgmpStackMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberDeviceId.setStatus("current")


class _HgmpStackMemberSerial_Type(Integer32):
    """Custom type hgmpStackMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HgmpStackMemberSerial_Type.__name__ = "Integer32"
_HgmpStackMemberSerial_Object = MibTableColumn
hgmpStackMemberSerial = _HgmpStackMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 2),
    _HgmpStackMemberSerial_Type()
)
hgmpStackMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberSerial.setStatus("current")
_HgmpStackMemberIpAddr_Type = IpAddress
_HgmpStackMemberIpAddr_Object = MibTableColumn
hgmpStackMemberIpAddr = _HgmpStackMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 3),
    _HgmpStackMemberIpAddr_Type()
)
hgmpStackMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberIpAddr.setStatus("current")
_HgmpStackMemberName_Type = OctetString
_HgmpStackMemberName_Object = MibTableColumn
hgmpStackMemberName = _HgmpStackMemberName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 4),
    _HgmpStackMemberName_Type()
)
hgmpStackMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberName.setStatus("current")
_HgmpStackMemberPassword_Type = OctetString
_HgmpStackMemberPassword_Object = MibTableColumn
hgmpStackMemberPassword = _HgmpStackMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 5),
    _HgmpStackMemberPassword_Type()
)
hgmpStackMemberPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberPassword.setStatus("current")
_HgmpStackMemberPlatform_Type = OctetString
_HgmpStackMemberPlatform_Object = MibTableColumn
hgmpStackMemberPlatform = _HgmpStackMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 6),
    _HgmpStackMemberPlatform_Type()
)
hgmpStackMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberPlatform.setStatus("current")


class _HgmpStackMemberStatus_Type(Integer32):
    """Custom type hgmpStackMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("normal", 0))
    )


_HgmpStackMemberStatus_Type.__name__ = "Integer32"
_HgmpStackMemberStatus_Object = MibTableColumn
hgmpStackMemberStatus = _HgmpStackMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 7),
    _HgmpStackMemberStatus_Type()
)
hgmpStackMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberStatus.setStatus("current")
_HgmpStackMemberDisconCount_Type = Integer32
_HgmpStackMemberDisconCount_Object = MibTableColumn
hgmpStackMemberDisconCount = _HgmpStackMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 8),
    _HgmpStackMemberDisconCount_Type()
)
hgmpStackMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberDisconCount.setStatus("current")
_HgmpStackMemberEnrollTime_Type = Integer32
_HgmpStackMemberEnrollTime_Object = MibTableColumn
hgmpStackMemberEnrollTime = _HgmpStackMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 6, 1, 9),
    _HgmpStackMemberEnrollTime_Type()
)
hgmpStackMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberEnrollTime.setStatus("current")


class _HgmpStackRole_Type(Integer32):
    """Custom type hgmpStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("roleBAKSW", 3),
          ("roleCASW", 16),
          ("roleCMDSW", 1),
          ("roleMEMBERSW", 2),
          ("roleUNISW", 17))
    )


_HgmpStackRole_Type.__name__ = "Integer32"
_HgmpStackRole_Object = MibScalar
hgmpStackRole = _HgmpStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 7),
    _HgmpStackRole_Type()
)
hgmpStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackRole.setStatus("current")
_HgmpStackMaxPoolNum_Type = Integer32
_HgmpStackMaxPoolNum_Object = MibScalar
hgmpStackMaxPoolNum = _HgmpStackMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 8),
    _HgmpStackMaxPoolNum_Type()
)
hgmpStackMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMaxPoolNum.setStatus("current")
_HgmpStackMainSwMac_Type = MacAddress
_HgmpStackMainSwMac_Object = MibScalar
hgmpStackMainSwMac = _HgmpStackMainSwMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 9),
    _HgmpStackMainSwMac_Type()
)
hgmpStackMainSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMainSwMac.setStatus("current")
_HgmpStackIpPoolMask_Type = IpAddress
_HgmpStackIpPoolMask_Object = MibScalar
hgmpStackIpPoolMask = _HgmpStackIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 10),
    _HgmpStackIpPoolMask_Type()
)
hgmpStackIpPoolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpStackIpPoolMask.setStatus("current")
_HwNTDPObject_ObjectIdentity = ObjectIdentity
hwNTDPObject = _HwNTDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4)
)


class _HgmpNTDPCollectTopTime_Type(Integer32):
    """Custom type hgmpNTDPCollectTopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPCollectTopTime_Type.__name__ = "Integer32"
_HgmpNTDPCollectTopTime_Object = MibScalar
hgmpNTDPCollectTopTime = _HgmpNTDPCollectTopTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 1),
    _HgmpNTDPCollectTopTime_Type()
)
hgmpNTDPCollectTopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPCollectTopTime.setStatus("current")


class _HgmpNTDPHopRange_Type(Integer32):
    """Custom type hgmpNTDPHopRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HgmpNTDPHopRange_Type.__name__ = "Integer32"
_HgmpNTDPHopRange_Object = MibScalar
hgmpNTDPHopRange = _HgmpNTDPHopRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 2),
    _HgmpNTDPHopRange_Type()
)
hgmpNTDPHopRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPHopRange.setStatus("current")


class _HgmpNTDPRun_Type(Integer32):
    """Custom type hgmpNTDPRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpNTDPRun_Type.__name__ = "Integer32"
_HgmpNTDPRun_Object = MibScalar
hgmpNTDPRun = _HgmpNTDPRun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 3),
    _HgmpNTDPRun_Type()
)
hgmpNTDPRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPRun.setStatus("current")


class _HgmpNTDPPortDelay_Type(Integer32):
    """Custom type hgmpNTDPPortDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HgmpNTDPPortDelay_Type.__name__ = "Integer32"
_HgmpNTDPPortDelay_Object = MibScalar
hgmpNTDPPortDelay = _HgmpNTDPPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 4),
    _HgmpNTDPPortDelay_Type()
)
hgmpNTDPPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPPortDelay.setStatus("current")


class _HgmpNTDPHopDelay_Type(Integer32):
    """Custom type hgmpNTDPHopDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HgmpNTDPHopDelay_Type.__name__ = "Integer32"
_HgmpNTDPHopDelay_Object = MibScalar
hgmpNTDPHopDelay = _HgmpNTDPHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 5),
    _HgmpNTDPHopDelay_Type()
)
hgmpNTDPHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPHopDelay.setStatus("current")
_HgmpNTDPLastTopCollectDuration_Type = Integer32
_HgmpNTDPLastTopCollectDuration_Object = MibScalar
hgmpNTDPLastTopCollectDuration = _HgmpNTDPLastTopCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 6),
    _HgmpNTDPLastTopCollectDuration_Type()
)
hgmpNTDPLastTopCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPLastTopCollectDuration.setStatus("current")


class _HgmpNTDPCacheChange_Type(Integer32):
    """Custom type hgmpNTDPCacheChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPCacheChange_Type.__name__ = "Integer32"
_HgmpNTDPCacheChange_Object = MibScalar
hgmpNTDPCacheChange = _HgmpNTDPCacheChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 7),
    _HgmpNTDPCacheChange_Type()
)
hgmpNTDPCacheChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheChange.setStatus("current")


class _HgmpNTDPTOPTableChange_Type(Integer32):
    """Custom type hgmpNTDPTOPTableChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPTOPTableChange_Type.__name__ = "Integer32"
_HgmpNTDPTOPTableChange_Object = MibScalar
hgmpNTDPTOPTableChange = _HgmpNTDPTOPTableChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 8),
    _HgmpNTDPTOPTableChange_Type()
)
hgmpNTDPTOPTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTOPTableChange.setStatus("current")
_HgmpNTDPInterfaceTable_Object = MibTable
hgmpNTDPInterfaceTable = _HgmpNTDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 9)
)
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceTable.setStatus("current")
_HgmpNTDPInterfaceEntry_Object = MibTableRow
hgmpNTDPInterfaceEntry = _HgmpNTDPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 9, 1)
)
hgmpNTDPInterfaceEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceEntry.setStatus("current")


class _HgmpNTDPInterfaceIfIndex_Type(Integer32):
    """Custom type hgmpNTDPInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPInterfaceIfIndex_Type.__name__ = "Integer32"
_HgmpNTDPInterfaceIfIndex_Object = MibTableColumn
hgmpNTDPInterfaceIfIndex = _HgmpNTDPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 9, 1, 1),
    _HgmpNTDPInterfaceIfIndex_Type()
)
hgmpNTDPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceIfIndex.setStatus("current")


class _HgmpNTDPInterfaceEnable_Type(Integer32):
    """Custom type hgmpNTDPInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HgmpNTDPInterfaceEnable_Type.__name__ = "Integer32"
_HgmpNTDPInterfaceEnable_Object = MibTableColumn
hgmpNTDPInterfaceEnable = _HgmpNTDPInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 9, 1, 2),
    _HgmpNTDPInterfaceEnable_Type()
)
hgmpNTDPInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceEnable.setStatus("current")
_HgmpNTDPCacheTable_Object = MibTable
hgmpNTDPCacheTable = _HgmpNTDPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10)
)
if mibBuilder.loadTexts:
    hgmpNTDPCacheTable.setStatus("current")
_HgmpNTDPCacheEntry_Object = MibTableRow
hgmpNTDPCacheEntry = _HgmpNTDPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1)
)
hgmpNTDPCacheEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPCacheHashIndex"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPCacheDeviceID"),
)
if mibBuilder.loadTexts:
    hgmpNTDPCacheEntry.setStatus("current")


class _HgmpNTDPCacheHashIndex_Type(Integer32):
    """Custom type hgmpNTDPCacheHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HgmpNTDPCacheHashIndex_Type.__name__ = "Integer32"
_HgmpNTDPCacheHashIndex_Object = MibTableColumn
hgmpNTDPCacheHashIndex = _HgmpNTDPCacheHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 1),
    _HgmpNTDPCacheHashIndex_Type()
)
hgmpNTDPCacheHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheHashIndex.setStatus("current")


class _HgmpNTDPCacheDeviceID_Type(OctetString):
    """Custom type hgmpNTDPCacheDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpNTDPCacheDeviceID_Type.__name__ = "OctetString"
_HgmpNTDPCacheDeviceID_Object = MibTableColumn
hgmpNTDPCacheDeviceID = _HgmpNTDPCacheDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 2),
    _HgmpNTDPCacheDeviceID_Type()
)
hgmpNTDPCacheDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheDeviceID.setStatus("current")
_HgmpNTDPCacheClusterName_Type = OctetString
_HgmpNTDPCacheClusterName_Object = MibTableColumn
hgmpNTDPCacheClusterName = _HgmpNTDPCacheClusterName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 3),
    _HgmpNTDPCacheClusterName_Type()
)
hgmpNTDPCacheClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheClusterName.setStatus("current")


class _HgmpNTDPCacheClusterRole_Type(Integer32):
    """Custom type hgmpNTDPCacheClusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("roleBKSW", 3),
          ("roleCASW", 16),
          ("roleCOSW", 1),
          ("roleMSW", 2),
          ("roleUNISW", 17))
    )


_HgmpNTDPCacheClusterRole_Type.__name__ = "Integer32"
_HgmpNTDPCacheClusterRole_Object = MibTableColumn
hgmpNTDPCacheClusterRole = _HgmpNTDPCacheClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 4),
    _HgmpNTDPCacheClusterRole_Type()
)
hgmpNTDPCacheClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheClusterRole.setStatus("current")
_HgmpNTDPCacheCapabilities_Type = Integer32
_HgmpNTDPCacheCapabilities_Object = MibTableColumn
hgmpNTDPCacheCapabilities = _HgmpNTDPCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 5),
    _HgmpNTDPCacheCapabilities_Type()
)
hgmpNTDPCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheCapabilities.setStatus("current")
_HgmpNTDPCacheVersion_Type = OctetString
_HgmpNTDPCacheVersion_Object = MibTableColumn
hgmpNTDPCacheVersion = _HgmpNTDPCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 6),
    _HgmpNTDPCacheVersion_Type()
)
hgmpNTDPCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheVersion.setStatus("current")
_HgmpNTDPCachePlatform_Type = OctetString
_HgmpNTDPCachePlatform_Object = MibTableColumn
hgmpNTDPCachePlatform = _HgmpNTDPCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 7),
    _HgmpNTDPCachePlatform_Type()
)
hgmpNTDPCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCachePlatform.setStatus("current")
_HgmpNTDPCacheMngVLAN_Type = Integer32
_HgmpNTDPCacheMngVLAN_Object = MibTableColumn
hgmpNTDPCacheMngVLAN = _HgmpNTDPCacheMngVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 8),
    _HgmpNTDPCacheMngVLAN_Type()
)
hgmpNTDPCacheMngVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheMngVLAN.setStatus("current")
_HgmpNTDPCacheHop_Type = Integer32
_HgmpNTDPCacheHop_Object = MibTableColumn
hgmpNTDPCacheHop = _HgmpNTDPCacheHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 10, 1, 9),
    _HgmpNTDPCacheHop_Type()
)
hgmpNTDPCacheHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheHop.setStatus("current")
_HgmpNTDPTopTable_Object = MibTable
hgmpNTDPTopTable = _HgmpNTDPTopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11)
)
if mibBuilder.loadTexts:
    hgmpNTDPTopTable.setStatus("current")
_HgmpNTDPTopEntry_Object = MibTableRow
hgmpNTDPTopEntry = _HgmpNTDPTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1)
)
hgmpNTDPTopEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopHashIndex"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartDevID"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeIndex"),
)
if mibBuilder.loadTexts:
    hgmpNTDPTopEntry.setStatus("current")


class _HgmpNTDPTopHashIndex_Type(Integer32):
    """Custom type hgmpNTDPTopHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HgmpNTDPTopHashIndex_Type.__name__ = "Integer32"
_HgmpNTDPTopHashIndex_Object = MibTableColumn
hgmpNTDPTopHashIndex = _HgmpNTDPTopHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 1),
    _HgmpNTDPTopHashIndex_Type()
)
hgmpNTDPTopHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopHashIndex.setStatus("current")


class _HgmpNTDPTopEdgeStartDevID_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeStartDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpNTDPTopEdgeStartDevID_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeStartDevID_Object = MibTableColumn
hgmpNTDPTopEdgeStartDevID = _HgmpNTDPTopEdgeStartDevID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 2),
    _HgmpNTDPTopEdgeStartDevID_Type()
)
hgmpNTDPTopEdgeStartDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartDevID.setStatus("current")


class _HgmpNTDPTopEdgeIndex_Type(Integer32):
    """Custom type hgmpNTDPTopEdgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPTopEdgeIndex_Type.__name__ = "Integer32"
_HgmpNTDPTopEdgeIndex_Object = MibTableColumn
hgmpNTDPTopEdgeIndex = _HgmpNTDPTopEdgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 3),
    _HgmpNTDPTopEdgeIndex_Type()
)
hgmpNTDPTopEdgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeIndex.setStatus("current")


class _HgmpNTDPTopEdgeEndDevID_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeEndDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpNTDPTopEdgeEndDevID_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeEndDevID_Object = MibTableColumn
hgmpNTDPTopEdgeEndDevID = _HgmpNTDPTopEdgeEndDevID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 4),
    _HgmpNTDPTopEdgeEndDevID_Type()
)
hgmpNTDPTopEdgeEndDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeEndDevID.setStatus("current")


class _HgmpNTDPTopEdgeStartPort_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeStartPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HgmpNTDPTopEdgeStartPort_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeStartPort_Object = MibTableColumn
hgmpNTDPTopEdgeStartPort = _HgmpNTDPTopEdgeStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 5),
    _HgmpNTDPTopEdgeStartPort_Type()
)
hgmpNTDPTopEdgeStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPort.setStatus("current")


class _HgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):
    """Custom type hgmpNTDPTopEdgeStartPortFullDuplex based on Integer32"""
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


_HgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__ = "Integer32"
_HgmpNTDPTopEdgeStartPortFullDuplex_Object = MibTableColumn
hgmpNTDPTopEdgeStartPortFullDuplex = _HgmpNTDPTopEdgeStartPortFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 6),
    _HgmpNTDPTopEdgeStartPortFullDuplex_Type()
)
hgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPortFullDuplex.setStatus("current")
_HgmpNTDPTopEdgeStartPortSpeed_Type = Integer32
_HgmpNTDPTopEdgeStartPortSpeed_Object = MibTableColumn
hgmpNTDPTopEdgeStartPortSpeed = _HgmpNTDPTopEdgeStartPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 7),
    _HgmpNTDPTopEdgeStartPortSpeed_Type()
)
hgmpNTDPTopEdgeStartPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPortSpeed.setStatus("current")


class _HgmpNTDPTopEdgeEndPort_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeEndPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HgmpNTDPTopEdgeEndPort_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeEndPort_Object = MibTableColumn
hgmpNTDPTopEdgeEndPort = _HgmpNTDPTopEdgeEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 8),
    _HgmpNTDPTopEdgeEndPort_Type()
)
hgmpNTDPTopEdgeEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeEndPort.setStatus("current")
_HgmpNTDPTopEdgeStartPortIfIndex_Type = Integer32
_HgmpNTDPTopEdgeStartPortIfIndex_Object = MibTableColumn
hgmpNTDPTopEdgeStartPortIfIndex = _HgmpNTDPTopEdgeStartPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 9),
    _HgmpNTDPTopEdgeStartPortIfIndex_Type()
)
hgmpNTDPTopEdgeStartPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPortIfIndex.setStatus("current")
_HgmpNTDPTopEdgeEndPortIfIndex_Type = Integer32
_HgmpNTDPTopEdgeEndPortIfIndex_Object = MibTableColumn
hgmpNTDPTopEdgeEndPortIfIndex = _HgmpNTDPTopEdgeEndPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 11, 1, 10),
    _HgmpNTDPTopEdgeEndPortIfIndex_Type()
)
hgmpNTDPTopEdgeEndPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeEndPortIfIndex.setStatus("current")


class _HgmpNTDPExplore_Type(Integer32):
    """Custom type hgmpNTDPExplore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("start", 1))
    )


_HgmpNTDPExplore_Type.__name__ = "Integer32"
_HgmpNTDPExplore_Object = MibScalar
hgmpNTDPExplore = _HgmpNTDPExplore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 12),
    _HgmpNTDPExplore_Type()
)
hgmpNTDPExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPExplore.setStatus("current")
_HgmpNTDPTopoLinkTable_Object = MibTable
hgmpNTDPTopoLinkTable = _HgmpNTDPTopoLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13)
)
if mibBuilder.loadTexts:
    hgmpNTDPTopoLinkTable.setStatus("current")
_HgmpNTDPTopoLinkEntry_Object = MibTableRow
hgmpNTDPTopoLinkEntry = _HgmpNTDPTopoLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1)
)
hgmpNTDPTopoLinkEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopoLocalDeviceID"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopoLocalPortName"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopoNbrDeviceID"),
    (0, "HUAWEI-HGMP-MIB", "hgmpNTDPTopoNbrPortName"),
)
if mibBuilder.loadTexts:
    hgmpNTDPTopoLinkEntry.setStatus("current")


class _HgmpNTDPTopoLocalDeviceID_Type(OctetString):
    """Custom type hgmpNTDPTopoLocalDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpNTDPTopoLocalDeviceID_Type.__name__ = "OctetString"
_HgmpNTDPTopoLocalDeviceID_Object = MibTableColumn
hgmpNTDPTopoLocalDeviceID = _HgmpNTDPTopoLocalDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1, 1),
    _HgmpNTDPTopoLocalDeviceID_Type()
)
hgmpNTDPTopoLocalDeviceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpNTDPTopoLocalDeviceID.setStatus("current")


class _HgmpNTDPTopoLocalPortName_Type(OctetString):
    """Custom type hgmpNTDPTopoLocalPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HgmpNTDPTopoLocalPortName_Type.__name__ = "OctetString"
_HgmpNTDPTopoLocalPortName_Object = MibTableColumn
hgmpNTDPTopoLocalPortName = _HgmpNTDPTopoLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1, 2),
    _HgmpNTDPTopoLocalPortName_Type()
)
hgmpNTDPTopoLocalPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpNTDPTopoLocalPortName.setStatus("current")


class _HgmpNTDPTopoNbrDeviceID_Type(OctetString):
    """Custom type hgmpNTDPTopoNbrDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpNTDPTopoNbrDeviceID_Type.__name__ = "OctetString"
_HgmpNTDPTopoNbrDeviceID_Object = MibTableColumn
hgmpNTDPTopoNbrDeviceID = _HgmpNTDPTopoNbrDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1, 3),
    _HgmpNTDPTopoNbrDeviceID_Type()
)
hgmpNTDPTopoNbrDeviceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpNTDPTopoNbrDeviceID.setStatus("current")


class _HgmpNTDPTopoNbrPortName_Type(OctetString):
    """Custom type hgmpNTDPTopoNbrPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HgmpNTDPTopoNbrPortName_Type.__name__ = "OctetString"
_HgmpNTDPTopoNbrPortName_Object = MibTableColumn
hgmpNTDPTopoNbrPortName = _HgmpNTDPTopoNbrPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1, 4),
    _HgmpNTDPTopoNbrPortName_Type()
)
hgmpNTDPTopoNbrPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpNTDPTopoNbrPortName.setStatus("current")


class _HgmpNTDPTopoLinkStatus_Type(Integer32):
    """Custom type hgmpNTDPTopoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_HgmpNTDPTopoLinkStatus_Type.__name__ = "Integer32"
_HgmpNTDPTopoLinkStatus_Object = MibTableColumn
hgmpNTDPTopoLinkStatus = _HgmpNTDPTopoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 13, 1, 5),
    _HgmpNTDPTopoLinkStatus_Type()
)
hgmpNTDPTopoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopoLinkStatus.setStatus("current")
_HgmpNTDPNotifications_ObjectIdentity = ObjectIdentity
hgmpNTDPNotifications = _HgmpNTDPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 14)
)
_HwNDPObject_ObjectIdentity = ObjectIdentity
hwNDPObject = _HwNDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5)
)


class _HwNDPStatus_Type(Integer32):
    """Custom type hwNDPStatus based on Integer32"""
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


_HwNDPStatus_Type.__name__ = "Integer32"
_HwNDPStatus_Object = MibScalar
hwNDPStatus = _HwNDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 1),
    _HwNDPStatus_Type()
)
hwNDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPStatus.setStatus("current")


class _HwNDPHelloTimer_Type(Integer32):
    """Custom type hwNDPHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_HwNDPHelloTimer_Type.__name__ = "Integer32"
_HwNDPHelloTimer_Object = MibScalar
hwNDPHelloTimer = _HwNDPHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 2),
    _HwNDPHelloTimer_Type()
)
hwNDPHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPHelloTimer.setStatus("current")


class _HwNDPAgingTime_Type(Integer32):
    """Custom type hwNDPAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 255),
    )


_HwNDPAgingTime_Type.__name__ = "Integer32"
_HwNDPAgingTime_Object = MibScalar
hwNDPAgingTime = _HwNDPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 3),
    _HwNDPAgingTime_Type()
)
hwNDPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPAgingTime.setStatus("current")
_HwNDPChange_Type = Counter32
_HwNDPChange_Object = MibScalar
hwNDPChange = _HwNDPChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 4),
    _HwNDPChange_Type()
)
hwNDPChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPChange.setStatus("current")
_HwNDPPortTable_Object = MibTable
hwNDPPortTable = _HwNDPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 5)
)
if mibBuilder.loadTexts:
    hwNDPPortTable.setStatus("current")
_HwNDPPortEntry_Object = MibTableRow
hwNDPPortEntry = _HwNDPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 5, 1)
)
hwNDPPortEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hwNDPIfIndex"),
)
if mibBuilder.loadTexts:
    hwNDPPortEntry.setStatus("current")


class _HwNDPIfIndex_Type(Integer32):
    """Custom type hwNDPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNDPIfIndex_Type.__name__ = "Integer32"
_HwNDPIfIndex_Object = MibTableColumn
hwNDPIfIndex = _HwNDPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 5, 1, 1),
    _HwNDPIfIndex_Type()
)
hwNDPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPIfIndex.setStatus("current")


class _HwNDPPortStatus_Type(Integer32):
    """Custom type hwNDPPortStatus based on Integer32"""
    defaultValue = 1

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


_HwNDPPortStatus_Type.__name__ = "Integer32"
_HwNDPPortStatus_Object = MibTableColumn
hwNDPPortStatus = _HwNDPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 5, 1, 2),
    _HwNDPPortStatus_Type()
)
hwNDPPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPPortStatus.setStatus("current")
_HwNDPPortNbTable_Object = MibTable
hwNDPPortNbTable = _HwNDPPortNbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6)
)
if mibBuilder.loadTexts:
    hwNDPPortNbTable.setStatus("current")
_HwNDPPortNbEntry_Object = MibTableRow
hwNDPPortNbEntry = _HwNDPPortNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1)
)
hwNDPPortNbEntry.setIndexNames(
    (0, "HUAWEI-HGMP-MIB", "hwNDPIfIndex"),
    (0, "HUAWEI-HGMP-MIB", "hwNDPPortNbDeviceId"),
    (0, "HUAWEI-HGMP-MIB", "hwNDPPortNbPortName"),
)
if mibBuilder.loadTexts:
    hwNDPPortNbEntry.setStatus("current")


class _HwNDPPortNbDeviceId_Type(OctetString):
    """Custom type hwNDPPortNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HwNDPPortNbDeviceId_Type.__name__ = "OctetString"
_HwNDPPortNbDeviceId_Object = MibTableColumn
hwNDPPortNbDeviceId = _HwNDPPortNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 1),
    _HwNDPPortNbDeviceId_Type()
)
hwNDPPortNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbDeviceId.setStatus("current")


class _HwNDPPortNbPortName_Type(OctetString):
    """Custom type hwNDPPortNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNDPPortNbPortName_Type.__name__ = "OctetString"
_HwNDPPortNbPortName_Object = MibTableColumn
hwNDPPortNbPortName = _HwNDPPortNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 2),
    _HwNDPPortNbPortName_Type()
)
hwNDPPortNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbPortName.setStatus("current")
_HwNDPPortNbDeviceName_Type = OctetString
_HwNDPPortNbDeviceName_Object = MibTableColumn
hwNDPPortNbDeviceName = _HwNDPPortNbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 3),
    _HwNDPPortNbDeviceName_Type()
)
hwNDPPortNbDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbDeviceName.setStatus("current")


class _HwNDPPortNbPortMode_Type(Integer32):
    """Custom type hwNDPPortNbPortMode based on Integer32"""
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


_HwNDPPortNbPortMode_Type.__name__ = "Integer32"
_HwNDPPortNbPortMode_Object = MibTableColumn
hwNDPPortNbPortMode = _HwNDPPortNbPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 4),
    _HwNDPPortNbPortMode_Type()
)
hwNDPPortNbPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbPortMode.setStatus("current")
_HwNDPPortNbProductVer_Type = OctetString
_HwNDPPortNbProductVer_Object = MibTableColumn
hwNDPPortNbProductVer = _HwNDPPortNbProductVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 5),
    _HwNDPPortNbProductVer_Type()
)
hwNDPPortNbProductVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbProductVer.setStatus("current")
_HwNDPPortNbHardVer_Type = OctetString
_HwNDPPortNbHardVer_Object = MibTableColumn
hwNDPPortNbHardVer = _HwNDPPortNbHardVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 6),
    _HwNDPPortNbHardVer_Type()
)
hwNDPPortNbHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbHardVer.setStatus("current")
_HwNDPPortNbBootromVer_Type = OctetString
_HwNDPPortNbBootromVer_Object = MibTableColumn
hwNDPPortNbBootromVer = _HwNDPPortNbBootromVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 7),
    _HwNDPPortNbBootromVer_Type()
)
hwNDPPortNbBootromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbBootromVer.setStatus("current")
_HwNDPPortNbSoftVer_Type = OctetString
_HwNDPPortNbSoftVer_Object = MibTableColumn
hwNDPPortNbSoftVer = _HwNDPPortNbSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 8),
    _HwNDPPortNbSoftVer_Type()
)
hwNDPPortNbSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbSoftVer.setStatus("current")


class _HwNDPPortNbAgingtime_Type(Integer32):
    """Custom type hwNDPPortNbAgingtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HwNDPPortNbAgingtime_Type.__name__ = "Integer32"
_HwNDPPortNbAgingtime_Object = MibTableColumn
hwNDPPortNbAgingtime = _HwNDPPortNbAgingtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 6, 1, 9),
    _HwNDPPortNbAgingtime_Type()
)
hwNDPPortNbAgingtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbAgingtime.setStatus("current")
_HwNDPTrunkMemberEnable_Type = EnabledStatus
_HwNDPTrunkMemberEnable_Object = MibScalar
hwNDPTrunkMemberEnable = _HwNDPTrunkMemberEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 5, 7),
    _HwNDPTrunkMemberEnable_Type()
)
hwNDPTrunkMemberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPTrunkMemberEnable.setStatus("current")
_HwClusterConformance_ObjectIdentity = ObjectIdentity
hwClusterConformance = _HwClusterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6)
)
_HwClusterGroups_ObjectIdentity = ObjectIdentity
hwClusterGroups = _HwClusterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6, 1)
)
_HwClusterCompliances_ObjectIdentity = ObjectIdentity
hwClusterCompliances = _HwClusterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-HGMP-MIB", "hgmpSetVLANSecurity"),
        ("HUAWEI-HGMP-MIB", "hgmpHandShakeInterval"),
        ("HUAWEI-HGMP-MIB", "hgmpHandShakeHoldtime"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberTableChange"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberDisconRate"),
        ("HUAWEI-HGMP-MIB", "hgmpCmdLanswitchFlag"),
        ("HUAWEI-HGMP-MIB", "hgmpCmdClusterName"),
        ("HUAWEI-HGMP-MIB", "hgmpMngPriIpSegCMIP"),
        ("HUAWEI-HGMP-MIB", "hgmpMngPriIpMask"),
        ("HUAWEI-HGMP-MIB", "hgmpFtpServer"),
        ("HUAWEI-HGMP-MIB", "hgmpTftpServer"),
        ("HUAWEI-HGMP-MIB", "hgmpSnmpHost"),
        ("HUAWEI-HGMP-MIB", "hgmpLogHost"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberSerial"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberIpAddr"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberName"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberPassword"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberPlatform"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDisconCount"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberEnrollTime"),
        ("HUAWEI-HGMP-MIB", "hgmpGrpMemberOperate"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberResetMAC"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberEraseflash"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterRole"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterMaxPoolNum"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterCmdSwMac"),
        ("HUAWEI-HGMP-MIB", "hgmpRun"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterAutojoin"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterDiscAgingTime"),
        ("HUAWEI-HGMP-MIB", "hgmpPlugAndPlayStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpMultiMacAddress"),
        ("HUAWEI-HGMP-MIB", "hgmpManageVlan"),
        ("HUAWEI-HGMP-MIB", "hgmpSftpServer"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpAdminRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNdpResult"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpAdminRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpUnrelatedPortNtdpResult"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeFileType"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeFileName"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchUpgradeResult"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchRebootGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchRebootGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchRebootRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchRebootResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchRebootResult"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSaveGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSaveGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSaveRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSaveResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSaveResult"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileGroupType"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileGroupValue"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileRowStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileResultMemberId"),
        ("HUAWEI-HGMP-MIB", "hgmpBatchSynchronizeCfgFileResult"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberRebootTimeoutValue"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberTableChange"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberDisconRate"),
        ("HUAWEI-HGMP-MIB", "hgmpMainLanswitchFlag"),
        ("HUAWEI-HGMP-MIB", "hgmpStackIpPoolStartIP"),
        ("HUAWEI-HGMP-MIB", "hgmpStackIpPoolLength"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberSerial"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberIpAddr"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberName"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberPassword"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberPlatform"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberStatus"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberDisconCount"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberEnrollTime"),
        ("HUAWEI-HGMP-MIB", "hgmpStackRole"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMaxPoolNum"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMainSwMac"),
        ("HUAWEI-HGMP-MIB", "hgmpStackIpPoolMask"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCollectTopTime"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPHopRange"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPRun"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPPortDelay"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPHopDelay"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPLastTopCollectDuration"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheChange"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTOPTableChange"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPInterfaceIfIndex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPInterfaceEnable"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheHashIndex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheDeviceID"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterName"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterRole"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheCapabilities"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheVersion"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCachePlatform"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheMngVLAN"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheHop"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopHashIndex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartDevID"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeIndex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeEndDevID"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartPort"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartPortFullDuplex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartPortSpeed"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeEndPort"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartPortIfIndex"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeEndPortIfIndex"),
        ("HUAWEI-HGMP-MIB", "hwNDPStatus"),
        ("HUAWEI-HGMP-MIB", "hwNDPHelloTimer"),
        ("HUAWEI-HGMP-MIB", "hwNDPAgingTime"),
        ("HUAWEI-HGMP-MIB", "hwNDPChange"),
        ("HUAWEI-HGMP-MIB", "hwNDPIfIndex"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortStatus"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbDeviceId"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbPortName"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbDeviceName"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbPortMode"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbProductVer"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbHardVer"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbBootromVer"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbSoftVer"),
        ("HUAWEI-HGMP-MIB", "hwNDPPortNbAgingtime"),
        ("HUAWEI-HGMP-MIB", "hgmpClusterVersion"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPExplore"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopoLinkStatus"),
        ("HUAWEI-HGMP-MIB", "hwNDPTrunkMemberEnable"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

hgmpMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0, 1)
)
hgmpMemberfailure.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpMemberfailure.setStatus(
        "current"
    )

hgmpMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0, 2)
)
hgmpMemberRecover.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpMemberRecover.setStatus(
        "current"
    )

hgmpMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0, 3)
)
hgmpMemberStatusChange.setObjects(
      *(("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hgmpMemberStatusChange.setStatus(
        "current"
    )

hgmpNetTopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0, 4)
)
hgmpNetTopChange.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpNetTopChange.setStatus(
        "current"
    )

hgmpMemberAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 1, 0, 6)
)
hgmpMemberAdd.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpMemberAdd.setStatus(
        "current"
    )

hgmpStackMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 0, 1)
)
hgmpStackMemberfailure.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpStackMemberfailure.setStatus(
        "current"
    )

hgmpStackMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 0, 2)
)
hgmpStackMemberRecover.setObjects(
    ("HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpStackMemberRecover.setStatus(
        "current"
    )

hgmpStackMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 2, 0, 3)
)
hgmpStackMemberStatusChange.setObjects(
      *(("HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hgmpStackMemberStatusChange.setStatus(
        "current"
    )

hgmpNTDPTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 4, 14, 1)
)
if mibBuilder.loadTexts:
    hgmpNTDPTopoChange.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6, 1, 2)
)
currentNotificationGroup.setObjects(
      *(("HUAWEI-HGMP-MIB", "hgmpMemberfailure"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberRecover"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberStatusChange"),
        ("HUAWEI-HGMP-MIB", "hgmpMemberAdd"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberfailure"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberRecover"),
        ("HUAWEI-HGMP-MIB", "hgmpStackMemberStatusChange"),
        ("HUAWEI-HGMP-MIB", "hgmpNetTopChange"),
        ("HUAWEI-HGMP-MIB", "hgmpNTDPTopoChange"))
)
if mibBuilder.loadTexts:
    currentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 7, 6, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-HGMP-MIB",
    **{"hwCluster": hwCluster,
       "hwClusterObject": hwClusterObject,
       "hgmpEventsV2": hgmpEventsV2,
       "hgmpMemberfailure": hgmpMemberfailure,
       "hgmpMemberRecover": hgmpMemberRecover,
       "hgmpMemberStatusChange": hgmpMemberStatusChange,
       "hgmpNetTopChange": hgmpNetTopChange,
       "hgmpMemberAdd": hgmpMemberAdd,
       "hgmpSetVLANSecurity": hgmpSetVLANSecurity,
       "hgmpHandShakeInterval": hgmpHandShakeInterval,
       "hgmpHandShakeHoldtime": hgmpHandShakeHoldtime,
       "hgmpGrpMemberTableChange": hgmpGrpMemberTableChange,
       "hgmpMemberDisconRate": hgmpMemberDisconRate,
       "hgmpCmdLanswitchFlag": hgmpCmdLanswitchFlag,
       "hgmpCmdClusterName": hgmpCmdClusterName,
       "hgmpMngPriIpSegCMIP": hgmpMngPriIpSegCMIP,
       "hgmpMngPriIpMask": hgmpMngPriIpMask,
       "hgmpFtpServer": hgmpFtpServer,
       "hgmpTftpServer": hgmpTftpServer,
       "hgmpSnmpHost": hgmpSnmpHost,
       "hgmpLogHost": hgmpLogHost,
       "hgmpGrpMemberTable": hgmpGrpMemberTable,
       "hgmpGrpMemberEntry": hgmpGrpMemberEntry,
       "hgmpGrpMemberDeviceId": hgmpGrpMemberDeviceId,
       "hgmpGrpMemberSerial": hgmpGrpMemberSerial,
       "hgmpGrpMemberIpAddr": hgmpGrpMemberIpAddr,
       "hgmpGrpMemberName": hgmpGrpMemberName,
       "hgmpGrpMemberPassword": hgmpGrpMemberPassword,
       "hgmpGrpMemberPlatform": hgmpGrpMemberPlatform,
       "hgmpGrpMemberStatus": hgmpGrpMemberStatus,
       "hgmpGrpMemberDisconCount": hgmpGrpMemberDisconCount,
       "hgmpGrpMemberEnrollTime": hgmpGrpMemberEnrollTime,
       "hgmpGrpMemberOperate": hgmpGrpMemberOperate,
       "hgmpMemberResetTable": hgmpMemberResetTable,
       "hgmpMemberResetEntry": hgmpMemberResetEntry,
       "hgmpMemberResetMAC": hgmpMemberResetMAC,
       "hgmpMemberEraseflash": hgmpMemberEraseflash,
       "hgmpClusterRole": hgmpClusterRole,
       "hgmpClusterMaxPoolNum": hgmpClusterMaxPoolNum,
       "hgmpClusterCmdSwMac": hgmpClusterCmdSwMac,
       "hgmpRun": hgmpRun,
       "hgmpClusterAutojoin": hgmpClusterAutojoin,
       "hgmpClusterDiscAgingTime": hgmpClusterDiscAgingTime,
       "hgmpPlugAndPlayStatus": hgmpPlugAndPlayStatus,
       "hgmpMultiMacAddress": hgmpMultiMacAddress,
       "hgmpManageVlan": hgmpManageVlan,
       "hgmpSftpServer": hgmpSftpServer,
       "hgmpUnrelatedPortNdpAdminTable": hgmpUnrelatedPortNdpAdminTable,
       "hgmpUnrelatedPortNdpAdminEntry": hgmpUnrelatedPortNdpAdminEntry,
       "hgmpUnrelatedPortNdpAdminCmdId": hgmpUnrelatedPortNdpAdminCmdId,
       "hgmpUnrelatedPortNdpAdminGroupType": hgmpUnrelatedPortNdpAdminGroupType,
       "hgmpUnrelatedPortNdpAdminGroupValue": hgmpUnrelatedPortNdpAdminGroupValue,
       "hgmpUnrelatedPortNdpAdminStatus": hgmpUnrelatedPortNdpAdminStatus,
       "hgmpUnrelatedPortNdpAdminRowStatus": hgmpUnrelatedPortNdpAdminRowStatus,
       "hgmpUnrelatedPortNdpResultTable": hgmpUnrelatedPortNdpResultTable,
       "hgmpUnrelatedPortNdpResultEntry": hgmpUnrelatedPortNdpResultEntry,
       "hgmpUnrelatedPortNdpResultMemberMac": hgmpUnrelatedPortNdpResultMemberMac,
       "hgmpUnrelatedPortNdpResultMemberId": hgmpUnrelatedPortNdpResultMemberId,
       "hgmpUnrelatedPortNdpResult": hgmpUnrelatedPortNdpResult,
       "hgmpUnrelatedPortNtdpAdminTable": hgmpUnrelatedPortNtdpAdminTable,
       "hgmpUnrelatedPortNtdpAdminEntry": hgmpUnrelatedPortNtdpAdminEntry,
       "hgmpUnrelatedPortNtdpAdminCmdId": hgmpUnrelatedPortNtdpAdminCmdId,
       "hgmpUnrelatedPortNtdpAdminGroupType": hgmpUnrelatedPortNtdpAdminGroupType,
       "hgmpUnrelatedPortNtdpAdminGroupValue": hgmpUnrelatedPortNtdpAdminGroupValue,
       "hgmpUnrelatedPortNtdpAdminStatus": hgmpUnrelatedPortNtdpAdminStatus,
       "hgmpUnrelatedPortNtdpAdminRowStatus": hgmpUnrelatedPortNtdpAdminRowStatus,
       "hgmpUnrelatedPortNtdpResultTable": hgmpUnrelatedPortNtdpResultTable,
       "hgmpUnrelatedPortNtdpResultEntry": hgmpUnrelatedPortNtdpResultEntry,
       "hgmpUnrelatedPortNtdpResultMemberMac": hgmpUnrelatedPortNtdpResultMemberMac,
       "hgmpUnrelatedPortNtdpResultMemberId": hgmpUnrelatedPortNtdpResultMemberId,
       "hgmpUnrelatedPortNtdpResult": hgmpUnrelatedPortNtdpResult,
       "hgmpBatchUpgradeTable": hgmpBatchUpgradeTable,
       "hgmpBatchUpgradeEntry": hgmpBatchUpgradeEntry,
       "hgmpBatchUpgradeCmdId": hgmpBatchUpgradeCmdId,
       "hgmpBatchUpgradeGroupType": hgmpBatchUpgradeGroupType,
       "hgmpBatchUpgradeGroupValue": hgmpBatchUpgradeGroupValue,
       "hgmpBatchUpgradeFileType": hgmpBatchUpgradeFileType,
       "hgmpBatchUpgradeFileName": hgmpBatchUpgradeFileName,
       "hgmpBatchUpgradeRowStatus": hgmpBatchUpgradeRowStatus,
       "hgmpBatchUpgradeResultTable": hgmpBatchUpgradeResultTable,
       "hgmpBatchUpgradeResultEntry": hgmpBatchUpgradeResultEntry,
       "hgmpBatchUpgradeResultMemberMac": hgmpBatchUpgradeResultMemberMac,
       "hgmpBatchUpgradeResultMemberId": hgmpBatchUpgradeResultMemberId,
       "hgmpBatchUpgradeResult": hgmpBatchUpgradeResult,
       "hgmpBatchRebootTable": hgmpBatchRebootTable,
       "hgmpBatchRebootEntry": hgmpBatchRebootEntry,
       "hgmpBatchRebootCmdId": hgmpBatchRebootCmdId,
       "hgmpBatchRebootGroupType": hgmpBatchRebootGroupType,
       "hgmpBatchRebootGroupValue": hgmpBatchRebootGroupValue,
       "hgmpBatchRebootRowStatus": hgmpBatchRebootRowStatus,
       "hgmpBatchRebootResultTable": hgmpBatchRebootResultTable,
       "hgmpBatchRebootResultEntry": hgmpBatchRebootResultEntry,
       "hgmpBatchRebootResultMemberMac": hgmpBatchRebootResultMemberMac,
       "hgmpBatchRebootResultMemberId": hgmpBatchRebootResultMemberId,
       "hgmpBatchRebootResult": hgmpBatchRebootResult,
       "hgmpBatchSaveTable": hgmpBatchSaveTable,
       "hgmpBatchSaveEntry": hgmpBatchSaveEntry,
       "hgmpBatchSaveCmdId": hgmpBatchSaveCmdId,
       "hgmpBatchSaveGroupType": hgmpBatchSaveGroupType,
       "hgmpBatchSaveGroupValue": hgmpBatchSaveGroupValue,
       "hgmpBatchSaveRowStatus": hgmpBatchSaveRowStatus,
       "hgmpBatchSaveResultTable": hgmpBatchSaveResultTable,
       "hgmpBatchSaveResultEntry": hgmpBatchSaveResultEntry,
       "hgmpBatchSaveResultMemberMac": hgmpBatchSaveResultMemberMac,
       "hgmpBatchSaveResultMemberId": hgmpBatchSaveResultMemberId,
       "hgmpBatchSaveResult": hgmpBatchSaveResult,
       "hgmpBatchSynchronizeCfgFileTable": hgmpBatchSynchronizeCfgFileTable,
       "hgmpBatchSynchronizeCfgFileEntry": hgmpBatchSynchronizeCfgFileEntry,
       "hgmpBatchSynchronizeCfgFileCmdId": hgmpBatchSynchronizeCfgFileCmdId,
       "hgmpBatchSynchronizeCfgFileGroupType": hgmpBatchSynchronizeCfgFileGroupType,
       "hgmpBatchSynchronizeCfgFileGroupValue": hgmpBatchSynchronizeCfgFileGroupValue,
       "hgmpBatchSynchronizeCfgFileRowStatus": hgmpBatchSynchronizeCfgFileRowStatus,
       "hgmpBatchSynchronizeCfgFileResultTable": hgmpBatchSynchronizeCfgFileResultTable,
       "hgmpBatchSynchronizeCfgFileResultEntry": hgmpBatchSynchronizeCfgFileResultEntry,
       "hgmpBatchSynchronizeCfgFileResultMemberMac": hgmpBatchSynchronizeCfgFileResultMemberMac,
       "hgmpBatchSynchronizeCfgFileResultMemberId": hgmpBatchSynchronizeCfgFileResultMemberId,
       "hgmpBatchSynchronizeCfgFileResult": hgmpBatchSynchronizeCfgFileResult,
       "hgmpMemberRebootTimeoutValue": hgmpMemberRebootTimeoutValue,
       "hgmpClusterVersion": hgmpClusterVersion,
       "hwStackObject": hwStackObject,
       "hgmpStackEventsV2": hgmpStackEventsV2,
       "hgmpStackMemberfailure": hgmpStackMemberfailure,
       "hgmpStackMemberRecover": hgmpStackMemberRecover,
       "hgmpStackMemberStatusChange": hgmpStackMemberStatusChange,
       "hgmpStackMemberTableChange": hgmpStackMemberTableChange,
       "hgmpStackMemberDisconRate": hgmpStackMemberDisconRate,
       "hgmpMainLanswitchFlag": hgmpMainLanswitchFlag,
       "hgmpStackIpPoolStartIP": hgmpStackIpPoolStartIP,
       "hgmpStackIpPoolLength": hgmpStackIpPoolLength,
       "hgmpStackMemberTable": hgmpStackMemberTable,
       "hgmpStackMemberEntry": hgmpStackMemberEntry,
       "hgmpStackMemberDeviceId": hgmpStackMemberDeviceId,
       "hgmpStackMemberSerial": hgmpStackMemberSerial,
       "hgmpStackMemberIpAddr": hgmpStackMemberIpAddr,
       "hgmpStackMemberName": hgmpStackMemberName,
       "hgmpStackMemberPassword": hgmpStackMemberPassword,
       "hgmpStackMemberPlatform": hgmpStackMemberPlatform,
       "hgmpStackMemberStatus": hgmpStackMemberStatus,
       "hgmpStackMemberDisconCount": hgmpStackMemberDisconCount,
       "hgmpStackMemberEnrollTime": hgmpStackMemberEnrollTime,
       "hgmpStackRole": hgmpStackRole,
       "hgmpStackMaxPoolNum": hgmpStackMaxPoolNum,
       "hgmpStackMainSwMac": hgmpStackMainSwMac,
       "hgmpStackIpPoolMask": hgmpStackIpPoolMask,
       "hwNTDPObject": hwNTDPObject,
       "hgmpNTDPCollectTopTime": hgmpNTDPCollectTopTime,
       "hgmpNTDPHopRange": hgmpNTDPHopRange,
       "hgmpNTDPRun": hgmpNTDPRun,
       "hgmpNTDPPortDelay": hgmpNTDPPortDelay,
       "hgmpNTDPHopDelay": hgmpNTDPHopDelay,
       "hgmpNTDPLastTopCollectDuration": hgmpNTDPLastTopCollectDuration,
       "hgmpNTDPCacheChange": hgmpNTDPCacheChange,
       "hgmpNTDPTOPTableChange": hgmpNTDPTOPTableChange,
       "hgmpNTDPInterfaceTable": hgmpNTDPInterfaceTable,
       "hgmpNTDPInterfaceEntry": hgmpNTDPInterfaceEntry,
       "hgmpNTDPInterfaceIfIndex": hgmpNTDPInterfaceIfIndex,
       "hgmpNTDPInterfaceEnable": hgmpNTDPInterfaceEnable,
       "hgmpNTDPCacheTable": hgmpNTDPCacheTable,
       "hgmpNTDPCacheEntry": hgmpNTDPCacheEntry,
       "hgmpNTDPCacheHashIndex": hgmpNTDPCacheHashIndex,
       "hgmpNTDPCacheDeviceID": hgmpNTDPCacheDeviceID,
       "hgmpNTDPCacheClusterName": hgmpNTDPCacheClusterName,
       "hgmpNTDPCacheClusterRole": hgmpNTDPCacheClusterRole,
       "hgmpNTDPCacheCapabilities": hgmpNTDPCacheCapabilities,
       "hgmpNTDPCacheVersion": hgmpNTDPCacheVersion,
       "hgmpNTDPCachePlatform": hgmpNTDPCachePlatform,
       "hgmpNTDPCacheMngVLAN": hgmpNTDPCacheMngVLAN,
       "hgmpNTDPCacheHop": hgmpNTDPCacheHop,
       "hgmpNTDPTopTable": hgmpNTDPTopTable,
       "hgmpNTDPTopEntry": hgmpNTDPTopEntry,
       "hgmpNTDPTopHashIndex": hgmpNTDPTopHashIndex,
       "hgmpNTDPTopEdgeStartDevID": hgmpNTDPTopEdgeStartDevID,
       "hgmpNTDPTopEdgeIndex": hgmpNTDPTopEdgeIndex,
       "hgmpNTDPTopEdgeEndDevID": hgmpNTDPTopEdgeEndDevID,
       "hgmpNTDPTopEdgeStartPort": hgmpNTDPTopEdgeStartPort,
       "hgmpNTDPTopEdgeStartPortFullDuplex": hgmpNTDPTopEdgeStartPortFullDuplex,
       "hgmpNTDPTopEdgeStartPortSpeed": hgmpNTDPTopEdgeStartPortSpeed,
       "hgmpNTDPTopEdgeEndPort": hgmpNTDPTopEdgeEndPort,
       "hgmpNTDPTopEdgeStartPortIfIndex": hgmpNTDPTopEdgeStartPortIfIndex,
       "hgmpNTDPTopEdgeEndPortIfIndex": hgmpNTDPTopEdgeEndPortIfIndex,
       "hgmpNTDPExplore": hgmpNTDPExplore,
       "hgmpNTDPTopoLinkTable": hgmpNTDPTopoLinkTable,
       "hgmpNTDPTopoLinkEntry": hgmpNTDPTopoLinkEntry,
       "hgmpNTDPTopoLocalDeviceID": hgmpNTDPTopoLocalDeviceID,
       "hgmpNTDPTopoLocalPortName": hgmpNTDPTopoLocalPortName,
       "hgmpNTDPTopoNbrDeviceID": hgmpNTDPTopoNbrDeviceID,
       "hgmpNTDPTopoNbrPortName": hgmpNTDPTopoNbrPortName,
       "hgmpNTDPTopoLinkStatus": hgmpNTDPTopoLinkStatus,
       "hgmpNTDPNotifications": hgmpNTDPNotifications,
       "hgmpNTDPTopoChange": hgmpNTDPTopoChange,
       "hwNDPObject": hwNDPObject,
       "hwNDPStatus": hwNDPStatus,
       "hwNDPHelloTimer": hwNDPHelloTimer,
       "hwNDPAgingTime": hwNDPAgingTime,
       "hwNDPChange": hwNDPChange,
       "hwNDPPortTable": hwNDPPortTable,
       "hwNDPPortEntry": hwNDPPortEntry,
       "hwNDPIfIndex": hwNDPIfIndex,
       "hwNDPPortStatus": hwNDPPortStatus,
       "hwNDPPortNbTable": hwNDPPortNbTable,
       "hwNDPPortNbEntry": hwNDPPortNbEntry,
       "hwNDPPortNbDeviceId": hwNDPPortNbDeviceId,
       "hwNDPPortNbPortName": hwNDPPortNbPortName,
       "hwNDPPortNbDeviceName": hwNDPPortNbDeviceName,
       "hwNDPPortNbPortMode": hwNDPPortNbPortMode,
       "hwNDPPortNbProductVer": hwNDPPortNbProductVer,
       "hwNDPPortNbHardVer": hwNDPPortNbHardVer,
       "hwNDPPortNbBootromVer": hwNDPPortNbBootromVer,
       "hwNDPPortNbSoftVer": hwNDPPortNbSoftVer,
       "hwNDPPortNbAgingtime": hwNDPPortNbAgingtime,
       "hwNDPTrunkMemberEnable": hwNDPTrunkMemberEnable,
       "hwClusterConformance": hwClusterConformance,
       "hwClusterGroups": hwClusterGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "hwClusterCompliances": hwClusterCompliances,
       "basicCompliance": basicCompliance}
)
