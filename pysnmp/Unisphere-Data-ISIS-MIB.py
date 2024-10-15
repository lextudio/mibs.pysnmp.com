# SNMP MIB module (Unisphere-Data-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:58 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdIsisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38)
)
usdIsisMIB.setRevisions(
        ("2001-12-10 21:29",
         "2001-12-07 15:22",
         "2001-04-17 21:26",
         "2000-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OSINSAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class SystemID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class OperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class AuthTime(Integer32, TextualConvention):
    status = "current"


class LSPBuffSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9180),
    )



class LevelState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("waiting", 3))
    )



class SupportedProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              204,
              205)
        )
    )
    namedValues = NamedValues(
        *(("ip", 204),
          ("ipV6", 205),
          ("iso8473", 129))
    )



class UsdDefaultMetric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )



class OtherMetric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class CircuitID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )



class ISPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



# MIB Managed Objects in the order of their OIDs

_UsdIsisObjects_ObjectIdentity = ObjectIdentity
usdIsisObjects = _UsdIsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1)
)
_UsdIsisSystemGroup_ObjectIdentity = ObjectIdentity
usdIsisSystemGroup = _UsdIsisSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1)
)
_UsdIsisSysTable_Object = MibTable
usdIsisSysTable = _UsdIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdIsisSysTable.setStatus("current")
_UsdIsisSysEntry_Object = MibTableRow
usdIsisSysEntry = _UsdIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1)
)
usdIsisSysEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysInstance"),
)
if mibBuilder.loadTexts:
    usdIsisSysEntry.setStatus("current")


class _UsdIsisSysInstance_Type(Integer32):
    """Custom type usdIsisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysInstance_Object = MibTableColumn
usdIsisSysInstance = _UsdIsisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 1),
    _UsdIsisSysInstance_Type()
)
usdIsisSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysInstance.setStatus("current")


class _UsdIsisSysVersion_Type(DisplayString):
    """Custom type usdIsisSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_UsdIsisSysVersion_Type.__name__ = "DisplayString"
_UsdIsisSysVersion_Object = MibTableColumn
usdIsisSysVersion = _UsdIsisSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 2),
    _UsdIsisSysVersion_Type()
)
usdIsisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysVersion.setStatus("current")


class _UsdIsisSysType_Type(Integer32):
    """Custom type usdIsisSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level1l2IS", 2),
          ("level2Only", 3))
    )


_UsdIsisSysType_Type.__name__ = "Integer32"
_UsdIsisSysType_Object = MibTableColumn
usdIsisSysType = _UsdIsisSysType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 3),
    _UsdIsisSysType_Type()
)
usdIsisSysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysType.setStatus("current")
_UsdIsisSysID_Type = SystemID
_UsdIsisSysID_Object = MibTableColumn
usdIsisSysID = _UsdIsisSysID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 4),
    _UsdIsisSysID_Type()
)
usdIsisSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysID.setStatus("current")


class _UsdIsisSysMaxPathSplits_Type(Integer32):
    """Custom type usdIsisSysMaxPathSplits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_UsdIsisSysMaxPathSplits_Type.__name__ = "Integer32"
_UsdIsisSysMaxPathSplits_Object = MibTableColumn
usdIsisSysMaxPathSplits = _UsdIsisSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 5),
    _UsdIsisSysMaxPathSplits_Type()
)
usdIsisSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMaxPathSplits.setStatus("current")


class _UsdIsisSysMaxLSPGenInt_Type(Integer32):
    """Custom type usdIsisSysMaxLSPGenInt based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysMaxLSPGenInt_Type.__name__ = "Integer32"
_UsdIsisSysMaxLSPGenInt_Object = MibTableColumn
usdIsisSysMaxLSPGenInt = _UsdIsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 6),
    _UsdIsisSysMaxLSPGenInt_Type()
)
usdIsisSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysMaxLSPGenInt.setUnits("seconds")


class _UsdIsisSysOrigL1LSPBuffSize_Type(LSPBuffSize):
    """Custom type usdIsisSysOrigL1LSPBuffSize based on LSPBuffSize"""
    defaultValue = 1497


_UsdIsisSysOrigL1LSPBuffSize_Object = MibTableColumn
usdIsisSysOrigL1LSPBuffSize = _UsdIsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 7),
    _UsdIsisSysOrigL1LSPBuffSize_Type()
)
usdIsisSysOrigL1LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysOrigL1LSPBuffSize.setStatus("current")


class _UsdIsisSysMaxAreaAddresses_Type(Integer32):
    """Custom type usdIsisSysMaxAreaAddresses based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_UsdIsisSysMaxAreaAddresses_Type.__name__ = "Integer32"
_UsdIsisSysMaxAreaAddresses_Object = MibTableColumn
usdIsisSysMaxAreaAddresses = _UsdIsisSysMaxAreaAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 8),
    _UsdIsisSysMaxAreaAddresses_Type()
)
usdIsisSysMaxAreaAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysMaxAreaAddresses.setStatus("current")


class _UsdIsisSysMinL1LSPGenInt_Type(Integer32):
    """Custom type usdIsisSysMinL1LSPGenInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UsdIsisSysMinL1LSPGenInt_Type.__name__ = "Integer32"
_UsdIsisSysMinL1LSPGenInt_Object = MibTableColumn
usdIsisSysMinL1LSPGenInt = _UsdIsisSysMinL1LSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 9),
    _UsdIsisSysMinL1LSPGenInt_Type()
)
usdIsisSysMinL1LSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMinL1LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysMinL1LSPGenInt.setUnits("seconds")


class _UsdIsisSysMinL2LSPGenInt_Type(Integer32):
    """Custom type usdIsisSysMinL2LSPGenInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UsdIsisSysMinL2LSPGenInt_Type.__name__ = "Integer32"
_UsdIsisSysMinL2LSPGenInt_Object = MibTableColumn
usdIsisSysMinL2LSPGenInt = _UsdIsisSysMinL2LSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 10),
    _UsdIsisSysMinL2LSPGenInt_Type()
)
usdIsisSysMinL2LSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMinL2LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysMinL2LSPGenInt.setUnits("seconds")


class _UsdIsisSysPollESHelloRate_Type(Integer32):
    """Custom type usdIsisSysPollESHelloRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysPollESHelloRate_Type.__name__ = "Integer32"
_UsdIsisSysPollESHelloRate_Object = MibTableColumn
usdIsisSysPollESHelloRate = _UsdIsisSysPollESHelloRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 11),
    _UsdIsisSysPollESHelloRate_Type()
)
usdIsisSysPollESHelloRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysPollESHelloRate.setUnits("seconds")


class _UsdIsisSysWaitTime_Type(Integer32):
    """Custom type usdIsisSysWaitTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysWaitTime_Type.__name__ = "Integer32"
_UsdIsisSysWaitTime_Object = MibTableColumn
usdIsisSysWaitTime = _UsdIsisSysWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 12),
    _UsdIsisSysWaitTime_Type()
)
usdIsisSysWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysWaitTime.setUnits("seconds")


class _UsdIsisSysOperState_Type(OperState):
    """Custom type usdIsisSysOperState based on OperState"""


_UsdIsisSysOperState_Object = MibTableColumn
usdIsisSysOperState = _UsdIsisSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 13),
    _UsdIsisSysOperState_Type()
)
usdIsisSysOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysOperState.setStatus("current")
_UsdIsisSysL1State_Type = LevelState
_UsdIsisSysL1State_Object = MibTableColumn
usdIsisSysL1State = _UsdIsisSysL1State_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 14),
    _UsdIsisSysL1State_Type()
)
usdIsisSysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysL1State.setStatus("current")
_UsdIsisSysCorrLSPs_Type = Counter32
_UsdIsisSysCorrLSPs_Object = MibTableColumn
usdIsisSysCorrLSPs = _UsdIsisSysCorrLSPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 15),
    _UsdIsisSysCorrLSPs_Type()
)
usdIsisSysCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysCorrLSPs.setStatus("current")
_UsdIsisSysLSPL1DbaseOloads_Type = Counter32
_UsdIsisSysLSPL1DbaseOloads_Object = MibTableColumn
usdIsisSysLSPL1DbaseOloads = _UsdIsisSysLSPL1DbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 16),
    _UsdIsisSysLSPL1DbaseOloads_Type()
)
usdIsisSysLSPL1DbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysLSPL1DbaseOloads.setStatus("current")
_UsdIsisSysManAddrDropFromAreas_Type = Counter32
_UsdIsisSysManAddrDropFromAreas_Object = MibTableColumn
usdIsisSysManAddrDropFromAreas = _UsdIsisSysManAddrDropFromAreas_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 17),
    _UsdIsisSysManAddrDropFromAreas_Type()
)
usdIsisSysManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysManAddrDropFromAreas.setStatus("current")
_UsdIsisSysAttmptToExMaxSeqNums_Type = Counter32
_UsdIsisSysAttmptToExMaxSeqNums_Object = MibTableColumn
usdIsisSysAttmptToExMaxSeqNums = _UsdIsisSysAttmptToExMaxSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 18),
    _UsdIsisSysAttmptToExMaxSeqNums_Type()
)
usdIsisSysAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysAttmptToExMaxSeqNums.setStatus("current")
_UsdIsisSysSeqNumSkips_Type = Counter32
_UsdIsisSysSeqNumSkips_Object = MibTableColumn
usdIsisSysSeqNumSkips = _UsdIsisSysSeqNumSkips_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 19),
    _UsdIsisSysSeqNumSkips_Type()
)
usdIsisSysSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysSeqNumSkips.setStatus("current")
_UsdIsisSysOwnLSPPurges_Type = Counter32
_UsdIsisSysOwnLSPPurges_Object = MibTableColumn
usdIsisSysOwnLSPPurges = _UsdIsisSysOwnLSPPurges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 20),
    _UsdIsisSysOwnLSPPurges_Type()
)
usdIsisSysOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysOwnLSPPurges.setStatus("current")
_UsdIsisSysIDFieldLenMismatches_Type = Counter32
_UsdIsisSysIDFieldLenMismatches_Object = MibTableColumn
usdIsisSysIDFieldLenMismatches = _UsdIsisSysIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 21),
    _UsdIsisSysIDFieldLenMismatches_Type()
)
usdIsisSysIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysIDFieldLenMismatches.setStatus("current")
_UsdIsisSysMaxAreaAddrMismatches_Type = Counter32
_UsdIsisSysMaxAreaAddrMismatches_Object = MibTableColumn
usdIsisSysMaxAreaAddrMismatches = _UsdIsisSysMaxAreaAddrMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 22),
    _UsdIsisSysMaxAreaAddrMismatches_Type()
)
usdIsisSysMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysMaxAreaAddrMismatches.setStatus("current")


class _UsdIsisSysOrigL2LSPBuffSize_Type(LSPBuffSize):
    """Custom type usdIsisSysOrigL2LSPBuffSize based on LSPBuffSize"""
    defaultValue = 1497


_UsdIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
usdIsisSysOrigL2LSPBuffSize = _UsdIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 23),
    _UsdIsisSysOrigL2LSPBuffSize_Type()
)
usdIsisSysOrigL2LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysOrigL2LSPBuffSize.setStatus("current")
_UsdIsisSysL2State_Type = LevelState
_UsdIsisSysL2State_Object = MibTableColumn
usdIsisSysL2State = _UsdIsisSysL2State_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 24),
    _UsdIsisSysL2State_Type()
)
usdIsisSysL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysL2State.setStatus("current")
_UsdIsisSysLSPL2DbaseOloads_Type = Counter32
_UsdIsisSysLSPL2DbaseOloads_Object = MibTableColumn
usdIsisSysLSPL2DbaseOloads = _UsdIsisSysLSPL2DbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 25),
    _UsdIsisSysLSPL2DbaseOloads_Type()
)
usdIsisSysLSPL2DbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysLSPL2DbaseOloads.setStatus("current")
_UsdIsisSysAuthFails_Type = Counter32
_UsdIsisSysAuthFails_Object = MibTableColumn
usdIsisSysAuthFails = _UsdIsisSysAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 26),
    _UsdIsisSysAuthFails_Type()
)
usdIsisSysAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysAuthFails.setStatus("current")


class _UsdIsisSysLSPIgnoreErrors_Type(TruthValue):
    """Custom type usdIsisSysLSPIgnoreErrors based on TruthValue"""


_UsdIsisSysLSPIgnoreErrors_Object = MibTableColumn
usdIsisSysLSPIgnoreErrors = _UsdIsisSysLSPIgnoreErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 27),
    _UsdIsisSysLSPIgnoreErrors_Type()
)
usdIsisSysLSPIgnoreErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysLSPIgnoreErrors.setStatus("current")


class _UsdIsisSysMaxAreaCheck_Type(TruthValue):
    """Custom type usdIsisSysMaxAreaCheck based on TruthValue"""


_UsdIsisSysMaxAreaCheck_Object = MibTableColumn
usdIsisSysMaxAreaCheck = _UsdIsisSysMaxAreaCheck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 28),
    _UsdIsisSysMaxAreaCheck_Type()
)
usdIsisSysMaxAreaCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysMaxAreaCheck.setStatus("current")


class _UsdIsisSysSetOverloadBit_Type(TruthValue):
    """Custom type usdIsisSysSetOverloadBit based on TruthValue"""


_UsdIsisSysSetOverloadBit_Object = MibTableColumn
usdIsisSysSetOverloadBit = _UsdIsisSysSetOverloadBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 29),
    _UsdIsisSysSetOverloadBit_Type()
)
usdIsisSysSetOverloadBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysSetOverloadBit.setStatus("current")


class _UsdIsisSysSetOverloadBitStartupDuration_Type(Integer32):
    """Custom type usdIsisSysSetOverloadBitStartupDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_UsdIsisSysSetOverloadBitStartupDuration_Type.__name__ = "Integer32"
_UsdIsisSysSetOverloadBitStartupDuration_Object = MibTableColumn
usdIsisSysSetOverloadBitStartupDuration = _UsdIsisSysSetOverloadBitStartupDuration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 30),
    _UsdIsisSysSetOverloadBitStartupDuration_Type()
)
usdIsisSysSetOverloadBitStartupDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysSetOverloadBitStartupDuration.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysSetOverloadBitStartupDuration.setUnits("seconds")


class _UsdIsisSysMaxLspLifetime_Type(Integer32):
    """Custom type usdIsisSysMaxLspLifetime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysMaxLspLifetime_Type.__name__ = "Integer32"
_UsdIsisSysMaxLspLifetime_Object = MibTableColumn
usdIsisSysMaxLspLifetime = _UsdIsisSysMaxLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 31),
    _UsdIsisSysMaxLspLifetime_Type()
)
usdIsisSysMaxLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMaxLspLifetime.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysMaxLspLifetime.setUnits("seconds")


class _UsdIsisSysL1SpfInterval_Type(Integer32):
    """Custom type usdIsisSysL1SpfInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UsdIsisSysL1SpfInterval_Type.__name__ = "Integer32"
_UsdIsisSysL1SpfInterval_Object = MibTableColumn
usdIsisSysL1SpfInterval = _UsdIsisSysL1SpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 32),
    _UsdIsisSysL1SpfInterval_Type()
)
usdIsisSysL1SpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1SpfInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysL1SpfInterval.setUnits("seconds")


class _UsdIsisSysL2SpfInterval_Type(Integer32):
    """Custom type usdIsisSysL2SpfInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UsdIsisSysL2SpfInterval_Type.__name__ = "Integer32"
_UsdIsisSysL2SpfInterval_Object = MibTableColumn
usdIsisSysL2SpfInterval = _UsdIsisSysL2SpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 33),
    _UsdIsisSysL2SpfInterval_Type()
)
usdIsisSysL2SpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2SpfInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisSysL2SpfInterval.setUnits("seconds")


class _UsdIsisSysIshHoldTime_Type(Integer32):
    """Custom type usdIsisSysIshHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysIshHoldTime_Type.__name__ = "Integer32"
_UsdIsisSysIshHoldTime_Object = MibTableColumn
usdIsisSysIshHoldTime = _UsdIsisSysIshHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 34),
    _UsdIsisSysIshHoldTime_Type()
)
usdIsisSysIshHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysIshHoldTime.setStatus("current")


class _UsdIsisSysIshConfigTimer_Type(Integer32):
    """Custom type usdIsisSysIshConfigTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisSysIshConfigTimer_Type.__name__ = "Integer32"
_UsdIsisSysIshConfigTimer_Object = MibTableColumn
usdIsisSysIshConfigTimer = _UsdIsisSysIshConfigTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 35),
    _UsdIsisSysIshConfigTimer_Type()
)
usdIsisSysIshConfigTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysIshConfigTimer.setStatus("current")


class _UsdIsisSysDistributeDomainWide_Type(TruthValue):
    """Custom type usdIsisSysDistributeDomainWide based on TruthValue"""


_UsdIsisSysDistributeDomainWide_Object = MibTableColumn
usdIsisSysDistributeDomainWide = _UsdIsisSysDistributeDomainWide_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 36),
    _UsdIsisSysDistributeDomainWide_Type()
)
usdIsisSysDistributeDomainWide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDistributeDomainWide.setStatus("current")


class _UsdIsisSysDistance_Type(Integer32):
    """Custom type usdIsisSysDistance based on Integer32"""
    defaultValue = 115

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdIsisSysDistance_Type.__name__ = "Integer32"
_UsdIsisSysDistance_Object = MibTableColumn
usdIsisSysDistance = _UsdIsisSysDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 37),
    _UsdIsisSysDistance_Type()
)
usdIsisSysDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDistance.setStatus("current")


class _UsdIsisSysL1MetricStyle_Type(Integer32):
    """Custom type usdIsisSysL1MetricStyle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("usdIsisMetricStyleNarrow", 2),
          ("usdIsisMetricStyleNarrowTransition", 3),
          ("usdIsisMetricStyleTransition", 4),
          ("usdIsisMetricStyleWide", 5),
          ("usdIsisMetricStyleWideTransition", 6))
    )


_UsdIsisSysL1MetricStyle_Type.__name__ = "Integer32"
_UsdIsisSysL1MetricStyle_Object = MibTableColumn
usdIsisSysL1MetricStyle = _UsdIsisSysL1MetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 38),
    _UsdIsisSysL1MetricStyle_Type()
)
usdIsisSysL1MetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1MetricStyle.setStatus("current")


class _UsdIsisSysL2MetricStyle_Type(Integer32):
    """Custom type usdIsisSysL2MetricStyle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("usdIsisMetricStyleNarrow", 2),
          ("usdIsisMetricStyleNarrowTransition", 3),
          ("usdIsisMetricStyleTransition", 4),
          ("usdIsisMetricStyleWide", 5),
          ("usdIsisMetricStyleWideTransition", 6))
    )


_UsdIsisSysL2MetricStyle_Type.__name__ = "Integer32"
_UsdIsisSysL2MetricStyle_Object = MibTableColumn
usdIsisSysL2MetricStyle = _UsdIsisSysL2MetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 39),
    _UsdIsisSysL2MetricStyle_Type()
)
usdIsisSysL2MetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2MetricStyle.setStatus("current")


class _UsdIsisSysIsoRouteTag_Type(OctetString):
    """Custom type usdIsisSysIsoRouteTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdIsisSysIsoRouteTag_Type.__name__ = "OctetString"
_UsdIsisSysIsoRouteTag_Object = MibTableColumn
usdIsisSysIsoRouteTag = _UsdIsisSysIsoRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 40),
    _UsdIsisSysIsoRouteTag_Type()
)
usdIsisSysIsoRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysIsoRouteTag.setStatus("current")


class _UsdIsisSysMplsTeLevel_Type(Integer32):
    """Custom type usdIsisSysMplsTeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("levelNone", 0))
    )


_UsdIsisSysMplsTeLevel_Type.__name__ = "Integer32"
_UsdIsisSysMplsTeLevel_Object = MibTableColumn
usdIsisSysMplsTeLevel = _UsdIsisSysMplsTeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 41),
    _UsdIsisSysMplsTeLevel_Type()
)
usdIsisSysMplsTeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMplsTeLevel.setStatus("current")
_UsdIsisSysMplsTeRtrIdIfIndex_Type = InterfaceIndexOrZero
_UsdIsisSysMplsTeRtrIdIfIndex_Object = MibTableColumn
usdIsisSysMplsTeRtrIdIfIndex = _UsdIsisSysMplsTeRtrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 42),
    _UsdIsisSysMplsTeRtrIdIfIndex_Type()
)
usdIsisSysMplsTeRtrIdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysMplsTeRtrIdIfIndex.setStatus("current")
_UsdIsisManAreaAddrTable_Object = MibTable
usdIsisManAreaAddrTable = _UsdIsisManAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdIsisManAreaAddrTable.setStatus("current")
_UsdIsisManAreaAddrEntry_Object = MibTableRow
usdIsisManAreaAddrEntry = _UsdIsisManAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1)
)
usdIsisManAreaAddrEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisManAreaAddrSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisManAreaAddr"),
)
if mibBuilder.loadTexts:
    usdIsisManAreaAddrEntry.setStatus("current")


class _UsdIsisManAreaAddrSysInstance_Type(Integer32):
    """Custom type usdIsisManAreaAddrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisManAreaAddrSysInstance_Type.__name__ = "Integer32"
_UsdIsisManAreaAddrSysInstance_Object = MibTableColumn
usdIsisManAreaAddrSysInstance = _UsdIsisManAreaAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 1),
    _UsdIsisManAreaAddrSysInstance_Type()
)
usdIsisManAreaAddrSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisManAreaAddrSysInstance.setStatus("current")
_UsdIsisManAreaAddr_Type = OSINSAddress
_UsdIsisManAreaAddr_Object = MibTableColumn
usdIsisManAreaAddr = _UsdIsisManAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 2),
    _UsdIsisManAreaAddr_Type()
)
usdIsisManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisManAreaAddr.setStatus("current")


class _UsdIsisManAreaAddrRowStatus_Type(RowStatus):
    """Custom type usdIsisManAreaAddrRowStatus based on RowStatus"""


_UsdIsisManAreaAddrRowStatus_Object = MibTableColumn
usdIsisManAreaAddrRowStatus = _UsdIsisManAreaAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 3),
    _UsdIsisManAreaAddrRowStatus_Type()
)
usdIsisManAreaAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIsisManAreaAddrRowStatus.setStatus("current")
_UsdIsisSysProtSuppTable_Object = MibTable
usdIsisSysProtSuppTable = _UsdIsisSysProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdIsisSysProtSuppTable.setStatus("current")
_UsdIsisSysProtSuppEntry_Object = MibTableRow
usdIsisSysProtSuppEntry = _UsdIsisSysProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1)
)
usdIsisSysProtSuppEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysProtSuppSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    usdIsisSysProtSuppEntry.setStatus("current")


class _UsdIsisSysProtSuppSysInstance_Type(Integer32):
    """Custom type usdIsisSysProtSuppSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysProtSuppSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysProtSuppSysInstance_Object = MibTableColumn
usdIsisSysProtSuppSysInstance = _UsdIsisSysProtSuppSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 1),
    _UsdIsisSysProtSuppSysInstance_Type()
)
usdIsisSysProtSuppSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysProtSuppSysInstance.setStatus("current")
_UsdIsisSysProtSuppProtocol_Type = SupportedProtocol
_UsdIsisSysProtSuppProtocol_Object = MibTableColumn
usdIsisSysProtSuppProtocol = _UsdIsisSysProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 2),
    _UsdIsisSysProtSuppProtocol_Type()
)
usdIsisSysProtSuppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysProtSuppProtocol.setStatus("current")


class _UsdIsisSysProtSuppRowStatus_Type(RowStatus):
    """Custom type usdIsisSysProtSuppRowStatus based on RowStatus"""


_UsdIsisSysProtSuppRowStatus_Object = MibTableColumn
usdIsisSysProtSuppRowStatus = _UsdIsisSysProtSuppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 3),
    _UsdIsisSysProtSuppRowStatus_Type()
)
usdIsisSysProtSuppRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysProtSuppRowStatus.setStatus("current")
_UsdIsisSummAddrTable_Object = MibTable
usdIsisSummAddrTable = _UsdIsisSummAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdIsisSummAddrTable.setStatus("current")
_UsdIsisSummAddrEntry_Object = MibTableRow
usdIsisSummAddrEntry = _UsdIsisSummAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1)
)
usdIsisSummAddrEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSummAddrSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSummAddress"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSummAddrMask"),
)
if mibBuilder.loadTexts:
    usdIsisSummAddrEntry.setStatus("current")


class _UsdIsisSummAddrSysInstance_Type(Integer32):
    """Custom type usdIsisSummAddrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSummAddrSysInstance_Type.__name__ = "Integer32"
_UsdIsisSummAddrSysInstance_Object = MibTableColumn
usdIsisSummAddrSysInstance = _UsdIsisSummAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 1),
    _UsdIsisSummAddrSysInstance_Type()
)
usdIsisSummAddrSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSummAddrSysInstance.setStatus("current")
_UsdIsisSummAddress_Type = IpAddress
_UsdIsisSummAddress_Object = MibTableColumn
usdIsisSummAddress = _UsdIsisSummAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 2),
    _UsdIsisSummAddress_Type()
)
usdIsisSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSummAddress.setStatus("current")
_UsdIsisSummAddrMask_Type = IpAddress
_UsdIsisSummAddrMask_Object = MibTableColumn
usdIsisSummAddrMask = _UsdIsisSummAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 3),
    _UsdIsisSummAddrMask_Type()
)
usdIsisSummAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSummAddrMask.setStatus("current")
_UsdIsisSummAddrRowStatus_Type = RowStatus
_UsdIsisSummAddrRowStatus_Object = MibTableColumn
usdIsisSummAddrRowStatus = _UsdIsisSummAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 4),
    _UsdIsisSummAddrRowStatus_Type()
)
usdIsisSummAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIsisSummAddrRowStatus.setStatus("current")
_UsdIsisSummAddrOperState_Type = OperState
_UsdIsisSummAddrOperState_Object = MibTableColumn
usdIsisSummAddrOperState = _UsdIsisSummAddrOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 5),
    _UsdIsisSummAddrOperState_Type()
)
usdIsisSummAddrOperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIsisSummAddrOperState.setStatus("current")


class _UsdIsisSummAddrDefaultMetric_Type(Integer32):
    """Custom type usdIsisSummAddrDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_UsdIsisSummAddrDefaultMetric_Type.__name__ = "Integer32"
_UsdIsisSummAddrDefaultMetric_Object = MibTableColumn
usdIsisSummAddrDefaultMetric = _UsdIsisSummAddrDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 6),
    _UsdIsisSummAddrDefaultMetric_Type()
)
usdIsisSummAddrDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIsisSummAddrDefaultMetric.setStatus("current")
_UsdIsisSummAddrDelayMetric_Type = OtherMetric
_UsdIsisSummAddrDelayMetric_Object = MibTableColumn
usdIsisSummAddrDelayMetric = _UsdIsisSummAddrDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 7),
    _UsdIsisSummAddrDelayMetric_Type()
)
usdIsisSummAddrDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSummAddrDelayMetric.setStatus("current")
_UsdIsisSummAddrExpenseMetric_Type = OtherMetric
_UsdIsisSummAddrExpenseMetric_Object = MibTableColumn
usdIsisSummAddrExpenseMetric = _UsdIsisSummAddrExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 8),
    _UsdIsisSummAddrExpenseMetric_Type()
)
usdIsisSummAddrExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSummAddrExpenseMetric.setStatus("current")
_UsdIsisSummAddrErrorMetric_Type = OtherMetric
_UsdIsisSummAddrErrorMetric_Object = MibTableColumn
usdIsisSummAddrErrorMetric = _UsdIsisSummAddrErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 9),
    _UsdIsisSummAddrErrorMetric_Type()
)
usdIsisSummAddrErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSummAddrErrorMetric.setStatus("current")


class _UsdIsisSummLevel_Type(Integer32):
    """Custom type usdIsisSummLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level1l2IS", 3),
          ("level2IS", 2))
    )


_UsdIsisSummLevel_Type.__name__ = "Integer32"
_UsdIsisSummLevel_Object = MibTableColumn
usdIsisSummLevel = _UsdIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 10),
    _UsdIsisSummLevel_Type()
)
usdIsisSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIsisSummLevel.setStatus("current")
_UsdIsisSysHostNameTable_Object = MibTable
usdIsisSysHostNameTable = _UsdIsisSysHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5)
)
if mibBuilder.loadTexts:
    usdIsisSysHostNameTable.setStatus("current")
_UsdIsisSysHostNameEntry_Object = MibTableRow
usdIsisSysHostNameEntry = _UsdIsisSysHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1)
)
usdIsisSysHostNameEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameSysId"),
)
if mibBuilder.loadTexts:
    usdIsisSysHostNameEntry.setStatus("current")


class _UsdIsisSysHostNameSysInstance_Type(Integer32):
    """Custom type usdIsisSysHostNameSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysHostNameSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysHostNameSysInstance_Object = MibTableColumn
usdIsisSysHostNameSysInstance = _UsdIsisSysHostNameSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 1),
    _UsdIsisSysHostNameSysInstance_Type()
)
usdIsisSysHostNameSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysHostNameSysInstance.setStatus("current")
_UsdIsisSysHostNameSysId_Type = SystemID
_UsdIsisSysHostNameSysId_Object = MibTableColumn
usdIsisSysHostNameSysId = _UsdIsisSysHostNameSysId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 2),
    _UsdIsisSysHostNameSysId_Type()
)
usdIsisSysHostNameSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysHostNameSysId.setStatus("current")
_UsdIsisSysHostNameAreaAddr_Type = OSINSAddress
_UsdIsisSysHostNameAreaAddr_Object = MibTableColumn
usdIsisSysHostNameAreaAddr = _UsdIsisSysHostNameAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 3),
    _UsdIsisSysHostNameAreaAddr_Type()
)
usdIsisSysHostNameAreaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysHostNameAreaAddr.setStatus("current")


class _UsdIsisSysHostNameName_Type(OctetString):
    """Custom type usdIsisSysHostNameName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdIsisSysHostNameName_Type.__name__ = "OctetString"
_UsdIsisSysHostNameName_Object = MibTableColumn
usdIsisSysHostNameName = _UsdIsisSysHostNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 4),
    _UsdIsisSysHostNameName_Type()
)
usdIsisSysHostNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysHostNameName.setStatus("current")


class _UsdIsisSysHostNameType_Type(Integer32):
    """Custom type usdIsisSysHostNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostNameTypeDynamic", 2),
          ("hostNameTypeStatic", 1))
    )


_UsdIsisSysHostNameType_Type.__name__ = "Integer32"
_UsdIsisSysHostNameType_Object = MibTableColumn
usdIsisSysHostNameType = _UsdIsisSysHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 5),
    _UsdIsisSysHostNameType_Type()
)
usdIsisSysHostNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisSysHostNameType.setStatus("current")
_UsdIsisSysHostNameRowStatus_Type = RowStatus
_UsdIsisSysHostNameRowStatus_Object = MibTableColumn
usdIsisSysHostNameRowStatus = _UsdIsisSysHostNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 6),
    _UsdIsisSysHostNameRowStatus_Type()
)
usdIsisSysHostNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysHostNameRowStatus.setStatus("current")
_UsdIsisSysAreaAuthenticationTable_Object = MibTable
usdIsisSysAreaAuthenticationTable = _UsdIsisSysAreaAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6)
)
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationTable.setStatus("current")
_UsdIsisSysAreaAuthenticationEntry_Object = MibTableRow
usdIsisSysAreaAuthenticationEntry = _UsdIsisSysAreaAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1)
)
usdIsisSysAreaAuthenticationEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationEntry.setStatus("current")


class _UsdIsisSysAreaAuthenticationSysInstance_Type(Integer32):
    """Custom type usdIsisSysAreaAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysAreaAuthenticationSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysAreaAuthenticationSysInstance_Object = MibTableColumn
usdIsisSysAreaAuthenticationSysInstance = _UsdIsisSysAreaAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 1),
    _UsdIsisSysAreaAuthenticationSysInstance_Type()
)
usdIsisSysAreaAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationSysInstance.setStatus("current")


class _UsdIsisSysAreaAuthenticationKeyId_Type(Integer32):
    """Custom type usdIsisSysAreaAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysAreaAuthenticationKeyId_Type.__name__ = "Integer32"
_UsdIsisSysAreaAuthenticationKeyId_Object = MibTableColumn
usdIsisSysAreaAuthenticationKeyId = _UsdIsisSysAreaAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 2),
    _UsdIsisSysAreaAuthenticationKeyId_Type()
)
usdIsisSysAreaAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationKeyId.setStatus("current")


class _UsdIsisSysAreaAuthenticationPwd_Type(OctetString):
    """Custom type usdIsisSysAreaAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdIsisSysAreaAuthenticationPwd_Type.__name__ = "OctetString"
_UsdIsisSysAreaAuthenticationPwd_Object = MibTableColumn
usdIsisSysAreaAuthenticationPwd = _UsdIsisSysAreaAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 3),
    _UsdIsisSysAreaAuthenticationPwd_Type()
)
usdIsisSysAreaAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationPwd.setStatus("current")


class _UsdIsisSysAreaAuthenticationKeyType_Type(Integer32):
    """Custom type usdIsisSysAreaAuthenticationKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 2),
          ("none", 0),
          ("plaintext", 1))
    )


_UsdIsisSysAreaAuthenticationKeyType_Type.__name__ = "Integer32"
_UsdIsisSysAreaAuthenticationKeyType_Object = MibTableColumn
usdIsisSysAreaAuthenticationKeyType = _UsdIsisSysAreaAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 4),
    _UsdIsisSysAreaAuthenticationKeyType_Type()
)
usdIsisSysAreaAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationKeyType.setStatus("current")
_UsdIsisSysAreaAuthenticationStartAcceptTime_Type = AuthTime
_UsdIsisSysAreaAuthenticationStartAcceptTime_Object = MibTableColumn
usdIsisSysAreaAuthenticationStartAcceptTime = _UsdIsisSysAreaAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 5),
    _UsdIsisSysAreaAuthenticationStartAcceptTime_Type()
)
usdIsisSysAreaAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationStartAcceptTime.setStatus("current")
_UsdIsisSysAreaAuthenticationStartGenerateTime_Type = AuthTime
_UsdIsisSysAreaAuthenticationStartGenerateTime_Object = MibTableColumn
usdIsisSysAreaAuthenticationStartGenerateTime = _UsdIsisSysAreaAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 6),
    _UsdIsisSysAreaAuthenticationStartGenerateTime_Type()
)
usdIsisSysAreaAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationStartGenerateTime.setStatus("current")


class _UsdIsisSysAreaAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type usdIsisSysAreaAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysAreaAuthenticationStopAcceptTime_Object = MibTableColumn
usdIsisSysAreaAuthenticationStopAcceptTime = _UsdIsisSysAreaAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 7),
    _UsdIsisSysAreaAuthenticationStopAcceptTime_Type()
)
usdIsisSysAreaAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationStopAcceptTime.setStatus("current")


class _UsdIsisSysAreaAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type usdIsisSysAreaAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysAreaAuthenticationStopGenerateTime_Object = MibTableColumn
usdIsisSysAreaAuthenticationStopGenerateTime = _UsdIsisSysAreaAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 8),
    _UsdIsisSysAreaAuthenticationStopGenerateTime_Type()
)
usdIsisSysAreaAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationStopGenerateTime.setStatus("current")
_UsdIsisSysAreaAuthenticationRowStatus_Type = RowStatus
_UsdIsisSysAreaAuthenticationRowStatus_Object = MibTableColumn
usdIsisSysAreaAuthenticationRowStatus = _UsdIsisSysAreaAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 9),
    _UsdIsisSysAreaAuthenticationRowStatus_Type()
)
usdIsisSysAreaAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysAreaAuthenticationRowStatus.setStatus("current")
_UsdIsisSysDomainAuthenticationTable_Object = MibTable
usdIsisSysDomainAuthenticationTable = _UsdIsisSysDomainAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7)
)
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationTable.setStatus("current")
_UsdIsisSysDomainAuthenticationEntry_Object = MibTableRow
usdIsisSysDomainAuthenticationEntry = _UsdIsisSysDomainAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1)
)
usdIsisSysDomainAuthenticationEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationEntry.setStatus("current")


class _UsdIsisSysDomainAuthenticationSysInstance_Type(Integer32):
    """Custom type usdIsisSysDomainAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysDomainAuthenticationSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysDomainAuthenticationSysInstance_Object = MibTableColumn
usdIsisSysDomainAuthenticationSysInstance = _UsdIsisSysDomainAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 1),
    _UsdIsisSysDomainAuthenticationSysInstance_Type()
)
usdIsisSysDomainAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationSysInstance.setStatus("current")


class _UsdIsisSysDomainAuthenticationKeyId_Type(Integer32):
    """Custom type usdIsisSysDomainAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysDomainAuthenticationKeyId_Type.__name__ = "Integer32"
_UsdIsisSysDomainAuthenticationKeyId_Object = MibTableColumn
usdIsisSysDomainAuthenticationKeyId = _UsdIsisSysDomainAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 2),
    _UsdIsisSysDomainAuthenticationKeyId_Type()
)
usdIsisSysDomainAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationKeyId.setStatus("current")


class _UsdIsisSysDomainAuthenticationPwd_Type(OctetString):
    """Custom type usdIsisSysDomainAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdIsisSysDomainAuthenticationPwd_Type.__name__ = "OctetString"
_UsdIsisSysDomainAuthenticationPwd_Object = MibTableColumn
usdIsisSysDomainAuthenticationPwd = _UsdIsisSysDomainAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 3),
    _UsdIsisSysDomainAuthenticationPwd_Type()
)
usdIsisSysDomainAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationPwd.setStatus("current")


class _UsdIsisSysDomainAuthenticationKeyType_Type(Integer32):
    """Custom type usdIsisSysDomainAuthenticationKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 2),
          ("none", 0),
          ("plaintext", 1))
    )


_UsdIsisSysDomainAuthenticationKeyType_Type.__name__ = "Integer32"
_UsdIsisSysDomainAuthenticationKeyType_Object = MibTableColumn
usdIsisSysDomainAuthenticationKeyType = _UsdIsisSysDomainAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 4),
    _UsdIsisSysDomainAuthenticationKeyType_Type()
)
usdIsisSysDomainAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationKeyType.setStatus("current")
_UsdIsisSysDomainAuthenticationStartAcceptTime_Type = AuthTime
_UsdIsisSysDomainAuthenticationStartAcceptTime_Object = MibTableColumn
usdIsisSysDomainAuthenticationStartAcceptTime = _UsdIsisSysDomainAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 5),
    _UsdIsisSysDomainAuthenticationStartAcceptTime_Type()
)
usdIsisSysDomainAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationStartAcceptTime.setStatus("current")
_UsdIsisSysDomainAuthenticationStartGenerateTime_Type = AuthTime
_UsdIsisSysDomainAuthenticationStartGenerateTime_Object = MibTableColumn
usdIsisSysDomainAuthenticationStartGenerateTime = _UsdIsisSysDomainAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 6),
    _UsdIsisSysDomainAuthenticationStartGenerateTime_Type()
)
usdIsisSysDomainAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationStartGenerateTime.setStatus("current")


class _UsdIsisSysDomainAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type usdIsisSysDomainAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysDomainAuthenticationStopAcceptTime_Object = MibTableColumn
usdIsisSysDomainAuthenticationStopAcceptTime = _UsdIsisSysDomainAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 7),
    _UsdIsisSysDomainAuthenticationStopAcceptTime_Type()
)
usdIsisSysDomainAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationStopAcceptTime.setStatus("current")


class _UsdIsisSysDomainAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type usdIsisSysDomainAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysDomainAuthenticationStopGenerateTime_Object = MibTableColumn
usdIsisSysDomainAuthenticationStopGenerateTime = _UsdIsisSysDomainAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 8),
    _UsdIsisSysDomainAuthenticationStopGenerateTime_Type()
)
usdIsisSysDomainAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationStopGenerateTime.setStatus("current")
_UsdIsisSysDomainAuthenticationRowStatus_Type = RowStatus
_UsdIsisSysDomainAuthenticationRowStatus_Object = MibTableColumn
usdIsisSysDomainAuthenticationRowStatus = _UsdIsisSysDomainAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 9),
    _UsdIsisSysDomainAuthenticationRowStatus_Type()
)
usdIsisSysDomainAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysDomainAuthenticationRowStatus.setStatus("current")
_UsdIsisCircuitGroup_ObjectIdentity = ObjectIdentity
usdIsisCircuitGroup = _UsdIsisCircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2)
)
_UsdIsisCircTable_Object = MibTable
usdIsisCircTable = _UsdIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdIsisCircTable.setStatus("current")
_UsdIsisCircEntry_Object = MibTableRow
usdIsisCircEntry = _UsdIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1)
)
usdIsisCircEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisCircSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisCircIfIndex"),
)
if mibBuilder.loadTexts:
    usdIsisCircEntry.setStatus("current")


class _UsdIsisCircSysInstance_Type(Integer32):
    """Custom type usdIsisCircSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisCircSysInstance_Type.__name__ = "Integer32"
_UsdIsisCircSysInstance_Object = MibTableColumn
usdIsisCircSysInstance = _UsdIsisCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 1),
    _UsdIsisCircSysInstance_Type()
)
usdIsisCircSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisCircSysInstance.setStatus("current")


class _UsdIsisCircIfIndex_Type(Integer32):
    """Custom type usdIsisCircIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisCircIfIndex_Type.__name__ = "Integer32"
_UsdIsisCircIfIndex_Object = MibTableColumn
usdIsisCircIfIndex = _UsdIsisCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 2),
    _UsdIsisCircIfIndex_Type()
)
usdIsisCircIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisCircIfIndex.setStatus("current")
_UsdIsisCircLocalID_Type = Integer32
_UsdIsisCircLocalID_Object = MibTableColumn
usdIsisCircLocalID = _UsdIsisCircLocalID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 3),
    _UsdIsisCircLocalID_Type()
)
usdIsisCircLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircLocalID.setStatus("current")


class _UsdIsisCircOperState_Type(OperState):
    """Custom type usdIsisCircOperState based on OperState"""


_UsdIsisCircOperState_Object = MibTableColumn
usdIsisCircOperState = _UsdIsisCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 4),
    _UsdIsisCircOperState_Type()
)
usdIsisCircOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircOperState.setStatus("current")


class _UsdIsisCircRowStatus_Type(RowStatus):
    """Custom type usdIsisCircRowStatus based on RowStatus"""


_UsdIsisCircRowStatus_Object = MibTableColumn
usdIsisCircRowStatus = _UsdIsisCircRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 5),
    _UsdIsisCircRowStatus_Type()
)
usdIsisCircRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircRowStatus.setStatus("current")


class _UsdIsisCircType_Type(Integer32):
    """Custom type usdIsisCircType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("ptToPt", 2))
    )


_UsdIsisCircType_Type.__name__ = "Integer32"
_UsdIsisCircType_Object = MibTableColumn
usdIsisCircType = _UsdIsisCircType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 6),
    _UsdIsisCircType_Type()
)
usdIsisCircType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircType.setStatus("current")


class _UsdIsisCircL1DefaultMetric_Type(UsdDefaultMetric):
    """Custom type usdIsisCircL1DefaultMetric based on UsdDefaultMetric"""
    defaultValue = 10


_UsdIsisCircL1DefaultMetric_Object = MibTableColumn
usdIsisCircL1DefaultMetric = _UsdIsisCircL1DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 7),
    _UsdIsisCircL1DefaultMetric_Type()
)
usdIsisCircL1DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL1DefaultMetric.setStatus("current")


class _UsdIsisCircL1DelayMetric_Type(OtherMetric):
    """Custom type usdIsisCircL1DelayMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL1DelayMetric_Object = MibTableColumn
usdIsisCircL1DelayMetric = _UsdIsisCircL1DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 8),
    _UsdIsisCircL1DelayMetric_Type()
)
usdIsisCircL1DelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL1DelayMetric.setStatus("current")


class _UsdIsisCircL1ExpenseMetric_Type(OtherMetric):
    """Custom type usdIsisCircL1ExpenseMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL1ExpenseMetric_Object = MibTableColumn
usdIsisCircL1ExpenseMetric = _UsdIsisCircL1ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 9),
    _UsdIsisCircL1ExpenseMetric_Type()
)
usdIsisCircL1ExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL1ExpenseMetric.setStatus("current")


class _UsdIsisCircL1ErrorMetric_Type(OtherMetric):
    """Custom type usdIsisCircL1ErrorMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL1ErrorMetric_Object = MibTableColumn
usdIsisCircL1ErrorMetric = _UsdIsisCircL1ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 10),
    _UsdIsisCircL1ErrorMetric_Type()
)
usdIsisCircL1ErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL1ErrorMetric.setStatus("current")


class _UsdIsisCircExtDomain_Type(TruthValue):
    """Custom type usdIsisCircExtDomain based on TruthValue"""


_UsdIsisCircExtDomain_Object = MibTableColumn
usdIsisCircExtDomain = _UsdIsisCircExtDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 11),
    _UsdIsisCircExtDomain_Type()
)
usdIsisCircExtDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircExtDomain.setStatus("current")
_UsdIsisCircAdjChanges_Type = Counter32
_UsdIsisCircAdjChanges_Object = MibTableColumn
usdIsisCircAdjChanges = _UsdIsisCircAdjChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 12),
    _UsdIsisCircAdjChanges_Type()
)
usdIsisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircAdjChanges.setStatus("current")
_UsdIsisCircInitFails_Type = Counter32
_UsdIsisCircInitFails_Object = MibTableColumn
usdIsisCircInitFails = _UsdIsisCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 13),
    _UsdIsisCircInitFails_Type()
)
usdIsisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircInitFails.setStatus("current")
_UsdIsisCircRejAdjs_Type = Counter32
_UsdIsisCircRejAdjs_Object = MibTableColumn
usdIsisCircRejAdjs = _UsdIsisCircRejAdjs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 14),
    _UsdIsisCircRejAdjs_Type()
)
usdIsisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircRejAdjs.setStatus("current")
_UsdIsisCircOutCtrlPDUs_Type = Counter32
_UsdIsisCircOutCtrlPDUs_Object = MibTableColumn
usdIsisCircOutCtrlPDUs = _UsdIsisCircOutCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 15),
    _UsdIsisCircOutCtrlPDUs_Type()
)
usdIsisCircOutCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircOutCtrlPDUs.setStatus("current")
_UsdIsisCircInCtrlPDUs_Type = Counter32
_UsdIsisCircInCtrlPDUs_Object = MibTableColumn
usdIsisCircInCtrlPDUs = _UsdIsisCircInCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 16),
    _UsdIsisCircInCtrlPDUs_Type()
)
usdIsisCircInCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircInCtrlPDUs.setStatus("current")
_UsdIsisCircIDFieldLenMismatches_Type = Counter32
_UsdIsisCircIDFieldLenMismatches_Object = MibTableColumn
usdIsisCircIDFieldLenMismatches = _UsdIsisCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 17),
    _UsdIsisCircIDFieldLenMismatches_Type()
)
usdIsisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircIDFieldLenMismatches.setStatus("current")


class _UsdIsisCircL2DefaultMetric_Type(UsdDefaultMetric):
    """Custom type usdIsisCircL2DefaultMetric based on UsdDefaultMetric"""
    defaultValue = 10


_UsdIsisCircL2DefaultMetric_Object = MibTableColumn
usdIsisCircL2DefaultMetric = _UsdIsisCircL2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 18),
    _UsdIsisCircL2DefaultMetric_Type()
)
usdIsisCircL2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL2DefaultMetric.setStatus("current")


class _UsdIsisCircL2DelayMetric_Type(OtherMetric):
    """Custom type usdIsisCircL2DelayMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL2DelayMetric_Object = MibTableColumn
usdIsisCircL2DelayMetric = _UsdIsisCircL2DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 19),
    _UsdIsisCircL2DelayMetric_Type()
)
usdIsisCircL2DelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL2DelayMetric.setStatus("current")


class _UsdIsisCircL2ExpenseMetric_Type(OtherMetric):
    """Custom type usdIsisCircL2ExpenseMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL2ExpenseMetric_Object = MibTableColumn
usdIsisCircL2ExpenseMetric = _UsdIsisCircL2ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 20),
    _UsdIsisCircL2ExpenseMetric_Type()
)
usdIsisCircL2ExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL2ExpenseMetric.setStatus("current")


class _UsdIsisCircL2ErrorMetric_Type(OtherMetric):
    """Custom type usdIsisCircL2ErrorMetric based on OtherMetric"""
    defaultValue = 0


_UsdIsisCircL2ErrorMetric_Object = MibTableColumn
usdIsisCircL2ErrorMetric = _UsdIsisCircL2ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 21),
    _UsdIsisCircL2ErrorMetric_Type()
)
usdIsisCircL2ErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL2ErrorMetric.setStatus("current")


class _UsdIsisCircManL2Only_Type(TruthValue):
    """Custom type usdIsisCircManL2Only based on TruthValue"""


_UsdIsisCircManL2Only_Object = MibTableColumn
usdIsisCircManL2Only = _UsdIsisCircManL2Only_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 22),
    _UsdIsisCircManL2Only_Type()
)
usdIsisCircManL2Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircManL2Only.setStatus("current")


class _UsdIsisCircL1ISPriority_Type(ISPriority):
    """Custom type usdIsisCircL1ISPriority based on ISPriority"""
    defaultValue = 64


_UsdIsisCircL1ISPriority_Object = MibTableColumn
usdIsisCircL1ISPriority = _UsdIsisCircL1ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 23),
    _UsdIsisCircL1ISPriority_Type()
)
usdIsisCircL1ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL1ISPriority.setStatus("current")
_UsdIsisCircL1CircID_Type = CircuitID
_UsdIsisCircL1CircID_Object = MibTableColumn
usdIsisCircL1CircID = _UsdIsisCircL1CircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 24),
    _UsdIsisCircL1CircID_Type()
)
usdIsisCircL1CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL1CircID.setStatus("current")
_UsdIsisCircL1DesIS_Type = SystemID
_UsdIsisCircL1DesIS_Object = MibTableColumn
usdIsisCircL1DesIS = _UsdIsisCircL1DesIS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 25),
    _UsdIsisCircL1DesIS_Type()
)
usdIsisCircL1DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL1DesIS.setStatus("current")
_UsdIsisCircLANL1DesISChanges_Type = Counter32
_UsdIsisCircLANL1DesISChanges_Object = MibTableColumn
usdIsisCircLANL1DesISChanges = _UsdIsisCircLANL1DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 26),
    _UsdIsisCircLANL1DesISChanges_Type()
)
usdIsisCircLANL1DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircLANL1DesISChanges.setStatus("current")


class _UsdIsisCircL2ISPriority_Type(ISPriority):
    """Custom type usdIsisCircL2ISPriority based on ISPriority"""
    defaultValue = 64


_UsdIsisCircL2ISPriority_Object = MibTableColumn
usdIsisCircL2ISPriority = _UsdIsisCircL2ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 27),
    _UsdIsisCircL2ISPriority_Type()
)
usdIsisCircL2ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL2ISPriority.setStatus("current")
_UsdIsisCircL2CircID_Type = CircuitID
_UsdIsisCircL2CircID_Object = MibTableColumn
usdIsisCircL2CircID = _UsdIsisCircL2CircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 28),
    _UsdIsisCircL2CircID_Type()
)
usdIsisCircL2CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL2CircID.setStatus("current")
_UsdIsisCircL2DesIS_Type = SystemID
_UsdIsisCircL2DesIS_Object = MibTableColumn
usdIsisCircL2DesIS = _UsdIsisCircL2DesIS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 29),
    _UsdIsisCircL2DesIS_Type()
)
usdIsisCircL2DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircL2DesIS.setStatus("current")
_UsdIsisCircLANL2DesISChanges_Type = Counter32
_UsdIsisCircLANL2DesISChanges_Object = MibTableColumn
usdIsisCircLANL2DesISChanges = _UsdIsisCircLANL2DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 30),
    _UsdIsisCircLANL2DesISChanges_Type()
)
usdIsisCircLANL2DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircLANL2DesISChanges.setStatus("current")


class _UsdIsisCircMCAddr_Type(Integer32):
    """Custom type usdIsisCircMCAddr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("functional", 2),
          ("group", 1))
    )


_UsdIsisCircMCAddr_Type.__name__ = "Integer32"
_UsdIsisCircMCAddr_Object = MibTableColumn
usdIsisCircMCAddr = _UsdIsisCircMCAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 31),
    _UsdIsisCircMCAddr_Type()
)
usdIsisCircMCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircMCAddr.setStatus("current")
_UsdIsisCircPtToPtCircID_Type = CircuitID
_UsdIsisCircPtToPtCircID_Object = MibTableColumn
usdIsisCircPtToPtCircID = _UsdIsisCircPtToPtCircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 32),
    _UsdIsisCircPtToPtCircID_Type()
)
usdIsisCircPtToPtCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircPtToPtCircID.setStatus("current")


class _UsdIsisCircL1HelloTimer_Type(Integer32):
    """Custom type usdIsisCircL1HelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIsisCircL1HelloTimer_Type.__name__ = "Integer32"
_UsdIsisCircL1HelloTimer_Object = MibTableColumn
usdIsisCircL1HelloTimer = _UsdIsisCircL1HelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 33),
    _UsdIsisCircL1HelloTimer_Type()
)
usdIsisCircL1HelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL1HelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircL1HelloTimer.setUnits("seconds")


class _UsdIsisCircL2HelloTimer_Type(Integer32):
    """Custom type usdIsisCircL2HelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIsisCircL2HelloTimer_Type.__name__ = "Integer32"
_UsdIsisCircL2HelloTimer_Object = MibTableColumn
usdIsisCircL2HelloTimer = _UsdIsisCircL2HelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 34),
    _UsdIsisCircL2HelloTimer_Type()
)
usdIsisCircL2HelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL2HelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircL2HelloTimer.setUnits("seconds")


class _UsdIsisCircL1HelloMultiplier_Type(Integer32):
    """Custom type usdIsisCircL1HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_UsdIsisCircL1HelloMultiplier_Type.__name__ = "Integer32"
_UsdIsisCircL1HelloMultiplier_Object = MibTableColumn
usdIsisCircL1HelloMultiplier = _UsdIsisCircL1HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 35),
    _UsdIsisCircL1HelloMultiplier_Type()
)
usdIsisCircL1HelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL1HelloMultiplier.setStatus("current")


class _UsdIsisCircL2HelloMultiplier_Type(Integer32):
    """Custom type usdIsisCircL2HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_UsdIsisCircL2HelloMultiplier_Type.__name__ = "Integer32"
_UsdIsisCircL2HelloMultiplier_Object = MibTableColumn
usdIsisCircL2HelloMultiplier = _UsdIsisCircL2HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 36),
    _UsdIsisCircL2HelloMultiplier_Type()
)
usdIsisCircL2HelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL2HelloMultiplier.setStatus("current")


class _UsdIsisCircMinLSPTransInt_Type(Integer32):
    """Custom type usdIsisCircMinLSPTransInt based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisCircMinLSPTransInt_Type.__name__ = "Integer32"
_UsdIsisCircMinLSPTransInt_Object = MibTableColumn
usdIsisCircMinLSPTransInt = _UsdIsisCircMinLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 37),
    _UsdIsisCircMinLSPTransInt_Type()
)
usdIsisCircMinLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircMinLSPTransInt.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircMinLSPTransInt.setUnits("milliseconds")


class _UsdIsisCircMinLSPReTransInt_Type(Integer32):
    """Custom type usdIsisCircMinLSPReTransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisCircMinLSPReTransInt_Type.__name__ = "Integer32"
_UsdIsisCircMinLSPReTransInt_Object = MibTableColumn
usdIsisCircMinLSPReTransInt = _UsdIsisCircMinLSPReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 38),
    _UsdIsisCircMinLSPReTransInt_Type()
)
usdIsisCircMinLSPReTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircMinLSPReTransInt.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircMinLSPReTransInt.setUnits("seconds")


class _UsdIsisCircL1CSNPInterval_Type(Integer32):
    """Custom type usdIsisCircL1CSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIsisCircL1CSNPInterval_Type.__name__ = "Integer32"
_UsdIsisCircL1CSNPInterval_Object = MibTableColumn
usdIsisCircL1CSNPInterval = _UsdIsisCircL1CSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 39),
    _UsdIsisCircL1CSNPInterval_Type()
)
usdIsisCircL1CSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL1CSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircL1CSNPInterval.setUnits("seconds")


class _UsdIsisCircL2CSNPInterval_Type(Integer32):
    """Custom type usdIsisCircL2CSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdIsisCircL2CSNPInterval_Type.__name__ = "Integer32"
_UsdIsisCircL2CSNPInterval_Object = MibTableColumn
usdIsisCircL2CSNPInterval = _UsdIsisCircL2CSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 40),
    _UsdIsisCircL2CSNPInterval_Type()
)
usdIsisCircL2CSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircL2CSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircL2CSNPInterval.setUnits("seconds")


class _UsdIsisCircLSPThrottle_Type(Integer32):
    """Custom type usdIsisCircLSPThrottle based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIsisCircLSPThrottle_Type.__name__ = "Integer32"
_UsdIsisCircLSPThrottle_Object = MibTableColumn
usdIsisCircLSPThrottle = _UsdIsisCircLSPThrottle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 41),
    _UsdIsisCircLSPThrottle_Type()
)
usdIsisCircLSPThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    usdIsisCircLSPThrottle.setUnits("milliseconds")


class _UsdIsisCircMeshGroupEnabled_Type(Integer32):
    """Custom type usdIsisCircMeshGroupEnabled based on Integer32"""
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
        *(("blocked", 2),
          ("inactive", 1),
          ("set", 3))
    )


_UsdIsisCircMeshGroupEnabled_Type.__name__ = "Integer32"
_UsdIsisCircMeshGroupEnabled_Object = MibTableColumn
usdIsisCircMeshGroupEnabled = _UsdIsisCircMeshGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 42),
    _UsdIsisCircMeshGroupEnabled_Type()
)
usdIsisCircMeshGroupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircMeshGroupEnabled.setStatus("current")


class _UsdIsisCircMeshGroup_Type(Integer32):
    """Custom type usdIsisCircMeshGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_UsdIsisCircMeshGroup_Type.__name__ = "Integer32"
_UsdIsisCircMeshGroup_Object = MibTableColumn
usdIsisCircMeshGroup = _UsdIsisCircMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 43),
    _UsdIsisCircMeshGroup_Type()
)
usdIsisCircMeshGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircMeshGroup.setStatus("current")


class _UsdIsisCircLevel_Type(Integer32):
    """Custom type usdIsisCircLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 0),
          ("level1l2IS", 1),
          ("level2Only", 2))
    )


_UsdIsisCircLevel_Type.__name__ = "Integer32"
_UsdIsisCircLevel_Object = MibTableColumn
usdIsisCircLevel = _UsdIsisCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 44),
    _UsdIsisCircLevel_Type()
)
usdIsisCircLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisCircLevel.setStatus("current")


class _UsdIsisCircState_Type(Integer32):
    """Custom type usdIsisCircState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isisCircuitDown", 1),
          ("isisCircuitUp", 2))
    )


_UsdIsisCircState_Type.__name__ = "Integer32"
_UsdIsisCircState_Object = MibTableColumn
usdIsisCircState = _UsdIsisCircState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 45),
    _UsdIsisCircState_Type()
)
usdIsisCircState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIsisCircState.setStatus("current")
_UsdIsisSysL1CircAuthenticationTable_Object = MibTable
usdIsisSysL1CircAuthenticationTable = _UsdIsisSysL1CircAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationTable.setStatus("current")
_UsdIsisSysL1CircAuthenticationEntry_Object = MibTableRow
usdIsisSysL1CircAuthenticationEntry = _UsdIsisSysL1CircAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1)
)
usdIsisSysL1CircAuthenticationEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationIfIndex"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationEntry.setStatus("current")


class _UsdIsisSysL1CircAuthenticationSysInstance_Type(Integer32):
    """Custom type usdIsisSysL1CircAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL1CircAuthenticationSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysL1CircAuthenticationSysInstance_Object = MibTableColumn
usdIsisSysL1CircAuthenticationSysInstance = _UsdIsisSysL1CircAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 1),
    _UsdIsisSysL1CircAuthenticationSysInstance_Type()
)
usdIsisSysL1CircAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationSysInstance.setStatus("current")


class _UsdIsisSysL1CircAuthenticationIfIndex_Type(Integer32):
    """Custom type usdIsisSysL1CircAuthenticationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL1CircAuthenticationIfIndex_Type.__name__ = "Integer32"
_UsdIsisSysL1CircAuthenticationIfIndex_Object = MibTableColumn
usdIsisSysL1CircAuthenticationIfIndex = _UsdIsisSysL1CircAuthenticationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 2),
    _UsdIsisSysL1CircAuthenticationIfIndex_Type()
)
usdIsisSysL1CircAuthenticationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationIfIndex.setStatus("current")


class _UsdIsisSysL1CircAuthenticationKeyId_Type(Integer32):
    """Custom type usdIsisSysL1CircAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL1CircAuthenticationKeyId_Type.__name__ = "Integer32"
_UsdIsisSysL1CircAuthenticationKeyId_Object = MibTableColumn
usdIsisSysL1CircAuthenticationKeyId = _UsdIsisSysL1CircAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 3),
    _UsdIsisSysL1CircAuthenticationKeyId_Type()
)
usdIsisSysL1CircAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationKeyId.setStatus("current")


class _UsdIsisSysL1CircAuthenticationPwd_Type(OctetString):
    """Custom type usdIsisSysL1CircAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdIsisSysL1CircAuthenticationPwd_Type.__name__ = "OctetString"
_UsdIsisSysL1CircAuthenticationPwd_Object = MibTableColumn
usdIsisSysL1CircAuthenticationPwd = _UsdIsisSysL1CircAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 4),
    _UsdIsisSysL1CircAuthenticationPwd_Type()
)
usdIsisSysL1CircAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationPwd.setStatus("current")


class _UsdIsisSysL1CircAuthenticationKeyType_Type(Integer32):
    """Custom type usdIsisSysL1CircAuthenticationKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 2),
          ("none", 0),
          ("plaintext", 1))
    )


_UsdIsisSysL1CircAuthenticationKeyType_Type.__name__ = "Integer32"
_UsdIsisSysL1CircAuthenticationKeyType_Object = MibTableColumn
usdIsisSysL1CircAuthenticationKeyType = _UsdIsisSysL1CircAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 5),
    _UsdIsisSysL1CircAuthenticationKeyType_Type()
)
usdIsisSysL1CircAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationKeyType.setStatus("current")
_UsdIsisSysL1CircAuthenticationStartAcceptTime_Type = AuthTime
_UsdIsisSysL1CircAuthenticationStartAcceptTime_Object = MibTableColumn
usdIsisSysL1CircAuthenticationStartAcceptTime = _UsdIsisSysL1CircAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 6),
    _UsdIsisSysL1CircAuthenticationStartAcceptTime_Type()
)
usdIsisSysL1CircAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationStartAcceptTime.setStatus("current")
_UsdIsisSysL1CircAuthenticationStartGenerateTime_Type = AuthTime
_UsdIsisSysL1CircAuthenticationStartGenerateTime_Object = MibTableColumn
usdIsisSysL1CircAuthenticationStartGenerateTime = _UsdIsisSysL1CircAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 7),
    _UsdIsisSysL1CircAuthenticationStartGenerateTime_Type()
)
usdIsisSysL1CircAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationStartGenerateTime.setStatus("current")


class _UsdIsisSysL1CircAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type usdIsisSysL1CircAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysL1CircAuthenticationStopAcceptTime_Object = MibTableColumn
usdIsisSysL1CircAuthenticationStopAcceptTime = _UsdIsisSysL1CircAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 8),
    _UsdIsisSysL1CircAuthenticationStopAcceptTime_Type()
)
usdIsisSysL1CircAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationStopAcceptTime.setStatus("current")


class _UsdIsisSysL1CircAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type usdIsisSysL1CircAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysL1CircAuthenticationStopGenerateTime_Object = MibTableColumn
usdIsisSysL1CircAuthenticationStopGenerateTime = _UsdIsisSysL1CircAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 9),
    _UsdIsisSysL1CircAuthenticationStopGenerateTime_Type()
)
usdIsisSysL1CircAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationStopGenerateTime.setStatus("current")
_UsdIsisSysL1CircAuthenticationRowStatus_Type = RowStatus
_UsdIsisSysL1CircAuthenticationRowStatus_Object = MibTableColumn
usdIsisSysL1CircAuthenticationRowStatus = _UsdIsisSysL1CircAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 10),
    _UsdIsisSysL1CircAuthenticationRowStatus_Type()
)
usdIsisSysL1CircAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL1CircAuthenticationRowStatus.setStatus("current")
_UsdIsisSysL2CircAuthenticationTable_Object = MibTable
usdIsisSysL2CircAuthenticationTable = _UsdIsisSysL2CircAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3)
)
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationTable.setStatus("current")
_UsdIsisSysL2CircAuthenticationEntry_Object = MibTableRow
usdIsisSysL2CircAuthenticationEntry = _UsdIsisSysL2CircAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1)
)
usdIsisSysL2CircAuthenticationEntry.setIndexNames(
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationSysInstance"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationIfIndex"),
    (0, "Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationEntry.setStatus("current")


class _UsdIsisSysL2CircAuthenticationSysInstance_Type(Integer32):
    """Custom type usdIsisSysL2CircAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL2CircAuthenticationSysInstance_Type.__name__ = "Integer32"
_UsdIsisSysL2CircAuthenticationSysInstance_Object = MibTableColumn
usdIsisSysL2CircAuthenticationSysInstance = _UsdIsisSysL2CircAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 1),
    _UsdIsisSysL2CircAuthenticationSysInstance_Type()
)
usdIsisSysL2CircAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationSysInstance.setStatus("current")


class _UsdIsisSysL2CircAuthenticationIfIndex_Type(Integer32):
    """Custom type usdIsisSysL2CircAuthenticationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL2CircAuthenticationIfIndex_Type.__name__ = "Integer32"
_UsdIsisSysL2CircAuthenticationIfIndex_Object = MibTableColumn
usdIsisSysL2CircAuthenticationIfIndex = _UsdIsisSysL2CircAuthenticationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 2),
    _UsdIsisSysL2CircAuthenticationIfIndex_Type()
)
usdIsisSysL2CircAuthenticationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationIfIndex.setStatus("current")


class _UsdIsisSysL2CircAuthenticationKeyId_Type(Integer32):
    """Custom type usdIsisSysL2CircAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIsisSysL2CircAuthenticationKeyId_Type.__name__ = "Integer32"
_UsdIsisSysL2CircAuthenticationKeyId_Object = MibTableColumn
usdIsisSysL2CircAuthenticationKeyId = _UsdIsisSysL2CircAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 3),
    _UsdIsisSysL2CircAuthenticationKeyId_Type()
)
usdIsisSysL2CircAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationKeyId.setStatus("current")


class _UsdIsisSysL2CircAuthenticationPwd_Type(OctetString):
    """Custom type usdIsisSysL2CircAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdIsisSysL2CircAuthenticationPwd_Type.__name__ = "OctetString"
_UsdIsisSysL2CircAuthenticationPwd_Object = MibTableColumn
usdIsisSysL2CircAuthenticationPwd = _UsdIsisSysL2CircAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 4),
    _UsdIsisSysL2CircAuthenticationPwd_Type()
)
usdIsisSysL2CircAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationPwd.setStatus("current")


class _UsdIsisSysL2CircAuthenticationKeyType_Type(Integer32):
    """Custom type usdIsisSysL2CircAuthenticationKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 2),
          ("none", 0),
          ("plaintext", 1))
    )


_UsdIsisSysL2CircAuthenticationKeyType_Type.__name__ = "Integer32"
_UsdIsisSysL2CircAuthenticationKeyType_Object = MibTableColumn
usdIsisSysL2CircAuthenticationKeyType = _UsdIsisSysL2CircAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 5),
    _UsdIsisSysL2CircAuthenticationKeyType_Type()
)
usdIsisSysL2CircAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationKeyType.setStatus("current")
_UsdIsisSysL2CircAuthenticationStartAcceptTime_Type = AuthTime
_UsdIsisSysL2CircAuthenticationStartAcceptTime_Object = MibTableColumn
usdIsisSysL2CircAuthenticationStartAcceptTime = _UsdIsisSysL2CircAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 6),
    _UsdIsisSysL2CircAuthenticationStartAcceptTime_Type()
)
usdIsisSysL2CircAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationStartAcceptTime.setStatus("current")
_UsdIsisSysL2CircAuthenticationStartGenerateTime_Type = AuthTime
_UsdIsisSysL2CircAuthenticationStartGenerateTime_Object = MibTableColumn
usdIsisSysL2CircAuthenticationStartGenerateTime = _UsdIsisSysL2CircAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 7),
    _UsdIsisSysL2CircAuthenticationStartGenerateTime_Type()
)
usdIsisSysL2CircAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationStartGenerateTime.setStatus("current")


class _UsdIsisSysL2CircAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type usdIsisSysL2CircAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysL2CircAuthenticationStopAcceptTime_Object = MibTableColumn
usdIsisSysL2CircAuthenticationStopAcceptTime = _UsdIsisSysL2CircAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 8),
    _UsdIsisSysL2CircAuthenticationStopAcceptTime_Type()
)
usdIsisSysL2CircAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationStopAcceptTime.setStatus("current")


class _UsdIsisSysL2CircAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type usdIsisSysL2CircAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_UsdIsisSysL2CircAuthenticationStopGenerateTime_Object = MibTableColumn
usdIsisSysL2CircAuthenticationStopGenerateTime = _UsdIsisSysL2CircAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 9),
    _UsdIsisSysL2CircAuthenticationStopGenerateTime_Type()
)
usdIsisSysL2CircAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationStopGenerateTime.setStatus("current")


class _UsdIsisSysL2CircAuthenticationRowStatus_Type(RowStatus):
    """Custom type usdIsisSysL2CircAuthenticationRowStatus based on RowStatus"""


_UsdIsisSysL2CircAuthenticationRowStatus_Object = MibTableColumn
usdIsisSysL2CircAuthenticationRowStatus = _UsdIsisSysL2CircAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 10),
    _UsdIsisSysL2CircAuthenticationRowStatus_Type()
)
usdIsisSysL2CircAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIsisSysL2CircAuthenticationRowStatus.setStatus("current")
_UsdIsisTrapGroup_ObjectIdentity = ObjectIdentity
usdIsisTrapGroup = _UsdIsisTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 2)
)
_UsdIsisConformance_ObjectIdentity = ObjectIdentity
usdIsisConformance = _UsdIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3)
)
_UsdIsisCompliances_ObjectIdentity = ObjectIdentity
usdIsisCompliances = _UsdIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1)
)
_UsdIsisMIBGroups_ObjectIdentity = ObjectIdentity
usdIsisMIBGroups = _UsdIsisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2)
)

# Managed Objects groups

usdIsisSystemMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 1)
)
usdIsisSystemMgmtGroup.setObjects(
      *(("Unisphere-Data-ISIS-MIB", "usdIsisSysVersion"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxPathSplits"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxLSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOrigL1LSPBuffSize"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaAddresses"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMinL1LSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMinL2LSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysPollESHelloRate"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysWaitTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1State"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysCorrLSPs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPL1DbaseOloads"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysManAddrDropFromAreas"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAttmptToExMaxSeqNums"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSeqNumSkips"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOwnLSPPurges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIDFieldLenMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaAddrMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOrigL2LSPBuffSize"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2State"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPL2DbaseOloads"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAuthFails"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPIgnoreErrors"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaCheck"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSetOverloadBit"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSetOverloadBitStartupDuration"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxLspLifetime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1SpfInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2SpfInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIshHoldTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIshConfigTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDistributeDomainWide"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDistance"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1MetricStyle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2MetricStyle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIsoRouteTag"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisManAreaAddrRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysProtSuppRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrDefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrDelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummLevel"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameAreaAddr"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameName"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    usdIsisSystemMgmtGroup.setStatus("obsolete")

usdIsisCircuitMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 2)
)
usdIsisCircuitMgmtGroup.setObjects(
      *(("Unisphere-Data-ISIS-MIB", "usdIsisCircLocalID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircExtDomain"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircAdjChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircInitFails"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircRejAdjs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircOutCtrlPDUs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircInCtrlPDUs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircIDFieldLenMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircManL2Only"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ISPriority"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1CircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DesIS"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLANL1DesISChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ISPriority"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2CircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DesIS"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLANL2DesISChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMCAddr"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircPtToPtCircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1HelloTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2HelloTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1HelloMultiplier"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2HelloMultiplier"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMinLSPTransInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMinLSPReTransInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1CSNPInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2CSNPInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLSPThrottle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMeshGroupEnabled"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMeshGroup"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLevel"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    usdIsisCircuitMgmtGroup.setStatus("obsolete")

usdIsisCircuitMgmtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 3)
)
usdIsisCircuitMgmtGroup2.setObjects(
      *(("Unisphere-Data-ISIS-MIB", "usdIsisCircLocalID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircExtDomain"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircAdjChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircInitFails"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircRejAdjs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircOutCtrlPDUs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircInCtrlPDUs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircIDFieldLenMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircManL2Only"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1ISPriority"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1CircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1DesIS"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLANL1DesISChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2ISPriority"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2CircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2DesIS"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLANL2DesISChanges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMCAddr"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircPtToPtCircID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1HelloTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2HelloTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1HelloMultiplier"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2HelloMultiplier"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMinLSPTransInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMinLSPReTransInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL1CSNPInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircL2CSNPInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLSPThrottle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMeshGroupEnabled"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircMeshGroup"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircLevel"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisCircState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1CircAuthenticationRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2CircAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    usdIsisCircuitMgmtGroup2.setStatus("current")

usdIsisSystemMgmtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 4)
)
usdIsisSystemMgmtGroup2.setObjects(
      *(("Unisphere-Data-ISIS-MIB", "usdIsisSysVersion"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysID"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxPathSplits"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxLSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOrigL1LSPBuffSize"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaAddresses"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMinL1LSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMinL2LSPGenInt"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysPollESHelloRate"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysWaitTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1State"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysCorrLSPs"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPL1DbaseOloads"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysManAddrDropFromAreas"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAttmptToExMaxSeqNums"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSeqNumSkips"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOwnLSPPurges"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIDFieldLenMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaAddrMismatches"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysOrigL2LSPBuffSize"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2State"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPL2DbaseOloads"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAuthFails"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysLSPIgnoreErrors"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxAreaCheck"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSetOverloadBit"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysSetOverloadBitStartupDuration"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMaxLspLifetime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1SpfInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2SpfInterval"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIshHoldTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIshConfigTimer"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDistributeDomainWide"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDistance"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL1MetricStyle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysL2MetricStyle"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysIsoRouteTag"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMplsTeLevel"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysMplsTeRtrIdIfIndex"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisManAreaAddrRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysProtSuppRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrOperState"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrDefaultMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrDelayMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrExpenseMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummAddrErrorMetric"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSummLevel"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameAreaAddr"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameName"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysHostNameRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysAreaAuthenticationRowStatus"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationPwd"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationKeyType"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStartAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStartGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStopAcceptTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationStopGenerateTime"),
        ("Unisphere-Data-ISIS-MIB", "usdIsisSysDomainAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    usdIsisSystemMgmtGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 1)
)
if mibBuilder.loadTexts:
    usdIsisCompliance.setStatus(
        "obsolete"
    )

usdIsisCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 2)
)
if mibBuilder.loadTexts:
    usdIsisCompliance2.setStatus(
        "obsolete"
    )

usdIsisCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 3)
)
if mibBuilder.loadTexts:
    usdIsisCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ISIS-MIB",
    **{"OSINSAddress": OSINSAddress,
       "SystemID": SystemID,
       "OperState": OperState,
       "AuthTime": AuthTime,
       "LSPBuffSize": LSPBuffSize,
       "LevelState": LevelState,
       "SupportedProtocol": SupportedProtocol,
       "UsdDefaultMetric": UsdDefaultMetric,
       "OtherMetric": OtherMetric,
       "CircuitID": CircuitID,
       "ISPriority": ISPriority,
       "usdIsisMIB": usdIsisMIB,
       "usdIsisObjects": usdIsisObjects,
       "usdIsisSystemGroup": usdIsisSystemGroup,
       "usdIsisSysTable": usdIsisSysTable,
       "usdIsisSysEntry": usdIsisSysEntry,
       "usdIsisSysInstance": usdIsisSysInstance,
       "usdIsisSysVersion": usdIsisSysVersion,
       "usdIsisSysType": usdIsisSysType,
       "usdIsisSysID": usdIsisSysID,
       "usdIsisSysMaxPathSplits": usdIsisSysMaxPathSplits,
       "usdIsisSysMaxLSPGenInt": usdIsisSysMaxLSPGenInt,
       "usdIsisSysOrigL1LSPBuffSize": usdIsisSysOrigL1LSPBuffSize,
       "usdIsisSysMaxAreaAddresses": usdIsisSysMaxAreaAddresses,
       "usdIsisSysMinL1LSPGenInt": usdIsisSysMinL1LSPGenInt,
       "usdIsisSysMinL2LSPGenInt": usdIsisSysMinL2LSPGenInt,
       "usdIsisSysPollESHelloRate": usdIsisSysPollESHelloRate,
       "usdIsisSysWaitTime": usdIsisSysWaitTime,
       "usdIsisSysOperState": usdIsisSysOperState,
       "usdIsisSysL1State": usdIsisSysL1State,
       "usdIsisSysCorrLSPs": usdIsisSysCorrLSPs,
       "usdIsisSysLSPL1DbaseOloads": usdIsisSysLSPL1DbaseOloads,
       "usdIsisSysManAddrDropFromAreas": usdIsisSysManAddrDropFromAreas,
       "usdIsisSysAttmptToExMaxSeqNums": usdIsisSysAttmptToExMaxSeqNums,
       "usdIsisSysSeqNumSkips": usdIsisSysSeqNumSkips,
       "usdIsisSysOwnLSPPurges": usdIsisSysOwnLSPPurges,
       "usdIsisSysIDFieldLenMismatches": usdIsisSysIDFieldLenMismatches,
       "usdIsisSysMaxAreaAddrMismatches": usdIsisSysMaxAreaAddrMismatches,
       "usdIsisSysOrigL2LSPBuffSize": usdIsisSysOrigL2LSPBuffSize,
       "usdIsisSysL2State": usdIsisSysL2State,
       "usdIsisSysLSPL2DbaseOloads": usdIsisSysLSPL2DbaseOloads,
       "usdIsisSysAuthFails": usdIsisSysAuthFails,
       "usdIsisSysLSPIgnoreErrors": usdIsisSysLSPIgnoreErrors,
       "usdIsisSysMaxAreaCheck": usdIsisSysMaxAreaCheck,
       "usdIsisSysSetOverloadBit": usdIsisSysSetOverloadBit,
       "usdIsisSysSetOverloadBitStartupDuration": usdIsisSysSetOverloadBitStartupDuration,
       "usdIsisSysMaxLspLifetime": usdIsisSysMaxLspLifetime,
       "usdIsisSysL1SpfInterval": usdIsisSysL1SpfInterval,
       "usdIsisSysL2SpfInterval": usdIsisSysL2SpfInterval,
       "usdIsisSysIshHoldTime": usdIsisSysIshHoldTime,
       "usdIsisSysIshConfigTimer": usdIsisSysIshConfigTimer,
       "usdIsisSysDistributeDomainWide": usdIsisSysDistributeDomainWide,
       "usdIsisSysDistance": usdIsisSysDistance,
       "usdIsisSysL1MetricStyle": usdIsisSysL1MetricStyle,
       "usdIsisSysL2MetricStyle": usdIsisSysL2MetricStyle,
       "usdIsisSysIsoRouteTag": usdIsisSysIsoRouteTag,
       "usdIsisSysMplsTeLevel": usdIsisSysMplsTeLevel,
       "usdIsisSysMplsTeRtrIdIfIndex": usdIsisSysMplsTeRtrIdIfIndex,
       "usdIsisManAreaAddrTable": usdIsisManAreaAddrTable,
       "usdIsisManAreaAddrEntry": usdIsisManAreaAddrEntry,
       "usdIsisManAreaAddrSysInstance": usdIsisManAreaAddrSysInstance,
       "usdIsisManAreaAddr": usdIsisManAreaAddr,
       "usdIsisManAreaAddrRowStatus": usdIsisManAreaAddrRowStatus,
       "usdIsisSysProtSuppTable": usdIsisSysProtSuppTable,
       "usdIsisSysProtSuppEntry": usdIsisSysProtSuppEntry,
       "usdIsisSysProtSuppSysInstance": usdIsisSysProtSuppSysInstance,
       "usdIsisSysProtSuppProtocol": usdIsisSysProtSuppProtocol,
       "usdIsisSysProtSuppRowStatus": usdIsisSysProtSuppRowStatus,
       "usdIsisSummAddrTable": usdIsisSummAddrTable,
       "usdIsisSummAddrEntry": usdIsisSummAddrEntry,
       "usdIsisSummAddrSysInstance": usdIsisSummAddrSysInstance,
       "usdIsisSummAddress": usdIsisSummAddress,
       "usdIsisSummAddrMask": usdIsisSummAddrMask,
       "usdIsisSummAddrRowStatus": usdIsisSummAddrRowStatus,
       "usdIsisSummAddrOperState": usdIsisSummAddrOperState,
       "usdIsisSummAddrDefaultMetric": usdIsisSummAddrDefaultMetric,
       "usdIsisSummAddrDelayMetric": usdIsisSummAddrDelayMetric,
       "usdIsisSummAddrExpenseMetric": usdIsisSummAddrExpenseMetric,
       "usdIsisSummAddrErrorMetric": usdIsisSummAddrErrorMetric,
       "usdIsisSummLevel": usdIsisSummLevel,
       "usdIsisSysHostNameTable": usdIsisSysHostNameTable,
       "usdIsisSysHostNameEntry": usdIsisSysHostNameEntry,
       "usdIsisSysHostNameSysInstance": usdIsisSysHostNameSysInstance,
       "usdIsisSysHostNameSysId": usdIsisSysHostNameSysId,
       "usdIsisSysHostNameAreaAddr": usdIsisSysHostNameAreaAddr,
       "usdIsisSysHostNameName": usdIsisSysHostNameName,
       "usdIsisSysHostNameType": usdIsisSysHostNameType,
       "usdIsisSysHostNameRowStatus": usdIsisSysHostNameRowStatus,
       "usdIsisSysAreaAuthenticationTable": usdIsisSysAreaAuthenticationTable,
       "usdIsisSysAreaAuthenticationEntry": usdIsisSysAreaAuthenticationEntry,
       "usdIsisSysAreaAuthenticationSysInstance": usdIsisSysAreaAuthenticationSysInstance,
       "usdIsisSysAreaAuthenticationKeyId": usdIsisSysAreaAuthenticationKeyId,
       "usdIsisSysAreaAuthenticationPwd": usdIsisSysAreaAuthenticationPwd,
       "usdIsisSysAreaAuthenticationKeyType": usdIsisSysAreaAuthenticationKeyType,
       "usdIsisSysAreaAuthenticationStartAcceptTime": usdIsisSysAreaAuthenticationStartAcceptTime,
       "usdIsisSysAreaAuthenticationStartGenerateTime": usdIsisSysAreaAuthenticationStartGenerateTime,
       "usdIsisSysAreaAuthenticationStopAcceptTime": usdIsisSysAreaAuthenticationStopAcceptTime,
       "usdIsisSysAreaAuthenticationStopGenerateTime": usdIsisSysAreaAuthenticationStopGenerateTime,
       "usdIsisSysAreaAuthenticationRowStatus": usdIsisSysAreaAuthenticationRowStatus,
       "usdIsisSysDomainAuthenticationTable": usdIsisSysDomainAuthenticationTable,
       "usdIsisSysDomainAuthenticationEntry": usdIsisSysDomainAuthenticationEntry,
       "usdIsisSysDomainAuthenticationSysInstance": usdIsisSysDomainAuthenticationSysInstance,
       "usdIsisSysDomainAuthenticationKeyId": usdIsisSysDomainAuthenticationKeyId,
       "usdIsisSysDomainAuthenticationPwd": usdIsisSysDomainAuthenticationPwd,
       "usdIsisSysDomainAuthenticationKeyType": usdIsisSysDomainAuthenticationKeyType,
       "usdIsisSysDomainAuthenticationStartAcceptTime": usdIsisSysDomainAuthenticationStartAcceptTime,
       "usdIsisSysDomainAuthenticationStartGenerateTime": usdIsisSysDomainAuthenticationStartGenerateTime,
       "usdIsisSysDomainAuthenticationStopAcceptTime": usdIsisSysDomainAuthenticationStopAcceptTime,
       "usdIsisSysDomainAuthenticationStopGenerateTime": usdIsisSysDomainAuthenticationStopGenerateTime,
       "usdIsisSysDomainAuthenticationRowStatus": usdIsisSysDomainAuthenticationRowStatus,
       "usdIsisCircuitGroup": usdIsisCircuitGroup,
       "usdIsisCircTable": usdIsisCircTable,
       "usdIsisCircEntry": usdIsisCircEntry,
       "usdIsisCircSysInstance": usdIsisCircSysInstance,
       "usdIsisCircIfIndex": usdIsisCircIfIndex,
       "usdIsisCircLocalID": usdIsisCircLocalID,
       "usdIsisCircOperState": usdIsisCircOperState,
       "usdIsisCircRowStatus": usdIsisCircRowStatus,
       "usdIsisCircType": usdIsisCircType,
       "usdIsisCircL1DefaultMetric": usdIsisCircL1DefaultMetric,
       "usdIsisCircL1DelayMetric": usdIsisCircL1DelayMetric,
       "usdIsisCircL1ExpenseMetric": usdIsisCircL1ExpenseMetric,
       "usdIsisCircL1ErrorMetric": usdIsisCircL1ErrorMetric,
       "usdIsisCircExtDomain": usdIsisCircExtDomain,
       "usdIsisCircAdjChanges": usdIsisCircAdjChanges,
       "usdIsisCircInitFails": usdIsisCircInitFails,
       "usdIsisCircRejAdjs": usdIsisCircRejAdjs,
       "usdIsisCircOutCtrlPDUs": usdIsisCircOutCtrlPDUs,
       "usdIsisCircInCtrlPDUs": usdIsisCircInCtrlPDUs,
       "usdIsisCircIDFieldLenMismatches": usdIsisCircIDFieldLenMismatches,
       "usdIsisCircL2DefaultMetric": usdIsisCircL2DefaultMetric,
       "usdIsisCircL2DelayMetric": usdIsisCircL2DelayMetric,
       "usdIsisCircL2ExpenseMetric": usdIsisCircL2ExpenseMetric,
       "usdIsisCircL2ErrorMetric": usdIsisCircL2ErrorMetric,
       "usdIsisCircManL2Only": usdIsisCircManL2Only,
       "usdIsisCircL1ISPriority": usdIsisCircL1ISPriority,
       "usdIsisCircL1CircID": usdIsisCircL1CircID,
       "usdIsisCircL1DesIS": usdIsisCircL1DesIS,
       "usdIsisCircLANL1DesISChanges": usdIsisCircLANL1DesISChanges,
       "usdIsisCircL2ISPriority": usdIsisCircL2ISPriority,
       "usdIsisCircL2CircID": usdIsisCircL2CircID,
       "usdIsisCircL2DesIS": usdIsisCircL2DesIS,
       "usdIsisCircLANL2DesISChanges": usdIsisCircLANL2DesISChanges,
       "usdIsisCircMCAddr": usdIsisCircMCAddr,
       "usdIsisCircPtToPtCircID": usdIsisCircPtToPtCircID,
       "usdIsisCircL1HelloTimer": usdIsisCircL1HelloTimer,
       "usdIsisCircL2HelloTimer": usdIsisCircL2HelloTimer,
       "usdIsisCircL1HelloMultiplier": usdIsisCircL1HelloMultiplier,
       "usdIsisCircL2HelloMultiplier": usdIsisCircL2HelloMultiplier,
       "usdIsisCircMinLSPTransInt": usdIsisCircMinLSPTransInt,
       "usdIsisCircMinLSPReTransInt": usdIsisCircMinLSPReTransInt,
       "usdIsisCircL1CSNPInterval": usdIsisCircL1CSNPInterval,
       "usdIsisCircL2CSNPInterval": usdIsisCircL2CSNPInterval,
       "usdIsisCircLSPThrottle": usdIsisCircLSPThrottle,
       "usdIsisCircMeshGroupEnabled": usdIsisCircMeshGroupEnabled,
       "usdIsisCircMeshGroup": usdIsisCircMeshGroup,
       "usdIsisCircLevel": usdIsisCircLevel,
       "usdIsisCircState": usdIsisCircState,
       "usdIsisSysL1CircAuthenticationTable": usdIsisSysL1CircAuthenticationTable,
       "usdIsisSysL1CircAuthenticationEntry": usdIsisSysL1CircAuthenticationEntry,
       "usdIsisSysL1CircAuthenticationSysInstance": usdIsisSysL1CircAuthenticationSysInstance,
       "usdIsisSysL1CircAuthenticationIfIndex": usdIsisSysL1CircAuthenticationIfIndex,
       "usdIsisSysL1CircAuthenticationKeyId": usdIsisSysL1CircAuthenticationKeyId,
       "usdIsisSysL1CircAuthenticationPwd": usdIsisSysL1CircAuthenticationPwd,
       "usdIsisSysL1CircAuthenticationKeyType": usdIsisSysL1CircAuthenticationKeyType,
       "usdIsisSysL1CircAuthenticationStartAcceptTime": usdIsisSysL1CircAuthenticationStartAcceptTime,
       "usdIsisSysL1CircAuthenticationStartGenerateTime": usdIsisSysL1CircAuthenticationStartGenerateTime,
       "usdIsisSysL1CircAuthenticationStopAcceptTime": usdIsisSysL1CircAuthenticationStopAcceptTime,
       "usdIsisSysL1CircAuthenticationStopGenerateTime": usdIsisSysL1CircAuthenticationStopGenerateTime,
       "usdIsisSysL1CircAuthenticationRowStatus": usdIsisSysL1CircAuthenticationRowStatus,
       "usdIsisSysL2CircAuthenticationTable": usdIsisSysL2CircAuthenticationTable,
       "usdIsisSysL2CircAuthenticationEntry": usdIsisSysL2CircAuthenticationEntry,
       "usdIsisSysL2CircAuthenticationSysInstance": usdIsisSysL2CircAuthenticationSysInstance,
       "usdIsisSysL2CircAuthenticationIfIndex": usdIsisSysL2CircAuthenticationIfIndex,
       "usdIsisSysL2CircAuthenticationKeyId": usdIsisSysL2CircAuthenticationKeyId,
       "usdIsisSysL2CircAuthenticationPwd": usdIsisSysL2CircAuthenticationPwd,
       "usdIsisSysL2CircAuthenticationKeyType": usdIsisSysL2CircAuthenticationKeyType,
       "usdIsisSysL2CircAuthenticationStartAcceptTime": usdIsisSysL2CircAuthenticationStartAcceptTime,
       "usdIsisSysL2CircAuthenticationStartGenerateTime": usdIsisSysL2CircAuthenticationStartGenerateTime,
       "usdIsisSysL2CircAuthenticationStopAcceptTime": usdIsisSysL2CircAuthenticationStopAcceptTime,
       "usdIsisSysL2CircAuthenticationStopGenerateTime": usdIsisSysL2CircAuthenticationStopGenerateTime,
       "usdIsisSysL2CircAuthenticationRowStatus": usdIsisSysL2CircAuthenticationRowStatus,
       "usdIsisTrapGroup": usdIsisTrapGroup,
       "usdIsisConformance": usdIsisConformance,
       "usdIsisCompliances": usdIsisCompliances,
       "usdIsisCompliance": usdIsisCompliance,
       "usdIsisCompliance2": usdIsisCompliance2,
       "usdIsisCompliance3": usdIsisCompliance3,
       "usdIsisMIBGroups": usdIsisMIBGroups,
       "usdIsisSystemMgmtGroup": usdIsisSystemMgmtGroup,
       "usdIsisCircuitMgmtGroup": usdIsisCircuitMgmtGroup,
       "usdIsisCircuitMgmtGroup2": usdIsisCircuitMgmtGroup2,
       "usdIsisSystemMgmtGroup2": usdIsisSystemMgmtGroup2}
)
