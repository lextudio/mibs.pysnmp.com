# SNMP MIB module (CT-ELS10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-ELS10-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:08 2024
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
            7
        )
    )
    namedValues = NamedValues(
        ("els10-27-bridge", 7)
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
    (1, 3, 6, 1, 4, 1, 97, 1, 6),
    _SysTrapPort_Type()
)
sysTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPort.setStatus("mandatory")
_Els10_27_ObjectIdentity = ObjectIdentity
els10_27 = _Els10_27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9)
)
_Els10_27hw_ObjectIdentity = ObjectIdentity
els10_27hw = _Els10_27hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 1)
)
_Els10_27hwDiagCode_Type = OctetString
_Els10_27hwDiagCode_Object = MibScalar
els10_27hwDiagCode = _Els10_27hwDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 1),
    _Els10_27hwDiagCode_Type()
)
els10_27hwDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwDiagCode.setStatus("mandatory")
_Els10_27hwManufData_Type = OctetString
_Els10_27hwManufData_Object = MibScalar
els10_27hwManufData = _Els10_27hwManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 2),
    _Els10_27hwManufData_Type()
)
els10_27hwManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwManufData.setStatus("mandatory")
_Els10_27hwPortCount_Type = Integer32
_Els10_27hwPortCount_Object = MibScalar
els10_27hwPortCount = _Els10_27hwPortCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 3),
    _Els10_27hwPortCount_Type()
)
els10_27hwPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwPortCount.setStatus("mandatory")
_Els10_27hwPortTable_Object = MibTable
els10_27hwPortTable = _Els10_27hwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4)
)
if mibBuilder.loadTexts:
    els10_27hwPortTable.setStatus("mandatory")
_Els10_27hwPortEntry_Object = MibTableRow
els10_27hwPortEntry = _Els10_27hwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1)
)
els10_27hwPortEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27hwPortIndex"),
)
if mibBuilder.loadTexts:
    els10_27hwPortEntry.setStatus("mandatory")
_Els10_27hwPortIndex_Type = Integer32
_Els10_27hwPortIndex_Object = MibScalar
els10_27hwPortIndex = _Els10_27hwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1, 1),
    _Els10_27hwPortIndex_Type()
)
els10_27hwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwPortIndex.setStatus("mandatory")


class _Els10_27hwPortType_Type(Integer32):
    """Custom type els10_27hwPortType based on Integer32"""
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


_Els10_27hwPortType_Type.__name__ = "Integer32"
_Els10_27hwPortType_Object = MibScalar
els10_27hwPortType = _Els10_27hwPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1, 2),
    _Els10_27hwPortType_Type()
)
els10_27hwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwPortType.setStatus("mandatory")


class _Els10_27hwPortSubType_Type(Integer32):
    """Custom type els10_27hwPortSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              16,
              17,
              80,
              255)
        )
    )
    namedValues = NamedValues(
        *(("csmacd-100-fx", 17),
          ("csmacd-100-tpx", 16),
          ("csmacd-tpx", 13),
          ("no-information", 255),
          ("uart-female-9pin", 80))
    )


_Els10_27hwPortSubType_Type.__name__ = "Integer32"
_Els10_27hwPortSubType_Object = MibScalar
els10_27hwPortSubType = _Els10_27hwPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1, 3),
    _Els10_27hwPortSubType_Type()
)
els10_27hwPortSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwPortSubType.setStatus("mandatory")


class _Els10_27hwPortDiagPassed_Type(Integer32):
    """Custom type els10_27hwPortDiagPassed based on Integer32"""
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


_Els10_27hwPortDiagPassed_Type.__name__ = "Integer32"
_Els10_27hwPortDiagPassed_Object = MibScalar
els10_27hwPortDiagPassed = _Els10_27hwPortDiagPassed_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1, 4),
    _Els10_27hwPortDiagPassed_Type()
)
els10_27hwPortDiagPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwPortDiagPassed.setStatus("mandatory")
_Els10_27hwAddr_Type = OctetString
_Els10_27hwAddr_Object = MibScalar
els10_27hwAddr = _Els10_27hwAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 4, 1, 5),
    _Els10_27hwAddr_Type()
)
els10_27hwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwAddr.setStatus("mandatory")


class _Els10_27hwUpLink_Type(Integer32):
    """Custom type els10_27hwUpLink based on Integer32"""
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


_Els10_27hwUpLink_Type.__name__ = "Integer32"
_Els10_27hwUpLink_Object = MibScalar
els10_27hwUpLink = _Els10_27hwUpLink_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 5),
    _Els10_27hwUpLink_Type()
)
els10_27hwUpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwUpLink.setStatus("mandatory")
_Els10_27hwUpLinkManufData_Type = OctetString
_Els10_27hwUpLinkManufData_Object = MibScalar
els10_27hwUpLinkManufData = _Els10_27hwUpLinkManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 1, 6),
    _Els10_27hwUpLinkManufData_Type()
)
els10_27hwUpLinkManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27hwUpLinkManufData.setStatus("mandatory")
_Els10_27sw_ObjectIdentity = ObjectIdentity
els10_27sw = _Els10_27sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 2)
)
_Els10_27swNumber_Type = Integer32
_Els10_27swNumber_Object = MibScalar
els10_27swNumber = _Els10_27swNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 1),
    _Els10_27swNumber_Type()
)
els10_27swNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swNumber.setStatus("mandatory")
_Els10_27swFilesetTable_Object = MibTable
els10_27swFilesetTable = _Els10_27swFilesetTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2)
)
if mibBuilder.loadTexts:
    els10_27swFilesetTable.setStatus("mandatory")
_Els10_27swFilesetEntry_Object = MibTableRow
els10_27swFilesetEntry = _Els10_27swFilesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1)
)
els10_27swFilesetEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27swIndex"),
)
if mibBuilder.loadTexts:
    els10_27swFilesetEntry.setStatus("mandatory")


class _Els10_27swIndex_Type(Integer32):
    """Custom type els10_27swIndex based on Integer32"""
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


_Els10_27swIndex_Type.__name__ = "Integer32"
_Els10_27swIndex_Object = MibScalar
els10_27swIndex = _Els10_27swIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 1),
    _Els10_27swIndex_Type()
)
els10_27swIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swIndex.setStatus("mandatory")
_Els10_27swDesc_Type = DisplayString
_Els10_27swDesc_Object = MibScalar
els10_27swDesc = _Els10_27swDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 2),
    _Els10_27swDesc_Type()
)
els10_27swDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swDesc.setStatus("mandatory")
_Els10_27swCount_Type = Integer32
_Els10_27swCount_Object = MibScalar
els10_27swCount = _Els10_27swCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 3),
    _Els10_27swCount_Type()
)
els10_27swCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swCount.setStatus("mandatory")
_Els10_27swType_Type = OctetString
_Els10_27swType_Object = MibScalar
els10_27swType = _Els10_27swType_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 4),
    _Els10_27swType_Type()
)
els10_27swType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swType.setStatus("mandatory")
_Els10_27swSizes_Type = OctetString
_Els10_27swSizes_Object = MibScalar
els10_27swSizes = _Els10_27swSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 5),
    _Els10_27swSizes_Type()
)
els10_27swSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swSizes.setStatus("mandatory")
_Els10_27swStarts_Type = OctetString
_Els10_27swStarts_Object = MibScalar
els10_27swStarts = _Els10_27swStarts_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 6),
    _Els10_27swStarts_Type()
)
els10_27swStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swStarts.setStatus("mandatory")
_Els10_27swBases_Type = OctetString
_Els10_27swBases_Object = MibScalar
els10_27swBases = _Els10_27swBases_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 7),
    _Els10_27swBases_Type()
)
els10_27swBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swBases.setStatus("mandatory")


class _Els10_27swFlashBank_Type(Integer32):
    """Custom type els10_27swFlashBank based on Integer32"""
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


_Els10_27swFlashBank_Type.__name__ = "Integer32"
_Els10_27swFlashBank_Object = MibScalar
els10_27swFlashBank = _Els10_27swFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 2, 2, 1, 8),
    _Els10_27swFlashBank_Type()
)
els10_27swFlashBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swFlashBank.setStatus("mandatory")
_Els10_27admin_ObjectIdentity = ObjectIdentity
els10_27admin = _Els10_27admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 3)
)
_Els10_27adminFatalErr_Type = OctetString
_Els10_27adminFatalErr_Object = MibScalar
els10_27adminFatalErr = _Els10_27adminFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 1),
    _Els10_27adminFatalErr_Type()
)
els10_27adminFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminFatalErr.setStatus("mandatory")
_Els10_27adminAnyPass_Type = OctetString
_Els10_27adminAnyPass_Object = MibScalar
els10_27adminAnyPass = _Els10_27adminAnyPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 2),
    _Els10_27adminAnyPass_Type()
)
els10_27adminAnyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminAnyPass.setStatus("mandatory")
_Els10_27adminGetPass_Type = OctetString
_Els10_27adminGetPass_Object = MibScalar
els10_27adminGetPass = _Els10_27adminGetPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 3),
    _Els10_27adminGetPass_Type()
)
els10_27adminGetPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminGetPass.setStatus("mandatory")
_Els10_27adminNMSIPAddr_Type = IpAddress
_Els10_27adminNMSIPAddr_Object = MibScalar
els10_27adminNMSIPAddr = _Els10_27adminNMSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 4),
    _Els10_27adminNMSIPAddr_Type()
)
els10_27adminNMSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminNMSIPAddr.setStatus("mandatory")


class _Els10_27adminStorageFailure_Type(Integer32):
    """Custom type els10_27adminStorageFailure based on Integer32"""
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


_Els10_27adminStorageFailure_Type.__name__ = "Integer32"
_Els10_27adminStorageFailure_Object = MibScalar
els10_27adminStorageFailure = _Els10_27adminStorageFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 7),
    _Els10_27adminStorageFailure_Type()
)
els10_27adminStorageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminStorageFailure.setStatus("mandatory")
_Els10_27adminAuthenticationFailure_Type = IpAddress
_Els10_27adminAuthenticationFailure_Object = MibScalar
els10_27adminAuthenticationFailure = _Els10_27adminAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 8),
    _Els10_27adminAuthenticationFailure_Type()
)
els10_27adminAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminAuthenticationFailure.setStatus("mandatory")
_Els10_27adminNAMReceiveCongests_Type = Counter32
_Els10_27adminNAMReceiveCongests_Object = MibScalar
els10_27adminNAMReceiveCongests = _Els10_27adminNAMReceiveCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 10),
    _Els10_27adminNAMReceiveCongests_Type()
)
els10_27adminNAMReceiveCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminNAMReceiveCongests.setStatus("mandatory")
_Els10_27adminArpEntries_Type = Counter32
_Els10_27adminArpEntries_Object = MibScalar
els10_27adminArpEntries = _Els10_27adminArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 11),
    _Els10_27adminArpEntries_Type()
)
els10_27adminArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminArpEntries.setStatus("mandatory")
_Els10_27adminArpStatics_Type = Counter32
_Els10_27adminArpStatics_Object = MibScalar
els10_27adminArpStatics = _Els10_27adminArpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 12),
    _Els10_27adminArpStatics_Type()
)
els10_27adminArpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminArpStatics.setStatus("mandatory")
_Els10_27adminArpOverflows_Type = Counter32
_Els10_27adminArpOverflows_Object = MibScalar
els10_27adminArpOverflows = _Els10_27adminArpOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 13),
    _Els10_27adminArpOverflows_Type()
)
els10_27adminArpOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminArpOverflows.setStatus("mandatory")
_Els10_27adminIpEntries_Type = Counter32
_Els10_27adminIpEntries_Object = MibScalar
els10_27adminIpEntries = _Els10_27adminIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 14),
    _Els10_27adminIpEntries_Type()
)
els10_27adminIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminIpEntries.setStatus("mandatory")
_Els10_27adminIpStatics_Type = Counter32
_Els10_27adminIpStatics_Object = MibScalar
els10_27adminIpStatics = _Els10_27adminIpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 15),
    _Els10_27adminIpStatics_Type()
)
els10_27adminIpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminIpStatics.setStatus("mandatory")
_Els10_27adminStaticPreference_Type = Integer32
_Els10_27adminStaticPreference_Object = MibScalar
els10_27adminStaticPreference = _Els10_27adminStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 16),
    _Els10_27adminStaticPreference_Type()
)
els10_27adminStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminStaticPreference.setStatus("mandatory")
_Els10_27adminRipPreference_Type = Integer32
_Els10_27adminRipPreference_Object = MibScalar
els10_27adminRipPreference = _Els10_27adminRipPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 17),
    _Els10_27adminRipPreference_Type()
)
els10_27adminRipPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminRipPreference.setStatus("mandatory")
_Els10_27adminRipRouteDiscards_Type = Counter32
_Els10_27adminRipRouteDiscards_Object = MibScalar
els10_27adminRipRouteDiscards = _Els10_27adminRipRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 18),
    _Els10_27adminRipRouteDiscards_Type()
)
els10_27adminRipRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27adminRipRouteDiscards.setStatus("mandatory")


class _Els10_27adminRebootConfig_Type(Integer32):
    """Custom type els10_27adminRebootConfig based on Integer32"""
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


_Els10_27adminRebootConfig_Type.__name__ = "Integer32"
_Els10_27adminRebootConfig_Object = MibScalar
els10_27adminRebootConfig = _Els10_27adminRebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 19),
    _Els10_27adminRebootConfig_Type()
)
els10_27adminRebootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminRebootConfig.setStatus("mandatory")


class _Els10_27adminDisableButton_Type(Integer32):
    """Custom type els10_27adminDisableButton based on Integer32"""
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


_Els10_27adminDisableButton_Type.__name__ = "Integer32"
_Els10_27adminDisableButton_Object = MibScalar
els10_27adminDisableButton = _Els10_27adminDisableButton_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 21),
    _Els10_27adminDisableButton_Type()
)
els10_27adminDisableButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminDisableButton.setStatus("mandatory")


class _Els10_27adminButtonSelection_Type(Integer32):
    """Custom type els10_27adminButtonSelection based on Integer32"""
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


_Els10_27adminButtonSelection_Type.__name__ = "Integer32"
_Els10_27adminButtonSelection_Object = MibScalar
els10_27adminButtonSelection = _Els10_27adminButtonSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 22),
    _Els10_27adminButtonSelection_Type()
)
els10_27adminButtonSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminButtonSelection.setStatus("mandatory")


class _Els10_27adminLEDProgramOption_Type(Integer32):
    """Custom type els10_27adminLEDProgramOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("program-led-any-error", 1)
    )


_Els10_27adminLEDProgramOption_Type.__name__ = "Integer32"
_Els10_27adminLEDProgramOption_Object = MibScalar
els10_27adminLEDProgramOption = _Els10_27adminLEDProgramOption_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 3, 23),
    _Els10_27adminLEDProgramOption_Type()
)
els10_27adminLEDProgramOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27adminLEDProgramOption.setStatus("mandatory")
_Els10_27swdis_ObjectIdentity = ObjectIdentity
els10_27swdis = _Els10_27swdis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 4)
)
_Els10_27swdisDesc_Type = OctetString
_Els10_27swdisDesc_Object = MibScalar
els10_27swdisDesc = _Els10_27swdisDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 1),
    _Els10_27swdisDesc_Type()
)
els10_27swdisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swdisDesc.setStatus("mandatory")


class _Els10_27swdisAccess_Type(Integer32):
    """Custom type els10_27swdisAccess based on Integer32"""
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


_Els10_27swdisAccess_Type.__name__ = "Integer32"
_Els10_27swdisAccess_Object = MibScalar
els10_27swdisAccess = _Els10_27swdisAccess_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 2),
    _Els10_27swdisAccess_Type()
)
els10_27swdisAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27swdisAccess.setStatus("mandatory")


class _Els10_27swdisWriteStatus_Type(Integer32):
    """Custom type els10_27swdisWriteStatus based on Integer32"""
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


_Els10_27swdisWriteStatus_Type.__name__ = "Integer32"
_Els10_27swdisWriteStatus_Object = MibScalar
els10_27swdisWriteStatus = _Els10_27swdisWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 3),
    _Els10_27swdisWriteStatus_Type()
)
els10_27swdisWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27swdisWriteStatus.setStatus("mandatory")
_Els10_27swdisConfigIp_Type = IpAddress
_Els10_27swdisConfigIp_Object = MibScalar
els10_27swdisConfigIp = _Els10_27swdisConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 4),
    _Els10_27swdisConfigIp_Type()
)
els10_27swdisConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27swdisConfigIp.setStatus("mandatory")
_Els10_27swdisConfigRetryTime_Type = Integer32
_Els10_27swdisConfigRetryTime_Object = MibScalar
els10_27swdisConfigRetryTime = _Els10_27swdisConfigRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 5),
    _Els10_27swdisConfigRetryTime_Type()
)
els10_27swdisConfigRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27swdisConfigRetryTime.setStatus("mandatory")
_Els10_27swdisConfigTotalTimeout_Type = Integer32
_Els10_27swdisConfigTotalTimeout_Object = MibScalar
els10_27swdisConfigTotalTimeout = _Els10_27swdisConfigTotalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 4, 6),
    _Els10_27swdisConfigTotalTimeout_Type()
)
els10_27swdisConfigTotalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27swdisConfigTotalTimeout.setStatus("mandatory")
_Els10_27addr_ObjectIdentity = ObjectIdentity
els10_27addr = _Els10_27addr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 5)
)
_Els10_27addrStatics_Type = Counter32
_Els10_27addrStatics_Object = MibScalar
els10_27addrStatics = _Els10_27addrStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 1),
    _Els10_27addrStatics_Type()
)
els10_27addrStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27addrStatics.setStatus("mandatory")
_Els10_27addrDynamics_Type = Counter32
_Els10_27addrDynamics_Object = MibScalar
els10_27addrDynamics = _Els10_27addrDynamics_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 2),
    _Els10_27addrDynamics_Type()
)
els10_27addrDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27addrDynamics.setStatus("mandatory")
_Els10_27addrDynamicMax_Type = Gauge32
_Els10_27addrDynamicMax_Object = MibScalar
els10_27addrDynamicMax = _Els10_27addrDynamicMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 3),
    _Els10_27addrDynamicMax_Type()
)
els10_27addrDynamicMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrDynamicMax.setStatus("mandatory")
_Els10_27addrDynamicOverflows_Type = Counter32
_Els10_27addrDynamicOverflows_Object = MibScalar
els10_27addrDynamicOverflows = _Els10_27addrDynamicOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 4),
    _Els10_27addrDynamicOverflows_Type()
)
els10_27addrDynamicOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27addrDynamicOverflows.setStatus("mandatory")
_Els10_27addrFlags_Type = Integer32
_Els10_27addrFlags_Object = MibScalar
els10_27addrFlags = _Els10_27addrFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 5),
    _Els10_27addrFlags_Type()
)
els10_27addrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrFlags.setStatus("mandatory")
_Els10_27addrMAC_Type = OctetString
_Els10_27addrMAC_Object = MibScalar
els10_27addrMAC = _Els10_27addrMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 6),
    _Els10_27addrMAC_Type()
)
els10_27addrMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrMAC.setStatus("mandatory")
_Els10_27addrPort_Type = Integer32
_Els10_27addrPort_Object = MibScalar
els10_27addrPort = _Els10_27addrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 7),
    _Els10_27addrPort_Type()
)
els10_27addrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrPort.setStatus("mandatory")


class _Els10_27addrOperation_Type(Integer32):
    """Custom type els10_27addrOperation based on Integer32"""
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


_Els10_27addrOperation_Type.__name__ = "Integer32"
_Els10_27addrOperation_Object = MibScalar
els10_27addrOperation = _Els10_27addrOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 8),
    _Els10_27addrOperation_Type()
)
els10_27addrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrOperation.setStatus("mandatory")
_Els10_27addrIndex_Type = Integer32
_Els10_27addrIndex_Object = MibScalar
els10_27addrIndex = _Els10_27addrIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 9),
    _Els10_27addrIndex_Type()
)
els10_27addrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrIndex.setStatus("mandatory")
_Els10_27addrNext_Type = Integer32
_Els10_27addrNext_Object = MibScalar
els10_27addrNext = _Els10_27addrNext_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 10),
    _Els10_27addrNext_Type()
)
els10_27addrNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrNext.setStatus("mandatory")
_Els10_27addrBlockSize_Type = Integer32
_Els10_27addrBlockSize_Object = MibScalar
els10_27addrBlockSize = _Els10_27addrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 19),
    _Els10_27addrBlockSize_Type()
)
els10_27addrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrBlockSize.setStatus("mandatory")
_Els10_27addrBlock_Type = OctetString
_Els10_27addrBlock_Object = MibScalar
els10_27addrBlock = _Els10_27addrBlock_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 5, 20),
    _Els10_27addrBlock_Type()
)
els10_27addrBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27addrBlock.setStatus("mandatory")
_Els10_27if_ObjectIdentity = ObjectIdentity
els10_27if = _Els10_27if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 6)
)
_Els10_27ifTable_Object = MibTable
els10_27ifTable = _Els10_27ifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1)
)
if mibBuilder.loadTexts:
    els10_27ifTable.setStatus("mandatory")
_Els10_27ifEntry_Object = MibTableRow
els10_27ifEntry = _Els10_27ifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1)
)
els10_27ifEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27ifIndex"),
)
if mibBuilder.loadTexts:
    els10_27ifEntry.setStatus("mandatory")
_Els10_27ifIndex_Type = Integer32
_Els10_27ifIndex_Object = MibScalar
els10_27ifIndex = _Els10_27ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 1),
    _Els10_27ifIndex_Type()
)
els10_27ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifIndex.setStatus("mandatory")
_Els10_27ifThreshold_Type = Integer32
_Els10_27ifThreshold_Object = MibScalar
els10_27ifThreshold = _Els10_27ifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 4),
    _Els10_27ifThreshold_Type()
)
els10_27ifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifThreshold.setStatus("mandatory")
_Els10_27ifThresholdTime_Type = Integer32
_Els10_27ifThresholdTime_Object = MibScalar
els10_27ifThresholdTime = _Els10_27ifThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 5),
    _Els10_27ifThresholdTime_Type()
)
els10_27ifThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifThresholdTime.setStatus("mandatory")
_Els10_27ifRxQueueThresh_Type = Integer32
_Els10_27ifRxQueueThresh_Object = MibScalar
els10_27ifRxQueueThresh = _Els10_27ifRxQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 6),
    _Els10_27ifRxQueueThresh_Type()
)
els10_27ifRxQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifRxQueueThresh.setStatus("mandatory")
_Els10_27ifRxQueueThreshTime_Type = Integer32
_Els10_27ifRxQueueThreshTime_Object = MibScalar
els10_27ifRxQueueThreshTime = _Els10_27ifRxQueueThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 7),
    _Els10_27ifRxQueueThreshTime_Type()
)
els10_27ifRxQueueThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifRxQueueThreshTime.setStatus("mandatory")
_Els10_27ifTxStormCnt_Type = Integer32
_Els10_27ifTxStormCnt_Object = MibScalar
els10_27ifTxStormCnt = _Els10_27ifTxStormCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 8),
    _Els10_27ifTxStormCnt_Type()
)
els10_27ifTxStormCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifTxStormCnt.setStatus("mandatory")
_Els10_27ifTxStormTime_Type = TimeTicks
_Els10_27ifTxStormTime_Object = MibScalar
els10_27ifTxStormTime = _Els10_27ifTxStormTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 9),
    _Els10_27ifTxStormTime_Type()
)
els10_27ifTxStormTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifTxStormTime.setStatus("mandatory")
_Els10_27ifFunction_Type = Integer32
_Els10_27ifFunction_Object = MibScalar
els10_27ifFunction = _Els10_27ifFunction_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 16),
    _Els10_27ifFunction_Type()
)
els10_27ifFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifFunction.setStatus("mandatory")
_Els10_27ifRxHwFCSs_Type = Counter32
_Els10_27ifRxHwFCSs_Object = MibScalar
els10_27ifRxHwFCSs = _Els10_27ifRxHwFCSs_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 18),
    _Els10_27ifRxHwFCSs_Type()
)
els10_27ifRxHwFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifRxHwFCSs.setStatus("mandatory")
_Els10_27ifRxQueues_Type = Counter32
_Els10_27ifRxQueues_Object = MibScalar
els10_27ifRxQueues = _Els10_27ifRxQueues_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 19),
    _Els10_27ifRxQueues_Type()
)
els10_27ifRxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifRxQueues.setStatus("mandatory")
_Els10_27ifStatisticsTime_Type = TimeTicks
_Els10_27ifStatisticsTime_Object = MibScalar
els10_27ifStatisticsTime = _Els10_27ifStatisticsTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 27),
    _Els10_27ifStatisticsTime_Type()
)
els10_27ifStatisticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifStatisticsTime.setStatus("mandatory")
_Els10_27ifForwardedChars_Type = Counter32
_Els10_27ifForwardedChars_Object = MibScalar
els10_27ifForwardedChars = _Els10_27ifForwardedChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 28),
    _Els10_27ifForwardedChars_Type()
)
els10_27ifForwardedChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifForwardedChars.setStatus("mandatory")
_Els10_27ifDescr_Type = DisplayString
_Els10_27ifDescr_Object = MibScalar
els10_27ifDescr = _Els10_27ifDescr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 29),
    _Els10_27ifDescr_Type()
)
els10_27ifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ifDescr.setStatus("mandatory")
_Els10_27ifGoodRxFrames_Type = Counter32
_Els10_27ifGoodRxFrames_Object = MibScalar
els10_27ifGoodRxFrames = _Els10_27ifGoodRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 30),
    _Els10_27ifGoodRxFrames_Type()
)
els10_27ifGoodRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifGoodRxFrames.setStatus("mandatory")
_Els10_27ifGoodTxFrames_Type = Counter32
_Els10_27ifGoodTxFrames_Object = MibScalar
els10_27ifGoodTxFrames = _Els10_27ifGoodTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 6, 1, 1, 31),
    _Els10_27ifGoodTxFrames_Type()
)
els10_27ifGoodTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27ifGoodTxFrames.setStatus("mandatory")
_Els10_27dot3_ObjectIdentity = ObjectIdentity
els10_27dot3 = _Els10_27dot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 7)
)
_Els10_27dot3Table_Object = MibTable
els10_27dot3Table = _Els10_27dot3Table_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1)
)
if mibBuilder.loadTexts:
    els10_27dot3Table.setStatus("mandatory")
_Els10_27dot3Entry_Object = MibTableRow
els10_27dot3Entry = _Els10_27dot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1)
)
els10_27dot3Entry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27dot3Index"),
)
if mibBuilder.loadTexts:
    els10_27dot3Entry.setStatus("mandatory")
_Els10_27dot3Index_Type = Integer32
_Els10_27dot3Index_Object = MibScalar
els10_27dot3Index = _Els10_27dot3Index_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 1),
    _Els10_27dot3Index_Type()
)
els10_27dot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3Index.setStatus("mandatory")


class _Els10_27dot3TPLinkOK_Type(Integer32):
    """Custom type els10_27dot3TPLinkOK based on Integer32"""
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


_Els10_27dot3TPLinkOK_Type.__name__ = "Integer32"
_Els10_27dot3TPLinkOK_Object = MibScalar
els10_27dot3TPLinkOK = _Els10_27dot3TPLinkOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 2),
    _Els10_27dot3TPLinkOK_Type()
)
els10_27dot3TPLinkOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3TPLinkOK.setStatus("mandatory")


class _Els10_27dot3LedOn_Type(Integer32):
    """Custom type els10_27dot3LedOn based on Integer32"""
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


_Els10_27dot3LedOn_Type.__name__ = "Integer32"
_Els10_27dot3LedOn_Object = MibScalar
els10_27dot3LedOn = _Els10_27dot3LedOn_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 3),
    _Els10_27dot3LedOn_Type()
)
els10_27dot3LedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3LedOn.setStatus("mandatory")
_Els10_27dot3RxCollisions_Type = Counter32
_Els10_27dot3RxCollisions_Object = MibScalar
els10_27dot3RxCollisions = _Els10_27dot3RxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 4),
    _Els10_27dot3RxCollisions_Type()
)
els10_27dot3RxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3RxCollisions.setStatus("mandatory")
_Els10_27dot3RxRunts_Type = Counter32
_Els10_27dot3RxRunts_Object = MibScalar
els10_27dot3RxRunts = _Els10_27dot3RxRunts_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 5),
    _Els10_27dot3RxRunts_Type()
)
els10_27dot3RxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3RxRunts.setStatus("mandatory")
_Els10_27dot3RxLateColls_Type = Counter32
_Els10_27dot3RxLateColls_Object = MibScalar
els10_27dot3RxLateColls = _Els10_27dot3RxLateColls_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 6),
    _Els10_27dot3RxLateColls_Type()
)
els10_27dot3RxLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3RxLateColls.setStatus("mandatory")
_Els10_27dot3TxJabbers_Type = Counter32
_Els10_27dot3TxJabbers_Object = MibScalar
els10_27dot3TxJabbers = _Els10_27dot3TxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 7),
    _Els10_27dot3TxJabbers_Type()
)
els10_27dot3TxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3TxJabbers.setStatus("mandatory")
_Els10_27dot3TxBabbles_Type = Counter32
_Els10_27dot3TxBabbles_Object = MibScalar
els10_27dot3TxBabbles = _Els10_27dot3TxBabbles_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 8),
    _Els10_27dot3TxBabbles_Type()
)
els10_27dot3TxBabbles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3TxBabbles.setStatus("mandatory")
_Els10_27dot3TxCollisions_Type = Counter32
_Els10_27dot3TxCollisions_Object = MibScalar
els10_27dot3TxCollisions = _Els10_27dot3TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 9),
    _Els10_27dot3TxCollisions_Type()
)
els10_27dot3TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27dot3TxCollisions.setStatus("mandatory")


class _Els10_27dot3SpeedSelection_Type(Integer32):
    """Custom type els10_27dot3SpeedSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-100mbit", 2),
          ("speed-10mbit", 1),
          ("speed-auto", 3))
    )


_Els10_27dot3SpeedSelection_Type.__name__ = "Integer32"
_Els10_27dot3SpeedSelection_Object = MibScalar
els10_27dot3SpeedSelection = _Els10_27dot3SpeedSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 13),
    _Els10_27dot3SpeedSelection_Type()
)
els10_27dot3SpeedSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27dot3SpeedSelection.setStatus("mandatory")


class _Els10_27dot3DuplexSelection_Type(Integer32):
    """Custom type els10_27dot3DuplexSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplex-auto", 1),
          ("duplex-full", 3),
          ("duplex-half", 2))
    )


_Els10_27dot3DuplexSelection_Type.__name__ = "Integer32"
_Els10_27dot3DuplexSelection_Object = MibScalar
els10_27dot3DuplexSelection = _Els10_27dot3DuplexSelection_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 7, 1, 1, 14),
    _Els10_27dot3DuplexSelection_Type()
)
els10_27dot3DuplexSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27dot3DuplexSelection.setStatus("mandatory")
_Els10_27uart_ObjectIdentity = ObjectIdentity
els10_27uart = _Els10_27uart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 8)
)
_Els10_27uartTable_Object = MibTable
els10_27uartTable = _Els10_27uartTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1)
)
if mibBuilder.loadTexts:
    els10_27uartTable.setStatus("mandatory")
_Els10_27uartEntry_Object = MibTableRow
els10_27uartEntry = _Els10_27uartEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1, 1)
)
els10_27uartEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27uartIndex"),
)
if mibBuilder.loadTexts:
    els10_27uartEntry.setStatus("mandatory")
_Els10_27uartIndex_Type = Integer32
_Els10_27uartIndex_Object = MibScalar
els10_27uartIndex = _Els10_27uartIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1, 1, 1),
    _Els10_27uartIndex_Type()
)
els10_27uartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27uartIndex.setStatus("mandatory")


class _Els10_27uartBaud_Type(Integer32):
    """Custom type els10_27uartBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("b19200-baud", 6),
          ("b2400-baud", 3),
          ("b4800-baud", 4),
          ("b9600-baud", 5))
    )


_Els10_27uartBaud_Type.__name__ = "Integer32"
_Els10_27uartBaud_Object = MibScalar
els10_27uartBaud = _Els10_27uartBaud_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1, 1, 2),
    _Els10_27uartBaud_Type()
)
els10_27uartBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27uartBaud.setStatus("mandatory")
_Els10_27uartAlignmentErrors_Type = Counter32
_Els10_27uartAlignmentErrors_Object = MibScalar
els10_27uartAlignmentErrors = _Els10_27uartAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1, 1, 3),
    _Els10_27uartAlignmentErrors_Type()
)
els10_27uartAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27uartAlignmentErrors.setStatus("mandatory")
_Els10_27uartOverrunErrors_Type = Counter32
_Els10_27uartOverrunErrors_Object = MibScalar
els10_27uartOverrunErrors = _Els10_27uartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 8, 1, 1, 4),
    _Els10_27uartOverrunErrors_Type()
)
els10_27uartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27uartOverrunErrors.setStatus("mandatory")
_Els10_27debug_ObjectIdentity = ObjectIdentity
els10_27debug = _Els10_27debug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 10)
)
_Els10_27debugStringID_Type = Integer32
_Els10_27debugStringID_Object = MibScalar
els10_27debugStringID = _Els10_27debugStringID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 1),
    _Els10_27debugStringID_Type()
)
els10_27debugStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27debugStringID.setStatus("mandatory")
_Els10_27debugString_Type = OctetString
_Els10_27debugString_Object = MibScalar
els10_27debugString = _Els10_27debugString_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 2),
    _Els10_27debugString_Type()
)
els10_27debugString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27debugString.setStatus("mandatory")
_Els10_27debugTable_Object = MibTable
els10_27debugTable = _Els10_27debugTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3)
)
if mibBuilder.loadTexts:
    els10_27debugTable.setStatus("mandatory")
_Els10_27debugEntry_Object = MibTableRow
els10_27debugEntry = _Els10_27debugEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1)
)
els10_27debugEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27debugIndex"),
)
if mibBuilder.loadTexts:
    els10_27debugEntry.setStatus("mandatory")


class _Els10_27debugIndex_Type(Integer32):
    """Custom type els10_27debugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("debug-nam", 1)
    )


_Els10_27debugIndex_Type.__name__ = "Integer32"
_Els10_27debugIndex_Object = MibScalar
els10_27debugIndex = _Els10_27debugIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1, 1),
    _Els10_27debugIndex_Type()
)
els10_27debugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27debugIndex.setStatus("mandatory")


class _Els10_27debugOperation_Type(Integer32):
    """Custom type els10_27debugOperation based on Integer32"""
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


_Els10_27debugOperation_Type.__name__ = "Integer32"
_Els10_27debugOperation_Object = MibScalar
els10_27debugOperation = _Els10_27debugOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1, 2),
    _Els10_27debugOperation_Type()
)
els10_27debugOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27debugOperation.setStatus("mandatory")
_Els10_27debugBase_Type = Integer32
_Els10_27debugBase_Object = MibScalar
els10_27debugBase = _Els10_27debugBase_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1, 3),
    _Els10_27debugBase_Type()
)
els10_27debugBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27debugBase.setStatus("mandatory")
_Els10_27debugLength_Type = Integer32
_Els10_27debugLength_Object = MibScalar
els10_27debugLength = _Els10_27debugLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1, 4),
    _Els10_27debugLength_Type()
)
els10_27debugLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27debugLength.setStatus("mandatory")
_Els10_27debugData_Type = OctetString
_Els10_27debugData_Object = MibScalar
els10_27debugData = _Els10_27debugData_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 10, 3, 1, 5),
    _Els10_27debugData_Type()
)
els10_27debugData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27debugData.setStatus("mandatory")
_Els10_27lpbk_ObjectIdentity = ObjectIdentity
els10_27lpbk = _Els10_27lpbk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 11)
)
_Els10_27lpbkTable_Object = MibTable
els10_27lpbkTable = _Els10_27lpbkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1)
)
if mibBuilder.loadTexts:
    els10_27lpbkTable.setStatus("mandatory")
_Els10_27lpbkEntry_Object = MibTableRow
els10_27lpbkEntry = _Els10_27lpbkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1)
)
els10_27lpbkEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27lpbkIndex"),
)
if mibBuilder.loadTexts:
    els10_27lpbkEntry.setStatus("mandatory")
_Els10_27lpbkIndex_Type = Integer32
_Els10_27lpbkIndex_Object = MibScalar
els10_27lpbkIndex = _Els10_27lpbkIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 1),
    _Els10_27lpbkIndex_Type()
)
els10_27lpbkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkIndex.setStatus("mandatory")


class _Els10_27lpbkOperation_Type(Integer32):
    """Custom type els10_27lpbkOperation based on Integer32"""
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


_Els10_27lpbkOperation_Type.__name__ = "Integer32"
_Els10_27lpbkOperation_Object = MibScalar
els10_27lpbkOperation = _Els10_27lpbkOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 2),
    _Els10_27lpbkOperation_Type()
)
els10_27lpbkOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkOperation.setStatus("mandatory")
_Els10_27lpbkDestAddr_Type = OctetString
_Els10_27lpbkDestAddr_Object = MibScalar
els10_27lpbkDestAddr = _Els10_27lpbkDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 3),
    _Els10_27lpbkDestAddr_Type()
)
els10_27lpbkDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkDestAddr.setStatus("mandatory")
_Els10_27lpbkPktNum_Type = Integer32
_Els10_27lpbkPktNum_Object = MibScalar
els10_27lpbkPktNum = _Els10_27lpbkPktNum_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 4),
    _Els10_27lpbkPktNum_Type()
)
els10_27lpbkPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkPktNum.setStatus("mandatory")
_Els10_27lpbkInterval_Type = TimeTicks
_Els10_27lpbkInterval_Object = MibScalar
els10_27lpbkInterval = _Els10_27lpbkInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 5),
    _Els10_27lpbkInterval_Type()
)
els10_27lpbkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkInterval.setStatus("mandatory")
_Els10_27lpbkPktLength_Type = Integer32
_Els10_27lpbkPktLength_Object = MibScalar
els10_27lpbkPktLength = _Els10_27lpbkPktLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 6),
    _Els10_27lpbkPktLength_Type()
)
els10_27lpbkPktLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkPktLength.setStatus("mandatory")
_Els10_27lpbkIncrements_Type = Integer32
_Els10_27lpbkIncrements_Object = MibScalar
els10_27lpbkIncrements = _Els10_27lpbkIncrements_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 7),
    _Els10_27lpbkIncrements_Type()
)
els10_27lpbkIncrements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27lpbkIncrements.setStatus("mandatory")
_Els10_27lpbkGoods_Type = Counter32
_Els10_27lpbkGoods_Object = MibScalar
els10_27lpbkGoods = _Els10_27lpbkGoods_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 8),
    _Els10_27lpbkGoods_Type()
)
els10_27lpbkGoods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkGoods.setStatus("mandatory")
_Els10_27lpbkErrorNoReceives_Type = Counter32
_Els10_27lpbkErrorNoReceives_Object = MibScalar
els10_27lpbkErrorNoReceives = _Els10_27lpbkErrorNoReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 9),
    _Els10_27lpbkErrorNoReceives_Type()
)
els10_27lpbkErrorNoReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorNoReceives.setStatus("mandatory")
_Els10_27lpbkErrorBadReceives_Type = Counter32
_Els10_27lpbkErrorBadReceives_Object = MibScalar
els10_27lpbkErrorBadReceives = _Els10_27lpbkErrorBadReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 10),
    _Els10_27lpbkErrorBadReceives_Type()
)
els10_27lpbkErrorBadReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorBadReceives.setStatus("mandatory")
_Els10_27lpbkErrorSize_Type = Integer32
_Els10_27lpbkErrorSize_Object = MibScalar
els10_27lpbkErrorSize = _Els10_27lpbkErrorSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 11),
    _Els10_27lpbkErrorSize_Type()
)
els10_27lpbkErrorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorSize.setStatus("mandatory")
_Els10_27lpbkErrorSent_Type = OctetString
_Els10_27lpbkErrorSent_Object = MibScalar
els10_27lpbkErrorSent = _Els10_27lpbkErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 12),
    _Els10_27lpbkErrorSent_Type()
)
els10_27lpbkErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorSent.setStatus("mandatory")
_Els10_27lpbkErrorReceived_Type = OctetString
_Els10_27lpbkErrorReceived_Object = MibScalar
els10_27lpbkErrorReceived = _Els10_27lpbkErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 13),
    _Els10_27lpbkErrorReceived_Type()
)
els10_27lpbkErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorReceived.setStatus("mandatory")
_Els10_27lpbkErrorOffset_Type = Integer32
_Els10_27lpbkErrorOffset_Object = MibScalar
els10_27lpbkErrorOffset = _Els10_27lpbkErrorOffset_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 11, 1, 1, 14),
    _Els10_27lpbkErrorOffset_Type()
)
els10_27lpbkErrorOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27lpbkErrorOffset.setStatus("mandatory")
_Els10_27proto_ObjectIdentity = ObjectIdentity
els10_27proto = _Els10_27proto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 12)
)
_Els10_27protoTable_Object = MibTable
els10_27protoTable = _Els10_27protoTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1)
)
if mibBuilder.loadTexts:
    els10_27protoTable.setStatus("mandatory")
_Els10_27protoEntry_Object = MibTableRow
els10_27protoEntry = _Els10_27protoEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1)
)
els10_27protoEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27protoIfIndex"),
)
if mibBuilder.loadTexts:
    els10_27protoEntry.setStatus("mandatory")
_Els10_27protoIfIndex_Type = Integer32
_Els10_27protoIfIndex_Object = MibScalar
els10_27protoIfIndex = _Els10_27protoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 1),
    _Els10_27protoIfIndex_Type()
)
els10_27protoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27protoIfIndex.setStatus("mandatory")


class _Els10_27protoBridge_Type(Integer32):
    """Custom type els10_27protoBridge based on Integer32"""
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


_Els10_27protoBridge_Type.__name__ = "Integer32"
_Els10_27protoBridge_Object = MibScalar
els10_27protoBridge = _Els10_27protoBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 2),
    _Els10_27protoBridge_Type()
)
els10_27protoBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27protoBridge.setStatus("mandatory")


class _Els10_27protoSuppressBpdu_Type(Integer32):
    """Custom type els10_27protoSuppressBpdu based on Integer32"""
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


_Els10_27protoSuppressBpdu_Type.__name__ = "Integer32"
_Els10_27protoSuppressBpdu_Object = MibScalar
els10_27protoSuppressBpdu = _Els10_27protoSuppressBpdu_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 3),
    _Els10_27protoSuppressBpdu_Type()
)
els10_27protoSuppressBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27protoSuppressBpdu.setStatus("mandatory")


class _Els10_27protoRipListen_Type(Integer32):
    """Custom type els10_27protoRipListen based on Integer32"""
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


_Els10_27protoRipListen_Type.__name__ = "Integer32"
_Els10_27protoRipListen_Object = MibScalar
els10_27protoRipListen = _Els10_27protoRipListen_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 4),
    _Els10_27protoRipListen_Type()
)
els10_27protoRipListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27protoRipListen.setStatus("mandatory")


class _Els10_27protoTrunking_Type(Integer32):
    """Custom type els10_27protoTrunking based on Integer32"""
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


_Els10_27protoTrunking_Type.__name__ = "Integer32"
_Els10_27protoTrunking_Object = MibScalar
els10_27protoTrunking = _Els10_27protoTrunking_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 5),
    _Els10_27protoTrunking_Type()
)
els10_27protoTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27protoTrunking.setStatus("mandatory")


class _Els10_27sprotoTransmitPacing_Type(Integer32):
    """Custom type els10_27sprotoTransmitPacing based on Integer32"""
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


_Els10_27sprotoTransmitPacing_Type.__name__ = "Integer32"
_Els10_27sprotoTransmitPacing_Object = MibScalar
els10_27sprotoTransmitPacing = _Els10_27sprotoTransmitPacing_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 12, 1, 1, 6),
    _Els10_27sprotoTransmitPacing_Type()
)
els10_27sprotoTransmitPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27sprotoTransmitPacing.setStatus("mandatory")
_Els10_27trunk_ObjectIdentity = ObjectIdentity
els10_27trunk = _Els10_27trunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 13)
)
_Els10_27trunkTable_Object = MibTable
els10_27trunkTable = _Els10_27trunkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1)
)
if mibBuilder.loadTexts:
    els10_27trunkTable.setStatus("mandatory")
_Els10_27trunkEntry_Object = MibTableRow
els10_27trunkEntry = _Els10_27trunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1)
)
els10_27trunkEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27trunkIfIndex"),
)
if mibBuilder.loadTexts:
    els10_27trunkEntry.setStatus("mandatory")
_Els10_27trunkIfIndex_Type = Integer32
_Els10_27trunkIfIndex_Object = MibScalar
els10_27trunkIfIndex = _Els10_27trunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 1),
    _Els10_27trunkIfIndex_Type()
)
els10_27trunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkIfIndex.setStatus("mandatory")


class _Els10_27trunkState_Type(Integer32):
    """Custom type els10_27trunkState based on Integer32"""
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


_Els10_27trunkState_Type.__name__ = "Integer32"
_Els10_27trunkState_Object = MibScalar
els10_27trunkState = _Els10_27trunkState_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 2),
    _Els10_27trunkState_Type()
)
els10_27trunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkState.setStatus("mandatory")
_Els10_27trunkRemoteBridgeAddr_Type = OctetString
_Els10_27trunkRemoteBridgeAddr_Object = MibScalar
els10_27trunkRemoteBridgeAddr = _Els10_27trunkRemoteBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 3),
    _Els10_27trunkRemoteBridgeAddr_Type()
)
els10_27trunkRemoteBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkRemoteBridgeAddr.setStatus("mandatory")
_Els10_27trunkRemoteIp_Type = IpAddress
_Els10_27trunkRemoteIp_Object = MibScalar
els10_27trunkRemoteIp = _Els10_27trunkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 4),
    _Els10_27trunkRemoteIp_Type()
)
els10_27trunkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkRemoteIp.setStatus("mandatory")


class _Els10_27trunkLastError_Type(Integer32):
    """Custom type els10_27trunkLastError based on Integer32"""
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


_Els10_27trunkLastError_Type.__name__ = "Integer32"
_Els10_27trunkLastError_Object = MibScalar
els10_27trunkLastError = _Els10_27trunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 5),
    _Els10_27trunkLastError_Type()
)
els10_27trunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkLastError.setStatus("mandatory")
_Els10_27trunkLinkOrdinal_Type = Integer32
_Els10_27trunkLinkOrdinal_Object = MibScalar
els10_27trunkLinkOrdinal = _Els10_27trunkLinkOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 6),
    _Els10_27trunkLinkOrdinal_Type()
)
els10_27trunkLinkOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkLinkOrdinal.setStatus("mandatory")
_Els10_27trunkLinkCount_Type = Integer32
_Els10_27trunkLinkCount_Object = MibScalar
els10_27trunkLinkCount = _Els10_27trunkLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 7),
    _Els10_27trunkLinkCount_Type()
)
els10_27trunkLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkLinkCount.setStatus("mandatory")
_Els10_27trunkLastChange_Type = Integer32
_Els10_27trunkLastChange_Object = MibScalar
els10_27trunkLastChange = _Els10_27trunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 13, 1, 1, 8),
    _Els10_27trunkLastChange_Type()
)
els10_27trunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trunkLastChange.setStatus("mandatory")
_Els10_27workgroup_ObjectIdentity = ObjectIdentity
els10_27workgroup = _Els10_27workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 14)
)
_Els10_27WorkGroupNextNumber_Type = Integer32
_Els10_27WorkGroupNextNumber_Object = MibScalar
els10_27WorkGroupNextNumber = _Els10_27WorkGroupNextNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 1),
    _Els10_27WorkGroupNextNumber_Type()
)
els10_27WorkGroupNextNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27WorkGroupNextNumber.setStatus("mandatory")
_Els10_27WorkGroupCurrentCount_Type = Integer32
_Els10_27WorkGroupCurrentCount_Object = MibScalar
els10_27WorkGroupCurrentCount = _Els10_27WorkGroupCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 2),
    _Els10_27WorkGroupCurrentCount_Type()
)
els10_27WorkGroupCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27WorkGroupCurrentCount.setStatus("mandatory")
_Els10_27WorkGroupMaxCount_Type = Integer32
_Els10_27WorkGroupMaxCount_Object = MibScalar
els10_27WorkGroupMaxCount = _Els10_27WorkGroupMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 3),
    _Els10_27WorkGroupMaxCount_Type()
)
els10_27WorkGroupMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27WorkGroupMaxCount.setStatus("mandatory")
_Els10_27WorkGroupTable_Object = MibTable
els10_27WorkGroupTable = _Els10_27WorkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4)
)
if mibBuilder.loadTexts:
    els10_27WorkGroupTable.setStatus("mandatory")
_Els10_27WorkGroupEntry_Object = MibTableRow
els10_27WorkGroupEntry = _Els10_27WorkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4, 1)
)
els10_27WorkGroupEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27WorkGroupNumber"),
)
if mibBuilder.loadTexts:
    els10_27WorkGroupEntry.setStatus("mandatory")
_Els10_27WorkGroupNumber_Type = Integer32
_Els10_27WorkGroupNumber_Object = MibScalar
els10_27WorkGroupNumber = _Els10_27WorkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4, 1, 1),
    _Els10_27WorkGroupNumber_Type()
)
els10_27WorkGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27WorkGroupNumber.setStatus("mandatory")
_Els10_27WorkGroupName_Type = DisplayString
_Els10_27WorkGroupName_Object = MibScalar
els10_27WorkGroupName = _Els10_27WorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4, 1, 2),
    _Els10_27WorkGroupName_Type()
)
els10_27WorkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27WorkGroupName.setStatus("mandatory")
_Els10_27WorkGroupPorts_Type = OctetString
_Els10_27WorkGroupPorts_Object = MibScalar
els10_27WorkGroupPorts = _Els10_27WorkGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4, 1, 3),
    _Els10_27WorkGroupPorts_Type()
)
els10_27WorkGroupPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27WorkGroupPorts.setStatus("mandatory")


class _Els10_27WorkGroupType_Type(Integer32):
    """Custom type els10_27WorkGroupType based on Integer32"""
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


_Els10_27WorkGroupType_Type.__name__ = "Integer32"
_Els10_27WorkGroupType_Object = MibScalar
els10_27WorkGroupType = _Els10_27WorkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 14, 4, 1, 4),
    _Els10_27WorkGroupType_Type()
)
els10_27WorkGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27WorkGroupType.setStatus("mandatory")
_Els10_27trapMgt_ObjectIdentity = ObjectIdentity
els10_27trapMgt = _Els10_27trapMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 15)
)
_Els10_27trapControlTable_Object = MibTable
els10_27trapControlTable = _Els10_27trapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1)
)
if mibBuilder.loadTexts:
    els10_27trapControlTable.setStatus("mandatory")
_Els10_27trapControlEntry_Object = MibTableRow
els10_27trapControlEntry = _Els10_27trapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1, 1)
)
els10_27trapControlEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27trapIndex"),
)
if mibBuilder.loadTexts:
    els10_27trapControlEntry.setStatus("mandatory")
_Els10_27trapIndex_Type = Integer32
_Els10_27trapIndex_Object = MibScalar
els10_27trapIndex = _Els10_27trapIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1, 1, 1),
    _Els10_27trapIndex_Type()
)
els10_27trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapIndex.setStatus("mandatory")


class _Els10_27trapEnabled_Type(Integer32):
    """Custom type els10_27trapEnabled based on Integer32"""
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


_Els10_27trapEnabled_Type.__name__ = "Integer32"
_Els10_27trapEnabled_Object = MibScalar
els10_27trapEnabled = _Els10_27trapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1, 1, 2),
    _Els10_27trapEnabled_Type()
)
els10_27trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapEnabled.setStatus("mandatory")


class _Els10_27trapSeverity_Type(Integer32):
    """Custom type els10_27trapSeverity based on Integer32"""
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


_Els10_27trapSeverity_Type.__name__ = "Integer32"
_Els10_27trapSeverity_Object = MibScalar
els10_27trapSeverity = _Els10_27trapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1, 1, 3),
    _Els10_27trapSeverity_Type()
)
els10_27trapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapSeverity.setStatus("mandatory")
_Els10_27trapText_Type = DisplayString
_Els10_27trapText_Object = MibScalar
els10_27trapText = _Els10_27trapText_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 1, 1, 4),
    _Els10_27trapText_Type()
)
els10_27trapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapText.setStatus("mandatory")
_Els10_27trapSeverityControlTable_Object = MibTable
els10_27trapSeverityControlTable = _Els10_27trapSeverityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 2)
)
if mibBuilder.loadTexts:
    els10_27trapSeverityControlTable.setStatus("mandatory")
_Els10_27trapSeverityControlEntry_Object = MibTableRow
els10_27trapSeverityControlEntry = _Els10_27trapSeverityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 2, 1)
)
els10_27trapSeverityControlEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27trapSeverity"),
)
if mibBuilder.loadTexts:
    els10_27trapSeverityControlEntry.setStatus("mandatory")


class _Els10_27trapSeverityControlSeverity_Type(Integer32):
    """Custom type els10_27trapSeverityControlSeverity based on Integer32"""
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


_Els10_27trapSeverityControlSeverity_Type.__name__ = "Integer32"
_Els10_27trapSeverityControlSeverity_Object = MibScalar
els10_27trapSeverityControlSeverity = _Els10_27trapSeverityControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 2, 1, 1),
    _Els10_27trapSeverityControlSeverity_Type()
)
els10_27trapSeverityControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapSeverityControlSeverity.setStatus("mandatory")


class _Els10_27trapSeverityEnable_Type(Integer32):
    """Custom type els10_27trapSeverityEnable based on Integer32"""
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


_Els10_27trapSeverityEnable_Type.__name__ = "Integer32"
_Els10_27trapSeverityEnable_Object = MibScalar
els10_27trapSeverityEnable = _Els10_27trapSeverityEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 2, 1, 2),
    _Els10_27trapSeverityEnable_Type()
)
els10_27trapSeverityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapSeverityEnable.setStatus("mandatory")


class _Els10_27trapIncludeText_Type(Integer32):
    """Custom type els10_27trapIncludeText based on Integer32"""
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


_Els10_27trapIncludeText_Type.__name__ = "Integer32"
_Els10_27trapIncludeText_Object = MibScalar
els10_27trapIncludeText = _Els10_27trapIncludeText_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 3),
    _Els10_27trapIncludeText_Type()
)
els10_27trapIncludeText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapIncludeText.setStatus("mandatory")
_Els10_27trapTime_Type = TimeTicks
_Els10_27trapTime_Object = MibScalar
els10_27trapTime = _Els10_27trapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 4),
    _Els10_27trapTime_Type()
)
els10_27trapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapTime.setStatus("mandatory")
_Els10_27trapRetry_Type = Integer32
_Els10_27trapRetry_Object = MibScalar
els10_27trapRetry = _Els10_27trapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 5),
    _Els10_27trapRetry_Type()
)
els10_27trapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27trapRetry.setStatus("mandatory")
_Els10_27trapNumber_Type = Integer32
_Els10_27trapNumber_Object = MibScalar
els10_27trapNumber = _Els10_27trapNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 6),
    _Els10_27trapNumber_Type()
)
els10_27trapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapNumber.setStatus("mandatory")
_Els10_27trapTable_Object = MibTable
els10_27trapTable = _Els10_27trapTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7)
)
if mibBuilder.loadTexts:
    els10_27trapTable.setStatus("mandatory")
_Els10_27trapEntry_Object = MibTableRow
els10_27trapEntry = _Els10_27trapEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1)
)
els10_27trapEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27trapEntryIndex"),
)
if mibBuilder.loadTexts:
    els10_27trapEntry.setStatus("mandatory")
_Els10_27trapEntryIndex_Type = Integer32
_Els10_27trapEntryIndex_Object = MibScalar
els10_27trapEntryIndex = _Els10_27trapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1, 1),
    _Els10_27trapEntryIndex_Type()
)
els10_27trapEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapEntryIndex.setStatus("mandatory")
_Els10_27trapEntryTimeStamp_Type = TimeTicks
_Els10_27trapEntryTimeStamp_Object = MibScalar
els10_27trapEntryTimeStamp = _Els10_27trapEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1, 2),
    _Els10_27trapEntryTimeStamp_Type()
)
els10_27trapEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapEntryTimeStamp.setStatus("mandatory")
_Els10_27trapEntryText_Type = DisplayString
_Els10_27trapEntryText_Object = MibScalar
els10_27trapEntryText = _Els10_27trapEntryText_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1, 3),
    _Els10_27trapEntryText_Type()
)
els10_27trapEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapEntryText.setStatus("mandatory")
_Els10_27trapEntryNumber_Type = Integer32
_Els10_27trapEntryNumber_Object = MibScalar
els10_27trapEntryNumber = _Els10_27trapEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1, 4),
    _Els10_27trapEntryNumber_Type()
)
els10_27trapEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapEntryNumber.setStatus("mandatory")


class _Els10_27trapEntrySeverity_Type(Integer32):
    """Custom type els10_27trapEntrySeverity based on Integer32"""
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


_Els10_27trapEntrySeverity_Type.__name__ = "Integer32"
_Els10_27trapEntrySeverity_Object = MibScalar
els10_27trapEntrySeverity = _Els10_27trapEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 15, 7, 1, 5),
    _Els10_27trapEntrySeverity_Type()
)
els10_27trapEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27trapEntrySeverity.setStatus("mandatory")
_Els10_27pingMgt_ObjectIdentity = ObjectIdentity
els10_27pingMgt = _Els10_27pingMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 16)
)
_Els10_27pingDataTimeout_Type = TimeTicks
_Els10_27pingDataTimeout_Object = MibScalar
els10_27pingDataTimeout = _Els10_27pingDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 1),
    _Els10_27pingDataTimeout_Type()
)
els10_27pingDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingDataTimeout.setStatus("mandatory")
_Els10_27pingTable_Object = MibTable
els10_27pingTable = _Els10_27pingTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2)
)
if mibBuilder.loadTexts:
    els10_27pingTable.setStatus("mandatory")
_Els10_27pingEntry_Object = MibTableRow
els10_27pingEntry = _Els10_27pingEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1)
)
els10_27pingEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27pingNMSAddr"),
    (0, "CT-ELS10-MIB", "els10-27pingDestAddr"),
)
if mibBuilder.loadTexts:
    els10_27pingEntry.setStatus("mandatory")
_Els10_27pingNMSAddr_Type = IpAddress
_Els10_27pingNMSAddr_Object = MibScalar
els10_27pingNMSAddr = _Els10_27pingNMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 1),
    _Els10_27pingNMSAddr_Type()
)
els10_27pingNMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingNMSAddr.setStatus("mandatory")
_Els10_27pingDestAddr_Type = IpAddress
_Els10_27pingDestAddr_Object = MibScalar
els10_27pingDestAddr = _Els10_27pingDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 2),
    _Els10_27pingDestAddr_Type()
)
els10_27pingDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingDestAddr.setStatus("mandatory")


class _Els10_27pingState_Type(Integer32):
    """Custom type els10_27pingState based on Integer32"""
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
        *(("active", 1),
          ("completed", 3),
          ("not-started", 0),
          ("timed-out", 2))
    )


_Els10_27pingState_Type.__name__ = "Integer32"
_Els10_27pingState_Object = MibScalar
els10_27pingState = _Els10_27pingState_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 3),
    _Els10_27pingState_Type()
)
els10_27pingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingState.setStatus("mandatory")
_Els10_27pingCount_Type = Integer32
_Els10_27pingCount_Object = MibScalar
els10_27pingCount = _Els10_27pingCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 4),
    _Els10_27pingCount_Type()
)
els10_27pingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingCount.setStatus("mandatory")
_Els10_27pingDataSize_Type = Integer32
_Els10_27pingDataSize_Object = MibScalar
els10_27pingDataSize = _Els10_27pingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 5),
    _Els10_27pingDataSize_Type()
)
els10_27pingDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingDataSize.setStatus("mandatory")
_Els10_27pingWait_Type = TimeTicks
_Els10_27pingWait_Object = MibScalar
els10_27pingWait = _Els10_27pingWait_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 6),
    _Els10_27pingWait_Type()
)
els10_27pingWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingWait.setStatus("mandatory")
_Els10_27pingTimeOut_Type = TimeTicks
_Els10_27pingTimeOut_Object = MibScalar
els10_27pingTimeOut = _Els10_27pingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 7),
    _Els10_27pingTimeOut_Type()
)
els10_27pingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingTimeOut.setStatus("mandatory")


class _Els10_27pingOperation_Type(Integer32):
    """Custom type els10_27pingOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Els10_27pingOperation_Type.__name__ = "Integer32"
_Els10_27pingOperation_Object = MibScalar
els10_27pingOperation = _Els10_27pingOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 8),
    _Els10_27pingOperation_Type()
)
els10_27pingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27pingOperation.setStatus("mandatory")
_Els10_27pingMin_Type = TimeTicks
_Els10_27pingMin_Object = MibScalar
els10_27pingMin = _Els10_27pingMin_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 9),
    _Els10_27pingMin_Type()
)
els10_27pingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingMin.setStatus("mandatory")
_Els10_27pingMax_Type = TimeTicks
_Els10_27pingMax_Object = MibScalar
els10_27pingMax = _Els10_27pingMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 10),
    _Els10_27pingMax_Type()
)
els10_27pingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingMax.setStatus("mandatory")
_Els10_27pingAvg_Type = TimeTicks
_Els10_27pingAvg_Object = MibScalar
els10_27pingAvg = _Els10_27pingAvg_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 11),
    _Els10_27pingAvg_Type()
)
els10_27pingAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingAvg.setStatus("mandatory")
_Els10_27pingNumTransmitted_Type = Integer32
_Els10_27pingNumTransmitted_Object = MibScalar
els10_27pingNumTransmitted = _Els10_27pingNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 12),
    _Els10_27pingNumTransmitted_Type()
)
els10_27pingNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingNumTransmitted.setStatus("mandatory")
_Els10_27pingNumReceived_Type = Integer32
_Els10_27pingNumReceived_Object = MibScalar
els10_27pingNumReceived = _Els10_27pingNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 16, 2, 1, 13),
    _Els10_27pingNumReceived_Type()
)
els10_27pingNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27pingNumReceived.setStatus("mandatory")
_Els10_27traceMgt_ObjectIdentity = ObjectIdentity
els10_27traceMgt = _Els10_27traceMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 17)
)
_Els10_27traceDataTimeout_Type = TimeTicks
_Els10_27traceDataTimeout_Object = MibScalar
els10_27traceDataTimeout = _Els10_27traceDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 1),
    _Els10_27traceDataTimeout_Type()
)
els10_27traceDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceDataTimeout.setStatus("mandatory")
_Els10_27traceTable_Object = MibTable
els10_27traceTable = _Els10_27traceTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2)
)
if mibBuilder.loadTexts:
    els10_27traceTable.setStatus("mandatory")
_Els10_27traceEntry_Object = MibTableRow
els10_27traceEntry = _Els10_27traceEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1)
)
els10_27traceEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27traceNMSAddr"),
    (0, "CT-ELS10-MIB", "els10-27traceDestAddr"),
    (0, "CT-ELS10-MIB", "els10-27traceHop"),
    (0, "CT-ELS10-MIB", "els10-27traceProbe"),
)
if mibBuilder.loadTexts:
    els10_27traceEntry.setStatus("mandatory")
_Els10_27traceNMSAddr_Type = IpAddress
_Els10_27traceNMSAddr_Object = MibScalar
els10_27traceNMSAddr = _Els10_27traceNMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 1),
    _Els10_27traceNMSAddr_Type()
)
els10_27traceNMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceNMSAddr.setStatus("mandatory")
_Els10_27traceDestAddr_Type = IpAddress
_Els10_27traceDestAddr_Object = MibScalar
els10_27traceDestAddr = _Els10_27traceDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 2),
    _Els10_27traceDestAddr_Type()
)
els10_27traceDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceDestAddr.setStatus("mandatory")
_Els10_27traceMaxTTL_Type = Integer32
_Els10_27traceMaxTTL_Object = MibScalar
els10_27traceMaxTTL = _Els10_27traceMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 3),
    _Els10_27traceMaxTTL_Type()
)
els10_27traceMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceMaxTTL.setStatus("mandatory")
_Els10_27traceDataSize_Type = Integer32
_Els10_27traceDataSize_Object = MibScalar
els10_27traceDataSize = _Els10_27traceDataSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 4),
    _Els10_27traceDataSize_Type()
)
els10_27traceDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceDataSize.setStatus("mandatory")
_Els10_27traceNumProbes_Type = Integer32
_Els10_27traceNumProbes_Object = MibScalar
els10_27traceNumProbes = _Els10_27traceNumProbes_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 5),
    _Els10_27traceNumProbes_Type()
)
els10_27traceNumProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceNumProbes.setStatus("mandatory")
_Els10_27traceWait_Type = TimeTicks
_Els10_27traceWait_Object = MibScalar
els10_27traceWait = _Els10_27traceWait_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 6),
    _Els10_27traceWait_Type()
)
els10_27traceWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceWait.setStatus("mandatory")


class _Els10_27traceOperation_Type(Integer32):
    """Custom type els10_27traceOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Els10_27traceOperation_Type.__name__ = "Integer32"
_Els10_27traceOperation_Object = MibScalar
els10_27traceOperation = _Els10_27traceOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 7),
    _Els10_27traceOperation_Type()
)
els10_27traceOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27traceOperation.setStatus("mandatory")
_Els10_27traceHop_Type = Integer32
_Els10_27traceHop_Object = MibScalar
els10_27traceHop = _Els10_27traceHop_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 8),
    _Els10_27traceHop_Type()
)
els10_27traceHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceHop.setStatus("mandatory")
_Els10_27traceHopAddr_Type = IpAddress
_Els10_27traceHopAddr_Object = MibScalar
els10_27traceHopAddr = _Els10_27traceHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 9),
    _Els10_27traceHopAddr_Type()
)
els10_27traceHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceHopAddr.setStatus("mandatory")
_Els10_27traceProbe_Type = Integer32
_Els10_27traceProbe_Object = MibScalar
els10_27traceProbe = _Els10_27traceProbe_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 10),
    _Els10_27traceProbe_Type()
)
els10_27traceProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceProbe.setStatus("mandatory")


class _Els10_27traceState_Type(Integer32):
    """Custom type els10_27traceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("completed", 5),
          ("host-unreachable", 3),
          ("net-unreachable", 4),
          ("not-started", 0),
          ("time-exceeded", 2))
    )


_Els10_27traceState_Type.__name__ = "Integer32"
_Els10_27traceState_Object = MibScalar
els10_27traceState = _Els10_27traceState_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 11),
    _Els10_27traceState_Type()
)
els10_27traceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceState.setStatus("mandatory")
_Els10_27traceTime_Type = TimeTicks
_Els10_27traceTime_Object = MibScalar
els10_27traceTime = _Els10_27traceTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 17, 2, 1, 12),
    _Els10_27traceTime_Type()
)
els10_27traceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27traceTime.setStatus("mandatory")
_Els10_27volmirrorgroup_ObjectIdentity = ObjectIdentity
els10_27volmirrorgroup = _Els10_27volmirrorgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 19)
)


class _Els10_27volmirrorMode_Type(Integer32):
    """Custom type els10_27volmirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Els10_27volmirrorMode_Type.__name__ = "Integer32"
_Els10_27volmirrorMode_Object = MibScalar
els10_27volmirrorMode = _Els10_27volmirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 1),
    _Els10_27volmirrorMode_Type()
)
els10_27volmirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27volmirrorMode.setStatus("mandatory")
_Els10_27volmirrorPort_Type = Integer32
_Els10_27volmirrorPort_Object = MibScalar
els10_27volmirrorPort = _Els10_27volmirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 2),
    _Els10_27volmirrorPort_Type()
)
els10_27volmirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27volmirrorPort.setStatus("mandatory")
_Els10_27volmonitorPort_Type = Integer32
_Els10_27volmonitorPort_Object = MibScalar
els10_27volmonitorPort = _Els10_27volmonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 3),
    _Els10_27volmonitorPort_Type()
)
els10_27volmonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27volmonitorPort.setStatus("mandatory")
_Els10_27volMirrorMacTable_Object = MibTable
els10_27volMirrorMacTable = _Els10_27volMirrorMacTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 4)
)
if mibBuilder.loadTexts:
    els10_27volMirrorMacTable.setStatus("mandatory")
_Els10_27volmirrorMacEntry_Object = MibTableRow
els10_27volmirrorMacEntry = _Els10_27volmirrorMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 4, 1)
)
els10_27volmirrorMacEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27volmirrorIndex"),
)
if mibBuilder.loadTexts:
    els10_27volmirrorMacEntry.setStatus("mandatory")
_Els10_27volmirrorIndex_Type = Integer32
_Els10_27volmirrorIndex_Object = MibScalar
els10_27volmirrorIndex = _Els10_27volmirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 4, 1, 1),
    _Els10_27volmirrorIndex_Type()
)
els10_27volmirrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27volmirrorIndex.setStatus("mandatory")
_Els10_27volmirrorMac1_Type = OctetString
_Els10_27volmirrorMac1_Object = MibScalar
els10_27volmirrorMac1 = _Els10_27volmirrorMac1_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 19, 4, 1, 2),
    _Els10_27volmirrorMac1_Type()
)
els10_27volmirrorMac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27volmirrorMac1.setStatus("mandatory")
_Els10_27VlanBridgeConfig_ObjectIdentity = ObjectIdentity
els10_27VlanBridgeConfig = _Els10_27VlanBridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 20)
)
_Els10_27VlanVersionNumber_Type = Integer32
_Els10_27VlanVersionNumber_Object = MibScalar
els10_27VlanVersionNumber = _Els10_27VlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 1),
    _Els10_27VlanVersionNumber_Type()
)
els10_27VlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27VlanVersionNumber.setStatus("mandatory")


class _Els10_27VlanOperatingMode_Type(Integer32):
    """Custom type els10_27VlanOperatingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021Q", 2),
          ("ieee8021d", 1))
    )


_Els10_27VlanOperatingMode_Type.__name__ = "Integer32"
_Els10_27VlanOperatingMode_Object = MibScalar
els10_27VlanOperatingMode = _Els10_27VlanOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 2),
    _Els10_27VlanOperatingMode_Type()
)
els10_27VlanOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanOperatingMode.setStatus("mandatory")


class _Els10_27VlanResetDefaults_Type(Integer32):
    """Custom type els10_27VlanResetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operating", 1),
          ("reset", 2))
    )


_Els10_27VlanResetDefaults_Type.__name__ = "Integer32"
_Els10_27VlanResetDefaults_Object = MibScalar
els10_27VlanResetDefaults = _Els10_27VlanResetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 3),
    _Els10_27VlanResetDefaults_Type()
)
els10_27VlanResetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanResetDefaults.setStatus("mandatory")


class _Els10_27VlanGVRPEnable_Type(Integer32):
    """Custom type els10_27VlanGVRPEnable based on Integer32"""
    defaultValue = 2

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


_Els10_27VlanGVRPEnable_Type.__name__ = "Integer32"
_Els10_27VlanGVRPEnable_Object = MibScalar
els10_27VlanGVRPEnable = _Els10_27VlanGVRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 4),
    _Els10_27VlanGVRPEnable_Type()
)
els10_27VlanGVRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanGVRPEnable.setStatus("mandatory")
_Els10_27VlanAccessList_Type = Integer32
_Els10_27VlanAccessList_Object = MibScalar
els10_27VlanAccessList = _Els10_27VlanAccessList_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 5),
    _Els10_27VlanAccessList_Type()
)
els10_27VlanAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanAccessList.setStatus("mandatory")
_Els10_27VlanConfigVlan_ObjectIdentity = ObjectIdentity
els10_27VlanConfigVlan = _Els10_27VlanConfigVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6)
)
_Els10_27VlanNumActiveEntries_Type = Integer32
_Els10_27VlanNumActiveEntries_Object = MibScalar
els10_27VlanNumActiveEntries = _Els10_27VlanNumActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 1),
    _Els10_27VlanNumActiveEntries_Type()
)
els10_27VlanNumActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27VlanNumActiveEntries.setStatus("mandatory")
_Els10_27VlanNumConfiguredEntries_Type = Integer32
_Els10_27VlanNumConfiguredEntries_Object = MibScalar
els10_27VlanNumConfiguredEntries = _Els10_27VlanNumConfiguredEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 2),
    _Els10_27VlanNumConfiguredEntries_Type()
)
els10_27VlanNumConfiguredEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27VlanNumConfiguredEntries.setStatus("mandatory")
_Els10_27VlanMaxNumEntries_Type = Integer32
_Els10_27VlanMaxNumEntries_Object = MibScalar
els10_27VlanMaxNumEntries = _Els10_27VlanMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 3),
    _Els10_27VlanMaxNumEntries_Type()
)
els10_27VlanMaxNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27VlanMaxNumEntries.setStatus("mandatory")
_Els10_27VlanConfigTable_Object = MibTable
els10_27VlanConfigTable = _Els10_27VlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4)
)
if mibBuilder.loadTexts:
    els10_27VlanConfigTable.setStatus("mandatory")
_Els10_27VlanConfigEntry_Object = MibTableRow
els10_27VlanConfigEntry = _Els10_27VlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1)
)
els10_27VlanConfigEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27VlanConfigVID"),
)
if mibBuilder.loadTexts:
    els10_27VlanConfigEntry.setStatus("mandatory")
_Els10_27VlanConfigIndex_Type = Integer32
_Els10_27VlanConfigIndex_Object = MibScalar
els10_27VlanConfigIndex = _Els10_27VlanConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 1),
    _Els10_27VlanConfigIndex_Type()
)
els10_27VlanConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigIndex.setStatus("mandatory")


class _Els10_27VlanConfigVID_Type(Integer32):
    """Custom type els10_27VlanConfigVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Els10_27VlanConfigVID_Type.__name__ = "Integer32"
_Els10_27VlanConfigVID_Object = MibScalar
els10_27VlanConfigVID = _Els10_27VlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 2),
    _Els10_27VlanConfigVID_Type()
)
els10_27VlanConfigVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigVID.setStatus("mandatory")
_Els10_27VlanConfigPorts_Type = Integer32
_Els10_27VlanConfigPorts_Object = MibScalar
els10_27VlanConfigPorts = _Els10_27VlanConfigPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 3),
    _Els10_27VlanConfigPorts_Type()
)
els10_27VlanConfigPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigPorts.setStatus("mandatory")
_Els10_27VlanConfigIP_Type = Integer32
_Els10_27VlanConfigIP_Object = MibScalar
els10_27VlanConfigIP = _Els10_27VlanConfigIP_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 4),
    _Els10_27VlanConfigIP_Type()
)
els10_27VlanConfigIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigIP.setStatus("mandatory")
_Els10_27VlanConfigIPMask_Type = Integer32
_Els10_27VlanConfigIPMask_Object = MibScalar
els10_27VlanConfigIPMask = _Els10_27VlanConfigIPMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 5),
    _Els10_27VlanConfigIPMask_Type()
)
els10_27VlanConfigIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigIPMask.setStatus("mandatory")


class _Els10_27VlanConfigName_Type(DisplayString):
    """Custom type els10_27VlanConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Els10_27VlanConfigName_Type.__name__ = "DisplayString"
_Els10_27VlanConfigName_Object = MibScalar
els10_27VlanConfigName = _Els10_27VlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 6),
    _Els10_27VlanConfigName_Type()
)
els10_27VlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigName.setStatus("mandatory")


class _Els10_27VlanConfigStatus_Type(Integer32):
    """Custom type els10_27VlanConfigStatus based on Integer32"""
    defaultValue = 2

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


_Els10_27VlanConfigStatus_Type.__name__ = "Integer32"
_Els10_27VlanConfigStatus_Object = MibScalar
els10_27VlanConfigStatus = _Els10_27VlanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 7),
    _Els10_27VlanConfigStatus_Type()
)
els10_27VlanConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigStatus.setStatus("mandatory")


class _Els10_27VlanConfigEstablish_Type(Integer32):
    """Custom type els10_27VlanConfigEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_Els10_27VlanConfigEstablish_Type.__name__ = "Integer32"
_Els10_27VlanConfigEstablish_Object = MibScalar
els10_27VlanConfigEstablish = _Els10_27VlanConfigEstablish_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 4, 1, 8),
    _Els10_27VlanConfigEstablish_Type()
)
els10_27VlanConfigEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanConfigEstablish.setStatus("mandatory")
_Els10_27VlanConfigEgressTable_Object = MibTable
els10_27VlanConfigEgressTable = _Els10_27VlanConfigEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5)
)
if mibBuilder.loadTexts:
    els10_27VlanConfigEgressTable.setStatus("mandatory")
_Els10_27VlanConfigEgressEntry_Object = MibTableRow
els10_27VlanConfigEgressEntry = _Els10_27VlanConfigEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5, 1)
)
els10_27VlanConfigEgressEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27VlanEgressVID"),
)
if mibBuilder.loadTexts:
    els10_27VlanConfigEgressEntry.setStatus("mandatory")
_Els10_27VlanEgressIndex_Type = Integer32
_Els10_27VlanEgressIndex_Object = MibScalar
els10_27VlanEgressIndex = _Els10_27VlanEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5, 1, 1),
    _Els10_27VlanEgressIndex_Type()
)
els10_27VlanEgressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanEgressIndex.setStatus("mandatory")


class _Els10_27VlanEgressVID_Type(Integer32):
    """Custom type els10_27VlanEgressVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Els10_27VlanEgressVID_Type.__name__ = "Integer32"
_Els10_27VlanEgressVID_Object = MibScalar
els10_27VlanEgressVID = _Els10_27VlanEgressVID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5, 1, 2),
    _Els10_27VlanEgressVID_Type()
)
els10_27VlanEgressVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanEgressVID.setStatus("mandatory")
_Els10_27VlanEgressList_Type = Integer32
_Els10_27VlanEgressList_Object = MibScalar
els10_27VlanEgressList = _Els10_27VlanEgressList_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5, 1, 3),
    _Els10_27VlanEgressList_Type()
)
els10_27VlanEgressList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanEgressList.setStatus("mandatory")


class _Els10_27VlanEgressStatus_Type(Integer32):
    """Custom type els10_27VlanEgressStatus based on Integer32"""
    defaultValue = 2

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


_Els10_27VlanEgressStatus_Type.__name__ = "Integer32"
_Els10_27VlanEgressStatus_Object = MibScalar
els10_27VlanEgressStatus = _Els10_27VlanEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 5, 1, 4),
    _Els10_27VlanEgressStatus_Type()
)
els10_27VlanEgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanEgressStatus.setStatus("mandatory")
_Els10_27VlanFilterGVRPTable_Object = MibTable
els10_27VlanFilterGVRPTable = _Els10_27VlanFilterGVRPTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6)
)
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPTable.setStatus("mandatory")
_Els10_27VlanFilterGVRPEntry_Object = MibTableRow
els10_27VlanFilterGVRPEntry = _Els10_27VlanFilterGVRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1)
)
els10_27VlanFilterGVRPEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27VlanFilterGVRPVID"),
)
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPEntry.setStatus("mandatory")
_Els10_27VlanFilterGVRPIndex_Type = Integer32
_Els10_27VlanFilterGVRPIndex_Object = MibScalar
els10_27VlanFilterGVRPIndex = _Els10_27VlanFilterGVRPIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1, 1),
    _Els10_27VlanFilterGVRPIndex_Type()
)
els10_27VlanFilterGVRPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPIndex.setStatus("mandatory")


class _Els10_27VlanFilterGVRPVID_Type(Integer32):
    """Custom type els10_27VlanFilterGVRPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Els10_27VlanFilterGVRPVID_Type.__name__ = "Integer32"
_Els10_27VlanFilterGVRPVID_Object = MibScalar
els10_27VlanFilterGVRPVID = _Els10_27VlanFilterGVRPVID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1, 2),
    _Els10_27VlanFilterGVRPVID_Type()
)
els10_27VlanFilterGVRPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPVID.setStatus("mandatory")
_Els10_27VlanFilterGVRPList_Type = Integer32
_Els10_27VlanFilterGVRPList_Object = MibScalar
els10_27VlanFilterGVRPList = _Els10_27VlanFilterGVRPList_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1, 3),
    _Els10_27VlanFilterGVRPList_Type()
)
els10_27VlanFilterGVRPList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPList.setStatus("mandatory")


class _Els10_27VlanFilterGVRPStatus_Type(Integer32):
    """Custom type els10_27VlanFilterGVRPStatus based on Integer32"""
    defaultValue = 2

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


_Els10_27VlanFilterGVRPStatus_Type.__name__ = "Integer32"
_Els10_27VlanFilterGVRPStatus_Object = MibScalar
els10_27VlanFilterGVRPStatus = _Els10_27VlanFilterGVRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1, 4),
    _Els10_27VlanFilterGVRPStatus_Type()
)
els10_27VlanFilterGVRPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPStatus.setStatus("mandatory")


class _Els10_27VlanFilterGVRPEstablishVID_Type(Integer32):
    """Custom type els10_27VlanFilterGVRPEstablishVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_Els10_27VlanFilterGVRPEstablishVID_Type.__name__ = "Integer32"
_Els10_27VlanFilterGVRPEstablishVID_Object = MibScalar
els10_27VlanFilterGVRPEstablishVID = _Els10_27VlanFilterGVRPEstablishVID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 6, 1, 5),
    _Els10_27VlanFilterGVRPEstablishVID_Type()
)
els10_27VlanFilterGVRPEstablishVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanFilterGVRPEstablishVID.setStatus("mandatory")
_Els10_27VlanStaticTable_Object = MibTable
els10_27VlanStaticTable = _Els10_27VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7)
)
if mibBuilder.loadTexts:
    els10_27VlanStaticTable.setStatus("mandatory")
_Els10_27VlanStaticEntry_Object = MibTableRow
els10_27VlanStaticEntry = _Els10_27VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7, 1)
)
els10_27VlanStaticEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27VlanStaticVID"),
)
if mibBuilder.loadTexts:
    els10_27VlanStaticEntry.setStatus("mandatory")


class _Els10_27VlanStaticVID_Type(Integer32):
    """Custom type els10_27VlanStaticVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Els10_27VlanStaticVID_Type.__name__ = "Integer32"
_Els10_27VlanStaticVID_Object = MibScalar
els10_27VlanStaticVID = _Els10_27VlanStaticVID_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7, 1, 1),
    _Els10_27VlanStaticVID_Type()
)
els10_27VlanStaticVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanStaticVID.setStatus("mandatory")
_Els10_27VlanStaticMAC_Type = PhysAddress
_Els10_27VlanStaticMAC_Object = MibScalar
els10_27VlanStaticMAC = _Els10_27VlanStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7, 1, 2),
    _Els10_27VlanStaticMAC_Type()
)
els10_27VlanStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanStaticMAC.setStatus("mandatory")


class _Els10_27VlanStaticPort_Type(Integer32):
    """Custom type els10_27VlanStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_Els10_27VlanStaticPort_Type.__name__ = "Integer32"
_Els10_27VlanStaticPort_Object = MibScalar
els10_27VlanStaticPort = _Els10_27VlanStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7, 1, 3),
    _Els10_27VlanStaticPort_Type()
)
els10_27VlanStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanStaticPort.setStatus("mandatory")


class _Els10_27VlanStaticEstablish_Type(Integer32):
    """Custom type els10_27VlanStaticEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_Els10_27VlanStaticEstablish_Type.__name__ = "Integer32"
_Els10_27VlanStaticEstablish_Object = MibScalar
els10_27VlanStaticEstablish = _Els10_27VlanStaticEstablish_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 20, 6, 7, 1, 4),
    _Els10_27VlanStaticEstablish_Type()
)
els10_27VlanStaticEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27VlanStaticEstablish.setStatus("mandatory")
_Els10_27volipmgroup_ObjectIdentity = ObjectIdentity
els10_27volipmgroup = _Els10_27volipmgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 21)
)


class _Els10_27IPMulticastStatus_Type(Integer32):
    """Custom type els10_27IPMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Els10_27IPMulticastStatus_Type.__name__ = "Integer32"
_Els10_27IPMulticastStatus_Object = MibScalar
els10_27IPMulticastStatus = _Els10_27IPMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 21, 1),
    _Els10_27IPMulticastStatus_Type()
)
els10_27IPMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27IPMulticastStatus.setStatus("mandatory")
_Els10_27ipmInterfaceRtr_Type = Integer32
_Els10_27ipmInterfaceRtr_Object = MibScalar
els10_27ipmInterfaceRtr = _Els10_27ipmInterfaceRtr_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 21, 2),
    _Els10_27ipmInterfaceRtr_Type()
)
els10_27ipmInterfaceRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27ipmInterfaceRtr.setStatus("mandatory")
_Els10_27voligmpgroup_ObjectIdentity = ObjectIdentity
els10_27voligmpgroup = _Els10_27voligmpgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 22)
)


class _Els10_27igmpStatus_Type(Integer32):
    """Custom type els10_27igmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_Els10_27igmpStatus_Type.__name__ = "Integer32"
_Els10_27igmpStatus_Object = MibScalar
els10_27igmpStatus = _Els10_27igmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 1),
    _Els10_27igmpStatus_Type()
)
els10_27igmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27igmpStatus.setStatus("mandatory")


class _Els10_27igmpQueryStatus_Type(Integer32):
    """Custom type els10_27igmpQueryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Els10_27igmpQueryStatus_Type.__name__ = "Integer32"
_Els10_27igmpQueryStatus_Object = MibScalar
els10_27igmpQueryStatus = _Els10_27igmpQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 2),
    _Els10_27igmpQueryStatus_Type()
)
els10_27igmpQueryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27igmpQueryStatus.setStatus("mandatory")
_Els10_27igmpQueryCount_Type = Integer32
_Els10_27igmpQueryCount_Object = MibScalar
els10_27igmpQueryCount = _Els10_27igmpQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 3),
    _Els10_27igmpQueryCount_Type()
)
els10_27igmpQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27igmpQueryCount.setStatus("mandatory")
_Els10_27igmpPortDelay_Type = Integer32
_Els10_27igmpPortDelay_Object = MibScalar
els10_27igmpPortDelay = _Els10_27igmpPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 4),
    _Els10_27igmpPortDelay_Type()
)
els10_27igmpPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27igmpPortDelay.setStatus("mandatory")
_Els10_27igmpCacheTable_Object = MibTable
els10_27igmpCacheTable = _Els10_27igmpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 5)
)
if mibBuilder.loadTexts:
    els10_27igmpCacheTable.setStatus("mandatory")
_Els10_27igmpCacheEntry_Object = MibTableRow
els10_27igmpCacheEntry = _Els10_27igmpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 5, 1)
)
els10_27igmpCacheEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27igmpCacheAddress"),
    (0, "CT-ELS10-MIB", "els10-27igmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    els10_27igmpCacheEntry.setStatus("mandatory")
_Els10_27igmpCacheAddress_Type = IpAddress
_Els10_27igmpCacheAddress_Object = MibScalar
els10_27igmpCacheAddress = _Els10_27igmpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 5, 1, 1),
    _Els10_27igmpCacheAddress_Type()
)
els10_27igmpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27igmpCacheAddress.setStatus("mandatory")
_Els10_27igmpCacheIfIndex_Type = Integer32
_Els10_27igmpCacheIfIndex_Object = MibScalar
els10_27igmpCacheIfIndex = _Els10_27igmpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 5, 1, 2),
    _Els10_27igmpCacheIfIndex_Type()
)
els10_27igmpCacheIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27igmpCacheIfIndex.setStatus("mandatory")
_Els10_27igmpCacheExpiryTime_Type = TimeTicks
_Els10_27igmpCacheExpiryTime_Object = MibScalar
els10_27igmpCacheExpiryTime = _Els10_27igmpCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 22, 5, 1, 3),
    _Els10_27igmpCacheExpiryTime_Type()
)
els10_27igmpCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27igmpCacheExpiryTime.setStatus("mandatory")
_Els10_27FlowControlCtl_ObjectIdentity = ObjectIdentity
els10_27FlowControlCtl = _Els10_27FlowControlCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 9, 23)
)
_Els10_27FlowControlBackPressure_Type = Integer32
_Els10_27FlowControlBackPressure_Object = MibScalar
els10_27FlowControlBackPressure = _Els10_27FlowControlBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 1),
    _Els10_27FlowControlBackPressure_Type()
)
els10_27FlowControlBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27FlowControlBackPressure.setStatus("mandatory")
_Els10_27FlowControlThresholdValue_Type = Integer32
_Els10_27FlowControlThresholdValue_Object = MibScalar
els10_27FlowControlThresholdValue = _Els10_27FlowControlThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 2),
    _Els10_27FlowControlThresholdValue_Type()
)
els10_27FlowControlThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27FlowControlThresholdValue.setStatus("mandatory")
_Els10_27FlowControlPauseInteval_Type = Integer32
_Els10_27FlowControlPauseInteval_Object = MibScalar
els10_27FlowControlPauseInteval = _Els10_27FlowControlPauseInteval_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 3),
    _Els10_27FlowControlPauseInteval_Type()
)
els10_27FlowControlPauseInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27FlowControlPauseInteval.setStatus("mandatory")
_Els10_27FlowControlTable_Object = MibTable
els10_27FlowControlTable = _Els10_27FlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4)
)
if mibBuilder.loadTexts:
    els10_27FlowControlTable.setStatus("mandatory")
_Els10_27FlowControlEntry_Object = MibTableRow
els10_27FlowControlEntry = _Els10_27FlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4, 1)
)
els10_27FlowControlEntry.setIndexNames(
    (0, "CT-ELS10-MIB", "els10-27FlowControlInterface"),
)
if mibBuilder.loadTexts:
    els10_27FlowControlEntry.setStatus("mandatory")
_Els10_27FlowControlInterface_Type = Integer32
_Els10_27FlowControlInterface_Object = MibScalar
els10_27FlowControlInterface = _Els10_27FlowControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4, 1, 1),
    _Els10_27FlowControlInterface_Type()
)
els10_27FlowControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27FlowControlInterface.setStatus("mandatory")
_Els10_27FlowControlEnable_Type = Integer32
_Els10_27FlowControlEnable_Object = MibScalar
els10_27FlowControlEnable = _Els10_27FlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4, 1, 2),
    _Els10_27FlowControlEnable_Type()
)
els10_27FlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    els10_27FlowControlEnable.setStatus("mandatory")
_Els10_27FlowControlRxPauseFrames_Type = Integer32
_Els10_27FlowControlRxPauseFrames_Object = MibScalar
els10_27FlowControlRxPauseFrames = _Els10_27FlowControlRxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4, 1, 3),
    _Els10_27FlowControlRxPauseFrames_Type()
)
els10_27FlowControlRxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27FlowControlRxPauseFrames.setStatus("mandatory")
_Els10_27FlowControlTxPauseFrames_Type = Integer32
_Els10_27FlowControlTxPauseFrames_Object = MibScalar
els10_27FlowControlTxPauseFrames = _Els10_27FlowControlTxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 97, 9, 23, 4, 1, 4),
    _Els10_27FlowControlTxPauseFrames_Type()
)
els10_27FlowControlTxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    els10_27FlowControlTxPauseFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects

els10_27WriteStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 2)
)
els10_27WriteStatusTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27swdisWriteStatus"),
        ("CT-ELS10-MIB", "els10_27swdisDesc"))
)
if mibBuilder.loadTexts:
    els10_27WriteStatusTrap.setStatus(
        ""
    )

els10_27PortFunctionsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 3)
)
els10_27PortFunctionsTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27ifFunction"))
)
if mibBuilder.loadTexts:
    els10_27PortFunctionsTrap.setStatus(
        ""
    )

els10_27RxQueuesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 4)
)
els10_27RxQueuesTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27ifRxQueues"))
)
if mibBuilder.loadTexts:
    els10_27RxQueuesTrap.setStatus(
        ""
    )

els10_27RxStormFlagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 5)
)
els10_27RxStormFlagTrap.setObjects(
    ("CT-ELS10-MIB", "els10_27trapSeverity")
)
if mibBuilder.loadTexts:
    els10_27RxStormFlagTrap.setStatus(
        ""
    )

els10_27TxCongestsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 6)
)
els10_27TxCongestsTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27adminNAMReceiveCongests"))
)
if mibBuilder.loadTexts:
    els10_27TxCongestsTrap.setStatus(
        ""
    )

els10_27DebugStringIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 8)
)
els10_27DebugStringIdTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27debugStringID"),
        ("CT-ELS10-MIB", "els10_27debugString"))
)
if mibBuilder.loadTexts:
    els10_27DebugStringIdTrap.setStatus(
        ""
    )

els10_27LpbkOperationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 9)
)
els10_27LpbkOperationTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27lpbkOperation"),
        ("CT-ELS10-MIB", "els10_27lpbkErrorNoReceives"),
        ("CT-ELS10-MIB", "els10_27lpbkErrorBadReceives"))
)
if mibBuilder.loadTexts:
    els10_27LpbkOperationTrap.setStatus(
        ""
    )

els10_27TrunkStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 10)
)
els10_27TrunkStateTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkState"))
)
if mibBuilder.loadTexts:
    els10_27TrunkStateTrap.setStatus(
        ""
    )

els10_27TrunkBridgeAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 11)
)
els10_27TrunkBridgeAddrTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkRemoteBridgeAddr"))
)
if mibBuilder.loadTexts:
    els10_27TrunkBridgeAddrTrap.setStatus(
        ""
    )

els10_27TrunkIPAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 12)
)
els10_27TrunkIPAddrTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkRemoteIp"))
)
if mibBuilder.loadTexts:
    els10_27TrunkIPAddrTrap.setStatus(
        ""
    )

els10_27TrunkErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 13)
)
els10_27TrunkErrorTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkLastError"))
)
if mibBuilder.loadTexts:
    els10_27TrunkErrorTrap.setStatus(
        ""
    )

els10_27TrunkLinkOrdinalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 14)
)
els10_27TrunkLinkOrdinalTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkLinkOrdinal"))
)
if mibBuilder.loadTexts:
    els10_27TrunkLinkOrdinalTrap.setStatus(
        ""
    )

els10_27TrunkLinkCountTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 15)
)
els10_27TrunkLinkCountTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27trunkLinkCount"))
)
if mibBuilder.loadTexts:
    els10_27TrunkLinkCountTrap.setStatus(
        ""
    )

els10_27DiagUnitBootedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 16)
)
els10_27DiagUnitBootedTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27adminFatalErr"))
)
if mibBuilder.loadTexts:
    els10_27DiagUnitBootedTrap.setStatus(
        ""
    )

els10_27StorageFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 17)
)
els10_27StorageFailureTrap.setObjects(
    ("CT-ELS10-MIB", "els10_27trapSeverity")
)
if mibBuilder.loadTexts:
    els10_27StorageFailureTrap.setStatus(
        ""
    )

els10_27PortCongestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 18)
)
els10_27PortCongestedTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("IF-MIB", "ifOutDiscards"))
)
if mibBuilder.loadTexts:
    els10_27PortCongestedTrap.setStatus(
        ""
    )

els10_27TopChangeBegunTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 19)
)
els10_27TopChangeBegunTrap.setObjects(
    ("CT-ELS10-MIB", "els10_27trapSeverity")
)
if mibBuilder.loadTexts:
    els10_27TopChangeBegunTrap.setStatus(
        ""
    )

els10_27TopChangeEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 20)
)
els10_27TopChangeEndTrap.setObjects(
    ("CT-ELS10-MIB", "els10_27trapSeverity")
)
if mibBuilder.loadTexts:
    els10_27TopChangeEndTrap.setStatus(
        ""
    )

els10_27IfErrorsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 21)
)
els10_27IfErrorsTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    els10_27IfErrorsTrap.setStatus(
        ""
    )

els10_27StRootIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 22)
)
els10_27StRootIDTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    els10_27StRootIDTrap.setStatus(
        ""
    )

els10_27StRootCostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 23)
)
els10_27StRootCostTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpRootCost"))
)
if mibBuilder.loadTexts:
    els10_27StRootCostTrap.setStatus(
        ""
    )

els10_27StRootPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 24)
)
els10_27StRootPortTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpRootPort"))
)
if mibBuilder.loadTexts:
    els10_27StRootPortTrap.setStatus(
        ""
    )

els10_27StMaxAgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 25)
)
els10_27StMaxAgeTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpMaxAge"))
)
if mibBuilder.loadTexts:
    els10_27StMaxAgeTrap.setStatus(
        ""
    )

els10_27StHelloTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 26)
)
els10_27StHelloTimeTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpHelloTime"))
)
if mibBuilder.loadTexts:
    els10_27StHelloTimeTrap.setStatus(
        ""
    )

els10_27StForwardDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 27)
)
els10_27StForwardDelayTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpForwardDelay"))
)
if mibBuilder.loadTexts:
    els10_27StForwardDelayTrap.setStatus(
        ""
    )

els10_27StDesigRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 28)
)
els10_27StDesigRootTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"))
)
if mibBuilder.loadTexts:
    els10_27StDesigRootTrap.setStatus(
        ""
    )

els10_27StPortDesigBridgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 29)
)
els10_27StPortDesigBridgeTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"))
)
if mibBuilder.loadTexts:
    els10_27StPortDesigBridgeTrap.setStatus(
        ""
    )

els10_27StPortDesigCostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 30)
)
els10_27StPortDesigCostTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"))
)
if mibBuilder.loadTexts:
    els10_27StPortDesigCostTrap.setStatus(
        ""
    )

els10_27StPortDesigPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 31)
)
els10_27StPortDesigPortTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"))
)
if mibBuilder.loadTexts:
    els10_27StPortDesigPortTrap.setStatus(
        ""
    )

els10_27StPortStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 32)
)
els10_27StPortStateTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortState"))
)
if mibBuilder.loadTexts:
    els10_27StPortStateTrap.setStatus(
        ""
    )

els10_27InvalidConfigurationFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 34)
)
els10_27InvalidConfigurationFileTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"))
)
if mibBuilder.loadTexts:
    els10_27InvalidConfigurationFileTrap.setStatus(
        ""
    )

els10_27StInvalidFlashCodeImageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 35)
)
els10_27StInvalidFlashCodeImageTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("BRIDGE-MIB", "dot1dStpPortState"))
)
if mibBuilder.loadTexts:
    els10_27StInvalidFlashCodeImageTrap.setStatus(
        ""
    )

els10_27hwDiagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 97, 0, 100)
)
els10_27hwDiagTrap.setObjects(
      *(("CT-ELS10-MIB", "els10_27trapSeverity"),
        ("CT-ELS10-MIB", "els10_27hwDiagCode"))
)
if mibBuilder.loadTexts:
    els10_27hwDiagTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-ELS10-MIB",
    **{"sigma": sigma,
       "els10-27WriteStatusTrap": els10_27WriteStatusTrap,
       "els10-27PortFunctionsTrap": els10_27PortFunctionsTrap,
       "els10-27RxQueuesTrap": els10_27RxQueuesTrap,
       "els10-27RxStormFlagTrap": els10_27RxStormFlagTrap,
       "els10-27TxCongestsTrap": els10_27TxCongestsTrap,
       "els10-27DebugStringIdTrap": els10_27DebugStringIdTrap,
       "els10-27LpbkOperationTrap": els10_27LpbkOperationTrap,
       "els10-27TrunkStateTrap": els10_27TrunkStateTrap,
       "els10-27TrunkBridgeAddrTrap": els10_27TrunkBridgeAddrTrap,
       "els10-27TrunkIPAddrTrap": els10_27TrunkIPAddrTrap,
       "els10-27TrunkErrorTrap": els10_27TrunkErrorTrap,
       "els10-27TrunkLinkOrdinalTrap": els10_27TrunkLinkOrdinalTrap,
       "els10-27TrunkLinkCountTrap": els10_27TrunkLinkCountTrap,
       "els10-27DiagUnitBootedTrap": els10_27DiagUnitBootedTrap,
       "els10-27StorageFailureTrap": els10_27StorageFailureTrap,
       "els10-27PortCongestedTrap": els10_27PortCongestedTrap,
       "els10-27TopChangeBegunTrap": els10_27TopChangeBegunTrap,
       "els10-27TopChangeEndTrap": els10_27TopChangeEndTrap,
       "els10-27IfErrorsTrap": els10_27IfErrorsTrap,
       "els10-27StRootIDTrap": els10_27StRootIDTrap,
       "els10-27StRootCostTrap": els10_27StRootCostTrap,
       "els10-27StRootPortTrap": els10_27StRootPortTrap,
       "els10-27StMaxAgeTrap": els10_27StMaxAgeTrap,
       "els10-27StHelloTimeTrap": els10_27StHelloTimeTrap,
       "els10-27StForwardDelayTrap": els10_27StForwardDelayTrap,
       "els10-27StDesigRootTrap": els10_27StDesigRootTrap,
       "els10-27StPortDesigBridgeTrap": els10_27StPortDesigBridgeTrap,
       "els10-27StPortDesigCostTrap": els10_27StPortDesigCostTrap,
       "els10-27StPortDesigPortTrap": els10_27StPortDesigPortTrap,
       "els10-27StPortStateTrap": els10_27StPortStateTrap,
       "els10-27InvalidConfigurationFileTrap": els10_27InvalidConfigurationFileTrap,
       "els10-27StInvalidFlashCodeImageTrap": els10_27StInvalidFlashCodeImageTrap,
       "els10-27hwDiagTrap": els10_27hwDiagTrap,
       "sys": sys,
       "sysID": sysID,
       "sysReset": sysReset,
       "sysTrapPort": sysTrapPort,
       "els10-27": els10_27,
       "els10-27hw": els10_27hw,
       "els10-27hwDiagCode": els10_27hwDiagCode,
       "els10-27hwManufData": els10_27hwManufData,
       "els10-27hwPortCount": els10_27hwPortCount,
       "els10-27hwPortTable": els10_27hwPortTable,
       "els10-27hwPortEntry": els10_27hwPortEntry,
       "els10-27hwPortIndex": els10_27hwPortIndex,
       "els10-27hwPortType": els10_27hwPortType,
       "els10-27hwPortSubType": els10_27hwPortSubType,
       "els10-27hwPortDiagPassed": els10_27hwPortDiagPassed,
       "els10-27hwAddr": els10_27hwAddr,
       "els10-27hwUpLink": els10_27hwUpLink,
       "els10-27hwUpLinkManufData": els10_27hwUpLinkManufData,
       "els10-27sw": els10_27sw,
       "els10-27swNumber": els10_27swNumber,
       "els10-27swFilesetTable": els10_27swFilesetTable,
       "els10-27swFilesetEntry": els10_27swFilesetEntry,
       "els10-27swIndex": els10_27swIndex,
       "els10-27swDesc": els10_27swDesc,
       "els10-27swCount": els10_27swCount,
       "els10-27swType": els10_27swType,
       "els10-27swSizes": els10_27swSizes,
       "els10-27swStarts": els10_27swStarts,
       "els10-27swBases": els10_27swBases,
       "els10-27swFlashBank": els10_27swFlashBank,
       "els10-27admin": els10_27admin,
       "els10-27adminFatalErr": els10_27adminFatalErr,
       "els10-27adminAnyPass": els10_27adminAnyPass,
       "els10-27adminGetPass": els10_27adminGetPass,
       "els10-27adminNMSIPAddr": els10_27adminNMSIPAddr,
       "els10-27adminStorageFailure": els10_27adminStorageFailure,
       "els10-27adminAuthenticationFailure": els10_27adminAuthenticationFailure,
       "els10-27adminNAMReceiveCongests": els10_27adminNAMReceiveCongests,
       "els10-27adminArpEntries": els10_27adminArpEntries,
       "els10-27adminArpStatics": els10_27adminArpStatics,
       "els10-27adminArpOverflows": els10_27adminArpOverflows,
       "els10-27adminIpEntries": els10_27adminIpEntries,
       "els10-27adminIpStatics": els10_27adminIpStatics,
       "els10-27adminStaticPreference": els10_27adminStaticPreference,
       "els10-27adminRipPreference": els10_27adminRipPreference,
       "els10-27adminRipRouteDiscards": els10_27adminRipRouteDiscards,
       "els10-27adminRebootConfig": els10_27adminRebootConfig,
       "els10-27adminDisableButton": els10_27adminDisableButton,
       "els10-27adminButtonSelection": els10_27adminButtonSelection,
       "els10-27adminLEDProgramOption": els10_27adminLEDProgramOption,
       "els10-27swdis": els10_27swdis,
       "els10-27swdisDesc": els10_27swdisDesc,
       "els10-27swdisAccess": els10_27swdisAccess,
       "els10-27swdisWriteStatus": els10_27swdisWriteStatus,
       "els10-27swdisConfigIp": els10_27swdisConfigIp,
       "els10-27swdisConfigRetryTime": els10_27swdisConfigRetryTime,
       "els10-27swdisConfigTotalTimeout": els10_27swdisConfigTotalTimeout,
       "els10-27addr": els10_27addr,
       "els10-27addrStatics": els10_27addrStatics,
       "els10-27addrDynamics": els10_27addrDynamics,
       "els10-27addrDynamicMax": els10_27addrDynamicMax,
       "els10-27addrDynamicOverflows": els10_27addrDynamicOverflows,
       "els10-27addrFlags": els10_27addrFlags,
       "els10-27addrMAC": els10_27addrMAC,
       "els10-27addrPort": els10_27addrPort,
       "els10-27addrOperation": els10_27addrOperation,
       "els10-27addrIndex": els10_27addrIndex,
       "els10-27addrNext": els10_27addrNext,
       "els10-27addrBlockSize": els10_27addrBlockSize,
       "els10-27addrBlock": els10_27addrBlock,
       "els10-27if": els10_27if,
       "els10-27ifTable": els10_27ifTable,
       "els10-27ifEntry": els10_27ifEntry,
       "els10-27ifIndex": els10_27ifIndex,
       "els10-27ifThreshold": els10_27ifThreshold,
       "els10-27ifThresholdTime": els10_27ifThresholdTime,
       "els10-27ifRxQueueThresh": els10_27ifRxQueueThresh,
       "els10-27ifRxQueueThreshTime": els10_27ifRxQueueThreshTime,
       "els10-27ifTxStormCnt": els10_27ifTxStormCnt,
       "els10-27ifTxStormTime": els10_27ifTxStormTime,
       "els10-27ifFunction": els10_27ifFunction,
       "els10-27ifRxHwFCSs": els10_27ifRxHwFCSs,
       "els10-27ifRxQueues": els10_27ifRxQueues,
       "els10-27ifStatisticsTime": els10_27ifStatisticsTime,
       "els10-27ifForwardedChars": els10_27ifForwardedChars,
       "els10-27ifDescr": els10_27ifDescr,
       "els10-27ifGoodRxFrames": els10_27ifGoodRxFrames,
       "els10-27ifGoodTxFrames": els10_27ifGoodTxFrames,
       "els10-27dot3": els10_27dot3,
       "els10-27dot3Table": els10_27dot3Table,
       "els10-27dot3Entry": els10_27dot3Entry,
       "els10-27dot3Index": els10_27dot3Index,
       "els10-27dot3TPLinkOK": els10_27dot3TPLinkOK,
       "els10-27dot3LedOn": els10_27dot3LedOn,
       "els10-27dot3RxCollisions": els10_27dot3RxCollisions,
       "els10-27dot3RxRunts": els10_27dot3RxRunts,
       "els10-27dot3RxLateColls": els10_27dot3RxLateColls,
       "els10-27dot3TxJabbers": els10_27dot3TxJabbers,
       "els10-27dot3TxBabbles": els10_27dot3TxBabbles,
       "els10-27dot3TxCollisions": els10_27dot3TxCollisions,
       "els10-27dot3SpeedSelection": els10_27dot3SpeedSelection,
       "els10-27dot3DuplexSelection": els10_27dot3DuplexSelection,
       "els10-27uart": els10_27uart,
       "els10-27uartTable": els10_27uartTable,
       "els10-27uartEntry": els10_27uartEntry,
       "els10-27uartIndex": els10_27uartIndex,
       "els10-27uartBaud": els10_27uartBaud,
       "els10-27uartAlignmentErrors": els10_27uartAlignmentErrors,
       "els10-27uartOverrunErrors": els10_27uartOverrunErrors,
       "els10-27debug": els10_27debug,
       "els10-27debugStringID": els10_27debugStringID,
       "els10-27debugString": els10_27debugString,
       "els10-27debugTable": els10_27debugTable,
       "els10-27debugEntry": els10_27debugEntry,
       "els10-27debugIndex": els10_27debugIndex,
       "els10-27debugOperation": els10_27debugOperation,
       "els10-27debugBase": els10_27debugBase,
       "els10-27debugLength": els10_27debugLength,
       "els10-27debugData": els10_27debugData,
       "els10-27lpbk": els10_27lpbk,
       "els10-27lpbkTable": els10_27lpbkTable,
       "els10-27lpbkEntry": els10_27lpbkEntry,
       "els10-27lpbkIndex": els10_27lpbkIndex,
       "els10-27lpbkOperation": els10_27lpbkOperation,
       "els10-27lpbkDestAddr": els10_27lpbkDestAddr,
       "els10-27lpbkPktNum": els10_27lpbkPktNum,
       "els10-27lpbkInterval": els10_27lpbkInterval,
       "els10-27lpbkPktLength": els10_27lpbkPktLength,
       "els10-27lpbkIncrements": els10_27lpbkIncrements,
       "els10-27lpbkGoods": els10_27lpbkGoods,
       "els10-27lpbkErrorNoReceives": els10_27lpbkErrorNoReceives,
       "els10-27lpbkErrorBadReceives": els10_27lpbkErrorBadReceives,
       "els10-27lpbkErrorSize": els10_27lpbkErrorSize,
       "els10-27lpbkErrorSent": els10_27lpbkErrorSent,
       "els10-27lpbkErrorReceived": els10_27lpbkErrorReceived,
       "els10-27lpbkErrorOffset": els10_27lpbkErrorOffset,
       "els10-27proto": els10_27proto,
       "els10-27protoTable": els10_27protoTable,
       "els10-27protoEntry": els10_27protoEntry,
       "els10-27protoIfIndex": els10_27protoIfIndex,
       "els10-27protoBridge": els10_27protoBridge,
       "els10-27protoSuppressBpdu": els10_27protoSuppressBpdu,
       "els10-27protoRipListen": els10_27protoRipListen,
       "els10-27protoTrunking": els10_27protoTrunking,
       "els10-27sprotoTransmitPacing": els10_27sprotoTransmitPacing,
       "els10-27trunk": els10_27trunk,
       "els10-27trunkTable": els10_27trunkTable,
       "els10-27trunkEntry": els10_27trunkEntry,
       "els10-27trunkIfIndex": els10_27trunkIfIndex,
       "els10-27trunkState": els10_27trunkState,
       "els10-27trunkRemoteBridgeAddr": els10_27trunkRemoteBridgeAddr,
       "els10-27trunkRemoteIp": els10_27trunkRemoteIp,
       "els10-27trunkLastError": els10_27trunkLastError,
       "els10-27trunkLinkOrdinal": els10_27trunkLinkOrdinal,
       "els10-27trunkLinkCount": els10_27trunkLinkCount,
       "els10-27trunkLastChange": els10_27trunkLastChange,
       "els10-27workgroup": els10_27workgroup,
       "els10-27WorkGroupNextNumber": els10_27WorkGroupNextNumber,
       "els10-27WorkGroupCurrentCount": els10_27WorkGroupCurrentCount,
       "els10-27WorkGroupMaxCount": els10_27WorkGroupMaxCount,
       "els10-27WorkGroupTable": els10_27WorkGroupTable,
       "els10-27WorkGroupEntry": els10_27WorkGroupEntry,
       "els10-27WorkGroupNumber": els10_27WorkGroupNumber,
       "els10-27WorkGroupName": els10_27WorkGroupName,
       "els10-27WorkGroupPorts": els10_27WorkGroupPorts,
       "els10-27WorkGroupType": els10_27WorkGroupType,
       "els10-27trapMgt": els10_27trapMgt,
       "els10-27trapControlTable": els10_27trapControlTable,
       "els10-27trapControlEntry": els10_27trapControlEntry,
       "els10-27trapIndex": els10_27trapIndex,
       "els10-27trapEnabled": els10_27trapEnabled,
       "els10-27trapSeverity": els10_27trapSeverity,
       "els10-27trapText": els10_27trapText,
       "els10-27trapSeverityControlTable": els10_27trapSeverityControlTable,
       "els10-27trapSeverityControlEntry": els10_27trapSeverityControlEntry,
       "els10-27trapSeverityControlSeverity": els10_27trapSeverityControlSeverity,
       "els10-27trapSeverityEnable": els10_27trapSeverityEnable,
       "els10-27trapIncludeText": els10_27trapIncludeText,
       "els10-27trapTime": els10_27trapTime,
       "els10-27trapRetry": els10_27trapRetry,
       "els10-27trapNumber": els10_27trapNumber,
       "els10-27trapTable": els10_27trapTable,
       "els10-27trapEntry": els10_27trapEntry,
       "els10-27trapEntryIndex": els10_27trapEntryIndex,
       "els10-27trapEntryTimeStamp": els10_27trapEntryTimeStamp,
       "els10-27trapEntryText": els10_27trapEntryText,
       "els10-27trapEntryNumber": els10_27trapEntryNumber,
       "els10-27trapEntrySeverity": els10_27trapEntrySeverity,
       "els10-27pingMgt": els10_27pingMgt,
       "els10-27pingDataTimeout": els10_27pingDataTimeout,
       "els10-27pingTable": els10_27pingTable,
       "els10-27pingEntry": els10_27pingEntry,
       "els10-27pingNMSAddr": els10_27pingNMSAddr,
       "els10-27pingDestAddr": els10_27pingDestAddr,
       "els10-27pingState": els10_27pingState,
       "els10-27pingCount": els10_27pingCount,
       "els10-27pingDataSize": els10_27pingDataSize,
       "els10-27pingWait": els10_27pingWait,
       "els10-27pingTimeOut": els10_27pingTimeOut,
       "els10-27pingOperation": els10_27pingOperation,
       "els10-27pingMin": els10_27pingMin,
       "els10-27pingMax": els10_27pingMax,
       "els10-27pingAvg": els10_27pingAvg,
       "els10-27pingNumTransmitted": els10_27pingNumTransmitted,
       "els10-27pingNumReceived": els10_27pingNumReceived,
       "els10-27traceMgt": els10_27traceMgt,
       "els10-27traceDataTimeout": els10_27traceDataTimeout,
       "els10-27traceTable": els10_27traceTable,
       "els10-27traceEntry": els10_27traceEntry,
       "els10-27traceNMSAddr": els10_27traceNMSAddr,
       "els10-27traceDestAddr": els10_27traceDestAddr,
       "els10-27traceMaxTTL": els10_27traceMaxTTL,
       "els10-27traceDataSize": els10_27traceDataSize,
       "els10-27traceNumProbes": els10_27traceNumProbes,
       "els10-27traceWait": els10_27traceWait,
       "els10-27traceOperation": els10_27traceOperation,
       "els10-27traceHop": els10_27traceHop,
       "els10-27traceHopAddr": els10_27traceHopAddr,
       "els10-27traceProbe": els10_27traceProbe,
       "els10-27traceState": els10_27traceState,
       "els10-27traceTime": els10_27traceTime,
       "els10-27volmirrorgroup": els10_27volmirrorgroup,
       "els10-27volmirrorMode": els10_27volmirrorMode,
       "els10-27volmirrorPort": els10_27volmirrorPort,
       "els10-27volmonitorPort": els10_27volmonitorPort,
       "els10-27volMirrorMacTable": els10_27volMirrorMacTable,
       "els10-27volmirrorMacEntry": els10_27volmirrorMacEntry,
       "els10-27volmirrorIndex": els10_27volmirrorIndex,
       "els10-27volmirrorMac1": els10_27volmirrorMac1,
       "els10-27VlanBridgeConfig": els10_27VlanBridgeConfig,
       "els10-27VlanVersionNumber": els10_27VlanVersionNumber,
       "els10-27VlanOperatingMode": els10_27VlanOperatingMode,
       "els10-27VlanResetDefaults": els10_27VlanResetDefaults,
       "els10-27VlanGVRPEnable": els10_27VlanGVRPEnable,
       "els10-27VlanAccessList": els10_27VlanAccessList,
       "els10-27VlanConfigVlan": els10_27VlanConfigVlan,
       "els10-27VlanNumActiveEntries": els10_27VlanNumActiveEntries,
       "els10-27VlanNumConfiguredEntries": els10_27VlanNumConfiguredEntries,
       "els10-27VlanMaxNumEntries": els10_27VlanMaxNumEntries,
       "els10-27VlanConfigTable": els10_27VlanConfigTable,
       "els10-27VlanConfigEntry": els10_27VlanConfigEntry,
       "els10-27VlanConfigIndex": els10_27VlanConfigIndex,
       "els10-27VlanConfigVID": els10_27VlanConfigVID,
       "els10-27VlanConfigPorts": els10_27VlanConfigPorts,
       "els10-27VlanConfigIP": els10_27VlanConfigIP,
       "els10-27VlanConfigIPMask": els10_27VlanConfigIPMask,
       "els10-27VlanConfigName": els10_27VlanConfigName,
       "els10-27VlanConfigStatus": els10_27VlanConfigStatus,
       "els10-27VlanConfigEstablish": els10_27VlanConfigEstablish,
       "els10-27VlanConfigEgressTable": els10_27VlanConfigEgressTable,
       "els10-27VlanConfigEgressEntry": els10_27VlanConfigEgressEntry,
       "els10-27VlanEgressIndex": els10_27VlanEgressIndex,
       "els10-27VlanEgressVID": els10_27VlanEgressVID,
       "els10-27VlanEgressList": els10_27VlanEgressList,
       "els10-27VlanEgressStatus": els10_27VlanEgressStatus,
       "els10-27VlanFilterGVRPTable": els10_27VlanFilterGVRPTable,
       "els10-27VlanFilterGVRPEntry": els10_27VlanFilterGVRPEntry,
       "els10-27VlanFilterGVRPIndex": els10_27VlanFilterGVRPIndex,
       "els10-27VlanFilterGVRPVID": els10_27VlanFilterGVRPVID,
       "els10-27VlanFilterGVRPList": els10_27VlanFilterGVRPList,
       "els10-27VlanFilterGVRPStatus": els10_27VlanFilterGVRPStatus,
       "els10-27VlanFilterGVRPEstablishVID": els10_27VlanFilterGVRPEstablishVID,
       "els10-27VlanStaticTable": els10_27VlanStaticTable,
       "els10-27VlanStaticEntry": els10_27VlanStaticEntry,
       "els10-27VlanStaticVID": els10_27VlanStaticVID,
       "els10-27VlanStaticMAC": els10_27VlanStaticMAC,
       "els10-27VlanStaticPort": els10_27VlanStaticPort,
       "els10-27VlanStaticEstablish": els10_27VlanStaticEstablish,
       "els10-27volipmgroup": els10_27volipmgroup,
       "els10-27IPMulticastStatus": els10_27IPMulticastStatus,
       "els10-27ipmInterfaceRtr": els10_27ipmInterfaceRtr,
       "els10-27voligmpgroup": els10_27voligmpgroup,
       "els10-27igmpStatus": els10_27igmpStatus,
       "els10-27igmpQueryStatus": els10_27igmpQueryStatus,
       "els10-27igmpQueryCount": els10_27igmpQueryCount,
       "els10-27igmpPortDelay": els10_27igmpPortDelay,
       "els10-27igmpCacheTable": els10_27igmpCacheTable,
       "els10-27igmpCacheEntry": els10_27igmpCacheEntry,
       "els10-27igmpCacheAddress": els10_27igmpCacheAddress,
       "els10-27igmpCacheIfIndex": els10_27igmpCacheIfIndex,
       "els10-27igmpCacheExpiryTime": els10_27igmpCacheExpiryTime,
       "els10-27FlowControlCtl": els10_27FlowControlCtl,
       "els10-27FlowControlBackPressure": els10_27FlowControlBackPressure,
       "els10-27FlowControlThresholdValue": els10_27FlowControlThresholdValue,
       "els10-27FlowControlPauseInteval": els10_27FlowControlPauseInteval,
       "els10-27FlowControlTable": els10_27FlowControlTable,
       "els10-27FlowControlEntry": els10_27FlowControlEntry,
       "els10-27FlowControlInterface": els10_27FlowControlInterface,
       "els10-27FlowControlEnable": els10_27FlowControlEnable,
       "els10-27FlowControlRxPauseFrames": els10_27FlowControlRxPauseFrames,
       "els10-27FlowControlTxPauseFrames": els10_27FlowControlTxPauseFrames}
)
