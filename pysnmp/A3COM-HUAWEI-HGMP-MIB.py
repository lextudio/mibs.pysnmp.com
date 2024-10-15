# SNMP MIB module (A3COM-HUAWEI-HGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-HGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:04 2024
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
    "A3COM-HUAWEI-OID-MIB",
    "huaweiUtility")

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwClusterObject_ObjectIdentity = ObjectIdentity
hwClusterObject = _HwClusterObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    hwClusterObject.setStatus("current")
_HgmpEventsV2_ObjectIdentity = ObjectIdentity
hgmpEventsV2 = _HgmpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 0)
)
if mibBuilder.loadTexts:
    hgmpEventsV2.setStatus("current")


class _HgmpSetVLANSecurity_Type(Integer32):
    """Custom type hgmpSetVLANSecurity based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 1),
    _HgmpSetVLANSecurity_Type()
)
hgmpSetVLANSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpSetVLANSecurity.setStatus("current")


class _HgmpHandShakeInterval_Type(Integer32):
    """Custom type hgmpHandShakeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HgmpHandShakeInterval_Type.__name__ = "Integer32"
_HgmpHandShakeInterval_Object = MibScalar
hgmpHandShakeInterval = _HgmpHandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 2),
    _HgmpHandShakeInterval_Type()
)
hgmpHandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpHandShakeInterval.setStatus("current")


class _HgmpHandShakeHoldtime_Type(Integer32):
    """Custom type hgmpHandShakeHoldtime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HgmpHandShakeHoldtime_Type.__name__ = "Integer32"
_HgmpHandShakeHoldtime_Object = MibScalar
hgmpHandShakeHoldtime = _HgmpHandShakeHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 3),
    _HgmpHandShakeHoldtime_Type()
)
hgmpHandShakeHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpHandShakeHoldtime.setStatus("current")


class _HgmpGrpMemberTableChange_Type(Integer32):
    """Custom type hgmpGrpMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpGrpMemberTableChange_Type.__name__ = "Integer32"
_HgmpGrpMemberTableChange_Object = MibScalar
hgmpGrpMemberTableChange = _HgmpGrpMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 4),
    _HgmpGrpMemberTableChange_Type()
)
hgmpGrpMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberTableChange.setStatus("current")


class _HgmpMemberDisconRate_Type(Integer32):
    """Custom type hgmpMemberDisconRate based on Integer32"""
    defaultValue = 0


_HgmpMemberDisconRate_Object = MibScalar
hgmpMemberDisconRate = _HgmpMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 5),
    _HgmpMemberDisconRate_Type()
)
hgmpMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberDisconRate.setStatus("current")


class _HgmpCmdLanswitchFlag_Type(Integer32):
    """Custom type hgmpCmdLanswitchFlag based on Integer32"""
    defaultValue = 0

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 7),
    _HgmpCmdClusterName_Type()
)
hgmpCmdClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpCmdClusterName.setStatus("current")
_HgmpMngPriIpSegCMIP_Type = IpAddress
_HgmpMngPriIpSegCMIP_Object = MibScalar
hgmpMngPriIpSegCMIP = _HgmpMngPriIpSegCMIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 8),
    _HgmpMngPriIpSegCMIP_Type()
)
hgmpMngPriIpSegCMIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMngPriIpSegCMIP.setStatus("current")
_HgmpMngPriIpMask_Type = IpAddress
_HgmpMngPriIpMask_Object = MibScalar
hgmpMngPriIpMask = _HgmpMngPriIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 9),
    _HgmpMngPriIpMask_Type()
)
hgmpMngPriIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMngPriIpMask.setStatus("current")
_HgmpFtpServer_Type = IpAddress
_HgmpFtpServer_Object = MibScalar
hgmpFtpServer = _HgmpFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 10),
    _HgmpFtpServer_Type()
)
hgmpFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpFtpServer.setStatus("current")
_HgmpTftpServer_Type = IpAddress
_HgmpTftpServer_Object = MibScalar
hgmpTftpServer = _HgmpTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 11),
    _HgmpTftpServer_Type()
)
hgmpTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpTftpServer.setStatus("current")
_HgmpSnmpHost_Type = IpAddress
_HgmpSnmpHost_Object = MibScalar
hgmpSnmpHost = _HgmpSnmpHost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 12),
    _HgmpSnmpHost_Type()
)
hgmpSnmpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpSnmpHost.setStatus("current")
_HgmpLogHost_Type = IpAddress
_HgmpLogHost_Object = MibScalar
hgmpLogHost = _HgmpLogHost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 13),
    _HgmpLogHost_Type()
)
hgmpLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpLogHost.setStatus("current")
_HgmpGrpMemberTable_Object = MibTable
hgmpGrpMemberTable = _HgmpGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14)
)
if mibBuilder.loadTexts:
    hgmpGrpMemberTable.setStatus("current")
_HgmpGrpMemberEntry_Object = MibTableRow
hgmpGrpMemberEntry = _HgmpGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1)
)
hgmpGrpMemberEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 2),
    _HgmpGrpMemberSerial_Type()
)
hgmpGrpMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberSerial.setStatus("current")
_HgmpGrpMemberIpAddr_Type = IpAddress
_HgmpGrpMemberIpAddr_Object = MibTableColumn
hgmpGrpMemberIpAddr = _HgmpGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 4),
    _HgmpGrpMemberName_Type()
)
hgmpGrpMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberName.setStatus("current")
_HgmpGrpMemberPassword_Type = OctetString
_HgmpGrpMemberPassword_Object = MibTableColumn
hgmpGrpMemberPassword = _HgmpGrpMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 5),
    _HgmpGrpMemberPassword_Type()
)
hgmpGrpMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpGrpMemberPassword.setStatus("current")
_HgmpGrpMemberPlatform_Type = OctetString
_HgmpGrpMemberPlatform_Object = MibTableColumn
hgmpGrpMemberPlatform = _HgmpGrpMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 6),
    _HgmpGrpMemberPlatform_Type()
)
hgmpGrpMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberPlatform.setStatus("current")


class _HgmpGrpMemberStatus_Type(Integer32):
    """Custom type hgmpGrpMemberStatus based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 7),
    _HgmpGrpMemberStatus_Type()
)
hgmpGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberStatus.setStatus("current")
_HgmpGrpMemberDisconCount_Type = Integer32
_HgmpGrpMemberDisconCount_Object = MibTableColumn
hgmpGrpMemberDisconCount = _HgmpGrpMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 8),
    _HgmpGrpMemberDisconCount_Type()
)
hgmpGrpMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberDisconCount.setStatus("current")
_HgmpGrpMemberEnrollTime_Type = Integer32
_HgmpGrpMemberEnrollTime_Object = MibTableColumn
hgmpGrpMemberEnrollTime = _HgmpGrpMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 9),
    _HgmpGrpMemberEnrollTime_Type()
)
hgmpGrpMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpGrpMemberEnrollTime.setStatus("current")
_HgmpGrpMemberOperate_Type = RowStatus
_HgmpGrpMemberOperate_Object = MibTableColumn
hgmpGrpMemberOperate = _HgmpGrpMemberOperate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 14, 1, 10),
    _HgmpGrpMemberOperate_Type()
)
hgmpGrpMemberOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpGrpMemberOperate.setStatus("current")
_HgmpMemberResetTable_Object = MibTable
hgmpMemberResetTable = _HgmpMemberResetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 15)
)
if mibBuilder.loadTexts:
    hgmpMemberResetTable.setStatus("current")
_HgmpMemberResetEntry_Object = MibTableRow
hgmpMemberResetEntry = _HgmpMemberResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 15, 1)
)
hgmpMemberResetEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpMemberResetMAC"),
)
if mibBuilder.loadTexts:
    hgmpMemberResetEntry.setStatus("current")


class _HgmpMemberResetMAC_Type(OctetString):
    """Custom type hgmpMemberResetMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HgmpMemberResetMAC_Type.__name__ = "OctetString"
_HgmpMemberResetMAC_Object = MibTableColumn
hgmpMemberResetMAC = _HgmpMemberResetMAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 15, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 15, 1, 2),
    _HgmpMemberEraseflash_Type()
)
hgmpMemberEraseflash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMemberEraseflash.setStatus("current")


class _HgmpClusterRole_Type(Integer32):
    """Custom type hgmpClusterRole based on Integer32"""
    defaultValue = 17

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 16),
    _HgmpClusterRole_Type()
)
hgmpClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterRole.setStatus("current")
_HgmpClusterMaxPoolNum_Type = Integer32
_HgmpClusterMaxPoolNum_Object = MibScalar
hgmpClusterMaxPoolNum = _HgmpClusterMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 17),
    _HgmpClusterMaxPoolNum_Type()
)
hgmpClusterMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterMaxPoolNum.setStatus("current")


class _HgmpClusterCmdSwMac_Type(OctetString):
    """Custom type hgmpClusterCmdSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HgmpClusterCmdSwMac_Type.__name__ = "OctetString"
_HgmpClusterCmdSwMac_Object = MibScalar
hgmpClusterCmdSwMac = _HgmpClusterCmdSwMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 18),
    _HgmpClusterCmdSwMac_Type()
)
hgmpClusterCmdSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpClusterCmdSwMac.setStatus("current")


class _HgmpRun_Type(Integer32):
    """Custom type hgmpRun based on Integer32"""
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


_HgmpRun_Type.__name__ = "Integer32"
_HgmpRun_Object = MibScalar
hgmpRun = _HgmpRun_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 19),
    _HgmpRun_Type()
)
hgmpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpRun.setStatus("current")
_HgmpProtocolMac_ObjectIdentity = ObjectIdentity
hgmpProtocolMac = _HgmpProtocolMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 22)
)


class _HgmpClusterProtocolMac_Type(MacAddress):
    """Custom type hgmpClusterProtocolMac based on MacAddress"""
    defaultHexValue = "0180C200000A"


_HgmpClusterProtocolMac_Object = MibScalar
hgmpClusterProtocolMac = _HgmpClusterProtocolMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 22, 1),
    _HgmpClusterProtocolMac_Type()
)
hgmpClusterProtocolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpClusterProtocolMac.setStatus("current")
_HgmpTopologyManagement_ObjectIdentity = ObjectIdentity
hgmpTopologyManagement = _HgmpTopologyManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23)
)
_HgmpWhitelistTable_Object = MibTable
hgmpWhitelistTable = _HgmpWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 1)
)
if mibBuilder.loadTexts:
    hgmpWhitelistTable.setStatus("current")
_HgmpWhitelistEntry_Object = MibTableRow
hgmpWhitelistEntry = _HgmpWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 1, 1)
)
hgmpWhitelistEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpWhitelistDeviceId"),
)
if mibBuilder.loadTexts:
    hgmpWhitelistEntry.setStatus("current")


class _HgmpWhitelistDeviceId_Type(OctetString):
    """Custom type hgmpWhitelistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HgmpWhitelistDeviceId_Type.__name__ = "OctetString"
_HgmpWhitelistDeviceId_Object = MibTableColumn
hgmpWhitelistDeviceId = _HgmpWhitelistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 1, 1, 1),
    _HgmpWhitelistDeviceId_Type()
)
hgmpWhitelistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpWhitelistDeviceId.setStatus("current")


class _HgmpWhitelistSerial_Type(Integer32):
    """Custom type hgmpWhitelistSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
        ValueRangeConstraint(65535, 65535),
    )


_HgmpWhitelistSerial_Type.__name__ = "Integer32"
_HgmpWhitelistSerial_Object = MibTableColumn
hgmpWhitelistSerial = _HgmpWhitelistSerial_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 1, 1, 2),
    _HgmpWhitelistSerial_Type()
)
hgmpWhitelistSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpWhitelistSerial.setStatus("current")
_HgmpWhitelistRowStatus_Type = RowStatus
_HgmpWhitelistRowStatus_Object = MibTableColumn
hgmpWhitelistRowStatus = _HgmpWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 1, 1, 3),
    _HgmpWhitelistRowStatus_Type()
)
hgmpWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpWhitelistRowStatus.setStatus("current")
_HgmpWhitelistNbTable_Object = MibTable
hgmpWhitelistNbTable = _HgmpWhitelistNbTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2)
)
if mibBuilder.loadTexts:
    hgmpWhitelistNbTable.setStatus("current")
_HgmpWhitelistNbEntry_Object = MibTableRow
hgmpWhitelistNbEntry = _HgmpWhitelistNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2, 1)
)
hgmpWhitelistNbEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpWhitelistDeviceId"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpWhitelistNbIndex"),
)
if mibBuilder.loadTexts:
    hgmpWhitelistNbEntry.setStatus("current")


class _HgmpWhitelistNbIndex_Type(Integer32):
    """Custom type hgmpWhitelistNbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HgmpWhitelistNbIndex_Type.__name__ = "Integer32"
_HgmpWhitelistNbIndex_Object = MibTableColumn
hgmpWhitelistNbIndex = _HgmpWhitelistNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2, 1, 1),
    _HgmpWhitelistNbIndex_Type()
)
hgmpWhitelistNbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpWhitelistNbIndex.setStatus("current")


class _HgmpWhitelistNbDeviceId_Type(OctetString):
    """Custom type hgmpWhitelistNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HgmpWhitelistNbDeviceId_Type.__name__ = "OctetString"
_HgmpWhitelistNbDeviceId_Object = MibTableColumn
hgmpWhitelistNbDeviceId = _HgmpWhitelistNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2, 1, 2),
    _HgmpWhitelistNbDeviceId_Type()
)
hgmpWhitelistNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpWhitelistNbDeviceId.setStatus("current")


class _HgmpWhitelistPortName_Type(OctetString):
    """Custom type hgmpWhitelistPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HgmpWhitelistPortName_Type.__name__ = "OctetString"
_HgmpWhitelistPortName_Object = MibTableColumn
hgmpWhitelistPortName = _HgmpWhitelistPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2, 1, 3),
    _HgmpWhitelistPortName_Type()
)
hgmpWhitelistPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpWhitelistPortName.setStatus("current")


class _HgmpWhitelistNbPortName_Type(OctetString):
    """Custom type hgmpWhitelistNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HgmpWhitelistNbPortName_Type.__name__ = "OctetString"
_HgmpWhitelistNbPortName_Object = MibTableColumn
hgmpWhitelistNbPortName = _HgmpWhitelistNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 2, 1, 4),
    _HgmpWhitelistNbPortName_Type()
)
hgmpWhitelistNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpWhitelistNbPortName.setStatus("current")
_HgmpBlacklistTable_Object = MibTable
hgmpBlacklistTable = _HgmpBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3)
)
if mibBuilder.loadTexts:
    hgmpBlacklistTable.setStatus("current")
_HgmpBlacklistEntry_Object = MibTableRow
hgmpBlacklistEntry = _HgmpBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3, 1)
)
hgmpBlacklistEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpBlacklistDeviceId"),
)
if mibBuilder.loadTexts:
    hgmpBlacklistEntry.setStatus("current")


class _HgmpBlacklistDeviceId_Type(OctetString):
    """Custom type hgmpBlacklistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HgmpBlacklistDeviceId_Type.__name__ = "OctetString"
_HgmpBlacklistDeviceId_Object = MibTableColumn
hgmpBlacklistDeviceId = _HgmpBlacklistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3, 1, 1),
    _HgmpBlacklistDeviceId_Type()
)
hgmpBlacklistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpBlacklistDeviceId.setStatus("current")


class _HgmpBlacklistAccessDeviceId_Type(OctetString):
    """Custom type hgmpBlacklistAccessDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HgmpBlacklistAccessDeviceId_Type.__name__ = "OctetString"
_HgmpBlacklistAccessDeviceId_Object = MibTableColumn
hgmpBlacklistAccessDeviceId = _HgmpBlacklistAccessDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3, 1, 2),
    _HgmpBlacklistAccessDeviceId_Type()
)
hgmpBlacklistAccessDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBlacklistAccessDeviceId.setStatus("current")


class _HgmpBlacklistAccessPortName_Type(OctetString):
    """Custom type hgmpBlacklistAccessPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HgmpBlacklistAccessPortName_Type.__name__ = "OctetString"
_HgmpBlacklistAccessPortName_Object = MibTableColumn
hgmpBlacklistAccessPortName = _HgmpBlacklistAccessPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3, 1, 3),
    _HgmpBlacklistAccessPortName_Type()
)
hgmpBlacklistAccessPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpBlacklistAccessPortName.setStatus("current")
_HgmpBlacklistRowStatus_Type = RowStatus
_HgmpBlacklistRowStatus_Object = MibTableColumn
hgmpBlacklistRowStatus = _HgmpBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 23, 3, 1, 4),
    _HgmpBlacklistRowStatus_Type()
)
hgmpBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hgmpBlacklistRowStatus.setStatus("current")
_HgmpMemberPriPortTable_Object = MibTable
hgmpMemberPriPortTable = _HgmpMemberPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24)
)
if mibBuilder.loadTexts:
    hgmpMemberPriPortTable.setStatus("current")
_HgmpMemberPriPortEntry_Object = MibTableRow
hgmpMemberPriPortEntry = _HgmpMemberPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24, 1)
)
hgmpMemberPriPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpMemberDevId"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpMemberPriPortProto"),
)
if mibBuilder.loadTexts:
    hgmpMemberPriPortEntry.setStatus("current")


class _HgmpMemberDevId_Type(OctetString):
    """Custom type hgmpMemberDevId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HgmpMemberDevId_Type.__name__ = "OctetString"
_HgmpMemberDevId_Object = MibTableColumn
hgmpMemberDevId = _HgmpMemberDevId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24, 1, 1),
    _HgmpMemberDevId_Type()
)
hgmpMemberDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberDevId.setStatus("current")
_HgmpMemberPriPortProto_Type = Unsigned32
_HgmpMemberPriPortProto_Object = MibTableColumn
hgmpMemberPriPortProto = _HgmpMemberPriPortProto_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24, 1, 2),
    _HgmpMemberPriPortProto_Type()
)
hgmpMemberPriPortProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgmpMemberPriPortProto.setStatus("current")
_HgmpMemberPriPortProtoDescr_Type = DisplayString
_HgmpMemberPriPortProtoDescr_Object = MibTableColumn
hgmpMemberPriPortProtoDescr = _HgmpMemberPriPortProtoDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24, 1, 3),
    _HgmpMemberPriPortProtoDescr_Type()
)
hgmpMemberPriPortProtoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberPriPortProtoDescr.setStatus("current")
_HgmpMemberPriPortNum_Type = Unsigned32
_HgmpMemberPriPortNum_Object = MibTableColumn
hgmpMemberPriPortNum = _HgmpMemberPriPortNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 24, 1, 4),
    _HgmpMemberPriPortNum_Type()
)
hgmpMemberPriPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpMemberPriPortNum.setStatus("current")
_HwStackObject_ObjectIdentity = ObjectIdentity
hwStackObject = _HwStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    hwStackObject.setStatus("current")
_HgmpStackEventsV2_ObjectIdentity = ObjectIdentity
hgmpStackEventsV2 = _HgmpStackEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 0)
)
if mibBuilder.loadTexts:
    hgmpStackEventsV2.setStatus("current")


class _HgmpStackMemberTableChange_Type(Integer32):
    """Custom type hgmpStackMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpStackMemberTableChange_Type.__name__ = "Integer32"
_HgmpStackMemberTableChange_Object = MibScalar
hgmpStackMemberTableChange = _HgmpStackMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 1),
    _HgmpStackMemberTableChange_Type()
)
hgmpStackMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberTableChange.setStatus("current")


class _HgmpStackMemberDisconRate_Type(Integer32):
    """Custom type hgmpStackMemberDisconRate based on Integer32"""
    defaultValue = 0


_HgmpStackMemberDisconRate_Object = MibScalar
hgmpStackMemberDisconRate = _HgmpStackMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 2),
    _HgmpStackMemberDisconRate_Type()
)
hgmpStackMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberDisconRate.setStatus("current")


class _HgmpMainLanswitchFlag_Type(Integer32):
    """Custom type hgmpMainLanswitchFlag based on Integer32"""
    defaultValue = 0

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 3),
    _HgmpMainLanswitchFlag_Type()
)
hgmpMainLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpMainLanswitchFlag.setStatus("current")
_HgmpStackIpPoolStartIP_Type = IpAddress
_HgmpStackIpPoolStartIP_Object = MibScalar
hgmpStackIpPoolStartIP = _HgmpStackIpPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 5),
    _HgmpStackIpPoolLength_Type()
)
hgmpStackIpPoolLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpStackIpPoolLength.setStatus("current")
_HgmpStackMemberTable_Object = MibTable
hgmpStackMemberTable = _HgmpStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hgmpStackMemberTable.setStatus("current")
_HgmpStackMemberEntry_Object = MibTableRow
hgmpStackMemberEntry = _HgmpStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1)
)
hgmpStackMemberEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 2),
    _HgmpStackMemberSerial_Type()
)
hgmpStackMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberSerial.setStatus("current")
_HgmpStackMemberIpAddr_Type = IpAddress
_HgmpStackMemberIpAddr_Object = MibTableColumn
hgmpStackMemberIpAddr = _HgmpStackMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 3),
    _HgmpStackMemberIpAddr_Type()
)
hgmpStackMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberIpAddr.setStatus("current")
_HgmpStackMemberName_Type = OctetString
_HgmpStackMemberName_Object = MibTableColumn
hgmpStackMemberName = _HgmpStackMemberName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 4),
    _HgmpStackMemberName_Type()
)
hgmpStackMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberName.setStatus("current")
_HgmpStackMemberPassword_Type = OctetString
_HgmpStackMemberPassword_Object = MibTableColumn
hgmpStackMemberPassword = _HgmpStackMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 5),
    _HgmpStackMemberPassword_Type()
)
hgmpStackMemberPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberPassword.setStatus("current")
_HgmpStackMemberPlatform_Type = OctetString
_HgmpStackMemberPlatform_Object = MibTableColumn
hgmpStackMemberPlatform = _HgmpStackMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 6),
    _HgmpStackMemberPlatform_Type()
)
hgmpStackMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberPlatform.setStatus("current")


class _HgmpStackMemberStatus_Type(Integer32):
    """Custom type hgmpStackMemberStatus based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 7),
    _HgmpStackMemberStatus_Type()
)
hgmpStackMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberStatus.setStatus("current")
_HgmpStackMemberDisconCount_Type = Integer32
_HgmpStackMemberDisconCount_Object = MibTableColumn
hgmpStackMemberDisconCount = _HgmpStackMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 8),
    _HgmpStackMemberDisconCount_Type()
)
hgmpStackMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberDisconCount.setStatus("current")
_HgmpStackMemberEnrollTime_Type = Integer32
_HgmpStackMemberEnrollTime_Object = MibTableColumn
hgmpStackMemberEnrollTime = _HgmpStackMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 6, 1, 9),
    _HgmpStackMemberEnrollTime_Type()
)
hgmpStackMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMemberEnrollTime.setStatus("current")


class _HgmpStackRole_Type(Integer32):
    """Custom type hgmpStackRole based on Integer32"""
    defaultValue = 17

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 7),
    _HgmpStackRole_Type()
)
hgmpStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackRole.setStatus("current")
_HgmpStackMaxPoolNum_Type = Integer32
_HgmpStackMaxPoolNum_Object = MibScalar
hgmpStackMaxPoolNum = _HgmpStackMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 8),
    _HgmpStackMaxPoolNum_Type()
)
hgmpStackMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMaxPoolNum.setStatus("current")


class _HgmpStackMainSwMac_Type(OctetString):
    """Custom type hgmpStackMainSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HgmpStackMainSwMac_Type.__name__ = "OctetString"
_HgmpStackMainSwMac_Object = MibScalar
hgmpStackMainSwMac = _HgmpStackMainSwMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 9),
    _HgmpStackMainSwMac_Type()
)
hgmpStackMainSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpStackMainSwMac.setStatus("current")


class _HgmpStackIpPoolMask_Type(IpAddress):
    """Custom type hgmpStackIpPoolMask based on IpAddress"""
    defaultHexValue = "FFFF0000"


_HgmpStackIpPoolMask_Object = MibScalar
hgmpStackIpPoolMask = _HgmpStackIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 10),
    _HgmpStackIpPoolMask_Type()
)
hgmpStackIpPoolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpStackIpPoolMask.setStatus("current")
_HwNTDPObject_ObjectIdentity = ObjectIdentity
hwNTDPObject = _HwNTDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4)
)
if mibBuilder.loadTexts:
    hwNTDPObject.setStatus("current")


class _HgmpNTDPCollectTopTime_Type(Integer32):
    """Custom type hgmpNTDPCollectTopTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPCollectTopTime_Type.__name__ = "Integer32"
_HgmpNTDPCollectTopTime_Object = MibScalar
hgmpNTDPCollectTopTime = _HgmpNTDPCollectTopTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 1),
    _HgmpNTDPCollectTopTime_Type()
)
hgmpNTDPCollectTopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPCollectTopTime.setStatus("current")


class _HgmpNTDPHopRange_Type(Integer32):
    """Custom type hgmpNTDPHopRange based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HgmpNTDPHopRange_Type.__name__ = "Integer32"
_HgmpNTDPHopRange_Object = MibScalar
hgmpNTDPHopRange = _HgmpNTDPHopRange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 2),
    _HgmpNTDPHopRange_Type()
)
hgmpNTDPHopRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPHopRange.setStatus("current")


class _HgmpNTDPRun_Type(Integer32):
    """Custom type hgmpNTDPRun based on Integer32"""
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


_HgmpNTDPRun_Type.__name__ = "Integer32"
_HgmpNTDPRun_Object = MibScalar
hgmpNTDPRun = _HgmpNTDPRun_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 3),
    _HgmpNTDPRun_Type()
)
hgmpNTDPRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPRun.setStatus("current")


class _HgmpNTDPPortDelay_Type(Integer32):
    """Custom type hgmpNTDPPortDelay based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HgmpNTDPPortDelay_Type.__name__ = "Integer32"
_HgmpNTDPPortDelay_Object = MibScalar
hgmpNTDPPortDelay = _HgmpNTDPPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 4),
    _HgmpNTDPPortDelay_Type()
)
hgmpNTDPPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPPortDelay.setStatus("current")


class _HgmpNTDPHopDelay_Type(Integer32):
    """Custom type hgmpNTDPHopDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HgmpNTDPHopDelay_Type.__name__ = "Integer32"
_HgmpNTDPHopDelay_Object = MibScalar
hgmpNTDPHopDelay = _HgmpNTDPHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 5),
    _HgmpNTDPHopDelay_Type()
)
hgmpNTDPHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPHopDelay.setStatus("current")


class _HgmpNTDPLastTopCollectDuration_Type(Integer32):
    """Custom type hgmpNTDPLastTopCollectDuration based on Integer32"""
    defaultValue = 0


_HgmpNTDPLastTopCollectDuration_Object = MibScalar
hgmpNTDPLastTopCollectDuration = _HgmpNTDPLastTopCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 6),
    _HgmpNTDPLastTopCollectDuration_Type()
)
hgmpNTDPLastTopCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPLastTopCollectDuration.setStatus("current")


class _HgmpNTDPCacheChange_Type(Integer32):
    """Custom type hgmpNTDPCacheChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPCacheChange_Type.__name__ = "Integer32"
_HgmpNTDPCacheChange_Object = MibScalar
hgmpNTDPCacheChange = _HgmpNTDPCacheChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 7),
    _HgmpNTDPCacheChange_Type()
)
hgmpNTDPCacheChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheChange.setStatus("current")


class _HgmpNTDPTOPTableChange_Type(Integer32):
    """Custom type hgmpNTDPTOPTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HgmpNTDPTOPTableChange_Type.__name__ = "Integer32"
_HgmpNTDPTOPTableChange_Object = MibScalar
hgmpNTDPTOPTableChange = _HgmpNTDPTOPTableChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 8),
    _HgmpNTDPTOPTableChange_Type()
)
hgmpNTDPTOPTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTOPTableChange.setStatus("current")
_HgmpNTDPInterfaceTable_Object = MibTable
hgmpNTDPInterfaceTable = _HgmpNTDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 9)
)
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceTable.setStatus("current")
_HgmpNTDPInterfaceEntry_Object = MibTableRow
hgmpNTDPInterfaceEntry = _HgmpNTDPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 9, 1)
)
hgmpNTDPInterfaceEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceEntry.setStatus("current")
_HgmpNTDPInterfaceIfIndex_Type = Integer32
_HgmpNTDPInterfaceIfIndex_Object = MibTableColumn
hgmpNTDPInterfaceIfIndex = _HgmpNTDPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 9, 1, 2),
    _HgmpNTDPInterfaceEnable_Type()
)
hgmpNTDPInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgmpNTDPInterfaceEnable.setStatus("current")
_HgmpNTDPCacheTable_Object = MibTable
hgmpNTDPCacheTable = _HgmpNTDPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10)
)
if mibBuilder.loadTexts:
    hgmpNTDPCacheTable.setStatus("current")
_HgmpNTDPCacheEntry_Object = MibTableRow
hgmpNTDPCacheEntry = _HgmpNTDPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1)
)
hgmpNTDPCacheEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPCacheHashIndex"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPCacheDeviceID"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 2),
    _HgmpNTDPCacheDeviceID_Type()
)
hgmpNTDPCacheDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheDeviceID.setStatus("current")
_HgmpNTDPCacheClusterName_Type = OctetString
_HgmpNTDPCacheClusterName_Object = MibTableColumn
hgmpNTDPCacheClusterName = _HgmpNTDPCacheClusterName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 3),
    _HgmpNTDPCacheClusterName_Type()
)
hgmpNTDPCacheClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheClusterName.setStatus("current")


class _HgmpNTDPCacheClusterRole_Type(Integer32):
    """Custom type hgmpNTDPCacheClusterRole based on Integer32"""
    defaultValue = 17

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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 4),
    _HgmpNTDPCacheClusterRole_Type()
)
hgmpNTDPCacheClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheClusterRole.setStatus("current")


class _HgmpNTDPCacheCapabilities_Type(Integer32):
    """Custom type hgmpNTDPCacheCapabilities based on Integer32"""
    defaultValue = 255


_HgmpNTDPCacheCapabilities_Object = MibTableColumn
hgmpNTDPCacheCapabilities = _HgmpNTDPCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 5),
    _HgmpNTDPCacheCapabilities_Type()
)
hgmpNTDPCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheCapabilities.setStatus("current")
_HgmpNTDPCacheVersion_Type = OctetString
_HgmpNTDPCacheVersion_Object = MibTableColumn
hgmpNTDPCacheVersion = _HgmpNTDPCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 6),
    _HgmpNTDPCacheVersion_Type()
)
hgmpNTDPCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheVersion.setStatus("current")
_HgmpNTDPCachePlatform_Type = OctetString
_HgmpNTDPCachePlatform_Object = MibTableColumn
hgmpNTDPCachePlatform = _HgmpNTDPCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 7),
    _HgmpNTDPCachePlatform_Type()
)
hgmpNTDPCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCachePlatform.setStatus("current")


class _HgmpNTDPCacheMngVLAN_Type(Integer32):
    """Custom type hgmpNTDPCacheMngVLAN based on Integer32"""
    defaultValue = 1


_HgmpNTDPCacheMngVLAN_Object = MibTableColumn
hgmpNTDPCacheMngVLAN = _HgmpNTDPCacheMngVLAN_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 8),
    _HgmpNTDPCacheMngVLAN_Type()
)
hgmpNTDPCacheMngVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheMngVLAN.setStatus("current")
_HgmpNTDPCacheHop_Type = Integer32
_HgmpNTDPCacheHop_Object = MibTableColumn
hgmpNTDPCacheHop = _HgmpNTDPCacheHop_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 10, 1, 9),
    _HgmpNTDPCacheHop_Type()
)
hgmpNTDPCacheHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPCacheHop.setStatus("current")
_HgmpNTDPTopTable_Object = MibTable
hgmpNTDPTopTable = _HgmpNTDPTopTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11)
)
if mibBuilder.loadTexts:
    hgmpNTDPTopTable.setStatus("current")
_HgmpNTDPTopEntry_Object = MibTableRow
hgmpNTDPTopEntry = _HgmpNTDPTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1)
)
hgmpNTDPTopEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPTopHashIndex"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeStartDevID"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPTopEdgeIndex"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 4),
    _HgmpNTDPTopEdgeEndDevID_Type()
)
hgmpNTDPTopEdgeEndDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeEndDevID.setStatus("current")


class _HgmpNTDPTopEdgeStartPort_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeStartPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HgmpNTDPTopEdgeStartPort_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeStartPort_Object = MibTableColumn
hgmpNTDPTopEdgeStartPort = _HgmpNTDPTopEdgeStartPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 5),
    _HgmpNTDPTopEdgeStartPort_Type()
)
hgmpNTDPTopEdgeStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPort.setStatus("current")


class _HgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):
    """Custom type hgmpNTDPTopEdgeStartPortFullDuplex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_HgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__ = "Integer32"
_HgmpNTDPTopEdgeStartPortFullDuplex_Object = MibTableColumn
hgmpNTDPTopEdgeStartPortFullDuplex = _HgmpNTDPTopEdgeStartPortFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 6),
    _HgmpNTDPTopEdgeStartPortFullDuplex_Type()
)
hgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPortFullDuplex.setStatus("current")


class _HgmpNTDPTopEdgeStartPortSpeed_Type(Integer32):
    """Custom type hgmpNTDPTopEdgeStartPortSpeed based on Integer32"""
    defaultValue = 0


_HgmpNTDPTopEdgeStartPortSpeed_Object = MibTableColumn
hgmpNTDPTopEdgeStartPortSpeed = _HgmpNTDPTopEdgeStartPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 7),
    _HgmpNTDPTopEdgeStartPortSpeed_Type()
)
hgmpNTDPTopEdgeStartPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeStartPortSpeed.setStatus("current")


class _HgmpNTDPTopEdgeEndPort_Type(OctetString):
    """Custom type hgmpNTDPTopEdgeEndPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HgmpNTDPTopEdgeEndPort_Type.__name__ = "OctetString"
_HgmpNTDPTopEdgeEndPort_Object = MibTableColumn
hgmpNTDPTopEdgeEndPort = _HgmpNTDPTopEdgeEndPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 8),
    _HgmpNTDPTopEdgeEndPort_Type()
)
hgmpNTDPTopEdgeEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopEdgeEndPort.setStatus("current")


class _HgmpNTDPTopLinkStatus_Type(Integer32):
    """Custom type hgmpNTDPTopLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("forwarding", 1))
    )


_HgmpNTDPTopLinkStatus_Type.__name__ = "Integer32"
_HgmpNTDPTopLinkStatus_Object = MibTableColumn
hgmpNTDPTopLinkStatus = _HgmpNTDPTopLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 4, 11, 1, 11),
    _HgmpNTDPTopLinkStatus_Type()
)
hgmpNTDPTopLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgmpNTDPTopLinkStatus.setStatus("current")
_HwNDPObject_ObjectIdentity = ObjectIdentity
hwNDPObject = _HwNDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5)
)
if mibBuilder.loadTexts:
    hwNDPObject.setStatus("current")


class _HwNDPStatus_Type(Integer32):
    """Custom type hwNDPStatus based on Integer32"""
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


_HwNDPStatus_Type.__name__ = "Integer32"
_HwNDPStatus_Object = MibScalar
hwNDPStatus = _HwNDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 1),
    _HwNDPStatus_Type()
)
hwNDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPStatus.setStatus("current")


class _HwNDPHelloTimer_Type(Integer32):
    """Custom type hwNDPHelloTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_HwNDPHelloTimer_Type.__name__ = "Integer32"
_HwNDPHelloTimer_Object = MibScalar
hwNDPHelloTimer = _HwNDPHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 2),
    _HwNDPHelloTimer_Type()
)
hwNDPHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPHelloTimer.setStatus("current")


class _HwNDPAgingTime_Type(Integer32):
    """Custom type hwNDPAgingTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HwNDPAgingTime_Type.__name__ = "Integer32"
_HwNDPAgingTime_Object = MibScalar
hwNDPAgingTime = _HwNDPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 3),
    _HwNDPAgingTime_Type()
)
hwNDPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPAgingTime.setStatus("current")


class _HwNDPChange_Type(Counter32):
    """Custom type hwNDPChange based on Counter32"""
    defaultValue = 0


_HwNDPChange_Object = MibScalar
hwNDPChange = _HwNDPChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 4),
    _HwNDPChange_Type()
)
hwNDPChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPChange.setStatus("current")
_HwNDPPortTable_Object = MibTable
hwNDPPortTable = _HwNDPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 5)
)
if mibBuilder.loadTexts:
    hwNDPPortTable.setStatus("current")
_HwNDPPortEntry_Object = MibTableRow
hwNDPPortEntry = _HwNDPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 5, 1)
)
hwNDPPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hwNDPIfIndex"),
)
if mibBuilder.loadTexts:
    hwNDPPortEntry.setStatus("current")
_HwNDPIfIndex_Type = Integer32
_HwNDPIfIndex_Object = MibTableColumn
hwNDPIfIndex = _HwNDPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 5, 1, 2),
    _HwNDPPortStatus_Type()
)
hwNDPPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNDPPortStatus.setStatus("current")
_HwNDPPortNbTable_Object = MibTable
hwNDPPortNbTable = _HwNDPPortNbTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6)
)
if mibBuilder.loadTexts:
    hwNDPPortNbTable.setStatus("current")
_HwNDPPortNbEntry_Object = MibTableRow
hwNDPPortNbEntry = _HwNDPPortNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1)
)
hwNDPPortNbEntry.setIndexNames(
    (0, "A3COM-HUAWEI-HGMP-MIB", "hwNDPIfIndex"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hwNDPPortNbDeviceId"),
    (0, "A3COM-HUAWEI-HGMP-MIB", "hwNDPPortNbPortName"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 1),
    _HwNDPPortNbDeviceId_Type()
)
hwNDPPortNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbDeviceId.setStatus("current")


class _HwNDPPortNbPortName_Type(OctetString):
    """Custom type hwNDPPortNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwNDPPortNbPortName_Type.__name__ = "OctetString"
_HwNDPPortNbPortName_Object = MibTableColumn
hwNDPPortNbPortName = _HwNDPPortNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 2),
    _HwNDPPortNbPortName_Type()
)
hwNDPPortNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbPortName.setStatus("current")
_HwNDPPortNbDeviceName_Type = OctetString
_HwNDPPortNbDeviceName_Object = MibTableColumn
hwNDPPortNbDeviceName = _HwNDPPortNbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 4),
    _HwNDPPortNbPortMode_Type()
)
hwNDPPortNbPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbPortMode.setStatus("current")
_HwNDPPortNbProductVer_Type = OctetString
_HwNDPPortNbProductVer_Object = MibTableColumn
hwNDPPortNbProductVer = _HwNDPPortNbProductVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 5),
    _HwNDPPortNbProductVer_Type()
)
hwNDPPortNbProductVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbProductVer.setStatus("current")
_HwNDPPortNbHardVer_Type = OctetString
_HwNDPPortNbHardVer_Object = MibTableColumn
hwNDPPortNbHardVer = _HwNDPPortNbHardVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 6),
    _HwNDPPortNbHardVer_Type()
)
hwNDPPortNbHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbHardVer.setStatus("current")
_HwNDPPortNbBootromVer_Type = OctetString
_HwNDPPortNbBootromVer_Object = MibTableColumn
hwNDPPortNbBootromVer = _HwNDPPortNbBootromVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 7),
    _HwNDPPortNbBootromVer_Type()
)
hwNDPPortNbBootromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbBootromVer.setStatus("current")
_HwNDPPortNbSoftVer_Type = OctetString
_HwNDPPortNbSoftVer_Object = MibTableColumn
hwNDPPortNbSoftVer = _HwNDPPortNbSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 5, 6, 1, 9),
    _HwNDPPortNbAgingtime_Type()
)
hwNDPPortNbAgingtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNDPPortNbAgingtime.setStatus("current")

# Managed Objects groups


# Notification objects

hgmpMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 0, 1)
)
hgmpMemberfailure.setObjects(
    ("A3COM-HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpMemberfailure.setStatus(
        "current"
    )

hgmpMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 0, 2)
)
hgmpMemberRecover.setObjects(
    ("A3COM-HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpMemberRecover.setStatus(
        "current"
    )

hgmpMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 0, 3)
)
hgmpMemberStatusChange.setObjects(
      *(("A3COM-HUAWEI-HGMP-MIB", "hgmpGrpMemberDeviceId"),
        ("A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hgmpMemberStatusChange.setStatus(
        "current"
    )

hgmpNetTopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 1, 0, 4)
)
if mibBuilder.loadTexts:
    hgmpNetTopChange.setStatus(
        "current"
    )

hgmpStackMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 0, 1)
)
hgmpStackMemberfailure.setObjects(
    ("A3COM-HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpStackMemberfailure.setStatus(
        "current"
    )

hgmpStackMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 0, 2)
)
hgmpStackMemberRecover.setObjects(
    ("A3COM-HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hgmpStackMemberRecover.setStatus(
        "current"
    )

hgmpStackMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 7, 2, 0, 3)
)
hgmpStackMemberStatusChange.setObjects(
      *(("A3COM-HUAWEI-HGMP-MIB", "hgmpStackMemberDeviceId"),
        ("A3COM-HUAWEI-HGMP-MIB", "hgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hgmpStackMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-HGMP-MIB",
    **{"hwCluster": hwCluster,
       "hwClusterObject": hwClusterObject,
       "hgmpEventsV2": hgmpEventsV2,
       "hgmpMemberfailure": hgmpMemberfailure,
       "hgmpMemberRecover": hgmpMemberRecover,
       "hgmpMemberStatusChange": hgmpMemberStatusChange,
       "hgmpNetTopChange": hgmpNetTopChange,
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
       "hgmpProtocolMac": hgmpProtocolMac,
       "hgmpClusterProtocolMac": hgmpClusterProtocolMac,
       "hgmpTopologyManagement": hgmpTopologyManagement,
       "hgmpWhitelistTable": hgmpWhitelistTable,
       "hgmpWhitelistEntry": hgmpWhitelistEntry,
       "hgmpWhitelistDeviceId": hgmpWhitelistDeviceId,
       "hgmpWhitelistSerial": hgmpWhitelistSerial,
       "hgmpWhitelistRowStatus": hgmpWhitelistRowStatus,
       "hgmpWhitelistNbTable": hgmpWhitelistNbTable,
       "hgmpWhitelistNbEntry": hgmpWhitelistNbEntry,
       "hgmpWhitelistNbIndex": hgmpWhitelistNbIndex,
       "hgmpWhitelistNbDeviceId": hgmpWhitelistNbDeviceId,
       "hgmpWhitelistPortName": hgmpWhitelistPortName,
       "hgmpWhitelistNbPortName": hgmpWhitelistNbPortName,
       "hgmpBlacklistTable": hgmpBlacklistTable,
       "hgmpBlacklistEntry": hgmpBlacklistEntry,
       "hgmpBlacklistDeviceId": hgmpBlacklistDeviceId,
       "hgmpBlacklistAccessDeviceId": hgmpBlacklistAccessDeviceId,
       "hgmpBlacklistAccessPortName": hgmpBlacklistAccessPortName,
       "hgmpBlacklistRowStatus": hgmpBlacklistRowStatus,
       "hgmpMemberPriPortTable": hgmpMemberPriPortTable,
       "hgmpMemberPriPortEntry": hgmpMemberPriPortEntry,
       "hgmpMemberDevId": hgmpMemberDevId,
       "hgmpMemberPriPortProto": hgmpMemberPriPortProto,
       "hgmpMemberPriPortProtoDescr": hgmpMemberPriPortProtoDescr,
       "hgmpMemberPriPortNum": hgmpMemberPriPortNum,
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
       "hgmpNTDPTopLinkStatus": hgmpNTDPTopLinkStatus,
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
       "hwNDPPortNbAgingtime": hwNDPPortNbAgingtime}
)
