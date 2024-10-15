# SNMP MIB module (HPN-ICF-HGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-HGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:29 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfHgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfClusterObject_ObjectIdentity = ObjectIdentity
hpnicfClusterObject = _HpnicfClusterObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hpnicfClusterObject.setStatus("current")
_HpnicfhgmpEventsV2_ObjectIdentity = ObjectIdentity
hpnicfhgmpEventsV2 = _HpnicfhgmpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 0)
)
if mibBuilder.loadTexts:
    hpnicfhgmpEventsV2.setStatus("current")


class _HpnicfhgmpSetVLANSecurity_Type(Integer32):
    """Custom type hpnicfhgmpSetVLANSecurity based on Integer32"""
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


_HpnicfhgmpSetVLANSecurity_Type.__name__ = "Integer32"
_HpnicfhgmpSetVLANSecurity_Object = MibScalar
hpnicfhgmpSetVLANSecurity = _HpnicfhgmpSetVLANSecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 1),
    _HpnicfhgmpSetVLANSecurity_Type()
)
hpnicfhgmpSetVLANSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpSetVLANSecurity.setStatus("current")


class _HpnicfhgmpHandShakeInterval_Type(Integer32):
    """Custom type hpnicfhgmpHandShakeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfhgmpHandShakeInterval_Type.__name__ = "Integer32"
_HpnicfhgmpHandShakeInterval_Object = MibScalar
hpnicfhgmpHandShakeInterval = _HpnicfhgmpHandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 2),
    _HpnicfhgmpHandShakeInterval_Type()
)
hpnicfhgmpHandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpHandShakeInterval.setStatus("current")


class _HpnicfhgmpHandShakeHoldtime_Type(Integer32):
    """Custom type hpnicfhgmpHandShakeHoldtime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfhgmpHandShakeHoldtime_Type.__name__ = "Integer32"
_HpnicfhgmpHandShakeHoldtime_Object = MibScalar
hpnicfhgmpHandShakeHoldtime = _HpnicfhgmpHandShakeHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 3),
    _HpnicfhgmpHandShakeHoldtime_Type()
)
hpnicfhgmpHandShakeHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpHandShakeHoldtime.setStatus("current")


class _HpnicfhgmpGrpMemberTableChange_Type(Integer32):
    """Custom type hpnicfhgmpGrpMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpGrpMemberTableChange_Type.__name__ = "Integer32"
_HpnicfhgmpGrpMemberTableChange_Object = MibScalar
hpnicfhgmpGrpMemberTableChange = _HpnicfhgmpGrpMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 4),
    _HpnicfhgmpGrpMemberTableChange_Type()
)
hpnicfhgmpGrpMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberTableChange.setStatus("current")


class _HpnicfhgmpMemberDisconRate_Type(Integer32):
    """Custom type hpnicfhgmpMemberDisconRate based on Integer32"""
    defaultValue = 0


_HpnicfhgmpMemberDisconRate_Object = MibScalar
hpnicfhgmpMemberDisconRate = _HpnicfhgmpMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 5),
    _HpnicfhgmpMemberDisconRate_Type()
)
hpnicfhgmpMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberDisconRate.setStatus("current")


class _HpnicfhgmpCmdLanswitchFlag_Type(Integer32):
    """Custom type hpnicfhgmpCmdLanswitchFlag based on Integer32"""
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


_HpnicfhgmpCmdLanswitchFlag_Type.__name__ = "Integer32"
_HpnicfhgmpCmdLanswitchFlag_Object = MibScalar
hpnicfhgmpCmdLanswitchFlag = _HpnicfhgmpCmdLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 6),
    _HpnicfhgmpCmdLanswitchFlag_Type()
)
hpnicfhgmpCmdLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpCmdLanswitchFlag.setStatus("current")


class _HpnicfhgmpCmdClusterName_Type(OctetString):
    """Custom type hpnicfhgmpCmdClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnicfhgmpCmdClusterName_Type.__name__ = "OctetString"
_HpnicfhgmpCmdClusterName_Object = MibScalar
hpnicfhgmpCmdClusterName = _HpnicfhgmpCmdClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 7),
    _HpnicfhgmpCmdClusterName_Type()
)
hpnicfhgmpCmdClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpCmdClusterName.setStatus("current")
_HpnicfhgmpMngPriIpSegCMIP_Type = IpAddress
_HpnicfhgmpMngPriIpSegCMIP_Object = MibScalar
hpnicfhgmpMngPriIpSegCMIP = _HpnicfhgmpMngPriIpSegCMIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 8),
    _HpnicfhgmpMngPriIpSegCMIP_Type()
)
hpnicfhgmpMngPriIpSegCMIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpMngPriIpSegCMIP.setStatus("current")
_HpnicfhgmpMngPriIpMask_Type = IpAddress
_HpnicfhgmpMngPriIpMask_Object = MibScalar
hpnicfhgmpMngPriIpMask = _HpnicfhgmpMngPriIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 9),
    _HpnicfhgmpMngPriIpMask_Type()
)
hpnicfhgmpMngPriIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpMngPriIpMask.setStatus("current")
_HpnicfhgmpFtpServer_Type = IpAddress
_HpnicfhgmpFtpServer_Object = MibScalar
hpnicfhgmpFtpServer = _HpnicfhgmpFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 10),
    _HpnicfhgmpFtpServer_Type()
)
hpnicfhgmpFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpFtpServer.setStatus("current")
_HpnicfhgmpTftpServer_Type = IpAddress
_HpnicfhgmpTftpServer_Object = MibScalar
hpnicfhgmpTftpServer = _HpnicfhgmpTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 11),
    _HpnicfhgmpTftpServer_Type()
)
hpnicfhgmpTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpTftpServer.setStatus("current")
_HpnicfhgmpSnmpHost_Type = IpAddress
_HpnicfhgmpSnmpHost_Object = MibScalar
hpnicfhgmpSnmpHost = _HpnicfhgmpSnmpHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 12),
    _HpnicfhgmpSnmpHost_Type()
)
hpnicfhgmpSnmpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpSnmpHost.setStatus("current")
_HpnicfhgmpLogHost_Type = IpAddress
_HpnicfhgmpLogHost_Object = MibScalar
hpnicfhgmpLogHost = _HpnicfhgmpLogHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 13),
    _HpnicfhgmpLogHost_Type()
)
hpnicfhgmpLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpLogHost.setStatus("current")
_HpnicfhgmpGrpMemberTable_Object = MibTable
hpnicfhgmpGrpMemberTable = _HpnicfhgmpGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14)
)
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberTable.setStatus("current")
_HpnicfhgmpGrpMemberEntry_Object = MibTableRow
hpnicfhgmpGrpMemberEntry = _HpnicfhgmpGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1)
)
hpnicfhgmpGrpMemberEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpGrpMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberEntry.setStatus("current")


class _HpnicfhgmpGrpMemberDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpGrpMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpGrpMemberDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpGrpMemberDeviceId_Object = MibTableColumn
hpnicfhgmpGrpMemberDeviceId = _HpnicfhgmpGrpMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 1),
    _HpnicfhgmpGrpMemberDeviceId_Type()
)
hpnicfhgmpGrpMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberDeviceId.setStatus("current")


class _HpnicfhgmpGrpMemberSerial_Type(Integer32):
    """Custom type hpnicfhgmpGrpMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HpnicfhgmpGrpMemberSerial_Type.__name__ = "Integer32"
_HpnicfhgmpGrpMemberSerial_Object = MibTableColumn
hpnicfhgmpGrpMemberSerial = _HpnicfhgmpGrpMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 2),
    _HpnicfhgmpGrpMemberSerial_Type()
)
hpnicfhgmpGrpMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberSerial.setStatus("current")
_HpnicfhgmpGrpMemberIpAddr_Type = IpAddress
_HpnicfhgmpGrpMemberIpAddr_Object = MibTableColumn
hpnicfhgmpGrpMemberIpAddr = _HpnicfhgmpGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 3),
    _HpnicfhgmpGrpMemberIpAddr_Type()
)
hpnicfhgmpGrpMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberIpAddr.setStatus("current")


class _HpnicfhgmpGrpMemberName_Type(OctetString):
    """Custom type hpnicfhgmpGrpMemberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfhgmpGrpMemberName_Type.__name__ = "OctetString"
_HpnicfhgmpGrpMemberName_Object = MibTableColumn
hpnicfhgmpGrpMemberName = _HpnicfhgmpGrpMemberName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 4),
    _HpnicfhgmpGrpMemberName_Type()
)
hpnicfhgmpGrpMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberName.setStatus("current")
_HpnicfhgmpGrpMemberPassword_Type = OctetString
_HpnicfhgmpGrpMemberPassword_Object = MibTableColumn
hpnicfhgmpGrpMemberPassword = _HpnicfhgmpGrpMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 5),
    _HpnicfhgmpGrpMemberPassword_Type()
)
hpnicfhgmpGrpMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberPassword.setStatus("current")
_HpnicfhgmpGrpMemberPlatform_Type = OctetString
_HpnicfhgmpGrpMemberPlatform_Object = MibTableColumn
hpnicfhgmpGrpMemberPlatform = _HpnicfhgmpGrpMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 6),
    _HpnicfhgmpGrpMemberPlatform_Type()
)
hpnicfhgmpGrpMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberPlatform.setStatus("current")


class _HpnicfhgmpGrpMemberStatus_Type(Integer32):
    """Custom type hpnicfhgmpGrpMemberStatus based on Integer32"""
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


_HpnicfhgmpGrpMemberStatus_Type.__name__ = "Integer32"
_HpnicfhgmpGrpMemberStatus_Object = MibTableColumn
hpnicfhgmpGrpMemberStatus = _HpnicfhgmpGrpMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 7),
    _HpnicfhgmpGrpMemberStatus_Type()
)
hpnicfhgmpGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberStatus.setStatus("current")
_HpnicfhgmpGrpMemberDisconCount_Type = Integer32
_HpnicfhgmpGrpMemberDisconCount_Object = MibTableColumn
hpnicfhgmpGrpMemberDisconCount = _HpnicfhgmpGrpMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 8),
    _HpnicfhgmpGrpMemberDisconCount_Type()
)
hpnicfhgmpGrpMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberDisconCount.setStatus("current")
_HpnicfhgmpGrpMemberEnrollTime_Type = Integer32
_HpnicfhgmpGrpMemberEnrollTime_Object = MibTableColumn
hpnicfhgmpGrpMemberEnrollTime = _HpnicfhgmpGrpMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 9),
    _HpnicfhgmpGrpMemberEnrollTime_Type()
)
hpnicfhgmpGrpMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberEnrollTime.setStatus("current")
_HpnicfhgmpGrpMemberOperate_Type = RowStatus
_HpnicfhgmpGrpMemberOperate_Object = MibTableColumn
hpnicfhgmpGrpMemberOperate = _HpnicfhgmpGrpMemberOperate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 14, 1, 10),
    _HpnicfhgmpGrpMemberOperate_Type()
)
hpnicfhgmpGrpMemberOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpGrpMemberOperate.setStatus("current")
_HpnicfhgmpMemberResetTable_Object = MibTable
hpnicfhgmpMemberResetTable = _HpnicfhgmpMemberResetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 15)
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberResetTable.setStatus("current")
_HpnicfhgmpMemberResetEntry_Object = MibTableRow
hpnicfhgmpMemberResetEntry = _HpnicfhgmpMemberResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 15, 1)
)
hpnicfhgmpMemberResetEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpMemberResetMAC"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberResetEntry.setStatus("current")


class _HpnicfhgmpMemberResetMAC_Type(OctetString):
    """Custom type hpnicfhgmpMemberResetMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HpnicfhgmpMemberResetMAC_Type.__name__ = "OctetString"
_HpnicfhgmpMemberResetMAC_Object = MibTableColumn
hpnicfhgmpMemberResetMAC = _HpnicfhgmpMemberResetMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 15, 1, 1),
    _HpnicfhgmpMemberResetMAC_Type()
)
hpnicfhgmpMemberResetMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberResetMAC.setStatus("current")


class _HpnicfhgmpMemberEraseflash_Type(Integer32):
    """Custom type hpnicfhgmpMemberEraseflash based on Integer32"""
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


_HpnicfhgmpMemberEraseflash_Type.__name__ = "Integer32"
_HpnicfhgmpMemberEraseflash_Object = MibTableColumn
hpnicfhgmpMemberEraseflash = _HpnicfhgmpMemberEraseflash_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 15, 1, 2),
    _HpnicfhgmpMemberEraseflash_Type()
)
hpnicfhgmpMemberEraseflash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberEraseflash.setStatus("current")


class _HpnicfhgmpClusterRole_Type(Integer32):
    """Custom type hpnicfhgmpClusterRole based on Integer32"""
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


_HpnicfhgmpClusterRole_Type.__name__ = "Integer32"
_HpnicfhgmpClusterRole_Object = MibScalar
hpnicfhgmpClusterRole = _HpnicfhgmpClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 16),
    _HpnicfhgmpClusterRole_Type()
)
hpnicfhgmpClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpClusterRole.setStatus("current")
_HpnicfhgmpClusterMaxPoolNum_Type = Integer32
_HpnicfhgmpClusterMaxPoolNum_Object = MibScalar
hpnicfhgmpClusterMaxPoolNum = _HpnicfhgmpClusterMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 17),
    _HpnicfhgmpClusterMaxPoolNum_Type()
)
hpnicfhgmpClusterMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpClusterMaxPoolNum.setStatus("current")


class _HpnicfhgmpClusterCmdSwMac_Type(OctetString):
    """Custom type hpnicfhgmpClusterCmdSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HpnicfhgmpClusterCmdSwMac_Type.__name__ = "OctetString"
_HpnicfhgmpClusterCmdSwMac_Object = MibScalar
hpnicfhgmpClusterCmdSwMac = _HpnicfhgmpClusterCmdSwMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 18),
    _HpnicfhgmpClusterCmdSwMac_Type()
)
hpnicfhgmpClusterCmdSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpClusterCmdSwMac.setStatus("current")


class _HpnicfhgmpRun_Type(Integer32):
    """Custom type hpnicfhgmpRun based on Integer32"""
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


_HpnicfhgmpRun_Type.__name__ = "Integer32"
_HpnicfhgmpRun_Object = MibScalar
hpnicfhgmpRun = _HpnicfhgmpRun_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 19),
    _HpnicfhgmpRun_Type()
)
hpnicfhgmpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpRun.setStatus("current")
_HpnicfhgmpProtocolMac_ObjectIdentity = ObjectIdentity
hpnicfhgmpProtocolMac = _HpnicfhgmpProtocolMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 22)
)


class _HpnicfhgmpClusterProtocolMac_Type(MacAddress):
    """Custom type hpnicfhgmpClusterProtocolMac based on MacAddress"""
    defaultHexValue = "0180C200000A"


_HpnicfhgmpClusterProtocolMac_Object = MibScalar
hpnicfhgmpClusterProtocolMac = _HpnicfhgmpClusterProtocolMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 22, 1),
    _HpnicfhgmpClusterProtocolMac_Type()
)
hpnicfhgmpClusterProtocolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpClusterProtocolMac.setStatus("current")
_HpnicfhgmpTopologyManagement_ObjectIdentity = ObjectIdentity
hpnicfhgmpTopologyManagement = _HpnicfhgmpTopologyManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23)
)
_HpnicfhgmpWhitelistTable_Object = MibTable
hpnicfhgmpWhitelistTable = _HpnicfhgmpWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 1)
)
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistTable.setStatus("current")
_HpnicfhgmpWhitelistEntry_Object = MibTableRow
hpnicfhgmpWhitelistEntry = _HpnicfhgmpWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 1, 1)
)
hpnicfhgmpWhitelistEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpWhitelistDeviceId"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistEntry.setStatus("current")


class _HpnicfhgmpWhitelistDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpWhitelistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfhgmpWhitelistDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpWhitelistDeviceId_Object = MibTableColumn
hpnicfhgmpWhitelistDeviceId = _HpnicfhgmpWhitelistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 1, 1, 1),
    _HpnicfhgmpWhitelistDeviceId_Type()
)
hpnicfhgmpWhitelistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistDeviceId.setStatus("current")


class _HpnicfhgmpWhitelistSerial_Type(Integer32):
    """Custom type hpnicfhgmpWhitelistSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfhgmpWhitelistSerial_Type.__name__ = "Integer32"
_HpnicfhgmpWhitelistSerial_Object = MibTableColumn
hpnicfhgmpWhitelistSerial = _HpnicfhgmpWhitelistSerial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 1, 1, 2),
    _HpnicfhgmpWhitelistSerial_Type()
)
hpnicfhgmpWhitelistSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistSerial.setStatus("current")
_HpnicfhgmpWhitelistRowStatus_Type = RowStatus
_HpnicfhgmpWhitelistRowStatus_Object = MibTableColumn
hpnicfhgmpWhitelistRowStatus = _HpnicfhgmpWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 1, 1, 3),
    _HpnicfhgmpWhitelistRowStatus_Type()
)
hpnicfhgmpWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistRowStatus.setStatus("current")
_HpnicfhgmpWhitelistNbTable_Object = MibTable
hpnicfhgmpWhitelistNbTable = _HpnicfhgmpWhitelistNbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2)
)
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistNbTable.setStatus("current")
_HpnicfhgmpWhitelistNbEntry_Object = MibTableRow
hpnicfhgmpWhitelistNbEntry = _HpnicfhgmpWhitelistNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2, 1)
)
hpnicfhgmpWhitelistNbEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpWhitelistDeviceId"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpWhitelistNbIndex"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistNbEntry.setStatus("current")


class _HpnicfhgmpWhitelistNbIndex_Type(Integer32):
    """Custom type hpnicfhgmpWhitelistNbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfhgmpWhitelistNbIndex_Type.__name__ = "Integer32"
_HpnicfhgmpWhitelistNbIndex_Object = MibTableColumn
hpnicfhgmpWhitelistNbIndex = _HpnicfhgmpWhitelistNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2, 1, 1),
    _HpnicfhgmpWhitelistNbIndex_Type()
)
hpnicfhgmpWhitelistNbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistNbIndex.setStatus("current")


class _HpnicfhgmpWhitelistNbDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpWhitelistNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfhgmpWhitelistNbDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpWhitelistNbDeviceId_Object = MibTableColumn
hpnicfhgmpWhitelistNbDeviceId = _HpnicfhgmpWhitelistNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2, 1, 2),
    _HpnicfhgmpWhitelistNbDeviceId_Type()
)
hpnicfhgmpWhitelistNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistNbDeviceId.setStatus("current")


class _HpnicfhgmpWhitelistPortName_Type(OctetString):
    """Custom type hpnicfhgmpWhitelistPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfhgmpWhitelistPortName_Type.__name__ = "OctetString"
_HpnicfhgmpWhitelistPortName_Object = MibTableColumn
hpnicfhgmpWhitelistPortName = _HpnicfhgmpWhitelistPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2, 1, 3),
    _HpnicfhgmpWhitelistPortName_Type()
)
hpnicfhgmpWhitelistPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistPortName.setStatus("current")


class _HpnicfhgmpWhitelistNbPortName_Type(OctetString):
    """Custom type hpnicfhgmpWhitelistNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfhgmpWhitelistNbPortName_Type.__name__ = "OctetString"
_HpnicfhgmpWhitelistNbPortName_Object = MibTableColumn
hpnicfhgmpWhitelistNbPortName = _HpnicfhgmpWhitelistNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 2, 1, 4),
    _HpnicfhgmpWhitelistNbPortName_Type()
)
hpnicfhgmpWhitelistNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpWhitelistNbPortName.setStatus("current")
_HpnicfhgmpBlacklistTable_Object = MibTable
hpnicfhgmpBlacklistTable = _HpnicfhgmpBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3)
)
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistTable.setStatus("current")
_HpnicfhgmpBlacklistEntry_Object = MibTableRow
hpnicfhgmpBlacklistEntry = _HpnicfhgmpBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3, 1)
)
hpnicfhgmpBlacklistEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpBlacklistDeviceId"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistEntry.setStatus("current")


class _HpnicfhgmpBlacklistDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpBlacklistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfhgmpBlacklistDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpBlacklistDeviceId_Object = MibTableColumn
hpnicfhgmpBlacklistDeviceId = _HpnicfhgmpBlacklistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3, 1, 1),
    _HpnicfhgmpBlacklistDeviceId_Type()
)
hpnicfhgmpBlacklistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistDeviceId.setStatus("current")


class _HpnicfhgmpBlacklistAccessDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpBlacklistAccessDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfhgmpBlacklistAccessDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpBlacklistAccessDeviceId_Object = MibTableColumn
hpnicfhgmpBlacklistAccessDeviceId = _HpnicfhgmpBlacklistAccessDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3, 1, 2),
    _HpnicfhgmpBlacklistAccessDeviceId_Type()
)
hpnicfhgmpBlacklistAccessDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistAccessDeviceId.setStatus("current")


class _HpnicfhgmpBlacklistAccessPortName_Type(OctetString):
    """Custom type hpnicfhgmpBlacklistAccessPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfhgmpBlacklistAccessPortName_Type.__name__ = "OctetString"
_HpnicfhgmpBlacklistAccessPortName_Object = MibTableColumn
hpnicfhgmpBlacklistAccessPortName = _HpnicfhgmpBlacklistAccessPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3, 1, 3),
    _HpnicfhgmpBlacklistAccessPortName_Type()
)
hpnicfhgmpBlacklistAccessPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistAccessPortName.setStatus("current")
_HpnicfhgmpBlacklistRowStatus_Type = RowStatus
_HpnicfhgmpBlacklistRowStatus_Object = MibTableColumn
hpnicfhgmpBlacklistRowStatus = _HpnicfhgmpBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 23, 3, 1, 4),
    _HpnicfhgmpBlacklistRowStatus_Type()
)
hpnicfhgmpBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfhgmpBlacklistRowStatus.setStatus("current")
_HpnicfhgmpMemberPriPortTable_Object = MibTable
hpnicfhgmpMemberPriPortTable = _HpnicfhgmpMemberPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24)
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberPriPortTable.setStatus("current")
_HpnicfhgmpMemberPriPortEntry_Object = MibTableRow
hpnicfhgmpMemberPriPortEntry = _HpnicfhgmpMemberPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24, 1)
)
hpnicfhgmpMemberPriPortEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpMemberDevId"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpMemberPriPortProto"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberPriPortEntry.setStatus("current")


class _HpnicfhgmpMemberDevId_Type(OctetString):
    """Custom type hpnicfhgmpMemberDevId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpMemberDevId_Type.__name__ = "OctetString"
_HpnicfhgmpMemberDevId_Object = MibTableColumn
hpnicfhgmpMemberDevId = _HpnicfhgmpMemberDevId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24, 1, 1),
    _HpnicfhgmpMemberDevId_Type()
)
hpnicfhgmpMemberDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberDevId.setStatus("current")
_HpnicfhgmpMemberPriPortProto_Type = Unsigned32
_HpnicfhgmpMemberPriPortProto_Object = MibTableColumn
hpnicfhgmpMemberPriPortProto = _HpnicfhgmpMemberPriPortProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24, 1, 2),
    _HpnicfhgmpMemberPriPortProto_Type()
)
hpnicfhgmpMemberPriPortProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberPriPortProto.setStatus("current")
_HpnicfhgmpMemberPriPortProtoDescr_Type = DisplayString
_HpnicfhgmpMemberPriPortProtoDescr_Object = MibTableColumn
hpnicfhgmpMemberPriPortProtoDescr = _HpnicfhgmpMemberPriPortProtoDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24, 1, 3),
    _HpnicfhgmpMemberPriPortProtoDescr_Type()
)
hpnicfhgmpMemberPriPortProtoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberPriPortProtoDescr.setStatus("current")
_HpnicfhgmpMemberPriPortNum_Type = Unsigned32
_HpnicfhgmpMemberPriPortNum_Object = MibTableColumn
hpnicfhgmpMemberPriPortNum = _HpnicfhgmpMemberPriPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 24, 1, 4),
    _HpnicfhgmpMemberPriPortNum_Type()
)
hpnicfhgmpMemberPriPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpMemberPriPortNum.setStatus("current")
_HpnicfStackObject_ObjectIdentity = ObjectIdentity
hpnicfStackObject = _HpnicfStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hpnicfStackObject.setStatus("current")
_HpnicfhgmpStackEventsV2_ObjectIdentity = ObjectIdentity
hpnicfhgmpStackEventsV2 = _HpnicfhgmpStackEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 0)
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackEventsV2.setStatus("current")


class _HpnicfhgmpStackMemberTableChange_Type(Integer32):
    """Custom type hpnicfhgmpStackMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpStackMemberTableChange_Type.__name__ = "Integer32"
_HpnicfhgmpStackMemberTableChange_Object = MibScalar
hpnicfhgmpStackMemberTableChange = _HpnicfhgmpStackMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 1),
    _HpnicfhgmpStackMemberTableChange_Type()
)
hpnicfhgmpStackMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberTableChange.setStatus("current")


class _HpnicfhgmpStackMemberDisconRate_Type(Integer32):
    """Custom type hpnicfhgmpStackMemberDisconRate based on Integer32"""
    defaultValue = 0


_HpnicfhgmpStackMemberDisconRate_Object = MibScalar
hpnicfhgmpStackMemberDisconRate = _HpnicfhgmpStackMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 2),
    _HpnicfhgmpStackMemberDisconRate_Type()
)
hpnicfhgmpStackMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberDisconRate.setStatus("current")


class _HpnicfhgmpMainLanswitchFlag_Type(Integer32):
    """Custom type hpnicfhgmpMainLanswitchFlag based on Integer32"""
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


_HpnicfhgmpMainLanswitchFlag_Type.__name__ = "Integer32"
_HpnicfhgmpMainLanswitchFlag_Object = MibScalar
hpnicfhgmpMainLanswitchFlag = _HpnicfhgmpMainLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 3),
    _HpnicfhgmpMainLanswitchFlag_Type()
)
hpnicfhgmpMainLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpMainLanswitchFlag.setStatus("current")
_HpnicfhgmpStackIpPoolStartIP_Type = IpAddress
_HpnicfhgmpStackIpPoolStartIP_Object = MibScalar
hpnicfhgmpStackIpPoolStartIP = _HpnicfhgmpStackIpPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 4),
    _HpnicfhgmpStackIpPoolStartIP_Type()
)
hpnicfhgmpStackIpPoolStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpStackIpPoolStartIP.setStatus("current")


class _HpnicfhgmpStackIpPoolLength_Type(Integer32):
    """Custom type hpnicfhgmpStackIpPoolLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HpnicfhgmpStackIpPoolLength_Type.__name__ = "Integer32"
_HpnicfhgmpStackIpPoolLength_Object = MibScalar
hpnicfhgmpStackIpPoolLength = _HpnicfhgmpStackIpPoolLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 5),
    _HpnicfhgmpStackIpPoolLength_Type()
)
hpnicfhgmpStackIpPoolLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpStackIpPoolLength.setStatus("current")
_HpnicfhgmpStackMemberTable_Object = MibTable
hpnicfhgmpStackMemberTable = _HpnicfhgmpStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberTable.setStatus("current")
_HpnicfhgmpStackMemberEntry_Object = MibTableRow
hpnicfhgmpStackMemberEntry = _HpnicfhgmpStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1)
)
hpnicfhgmpStackMemberEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpStackMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberEntry.setStatus("current")


class _HpnicfhgmpStackMemberDeviceId_Type(OctetString):
    """Custom type hpnicfhgmpStackMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpStackMemberDeviceId_Type.__name__ = "OctetString"
_HpnicfhgmpStackMemberDeviceId_Object = MibTableColumn
hpnicfhgmpStackMemberDeviceId = _HpnicfhgmpStackMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 1),
    _HpnicfhgmpStackMemberDeviceId_Type()
)
hpnicfhgmpStackMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberDeviceId.setStatus("current")


class _HpnicfhgmpStackMemberSerial_Type(Integer32):
    """Custom type hpnicfhgmpStackMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HpnicfhgmpStackMemberSerial_Type.__name__ = "Integer32"
_HpnicfhgmpStackMemberSerial_Object = MibTableColumn
hpnicfhgmpStackMemberSerial = _HpnicfhgmpStackMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 2),
    _HpnicfhgmpStackMemberSerial_Type()
)
hpnicfhgmpStackMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberSerial.setStatus("current")
_HpnicfhgmpStackMemberIpAddr_Type = IpAddress
_HpnicfhgmpStackMemberIpAddr_Object = MibTableColumn
hpnicfhgmpStackMemberIpAddr = _HpnicfhgmpStackMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 3),
    _HpnicfhgmpStackMemberIpAddr_Type()
)
hpnicfhgmpStackMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberIpAddr.setStatus("current")
_HpnicfhgmpStackMemberName_Type = OctetString
_HpnicfhgmpStackMemberName_Object = MibTableColumn
hpnicfhgmpStackMemberName = _HpnicfhgmpStackMemberName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 4),
    _HpnicfhgmpStackMemberName_Type()
)
hpnicfhgmpStackMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberName.setStatus("current")
_HpnicfhgmpStackMemberPassword_Type = OctetString
_HpnicfhgmpStackMemberPassword_Object = MibTableColumn
hpnicfhgmpStackMemberPassword = _HpnicfhgmpStackMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 5),
    _HpnicfhgmpStackMemberPassword_Type()
)
hpnicfhgmpStackMemberPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberPassword.setStatus("current")
_HpnicfhgmpStackMemberPlatform_Type = OctetString
_HpnicfhgmpStackMemberPlatform_Object = MibTableColumn
hpnicfhgmpStackMemberPlatform = _HpnicfhgmpStackMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 6),
    _HpnicfhgmpStackMemberPlatform_Type()
)
hpnicfhgmpStackMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberPlatform.setStatus("current")


class _HpnicfhgmpStackMemberStatus_Type(Integer32):
    """Custom type hpnicfhgmpStackMemberStatus based on Integer32"""
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


_HpnicfhgmpStackMemberStatus_Type.__name__ = "Integer32"
_HpnicfhgmpStackMemberStatus_Object = MibTableColumn
hpnicfhgmpStackMemberStatus = _HpnicfhgmpStackMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 7),
    _HpnicfhgmpStackMemberStatus_Type()
)
hpnicfhgmpStackMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberStatus.setStatus("current")
_HpnicfhgmpStackMemberDisconCount_Type = Integer32
_HpnicfhgmpStackMemberDisconCount_Object = MibTableColumn
hpnicfhgmpStackMemberDisconCount = _HpnicfhgmpStackMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 8),
    _HpnicfhgmpStackMemberDisconCount_Type()
)
hpnicfhgmpStackMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberDisconCount.setStatus("current")
_HpnicfhgmpStackMemberEnrollTime_Type = Integer32
_HpnicfhgmpStackMemberEnrollTime_Object = MibTableColumn
hpnicfhgmpStackMemberEnrollTime = _HpnicfhgmpStackMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 6, 1, 9),
    _HpnicfhgmpStackMemberEnrollTime_Type()
)
hpnicfhgmpStackMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberEnrollTime.setStatus("current")


class _HpnicfhgmpStackRole_Type(Integer32):
    """Custom type hpnicfhgmpStackRole based on Integer32"""
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


_HpnicfhgmpStackRole_Type.__name__ = "Integer32"
_HpnicfhgmpStackRole_Object = MibScalar
hpnicfhgmpStackRole = _HpnicfhgmpStackRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 7),
    _HpnicfhgmpStackRole_Type()
)
hpnicfhgmpStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackRole.setStatus("current")
_HpnicfhgmpStackMaxPoolNum_Type = Integer32
_HpnicfhgmpStackMaxPoolNum_Object = MibScalar
hpnicfhgmpStackMaxPoolNum = _HpnicfhgmpStackMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 8),
    _HpnicfhgmpStackMaxPoolNum_Type()
)
hpnicfhgmpStackMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMaxPoolNum.setStatus("current")


class _HpnicfhgmpStackMainSwMac_Type(OctetString):
    """Custom type hpnicfhgmpStackMainSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HpnicfhgmpStackMainSwMac_Type.__name__ = "OctetString"
_HpnicfhgmpStackMainSwMac_Object = MibScalar
hpnicfhgmpStackMainSwMac = _HpnicfhgmpStackMainSwMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 9),
    _HpnicfhgmpStackMainSwMac_Type()
)
hpnicfhgmpStackMainSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpStackMainSwMac.setStatus("current")


class _HpnicfhgmpStackIpPoolMask_Type(IpAddress):
    """Custom type hpnicfhgmpStackIpPoolMask based on IpAddress"""
    defaultHexValue = "FFFF0000"


_HpnicfhgmpStackIpPoolMask_Object = MibScalar
hpnicfhgmpStackIpPoolMask = _HpnicfhgmpStackIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 10),
    _HpnicfhgmpStackIpPoolMask_Type()
)
hpnicfhgmpStackIpPoolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpStackIpPoolMask.setStatus("current")
_HpnicfNTDPObject_ObjectIdentity = ObjectIdentity
hpnicfNTDPObject = _HpnicfNTDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4)
)
if mibBuilder.loadTexts:
    hpnicfNTDPObject.setStatus("current")


class _HpnicfhgmpNTDPCollectTopTime_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCollectTopTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpNTDPCollectTopTime_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPCollectTopTime_Object = MibScalar
hpnicfhgmpNTDPCollectTopTime = _HpnicfhgmpNTDPCollectTopTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 1),
    _HpnicfhgmpNTDPCollectTopTime_Type()
)
hpnicfhgmpNTDPCollectTopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCollectTopTime.setStatus("current")


class _HpnicfhgmpNTDPHopRange_Type(Integer32):
    """Custom type hpnicfhgmpNTDPHopRange based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfhgmpNTDPHopRange_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPHopRange_Object = MibScalar
hpnicfhgmpNTDPHopRange = _HpnicfhgmpNTDPHopRange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 2),
    _HpnicfhgmpNTDPHopRange_Type()
)
hpnicfhgmpNTDPHopRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPHopRange.setStatus("current")


class _HpnicfhgmpNTDPRun_Type(Integer32):
    """Custom type hpnicfhgmpNTDPRun based on Integer32"""
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


_HpnicfhgmpNTDPRun_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPRun_Object = MibScalar
hpnicfhgmpNTDPRun = _HpnicfhgmpNTDPRun_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 3),
    _HpnicfhgmpNTDPRun_Type()
)
hpnicfhgmpNTDPRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPRun.setStatus("current")


class _HpnicfhgmpNTDPPortDelay_Type(Integer32):
    """Custom type hpnicfhgmpNTDPPortDelay based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfhgmpNTDPPortDelay_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPPortDelay_Object = MibScalar
hpnicfhgmpNTDPPortDelay = _HpnicfhgmpNTDPPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 4),
    _HpnicfhgmpNTDPPortDelay_Type()
)
hpnicfhgmpNTDPPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPPortDelay.setStatus("current")


class _HpnicfhgmpNTDPHopDelay_Type(Integer32):
    """Custom type hpnicfhgmpNTDPHopDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HpnicfhgmpNTDPHopDelay_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPHopDelay_Object = MibScalar
hpnicfhgmpNTDPHopDelay = _HpnicfhgmpNTDPHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 5),
    _HpnicfhgmpNTDPHopDelay_Type()
)
hpnicfhgmpNTDPHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPHopDelay.setStatus("current")


class _HpnicfhgmpNTDPLastTopCollectDuration_Type(Integer32):
    """Custom type hpnicfhgmpNTDPLastTopCollectDuration based on Integer32"""
    defaultValue = 0


_HpnicfhgmpNTDPLastTopCollectDuration_Object = MibScalar
hpnicfhgmpNTDPLastTopCollectDuration = _HpnicfhgmpNTDPLastTopCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 6),
    _HpnicfhgmpNTDPLastTopCollectDuration_Type()
)
hpnicfhgmpNTDPLastTopCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPLastTopCollectDuration.setStatus("current")


class _HpnicfhgmpNTDPCacheChange_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCacheChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpNTDPCacheChange_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPCacheChange_Object = MibScalar
hpnicfhgmpNTDPCacheChange = _HpnicfhgmpNTDPCacheChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 7),
    _HpnicfhgmpNTDPCacheChange_Type()
)
hpnicfhgmpNTDPCacheChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheChange.setStatus("current")


class _HpnicfhgmpNTDPTOPTableChange_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTOPTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpNTDPTOPTableChange_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPTOPTableChange_Object = MibScalar
hpnicfhgmpNTDPTOPTableChange = _HpnicfhgmpNTDPTOPTableChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 8),
    _HpnicfhgmpNTDPTOPTableChange_Type()
)
hpnicfhgmpNTDPTOPTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTOPTableChange.setStatus("current")
_HpnicfhgmpNTDPInterfaceTable_Object = MibTable
hpnicfhgmpNTDPInterfaceTable = _HpnicfhgmpNTDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 9)
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPInterfaceTable.setStatus("current")
_HpnicfhgmpNTDPInterfaceEntry_Object = MibTableRow
hpnicfhgmpNTDPInterfaceEntry = _HpnicfhgmpNTDPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 9, 1)
)
hpnicfhgmpNTDPInterfaceEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPInterfaceEntry.setStatus("current")
_HpnicfhgmpNTDPInterfaceIfIndex_Type = Integer32
_HpnicfhgmpNTDPInterfaceIfIndex_Object = MibTableColumn
hpnicfhgmpNTDPInterfaceIfIndex = _HpnicfhgmpNTDPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 9, 1, 1),
    _HpnicfhgmpNTDPInterfaceIfIndex_Type()
)
hpnicfhgmpNTDPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPInterfaceIfIndex.setStatus("current")


class _HpnicfhgmpNTDPInterfaceEnable_Type(Integer32):
    """Custom type hpnicfhgmpNTDPInterfaceEnable based on Integer32"""
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


_HpnicfhgmpNTDPInterfaceEnable_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPInterfaceEnable_Object = MibTableColumn
hpnicfhgmpNTDPInterfaceEnable = _HpnicfhgmpNTDPInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 9, 1, 2),
    _HpnicfhgmpNTDPInterfaceEnable_Type()
)
hpnicfhgmpNTDPInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPInterfaceEnable.setStatus("current")
_HpnicfhgmpNTDPCacheTable_Object = MibTable
hpnicfhgmpNTDPCacheTable = _HpnicfhgmpNTDPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10)
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheTable.setStatus("current")
_HpnicfhgmpNTDPCacheEntry_Object = MibTableRow
hpnicfhgmpNTDPCacheEntry = _HpnicfhgmpNTDPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1)
)
hpnicfhgmpNTDPCacheEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPCacheHashIndex"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPCacheDeviceID"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheEntry.setStatus("current")


class _HpnicfhgmpNTDPCacheHashIndex_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCacheHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfhgmpNTDPCacheHashIndex_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPCacheHashIndex_Object = MibTableColumn
hpnicfhgmpNTDPCacheHashIndex = _HpnicfhgmpNTDPCacheHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 1),
    _HpnicfhgmpNTDPCacheHashIndex_Type()
)
hpnicfhgmpNTDPCacheHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheHashIndex.setStatus("current")


class _HpnicfhgmpNTDPCacheDeviceID_Type(OctetString):
    """Custom type hpnicfhgmpNTDPCacheDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpNTDPCacheDeviceID_Type.__name__ = "OctetString"
_HpnicfhgmpNTDPCacheDeviceID_Object = MibTableColumn
hpnicfhgmpNTDPCacheDeviceID = _HpnicfhgmpNTDPCacheDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 2),
    _HpnicfhgmpNTDPCacheDeviceID_Type()
)
hpnicfhgmpNTDPCacheDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheDeviceID.setStatus("current")
_HpnicfhgmpNTDPCacheClusterName_Type = OctetString
_HpnicfhgmpNTDPCacheClusterName_Object = MibTableColumn
hpnicfhgmpNTDPCacheClusterName = _HpnicfhgmpNTDPCacheClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 3),
    _HpnicfhgmpNTDPCacheClusterName_Type()
)
hpnicfhgmpNTDPCacheClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheClusterName.setStatus("current")


class _HpnicfhgmpNTDPCacheClusterRole_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCacheClusterRole based on Integer32"""
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


_HpnicfhgmpNTDPCacheClusterRole_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPCacheClusterRole_Object = MibTableColumn
hpnicfhgmpNTDPCacheClusterRole = _HpnicfhgmpNTDPCacheClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 4),
    _HpnicfhgmpNTDPCacheClusterRole_Type()
)
hpnicfhgmpNTDPCacheClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheClusterRole.setStatus("current")


class _HpnicfhgmpNTDPCacheCapabilities_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCacheCapabilities based on Integer32"""
    defaultValue = 255


_HpnicfhgmpNTDPCacheCapabilities_Object = MibTableColumn
hpnicfhgmpNTDPCacheCapabilities = _HpnicfhgmpNTDPCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 5),
    _HpnicfhgmpNTDPCacheCapabilities_Type()
)
hpnicfhgmpNTDPCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheCapabilities.setStatus("current")
_HpnicfhgmpNTDPCacheVersion_Type = OctetString
_HpnicfhgmpNTDPCacheVersion_Object = MibTableColumn
hpnicfhgmpNTDPCacheVersion = _HpnicfhgmpNTDPCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 6),
    _HpnicfhgmpNTDPCacheVersion_Type()
)
hpnicfhgmpNTDPCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheVersion.setStatus("current")
_HpnicfhgmpNTDPCachePlatform_Type = OctetString
_HpnicfhgmpNTDPCachePlatform_Object = MibTableColumn
hpnicfhgmpNTDPCachePlatform = _HpnicfhgmpNTDPCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 7),
    _HpnicfhgmpNTDPCachePlatform_Type()
)
hpnicfhgmpNTDPCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCachePlatform.setStatus("current")


class _HpnicfhgmpNTDPCacheMngVLAN_Type(Integer32):
    """Custom type hpnicfhgmpNTDPCacheMngVLAN based on Integer32"""
    defaultValue = 1


_HpnicfhgmpNTDPCacheMngVLAN_Object = MibTableColumn
hpnicfhgmpNTDPCacheMngVLAN = _HpnicfhgmpNTDPCacheMngVLAN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 8),
    _HpnicfhgmpNTDPCacheMngVLAN_Type()
)
hpnicfhgmpNTDPCacheMngVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheMngVLAN.setStatus("current")
_HpnicfhgmpNTDPCacheHop_Type = Integer32
_HpnicfhgmpNTDPCacheHop_Object = MibTableColumn
hpnicfhgmpNTDPCacheHop = _HpnicfhgmpNTDPCacheHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 10, 1, 9),
    _HpnicfhgmpNTDPCacheHop_Type()
)
hpnicfhgmpNTDPCacheHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPCacheHop.setStatus("current")
_HpnicfhgmpNTDPTopTable_Object = MibTable
hpnicfhgmpNTDPTopTable = _HpnicfhgmpNTDPTopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11)
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopTable.setStatus("current")
_HpnicfhgmpNTDPTopEntry_Object = MibTableRow
hpnicfhgmpNTDPTopEntry = _HpnicfhgmpNTDPTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1)
)
hpnicfhgmpNTDPTopEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPTopHashIndex"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPTopEdgeStartDevID"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPTopEdgeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEntry.setStatus("current")


class _HpnicfhgmpNTDPTopHashIndex_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTopHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfhgmpNTDPTopHashIndex_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPTopHashIndex_Object = MibTableColumn
hpnicfhgmpNTDPTopHashIndex = _HpnicfhgmpNTDPTopHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 1),
    _HpnicfhgmpNTDPTopHashIndex_Type()
)
hpnicfhgmpNTDPTopHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopHashIndex.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeStartDevID_Type(OctetString):
    """Custom type hpnicfhgmpNTDPTopEdgeStartDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpNTDPTopEdgeStartDevID_Type.__name__ = "OctetString"
_HpnicfhgmpNTDPTopEdgeStartDevID_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeStartDevID = _HpnicfhgmpNTDPTopEdgeStartDevID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 2),
    _HpnicfhgmpNTDPTopEdgeStartDevID_Type()
)
hpnicfhgmpNTDPTopEdgeStartDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeStartDevID.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeIndex_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTopEdgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfhgmpNTDPTopEdgeIndex_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPTopEdgeIndex_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeIndex = _HpnicfhgmpNTDPTopEdgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 3),
    _HpnicfhgmpNTDPTopEdgeIndex_Type()
)
hpnicfhgmpNTDPTopEdgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeIndex.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeEndDevID_Type(OctetString):
    """Custom type hpnicfhgmpNTDPTopEdgeEndDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfhgmpNTDPTopEdgeEndDevID_Type.__name__ = "OctetString"
_HpnicfhgmpNTDPTopEdgeEndDevID_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeEndDevID = _HpnicfhgmpNTDPTopEdgeEndDevID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 4),
    _HpnicfhgmpNTDPTopEdgeEndDevID_Type()
)
hpnicfhgmpNTDPTopEdgeEndDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeEndDevID.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeStartPort_Type(OctetString):
    """Custom type hpnicfhgmpNTDPTopEdgeStartPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfhgmpNTDPTopEdgeStartPort_Type.__name__ = "OctetString"
_HpnicfhgmpNTDPTopEdgeStartPort_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPort = _HpnicfhgmpNTDPTopEdgeStartPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 5),
    _HpnicfhgmpNTDPTopEdgeStartPort_Type()
)
hpnicfhgmpNTDPTopEdgeStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeStartPort.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTopEdgeStartPortFullDuplex based on Integer32"""
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


_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPortFullDuplex = _HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 6),
    _HpnicfhgmpNTDPTopEdgeStartPortFullDuplex_Type()
)
hpnicfhgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeStartPortFullDuplex.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeStartPortSpeed_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTopEdgeStartPortSpeed based on Integer32"""
    defaultValue = 0


_HpnicfhgmpNTDPTopEdgeStartPortSpeed_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeStartPortSpeed = _HpnicfhgmpNTDPTopEdgeStartPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 7),
    _HpnicfhgmpNTDPTopEdgeStartPortSpeed_Type()
)
hpnicfhgmpNTDPTopEdgeStartPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeStartPortSpeed.setStatus("current")


class _HpnicfhgmpNTDPTopEdgeEndPort_Type(OctetString):
    """Custom type hpnicfhgmpNTDPTopEdgeEndPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfhgmpNTDPTopEdgeEndPort_Type.__name__ = "OctetString"
_HpnicfhgmpNTDPTopEdgeEndPort_Object = MibTableColumn
hpnicfhgmpNTDPTopEdgeEndPort = _HpnicfhgmpNTDPTopEdgeEndPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 8),
    _HpnicfhgmpNTDPTopEdgeEndPort_Type()
)
hpnicfhgmpNTDPTopEdgeEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopEdgeEndPort.setStatus("current")


class _HpnicfhgmpNTDPTopLinkStatus_Type(Integer32):
    """Custom type hpnicfhgmpNTDPTopLinkStatus based on Integer32"""
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


_HpnicfhgmpNTDPTopLinkStatus_Type.__name__ = "Integer32"
_HpnicfhgmpNTDPTopLinkStatus_Object = MibTableColumn
hpnicfhgmpNTDPTopLinkStatus = _HpnicfhgmpNTDPTopLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 4, 11, 1, 11),
    _HpnicfhgmpNTDPTopLinkStatus_Type()
)
hpnicfhgmpNTDPTopLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfhgmpNTDPTopLinkStatus.setStatus("current")
_HpnicfNDPObject_ObjectIdentity = ObjectIdentity
hpnicfNDPObject = _HpnicfNDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5)
)
if mibBuilder.loadTexts:
    hpnicfNDPObject.setStatus("current")


class _HpnicfNDPStatus_Type(Integer32):
    """Custom type hpnicfNDPStatus based on Integer32"""
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


_HpnicfNDPStatus_Type.__name__ = "Integer32"
_HpnicfNDPStatus_Object = MibScalar
hpnicfNDPStatus = _HpnicfNDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 1),
    _HpnicfNDPStatus_Type()
)
hpnicfNDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNDPStatus.setStatus("current")


class _HpnicfNDPHelloTimer_Type(Integer32):
    """Custom type hpnicfNDPHelloTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_HpnicfNDPHelloTimer_Type.__name__ = "Integer32"
_HpnicfNDPHelloTimer_Object = MibScalar
hpnicfNDPHelloTimer = _HpnicfNDPHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 2),
    _HpnicfNDPHelloTimer_Type()
)
hpnicfNDPHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNDPHelloTimer.setStatus("current")


class _HpnicfNDPAgingTime_Type(Integer32):
    """Custom type hpnicfNDPAgingTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HpnicfNDPAgingTime_Type.__name__ = "Integer32"
_HpnicfNDPAgingTime_Object = MibScalar
hpnicfNDPAgingTime = _HpnicfNDPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 3),
    _HpnicfNDPAgingTime_Type()
)
hpnicfNDPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNDPAgingTime.setStatus("current")


class _HpnicfNDPChange_Type(Counter32):
    """Custom type hpnicfNDPChange based on Counter32"""
    defaultValue = 0


_HpnicfNDPChange_Object = MibScalar
hpnicfNDPChange = _HpnicfNDPChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 4),
    _HpnicfNDPChange_Type()
)
hpnicfNDPChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPChange.setStatus("current")
_HpnicfNDPPortTable_Object = MibTable
hpnicfNDPPortTable = _HpnicfNDPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 5)
)
if mibBuilder.loadTexts:
    hpnicfNDPPortTable.setStatus("current")
_HpnicfNDPPortEntry_Object = MibTableRow
hpnicfNDPPortEntry = _HpnicfNDPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 5, 1)
)
hpnicfNDPPortEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfNDPIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNDPPortEntry.setStatus("current")
_HpnicfNDPIfIndex_Type = Integer32
_HpnicfNDPIfIndex_Object = MibTableColumn
hpnicfNDPIfIndex = _HpnicfNDPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 5, 1, 1),
    _HpnicfNDPIfIndex_Type()
)
hpnicfNDPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPIfIndex.setStatus("current")


class _HpnicfNDPPortStatus_Type(Integer32):
    """Custom type hpnicfNDPPortStatus based on Integer32"""
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


_HpnicfNDPPortStatus_Type.__name__ = "Integer32"
_HpnicfNDPPortStatus_Object = MibTableColumn
hpnicfNDPPortStatus = _HpnicfNDPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 5, 1, 2),
    _HpnicfNDPPortStatus_Type()
)
hpnicfNDPPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNDPPortStatus.setStatus("current")
_HpnicfNDPPortNbTable_Object = MibTable
hpnicfNDPPortNbTable = _HpnicfNDPPortNbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6)
)
if mibBuilder.loadTexts:
    hpnicfNDPPortNbTable.setStatus("current")
_HpnicfNDPPortNbEntry_Object = MibTableRow
hpnicfNDPPortNbEntry = _HpnicfNDPPortNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1)
)
hpnicfNDPPortNbEntry.setIndexNames(
    (0, "HPN-ICF-HGMP-MIB", "hpnicfNDPIfIndex"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfNDPPortNbDeviceId"),
    (0, "HPN-ICF-HGMP-MIB", "hpnicfNDPPortNbPortName"),
)
if mibBuilder.loadTexts:
    hpnicfNDPPortNbEntry.setStatus("current")


class _HpnicfNDPPortNbDeviceId_Type(OctetString):
    """Custom type hpnicfNDPPortNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnicfNDPPortNbDeviceId_Type.__name__ = "OctetString"
_HpnicfNDPPortNbDeviceId_Object = MibTableColumn
hpnicfNDPPortNbDeviceId = _HpnicfNDPPortNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 1),
    _HpnicfNDPPortNbDeviceId_Type()
)
hpnicfNDPPortNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbDeviceId.setStatus("current")


class _HpnicfNDPPortNbPortName_Type(OctetString):
    """Custom type hpnicfNDPPortNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfNDPPortNbPortName_Type.__name__ = "OctetString"
_HpnicfNDPPortNbPortName_Object = MibTableColumn
hpnicfNDPPortNbPortName = _HpnicfNDPPortNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 2),
    _HpnicfNDPPortNbPortName_Type()
)
hpnicfNDPPortNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbPortName.setStatus("current")
_HpnicfNDPPortNbDeviceName_Type = OctetString
_HpnicfNDPPortNbDeviceName_Object = MibTableColumn
hpnicfNDPPortNbDeviceName = _HpnicfNDPPortNbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 3),
    _HpnicfNDPPortNbDeviceName_Type()
)
hpnicfNDPPortNbDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbDeviceName.setStatus("current")


class _HpnicfNDPPortNbPortMode_Type(Integer32):
    """Custom type hpnicfNDPPortNbPortMode based on Integer32"""
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


_HpnicfNDPPortNbPortMode_Type.__name__ = "Integer32"
_HpnicfNDPPortNbPortMode_Object = MibTableColumn
hpnicfNDPPortNbPortMode = _HpnicfNDPPortNbPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 4),
    _HpnicfNDPPortNbPortMode_Type()
)
hpnicfNDPPortNbPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbPortMode.setStatus("current")
_HpnicfNDPPortNbProductVer_Type = OctetString
_HpnicfNDPPortNbProductVer_Object = MibTableColumn
hpnicfNDPPortNbProductVer = _HpnicfNDPPortNbProductVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 5),
    _HpnicfNDPPortNbProductVer_Type()
)
hpnicfNDPPortNbProductVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbProductVer.setStatus("current")
_HpnicfNDPPortNbHardVer_Type = OctetString
_HpnicfNDPPortNbHardVer_Object = MibTableColumn
hpnicfNDPPortNbHardVer = _HpnicfNDPPortNbHardVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 6),
    _HpnicfNDPPortNbHardVer_Type()
)
hpnicfNDPPortNbHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbHardVer.setStatus("current")
_HpnicfNDPPortNbBootromVer_Type = OctetString
_HpnicfNDPPortNbBootromVer_Object = MibTableColumn
hpnicfNDPPortNbBootromVer = _HpnicfNDPPortNbBootromVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 7),
    _HpnicfNDPPortNbBootromVer_Type()
)
hpnicfNDPPortNbBootromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbBootromVer.setStatus("current")
_HpnicfNDPPortNbSoftVer_Type = OctetString
_HpnicfNDPPortNbSoftVer_Object = MibTableColumn
hpnicfNDPPortNbSoftVer = _HpnicfNDPPortNbSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 8),
    _HpnicfNDPPortNbSoftVer_Type()
)
hpnicfNDPPortNbSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbSoftVer.setStatus("current")


class _HpnicfNDPPortNbAgingtime_Type(Integer32):
    """Custom type hpnicfNDPPortNbAgingtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HpnicfNDPPortNbAgingtime_Type.__name__ = "Integer32"
_HpnicfNDPPortNbAgingtime_Object = MibTableColumn
hpnicfNDPPortNbAgingtime = _HpnicfNDPPortNbAgingtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 5, 6, 1, 9),
    _HpnicfNDPPortNbAgingtime_Type()
)
hpnicfNDPPortNbAgingtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNDPPortNbAgingtime.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfhgmpMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 0, 1)
)
hpnicfhgmpMemberfailure.setObjects(
    ("HPN-ICF-HGMP-MIB", "hpnicfhgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberfailure.setStatus(
        "current"
    )

hpnicfhgmpMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 0, 2)
)
hpnicfhgmpMemberRecover.setObjects(
    ("HPN-ICF-HGMP-MIB", "hpnicfhgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberRecover.setStatus(
        "current"
    )

hpnicfhgmpMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 0, 3)
)
hpnicfhgmpMemberStatusChange.setObjects(
      *(("HPN-ICF-HGMP-MIB", "hpnicfhgmpGrpMemberDeviceId"),
        ("HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hpnicfhgmpMemberStatusChange.setStatus(
        "current"
    )

hpnicfhgmpNetTopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 1, 0, 4)
)
if mibBuilder.loadTexts:
    hpnicfhgmpNetTopChange.setStatus(
        "current"
    )

hpnicfhgmpStackMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 0, 1)
)
hpnicfhgmpStackMemberfailure.setObjects(
    ("HPN-ICF-HGMP-MIB", "hpnicfhgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberfailure.setStatus(
        "current"
    )

hpnicfhgmpStackMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 0, 2)
)
hpnicfhgmpStackMemberRecover.setObjects(
    ("HPN-ICF-HGMP-MIB", "hpnicfhgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberRecover.setStatus(
        "current"
    )

hpnicfhgmpStackMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7, 2, 0, 3)
)
hpnicfhgmpStackMemberStatusChange.setObjects(
      *(("HPN-ICF-HGMP-MIB", "hpnicfhgmpStackMemberDeviceId"),
        ("HPN-ICF-HGMP-MIB", "hpnicfhgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hpnicfhgmpStackMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-HGMP-MIB",
    **{"hpnicfHgmp": hpnicfHgmp,
       "hpnicfClusterObject": hpnicfClusterObject,
       "hpnicfhgmpEventsV2": hpnicfhgmpEventsV2,
       "hpnicfhgmpMemberfailure": hpnicfhgmpMemberfailure,
       "hpnicfhgmpMemberRecover": hpnicfhgmpMemberRecover,
       "hpnicfhgmpMemberStatusChange": hpnicfhgmpMemberStatusChange,
       "hpnicfhgmpNetTopChange": hpnicfhgmpNetTopChange,
       "hpnicfhgmpSetVLANSecurity": hpnicfhgmpSetVLANSecurity,
       "hpnicfhgmpHandShakeInterval": hpnicfhgmpHandShakeInterval,
       "hpnicfhgmpHandShakeHoldtime": hpnicfhgmpHandShakeHoldtime,
       "hpnicfhgmpGrpMemberTableChange": hpnicfhgmpGrpMemberTableChange,
       "hpnicfhgmpMemberDisconRate": hpnicfhgmpMemberDisconRate,
       "hpnicfhgmpCmdLanswitchFlag": hpnicfhgmpCmdLanswitchFlag,
       "hpnicfhgmpCmdClusterName": hpnicfhgmpCmdClusterName,
       "hpnicfhgmpMngPriIpSegCMIP": hpnicfhgmpMngPriIpSegCMIP,
       "hpnicfhgmpMngPriIpMask": hpnicfhgmpMngPriIpMask,
       "hpnicfhgmpFtpServer": hpnicfhgmpFtpServer,
       "hpnicfhgmpTftpServer": hpnicfhgmpTftpServer,
       "hpnicfhgmpSnmpHost": hpnicfhgmpSnmpHost,
       "hpnicfhgmpLogHost": hpnicfhgmpLogHost,
       "hpnicfhgmpGrpMemberTable": hpnicfhgmpGrpMemberTable,
       "hpnicfhgmpGrpMemberEntry": hpnicfhgmpGrpMemberEntry,
       "hpnicfhgmpGrpMemberDeviceId": hpnicfhgmpGrpMemberDeviceId,
       "hpnicfhgmpGrpMemberSerial": hpnicfhgmpGrpMemberSerial,
       "hpnicfhgmpGrpMemberIpAddr": hpnicfhgmpGrpMemberIpAddr,
       "hpnicfhgmpGrpMemberName": hpnicfhgmpGrpMemberName,
       "hpnicfhgmpGrpMemberPassword": hpnicfhgmpGrpMemberPassword,
       "hpnicfhgmpGrpMemberPlatform": hpnicfhgmpGrpMemberPlatform,
       "hpnicfhgmpGrpMemberStatus": hpnicfhgmpGrpMemberStatus,
       "hpnicfhgmpGrpMemberDisconCount": hpnicfhgmpGrpMemberDisconCount,
       "hpnicfhgmpGrpMemberEnrollTime": hpnicfhgmpGrpMemberEnrollTime,
       "hpnicfhgmpGrpMemberOperate": hpnicfhgmpGrpMemberOperate,
       "hpnicfhgmpMemberResetTable": hpnicfhgmpMemberResetTable,
       "hpnicfhgmpMemberResetEntry": hpnicfhgmpMemberResetEntry,
       "hpnicfhgmpMemberResetMAC": hpnicfhgmpMemberResetMAC,
       "hpnicfhgmpMemberEraseflash": hpnicfhgmpMemberEraseflash,
       "hpnicfhgmpClusterRole": hpnicfhgmpClusterRole,
       "hpnicfhgmpClusterMaxPoolNum": hpnicfhgmpClusterMaxPoolNum,
       "hpnicfhgmpClusterCmdSwMac": hpnicfhgmpClusterCmdSwMac,
       "hpnicfhgmpRun": hpnicfhgmpRun,
       "hpnicfhgmpProtocolMac": hpnicfhgmpProtocolMac,
       "hpnicfhgmpClusterProtocolMac": hpnicfhgmpClusterProtocolMac,
       "hpnicfhgmpTopologyManagement": hpnicfhgmpTopologyManagement,
       "hpnicfhgmpWhitelistTable": hpnicfhgmpWhitelistTable,
       "hpnicfhgmpWhitelistEntry": hpnicfhgmpWhitelistEntry,
       "hpnicfhgmpWhitelistDeviceId": hpnicfhgmpWhitelistDeviceId,
       "hpnicfhgmpWhitelistSerial": hpnicfhgmpWhitelistSerial,
       "hpnicfhgmpWhitelistRowStatus": hpnicfhgmpWhitelistRowStatus,
       "hpnicfhgmpWhitelistNbTable": hpnicfhgmpWhitelistNbTable,
       "hpnicfhgmpWhitelistNbEntry": hpnicfhgmpWhitelistNbEntry,
       "hpnicfhgmpWhitelistNbIndex": hpnicfhgmpWhitelistNbIndex,
       "hpnicfhgmpWhitelistNbDeviceId": hpnicfhgmpWhitelistNbDeviceId,
       "hpnicfhgmpWhitelistPortName": hpnicfhgmpWhitelistPortName,
       "hpnicfhgmpWhitelistNbPortName": hpnicfhgmpWhitelistNbPortName,
       "hpnicfhgmpBlacklistTable": hpnicfhgmpBlacklistTable,
       "hpnicfhgmpBlacklistEntry": hpnicfhgmpBlacklistEntry,
       "hpnicfhgmpBlacklistDeviceId": hpnicfhgmpBlacklistDeviceId,
       "hpnicfhgmpBlacklistAccessDeviceId": hpnicfhgmpBlacklistAccessDeviceId,
       "hpnicfhgmpBlacklistAccessPortName": hpnicfhgmpBlacklistAccessPortName,
       "hpnicfhgmpBlacklistRowStatus": hpnicfhgmpBlacklistRowStatus,
       "hpnicfhgmpMemberPriPortTable": hpnicfhgmpMemberPriPortTable,
       "hpnicfhgmpMemberPriPortEntry": hpnicfhgmpMemberPriPortEntry,
       "hpnicfhgmpMemberDevId": hpnicfhgmpMemberDevId,
       "hpnicfhgmpMemberPriPortProto": hpnicfhgmpMemberPriPortProto,
       "hpnicfhgmpMemberPriPortProtoDescr": hpnicfhgmpMemberPriPortProtoDescr,
       "hpnicfhgmpMemberPriPortNum": hpnicfhgmpMemberPriPortNum,
       "hpnicfStackObject": hpnicfStackObject,
       "hpnicfhgmpStackEventsV2": hpnicfhgmpStackEventsV2,
       "hpnicfhgmpStackMemberfailure": hpnicfhgmpStackMemberfailure,
       "hpnicfhgmpStackMemberRecover": hpnicfhgmpStackMemberRecover,
       "hpnicfhgmpStackMemberStatusChange": hpnicfhgmpStackMemberStatusChange,
       "hpnicfhgmpStackMemberTableChange": hpnicfhgmpStackMemberTableChange,
       "hpnicfhgmpStackMemberDisconRate": hpnicfhgmpStackMemberDisconRate,
       "hpnicfhgmpMainLanswitchFlag": hpnicfhgmpMainLanswitchFlag,
       "hpnicfhgmpStackIpPoolStartIP": hpnicfhgmpStackIpPoolStartIP,
       "hpnicfhgmpStackIpPoolLength": hpnicfhgmpStackIpPoolLength,
       "hpnicfhgmpStackMemberTable": hpnicfhgmpStackMemberTable,
       "hpnicfhgmpStackMemberEntry": hpnicfhgmpStackMemberEntry,
       "hpnicfhgmpStackMemberDeviceId": hpnicfhgmpStackMemberDeviceId,
       "hpnicfhgmpStackMemberSerial": hpnicfhgmpStackMemberSerial,
       "hpnicfhgmpStackMemberIpAddr": hpnicfhgmpStackMemberIpAddr,
       "hpnicfhgmpStackMemberName": hpnicfhgmpStackMemberName,
       "hpnicfhgmpStackMemberPassword": hpnicfhgmpStackMemberPassword,
       "hpnicfhgmpStackMemberPlatform": hpnicfhgmpStackMemberPlatform,
       "hpnicfhgmpStackMemberStatus": hpnicfhgmpStackMemberStatus,
       "hpnicfhgmpStackMemberDisconCount": hpnicfhgmpStackMemberDisconCount,
       "hpnicfhgmpStackMemberEnrollTime": hpnicfhgmpStackMemberEnrollTime,
       "hpnicfhgmpStackRole": hpnicfhgmpStackRole,
       "hpnicfhgmpStackMaxPoolNum": hpnicfhgmpStackMaxPoolNum,
       "hpnicfhgmpStackMainSwMac": hpnicfhgmpStackMainSwMac,
       "hpnicfhgmpStackIpPoolMask": hpnicfhgmpStackIpPoolMask,
       "hpnicfNTDPObject": hpnicfNTDPObject,
       "hpnicfhgmpNTDPCollectTopTime": hpnicfhgmpNTDPCollectTopTime,
       "hpnicfhgmpNTDPHopRange": hpnicfhgmpNTDPHopRange,
       "hpnicfhgmpNTDPRun": hpnicfhgmpNTDPRun,
       "hpnicfhgmpNTDPPortDelay": hpnicfhgmpNTDPPortDelay,
       "hpnicfhgmpNTDPHopDelay": hpnicfhgmpNTDPHopDelay,
       "hpnicfhgmpNTDPLastTopCollectDuration": hpnicfhgmpNTDPLastTopCollectDuration,
       "hpnicfhgmpNTDPCacheChange": hpnicfhgmpNTDPCacheChange,
       "hpnicfhgmpNTDPTOPTableChange": hpnicfhgmpNTDPTOPTableChange,
       "hpnicfhgmpNTDPInterfaceTable": hpnicfhgmpNTDPInterfaceTable,
       "hpnicfhgmpNTDPInterfaceEntry": hpnicfhgmpNTDPInterfaceEntry,
       "hpnicfhgmpNTDPInterfaceIfIndex": hpnicfhgmpNTDPInterfaceIfIndex,
       "hpnicfhgmpNTDPInterfaceEnable": hpnicfhgmpNTDPInterfaceEnable,
       "hpnicfhgmpNTDPCacheTable": hpnicfhgmpNTDPCacheTable,
       "hpnicfhgmpNTDPCacheEntry": hpnicfhgmpNTDPCacheEntry,
       "hpnicfhgmpNTDPCacheHashIndex": hpnicfhgmpNTDPCacheHashIndex,
       "hpnicfhgmpNTDPCacheDeviceID": hpnicfhgmpNTDPCacheDeviceID,
       "hpnicfhgmpNTDPCacheClusterName": hpnicfhgmpNTDPCacheClusterName,
       "hpnicfhgmpNTDPCacheClusterRole": hpnicfhgmpNTDPCacheClusterRole,
       "hpnicfhgmpNTDPCacheCapabilities": hpnicfhgmpNTDPCacheCapabilities,
       "hpnicfhgmpNTDPCacheVersion": hpnicfhgmpNTDPCacheVersion,
       "hpnicfhgmpNTDPCachePlatform": hpnicfhgmpNTDPCachePlatform,
       "hpnicfhgmpNTDPCacheMngVLAN": hpnicfhgmpNTDPCacheMngVLAN,
       "hpnicfhgmpNTDPCacheHop": hpnicfhgmpNTDPCacheHop,
       "hpnicfhgmpNTDPTopTable": hpnicfhgmpNTDPTopTable,
       "hpnicfhgmpNTDPTopEntry": hpnicfhgmpNTDPTopEntry,
       "hpnicfhgmpNTDPTopHashIndex": hpnicfhgmpNTDPTopHashIndex,
       "hpnicfhgmpNTDPTopEdgeStartDevID": hpnicfhgmpNTDPTopEdgeStartDevID,
       "hpnicfhgmpNTDPTopEdgeIndex": hpnicfhgmpNTDPTopEdgeIndex,
       "hpnicfhgmpNTDPTopEdgeEndDevID": hpnicfhgmpNTDPTopEdgeEndDevID,
       "hpnicfhgmpNTDPTopEdgeStartPort": hpnicfhgmpNTDPTopEdgeStartPort,
       "hpnicfhgmpNTDPTopEdgeStartPortFullDuplex": hpnicfhgmpNTDPTopEdgeStartPortFullDuplex,
       "hpnicfhgmpNTDPTopEdgeStartPortSpeed": hpnicfhgmpNTDPTopEdgeStartPortSpeed,
       "hpnicfhgmpNTDPTopEdgeEndPort": hpnicfhgmpNTDPTopEdgeEndPort,
       "hpnicfhgmpNTDPTopLinkStatus": hpnicfhgmpNTDPTopLinkStatus,
       "hpnicfNDPObject": hpnicfNDPObject,
       "hpnicfNDPStatus": hpnicfNDPStatus,
       "hpnicfNDPHelloTimer": hpnicfNDPHelloTimer,
       "hpnicfNDPAgingTime": hpnicfNDPAgingTime,
       "hpnicfNDPChange": hpnicfNDPChange,
       "hpnicfNDPPortTable": hpnicfNDPPortTable,
       "hpnicfNDPPortEntry": hpnicfNDPPortEntry,
       "hpnicfNDPIfIndex": hpnicfNDPIfIndex,
       "hpnicfNDPPortStatus": hpnicfNDPPortStatus,
       "hpnicfNDPPortNbTable": hpnicfNDPPortNbTable,
       "hpnicfNDPPortNbEntry": hpnicfNDPPortNbEntry,
       "hpnicfNDPPortNbDeviceId": hpnicfNDPPortNbDeviceId,
       "hpnicfNDPPortNbPortName": hpnicfNDPPortNbPortName,
       "hpnicfNDPPortNbDeviceName": hpnicfNDPPortNbDeviceName,
       "hpnicfNDPPortNbPortMode": hpnicfNDPPortNbPortMode,
       "hpnicfNDPPortNbProductVer": hpnicfNDPPortNbProductVer,
       "hpnicfNDPPortNbHardVer": hpnicfNDPPortNbHardVer,
       "hpnicfNDPPortNbBootromVer": hpnicfNDPPortNbBootromVer,
       "hpnicfNDPPortNbSoftVer": hpnicfNDPPortNbSoftVer,
       "hpnicfNDPPortNbAgingtime": hpnicfNDPPortNbAgingtime}
)
