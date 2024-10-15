# SNMP MIB module (CT-ELS100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-ELS100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:09 2024
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

(ifInErrors,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors",
    "ifOutErrors")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sigma_ObjectIdentity = ObjectIdentity
sigma = _Sigma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 1)
)


class _SysID_Type(Integer32):
    """Custom type sysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("els-100-bridge", 8)
    )


_SysID_Type.__name__ = "Integer32"
_SysID_Object = MibScalar
sysID = _SysID_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 1),
    _SysID_Type()
)
sysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysID.setStatus("mandatory")
_SysReset_Type = TimeTicks
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 2),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")
_SysTrapPort_Type = Integer32
_SysTrapPort_Object = MibScalar
sysTrapPort = _SysTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 3),
    _SysTrapPort_Type()
)
sysTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPort.setStatus("mandatory")
_Els_100_ObjectIdentity = ObjectIdentity
els_100 = _Els_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8)
)
_Kxhw_ObjectIdentity = ObjectIdentity
kxhw = _Kxhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 1)
)
_KxhwDiagCode_Type = OctetString
_KxhwDiagCode_Object = MibScalar
kxhwDiagCode = _KxhwDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 1, 1),
    _KxhwDiagCode_Type()
)
kxhwDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxhwDiagCode.setStatus("mandatory")
_KxhwManufData_Type = OctetString
_KxhwManufData_Object = MibScalar
kxhwManufData = _KxhwManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 1, 2),
    _KxhwManufData_Type()
)
kxhwManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxhwManufData.setStatus("mandatory")
_KxhwPortCount_Type = Integer32
_KxhwPortCount_Object = MibScalar
kxhwPortCount = _KxhwPortCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 1, 3),
    _KxhwPortCount_Type()
)
kxhwPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxhwPortCount.setStatus("mandatory")
_Kxsw_ObjectIdentity = ObjectIdentity
kxsw = _Kxsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 2)
)
_KxswNumber_Type = Integer32
_KxswNumber_Object = MibScalar
kxswNumber = _KxswNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 1),
    _KxswNumber_Type()
)
kxswNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswNumber.setStatus("mandatory")
_KxswFilesetTable_Object = MibTable
kxswFilesetTable = _KxswFilesetTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2)
)
if mibBuilder.loadTexts:
    kxswFilesetTable.setStatus("mandatory")
_KxswFilesetEntry_Object = MibTableRow
kxswFilesetEntry = _KxswFilesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1)
)
kxswFilesetEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxswIndex"),
)
if mibBuilder.loadTexts:
    kxswFilesetEntry.setStatus("mandatory")


class _KxswIndex_Type(Integer32):
    """Custom type kxswIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currently-executing", 1),
          ("next-boot", 2))
    )


_KxswIndex_Type.__name__ = "Integer32"
_KxswIndex_Object = MibTableColumn
kxswIndex = _KxswIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 1),
    _KxswIndex_Type()
)
kxswIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswIndex.setStatus("mandatory")
_KxswDesc_Type = DisplayString
_KxswDesc_Object = MibTableColumn
kxswDesc = _KxswDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 2),
    _KxswDesc_Type()
)
kxswDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswDesc.setStatus("mandatory")
_KxswCount_Type = Integer32
_KxswCount_Object = MibTableColumn
kxswCount = _KxswCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 3),
    _KxswCount_Type()
)
kxswCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswCount.setStatus("mandatory")
_KxswType_Type = OctetString
_KxswType_Object = MibTableColumn
kxswType = _KxswType_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 4),
    _KxswType_Type()
)
kxswType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswType.setStatus("mandatory")
_KxswSizes_Type = OctetString
_KxswSizes_Object = MibTableColumn
kxswSizes = _KxswSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 5),
    _KxswSizes_Type()
)
kxswSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswSizes.setStatus("mandatory")
_KxswStarts_Type = OctetString
_KxswStarts_Object = MibTableColumn
kxswStarts = _KxswStarts_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 6),
    _KxswStarts_Type()
)
kxswStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswStarts.setStatus("mandatory")
_KxswBases_Type = OctetString
_KxswBases_Object = MibTableColumn
kxswBases = _KxswBases_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 7),
    _KxswBases_Type()
)
kxswBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswBases.setStatus("mandatory")


class _KxswFlashBank_Type(Integer32):
    """Custom type kxswFlashBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first-bank", 1),
          ("second-bank", 2))
    )


_KxswFlashBank_Type.__name__ = "Integer32"
_KxswFlashBank_Object = MibTableColumn
kxswFlashBank = _KxswFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 2, 2, 1, 8),
    _KxswFlashBank_Type()
)
kxswFlashBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswFlashBank.setStatus("mandatory")
_Kxadmin_ObjectIdentity = ObjectIdentity
kxadmin = _Kxadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 3)
)
_KxadminFatalErr_Type = OctetString
_KxadminFatalErr_Object = MibScalar
kxadminFatalErr = _KxadminFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 1),
    _KxadminFatalErr_Type()
)
kxadminFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminFatalErr.setStatus("mandatory")
_KxadminAnyPass_Type = OctetString
_KxadminAnyPass_Object = MibScalar
kxadminAnyPass = _KxadminAnyPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 2),
    _KxadminAnyPass_Type()
)
kxadminAnyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminAnyPass.setStatus("mandatory")
_KxadminGetPass_Type = OctetString
_KxadminGetPass_Object = MibScalar
kxadminGetPass = _KxadminGetPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 3),
    _KxadminGetPass_Type()
)
kxadminGetPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminGetPass.setStatus("mandatory")
_KxadminNMSIPAddr_Type = IpAddress
_KxadminNMSIPAddr_Object = MibScalar
kxadminNMSIPAddr = _KxadminNMSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 4),
    _KxadminNMSIPAddr_Type()
)
kxadminNMSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminNMSIPAddr.setStatus("mandatory")


class _KxadminStorageFailure_Type(Integer32):
    """Custom type kxadminStorageFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_KxadminStorageFailure_Type.__name__ = "Integer32"
_KxadminStorageFailure_Object = MibScalar
kxadminStorageFailure = _KxadminStorageFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 5),
    _KxadminStorageFailure_Type()
)
kxadminStorageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminStorageFailure.setStatus("mandatory")
_KxadminAuthenticationFailure_Type = IpAddress
_KxadminAuthenticationFailure_Object = MibScalar
kxadminAuthenticationFailure = _KxadminAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 6),
    _KxadminAuthenticationFailure_Type()
)
kxadminAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminAuthenticationFailure.setStatus("mandatory")
_KxadminNAMReceiveCongests_Type = Counter32
_KxadminNAMReceiveCongests_Object = MibScalar
kxadminNAMReceiveCongests = _KxadminNAMReceiveCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 7),
    _KxadminNAMReceiveCongests_Type()
)
kxadminNAMReceiveCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminNAMReceiveCongests.setStatus("mandatory")
_KxadminArpEntries_Type = Counter32
_KxadminArpEntries_Object = MibScalar
kxadminArpEntries = _KxadminArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 8),
    _KxadminArpEntries_Type()
)
kxadminArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminArpEntries.setStatus("mandatory")
_KxadminArpStatics_Type = Counter32
_KxadminArpStatics_Object = MibScalar
kxadminArpStatics = _KxadminArpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 9),
    _KxadminArpStatics_Type()
)
kxadminArpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminArpStatics.setStatus("mandatory")
_KxadminArpOverflows_Type = Counter32
_KxadminArpOverflows_Object = MibScalar
kxadminArpOverflows = _KxadminArpOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 10),
    _KxadminArpOverflows_Type()
)
kxadminArpOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminArpOverflows.setStatus("mandatory")
_KxadminRipPreference_Type = Integer32
_KxadminRipPreference_Object = MibScalar
kxadminRipPreference = _KxadminRipPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 11),
    _KxadminRipPreference_Type()
)
kxadminRipPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminRipPreference.setStatus("mandatory")
_KxadminRipRouteDiscards_Type = Counter32
_KxadminRipRouteDiscards_Object = MibScalar
kxadminRipRouteDiscards = _KxadminRipRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 12),
    _KxadminRipRouteDiscards_Type()
)
kxadminRipRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxadminRipRouteDiscards.setStatus("mandatory")


class _KxadminRebootConfig_Type(Integer32):
    """Custom type kxadminRebootConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-change", 1),
          ("revert-to-defaults", 3),
          ("tftp-config", 2))
    )


_KxadminRebootConfig_Type.__name__ = "Integer32"
_KxadminRebootConfig_Object = MibScalar
kxadminRebootConfig = _KxadminRebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 13),
    _KxadminRebootConfig_Type()
)
kxadminRebootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminRebootConfig.setStatus("mandatory")


class _KxadminDisableButton_Type(Integer32):
    """Custom type kxadminDisableButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_KxadminDisableButton_Type.__name__ = "Integer32"
_KxadminDisableButton_Object = MibScalar
kxadminDisableButton = _KxadminDisableButton_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 14),
    _KxadminDisableButton_Type()
)
kxadminDisableButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminDisableButton.setStatus("mandatory")


class _KxadminButtonSelection_Type(Integer32):
    """Custom type kxadminButtonSelection based on Integer32"""
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
        *(("led-any-activity", 1),
          ("led-any-collision", 4),
          ("led-duplex", 6),
          ("led-mirror", 8),
          ("led-programmed", 5),
          ("led-rx-activity", 2),
          ("led-speed", 7),
          ("led-tx-activity", 3))
    )


_KxadminButtonSelection_Type.__name__ = "Integer32"
_KxadminButtonSelection_Object = MibScalar
kxadminButtonSelection = _KxadminButtonSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 15),
    _KxadminButtonSelection_Type()
)
kxadminButtonSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminButtonSelection.setStatus("mandatory")


class _KxadminLEDProgramOption_Type(Integer32):
    """Custom type kxadminLEDProgramOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("program-led-any-error", 1)
    )


_KxadminLEDProgramOption_Type.__name__ = "Integer32"
_KxadminLEDProgramOption_Object = MibScalar
kxadminLEDProgramOption = _KxadminLEDProgramOption_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 3, 16),
    _KxadminLEDProgramOption_Type()
)
kxadminLEDProgramOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxadminLEDProgramOption.setStatus("mandatory")
_Kxswdis_ObjectIdentity = ObjectIdentity
kxswdis = _Kxswdis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 4)
)
_KxswdisDesc_Type = OctetString
_KxswdisDesc_Object = MibScalar
kxswdisDesc = _KxswdisDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 1),
    _KxswdisDesc_Type()
)
kxswdisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswdisDesc.setStatus("mandatory")


class _KxswdisAccess_Type(Integer32):
    """Custom type kxswdisAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any-software", 2),
          ("protected", 1))
    )


_KxswdisAccess_Type.__name__ = "Integer32"
_KxswdisAccess_Object = MibScalar
kxswdisAccess = _KxswdisAccess_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 2),
    _KxswdisAccess_Type()
)
kxswdisAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxswdisAccess.setStatus("mandatory")


class _KxswdisWriteStatus_Type(Integer32):
    """Custom type kxswdisWriteStatus based on Integer32"""
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
        *(("config-and-flash-errors", 5),
          ("config-error", 3),
          ("flash-error", 4),
          ("in-progress", 1),
          ("success", 2))
    )


_KxswdisWriteStatus_Type.__name__ = "Integer32"
_KxswdisWriteStatus_Object = MibScalar
kxswdisWriteStatus = _KxswdisWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 3),
    _KxswdisWriteStatus_Type()
)
kxswdisWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxswdisWriteStatus.setStatus("mandatory")
_KxswdisConfigIp_Type = IpAddress
_KxswdisConfigIp_Object = MibScalar
kxswdisConfigIp = _KxswdisConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 4),
    _KxswdisConfigIp_Type()
)
kxswdisConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxswdisConfigIp.setStatus("mandatory")
_KxswdisConfigRetryTime_Type = Integer32
_KxswdisConfigRetryTime_Object = MibScalar
kxswdisConfigRetryTime = _KxswdisConfigRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 5),
    _KxswdisConfigRetryTime_Type()
)
kxswdisConfigRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxswdisConfigRetryTime.setStatus("mandatory")
_KxswdisConfigTotalTimeout_Type = Integer32
_KxswdisConfigTotalTimeout_Object = MibScalar
kxswdisConfigTotalTimeout = _KxswdisConfigTotalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 4, 6),
    _KxswdisConfigTotalTimeout_Type()
)
kxswdisConfigTotalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxswdisConfigTotalTimeout.setStatus("mandatory")
_Kxaddr_ObjectIdentity = ObjectIdentity
kxaddr = _Kxaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 5)
)
_KxaddrStatics_Type = Counter32
_KxaddrStatics_Object = MibScalar
kxaddrStatics = _KxaddrStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 1),
    _KxaddrStatics_Type()
)
kxaddrStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxaddrStatics.setStatus("mandatory")
_KxaddrDynamics_Type = Counter32
_KxaddrDynamics_Object = MibScalar
kxaddrDynamics = _KxaddrDynamics_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 2),
    _KxaddrDynamics_Type()
)
kxaddrDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxaddrDynamics.setStatus("mandatory")
_KxaddrDynamicMax_Type = Gauge32
_KxaddrDynamicMax_Object = MibScalar
kxaddrDynamicMax = _KxaddrDynamicMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 3),
    _KxaddrDynamicMax_Type()
)
kxaddrDynamicMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrDynamicMax.setStatus("mandatory")
_KxaddrDynamicOverflows_Type = Counter32
_KxaddrDynamicOverflows_Object = MibScalar
kxaddrDynamicOverflows = _KxaddrDynamicOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 4),
    _KxaddrDynamicOverflows_Type()
)
kxaddrDynamicOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxaddrDynamicOverflows.setStatus("mandatory")
_KxaddrFlags_Type = Integer32
_KxaddrFlags_Object = MibScalar
kxaddrFlags = _KxaddrFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 5),
    _KxaddrFlags_Type()
)
kxaddrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrFlags.setStatus("mandatory")
_KxaddrMAC_Type = OctetString
_KxaddrMAC_Object = MibScalar
kxaddrMAC = _KxaddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 6),
    _KxaddrMAC_Type()
)
kxaddrMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrMAC.setStatus("mandatory")
_KxaddrPort_Type = Integer32
_KxaddrPort_Object = MibScalar
kxaddrPort = _KxaddrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 7),
    _KxaddrPort_Type()
)
kxaddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrPort.setStatus("mandatory")


class _KxaddrOperation_Type(Integer32):
    """Custom type kxaddrOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delete", 5),
          ("read-block", 6),
          ("read-next", 2),
          ("read-random", 1),
          ("update", 4))
    )


_KxaddrOperation_Type.__name__ = "Integer32"
_KxaddrOperation_Object = MibScalar
kxaddrOperation = _KxaddrOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 8),
    _KxaddrOperation_Type()
)
kxaddrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrOperation.setStatus("mandatory")
_KxaddrIndex_Type = Integer32
_KxaddrIndex_Object = MibScalar
kxaddrIndex = _KxaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 9),
    _KxaddrIndex_Type()
)
kxaddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrIndex.setStatus("mandatory")
_KxaddrNext_Type = Integer32
_KxaddrNext_Object = MibScalar
kxaddrNext = _KxaddrNext_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 10),
    _KxaddrNext_Type()
)
kxaddrNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrNext.setStatus("mandatory")
_KxaddrBlockSize_Type = Integer32
_KxaddrBlockSize_Object = MibScalar
kxaddrBlockSize = _KxaddrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 11),
    _KxaddrBlockSize_Type()
)
kxaddrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrBlockSize.setStatus("mandatory")
_KxaddrBlock_Type = OctetString
_KxaddrBlock_Object = MibScalar
kxaddrBlock = _KxaddrBlock_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 5, 12),
    _KxaddrBlock_Type()
)
kxaddrBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxaddrBlock.setStatus("mandatory")
_Kxif_ObjectIdentity = ObjectIdentity
kxif = _Kxif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 6)
)
_KxifTable_Object = MibTable
kxifTable = _KxifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1)
)
if mibBuilder.loadTexts:
    kxifTable.setStatus("mandatory")
_KxifEntry_Object = MibTableRow
kxifEntry = _KxifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1)
)
kxifEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxifIndex"),
)
if mibBuilder.loadTexts:
    kxifEntry.setStatus("mandatory")
_KxifIndex_Type = Integer32
_KxifIndex_Object = MibTableColumn
kxifIndex = _KxifIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 1),
    _KxifIndex_Type()
)
kxifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxifIndex.setStatus("mandatory")
_KxifRxCnt_Type = Integer32
_KxifRxCnt_Object = MibTableColumn
kxifRxCnt = _KxifRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 2),
    _KxifRxCnt_Type()
)
kxifRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxifRxCnt.setStatus("mandatory")
_KxifTxCnt_Type = Integer32
_KxifTxCnt_Object = MibTableColumn
kxifTxCnt = _KxifTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 3),
    _KxifTxCnt_Type()
)
kxifTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxifTxCnt.setStatus("mandatory")
_KxifThreshold_Type = Integer32
_KxifThreshold_Object = MibTableColumn
kxifThreshold = _KxifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 4),
    _KxifThreshold_Type()
)
kxifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxifThreshold.setStatus("mandatory")
_KxifThresholdTime_Type = Integer32
_KxifThresholdTime_Object = MibTableColumn
kxifThresholdTime = _KxifThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 5),
    _KxifThresholdTime_Type()
)
kxifThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxifThresholdTime.setStatus("mandatory")
_KxifRxQueueThresh_Type = Integer32
_KxifRxQueueThresh_Object = MibTableColumn
kxifRxQueueThresh = _KxifRxQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 6),
    _KxifRxQueueThresh_Type()
)
kxifRxQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxifRxQueueThresh.setStatus("mandatory")
_KxifRxQueueThreshTime_Type = Integer32
_KxifRxQueueThreshTime_Object = MibTableColumn
kxifRxQueueThreshTime = _KxifRxQueueThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 7),
    _KxifRxQueueThreshTime_Type()
)
kxifRxQueueThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxifRxQueueThreshTime.setStatus("mandatory")
_KxifFunction_Type = Integer32
_KxifFunction_Object = MibTableColumn
kxifFunction = _KxifFunction_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 8),
    _KxifFunction_Type()
)
kxifFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxifFunction.setStatus("mandatory")
_KxifStatisticsTime_Type = TimeTicks
_KxifStatisticsTime_Object = MibTableColumn
kxifStatisticsTime = _KxifStatisticsTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 6, 1, 1, 9),
    _KxifStatisticsTime_Type()
)
kxifStatisticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxifStatisticsTime.setStatus("mandatory")
_Kxuart_ObjectIdentity = ObjectIdentity
kxuart = _Kxuart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 7)
)
_KxuartTable_Object = MibTable
kxuartTable = _KxuartTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1)
)
if mibBuilder.loadTexts:
    kxuartTable.setStatus("mandatory")
_KxuartEntry_Object = MibTableRow
kxuartEntry = _KxuartEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1, 1)
)
kxuartEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxuartIndex"),
)
if mibBuilder.loadTexts:
    kxuartEntry.setStatus("mandatory")
_KxuartIndex_Type = Integer32
_KxuartIndex_Object = MibTableColumn
kxuartIndex = _KxuartIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1, 1, 1),
    _KxuartIndex_Type()
)
kxuartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxuartIndex.setStatus("mandatory")


class _KxuartBaud_Type(Integer32):
    """Custom type kxuartBaud based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("b1200-baud", 2),
          ("b1544-kilobits", 9),
          ("b19200-baud", 6),
          ("b2048-kilobits", 10),
          ("b2400-baud", 3),
          ("b38400-baud", 7),
          ("b45-megabits", 11),
          ("b4800-baud", 4),
          ("b56-kilobits", 8),
          ("b9600-baud", 5),
          ("external-clock", 1))
    )


_KxuartBaud_Type.__name__ = "Integer32"
_KxuartBaud_Object = MibTableColumn
kxuartBaud = _KxuartBaud_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1, 1, 2),
    _KxuartBaud_Type()
)
kxuartBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxuartBaud.setStatus("mandatory")
_KxuartAlignmentErrors_Type = Counter32
_KxuartAlignmentErrors_Object = MibTableColumn
kxuartAlignmentErrors = _KxuartAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1, 1, 3),
    _KxuartAlignmentErrors_Type()
)
kxuartAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxuartAlignmentErrors.setStatus("mandatory")
_KxuartOverrunErrors_Type = Counter32
_KxuartOverrunErrors_Object = MibTableColumn
kxuartOverrunErrors = _KxuartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 7, 1, 1, 4),
    _KxuartOverrunErrors_Type()
)
kxuartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxuartOverrunErrors.setStatus("mandatory")
_Kxproto_ObjectIdentity = ObjectIdentity
kxproto = _Kxproto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 8)
)
_KxprotoTable_Object = MibTable
kxprotoTable = _KxprotoTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1)
)
if mibBuilder.loadTexts:
    kxprotoTable.setStatus("mandatory")
_KxprotoEntry_Object = MibTableRow
kxprotoEntry = _KxprotoEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1)
)
kxprotoEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxprotoIfIndex"),
)
if mibBuilder.loadTexts:
    kxprotoEntry.setStatus("mandatory")
_KxprotoIfIndex_Type = Integer32
_KxprotoIfIndex_Object = MibTableColumn
kxprotoIfIndex = _KxprotoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1, 1),
    _KxprotoIfIndex_Type()
)
kxprotoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxprotoIfIndex.setStatus("mandatory")


class _KxprotoBridge_Type(Integer32):
    """Custom type kxprotoBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("transparent", 1))
    )


_KxprotoBridge_Type.__name__ = "Integer32"
_KxprotoBridge_Object = MibTableColumn
kxprotoBridge = _KxprotoBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1, 2),
    _KxprotoBridge_Type()
)
kxprotoBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxprotoBridge.setStatus("mandatory")


class _KxprotoSuppressBpdu_Type(Integer32):
    """Custom type kxprotoSuppressBpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("suppressed", 2))
    )


_KxprotoSuppressBpdu_Type.__name__ = "Integer32"
_KxprotoSuppressBpdu_Object = MibTableColumn
kxprotoSuppressBpdu = _KxprotoSuppressBpdu_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1, 3),
    _KxprotoSuppressBpdu_Type()
)
kxprotoSuppressBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxprotoSuppressBpdu.setStatus("mandatory")


class _KxprotoRipListen_Type(Integer32):
    """Custom type kxprotoRipListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_KxprotoRipListen_Type.__name__ = "Integer32"
_KxprotoRipListen_Object = MibTableColumn
kxprotoRipListen = _KxprotoRipListen_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1, 4),
    _KxprotoRipListen_Type()
)
kxprotoRipListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxprotoRipListen.setStatus("mandatory")


class _KxprotoTrunking_Type(Integer32):
    """Custom type kxprotoTrunking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_KxprotoTrunking_Type.__name__ = "Integer32"
_KxprotoTrunking_Object = MibTableColumn
kxprotoTrunking = _KxprotoTrunking_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 8, 1, 1, 5),
    _KxprotoTrunking_Type()
)
kxprotoTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxprotoTrunking.setStatus("mandatory")
_Kxtrunk_ObjectIdentity = ObjectIdentity
kxtrunk = _Kxtrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 9)
)
_KxtrunkTable_Object = MibTable
kxtrunkTable = _KxtrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1)
)
if mibBuilder.loadTexts:
    kxtrunkTable.setStatus("mandatory")
_KxtrunkEntry_Object = MibTableRow
kxtrunkEntry = _KxtrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1)
)
kxtrunkEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxtrunkIfIndex"),
)
if mibBuilder.loadTexts:
    kxtrunkEntry.setStatus("mandatory")
_KxtrunkIfIndex_Type = Integer32
_KxtrunkIfIndex_Object = MibTableColumn
kxtrunkIfIndex = _KxtrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 1),
    _KxtrunkIfIndex_Type()
)
kxtrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkIfIndex.setStatus("mandatory")


class _KxtrunkState_Type(Integer32):
    """Custom type kxtrunkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("disabled", 7),
          ("helddown", 6),
          ("joined", 4),
          ("off", 1),
          ("oneway", 3),
          ("perturbed", 5))
    )


_KxtrunkState_Type.__name__ = "Integer32"
_KxtrunkState_Object = MibTableColumn
kxtrunkState = _KxtrunkState_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 2),
    _KxtrunkState_Type()
)
kxtrunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkState.setStatus("mandatory")
_KxtrunkRemoteBridgeAddr_Type = OctetString
_KxtrunkRemoteBridgeAddr_Object = MibTableColumn
kxtrunkRemoteBridgeAddr = _KxtrunkRemoteBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 3),
    _KxtrunkRemoteBridgeAddr_Type()
)
kxtrunkRemoteBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkRemoteBridgeAddr.setStatus("mandatory")
_KxtrunkRemoteIp_Type = IpAddress
_KxtrunkRemoteIp_Object = MibTableColumn
kxtrunkRemoteIp = _KxtrunkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 4),
    _KxtrunkRemoteIp_Type()
)
kxtrunkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkRemoteIp.setStatus("mandatory")


class _KxtrunkLastError_Type(Integer32):
    """Custom type kxtrunkLastError based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ack-lost", 4),
          ("in-bpdu", 2),
          ("multiple-bridges", 3),
          ("multiple-lan-types", 11),
          ("no-ack", 7),
          ("none", 1),
          ("perturbed-threshold", 8),
          ("port-moved", 10),
          ("self-connect", 9),
          ("standby", 5),
          ("too-many-groups", 6))
    )


_KxtrunkLastError_Type.__name__ = "Integer32"
_KxtrunkLastError_Object = MibTableColumn
kxtrunkLastError = _KxtrunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 5),
    _KxtrunkLastError_Type()
)
kxtrunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkLastError.setStatus("mandatory")
_KxtrunkLinkOrdinal_Type = Integer32
_KxtrunkLinkOrdinal_Object = MibTableColumn
kxtrunkLinkOrdinal = _KxtrunkLinkOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 6),
    _KxtrunkLinkOrdinal_Type()
)
kxtrunkLinkOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkLinkOrdinal.setStatus("mandatory")
_KxtrunkLinkCount_Type = Integer32
_KxtrunkLinkCount_Object = MibTableColumn
kxtrunkLinkCount = _KxtrunkLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 7),
    _KxtrunkLinkCount_Type()
)
kxtrunkLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkLinkCount.setStatus("mandatory")
_KxtrunkLastChange_Type = Integer32
_KxtrunkLastChange_Object = MibTableColumn
kxtrunkLastChange = _KxtrunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 9, 1, 1, 8),
    _KxtrunkLastChange_Type()
)
kxtrunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrunkLastChange.setStatus("mandatory")
_Kxworkgroup_ObjectIdentity = ObjectIdentity
kxworkgroup = _Kxworkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 10)
)
_KxWorkGroupNextNumber_Type = Integer32
_KxWorkGroupNextNumber_Object = MibScalar
kxWorkGroupNextNumber = _KxWorkGroupNextNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 1),
    _KxWorkGroupNextNumber_Type()
)
kxWorkGroupNextNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxWorkGroupNextNumber.setStatus("mandatory")
_KxWorkGroupCurrentCount_Type = Integer32
_KxWorkGroupCurrentCount_Object = MibScalar
kxWorkGroupCurrentCount = _KxWorkGroupCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 2),
    _KxWorkGroupCurrentCount_Type()
)
kxWorkGroupCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxWorkGroupCurrentCount.setStatus("mandatory")
_KxWorkGroupMaxCount_Type = Integer32
_KxWorkGroupMaxCount_Object = MibScalar
kxWorkGroupMaxCount = _KxWorkGroupMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 3),
    _KxWorkGroupMaxCount_Type()
)
kxWorkGroupMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxWorkGroupMaxCount.setStatus("mandatory")
_KxWorkGroupTable_Object = MibTable
kxWorkGroupTable = _KxWorkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4)
)
if mibBuilder.loadTexts:
    kxWorkGroupTable.setStatus("mandatory")
_KxWorkGroupEntry_Object = MibTableRow
kxWorkGroupEntry = _KxWorkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4, 1)
)
kxWorkGroupEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxWorkGroupNumber"),
)
if mibBuilder.loadTexts:
    kxWorkGroupEntry.setStatus("mandatory")
_KxWorkGroupNumber_Type = Integer32
_KxWorkGroupNumber_Object = MibTableColumn
kxWorkGroupNumber = _KxWorkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4, 1, 1),
    _KxWorkGroupNumber_Type()
)
kxWorkGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxWorkGroupNumber.setStatus("mandatory")
_KxWorkGroupName_Type = DisplayString
_KxWorkGroupName_Object = MibTableColumn
kxWorkGroupName = _KxWorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4, 1, 2),
    _KxWorkGroupName_Type()
)
kxWorkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxWorkGroupName.setStatus("mandatory")
_KxWorkGroupPorts_Type = OctetString
_KxWorkGroupPorts_Object = MibTableColumn
kxWorkGroupPorts = _KxWorkGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4, 1, 3),
    _KxWorkGroupPorts_Type()
)
kxWorkGroupPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxWorkGroupPorts.setStatus("mandatory")


class _KxWorkGroupType_Type(Integer32):
    """Custom type kxWorkGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("invalid", 4))
    )


_KxWorkGroupType_Type.__name__ = "Integer32"
_KxWorkGroupType_Object = MibTableColumn
kxWorkGroupType = _KxWorkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 10, 4, 1, 4),
    _KxWorkGroupType_Type()
)
kxWorkGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxWorkGroupType.setStatus("mandatory")
_KxtrapMgt_ObjectIdentity = ObjectIdentity
kxtrapMgt = _KxtrapMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 11)
)
_KxtrapControlTable_Object = MibTable
kxtrapControlTable = _KxtrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1)
)
if mibBuilder.loadTexts:
    kxtrapControlTable.setStatus("mandatory")
_KxtrapControlEntry_Object = MibTableRow
kxtrapControlEntry = _KxtrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1, 1)
)
kxtrapControlEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxtrapIndex"),
)
if mibBuilder.loadTexts:
    kxtrapControlEntry.setStatus("mandatory")
_KxtrapIndex_Type = Integer32
_KxtrapIndex_Object = MibTableColumn
kxtrapIndex = _KxtrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1, 1, 1),
    _KxtrapIndex_Type()
)
kxtrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapIndex.setStatus("mandatory")


class _KxtrapEnabled_Type(Integer32):
    """Custom type kxtrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_KxtrapEnabled_Type.__name__ = "Integer32"
_KxtrapEnabled_Object = MibTableColumn
kxtrapEnabled = _KxtrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1, 1, 2),
    _KxtrapEnabled_Type()
)
kxtrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapEnabled.setStatus("mandatory")


class _KxtrapSeverity_Type(Integer32):
    """Custom type kxtrapSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_KxtrapSeverity_Type.__name__ = "Integer32"
_KxtrapSeverity_Object = MibTableColumn
kxtrapSeverity = _KxtrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1, 1, 3),
    _KxtrapSeverity_Type()
)
kxtrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapSeverity.setStatus("mandatory")
_KxtrapText_Type = DisplayString
_KxtrapText_Object = MibTableColumn
kxtrapText = _KxtrapText_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 1, 1, 4),
    _KxtrapText_Type()
)
kxtrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapText.setStatus("mandatory")
_KxtrapSeverityControlTable_Object = MibTable
kxtrapSeverityControlTable = _KxtrapSeverityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 2)
)
if mibBuilder.loadTexts:
    kxtrapSeverityControlTable.setStatus("mandatory")
_KxtrapSeverityControlEntry_Object = MibTableRow
kxtrapSeverityControlEntry = _KxtrapSeverityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 2, 1)
)
kxtrapSeverityControlEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxtrapSeverity"),
)
if mibBuilder.loadTexts:
    kxtrapSeverityControlEntry.setStatus("mandatory")


class _KxtrapSeverityControlSeverity_Type(Integer32):
    """Custom type kxtrapSeverityControlSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_KxtrapSeverityControlSeverity_Type.__name__ = "Integer32"
_KxtrapSeverityControlSeverity_Object = MibTableColumn
kxtrapSeverityControlSeverity = _KxtrapSeverityControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 2, 1, 1),
    _KxtrapSeverityControlSeverity_Type()
)
kxtrapSeverityControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapSeverityControlSeverity.setStatus("mandatory")


class _KxtrapSeverityEnable_Type(Integer32):
    """Custom type kxtrapSeverityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_KxtrapSeverityEnable_Type.__name__ = "Integer32"
_KxtrapSeverityEnable_Object = MibTableColumn
kxtrapSeverityEnable = _KxtrapSeverityEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 2, 1, 2),
    _KxtrapSeverityEnable_Type()
)
kxtrapSeverityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapSeverityEnable.setStatus("mandatory")


class _KxtrapIncludeText_Type(Integer32):
    """Custom type kxtrapIncludeText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_KxtrapIncludeText_Type.__name__ = "Integer32"
_KxtrapIncludeText_Object = MibScalar
kxtrapIncludeText = _KxtrapIncludeText_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 3),
    _KxtrapIncludeText_Type()
)
kxtrapIncludeText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapIncludeText.setStatus("mandatory")
_KxtrapTime_Type = TimeTicks
_KxtrapTime_Object = MibScalar
kxtrapTime = _KxtrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 4),
    _KxtrapTime_Type()
)
kxtrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapTime.setStatus("mandatory")
_KxtrapRetry_Type = Integer32
_KxtrapRetry_Object = MibScalar
kxtrapRetry = _KxtrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 5),
    _KxtrapRetry_Type()
)
kxtrapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxtrapRetry.setStatus("mandatory")
_KxtrapNumber_Type = Integer32
_KxtrapNumber_Object = MibScalar
kxtrapNumber = _KxtrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 6),
    _KxtrapNumber_Type()
)
kxtrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapNumber.setStatus("mandatory")
_KxtrapTable_Object = MibTable
kxtrapTable = _KxtrapTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7)
)
if mibBuilder.loadTexts:
    kxtrapTable.setStatus("mandatory")
_KxtrapEntry_Object = MibTableRow
kxtrapEntry = _KxtrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1)
)
kxtrapEntry.setIndexNames(
    (0, "CT-ELS100-MIB", "kxtrapEntryIndex"),
)
if mibBuilder.loadTexts:
    kxtrapEntry.setStatus("mandatory")
_KxtrapEntryIndex_Type = Integer32
_KxtrapEntryIndex_Object = MibTableColumn
kxtrapEntryIndex = _KxtrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1, 1),
    _KxtrapEntryIndex_Type()
)
kxtrapEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapEntryIndex.setStatus("mandatory")
_KxtrapEntryTimeStamp_Type = TimeTicks
_KxtrapEntryTimeStamp_Object = MibTableColumn
kxtrapEntryTimeStamp = _KxtrapEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1, 2),
    _KxtrapEntryTimeStamp_Type()
)
kxtrapEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapEntryTimeStamp.setStatus("mandatory")
_KxtrapEntryText_Type = DisplayString
_KxtrapEntryText_Object = MibTableColumn
kxtrapEntryText = _KxtrapEntryText_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1, 3),
    _KxtrapEntryText_Type()
)
kxtrapEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapEntryText.setStatus("mandatory")
_KxtrapEntryNumber_Type = Integer32
_KxtrapEntryNumber_Object = MibTableColumn
kxtrapEntryNumber = _KxtrapEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1, 4),
    _KxtrapEntryNumber_Type()
)
kxtrapEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapEntryNumber.setStatus("mandatory")


class _KxtrapEntrySeverity_Type(Integer32):
    """Custom type kxtrapEntrySeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_KxtrapEntrySeverity_Type.__name__ = "Integer32"
_KxtrapEntrySeverity_Object = MibTableColumn
kxtrapEntrySeverity = _KxtrapEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 11, 7, 1, 5),
    _KxtrapEntrySeverity_Type()
)
kxtrapEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kxtrapEntrySeverity.setStatus("mandatory")
_Kxmirrorgroup_ObjectIdentity = ObjectIdentity
kxmirrorgroup = _Kxmirrorgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 8, 12)
)


class _KxmirrorMode_Type(Integer32):
    """Custom type kxmirrorMode based on Integer32"""
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
        *(("off", 1),
          ("rx", 3),
          ("rxandtx", 4),
          ("tx", 2))
    )


_KxmirrorMode_Type.__name__ = "Integer32"
_KxmirrorMode_Object = MibScalar
kxmirrorMode = _KxmirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 12, 1),
    _KxmirrorMode_Type()
)
kxmirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxmirrorMode.setStatus("mandatory")
_KxmirrorDiagPort_Type = Integer32
_KxmirrorDiagPort_Object = MibScalar
kxmirrorDiagPort = _KxmirrorDiagPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 12, 2),
    _KxmirrorDiagPort_Type()
)
kxmirrorDiagPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxmirrorDiagPort.setStatus("mandatory")
_KxmirrorTargetPortLists_Type = OctetString
_KxmirrorTargetPortLists_Object = MibScalar
kxmirrorTargetPortLists = _KxmirrorTargetPortLists_Object(
    (1, 3, 6, 1, 4, 1, 97, 8, 12, 3),
    _KxmirrorTargetPortLists_Type()
)
kxmirrorTargetPortLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kxmirrorTargetPortLists.setStatus("mandatory")

# Managed Objects groups


# Notification objects

kxPortFunctionsTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 1)
)
kxPortFunctionsTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxifFunction"))
)
if mibBuilder.loadTexts:
    kxPortFunctionsTrap.setStatus(
        ""
    )

kxRxQueuesTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 2)
)
kxRxQueuesTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxifRxQueueThreshTime"))
)
if mibBuilder.loadTexts:
    kxRxQueuesTrap.setStatus(
        ""
    )

kxTxStormFlagTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 3)
)
kxTxStormFlagTrap.setObjects(
    ("CT-ELS100-MIB", "kxtrapSeverity")
)
if mibBuilder.loadTexts:
    kxTxStormFlagTrap.setStatus(
        ""
    )

kxTxCongestsTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 4)
)
kxTxCongestsTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxadminNAMReceiveCongests"))
)
if mibBuilder.loadTexts:
    kxTxCongestsTrap.setStatus(
        ""
    )

kxTrunkStateTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 5)
)
kxTrunkStateTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkState"))
)
if mibBuilder.loadTexts:
    kxTrunkStateTrap.setStatus(
        ""
    )

kxTrunkBridgeAddrTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 6)
)
kxTrunkBridgeAddrTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkRemoteBridgeAddr"))
)
if mibBuilder.loadTexts:
    kxTrunkBridgeAddrTrap.setStatus(
        ""
    )

kxTrunkIPAddrTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 7)
)
kxTrunkIPAddrTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkRemoteIp"))
)
if mibBuilder.loadTexts:
    kxTrunkIPAddrTrap.setStatus(
        ""
    )

kxTrunkErrorTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 8)
)
kxTrunkErrorTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkLastError"))
)
if mibBuilder.loadTexts:
    kxTrunkErrorTrap.setStatus(
        ""
    )

kxTrunkLinkOrdinalTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 9)
)
kxTrunkLinkOrdinalTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkLinkOrdinal"))
)
if mibBuilder.loadTexts:
    kxTrunkLinkOrdinalTrap.setStatus(
        ""
    )

kxTrunkLinkCountTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 10)
)
kxTrunkLinkCountTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxtrunkLinkCount"))
)
if mibBuilder.loadTexts:
    kxTrunkLinkCountTrap.setStatus(
        ""
    )

kxDiagUnitBootedTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 11)
)
kxDiagUnitBootedTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("CT-ELS100-MIB", "kxadminFatalErr"))
)
if mibBuilder.loadTexts:
    kxDiagUnitBootedTrap.setStatus(
        ""
    )

kxStorageFailureTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 12)
)
kxStorageFailureTrap.setObjects(
    ("CT-ELS100-MIB", "kxtrapSeverity")
)
if mibBuilder.loadTexts:
    kxStorageFailureTrap.setStatus(
        ""
    )

kxIfErrorsTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 2, 0, 13)
)
kxIfErrorsTrap.setObjects(
      *(("CT-ELS100-MIB", "kxtrapSeverity"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    kxIfErrorsTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-ELS100-MIB",
    **{"kxPortFunctionsTrap": kxPortFunctionsTrap,
       "kxRxQueuesTrap": kxRxQueuesTrap,
       "kxTxStormFlagTrap": kxTxStormFlagTrap,
       "kxTxCongestsTrap": kxTxCongestsTrap,
       "kxTrunkStateTrap": kxTrunkStateTrap,
       "kxTrunkBridgeAddrTrap": kxTrunkBridgeAddrTrap,
       "kxTrunkIPAddrTrap": kxTrunkIPAddrTrap,
       "kxTrunkErrorTrap": kxTrunkErrorTrap,
       "kxTrunkLinkOrdinalTrap": kxTrunkLinkOrdinalTrap,
       "kxTrunkLinkCountTrap": kxTrunkLinkCountTrap,
       "kxDiagUnitBootedTrap": kxDiagUnitBootedTrap,
       "kxStorageFailureTrap": kxStorageFailureTrap,
       "kxIfErrorsTrap": kxIfErrorsTrap,
       "sigma": sigma,
       "sys": sys,
       "sysID": sysID,
       "sysReset": sysReset,
       "sysTrapPort": sysTrapPort,
       "els-100": els_100,
       "kxhw": kxhw,
       "kxhwDiagCode": kxhwDiagCode,
       "kxhwManufData": kxhwManufData,
       "kxhwPortCount": kxhwPortCount,
       "kxsw": kxsw,
       "kxswNumber": kxswNumber,
       "kxswFilesetTable": kxswFilesetTable,
       "kxswFilesetEntry": kxswFilesetEntry,
       "kxswIndex": kxswIndex,
       "kxswDesc": kxswDesc,
       "kxswCount": kxswCount,
       "kxswType": kxswType,
       "kxswSizes": kxswSizes,
       "kxswStarts": kxswStarts,
       "kxswBases": kxswBases,
       "kxswFlashBank": kxswFlashBank,
       "kxadmin": kxadmin,
       "kxadminFatalErr": kxadminFatalErr,
       "kxadminAnyPass": kxadminAnyPass,
       "kxadminGetPass": kxadminGetPass,
       "kxadminNMSIPAddr": kxadminNMSIPAddr,
       "kxadminStorageFailure": kxadminStorageFailure,
       "kxadminAuthenticationFailure": kxadminAuthenticationFailure,
       "kxadminNAMReceiveCongests": kxadminNAMReceiveCongests,
       "kxadminArpEntries": kxadminArpEntries,
       "kxadminArpStatics": kxadminArpStatics,
       "kxadminArpOverflows": kxadminArpOverflows,
       "kxadminRipPreference": kxadminRipPreference,
       "kxadminRipRouteDiscards": kxadminRipRouteDiscards,
       "kxadminRebootConfig": kxadminRebootConfig,
       "kxadminDisableButton": kxadminDisableButton,
       "kxadminButtonSelection": kxadminButtonSelection,
       "kxadminLEDProgramOption": kxadminLEDProgramOption,
       "kxswdis": kxswdis,
       "kxswdisDesc": kxswdisDesc,
       "kxswdisAccess": kxswdisAccess,
       "kxswdisWriteStatus": kxswdisWriteStatus,
       "kxswdisConfigIp": kxswdisConfigIp,
       "kxswdisConfigRetryTime": kxswdisConfigRetryTime,
       "kxswdisConfigTotalTimeout": kxswdisConfigTotalTimeout,
       "kxaddr": kxaddr,
       "kxaddrStatics": kxaddrStatics,
       "kxaddrDynamics": kxaddrDynamics,
       "kxaddrDynamicMax": kxaddrDynamicMax,
       "kxaddrDynamicOverflows": kxaddrDynamicOverflows,
       "kxaddrFlags": kxaddrFlags,
       "kxaddrMAC": kxaddrMAC,
       "kxaddrPort": kxaddrPort,
       "kxaddrOperation": kxaddrOperation,
       "kxaddrIndex": kxaddrIndex,
       "kxaddrNext": kxaddrNext,
       "kxaddrBlockSize": kxaddrBlockSize,
       "kxaddrBlock": kxaddrBlock,
       "kxif": kxif,
       "kxifTable": kxifTable,
       "kxifEntry": kxifEntry,
       "kxifIndex": kxifIndex,
       "kxifRxCnt": kxifRxCnt,
       "kxifTxCnt": kxifTxCnt,
       "kxifThreshold": kxifThreshold,
       "kxifThresholdTime": kxifThresholdTime,
       "kxifRxQueueThresh": kxifRxQueueThresh,
       "kxifRxQueueThreshTime": kxifRxQueueThreshTime,
       "kxifFunction": kxifFunction,
       "kxifStatisticsTime": kxifStatisticsTime,
       "kxuart": kxuart,
       "kxuartTable": kxuartTable,
       "kxuartEntry": kxuartEntry,
       "kxuartIndex": kxuartIndex,
       "kxuartBaud": kxuartBaud,
       "kxuartAlignmentErrors": kxuartAlignmentErrors,
       "kxuartOverrunErrors": kxuartOverrunErrors,
       "kxproto": kxproto,
       "kxprotoTable": kxprotoTable,
       "kxprotoEntry": kxprotoEntry,
       "kxprotoIfIndex": kxprotoIfIndex,
       "kxprotoBridge": kxprotoBridge,
       "kxprotoSuppressBpdu": kxprotoSuppressBpdu,
       "kxprotoRipListen": kxprotoRipListen,
       "kxprotoTrunking": kxprotoTrunking,
       "kxtrunk": kxtrunk,
       "kxtrunkTable": kxtrunkTable,
       "kxtrunkEntry": kxtrunkEntry,
       "kxtrunkIfIndex": kxtrunkIfIndex,
       "kxtrunkState": kxtrunkState,
       "kxtrunkRemoteBridgeAddr": kxtrunkRemoteBridgeAddr,
       "kxtrunkRemoteIp": kxtrunkRemoteIp,
       "kxtrunkLastError": kxtrunkLastError,
       "kxtrunkLinkOrdinal": kxtrunkLinkOrdinal,
       "kxtrunkLinkCount": kxtrunkLinkCount,
       "kxtrunkLastChange": kxtrunkLastChange,
       "kxworkgroup": kxworkgroup,
       "kxWorkGroupNextNumber": kxWorkGroupNextNumber,
       "kxWorkGroupCurrentCount": kxWorkGroupCurrentCount,
       "kxWorkGroupMaxCount": kxWorkGroupMaxCount,
       "kxWorkGroupTable": kxWorkGroupTable,
       "kxWorkGroupEntry": kxWorkGroupEntry,
       "kxWorkGroupNumber": kxWorkGroupNumber,
       "kxWorkGroupName": kxWorkGroupName,
       "kxWorkGroupPorts": kxWorkGroupPorts,
       "kxWorkGroupType": kxWorkGroupType,
       "kxtrapMgt": kxtrapMgt,
       "kxtrapControlTable": kxtrapControlTable,
       "kxtrapControlEntry": kxtrapControlEntry,
       "kxtrapIndex": kxtrapIndex,
       "kxtrapEnabled": kxtrapEnabled,
       "kxtrapSeverity": kxtrapSeverity,
       "kxtrapText": kxtrapText,
       "kxtrapSeverityControlTable": kxtrapSeverityControlTable,
       "kxtrapSeverityControlEntry": kxtrapSeverityControlEntry,
       "kxtrapSeverityControlSeverity": kxtrapSeverityControlSeverity,
       "kxtrapSeverityEnable": kxtrapSeverityEnable,
       "kxtrapIncludeText": kxtrapIncludeText,
       "kxtrapTime": kxtrapTime,
       "kxtrapRetry": kxtrapRetry,
       "kxtrapNumber": kxtrapNumber,
       "kxtrapTable": kxtrapTable,
       "kxtrapEntry": kxtrapEntry,
       "kxtrapEntryIndex": kxtrapEntryIndex,
       "kxtrapEntryTimeStamp": kxtrapEntryTimeStamp,
       "kxtrapEntryText": kxtrapEntryText,
       "kxtrapEntryNumber": kxtrapEntryNumber,
       "kxtrapEntrySeverity": kxtrapEntrySeverity,
       "kxmirrorgroup": kxmirrorgroup,
       "kxmirrorMode": kxmirrorMode,
       "kxmirrorDiagPort": kxmirrorDiagPort,
       "kxmirrorTargetPortLists": kxmirrorTargetPortLists}
)
