# SNMP MIB module (FN100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FN100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:15 2024
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
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
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
        ("es-1fe-bridge", 2)
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
sysTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapAck.setStatus("mandatory")
_SysTrapTime_Type = TimeTicks
_SysTrapTime_Object = MibScalar
sysTrapTime = _SysTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 4),
    _SysTrapTime_Type()
)
sysTrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapTime.setStatus("mandatory")
_SysTrapRetry_Type = TimeTicks
_SysTrapRetry_Object = MibScalar
sysTrapRetry = _SysTrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 5),
    _SysTrapRetry_Type()
)
sysTrapRetry.setMaxAccess("read-write")
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
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5)
)
_Es_1fe_ObjectIdentity = ObjectIdentity
es_1fe = _Es_1fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3)
)
_Sfhw_ObjectIdentity = ObjectIdentity
sfhw = _Sfhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1)
)
_SfhwDiagCode_Type = OctetString
_SfhwDiagCode_Object = MibScalar
sfhwDiagCode = _SfhwDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 1),
    _SfhwDiagCode_Type()
)
sfhwDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwDiagCode.setStatus("mandatory")
_SfhwManufData_Type = DisplayString
_SfhwManufData_Object = MibScalar
sfhwManufData = _SfhwManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 2),
    _SfhwManufData_Type()
)
sfhwManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwManufData.setStatus("mandatory")
_SfhwPortCount_Type = Integer32
_SfhwPortCount_Object = MibScalar
sfhwPortCount = _SfhwPortCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 3),
    _SfhwPortCount_Type()
)
sfhwPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwPortCount.setStatus("mandatory")
_SfhwPortTable_Object = MibTable
sfhwPortTable = _SfhwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4)
)
if mibBuilder.loadTexts:
    sfhwPortTable.setStatus("mandatory")
_SfhwPortEntry_Object = MibTableRow
sfhwPortEntry = _SfhwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1)
)
sfhwPortEntry.setIndexNames(
    (0, "FN100-MIB", "sfhwPortIndex"),
)
if mibBuilder.loadTexts:
    sfhwPortEntry.setStatus("mandatory")
_SfhwPortIndex_Type = Integer32
_SfhwPortIndex_Object = MibTableColumn
sfhwPortIndex = _SfhwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1, 1),
    _SfhwPortIndex_Type()
)
sfhwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwPortIndex.setStatus("mandatory")


class _SfhwPortType_Type(Integer32):
    """Custom type sfhwPortType based on Integer32"""
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


_SfhwPortType_Type.__name__ = "Integer32"
_SfhwPortType_Object = MibTableColumn
sfhwPortType = _SfhwPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1, 2),
    _SfhwPortType_Type()
)
sfhwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwPortType.setStatus("mandatory")


class _SfhwPortSubType_Type(Integer32):
    """Custom type sfhwPortSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              13,
              16,
              80,
              255)
        )
    )
    namedValues = NamedValues(
        *(("csmacd-fx", 10),
          ("csmacd-tpx", 13),
          ("csmacd-tpx-fx", 16),
          ("no-information", 255),
          ("uart-female-9pin", 80))
    )


_SfhwPortSubType_Type.__name__ = "Integer32"
_SfhwPortSubType_Object = MibTableColumn
sfhwPortSubType = _SfhwPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1, 3),
    _SfhwPortSubType_Type()
)
sfhwPortSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwPortSubType.setStatus("mandatory")


class _SfhwPortDiagPassed_Type(Integer32):
    """Custom type sfhwPortDiagPassed based on Integer32"""
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


_SfhwPortDiagPassed_Type.__name__ = "Integer32"
_SfhwPortDiagPassed_Object = MibTableColumn
sfhwPortDiagPassed = _SfhwPortDiagPassed_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1, 4),
    _SfhwPortDiagPassed_Type()
)
sfhwPortDiagPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwPortDiagPassed.setStatus("mandatory")
_SfhwAddr_Type = OctetString
_SfhwAddr_Object = MibTableColumn
sfhwAddr = _SfhwAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 1, 4, 1, 5),
    _SfhwAddr_Type()
)
sfhwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfhwAddr.setStatus("mandatory")
_Sfsw_ObjectIdentity = ObjectIdentity
sfsw = _Sfsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2)
)
_SfswNumber_Type = Integer32
_SfswNumber_Object = MibScalar
sfswNumber = _SfswNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 1),
    _SfswNumber_Type()
)
sfswNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswNumber.setStatus("mandatory")
_SfswFilesetTable_Object = MibTable
sfswFilesetTable = _SfswFilesetTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sfswFilesetTable.setStatus("mandatory")
_SfswFileset_Object = MibTableRow
sfswFileset = _SfswFileset_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1)
)
sfswFileset.setIndexNames(
    (0, "FN100-MIB", "sfswIndex"),
)
if mibBuilder.loadTexts:
    sfswFileset.setStatus("mandatory")


class _SfswIndex_Type(Integer32):
    """Custom type sfswIndex based on Integer32"""
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


_SfswIndex_Type.__name__ = "Integer32"
_SfswIndex_Object = MibTableColumn
sfswIndex = _SfswIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 1),
    _SfswIndex_Type()
)
sfswIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswIndex.setStatus("mandatory")
_SfswDesc_Type = DisplayString
_SfswDesc_Object = MibTableColumn
sfswDesc = _SfswDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 2),
    _SfswDesc_Type()
)
sfswDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswDesc.setStatus("mandatory")
_SfswCount_Type = Integer32
_SfswCount_Object = MibTableColumn
sfswCount = _SfswCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 3),
    _SfswCount_Type()
)
sfswCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswCount.setStatus("mandatory")
_SfswType_Type = OctetString
_SfswType_Object = MibTableColumn
sfswType = _SfswType_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 4),
    _SfswType_Type()
)
sfswType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswType.setStatus("mandatory")
_SfswSizes_Type = OctetString
_SfswSizes_Object = MibTableColumn
sfswSizes = _SfswSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 5),
    _SfswSizes_Type()
)
sfswSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswSizes.setStatus("mandatory")
_SfswStarts_Type = OctetString
_SfswStarts_Object = MibTableColumn
sfswStarts = _SfswStarts_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 6),
    _SfswStarts_Type()
)
sfswStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswStarts.setStatus("mandatory")
_SfswBases_Type = OctetString
_SfswBases_Object = MibTableColumn
sfswBases = _SfswBases_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 7),
    _SfswBases_Type()
)
sfswBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswBases.setStatus("mandatory")


class _SfswFlashBank_Type(Integer32):
    """Custom type sfswFlashBank based on Integer32"""
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


_SfswFlashBank_Type.__name__ = "Integer32"
_SfswFlashBank_Object = MibTableColumn
sfswFlashBank = _SfswFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 2, 2, 1, 8),
    _SfswFlashBank_Type()
)
sfswFlashBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswFlashBank.setStatus("mandatory")
_Sfadmin_ObjectIdentity = ObjectIdentity
sfadmin = _Sfadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3)
)
_SfadminFatalErr_Type = OctetString
_SfadminFatalErr_Object = MibScalar
sfadminFatalErr = _SfadminFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 1),
    _SfadminFatalErr_Type()
)
sfadminFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminFatalErr.setStatus("mandatory")
_SfadminAnyPass_Type = OctetString
_SfadminAnyPass_Object = MibScalar
sfadminAnyPass = _SfadminAnyPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 2),
    _SfadminAnyPass_Type()
)
sfadminAnyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminAnyPass.setStatus("mandatory")
_SfadminGetPass_Type = OctetString
_SfadminGetPass_Object = MibScalar
sfadminGetPass = _SfadminGetPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 3),
    _SfadminGetPass_Type()
)
sfadminGetPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminGetPass.setStatus("mandatory")
_SfadminNMSIPAddr_Type = IpAddress
_SfadminNMSIPAddr_Object = MibScalar
sfadminNMSIPAddr = _SfadminNMSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 4),
    _SfadminNMSIPAddr_Type()
)
sfadminNMSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminNMSIPAddr.setStatus("mandatory")


class _SfadminAlarmDynamic_Type(Integer32):
    """Custom type sfadminAlarmDynamic based on Integer32"""
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


_SfadminAlarmDynamic_Type.__name__ = "Integer32"
_SfadminAlarmDynamic_Object = MibScalar
sfadminAlarmDynamic = _SfadminAlarmDynamic_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 5),
    _SfadminAlarmDynamic_Type()
)
sfadminAlarmDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminAlarmDynamic.setStatus("mandatory")


class _SfadminAlarmAddressChange_Type(Integer32):
    """Custom type sfadminAlarmAddressChange based on Integer32"""
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


_SfadminAlarmAddressChange_Type.__name__ = "Integer32"
_SfadminAlarmAddressChange_Object = MibScalar
sfadminAlarmAddressChange = _SfadminAlarmAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 6),
    _SfadminAlarmAddressChange_Type()
)
sfadminAlarmAddressChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminAlarmAddressChange.setStatus("mandatory")


class _SfadminStorageFailure_Type(Integer32):
    """Custom type sfadminStorageFailure based on Integer32"""
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


_SfadminStorageFailure_Type.__name__ = "Integer32"
_SfadminStorageFailure_Object = MibScalar
sfadminStorageFailure = _SfadminStorageFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 7),
    _SfadminStorageFailure_Type()
)
sfadminStorageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminStorageFailure.setStatus("mandatory")
_SfadminAuthenticationFailure_Type = IpAddress
_SfadminAuthenticationFailure_Object = MibScalar
sfadminAuthenticationFailure = _SfadminAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 8),
    _SfadminAuthenticationFailure_Type()
)
sfadminAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminAuthenticationFailure.setStatus("mandatory")
_SfadminMPReceiveCongests_Type = Counter32
_SfadminMPReceiveCongests_Object = MibScalar
sfadminMPReceiveCongests = _SfadminMPReceiveCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 9),
    _SfadminMPReceiveCongests_Type()
)
sfadminMPReceiveCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminMPReceiveCongests.setStatus("mandatory")
_SfadminArpEntries_Type = Counter32
_SfadminArpEntries_Object = MibScalar
sfadminArpEntries = _SfadminArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 10),
    _SfadminArpEntries_Type()
)
sfadminArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminArpEntries.setStatus("mandatory")
_SfadminArpStatics_Type = Counter32
_SfadminArpStatics_Object = MibScalar
sfadminArpStatics = _SfadminArpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 11),
    _SfadminArpStatics_Type()
)
sfadminArpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminArpStatics.setStatus("mandatory")
_SfadminArpOverflows_Type = Counter32
_SfadminArpOverflows_Object = MibScalar
sfadminArpOverflows = _SfadminArpOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 12),
    _SfadminArpOverflows_Type()
)
sfadminArpOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminArpOverflows.setStatus("mandatory")
_SfadminIpEntries_Type = Counter32
_SfadminIpEntries_Object = MibScalar
sfadminIpEntries = _SfadminIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 13),
    _SfadminIpEntries_Type()
)
sfadminIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminIpEntries.setStatus("mandatory")
_SfadminIpStatics_Type = Counter32
_SfadminIpStatics_Object = MibScalar
sfadminIpStatics = _SfadminIpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 14),
    _SfadminIpStatics_Type()
)
sfadminIpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminIpStatics.setStatus("mandatory")
_SfadminStaticPreference_Type = Integer32
_SfadminStaticPreference_Object = MibScalar
sfadminStaticPreference = _SfadminStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 15),
    _SfadminStaticPreference_Type()
)
sfadminStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminStaticPreference.setStatus("mandatory")
_SfadminRipPreference_Type = Integer32
_SfadminRipPreference_Object = MibScalar
sfadminRipPreference = _SfadminRipPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 16),
    _SfadminRipPreference_Type()
)
sfadminRipPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminRipPreference.setStatus("mandatory")
_SfadminRipRouteDiscards_Type = Counter32
_SfadminRipRouteDiscards_Object = MibScalar
sfadminRipRouteDiscards = _SfadminRipRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 17),
    _SfadminRipRouteDiscards_Type()
)
sfadminRipRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminRipRouteDiscards.setStatus("mandatory")


class _SfadminRebootConfig_Type(Integer32):
    """Custom type sfadminRebootConfig based on Integer32"""
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


_SfadminRebootConfig_Type.__name__ = "Integer32"
_SfadminRebootConfig_Object = MibScalar
sfadminRebootConfig = _SfadminRebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 18),
    _SfadminRebootConfig_Type()
)
sfadminRebootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminRebootConfig.setStatus("mandatory")


class _SfadminTempOK_Type(Integer32):
    """Custom type sfadminTempOK based on Integer32"""
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


_SfadminTempOK_Type.__name__ = "Integer32"
_SfadminTempOK_Object = MibScalar
sfadminTempOK = _SfadminTempOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 19),
    _SfadminTempOK_Type()
)
sfadminTempOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfadminTempOK.setStatus("mandatory")


class _SfadminDisableButton_Type(Integer32):
    """Custom type sfadminDisableButton based on Integer32"""
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


_SfadminDisableButton_Type.__name__ = "Integer32"
_SfadminDisableButton_Object = MibScalar
sfadminDisableButton = _SfadminDisableButton_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 20),
    _SfadminDisableButton_Type()
)
sfadminDisableButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminDisableButton.setStatus("mandatory")


class _SfadminButtonSelection_Type(Integer32):
    """Custom type sfadminButtonSelection based on Integer32"""
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
        *(("led-any-activity", 1),
          ("led-any-collision", 4),
          ("led-programmed", 5),
          ("led-rx-activity", 2),
          ("led-speed", 6),
          ("led-tx-activity", 3))
    )


_SfadminButtonSelection_Type.__name__ = "Integer32"
_SfadminButtonSelection_Object = MibScalar
sfadminButtonSelection = _SfadminButtonSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 21),
    _SfadminButtonSelection_Type()
)
sfadminButtonSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminButtonSelection.setStatus("mandatory")


class _SfadminLEDProgramOption_Type(Integer32):
    """Custom type sfadminLEDProgramOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("program-led-any-error", 1)
    )


_SfadminLEDProgramOption_Type.__name__ = "Integer32"
_SfadminLEDProgramOption_Object = MibScalar
sfadminLEDProgramOption = _SfadminLEDProgramOption_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 22),
    _SfadminLEDProgramOption_Type()
)
sfadminLEDProgramOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminLEDProgramOption.setStatus("mandatory")
_SfadminVirtualSwitch1_Type = OctetString
_SfadminVirtualSwitch1_Object = MibScalar
sfadminVirtualSwitch1 = _SfadminVirtualSwitch1_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 23),
    _SfadminVirtualSwitch1_Type()
)
sfadminVirtualSwitch1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminVirtualSwitch1.setStatus("mandatory")
_SfadminVirtualSwitch2_Type = OctetString
_SfadminVirtualSwitch2_Object = MibScalar
sfadminVirtualSwitch2 = _SfadminVirtualSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 24),
    _SfadminVirtualSwitch2_Type()
)
sfadminVirtualSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminVirtualSwitch2.setStatus("mandatory")
_SfadminVirtualSwitch3_Type = OctetString
_SfadminVirtualSwitch3_Object = MibScalar
sfadminVirtualSwitch3 = _SfadminVirtualSwitch3_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 25),
    _SfadminVirtualSwitch3_Type()
)
sfadminVirtualSwitch3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminVirtualSwitch3.setStatus("mandatory")
_SfadminVirtualSwitch4_Type = OctetString
_SfadminVirtualSwitch4_Object = MibScalar
sfadminVirtualSwitch4 = _SfadminVirtualSwitch4_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 26),
    _SfadminVirtualSwitch4_Type()
)
sfadminVirtualSwitch4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminVirtualSwitch4.setStatus("mandatory")


class _SfadminDefaultVirtualSwitch_Type(Integer32):
    """Custom type sfadminDefaultVirtualSwitch based on Integer32"""
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
        *(("virtual-switch-1", 1),
          ("virtual-switch-2", 2),
          ("virtual-switch-3", 3),
          ("virtual-switch-4", 4))
    )


_SfadminDefaultVirtualSwitch_Type.__name__ = "Integer32"
_SfadminDefaultVirtualSwitch_Object = MibScalar
sfadminDefaultVirtualSwitch = _SfadminDefaultVirtualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 3, 27),
    _SfadminDefaultVirtualSwitch_Type()
)
sfadminDefaultVirtualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfadminDefaultVirtualSwitch.setStatus("mandatory")
_Sfswdis_ObjectIdentity = ObjectIdentity
sfswdis = _Sfswdis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4)
)
_SfswdisDesc_Type = OctetString
_SfswdisDesc_Object = MibScalar
sfswdisDesc = _SfswdisDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 1),
    _SfswdisDesc_Type()
)
sfswdisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswdisDesc.setStatus("mandatory")


class _SfswdisAccess_Type(Integer32):
    """Custom type sfswdisAccess based on Integer32"""
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


_SfswdisAccess_Type.__name__ = "Integer32"
_SfswdisAccess_Object = MibScalar
sfswdisAccess = _SfswdisAccess_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 2),
    _SfswdisAccess_Type()
)
sfswdisAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfswdisAccess.setStatus("mandatory")


class _SfswdisWriteStatus_Type(Integer32):
    """Custom type sfswdisWriteStatus based on Integer32"""
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


_SfswdisWriteStatus_Type.__name__ = "Integer32"
_SfswdisWriteStatus_Object = MibScalar
sfswdisWriteStatus = _SfswdisWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 3),
    _SfswdisWriteStatus_Type()
)
sfswdisWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfswdisWriteStatus.setStatus("mandatory")
_SfswdisConfigIp_Type = IpAddress
_SfswdisConfigIp_Object = MibScalar
sfswdisConfigIp = _SfswdisConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 4),
    _SfswdisConfigIp_Type()
)
sfswdisConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfswdisConfigIp.setStatus("mandatory")
_SfswdisConfigRetryTime_Type = Integer32
_SfswdisConfigRetryTime_Object = MibScalar
sfswdisConfigRetryTime = _SfswdisConfigRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 5),
    _SfswdisConfigRetryTime_Type()
)
sfswdisConfigRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfswdisConfigRetryTime.setStatus("mandatory")
_SfswdisConfigTotalTimeout_Type = Integer32
_SfswdisConfigTotalTimeout_Object = MibScalar
sfswdisConfigTotalTimeout = _SfswdisConfigTotalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 4, 6),
    _SfswdisConfigTotalTimeout_Type()
)
sfswdisConfigTotalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfswdisConfigTotalTimeout.setStatus("mandatory")
_Sfaddr_ObjectIdentity = ObjectIdentity
sfaddr = _Sfaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5)
)
_SfaddrDynamics_Type = Counter32
_SfaddrDynamics_Object = MibScalar
sfaddrDynamics = _SfaddrDynamics_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 1),
    _SfaddrDynamics_Type()
)
sfaddrDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDynamics.setStatus("mandatory")
_SfaddrDynamicMax_Type = Gauge32
_SfaddrDynamicMax_Object = MibScalar
sfaddrDynamicMax = _SfaddrDynamicMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 2),
    _SfaddrDynamicMax_Type()
)
sfaddrDynamicMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrDynamicMax.setStatus("mandatory")
_SfaddrFlags_Type = Integer32
_SfaddrFlags_Object = MibScalar
sfaddrFlags = _SfaddrFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 3),
    _SfaddrFlags_Type()
)
sfaddrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrFlags.setStatus("mandatory")
_SfaddrMAC_Type = OctetString
_SfaddrMAC_Object = MibScalar
sfaddrMAC = _SfaddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 4),
    _SfaddrMAC_Type()
)
sfaddrMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrMAC.setStatus("mandatory")
_SfaddrPort_Type = Integer32
_SfaddrPort_Object = MibScalar
sfaddrPort = _SfaddrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 5),
    _SfaddrPort_Type()
)
sfaddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrPort.setStatus("mandatory")


class _SfaddrOperation_Type(Integer32):
    """Custom type sfaddrOperation based on Integer32"""
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
          ("reserved", 3),
          ("update", 4))
    )


_SfaddrOperation_Type.__name__ = "Integer32"
_SfaddrOperation_Object = MibScalar
sfaddrOperation = _SfaddrOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 6),
    _SfaddrOperation_Type()
)
sfaddrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrOperation.setStatus("mandatory")
_SfaddrIndex_Type = Integer32
_SfaddrIndex_Object = MibScalar
sfaddrIndex = _SfaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 7),
    _SfaddrIndex_Type()
)
sfaddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrIndex.setStatus("mandatory")
_SfaddrNext_Type = Integer32
_SfaddrNext_Object = MibScalar
sfaddrNext = _SfaddrNext_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 8),
    _SfaddrNext_Type()
)
sfaddrNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrNext.setStatus("mandatory")
_SfaddrBlockSize_Type = Integer32
_SfaddrBlockSize_Object = MibScalar
sfaddrBlockSize = _SfaddrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 9),
    _SfaddrBlockSize_Type()
)
sfaddrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrBlockSize.setStatus("mandatory")
_SfaddrBlock_Type = OctetString
_SfaddrBlock_Object = MibScalar
sfaddrBlock = _SfaddrBlock_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 10),
    _SfaddrBlock_Type()
)
sfaddrBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrBlock.setStatus("mandatory")
_SfaddrAlarmMAC_Type = OctetString
_SfaddrAlarmMAC_Object = MibScalar
sfaddrAlarmMAC = _SfaddrAlarmMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 11),
    _SfaddrAlarmMAC_Type()
)
sfaddrAlarmMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrAlarmMAC.setStatus("mandatory")
_SfaddrDbFullBuckets_Type = Integer32
_SfaddrDbFullBuckets_Object = MibScalar
sfaddrDbFullBuckets = _SfaddrDbFullBuckets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 12),
    _SfaddrDbFullBuckets_Type()
)
sfaddrDbFullBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbFullBuckets.setStatus("mandatory")
_SfaddrDbMaxFullBuckets_Type = Integer32
_SfaddrDbMaxFullBuckets_Object = MibScalar
sfaddrDbMaxFullBuckets = _SfaddrDbMaxFullBuckets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 13),
    _SfaddrDbMaxFullBuckets_Type()
)
sfaddrDbMaxFullBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrDbMaxFullBuckets.setStatus("mandatory")
_SfaddrDbMaxSize_Type = Integer32
_SfaddrDbMaxSize_Object = MibScalar
sfaddrDbMaxSize = _SfaddrDbMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 14),
    _SfaddrDbMaxSize_Type()
)
sfaddrDbMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbMaxSize.setStatus("mandatory")
_SfaddrDbBuckets_Type = Integer32
_SfaddrDbBuckets_Object = MibScalar
sfaddrDbBuckets = _SfaddrDbBuckets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 15),
    _SfaddrDbBuckets_Type()
)
sfaddrDbBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbBuckets.setStatus("mandatory")
_SfaddrDbSearchDepth_Type = Integer32
_SfaddrDbSearchDepth_Object = MibScalar
sfaddrDbSearchDepth = _SfaddrDbSearchDepth_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 16),
    _SfaddrDbSearchDepth_Type()
)
sfaddrDbSearchDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfaddrDbSearchDepth.setStatus("mandatory")
_SfaddrDbDistribution_Type = OctetString
_SfaddrDbDistribution_Object = MibScalar
sfaddrDbDistribution = _SfaddrDbDistribution_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 17),
    _SfaddrDbDistribution_Type()
)
sfaddrDbDistribution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbDistribution.setStatus("mandatory")
_SfaddrDbTable_Object = MibTable
sfaddrDbTable = _SfaddrDbTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 18)
)
if mibBuilder.loadTexts:
    sfaddrDbTable.setStatus("mandatory")
_SfaddrDbEntry_Object = MibTableRow
sfaddrDbEntry = _SfaddrDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 18, 1)
)
sfaddrDbEntry.setIndexNames(
    (0, "FN100-MIB", "sfaddrDbBucketAddress"),
)
if mibBuilder.loadTexts:
    sfaddrDbEntry.setStatus("mandatory")


class _SfaddrDbBucketAddress_Type(OctetString):
    """Custom type sfaddrDbBucketAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SfaddrDbBucketAddress_Type.__name__ = "OctetString"
_SfaddrDbBucketAddress_Object = MibTableColumn
sfaddrDbBucketAddress = _SfaddrDbBucketAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 18, 1, 1),
    _SfaddrDbBucketAddress_Type()
)
sfaddrDbBucketAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbBucketAddress.setStatus("mandatory")
_SfaddrDbBucketEntCnt_Type = Integer32
_SfaddrDbBucketEntCnt_Object = MibTableColumn
sfaddrDbBucketEntCnt = _SfaddrDbBucketEntCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 18, 1, 2),
    _SfaddrDbBucketEntCnt_Type()
)
sfaddrDbBucketEntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbBucketEntCnt.setStatus("mandatory")
_SfaddrDbBucketEntries_Type = OctetString
_SfaddrDbBucketEntries_Object = MibTableColumn
sfaddrDbBucketEntries = _SfaddrDbBucketEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 5, 18, 1, 3),
    _SfaddrDbBucketEntries_Type()
)
sfaddrDbBucketEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfaddrDbBucketEntries.setStatus("mandatory")
_Sfif_ObjectIdentity = ObjectIdentity
sfif = _Sfif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6)
)
_SfifTable_Object = MibTable
sfifTable = _SfifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1)
)
if mibBuilder.loadTexts:
    sfifTable.setStatus("mandatory")
_SfifEntry_Object = MibTableRow
sfifEntry = _SfifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1)
)
sfifEntry.setIndexNames(
    (0, "FN100-MIB", "sfifIndex"),
)
if mibBuilder.loadTexts:
    sfifEntry.setStatus("mandatory")
_SfifIndex_Type = Integer32
_SfifIndex_Object = MibTableColumn
sfifIndex = _SfifIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 1),
    _SfifIndex_Type()
)
sfifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifIndex.setStatus("mandatory")
_SfifRxCnt_Type = Integer32
_SfifRxCnt_Object = MibTableColumn
sfifRxCnt = _SfifRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 2),
    _SfifRxCnt_Type()
)
sfifRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxCnt.setStatus("mandatory")
_SfifTxCnt_Type = Integer32
_SfifTxCnt_Object = MibTableColumn
sfifTxCnt = _SfifTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 3),
    _SfifTxCnt_Type()
)
sfifTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifTxCnt.setStatus("mandatory")
_SfifTxStormCnt_Type = Integer32
_SfifTxStormCnt_Object = MibTableColumn
sfifTxStormCnt = _SfifTxStormCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 4),
    _SfifTxStormCnt_Type()
)
sfifTxStormCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifTxStormCnt.setStatus("mandatory")
_SfifTxStormTime_Type = TimeTicks
_SfifTxStormTime_Object = MibTableColumn
sfifTxStormTime = _SfifTxStormTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 5),
    _SfifTxStormTime_Type()
)
sfifTxStormTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifTxStormTime.setStatus("mandatory")


class _SfifFilterFloodSourceSame_Type(Integer32):
    """Custom type sfifFilterFloodSourceSame based on Integer32"""
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


_SfifFilterFloodSourceSame_Type.__name__ = "Integer32"
_SfifFilterFloodSourceSame_Object = MibTableColumn
sfifFilterFloodSourceSame = _SfifFilterFloodSourceSame_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 6),
    _SfifFilterFloodSourceSame_Type()
)
sfifFilterFloodSourceSame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifFilterFloodSourceSame.setStatus("mandatory")
_SfifFunction_Type = Integer32
_SfifFunction_Object = MibTableColumn
sfifFunction = _SfifFunction_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 7),
    _SfifFunction_Type()
)
sfifFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifFunction.setStatus("mandatory")
_SfifRxPacket_Type = OctetString
_SfifRxPacket_Object = MibTableColumn
sfifRxPacket = _SfifRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 8),
    _SfifRxPacket_Type()
)
sfifRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxPacket.setStatus("mandatory")
_SfifRxHwFCSs_Type = Counter32
_SfifRxHwFCSs_Object = MibTableColumn
sfifRxHwFCSs = _SfifRxHwFCSs_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 9),
    _SfifRxHwFCSs_Type()
)
sfifRxHwFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxHwFCSs.setStatus("mandatory")
_SfifRxQueues_Type = Counter32
_SfifRxQueues_Object = MibTableColumn
sfifRxQueues = _SfifRxQueues_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 10),
    _SfifRxQueues_Type()
)
sfifRxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxQueues.setStatus("mandatory")
_SfifTxPacket_Type = OctetString
_SfifTxPacket_Object = MibTableColumn
sfifTxPacket = _SfifTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 11),
    _SfifTxPacket_Type()
)
sfifTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifTxPacket.setStatus("mandatory")
_SfifTxStorms_Type = Counter32
_SfifTxStorms_Object = MibTableColumn
sfifTxStorms = _SfifTxStorms_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 12),
    _SfifTxStorms_Type()
)
sfifTxStorms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifTxStorms.setStatus("mandatory")
_SfifStatisticsTime_Type = TimeTicks
_SfifStatisticsTime_Object = MibTableColumn
sfifStatisticsTime = _SfifStatisticsTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 13),
    _SfifStatisticsTime_Type()
)
sfifStatisticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifStatisticsTime.setStatus("mandatory")
_SfifIpAddr_Type = IpAddress
_SfifIpAddr_Object = MibTableColumn
sfifIpAddr = _SfifIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 14),
    _SfifIpAddr_Type()
)
sfifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifIpAddr.setStatus("mandatory")
_SfifIpGroupAddr_Type = IpAddress
_SfifIpGroupAddr_Object = MibTableColumn
sfifIpGroupAddr = _SfifIpGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 15),
    _SfifIpGroupAddr_Type()
)
sfifIpGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifIpGroupAddr.setStatus("mandatory")
_SfifRxForwardChars_Type = Counter32
_SfifRxForwardChars_Object = MibTableColumn
sfifRxForwardChars = _SfifRxForwardChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 16),
    _SfifRxForwardChars_Type()
)
sfifRxForwardChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxForwardChars.setStatus("mandatory")
_SfifRxFilteredChars_Type = Counter32
_SfifRxFilteredChars_Object = MibTableColumn
sfifRxFilteredChars = _SfifRxFilteredChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 17),
    _SfifRxFilteredChars_Type()
)
sfifRxFilteredChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifRxFilteredChars.setStatus("mandatory")
_SfifSpeed_Type = Integer32
_SfifSpeed_Object = MibTableColumn
sfifSpeed = _SfifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 18),
    _SfifSpeed_Type()
)
sfifSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifSpeed.setStatus("mandatory")
_SfifMgntRxQueueSize_Type = Integer32
_SfifMgntRxQueueSize_Object = MibTableColumn
sfifMgntRxQueueSize = _SfifMgntRxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 19),
    _SfifMgntRxQueueSize_Type()
)
sfifMgntRxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifMgntRxQueueSize.setStatus("mandatory")
_SfifVirtualSwitchID_Type = Integer32
_SfifVirtualSwitchID_Object = MibTableColumn
sfifVirtualSwitchID = _SfifVirtualSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 20),
    _SfifVirtualSwitchID_Type()
)
sfifVirtualSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifVirtualSwitchID.setStatus("mandatory")
_SfifTPLinkOK_Type = Integer32
_SfifTPLinkOK_Object = MibTableColumn
sfifTPLinkOK = _SfifTPLinkOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 21),
    _SfifTPLinkOK_Type()
)
sfifTPLinkOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifTPLinkOK.setStatus("mandatory")


class _SfifLedOn_Type(Integer32):
    """Custom type sfifLedOn based on Integer32"""
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


_SfifLedOn_Type.__name__ = "Integer32"
_SfifLedOn_Object = MibTableColumn
sfifLedOn = _SfifLedOn_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 22),
    _SfifLedOn_Type()
)
sfifLedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifLedOn.setStatus("mandatory")
_SfifTxCollisions_Type = Counter32
_SfifTxCollisions_Object = MibTableColumn
sfifTxCollisions = _SfifTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 23),
    _SfifTxCollisions_Type()
)
sfifTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifTxCollisions.setStatus("mandatory")


class _SfifFuseOkay_Type(Integer32):
    """Custom type sfifFuseOkay based on Integer32"""
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


_SfifFuseOkay_Type.__name__ = "Integer32"
_SfifFuseOkay_Object = MibTableColumn
sfifFuseOkay = _SfifFuseOkay_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 24),
    _SfifFuseOkay_Type()
)
sfifFuseOkay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifFuseOkay.setStatus("mandatory")
_SfifCrashEvents_Type = Counter32
_SfifCrashEvents_Object = MibTableColumn
sfifCrashEvents = _SfifCrashEvents_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 25),
    _SfifCrashEvents_Type()
)
sfifCrashEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifCrashEvents.setStatus("mandatory")
_SfifCrashTime_Type = TimeTicks
_SfifCrashTime_Object = MibTableColumn
sfifCrashTime = _SfifCrashTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 26),
    _SfifCrashTime_Type()
)
sfifCrashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifCrashTime.setStatus("mandatory")
_SfifMinimumUpTime_Type = TimeTicks
_SfifMinimumUpTime_Object = MibTableColumn
sfifMinimumUpTime = _SfifMinimumUpTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 27),
    _SfifMinimumUpTime_Type()
)
sfifMinimumUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifMinimumUpTime.setStatus("mandatory")


class _SfifDMAFlowControlEnable_Type(Integer32):
    """Custom type sfifDMAFlowControlEnable based on Integer32"""
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


_SfifDMAFlowControlEnable_Type.__name__ = "Integer32"
_SfifDMAFlowControlEnable_Object = MibTableColumn
sfifDMAFlowControlEnable = _SfifDMAFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 28),
    _SfifDMAFlowControlEnable_Type()
)
sfifDMAFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifDMAFlowControlEnable.setStatus("mandatory")
_SfifDMARetryCount_Type = Integer32
_SfifDMARetryCount_Object = MibTableColumn
sfifDMARetryCount = _SfifDMARetryCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 29),
    _SfifDMARetryCount_Type()
)
sfifDMARetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifDMARetryCount.setStatus("mandatory")
_SfifDMARetryBufferCount_Type = Integer32
_SfifDMARetryBufferCount_Object = MibTableColumn
sfifDMARetryBufferCount = _SfifDMARetryBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 30),
    _SfifDMARetryBufferCount_Type()
)
sfifDMARetryBufferCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifDMARetryBufferCount.setStatus("mandatory")
_SfifDMAPeakRetries_Type = Counter32
_SfifDMAPeakRetries_Object = MibTableColumn
sfifDMAPeakRetries = _SfifDMAPeakRetries_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 31),
    _SfifDMAPeakRetries_Type()
)
sfifDMAPeakRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifDMAPeakRetries.setStatus("mandatory")
_SfifDMATotalRetries_Type = Counter32
_SfifDMATotalRetries_Object = MibTableColumn
sfifDMATotalRetries = _SfifDMATotalRetries_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 32),
    _SfifDMATotalRetries_Type()
)
sfifDMATotalRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifDMATotalRetries.setStatus("mandatory")
_SfifDMAPackets_Type = Counter32
_SfifDMAPackets_Object = MibTableColumn
sfifDMAPackets = _SfifDMAPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 33),
    _SfifDMAPackets_Type()
)
sfifDMAPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifDMAPackets.setStatus("mandatory")
_SfifDMADroppedPackets_Type = Counter32
_SfifDMADroppedPackets_Object = MibTableColumn
sfifDMADroppedPackets = _SfifDMADroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 34),
    _SfifDMADroppedPackets_Type()
)
sfifDMADroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifDMADroppedPackets.setStatus("mandatory")
_SfifDescr_Type = DisplayString
_SfifDescr_Object = MibTableColumn
sfifDescr = _SfifDescr_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 35),
    _SfifDescr_Type()
)
sfifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifDescr.setStatus("mandatory")
_SfifMgtDroppedPackets_Type = Counter32
_SfifMgtDroppedPackets_Object = MibTableColumn
sfifMgtDroppedPackets = _SfifMgtDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 36),
    _SfifMgtDroppedPackets_Type()
)
sfifMgtDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifMgtDroppedPackets.setStatus("mandatory")
_SfifLinkStatusOutages_Type = Counter32
_SfifLinkStatusOutages_Object = MibTableColumn
sfifLinkStatusOutages = _SfifLinkStatusOutages_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 37),
    _SfifLinkStatusOutages_Type()
)
sfifLinkStatusOutages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfifLinkStatusOutages.setStatus("mandatory")


class _SfifLocalFilter_Type(Integer32):
    """Custom type sfifLocalFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2))
    )


_SfifLocalFilter_Type.__name__ = "Integer32"
_SfifLocalFilter_Object = MibTableColumn
sfifLocalFilter = _SfifLocalFilter_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 6, 1, 1, 38),
    _SfifLocalFilter_Type()
)
sfifLocalFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfifLocalFilter.setStatus("mandatory")
_Sfuart_ObjectIdentity = ObjectIdentity
sfuart = _Sfuart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7)
)
_SfuartTable_Object = MibTable
sfuartTable = _SfuartTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1)
)
if mibBuilder.loadTexts:
    sfuartTable.setStatus("mandatory")
_SfuartEntry_Object = MibTableRow
sfuartEntry = _SfuartEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1, 1)
)
sfuartEntry.setIndexNames(
    (0, "FN100-MIB", "sfuartIndex"),
)
if mibBuilder.loadTexts:
    sfuartEntry.setStatus("mandatory")
_SfuartIndex_Type = Integer32
_SfuartIndex_Object = MibTableColumn
sfuartIndex = _SfuartIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1, 1, 1),
    _SfuartIndex_Type()
)
sfuartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfuartIndex.setStatus("mandatory")


class _SfuartBaud_Type(Integer32):
    """Custom type sfuartBaud based on Integer32"""
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


_SfuartBaud_Type.__name__ = "Integer32"
_SfuartBaud_Object = MibTableColumn
sfuartBaud = _SfuartBaud_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1, 1, 2),
    _SfuartBaud_Type()
)
sfuartBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfuartBaud.setStatus("mandatory")
_SfuartAlignmentErrors_Type = Counter32
_SfuartAlignmentErrors_Object = MibTableColumn
sfuartAlignmentErrors = _SfuartAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1, 1, 3),
    _SfuartAlignmentErrors_Type()
)
sfuartAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfuartAlignmentErrors.setStatus("mandatory")
_SfuartOverrunErrors_Type = Counter32
_SfuartOverrunErrors_Object = MibTableColumn
sfuartOverrunErrors = _SfuartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 7, 1, 1, 4),
    _SfuartOverrunErrors_Type()
)
sfuartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfuartOverrunErrors.setStatus("mandatory")
_Sfdebug_ObjectIdentity = ObjectIdentity
sfdebug = _Sfdebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8)
)
_SfdebugStringID_Type = Integer32
_SfdebugStringID_Object = MibScalar
sfdebugStringID = _SfdebugStringID_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 1),
    _SfdebugStringID_Type()
)
sfdebugStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdebugStringID.setStatus("mandatory")
_SfdebugString_Type = OctetString
_SfdebugString_Object = MibScalar
sfdebugString = _SfdebugString_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 2),
    _SfdebugString_Type()
)
sfdebugString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdebugString.setStatus("mandatory")
_SfdebugTable_Object = MibTable
sfdebugTable = _SfdebugTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3)
)
if mibBuilder.loadTexts:
    sfdebugTable.setStatus("mandatory")
_SfdebugEntry_Object = MibTableRow
sfdebugEntry = _SfdebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1)
)
sfdebugEntry.setIndexNames(
    (0, "FN100-MIB", "sfdebugIndex"),
)
if mibBuilder.loadTexts:
    sfdebugEntry.setStatus("mandatory")


class _SfdebugIndex_Type(Integer32):
    """Custom type sfdebugIndex based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("debug-mp", 100),
          ("debug-port1", 1),
          ("debug-port10", 10),
          ("debug-port11", 11),
          ("debug-port12", 12),
          ("debug-port2", 2),
          ("debug-port3", 3),
          ("debug-port4", 4),
          ("debug-port5", 5),
          ("debug-port6", 6),
          ("debug-port7", 7),
          ("debug-port8", 8),
          ("debug-port9", 9))
    )


_SfdebugIndex_Type.__name__ = "Integer32"
_SfdebugIndex_Object = MibTableColumn
sfdebugIndex = _SfdebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1, 1),
    _SfdebugIndex_Type()
)
sfdebugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdebugIndex.setStatus("mandatory")


class _SfdebugOperation_Type(Integer32):
    """Custom type sfdebugOperation based on Integer32"""
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


_SfdebugOperation_Type.__name__ = "Integer32"
_SfdebugOperation_Object = MibTableColumn
sfdebugOperation = _SfdebugOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1, 2),
    _SfdebugOperation_Type()
)
sfdebugOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdebugOperation.setStatus("mandatory")
_SfdebugBase_Type = Integer32
_SfdebugBase_Object = MibTableColumn
sfdebugBase = _SfdebugBase_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1, 3),
    _SfdebugBase_Type()
)
sfdebugBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdebugBase.setStatus("mandatory")
_SfdebugLength_Type = Integer32
_SfdebugLength_Object = MibTableColumn
sfdebugLength = _SfdebugLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1, 4),
    _SfdebugLength_Type()
)
sfdebugLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdebugLength.setStatus("mandatory")
_SfdebugData_Type = OctetString
_SfdebugData_Object = MibTableColumn
sfdebugData = _SfdebugData_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 8, 3, 1, 5),
    _SfdebugData_Type()
)
sfdebugData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdebugData.setStatus("mandatory")
_Sfproto_ObjectIdentity = ObjectIdentity
sfproto = _Sfproto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9)
)
_SfprotoTable_Object = MibTable
sfprotoTable = _SfprotoTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1)
)
if mibBuilder.loadTexts:
    sfprotoTable.setStatus("mandatory")
_SfprotoEntry_Object = MibTableRow
sfprotoEntry = _SfprotoEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1)
)
sfprotoEntry.setIndexNames(
    (0, "FN100-MIB", "sfprotoIfIndex"),
)
if mibBuilder.loadTexts:
    sfprotoEntry.setStatus("mandatory")
_SfprotoIfIndex_Type = Integer32
_SfprotoIfIndex_Object = MibTableColumn
sfprotoIfIndex = _SfprotoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1, 1),
    _SfprotoIfIndex_Type()
)
sfprotoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfprotoIfIndex.setStatus("mandatory")


class _SfprotoBridge_Type(Integer32):
    """Custom type sfprotoBridge based on Integer32"""
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


_SfprotoBridge_Type.__name__ = "Integer32"
_SfprotoBridge_Object = MibTableColumn
sfprotoBridge = _SfprotoBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1, 2),
    _SfprotoBridge_Type()
)
sfprotoBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfprotoBridge.setStatus("mandatory")


class _SfprotoSuppressBpdu_Type(Integer32):
    """Custom type sfprotoSuppressBpdu based on Integer32"""
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


_SfprotoSuppressBpdu_Type.__name__ = "Integer32"
_SfprotoSuppressBpdu_Object = MibTableColumn
sfprotoSuppressBpdu = _SfprotoSuppressBpdu_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1, 3),
    _SfprotoSuppressBpdu_Type()
)
sfprotoSuppressBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfprotoSuppressBpdu.setStatus("mandatory")


class _SfprotoRipListen_Type(Integer32):
    """Custom type sfprotoRipListen based on Integer32"""
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


_SfprotoRipListen_Type.__name__ = "Integer32"
_SfprotoRipListen_Object = MibTableColumn
sfprotoRipListen = _SfprotoRipListen_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1, 4),
    _SfprotoRipListen_Type()
)
sfprotoRipListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfprotoRipListen.setStatus("mandatory")


class _SfprotoTrunking_Type(Integer32):
    """Custom type sfprotoTrunking based on Integer32"""
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


_SfprotoTrunking_Type.__name__ = "Integer32"
_SfprotoTrunking_Object = MibTableColumn
sfprotoTrunking = _SfprotoTrunking_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 9, 1, 1, 5),
    _SfprotoTrunking_Type()
)
sfprotoTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfprotoTrunking.setStatus("mandatory")
_Sftrunk_ObjectIdentity = ObjectIdentity
sftrunk = _Sftrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10)
)
_SftrunkTable_Object = MibTable
sftrunkTable = _SftrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1)
)
if mibBuilder.loadTexts:
    sftrunkTable.setStatus("mandatory")
_SftrunkEntry_Object = MibTableRow
sftrunkEntry = _SftrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1)
)
sftrunkEntry.setIndexNames(
    (0, "FN100-MIB", "sftrunkIfIndex"),
)
if mibBuilder.loadTexts:
    sftrunkEntry.setStatus("mandatory")
_SftrunkIfIndex_Type = Integer32
_SftrunkIfIndex_Object = MibTableColumn
sftrunkIfIndex = _SftrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 1),
    _SftrunkIfIndex_Type()
)
sftrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkIfIndex.setStatus("mandatory")


class _SftrunkState_Type(Integer32):
    """Custom type sftrunkState based on Integer32"""
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
        *(("closed", 1),
          ("helddown", 4),
          ("joined", 3),
          ("oneway", 2))
    )


_SftrunkState_Type.__name__ = "Integer32"
_SftrunkState_Object = MibTableColumn
sftrunkState = _SftrunkState_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 2),
    _SftrunkState_Type()
)
sftrunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkState.setStatus("mandatory")
_SftrunkRemoteBridgeId_Type = OctetString
_SftrunkRemoteBridgeId_Object = MibTableColumn
sftrunkRemoteBridgeId = _SftrunkRemoteBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 3),
    _SftrunkRemoteBridgeId_Type()
)
sftrunkRemoteBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkRemoteBridgeId.setStatus("mandatory")
_SftrunkRemoteIp_Type = IpAddress
_SftrunkRemoteIp_Object = MibTableColumn
sftrunkRemoteIp = _SftrunkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 4),
    _SftrunkRemoteIp_Type()
)
sftrunkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkRemoteIp.setStatus("mandatory")


class _SftrunkLastError_Type(Integer32):
    """Custom type sftrunkLastError based on Integer32"""
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
        *(("in-bpdu", 2),
          ("multiple-bridges", 3),
          ("no-ack", 4),
          ("none", 1))
    )


_SftrunkLastError_Type.__name__ = "Integer32"
_SftrunkLastError_Object = MibTableColumn
sftrunkLastError = _SftrunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 5),
    _SftrunkLastError_Type()
)
sftrunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkLastError.setStatus("mandatory")
_SftrunkLinkOrdinal_Type = Integer32
_SftrunkLinkOrdinal_Object = MibTableColumn
sftrunkLinkOrdinal = _SftrunkLinkOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 6),
    _SftrunkLinkOrdinal_Type()
)
sftrunkLinkOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkLinkOrdinal.setStatus("mandatory")
_SftrunkLinkCount_Type = Integer32
_SftrunkLinkCount_Object = MibTableColumn
sftrunkLinkCount = _SftrunkLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 7),
    _SftrunkLinkCount_Type()
)
sftrunkLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkLinkCount.setStatus("mandatory")
_SftrunkLastChange_Type = Integer32
_SftrunkLastChange_Object = MibTableColumn
sftrunkLastChange = _SftrunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 10, 1, 1, 8),
    _SftrunkLastChange_Type()
)
sftrunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftrunkLastChange.setStatus("mandatory")
_SfworkGroup_ObjectIdentity = ObjectIdentity
sfworkGroup = _SfworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11)
)
_SfworkGroupNextIndex_Type = Integer32
_SfworkGroupNextIndex_Object = MibScalar
sfworkGroupNextIndex = _SfworkGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 1),
    _SfworkGroupNextIndex_Type()
)
sfworkGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfworkGroupNextIndex.setStatus("mandatory")
_SfworkGroupCurrentCounts_Type = Integer32
_SfworkGroupCurrentCounts_Object = MibScalar
sfworkGroupCurrentCounts = _SfworkGroupCurrentCounts_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 2),
    _SfworkGroupCurrentCounts_Type()
)
sfworkGroupCurrentCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfworkGroupCurrentCounts.setStatus("mandatory")
_SfworkGroupMaxCount_Type = Integer32
_SfworkGroupMaxCount_Object = MibScalar
sfworkGroupMaxCount = _SfworkGroupMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 3),
    _SfworkGroupMaxCount_Type()
)
sfworkGroupMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfworkGroupMaxCount.setStatus("mandatory")
_SfworkGroupTable_Object = MibTable
sfworkGroupTable = _SfworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4)
)
if mibBuilder.loadTexts:
    sfworkGroupTable.setStatus("mandatory")
_SfworkGroupEntry_Object = MibTableRow
sfworkGroupEntry = _SfworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4, 1)
)
sfworkGroupEntry.setIndexNames(
    (0, "FN100-MIB", "sfworkGroupIndex"),
)
if mibBuilder.loadTexts:
    sfworkGroupEntry.setStatus("mandatory")
_SfworkGroupIndex_Type = Integer32
_SfworkGroupIndex_Object = MibTableColumn
sfworkGroupIndex = _SfworkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4, 1, 1),
    _SfworkGroupIndex_Type()
)
sfworkGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfworkGroupIndex.setStatus("mandatory")
_SfworkGroupName_Type = DisplayString
_SfworkGroupName_Object = MibTableColumn
sfworkGroupName = _SfworkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4, 1, 2),
    _SfworkGroupName_Type()
)
sfworkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfworkGroupName.setStatus("mandatory")


class _SfworkGroupType_Type(Integer32):
    """Custom type sfworkGroupType based on Integer32"""
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
        *(("workgroup-all", 1),
          ("workgroup-invalid", 4),
          ("workgroup-multicast", 2),
          ("workgroup-unicast", 3))
    )


_SfworkGroupType_Type.__name__ = "Integer32"
_SfworkGroupType_Object = MibTableColumn
sfworkGroupType = _SfworkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4, 1, 3),
    _SfworkGroupType_Type()
)
sfworkGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfworkGroupType.setStatus("mandatory")
_SfworkGroupPort_Type = OctetString
_SfworkGroupPort_Object = MibTableColumn
sfworkGroupPort = _SfworkGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 5, 3, 11, 4, 1, 4),
    _SfworkGroupPort_Type()
)
sfworkGroupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfworkGroupPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FN100-MIB",
    **{"cmu": cmu,
       "systems": systems,
       "cmuSNMP": cmuSNMP,
       "cmuKip": cmuKip,
       "cmuRouter": cmuRouter,
       "mibs": mibs,
       "sigma": sigma,
       "sys": sys,
       "sysID": sysID,
       "sysReset": sysReset,
       "sysTrapAck": sysTrapAck,
       "sysTrapTime": sysTrapTime,
       "sysTrapRetry": sysTrapRetry,
       "sysTrapPort": sysTrapPort,
       "platform": platform,
       "es-1fe": es_1fe,
       "sfhw": sfhw,
       "sfhwDiagCode": sfhwDiagCode,
       "sfhwManufData": sfhwManufData,
       "sfhwPortCount": sfhwPortCount,
       "sfhwPortTable": sfhwPortTable,
       "sfhwPortEntry": sfhwPortEntry,
       "sfhwPortIndex": sfhwPortIndex,
       "sfhwPortType": sfhwPortType,
       "sfhwPortSubType": sfhwPortSubType,
       "sfhwPortDiagPassed": sfhwPortDiagPassed,
       "sfhwAddr": sfhwAddr,
       "sfsw": sfsw,
       "sfswNumber": sfswNumber,
       "sfswFilesetTable": sfswFilesetTable,
       "sfswFileset": sfswFileset,
       "sfswIndex": sfswIndex,
       "sfswDesc": sfswDesc,
       "sfswCount": sfswCount,
       "sfswType": sfswType,
       "sfswSizes": sfswSizes,
       "sfswStarts": sfswStarts,
       "sfswBases": sfswBases,
       "sfswFlashBank": sfswFlashBank,
       "sfadmin": sfadmin,
       "sfadminFatalErr": sfadminFatalErr,
       "sfadminAnyPass": sfadminAnyPass,
       "sfadminGetPass": sfadminGetPass,
       "sfadminNMSIPAddr": sfadminNMSIPAddr,
       "sfadminAlarmDynamic": sfadminAlarmDynamic,
       "sfadminAlarmAddressChange": sfadminAlarmAddressChange,
       "sfadminStorageFailure": sfadminStorageFailure,
       "sfadminAuthenticationFailure": sfadminAuthenticationFailure,
       "sfadminMPReceiveCongests": sfadminMPReceiveCongests,
       "sfadminArpEntries": sfadminArpEntries,
       "sfadminArpStatics": sfadminArpStatics,
       "sfadminArpOverflows": sfadminArpOverflows,
       "sfadminIpEntries": sfadminIpEntries,
       "sfadminIpStatics": sfadminIpStatics,
       "sfadminStaticPreference": sfadminStaticPreference,
       "sfadminRipPreference": sfadminRipPreference,
       "sfadminRipRouteDiscards": sfadminRipRouteDiscards,
       "sfadminRebootConfig": sfadminRebootConfig,
       "sfadminTempOK": sfadminTempOK,
       "sfadminDisableButton": sfadminDisableButton,
       "sfadminButtonSelection": sfadminButtonSelection,
       "sfadminLEDProgramOption": sfadminLEDProgramOption,
       "sfadminVirtualSwitch1": sfadminVirtualSwitch1,
       "sfadminVirtualSwitch2": sfadminVirtualSwitch2,
       "sfadminVirtualSwitch3": sfadminVirtualSwitch3,
       "sfadminVirtualSwitch4": sfadminVirtualSwitch4,
       "sfadminDefaultVirtualSwitch": sfadminDefaultVirtualSwitch,
       "sfswdis": sfswdis,
       "sfswdisDesc": sfswdisDesc,
       "sfswdisAccess": sfswdisAccess,
       "sfswdisWriteStatus": sfswdisWriteStatus,
       "sfswdisConfigIp": sfswdisConfigIp,
       "sfswdisConfigRetryTime": sfswdisConfigRetryTime,
       "sfswdisConfigTotalTimeout": sfswdisConfigTotalTimeout,
       "sfaddr": sfaddr,
       "sfaddrDynamics": sfaddrDynamics,
       "sfaddrDynamicMax": sfaddrDynamicMax,
       "sfaddrFlags": sfaddrFlags,
       "sfaddrMAC": sfaddrMAC,
       "sfaddrPort": sfaddrPort,
       "sfaddrOperation": sfaddrOperation,
       "sfaddrIndex": sfaddrIndex,
       "sfaddrNext": sfaddrNext,
       "sfaddrBlockSize": sfaddrBlockSize,
       "sfaddrBlock": sfaddrBlock,
       "sfaddrAlarmMAC": sfaddrAlarmMAC,
       "sfaddrDbFullBuckets": sfaddrDbFullBuckets,
       "sfaddrDbMaxFullBuckets": sfaddrDbMaxFullBuckets,
       "sfaddrDbMaxSize": sfaddrDbMaxSize,
       "sfaddrDbBuckets": sfaddrDbBuckets,
       "sfaddrDbSearchDepth": sfaddrDbSearchDepth,
       "sfaddrDbDistribution": sfaddrDbDistribution,
       "sfaddrDbTable": sfaddrDbTable,
       "sfaddrDbEntry": sfaddrDbEntry,
       "sfaddrDbBucketAddress": sfaddrDbBucketAddress,
       "sfaddrDbBucketEntCnt": sfaddrDbBucketEntCnt,
       "sfaddrDbBucketEntries": sfaddrDbBucketEntries,
       "sfif": sfif,
       "sfifTable": sfifTable,
       "sfifEntry": sfifEntry,
       "sfifIndex": sfifIndex,
       "sfifRxCnt": sfifRxCnt,
       "sfifTxCnt": sfifTxCnt,
       "sfifTxStormCnt": sfifTxStormCnt,
       "sfifTxStormTime": sfifTxStormTime,
       "sfifFilterFloodSourceSame": sfifFilterFloodSourceSame,
       "sfifFunction": sfifFunction,
       "sfifRxPacket": sfifRxPacket,
       "sfifRxHwFCSs": sfifRxHwFCSs,
       "sfifRxQueues": sfifRxQueues,
       "sfifTxPacket": sfifTxPacket,
       "sfifTxStorms": sfifTxStorms,
       "sfifStatisticsTime": sfifStatisticsTime,
       "sfifIpAddr": sfifIpAddr,
       "sfifIpGroupAddr": sfifIpGroupAddr,
       "sfifRxForwardChars": sfifRxForwardChars,
       "sfifRxFilteredChars": sfifRxFilteredChars,
       "sfifSpeed": sfifSpeed,
       "sfifMgntRxQueueSize": sfifMgntRxQueueSize,
       "sfifVirtualSwitchID": sfifVirtualSwitchID,
       "sfifTPLinkOK": sfifTPLinkOK,
       "sfifLedOn": sfifLedOn,
       "sfifTxCollisions": sfifTxCollisions,
       "sfifFuseOkay": sfifFuseOkay,
       "sfifCrashEvents": sfifCrashEvents,
       "sfifCrashTime": sfifCrashTime,
       "sfifMinimumUpTime": sfifMinimumUpTime,
       "sfifDMAFlowControlEnable": sfifDMAFlowControlEnable,
       "sfifDMARetryCount": sfifDMARetryCount,
       "sfifDMARetryBufferCount": sfifDMARetryBufferCount,
       "sfifDMAPeakRetries": sfifDMAPeakRetries,
       "sfifDMATotalRetries": sfifDMATotalRetries,
       "sfifDMAPackets": sfifDMAPackets,
       "sfifDMADroppedPackets": sfifDMADroppedPackets,
       "sfifDescr": sfifDescr,
       "sfifMgtDroppedPackets": sfifMgtDroppedPackets,
       "sfifLinkStatusOutages": sfifLinkStatusOutages,
       "sfifLocalFilter": sfifLocalFilter,
       "sfuart": sfuart,
       "sfuartTable": sfuartTable,
       "sfuartEntry": sfuartEntry,
       "sfuartIndex": sfuartIndex,
       "sfuartBaud": sfuartBaud,
       "sfuartAlignmentErrors": sfuartAlignmentErrors,
       "sfuartOverrunErrors": sfuartOverrunErrors,
       "sfdebug": sfdebug,
       "sfdebugStringID": sfdebugStringID,
       "sfdebugString": sfdebugString,
       "sfdebugTable": sfdebugTable,
       "sfdebugEntry": sfdebugEntry,
       "sfdebugIndex": sfdebugIndex,
       "sfdebugOperation": sfdebugOperation,
       "sfdebugBase": sfdebugBase,
       "sfdebugLength": sfdebugLength,
       "sfdebugData": sfdebugData,
       "sfproto": sfproto,
       "sfprotoTable": sfprotoTable,
       "sfprotoEntry": sfprotoEntry,
       "sfprotoIfIndex": sfprotoIfIndex,
       "sfprotoBridge": sfprotoBridge,
       "sfprotoSuppressBpdu": sfprotoSuppressBpdu,
       "sfprotoRipListen": sfprotoRipListen,
       "sfprotoTrunking": sfprotoTrunking,
       "sftrunk": sftrunk,
       "sftrunkTable": sftrunkTable,
       "sftrunkEntry": sftrunkEntry,
       "sftrunkIfIndex": sftrunkIfIndex,
       "sftrunkState": sftrunkState,
       "sftrunkRemoteBridgeId": sftrunkRemoteBridgeId,
       "sftrunkRemoteIp": sftrunkRemoteIp,
       "sftrunkLastError": sftrunkLastError,
       "sftrunkLinkOrdinal": sftrunkLinkOrdinal,
       "sftrunkLinkCount": sftrunkLinkCount,
       "sftrunkLastChange": sftrunkLastChange,
       "sfworkGroup": sfworkGroup,
       "sfworkGroupNextIndex": sfworkGroupNextIndex,
       "sfworkGroupCurrentCounts": sfworkGroupCurrentCounts,
       "sfworkGroupMaxCount": sfworkGroupMaxCount,
       "sfworkGroupTable": sfworkGroupTable,
       "sfworkGroupEntry": sfworkGroupEntry,
       "sfworkGroupIndex": sfworkGroupIndex,
       "sfworkGroupName": sfworkGroupName,
       "sfworkGroupType": sfworkGroupType,
       "sfworkGroupPort": sfworkGroupPort}
)
