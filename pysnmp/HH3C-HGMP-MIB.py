# SNMP MIB module (HH3C-HGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-HGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:29 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cHgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cClusterObject_ObjectIdentity = ObjectIdentity
hh3cClusterObject = _Hh3cClusterObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cClusterObject.setStatus("current")
_Hh3chgmpEventsV2_ObjectIdentity = ObjectIdentity
hh3chgmpEventsV2 = _Hh3chgmpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 0)
)
if mibBuilder.loadTexts:
    hh3chgmpEventsV2.setStatus("current")


class _Hh3chgmpSetVLANSecurity_Type(Integer32):
    """Custom type hh3chgmpSetVLANSecurity based on Integer32"""
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


_Hh3chgmpSetVLANSecurity_Type.__name__ = "Integer32"
_Hh3chgmpSetVLANSecurity_Object = MibScalar
hh3chgmpSetVLANSecurity = _Hh3chgmpSetVLANSecurity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 1),
    _Hh3chgmpSetVLANSecurity_Type()
)
hh3chgmpSetVLANSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpSetVLANSecurity.setStatus("current")


class _Hh3chgmpHandShakeInterval_Type(Integer32):
    """Custom type hh3chgmpHandShakeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3chgmpHandShakeInterval_Type.__name__ = "Integer32"
_Hh3chgmpHandShakeInterval_Object = MibScalar
hh3chgmpHandShakeInterval = _Hh3chgmpHandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 2),
    _Hh3chgmpHandShakeInterval_Type()
)
hh3chgmpHandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpHandShakeInterval.setStatus("current")


class _Hh3chgmpHandShakeHoldtime_Type(Integer32):
    """Custom type hh3chgmpHandShakeHoldtime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3chgmpHandShakeHoldtime_Type.__name__ = "Integer32"
_Hh3chgmpHandShakeHoldtime_Object = MibScalar
hh3chgmpHandShakeHoldtime = _Hh3chgmpHandShakeHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 3),
    _Hh3chgmpHandShakeHoldtime_Type()
)
hh3chgmpHandShakeHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpHandShakeHoldtime.setStatus("current")


class _Hh3chgmpGrpMemberTableChange_Type(Integer32):
    """Custom type hh3chgmpGrpMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpGrpMemberTableChange_Type.__name__ = "Integer32"
_Hh3chgmpGrpMemberTableChange_Object = MibScalar
hh3chgmpGrpMemberTableChange = _Hh3chgmpGrpMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 4),
    _Hh3chgmpGrpMemberTableChange_Type()
)
hh3chgmpGrpMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberTableChange.setStatus("current")


class _Hh3chgmpMemberDisconRate_Type(Integer32):
    """Custom type hh3chgmpMemberDisconRate based on Integer32"""
    defaultValue = 0


_Hh3chgmpMemberDisconRate_Object = MibScalar
hh3chgmpMemberDisconRate = _Hh3chgmpMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 5),
    _Hh3chgmpMemberDisconRate_Type()
)
hh3chgmpMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpMemberDisconRate.setStatus("current")


class _Hh3chgmpCmdLanswitchFlag_Type(Integer32):
    """Custom type hh3chgmpCmdLanswitchFlag based on Integer32"""
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


_Hh3chgmpCmdLanswitchFlag_Type.__name__ = "Integer32"
_Hh3chgmpCmdLanswitchFlag_Object = MibScalar
hh3chgmpCmdLanswitchFlag = _Hh3chgmpCmdLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 6),
    _Hh3chgmpCmdLanswitchFlag_Type()
)
hh3chgmpCmdLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpCmdLanswitchFlag.setStatus("current")


class _Hh3chgmpCmdClusterName_Type(OctetString):
    """Custom type hh3chgmpCmdClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Hh3chgmpCmdClusterName_Type.__name__ = "OctetString"
_Hh3chgmpCmdClusterName_Object = MibScalar
hh3chgmpCmdClusterName = _Hh3chgmpCmdClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 7),
    _Hh3chgmpCmdClusterName_Type()
)
hh3chgmpCmdClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpCmdClusterName.setStatus("current")
_Hh3chgmpMngPriIpSegCMIP_Type = IpAddress
_Hh3chgmpMngPriIpSegCMIP_Object = MibScalar
hh3chgmpMngPriIpSegCMIP = _Hh3chgmpMngPriIpSegCMIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 8),
    _Hh3chgmpMngPriIpSegCMIP_Type()
)
hh3chgmpMngPriIpSegCMIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpMngPriIpSegCMIP.setStatus("current")
_Hh3chgmpMngPriIpMask_Type = IpAddress
_Hh3chgmpMngPriIpMask_Object = MibScalar
hh3chgmpMngPriIpMask = _Hh3chgmpMngPriIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 9),
    _Hh3chgmpMngPriIpMask_Type()
)
hh3chgmpMngPriIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpMngPriIpMask.setStatus("current")
_Hh3chgmpFtpServer_Type = IpAddress
_Hh3chgmpFtpServer_Object = MibScalar
hh3chgmpFtpServer = _Hh3chgmpFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 10),
    _Hh3chgmpFtpServer_Type()
)
hh3chgmpFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpFtpServer.setStatus("current")
_Hh3chgmpTftpServer_Type = IpAddress
_Hh3chgmpTftpServer_Object = MibScalar
hh3chgmpTftpServer = _Hh3chgmpTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 11),
    _Hh3chgmpTftpServer_Type()
)
hh3chgmpTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpTftpServer.setStatus("current")
_Hh3chgmpSnmpHost_Type = IpAddress
_Hh3chgmpSnmpHost_Object = MibScalar
hh3chgmpSnmpHost = _Hh3chgmpSnmpHost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 12),
    _Hh3chgmpSnmpHost_Type()
)
hh3chgmpSnmpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpSnmpHost.setStatus("current")
_Hh3chgmpLogHost_Type = IpAddress
_Hh3chgmpLogHost_Object = MibScalar
hh3chgmpLogHost = _Hh3chgmpLogHost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 13),
    _Hh3chgmpLogHost_Type()
)
hh3chgmpLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpLogHost.setStatus("current")
_Hh3chgmpGrpMemberTable_Object = MibTable
hh3chgmpGrpMemberTable = _Hh3chgmpGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14)
)
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberTable.setStatus("current")
_Hh3chgmpGrpMemberEntry_Object = MibTableRow
hh3chgmpGrpMemberEntry = _Hh3chgmpGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1)
)
hh3chgmpGrpMemberEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpGrpMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberEntry.setStatus("current")


class _Hh3chgmpGrpMemberDeviceId_Type(OctetString):
    """Custom type hh3chgmpGrpMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpGrpMemberDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpGrpMemberDeviceId_Object = MibTableColumn
hh3chgmpGrpMemberDeviceId = _Hh3chgmpGrpMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 1),
    _Hh3chgmpGrpMemberDeviceId_Type()
)
hh3chgmpGrpMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberDeviceId.setStatus("current")


class _Hh3chgmpGrpMemberSerial_Type(Integer32):
    """Custom type hh3chgmpGrpMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_Hh3chgmpGrpMemberSerial_Type.__name__ = "Integer32"
_Hh3chgmpGrpMemberSerial_Object = MibTableColumn
hh3chgmpGrpMemberSerial = _Hh3chgmpGrpMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 2),
    _Hh3chgmpGrpMemberSerial_Type()
)
hh3chgmpGrpMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberSerial.setStatus("current")
_Hh3chgmpGrpMemberIpAddr_Type = IpAddress
_Hh3chgmpGrpMemberIpAddr_Object = MibTableColumn
hh3chgmpGrpMemberIpAddr = _Hh3chgmpGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 3),
    _Hh3chgmpGrpMemberIpAddr_Type()
)
hh3chgmpGrpMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberIpAddr.setStatus("current")


class _Hh3chgmpGrpMemberName_Type(OctetString):
    """Custom type hh3chgmpGrpMemberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3chgmpGrpMemberName_Type.__name__ = "OctetString"
_Hh3chgmpGrpMemberName_Object = MibTableColumn
hh3chgmpGrpMemberName = _Hh3chgmpGrpMemberName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 4),
    _Hh3chgmpGrpMemberName_Type()
)
hh3chgmpGrpMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberName.setStatus("current")
_Hh3chgmpGrpMemberPassword_Type = OctetString
_Hh3chgmpGrpMemberPassword_Object = MibTableColumn
hh3chgmpGrpMemberPassword = _Hh3chgmpGrpMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 5),
    _Hh3chgmpGrpMemberPassword_Type()
)
hh3chgmpGrpMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberPassword.setStatus("current")
_Hh3chgmpGrpMemberPlatform_Type = OctetString
_Hh3chgmpGrpMemberPlatform_Object = MibTableColumn
hh3chgmpGrpMemberPlatform = _Hh3chgmpGrpMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 6),
    _Hh3chgmpGrpMemberPlatform_Type()
)
hh3chgmpGrpMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberPlatform.setStatus("current")


class _Hh3chgmpGrpMemberStatus_Type(Integer32):
    """Custom type hh3chgmpGrpMemberStatus based on Integer32"""
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


_Hh3chgmpGrpMemberStatus_Type.__name__ = "Integer32"
_Hh3chgmpGrpMemberStatus_Object = MibTableColumn
hh3chgmpGrpMemberStatus = _Hh3chgmpGrpMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 7),
    _Hh3chgmpGrpMemberStatus_Type()
)
hh3chgmpGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberStatus.setStatus("current")
_Hh3chgmpGrpMemberDisconCount_Type = Integer32
_Hh3chgmpGrpMemberDisconCount_Object = MibTableColumn
hh3chgmpGrpMemberDisconCount = _Hh3chgmpGrpMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 8),
    _Hh3chgmpGrpMemberDisconCount_Type()
)
hh3chgmpGrpMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberDisconCount.setStatus("current")
_Hh3chgmpGrpMemberEnrollTime_Type = Integer32
_Hh3chgmpGrpMemberEnrollTime_Object = MibTableColumn
hh3chgmpGrpMemberEnrollTime = _Hh3chgmpGrpMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 9),
    _Hh3chgmpGrpMemberEnrollTime_Type()
)
hh3chgmpGrpMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberEnrollTime.setStatus("current")
_Hh3chgmpGrpMemberOperate_Type = RowStatus
_Hh3chgmpGrpMemberOperate_Object = MibTableColumn
hh3chgmpGrpMemberOperate = _Hh3chgmpGrpMemberOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 14, 1, 10),
    _Hh3chgmpGrpMemberOperate_Type()
)
hh3chgmpGrpMemberOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpGrpMemberOperate.setStatus("current")
_Hh3chgmpMemberResetTable_Object = MibTable
hh3chgmpMemberResetTable = _Hh3chgmpMemberResetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 15)
)
if mibBuilder.loadTexts:
    hh3chgmpMemberResetTable.setStatus("current")
_Hh3chgmpMemberResetEntry_Object = MibTableRow
hh3chgmpMemberResetEntry = _Hh3chgmpMemberResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 15, 1)
)
hh3chgmpMemberResetEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpMemberResetMAC"),
)
if mibBuilder.loadTexts:
    hh3chgmpMemberResetEntry.setStatus("current")


class _Hh3chgmpMemberResetMAC_Type(OctetString):
    """Custom type hh3chgmpMemberResetMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hh3chgmpMemberResetMAC_Type.__name__ = "OctetString"
_Hh3chgmpMemberResetMAC_Object = MibTableColumn
hh3chgmpMemberResetMAC = _Hh3chgmpMemberResetMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 15, 1, 1),
    _Hh3chgmpMemberResetMAC_Type()
)
hh3chgmpMemberResetMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpMemberResetMAC.setStatus("current")


class _Hh3chgmpMemberEraseflash_Type(Integer32):
    """Custom type hh3chgmpMemberEraseflash based on Integer32"""
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


_Hh3chgmpMemberEraseflash_Type.__name__ = "Integer32"
_Hh3chgmpMemberEraseflash_Object = MibTableColumn
hh3chgmpMemberEraseflash = _Hh3chgmpMemberEraseflash_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 15, 1, 2),
    _Hh3chgmpMemberEraseflash_Type()
)
hh3chgmpMemberEraseflash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpMemberEraseflash.setStatus("current")


class _Hh3chgmpClusterRole_Type(Integer32):
    """Custom type hh3chgmpClusterRole based on Integer32"""
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


_Hh3chgmpClusterRole_Type.__name__ = "Integer32"
_Hh3chgmpClusterRole_Object = MibScalar
hh3chgmpClusterRole = _Hh3chgmpClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 16),
    _Hh3chgmpClusterRole_Type()
)
hh3chgmpClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpClusterRole.setStatus("current")
_Hh3chgmpClusterMaxPoolNum_Type = Integer32
_Hh3chgmpClusterMaxPoolNum_Object = MibScalar
hh3chgmpClusterMaxPoolNum = _Hh3chgmpClusterMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 17),
    _Hh3chgmpClusterMaxPoolNum_Type()
)
hh3chgmpClusterMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpClusterMaxPoolNum.setStatus("current")


class _Hh3chgmpClusterCmdSwMac_Type(OctetString):
    """Custom type hh3chgmpClusterCmdSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hh3chgmpClusterCmdSwMac_Type.__name__ = "OctetString"
_Hh3chgmpClusterCmdSwMac_Object = MibScalar
hh3chgmpClusterCmdSwMac = _Hh3chgmpClusterCmdSwMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 18),
    _Hh3chgmpClusterCmdSwMac_Type()
)
hh3chgmpClusterCmdSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpClusterCmdSwMac.setStatus("current")


class _Hh3chgmpRun_Type(Integer32):
    """Custom type hh3chgmpRun based on Integer32"""
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


_Hh3chgmpRun_Type.__name__ = "Integer32"
_Hh3chgmpRun_Object = MibScalar
hh3chgmpRun = _Hh3chgmpRun_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 19),
    _Hh3chgmpRun_Type()
)
hh3chgmpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpRun.setStatus("current")
_Hh3chgmpProtocolMac_ObjectIdentity = ObjectIdentity
hh3chgmpProtocolMac = _Hh3chgmpProtocolMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 22)
)


class _Hh3chgmpClusterProtocolMac_Type(MacAddress):
    """Custom type hh3chgmpClusterProtocolMac based on MacAddress"""
    defaultHexValue = "0180C200000A"


_Hh3chgmpClusterProtocolMac_Object = MibScalar
hh3chgmpClusterProtocolMac = _Hh3chgmpClusterProtocolMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 22, 1),
    _Hh3chgmpClusterProtocolMac_Type()
)
hh3chgmpClusterProtocolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpClusterProtocolMac.setStatus("current")
_Hh3chgmpTopologyManagement_ObjectIdentity = ObjectIdentity
hh3chgmpTopologyManagement = _Hh3chgmpTopologyManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23)
)
_Hh3chgmpWhitelistTable_Object = MibTable
hh3chgmpWhitelistTable = _Hh3chgmpWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 1)
)
if mibBuilder.loadTexts:
    hh3chgmpWhitelistTable.setStatus("current")
_Hh3chgmpWhitelistEntry_Object = MibTableRow
hh3chgmpWhitelistEntry = _Hh3chgmpWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 1, 1)
)
hh3chgmpWhitelistEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpWhitelistDeviceId"),
)
if mibBuilder.loadTexts:
    hh3chgmpWhitelistEntry.setStatus("current")


class _Hh3chgmpWhitelistDeviceId_Type(OctetString):
    """Custom type hh3chgmpWhitelistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3chgmpWhitelistDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpWhitelistDeviceId_Object = MibTableColumn
hh3chgmpWhitelistDeviceId = _Hh3chgmpWhitelistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 1, 1, 1),
    _Hh3chgmpWhitelistDeviceId_Type()
)
hh3chgmpWhitelistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistDeviceId.setStatus("current")


class _Hh3chgmpWhitelistSerial_Type(Integer32):
    """Custom type hh3chgmpWhitelistSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3chgmpWhitelistSerial_Type.__name__ = "Integer32"
_Hh3chgmpWhitelistSerial_Object = MibTableColumn
hh3chgmpWhitelistSerial = _Hh3chgmpWhitelistSerial_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 1, 1, 2),
    _Hh3chgmpWhitelistSerial_Type()
)
hh3chgmpWhitelistSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistSerial.setStatus("current")
_Hh3chgmpWhitelistRowStatus_Type = RowStatus
_Hh3chgmpWhitelistRowStatus_Object = MibTableColumn
hh3chgmpWhitelistRowStatus = _Hh3chgmpWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 1, 1, 3),
    _Hh3chgmpWhitelistRowStatus_Type()
)
hh3chgmpWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistRowStatus.setStatus("current")
_Hh3chgmpWhitelistNbTable_Object = MibTable
hh3chgmpWhitelistNbTable = _Hh3chgmpWhitelistNbTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2)
)
if mibBuilder.loadTexts:
    hh3chgmpWhitelistNbTable.setStatus("current")
_Hh3chgmpWhitelistNbEntry_Object = MibTableRow
hh3chgmpWhitelistNbEntry = _Hh3chgmpWhitelistNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2, 1)
)
hh3chgmpWhitelistNbEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpWhitelistDeviceId"),
    (0, "HH3C-HGMP-MIB", "hh3chgmpWhitelistNbIndex"),
)
if mibBuilder.loadTexts:
    hh3chgmpWhitelistNbEntry.setStatus("current")


class _Hh3chgmpWhitelistNbIndex_Type(Integer32):
    """Custom type hh3chgmpWhitelistNbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3chgmpWhitelistNbIndex_Type.__name__ = "Integer32"
_Hh3chgmpWhitelistNbIndex_Object = MibTableColumn
hh3chgmpWhitelistNbIndex = _Hh3chgmpWhitelistNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2, 1, 1),
    _Hh3chgmpWhitelistNbIndex_Type()
)
hh3chgmpWhitelistNbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistNbIndex.setStatus("current")


class _Hh3chgmpWhitelistNbDeviceId_Type(OctetString):
    """Custom type hh3chgmpWhitelistNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3chgmpWhitelistNbDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpWhitelistNbDeviceId_Object = MibTableColumn
hh3chgmpWhitelistNbDeviceId = _Hh3chgmpWhitelistNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2, 1, 2),
    _Hh3chgmpWhitelistNbDeviceId_Type()
)
hh3chgmpWhitelistNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistNbDeviceId.setStatus("current")


class _Hh3chgmpWhitelistPortName_Type(OctetString):
    """Custom type hh3chgmpWhitelistPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3chgmpWhitelistPortName_Type.__name__ = "OctetString"
_Hh3chgmpWhitelistPortName_Object = MibTableColumn
hh3chgmpWhitelistPortName = _Hh3chgmpWhitelistPortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2, 1, 3),
    _Hh3chgmpWhitelistPortName_Type()
)
hh3chgmpWhitelistPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistPortName.setStatus("current")


class _Hh3chgmpWhitelistNbPortName_Type(OctetString):
    """Custom type hh3chgmpWhitelistNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3chgmpWhitelistNbPortName_Type.__name__ = "OctetString"
_Hh3chgmpWhitelistNbPortName_Object = MibTableColumn
hh3chgmpWhitelistNbPortName = _Hh3chgmpWhitelistNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 2, 1, 4),
    _Hh3chgmpWhitelistNbPortName_Type()
)
hh3chgmpWhitelistNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpWhitelistNbPortName.setStatus("current")
_Hh3chgmpBlacklistTable_Object = MibTable
hh3chgmpBlacklistTable = _Hh3chgmpBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3)
)
if mibBuilder.loadTexts:
    hh3chgmpBlacklistTable.setStatus("current")
_Hh3chgmpBlacklistEntry_Object = MibTableRow
hh3chgmpBlacklistEntry = _Hh3chgmpBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3, 1)
)
hh3chgmpBlacklistEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpBlacklistDeviceId"),
)
if mibBuilder.loadTexts:
    hh3chgmpBlacklistEntry.setStatus("current")


class _Hh3chgmpBlacklistDeviceId_Type(OctetString):
    """Custom type hh3chgmpBlacklistDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3chgmpBlacklistDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpBlacklistDeviceId_Object = MibTableColumn
hh3chgmpBlacklistDeviceId = _Hh3chgmpBlacklistDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3, 1, 1),
    _Hh3chgmpBlacklistDeviceId_Type()
)
hh3chgmpBlacklistDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3chgmpBlacklistDeviceId.setStatus("current")


class _Hh3chgmpBlacklistAccessDeviceId_Type(OctetString):
    """Custom type hh3chgmpBlacklistAccessDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3chgmpBlacklistAccessDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpBlacklistAccessDeviceId_Object = MibTableColumn
hh3chgmpBlacklistAccessDeviceId = _Hh3chgmpBlacklistAccessDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3, 1, 2),
    _Hh3chgmpBlacklistAccessDeviceId_Type()
)
hh3chgmpBlacklistAccessDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpBlacklistAccessDeviceId.setStatus("current")


class _Hh3chgmpBlacklistAccessPortName_Type(OctetString):
    """Custom type hh3chgmpBlacklistAccessPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3chgmpBlacklistAccessPortName_Type.__name__ = "OctetString"
_Hh3chgmpBlacklistAccessPortName_Object = MibTableColumn
hh3chgmpBlacklistAccessPortName = _Hh3chgmpBlacklistAccessPortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3, 1, 3),
    _Hh3chgmpBlacklistAccessPortName_Type()
)
hh3chgmpBlacklistAccessPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpBlacklistAccessPortName.setStatus("current")
_Hh3chgmpBlacklistRowStatus_Type = RowStatus
_Hh3chgmpBlacklistRowStatus_Object = MibTableColumn
hh3chgmpBlacklistRowStatus = _Hh3chgmpBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 23, 3, 1, 4),
    _Hh3chgmpBlacklistRowStatus_Type()
)
hh3chgmpBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3chgmpBlacklistRowStatus.setStatus("current")
_Hh3chgmpMemberPriPortTable_Object = MibTable
hh3chgmpMemberPriPortTable = _Hh3chgmpMemberPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24)
)
if mibBuilder.loadTexts:
    hh3chgmpMemberPriPortTable.setStatus("current")
_Hh3chgmpMemberPriPortEntry_Object = MibTableRow
hh3chgmpMemberPriPortEntry = _Hh3chgmpMemberPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24, 1)
)
hh3chgmpMemberPriPortEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpMemberDevId"),
    (0, "HH3C-HGMP-MIB", "hh3chgmpMemberPriPortProto"),
)
if mibBuilder.loadTexts:
    hh3chgmpMemberPriPortEntry.setStatus("current")


class _Hh3chgmpMemberDevId_Type(OctetString):
    """Custom type hh3chgmpMemberDevId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpMemberDevId_Type.__name__ = "OctetString"
_Hh3chgmpMemberDevId_Object = MibTableColumn
hh3chgmpMemberDevId = _Hh3chgmpMemberDevId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24, 1, 1),
    _Hh3chgmpMemberDevId_Type()
)
hh3chgmpMemberDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpMemberDevId.setStatus("current")
_Hh3chgmpMemberPriPortProto_Type = Unsigned32
_Hh3chgmpMemberPriPortProto_Object = MibTableColumn
hh3chgmpMemberPriPortProto = _Hh3chgmpMemberPriPortProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24, 1, 2),
    _Hh3chgmpMemberPriPortProto_Type()
)
hh3chgmpMemberPriPortProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3chgmpMemberPriPortProto.setStatus("current")
_Hh3chgmpMemberPriPortProtoDescr_Type = DisplayString
_Hh3chgmpMemberPriPortProtoDescr_Object = MibTableColumn
hh3chgmpMemberPriPortProtoDescr = _Hh3chgmpMemberPriPortProtoDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24, 1, 3),
    _Hh3chgmpMemberPriPortProtoDescr_Type()
)
hh3chgmpMemberPriPortProtoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpMemberPriPortProtoDescr.setStatus("current")
_Hh3chgmpMemberPriPortNum_Type = Unsigned32
_Hh3chgmpMemberPriPortNum_Object = MibTableColumn
hh3chgmpMemberPriPortNum = _Hh3chgmpMemberPriPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 24, 1, 4),
    _Hh3chgmpMemberPriPortNum_Type()
)
hh3chgmpMemberPriPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpMemberPriPortNum.setStatus("current")
_Hh3cStackObject_ObjectIdentity = ObjectIdentity
hh3cStackObject = _Hh3cStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hh3cStackObject.setStatus("current")
_Hh3chgmpStackEventsV2_ObjectIdentity = ObjectIdentity
hh3chgmpStackEventsV2 = _Hh3chgmpStackEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 0)
)
if mibBuilder.loadTexts:
    hh3chgmpStackEventsV2.setStatus("current")


class _Hh3chgmpStackMemberTableChange_Type(Integer32):
    """Custom type hh3chgmpStackMemberTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpStackMemberTableChange_Type.__name__ = "Integer32"
_Hh3chgmpStackMemberTableChange_Object = MibScalar
hh3chgmpStackMemberTableChange = _Hh3chgmpStackMemberTableChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 1),
    _Hh3chgmpStackMemberTableChange_Type()
)
hh3chgmpStackMemberTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberTableChange.setStatus("current")


class _Hh3chgmpStackMemberDisconRate_Type(Integer32):
    """Custom type hh3chgmpStackMemberDisconRate based on Integer32"""
    defaultValue = 0


_Hh3chgmpStackMemberDisconRate_Object = MibScalar
hh3chgmpStackMemberDisconRate = _Hh3chgmpStackMemberDisconRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 2),
    _Hh3chgmpStackMemberDisconRate_Type()
)
hh3chgmpStackMemberDisconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberDisconRate.setStatus("current")


class _Hh3chgmpMainLanswitchFlag_Type(Integer32):
    """Custom type hh3chgmpMainLanswitchFlag based on Integer32"""
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


_Hh3chgmpMainLanswitchFlag_Type.__name__ = "Integer32"
_Hh3chgmpMainLanswitchFlag_Object = MibScalar
hh3chgmpMainLanswitchFlag = _Hh3chgmpMainLanswitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 3),
    _Hh3chgmpMainLanswitchFlag_Type()
)
hh3chgmpMainLanswitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpMainLanswitchFlag.setStatus("current")
_Hh3chgmpStackIpPoolStartIP_Type = IpAddress
_Hh3chgmpStackIpPoolStartIP_Object = MibScalar
hh3chgmpStackIpPoolStartIP = _Hh3chgmpStackIpPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 4),
    _Hh3chgmpStackIpPoolStartIP_Type()
)
hh3chgmpStackIpPoolStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpStackIpPoolStartIP.setStatus("current")


class _Hh3chgmpStackIpPoolLength_Type(Integer32):
    """Custom type hh3chgmpStackIpPoolLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Hh3chgmpStackIpPoolLength_Type.__name__ = "Integer32"
_Hh3chgmpStackIpPoolLength_Object = MibScalar
hh3chgmpStackIpPoolLength = _Hh3chgmpStackIpPoolLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 5),
    _Hh3chgmpStackIpPoolLength_Type()
)
hh3chgmpStackIpPoolLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpStackIpPoolLength.setStatus("current")
_Hh3chgmpStackMemberTable_Object = MibTable
hh3chgmpStackMemberTable = _Hh3chgmpStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hh3chgmpStackMemberTable.setStatus("current")
_Hh3chgmpStackMemberEntry_Object = MibTableRow
hh3chgmpStackMemberEntry = _Hh3chgmpStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1)
)
hh3chgmpStackMemberEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpStackMemberDeviceId"),
)
if mibBuilder.loadTexts:
    hh3chgmpStackMemberEntry.setStatus("current")


class _Hh3chgmpStackMemberDeviceId_Type(OctetString):
    """Custom type hh3chgmpStackMemberDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpStackMemberDeviceId_Type.__name__ = "OctetString"
_Hh3chgmpStackMemberDeviceId_Object = MibTableColumn
hh3chgmpStackMemberDeviceId = _Hh3chgmpStackMemberDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 1),
    _Hh3chgmpStackMemberDeviceId_Type()
)
hh3chgmpStackMemberDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberDeviceId.setStatus("current")


class _Hh3chgmpStackMemberSerial_Type(Integer32):
    """Custom type hh3chgmpStackMemberSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_Hh3chgmpStackMemberSerial_Type.__name__ = "Integer32"
_Hh3chgmpStackMemberSerial_Object = MibTableColumn
hh3chgmpStackMemberSerial = _Hh3chgmpStackMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 2),
    _Hh3chgmpStackMemberSerial_Type()
)
hh3chgmpStackMemberSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberSerial.setStatus("current")
_Hh3chgmpStackMemberIpAddr_Type = IpAddress
_Hh3chgmpStackMemberIpAddr_Object = MibTableColumn
hh3chgmpStackMemberIpAddr = _Hh3chgmpStackMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 3),
    _Hh3chgmpStackMemberIpAddr_Type()
)
hh3chgmpStackMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberIpAddr.setStatus("current")
_Hh3chgmpStackMemberName_Type = OctetString
_Hh3chgmpStackMemberName_Object = MibTableColumn
hh3chgmpStackMemberName = _Hh3chgmpStackMemberName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 4),
    _Hh3chgmpStackMemberName_Type()
)
hh3chgmpStackMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberName.setStatus("current")
_Hh3chgmpStackMemberPassword_Type = OctetString
_Hh3chgmpStackMemberPassword_Object = MibTableColumn
hh3chgmpStackMemberPassword = _Hh3chgmpStackMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 5),
    _Hh3chgmpStackMemberPassword_Type()
)
hh3chgmpStackMemberPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberPassword.setStatus("current")
_Hh3chgmpStackMemberPlatform_Type = OctetString
_Hh3chgmpStackMemberPlatform_Object = MibTableColumn
hh3chgmpStackMemberPlatform = _Hh3chgmpStackMemberPlatform_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 6),
    _Hh3chgmpStackMemberPlatform_Type()
)
hh3chgmpStackMemberPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberPlatform.setStatus("current")


class _Hh3chgmpStackMemberStatus_Type(Integer32):
    """Custom type hh3chgmpStackMemberStatus based on Integer32"""
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


_Hh3chgmpStackMemberStatus_Type.__name__ = "Integer32"
_Hh3chgmpStackMemberStatus_Object = MibTableColumn
hh3chgmpStackMemberStatus = _Hh3chgmpStackMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 7),
    _Hh3chgmpStackMemberStatus_Type()
)
hh3chgmpStackMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberStatus.setStatus("current")
_Hh3chgmpStackMemberDisconCount_Type = Integer32
_Hh3chgmpStackMemberDisconCount_Object = MibTableColumn
hh3chgmpStackMemberDisconCount = _Hh3chgmpStackMemberDisconCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 8),
    _Hh3chgmpStackMemberDisconCount_Type()
)
hh3chgmpStackMemberDisconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberDisconCount.setStatus("current")
_Hh3chgmpStackMemberEnrollTime_Type = Integer32
_Hh3chgmpStackMemberEnrollTime_Object = MibTableColumn
hh3chgmpStackMemberEnrollTime = _Hh3chgmpStackMemberEnrollTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 6, 1, 9),
    _Hh3chgmpStackMemberEnrollTime_Type()
)
hh3chgmpStackMemberEnrollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMemberEnrollTime.setStatus("current")


class _Hh3chgmpStackRole_Type(Integer32):
    """Custom type hh3chgmpStackRole based on Integer32"""
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


_Hh3chgmpStackRole_Type.__name__ = "Integer32"
_Hh3chgmpStackRole_Object = MibScalar
hh3chgmpStackRole = _Hh3chgmpStackRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 7),
    _Hh3chgmpStackRole_Type()
)
hh3chgmpStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackRole.setStatus("current")
_Hh3chgmpStackMaxPoolNum_Type = Integer32
_Hh3chgmpStackMaxPoolNum_Object = MibScalar
hh3chgmpStackMaxPoolNum = _Hh3chgmpStackMaxPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 8),
    _Hh3chgmpStackMaxPoolNum_Type()
)
hh3chgmpStackMaxPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMaxPoolNum.setStatus("current")


class _Hh3chgmpStackMainSwMac_Type(OctetString):
    """Custom type hh3chgmpStackMainSwMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hh3chgmpStackMainSwMac_Type.__name__ = "OctetString"
_Hh3chgmpStackMainSwMac_Object = MibScalar
hh3chgmpStackMainSwMac = _Hh3chgmpStackMainSwMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 9),
    _Hh3chgmpStackMainSwMac_Type()
)
hh3chgmpStackMainSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpStackMainSwMac.setStatus("current")


class _Hh3chgmpStackIpPoolMask_Type(IpAddress):
    """Custom type hh3chgmpStackIpPoolMask based on IpAddress"""
    defaultHexValue = "FFFF0000"


_Hh3chgmpStackIpPoolMask_Object = MibScalar
hh3chgmpStackIpPoolMask = _Hh3chgmpStackIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 10),
    _Hh3chgmpStackIpPoolMask_Type()
)
hh3chgmpStackIpPoolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpStackIpPoolMask.setStatus("current")
_Hh3cNTDPObject_ObjectIdentity = ObjectIdentity
hh3cNTDPObject = _Hh3cNTDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4)
)
if mibBuilder.loadTexts:
    hh3cNTDPObject.setStatus("current")


class _Hh3chgmpNTDPCollectTopTime_Type(Integer32):
    """Custom type hh3chgmpNTDPCollectTopTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpNTDPCollectTopTime_Type.__name__ = "Integer32"
_Hh3chgmpNTDPCollectTopTime_Object = MibScalar
hh3chgmpNTDPCollectTopTime = _Hh3chgmpNTDPCollectTopTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 1),
    _Hh3chgmpNTDPCollectTopTime_Type()
)
hh3chgmpNTDPCollectTopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCollectTopTime.setStatus("current")


class _Hh3chgmpNTDPHopRange_Type(Integer32):
    """Custom type hh3chgmpNTDPHopRange based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3chgmpNTDPHopRange_Type.__name__ = "Integer32"
_Hh3chgmpNTDPHopRange_Object = MibScalar
hh3chgmpNTDPHopRange = _Hh3chgmpNTDPHopRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 2),
    _Hh3chgmpNTDPHopRange_Type()
)
hh3chgmpNTDPHopRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPHopRange.setStatus("current")


class _Hh3chgmpNTDPRun_Type(Integer32):
    """Custom type hh3chgmpNTDPRun based on Integer32"""
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


_Hh3chgmpNTDPRun_Type.__name__ = "Integer32"
_Hh3chgmpNTDPRun_Object = MibScalar
hh3chgmpNTDPRun = _Hh3chgmpNTDPRun_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 3),
    _Hh3chgmpNTDPRun_Type()
)
hh3chgmpNTDPRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPRun.setStatus("current")


class _Hh3chgmpNTDPPortDelay_Type(Integer32):
    """Custom type hh3chgmpNTDPPortDelay based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3chgmpNTDPPortDelay_Type.__name__ = "Integer32"
_Hh3chgmpNTDPPortDelay_Object = MibScalar
hh3chgmpNTDPPortDelay = _Hh3chgmpNTDPPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 4),
    _Hh3chgmpNTDPPortDelay_Type()
)
hh3chgmpNTDPPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPPortDelay.setStatus("current")


class _Hh3chgmpNTDPHopDelay_Type(Integer32):
    """Custom type hh3chgmpNTDPHopDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Hh3chgmpNTDPHopDelay_Type.__name__ = "Integer32"
_Hh3chgmpNTDPHopDelay_Object = MibScalar
hh3chgmpNTDPHopDelay = _Hh3chgmpNTDPHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 5),
    _Hh3chgmpNTDPHopDelay_Type()
)
hh3chgmpNTDPHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPHopDelay.setStatus("current")


class _Hh3chgmpNTDPLastTopCollectDuration_Type(Integer32):
    """Custom type hh3chgmpNTDPLastTopCollectDuration based on Integer32"""
    defaultValue = 0


_Hh3chgmpNTDPLastTopCollectDuration_Object = MibScalar
hh3chgmpNTDPLastTopCollectDuration = _Hh3chgmpNTDPLastTopCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 6),
    _Hh3chgmpNTDPLastTopCollectDuration_Type()
)
hh3chgmpNTDPLastTopCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPLastTopCollectDuration.setStatus("current")


class _Hh3chgmpNTDPCacheChange_Type(Integer32):
    """Custom type hh3chgmpNTDPCacheChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpNTDPCacheChange_Type.__name__ = "Integer32"
_Hh3chgmpNTDPCacheChange_Object = MibScalar
hh3chgmpNTDPCacheChange = _Hh3chgmpNTDPCacheChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 7),
    _Hh3chgmpNTDPCacheChange_Type()
)
hh3chgmpNTDPCacheChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheChange.setStatus("current")


class _Hh3chgmpNTDPTOPTableChange_Type(Integer32):
    """Custom type hh3chgmpNTDPTOPTableChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpNTDPTOPTableChange_Type.__name__ = "Integer32"
_Hh3chgmpNTDPTOPTableChange_Object = MibScalar
hh3chgmpNTDPTOPTableChange = _Hh3chgmpNTDPTOPTableChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 8),
    _Hh3chgmpNTDPTOPTableChange_Type()
)
hh3chgmpNTDPTOPTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTOPTableChange.setStatus("current")
_Hh3chgmpNTDPInterfaceTable_Object = MibTable
hh3chgmpNTDPInterfaceTable = _Hh3chgmpNTDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 9)
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPInterfaceTable.setStatus("current")
_Hh3chgmpNTDPInterfaceEntry_Object = MibTableRow
hh3chgmpNTDPInterfaceEntry = _Hh3chgmpNTDPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 9, 1)
)
hh3chgmpNTDPInterfaceEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPInterfaceEntry.setStatus("current")
_Hh3chgmpNTDPInterfaceIfIndex_Type = Integer32
_Hh3chgmpNTDPInterfaceIfIndex_Object = MibTableColumn
hh3chgmpNTDPInterfaceIfIndex = _Hh3chgmpNTDPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 9, 1, 1),
    _Hh3chgmpNTDPInterfaceIfIndex_Type()
)
hh3chgmpNTDPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPInterfaceIfIndex.setStatus("current")


class _Hh3chgmpNTDPInterfaceEnable_Type(Integer32):
    """Custom type hh3chgmpNTDPInterfaceEnable based on Integer32"""
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


_Hh3chgmpNTDPInterfaceEnable_Type.__name__ = "Integer32"
_Hh3chgmpNTDPInterfaceEnable_Object = MibTableColumn
hh3chgmpNTDPInterfaceEnable = _Hh3chgmpNTDPInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 9, 1, 2),
    _Hh3chgmpNTDPInterfaceEnable_Type()
)
hh3chgmpNTDPInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chgmpNTDPInterfaceEnable.setStatus("current")
_Hh3chgmpNTDPCacheTable_Object = MibTable
hh3chgmpNTDPCacheTable = _Hh3chgmpNTDPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10)
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheTable.setStatus("current")
_Hh3chgmpNTDPCacheEntry_Object = MibTableRow
hh3chgmpNTDPCacheEntry = _Hh3chgmpNTDPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1)
)
hh3chgmpNTDPCacheEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPCacheHashIndex"),
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPCacheDeviceID"),
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheEntry.setStatus("current")


class _Hh3chgmpNTDPCacheHashIndex_Type(Integer32):
    """Custom type hh3chgmpNTDPCacheHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3chgmpNTDPCacheHashIndex_Type.__name__ = "Integer32"
_Hh3chgmpNTDPCacheHashIndex_Object = MibTableColumn
hh3chgmpNTDPCacheHashIndex = _Hh3chgmpNTDPCacheHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 1),
    _Hh3chgmpNTDPCacheHashIndex_Type()
)
hh3chgmpNTDPCacheHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheHashIndex.setStatus("current")


class _Hh3chgmpNTDPCacheDeviceID_Type(OctetString):
    """Custom type hh3chgmpNTDPCacheDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpNTDPCacheDeviceID_Type.__name__ = "OctetString"
_Hh3chgmpNTDPCacheDeviceID_Object = MibTableColumn
hh3chgmpNTDPCacheDeviceID = _Hh3chgmpNTDPCacheDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 2),
    _Hh3chgmpNTDPCacheDeviceID_Type()
)
hh3chgmpNTDPCacheDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheDeviceID.setStatus("current")
_Hh3chgmpNTDPCacheClusterName_Type = OctetString
_Hh3chgmpNTDPCacheClusterName_Object = MibTableColumn
hh3chgmpNTDPCacheClusterName = _Hh3chgmpNTDPCacheClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 3),
    _Hh3chgmpNTDPCacheClusterName_Type()
)
hh3chgmpNTDPCacheClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheClusterName.setStatus("current")


class _Hh3chgmpNTDPCacheClusterRole_Type(Integer32):
    """Custom type hh3chgmpNTDPCacheClusterRole based on Integer32"""
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


_Hh3chgmpNTDPCacheClusterRole_Type.__name__ = "Integer32"
_Hh3chgmpNTDPCacheClusterRole_Object = MibTableColumn
hh3chgmpNTDPCacheClusterRole = _Hh3chgmpNTDPCacheClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 4),
    _Hh3chgmpNTDPCacheClusterRole_Type()
)
hh3chgmpNTDPCacheClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheClusterRole.setStatus("current")


class _Hh3chgmpNTDPCacheCapabilities_Type(Integer32):
    """Custom type hh3chgmpNTDPCacheCapabilities based on Integer32"""
    defaultValue = 255


_Hh3chgmpNTDPCacheCapabilities_Object = MibTableColumn
hh3chgmpNTDPCacheCapabilities = _Hh3chgmpNTDPCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 5),
    _Hh3chgmpNTDPCacheCapabilities_Type()
)
hh3chgmpNTDPCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheCapabilities.setStatus("current")
_Hh3chgmpNTDPCacheVersion_Type = OctetString
_Hh3chgmpNTDPCacheVersion_Object = MibTableColumn
hh3chgmpNTDPCacheVersion = _Hh3chgmpNTDPCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 6),
    _Hh3chgmpNTDPCacheVersion_Type()
)
hh3chgmpNTDPCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheVersion.setStatus("current")
_Hh3chgmpNTDPCachePlatform_Type = OctetString
_Hh3chgmpNTDPCachePlatform_Object = MibTableColumn
hh3chgmpNTDPCachePlatform = _Hh3chgmpNTDPCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 7),
    _Hh3chgmpNTDPCachePlatform_Type()
)
hh3chgmpNTDPCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCachePlatform.setStatus("current")


class _Hh3chgmpNTDPCacheMngVLAN_Type(Integer32):
    """Custom type hh3chgmpNTDPCacheMngVLAN based on Integer32"""
    defaultValue = 1


_Hh3chgmpNTDPCacheMngVLAN_Object = MibTableColumn
hh3chgmpNTDPCacheMngVLAN = _Hh3chgmpNTDPCacheMngVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 8),
    _Hh3chgmpNTDPCacheMngVLAN_Type()
)
hh3chgmpNTDPCacheMngVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheMngVLAN.setStatus("current")
_Hh3chgmpNTDPCacheHop_Type = Integer32
_Hh3chgmpNTDPCacheHop_Object = MibTableColumn
hh3chgmpNTDPCacheHop = _Hh3chgmpNTDPCacheHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 10, 1, 9),
    _Hh3chgmpNTDPCacheHop_Type()
)
hh3chgmpNTDPCacheHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPCacheHop.setStatus("current")
_Hh3chgmpNTDPTopTable_Object = MibTable
hh3chgmpNTDPTopTable = _Hh3chgmpNTDPTopTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11)
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopTable.setStatus("current")
_Hh3chgmpNTDPTopEntry_Object = MibTableRow
hh3chgmpNTDPTopEntry = _Hh3chgmpNTDPTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1)
)
hh3chgmpNTDPTopEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPTopHashIndex"),
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPTopEdgeStartDevID"),
    (0, "HH3C-HGMP-MIB", "hh3chgmpNTDPTopEdgeIndex"),
)
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEntry.setStatus("current")


class _Hh3chgmpNTDPTopHashIndex_Type(Integer32):
    """Custom type hh3chgmpNTDPTopHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3chgmpNTDPTopHashIndex_Type.__name__ = "Integer32"
_Hh3chgmpNTDPTopHashIndex_Object = MibTableColumn
hh3chgmpNTDPTopHashIndex = _Hh3chgmpNTDPTopHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 1),
    _Hh3chgmpNTDPTopHashIndex_Type()
)
hh3chgmpNTDPTopHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopHashIndex.setStatus("current")


class _Hh3chgmpNTDPTopEdgeStartDevID_Type(OctetString):
    """Custom type hh3chgmpNTDPTopEdgeStartDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpNTDPTopEdgeStartDevID_Type.__name__ = "OctetString"
_Hh3chgmpNTDPTopEdgeStartDevID_Object = MibTableColumn
hh3chgmpNTDPTopEdgeStartDevID = _Hh3chgmpNTDPTopEdgeStartDevID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 2),
    _Hh3chgmpNTDPTopEdgeStartDevID_Type()
)
hh3chgmpNTDPTopEdgeStartDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeStartDevID.setStatus("current")


class _Hh3chgmpNTDPTopEdgeIndex_Type(Integer32):
    """Custom type hh3chgmpNTDPTopEdgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chgmpNTDPTopEdgeIndex_Type.__name__ = "Integer32"
_Hh3chgmpNTDPTopEdgeIndex_Object = MibTableColumn
hh3chgmpNTDPTopEdgeIndex = _Hh3chgmpNTDPTopEdgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 3),
    _Hh3chgmpNTDPTopEdgeIndex_Type()
)
hh3chgmpNTDPTopEdgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeIndex.setStatus("current")


class _Hh3chgmpNTDPTopEdgeEndDevID_Type(OctetString):
    """Custom type hh3chgmpNTDPTopEdgeEndDevID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3chgmpNTDPTopEdgeEndDevID_Type.__name__ = "OctetString"
_Hh3chgmpNTDPTopEdgeEndDevID_Object = MibTableColumn
hh3chgmpNTDPTopEdgeEndDevID = _Hh3chgmpNTDPTopEdgeEndDevID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 4),
    _Hh3chgmpNTDPTopEdgeEndDevID_Type()
)
hh3chgmpNTDPTopEdgeEndDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeEndDevID.setStatus("current")


class _Hh3chgmpNTDPTopEdgeStartPort_Type(OctetString):
    """Custom type hh3chgmpNTDPTopEdgeStartPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3chgmpNTDPTopEdgeStartPort_Type.__name__ = "OctetString"
_Hh3chgmpNTDPTopEdgeStartPort_Object = MibTableColumn
hh3chgmpNTDPTopEdgeStartPort = _Hh3chgmpNTDPTopEdgeStartPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 5),
    _Hh3chgmpNTDPTopEdgeStartPort_Type()
)
hh3chgmpNTDPTopEdgeStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeStartPort.setStatus("current")


class _Hh3chgmpNTDPTopEdgeStartPortFullDuplex_Type(Integer32):
    """Custom type hh3chgmpNTDPTopEdgeStartPortFullDuplex based on Integer32"""
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


_Hh3chgmpNTDPTopEdgeStartPortFullDuplex_Type.__name__ = "Integer32"
_Hh3chgmpNTDPTopEdgeStartPortFullDuplex_Object = MibTableColumn
hh3chgmpNTDPTopEdgeStartPortFullDuplex = _Hh3chgmpNTDPTopEdgeStartPortFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 6),
    _Hh3chgmpNTDPTopEdgeStartPortFullDuplex_Type()
)
hh3chgmpNTDPTopEdgeStartPortFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeStartPortFullDuplex.setStatus("current")


class _Hh3chgmpNTDPTopEdgeStartPortSpeed_Type(Integer32):
    """Custom type hh3chgmpNTDPTopEdgeStartPortSpeed based on Integer32"""
    defaultValue = 0


_Hh3chgmpNTDPTopEdgeStartPortSpeed_Object = MibTableColumn
hh3chgmpNTDPTopEdgeStartPortSpeed = _Hh3chgmpNTDPTopEdgeStartPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 7),
    _Hh3chgmpNTDPTopEdgeStartPortSpeed_Type()
)
hh3chgmpNTDPTopEdgeStartPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeStartPortSpeed.setStatus("current")


class _Hh3chgmpNTDPTopEdgeEndPort_Type(OctetString):
    """Custom type hh3chgmpNTDPTopEdgeEndPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3chgmpNTDPTopEdgeEndPort_Type.__name__ = "OctetString"
_Hh3chgmpNTDPTopEdgeEndPort_Object = MibTableColumn
hh3chgmpNTDPTopEdgeEndPort = _Hh3chgmpNTDPTopEdgeEndPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 8),
    _Hh3chgmpNTDPTopEdgeEndPort_Type()
)
hh3chgmpNTDPTopEdgeEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopEdgeEndPort.setStatus("current")


class _Hh3chgmpNTDPTopLinkStatus_Type(Integer32):
    """Custom type hh3chgmpNTDPTopLinkStatus based on Integer32"""
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


_Hh3chgmpNTDPTopLinkStatus_Type.__name__ = "Integer32"
_Hh3chgmpNTDPTopLinkStatus_Object = MibTableColumn
hh3chgmpNTDPTopLinkStatus = _Hh3chgmpNTDPTopLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 4, 11, 1, 11),
    _Hh3chgmpNTDPTopLinkStatus_Type()
)
hh3chgmpNTDPTopLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chgmpNTDPTopLinkStatus.setStatus("current")
_Hh3cNDPObject_ObjectIdentity = ObjectIdentity
hh3cNDPObject = _Hh3cNDPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5)
)
if mibBuilder.loadTexts:
    hh3cNDPObject.setStatus("current")


class _Hh3cNDPStatus_Type(Integer32):
    """Custom type hh3cNDPStatus based on Integer32"""
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


_Hh3cNDPStatus_Type.__name__ = "Integer32"
_Hh3cNDPStatus_Object = MibScalar
hh3cNDPStatus = _Hh3cNDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 1),
    _Hh3cNDPStatus_Type()
)
hh3cNDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNDPStatus.setStatus("current")


class _Hh3cNDPHelloTimer_Type(Integer32):
    """Custom type hh3cNDPHelloTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_Hh3cNDPHelloTimer_Type.__name__ = "Integer32"
_Hh3cNDPHelloTimer_Object = MibScalar
hh3cNDPHelloTimer = _Hh3cNDPHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 2),
    _Hh3cNDPHelloTimer_Type()
)
hh3cNDPHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNDPHelloTimer.setStatus("current")


class _Hh3cNDPAgingTime_Type(Integer32):
    """Custom type hh3cNDPAgingTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Hh3cNDPAgingTime_Type.__name__ = "Integer32"
_Hh3cNDPAgingTime_Object = MibScalar
hh3cNDPAgingTime = _Hh3cNDPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 3),
    _Hh3cNDPAgingTime_Type()
)
hh3cNDPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNDPAgingTime.setStatus("current")


class _Hh3cNDPChange_Type(Counter32):
    """Custom type hh3cNDPChange based on Counter32"""
    defaultValue = 0


_Hh3cNDPChange_Object = MibScalar
hh3cNDPChange = _Hh3cNDPChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 4),
    _Hh3cNDPChange_Type()
)
hh3cNDPChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPChange.setStatus("current")
_Hh3cNDPPortTable_Object = MibTable
hh3cNDPPortTable = _Hh3cNDPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 5)
)
if mibBuilder.loadTexts:
    hh3cNDPPortTable.setStatus("current")
_Hh3cNDPPortEntry_Object = MibTableRow
hh3cNDPPortEntry = _Hh3cNDPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 5, 1)
)
hh3cNDPPortEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3cNDPIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cNDPPortEntry.setStatus("current")
_Hh3cNDPIfIndex_Type = Integer32
_Hh3cNDPIfIndex_Object = MibTableColumn
hh3cNDPIfIndex = _Hh3cNDPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 5, 1, 1),
    _Hh3cNDPIfIndex_Type()
)
hh3cNDPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPIfIndex.setStatus("current")


class _Hh3cNDPPortStatus_Type(Integer32):
    """Custom type hh3cNDPPortStatus based on Integer32"""
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


_Hh3cNDPPortStatus_Type.__name__ = "Integer32"
_Hh3cNDPPortStatus_Object = MibTableColumn
hh3cNDPPortStatus = _Hh3cNDPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 5, 1, 2),
    _Hh3cNDPPortStatus_Type()
)
hh3cNDPPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNDPPortStatus.setStatus("current")
_Hh3cNDPPortNbTable_Object = MibTable
hh3cNDPPortNbTable = _Hh3cNDPPortNbTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6)
)
if mibBuilder.loadTexts:
    hh3cNDPPortNbTable.setStatus("current")
_Hh3cNDPPortNbEntry_Object = MibTableRow
hh3cNDPPortNbEntry = _Hh3cNDPPortNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1)
)
hh3cNDPPortNbEntry.setIndexNames(
    (0, "HH3C-HGMP-MIB", "hh3cNDPIfIndex"),
    (0, "HH3C-HGMP-MIB", "hh3cNDPPortNbDeviceId"),
    (0, "HH3C-HGMP-MIB", "hh3cNDPPortNbPortName"),
)
if mibBuilder.loadTexts:
    hh3cNDPPortNbEntry.setStatus("current")


class _Hh3cNDPPortNbDeviceId_Type(OctetString):
    """Custom type hh3cNDPPortNbDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3cNDPPortNbDeviceId_Type.__name__ = "OctetString"
_Hh3cNDPPortNbDeviceId_Object = MibTableColumn
hh3cNDPPortNbDeviceId = _Hh3cNDPPortNbDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 1),
    _Hh3cNDPPortNbDeviceId_Type()
)
hh3cNDPPortNbDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbDeviceId.setStatus("current")


class _Hh3cNDPPortNbPortName_Type(OctetString):
    """Custom type hh3cNDPPortNbPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3cNDPPortNbPortName_Type.__name__ = "OctetString"
_Hh3cNDPPortNbPortName_Object = MibTableColumn
hh3cNDPPortNbPortName = _Hh3cNDPPortNbPortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 2),
    _Hh3cNDPPortNbPortName_Type()
)
hh3cNDPPortNbPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbPortName.setStatus("current")
_Hh3cNDPPortNbDeviceName_Type = OctetString
_Hh3cNDPPortNbDeviceName_Object = MibTableColumn
hh3cNDPPortNbDeviceName = _Hh3cNDPPortNbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 3),
    _Hh3cNDPPortNbDeviceName_Type()
)
hh3cNDPPortNbDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbDeviceName.setStatus("current")


class _Hh3cNDPPortNbPortMode_Type(Integer32):
    """Custom type hh3cNDPPortNbPortMode based on Integer32"""
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


_Hh3cNDPPortNbPortMode_Type.__name__ = "Integer32"
_Hh3cNDPPortNbPortMode_Object = MibTableColumn
hh3cNDPPortNbPortMode = _Hh3cNDPPortNbPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 4),
    _Hh3cNDPPortNbPortMode_Type()
)
hh3cNDPPortNbPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbPortMode.setStatus("current")
_Hh3cNDPPortNbProductVer_Type = OctetString
_Hh3cNDPPortNbProductVer_Object = MibTableColumn
hh3cNDPPortNbProductVer = _Hh3cNDPPortNbProductVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 5),
    _Hh3cNDPPortNbProductVer_Type()
)
hh3cNDPPortNbProductVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbProductVer.setStatus("current")
_Hh3cNDPPortNbHardVer_Type = OctetString
_Hh3cNDPPortNbHardVer_Object = MibTableColumn
hh3cNDPPortNbHardVer = _Hh3cNDPPortNbHardVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 6),
    _Hh3cNDPPortNbHardVer_Type()
)
hh3cNDPPortNbHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbHardVer.setStatus("current")
_Hh3cNDPPortNbBootromVer_Type = OctetString
_Hh3cNDPPortNbBootromVer_Object = MibTableColumn
hh3cNDPPortNbBootromVer = _Hh3cNDPPortNbBootromVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 7),
    _Hh3cNDPPortNbBootromVer_Type()
)
hh3cNDPPortNbBootromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbBootromVer.setStatus("current")
_Hh3cNDPPortNbSoftVer_Type = OctetString
_Hh3cNDPPortNbSoftVer_Object = MibTableColumn
hh3cNDPPortNbSoftVer = _Hh3cNDPPortNbSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 8),
    _Hh3cNDPPortNbSoftVer_Type()
)
hh3cNDPPortNbSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbSoftVer.setStatus("current")


class _Hh3cNDPPortNbAgingtime_Type(Integer32):
    """Custom type hh3cNDPPortNbAgingtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Hh3cNDPPortNbAgingtime_Type.__name__ = "Integer32"
_Hh3cNDPPortNbAgingtime_Object = MibTableColumn
hh3cNDPPortNbAgingtime = _Hh3cNDPPortNbAgingtime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 5, 6, 1, 9),
    _Hh3cNDPPortNbAgingtime_Type()
)
hh3cNDPPortNbAgingtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNDPPortNbAgingtime.setStatus("current")

# Managed Objects groups


# Notification objects

hh3chgmpMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 0, 1)
)
hh3chgmpMemberfailure.setObjects(
    ("HH3C-HGMP-MIB", "hh3chgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hh3chgmpMemberfailure.setStatus(
        "current"
    )

hh3chgmpMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 0, 2)
)
hh3chgmpMemberRecover.setObjects(
    ("HH3C-HGMP-MIB", "hh3chgmpGrpMemberDeviceId")
)
if mibBuilder.loadTexts:
    hh3chgmpMemberRecover.setStatus(
        "current"
    )

hh3chgmpMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 0, 3)
)
hh3chgmpMemberStatusChange.setObjects(
      *(("HH3C-HGMP-MIB", "hh3chgmpGrpMemberDeviceId"),
        ("HH3C-HGMP-MIB", "hh3chgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hh3chgmpMemberStatusChange.setStatus(
        "current"
    )

hh3chgmpNetTopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 1, 0, 4)
)
if mibBuilder.loadTexts:
    hh3chgmpNetTopChange.setStatus(
        "current"
    )

hh3chgmpStackMemberfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 0, 1)
)
hh3chgmpStackMemberfailure.setObjects(
    ("HH3C-HGMP-MIB", "hh3chgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hh3chgmpStackMemberfailure.setStatus(
        "current"
    )

hh3chgmpStackMemberRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 0, 2)
)
hh3chgmpStackMemberRecover.setObjects(
    ("HH3C-HGMP-MIB", "hh3chgmpStackMemberDeviceId")
)
if mibBuilder.loadTexts:
    hh3chgmpStackMemberRecover.setStatus(
        "current"
    )

hh3chgmpStackMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7, 2, 0, 3)
)
hh3chgmpStackMemberStatusChange.setObjects(
      *(("HH3C-HGMP-MIB", "hh3chgmpStackMemberDeviceId"),
        ("HH3C-HGMP-MIB", "hh3chgmpNTDPCacheClusterRole"))
)
if mibBuilder.loadTexts:
    hh3chgmpStackMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-HGMP-MIB",
    **{"hh3cHgmp": hh3cHgmp,
       "hh3cClusterObject": hh3cClusterObject,
       "hh3chgmpEventsV2": hh3chgmpEventsV2,
       "hh3chgmpMemberfailure": hh3chgmpMemberfailure,
       "hh3chgmpMemberRecover": hh3chgmpMemberRecover,
       "hh3chgmpMemberStatusChange": hh3chgmpMemberStatusChange,
       "hh3chgmpNetTopChange": hh3chgmpNetTopChange,
       "hh3chgmpSetVLANSecurity": hh3chgmpSetVLANSecurity,
       "hh3chgmpHandShakeInterval": hh3chgmpHandShakeInterval,
       "hh3chgmpHandShakeHoldtime": hh3chgmpHandShakeHoldtime,
       "hh3chgmpGrpMemberTableChange": hh3chgmpGrpMemberTableChange,
       "hh3chgmpMemberDisconRate": hh3chgmpMemberDisconRate,
       "hh3chgmpCmdLanswitchFlag": hh3chgmpCmdLanswitchFlag,
       "hh3chgmpCmdClusterName": hh3chgmpCmdClusterName,
       "hh3chgmpMngPriIpSegCMIP": hh3chgmpMngPriIpSegCMIP,
       "hh3chgmpMngPriIpMask": hh3chgmpMngPriIpMask,
       "hh3chgmpFtpServer": hh3chgmpFtpServer,
       "hh3chgmpTftpServer": hh3chgmpTftpServer,
       "hh3chgmpSnmpHost": hh3chgmpSnmpHost,
       "hh3chgmpLogHost": hh3chgmpLogHost,
       "hh3chgmpGrpMemberTable": hh3chgmpGrpMemberTable,
       "hh3chgmpGrpMemberEntry": hh3chgmpGrpMemberEntry,
       "hh3chgmpGrpMemberDeviceId": hh3chgmpGrpMemberDeviceId,
       "hh3chgmpGrpMemberSerial": hh3chgmpGrpMemberSerial,
       "hh3chgmpGrpMemberIpAddr": hh3chgmpGrpMemberIpAddr,
       "hh3chgmpGrpMemberName": hh3chgmpGrpMemberName,
       "hh3chgmpGrpMemberPassword": hh3chgmpGrpMemberPassword,
       "hh3chgmpGrpMemberPlatform": hh3chgmpGrpMemberPlatform,
       "hh3chgmpGrpMemberStatus": hh3chgmpGrpMemberStatus,
       "hh3chgmpGrpMemberDisconCount": hh3chgmpGrpMemberDisconCount,
       "hh3chgmpGrpMemberEnrollTime": hh3chgmpGrpMemberEnrollTime,
       "hh3chgmpGrpMemberOperate": hh3chgmpGrpMemberOperate,
       "hh3chgmpMemberResetTable": hh3chgmpMemberResetTable,
       "hh3chgmpMemberResetEntry": hh3chgmpMemberResetEntry,
       "hh3chgmpMemberResetMAC": hh3chgmpMemberResetMAC,
       "hh3chgmpMemberEraseflash": hh3chgmpMemberEraseflash,
       "hh3chgmpClusterRole": hh3chgmpClusterRole,
       "hh3chgmpClusterMaxPoolNum": hh3chgmpClusterMaxPoolNum,
       "hh3chgmpClusterCmdSwMac": hh3chgmpClusterCmdSwMac,
       "hh3chgmpRun": hh3chgmpRun,
       "hh3chgmpProtocolMac": hh3chgmpProtocolMac,
       "hh3chgmpClusterProtocolMac": hh3chgmpClusterProtocolMac,
       "hh3chgmpTopologyManagement": hh3chgmpTopologyManagement,
       "hh3chgmpWhitelistTable": hh3chgmpWhitelistTable,
       "hh3chgmpWhitelistEntry": hh3chgmpWhitelistEntry,
       "hh3chgmpWhitelistDeviceId": hh3chgmpWhitelistDeviceId,
       "hh3chgmpWhitelistSerial": hh3chgmpWhitelistSerial,
       "hh3chgmpWhitelistRowStatus": hh3chgmpWhitelistRowStatus,
       "hh3chgmpWhitelistNbTable": hh3chgmpWhitelistNbTable,
       "hh3chgmpWhitelistNbEntry": hh3chgmpWhitelistNbEntry,
       "hh3chgmpWhitelistNbIndex": hh3chgmpWhitelistNbIndex,
       "hh3chgmpWhitelistNbDeviceId": hh3chgmpWhitelistNbDeviceId,
       "hh3chgmpWhitelistPortName": hh3chgmpWhitelistPortName,
       "hh3chgmpWhitelistNbPortName": hh3chgmpWhitelistNbPortName,
       "hh3chgmpBlacklistTable": hh3chgmpBlacklistTable,
       "hh3chgmpBlacklistEntry": hh3chgmpBlacklistEntry,
       "hh3chgmpBlacklistDeviceId": hh3chgmpBlacklistDeviceId,
       "hh3chgmpBlacklistAccessDeviceId": hh3chgmpBlacklistAccessDeviceId,
       "hh3chgmpBlacklistAccessPortName": hh3chgmpBlacklistAccessPortName,
       "hh3chgmpBlacklistRowStatus": hh3chgmpBlacklistRowStatus,
       "hh3chgmpMemberPriPortTable": hh3chgmpMemberPriPortTable,
       "hh3chgmpMemberPriPortEntry": hh3chgmpMemberPriPortEntry,
       "hh3chgmpMemberDevId": hh3chgmpMemberDevId,
       "hh3chgmpMemberPriPortProto": hh3chgmpMemberPriPortProto,
       "hh3chgmpMemberPriPortProtoDescr": hh3chgmpMemberPriPortProtoDescr,
       "hh3chgmpMemberPriPortNum": hh3chgmpMemberPriPortNum,
       "hh3cStackObject": hh3cStackObject,
       "hh3chgmpStackEventsV2": hh3chgmpStackEventsV2,
       "hh3chgmpStackMemberfailure": hh3chgmpStackMemberfailure,
       "hh3chgmpStackMemberRecover": hh3chgmpStackMemberRecover,
       "hh3chgmpStackMemberStatusChange": hh3chgmpStackMemberStatusChange,
       "hh3chgmpStackMemberTableChange": hh3chgmpStackMemberTableChange,
       "hh3chgmpStackMemberDisconRate": hh3chgmpStackMemberDisconRate,
       "hh3chgmpMainLanswitchFlag": hh3chgmpMainLanswitchFlag,
       "hh3chgmpStackIpPoolStartIP": hh3chgmpStackIpPoolStartIP,
       "hh3chgmpStackIpPoolLength": hh3chgmpStackIpPoolLength,
       "hh3chgmpStackMemberTable": hh3chgmpStackMemberTable,
       "hh3chgmpStackMemberEntry": hh3chgmpStackMemberEntry,
       "hh3chgmpStackMemberDeviceId": hh3chgmpStackMemberDeviceId,
       "hh3chgmpStackMemberSerial": hh3chgmpStackMemberSerial,
       "hh3chgmpStackMemberIpAddr": hh3chgmpStackMemberIpAddr,
       "hh3chgmpStackMemberName": hh3chgmpStackMemberName,
       "hh3chgmpStackMemberPassword": hh3chgmpStackMemberPassword,
       "hh3chgmpStackMemberPlatform": hh3chgmpStackMemberPlatform,
       "hh3chgmpStackMemberStatus": hh3chgmpStackMemberStatus,
       "hh3chgmpStackMemberDisconCount": hh3chgmpStackMemberDisconCount,
       "hh3chgmpStackMemberEnrollTime": hh3chgmpStackMemberEnrollTime,
       "hh3chgmpStackRole": hh3chgmpStackRole,
       "hh3chgmpStackMaxPoolNum": hh3chgmpStackMaxPoolNum,
       "hh3chgmpStackMainSwMac": hh3chgmpStackMainSwMac,
       "hh3chgmpStackIpPoolMask": hh3chgmpStackIpPoolMask,
       "hh3cNTDPObject": hh3cNTDPObject,
       "hh3chgmpNTDPCollectTopTime": hh3chgmpNTDPCollectTopTime,
       "hh3chgmpNTDPHopRange": hh3chgmpNTDPHopRange,
       "hh3chgmpNTDPRun": hh3chgmpNTDPRun,
       "hh3chgmpNTDPPortDelay": hh3chgmpNTDPPortDelay,
       "hh3chgmpNTDPHopDelay": hh3chgmpNTDPHopDelay,
       "hh3chgmpNTDPLastTopCollectDuration": hh3chgmpNTDPLastTopCollectDuration,
       "hh3chgmpNTDPCacheChange": hh3chgmpNTDPCacheChange,
       "hh3chgmpNTDPTOPTableChange": hh3chgmpNTDPTOPTableChange,
       "hh3chgmpNTDPInterfaceTable": hh3chgmpNTDPInterfaceTable,
       "hh3chgmpNTDPInterfaceEntry": hh3chgmpNTDPInterfaceEntry,
       "hh3chgmpNTDPInterfaceIfIndex": hh3chgmpNTDPInterfaceIfIndex,
       "hh3chgmpNTDPInterfaceEnable": hh3chgmpNTDPInterfaceEnable,
       "hh3chgmpNTDPCacheTable": hh3chgmpNTDPCacheTable,
       "hh3chgmpNTDPCacheEntry": hh3chgmpNTDPCacheEntry,
       "hh3chgmpNTDPCacheHashIndex": hh3chgmpNTDPCacheHashIndex,
       "hh3chgmpNTDPCacheDeviceID": hh3chgmpNTDPCacheDeviceID,
       "hh3chgmpNTDPCacheClusterName": hh3chgmpNTDPCacheClusterName,
       "hh3chgmpNTDPCacheClusterRole": hh3chgmpNTDPCacheClusterRole,
       "hh3chgmpNTDPCacheCapabilities": hh3chgmpNTDPCacheCapabilities,
       "hh3chgmpNTDPCacheVersion": hh3chgmpNTDPCacheVersion,
       "hh3chgmpNTDPCachePlatform": hh3chgmpNTDPCachePlatform,
       "hh3chgmpNTDPCacheMngVLAN": hh3chgmpNTDPCacheMngVLAN,
       "hh3chgmpNTDPCacheHop": hh3chgmpNTDPCacheHop,
       "hh3chgmpNTDPTopTable": hh3chgmpNTDPTopTable,
       "hh3chgmpNTDPTopEntry": hh3chgmpNTDPTopEntry,
       "hh3chgmpNTDPTopHashIndex": hh3chgmpNTDPTopHashIndex,
       "hh3chgmpNTDPTopEdgeStartDevID": hh3chgmpNTDPTopEdgeStartDevID,
       "hh3chgmpNTDPTopEdgeIndex": hh3chgmpNTDPTopEdgeIndex,
       "hh3chgmpNTDPTopEdgeEndDevID": hh3chgmpNTDPTopEdgeEndDevID,
       "hh3chgmpNTDPTopEdgeStartPort": hh3chgmpNTDPTopEdgeStartPort,
       "hh3chgmpNTDPTopEdgeStartPortFullDuplex": hh3chgmpNTDPTopEdgeStartPortFullDuplex,
       "hh3chgmpNTDPTopEdgeStartPortSpeed": hh3chgmpNTDPTopEdgeStartPortSpeed,
       "hh3chgmpNTDPTopEdgeEndPort": hh3chgmpNTDPTopEdgeEndPort,
       "hh3chgmpNTDPTopLinkStatus": hh3chgmpNTDPTopLinkStatus,
       "hh3cNDPObject": hh3cNDPObject,
       "hh3cNDPStatus": hh3cNDPStatus,
       "hh3cNDPHelloTimer": hh3cNDPHelloTimer,
       "hh3cNDPAgingTime": hh3cNDPAgingTime,
       "hh3cNDPChange": hh3cNDPChange,
       "hh3cNDPPortTable": hh3cNDPPortTable,
       "hh3cNDPPortEntry": hh3cNDPPortEntry,
       "hh3cNDPIfIndex": hh3cNDPIfIndex,
       "hh3cNDPPortStatus": hh3cNDPPortStatus,
       "hh3cNDPPortNbTable": hh3cNDPPortNbTable,
       "hh3cNDPPortNbEntry": hh3cNDPPortNbEntry,
       "hh3cNDPPortNbDeviceId": hh3cNDPPortNbDeviceId,
       "hh3cNDPPortNbPortName": hh3cNDPPortNbPortName,
       "hh3cNDPPortNbDeviceName": hh3cNDPPortNbDeviceName,
       "hh3cNDPPortNbPortMode": hh3cNDPPortNbPortMode,
       "hh3cNDPPortNbProductVer": hh3cNDPPortNbProductVer,
       "hh3cNDPPortNbHardVer": hh3cNDPPortNbHardVer,
       "hh3cNDPPortNbBootromVer": hh3cNDPPortNbBootromVer,
       "hh3cNDPPortNbSoftVer": hh3cNDPPortNbSoftVer,
       "hh3cNDPPortNbAgingtime": hh3cNDPPortNbAgingtime}
)
