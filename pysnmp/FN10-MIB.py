# SNMP MIB module (FN10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FN10-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:14 2024
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

(dot1dStpDesignatedRoot,
 dot1dStpForwardDelay,
 dot1dStpHelloTime,
 dot1dStpMaxAge,
 dot1dStpPortDesignatedBridge,
 dot1dStpPortDesignatedCost,
 dot1dStpPortDesignatedPort,
 dot1dStpPortDesignatedRoot,
 dot1dStpPortState,
 dot1dStpRootCost,
 dot1dStpRootPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpDesignatedRoot",
    "dot1dStpForwardDelay",
    "dot1dStpHelloTime",
    "dot1dStpMaxAge",
    "dot1dStpPortDesignatedBridge",
    "dot1dStpPortDesignatedCost",
    "dot1dStpPortDesignatedPort",
    "dot1dStpPortDesignatedRoot",
    "dot1dStpPortState",
    "dot1dStpRootCost",
    "dot1dStpRootPort")

(ifInErrors,
 ifOutDiscards,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors",
    "ifOutDiscards",
    "ifOutErrors")

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

_Cmu_ObjectIdentity = ObjectIdentity
cmu = _Cmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3, 1)
)
_CmuSNMP_ObjectIdentity = ObjectIdentity
cmuSNMP = _CmuSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3, 1, 1)
)
_CmuKip_ObjectIdentity = ObjectIdentity
cmuKip = _CmuKip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3, 1, 2)
)
_CmuRouter_ObjectIdentity = ObjectIdentity
cmuRouter = _CmuRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3, 1, 3)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3, 2)
)
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
            2
        )
    )
    namedValues = NamedValues(
        ("es-1xe-bridge", 2)
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


class _SysTrapAck_Type(Integer32):
    """Custom type sysTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traps-need-acks", 1),
          ("traps-not-acked", 2))
    )


_SysTrapAck_Type.__name__ = "Integer32"
_SysTrapAck_Object = MibScalar
sysTrapAck = _SysTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 3),
    _SysTrapAck_Type()
)
sysTrapAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapAck.setStatus("mandatory")
_SysTrapTime_Type = TimeTicks
_SysTrapTime_Object = MibScalar
sysTrapTime = _SysTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 4),
    _SysTrapTime_Type()
)
sysTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapTime.setStatus("mandatory")
_SysTrapRetry_Type = TimeTicks
_SysTrapRetry_Object = MibScalar
sysTrapRetry = _SysTrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 5),
    _SysTrapRetry_Type()
)
sysTrapRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapRetry.setStatus("mandatory")
_SysTrapPort_Type = Integer32
_SysTrapPort_Object = MibScalar
sysTrapPort = _SysTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 6),
    _SysTrapPort_Type()
)
sysTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPort.setStatus("mandatory")
_Es_1xe_ObjectIdentity = ObjectIdentity
es_1xe = _Es_1xe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2)
)
_Sxhw_ObjectIdentity = ObjectIdentity
sxhw = _Sxhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 1)
)
_SxhwDiagCode_Type = OctetString
_SxhwDiagCode_Object = MibScalar
sxhwDiagCode = _SxhwDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 1),
    _SxhwDiagCode_Type()
)
sxhwDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwDiagCode.setStatus("mandatory")
_SxhwManufData_Type = OctetString
_SxhwManufData_Object = MibScalar
sxhwManufData = _SxhwManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 2),
    _SxhwManufData_Type()
)
sxhwManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwManufData.setStatus("mandatory")
_SxhwPortCount_Type = Integer32
_SxhwPortCount_Object = MibScalar
sxhwPortCount = _SxhwPortCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 3),
    _SxhwPortCount_Type()
)
sxhwPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwPortCount.setStatus("mandatory")
_SxhwPortTable_Object = MibTable
sxhwPortTable = _SxhwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sxhwPortTable.setStatus("mandatory")
_SxhwPortEntry_Object = MibTableRow
sxhwPortEntry = _SxhwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1)
)
sxhwPortEntry.setIndexNames(
    (0, "FN10-MIB", "sxhwPortIndex"),
)
if mibBuilder.loadTexts:
    sxhwPortEntry.setStatus("mandatory")
_SxhwPortIndex_Type = Integer32
_SxhwPortIndex_Object = MibTableColumn
sxhwPortIndex = _SxhwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1, 1),
    _SxhwPortIndex_Type()
)
sxhwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwPortIndex.setStatus("mandatory")


class _SxhwPortType_Type(Integer32):
    """Custom type sxhwPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("port-csma", 1),
          ("port-none", 255),
          ("port-uart", 6))
    )


_SxhwPortType_Type.__name__ = "Integer32"
_SxhwPortType_Object = MibTableColumn
sxhwPortType = _SxhwPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1, 2),
    _SxhwPortType_Type()
)
sxhwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwPortType.setStatus("mandatory")


class _SxhwPortSubType_Type(Integer32):
    """Custom type sxhwPortSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14,
              16,
              17,
              18,
              80,
              255)
        )
    )
    namedValues = NamedValues(
        *(("csmacd-100-fx", 17),
          ("csmacd-100-tp4", 18),
          ("csmacd-100-tpx", 16),
          ("csmacd-aui-tpx", 14),
          ("csmacd-tpx", 13),
          ("no-information", 255),
          ("uart-female-9pin", 80))
    )


_SxhwPortSubType_Type.__name__ = "Integer32"
_SxhwPortSubType_Object = MibTableColumn
sxhwPortSubType = _SxhwPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1, 3),
    _SxhwPortSubType_Type()
)
sxhwPortSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwPortSubType.setStatus("mandatory")


class _SxhwPortDiagPassed_Type(Integer32):
    """Custom type sxhwPortDiagPassed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diag-failed", 2),
          ("diag-passed", 1))
    )


_SxhwPortDiagPassed_Type.__name__ = "Integer32"
_SxhwPortDiagPassed_Object = MibTableColumn
sxhwPortDiagPassed = _SxhwPortDiagPassed_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1, 4),
    _SxhwPortDiagPassed_Type()
)
sxhwPortDiagPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwPortDiagPassed.setStatus("mandatory")
_SxhwAddr_Type = OctetString
_SxhwAddr_Object = MibTableColumn
sxhwAddr = _SxhwAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 4, 1, 5),
    _SxhwAddr_Type()
)
sxhwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwAddr.setStatus("mandatory")


class _SxhwUpLink_Type(Integer32):
    """Custom type sxhwUpLink based on Integer32"""
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


_SxhwUpLink_Type.__name__ = "Integer32"
_SxhwUpLink_Object = MibScalar
sxhwUpLink = _SxhwUpLink_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 5),
    _SxhwUpLink_Type()
)
sxhwUpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwUpLink.setStatus("mandatory")
_SxhwUpLinkManufData_Type = OctetString
_SxhwUpLinkManufData_Object = MibScalar
sxhwUpLinkManufData = _SxhwUpLinkManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 1, 6),
    _SxhwUpLinkManufData_Type()
)
sxhwUpLinkManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxhwUpLinkManufData.setStatus("mandatory")
_Sxsw_ObjectIdentity = ObjectIdentity
sxsw = _Sxsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 2)
)
_SxswNumber_Type = Integer32
_SxswNumber_Object = MibScalar
sxswNumber = _SxswNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 1),
    _SxswNumber_Type()
)
sxswNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswNumber.setStatus("mandatory")
_SxswFilesetTable_Object = MibTable
sxswFilesetTable = _SxswFilesetTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sxswFilesetTable.setStatus("mandatory")
_SxswFileset_Object = MibTableRow
sxswFileset = _SxswFileset_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1)
)
sxswFileset.setIndexNames(
    (0, "FN10-MIB", "sxswIndex"),
)
if mibBuilder.loadTexts:
    sxswFileset.setStatus("mandatory")


class _SxswIndex_Type(Integer32):
    """Custom type sxswIndex based on Integer32"""
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


_SxswIndex_Type.__name__ = "Integer32"
_SxswIndex_Object = MibTableColumn
sxswIndex = _SxswIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 1),
    _SxswIndex_Type()
)
sxswIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswIndex.setStatus("mandatory")
_SxswDesc_Type = DisplayString
_SxswDesc_Object = MibTableColumn
sxswDesc = _SxswDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 2),
    _SxswDesc_Type()
)
sxswDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswDesc.setStatus("mandatory")
_SxswCount_Type = Integer32
_SxswCount_Object = MibTableColumn
sxswCount = _SxswCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 3),
    _SxswCount_Type()
)
sxswCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswCount.setStatus("mandatory")
_SxswType_Type = OctetString
_SxswType_Object = MibTableColumn
sxswType = _SxswType_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 4),
    _SxswType_Type()
)
sxswType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswType.setStatus("mandatory")
_SxswSizes_Type = OctetString
_SxswSizes_Object = MibTableColumn
sxswSizes = _SxswSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 5),
    _SxswSizes_Type()
)
sxswSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswSizes.setStatus("mandatory")
_SxswStarts_Type = OctetString
_SxswStarts_Object = MibTableColumn
sxswStarts = _SxswStarts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 6),
    _SxswStarts_Type()
)
sxswStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswStarts.setStatus("mandatory")
_SxswBases_Type = OctetString
_SxswBases_Object = MibTableColumn
sxswBases = _SxswBases_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 7),
    _SxswBases_Type()
)
sxswBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswBases.setStatus("mandatory")


class _SxswFlashBank_Type(Integer32):
    """Custom type sxswFlashBank based on Integer32"""
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


_SxswFlashBank_Type.__name__ = "Integer32"
_SxswFlashBank_Object = MibTableColumn
sxswFlashBank = _SxswFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 2, 2, 1, 8),
    _SxswFlashBank_Type()
)
sxswFlashBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswFlashBank.setStatus("mandatory")
_Sxadmin_ObjectIdentity = ObjectIdentity
sxadmin = _Sxadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 3)
)
_SxadminFatalErr_Type = OctetString
_SxadminFatalErr_Object = MibScalar
sxadminFatalErr = _SxadminFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 1),
    _SxadminFatalErr_Type()
)
sxadminFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminFatalErr.setStatus("mandatory")
_SxadminAnyPass_Type = OctetString
_SxadminAnyPass_Object = MibScalar
sxadminAnyPass = _SxadminAnyPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 2),
    _SxadminAnyPass_Type()
)
sxadminAnyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminAnyPass.setStatus("mandatory")
_SxadminGetPass_Type = OctetString
_SxadminGetPass_Object = MibScalar
sxadminGetPass = _SxadminGetPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 3),
    _SxadminGetPass_Type()
)
sxadminGetPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminGetPass.setStatus("mandatory")
_SxadminNMSIPAddr_Type = IpAddress
_SxadminNMSIPAddr_Object = MibScalar
sxadminNMSIPAddr = _SxadminNMSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 4),
    _SxadminNMSIPAddr_Type()
)
sxadminNMSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminNMSIPAddr.setStatus("mandatory")


class _SxadminAlarmDynamic_Type(Integer32):
    """Custom type sxadminAlarmDynamic based on Integer32"""
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


_SxadminAlarmDynamic_Type.__name__ = "Integer32"
_SxadminAlarmDynamic_Object = MibScalar
sxadminAlarmDynamic = _SxadminAlarmDynamic_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 5),
    _SxadminAlarmDynamic_Type()
)
sxadminAlarmDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminAlarmDynamic.setStatus("mandatory")


class _SxadminAlarmAddressChange_Type(Integer32):
    """Custom type sxadminAlarmAddressChange based on Integer32"""
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


_SxadminAlarmAddressChange_Type.__name__ = "Integer32"
_SxadminAlarmAddressChange_Object = MibScalar
sxadminAlarmAddressChange = _SxadminAlarmAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 6),
    _SxadminAlarmAddressChange_Type()
)
sxadminAlarmAddressChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminAlarmAddressChange.setStatus("mandatory")


class _SxadminStorageFailure_Type(Integer32):
    """Custom type sxadminStorageFailure based on Integer32"""
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


_SxadminStorageFailure_Type.__name__ = "Integer32"
_SxadminStorageFailure_Object = MibScalar
sxadminStorageFailure = _SxadminStorageFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 7),
    _SxadminStorageFailure_Type()
)
sxadminStorageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminStorageFailure.setStatus("mandatory")
_SxadminAuthenticationFailure_Type = IpAddress
_SxadminAuthenticationFailure_Object = MibScalar
sxadminAuthenticationFailure = _SxadminAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 8),
    _SxadminAuthenticationFailure_Type()
)
sxadminAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminAuthenticationFailure.setStatus("mandatory")


class _SxadminStatsExtended_Type(Integer32):
    """Custom type sxadminStatsExtended based on Integer32"""
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


_SxadminStatsExtended_Type.__name__ = "Integer32"
_SxadminStatsExtended_Object = MibScalar
sxadminStatsExtended = _SxadminStatsExtended_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 9),
    _SxadminStatsExtended_Type()
)
sxadminStatsExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminStatsExtended.setStatus("mandatory")
_SxadminNAMReceiveCongests_Type = Counter32
_SxadminNAMReceiveCongests_Object = MibScalar
sxadminNAMReceiveCongests = _SxadminNAMReceiveCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 10),
    _SxadminNAMReceiveCongests_Type()
)
sxadminNAMReceiveCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminNAMReceiveCongests.setStatus("mandatory")
_SxadminArpEntries_Type = Counter32
_SxadminArpEntries_Object = MibScalar
sxadminArpEntries = _SxadminArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 11),
    _SxadminArpEntries_Type()
)
sxadminArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminArpEntries.setStatus("mandatory")
_SxadminArpStatics_Type = Counter32
_SxadminArpStatics_Object = MibScalar
sxadminArpStatics = _SxadminArpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 12),
    _SxadminArpStatics_Type()
)
sxadminArpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminArpStatics.setStatus("mandatory")
_SxadminArpOverflows_Type = Counter32
_SxadminArpOverflows_Object = MibScalar
sxadminArpOverflows = _SxadminArpOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 13),
    _SxadminArpOverflows_Type()
)
sxadminArpOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminArpOverflows.setStatus("mandatory")
_SxadminIpEntries_Type = Counter32
_SxadminIpEntries_Object = MibScalar
sxadminIpEntries = _SxadminIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 14),
    _SxadminIpEntries_Type()
)
sxadminIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminIpEntries.setStatus("mandatory")
_SxadminIpStatics_Type = Counter32
_SxadminIpStatics_Object = MibScalar
sxadminIpStatics = _SxadminIpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 15),
    _SxadminIpStatics_Type()
)
sxadminIpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminIpStatics.setStatus("mandatory")
_SxadminStaticPreference_Type = Integer32
_SxadminStaticPreference_Object = MibScalar
sxadminStaticPreference = _SxadminStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 16),
    _SxadminStaticPreference_Type()
)
sxadminStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminStaticPreference.setStatus("mandatory")
_SxadminRipPreference_Type = Integer32
_SxadminRipPreference_Object = MibScalar
sxadminRipPreference = _SxadminRipPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 17),
    _SxadminRipPreference_Type()
)
sxadminRipPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminRipPreference.setStatus("mandatory")
_SxadminRipRouteDiscards_Type = Counter32
_SxadminRipRouteDiscards_Object = MibScalar
sxadminRipRouteDiscards = _SxadminRipRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 18),
    _SxadminRipRouteDiscards_Type()
)
sxadminRipRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminRipRouteDiscards.setStatus("mandatory")


class _SxadminRebootConfig_Type(Integer32):
    """Custom type sxadminRebootConfig based on Integer32"""
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


_SxadminRebootConfig_Type.__name__ = "Integer32"
_SxadminRebootConfig_Object = MibScalar
sxadminRebootConfig = _SxadminRebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 19),
    _SxadminRebootConfig_Type()
)
sxadminRebootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminRebootConfig.setStatus("mandatory")


class _SxadminTempOK_Type(Integer32):
    """Custom type sxadminTempOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperature-normal", 1),
          ("temperature-too-hot", 2))
    )


_SxadminTempOK_Type.__name__ = "Integer32"
_SxadminTempOK_Object = MibScalar
sxadminTempOK = _SxadminTempOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 20),
    _SxadminTempOK_Type()
)
sxadminTempOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminTempOK.setStatus("mandatory")


class _SxadminDisableButton_Type(Integer32):
    """Custom type sxadminDisableButton based on Integer32"""
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


_SxadminDisableButton_Type.__name__ = "Integer32"
_SxadminDisableButton_Object = MibScalar
sxadminDisableButton = _SxadminDisableButton_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 21),
    _SxadminDisableButton_Type()
)
sxadminDisableButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminDisableButton.setStatus("mandatory")


class _SxadminButtonSelection_Type(Integer32):
    """Custom type sxadminButtonSelection based on Integer32"""
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
        *(("led-any-activity", 1),
          ("led-any-collision", 4),
          ("led-programmed", 5),
          ("led-rx-activity", 2),
          ("led-tx-activity", 3))
    )


_SxadminButtonSelection_Type.__name__ = "Integer32"
_SxadminButtonSelection_Object = MibScalar
sxadminButtonSelection = _SxadminButtonSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 22),
    _SxadminButtonSelection_Type()
)
sxadminButtonSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminButtonSelection.setStatus("mandatory")


class _SxadminLEDProgramOption_Type(Integer32):
    """Custom type sxadminLEDProgramOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("program-led-any-error", 1)
    )


_SxadminLEDProgramOption_Type.__name__ = "Integer32"
_SxadminLEDProgramOption_Object = MibScalar
sxadminLEDProgramOption = _SxadminLEDProgramOption_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 23),
    _SxadminLEDProgramOption_Type()
)
sxadminLEDProgramOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminLEDProgramOption.setStatus("mandatory")
_SxadminNAMTxBufferCount_Type = Integer32
_SxadminNAMTxBufferCount_Object = MibScalar
sxadminNAMTxBufferCount = _SxadminNAMTxBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 24),
    _SxadminNAMTxBufferCount_Type()
)
sxadminNAMTxBufferCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminNAMTxBufferCount.setStatus("mandatory")
_SxadminNAMRxBufferSize_Type = Integer32
_SxadminNAMRxBufferSize_Object = MibScalar
sxadminNAMRxBufferSize = _SxadminNAMRxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 25),
    _SxadminNAMRxBufferSize_Type()
)
sxadminNAMRxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminNAMRxBufferSize.setStatus("mandatory")


class _SxadminCpuUtilization_Type(Integer32):
    """Custom type sxadminCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-cpu", 3),
          ("low-cpu", 1),
          ("medium-cpu", 2))
    )


_SxadminCpuUtilization_Type.__name__ = "Integer32"
_SxadminCpuUtilization_Object = MibScalar
sxadminCpuUtilization = _SxadminCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 26),
    _SxadminCpuUtilization_Type()
)
sxadminCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxadminCpuUtilization.setStatus("mandatory")


class _SxadminExtraTrunkGrouping_Type(Integer32):
    """Custom type sxadminExtraTrunkGrouping based on Integer32"""
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


_SxadminExtraTrunkGrouping_Type.__name__ = "Integer32"
_SxadminExtraTrunkGrouping_Object = MibScalar
sxadminExtraTrunkGrouping = _SxadminExtraTrunkGrouping_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 3, 27),
    _SxadminExtraTrunkGrouping_Type()
)
sxadminExtraTrunkGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxadminExtraTrunkGrouping.setStatus("mandatory")
_Sxswdis_ObjectIdentity = ObjectIdentity
sxswdis = _Sxswdis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 4)
)
_SxswdisDesc_Type = OctetString
_SxswdisDesc_Object = MibScalar
sxswdisDesc = _SxswdisDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 1),
    _SxswdisDesc_Type()
)
sxswdisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswdisDesc.setStatus("mandatory")


class _SxswdisAccess_Type(Integer32):
    """Custom type sxswdisAccess based on Integer32"""
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


_SxswdisAccess_Type.__name__ = "Integer32"
_SxswdisAccess_Object = MibScalar
sxswdisAccess = _SxswdisAccess_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 2),
    _SxswdisAccess_Type()
)
sxswdisAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxswdisAccess.setStatus("mandatory")


class _SxswdisWriteStatus_Type(Integer32):
    """Custom type sxswdisWriteStatus based on Integer32"""
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


_SxswdisWriteStatus_Type.__name__ = "Integer32"
_SxswdisWriteStatus_Object = MibScalar
sxswdisWriteStatus = _SxswdisWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 3),
    _SxswdisWriteStatus_Type()
)
sxswdisWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxswdisWriteStatus.setStatus("mandatory")
_SxswdisConfigIp_Type = IpAddress
_SxswdisConfigIp_Object = MibScalar
sxswdisConfigIp = _SxswdisConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 4),
    _SxswdisConfigIp_Type()
)
sxswdisConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxswdisConfigIp.setStatus("mandatory")
_SxswdisConfigRetryTime_Type = Integer32
_SxswdisConfigRetryTime_Object = MibScalar
sxswdisConfigRetryTime = _SxswdisConfigRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 5),
    _SxswdisConfigRetryTime_Type()
)
sxswdisConfigRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxswdisConfigRetryTime.setStatus("mandatory")
_SxswdisConfigTotalTimeout_Type = Integer32
_SxswdisConfigTotalTimeout_Object = MibScalar
sxswdisConfigTotalTimeout = _SxswdisConfigTotalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 4, 6),
    _SxswdisConfigTotalTimeout_Type()
)
sxswdisConfigTotalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxswdisConfigTotalTimeout.setStatus("mandatory")
_Sxaddr_ObjectIdentity = ObjectIdentity
sxaddr = _Sxaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 5)
)
_SxaddrStatics_Type = Counter32
_SxaddrStatics_Object = MibScalar
sxaddrStatics = _SxaddrStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 1),
    _SxaddrStatics_Type()
)
sxaddrStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxaddrStatics.setStatus("mandatory")
_SxaddrDynamics_Type = Counter32
_SxaddrDynamics_Object = MibScalar
sxaddrDynamics = _SxaddrDynamics_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 2),
    _SxaddrDynamics_Type()
)
sxaddrDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxaddrDynamics.setStatus("mandatory")
_SxaddrDynamicMax_Type = Gauge32
_SxaddrDynamicMax_Object = MibScalar
sxaddrDynamicMax = _SxaddrDynamicMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 3),
    _SxaddrDynamicMax_Type()
)
sxaddrDynamicMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrDynamicMax.setStatus("mandatory")
_SxaddrDynamicOverflows_Type = Counter32
_SxaddrDynamicOverflows_Object = MibScalar
sxaddrDynamicOverflows = _SxaddrDynamicOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 4),
    _SxaddrDynamicOverflows_Type()
)
sxaddrDynamicOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxaddrDynamicOverflows.setStatus("mandatory")
_SxaddrFlags_Type = Integer32
_SxaddrFlags_Object = MibScalar
sxaddrFlags = _SxaddrFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 5),
    _SxaddrFlags_Type()
)
sxaddrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrFlags.setStatus("mandatory")
_SxaddrMAC_Type = OctetString
_SxaddrMAC_Object = MibScalar
sxaddrMAC = _SxaddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 6),
    _SxaddrMAC_Type()
)
sxaddrMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrMAC.setStatus("mandatory")
_SxaddrPort_Type = Integer32
_SxaddrPort_Object = MibScalar
sxaddrPort = _SxaddrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 7),
    _SxaddrPort_Type()
)
sxaddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrPort.setStatus("mandatory")


class _SxaddrOperation_Type(Integer32):
    """Custom type sxaddrOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
          ("update", 4),
          ("zero-stats", 3))
    )


_SxaddrOperation_Type.__name__ = "Integer32"
_SxaddrOperation_Object = MibScalar
sxaddrOperation = _SxaddrOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 8),
    _SxaddrOperation_Type()
)
sxaddrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrOperation.setStatus("mandatory")
_SxaddrIndex_Type = Integer32
_SxaddrIndex_Object = MibScalar
sxaddrIndex = _SxaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 9),
    _SxaddrIndex_Type()
)
sxaddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrIndex.setStatus("mandatory")
_SxaddrNext_Type = Integer32
_SxaddrNext_Object = MibScalar
sxaddrNext = _SxaddrNext_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 10),
    _SxaddrNext_Type()
)
sxaddrNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrNext.setStatus("mandatory")
_SxaddrAge_Type = TimeTicks
_SxaddrAge_Object = MibScalar
sxaddrAge = _SxaddrAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 11),
    _SxaddrAge_Type()
)
sxaddrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrAge.setStatus("mandatory")
_SxaddrDestAge_Type = TimeTicks
_SxaddrDestAge_Object = MibScalar
sxaddrDestAge = _SxaddrDestAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 12),
    _SxaddrDestAge_Type()
)
sxaddrDestAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrDestAge.setStatus("mandatory")
_SxaddrRxPkts_Type = Counter32
_SxaddrRxPkts_Object = MibScalar
sxaddrRxPkts = _SxaddrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 13),
    _SxaddrRxPkts_Type()
)
sxaddrRxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrRxPkts.setStatus("mandatory")
_SxaddrRxChars_Type = Counter32
_SxaddrRxChars_Object = MibScalar
sxaddrRxChars = _SxaddrRxChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 14),
    _SxaddrRxChars_Type()
)
sxaddrRxChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrRxChars.setStatus("mandatory")
_SxaddrRxMultiPkts_Type = Counter32
_SxaddrRxMultiPkts_Object = MibScalar
sxaddrRxMultiPkts = _SxaddrRxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 15),
    _SxaddrRxMultiPkts_Type()
)
sxaddrRxMultiPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrRxMultiPkts.setStatus("mandatory")
_SxaddrRxFwdPkts_Type = Counter32
_SxaddrRxFwdPkts_Object = MibScalar
sxaddrRxFwdPkts = _SxaddrRxFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 16),
    _SxaddrRxFwdPkts_Type()
)
sxaddrRxFwdPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrRxFwdPkts.setStatus("mandatory")
_SxaddrTxPkts_Type = Counter32
_SxaddrTxPkts_Object = MibScalar
sxaddrTxPkts = _SxaddrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 17),
    _SxaddrTxPkts_Type()
)
sxaddrTxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrTxPkts.setStatus("mandatory")
_SxaddrTxChars_Type = Counter32
_SxaddrTxChars_Object = MibScalar
sxaddrTxChars = _SxaddrTxChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 18),
    _SxaddrTxChars_Type()
)
sxaddrTxChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrTxChars.setStatus("mandatory")
_SxaddrBlockSize_Type = Integer32
_SxaddrBlockSize_Object = MibScalar
sxaddrBlockSize = _SxaddrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 19),
    _SxaddrBlockSize_Type()
)
sxaddrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrBlockSize.setStatus("mandatory")
_SxaddrBlock_Type = OctetString
_SxaddrBlock_Object = MibScalar
sxaddrBlock = _SxaddrBlock_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 20),
    _SxaddrBlock_Type()
)
sxaddrBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxaddrBlock.setStatus("mandatory")
_SxaddrAlarmMAC_Type = OctetString
_SxaddrAlarmMAC_Object = MibScalar
sxaddrAlarmMAC = _SxaddrAlarmMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 5, 21),
    _SxaddrAlarmMAC_Type()
)
sxaddrAlarmMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxaddrAlarmMAC.setStatus("mandatory")
_Sxif_ObjectIdentity = ObjectIdentity
sxif = _Sxif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 6)
)
_SxifTable_Object = MibTable
sxifTable = _SxifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sxifTable.setStatus("mandatory")
_SxifEntry_Object = MibTableRow
sxifEntry = _SxifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1)
)
sxifEntry.setIndexNames(
    (0, "FN10-MIB", "sxifIndex"),
)
if mibBuilder.loadTexts:
    sxifEntry.setStatus("mandatory")
_SxifIndex_Type = Integer32
_SxifIndex_Object = MibTableColumn
sxifIndex = _SxifIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 1),
    _SxifIndex_Type()
)
sxifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifIndex.setStatus("mandatory")
_SxifRxCnt_Type = Integer32
_SxifRxCnt_Object = MibTableColumn
sxifRxCnt = _SxifRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 2),
    _SxifRxCnt_Type()
)
sxifRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifRxCnt.setStatus("mandatory")
_SxifTxCnt_Type = Integer32
_SxifTxCnt_Object = MibTableColumn
sxifTxCnt = _SxifTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 3),
    _SxifTxCnt_Type()
)
sxifTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifTxCnt.setStatus("mandatory")
_SxifThreshold_Type = Integer32
_SxifThreshold_Object = MibTableColumn
sxifThreshold = _SxifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 4),
    _SxifThreshold_Type()
)
sxifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifThreshold.setStatus("mandatory")
_SxifThresholdTime_Type = TimeTicks
_SxifThresholdTime_Object = MibTableColumn
sxifThresholdTime = _SxifThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 5),
    _SxifThresholdTime_Type()
)
sxifThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifThresholdTime.setStatus("mandatory")
_SxifRxQueueThresh_Type = Integer32
_SxifRxQueueThresh_Object = MibTableColumn
sxifRxQueueThresh = _SxifRxQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 6),
    _SxifRxQueueThresh_Type()
)
sxifRxQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifRxQueueThresh.setStatus("mandatory")
_SxifRxQueueThreshTime_Type = TimeTicks
_SxifRxQueueThreshTime_Object = MibTableColumn
sxifRxQueueThreshTime = _SxifRxQueueThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 7),
    _SxifRxQueueThreshTime_Type()
)
sxifRxQueueThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifRxQueueThreshTime.setStatus("mandatory")
_SxifTxStormCnt_Type = Integer32
_SxifTxStormCnt_Object = MibTableColumn
sxifTxStormCnt = _SxifTxStormCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 8),
    _SxifTxStormCnt_Type()
)
sxifTxStormCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifTxStormCnt.setStatus("mandatory")
_SxifTxStormTime_Type = TimeTicks
_SxifTxStormTime_Object = MibTableColumn
sxifTxStormTime = _SxifTxStormTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 9),
    _SxifTxStormTime_Type()
)
sxifTxStormTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifTxStormTime.setStatus("mandatory")


class _SxifFilterFloodSourceSame_Type(Integer32):
    """Custom type sxifFilterFloodSourceSame based on Integer32"""
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


_SxifFilterFloodSourceSame_Type.__name__ = "Integer32"
_SxifFilterFloodSourceSame_Object = MibTableColumn
sxifFilterFloodSourceSame = _SxifFilterFloodSourceSame_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 10),
    _SxifFilterFloodSourceSame_Type()
)
sxifFilterFloodSourceSame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifFilterFloodSourceSame.setStatus("mandatory")


class _SxifFilterAllSourceLearned_Type(Integer32):
    """Custom type sxifFilterAllSourceLearned based on Integer32"""
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


_SxifFilterAllSourceLearned_Type.__name__ = "Integer32"
_SxifFilterAllSourceLearned_Object = MibTableColumn
sxifFilterAllSourceLearned = _SxifFilterAllSourceLearned_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 11),
    _SxifFilterAllSourceLearned_Type()
)
sxifFilterAllSourceLearned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifFilterAllSourceLearned.setStatus("mandatory")


class _SxifFilterNoLearning_Type(Integer32):
    """Custom type sxifFilterNoLearning based on Integer32"""
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


_SxifFilterNoLearning_Type.__name__ = "Integer32"
_SxifFilterNoLearning_Object = MibTableColumn
sxifFilterNoLearning = _SxifFilterNoLearning_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 12),
    _SxifFilterNoLearning_Type()
)
sxifFilterNoLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifFilterNoLearning.setStatus("mandatory")


class _SxifFilterAllDestLearned_Type(Integer32):
    """Custom type sxifFilterAllDestLearned based on Integer32"""
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


_SxifFilterAllDestLearned_Type.__name__ = "Integer32"
_SxifFilterAllDestLearned_Object = MibTableColumn
sxifFilterAllDestLearned = _SxifFilterAllDestLearned_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 13),
    _SxifFilterAllDestLearned_Type()
)
sxifFilterAllDestLearned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifFilterAllDestLearned.setStatus("mandatory")
_SxifCongestTime_Type = TimeTicks
_SxifCongestTime_Object = MibTableColumn
sxifCongestTime = _SxifCongestTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 14),
    _SxifCongestTime_Type()
)
sxifCongestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifCongestTime.setStatus("mandatory")
_SxifQueueTime_Type = TimeTicks
_SxifQueueTime_Object = MibTableColumn
sxifQueueTime = _SxifQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 15),
    _SxifQueueTime_Type()
)
sxifQueueTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifQueueTime.setStatus("mandatory")
_SxifFunction_Type = Integer32
_SxifFunction_Object = MibTableColumn
sxifFunction = _SxifFunction_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 16),
    _SxifFunction_Type()
)
sxifFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifFunction.setStatus("mandatory")
_SxifRxPacket_Type = OctetString
_SxifRxPacket_Object = MibTableColumn
sxifRxPacket = _SxifRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 17),
    _SxifRxPacket_Type()
)
sxifRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifRxPacket.setStatus("mandatory")
_SxifRxHwFCSs_Type = Counter32
_SxifRxHwFCSs_Object = MibTableColumn
sxifRxHwFCSs = _SxifRxHwFCSs_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 18),
    _SxifRxHwFCSs_Type()
)
sxifRxHwFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifRxHwFCSs.setStatus("mandatory")
_SxifRxQueues_Type = Counter32
_SxifRxQueues_Object = MibTableColumn
sxifRxQueues = _SxifRxQueues_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 19),
    _SxifRxQueues_Type()
)
sxifRxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifRxQueues.setStatus("mandatory")
_SxifTxPacket_Type = OctetString
_SxifTxPacket_Object = MibTableColumn
sxifTxPacket = _SxifTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 20),
    _SxifTxPacket_Type()
)
sxifTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifTxPacket.setStatus("mandatory")
_SxifTxStorms_Type = Counter32
_SxifTxStorms_Object = MibTableColumn
sxifTxStorms = _SxifTxStorms_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 21),
    _SxifTxStorms_Type()
)
sxifTxStorms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifTxStorms.setStatus("mandatory")
_SxifTxDests_Type = Counter32
_SxifTxDests_Object = MibTableColumn
sxifTxDests = _SxifTxDests_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 22),
    _SxifTxDests_Type()
)
sxifTxDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifTxDests.setStatus("mandatory")
_SxifLan1_Type = Integer32
_SxifLan1_Object = MibTableColumn
sxifLan1 = _SxifLan1_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 23),
    _SxifLan1_Type()
)
sxifLan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifLan1.setStatus("mandatory")
_SxifLan2_Type = Integer32
_SxifLan2_Object = MibTableColumn
sxifLan2 = _SxifLan2_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 24),
    _SxifLan2_Type()
)
sxifLan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifLan2.setStatus("mandatory")
_SxifLan3_Type = Integer32
_SxifLan3_Object = MibTableColumn
sxifLan3 = _SxifLan3_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 25),
    _SxifLan3_Type()
)
sxifLan3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifLan3.setStatus("mandatory")
_SxifLan4_Type = Integer32
_SxifLan4_Object = MibTableColumn
sxifLan4 = _SxifLan4_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 26),
    _SxifLan4_Type()
)
sxifLan4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifLan4.setStatus("mandatory")
_SxifStatisticsTime_Type = TimeTicks
_SxifStatisticsTime_Object = MibTableColumn
sxifStatisticsTime = _SxifStatisticsTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 27),
    _SxifStatisticsTime_Type()
)
sxifStatisticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifStatisticsTime.setStatus("mandatory")
_SxifIpAddr_Type = IpAddress
_SxifIpAddr_Object = MibTableColumn
sxifIpAddr = _SxifIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 28),
    _SxifIpAddr_Type()
)
sxifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifIpAddr.setStatus("mandatory")
_SxifIpGroupAddr_Type = IpAddress
_SxifIpGroupAddr_Object = MibTableColumn
sxifIpGroupAddr = _SxifIpGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 29),
    _SxifIpGroupAddr_Type()
)
sxifIpGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifIpGroupAddr.setStatus("mandatory")
_SxifForwardedChars_Type = Counter32
_SxifForwardedChars_Object = MibTableColumn
sxifForwardedChars = _SxifForwardedChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 30),
    _SxifForwardedChars_Type()
)
sxifForwardedChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifForwardedChars.setStatus("mandatory")
_SxifFilteredChars_Type = Counter32
_SxifFilteredChars_Object = MibTableColumn
sxifFilteredChars = _SxifFilteredChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 31),
    _SxifFilteredChars_Type()
)
sxifFilteredChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxifFilteredChars.setStatus("mandatory")
_SxifDescr_Type = DisplayString
_SxifDescr_Object = MibTableColumn
sxifDescr = _SxifDescr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 6, 1, 1, 32),
    _SxifDescr_Type()
)
sxifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxifDescr.setStatus("mandatory")
_Sxdot3_ObjectIdentity = ObjectIdentity
sxdot3 = _Sxdot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 7)
)
_Sxdot3Table_Object = MibTable
sxdot3Table = _Sxdot3Table_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sxdot3Table.setStatus("mandatory")
_Sxdot3Entry_Object = MibTableRow
sxdot3Entry = _Sxdot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1)
)
sxdot3Entry.setIndexNames(
    (0, "FN10-MIB", "sxdot3Index"),
)
if mibBuilder.loadTexts:
    sxdot3Entry.setStatus("mandatory")
_Sxdot3Index_Type = Integer32
_Sxdot3Index_Object = MibTableColumn
sxdot3Index = _Sxdot3Index_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 1),
    _Sxdot3Index_Type()
)
sxdot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3Index.setStatus("mandatory")


class _Sxdot3TPLinkOK_Type(Integer32):
    """Custom type sxdot3TPLinkOK based on Integer32"""
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


_Sxdot3TPLinkOK_Type.__name__ = "Integer32"
_Sxdot3TPLinkOK_Object = MibTableColumn
sxdot3TPLinkOK = _Sxdot3TPLinkOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 2),
    _Sxdot3TPLinkOK_Type()
)
sxdot3TPLinkOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3TPLinkOK.setStatus("mandatory")


class _Sxdot3LedOn_Type(Integer32):
    """Custom type sxdot3LedOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("led-off", 2),
          ("led-on", 1))
    )


_Sxdot3LedOn_Type.__name__ = "Integer32"
_Sxdot3LedOn_Object = MibTableColumn
sxdot3LedOn = _Sxdot3LedOn_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 3),
    _Sxdot3LedOn_Type()
)
sxdot3LedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3LedOn.setStatus("mandatory")
_Sxdot3RxCollisions_Type = Counter32
_Sxdot3RxCollisions_Object = MibTableColumn
sxdot3RxCollisions = _Sxdot3RxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 4),
    _Sxdot3RxCollisions_Type()
)
sxdot3RxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3RxCollisions.setStatus("mandatory")
_Sxdot3RxRunts_Type = Counter32
_Sxdot3RxRunts_Object = MibTableColumn
sxdot3RxRunts = _Sxdot3RxRunts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 5),
    _Sxdot3RxRunts_Type()
)
sxdot3RxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3RxRunts.setStatus("mandatory")
_Sxdot3RxLateColls_Type = Counter32
_Sxdot3RxLateColls_Object = MibTableColumn
sxdot3RxLateColls = _Sxdot3RxLateColls_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 6),
    _Sxdot3RxLateColls_Type()
)
sxdot3RxLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3RxLateColls.setStatus("mandatory")
_Sxdot3TxJabbers_Type = Counter32
_Sxdot3TxJabbers_Object = MibTableColumn
sxdot3TxJabbers = _Sxdot3TxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 7),
    _Sxdot3TxJabbers_Type()
)
sxdot3TxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3TxJabbers.setStatus("mandatory")
_Sxdot3TxBabbles_Type = Counter32
_Sxdot3TxBabbles_Object = MibTableColumn
sxdot3TxBabbles = _Sxdot3TxBabbles_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 8),
    _Sxdot3TxBabbles_Type()
)
sxdot3TxBabbles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3TxBabbles.setStatus("mandatory")
_Sxdot3TxCollisions_Type = Counter32
_Sxdot3TxCollisions_Object = MibTableColumn
sxdot3TxCollisions = _Sxdot3TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 9),
    _Sxdot3TxCollisions_Type()
)
sxdot3TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3TxCollisions.setStatus("mandatory")
_Sxdot3RxErrInfo_Type = OctetString
_Sxdot3RxErrInfo_Object = MibTableColumn
sxdot3RxErrInfo = _Sxdot3RxErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 10),
    _Sxdot3RxErrInfo_Type()
)
sxdot3RxErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3RxErrInfo.setStatus("mandatory")
_Sxdot3TxErrInfo_Type = OctetString
_Sxdot3TxErrInfo_Object = MibTableColumn
sxdot3TxErrInfo = _Sxdot3TxErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 11),
    _Sxdot3TxErrInfo_Type()
)
sxdot3TxErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3TxErrInfo.setStatus("mandatory")


class _Sxdot3FuseOkay_Type(Integer32):
    """Custom type sxdot3FuseOkay based on Integer32"""
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


_Sxdot3FuseOkay_Type.__name__ = "Integer32"
_Sxdot3FuseOkay_Object = MibTableColumn
sxdot3FuseOkay = _Sxdot3FuseOkay_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 12),
    _Sxdot3FuseOkay_Type()
)
sxdot3FuseOkay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdot3FuseOkay.setStatus("mandatory")


class _Sxdot3SpeedSelection_Type(Integer32):
    """Custom type sxdot3SpeedSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-100mbit", 2),
          ("speed-10mbit", 1))
    )


_Sxdot3SpeedSelection_Type.__name__ = "Integer32"
_Sxdot3SpeedSelection_Object = MibTableColumn
sxdot3SpeedSelection = _Sxdot3SpeedSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 7, 1, 1, 13),
    _Sxdot3SpeedSelection_Type()
)
sxdot3SpeedSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxdot3SpeedSelection.setStatus("mandatory")
_Sxuart_ObjectIdentity = ObjectIdentity
sxuart = _Sxuart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 8)
)
_SxuartTable_Object = MibTable
sxuartTable = _SxuartTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1)
)
if mibBuilder.loadTexts:
    sxuartTable.setStatus("mandatory")
_SxuartEntry_Object = MibTableRow
sxuartEntry = _SxuartEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1, 1)
)
sxuartEntry.setIndexNames(
    (0, "FN10-MIB", "sxuartIndex"),
)
if mibBuilder.loadTexts:
    sxuartEntry.setStatus("mandatory")
_SxuartIndex_Type = Integer32
_SxuartIndex_Object = MibTableColumn
sxuartIndex = _SxuartIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1, 1, 1),
    _SxuartIndex_Type()
)
sxuartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxuartIndex.setStatus("mandatory")


class _SxuartBaud_Type(Integer32):
    """Custom type sxuartBaud based on Integer32"""
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


_SxuartBaud_Type.__name__ = "Integer32"
_SxuartBaud_Object = MibTableColumn
sxuartBaud = _SxuartBaud_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1, 1, 2),
    _SxuartBaud_Type()
)
sxuartBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxuartBaud.setStatus("mandatory")
_SxuartAlignmentErrors_Type = Counter32
_SxuartAlignmentErrors_Object = MibTableColumn
sxuartAlignmentErrors = _SxuartAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1, 1, 3),
    _SxuartAlignmentErrors_Type()
)
sxuartAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxuartAlignmentErrors.setStatus("mandatory")
_SxuartOverrunErrors_Type = Counter32
_SxuartOverrunErrors_Object = MibTableColumn
sxuartOverrunErrors = _SxuartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 8, 1, 1, 4),
    _SxuartOverrunErrors_Type()
)
sxuartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxuartOverrunErrors.setStatus("mandatory")
_Sxfilter_ObjectIdentity = ObjectIdentity
sxfilter = _Sxfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 9)
)
_SxfilterMaxCount_Type = Integer32
_SxfilterMaxCount_Object = MibScalar
sxfilterMaxCount = _SxfilterMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 1),
    _SxfilterMaxCount_Type()
)
sxfilterMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterMaxCount.setStatus("mandatory")
_SxfilterCurrentCount_Type = Integer32
_SxfilterCurrentCount_Object = MibScalar
sxfilterCurrentCount = _SxfilterCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 2),
    _SxfilterCurrentCount_Type()
)
sxfilterCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterCurrentCount.setStatus("mandatory")
_SxfilterDeleteID_Type = Integer32
_SxfilterDeleteID_Object = MibScalar
sxfilterDeleteID = _SxfilterDeleteID_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 3),
    _SxfilterDeleteID_Type()
)
sxfilterDeleteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterDeleteID.setStatus("mandatory")
_SxfilterNextID_Type = Integer32
_SxfilterNextID_Object = MibScalar
sxfilterNextID = _SxfilterNextID_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 4),
    _SxfilterNextID_Type()
)
sxfilterNextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterNextID.setStatus("mandatory")
_SxfilterAddID_Type = Integer32
_SxfilterAddID_Object = MibScalar
sxfilterAddID = _SxfilterAddID_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 5),
    _SxfilterAddID_Type()
)
sxfilterAddID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterAddID.setStatus("mandatory")
_SxfilterAddIndex_Type = Integer32
_SxfilterAddIndex_Object = MibScalar
sxfilterAddIndex = _SxfilterAddIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 6),
    _SxfilterAddIndex_Type()
)
sxfilterAddIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterAddIndex.setStatus("mandatory")
_SxfilterTable_Object = MibTable
sxfilterTable = _SxfilterTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7)
)
if mibBuilder.loadTexts:
    sxfilterTable.setStatus("mandatory")
_SxfilterEntry_Object = MibTableRow
sxfilterEntry = _SxfilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1)
)
sxfilterEntry.setIndexNames(
    (0, "FN10-MIB", "sxfilterIndex"),
)
if mibBuilder.loadTexts:
    sxfilterEntry.setStatus("mandatory")
_SxfilterIndex_Type = Integer32
_SxfilterIndex_Object = MibTableColumn
sxfilterIndex = _SxfilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 1),
    _SxfilterIndex_Type()
)
sxfilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterIndex.setStatus("mandatory")
_SxfilterID_Type = Integer32
_SxfilterID_Object = MibTableColumn
sxfilterID = _SxfilterID_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 2),
    _SxfilterID_Type()
)
sxfilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterID.setStatus("mandatory")
_SxfilterPortNo_Type = Integer32
_SxfilterPortNo_Object = MibTableColumn
sxfilterPortNo = _SxfilterPortNo_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 3),
    _SxfilterPortNo_Type()
)
sxfilterPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterPortNo.setStatus("mandatory")
_SxfilterComboType_Type = Integer32
_SxfilterComboType_Object = MibTableColumn
sxfilterComboType = _SxfilterComboType_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 4),
    _SxfilterComboType_Type()
)
sxfilterComboType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterComboType.setStatus("mandatory")
_SxfilterFlags_Type = Integer32
_SxfilterFlags_Object = MibTableColumn
sxfilterFlags = _SxfilterFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 5),
    _SxfilterFlags_Type()
)
sxfilterFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterFlags.setStatus("mandatory")


class _SxfilterFrame_Type(Integer32):
    """Custom type sxfilterFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any-ethernet", 2),
          ("any-llc", 1))
    )


_SxfilterFrame_Type.__name__ = "Integer32"
_SxfilterFrame_Object = MibTableColumn
sxfilterFrame = _SxfilterFrame_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 6),
    _SxfilterFrame_Type()
)
sxfilterFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterFrame.setStatus("mandatory")
_SxfilterSource_Type = OctetString
_SxfilterSource_Object = MibTableColumn
sxfilterSource = _SxfilterSource_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 7),
    _SxfilterSource_Type()
)
sxfilterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterSource.setStatus("mandatory")
_SxfilterSourceEnd_Type = OctetString
_SxfilterSourceEnd_Object = MibTableColumn
sxfilterSourceEnd = _SxfilterSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 8),
    _SxfilterSourceEnd_Type()
)
sxfilterSourceEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterSourceEnd.setStatus("mandatory")
_SxfilterDest_Type = OctetString
_SxfilterDest_Object = MibTableColumn
sxfilterDest = _SxfilterDest_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 9),
    _SxfilterDest_Type()
)
sxfilterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterDest.setStatus("mandatory")
_SxfilterDestEnd_Type = OctetString
_SxfilterDestEnd_Object = MibTableColumn
sxfilterDestEnd = _SxfilterDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 10),
    _SxfilterDestEnd_Type()
)
sxfilterDestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterDestEnd.setStatus("mandatory")
_SxfilterSourceMask_Type = OctetString
_SxfilterSourceMask_Object = MibTableColumn
sxfilterSourceMask = _SxfilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 11),
    _SxfilterSourceMask_Type()
)
sxfilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterSourceMask.setStatus("mandatory")
_SxfilterDestMask_Type = OctetString
_SxfilterDestMask_Object = MibTableColumn
sxfilterDestMask = _SxfilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 12),
    _SxfilterDestMask_Type()
)
sxfilterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterDestMask.setStatus("mandatory")
_SxfilterSrcLan_Type = Integer32
_SxfilterSrcLan_Object = MibTableColumn
sxfilterSrcLan = _SxfilterSrcLan_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 13),
    _SxfilterSrcLan_Type()
)
sxfilterSrcLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterSrcLan.setStatus("mandatory")
_SxfilterOffset_Type = Integer32
_SxfilterOffset_Object = MibTableColumn
sxfilterOffset = _SxfilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 14),
    _SxfilterOffset_Type()
)
sxfilterOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterOffset.setStatus("mandatory")
_SxfilterField_Type = OctetString
_SxfilterField_Object = MibTableColumn
sxfilterField = _SxfilterField_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 15),
    _SxfilterField_Type()
)
sxfilterField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterField.setStatus("mandatory")
_SxfilterMask_Type = OctetString
_SxfilterMask_Object = MibTableColumn
sxfilterMask = _SxfilterMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 16),
    _SxfilterMask_Type()
)
sxfilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterMask.setStatus("mandatory")
_SxfilterThreshold_Type = Integer32
_SxfilterThreshold_Object = MibTableColumn
sxfilterThreshold = _SxfilterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 17),
    _SxfilterThreshold_Type()
)
sxfilterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterThreshold.setStatus("mandatory")
_SxfilterThreshTime_Type = Integer32
_SxfilterThreshTime_Object = MibTableColumn
sxfilterThreshTime = _SxfilterThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 18),
    _SxfilterThreshTime_Type()
)
sxfilterThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxfilterThreshTime.setStatus("mandatory")


class _SxfilterThreshFlag_Type(Integer32):
    """Custom type sxfilterThreshFlag based on Integer32"""
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


_SxfilterThreshFlag_Type.__name__ = "Integer32"
_SxfilterThreshFlag_Object = MibTableColumn
sxfilterThreshFlag = _SxfilterThreshFlag_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 19),
    _SxfilterThreshFlag_Type()
)
sxfilterThreshFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterThreshFlag.setStatus("mandatory")
_SxfilterPktCnts_Type = Counter32
_SxfilterPktCnts_Object = MibTableColumn
sxfilterPktCnts = _SxfilterPktCnts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 20),
    _SxfilterPktCnts_Type()
)
sxfilterPktCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterPktCnts.setStatus("mandatory")
_SxfilterLastSrc_Type = OctetString
_SxfilterLastSrc_Object = MibTableColumn
sxfilterLastSrc = _SxfilterLastSrc_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 21),
    _SxfilterLastSrc_Type()
)
sxfilterLastSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterLastSrc.setStatus("mandatory")
_SxfilterByteCnts_Type = Counter32
_SxfilterByteCnts_Object = MibTableColumn
sxfilterByteCnts = _SxfilterByteCnts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 9, 7, 1, 22),
    _SxfilterByteCnts_Type()
)
sxfilterByteCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxfilterByteCnts.setStatus("mandatory")
_Sxdebug_ObjectIdentity = ObjectIdentity
sxdebug = _Sxdebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 10)
)
_SxdebugStringID_Type = Integer32
_SxdebugStringID_Object = MibScalar
sxdebugStringID = _SxdebugStringID_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 1),
    _SxdebugStringID_Type()
)
sxdebugStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdebugStringID.setStatus("mandatory")
_SxdebugString_Type = OctetString
_SxdebugString_Object = MibScalar
sxdebugString = _SxdebugString_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 2),
    _SxdebugString_Type()
)
sxdebugString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdebugString.setStatus("mandatory")
_SxdebugTable_Object = MibTable
sxdebugTable = _SxdebugTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3)
)
if mibBuilder.loadTexts:
    sxdebugTable.setStatus("mandatory")
_SxdebugEntry_Object = MibTableRow
sxdebugEntry = _SxdebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1)
)
sxdebugEntry.setIndexNames(
    (0, "FN10-MIB", "sxdebugIndex"),
)
if mibBuilder.loadTexts:
    sxdebugEntry.setStatus("mandatory")
_SxdebugIndex_Type = Integer32
_SxdebugIndex_Object = MibTableColumn
sxdebugIndex = _SxdebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1, 1),
    _SxdebugIndex_Type()
)
sxdebugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxdebugIndex.setStatus("mandatory")


class _SxdebugOperation_Type(Integer32):
    """Custom type sxdebugOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("examine", 1),
          ("modify", 2))
    )


_SxdebugOperation_Type.__name__ = "Integer32"
_SxdebugOperation_Object = MibTableColumn
sxdebugOperation = _SxdebugOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1, 2),
    _SxdebugOperation_Type()
)
sxdebugOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxdebugOperation.setStatus("mandatory")
_SxdebugBase_Type = Integer32
_SxdebugBase_Object = MibTableColumn
sxdebugBase = _SxdebugBase_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1, 3),
    _SxdebugBase_Type()
)
sxdebugBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxdebugBase.setStatus("mandatory")
_SxdebugLength_Type = Integer32
_SxdebugLength_Object = MibTableColumn
sxdebugLength = _SxdebugLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1, 4),
    _SxdebugLength_Type()
)
sxdebugLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxdebugLength.setStatus("mandatory")
_SxdebugData_Type = OctetString
_SxdebugData_Object = MibTableColumn
sxdebugData = _SxdebugData_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 10, 3, 1, 5),
    _SxdebugData_Type()
)
sxdebugData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxdebugData.setStatus("mandatory")
_Sxlpbk_ObjectIdentity = ObjectIdentity
sxlpbk = _Sxlpbk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 11)
)
_SxlpbkTable_Object = MibTable
sxlpbkTable = _SxlpbkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1)
)
if mibBuilder.loadTexts:
    sxlpbkTable.setStatus("mandatory")
_SxlpbkEntry_Object = MibTableRow
sxlpbkEntry = _SxlpbkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1)
)
sxlpbkEntry.setIndexNames(
    (0, "FN10-MIB", "sxlpbkIndex"),
)
if mibBuilder.loadTexts:
    sxlpbkEntry.setStatus("mandatory")
_SxlpbkIndex_Type = Integer32
_SxlpbkIndex_Object = MibTableColumn
sxlpbkIndex = _SxlpbkIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 1),
    _SxlpbkIndex_Type()
)
sxlpbkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkIndex.setStatus("mandatory")


class _SxlpbkOperation_Type(Integer32):
    """Custom type sxlpbkOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback-local", 2),
          ("loopback-off", 1),
          ("loopback-remote", 3))
    )


_SxlpbkOperation_Type.__name__ = "Integer32"
_SxlpbkOperation_Object = MibTableColumn
sxlpbkOperation = _SxlpbkOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 2),
    _SxlpbkOperation_Type()
)
sxlpbkOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkOperation.setStatus("mandatory")
_SxlpbkDestAddr_Type = OctetString
_SxlpbkDestAddr_Object = MibTableColumn
sxlpbkDestAddr = _SxlpbkDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 3),
    _SxlpbkDestAddr_Type()
)
sxlpbkDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkDestAddr.setStatus("mandatory")
_SxlpbkPktNum_Type = Integer32
_SxlpbkPktNum_Object = MibTableColumn
sxlpbkPktNum = _SxlpbkPktNum_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 4),
    _SxlpbkPktNum_Type()
)
sxlpbkPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkPktNum.setStatus("mandatory")
_SxlpbkInterval_Type = TimeTicks
_SxlpbkInterval_Object = MibTableColumn
sxlpbkInterval = _SxlpbkInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 5),
    _SxlpbkInterval_Type()
)
sxlpbkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkInterval.setStatus("mandatory")
_SxlpbkPktLength_Type = Integer32
_SxlpbkPktLength_Object = MibTableColumn
sxlpbkPktLength = _SxlpbkPktLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 6),
    _SxlpbkPktLength_Type()
)
sxlpbkPktLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkPktLength.setStatus("mandatory")
_SxlpbkIncrements_Type = Integer32
_SxlpbkIncrements_Object = MibTableColumn
sxlpbkIncrements = _SxlpbkIncrements_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 7),
    _SxlpbkIncrements_Type()
)
sxlpbkIncrements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxlpbkIncrements.setStatus("mandatory")
_SxlpbkGoods_Type = Counter32
_SxlpbkGoods_Object = MibTableColumn
sxlpbkGoods = _SxlpbkGoods_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 8),
    _SxlpbkGoods_Type()
)
sxlpbkGoods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkGoods.setStatus("mandatory")
_SxlpbkErrorNoReceives_Type = Counter32
_SxlpbkErrorNoReceives_Object = MibTableColumn
sxlpbkErrorNoReceives = _SxlpbkErrorNoReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 9),
    _SxlpbkErrorNoReceives_Type()
)
sxlpbkErrorNoReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorNoReceives.setStatus("mandatory")
_SxlpbkErrorBadReceives_Type = Counter32
_SxlpbkErrorBadReceives_Object = MibTableColumn
sxlpbkErrorBadReceives = _SxlpbkErrorBadReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 10),
    _SxlpbkErrorBadReceives_Type()
)
sxlpbkErrorBadReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorBadReceives.setStatus("mandatory")
_SxlpbkErrorSize_Type = Integer32
_SxlpbkErrorSize_Object = MibTableColumn
sxlpbkErrorSize = _SxlpbkErrorSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 11),
    _SxlpbkErrorSize_Type()
)
sxlpbkErrorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorSize.setStatus("mandatory")
_SxlpbkErrorSent_Type = OctetString
_SxlpbkErrorSent_Object = MibTableColumn
sxlpbkErrorSent = _SxlpbkErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 12),
    _SxlpbkErrorSent_Type()
)
sxlpbkErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorSent.setStatus("mandatory")
_SxlpbkErrorReceived_Type = OctetString
_SxlpbkErrorReceived_Object = MibTableColumn
sxlpbkErrorReceived = _SxlpbkErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 13),
    _SxlpbkErrorReceived_Type()
)
sxlpbkErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorReceived.setStatus("mandatory")
_SxlpbkErrorOffset_Type = Integer32
_SxlpbkErrorOffset_Object = MibTableColumn
sxlpbkErrorOffset = _SxlpbkErrorOffset_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 11, 1, 1, 14),
    _SxlpbkErrorOffset_Type()
)
sxlpbkErrorOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxlpbkErrorOffset.setStatus("mandatory")
_Sxproto_ObjectIdentity = ObjectIdentity
sxproto = _Sxproto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 12)
)
_SxprotoTable_Object = MibTable
sxprotoTable = _SxprotoTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1)
)
if mibBuilder.loadTexts:
    sxprotoTable.setStatus("mandatory")
_SxprotoEntry_Object = MibTableRow
sxprotoEntry = _SxprotoEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1)
)
sxprotoEntry.setIndexNames(
    (0, "FN10-MIB", "sxprotoIfIndex"),
)
if mibBuilder.loadTexts:
    sxprotoEntry.setStatus("mandatory")
_SxprotoIfIndex_Type = Integer32
_SxprotoIfIndex_Object = MibTableColumn
sxprotoIfIndex = _SxprotoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 1),
    _SxprotoIfIndex_Type()
)
sxprotoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxprotoIfIndex.setStatus("mandatory")


class _SxprotoBridge_Type(Integer32):
    """Custom type sxprotoBridge based on Integer32"""
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


_SxprotoBridge_Type.__name__ = "Integer32"
_SxprotoBridge_Object = MibTableColumn
sxprotoBridge = _SxprotoBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 2),
    _SxprotoBridge_Type()
)
sxprotoBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxprotoBridge.setStatus("mandatory")


class _SxprotoSuppressBpdu_Type(Integer32):
    """Custom type sxprotoSuppressBpdu based on Integer32"""
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


_SxprotoSuppressBpdu_Type.__name__ = "Integer32"
_SxprotoSuppressBpdu_Object = MibTableColumn
sxprotoSuppressBpdu = _SxprotoSuppressBpdu_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 3),
    _SxprotoSuppressBpdu_Type()
)
sxprotoSuppressBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxprotoSuppressBpdu.setStatus("mandatory")


class _SxprotoRipListen_Type(Integer32):
    """Custom type sxprotoRipListen based on Integer32"""
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


_SxprotoRipListen_Type.__name__ = "Integer32"
_SxprotoRipListen_Object = MibTableColumn
sxprotoRipListen = _SxprotoRipListen_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 4),
    _SxprotoRipListen_Type()
)
sxprotoRipListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxprotoRipListen.setStatus("mandatory")


class _SxprotoTrunking_Type(Integer32):
    """Custom type sxprotoTrunking based on Integer32"""
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


_SxprotoTrunking_Type.__name__ = "Integer32"
_SxprotoTrunking_Object = MibTableColumn
sxprotoTrunking = _SxprotoTrunking_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 5),
    _SxprotoTrunking_Type()
)
sxprotoTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxprotoTrunking.setStatus("mandatory")


class _SxsprotoCollisionRelief_Type(Integer32):
    """Custom type sxsprotoCollisionRelief based on Integer32"""
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


_SxsprotoCollisionRelief_Type.__name__ = "Integer32"
_SxsprotoCollisionRelief_Object = MibTableColumn
sxsprotoCollisionRelief = _SxsprotoCollisionRelief_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 12, 1, 1, 6),
    _SxsprotoCollisionRelief_Type()
)
sxsprotoCollisionRelief.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxsprotoCollisionRelief.setStatus("mandatory")
_Sxtrunk_ObjectIdentity = ObjectIdentity
sxtrunk = _Sxtrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 13)
)
_SxtrunkTable_Object = MibTable
sxtrunkTable = _SxtrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1)
)
if mibBuilder.loadTexts:
    sxtrunkTable.setStatus("mandatory")
_SxtrunkEntry_Object = MibTableRow
sxtrunkEntry = _SxtrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1)
)
sxtrunkEntry.setIndexNames(
    (0, "FN10-MIB", "sxtrunkIfIndex"),
)
if mibBuilder.loadTexts:
    sxtrunkEntry.setStatus("mandatory")
_SxtrunkIfIndex_Type = Integer32
_SxtrunkIfIndex_Object = MibTableColumn
sxtrunkIfIndex = _SxtrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 1),
    _SxtrunkIfIndex_Type()
)
sxtrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkIfIndex.setStatus("mandatory")


class _SxtrunkState_Type(Integer32):
    """Custom type sxtrunkState based on Integer32"""
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
        *(("broken", 7),
          ("closed", 2),
          ("helddown", 6),
          ("joined", 4),
          ("off", 1),
          ("oneway", 3),
          ("perturbed", 5))
    )


_SxtrunkState_Type.__name__ = "Integer32"
_SxtrunkState_Object = MibTableColumn
sxtrunkState = _SxtrunkState_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 2),
    _SxtrunkState_Type()
)
sxtrunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkState.setStatus("mandatory")
_SxtrunkRemoteBridgeAddr_Type = OctetString
_SxtrunkRemoteBridgeAddr_Object = MibTableColumn
sxtrunkRemoteBridgeAddr = _SxtrunkRemoteBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 3),
    _SxtrunkRemoteBridgeAddr_Type()
)
sxtrunkRemoteBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkRemoteBridgeAddr.setStatus("mandatory")
_SxtrunkRemoteIp_Type = IpAddress
_SxtrunkRemoteIp_Object = MibTableColumn
sxtrunkRemoteIp = _SxtrunkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 4),
    _SxtrunkRemoteIp_Type()
)
sxtrunkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkRemoteIp.setStatus("mandatory")


class _SxtrunkLastError_Type(Integer32):
    """Custom type sxtrunkLastError based on Integer32"""
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


_SxtrunkLastError_Type.__name__ = "Integer32"
_SxtrunkLastError_Object = MibTableColumn
sxtrunkLastError = _SxtrunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 5),
    _SxtrunkLastError_Type()
)
sxtrunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkLastError.setStatus("mandatory")
_SxtrunkLinkOrdinal_Type = Integer32
_SxtrunkLinkOrdinal_Object = MibTableColumn
sxtrunkLinkOrdinal = _SxtrunkLinkOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 6),
    _SxtrunkLinkOrdinal_Type()
)
sxtrunkLinkOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkLinkOrdinal.setStatus("mandatory")
_SxtrunkLinkCount_Type = Integer32
_SxtrunkLinkCount_Object = MibTableColumn
sxtrunkLinkCount = _SxtrunkLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 7),
    _SxtrunkLinkCount_Type()
)
sxtrunkLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkLinkCount.setStatus("mandatory")
_SxtrunkLastChange_Type = Integer32
_SxtrunkLastChange_Object = MibTableColumn
sxtrunkLastChange = _SxtrunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 13, 1, 1, 8),
    _SxtrunkLastChange_Type()
)
sxtrunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrunkLastChange.setStatus("mandatory")
_Sxworkgroup_ObjectIdentity = ObjectIdentity
sxworkgroup = _Sxworkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 14)
)
_SxWorkGroupNextNumber_Type = Integer32
_SxWorkGroupNextNumber_Object = MibScalar
sxWorkGroupNextNumber = _SxWorkGroupNextNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 1),
    _SxWorkGroupNextNumber_Type()
)
sxWorkGroupNextNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxWorkGroupNextNumber.setStatus("mandatory")
_SxWorkGroupCurrentCount_Type = Integer32
_SxWorkGroupCurrentCount_Object = MibScalar
sxWorkGroupCurrentCount = _SxWorkGroupCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 2),
    _SxWorkGroupCurrentCount_Type()
)
sxWorkGroupCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxWorkGroupCurrentCount.setStatus("mandatory")
_SxWorkGroupMaxCount_Type = Integer32
_SxWorkGroupMaxCount_Object = MibScalar
sxWorkGroupMaxCount = _SxWorkGroupMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 3),
    _SxWorkGroupMaxCount_Type()
)
sxWorkGroupMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxWorkGroupMaxCount.setStatus("mandatory")
_SxWorkGroupTable_Object = MibTable
sxWorkGroupTable = _SxWorkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4)
)
if mibBuilder.loadTexts:
    sxWorkGroupTable.setStatus("mandatory")
_SxWorkGroupEntry_Object = MibTableRow
sxWorkGroupEntry = _SxWorkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1)
)
sxWorkGroupEntry.setIndexNames(
    (0, "FN10-MIB", "sxWorkGroupNumber"),
)
if mibBuilder.loadTexts:
    sxWorkGroupEntry.setStatus("mandatory")
_SxWorkGroupNumber_Type = Integer32
_SxWorkGroupNumber_Object = MibTableColumn
sxWorkGroupNumber = _SxWorkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 1),
    _SxWorkGroupNumber_Type()
)
sxWorkGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupNumber.setStatus("mandatory")
_SxWorkGroupName_Type = DisplayString
_SxWorkGroupName_Object = MibTableColumn
sxWorkGroupName = _SxWorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 2),
    _SxWorkGroupName_Type()
)
sxWorkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupName.setStatus("mandatory")
_SxWorkGroupPorts_Type = OctetString
_SxWorkGroupPorts_Object = MibTableColumn
sxWorkGroupPorts = _SxWorkGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 3),
    _SxWorkGroupPorts_Type()
)
sxWorkGroupPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupPorts.setStatus("mandatory")


class _SxWorkGroupType_Type(Integer32):
    """Custom type sxWorkGroupType based on Integer32"""
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
        *(("all", 3),
          ("invalid", 4),
          ("ip", 1),
          ("ipx", 2))
    )


_SxWorkGroupType_Type.__name__ = "Integer32"
_SxWorkGroupType_Object = MibTableColumn
sxWorkGroupType = _SxWorkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 4),
    _SxWorkGroupType_Type()
)
sxWorkGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupType.setStatus("mandatory")
_SxWorkGroupIpAddress_Type = IpAddress
_SxWorkGroupIpAddress_Object = MibTableColumn
sxWorkGroupIpAddress = _SxWorkGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 5),
    _SxWorkGroupIpAddress_Type()
)
sxWorkGroupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupIpAddress.setStatus("mandatory")
_SxWorkGroupIpMask_Type = IpAddress
_SxWorkGroupIpMask_Object = MibTableColumn
sxWorkGroupIpMask = _SxWorkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 6),
    _SxWorkGroupIpMask_Type()
)
sxWorkGroupIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupIpMask.setStatus("mandatory")
_SxWorkGroupIpxNetwork_Type = OctetString
_SxWorkGroupIpxNetwork_Object = MibTableColumn
sxWorkGroupIpxNetwork = _SxWorkGroupIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 14, 4, 1, 7),
    _SxWorkGroupIpxNetwork_Type()
)
sxWorkGroupIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxWorkGroupIpxNetwork.setStatus("mandatory")
_SxtrapMgt_ObjectIdentity = ObjectIdentity
sxtrapMgt = _SxtrapMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 2, 15)
)
_SxtrapControlTable_Object = MibTable
sxtrapControlTable = _SxtrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1)
)
if mibBuilder.loadTexts:
    sxtrapControlTable.setStatus("mandatory")
_SxtrapControl_Object = MibTableRow
sxtrapControl = _SxtrapControl_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1, 1)
)
sxtrapControl.setIndexNames(
    (0, "FN10-MIB", "sxtrapIndex"),
)
if mibBuilder.loadTexts:
    sxtrapControl.setStatus("mandatory")
_SxtrapIndex_Type = Integer32
_SxtrapIndex_Object = MibTableColumn
sxtrapIndex = _SxtrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1, 1, 1),
    _SxtrapIndex_Type()
)
sxtrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapIndex.setStatus("mandatory")


class _SxtrapEnabled_Type(Integer32):
    """Custom type sxtrapEnabled based on Integer32"""
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


_SxtrapEnabled_Type.__name__ = "Integer32"
_SxtrapEnabled_Object = MibTableColumn
sxtrapEnabled = _SxtrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1, 1, 2),
    _SxtrapEnabled_Type()
)
sxtrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapEnabled.setStatus("mandatory")


class _SxtrapSeverity_Type(Integer32):
    """Custom type sxtrapSeverity based on Integer32"""
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


_SxtrapSeverity_Type.__name__ = "Integer32"
_SxtrapSeverity_Object = MibTableColumn
sxtrapSeverity = _SxtrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1, 1, 3),
    _SxtrapSeverity_Type()
)
sxtrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapSeverity.setStatus("mandatory")
_SxtrapText_Type = DisplayString
_SxtrapText_Object = MibTableColumn
sxtrapText = _SxtrapText_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 1, 1, 4),
    _SxtrapText_Type()
)
sxtrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapText.setStatus("mandatory")
_SxtrapSeverityControlTable_Object = MibTable
sxtrapSeverityControlTable = _SxtrapSeverityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 2)
)
if mibBuilder.loadTexts:
    sxtrapSeverityControlTable.setStatus("mandatory")
_SxtrapSeverityControl_Object = MibTableRow
sxtrapSeverityControl = _SxtrapSeverityControl_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 2, 1)
)
sxtrapSeverityControl.setIndexNames(
    (0, "FN10-MIB", "sxtrapSeverityControlSeverity"),
)
if mibBuilder.loadTexts:
    sxtrapSeverityControl.setStatus("mandatory")


class _SxtrapSeverityControlSeverity_Type(Integer32):
    """Custom type sxtrapSeverityControlSeverity based on Integer32"""
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


_SxtrapSeverityControlSeverity_Type.__name__ = "Integer32"
_SxtrapSeverityControlSeverity_Object = MibTableColumn
sxtrapSeverityControlSeverity = _SxtrapSeverityControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 2, 1, 1),
    _SxtrapSeverityControlSeverity_Type()
)
sxtrapSeverityControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapSeverityControlSeverity.setStatus("mandatory")


class _SxtrapSeverityEnable_Type(Integer32):
    """Custom type sxtrapSeverityEnable based on Integer32"""
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


_SxtrapSeverityEnable_Type.__name__ = "Integer32"
_SxtrapSeverityEnable_Object = MibTableColumn
sxtrapSeverityEnable = _SxtrapSeverityEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 2, 1, 2),
    _SxtrapSeverityEnable_Type()
)
sxtrapSeverityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapSeverityEnable.setStatus("mandatory")


class _SxtrapIncludeText_Type(Integer32):
    """Custom type sxtrapIncludeText based on Integer32"""
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


_SxtrapIncludeText_Type.__name__ = "Integer32"
_SxtrapIncludeText_Object = MibScalar
sxtrapIncludeText = _SxtrapIncludeText_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 3),
    _SxtrapIncludeText_Type()
)
sxtrapIncludeText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapIncludeText.setStatus("mandatory")
_SxtrapTime_Type = TimeTicks
_SxtrapTime_Object = MibScalar
sxtrapTime = _SxtrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 4),
    _SxtrapTime_Type()
)
sxtrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapTime.setStatus("mandatory")
_SxtrapRetry_Type = Integer32
_SxtrapRetry_Object = MibScalar
sxtrapRetry = _SxtrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 5),
    _SxtrapRetry_Type()
)
sxtrapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxtrapRetry.setStatus("mandatory")
_SxtrapEntryNumber_Type = Integer32
_SxtrapEntryNumber_Object = MibScalar
sxtrapEntryNumber = _SxtrapEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 6),
    _SxtrapEntryNumber_Type()
)
sxtrapEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapEntryNumber.setStatus("mandatory")
_SxtrapTable_Object = MibTable
sxtrapTable = _SxtrapTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7)
)
if mibBuilder.loadTexts:
    sxtrapTable.setStatus("mandatory")
_SxtrapEntry_Object = MibTableRow
sxtrapEntry = _SxtrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1)
)
sxtrapEntry.setIndexNames(
    (0, "FN10-MIB", "sxtrapEntryIndex"),
)
if mibBuilder.loadTexts:
    sxtrapEntry.setStatus("mandatory")
_SxtrapEntryIndex_Type = Integer32
_SxtrapEntryIndex_Object = MibTableColumn
sxtrapEntryIndex = _SxtrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1, 1),
    _SxtrapEntryIndex_Type()
)
sxtrapEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapEntryIndex.setStatus("mandatory")
_SxtrapEntryTimeStamp_Type = TimeTicks
_SxtrapEntryTimeStamp_Object = MibTableColumn
sxtrapEntryTimeStamp = _SxtrapEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1, 2),
    _SxtrapEntryTimeStamp_Type()
)
sxtrapEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapEntryTimeStamp.setStatus("mandatory")
_SxtrapEntryText_Type = DisplayString
_SxtrapEntryText_Object = MibTableColumn
sxtrapEntryText = _SxtrapEntryText_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1, 3),
    _SxtrapEntryText_Type()
)
sxtrapEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapEntryText.setStatus("mandatory")
_SxtrapNumber_Type = Integer32
_SxtrapNumber_Object = MibTableColumn
sxtrapNumber = _SxtrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1, 4),
    _SxtrapNumber_Type()
)
sxtrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapNumber.setStatus("mandatory")


class _SxtrapEntrySeverity_Type(Integer32):
    """Custom type sxtrapEntrySeverity based on Integer32"""
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


_SxtrapEntrySeverity_Type.__name__ = "Integer32"
_SxtrapEntrySeverity_Object = MibTableColumn
sxtrapEntrySeverity = _SxtrapEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 2, 15, 7, 1, 5),
    _SxtrapEntrySeverity_Type()
)
sxtrapEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxtrapEntrySeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sxTempOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 1)
)
sxTempOKTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxadminTempOK"),
        ("FN10-MIB", "sxhwManufData"))
)
if mibBuilder.loadTexts:
    sxTempOKTrap.setStatus(
        ""
    )

sxWriteStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 2)
)
sxWriteStatusTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxswdisWriteStatus"),
        ("FN10-MIB", "sxswdisDesc"))
)
if mibBuilder.loadTexts:
    sxWriteStatusTrap.setStatus(
        ""
    )

sxPortFunctionsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 3)
)
sxPortFunctionsTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxifFunction"))
)
if mibBuilder.loadTexts:
    sxPortFunctionsTrap.setStatus(
        ""
    )

sxRxQueuesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 4)
)
sxRxQueuesTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxifRxQueues"))
)
if mibBuilder.loadTexts:
    sxRxQueuesTrap.setStatus(
        ""
    )

sxTxStormFlagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 5)
)
sxTxStormFlagTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxifTxStorms"))
)
if mibBuilder.loadTexts:
    sxTxStormFlagTrap.setStatus(
        ""
    )

sxTxCongestsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 6)
)
sxTxCongestsTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxadminNAMReceiveCongests"))
)
if mibBuilder.loadTexts:
    sxTxCongestsTrap.setStatus(
        ""
    )

sxFilterThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 7)
)
sxFilterThreshTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxfilterLastSrc"),
        ("FN10-MIB", "sxfilterPortNo"))
)
if mibBuilder.loadTexts:
    sxFilterThreshTrap.setStatus(
        ""
    )

sxDebugStringIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 8)
)
sxDebugStringIdTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxdebugStringID"),
        ("FN10-MIB", "sxdebugString"))
)
if mibBuilder.loadTexts:
    sxDebugStringIdTrap.setStatus(
        ""
    )

sxLpbkOperationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 9)
)
sxLpbkOperationTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxlpbkOperation"),
        ("FN10-MIB", "sxlpbkErrorNoReceives"),
        ("FN10-MIB", "sxlpbkErrorBadReceives"))
)
if mibBuilder.loadTexts:
    sxLpbkOperationTrap.setStatus(
        ""
    )

sxTrunkStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 10)
)
sxTrunkStateTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkState"))
)
if mibBuilder.loadTexts:
    sxTrunkStateTrap.setStatus(
        ""
    )

sxTrunkBridgeAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 11)
)
sxTrunkBridgeAddrTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkRemoteBridgeAddr"))
)
if mibBuilder.loadTexts:
    sxTrunkBridgeAddrTrap.setStatus(
        ""
    )

sxTrunkIPAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 12)
)
sxTrunkIPAddrTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkRemoteIp"))
)
if mibBuilder.loadTexts:
    sxTrunkIPAddrTrap.setStatus(
        ""
    )

sxTrunkErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 13)
)
sxTrunkErrorTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkLastError"))
)
if mibBuilder.loadTexts:
    sxTrunkErrorTrap.setStatus(
        ""
    )

sxTrunkLinkOrdinalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 14)
)
sxTrunkLinkOrdinalTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkLinkOrdinal"))
)
if mibBuilder.loadTexts:
    sxTrunkLinkOrdinalTrap.setStatus(
        ""
    )

sxTrunkLinkCountTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 15)
)
sxTrunkLinkCountTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxtrunkLinkCount"))
)
if mibBuilder.loadTexts:
    sxTrunkLinkCountTrap.setStatus(
        ""
    )

sxDiagUnitBootedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 16)
)
sxDiagUnitBootedTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxadminFatalErr"))
)
if mibBuilder.loadTexts:
    sxDiagUnitBootedTrap.setStatus(
        ""
    )

sxStorageFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 17)
)
sxStorageFailureTrap.setObjects(
    ("FN10-MIB", "sxtrapSeverity")
)
if mibBuilder.loadTexts:
    sxStorageFailureTrap.setStatus(
        ""
    )

sxPortCongestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 18)
)
sxPortCongestedTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("IF-MIB", "ifOutDiscards"))
)
if mibBuilder.loadTexts:
    sxPortCongestedTrap.setStatus(
        ""
    )

sxTopChangeBegunTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 19)
)
sxTopChangeBegunTrap.setObjects(
    ("FN10-MIB", "sxtrapSeverity")
)
if mibBuilder.loadTexts:
    sxTopChangeBegunTrap.setStatus(
        ""
    )

sxTopChangeEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 20)
)
sxTopChangeEndTrap.setObjects(
    ("FN10-MIB", "sxtrapSeverity")
)
if mibBuilder.loadTexts:
    sxTopChangeEndTrap.setStatus(
        ""
    )

sxIfErrorsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 21)
)
sxIfErrorsTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    sxIfErrorsTrap.setStatus(
        ""
    )

sxStRootIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 22)
)
sxStRootIDTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    sxStRootIDTrap.setStatus(
        ""
    )

sxStRootCostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 23)
)
sxStRootCostTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpRootCost"))
)
if mibBuilder.loadTexts:
    sxStRootCostTrap.setStatus(
        ""
    )

sxStRootPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 24)
)
sxStRootPortTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpRootPort"))
)
if mibBuilder.loadTexts:
    sxStRootPortTrap.setStatus(
        ""
    )

sxStMaxAgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 25)
)
sxStMaxAgeTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpMaxAge"))
)
if mibBuilder.loadTexts:
    sxStMaxAgeTrap.setStatus(
        ""
    )

sxStHelloTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 26)
)
sxStHelloTimeTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpHelloTime"))
)
if mibBuilder.loadTexts:
    sxStHelloTimeTrap.setStatus(
        ""
    )

sxStForwardDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 27)
)
sxStForwardDelayTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpForwardDelay"))
)
if mibBuilder.loadTexts:
    sxStForwardDelayTrap.setStatus(
        ""
    )

sxStDesigRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 28)
)
sxStDesigRootTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"))
)
if mibBuilder.loadTexts:
    sxStDesigRootTrap.setStatus(
        ""
    )

sxStPortDesigBridgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 29)
)
sxStPortDesigBridgeTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"))
)
if mibBuilder.loadTexts:
    sxStPortDesigBridgeTrap.setStatus(
        ""
    )

sxStPortDesigCostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 30)
)
sxStPortDesigCostTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"))
)
if mibBuilder.loadTexts:
    sxStPortDesigCostTrap.setStatus(
        ""
    )

sxStPortDesigPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 31)
)
sxStPortDesigPortTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"))
)
if mibBuilder.loadTexts:
    sxStPortDesigPortTrap.setStatus(
        ""
    )

sxStPortStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 32)
)
sxStPortStateTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortState"))
)
if mibBuilder.loadTexts:
    sxStPortStateTrap.setStatus(
        ""
    )

sxhwDiagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 100)
)
sxhwDiagTrap.setObjects(
      *(("FN10-MIB", "sxtrapSeverity"),
        ("FN10-MIB", "sxhwDiagCode"))
)
if mibBuilder.loadTexts:
    sxhwDiagTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FN10-MIB",
    **{"cmu": cmu,
       "systems": systems,
       "cmuSNMP": cmuSNMP,
       "cmuKip": cmuKip,
       "cmuRouter": cmuRouter,
       "mibs": mibs,
       "sigma": sigma,
       "sxTempOKTrap": sxTempOKTrap,
       "sxWriteStatusTrap": sxWriteStatusTrap,
       "sxPortFunctionsTrap": sxPortFunctionsTrap,
       "sxRxQueuesTrap": sxRxQueuesTrap,
       "sxTxStormFlagTrap": sxTxStormFlagTrap,
       "sxTxCongestsTrap": sxTxCongestsTrap,
       "sxFilterThreshTrap": sxFilterThreshTrap,
       "sxDebugStringIdTrap": sxDebugStringIdTrap,
       "sxLpbkOperationTrap": sxLpbkOperationTrap,
       "sxTrunkStateTrap": sxTrunkStateTrap,
       "sxTrunkBridgeAddrTrap": sxTrunkBridgeAddrTrap,
       "sxTrunkIPAddrTrap": sxTrunkIPAddrTrap,
       "sxTrunkErrorTrap": sxTrunkErrorTrap,
       "sxTrunkLinkOrdinalTrap": sxTrunkLinkOrdinalTrap,
       "sxTrunkLinkCountTrap": sxTrunkLinkCountTrap,
       "sxDiagUnitBootedTrap": sxDiagUnitBootedTrap,
       "sxStorageFailureTrap": sxStorageFailureTrap,
       "sxPortCongestedTrap": sxPortCongestedTrap,
       "sxTopChangeBegunTrap": sxTopChangeBegunTrap,
       "sxTopChangeEndTrap": sxTopChangeEndTrap,
       "sxIfErrorsTrap": sxIfErrorsTrap,
       "sxStRootIDTrap": sxStRootIDTrap,
       "sxStRootCostTrap": sxStRootCostTrap,
       "sxStRootPortTrap": sxStRootPortTrap,
       "sxStMaxAgeTrap": sxStMaxAgeTrap,
       "sxStHelloTimeTrap": sxStHelloTimeTrap,
       "sxStForwardDelayTrap": sxStForwardDelayTrap,
       "sxStDesigRootTrap": sxStDesigRootTrap,
       "sxStPortDesigBridgeTrap": sxStPortDesigBridgeTrap,
       "sxStPortDesigCostTrap": sxStPortDesigCostTrap,
       "sxStPortDesigPortTrap": sxStPortDesigPortTrap,
       "sxStPortStateTrap": sxStPortStateTrap,
       "sxhwDiagTrap": sxhwDiagTrap,
       "sys": sys,
       "sysID": sysID,
       "sysReset": sysReset,
       "sysTrapAck": sysTrapAck,
       "sysTrapTime": sysTrapTime,
       "sysTrapRetry": sysTrapRetry,
       "sysTrapPort": sysTrapPort,
       "es-1xe": es_1xe,
       "sxhw": sxhw,
       "sxhwDiagCode": sxhwDiagCode,
       "sxhwManufData": sxhwManufData,
       "sxhwPortCount": sxhwPortCount,
       "sxhwPortTable": sxhwPortTable,
       "sxhwPortEntry": sxhwPortEntry,
       "sxhwPortIndex": sxhwPortIndex,
       "sxhwPortType": sxhwPortType,
       "sxhwPortSubType": sxhwPortSubType,
       "sxhwPortDiagPassed": sxhwPortDiagPassed,
       "sxhwAddr": sxhwAddr,
       "sxhwUpLink": sxhwUpLink,
       "sxhwUpLinkManufData": sxhwUpLinkManufData,
       "sxsw": sxsw,
       "sxswNumber": sxswNumber,
       "sxswFilesetTable": sxswFilesetTable,
       "sxswFileset": sxswFileset,
       "sxswIndex": sxswIndex,
       "sxswDesc": sxswDesc,
       "sxswCount": sxswCount,
       "sxswType": sxswType,
       "sxswSizes": sxswSizes,
       "sxswStarts": sxswStarts,
       "sxswBases": sxswBases,
       "sxswFlashBank": sxswFlashBank,
       "sxadmin": sxadmin,
       "sxadminFatalErr": sxadminFatalErr,
       "sxadminAnyPass": sxadminAnyPass,
       "sxadminGetPass": sxadminGetPass,
       "sxadminNMSIPAddr": sxadminNMSIPAddr,
       "sxadminAlarmDynamic": sxadminAlarmDynamic,
       "sxadminAlarmAddressChange": sxadminAlarmAddressChange,
       "sxadminStorageFailure": sxadminStorageFailure,
       "sxadminAuthenticationFailure": sxadminAuthenticationFailure,
       "sxadminStatsExtended": sxadminStatsExtended,
       "sxadminNAMReceiveCongests": sxadminNAMReceiveCongests,
       "sxadminArpEntries": sxadminArpEntries,
       "sxadminArpStatics": sxadminArpStatics,
       "sxadminArpOverflows": sxadminArpOverflows,
       "sxadminIpEntries": sxadminIpEntries,
       "sxadminIpStatics": sxadminIpStatics,
       "sxadminStaticPreference": sxadminStaticPreference,
       "sxadminRipPreference": sxadminRipPreference,
       "sxadminRipRouteDiscards": sxadminRipRouteDiscards,
       "sxadminRebootConfig": sxadminRebootConfig,
       "sxadminTempOK": sxadminTempOK,
       "sxadminDisableButton": sxadminDisableButton,
       "sxadminButtonSelection": sxadminButtonSelection,
       "sxadminLEDProgramOption": sxadminLEDProgramOption,
       "sxadminNAMTxBufferCount": sxadminNAMTxBufferCount,
       "sxadminNAMRxBufferSize": sxadminNAMRxBufferSize,
       "sxadminCpuUtilization": sxadminCpuUtilization,
       "sxadminExtraTrunkGrouping": sxadminExtraTrunkGrouping,
       "sxswdis": sxswdis,
       "sxswdisDesc": sxswdisDesc,
       "sxswdisAccess": sxswdisAccess,
       "sxswdisWriteStatus": sxswdisWriteStatus,
       "sxswdisConfigIp": sxswdisConfigIp,
       "sxswdisConfigRetryTime": sxswdisConfigRetryTime,
       "sxswdisConfigTotalTimeout": sxswdisConfigTotalTimeout,
       "sxaddr": sxaddr,
       "sxaddrStatics": sxaddrStatics,
       "sxaddrDynamics": sxaddrDynamics,
       "sxaddrDynamicMax": sxaddrDynamicMax,
       "sxaddrDynamicOverflows": sxaddrDynamicOverflows,
       "sxaddrFlags": sxaddrFlags,
       "sxaddrMAC": sxaddrMAC,
       "sxaddrPort": sxaddrPort,
       "sxaddrOperation": sxaddrOperation,
       "sxaddrIndex": sxaddrIndex,
       "sxaddrNext": sxaddrNext,
       "sxaddrAge": sxaddrAge,
       "sxaddrDestAge": sxaddrDestAge,
       "sxaddrRxPkts": sxaddrRxPkts,
       "sxaddrRxChars": sxaddrRxChars,
       "sxaddrRxMultiPkts": sxaddrRxMultiPkts,
       "sxaddrRxFwdPkts": sxaddrRxFwdPkts,
       "sxaddrTxPkts": sxaddrTxPkts,
       "sxaddrTxChars": sxaddrTxChars,
       "sxaddrBlockSize": sxaddrBlockSize,
       "sxaddrBlock": sxaddrBlock,
       "sxaddrAlarmMAC": sxaddrAlarmMAC,
       "sxif": sxif,
       "sxifTable": sxifTable,
       "sxifEntry": sxifEntry,
       "sxifIndex": sxifIndex,
       "sxifRxCnt": sxifRxCnt,
       "sxifTxCnt": sxifTxCnt,
       "sxifThreshold": sxifThreshold,
       "sxifThresholdTime": sxifThresholdTime,
       "sxifRxQueueThresh": sxifRxQueueThresh,
       "sxifRxQueueThreshTime": sxifRxQueueThreshTime,
       "sxifTxStormCnt": sxifTxStormCnt,
       "sxifTxStormTime": sxifTxStormTime,
       "sxifFilterFloodSourceSame": sxifFilterFloodSourceSame,
       "sxifFilterAllSourceLearned": sxifFilterAllSourceLearned,
       "sxifFilterNoLearning": sxifFilterNoLearning,
       "sxifFilterAllDestLearned": sxifFilterAllDestLearned,
       "sxifCongestTime": sxifCongestTime,
       "sxifQueueTime": sxifQueueTime,
       "sxifFunction": sxifFunction,
       "sxifRxPacket": sxifRxPacket,
       "sxifRxHwFCSs": sxifRxHwFCSs,
       "sxifRxQueues": sxifRxQueues,
       "sxifTxPacket": sxifTxPacket,
       "sxifTxStorms": sxifTxStorms,
       "sxifTxDests": sxifTxDests,
       "sxifLan1": sxifLan1,
       "sxifLan2": sxifLan2,
       "sxifLan3": sxifLan3,
       "sxifLan4": sxifLan4,
       "sxifStatisticsTime": sxifStatisticsTime,
       "sxifIpAddr": sxifIpAddr,
       "sxifIpGroupAddr": sxifIpGroupAddr,
       "sxifForwardedChars": sxifForwardedChars,
       "sxifFilteredChars": sxifFilteredChars,
       "sxifDescr": sxifDescr,
       "sxdot3": sxdot3,
       "sxdot3Table": sxdot3Table,
       "sxdot3Entry": sxdot3Entry,
       "sxdot3Index": sxdot3Index,
       "sxdot3TPLinkOK": sxdot3TPLinkOK,
       "sxdot3LedOn": sxdot3LedOn,
       "sxdot3RxCollisions": sxdot3RxCollisions,
       "sxdot3RxRunts": sxdot3RxRunts,
       "sxdot3RxLateColls": sxdot3RxLateColls,
       "sxdot3TxJabbers": sxdot3TxJabbers,
       "sxdot3TxBabbles": sxdot3TxBabbles,
       "sxdot3TxCollisions": sxdot3TxCollisions,
       "sxdot3RxErrInfo": sxdot3RxErrInfo,
       "sxdot3TxErrInfo": sxdot3TxErrInfo,
       "sxdot3FuseOkay": sxdot3FuseOkay,
       "sxdot3SpeedSelection": sxdot3SpeedSelection,
       "sxuart": sxuart,
       "sxuartTable": sxuartTable,
       "sxuartEntry": sxuartEntry,
       "sxuartIndex": sxuartIndex,
       "sxuartBaud": sxuartBaud,
       "sxuartAlignmentErrors": sxuartAlignmentErrors,
       "sxuartOverrunErrors": sxuartOverrunErrors,
       "sxfilter": sxfilter,
       "sxfilterMaxCount": sxfilterMaxCount,
       "sxfilterCurrentCount": sxfilterCurrentCount,
       "sxfilterDeleteID": sxfilterDeleteID,
       "sxfilterNextID": sxfilterNextID,
       "sxfilterAddID": sxfilterAddID,
       "sxfilterAddIndex": sxfilterAddIndex,
       "sxfilterTable": sxfilterTable,
       "sxfilterEntry": sxfilterEntry,
       "sxfilterIndex": sxfilterIndex,
       "sxfilterID": sxfilterID,
       "sxfilterPortNo": sxfilterPortNo,
       "sxfilterComboType": sxfilterComboType,
       "sxfilterFlags": sxfilterFlags,
       "sxfilterFrame": sxfilterFrame,
       "sxfilterSource": sxfilterSource,
       "sxfilterSourceEnd": sxfilterSourceEnd,
       "sxfilterDest": sxfilterDest,
       "sxfilterDestEnd": sxfilterDestEnd,
       "sxfilterSourceMask": sxfilterSourceMask,
       "sxfilterDestMask": sxfilterDestMask,
       "sxfilterSrcLan": sxfilterSrcLan,
       "sxfilterOffset": sxfilterOffset,
       "sxfilterField": sxfilterField,
       "sxfilterMask": sxfilterMask,
       "sxfilterThreshold": sxfilterThreshold,
       "sxfilterThreshTime": sxfilterThreshTime,
       "sxfilterThreshFlag": sxfilterThreshFlag,
       "sxfilterPktCnts": sxfilterPktCnts,
       "sxfilterLastSrc": sxfilterLastSrc,
       "sxfilterByteCnts": sxfilterByteCnts,
       "sxdebug": sxdebug,
       "sxdebugStringID": sxdebugStringID,
       "sxdebugString": sxdebugString,
       "sxdebugTable": sxdebugTable,
       "sxdebugEntry": sxdebugEntry,
       "sxdebugIndex": sxdebugIndex,
       "sxdebugOperation": sxdebugOperation,
       "sxdebugBase": sxdebugBase,
       "sxdebugLength": sxdebugLength,
       "sxdebugData": sxdebugData,
       "sxlpbk": sxlpbk,
       "sxlpbkTable": sxlpbkTable,
       "sxlpbkEntry": sxlpbkEntry,
       "sxlpbkIndex": sxlpbkIndex,
       "sxlpbkOperation": sxlpbkOperation,
       "sxlpbkDestAddr": sxlpbkDestAddr,
       "sxlpbkPktNum": sxlpbkPktNum,
       "sxlpbkInterval": sxlpbkInterval,
       "sxlpbkPktLength": sxlpbkPktLength,
       "sxlpbkIncrements": sxlpbkIncrements,
       "sxlpbkGoods": sxlpbkGoods,
       "sxlpbkErrorNoReceives": sxlpbkErrorNoReceives,
       "sxlpbkErrorBadReceives": sxlpbkErrorBadReceives,
       "sxlpbkErrorSize": sxlpbkErrorSize,
       "sxlpbkErrorSent": sxlpbkErrorSent,
       "sxlpbkErrorReceived": sxlpbkErrorReceived,
       "sxlpbkErrorOffset": sxlpbkErrorOffset,
       "sxproto": sxproto,
       "sxprotoTable": sxprotoTable,
       "sxprotoEntry": sxprotoEntry,
       "sxprotoIfIndex": sxprotoIfIndex,
       "sxprotoBridge": sxprotoBridge,
       "sxprotoSuppressBpdu": sxprotoSuppressBpdu,
       "sxprotoRipListen": sxprotoRipListen,
       "sxprotoTrunking": sxprotoTrunking,
       "sxsprotoCollisionRelief": sxsprotoCollisionRelief,
       "sxtrunk": sxtrunk,
       "sxtrunkTable": sxtrunkTable,
       "sxtrunkEntry": sxtrunkEntry,
       "sxtrunkIfIndex": sxtrunkIfIndex,
       "sxtrunkState": sxtrunkState,
       "sxtrunkRemoteBridgeAddr": sxtrunkRemoteBridgeAddr,
       "sxtrunkRemoteIp": sxtrunkRemoteIp,
       "sxtrunkLastError": sxtrunkLastError,
       "sxtrunkLinkOrdinal": sxtrunkLinkOrdinal,
       "sxtrunkLinkCount": sxtrunkLinkCount,
       "sxtrunkLastChange": sxtrunkLastChange,
       "sxworkgroup": sxworkgroup,
       "sxWorkGroupNextNumber": sxWorkGroupNextNumber,
       "sxWorkGroupCurrentCount": sxWorkGroupCurrentCount,
       "sxWorkGroupMaxCount": sxWorkGroupMaxCount,
       "sxWorkGroupTable": sxWorkGroupTable,
       "sxWorkGroupEntry": sxWorkGroupEntry,
       "sxWorkGroupNumber": sxWorkGroupNumber,
       "sxWorkGroupName": sxWorkGroupName,
       "sxWorkGroupPorts": sxWorkGroupPorts,
       "sxWorkGroupType": sxWorkGroupType,
       "sxWorkGroupIpAddress": sxWorkGroupIpAddress,
       "sxWorkGroupIpMask": sxWorkGroupIpMask,
       "sxWorkGroupIpxNetwork": sxWorkGroupIpxNetwork,
       "sxtrapMgt": sxtrapMgt,
       "sxtrapControlTable": sxtrapControlTable,
       "sxtrapControl": sxtrapControl,
       "sxtrapIndex": sxtrapIndex,
       "sxtrapEnabled": sxtrapEnabled,
       "sxtrapSeverity": sxtrapSeverity,
       "sxtrapText": sxtrapText,
       "sxtrapSeverityControlTable": sxtrapSeverityControlTable,
       "sxtrapSeverityControl": sxtrapSeverityControl,
       "sxtrapSeverityControlSeverity": sxtrapSeverityControlSeverity,
       "sxtrapSeverityEnable": sxtrapSeverityEnable,
       "sxtrapIncludeText": sxtrapIncludeText,
       "sxtrapTime": sxtrapTime,
       "sxtrapRetry": sxtrapRetry,
       "sxtrapEntryNumber": sxtrapEntryNumber,
       "sxtrapTable": sxtrapTable,
       "sxtrapEntry": sxtrapEntry,
       "sxtrapEntryIndex": sxtrapEntryIndex,
       "sxtrapEntryTimeStamp": sxtrapEntryTimeStamp,
       "sxtrapEntryText": sxtrapEntryText,
       "sxtrapNumber": sxtrapNumber,
       "sxtrapEntrySeverity": sxtrapEntrySeverity}
)
