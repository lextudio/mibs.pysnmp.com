# SNMP MIB module (Juniper-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:38 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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


# MODULE-IDENTITY

juniIsisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38)
)
juniIsisMIB.setRevisions(
        ("2006-12-13 13:30",
         "2006-03-01 14:30",
         "2006-03-01 14:30",
         "2005-12-26 14:30",
         "2005-10-21 08:10",
         "2005-03-29 14:30",
         "2005-01-17 08:10",
         "2005-01-06 05:04",
         "2004-11-02 05:04",
         "2004-10-18 14:14",
         "2002-09-16 21:44",
         "2001-12-10 21:29",
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
        ValueSizeConstraint(6, 6),
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



class JuniDefaultMetric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
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

_JuniIsisObjects_ObjectIdentity = ObjectIdentity
juniIsisObjects = _JuniIsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1)
)
_JuniIsisSystemGroup_ObjectIdentity = ObjectIdentity
juniIsisSystemGroup = _JuniIsisSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1)
)
_JuniIsisSysTable_Object = MibTable
juniIsisSysTable = _JuniIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIsisSysTable.setStatus("current")
_JuniIsisSysEntry_Object = MibTableRow
juniIsisSysEntry = _JuniIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1)
)
juniIsisSysEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysInstance"),
)
if mibBuilder.loadTexts:
    juniIsisSysEntry.setStatus("current")


class _JuniIsisSysInstance_Type(Integer32):
    """Custom type juniIsisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysInstance_Object = MibTableColumn
juniIsisSysInstance = _JuniIsisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 1),
    _JuniIsisSysInstance_Type()
)
juniIsisSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysInstance.setStatus("current")


class _JuniIsisSysVersion_Type(DisplayString):
    """Custom type juniIsisSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JuniIsisSysVersion_Type.__name__ = "DisplayString"
_JuniIsisSysVersion_Object = MibTableColumn
juniIsisSysVersion = _JuniIsisSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 2),
    _JuniIsisSysVersion_Type()
)
juniIsisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysVersion.setStatus("current")


class _JuniIsisSysType_Type(Integer32):
    """Custom type juniIsisSysType based on Integer32"""
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


_JuniIsisSysType_Type.__name__ = "Integer32"
_JuniIsisSysType_Object = MibTableColumn
juniIsisSysType = _JuniIsisSysType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 3),
    _JuniIsisSysType_Type()
)
juniIsisSysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysType.setStatus("current")
_JuniIsisSysID_Type = SystemID
_JuniIsisSysID_Object = MibTableColumn
juniIsisSysID = _JuniIsisSysID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 4),
    _JuniIsisSysID_Type()
)
juniIsisSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysID.setStatus("current")


class _JuniIsisSysMaxPathSplits_Type(Integer32):
    """Custom type juniIsisSysMaxPathSplits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_JuniIsisSysMaxPathSplits_Type.__name__ = "Integer32"
_JuniIsisSysMaxPathSplits_Object = MibTableColumn
juniIsisSysMaxPathSplits = _JuniIsisSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 5),
    _JuniIsisSysMaxPathSplits_Type()
)
juniIsisSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMaxPathSplits.setStatus("current")


class _JuniIsisSysMaxLSPGenInt_Type(Integer32):
    """Custom type juniIsisSysMaxLSPGenInt based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysMaxLSPGenInt_Type.__name__ = "Integer32"
_JuniIsisSysMaxLSPGenInt_Object = MibTableColumn
juniIsisSysMaxLSPGenInt = _JuniIsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 6),
    _JuniIsisSysMaxLSPGenInt_Type()
)
juniIsisSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysMaxLSPGenInt.setUnits("seconds")


class _JuniIsisSysOrigLSPBuffSize_Type(LSPBuffSize):
    """Custom type juniIsisSysOrigLSPBuffSize based on LSPBuffSize"""
    defaultValue = 1497


_JuniIsisSysOrigLSPBuffSize_Object = MibTableColumn
juniIsisSysOrigLSPBuffSize = _JuniIsisSysOrigLSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 7),
    _JuniIsisSysOrigLSPBuffSize_Type()
)
juniIsisSysOrigLSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysOrigLSPBuffSize.setStatus("current")


class _JuniIsisSysMaxAreaAddresses_Type(Integer32):
    """Custom type juniIsisSysMaxAreaAddresses based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_JuniIsisSysMaxAreaAddresses_Type.__name__ = "Integer32"
_JuniIsisSysMaxAreaAddresses_Object = MibTableColumn
juniIsisSysMaxAreaAddresses = _JuniIsisSysMaxAreaAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 8),
    _JuniIsisSysMaxAreaAddresses_Type()
)
juniIsisSysMaxAreaAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysMaxAreaAddresses.setStatus("current")


class _JuniIsisSysMinL1LSPGenInt_Type(Integer32):
    """Custom type juniIsisSysMinL1LSPGenInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_JuniIsisSysMinL1LSPGenInt_Type.__name__ = "Integer32"
_JuniIsisSysMinL1LSPGenInt_Object = MibTableColumn
juniIsisSysMinL1LSPGenInt = _JuniIsisSysMinL1LSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 9),
    _JuniIsisSysMinL1LSPGenInt_Type()
)
juniIsisSysMinL1LSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMinL1LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysMinL1LSPGenInt.setUnits("seconds")


class _JuniIsisSysMinL2LSPGenInt_Type(Integer32):
    """Custom type juniIsisSysMinL2LSPGenInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_JuniIsisSysMinL2LSPGenInt_Type.__name__ = "Integer32"
_JuniIsisSysMinL2LSPGenInt_Object = MibTableColumn
juniIsisSysMinL2LSPGenInt = _JuniIsisSysMinL2LSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 10),
    _JuniIsisSysMinL2LSPGenInt_Type()
)
juniIsisSysMinL2LSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMinL2LSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysMinL2LSPGenInt.setUnits("seconds")


class _JuniIsisSysPollESHelloRate_Type(Integer32):
    """Custom type juniIsisSysPollESHelloRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysPollESHelloRate_Type.__name__ = "Integer32"
_JuniIsisSysPollESHelloRate_Object = MibTableColumn
juniIsisSysPollESHelloRate = _JuniIsisSysPollESHelloRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 11),
    _JuniIsisSysPollESHelloRate_Type()
)
juniIsisSysPollESHelloRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysPollESHelloRate.setUnits("seconds")


class _JuniIsisSysWaitTime_Type(Integer32):
    """Custom type juniIsisSysWaitTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysWaitTime_Type.__name__ = "Integer32"
_JuniIsisSysWaitTime_Object = MibTableColumn
juniIsisSysWaitTime = _JuniIsisSysWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 12),
    _JuniIsisSysWaitTime_Type()
)
juniIsisSysWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysWaitTime.setUnits("seconds")


class _JuniIsisSysOperState_Type(OperState):
    """Custom type juniIsisSysOperState based on OperState"""


_JuniIsisSysOperState_Object = MibTableColumn
juniIsisSysOperState = _JuniIsisSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 13),
    _JuniIsisSysOperState_Type()
)
juniIsisSysOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysOperState.setStatus("current")
_JuniIsisSysL1State_Type = LevelState
_JuniIsisSysL1State_Object = MibTableColumn
juniIsisSysL1State = _JuniIsisSysL1State_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 14),
    _JuniIsisSysL1State_Type()
)
juniIsisSysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysL1State.setStatus("current")
_JuniIsisSysCorrLSPs_Type = Counter32
_JuniIsisSysCorrLSPs_Object = MibTableColumn
juniIsisSysCorrLSPs = _JuniIsisSysCorrLSPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 15),
    _JuniIsisSysCorrLSPs_Type()
)
juniIsisSysCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysCorrLSPs.setStatus("current")
_JuniIsisSysLSPL1DbaseOloads_Type = Counter32
_JuniIsisSysLSPL1DbaseOloads_Object = MibTableColumn
juniIsisSysLSPL1DbaseOloads = _JuniIsisSysLSPL1DbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 16),
    _JuniIsisSysLSPL1DbaseOloads_Type()
)
juniIsisSysLSPL1DbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysLSPL1DbaseOloads.setStatus("current")
_JuniIsisSysManAddrDropFromAreas_Type = Counter32
_JuniIsisSysManAddrDropFromAreas_Object = MibTableColumn
juniIsisSysManAddrDropFromAreas = _JuniIsisSysManAddrDropFromAreas_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 17),
    _JuniIsisSysManAddrDropFromAreas_Type()
)
juniIsisSysManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysManAddrDropFromAreas.setStatus("current")
_JuniIsisSysAttmptToExMaxSeqNums_Type = Counter32
_JuniIsisSysAttmptToExMaxSeqNums_Object = MibTableColumn
juniIsisSysAttmptToExMaxSeqNums = _JuniIsisSysAttmptToExMaxSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 18),
    _JuniIsisSysAttmptToExMaxSeqNums_Type()
)
juniIsisSysAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysAttmptToExMaxSeqNums.setStatus("current")
_JuniIsisSysSeqNumSkips_Type = Counter32
_JuniIsisSysSeqNumSkips_Object = MibTableColumn
juniIsisSysSeqNumSkips = _JuniIsisSysSeqNumSkips_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 19),
    _JuniIsisSysSeqNumSkips_Type()
)
juniIsisSysSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysSeqNumSkips.setStatus("current")
_JuniIsisSysOwnLSPPurges_Type = Counter32
_JuniIsisSysOwnLSPPurges_Object = MibTableColumn
juniIsisSysOwnLSPPurges = _JuniIsisSysOwnLSPPurges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 20),
    _JuniIsisSysOwnLSPPurges_Type()
)
juniIsisSysOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysOwnLSPPurges.setStatus("current")
_JuniIsisSysIDFieldLenMismatches_Type = Counter32
_JuniIsisSysIDFieldLenMismatches_Object = MibTableColumn
juniIsisSysIDFieldLenMismatches = _JuniIsisSysIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 21),
    _JuniIsisSysIDFieldLenMismatches_Type()
)
juniIsisSysIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysIDFieldLenMismatches.setStatus("current")
_JuniIsisSysMaxAreaAddrMismatches_Type = Counter32
_JuniIsisSysMaxAreaAddrMismatches_Object = MibTableColumn
juniIsisSysMaxAreaAddrMismatches = _JuniIsisSysMaxAreaAddrMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 22),
    _JuniIsisSysMaxAreaAddrMismatches_Type()
)
juniIsisSysMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysMaxAreaAddrMismatches.setStatus("current")


class _JuniIsisSysOrigL2LSPBuffSize_Type(LSPBuffSize):
    """Custom type juniIsisSysOrigL2LSPBuffSize based on LSPBuffSize"""
    defaultValue = 1497


_JuniIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
juniIsisSysOrigL2LSPBuffSize = _JuniIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 23),
    _JuniIsisSysOrigL2LSPBuffSize_Type()
)
juniIsisSysOrigL2LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysOrigL2LSPBuffSize.setStatus("obsolete")
_JuniIsisSysL2State_Type = LevelState
_JuniIsisSysL2State_Object = MibTableColumn
juniIsisSysL2State = _JuniIsisSysL2State_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 24),
    _JuniIsisSysL2State_Type()
)
juniIsisSysL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysL2State.setStatus("current")
_JuniIsisSysLSPL2DbaseOloads_Type = Counter32
_JuniIsisSysLSPL2DbaseOloads_Object = MibTableColumn
juniIsisSysLSPL2DbaseOloads = _JuniIsisSysLSPL2DbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 25),
    _JuniIsisSysLSPL2DbaseOloads_Type()
)
juniIsisSysLSPL2DbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysLSPL2DbaseOloads.setStatus("current")
_JuniIsisSysAuthFails_Type = Counter32
_JuniIsisSysAuthFails_Object = MibTableColumn
juniIsisSysAuthFails = _JuniIsisSysAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 26),
    _JuniIsisSysAuthFails_Type()
)
juniIsisSysAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysAuthFails.setStatus("current")


class _JuniIsisSysLSPIgnoreErrors_Type(TruthValue):
    """Custom type juniIsisSysLSPIgnoreErrors based on TruthValue"""


_JuniIsisSysLSPIgnoreErrors_Object = MibTableColumn
juniIsisSysLSPIgnoreErrors = _JuniIsisSysLSPIgnoreErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 27),
    _JuniIsisSysLSPIgnoreErrors_Type()
)
juniIsisSysLSPIgnoreErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysLSPIgnoreErrors.setStatus("current")


class _JuniIsisSysMaxAreaCheck_Type(TruthValue):
    """Custom type juniIsisSysMaxAreaCheck based on TruthValue"""


_JuniIsisSysMaxAreaCheck_Object = MibTableColumn
juniIsisSysMaxAreaCheck = _JuniIsisSysMaxAreaCheck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 28),
    _JuniIsisSysMaxAreaCheck_Type()
)
juniIsisSysMaxAreaCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysMaxAreaCheck.setStatus("current")


class _JuniIsisSysSetOverloadBit_Type(TruthValue):
    """Custom type juniIsisSysSetOverloadBit based on TruthValue"""


_JuniIsisSysSetOverloadBit_Object = MibTableColumn
juniIsisSysSetOverloadBit = _JuniIsisSysSetOverloadBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 29),
    _JuniIsisSysSetOverloadBit_Type()
)
juniIsisSysSetOverloadBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysSetOverloadBit.setStatus("current")


class _JuniIsisSysSetOverloadBitStartupDuration_Type(Integer32):
    """Custom type juniIsisSysSetOverloadBitStartupDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_JuniIsisSysSetOverloadBitStartupDuration_Type.__name__ = "Integer32"
_JuniIsisSysSetOverloadBitStartupDuration_Object = MibTableColumn
juniIsisSysSetOverloadBitStartupDuration = _JuniIsisSysSetOverloadBitStartupDuration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 30),
    _JuniIsisSysSetOverloadBitStartupDuration_Type()
)
juniIsisSysSetOverloadBitStartupDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysSetOverloadBitStartupDuration.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysSetOverloadBitStartupDuration.setUnits("seconds")


class _JuniIsisSysMaxLspLifetime_Type(Integer32):
    """Custom type juniIsisSysMaxLspLifetime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysMaxLspLifetime_Type.__name__ = "Integer32"
_JuniIsisSysMaxLspLifetime_Object = MibTableColumn
juniIsisSysMaxLspLifetime = _JuniIsisSysMaxLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 31),
    _JuniIsisSysMaxLspLifetime_Type()
)
juniIsisSysMaxLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMaxLspLifetime.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysMaxLspLifetime.setUnits("seconds")


class _JuniIsisSysL1SpfInterval_Type(Integer32):
    """Custom type juniIsisSysL1SpfInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_JuniIsisSysL1SpfInterval_Type.__name__ = "Integer32"
_JuniIsisSysL1SpfInterval_Object = MibTableColumn
juniIsisSysL1SpfInterval = _JuniIsisSysL1SpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 32),
    _JuniIsisSysL1SpfInterval_Type()
)
juniIsisSysL1SpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1SpfInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysL1SpfInterval.setUnits("seconds")


class _JuniIsisSysL2SpfInterval_Type(Integer32):
    """Custom type juniIsisSysL2SpfInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_JuniIsisSysL2SpfInterval_Type.__name__ = "Integer32"
_JuniIsisSysL2SpfInterval_Object = MibTableColumn
juniIsisSysL2SpfInterval = _JuniIsisSysL2SpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 33),
    _JuniIsisSysL2SpfInterval_Type()
)
juniIsisSysL2SpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2SpfInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisSysL2SpfInterval.setUnits("seconds")


class _JuniIsisSysIshHoldTime_Type(Integer32):
    """Custom type juniIsisSysIshHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysIshHoldTime_Type.__name__ = "Integer32"
_JuniIsisSysIshHoldTime_Object = MibTableColumn
juniIsisSysIshHoldTime = _JuniIsisSysIshHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 34),
    _JuniIsisSysIshHoldTime_Type()
)
juniIsisSysIshHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysIshHoldTime.setStatus("current")


class _JuniIsisSysIshConfigTimer_Type(Integer32):
    """Custom type juniIsisSysIshConfigTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisSysIshConfigTimer_Type.__name__ = "Integer32"
_JuniIsisSysIshConfigTimer_Object = MibTableColumn
juniIsisSysIshConfigTimer = _JuniIsisSysIshConfigTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 35),
    _JuniIsisSysIshConfigTimer_Type()
)
juniIsisSysIshConfigTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysIshConfigTimer.setStatus("current")


class _JuniIsisSysDistributeDomainWide_Type(TruthValue):
    """Custom type juniIsisSysDistributeDomainWide based on TruthValue"""


_JuniIsisSysDistributeDomainWide_Object = MibTableColumn
juniIsisSysDistributeDomainWide = _JuniIsisSysDistributeDomainWide_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 36),
    _JuniIsisSysDistributeDomainWide_Type()
)
juniIsisSysDistributeDomainWide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDistributeDomainWide.setStatus("current")


class _JuniIsisSysDistance_Type(Integer32):
    """Custom type juniIsisSysDistance based on Integer32"""
    defaultValue = 115

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniIsisSysDistance_Type.__name__ = "Integer32"
_JuniIsisSysDistance_Object = MibTableColumn
juniIsisSysDistance = _JuniIsisSysDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 37),
    _JuniIsisSysDistance_Type()
)
juniIsisSysDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDistance.setStatus("current")


class _JuniIsisSysL1MetricStyle_Type(Integer32):
    """Custom type juniIsisSysL1MetricStyle based on Integer32"""
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
        *(("juniIsisMetricStyleNarrow", 2),
          ("juniIsisMetricStyleNarrowTransition", 3),
          ("juniIsisMetricStyleTransition", 4),
          ("juniIsisMetricStyleWide", 5),
          ("juniIsisMetricStyleWideTransition", 6))
    )


_JuniIsisSysL1MetricStyle_Type.__name__ = "Integer32"
_JuniIsisSysL1MetricStyle_Object = MibTableColumn
juniIsisSysL1MetricStyle = _JuniIsisSysL1MetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 38),
    _JuniIsisSysL1MetricStyle_Type()
)
juniIsisSysL1MetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1MetricStyle.setStatus("current")


class _JuniIsisSysL2MetricStyle_Type(Integer32):
    """Custom type juniIsisSysL2MetricStyle based on Integer32"""
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
        *(("juniIsisMetricStyleNarrow", 2),
          ("juniIsisMetricStyleNarrowTransition", 3),
          ("juniIsisMetricStyleTransition", 4),
          ("juniIsisMetricStyleWide", 5),
          ("juniIsisMetricStyleWideTransition", 6))
    )


_JuniIsisSysL2MetricStyle_Type.__name__ = "Integer32"
_JuniIsisSysL2MetricStyle_Object = MibTableColumn
juniIsisSysL2MetricStyle = _JuniIsisSysL2MetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 39),
    _JuniIsisSysL2MetricStyle_Type()
)
juniIsisSysL2MetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2MetricStyle.setStatus("current")


class _JuniIsisSysIsoRouteTag_Type(OctetString):
    """Custom type juniIsisSysIsoRouteTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_JuniIsisSysIsoRouteTag_Type.__name__ = "OctetString"
_JuniIsisSysIsoRouteTag_Object = MibTableColumn
juniIsisSysIsoRouteTag = _JuniIsisSysIsoRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 40),
    _JuniIsisSysIsoRouteTag_Type()
)
juniIsisSysIsoRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysIsoRouteTag.setStatus("current")


class _JuniIsisSysMplsTeLevel_Type(Integer32):
    """Custom type juniIsisSysMplsTeLevel based on Integer32"""
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


_JuniIsisSysMplsTeLevel_Type.__name__ = "Integer32"
_JuniIsisSysMplsTeLevel_Object = MibTableColumn
juniIsisSysMplsTeLevel = _JuniIsisSysMplsTeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 41),
    _JuniIsisSysMplsTeLevel_Type()
)
juniIsisSysMplsTeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMplsTeLevel.setStatus("current")
_JuniIsisSysMplsTeRtrIdIfIndex_Type = InterfaceIndexOrZero
_JuniIsisSysMplsTeRtrIdIfIndex_Object = MibTableColumn
juniIsisSysMplsTeRtrIdIfIndex = _JuniIsisSysMplsTeRtrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 42),
    _JuniIsisSysMplsTeRtrIdIfIndex_Type()
)
juniIsisSysMplsTeRtrIdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMplsTeRtrIdIfIndex.setStatus("current")
_JuniIsisSysMplsTeSpfUseAnyBestPath_Type = TruthValue
_JuniIsisSysMplsTeSpfUseAnyBestPath_Object = MibTableColumn
juniIsisSysMplsTeSpfUseAnyBestPath = _JuniIsisSysMplsTeSpfUseAnyBestPath_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 43),
    _JuniIsisSysMplsTeSpfUseAnyBestPath_Type()
)
juniIsisSysMplsTeSpfUseAnyBestPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysMplsTeSpfUseAnyBestPath.setStatus("current")
_JuniIsisSysReferenceBandwidth_Type = Gauge32
_JuniIsisSysReferenceBandwidth_Object = MibTableColumn
juniIsisSysReferenceBandwidth = _JuniIsisSysReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 44),
    _JuniIsisSysReferenceBandwidth_Type()
)
juniIsisSysReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysReferenceBandwidth.setStatus("current")


class _JuniIsisSysHighReferenceBandwidth_Type(Gauge32):
    """Custom type juniIsisSysHighReferenceBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_JuniIsisSysHighReferenceBandwidth_Type.__name__ = "Gauge32"
_JuniIsisSysHighReferenceBandwidth_Object = MibTableColumn
juniIsisSysHighReferenceBandwidth = _JuniIsisSysHighReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 1, 1, 45),
    _JuniIsisSysHighReferenceBandwidth_Type()
)
juniIsisSysHighReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysHighReferenceBandwidth.setStatus("current")
_JuniIsisManAreaAddrTable_Object = MibTable
juniIsisManAreaAddrTable = _JuniIsisManAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniIsisManAreaAddrTable.setStatus("current")
_JuniIsisManAreaAddrEntry_Object = MibTableRow
juniIsisManAreaAddrEntry = _JuniIsisManAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1)
)
juniIsisManAreaAddrEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisManAreaAddrSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisManAreaAddr"),
)
if mibBuilder.loadTexts:
    juniIsisManAreaAddrEntry.setStatus("current")


class _JuniIsisManAreaAddrSysInstance_Type(Integer32):
    """Custom type juniIsisManAreaAddrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisManAreaAddrSysInstance_Type.__name__ = "Integer32"
_JuniIsisManAreaAddrSysInstance_Object = MibTableColumn
juniIsisManAreaAddrSysInstance = _JuniIsisManAreaAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 1),
    _JuniIsisManAreaAddrSysInstance_Type()
)
juniIsisManAreaAddrSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisManAreaAddrSysInstance.setStatus("current")
_JuniIsisManAreaAddr_Type = OSINSAddress
_JuniIsisManAreaAddr_Object = MibTableColumn
juniIsisManAreaAddr = _JuniIsisManAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 2),
    _JuniIsisManAreaAddr_Type()
)
juniIsisManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisManAreaAddr.setStatus("current")


class _JuniIsisManAreaAddrRowStatus_Type(RowStatus):
    """Custom type juniIsisManAreaAddrRowStatus based on RowStatus"""


_JuniIsisManAreaAddrRowStatus_Object = MibTableColumn
juniIsisManAreaAddrRowStatus = _JuniIsisManAreaAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 2, 1, 3),
    _JuniIsisManAreaAddrRowStatus_Type()
)
juniIsisManAreaAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisManAreaAddrRowStatus.setStatus("current")
_JuniIsisSysProtSuppTable_Object = MibTable
juniIsisSysProtSuppTable = _JuniIsisSysProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniIsisSysProtSuppTable.setStatus("current")
_JuniIsisSysProtSuppEntry_Object = MibTableRow
juniIsisSysProtSuppEntry = _JuniIsisSysProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1)
)
juniIsisSysProtSuppEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysProtSuppSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    juniIsisSysProtSuppEntry.setStatus("current")


class _JuniIsisSysProtSuppSysInstance_Type(Integer32):
    """Custom type juniIsisSysProtSuppSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysProtSuppSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysProtSuppSysInstance_Object = MibTableColumn
juniIsisSysProtSuppSysInstance = _JuniIsisSysProtSuppSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 1),
    _JuniIsisSysProtSuppSysInstance_Type()
)
juniIsisSysProtSuppSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysProtSuppSysInstance.setStatus("current")
_JuniIsisSysProtSuppProtocol_Type = SupportedProtocol
_JuniIsisSysProtSuppProtocol_Object = MibTableColumn
juniIsisSysProtSuppProtocol = _JuniIsisSysProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 2),
    _JuniIsisSysProtSuppProtocol_Type()
)
juniIsisSysProtSuppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysProtSuppProtocol.setStatus("current")


class _JuniIsisSysProtSuppRowStatus_Type(RowStatus):
    """Custom type juniIsisSysProtSuppRowStatus based on RowStatus"""


_JuniIsisSysProtSuppRowStatus_Object = MibTableColumn
juniIsisSysProtSuppRowStatus = _JuniIsisSysProtSuppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 3, 1, 3),
    _JuniIsisSysProtSuppRowStatus_Type()
)
juniIsisSysProtSuppRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysProtSuppRowStatus.setStatus("current")
_JuniIsisSummAddrTable_Object = MibTable
juniIsisSummAddrTable = _JuniIsisSummAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniIsisSummAddrTable.setStatus("current")
_JuniIsisSummAddrEntry_Object = MibTableRow
juniIsisSummAddrEntry = _JuniIsisSummAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1)
)
juniIsisSummAddrEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSummAddrSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSummAddress"),
    (0, "Juniper-ISIS-MIB", "juniIsisSummAddrMask"),
)
if mibBuilder.loadTexts:
    juniIsisSummAddrEntry.setStatus("current")


class _JuniIsisSummAddrSysInstance_Type(Integer32):
    """Custom type juniIsisSummAddrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSummAddrSysInstance_Type.__name__ = "Integer32"
_JuniIsisSummAddrSysInstance_Object = MibTableColumn
juniIsisSummAddrSysInstance = _JuniIsisSummAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 1),
    _JuniIsisSummAddrSysInstance_Type()
)
juniIsisSummAddrSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSummAddrSysInstance.setStatus("current")
_JuniIsisSummAddress_Type = IpAddress
_JuniIsisSummAddress_Object = MibTableColumn
juniIsisSummAddress = _JuniIsisSummAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 2),
    _JuniIsisSummAddress_Type()
)
juniIsisSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSummAddress.setStatus("current")
_JuniIsisSummAddrMask_Type = IpAddress
_JuniIsisSummAddrMask_Object = MibTableColumn
juniIsisSummAddrMask = _JuniIsisSummAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 3),
    _JuniIsisSummAddrMask_Type()
)
juniIsisSummAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSummAddrMask.setStatus("current")
_JuniIsisSummAddrRowStatus_Type = RowStatus
_JuniIsisSummAddrRowStatus_Object = MibTableColumn
juniIsisSummAddrRowStatus = _JuniIsisSummAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 4),
    _JuniIsisSummAddrRowStatus_Type()
)
juniIsisSummAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisSummAddrRowStatus.setStatus("current")
_JuniIsisSummAddrOperState_Type = OperState
_JuniIsisSummAddrOperState_Object = MibTableColumn
juniIsisSummAddrOperState = _JuniIsisSummAddrOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 5),
    _JuniIsisSummAddrOperState_Type()
)
juniIsisSummAddrOperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisSummAddrOperState.setStatus("current")


class _JuniIsisSummAddrDefaultMetric_Type(Integer32):
    """Custom type juniIsisSummAddrDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_JuniIsisSummAddrDefaultMetric_Type.__name__ = "Integer32"
_JuniIsisSummAddrDefaultMetric_Object = MibTableColumn
juniIsisSummAddrDefaultMetric = _JuniIsisSummAddrDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 6),
    _JuniIsisSummAddrDefaultMetric_Type()
)
juniIsisSummAddrDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisSummAddrDefaultMetric.setStatus("current")
_JuniIsisSummAddrDelayMetric_Type = OtherMetric
_JuniIsisSummAddrDelayMetric_Object = MibTableColumn
juniIsisSummAddrDelayMetric = _JuniIsisSummAddrDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 7),
    _JuniIsisSummAddrDelayMetric_Type()
)
juniIsisSummAddrDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSummAddrDelayMetric.setStatus("current")
_JuniIsisSummAddrExpenseMetric_Type = OtherMetric
_JuniIsisSummAddrExpenseMetric_Object = MibTableColumn
juniIsisSummAddrExpenseMetric = _JuniIsisSummAddrExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 8),
    _JuniIsisSummAddrExpenseMetric_Type()
)
juniIsisSummAddrExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSummAddrExpenseMetric.setStatus("current")
_JuniIsisSummAddrErrorMetric_Type = OtherMetric
_JuniIsisSummAddrErrorMetric_Object = MibTableColumn
juniIsisSummAddrErrorMetric = _JuniIsisSummAddrErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 9),
    _JuniIsisSummAddrErrorMetric_Type()
)
juniIsisSummAddrErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSummAddrErrorMetric.setStatus("current")


class _JuniIsisSummLevel_Type(Integer32):
    """Custom type juniIsisSummLevel based on Integer32"""
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


_JuniIsisSummLevel_Type.__name__ = "Integer32"
_JuniIsisSummLevel_Object = MibTableColumn
juniIsisSummLevel = _JuniIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 4, 1, 10),
    _JuniIsisSummLevel_Type()
)
juniIsisSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisSummLevel.setStatus("current")
_JuniIsisSysHostNameTable_Object = MibTable
juniIsisSysHostNameTable = _JuniIsisSysHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniIsisSysHostNameTable.setStatus("current")
_JuniIsisSysHostNameEntry_Object = MibTableRow
juniIsisSysHostNameEntry = _JuniIsisSysHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1)
)
juniIsisSysHostNameEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysHostNameSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysHostNameSysId"),
)
if mibBuilder.loadTexts:
    juniIsisSysHostNameEntry.setStatus("current")


class _JuniIsisSysHostNameSysInstance_Type(Integer32):
    """Custom type juniIsisSysHostNameSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysHostNameSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysHostNameSysInstance_Object = MibTableColumn
juniIsisSysHostNameSysInstance = _JuniIsisSysHostNameSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 1),
    _JuniIsisSysHostNameSysInstance_Type()
)
juniIsisSysHostNameSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysHostNameSysInstance.setStatus("current")
_JuniIsisSysHostNameSysId_Type = SystemID
_JuniIsisSysHostNameSysId_Object = MibTableColumn
juniIsisSysHostNameSysId = _JuniIsisSysHostNameSysId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 2),
    _JuniIsisSysHostNameSysId_Type()
)
juniIsisSysHostNameSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysHostNameSysId.setStatus("current")
_JuniIsisSysHostNameAreaAddr_Type = OSINSAddress
_JuniIsisSysHostNameAreaAddr_Object = MibTableColumn
juniIsisSysHostNameAreaAddr = _JuniIsisSysHostNameAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 3),
    _JuniIsisSysHostNameAreaAddr_Type()
)
juniIsisSysHostNameAreaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisSysHostNameAreaAddr.setStatus("current")


class _JuniIsisSysHostNameName_Type(OctetString):
    """Custom type juniIsisSysHostNameName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniIsisSysHostNameName_Type.__name__ = "OctetString"
_JuniIsisSysHostNameName_Object = MibTableColumn
juniIsisSysHostNameName = _JuniIsisSysHostNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 4),
    _JuniIsisSysHostNameName_Type()
)
juniIsisSysHostNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysHostNameName.setStatus("current")


class _JuniIsisSysHostNameType_Type(Integer32):
    """Custom type juniIsisSysHostNameType based on Integer32"""
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


_JuniIsisSysHostNameType_Type.__name__ = "Integer32"
_JuniIsisSysHostNameType_Object = MibTableColumn
juniIsisSysHostNameType = _JuniIsisSysHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 5),
    _JuniIsisSysHostNameType_Type()
)
juniIsisSysHostNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisSysHostNameType.setStatus("current")
_JuniIsisSysHostNameRowStatus_Type = RowStatus
_JuniIsisSysHostNameRowStatus_Object = MibTableColumn
juniIsisSysHostNameRowStatus = _JuniIsisSysHostNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 5, 1, 6),
    _JuniIsisSysHostNameRowStatus_Type()
)
juniIsisSysHostNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysHostNameRowStatus.setStatus("current")
_JuniIsisSysAreaAuthenticationTable_Object = MibTable
juniIsisSysAreaAuthenticationTable = _JuniIsisSysAreaAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6)
)
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationTable.setStatus("current")
_JuniIsisSysAreaAuthenticationEntry_Object = MibTableRow
juniIsisSysAreaAuthenticationEntry = _JuniIsisSysAreaAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1)
)
juniIsisSysAreaAuthenticationEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationEntry.setStatus("current")


class _JuniIsisSysAreaAuthenticationSysInstance_Type(Integer32):
    """Custom type juniIsisSysAreaAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysAreaAuthenticationSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysAreaAuthenticationSysInstance_Object = MibTableColumn
juniIsisSysAreaAuthenticationSysInstance = _JuniIsisSysAreaAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 1),
    _JuniIsisSysAreaAuthenticationSysInstance_Type()
)
juniIsisSysAreaAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationSysInstance.setStatus("current")


class _JuniIsisSysAreaAuthenticationKeyId_Type(Integer32):
    """Custom type juniIsisSysAreaAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIsisSysAreaAuthenticationKeyId_Type.__name__ = "Integer32"
_JuniIsisSysAreaAuthenticationKeyId_Object = MibTableColumn
juniIsisSysAreaAuthenticationKeyId = _JuniIsisSysAreaAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 2),
    _JuniIsisSysAreaAuthenticationKeyId_Type()
)
juniIsisSysAreaAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationKeyId.setStatus("current")


class _JuniIsisSysAreaAuthenticationPwd_Type(OctetString):
    """Custom type juniIsisSysAreaAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniIsisSysAreaAuthenticationPwd_Type.__name__ = "OctetString"
_JuniIsisSysAreaAuthenticationPwd_Object = MibTableColumn
juniIsisSysAreaAuthenticationPwd = _JuniIsisSysAreaAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 3),
    _JuniIsisSysAreaAuthenticationPwd_Type()
)
juniIsisSysAreaAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationPwd.setStatus("current")


class _JuniIsisSysAreaAuthenticationKeyType_Type(Integer32):
    """Custom type juniIsisSysAreaAuthenticationKeyType based on Integer32"""
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


_JuniIsisSysAreaAuthenticationKeyType_Type.__name__ = "Integer32"
_JuniIsisSysAreaAuthenticationKeyType_Object = MibTableColumn
juniIsisSysAreaAuthenticationKeyType = _JuniIsisSysAreaAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 4),
    _JuniIsisSysAreaAuthenticationKeyType_Type()
)
juniIsisSysAreaAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationKeyType.setStatus("current")
_JuniIsisSysAreaAuthenticationStartAcceptTime_Type = AuthTime
_JuniIsisSysAreaAuthenticationStartAcceptTime_Object = MibTableColumn
juniIsisSysAreaAuthenticationStartAcceptTime = _JuniIsisSysAreaAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 5),
    _JuniIsisSysAreaAuthenticationStartAcceptTime_Type()
)
juniIsisSysAreaAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationStartAcceptTime.setStatus("current")
_JuniIsisSysAreaAuthenticationStartGenerateTime_Type = AuthTime
_JuniIsisSysAreaAuthenticationStartGenerateTime_Object = MibTableColumn
juniIsisSysAreaAuthenticationStartGenerateTime = _JuniIsisSysAreaAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 6),
    _JuniIsisSysAreaAuthenticationStartGenerateTime_Type()
)
juniIsisSysAreaAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationStartGenerateTime.setStatus("current")


class _JuniIsisSysAreaAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type juniIsisSysAreaAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysAreaAuthenticationStopAcceptTime_Object = MibTableColumn
juniIsisSysAreaAuthenticationStopAcceptTime = _JuniIsisSysAreaAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 7),
    _JuniIsisSysAreaAuthenticationStopAcceptTime_Type()
)
juniIsisSysAreaAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationStopAcceptTime.setStatus("current")


class _JuniIsisSysAreaAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type juniIsisSysAreaAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysAreaAuthenticationStopGenerateTime_Object = MibTableColumn
juniIsisSysAreaAuthenticationStopGenerateTime = _JuniIsisSysAreaAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 8),
    _JuniIsisSysAreaAuthenticationStopGenerateTime_Type()
)
juniIsisSysAreaAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationStopGenerateTime.setStatus("current")
_JuniIsisSysAreaAuthenticationRowStatus_Type = RowStatus
_JuniIsisSysAreaAuthenticationRowStatus_Object = MibTableColumn
juniIsisSysAreaAuthenticationRowStatus = _JuniIsisSysAreaAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 6, 1, 9),
    _JuniIsisSysAreaAuthenticationRowStatus_Type()
)
juniIsisSysAreaAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysAreaAuthenticationRowStatus.setStatus("current")
_JuniIsisSysDomainAuthenticationTable_Object = MibTable
juniIsisSysDomainAuthenticationTable = _JuniIsisSysDomainAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7)
)
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationTable.setStatus("current")
_JuniIsisSysDomainAuthenticationEntry_Object = MibTableRow
juniIsisSysDomainAuthenticationEntry = _JuniIsisSysDomainAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1)
)
juniIsisSysDomainAuthenticationEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationEntry.setStatus("current")


class _JuniIsisSysDomainAuthenticationSysInstance_Type(Integer32):
    """Custom type juniIsisSysDomainAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysDomainAuthenticationSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysDomainAuthenticationSysInstance_Object = MibTableColumn
juniIsisSysDomainAuthenticationSysInstance = _JuniIsisSysDomainAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 1),
    _JuniIsisSysDomainAuthenticationSysInstance_Type()
)
juniIsisSysDomainAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationSysInstance.setStatus("current")


class _JuniIsisSysDomainAuthenticationKeyId_Type(Integer32):
    """Custom type juniIsisSysDomainAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIsisSysDomainAuthenticationKeyId_Type.__name__ = "Integer32"
_JuniIsisSysDomainAuthenticationKeyId_Object = MibTableColumn
juniIsisSysDomainAuthenticationKeyId = _JuniIsisSysDomainAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 2),
    _JuniIsisSysDomainAuthenticationKeyId_Type()
)
juniIsisSysDomainAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationKeyId.setStatus("current")


class _JuniIsisSysDomainAuthenticationPwd_Type(OctetString):
    """Custom type juniIsisSysDomainAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniIsisSysDomainAuthenticationPwd_Type.__name__ = "OctetString"
_JuniIsisSysDomainAuthenticationPwd_Object = MibTableColumn
juniIsisSysDomainAuthenticationPwd = _JuniIsisSysDomainAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 3),
    _JuniIsisSysDomainAuthenticationPwd_Type()
)
juniIsisSysDomainAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationPwd.setStatus("current")


class _JuniIsisSysDomainAuthenticationKeyType_Type(Integer32):
    """Custom type juniIsisSysDomainAuthenticationKeyType based on Integer32"""
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


_JuniIsisSysDomainAuthenticationKeyType_Type.__name__ = "Integer32"
_JuniIsisSysDomainAuthenticationKeyType_Object = MibTableColumn
juniIsisSysDomainAuthenticationKeyType = _JuniIsisSysDomainAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 4),
    _JuniIsisSysDomainAuthenticationKeyType_Type()
)
juniIsisSysDomainAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationKeyType.setStatus("current")
_JuniIsisSysDomainAuthenticationStartAcceptTime_Type = AuthTime
_JuniIsisSysDomainAuthenticationStartAcceptTime_Object = MibTableColumn
juniIsisSysDomainAuthenticationStartAcceptTime = _JuniIsisSysDomainAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 5),
    _JuniIsisSysDomainAuthenticationStartAcceptTime_Type()
)
juniIsisSysDomainAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationStartAcceptTime.setStatus("current")
_JuniIsisSysDomainAuthenticationStartGenerateTime_Type = AuthTime
_JuniIsisSysDomainAuthenticationStartGenerateTime_Object = MibTableColumn
juniIsisSysDomainAuthenticationStartGenerateTime = _JuniIsisSysDomainAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 6),
    _JuniIsisSysDomainAuthenticationStartGenerateTime_Type()
)
juniIsisSysDomainAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationStartGenerateTime.setStatus("current")


class _JuniIsisSysDomainAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type juniIsisSysDomainAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysDomainAuthenticationStopAcceptTime_Object = MibTableColumn
juniIsisSysDomainAuthenticationStopAcceptTime = _JuniIsisSysDomainAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 7),
    _JuniIsisSysDomainAuthenticationStopAcceptTime_Type()
)
juniIsisSysDomainAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationStopAcceptTime.setStatus("current")


class _JuniIsisSysDomainAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type juniIsisSysDomainAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysDomainAuthenticationStopGenerateTime_Object = MibTableColumn
juniIsisSysDomainAuthenticationStopGenerateTime = _JuniIsisSysDomainAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 8),
    _JuniIsisSysDomainAuthenticationStopGenerateTime_Type()
)
juniIsisSysDomainAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationStopGenerateTime.setStatus("current")
_JuniIsisSysDomainAuthenticationRowStatus_Type = RowStatus
_JuniIsisSysDomainAuthenticationRowStatus_Object = MibTableColumn
juniIsisSysDomainAuthenticationRowStatus = _JuniIsisSysDomainAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 7, 1, 9),
    _JuniIsisSysDomainAuthenticationRowStatus_Type()
)
juniIsisSysDomainAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysDomainAuthenticationRowStatus.setStatus("current")
_JuniIsisMplsTeTunnelTable_Object = MibTable
juniIsisMplsTeTunnelTable = _JuniIsisMplsTeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8)
)
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelTable.setStatus("current")
_JuniIsisMplsTeTunnelEntry_Object = MibTableRow
juniIsisMplsTeTunnelEntry = _JuniIsisMplsTeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1)
)
juniIsisMplsTeTunnelEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisMplsTeTunnelSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisMplsNextHopIndex"),
)
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelEntry.setStatus("current")


class _JuniIsisMplsTeTunnelSysInstance_Type(Integer32):
    """Custom type juniIsisMplsTeTunnelSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisMplsTeTunnelSysInstance_Type.__name__ = "Integer32"
_JuniIsisMplsTeTunnelSysInstance_Object = MibTableColumn
juniIsisMplsTeTunnelSysInstance = _JuniIsisMplsTeTunnelSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 1),
    _JuniIsisMplsTeTunnelSysInstance_Type()
)
juniIsisMplsTeTunnelSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelSysInstance.setStatus("current")
_JuniIsisMplsNextHopIndex_Type = Integer32
_JuniIsisMplsNextHopIndex_Object = MibTableColumn
juniIsisMplsNextHopIndex = _JuniIsisMplsNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 2),
    _JuniIsisMplsNextHopIndex_Type()
)
juniIsisMplsNextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisMplsNextHopIndex.setStatus("current")
_JuniIsisMplsTeSystemId_Type = SystemID
_JuniIsisMplsTeSystemId_Object = MibTableColumn
juniIsisMplsTeSystemId = _JuniIsisMplsTeSystemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 3),
    _JuniIsisMplsTeSystemId_Type()
)
juniIsisMplsTeSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisMplsTeSystemId.setStatus("current")
_JuniIsisMplsTeRouterId_Type = IpAddress
_JuniIsisMplsTeRouterId_Object = MibTableColumn
juniIsisMplsTeRouterId = _JuniIsisMplsTeRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 4),
    _JuniIsisMplsTeRouterId_Type()
)
juniIsisMplsTeRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisMplsTeRouterId.setStatus("current")
_JuniIsisMplsTeTunnelMetric_Type = Integer32
_JuniIsisMplsTeTunnelMetric_Object = MibTableColumn
juniIsisMplsTeTunnelMetric = _JuniIsisMplsTeTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 5),
    _JuniIsisMplsTeTunnelMetric_Type()
)
juniIsisMplsTeTunnelMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelMetric.setStatus("current")
_JuniIsisMplsTeTunnelRelMetric_Type = Integer32
_JuniIsisMplsTeTunnelRelMetric_Object = MibTableColumn
juniIsisMplsTeTunnelRelMetric = _JuniIsisMplsTeTunnelRelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 6),
    _JuniIsisMplsTeTunnelRelMetric_Type()
)
juniIsisMplsTeTunnelRelMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelRelMetric.setStatus("current")


class _JuniIsisMplsTeTunnelName_Type(OctetString):
    """Custom type juniIsisMplsTeTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniIsisMplsTeTunnelName_Type.__name__ = "OctetString"
_JuniIsisMplsTeTunnelName_Object = MibTableColumn
juniIsisMplsTeTunnelName = _JuniIsisMplsTeTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 1, 8, 1, 7),
    _JuniIsisMplsTeTunnelName_Type()
)
juniIsisMplsTeTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisMplsTeTunnelName.setStatus("current")
_JuniIsisCircuitGroup_ObjectIdentity = ObjectIdentity
juniIsisCircuitGroup = _JuniIsisCircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2)
)
_JuniIsisCircTable_Object = MibTable
juniIsisCircTable = _JuniIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniIsisCircTable.setStatus("current")
_JuniIsisCircEntry_Object = MibTableRow
juniIsisCircEntry = _JuniIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1)
)
juniIsisCircEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisCircSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisCircIfIndex"),
)
if mibBuilder.loadTexts:
    juniIsisCircEntry.setStatus("current")


class _JuniIsisCircSysInstance_Type(Integer32):
    """Custom type juniIsisCircSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisCircSysInstance_Type.__name__ = "Integer32"
_JuniIsisCircSysInstance_Object = MibTableColumn
juniIsisCircSysInstance = _JuniIsisCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 1),
    _JuniIsisCircSysInstance_Type()
)
juniIsisCircSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisCircSysInstance.setStatus("current")


class _JuniIsisCircIfIndex_Type(Integer32):
    """Custom type juniIsisCircIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisCircIfIndex_Type.__name__ = "Integer32"
_JuniIsisCircIfIndex_Object = MibTableColumn
juniIsisCircIfIndex = _JuniIsisCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 2),
    _JuniIsisCircIfIndex_Type()
)
juniIsisCircIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisCircIfIndex.setStatus("current")
_JuniIsisCircLocalID_Type = Integer32
_JuniIsisCircLocalID_Object = MibTableColumn
juniIsisCircLocalID = _JuniIsisCircLocalID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 3),
    _JuniIsisCircLocalID_Type()
)
juniIsisCircLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircLocalID.setStatus("current")


class _JuniIsisCircOperState_Type(OperState):
    """Custom type juniIsisCircOperState based on OperState"""


_JuniIsisCircOperState_Object = MibTableColumn
juniIsisCircOperState = _JuniIsisCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 4),
    _JuniIsisCircOperState_Type()
)
juniIsisCircOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircOperState.setStatus("current")


class _JuniIsisCircRowStatus_Type(RowStatus):
    """Custom type juniIsisCircRowStatus based on RowStatus"""


_JuniIsisCircRowStatus_Object = MibTableColumn
juniIsisCircRowStatus = _JuniIsisCircRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 5),
    _JuniIsisCircRowStatus_Type()
)
juniIsisCircRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircRowStatus.setStatus("current")


class _JuniIsisCircType_Type(Integer32):
    """Custom type juniIsisCircType based on Integer32"""
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


_JuniIsisCircType_Type.__name__ = "Integer32"
_JuniIsisCircType_Object = MibTableColumn
juniIsisCircType = _JuniIsisCircType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 6),
    _JuniIsisCircType_Type()
)
juniIsisCircType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircType.setStatus("current")


class _JuniIsisCircL1DefaultMetric_Type(JuniDefaultMetric):
    """Custom type juniIsisCircL1DefaultMetric based on JuniDefaultMetric"""
    defaultValue = 10


_JuniIsisCircL1DefaultMetric_Object = MibTableColumn
juniIsisCircL1DefaultMetric = _JuniIsisCircL1DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 7),
    _JuniIsisCircL1DefaultMetric_Type()
)
juniIsisCircL1DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL1DefaultMetric.setStatus("current")


class _JuniIsisCircL1DelayMetric_Type(OtherMetric):
    """Custom type juniIsisCircL1DelayMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL1DelayMetric_Object = MibTableColumn
juniIsisCircL1DelayMetric = _JuniIsisCircL1DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 8),
    _JuniIsisCircL1DelayMetric_Type()
)
juniIsisCircL1DelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL1DelayMetric.setStatus("current")


class _JuniIsisCircL1ExpenseMetric_Type(OtherMetric):
    """Custom type juniIsisCircL1ExpenseMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL1ExpenseMetric_Object = MibTableColumn
juniIsisCircL1ExpenseMetric = _JuniIsisCircL1ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 9),
    _JuniIsisCircL1ExpenseMetric_Type()
)
juniIsisCircL1ExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL1ExpenseMetric.setStatus("current")


class _JuniIsisCircL1ErrorMetric_Type(OtherMetric):
    """Custom type juniIsisCircL1ErrorMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL1ErrorMetric_Object = MibTableColumn
juniIsisCircL1ErrorMetric = _JuniIsisCircL1ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 10),
    _JuniIsisCircL1ErrorMetric_Type()
)
juniIsisCircL1ErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL1ErrorMetric.setStatus("current")


class _JuniIsisCircExtDomain_Type(TruthValue):
    """Custom type juniIsisCircExtDomain based on TruthValue"""


_JuniIsisCircExtDomain_Object = MibTableColumn
juniIsisCircExtDomain = _JuniIsisCircExtDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 11),
    _JuniIsisCircExtDomain_Type()
)
juniIsisCircExtDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircExtDomain.setStatus("current")
_JuniIsisCircAdjChanges_Type = Counter32
_JuniIsisCircAdjChanges_Object = MibTableColumn
juniIsisCircAdjChanges = _JuniIsisCircAdjChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 12),
    _JuniIsisCircAdjChanges_Type()
)
juniIsisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircAdjChanges.setStatus("current")
_JuniIsisCircInitFails_Type = Counter32
_JuniIsisCircInitFails_Object = MibTableColumn
juniIsisCircInitFails = _JuniIsisCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 13),
    _JuniIsisCircInitFails_Type()
)
juniIsisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircInitFails.setStatus("current")
_JuniIsisCircRejAdjs_Type = Counter32
_JuniIsisCircRejAdjs_Object = MibTableColumn
juniIsisCircRejAdjs = _JuniIsisCircRejAdjs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 14),
    _JuniIsisCircRejAdjs_Type()
)
juniIsisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircRejAdjs.setStatus("current")
_JuniIsisCircOutCtrlPDUs_Type = Counter32
_JuniIsisCircOutCtrlPDUs_Object = MibTableColumn
juniIsisCircOutCtrlPDUs = _JuniIsisCircOutCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 15),
    _JuniIsisCircOutCtrlPDUs_Type()
)
juniIsisCircOutCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircOutCtrlPDUs.setStatus("current")
_JuniIsisCircInCtrlPDUs_Type = Counter32
_JuniIsisCircInCtrlPDUs_Object = MibTableColumn
juniIsisCircInCtrlPDUs = _JuniIsisCircInCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 16),
    _JuniIsisCircInCtrlPDUs_Type()
)
juniIsisCircInCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircInCtrlPDUs.setStatus("current")
_JuniIsisCircIDFieldLenMismatches_Type = Counter32
_JuniIsisCircIDFieldLenMismatches_Object = MibTableColumn
juniIsisCircIDFieldLenMismatches = _JuniIsisCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 17),
    _JuniIsisCircIDFieldLenMismatches_Type()
)
juniIsisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircIDFieldLenMismatches.setStatus("current")


class _JuniIsisCircL2DefaultMetric_Type(JuniDefaultMetric):
    """Custom type juniIsisCircL2DefaultMetric based on JuniDefaultMetric"""
    defaultValue = 10


_JuniIsisCircL2DefaultMetric_Object = MibTableColumn
juniIsisCircL2DefaultMetric = _JuniIsisCircL2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 18),
    _JuniIsisCircL2DefaultMetric_Type()
)
juniIsisCircL2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL2DefaultMetric.setStatus("current")


class _JuniIsisCircL2DelayMetric_Type(OtherMetric):
    """Custom type juniIsisCircL2DelayMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL2DelayMetric_Object = MibTableColumn
juniIsisCircL2DelayMetric = _JuniIsisCircL2DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 19),
    _JuniIsisCircL2DelayMetric_Type()
)
juniIsisCircL2DelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL2DelayMetric.setStatus("current")


class _JuniIsisCircL2ExpenseMetric_Type(OtherMetric):
    """Custom type juniIsisCircL2ExpenseMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL2ExpenseMetric_Object = MibTableColumn
juniIsisCircL2ExpenseMetric = _JuniIsisCircL2ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 20),
    _JuniIsisCircL2ExpenseMetric_Type()
)
juniIsisCircL2ExpenseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL2ExpenseMetric.setStatus("current")


class _JuniIsisCircL2ErrorMetric_Type(OtherMetric):
    """Custom type juniIsisCircL2ErrorMetric based on OtherMetric"""
    defaultValue = 0


_JuniIsisCircL2ErrorMetric_Object = MibTableColumn
juniIsisCircL2ErrorMetric = _JuniIsisCircL2ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 21),
    _JuniIsisCircL2ErrorMetric_Type()
)
juniIsisCircL2ErrorMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL2ErrorMetric.setStatus("current")


class _JuniIsisCircManL2Only_Type(TruthValue):
    """Custom type juniIsisCircManL2Only based on TruthValue"""


_JuniIsisCircManL2Only_Object = MibTableColumn
juniIsisCircManL2Only = _JuniIsisCircManL2Only_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 22),
    _JuniIsisCircManL2Only_Type()
)
juniIsisCircManL2Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircManL2Only.setStatus("current")


class _JuniIsisCircL1ISPriority_Type(ISPriority):
    """Custom type juniIsisCircL1ISPriority based on ISPriority"""
    defaultValue = 64


_JuniIsisCircL1ISPriority_Object = MibTableColumn
juniIsisCircL1ISPriority = _JuniIsisCircL1ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 23),
    _JuniIsisCircL1ISPriority_Type()
)
juniIsisCircL1ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL1ISPriority.setStatus("current")
_JuniIsisCircL1CircID_Type = CircuitID
_JuniIsisCircL1CircID_Object = MibTableColumn
juniIsisCircL1CircID = _JuniIsisCircL1CircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 24),
    _JuniIsisCircL1CircID_Type()
)
juniIsisCircL1CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL1CircID.setStatus("current")
_JuniIsisCircL1DesIS_Type = SystemID
_JuniIsisCircL1DesIS_Object = MibTableColumn
juniIsisCircL1DesIS = _JuniIsisCircL1DesIS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 25),
    _JuniIsisCircL1DesIS_Type()
)
juniIsisCircL1DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL1DesIS.setStatus("current")
_JuniIsisCircLANL1DesISChanges_Type = Counter32
_JuniIsisCircLANL1DesISChanges_Object = MibTableColumn
juniIsisCircLANL1DesISChanges = _JuniIsisCircLANL1DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 26),
    _JuniIsisCircLANL1DesISChanges_Type()
)
juniIsisCircLANL1DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircLANL1DesISChanges.setStatus("current")


class _JuniIsisCircL2ISPriority_Type(ISPriority):
    """Custom type juniIsisCircL2ISPriority based on ISPriority"""
    defaultValue = 64


_JuniIsisCircL2ISPriority_Object = MibTableColumn
juniIsisCircL2ISPriority = _JuniIsisCircL2ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 27),
    _JuniIsisCircL2ISPriority_Type()
)
juniIsisCircL2ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL2ISPriority.setStatus("current")
_JuniIsisCircL2CircID_Type = CircuitID
_JuniIsisCircL2CircID_Object = MibTableColumn
juniIsisCircL2CircID = _JuniIsisCircL2CircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 28),
    _JuniIsisCircL2CircID_Type()
)
juniIsisCircL2CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL2CircID.setStatus("current")
_JuniIsisCircL2DesIS_Type = SystemID
_JuniIsisCircL2DesIS_Object = MibTableColumn
juniIsisCircL2DesIS = _JuniIsisCircL2DesIS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 29),
    _JuniIsisCircL2DesIS_Type()
)
juniIsisCircL2DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircL2DesIS.setStatus("current")
_JuniIsisCircLANL2DesISChanges_Type = Counter32
_JuniIsisCircLANL2DesISChanges_Object = MibTableColumn
juniIsisCircLANL2DesISChanges = _JuniIsisCircLANL2DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 30),
    _JuniIsisCircLANL2DesISChanges_Type()
)
juniIsisCircLANL2DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircLANL2DesISChanges.setStatus("current")


class _JuniIsisCircMCAddr_Type(Integer32):
    """Custom type juniIsisCircMCAddr based on Integer32"""
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


_JuniIsisCircMCAddr_Type.__name__ = "Integer32"
_JuniIsisCircMCAddr_Object = MibTableColumn
juniIsisCircMCAddr = _JuniIsisCircMCAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 31),
    _JuniIsisCircMCAddr_Type()
)
juniIsisCircMCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircMCAddr.setStatus("current")
_JuniIsisCircPtToPtCircID_Type = CircuitID
_JuniIsisCircPtToPtCircID_Object = MibTableColumn
juniIsisCircPtToPtCircID = _JuniIsisCircPtToPtCircID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 32),
    _JuniIsisCircPtToPtCircID_Type()
)
juniIsisCircPtToPtCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircPtToPtCircID.setStatus("current")


class _JuniIsisCircL1HelloTimer_Type(Integer32):
    """Custom type juniIsisCircL1HelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisCircL1HelloTimer_Type.__name__ = "Integer32"
_JuniIsisCircL1HelloTimer_Object = MibTableColumn
juniIsisCircL1HelloTimer = _JuniIsisCircL1HelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 33),
    _JuniIsisCircL1HelloTimer_Type()
)
juniIsisCircL1HelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL1HelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircL1HelloTimer.setUnits("seconds")


class _JuniIsisCircL2HelloTimer_Type(Integer32):
    """Custom type juniIsisCircL2HelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisCircL2HelloTimer_Type.__name__ = "Integer32"
_JuniIsisCircL2HelloTimer_Object = MibTableColumn
juniIsisCircL2HelloTimer = _JuniIsisCircL2HelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 34),
    _JuniIsisCircL2HelloTimer_Type()
)
juniIsisCircL2HelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL2HelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircL2HelloTimer.setUnits("seconds")


class _JuniIsisCircL1HelloMultiplier_Type(Integer32):
    """Custom type juniIsisCircL1HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_JuniIsisCircL1HelloMultiplier_Type.__name__ = "Integer32"
_JuniIsisCircL1HelloMultiplier_Object = MibTableColumn
juniIsisCircL1HelloMultiplier = _JuniIsisCircL1HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 35),
    _JuniIsisCircL1HelloMultiplier_Type()
)
juniIsisCircL1HelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL1HelloMultiplier.setStatus("current")


class _JuniIsisCircL2HelloMultiplier_Type(Integer32):
    """Custom type juniIsisCircL2HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_JuniIsisCircL2HelloMultiplier_Type.__name__ = "Integer32"
_JuniIsisCircL2HelloMultiplier_Object = MibTableColumn
juniIsisCircL2HelloMultiplier = _JuniIsisCircL2HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 36),
    _JuniIsisCircL2HelloMultiplier_Type()
)
juniIsisCircL2HelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL2HelloMultiplier.setStatus("current")


class _JuniIsisCircMinLSPTransInt_Type(Unsigned32):
    """Custom type juniIsisCircMinLSPTransInt based on Unsigned32"""
    defaultValue = 33


_JuniIsisCircMinLSPTransInt_Object = MibTableColumn
juniIsisCircMinLSPTransInt = _JuniIsisCircMinLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 37),
    _JuniIsisCircMinLSPTransInt_Type()
)
juniIsisCircMinLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircMinLSPTransInt.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircMinLSPTransInt.setUnits("milliseconds")


class _JuniIsisCircMinLSPReTransInt_Type(Integer32):
    """Custom type juniIsisCircMinLSPReTransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisCircMinLSPReTransInt_Type.__name__ = "Integer32"
_JuniIsisCircMinLSPReTransInt_Object = MibTableColumn
juniIsisCircMinLSPReTransInt = _JuniIsisCircMinLSPReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 38),
    _JuniIsisCircMinLSPReTransInt_Type()
)
juniIsisCircMinLSPReTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircMinLSPReTransInt.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircMinLSPReTransInt.setUnits("seconds")


class _JuniIsisCircL1CSNPInterval_Type(Integer32):
    """Custom type juniIsisCircL1CSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisCircL1CSNPInterval_Type.__name__ = "Integer32"
_JuniIsisCircL1CSNPInterval_Object = MibTableColumn
juniIsisCircL1CSNPInterval = _JuniIsisCircL1CSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 39),
    _JuniIsisCircL1CSNPInterval_Type()
)
juniIsisCircL1CSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL1CSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircL1CSNPInterval.setUnits("seconds")


class _JuniIsisCircL2CSNPInterval_Type(Integer32):
    """Custom type juniIsisCircL2CSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniIsisCircL2CSNPInterval_Type.__name__ = "Integer32"
_JuniIsisCircL2CSNPInterval_Object = MibTableColumn
juniIsisCircL2CSNPInterval = _JuniIsisCircL2CSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 40),
    _JuniIsisCircL2CSNPInterval_Type()
)
juniIsisCircL2CSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircL2CSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircL2CSNPInterval.setUnits("seconds")


class _JuniIsisCircLSPThrottle_Type(Integer32):
    """Custom type juniIsisCircLSPThrottle based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniIsisCircLSPThrottle_Type.__name__ = "Integer32"
_JuniIsisCircLSPThrottle_Object = MibTableColumn
juniIsisCircLSPThrottle = _JuniIsisCircLSPThrottle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 41),
    _JuniIsisCircLSPThrottle_Type()
)
juniIsisCircLSPThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    juniIsisCircLSPThrottle.setUnits("milliseconds")


class _JuniIsisCircMeshGroupEnabled_Type(Integer32):
    """Custom type juniIsisCircMeshGroupEnabled based on Integer32"""
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


_JuniIsisCircMeshGroupEnabled_Type.__name__ = "Integer32"
_JuniIsisCircMeshGroupEnabled_Object = MibTableColumn
juniIsisCircMeshGroupEnabled = _JuniIsisCircMeshGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 42),
    _JuniIsisCircMeshGroupEnabled_Type()
)
juniIsisCircMeshGroupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircMeshGroupEnabled.setStatus("current")
_JuniIsisCircMeshGroup_Type = Unsigned32
_JuniIsisCircMeshGroup_Object = MibTableColumn
juniIsisCircMeshGroup = _JuniIsisCircMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 43),
    _JuniIsisCircMeshGroup_Type()
)
juniIsisCircMeshGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircMeshGroup.setStatus("current")


class _JuniIsisCircLevel_Type(Integer32):
    """Custom type juniIsisCircLevel based on Integer32"""
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


_JuniIsisCircLevel_Type.__name__ = "Integer32"
_JuniIsisCircLevel_Object = MibTableColumn
juniIsisCircLevel = _JuniIsisCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 44),
    _JuniIsisCircLevel_Type()
)
juniIsisCircLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisCircLevel.setStatus("current")


class _JuniIsisCircState_Type(Integer32):
    """Custom type juniIsisCircState based on Integer32"""
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


_JuniIsisCircState_Type.__name__ = "Integer32"
_JuniIsisCircState_Object = MibTableColumn
juniIsisCircState = _JuniIsisCircState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 1, 1, 45),
    _JuniIsisCircState_Type()
)
juniIsisCircState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIsisCircState.setStatus("current")
_JuniIsisSysL1CircAuthenticationTable_Object = MibTable
juniIsisSysL1CircAuthenticationTable = _JuniIsisSysL1CircAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationTable.setStatus("current")
_JuniIsisSysL1CircAuthenticationEntry_Object = MibTableRow
juniIsisSysL1CircAuthenticationEntry = _JuniIsisSysL1CircAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1)
)
juniIsisSysL1CircAuthenticationEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationIfIndex"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationEntry.setStatus("current")


class _JuniIsisSysL1CircAuthenticationSysInstance_Type(Integer32):
    """Custom type juniIsisSysL1CircAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysL1CircAuthenticationSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysL1CircAuthenticationSysInstance_Object = MibTableColumn
juniIsisSysL1CircAuthenticationSysInstance = _JuniIsisSysL1CircAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 1),
    _JuniIsisSysL1CircAuthenticationSysInstance_Type()
)
juniIsisSysL1CircAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationSysInstance.setStatus("current")


class _JuniIsisSysL1CircAuthenticationIfIndex_Type(Integer32):
    """Custom type juniIsisSysL1CircAuthenticationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysL1CircAuthenticationIfIndex_Type.__name__ = "Integer32"
_JuniIsisSysL1CircAuthenticationIfIndex_Object = MibTableColumn
juniIsisSysL1CircAuthenticationIfIndex = _JuniIsisSysL1CircAuthenticationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 2),
    _JuniIsisSysL1CircAuthenticationIfIndex_Type()
)
juniIsisSysL1CircAuthenticationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationIfIndex.setStatus("current")


class _JuniIsisSysL1CircAuthenticationKeyId_Type(Integer32):
    """Custom type juniIsisSysL1CircAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIsisSysL1CircAuthenticationKeyId_Type.__name__ = "Integer32"
_JuniIsisSysL1CircAuthenticationKeyId_Object = MibTableColumn
juniIsisSysL1CircAuthenticationKeyId = _JuniIsisSysL1CircAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 3),
    _JuniIsisSysL1CircAuthenticationKeyId_Type()
)
juniIsisSysL1CircAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationKeyId.setStatus("current")


class _JuniIsisSysL1CircAuthenticationPwd_Type(OctetString):
    """Custom type juniIsisSysL1CircAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniIsisSysL1CircAuthenticationPwd_Type.__name__ = "OctetString"
_JuniIsisSysL1CircAuthenticationPwd_Object = MibTableColumn
juniIsisSysL1CircAuthenticationPwd = _JuniIsisSysL1CircAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 4),
    _JuniIsisSysL1CircAuthenticationPwd_Type()
)
juniIsisSysL1CircAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationPwd.setStatus("current")


class _JuniIsisSysL1CircAuthenticationKeyType_Type(Integer32):
    """Custom type juniIsisSysL1CircAuthenticationKeyType based on Integer32"""
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


_JuniIsisSysL1CircAuthenticationKeyType_Type.__name__ = "Integer32"
_JuniIsisSysL1CircAuthenticationKeyType_Object = MibTableColumn
juniIsisSysL1CircAuthenticationKeyType = _JuniIsisSysL1CircAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 5),
    _JuniIsisSysL1CircAuthenticationKeyType_Type()
)
juniIsisSysL1CircAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationKeyType.setStatus("current")
_JuniIsisSysL1CircAuthenticationStartAcceptTime_Type = AuthTime
_JuniIsisSysL1CircAuthenticationStartAcceptTime_Object = MibTableColumn
juniIsisSysL1CircAuthenticationStartAcceptTime = _JuniIsisSysL1CircAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 6),
    _JuniIsisSysL1CircAuthenticationStartAcceptTime_Type()
)
juniIsisSysL1CircAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationStartAcceptTime.setStatus("current")
_JuniIsisSysL1CircAuthenticationStartGenerateTime_Type = AuthTime
_JuniIsisSysL1CircAuthenticationStartGenerateTime_Object = MibTableColumn
juniIsisSysL1CircAuthenticationStartGenerateTime = _JuniIsisSysL1CircAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 7),
    _JuniIsisSysL1CircAuthenticationStartGenerateTime_Type()
)
juniIsisSysL1CircAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationStartGenerateTime.setStatus("current")


class _JuniIsisSysL1CircAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type juniIsisSysL1CircAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysL1CircAuthenticationStopAcceptTime_Object = MibTableColumn
juniIsisSysL1CircAuthenticationStopAcceptTime = _JuniIsisSysL1CircAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 8),
    _JuniIsisSysL1CircAuthenticationStopAcceptTime_Type()
)
juniIsisSysL1CircAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationStopAcceptTime.setStatus("current")


class _JuniIsisSysL1CircAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type juniIsisSysL1CircAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysL1CircAuthenticationStopGenerateTime_Object = MibTableColumn
juniIsisSysL1CircAuthenticationStopGenerateTime = _JuniIsisSysL1CircAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 9),
    _JuniIsisSysL1CircAuthenticationStopGenerateTime_Type()
)
juniIsisSysL1CircAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationStopGenerateTime.setStatus("current")
_JuniIsisSysL1CircAuthenticationRowStatus_Type = RowStatus
_JuniIsisSysL1CircAuthenticationRowStatus_Object = MibTableColumn
juniIsisSysL1CircAuthenticationRowStatus = _JuniIsisSysL1CircAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 2, 1, 10),
    _JuniIsisSysL1CircAuthenticationRowStatus_Type()
)
juniIsisSysL1CircAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL1CircAuthenticationRowStatus.setStatus("current")
_JuniIsisSysL2CircAuthenticationTable_Object = MibTable
juniIsisSysL2CircAuthenticationTable = _JuniIsisSysL2CircAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationTable.setStatus("current")
_JuniIsisSysL2CircAuthenticationEntry_Object = MibTableRow
juniIsisSysL2CircAuthenticationEntry = _JuniIsisSysL2CircAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1)
)
juniIsisSysL2CircAuthenticationEntry.setIndexNames(
    (0, "Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationSysInstance"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationIfIndex"),
    (0, "Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationEntry.setStatus("current")


class _JuniIsisSysL2CircAuthenticationSysInstance_Type(Integer32):
    """Custom type juniIsisSysL2CircAuthenticationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysL2CircAuthenticationSysInstance_Type.__name__ = "Integer32"
_JuniIsisSysL2CircAuthenticationSysInstance_Object = MibTableColumn
juniIsisSysL2CircAuthenticationSysInstance = _JuniIsisSysL2CircAuthenticationSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 1),
    _JuniIsisSysL2CircAuthenticationSysInstance_Type()
)
juniIsisSysL2CircAuthenticationSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationSysInstance.setStatus("current")


class _JuniIsisSysL2CircAuthenticationIfIndex_Type(Integer32):
    """Custom type juniIsisSysL2CircAuthenticationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIsisSysL2CircAuthenticationIfIndex_Type.__name__ = "Integer32"
_JuniIsisSysL2CircAuthenticationIfIndex_Object = MibTableColumn
juniIsisSysL2CircAuthenticationIfIndex = _JuniIsisSysL2CircAuthenticationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 2),
    _JuniIsisSysL2CircAuthenticationIfIndex_Type()
)
juniIsisSysL2CircAuthenticationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationIfIndex.setStatus("current")


class _JuniIsisSysL2CircAuthenticationKeyId_Type(Integer32):
    """Custom type juniIsisSysL2CircAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIsisSysL2CircAuthenticationKeyId_Type.__name__ = "Integer32"
_JuniIsisSysL2CircAuthenticationKeyId_Object = MibTableColumn
juniIsisSysL2CircAuthenticationKeyId = _JuniIsisSysL2CircAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 3),
    _JuniIsisSysL2CircAuthenticationKeyId_Type()
)
juniIsisSysL2CircAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationKeyId.setStatus("current")


class _JuniIsisSysL2CircAuthenticationPwd_Type(OctetString):
    """Custom type juniIsisSysL2CircAuthenticationPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniIsisSysL2CircAuthenticationPwd_Type.__name__ = "OctetString"
_JuniIsisSysL2CircAuthenticationPwd_Object = MibTableColumn
juniIsisSysL2CircAuthenticationPwd = _JuniIsisSysL2CircAuthenticationPwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 4),
    _JuniIsisSysL2CircAuthenticationPwd_Type()
)
juniIsisSysL2CircAuthenticationPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationPwd.setStatus("current")


class _JuniIsisSysL2CircAuthenticationKeyType_Type(Integer32):
    """Custom type juniIsisSysL2CircAuthenticationKeyType based on Integer32"""
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


_JuniIsisSysL2CircAuthenticationKeyType_Type.__name__ = "Integer32"
_JuniIsisSysL2CircAuthenticationKeyType_Object = MibTableColumn
juniIsisSysL2CircAuthenticationKeyType = _JuniIsisSysL2CircAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 5),
    _JuniIsisSysL2CircAuthenticationKeyType_Type()
)
juniIsisSysL2CircAuthenticationKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationKeyType.setStatus("current")
_JuniIsisSysL2CircAuthenticationStartAcceptTime_Type = AuthTime
_JuniIsisSysL2CircAuthenticationStartAcceptTime_Object = MibTableColumn
juniIsisSysL2CircAuthenticationStartAcceptTime = _JuniIsisSysL2CircAuthenticationStartAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 6),
    _JuniIsisSysL2CircAuthenticationStartAcceptTime_Type()
)
juniIsisSysL2CircAuthenticationStartAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationStartAcceptTime.setStatus("current")
_JuniIsisSysL2CircAuthenticationStartGenerateTime_Type = AuthTime
_JuniIsisSysL2CircAuthenticationStartGenerateTime_Object = MibTableColumn
juniIsisSysL2CircAuthenticationStartGenerateTime = _JuniIsisSysL2CircAuthenticationStartGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 7),
    _JuniIsisSysL2CircAuthenticationStartGenerateTime_Type()
)
juniIsisSysL2CircAuthenticationStartGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationStartGenerateTime.setStatus("current")


class _JuniIsisSysL2CircAuthenticationStopAcceptTime_Type(AuthTime):
    """Custom type juniIsisSysL2CircAuthenticationStopAcceptTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysL2CircAuthenticationStopAcceptTime_Object = MibTableColumn
juniIsisSysL2CircAuthenticationStopAcceptTime = _JuniIsisSysL2CircAuthenticationStopAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 8),
    _JuniIsisSysL2CircAuthenticationStopAcceptTime_Type()
)
juniIsisSysL2CircAuthenticationStopAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationStopAcceptTime.setStatus("current")


class _JuniIsisSysL2CircAuthenticationStopGenerateTime_Type(AuthTime):
    """Custom type juniIsisSysL2CircAuthenticationStopGenerateTime based on AuthTime"""
    defaultValue = 0


_JuniIsisSysL2CircAuthenticationStopGenerateTime_Object = MibTableColumn
juniIsisSysL2CircAuthenticationStopGenerateTime = _JuniIsisSysL2CircAuthenticationStopGenerateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 9),
    _JuniIsisSysL2CircAuthenticationStopGenerateTime_Type()
)
juniIsisSysL2CircAuthenticationStopGenerateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationStopGenerateTime.setStatus("current")


class _JuniIsisSysL2CircAuthenticationRowStatus_Type(RowStatus):
    """Custom type juniIsisSysL2CircAuthenticationRowStatus based on RowStatus"""


_JuniIsisSysL2CircAuthenticationRowStatus_Object = MibTableColumn
juniIsisSysL2CircAuthenticationRowStatus = _JuniIsisSysL2CircAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 3, 1, 10),
    _JuniIsisSysL2CircAuthenticationRowStatus_Type()
)
juniIsisSysL2CircAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIsisSysL2CircAuthenticationRowStatus.setStatus("current")
_JuniIsisCircBFDTable_Object = MibTable
juniIsisCircBFDTable = _JuniIsisCircBFDTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniIsisCircBFDTable.setStatus("current")
_JuniIsisCircBFDEntry_Object = MibTableRow
juniIsisCircBFDEntry = _JuniIsisCircBFDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    juniIsisCircBFDEntry.setStatus("current")


class _JuniIsisCircBfdEnable_Type(TruthValue):
    """Custom type juniIsisCircBfdEnable based on TruthValue"""


_JuniIsisCircBfdEnable_Object = MibTableColumn
juniIsisCircBfdEnable = _JuniIsisCircBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4, 1, 1),
    _JuniIsisCircBfdEnable_Type()
)
juniIsisCircBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisCircBfdEnable.setStatus("current")


class _JuniIsisCircBfdMinRxInterval_Type(Integer32):
    """Custom type juniIsisCircBfdMinRxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniIsisCircBfdMinRxInterval_Type.__name__ = "Integer32"
_JuniIsisCircBfdMinRxInterval_Object = MibTableColumn
juniIsisCircBfdMinRxInterval = _JuniIsisCircBfdMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4, 1, 2),
    _JuniIsisCircBfdMinRxInterval_Type()
)
juniIsisCircBfdMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisCircBfdMinRxInterval.setStatus("current")


class _JuniIsisCircBfdMinTxInterval_Type(Integer32):
    """Custom type juniIsisCircBfdMinTxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniIsisCircBfdMinTxInterval_Type.__name__ = "Integer32"
_JuniIsisCircBfdMinTxInterval_Object = MibTableColumn
juniIsisCircBfdMinTxInterval = _JuniIsisCircBfdMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4, 1, 3),
    _JuniIsisCircBfdMinTxInterval_Type()
)
juniIsisCircBfdMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisCircBfdMinTxInterval.setStatus("current")


class _JuniIsisCircBfdMultiplier_Type(Integer32):
    """Custom type juniIsisCircBfdMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniIsisCircBfdMultiplier_Type.__name__ = "Integer32"
_JuniIsisCircBfdMultiplier_Object = MibTableColumn
juniIsisCircBfdMultiplier = _JuniIsisCircBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 1, 2, 4, 1, 4),
    _JuniIsisCircBfdMultiplier_Type()
)
juniIsisCircBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIsisCircBfdMultiplier.setStatus("current")
_JuniIsisTrapGroup_ObjectIdentity = ObjectIdentity
juniIsisTrapGroup = _JuniIsisTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 2)
)
_JuniIsisConformance_ObjectIdentity = ObjectIdentity
juniIsisConformance = _JuniIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3)
)
_JuniIsisCompliances_ObjectIdentity = ObjectIdentity
juniIsisCompliances = _JuniIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1)
)
_JuniIsisMIBGroups_ObjectIdentity = ObjectIdentity
juniIsisMIBGroups = _JuniIsisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2)
)
juniIsisCircEntry.registerAugmentions(
    ("Juniper-ISIS-MIB",
     "juniIsisCircBFDEntry")
)
juniIsisCircBFDEntry.setIndexNames(*juniIsisCircEntry.getIndexNames())

# Managed Objects groups

juniIsisSystemMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 1)
)
juniIsisSystemMgmtGroup.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisSysVersion"),
        ("Juniper-ISIS-MIB", "juniIsisSysType"),
        ("Juniper-ISIS-MIB", "juniIsisSysID"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxPathSplits"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigLSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddresses"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL1LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL2LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysPollESHelloRate"),
        ("Juniper-ISIS-MIB", "juniIsisSysWaitTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1State"),
        ("Juniper-ISIS-MIB", "juniIsisSysCorrLSPs"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL1DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysManAddrDropFromAreas"),
        ("Juniper-ISIS-MIB", "juniIsisSysAttmptToExMaxSeqNums"),
        ("Juniper-ISIS-MIB", "juniIsisSysSeqNumSkips"),
        ("Juniper-ISIS-MIB", "juniIsisSysOwnLSPPurges"),
        ("Juniper-ISIS-MIB", "juniIsisSysIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddrMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2State"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL2DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysAuthFails"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPIgnoreErrors"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaCheck"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBit"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBitStartupDuration"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLspLifetime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshHoldTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshConfigTimer"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistributeDomainWide"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistance"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysIsoRouteTag"),
        ("Juniper-ISIS-MIB", "juniIsisManAreaAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysProtSuppRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameAreaAddr"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameName"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameType"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    juniIsisSystemMgmtGroup.setStatus("obsolete")

juniIsisCircuitMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 2)
)
juniIsisCircuitMgmtGroup.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisCircLocalID"),
        ("Juniper-ISIS-MIB", "juniIsisCircOperState"),
        ("Juniper-ISIS-MIB", "juniIsisCircRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisCircType"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircExtDomain"),
        ("Juniper-ISIS-MIB", "juniIsisCircAdjChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircInitFails"),
        ("Juniper-ISIS-MIB", "juniIsisCircRejAdjs"),
        ("Juniper-ISIS-MIB", "juniIsisCircOutCtrlPDUs"),
        ("Juniper-ISIS-MIB", "juniIsisCircInCtrlPDUs"),
        ("Juniper-ISIS-MIB", "juniIsisCircIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircManL2Only"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ISPriority"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1CircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DesIS"),
        ("Juniper-ISIS-MIB", "juniIsisCircLANL1DesISChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ISPriority"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2CircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DesIS"),
        ("Juniper-ISIS-MIB", "juniIsisCircLANL2DesISChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircMCAddr"),
        ("Juniper-ISIS-MIB", "juniIsisCircPtToPtCircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1HelloTimer"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2HelloTimer"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1HelloMultiplier"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2HelloMultiplier"),
        ("Juniper-ISIS-MIB", "juniIsisCircMinLSPTransInt"),
        ("Juniper-ISIS-MIB", "juniIsisCircMinLSPReTransInt"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1CSNPInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2CSNPInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircLSPThrottle"),
        ("Juniper-ISIS-MIB", "juniIsisCircMeshGroupEnabled"),
        ("Juniper-ISIS-MIB", "juniIsisCircMeshGroup"),
        ("Juniper-ISIS-MIB", "juniIsisCircLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    juniIsisCircuitMgmtGroup.setStatus("obsolete")

juniIsisCircuitMgmtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 3)
)
juniIsisCircuitMgmtGroup2.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisCircLocalID"),
        ("Juniper-ISIS-MIB", "juniIsisCircOperState"),
        ("Juniper-ISIS-MIB", "juniIsisCircRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisCircType"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircExtDomain"),
        ("Juniper-ISIS-MIB", "juniIsisCircAdjChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircInitFails"),
        ("Juniper-ISIS-MIB", "juniIsisCircRejAdjs"),
        ("Juniper-ISIS-MIB", "juniIsisCircOutCtrlPDUs"),
        ("Juniper-ISIS-MIB", "juniIsisCircInCtrlPDUs"),
        ("Juniper-ISIS-MIB", "juniIsisCircIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisCircManL2Only"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1ISPriority"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1CircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1DesIS"),
        ("Juniper-ISIS-MIB", "juniIsisCircLANL1DesISChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2ISPriority"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2CircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2DesIS"),
        ("Juniper-ISIS-MIB", "juniIsisCircLANL2DesISChanges"),
        ("Juniper-ISIS-MIB", "juniIsisCircMCAddr"),
        ("Juniper-ISIS-MIB", "juniIsisCircPtToPtCircID"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1HelloTimer"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2HelloTimer"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1HelloMultiplier"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2HelloMultiplier"),
        ("Juniper-ISIS-MIB", "juniIsisCircMinLSPTransInt"),
        ("Juniper-ISIS-MIB", "juniIsisCircMinLSPReTransInt"),
        ("Juniper-ISIS-MIB", "juniIsisCircL1CSNPInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircL2CSNPInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircLSPThrottle"),
        ("Juniper-ISIS-MIB", "juniIsisCircMeshGroupEnabled"),
        ("Juniper-ISIS-MIB", "juniIsisCircMeshGroup"),
        ("Juniper-ISIS-MIB", "juniIsisCircLevel"),
        ("Juniper-ISIS-MIB", "juniIsisCircState"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1CircAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2CircAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    juniIsisCircuitMgmtGroup2.setStatus("current")

juniIsisSystemMgmtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 4)
)
juniIsisSystemMgmtGroup2.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisSysVersion"),
        ("Juniper-ISIS-MIB", "juniIsisSysType"),
        ("Juniper-ISIS-MIB", "juniIsisSysID"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxPathSplits"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigLSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddresses"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL1LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL2LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysPollESHelloRate"),
        ("Juniper-ISIS-MIB", "juniIsisSysWaitTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1State"),
        ("Juniper-ISIS-MIB", "juniIsisSysCorrLSPs"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL1DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysManAddrDropFromAreas"),
        ("Juniper-ISIS-MIB", "juniIsisSysAttmptToExMaxSeqNums"),
        ("Juniper-ISIS-MIB", "juniIsisSysSeqNumSkips"),
        ("Juniper-ISIS-MIB", "juniIsisSysOwnLSPPurges"),
        ("Juniper-ISIS-MIB", "juniIsisSysIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddrMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigL2LSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2State"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL2DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysAuthFails"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPIgnoreErrors"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaCheck"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBit"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBitStartupDuration"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLspLifetime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshHoldTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshConfigTimer"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistributeDomainWide"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistance"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysIsoRouteTag"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeRtrIdIfIndex"),
        ("Juniper-ISIS-MIB", "juniIsisManAreaAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysProtSuppRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameAreaAddr"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameName"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameType"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    juniIsisSystemMgmtGroup2.setStatus("obsolete")

juniIsisCircBFDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 5)
)
juniIsisCircBFDGroup.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisCircBfdEnable"),
        ("Juniper-ISIS-MIB", "juniIsisCircBfdMinRxInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircBfdMinTxInterval"),
        ("Juniper-ISIS-MIB", "juniIsisCircBfdMultiplier"))
)
if mibBuilder.loadTexts:
    juniIsisCircBFDGroup.setStatus("current")

juniIsisSystemMgmtGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 6)
)
juniIsisSystemMgmtGroup3.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisSysVersion"),
        ("Juniper-ISIS-MIB", "juniIsisSysType"),
        ("Juniper-ISIS-MIB", "juniIsisSysID"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxPathSplits"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigLSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddresses"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL1LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL2LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysPollESHelloRate"),
        ("Juniper-ISIS-MIB", "juniIsisSysWaitTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1State"),
        ("Juniper-ISIS-MIB", "juniIsisSysCorrLSPs"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL1DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysManAddrDropFromAreas"),
        ("Juniper-ISIS-MIB", "juniIsisSysAttmptToExMaxSeqNums"),
        ("Juniper-ISIS-MIB", "juniIsisSysSeqNumSkips"),
        ("Juniper-ISIS-MIB", "juniIsisSysOwnLSPPurges"),
        ("Juniper-ISIS-MIB", "juniIsisSysIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddrMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigL2LSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2State"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL2DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysAuthFails"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPIgnoreErrors"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaCheck"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBit"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBitStartupDuration"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLspLifetime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshHoldTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshConfigTimer"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistributeDomainWide"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistance"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysIsoRouteTag"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeRtrIdIfIndex"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeSpfUseAnyBestPath"),
        ("Juniper-ISIS-MIB", "juniIsisManAreaAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysProtSuppRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameAreaAddr"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameName"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameType"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeSystemId"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeRouterId"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelMetric"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelRelMetric"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelName"))
)
if mibBuilder.loadTexts:
    juniIsisSystemMgmtGroup3.setStatus("obsolete")

juniIsisSystemMgmtGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 2, 7)
)
juniIsisSystemMgmtGroup4.setObjects(
      *(("Juniper-ISIS-MIB", "juniIsisSysVersion"),
        ("Juniper-ISIS-MIB", "juniIsisSysType"),
        ("Juniper-ISIS-MIB", "juniIsisSysID"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxPathSplits"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigLSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddresses"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL1LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysMinL2LSPGenInt"),
        ("Juniper-ISIS-MIB", "juniIsisSysPollESHelloRate"),
        ("Juniper-ISIS-MIB", "juniIsisSysWaitTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1State"),
        ("Juniper-ISIS-MIB", "juniIsisSysCorrLSPs"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL1DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysManAddrDropFromAreas"),
        ("Juniper-ISIS-MIB", "juniIsisSysAttmptToExMaxSeqNums"),
        ("Juniper-ISIS-MIB", "juniIsisSysSeqNumSkips"),
        ("Juniper-ISIS-MIB", "juniIsisSysOwnLSPPurges"),
        ("Juniper-ISIS-MIB", "juniIsisSysIDFieldLenMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaAddrMismatches"),
        ("Juniper-ISIS-MIB", "juniIsisSysOrigL2LSPBuffSize"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2State"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPL2DbaseOloads"),
        ("Juniper-ISIS-MIB", "juniIsisSysAuthFails"),
        ("Juniper-ISIS-MIB", "juniIsisSysLSPIgnoreErrors"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxAreaCheck"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBit"),
        ("Juniper-ISIS-MIB", "juniIsisSysSetOverloadBitStartupDuration"),
        ("Juniper-ISIS-MIB", "juniIsisSysMaxLspLifetime"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2SpfInterval"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshHoldTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysIshConfigTimer"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistributeDomainWide"),
        ("Juniper-ISIS-MIB", "juniIsisSysDistance"),
        ("Juniper-ISIS-MIB", "juniIsisSysL1MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysL2MetricStyle"),
        ("Juniper-ISIS-MIB", "juniIsisSysIsoRouteTag"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeRtrIdIfIndex"),
        ("Juniper-ISIS-MIB", "juniIsisSysMplsTeSpfUseAnyBestPath"),
        ("Juniper-ISIS-MIB", "juniIsisSysReferenceBandwidth"),
        ("Juniper-ISIS-MIB", "juniIsisSysHighReferenceBandwidth"),
        ("Juniper-ISIS-MIB", "juniIsisManAreaAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysProtSuppRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrOperState"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDefaultMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrDelayMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrExpenseMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummAddrErrorMetric"),
        ("Juniper-ISIS-MIB", "juniIsisSummLevel"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameAreaAddr"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameName"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameType"),
        ("Juniper-ISIS-MIB", "juniIsisSysHostNameRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysAreaAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationPwd"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationKeyType"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStartGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopAcceptTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationStopGenerateTime"),
        ("Juniper-ISIS-MIB", "juniIsisSysDomainAuthenticationRowStatus"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeSystemId"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeRouterId"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelMetric"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelRelMetric"),
        ("Juniper-ISIS-MIB", "juniIsisMplsTeTunnelName"))
)
if mibBuilder.loadTexts:
    juniIsisSystemMgmtGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 1)
)
if mibBuilder.loadTexts:
    juniIsisCompliance.setStatus(
        "obsolete"
    )

juniIsisCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 2)
)
if mibBuilder.loadTexts:
    juniIsisCompliance2.setStatus(
        "obsolete"
    )

juniIsisCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 3)
)
if mibBuilder.loadTexts:
    juniIsisCompliance3.setStatus(
        "obsolete"
    )

juniIsisCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 4)
)
if mibBuilder.loadTexts:
    juniIsisCompliance4.setStatus(
        "obsolete"
    )

juniIsisCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 5)
)
if mibBuilder.loadTexts:
    juniIsisCompliance5.setStatus(
        "obsolete"
    )

juniIsisCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38, 3, 1, 6)
)
if mibBuilder.loadTexts:
    juniIsisCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ISIS-MIB",
    **{"OSINSAddress": OSINSAddress,
       "SystemID": SystemID,
       "OperState": OperState,
       "AuthTime": AuthTime,
       "LSPBuffSize": LSPBuffSize,
       "LevelState": LevelState,
       "SupportedProtocol": SupportedProtocol,
       "JuniDefaultMetric": JuniDefaultMetric,
       "OtherMetric": OtherMetric,
       "CircuitID": CircuitID,
       "ISPriority": ISPriority,
       "juniIsisMIB": juniIsisMIB,
       "juniIsisObjects": juniIsisObjects,
       "juniIsisSystemGroup": juniIsisSystemGroup,
       "juniIsisSysTable": juniIsisSysTable,
       "juniIsisSysEntry": juniIsisSysEntry,
       "juniIsisSysInstance": juniIsisSysInstance,
       "juniIsisSysVersion": juniIsisSysVersion,
       "juniIsisSysType": juniIsisSysType,
       "juniIsisSysID": juniIsisSysID,
       "juniIsisSysMaxPathSplits": juniIsisSysMaxPathSplits,
       "juniIsisSysMaxLSPGenInt": juniIsisSysMaxLSPGenInt,
       "juniIsisSysOrigLSPBuffSize": juniIsisSysOrigLSPBuffSize,
       "juniIsisSysMaxAreaAddresses": juniIsisSysMaxAreaAddresses,
       "juniIsisSysMinL1LSPGenInt": juniIsisSysMinL1LSPGenInt,
       "juniIsisSysMinL2LSPGenInt": juniIsisSysMinL2LSPGenInt,
       "juniIsisSysPollESHelloRate": juniIsisSysPollESHelloRate,
       "juniIsisSysWaitTime": juniIsisSysWaitTime,
       "juniIsisSysOperState": juniIsisSysOperState,
       "juniIsisSysL1State": juniIsisSysL1State,
       "juniIsisSysCorrLSPs": juniIsisSysCorrLSPs,
       "juniIsisSysLSPL1DbaseOloads": juniIsisSysLSPL1DbaseOloads,
       "juniIsisSysManAddrDropFromAreas": juniIsisSysManAddrDropFromAreas,
       "juniIsisSysAttmptToExMaxSeqNums": juniIsisSysAttmptToExMaxSeqNums,
       "juniIsisSysSeqNumSkips": juniIsisSysSeqNumSkips,
       "juniIsisSysOwnLSPPurges": juniIsisSysOwnLSPPurges,
       "juniIsisSysIDFieldLenMismatches": juniIsisSysIDFieldLenMismatches,
       "juniIsisSysMaxAreaAddrMismatches": juniIsisSysMaxAreaAddrMismatches,
       "juniIsisSysOrigL2LSPBuffSize": juniIsisSysOrigL2LSPBuffSize,
       "juniIsisSysL2State": juniIsisSysL2State,
       "juniIsisSysLSPL2DbaseOloads": juniIsisSysLSPL2DbaseOloads,
       "juniIsisSysAuthFails": juniIsisSysAuthFails,
       "juniIsisSysLSPIgnoreErrors": juniIsisSysLSPIgnoreErrors,
       "juniIsisSysMaxAreaCheck": juniIsisSysMaxAreaCheck,
       "juniIsisSysSetOverloadBit": juniIsisSysSetOverloadBit,
       "juniIsisSysSetOverloadBitStartupDuration": juniIsisSysSetOverloadBitStartupDuration,
       "juniIsisSysMaxLspLifetime": juniIsisSysMaxLspLifetime,
       "juniIsisSysL1SpfInterval": juniIsisSysL1SpfInterval,
       "juniIsisSysL2SpfInterval": juniIsisSysL2SpfInterval,
       "juniIsisSysIshHoldTime": juniIsisSysIshHoldTime,
       "juniIsisSysIshConfigTimer": juniIsisSysIshConfigTimer,
       "juniIsisSysDistributeDomainWide": juniIsisSysDistributeDomainWide,
       "juniIsisSysDistance": juniIsisSysDistance,
       "juniIsisSysL1MetricStyle": juniIsisSysL1MetricStyle,
       "juniIsisSysL2MetricStyle": juniIsisSysL2MetricStyle,
       "juniIsisSysIsoRouteTag": juniIsisSysIsoRouteTag,
       "juniIsisSysMplsTeLevel": juniIsisSysMplsTeLevel,
       "juniIsisSysMplsTeRtrIdIfIndex": juniIsisSysMplsTeRtrIdIfIndex,
       "juniIsisSysMplsTeSpfUseAnyBestPath": juniIsisSysMplsTeSpfUseAnyBestPath,
       "juniIsisSysReferenceBandwidth": juniIsisSysReferenceBandwidth,
       "juniIsisSysHighReferenceBandwidth": juniIsisSysHighReferenceBandwidth,
       "juniIsisManAreaAddrTable": juniIsisManAreaAddrTable,
       "juniIsisManAreaAddrEntry": juniIsisManAreaAddrEntry,
       "juniIsisManAreaAddrSysInstance": juniIsisManAreaAddrSysInstance,
       "juniIsisManAreaAddr": juniIsisManAreaAddr,
       "juniIsisManAreaAddrRowStatus": juniIsisManAreaAddrRowStatus,
       "juniIsisSysProtSuppTable": juniIsisSysProtSuppTable,
       "juniIsisSysProtSuppEntry": juniIsisSysProtSuppEntry,
       "juniIsisSysProtSuppSysInstance": juniIsisSysProtSuppSysInstance,
       "juniIsisSysProtSuppProtocol": juniIsisSysProtSuppProtocol,
       "juniIsisSysProtSuppRowStatus": juniIsisSysProtSuppRowStatus,
       "juniIsisSummAddrTable": juniIsisSummAddrTable,
       "juniIsisSummAddrEntry": juniIsisSummAddrEntry,
       "juniIsisSummAddrSysInstance": juniIsisSummAddrSysInstance,
       "juniIsisSummAddress": juniIsisSummAddress,
       "juniIsisSummAddrMask": juniIsisSummAddrMask,
       "juniIsisSummAddrRowStatus": juniIsisSummAddrRowStatus,
       "juniIsisSummAddrOperState": juniIsisSummAddrOperState,
       "juniIsisSummAddrDefaultMetric": juniIsisSummAddrDefaultMetric,
       "juniIsisSummAddrDelayMetric": juniIsisSummAddrDelayMetric,
       "juniIsisSummAddrExpenseMetric": juniIsisSummAddrExpenseMetric,
       "juniIsisSummAddrErrorMetric": juniIsisSummAddrErrorMetric,
       "juniIsisSummLevel": juniIsisSummLevel,
       "juniIsisSysHostNameTable": juniIsisSysHostNameTable,
       "juniIsisSysHostNameEntry": juniIsisSysHostNameEntry,
       "juniIsisSysHostNameSysInstance": juniIsisSysHostNameSysInstance,
       "juniIsisSysHostNameSysId": juniIsisSysHostNameSysId,
       "juniIsisSysHostNameAreaAddr": juniIsisSysHostNameAreaAddr,
       "juniIsisSysHostNameName": juniIsisSysHostNameName,
       "juniIsisSysHostNameType": juniIsisSysHostNameType,
       "juniIsisSysHostNameRowStatus": juniIsisSysHostNameRowStatus,
       "juniIsisSysAreaAuthenticationTable": juniIsisSysAreaAuthenticationTable,
       "juniIsisSysAreaAuthenticationEntry": juniIsisSysAreaAuthenticationEntry,
       "juniIsisSysAreaAuthenticationSysInstance": juniIsisSysAreaAuthenticationSysInstance,
       "juniIsisSysAreaAuthenticationKeyId": juniIsisSysAreaAuthenticationKeyId,
       "juniIsisSysAreaAuthenticationPwd": juniIsisSysAreaAuthenticationPwd,
       "juniIsisSysAreaAuthenticationKeyType": juniIsisSysAreaAuthenticationKeyType,
       "juniIsisSysAreaAuthenticationStartAcceptTime": juniIsisSysAreaAuthenticationStartAcceptTime,
       "juniIsisSysAreaAuthenticationStartGenerateTime": juniIsisSysAreaAuthenticationStartGenerateTime,
       "juniIsisSysAreaAuthenticationStopAcceptTime": juniIsisSysAreaAuthenticationStopAcceptTime,
       "juniIsisSysAreaAuthenticationStopGenerateTime": juniIsisSysAreaAuthenticationStopGenerateTime,
       "juniIsisSysAreaAuthenticationRowStatus": juniIsisSysAreaAuthenticationRowStatus,
       "juniIsisSysDomainAuthenticationTable": juniIsisSysDomainAuthenticationTable,
       "juniIsisSysDomainAuthenticationEntry": juniIsisSysDomainAuthenticationEntry,
       "juniIsisSysDomainAuthenticationSysInstance": juniIsisSysDomainAuthenticationSysInstance,
       "juniIsisSysDomainAuthenticationKeyId": juniIsisSysDomainAuthenticationKeyId,
       "juniIsisSysDomainAuthenticationPwd": juniIsisSysDomainAuthenticationPwd,
       "juniIsisSysDomainAuthenticationKeyType": juniIsisSysDomainAuthenticationKeyType,
       "juniIsisSysDomainAuthenticationStartAcceptTime": juniIsisSysDomainAuthenticationStartAcceptTime,
       "juniIsisSysDomainAuthenticationStartGenerateTime": juniIsisSysDomainAuthenticationStartGenerateTime,
       "juniIsisSysDomainAuthenticationStopAcceptTime": juniIsisSysDomainAuthenticationStopAcceptTime,
       "juniIsisSysDomainAuthenticationStopGenerateTime": juniIsisSysDomainAuthenticationStopGenerateTime,
       "juniIsisSysDomainAuthenticationRowStatus": juniIsisSysDomainAuthenticationRowStatus,
       "juniIsisMplsTeTunnelTable": juniIsisMplsTeTunnelTable,
       "juniIsisMplsTeTunnelEntry": juniIsisMplsTeTunnelEntry,
       "juniIsisMplsTeTunnelSysInstance": juniIsisMplsTeTunnelSysInstance,
       "juniIsisMplsNextHopIndex": juniIsisMplsNextHopIndex,
       "juniIsisMplsTeSystemId": juniIsisMplsTeSystemId,
       "juniIsisMplsTeRouterId": juniIsisMplsTeRouterId,
       "juniIsisMplsTeTunnelMetric": juniIsisMplsTeTunnelMetric,
       "juniIsisMplsTeTunnelRelMetric": juniIsisMplsTeTunnelRelMetric,
       "juniIsisMplsTeTunnelName": juniIsisMplsTeTunnelName,
       "juniIsisCircuitGroup": juniIsisCircuitGroup,
       "juniIsisCircTable": juniIsisCircTable,
       "juniIsisCircEntry": juniIsisCircEntry,
       "juniIsisCircSysInstance": juniIsisCircSysInstance,
       "juniIsisCircIfIndex": juniIsisCircIfIndex,
       "juniIsisCircLocalID": juniIsisCircLocalID,
       "juniIsisCircOperState": juniIsisCircOperState,
       "juniIsisCircRowStatus": juniIsisCircRowStatus,
       "juniIsisCircType": juniIsisCircType,
       "juniIsisCircL1DefaultMetric": juniIsisCircL1DefaultMetric,
       "juniIsisCircL1DelayMetric": juniIsisCircL1DelayMetric,
       "juniIsisCircL1ExpenseMetric": juniIsisCircL1ExpenseMetric,
       "juniIsisCircL1ErrorMetric": juniIsisCircL1ErrorMetric,
       "juniIsisCircExtDomain": juniIsisCircExtDomain,
       "juniIsisCircAdjChanges": juniIsisCircAdjChanges,
       "juniIsisCircInitFails": juniIsisCircInitFails,
       "juniIsisCircRejAdjs": juniIsisCircRejAdjs,
       "juniIsisCircOutCtrlPDUs": juniIsisCircOutCtrlPDUs,
       "juniIsisCircInCtrlPDUs": juniIsisCircInCtrlPDUs,
       "juniIsisCircIDFieldLenMismatches": juniIsisCircIDFieldLenMismatches,
       "juniIsisCircL2DefaultMetric": juniIsisCircL2DefaultMetric,
       "juniIsisCircL2DelayMetric": juniIsisCircL2DelayMetric,
       "juniIsisCircL2ExpenseMetric": juniIsisCircL2ExpenseMetric,
       "juniIsisCircL2ErrorMetric": juniIsisCircL2ErrorMetric,
       "juniIsisCircManL2Only": juniIsisCircManL2Only,
       "juniIsisCircL1ISPriority": juniIsisCircL1ISPriority,
       "juniIsisCircL1CircID": juniIsisCircL1CircID,
       "juniIsisCircL1DesIS": juniIsisCircL1DesIS,
       "juniIsisCircLANL1DesISChanges": juniIsisCircLANL1DesISChanges,
       "juniIsisCircL2ISPriority": juniIsisCircL2ISPriority,
       "juniIsisCircL2CircID": juniIsisCircL2CircID,
       "juniIsisCircL2DesIS": juniIsisCircL2DesIS,
       "juniIsisCircLANL2DesISChanges": juniIsisCircLANL2DesISChanges,
       "juniIsisCircMCAddr": juniIsisCircMCAddr,
       "juniIsisCircPtToPtCircID": juniIsisCircPtToPtCircID,
       "juniIsisCircL1HelloTimer": juniIsisCircL1HelloTimer,
       "juniIsisCircL2HelloTimer": juniIsisCircL2HelloTimer,
       "juniIsisCircL1HelloMultiplier": juniIsisCircL1HelloMultiplier,
       "juniIsisCircL2HelloMultiplier": juniIsisCircL2HelloMultiplier,
       "juniIsisCircMinLSPTransInt": juniIsisCircMinLSPTransInt,
       "juniIsisCircMinLSPReTransInt": juniIsisCircMinLSPReTransInt,
       "juniIsisCircL1CSNPInterval": juniIsisCircL1CSNPInterval,
       "juniIsisCircL2CSNPInterval": juniIsisCircL2CSNPInterval,
       "juniIsisCircLSPThrottle": juniIsisCircLSPThrottle,
       "juniIsisCircMeshGroupEnabled": juniIsisCircMeshGroupEnabled,
       "juniIsisCircMeshGroup": juniIsisCircMeshGroup,
       "juniIsisCircLevel": juniIsisCircLevel,
       "juniIsisCircState": juniIsisCircState,
       "juniIsisSysL1CircAuthenticationTable": juniIsisSysL1CircAuthenticationTable,
       "juniIsisSysL1CircAuthenticationEntry": juniIsisSysL1CircAuthenticationEntry,
       "juniIsisSysL1CircAuthenticationSysInstance": juniIsisSysL1CircAuthenticationSysInstance,
       "juniIsisSysL1CircAuthenticationIfIndex": juniIsisSysL1CircAuthenticationIfIndex,
       "juniIsisSysL1CircAuthenticationKeyId": juniIsisSysL1CircAuthenticationKeyId,
       "juniIsisSysL1CircAuthenticationPwd": juniIsisSysL1CircAuthenticationPwd,
       "juniIsisSysL1CircAuthenticationKeyType": juniIsisSysL1CircAuthenticationKeyType,
       "juniIsisSysL1CircAuthenticationStartAcceptTime": juniIsisSysL1CircAuthenticationStartAcceptTime,
       "juniIsisSysL1CircAuthenticationStartGenerateTime": juniIsisSysL1CircAuthenticationStartGenerateTime,
       "juniIsisSysL1CircAuthenticationStopAcceptTime": juniIsisSysL1CircAuthenticationStopAcceptTime,
       "juniIsisSysL1CircAuthenticationStopGenerateTime": juniIsisSysL1CircAuthenticationStopGenerateTime,
       "juniIsisSysL1CircAuthenticationRowStatus": juniIsisSysL1CircAuthenticationRowStatus,
       "juniIsisSysL2CircAuthenticationTable": juniIsisSysL2CircAuthenticationTable,
       "juniIsisSysL2CircAuthenticationEntry": juniIsisSysL2CircAuthenticationEntry,
       "juniIsisSysL2CircAuthenticationSysInstance": juniIsisSysL2CircAuthenticationSysInstance,
       "juniIsisSysL2CircAuthenticationIfIndex": juniIsisSysL2CircAuthenticationIfIndex,
       "juniIsisSysL2CircAuthenticationKeyId": juniIsisSysL2CircAuthenticationKeyId,
       "juniIsisSysL2CircAuthenticationPwd": juniIsisSysL2CircAuthenticationPwd,
       "juniIsisSysL2CircAuthenticationKeyType": juniIsisSysL2CircAuthenticationKeyType,
       "juniIsisSysL2CircAuthenticationStartAcceptTime": juniIsisSysL2CircAuthenticationStartAcceptTime,
       "juniIsisSysL2CircAuthenticationStartGenerateTime": juniIsisSysL2CircAuthenticationStartGenerateTime,
       "juniIsisSysL2CircAuthenticationStopAcceptTime": juniIsisSysL2CircAuthenticationStopAcceptTime,
       "juniIsisSysL2CircAuthenticationStopGenerateTime": juniIsisSysL2CircAuthenticationStopGenerateTime,
       "juniIsisSysL2CircAuthenticationRowStatus": juniIsisSysL2CircAuthenticationRowStatus,
       "juniIsisCircBFDTable": juniIsisCircBFDTable,
       "juniIsisCircBFDEntry": juniIsisCircBFDEntry,
       "juniIsisCircBfdEnable": juniIsisCircBfdEnable,
       "juniIsisCircBfdMinRxInterval": juniIsisCircBfdMinRxInterval,
       "juniIsisCircBfdMinTxInterval": juniIsisCircBfdMinTxInterval,
       "juniIsisCircBfdMultiplier": juniIsisCircBfdMultiplier,
       "juniIsisTrapGroup": juniIsisTrapGroup,
       "juniIsisConformance": juniIsisConformance,
       "juniIsisCompliances": juniIsisCompliances,
       "juniIsisCompliance": juniIsisCompliance,
       "juniIsisCompliance2": juniIsisCompliance2,
       "juniIsisCompliance3": juniIsisCompliance3,
       "juniIsisCompliance4": juniIsisCompliance4,
       "juniIsisCompliance5": juniIsisCompliance5,
       "juniIsisCompliance6": juniIsisCompliance6,
       "juniIsisMIBGroups": juniIsisMIBGroups,
       "juniIsisSystemMgmtGroup": juniIsisSystemMgmtGroup,
       "juniIsisCircuitMgmtGroup": juniIsisCircuitMgmtGroup,
       "juniIsisCircuitMgmtGroup2": juniIsisCircuitMgmtGroup2,
       "juniIsisSystemMgmtGroup2": juniIsisSystemMgmtGroup2,
       "juniIsisCircBFDGroup": juniIsisCircBFDGroup,
       "juniIsisSystemMgmtGroup3": juniIsisSystemMgmtGroup3,
       "juniIsisSystemMgmtGroup4": juniIsisSystemMgmtGroup4}
)
