# SNMP MIB module (TERAWAVE-teratest-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teratest-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:25 2024
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraTestGroup_ObjectIdentity = ObjectIdentity
teraTestGroup = _TeraTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 14)
)
_TeraTestTable_Object = MibTable
teraTestTable = _TeraTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1)
)
if mibBuilder.loadTexts:
    teraTestTable.setStatus("mandatory")
_TeraTestTableEntry_Object = MibTableRow
teraTestTableEntry = _TeraTestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1)
)
teraTestTableEntry.setIndexNames(
    (0, "TERAWAVE-teratest-MIB", "teraTestSourceSlot"),
    (0, "TERAWAVE-teratest-MIB", "teraTestIndex"),
)
if mibBuilder.loadTexts:
    teraTestTableEntry.setStatus("mandatory")


class _TeraTestSourceSlot_Type(Integer32):
    """Custom type teraTestSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraTestSourceSlot_Type.__name__ = "Integer32"
_TeraTestSourceSlot_Object = MibTableColumn
teraTestSourceSlot = _TeraTestSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 1),
    _TeraTestSourceSlot_Type()
)
teraTestSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestSourceSlot.setStatus("mandatory")


class _TeraTestIndex_Type(Counter32):
    """Custom type teraTestIndex based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TeraTestIndex_Type.__name__ = "Counter32"
_TeraTestIndex_Object = MibTableColumn
teraTestIndex = _TeraTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 2),
    _TeraTestIndex_Type()
)
teraTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestIndex.setStatus("mandatory")
_TeraTestTargetIfIndex_Type = Integer32
_TeraTestTargetIfIndex_Object = MibTableColumn
teraTestTargetIfIndex = _TeraTestTargetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 3),
    _TeraTestTargetIfIndex_Type()
)
teraTestTargetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestTargetIfIndex.setStatus("mandatory")
_TeraTestTargetVpi_Type = Integer32
_TeraTestTargetVpi_Object = MibTableColumn
teraTestTargetVpi = _TeraTestTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 4),
    _TeraTestTargetVpi_Type()
)
teraTestTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestTargetVpi.setStatus("mandatory")
_TeraTestTargetVci_Type = Integer32
_TeraTestTargetVci_Object = MibTableColumn
teraTestTargetVci = _TeraTestTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 5),
    _TeraTestTargetVci_Type()
)
teraTestTargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestTargetVci.setStatus("mandatory")


class _TeraTestTargetDirection_Type(Integer32):
    """Custom type teraTestTargetDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_TeraTestTargetDirection_Type.__name__ = "Integer32"
_TeraTestTargetDirection_Object = MibTableColumn
teraTestTargetDirection = _TeraTestTargetDirection_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 6),
    _TeraTestTargetDirection_Type()
)
teraTestTargetDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestTargetDirection.setStatus("mandatory")
_TeraTestType_Type = ObjectIdentifier
_TeraTestType_Object = MibTableColumn
teraTestType = _TeraTestType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 7),
    _TeraTestType_Type()
)
teraTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestType.setStatus("mandatory")
_TeraTestMoreInfo_Type = OctetString
_TeraTestMoreInfo_Object = MibTableColumn
teraTestMoreInfo = _TeraTestMoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 8),
    _TeraTestMoreInfo_Type()
)
teraTestMoreInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestMoreInfo.setStatus("mandatory")
_TeraTestResultTimeStamp_Type = TimeTicks
_TeraTestResultTimeStamp_Object = MibTableColumn
teraTestResultTimeStamp = _TeraTestResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 9),
    _TeraTestResultTimeStamp_Type()
)
teraTestResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestResultTimeStamp.setStatus("mandatory")


class _TeraTestResult_Type(Integer32):
    """Custom type teraTestResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_TeraTestResult_Type.__name__ = "Integer32"
_TeraTestResult_Object = MibTableColumn
teraTestResult = _TeraTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 10),
    _TeraTestResult_Type()
)
teraTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestResult.setStatus("mandatory")


class _TeraTestCode_Type(Integer32):
    """Custom type teraTestCode based on Integer32"""
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
        *(("invalidTarget", 6),
          ("manualStop", 4),
          ("none", 1),
          ("portFail", 5),
          ("timeout", 3),
          ("unkown", 2))
    )


_TeraTestCode_Type.__name__ = "Integer32"
_TeraTestCode_Object = MibTableColumn
teraTestCode = _TeraTestCode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 11),
    _TeraTestCode_Type()
)
teraTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestCode.setStatus("mandatory")


class _TeraTestRowStatus_Type(Integer32):
    """Custom type teraTestRowStatus based on Integer32"""
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
        *(("active", 2),
          ("destroy", 4),
          ("inProgress", 3),
          ("notInService", 1))
    )


_TeraTestRowStatus_Type.__name__ = "Integer32"
_TeraTestRowStatus_Object = MibTableColumn
teraTestRowStatus = _TeraTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 12),
    _TeraTestRowStatus_Type()
)
teraTestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestRowStatus.setStatus("mandatory")


class _TeraTestAction_Type(Integer32):
    """Custom type teraTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("send", 2))
    )


_TeraTestAction_Type.__name__ = "Integer32"
_TeraTestAction_Object = MibTableColumn
teraTestAction = _TeraTestAction_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 1, 1, 13),
    _TeraTestAction_Type()
)
teraTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestAction.setStatus("mandatory")
_TeraTestCapabilityTable_Object = MibTable
teraTestCapabilityTable = _TeraTestCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 2)
)
if mibBuilder.loadTexts:
    teraTestCapabilityTable.setStatus("mandatory")
_TeraTestCapabilityTableEntry_Object = MibTableRow
teraTestCapabilityTableEntry = _TeraTestCapabilityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 2, 1)
)
teraTestCapabilityTableEntry.setIndexNames(
    (0, "TERAWAVE-teratest-MIB", "teraTestSourceSlot"),
)
if mibBuilder.loadTexts:
    teraTestCapabilityTableEntry.setStatus("mandatory")
_TeraTestIndexNext_Type = Counter32
_TeraTestIndexNext_Object = MibTableColumn
teraTestIndexNext = _TeraTestIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 2, 1, 1),
    _TeraTestIndexNext_Type()
)
teraTestIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestIndexNext.setStatus("mandatory")


class _TeraTestTableMaxSize_Type(Counter32):
    """Custom type teraTestTableMaxSize based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4294967295),
    )


_TeraTestTableMaxSize_Type.__name__ = "Counter32"
_TeraTestTableMaxSize_Object = MibTableColumn
teraTestTableMaxSize = _TeraTestTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 2, 1, 2),
    _TeraTestTableMaxSize_Type()
)
teraTestTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestTableMaxSize.setStatus("mandatory")
_TeraTestCapabilityTypeBits_Type = Integer32
_TeraTestCapabilityTypeBits_Object = MibTableColumn
teraTestCapabilityTypeBits = _TeraTestCapabilityTypeBits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 14, 2, 1, 3),
    _TeraTestCapabilityTypeBits_Type()
)
teraTestCapabilityTypeBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTestCapabilityTypeBits.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teratest-MIB",
    **{"terawave": terawave,
       "teraTestGroup": teraTestGroup,
       "teraTestTable": teraTestTable,
       "teraTestTableEntry": teraTestTableEntry,
       "teraTestSourceSlot": teraTestSourceSlot,
       "teraTestIndex": teraTestIndex,
       "teraTestTargetIfIndex": teraTestTargetIfIndex,
       "teraTestTargetVpi": teraTestTargetVpi,
       "teraTestTargetVci": teraTestTargetVci,
       "teraTestTargetDirection": teraTestTargetDirection,
       "teraTestType": teraTestType,
       "teraTestMoreInfo": teraTestMoreInfo,
       "teraTestResultTimeStamp": teraTestResultTimeStamp,
       "teraTestResult": teraTestResult,
       "teraTestCode": teraTestCode,
       "teraTestRowStatus": teraTestRowStatus,
       "teraTestAction": teraTestAction,
       "teraTestCapabilityTable": teraTestCapabilityTable,
       "teraTestCapabilityTableEntry": teraTestCapabilityTableEntry,
       "teraTestIndexNext": teraTestIndexNext,
       "teraTestTableMaxSize": teraTestTableMaxSize,
       "teraTestCapabilityTypeBits": teraTestCapabilityTypeBits}
)
