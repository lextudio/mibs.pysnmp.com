# SNMP MIB module (CISCO-WAN-CES-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CES-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:57 2024
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

(cesmChan,
 circuitEmulation) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cesmChan",
    "circuitEmulation")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanCesConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 42)
)
ciscoWanCesConnMIB.setRevisions(
        ("2002-09-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesmChanCnfGrp_ObjectIdentity = ObjectIdentity
cesmChanCnfGrp = _CesmChanCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1)
)
_CesmChanCnfGrpTable_Object = MibTable
cesmChanCnfGrpTable = _CesmChanCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cesmChanCnfGrpTable.setStatus("current")
_CesmChanCnfGrpEntry_Object = MibTableRow
cesmChanCnfGrpEntry = _CesmChanCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1)
)
cesmChanCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-CES-CONN-MIB", "cesCnfChanNum"),
)
if mibBuilder.loadTexts:
    cesmChanCnfGrpEntry.setStatus("current")


class _CesCnfChanNum_Type(Integer32):
    """Custom type cesCnfChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2064),
    )


_CesCnfChanNum_Type.__name__ = "Integer32"
_CesCnfChanNum_Object = MibTableColumn
cesCnfChanNum = _CesCnfChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 1),
    _CesCnfChanNum_Type()
)
cesCnfChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCnfChanNum.setStatus("current")


class _CesChanRowStatus_Type(Integer32):
    """Custom type cesChanRowStatus based on Integer32"""
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
        *(("add", 1),
          ("del", 2),
          ("mod", 3),
          ("outOfService", 4))
    )


_CesChanRowStatus_Type.__name__ = "Integer32"
_CesChanRowStatus_Object = MibTableColumn
cesChanRowStatus = _CesChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 2),
    _CesChanRowStatus_Type()
)
cesChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanRowStatus.setStatus("current")


class _CesMapPortNum_Type(Integer32):
    """Custom type cesMapPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CesMapPortNum_Type.__name__ = "Integer32"
_CesMapPortNum_Object = MibTableColumn
cesMapPortNum = _CesMapPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 3),
    _CesMapPortNum_Type()
)
cesMapPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesMapPortNum.setStatus("current")


class _CesMapVpi_Type(Integer32):
    """Custom type cesMapVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 14),
    )


_CesMapVpi_Type.__name__ = "Integer32"
_CesMapVpi_Object = MibTableColumn
cesMapVpi = _CesMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 4),
    _CesMapVpi_Type()
)
cesMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesMapVpi.setStatus("current")


class _CesMapVci_Type(Integer32):
    """Custom type cesMapVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2064),
    )


_CesMapVci_Type.__name__ = "Integer32"
_CesMapVci_Object = MibTableColumn
cesMapVci = _CesMapVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 5),
    _CesMapVci_Type()
)
cesMapVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesMapVci.setStatus("current")


class _CesCBRService_Type(Integer32):
    """Custom type cesCBRService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )


_CesCBRService_Type.__name__ = "Integer32"
_CesCBRService_Object = MibTableColumn
cesCBRService = _CesCBRService_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 6),
    _CesCBRService_Type()
)
cesCBRService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCBRService.setStatus("current")


class _CesCBRClockMode_Type(Integer32):
    """Custom type cesCBRClockMode based on Integer32"""
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
        *(("adaptive", 3),
          ("srts", 2),
          ("synchronous", 1))
    )


_CesCBRClockMode_Type.__name__ = "Integer32"
_CesCBRClockMode_Object = MibTableColumn
cesCBRClockMode = _CesCBRClockMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 7),
    _CesCBRClockMode_Type()
)
cesCBRClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCBRClockMode.setStatus("current")


class _CesCas_Type(Integer32):
    """Custom type cesCas based on Integer32"""
    defaultValue = 1

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("basicNoPointer", 7),
          ("ccs", 5),
          ("conditionedE1Cas", 6),
          ("ds1EsfCas", 4),
          ("ds1EsfCasMF", 9),
          ("ds1SfCas", 3),
          ("ds1SfCasMF", 8),
          ("e1Cas", 2))
    )


_CesCas_Type.__name__ = "Integer32"
_CesCas_Object = MibTableColumn
cesCas = _CesCas_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 8),
    _CesCas_Type()
)
cesCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCas.setStatus("current")


class _CesPartialFill_Type(Integer32):
    """Custom type cesPartialFill based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_CesPartialFill_Type.__name__ = "Integer32"
_CesPartialFill_Object = MibTableColumn
cesPartialFill = _CesPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 9),
    _CesPartialFill_Type()
)
cesPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPartialFill.setStatus("current")


class _CesBufMaxSize_Type(Integer32):
    """Custom type cesBufMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesBufMaxSize_Type.__name__ = "Integer32"
_CesBufMaxSize_Object = MibTableColumn
cesBufMaxSize = _CesBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 10),
    _CesBufMaxSize_Type()
)
cesBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesBufMaxSize.setStatus("current")


class _CesCDVRxT_Type(Integer32):
    """Custom type cesCDVRxT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 65535),
    )


_CesCDVRxT_Type.__name__ = "Integer32"
_CesCDVRxT_Object = MibTableColumn
cesCDVRxT = _CesCDVRxT_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 11),
    _CesCDVRxT_Type()
)
cesCDVRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCDVRxT.setStatus("current")


class _CesCellLossIntegrationPeriod_Type(Integer32):
    """Custom type cesCellLossIntegrationPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_CesCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_CesCellLossIntegrationPeriod_Object = MibTableColumn
cesCellLossIntegrationPeriod = _CesCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 12),
    _CesCellLossIntegrationPeriod_Type()
)
cesCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCellLossIntegrationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cesCellLossIntegrationPeriod.setUnits("milliseconds")


class _CesChanLocRmtLpbkState_Type(Integer32):
    """Custom type cesChanLocRmtLpbkState based on Integer32"""
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


_CesChanLocRmtLpbkState_Type.__name__ = "Integer32"
_CesChanLocRmtLpbkState_Object = MibTableColumn
cesChanLocRmtLpbkState = _CesChanLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 13),
    _CesChanLocRmtLpbkState_Type()
)
cesChanLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanLocRmtLpbkState.setStatus("current")


class _CesChanTestType_Type(Integer32):
    """Custom type cesChanTestType based on Integer32"""
    defaultValue = 3

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
        *(("notest", 3),
          ("testcon", 1),
          ("testconsti", 4),
          ("testdelay", 2),
          ("testdelaysti", 5))
    )


_CesChanTestType_Type.__name__ = "Integer32"
_CesChanTestType_Object = MibTableColumn
cesChanTestType = _CesChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 14),
    _CesChanTestType_Type()
)
cesChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanTestType.setStatus("current")


class _CesChanTestState_Type(Integer32):
    """Custom type cesChanTestState based on Integer32"""
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
        *(("failed", 2),
          ("inprogress", 3),
          ("notinprogress", 4),
          ("passed", 1))
    )


_CesChanTestState_Type.__name__ = "Integer32"
_CesChanTestState_Object = MibTableColumn
cesChanTestState = _CesChanTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 15),
    _CesChanTestState_Type()
)
cesChanTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanTestState.setStatus("current")


class _CesChanRTDResult_Type(Integer32):
    """Custom type cesChanRTDResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CesChanRTDResult_Type.__name__ = "Integer32"
_CesChanRTDResult_Object = MibTableColumn
cesChanRTDResult = _CesChanRTDResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 16),
    _CesChanRTDResult_Type()
)
cesChanRTDResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanRTDResult.setStatus("current")
if mibBuilder.loadTexts:
    cesChanRTDResult.setUnits("milliseconds")


class _CesChanPortNum_Type(Integer32):
    """Custom type cesChanPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesChanPortNum_Type.__name__ = "Integer32"
_CesChanPortNum_Object = MibTableColumn
cesChanPortNum = _CesChanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 17),
    _CesChanPortNum_Type()
)
cesChanPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanPortNum.setStatus("current")


class _CesChanConnType_Type(Integer32):
    """Custom type cesChanConnType based on Integer32"""
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
        *(("pvc", 1),
          ("spvc", 3),
          ("svc", 2))
    )


_CesChanConnType_Type.__name__ = "Integer32"
_CesChanConnType_Object = MibTableColumn
cesChanConnType = _CesChanConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 18),
    _CesChanConnType_Type()
)
cesChanConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanConnType.setStatus("current")


class _CesChanStrauSciNum_Type(Integer32):
    """Custom type cesChanStrauSciNum based on Integer32"""
    defaultValue = 1

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
        *(("nonStrauChannel", 1),
          ("sci1", 2),
          ("sci2", 3),
          ("sci3", 4),
          ("sci4", 5))
    )


_CesChanStrauSciNum_Type.__name__ = "Integer32"
_CesChanStrauSciNum_Object = MibTableColumn
cesChanStrauSciNum = _CesChanStrauSciNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 19),
    _CesChanStrauSciNum_Type()
)
cesChanStrauSciNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanStrauSciNum.setStatus("current")


class _CesChanIdleDetEnable_Type(Integer32):
    """Custom type cesChanIdleDetEnable based on Integer32"""
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
        *(("disable", 1),
          ("enableIdlePatternDet", 3),
          ("enableOnhookDet", 2))
    )


_CesChanIdleDetEnable_Type.__name__ = "Integer32"
_CesChanIdleDetEnable_Object = MibTableColumn
cesChanIdleDetEnable = _CesChanIdleDetEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 20),
    _CesChanIdleDetEnable_Type()
)
cesChanIdleDetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanIdleDetEnable.setStatus("current")


class _CesChanIdleSignalCode_Type(Integer32):
    """Custom type cesChanIdleSignalCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesChanIdleSignalCode_Type.__name__ = "Integer32"
_CesChanIdleSignalCode_Object = MibTableColumn
cesChanIdleSignalCode = _CesChanIdleSignalCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 21),
    _CesChanIdleSignalCode_Type()
)
cesChanIdleSignalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanIdleSignalCode.setStatus("current")


class _CesChanIdleCodeIntgnPeriod_Type(Integer32):
    """Custom type cesChanIdleCodeIntgnPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CesChanIdleCodeIntgnPeriod_Type.__name__ = "Integer32"
_CesChanIdleCodeIntgnPeriod_Object = MibTableColumn
cesChanIdleCodeIntgnPeriod = _CesChanIdleCodeIntgnPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 22),
    _CesChanIdleCodeIntgnPeriod_Type()
)
cesChanIdleCodeIntgnPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanIdleCodeIntgnPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cesChanIdleCodeIntgnPeriod.setUnits("seconds")


class _CesChanOnhookCode_Type(Integer32):
    """Custom type cesChanOnhookCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CesChanOnhookCode_Type.__name__ = "Integer32"
_CesChanOnhookCode_Object = MibTableColumn
cesChanOnhookCode = _CesChanOnhookCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 23),
    _CesChanOnhookCode_Type()
)
cesChanOnhookCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanOnhookCode.setStatus("current")


class _CesChanConditionedData_Type(Integer32):
    """Custom type cesChanConditionedData based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesChanConditionedData_Type.__name__ = "Integer32"
_CesChanConditionedData_Object = MibTableColumn
cesChanConditionedData = _CesChanConditionedData_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 24),
    _CesChanConditionedData_Type()
)
cesChanConditionedData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesChanConditionedData.setStatus("current")


class _CesmChanExtTrgIdleSupp_Type(Integer32):
    """Custom type cesmChanExtTrgIdleSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablesuppression", 1),
          ("enableSuppresion", 2))
    )


_CesmChanExtTrgIdleSupp_Type.__name__ = "Integer32"
_CesmChanExtTrgIdleSupp_Object = MibTableColumn
cesmChanExtTrgIdleSupp = _CesmChanExtTrgIdleSupp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 25),
    _CesmChanExtTrgIdleSupp_Type()
)
cesmChanExtTrgIdleSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmChanExtTrgIdleSupp.setStatus("current")


class _CesmChanConditionedSigCode_Type(Integer32):
    """Custom type cesmChanConditionedSigCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesmChanConditionedSigCode_Type.__name__ = "Integer32"
_CesmChanConditionedSigCode_Object = MibTableColumn
cesmChanConditionedSigCode = _CesmChanConditionedSigCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 26),
    _CesmChanConditionedSigCode_Type()
)
cesmChanConditionedSigCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmChanConditionedSigCode.setStatus("current")


class _CesLocalVpi_Type(Integer32):
    """Custom type cesLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesLocalVpi_Type.__name__ = "Integer32"
_CesLocalVpi_Object = MibTableColumn
cesLocalVpi = _CesLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 27),
    _CesLocalVpi_Type()
)
cesLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesLocalVpi.setStatus("current")


class _CesLocalVci_Type(Integer32):
    """Custom type cesLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesLocalVci_Type.__name__ = "Integer32"
_CesLocalVci_Object = MibTableColumn
cesLocalVci = _CesLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 28),
    _CesLocalVci_Type()
)
cesLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesLocalVci.setStatus("current")


class _CesLocalNSAP_Type(OctetString):
    """Custom type cesLocalNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CesLocalNSAP_Type.__name__ = "OctetString"
_CesLocalNSAP_Object = MibTableColumn
cesLocalNSAP = _CesLocalNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 29),
    _CesLocalNSAP_Type()
)
cesLocalNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesLocalNSAP.setStatus("current")


class _CesRemoteVpi_Type(Integer32):
    """Custom type cesRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesRemoteVpi_Type.__name__ = "Integer32"
_CesRemoteVpi_Object = MibTableColumn
cesRemoteVpi = _CesRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 30),
    _CesRemoteVpi_Type()
)
cesRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRemoteVpi.setStatus("current")


class _CesRemoteVci_Type(Integer32):
    """Custom type cesRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesRemoteVci_Type.__name__ = "Integer32"
_CesRemoteVci_Object = MibTableColumn
cesRemoteVci = _CesRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 31),
    _CesRemoteVci_Type()
)
cesRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRemoteVci.setStatus("current")


class _CesRemoteNSAP_Type(OctetString):
    """Custom type cesRemoteNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CesRemoteNSAP_Type.__name__ = "OctetString"
_CesRemoteNSAP_Object = MibTableColumn
cesRemoteNSAP = _CesRemoteNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 32),
    _CesRemoteNSAP_Type()
)
cesRemoteNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRemoteNSAP.setStatus("current")


class _CesMastership_Type(Integer32):
    """Custom type cesMastership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unkown", 3))
    )


_CesMastership_Type.__name__ = "Integer32"
_CesMastership_Object = MibTableColumn
cesMastership = _CesMastership_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 33),
    _CesMastership_Type()
)
cesMastership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesMastership.setStatus("current")


class _CesVpcFlag_Type(Integer32):
    """Custom type cesVpcFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_CesVpcFlag_Type.__name__ = "Integer32"
_CesVpcFlag_Object = MibTableColumn
cesVpcFlag = _CesVpcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 34),
    _CesVpcFlag_Type()
)
cesVpcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesVpcFlag.setStatus("current")


class _CesConnServiceType_Type(Integer32):
    """Custom type cesConnServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("abrfst", 7),
          ("abrstd", 6),
          ("atfr", 5),
          ("cbr", 1),
          ("cbr1", 21),
          ("cbr2", 31),
          ("cbr3", 32),
          ("stdabr", 30),
          ("ubr", 4),
          ("ubr1", 28),
          ("ubr2", 29),
          ("vbr", 2),
          ("vbr1nrt", 25),
          ("vbr1rt", 22),
          ("vbr2nrt", 26),
          ("vbr2rt", 23),
          ("vbr3nrt", 27),
          ("vbr3rt", 24))
    )


_CesConnServiceType_Type.__name__ = "Integer32"
_CesConnServiceType_Object = MibTableColumn
cesConnServiceType = _CesConnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 35),
    _CesConnServiceType_Type()
)
cesConnServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConnServiceType.setStatus("current")


class _CesRoutingPriority_Type(Integer32):
    """Custom type cesRoutingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CesRoutingPriority_Type.__name__ = "Integer32"
_CesRoutingPriority_Object = MibTableColumn
cesRoutingPriority = _CesRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 36),
    _CesRoutingPriority_Type()
)
cesRoutingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRoutingPriority.setStatus("current")


class _CesMaxCost_Type(Integer32):
    """Custom type cesMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CesMaxCost_Type.__name__ = "Integer32"
_CesMaxCost_Object = MibTableColumn
cesMaxCost = _CesMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 37),
    _CesMaxCost_Type()
)
cesMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesMaxCost.setStatus("current")


class _CesRestrictTrunkType_Type(Integer32):
    """Custom type cesRestrictTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noresriction", 1),
          ("sateliteTrunk", 3),
          ("terrestrialTrunk", 2))
    )


_CesRestrictTrunkType_Type.__name__ = "Integer32"
_CesRestrictTrunkType_Object = MibTableColumn
cesRestrictTrunkType = _CesRestrictTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 38),
    _CesRestrictTrunkType_Type()
)
cesRestrictTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRestrictTrunkType.setStatus("current")
_CesConnPCR_Type = Integer32
_CesConnPCR_Object = MibTableColumn
cesConnPCR = _CesConnPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 39),
    _CesConnPCR_Type()
)
cesConnPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConnPCR.setStatus("current")
_CesConnMCR_Type = Integer32
_CesConnMCR_Object = MibTableColumn
cesConnMCR = _CesConnMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 40),
    _CesConnMCR_Type()
)
cesConnMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConnMCR.setStatus("current")


class _CesConnPercentUtil_Type(Integer32):
    """Custom type cesConnPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CesConnPercentUtil_Type.__name__ = "Integer32"
_CesConnPercentUtil_Object = MibTableColumn
cesConnPercentUtil = _CesConnPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 41),
    _CesConnPercentUtil_Type()
)
cesConnPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConnPercentUtil.setStatus("current")
_CesmConnRemotePCR_Type = Integer32
_CesmConnRemotePCR_Object = MibTableColumn
cesmConnRemotePCR = _CesmConnRemotePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 42),
    _CesmConnRemotePCR_Type()
)
cesmConnRemotePCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnRemotePCR.setStatus("current")
_CesmConnRemoteMCR_Type = Integer32
_CesmConnRemoteMCR_Object = MibTableColumn
cesmConnRemoteMCR = _CesmConnRemoteMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 43),
    _CesmConnRemoteMCR_Type()
)
cesmConnRemoteMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnRemoteMCR.setStatus("current")


class _CesmConnRemotePercentUtil_Type(Integer32):
    """Custom type cesmConnRemotePercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CesmConnRemotePercentUtil_Type.__name__ = "Integer32"
_CesmConnRemotePercentUtil_Object = MibTableColumn
cesmConnRemotePercentUtil = _CesmConnRemotePercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 44),
    _CesmConnRemotePercentUtil_Type()
)
cesmConnRemotePercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnRemotePercentUtil.setStatus("current")


class _CesmConnForeSightEnable_Type(Integer32):
    """Custom type cesmConnForeSightEnable based on Integer32"""
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


_CesmConnForeSightEnable_Type.__name__ = "Integer32"
_CesmConnForeSightEnable_Object = MibTableColumn
cesmConnForeSightEnable = _CesmConnForeSightEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 45),
    _CesmConnForeSightEnable_Type()
)
cesmConnForeSightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnForeSightEnable.setStatus("current")


class _CesmConnFGCRAEnable_Type(Integer32):
    """Custom type cesmConnFGCRAEnable based on Integer32"""
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


_CesmConnFGCRAEnable_Type.__name__ = "Integer32"
_CesmConnFGCRAEnable_Object = MibTableColumn
cesmConnFGCRAEnable = _CesmConnFGCRAEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 46),
    _CesmConnFGCRAEnable_Type()
)
cesmConnFGCRAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnFGCRAEnable.setStatus("current")


class _CesmChanReroute_Type(Integer32):
    """Custom type cesmChanReroute based on Integer32"""
    defaultValue = 2

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


_CesmChanReroute_Type.__name__ = "Integer32"
_CesmChanReroute_Object = MibTableColumn
cesmChanReroute = _CesmChanReroute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 47),
    _CesmChanReroute_Type()
)
cesmChanReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmChanReroute.setStatus("current")


class _CesmConnAdminStatus_Type(Integer32):
    """Custom type cesmConnAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CesmConnAdminStatus_Type.__name__ = "Integer32"
_CesmConnAdminStatus_Object = MibTableColumn
cesmConnAdminStatus = _CesmConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 48),
    _CesmConnAdminStatus_Type()
)
cesmConnAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmConnAdminStatus.setStatus("current")


class _CesmChanPrefRouteId_Type(Integer32):
    """Custom type cesmChanPrefRouteId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesmChanPrefRouteId_Type.__name__ = "Integer32"
_CesmChanPrefRouteId_Object = MibTableColumn
cesmChanPrefRouteId = _CesmChanPrefRouteId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 49),
    _CesmChanPrefRouteId_Type()
)
cesmChanPrefRouteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmChanPrefRouteId.setStatus("current")


class _CesmChanDirectRoute_Type(TruthValue):
    """Custom type cesmChanDirectRoute based on TruthValue"""


_CesmChanDirectRoute_Object = MibTableColumn
cesmChanDirectRoute = _CesmChanDirectRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 1, 1, 50),
    _CesmChanDirectRoute_Type()
)
cesmChanDirectRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmChanDirectRoute.setStatus("current")


class _CesmChanNumNextAvailable_Type(Integer32):
    """Custom type cesmChanNumNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CesmChanNumNextAvailable_Type.__name__ = "Integer32"
_CesmChanNumNextAvailable_Object = MibScalar
cesmChanNumNextAvailable = _CesmChanNumNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 1, 2),
    _CesmChanNumNextAvailable_Type()
)
cesmChanNumNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesmChanNumNextAvailable.setStatus("current")
_CesmEndPtMapGrp_ObjectIdentity = ObjectIdentity
cesmEndPtMapGrp = _CesmEndPtMapGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3)
)
_CesmEndPtMapGrpTable_Object = MibTable
cesmEndPtMapGrpTable = _CesmEndPtMapGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cesmEndPtMapGrpTable.setStatus("current")
_CesmEndPtMapGrpEntry_Object = MibTableRow
cesmEndPtMapGrpEntry = _CesmEndPtMapGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3, 1, 1)
)
cesmEndPtMapGrpEntry.setIndexNames(
    (0, "CISCO-WAN-CES-CONN-MIB", "cesEndPortNum"),
)
if mibBuilder.loadTexts:
    cesmEndPtMapGrpEntry.setStatus("current")


class _CesEndPortNum_Type(Integer32):
    """Custom type cesEndPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesEndPortNum_Type.__name__ = "Integer32"
_CesEndPortNum_Object = MibTableColumn
cesEndPortNum = _CesEndPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3, 1, 1, 1),
    _CesEndPortNum_Type()
)
cesEndPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesEndPortNum.setStatus("current")


class _CesEndChanNum_Type(Integer32):
    """Custom type cesEndChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2080),
    )


_CesEndChanNum_Type.__name__ = "Integer32"
_CesEndChanNum_Object = MibTableColumn
cesEndChanNum = _CesEndChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3, 1, 1, 2),
    _CesEndChanNum_Type()
)
cesEndChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesEndChanNum.setStatus("current")


class _CesEndLineNum_Type(Integer32):
    """Custom type cesEndLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CesEndLineNum_Type.__name__ = "Integer32"
_CesEndLineNum_Object = MibTableColumn
cesEndLineNum = _CesEndLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 3, 1, 1, 3),
    _CesEndLineNum_Type()
)
cesEndLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesEndLineNum.setStatus("current")
_CiscoWanCesConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanCesConnMIBConformance = _CiscoWanCesConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2)
)
_CiscoWanCesConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanCesConnMIBGroups = _CiscoWanCesConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 1)
)
_CiscoWanCesConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanCesConnMIBCompliances = _CiscoWanCesConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 2)
)

# Managed Objects groups

ciscoWanCesConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 1, 1)
)
ciscoWanCesConnGroup.setObjects(
      *(("CISCO-WAN-CES-CONN-MIB", "cesCnfChanNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanRowStatus"),
        ("CISCO-WAN-CES-CONN-MIB", "cesMapPortNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesMapVpi"),
        ("CISCO-WAN-CES-CONN-MIB", "cesMapVci"),
        ("CISCO-WAN-CES-CONN-MIB", "cesCBRService"),
        ("CISCO-WAN-CES-CONN-MIB", "cesCBRClockMode"),
        ("CISCO-WAN-CES-CONN-MIB", "cesCas"),
        ("CISCO-WAN-CES-CONN-MIB", "cesPartialFill"),
        ("CISCO-WAN-CES-CONN-MIB", "cesBufMaxSize"),
        ("CISCO-WAN-CES-CONN-MIB", "cesCDVRxT"),
        ("CISCO-WAN-CES-CONN-MIB", "cesCellLossIntegrationPeriod"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanLocRmtLpbkState"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanTestType"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanTestState"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanRTDResult"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanPortNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanConnType"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanStrauSciNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanIdleDetEnable"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanIdleSignalCode"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanIdleCodeIntgnPeriod"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanOnhookCode"),
        ("CISCO-WAN-CES-CONN-MIB", "cesChanConditionedData"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmChanExtTrgIdleSupp"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmChanConditionedSigCode"),
        ("CISCO-WAN-CES-CONN-MIB", "cesLocalVpi"),
        ("CISCO-WAN-CES-CONN-MIB", "cesLocalVci"),
        ("CISCO-WAN-CES-CONN-MIB", "cesLocalNSAP"),
        ("CISCO-WAN-CES-CONN-MIB", "cesRemoteVpi"),
        ("CISCO-WAN-CES-CONN-MIB", "cesRemoteVci"),
        ("CISCO-WAN-CES-CONN-MIB", "cesRemoteNSAP"),
        ("CISCO-WAN-CES-CONN-MIB", "cesMastership"),
        ("CISCO-WAN-CES-CONN-MIB", "cesVpcFlag"),
        ("CISCO-WAN-CES-CONN-MIB", "cesConnServiceType"),
        ("CISCO-WAN-CES-CONN-MIB", "cesRoutingPriority"),
        ("CISCO-WAN-CES-CONN-MIB", "cesMaxCost"),
        ("CISCO-WAN-CES-CONN-MIB", "cesRestrictTrunkType"),
        ("CISCO-WAN-CES-CONN-MIB", "cesConnPCR"),
        ("CISCO-WAN-CES-CONN-MIB", "cesConnMCR"),
        ("CISCO-WAN-CES-CONN-MIB", "cesConnPercentUtil"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnRemotePCR"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnRemoteMCR"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnRemotePercentUtil"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnForeSightEnable"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnFGCRAEnable"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmChanReroute"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmConnAdminStatus"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmChanPrefRouteId"),
        ("CISCO-WAN-CES-CONN-MIB", "cesmChanDirectRoute"))
)
if mibBuilder.loadTexts:
    ciscoWanCesConnGroup.setStatus("current")

ciscoWanCesConnEndptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 1, 2)
)
ciscoWanCesConnEndptGroup.setObjects(
      *(("CISCO-WAN-CES-CONN-MIB", "cesEndPortNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesEndChanNum"),
        ("CISCO-WAN-CES-CONN-MIB", "cesEndLineNum"))
)
if mibBuilder.loadTexts:
    ciscoWanCesConnEndptGroup.setStatus("current")

ciscoWanCesConnGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 1, 3)
)
ciscoWanCesConnGeneralGroup.setObjects(
    ("CISCO-WAN-CES-CONN-MIB", "cesmChanNumNextAvailable")
)
if mibBuilder.loadTexts:
    ciscoWanCesConnGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanCesConnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoWanCesConnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CES-CONN-MIB",
    **{"cesmChanCnfGrp": cesmChanCnfGrp,
       "cesmChanCnfGrpTable": cesmChanCnfGrpTable,
       "cesmChanCnfGrpEntry": cesmChanCnfGrpEntry,
       "cesCnfChanNum": cesCnfChanNum,
       "cesChanRowStatus": cesChanRowStatus,
       "cesMapPortNum": cesMapPortNum,
       "cesMapVpi": cesMapVpi,
       "cesMapVci": cesMapVci,
       "cesCBRService": cesCBRService,
       "cesCBRClockMode": cesCBRClockMode,
       "cesCas": cesCas,
       "cesPartialFill": cesPartialFill,
       "cesBufMaxSize": cesBufMaxSize,
       "cesCDVRxT": cesCDVRxT,
       "cesCellLossIntegrationPeriod": cesCellLossIntegrationPeriod,
       "cesChanLocRmtLpbkState": cesChanLocRmtLpbkState,
       "cesChanTestType": cesChanTestType,
       "cesChanTestState": cesChanTestState,
       "cesChanRTDResult": cesChanRTDResult,
       "cesChanPortNum": cesChanPortNum,
       "cesChanConnType": cesChanConnType,
       "cesChanStrauSciNum": cesChanStrauSciNum,
       "cesChanIdleDetEnable": cesChanIdleDetEnable,
       "cesChanIdleSignalCode": cesChanIdleSignalCode,
       "cesChanIdleCodeIntgnPeriod": cesChanIdleCodeIntgnPeriod,
       "cesChanOnhookCode": cesChanOnhookCode,
       "cesChanConditionedData": cesChanConditionedData,
       "cesmChanExtTrgIdleSupp": cesmChanExtTrgIdleSupp,
       "cesmChanConditionedSigCode": cesmChanConditionedSigCode,
       "cesLocalVpi": cesLocalVpi,
       "cesLocalVci": cesLocalVci,
       "cesLocalNSAP": cesLocalNSAP,
       "cesRemoteVpi": cesRemoteVpi,
       "cesRemoteVci": cesRemoteVci,
       "cesRemoteNSAP": cesRemoteNSAP,
       "cesMastership": cesMastership,
       "cesVpcFlag": cesVpcFlag,
       "cesConnServiceType": cesConnServiceType,
       "cesRoutingPriority": cesRoutingPriority,
       "cesMaxCost": cesMaxCost,
       "cesRestrictTrunkType": cesRestrictTrunkType,
       "cesConnPCR": cesConnPCR,
       "cesConnMCR": cesConnMCR,
       "cesConnPercentUtil": cesConnPercentUtil,
       "cesmConnRemotePCR": cesmConnRemotePCR,
       "cesmConnRemoteMCR": cesmConnRemoteMCR,
       "cesmConnRemotePercentUtil": cesmConnRemotePercentUtil,
       "cesmConnForeSightEnable": cesmConnForeSightEnable,
       "cesmConnFGCRAEnable": cesmConnFGCRAEnable,
       "cesmChanReroute": cesmChanReroute,
       "cesmConnAdminStatus": cesmConnAdminStatus,
       "cesmChanPrefRouteId": cesmChanPrefRouteId,
       "cesmChanDirectRoute": cesmChanDirectRoute,
       "cesmChanNumNextAvailable": cesmChanNumNextAvailable,
       "cesmEndPtMapGrp": cesmEndPtMapGrp,
       "cesmEndPtMapGrpTable": cesmEndPtMapGrpTable,
       "cesmEndPtMapGrpEntry": cesmEndPtMapGrpEntry,
       "cesEndPortNum": cesEndPortNum,
       "cesEndChanNum": cesEndChanNum,
       "cesEndLineNum": cesEndLineNum,
       "ciscoWanCesConnMIB": ciscoWanCesConnMIB,
       "ciscoWanCesConnMIBConformance": ciscoWanCesConnMIBConformance,
       "ciscoWanCesConnMIBGroups": ciscoWanCesConnMIBGroups,
       "ciscoWanCesConnGroup": ciscoWanCesConnGroup,
       "ciscoWanCesConnEndptGroup": ciscoWanCesConnEndptGroup,
       "ciscoWanCesConnGeneralGroup": ciscoWanCesConnGeneralGroup,
       "ciscoWanCesConnMIBCompliances": ciscoWanCesConnMIBCompliances,
       "ciscoWanCesConnCompliance": ciscoWanCesConnCompliance}
)
