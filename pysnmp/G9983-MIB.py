# SNMP MIB module (G9983-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G9983-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:36 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

g9983MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 210)
)
g9983MIB.setRevisions(
        ("2013-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class G9983SvcIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class G9983SvcIndexList(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )



class G9983SvcOrderIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )



# MIB Managed Objects in the order of their OIDs

_G9983Objects_ObjectIdentity = ObjectIdentity
g9983Objects = _G9983Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 1)
)
_G9983Port_ObjectIdentity = ObjectIdentity
g9983Port = _G9983Port_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 1, 1)
)
_G9983PortNotifications_ObjectIdentity = ObjectIdentity
g9983PortNotifications = _G9983PortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 0)
)
_G9983PortConfTable_Object = MibTable
g9983PortConfTable = _G9983PortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1)
)
if mibBuilder.loadTexts:
    g9983PortConfTable.setStatus("current")
_G9983PortConfEntry_Object = MibTableRow
g9983PortConfEntry = _G9983PortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1)
)
g9983PortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9983PortConfEntry.setStatus("current")
_G9983PortConfFecAdminState_Type = TruthValue
_G9983PortConfFecAdminState_Object = MibTableColumn
g9983PortConfFecAdminState = _G9983PortConfFecAdminState_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 1),
    _G9983PortConfFecAdminState_Type()
)
g9983PortConfFecAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfFecAdminState.setStatus("current")


class _G9983PortConfFecWordSize_Type(Unsigned32):
    """Custom type g9983PortConfFecWordSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_G9983PortConfFecWordSize_Type.__name__ = "Unsigned32"
_G9983PortConfFecWordSize_Object = MibTableColumn
g9983PortConfFecWordSize = _G9983PortConfFecWordSize_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 2),
    _G9983PortConfFecWordSize_Type()
)
g9983PortConfFecWordSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfFecWordSize.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortConfFecWordSize.setUnits("octets")


class _G9983PortConfFecRedundancySize_Type(Unsigned32):
    """Custom type g9983PortConfFecRedundancySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
    )


_G9983PortConfFecRedundancySize_Type.__name__ = "Unsigned32"
_G9983PortConfFecRedundancySize_Object = MibTableColumn
g9983PortConfFecRedundancySize = _G9983PortConfFecRedundancySize_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 3),
    _G9983PortConfFecRedundancySize_Type()
)
g9983PortConfFecRedundancySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfFecRedundancySize.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortConfFecRedundancySize.setUnits("octets")


class _G9983PortConfFecInterleaverType_Type(Integer32):
    """Custom type g9983PortConfFecInterleaverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("convolution", 2),
          ("none", 0))
    )


_G9983PortConfFecInterleaverType_Type.__name__ = "Integer32"
_G9983PortConfFecInterleaverType_Object = MibTableColumn
g9983PortConfFecInterleaverType = _G9983PortConfFecInterleaverType_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 4),
    _G9983PortConfFecInterleaverType_Type()
)
g9983PortConfFecInterleaverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfFecInterleaverType.setStatus("current")


class _G9983PortConfFecInterleaverDepth_Type(Unsigned32):
    """Custom type g9983PortConfFecInterleaverDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(96, 96),
    )


_G9983PortConfFecInterleaverDepth_Type.__name__ = "Unsigned32"
_G9983PortConfFecInterleaverDepth_Object = MibTableColumn
g9983PortConfFecInterleaverDepth = _G9983PortConfFecInterleaverDepth_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 5),
    _G9983PortConfFecInterleaverDepth_Type()
)
g9983PortConfFecInterleaverDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfFecInterleaverDepth.setStatus("current")
_G9983PortConfAdminServices_Type = G9983SvcIndexList
_G9983PortConfAdminServices_Object = MibTableColumn
g9983PortConfAdminServices = _G9983PortConfAdminServices_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 6),
    _G9983PortConfAdminServices_Type()
)
g9983PortConfAdminServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfAdminServices.setStatus("current")
_G9983PortConfSvcUpDownEnable_Type = TruthValue
_G9983PortConfSvcUpDownEnable_Object = MibTableColumn
g9983PortConfSvcUpDownEnable = _G9983PortConfSvcUpDownEnable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 1, 1, 7),
    _G9983PortConfSvcUpDownEnable_Type()
)
g9983PortConfSvcUpDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9983PortConfSvcUpDownEnable.setStatus("current")
_G9983PortCapTable_Object = MibTable
g9983PortCapTable = _G9983PortCapTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2)
)
if mibBuilder.loadTexts:
    g9983PortCapTable.setStatus("current")
_G9983PortCapEntry_Object = MibTableRow
g9983PortCapEntry = _G9983PortCapEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1)
)
g9983PortCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9983PortCapEntry.setStatus("current")
_G9983PortCapFecSupported_Type = TruthValue
_G9983PortCapFecSupported_Object = MibTableColumn
g9983PortCapFecSupported = _G9983PortCapFecSupported_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1, 1),
    _G9983PortCapFecSupported_Type()
)
g9983PortCapFecSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortCapFecSupported.setStatus("current")


class _G9983PortCapFecMaxWordSize_Type(Unsigned32):
    """Custom type g9983PortCapFecMaxWordSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_G9983PortCapFecMaxWordSize_Type.__name__ = "Unsigned32"
_G9983PortCapFecMaxWordSize_Object = MibTableColumn
g9983PortCapFecMaxWordSize = _G9983PortCapFecMaxWordSize_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1, 2),
    _G9983PortCapFecMaxWordSize_Type()
)
g9983PortCapFecMaxWordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortCapFecMaxWordSize.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortCapFecMaxWordSize.setUnits("octets")


class _G9983PortCapFecMaxRedundancySize_Type(Unsigned32):
    """Custom type g9983PortCapFecMaxRedundancySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
    )


_G9983PortCapFecMaxRedundancySize_Type.__name__ = "Unsigned32"
_G9983PortCapFecMaxRedundancySize_Object = MibTableColumn
g9983PortCapFecMaxRedundancySize = _G9983PortCapFecMaxRedundancySize_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1, 3),
    _G9983PortCapFecMaxRedundancySize_Type()
)
g9983PortCapFecMaxRedundancySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortCapFecMaxRedundancySize.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortCapFecMaxRedundancySize.setUnits("octets")


class _G9983PortCapFecInterleaverTypeSupported_Type(Integer32):
    """Custom type g9983PortCapFecInterleaverTypeSupported based on Integer32"""
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
        *(("block", 1),
          ("blockConvolution", 3),
          ("convolution", 2),
          ("none", 0))
    )


_G9983PortCapFecInterleaverTypeSupported_Type.__name__ = "Integer32"
_G9983PortCapFecInterleaverTypeSupported_Object = MibTableColumn
g9983PortCapFecInterleaverTypeSupported = _G9983PortCapFecInterleaverTypeSupported_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1, 4),
    _G9983PortCapFecInterleaverTypeSupported_Type()
)
g9983PortCapFecInterleaverTypeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortCapFecInterleaverTypeSupported.setStatus("current")


class _G9983PortCapFecMaxInterleaverDepth_Type(Unsigned32):
    """Custom type g9983PortCapFecMaxInterleaverDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(96, 96),
    )


_G9983PortCapFecMaxInterleaverDepth_Type.__name__ = "Unsigned32"
_G9983PortCapFecMaxInterleaverDepth_Object = MibTableColumn
g9983PortCapFecMaxInterleaverDepth = _G9983PortCapFecMaxInterleaverDepth_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 2, 1, 5),
    _G9983PortCapFecMaxInterleaverDepth_Type()
)
g9983PortCapFecMaxInterleaverDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortCapFecMaxInterleaverDepth.setStatus("current")
_G9983PortStatTable_Object = MibTable
g9983PortStatTable = _G9983PortStatTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3)
)
if mibBuilder.loadTexts:
    g9983PortStatTable.setStatus("current")
_G9983PortStatEntry_Object = MibTableRow
g9983PortStatEntry = _G9983PortStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1)
)
g9983PortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9983PortStatEntry.setStatus("current")
_G9983PortStatFecOperState_Type = TruthValue
_G9983PortStatFecOperState_Object = MibTableColumn
g9983PortStatFecOperState = _G9983PortStatFecOperState_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1, 1),
    _G9983PortStatFecOperState_Type()
)
g9983PortStatFecOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortStatFecOperState.setStatus("current")


class _G9983PortStatFltStatus_Type(Bits):
    """Custom type g9983PortStatFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("serviceDown", 0),
          ("wrongConfig", 1))
    )

_G9983PortStatFltStatus_Type.__name__ = "Bits"
_G9983PortStatFltStatus_Object = MibTableColumn
g9983PortStatFltStatus = _G9983PortStatFltStatus_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1, 2),
    _G9983PortStatFltStatus_Type()
)
g9983PortStatFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortStatFltStatus.setStatus("current")
_G9983PortStatCrc4Errors_Type = Counter32
_G9983PortStatCrc4Errors_Object = MibTableColumn
g9983PortStatCrc4Errors = _G9983PortStatCrc4Errors_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1, 3),
    _G9983PortStatCrc4Errors_Type()
)
g9983PortStatCrc4Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortStatCrc4Errors.setStatus("current")
_G9983PortStatCrc6Errors_Type = Counter32
_G9983PortStatCrc6Errors_Object = MibTableColumn
g9983PortStatCrc6Errors = _G9983PortStatCrc6Errors_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1, 4),
    _G9983PortStatCrc6Errors_Type()
)
g9983PortStatCrc6Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortStatCrc6Errors.setStatus("current")
_G9983PortStatCrc8Errors_Type = Counter32
_G9983PortStatCrc8Errors_Object = MibTableColumn
g9983PortStatCrc8Errors = _G9983PortStatCrc8Errors_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 3, 1, 5),
    _G9983PortStatCrc8Errors_Type()
)
g9983PortStatCrc8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortStatCrc8Errors.setStatus("current")
_G9983OperSvcTable_Object = MibTable
g9983OperSvcTable = _G9983OperSvcTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 4)
)
if mibBuilder.loadTexts:
    g9983OperSvcTable.setStatus("current")
_G9983OperSvcEntry_Object = MibTableRow
g9983OperSvcEntry = _G9983OperSvcEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 4, 1)
)
g9983OperSvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983OperSvcPosition"),
)
if mibBuilder.loadTexts:
    g9983OperSvcEntry.setStatus("current")
_G9983OperSvcPosition_Type = G9983SvcOrderIndex
_G9983OperSvcPosition_Object = MibTableColumn
g9983OperSvcPosition = _G9983OperSvcPosition_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 4, 1, 1),
    _G9983OperSvcPosition_Type()
)
g9983OperSvcPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983OperSvcPosition.setStatus("current")
_G9983OperSvcIdx_Type = G9983SvcIndex
_G9983OperSvcIdx_Object = MibTableColumn
g9983OperSvcIdx = _G9983OperSvcIdx_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 4, 1, 2),
    _G9983OperSvcIdx_Type()
)
g9983OperSvcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983OperSvcIdx.setStatus("current")


class _G9983OperSvcState_Type(Integer32):
    """Custom type g9983OperSvcState based on Integer32"""
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


_G9983OperSvcState_Type.__name__ = "Integer32"
_G9983OperSvcState_Object = MibTableColumn
g9983OperSvcState = _G9983OperSvcState_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 4, 1, 3),
    _G9983OperSvcState_Type()
)
g9983OperSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983OperSvcState.setStatus("current")
_G9983SvcTable_Object = MibTable
g9983SvcTable = _G9983SvcTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5)
)
if mibBuilder.loadTexts:
    g9983SvcTable.setStatus("current")
_G9983SvcEntry_Object = MibTableRow
g9983SvcEntry = _G9983SvcEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1)
)
g9983SvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983SvcIdx"),
)
if mibBuilder.loadTexts:
    g9983SvcEntry.setStatus("current")
_G9983SvcIdx_Type = G9983SvcIndex
_G9983SvcIdx_Object = MibTableColumn
g9983SvcIdx = _G9983SvcIdx_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1, 1),
    _G9983SvcIdx_Type()
)
g9983SvcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983SvcIdx.setStatus("current")
_G9983SvcIfIdx_Type = InterfaceIndex
_G9983SvcIfIdx_Object = MibTableColumn
g9983SvcIfIdx = _G9983SvcIfIdx_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1, 2),
    _G9983SvcIfIdx_Type()
)
g9983SvcIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    g9983SvcIfIdx.setStatus("current")


class _G9983SvcType_Type(Integer32):
    """Custom type g9983SvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("atm", 8),
          ("clock", 6),
          ("ds1", 0),
          ("ds3", 4),
          ("e1", 1),
          ("e3", 5),
          ("ethernet", 7),
          ("gfp", 10),
          ("gfpNoFCS", 9),
          ("nxds0", 2),
          ("nxe0", 3))
    )


_G9983SvcType_Type.__name__ = "Integer32"
_G9983SvcType_Object = MibTableColumn
g9983SvcType = _G9983SvcType_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1, 3),
    _G9983SvcType_Type()
)
g9983SvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    g9983SvcType.setStatus("current")


class _G9983SvcSize_Type(Unsigned32):
    """Custom type g9983SvcSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_G9983SvcSize_Type.__name__ = "Unsigned32"
_G9983SvcSize_Object = MibTableColumn
g9983SvcSize = _G9983SvcSize_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1, 4),
    _G9983SvcSize_Type()
)
g9983SvcSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    g9983SvcSize.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcSize.setUnits("octets")
_G9983SvcRowStatus_Type = RowStatus
_G9983SvcRowStatus_Object = MibTableColumn
g9983SvcRowStatus = _G9983SvcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 5, 1, 5),
    _G9983SvcRowStatus_Type()
)
g9983SvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    g9983SvcRowStatus.setStatus("current")
_G9983PM_ObjectIdentity = ObjectIdentity
g9983PM = _G9983PM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6)
)
_G9983PortPmCurTable_Object = MibTable
g9983PortPmCurTable = _G9983PortPmCurTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    g9983PortPmCurTable.setStatus("current")
_G9983PortPmCurEntry_Object = MibTableRow
g9983PortPmCurEntry = _G9983PortPmCurEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1)
)
g9983PortPmCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9983PortPmCurEntry.setStatus("current")
_G9983PortPmCur15MinValidIntervals_Type = HCPerfValidIntervals
_G9983PortPmCur15MinValidIntervals_Object = MibTableColumn
g9983PortPmCur15MinValidIntervals = _G9983PortPmCur15MinValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 1),
    _G9983PortPmCur15MinValidIntervals_Type()
)
g9983PortPmCur15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinValidIntervals.setStatus("current")
_G9983PortPmCur15MinInvalidIntervals_Type = HCPerfInvalidIntervals
_G9983PortPmCur15MinInvalidIntervals_Object = MibTableColumn
g9983PortPmCur15MinInvalidIntervals = _G9983PortPmCur15MinInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 2),
    _G9983PortPmCur15MinInvalidIntervals_Type()
)
g9983PortPmCur15MinInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinInvalidIntervals.setStatus("current")
_G9983PortPmCur15MinTimeElapsed_Type = HCPerfTimeElapsed
_G9983PortPmCur15MinTimeElapsed_Object = MibTableColumn
g9983PortPmCur15MinTimeElapsed = _G9983PortPmCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 3),
    _G9983PortPmCur15MinTimeElapsed_Type()
)
g9983PortPmCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinTimeElapsed.setUnits("seconds")
_G9983PortPmCur15MinCrc4s_Type = HCPerfCurrentCount
_G9983PortPmCur15MinCrc4s_Object = MibTableColumn
g9983PortPmCur15MinCrc4s = _G9983PortPmCur15MinCrc4s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 4),
    _G9983PortPmCur15MinCrc4s_Type()
)
g9983PortPmCur15MinCrc4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinCrc4s.setStatus("current")
_G9983PortPmCur15MinCrc6s_Type = HCPerfCurrentCount
_G9983PortPmCur15MinCrc6s_Object = MibTableColumn
g9983PortPmCur15MinCrc6s = _G9983PortPmCur15MinCrc6s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 5),
    _G9983PortPmCur15MinCrc6s_Type()
)
g9983PortPmCur15MinCrc6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinCrc6s.setStatus("current")
_G9983PortPmCur15MinCrc8s_Type = HCPerfCurrentCount
_G9983PortPmCur15MinCrc8s_Object = MibTableColumn
g9983PortPmCur15MinCrc8s = _G9983PortPmCur15MinCrc8s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 6),
    _G9983PortPmCur15MinCrc8s_Type()
)
g9983PortPmCur15MinCrc8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur15MinCrc8s.setStatus("current")


class _G9983PortPmCur1DayValidIntervals_Type(Unsigned32):
    """Custom type g9983PortPmCur1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9983PortPmCur1DayValidIntervals_Type.__name__ = "Unsigned32"
_G9983PortPmCur1DayValidIntervals_Object = MibTableColumn
g9983PortPmCur1DayValidIntervals = _G9983PortPmCur1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 7),
    _G9983PortPmCur1DayValidIntervals_Type()
)
g9983PortPmCur1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayValidIntervals.setStatus("current")


class _G9983PortPmCur1DayInvalidIntervals_Type(Unsigned32):
    """Custom type g9983PortPmCur1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9983PortPmCur1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_G9983PortPmCur1DayInvalidIntervals_Object = MibTableColumn
g9983PortPmCur1DayInvalidIntervals = _G9983PortPmCur1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 8),
    _G9983PortPmCur1DayInvalidIntervals_Type()
)
g9983PortPmCur1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayInvalidIntervals.setStatus("current")
_G9983PortPmCur1DayTimeElapsed_Type = HCPerfTimeElapsed
_G9983PortPmCur1DayTimeElapsed_Object = MibTableColumn
g9983PortPmCur1DayTimeElapsed = _G9983PortPmCur1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 9),
    _G9983PortPmCur1DayTimeElapsed_Type()
)
g9983PortPmCur1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayTimeElapsed.setUnits("seconds")
_G9983PortPmCur1DayCrc4s_Type = HCPerfCurrentCount
_G9983PortPmCur1DayCrc4s_Object = MibTableColumn
g9983PortPmCur1DayCrc4s = _G9983PortPmCur1DayCrc4s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 10),
    _G9983PortPmCur1DayCrc4s_Type()
)
g9983PortPmCur1DayCrc4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayCrc4s.setStatus("current")
_G9983PortPmCur1DayCrc6s_Type = HCPerfCurrentCount
_G9983PortPmCur1DayCrc6s_Object = MibTableColumn
g9983PortPmCur1DayCrc6s = _G9983PortPmCur1DayCrc6s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 11),
    _G9983PortPmCur1DayCrc6s_Type()
)
g9983PortPmCur1DayCrc6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayCrc6s.setStatus("current")
_G9983PortPmCur1DayCrc8s_Type = HCPerfCurrentCount
_G9983PortPmCur1DayCrc8s_Object = MibTableColumn
g9983PortPmCur1DayCrc8s = _G9983PortPmCur1DayCrc8s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 1, 1, 12),
    _G9983PortPmCur1DayCrc8s_Type()
)
g9983PortPmCur1DayCrc8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPmCur1DayCrc8s.setStatus("current")
_G9983PortPm15MinTable_Object = MibTable
g9983PortPm15MinTable = _G9983PortPm15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    g9983PortPm15MinTable.setStatus("current")
_G9983PortPm15MinEntry_Object = MibTableRow
g9983PortPm15MinEntry = _G9983PortPm15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1)
)
g9983PortPm15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983PortPm15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9983PortPm15MinEntry.setStatus("current")


class _G9983PortPm15MinIntervalIndex_Type(Unsigned32):
    """Custom type g9983PortPm15MinIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_G9983PortPm15MinIntervalIndex_Type.__name__ = "Unsigned32"
_G9983PortPm15MinIntervalIndex_Object = MibTableColumn
g9983PortPm15MinIntervalIndex = _G9983PortPm15MinIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 1),
    _G9983PortPm15MinIntervalIndex_Type()
)
g9983PortPm15MinIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalIndex.setStatus("current")
_G9983PortPm15MinIntervalMoniTime_Type = HCPerfTimeElapsed
_G9983PortPm15MinIntervalMoniTime_Object = MibTableColumn
g9983PortPm15MinIntervalMoniTime = _G9983PortPm15MinIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 2),
    _G9983PortPm15MinIntervalMoniTime_Type()
)
g9983PortPm15MinIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalMoniTime.setUnits("seconds")
_G9983PortPm15MinIntervalCrc4s_Type = HCPerfIntervalCount
_G9983PortPm15MinIntervalCrc4s_Object = MibTableColumn
g9983PortPm15MinIntervalCrc4s = _G9983PortPm15MinIntervalCrc4s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 3),
    _G9983PortPm15MinIntervalCrc4s_Type()
)
g9983PortPm15MinIntervalCrc4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalCrc4s.setStatus("current")
_G9983PortPm15MinIntervalCrc6s_Type = HCPerfIntervalCount
_G9983PortPm15MinIntervalCrc6s_Object = MibTableColumn
g9983PortPm15MinIntervalCrc6s = _G9983PortPm15MinIntervalCrc6s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 4),
    _G9983PortPm15MinIntervalCrc6s_Type()
)
g9983PortPm15MinIntervalCrc6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalCrc6s.setStatus("current")
_G9983PortPm15MinIntervalCrc8s_Type = HCPerfIntervalCount
_G9983PortPm15MinIntervalCrc8s_Object = MibTableColumn
g9983PortPm15MinIntervalCrc8s = _G9983PortPm15MinIntervalCrc8s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 5),
    _G9983PortPm15MinIntervalCrc8s_Type()
)
g9983PortPm15MinIntervalCrc8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalCrc8s.setStatus("current")
_G9983PortPm15MinIntervalValid_Type = TruthValue
_G9983PortPm15MinIntervalValid_Object = MibTableColumn
g9983PortPm15MinIntervalValid = _G9983PortPm15MinIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 2, 1, 6),
    _G9983PortPm15MinIntervalValid_Type()
)
g9983PortPm15MinIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm15MinIntervalValid.setStatus("current")
_G9983PortPm1DayTable_Object = MibTable
g9983PortPm1DayTable = _G9983PortPm1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    g9983PortPm1DayTable.setStatus("current")
_G9983PortPm1DayEntry_Object = MibTableRow
g9983PortPm1DayEntry = _G9983PortPm1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1)
)
g9983PortPm1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983PortPm1DayIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9983PortPm1DayEntry.setStatus("current")


class _G9983PortPm1DayIntervalIndex_Type(Unsigned32):
    """Custom type g9983PortPm1DayIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_G9983PortPm1DayIntervalIndex_Type.__name__ = "Unsigned32"
_G9983PortPm1DayIntervalIndex_Object = MibTableColumn
g9983PortPm1DayIntervalIndex = _G9983PortPm1DayIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 1),
    _G9983PortPm1DayIntervalIndex_Type()
)
g9983PortPm1DayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalIndex.setStatus("current")
_G9983PortPm1DayIntervalMoniTime_Type = HCPerfTimeElapsed
_G9983PortPm1DayIntervalMoniTime_Object = MibTableColumn
g9983PortPm1DayIntervalMoniTime = _G9983PortPm1DayIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 2),
    _G9983PortPm1DayIntervalMoniTime_Type()
)
g9983PortPm1DayIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalMoniTime.setUnits("seconds")
_G9983PortPm1DayIntervalCrc4s_Type = HCPerfIntervalCount
_G9983PortPm1DayIntervalCrc4s_Object = MibTableColumn
g9983PortPm1DayIntervalCrc4s = _G9983PortPm1DayIntervalCrc4s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 3),
    _G9983PortPm1DayIntervalCrc4s_Type()
)
g9983PortPm1DayIntervalCrc4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalCrc4s.setStatus("current")
_G9983PortPm1DayIntervalCrc6s_Type = HCPerfIntervalCount
_G9983PortPm1DayIntervalCrc6s_Object = MibTableColumn
g9983PortPm1DayIntervalCrc6s = _G9983PortPm1DayIntervalCrc6s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 4),
    _G9983PortPm1DayIntervalCrc6s_Type()
)
g9983PortPm1DayIntervalCrc6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalCrc6s.setStatus("current")
_G9983PortPm1DayIntervalCrc8s_Type = HCPerfIntervalCount
_G9983PortPm1DayIntervalCrc8s_Object = MibTableColumn
g9983PortPm1DayIntervalCrc8s = _G9983PortPm1DayIntervalCrc8s_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 5),
    _G9983PortPm1DayIntervalCrc8s_Type()
)
g9983PortPm1DayIntervalCrc8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalCrc8s.setStatus("current")
_G9983PortPm1DayIntervalValid_Type = TruthValue
_G9983PortPm1DayIntervalValid_Object = MibTableColumn
g9983PortPm1DayIntervalValid = _G9983PortPm1DayIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 3, 1, 6),
    _G9983PortPm1DayIntervalValid_Type()
)
g9983PortPm1DayIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983PortPm1DayIntervalValid.setStatus("current")
_G9983SvcPmCurTable_Object = MibTable
g9983SvcPmCurTable = _G9983SvcPmCurTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    g9983SvcPmCurTable.setStatus("current")
_G9983SvcPmCurEntry_Object = MibTableRow
g9983SvcPmCurEntry = _G9983SvcPmCurEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1)
)
g9983SvcPmCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983SvcIdx"),
)
if mibBuilder.loadTexts:
    g9983SvcPmCurEntry.setStatus("current")
_G9983SvcPmCur15MinValidIntervals_Type = HCPerfValidIntervals
_G9983SvcPmCur15MinValidIntervals_Object = MibTableColumn
g9983SvcPmCur15MinValidIntervals = _G9983SvcPmCur15MinValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 1),
    _G9983SvcPmCur15MinValidIntervals_Type()
)
g9983SvcPmCur15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinValidIntervals.setStatus("current")
_G9983SvcPmCur15MinInvalidIntervals_Type = HCPerfInvalidIntervals
_G9983SvcPmCur15MinInvalidIntervals_Object = MibTableColumn
g9983SvcPmCur15MinInvalidIntervals = _G9983SvcPmCur15MinInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 2),
    _G9983SvcPmCur15MinInvalidIntervals_Type()
)
g9983SvcPmCur15MinInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinInvalidIntervals.setStatus("current")
_G9983SvcPmCur15MinTimeElapsed_Type = HCPerfTimeElapsed
_G9983SvcPmCur15MinTimeElapsed_Object = MibTableColumn
g9983SvcPmCur15MinTimeElapsed = _G9983SvcPmCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 3),
    _G9983SvcPmCur15MinTimeElapsed_Type()
)
g9983SvcPmCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinTimeElapsed.setUnits("seconds")
_G9983SvcPmCur15MinDowns_Type = HCPerfCurrentCount
_G9983SvcPmCur15MinDowns_Object = MibTableColumn
g9983SvcPmCur15MinDowns = _G9983SvcPmCur15MinDowns_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 4),
    _G9983SvcPmCur15MinDowns_Type()
)
g9983SvcPmCur15MinDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinDowns.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur15MinDowns.setUnits("seconds")


class _G9983SvcPmCur1DayValidIntervals_Type(Unsigned32):
    """Custom type g9983SvcPmCur1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9983SvcPmCur1DayValidIntervals_Type.__name__ = "Unsigned32"
_G9983SvcPmCur1DayValidIntervals_Object = MibTableColumn
g9983SvcPmCur1DayValidIntervals = _G9983SvcPmCur1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 5),
    _G9983SvcPmCur1DayValidIntervals_Type()
)
g9983SvcPmCur1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayValidIntervals.setUnits("days")


class _G9983SvcPmCur1DayInvalidIntervals_Type(Unsigned32):
    """Custom type g9983SvcPmCur1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9983SvcPmCur1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_G9983SvcPmCur1DayInvalidIntervals_Object = MibTableColumn
g9983SvcPmCur1DayInvalidIntervals = _G9983SvcPmCur1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 6),
    _G9983SvcPmCur1DayInvalidIntervals_Type()
)
g9983SvcPmCur1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayInvalidIntervals.setUnits("days")
_G9983SvcPmCur1DayTimeElapsed_Type = HCPerfTimeElapsed
_G9983SvcPmCur1DayTimeElapsed_Object = MibTableColumn
g9983SvcPmCur1DayTimeElapsed = _G9983SvcPmCur1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 7),
    _G9983SvcPmCur1DayTimeElapsed_Type()
)
g9983SvcPmCur1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayTimeElapsed.setUnits("seconds")
_G9983SvcPmCur1DayDowns_Type = HCPerfCurrentCount
_G9983SvcPmCur1DayDowns_Object = MibTableColumn
g9983SvcPmCur1DayDowns = _G9983SvcPmCur1DayDowns_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 4, 1, 8),
    _G9983SvcPmCur1DayDowns_Type()
)
g9983SvcPmCur1DayDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayDowns.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPmCur1DayDowns.setUnits("seconds")
_G9983SvcPm15MinTable_Object = MibTable
g9983SvcPm15MinTable = _G9983SvcPm15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    g9983SvcPm15MinTable.setStatus("current")
_G9983SvcPm15MinEntry_Object = MibTableRow
g9983SvcPm15MinEntry = _G9983SvcPm15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5, 1)
)
g9983SvcPm15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983SvcIdx"),
    (0, "G9983-MIB", "g9983SvcPm15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9983SvcPm15MinEntry.setStatus("current")


class _G9983SvcPm15MinIntervalIndex_Type(Unsigned32):
    """Custom type g9983SvcPm15MinIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_G9983SvcPm15MinIntervalIndex_Type.__name__ = "Unsigned32"
_G9983SvcPm15MinIntervalIndex_Object = MibTableColumn
g9983SvcPm15MinIntervalIndex = _G9983SvcPm15MinIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5, 1, 1),
    _G9983SvcPm15MinIntervalIndex_Type()
)
g9983SvcPm15MinIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalIndex.setStatus("current")
_G9983SvcPm15MinIntervalMoniTime_Type = HCPerfTimeElapsed
_G9983SvcPm15MinIntervalMoniTime_Object = MibTableColumn
g9983SvcPm15MinIntervalMoniTime = _G9983SvcPm15MinIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5, 1, 2),
    _G9983SvcPm15MinIntervalMoniTime_Type()
)
g9983SvcPm15MinIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalMoniTime.setUnits("seconds")
_G9983SvcPm15MinIntervalDowns_Type = HCPerfIntervalCount
_G9983SvcPm15MinIntervalDowns_Object = MibTableColumn
g9983SvcPm15MinIntervalDowns = _G9983SvcPm15MinIntervalDowns_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5, 1, 3),
    _G9983SvcPm15MinIntervalDowns_Type()
)
g9983SvcPm15MinIntervalDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalDowns.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalDowns.setUnits("seconds")
_G9983SvcPm15MinIntervalValid_Type = TruthValue
_G9983SvcPm15MinIntervalValid_Object = MibTableColumn
g9983SvcPm15MinIntervalValid = _G9983SvcPm15MinIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 5, 1, 4),
    _G9983SvcPm15MinIntervalValid_Type()
)
g9983SvcPm15MinIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm15MinIntervalValid.setStatus("current")
_G9983SvcPm1DayTable_Object = MibTable
g9983SvcPm1DayTable = _G9983SvcPm1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    g9983SvcPm1DayTable.setStatus("current")
_G9983SvcPm1DayEntry_Object = MibTableRow
g9983SvcPm1DayEntry = _G9983SvcPm1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6, 1)
)
g9983SvcPm1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9983-MIB", "g9983SvcIdx"),
    (0, "G9983-MIB", "g9983SvcPm1DayIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9983SvcPm1DayEntry.setStatus("current")


class _G9983SvcPm1DayIntervalIndex_Type(Unsigned32):
    """Custom type g9983SvcPm1DayIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_G9983SvcPm1DayIntervalIndex_Type.__name__ = "Unsigned32"
_G9983SvcPm1DayIntervalIndex_Object = MibTableColumn
g9983SvcPm1DayIntervalIndex = _G9983SvcPm1DayIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6, 1, 1),
    _G9983SvcPm1DayIntervalIndex_Type()
)
g9983SvcPm1DayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalIndex.setStatus("current")
_G9983SvcPm1DayIntervalMoniTime_Type = HCPerfTimeElapsed
_G9983SvcPm1DayIntervalMoniTime_Object = MibTableColumn
g9983SvcPm1DayIntervalMoniTime = _G9983SvcPm1DayIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6, 1, 2),
    _G9983SvcPm1DayIntervalMoniTime_Type()
)
g9983SvcPm1DayIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalMoniTime.setUnits("seconds")
_G9983SvcPm1DayIntervalDowns_Type = HCPerfIntervalCount
_G9983SvcPm1DayIntervalDowns_Object = MibTableColumn
g9983SvcPm1DayIntervalDowns = _G9983SvcPm1DayIntervalDowns_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6, 1, 3),
    _G9983SvcPm1DayIntervalDowns_Type()
)
g9983SvcPm1DayIntervalDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalDowns.setStatus("current")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalDowns.setUnits("seconds")
_G9983SvcPm1DayIntervalValid_Type = TruthValue
_G9983SvcPm1DayIntervalValid_Object = MibTableColumn
g9983SvcPm1DayIntervalValid = _G9983SvcPm1DayIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 6, 6, 1, 4),
    _G9983SvcPm1DayIntervalValid_Type()
)
g9983SvcPm1DayIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9983SvcPm1DayIntervalValid.setStatus("current")
_G9983Conformance_ObjectIdentity = ObjectIdentity
g9983Conformance = _G9983Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 2)
)
_G9983Groups_ObjectIdentity = ObjectIdentity
g9983Groups = _G9983Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 2, 1)
)
_G9983Compliances_ObjectIdentity = ObjectIdentity
g9983Compliances = _G9983Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 210, 2, 2)
)

# Managed Objects groups

g9983BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 1)
)
g9983BasicGroup.setObjects(
      *(("G9983-MIB", "g9983PortConfAdminServices"),
        ("G9983-MIB", "g9983PortStatCrc4Errors"),
        ("G9983-MIB", "g9983PortStatCrc6Errors"),
        ("G9983-MIB", "g9983PortStatCrc8Errors"),
        ("G9983-MIB", "g9983PortCapFecSupported"),
        ("G9983-MIB", "g9983OperSvcIdx"),
        ("G9983-MIB", "g9983OperSvcState"),
        ("G9983-MIB", "g9983SvcIfIdx"),
        ("G9983-MIB", "g9983SvcType"),
        ("G9983-MIB", "g9983SvcSize"),
        ("G9983-MIB", "g9983SvcRowStatus"),
        ("G9983-MIB", "g9983PortStatFltStatus"))
)
if mibBuilder.loadTexts:
    g9983BasicGroup.setStatus("current")

g9983FecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 2)
)
g9983FecGroup.setObjects(
      *(("G9983-MIB", "g9983PortCapFecSupported"),
        ("G9983-MIB", "g9983PortConfFecAdminState"),
        ("G9983-MIB", "g9983PortStatFecOperState"),
        ("G9983-MIB", "g9983PortConfFecWordSize"),
        ("G9983-MIB", "g9983PortConfFecRedundancySize"),
        ("G9983-MIB", "g9983PortConfFecInterleaverType"),
        ("G9983-MIB", "g9983PortConfFecInterleaverDepth"),
        ("G9983-MIB", "g9983PortCapFecMaxWordSize"),
        ("G9983-MIB", "g9983PortCapFecMaxRedundancySize"),
        ("G9983-MIB", "g9983PortCapFecInterleaverTypeSupported"),
        ("G9983-MIB", "g9983PortCapFecMaxInterleaverDepth"))
)
if mibBuilder.loadTexts:
    g9983FecGroup.setStatus("current")

g9983AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 3)
)
g9983AlarmConfGroup.setObjects(
    ("G9983-MIB", "g9983PortConfSvcUpDownEnable")
)
if mibBuilder.loadTexts:
    g9983AlarmConfGroup.setStatus("current")

g9983PerfCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 5)
)
g9983PerfCurrGroup.setObjects(
      *(("G9983-MIB", "g9983PortPmCur15MinValidIntervals"),
        ("G9983-MIB", "g9983PortPmCur15MinInvalidIntervals"),
        ("G9983-MIB", "g9983PortPmCur15MinTimeElapsed"),
        ("G9983-MIB", "g9983PortPmCur15MinCrc4s"),
        ("G9983-MIB", "g9983PortPmCur15MinCrc6s"),
        ("G9983-MIB", "g9983PortPmCur15MinCrc8s"),
        ("G9983-MIB", "g9983PortPmCur1DayValidIntervals"),
        ("G9983-MIB", "g9983PortPmCur1DayInvalidIntervals"),
        ("G9983-MIB", "g9983PortPmCur1DayTimeElapsed"),
        ("G9983-MIB", "g9983PortPmCur1DayCrc4s"),
        ("G9983-MIB", "g9983PortPmCur1DayCrc6s"),
        ("G9983-MIB", "g9983PortPmCur1DayCrc8s"),
        ("G9983-MIB", "g9983SvcPmCur15MinValidIntervals"),
        ("G9983-MIB", "g9983SvcPmCur15MinInvalidIntervals"),
        ("G9983-MIB", "g9983SvcPmCur15MinTimeElapsed"),
        ("G9983-MIB", "g9983SvcPmCur15MinDowns"),
        ("G9983-MIB", "g9983SvcPmCur1DayValidIntervals"),
        ("G9983-MIB", "g9983SvcPmCur1DayInvalidIntervals"),
        ("G9983-MIB", "g9983SvcPmCur1DayTimeElapsed"),
        ("G9983-MIB", "g9983SvcPmCur1DayDowns"))
)
if mibBuilder.loadTexts:
    g9983PerfCurrGroup.setStatus("current")

g9983Perf15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 6)
)
g9983Perf15MinGroup.setObjects(
      *(("G9983-MIB", "g9983PortPm15MinIntervalMoniTime"),
        ("G9983-MIB", "g9983PortPm15MinIntervalCrc4s"),
        ("G9983-MIB", "g9983PortPm15MinIntervalCrc6s"),
        ("G9983-MIB", "g9983PortPm15MinIntervalCrc8s"),
        ("G9983-MIB", "g9983PortPm15MinIntervalValid"),
        ("G9983-MIB", "g9983SvcPm15MinIntervalMoniTime"),
        ("G9983-MIB", "g9983SvcPm15MinIntervalDowns"),
        ("G9983-MIB", "g9983SvcPm15MinIntervalValid"))
)
if mibBuilder.loadTexts:
    g9983Perf15MinGroup.setStatus("current")

g9983Perf1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 7)
)
g9983Perf1DayGroup.setObjects(
      *(("G9983-MIB", "g9983PortPm1DayIntervalMoniTime"),
        ("G9983-MIB", "g9983PortPm1DayIntervalCrc4s"),
        ("G9983-MIB", "g9983PortPm1DayIntervalCrc6s"),
        ("G9983-MIB", "g9983PortPm1DayIntervalCrc8s"),
        ("G9983-MIB", "g9983PortPm1DayIntervalValid"),
        ("G9983-MIB", "g9983SvcPm1DayIntervalMoniTime"),
        ("G9983-MIB", "g9983SvcPm1DayIntervalDowns"),
        ("G9983-MIB", "g9983SvcPm1DayIntervalValid"))
)
if mibBuilder.loadTexts:
    g9983Perf1DayGroup.setStatus("current")


# Notification objects

g9983SvcUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 0, 1)
)
g9983SvcUp.setObjects(
      *(("G9983-MIB", "g9983OperSvcIdx"),
        ("G9983-MIB", "g9983SvcIfIdx"))
)
if mibBuilder.loadTexts:
    g9983SvcUp.setStatus(
        "current"
    )

g9983SvcDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 210, 1, 1, 0, 2)
)
g9983SvcDown.setObjects(
      *(("G9983-MIB", "g9983OperSvcIdx"),
        ("G9983-MIB", "g9983SvcIfIdx"))
)
if mibBuilder.loadTexts:
    g9983SvcDown.setStatus(
        "current"
    )


# Notifications groups

g9983NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 210, 2, 1, 4)
)
g9983NotificationGroup.setObjects(
      *(("G9983-MIB", "g9983SvcUp"),
        ("G9983-MIB", "g9983SvcDown"))
)
if mibBuilder.loadTexts:
    g9983NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

g9983Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 210, 2, 2, 1)
)
if mibBuilder.loadTexts:
    g9983Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G9983-MIB",
    **{"G9983SvcIndex": G9983SvcIndex,
       "G9983SvcIndexList": G9983SvcIndexList,
       "G9983SvcOrderIndex": G9983SvcOrderIndex,
       "g9983MIB": g9983MIB,
       "g9983Objects": g9983Objects,
       "g9983Port": g9983Port,
       "g9983PortNotifications": g9983PortNotifications,
       "g9983SvcUp": g9983SvcUp,
       "g9983SvcDown": g9983SvcDown,
       "g9983PortConfTable": g9983PortConfTable,
       "g9983PortConfEntry": g9983PortConfEntry,
       "g9983PortConfFecAdminState": g9983PortConfFecAdminState,
       "g9983PortConfFecWordSize": g9983PortConfFecWordSize,
       "g9983PortConfFecRedundancySize": g9983PortConfFecRedundancySize,
       "g9983PortConfFecInterleaverType": g9983PortConfFecInterleaverType,
       "g9983PortConfFecInterleaverDepth": g9983PortConfFecInterleaverDepth,
       "g9983PortConfAdminServices": g9983PortConfAdminServices,
       "g9983PortConfSvcUpDownEnable": g9983PortConfSvcUpDownEnable,
       "g9983PortCapTable": g9983PortCapTable,
       "g9983PortCapEntry": g9983PortCapEntry,
       "g9983PortCapFecSupported": g9983PortCapFecSupported,
       "g9983PortCapFecMaxWordSize": g9983PortCapFecMaxWordSize,
       "g9983PortCapFecMaxRedundancySize": g9983PortCapFecMaxRedundancySize,
       "g9983PortCapFecInterleaverTypeSupported": g9983PortCapFecInterleaverTypeSupported,
       "g9983PortCapFecMaxInterleaverDepth": g9983PortCapFecMaxInterleaverDepth,
       "g9983PortStatTable": g9983PortStatTable,
       "g9983PortStatEntry": g9983PortStatEntry,
       "g9983PortStatFecOperState": g9983PortStatFecOperState,
       "g9983PortStatFltStatus": g9983PortStatFltStatus,
       "g9983PortStatCrc4Errors": g9983PortStatCrc4Errors,
       "g9983PortStatCrc6Errors": g9983PortStatCrc6Errors,
       "g9983PortStatCrc8Errors": g9983PortStatCrc8Errors,
       "g9983OperSvcTable": g9983OperSvcTable,
       "g9983OperSvcEntry": g9983OperSvcEntry,
       "g9983OperSvcPosition": g9983OperSvcPosition,
       "g9983OperSvcIdx": g9983OperSvcIdx,
       "g9983OperSvcState": g9983OperSvcState,
       "g9983SvcTable": g9983SvcTable,
       "g9983SvcEntry": g9983SvcEntry,
       "g9983SvcIdx": g9983SvcIdx,
       "g9983SvcIfIdx": g9983SvcIfIdx,
       "g9983SvcType": g9983SvcType,
       "g9983SvcSize": g9983SvcSize,
       "g9983SvcRowStatus": g9983SvcRowStatus,
       "g9983PM": g9983PM,
       "g9983PortPmCurTable": g9983PortPmCurTable,
       "g9983PortPmCurEntry": g9983PortPmCurEntry,
       "g9983PortPmCur15MinValidIntervals": g9983PortPmCur15MinValidIntervals,
       "g9983PortPmCur15MinInvalidIntervals": g9983PortPmCur15MinInvalidIntervals,
       "g9983PortPmCur15MinTimeElapsed": g9983PortPmCur15MinTimeElapsed,
       "g9983PortPmCur15MinCrc4s": g9983PortPmCur15MinCrc4s,
       "g9983PortPmCur15MinCrc6s": g9983PortPmCur15MinCrc6s,
       "g9983PortPmCur15MinCrc8s": g9983PortPmCur15MinCrc8s,
       "g9983PortPmCur1DayValidIntervals": g9983PortPmCur1DayValidIntervals,
       "g9983PortPmCur1DayInvalidIntervals": g9983PortPmCur1DayInvalidIntervals,
       "g9983PortPmCur1DayTimeElapsed": g9983PortPmCur1DayTimeElapsed,
       "g9983PortPmCur1DayCrc4s": g9983PortPmCur1DayCrc4s,
       "g9983PortPmCur1DayCrc6s": g9983PortPmCur1DayCrc6s,
       "g9983PortPmCur1DayCrc8s": g9983PortPmCur1DayCrc8s,
       "g9983PortPm15MinTable": g9983PortPm15MinTable,
       "g9983PortPm15MinEntry": g9983PortPm15MinEntry,
       "g9983PortPm15MinIntervalIndex": g9983PortPm15MinIntervalIndex,
       "g9983PortPm15MinIntervalMoniTime": g9983PortPm15MinIntervalMoniTime,
       "g9983PortPm15MinIntervalCrc4s": g9983PortPm15MinIntervalCrc4s,
       "g9983PortPm15MinIntervalCrc6s": g9983PortPm15MinIntervalCrc6s,
       "g9983PortPm15MinIntervalCrc8s": g9983PortPm15MinIntervalCrc8s,
       "g9983PortPm15MinIntervalValid": g9983PortPm15MinIntervalValid,
       "g9983PortPm1DayTable": g9983PortPm1DayTable,
       "g9983PortPm1DayEntry": g9983PortPm1DayEntry,
       "g9983PortPm1DayIntervalIndex": g9983PortPm1DayIntervalIndex,
       "g9983PortPm1DayIntervalMoniTime": g9983PortPm1DayIntervalMoniTime,
       "g9983PortPm1DayIntervalCrc4s": g9983PortPm1DayIntervalCrc4s,
       "g9983PortPm1DayIntervalCrc6s": g9983PortPm1DayIntervalCrc6s,
       "g9983PortPm1DayIntervalCrc8s": g9983PortPm1DayIntervalCrc8s,
       "g9983PortPm1DayIntervalValid": g9983PortPm1DayIntervalValid,
       "g9983SvcPmCurTable": g9983SvcPmCurTable,
       "g9983SvcPmCurEntry": g9983SvcPmCurEntry,
       "g9983SvcPmCur15MinValidIntervals": g9983SvcPmCur15MinValidIntervals,
       "g9983SvcPmCur15MinInvalidIntervals": g9983SvcPmCur15MinInvalidIntervals,
       "g9983SvcPmCur15MinTimeElapsed": g9983SvcPmCur15MinTimeElapsed,
       "g9983SvcPmCur15MinDowns": g9983SvcPmCur15MinDowns,
       "g9983SvcPmCur1DayValidIntervals": g9983SvcPmCur1DayValidIntervals,
       "g9983SvcPmCur1DayInvalidIntervals": g9983SvcPmCur1DayInvalidIntervals,
       "g9983SvcPmCur1DayTimeElapsed": g9983SvcPmCur1DayTimeElapsed,
       "g9983SvcPmCur1DayDowns": g9983SvcPmCur1DayDowns,
       "g9983SvcPm15MinTable": g9983SvcPm15MinTable,
       "g9983SvcPm15MinEntry": g9983SvcPm15MinEntry,
       "g9983SvcPm15MinIntervalIndex": g9983SvcPm15MinIntervalIndex,
       "g9983SvcPm15MinIntervalMoniTime": g9983SvcPm15MinIntervalMoniTime,
       "g9983SvcPm15MinIntervalDowns": g9983SvcPm15MinIntervalDowns,
       "g9983SvcPm15MinIntervalValid": g9983SvcPm15MinIntervalValid,
       "g9983SvcPm1DayTable": g9983SvcPm1DayTable,
       "g9983SvcPm1DayEntry": g9983SvcPm1DayEntry,
       "g9983SvcPm1DayIntervalIndex": g9983SvcPm1DayIntervalIndex,
       "g9983SvcPm1DayIntervalMoniTime": g9983SvcPm1DayIntervalMoniTime,
       "g9983SvcPm1DayIntervalDowns": g9983SvcPm1DayIntervalDowns,
       "g9983SvcPm1DayIntervalValid": g9983SvcPm1DayIntervalValid,
       "g9983Conformance": g9983Conformance,
       "g9983Groups": g9983Groups,
       "g9983BasicGroup": g9983BasicGroup,
       "g9983FecGroup": g9983FecGroup,
       "g9983AlarmConfGroup": g9983AlarmConfGroup,
       "g9983NotificationGroup": g9983NotificationGroup,
       "g9983PerfCurrGroup": g9983PerfCurrGroup,
       "g9983Perf15MinGroup": g9983Perf15MinGroup,
       "g9983Perf1DayGroup": g9983Perf1DayGroup,
       "g9983Compliances": g9983Compliances,
       "g9983Compliance": g9983Compliance}
)
