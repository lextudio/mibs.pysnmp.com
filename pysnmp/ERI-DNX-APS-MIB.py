# SNMP MIB module (ERI-DNX-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:22 2024
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

(DataSwitch,
 FunctionSwitch,
 NestSlotAddress,
 OneByteField,
 dnxTrapEnterprise,
 trapSequence,
 utilities) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DataSwitch",
    "FunctionSwitch",
    "NestSlotAddress",
    "OneByteField",
    "dnxTrapEnterprise",
    "trapSequence",
    "utilities")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eriDNXApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 13)
)
eriDNXApsMIB.setRevisions(
        ("2002-05-14 00:00",
         "2002-04-29 00:00",
         "2002-04-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsSwitchRequestCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("clearRequest", 31),
          ("doNotRevert", 1),
          ("forceSwitch", 14),
          ("lockout", 15),
          ("manualSwitch", 8),
          ("noRequest", 0),
          ("reverseRequest", 2),
          ("signalDegradeHigh", 11),
          ("signalDegradeLow", 10),
          ("signalFailureHigh", 13),
          ("signalFailureLow", 12))
    )



# MIB Managed Objects in the order of their OIDs

_DnxAPS_ObjectIdentity = ObjectIdentity
dnxAPS = _DnxAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2)
)
_ApsConfigTable_Object = MibTable
apsConfigTable = _ApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    apsConfigTable.setStatus("current")
_ApsConfigEntry_Object = MibTableRow
apsConfigEntry = _ApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1)
)
apsConfigEntry.setIndexNames(
    (0, "ERI-DNX-APS-MIB", "apsCfgAddr"),
)
if mibBuilder.loadTexts:
    apsConfigEntry.setStatus("current")
_ApsCfgAddr_Type = NestSlotAddress
_ApsCfgAddr_Object = MibTableColumn
apsCfgAddr = _ApsCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 1),
    _ApsCfgAddr_Type()
)
apsCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCfgAddr.setStatus("current")
_ApsCfgResource_Type = Integer32
_ApsCfgResource_Object = MibTableColumn
apsCfgResource = _ApsCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 2),
    _ApsCfgResource_Type()
)
apsCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCfgResource.setStatus("current")


class _ApsCfgCardType_Type(Integer32):
    """Custom type apsCfgCardType based on Integer32"""
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
        *(("oc3", 1),
          ("oc3X", 3),
          ("stm1", 0),
          ("stm1X", 2))
    )


_ApsCfgCardType_Type.__name__ = "Integer32"
_ApsCfgCardType_Object = MibTableColumn
apsCfgCardType = _ApsCfgCardType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 3),
    _ApsCfgCardType_Type()
)
apsCfgCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCfgCardType.setStatus("current")


class _ApsCfgSfThreshold_Type(Integer32):
    """Custom type apsCfgSfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_ApsCfgSfThreshold_Type.__name__ = "Integer32"
_ApsCfgSfThreshold_Object = MibTableColumn
apsCfgSfThreshold = _ApsCfgSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 4),
    _ApsCfgSfThreshold_Type()
)
apsCfgSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCfgSfThreshold.setStatus("current")


class _ApsCfgSdThreshold_Type(Integer32):
    """Custom type apsCfgSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_ApsCfgSdThreshold_Type.__name__ = "Integer32"
_ApsCfgSdThreshold_Object = MibTableColumn
apsCfgSdThreshold = _ApsCfgSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 5),
    _ApsCfgSdThreshold_Type()
)
apsCfgSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCfgSdThreshold.setStatus("current")
_ApsCfgRdiSfCriteria_Type = FunctionSwitch
_ApsCfgRdiSfCriteria_Object = MibTableColumn
apsCfgRdiSfCriteria = _ApsCfgRdiSfCriteria_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 6),
    _ApsCfgRdiSfCriteria_Type()
)
apsCfgRdiSfCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCfgRdiSfCriteria.setStatus("current")


class _ApsCfgCmdStatus_Type(Integer32):
    """Custom type apsCfgCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              400,
              401,
              402,
              403,
              404,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-aps-not-applicable", 404),
          ("err-data-locked-by-another-user", 450),
          ("err-general-aps-config-error", 400),
          ("err-invalid-aps-dev-command", 403),
          ("err-invalid-asp-threshold", 401),
          ("err-invalid-rdi-criteria", 402),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-config", 1),
          ("update-successful", 101))
    )


_ApsCfgCmdStatus_Type.__name__ = "Integer32"
_ApsCfgCmdStatus_Object = MibTableColumn
apsCfgCmdStatus = _ApsCfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 7),
    _ApsCfgCmdStatus_Type()
)
apsCfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCfgCmdStatus.setStatus("current")
_ApsStatusTable_Object = MibTable
apsStatusTable = _ApsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2)
)
if mibBuilder.loadTexts:
    apsStatusTable.setStatus("current")
_ApsStatusEntry_Object = MibTableRow
apsStatusEntry = _ApsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1)
)
apsStatusEntry.setIndexNames(
    (0, "ERI-DNX-APS-MIB", "apsStatusAddr"),
)
if mibBuilder.loadTexts:
    apsStatusEntry.setStatus("current")
_ApsStatusAddr_Type = NestSlotAddress
_ApsStatusAddr_Object = MibTableColumn
apsStatusAddr = _ApsStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 1),
    _ApsStatusAddr_Type()
)
apsStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusAddr.setStatus("current")
_ApsStatusResource_Type = Integer32
_ApsStatusResource_Object = MibTableColumn
apsStatusResource = _ApsStatusResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 2),
    _ApsStatusResource_Type()
)
apsStatusResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusResource.setStatus("current")


class _ApsStatusCardType_Type(Integer32):
    """Custom type apsStatusCardType based on Integer32"""
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
        *(("oc3Protection", 4),
          ("oc3Working", 3),
          ("oc3XProtection", 8),
          ("oc3XWorking", 7),
          ("stm1Protection", 2),
          ("stm1Working", 1),
          ("stm1XProtection", 6),
          ("stm1XWorking", 5))
    )


_ApsStatusCardType_Type.__name__ = "Integer32"
_ApsStatusCardType_Object = MibTableColumn
apsStatusCardType = _ApsStatusCardType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 3),
    _ApsStatusCardType_Type()
)
apsStatusCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCardType.setStatus("current")


class _ApsStatusCardState_Type(Integer32):
    """Custom type apsStatusCardState based on Integer32"""
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
        *(("busError", 5),
          ("defective", 4),
          ("offline", 3),
          ("online", 2),
          ("standby", 1))
    )


_ApsStatusCardState_Type.__name__ = "Integer32"
_ApsStatusCardState_Object = MibTableColumn
apsStatusCardState = _ApsStatusCardState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 4),
    _ApsStatusCardState_Type()
)
apsStatusCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCardState.setStatus("current")


class _ApsRedundancyState_Type(Integer32):
    """Custom type apsRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 0),
          ("failed", 2),
          ("notDetected", 1))
    )


_ApsRedundancyState_Type.__name__ = "Integer32"
_ApsRedundancyState_Object = MibTableColumn
apsRedundancyState = _ApsRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 5),
    _ApsRedundancyState_Type()
)
apsRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsRedundancyState.setStatus("current")
_ApsSignalFailure_Type = DataSwitch
_ApsSignalFailure_Object = MibTableColumn
apsSignalFailure = _ApsSignalFailure_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 6),
    _ApsSignalFailure_Type()
)
apsSignalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSignalFailure.setStatus("current")
_ApsSignalDegrade_Type = DataSwitch
_ApsSignalDegrade_Object = MibTableColumn
apsSignalDegrade = _ApsSignalDegrade_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 7),
    _ApsSignalDegrade_Type()
)
apsSignalDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSignalDegrade.setStatus("current")
_ApsLineRxK1Byte_Type = OneByteField
_ApsLineRxK1Byte_Object = MibTableColumn
apsLineRxK1Byte = _ApsLineRxK1Byte_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 8),
    _ApsLineRxK1Byte_Type()
)
apsLineRxK1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLineRxK1Byte.setStatus("current")
_ApsLineRxK2Byte_Type = OneByteField
_ApsLineRxK2Byte_Object = MibTableColumn
apsLineRxK2Byte = _ApsLineRxK2Byte_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 9),
    _ApsLineRxK2Byte_Type()
)
apsLineRxK2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLineRxK2Byte.setStatus("current")
_ApsSysRxReqCode_Type = ApsSwitchRequestCode
_ApsSysRxReqCode_Object = MibTableColumn
apsSysRxReqCode = _ApsSysRxReqCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 10),
    _ApsSysRxReqCode_Type()
)
apsSysRxReqCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSysRxReqCode.setStatus("current")
_ApsSysTxReqCode_Type = ApsSwitchRequestCode
_ApsSysTxReqCode_Object = MibTableColumn
apsSysTxReqCode = _ApsSysTxReqCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 11),
    _ApsSysTxReqCode_Type()
)
apsSysTxReqCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSysTxReqCode.setStatus("current")
_ApsUserPendingReq_Type = ApsSwitchRequestCode
_ApsUserPendingReq_Object = MibTableColumn
apsUserPendingReq = _ApsUserPendingReq_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 12),
    _ApsUserPendingReq_Type()
)
apsUserPendingReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsUserPendingReq.setStatus("current")


class _ApsSwitchCmdStatus_Type(Integer32):
    """Custom type apsSwitchCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              14,
              31,
              108,
              114,
              131,
              400,
              402,
              406,
              408,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 131),
          ("clearRequest", 31),
          ("err-field-cannot-be-set", 406),
          ("err-gen-aps-req-error", 400),
          ("err-invalid-aps-card-type", 402),
          ("err-invalid-aps-command", 408),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("force-successful", 114),
          ("forceSwitchReq", 14),
          ("manual-successful", 108),
          ("manualSwitchReq", 8),
          ("readyForRequest", 0))
    )


_ApsSwitchCmdStatus_Type.__name__ = "Integer32"
_ApsSwitchCmdStatus_Object = MibTableColumn
apsSwitchCmdStatus = _ApsSwitchCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 13),
    _ApsSwitchCmdStatus_Type()
)
apsSwitchCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsSwitchCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

apsConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 11)
)
apsConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-APS-MIB", "apsCfgAddr"),
        ("ERI-DNX-APS-MIB", "apsCfgCmdStatus"))
)
if mibBuilder.loadTexts:
    apsConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-APS-MIB",
    **{"ApsSwitchRequestCode": ApsSwitchRequestCode,
       "apsConfigTrap": apsConfigTrap,
       "dnxAPS": dnxAPS,
       "apsConfigTable": apsConfigTable,
       "apsConfigEntry": apsConfigEntry,
       "apsCfgAddr": apsCfgAddr,
       "apsCfgResource": apsCfgResource,
       "apsCfgCardType": apsCfgCardType,
       "apsCfgSfThreshold": apsCfgSfThreshold,
       "apsCfgSdThreshold": apsCfgSdThreshold,
       "apsCfgRdiSfCriteria": apsCfgRdiSfCriteria,
       "apsCfgCmdStatus": apsCfgCmdStatus,
       "apsStatusTable": apsStatusTable,
       "apsStatusEntry": apsStatusEntry,
       "apsStatusAddr": apsStatusAddr,
       "apsStatusResource": apsStatusResource,
       "apsStatusCardType": apsStatusCardType,
       "apsStatusCardState": apsStatusCardState,
       "apsRedundancyState": apsRedundancyState,
       "apsSignalFailure": apsSignalFailure,
       "apsSignalDegrade": apsSignalDegrade,
       "apsLineRxK1Byte": apsLineRxK1Byte,
       "apsLineRxK2Byte": apsLineRxK2Byte,
       "apsSysRxReqCode": apsSysRxReqCode,
       "apsSysTxReqCode": apsSysTxReqCode,
       "apsUserPendingReq": apsUserPendingReq,
       "apsSwitchCmdStatus": apsSwitchCmdStatus,
       "eriDNXApsMIB": eriDNXApsMIB}
)
