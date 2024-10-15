# SNMP MIB module (MLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MLM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:33 2024
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
 enterprises,
 experimental,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

mlmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 99, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpResearch_ObjectIdentity = ObjectIdentity
snmpResearch = _SnmpResearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99)
)
_MlmMIBObjects_ObjectIdentity = ObjectIdentity
mlmMIBObjects = _MlmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99, 42, 1)
)
_MlmLock_Type = TestAndIncr
_MlmLock_Object = MibScalar
mlmLock = _MlmLock_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 1),
    _MlmLock_Type()
)
mlmLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmLock.setStatus("current")


class _MlmScriptWrite_Type(Integer32):
    """Custom type mlmScriptWrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MlmScriptWrite_Type.__name__ = "Integer32"
_MlmScriptWrite_Object = MibScalar
mlmScriptWrite = _MlmScriptWrite_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 2),
    _MlmScriptWrite_Type()
)
mlmScriptWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmScriptWrite.setStatus("current")


class _MlmExecutionSpeed_Type(Integer32):
    """Custom type mlmExecutionSpeed based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MlmExecutionSpeed_Type.__name__ = "Integer32"
_MlmExecutionSpeed_Object = MibScalar
mlmExecutionSpeed = _MlmExecutionSpeed_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 3),
    _MlmExecutionSpeed_Type()
)
mlmExecutionSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmExecutionSpeed.setStatus("current")


class _MlmTimeSlice_Type(Integer32):
    """Custom type mlmTimeSlice based on Integer32"""
    defaultValue = 10


_MlmTimeSlice_Object = MibScalar
mlmTimeSlice = _MlmTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 4),
    _MlmTimeSlice_Type()
)
mlmTimeSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmTimeSlice.setStatus("current")
_MlmCompileTable_Object = MibTable
mlmCompileTable = _MlmCompileTable_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5)
)
if mibBuilder.loadTexts:
    mlmCompileTable.setStatus("current")
_MlmCompileEntry_Object = MibTableRow
mlmCompileEntry = _MlmCompileEntry_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1)
)
mlmCompileEntry.setIndexNames(
    (0, "MLM-MIB", "mlmCompileIndex"),
)
if mibBuilder.loadTexts:
    mlmCompileEntry.setStatus("current")


class _MlmCompileIndex_Type(Integer32):
    """Custom type mlmCompileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MlmCompileIndex_Type.__name__ = "Integer32"
_MlmCompileIndex_Object = MibTableColumn
mlmCompileIndex = _MlmCompileIndex_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 1),
    _MlmCompileIndex_Type()
)
mlmCompileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmCompileIndex.setStatus("current")


class _MlmScriptNumber_Type(Integer32):
    """Custom type mlmScriptNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MlmScriptNumber_Type.__name__ = "Integer32"
_MlmScriptNumber_Object = MibTableColumn
mlmScriptNumber = _MlmScriptNumber_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 2),
    _MlmScriptNumber_Type()
)
mlmScriptNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmScriptNumber.setStatus("current")
_MlmScriptName_Type = DisplayString
_MlmScriptName_Object = MibTableColumn
mlmScriptName = _MlmScriptName_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 3),
    _MlmScriptName_Type()
)
mlmScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmScriptName.setStatus("current")
_MlmCompileResult_Type = Integer32
_MlmCompileResult_Object = MibTableColumn
mlmCompileResult = _MlmCompileResult_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 4),
    _MlmCompileResult_Type()
)
mlmCompileResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmCompileResult.setStatus("current")


class _MlmExecutionArgs_Type(OctetString):
    """Custom type mlmExecutionArgs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_MlmExecutionArgs_Type.__name__ = "OctetString"
_MlmExecutionArgs_Object = MibTableColumn
mlmExecutionArgs = _MlmExecutionArgs_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 5),
    _MlmExecutionArgs_Type()
)
mlmExecutionArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmExecutionArgs.setStatus("current")


class _MlmExecutionPeriod_Type(Integer32):
    """Custom type mlmExecutionPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MlmExecutionPeriod_Type.__name__ = "Integer32"
_MlmExecutionPeriod_Object = MibTableColumn
mlmExecutionPeriod = _MlmExecutionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 6),
    _MlmExecutionPeriod_Type()
)
mlmExecutionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmExecutionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    mlmExecutionPeriod.setUnits("100ths of seconds")
_MlmRowStatus_Type = RowStatus
_MlmRowStatus_Object = MibTableColumn
mlmRowStatus = _MlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 7),
    _MlmRowStatus_Type()
)
mlmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmRowStatus.setStatus("current")


class _MlmPermanence_Type(Integer32):
    """Custom type mlmPermanence based on Integer32"""
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
        *(("permanent", 3),
          ("startup", 2),
          ("temporary", 1))
    )


_MlmPermanence_Type.__name__ = "Integer32"
_MlmPermanence_Object = MibTableColumn
mlmPermanence = _MlmPermanence_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 5, 1, 8),
    _MlmPermanence_Type()
)
mlmPermanence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmPermanence.setStatus("current")
_MlmScriptTable_Object = MibTable
mlmScriptTable = _MlmScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6)
)
if mibBuilder.loadTexts:
    mlmScriptTable.setStatus("current")
_MlmScriptEntry_Object = MibTableRow
mlmScriptEntry = _MlmScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6, 1)
)
mlmScriptEntry.setIndexNames(
    (0, "MLM-MIB", "mlmScriptIndex"),
    (0, "MLM-MIB", "mlmScriptLineIndex"),
)
if mibBuilder.loadTexts:
    mlmScriptEntry.setStatus("current")


class _MlmScriptIndex_Type(Integer32):
    """Custom type mlmScriptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MlmScriptIndex_Type.__name__ = "Integer32"
_MlmScriptIndex_Object = MibTableColumn
mlmScriptIndex = _MlmScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6, 1, 1),
    _MlmScriptIndex_Type()
)
mlmScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmScriptIndex.setStatus("current")


class _MlmScriptLineIndex_Type(Integer32):
    """Custom type mlmScriptLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MlmScriptLineIndex_Type.__name__ = "Integer32"
_MlmScriptLineIndex_Object = MibTableColumn
mlmScriptLineIndex = _MlmScriptLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6, 1, 2),
    _MlmScriptLineIndex_Type()
)
mlmScriptLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmScriptLineIndex.setStatus("current")


class _MlmScriptCode_Type(OctetString):
    """Custom type mlmScriptCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_MlmScriptCode_Type.__name__ = "OctetString"
_MlmScriptCode_Object = MibTableColumn
mlmScriptCode = _MlmScriptCode_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6, 1, 3),
    _MlmScriptCode_Type()
)
mlmScriptCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmScriptCode.setStatus("current")


class _MlmCompileErrors_Type(OctetString):
    """Custom type mlmCompileErrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_MlmCompileErrors_Type.__name__ = "OctetString"
_MlmCompileErrors_Object = MibTableColumn
mlmCompileErrors = _MlmCompileErrors_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 6, 1, 4),
    _MlmCompileErrors_Type()
)
mlmCompileErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmCompileErrors.setStatus("current")
_MlmResultTable_Object = MibTable
mlmResultTable = _MlmResultTable_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7)
)
if mibBuilder.loadTexts:
    mlmResultTable.setStatus("current")
_MlmResultEntry_Object = MibTableRow
mlmResultEntry = _MlmResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1)
)
mlmResultEntry.setIndexNames(
    (0, "MLM-MIB", "mlmCompileIndex"),
    (0, "MLM-MIB", "mlmResultIndex"),
)
if mibBuilder.loadTexts:
    mlmResultEntry.setStatus("current")


class _MlmResultIndex_Type(Integer32):
    """Custom type mlmResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MlmResultIndex_Type.__name__ = "Integer32"
_MlmResultIndex_Object = MibTableColumn
mlmResultIndex = _MlmResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 1),
    _MlmResultIndex_Type()
)
mlmResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmResultIndex.setStatus("current")
_MlmResultOID_Type = ObjectIdentifier
_MlmResultOID_Object = MibTableColumn
mlmResultOID = _MlmResultOID_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 2),
    _MlmResultOID_Type()
)
mlmResultOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmResultOID.setStatus("current")


class _MlmResultType_Type(Integer32):
    """Custom type mlmResultType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 5),
          ("counter64", 13),
          ("error", 1),
          ("gauge32", 6),
          ("integer", 4),
          ("ipaddress", 8),
          ("nothing", 2),
          ("null", 3),
          ("objectid", 10),
          ("octetstring", 9),
          ("timeticks", 7))
    )


_MlmResultType_Type.__name__ = "Integer32"
_MlmResultType_Object = MibTableColumn
mlmResultType = _MlmResultType_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 3),
    _MlmResultType_Type()
)
mlmResultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmResultType.setStatus("current")
_MlmIntegerValue_Type = Integer32
_MlmIntegerValue_Object = MibTableColumn
mlmIntegerValue = _MlmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 4),
    _MlmIntegerValue_Type()
)
mlmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmIntegerValue.setStatus("current")
_MlmCounter32Value_Type = Counter32
_MlmCounter32Value_Object = MibTableColumn
mlmCounter32Value = _MlmCounter32Value_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 5),
    _MlmCounter32Value_Type()
)
mlmCounter32Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmCounter32Value.setStatus("current")
_MlmGauge32Value_Type = Gauge32
_MlmGauge32Value_Object = MibTableColumn
mlmGauge32Value = _MlmGauge32Value_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 6),
    _MlmGauge32Value_Type()
)
mlmGauge32Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmGauge32Value.setStatus("current")
_MlmTimeTicksValue_Type = TimeTicks
_MlmTimeTicksValue_Object = MibTableColumn
mlmTimeTicksValue = _MlmTimeTicksValue_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 7),
    _MlmTimeTicksValue_Type()
)
mlmTimeTicksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmTimeTicksValue.setStatus("current")
_MlmIpAddressValue_Type = IpAddress
_MlmIpAddressValue_Object = MibTableColumn
mlmIpAddressValue = _MlmIpAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 8),
    _MlmIpAddressValue_Type()
)
mlmIpAddressValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmIpAddressValue.setStatus("current")


class _MlmOctetStringValue_Type(OctetString):
    """Custom type mlmOctetStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_MlmOctetStringValue_Type.__name__ = "OctetString"
_MlmOctetStringValue_Object = MibTableColumn
mlmOctetStringValue = _MlmOctetStringValue_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 9),
    _MlmOctetStringValue_Type()
)
mlmOctetStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmOctetStringValue.setStatus("current")
_MlmObjectIDValue_Type = ObjectIdentifier
_MlmObjectIDValue_Object = MibTableColumn
mlmObjectIDValue = _MlmObjectIDValue_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 10),
    _MlmObjectIDValue_Type()
)
mlmObjectIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmObjectIDValue.setStatus("current")
_MlmCounter64Value_Type = Counter64
_MlmCounter64Value_Object = MibTableColumn
mlmCounter64Value = _MlmCounter64Value_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 13),
    _MlmCounter64Value_Type()
)
mlmCounter64Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmCounter64Value.setStatus("current")


class _MlmRuntimeError_Type(OctetString):
    """Custom type mlmRuntimeError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_MlmRuntimeError_Type.__name__ = "OctetString"
_MlmRuntimeError_Object = MibTableColumn
mlmRuntimeError = _MlmRuntimeError_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 7, 1, 15),
    _MlmRuntimeError_Type()
)
mlmRuntimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlmRuntimeError.setStatus("current")
_MlmNextScript_Type = TestAndIncr
_MlmNextScript_Object = MibScalar
mlmNextScript = _MlmNextScript_Object(
    (1, 3, 6, 1, 4, 1, 99, 42, 1, 8),
    _MlmNextScript_Type()
)
mlmNextScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlmNextScript.setStatus("current")
_MlmMIBConformance_ObjectIdentity = ObjectIdentity
mlmMIBConformance = _MlmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99, 42, 2)
)
_MlmMIBCompliances_ObjectIdentity = ObjectIdentity
mlmMIBCompliances = _MlmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99, 42, 2, 1)
)
_MlmMIBGroups_ObjectIdentity = ObjectIdentity
mlmMIBGroups = _MlmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99, 42, 2, 2)
)

# Managed Objects groups

mlmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 99, 42, 2, 2, 1)
)
mlmMIBGroup.setObjects(
      *(("MLM-MIB", "mlmLock"),
        ("MLM-MIB", "mlmScriptWrite"),
        ("MLM-MIB", "mlmExecutionSpeed"),
        ("MLM-MIB", "mlmTimeSlice"),
        ("MLM-MIB", "mlmNextScript"),
        ("MLM-MIB", "mlmCompileIndex"),
        ("MLM-MIB", "mlmScriptNumber"),
        ("MLM-MIB", "mlmScriptName"),
        ("MLM-MIB", "mlmCompileResult"),
        ("MLM-MIB", "mlmExecutionArgs"),
        ("MLM-MIB", "mlmExecutionPeriod"),
        ("MLM-MIB", "mlmRowStatus"),
        ("MLM-MIB", "mlmPermanence"),
        ("MLM-MIB", "mlmScriptIndex"),
        ("MLM-MIB", "mlmScriptLineIndex"),
        ("MLM-MIB", "mlmScriptCode"),
        ("MLM-MIB", "mlmCompileErrors"),
        ("MLM-MIB", "mlmResultIndex"),
        ("MLM-MIB", "mlmResultOID"),
        ("MLM-MIB", "mlmResultType"),
        ("MLM-MIB", "mlmIntegerValue"),
        ("MLM-MIB", "mlmCounter32Value"),
        ("MLM-MIB", "mlmGauge32Value"),
        ("MLM-MIB", "mlmTimeTicksValue"),
        ("MLM-MIB", "mlmIpAddressValue"),
        ("MLM-MIB", "mlmOctetStringValue"),
        ("MLM-MIB", "mlmObjectIDValue"),
        ("MLM-MIB", "mlmCounter64Value"),
        ("MLM-MIB", "mlmRuntimeError"))
)
if mibBuilder.loadTexts:
    mlmMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mlmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 99, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mlmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MLM-MIB",
    **{"snmpResearch": snmpResearch,
       "mlmMIB": mlmMIB,
       "mlmMIBObjects": mlmMIBObjects,
       "mlmLock": mlmLock,
       "mlmScriptWrite": mlmScriptWrite,
       "mlmExecutionSpeed": mlmExecutionSpeed,
       "mlmTimeSlice": mlmTimeSlice,
       "mlmCompileTable": mlmCompileTable,
       "mlmCompileEntry": mlmCompileEntry,
       "mlmCompileIndex": mlmCompileIndex,
       "mlmScriptNumber": mlmScriptNumber,
       "mlmScriptName": mlmScriptName,
       "mlmCompileResult": mlmCompileResult,
       "mlmExecutionArgs": mlmExecutionArgs,
       "mlmExecutionPeriod": mlmExecutionPeriod,
       "mlmRowStatus": mlmRowStatus,
       "mlmPermanence": mlmPermanence,
       "mlmScriptTable": mlmScriptTable,
       "mlmScriptEntry": mlmScriptEntry,
       "mlmScriptIndex": mlmScriptIndex,
       "mlmScriptLineIndex": mlmScriptLineIndex,
       "mlmScriptCode": mlmScriptCode,
       "mlmCompileErrors": mlmCompileErrors,
       "mlmResultTable": mlmResultTable,
       "mlmResultEntry": mlmResultEntry,
       "mlmResultIndex": mlmResultIndex,
       "mlmResultOID": mlmResultOID,
       "mlmResultType": mlmResultType,
       "mlmIntegerValue": mlmIntegerValue,
       "mlmCounter32Value": mlmCounter32Value,
       "mlmGauge32Value": mlmGauge32Value,
       "mlmTimeTicksValue": mlmTimeTicksValue,
       "mlmIpAddressValue": mlmIpAddressValue,
       "mlmOctetStringValue": mlmOctetStringValue,
       "mlmObjectIDValue": mlmObjectIDValue,
       "mlmCounter64Value": mlmCounter64Value,
       "mlmRuntimeError": mlmRuntimeError,
       "mlmNextScript": mlmNextScript,
       "mlmMIBConformance": mlmMIBConformance,
       "mlmMIBCompliances": mlmMIBCompliances,
       "mlmCompliance": mlmCompliance,
       "mlmMIBGroups": mlmMIBGroups,
       "mlmMIBGroup": mlmMIBGroup}
)
