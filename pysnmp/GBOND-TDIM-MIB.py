# SNMP MIB module (GBOND-TDIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBOND-TDIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:05 2024
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

(gBondMIB,) = mibBuilder.importSymbols(
    "GBOND-MIB",
    "gBondMIB")

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

gBondTdimMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3)
)
gBondTdimMIB.setRevisions(
        ("2007-04-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GBondTdimServiceIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )



# MIB Managed Objects in the order of their OIDs

_GBondTdimObjects_ObjectIdentity = ObjectIdentity
gBondTdimObjects = _GBondTdimObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 1)
)
_GBondTdimPort_ObjectIdentity = ObjectIdentity
gBondTdimPort = _GBondTdimPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1)
)
_GBondTdimPortNotifications_ObjectIdentity = ObjectIdentity
gBondTdimPortNotifications = _GBondTdimPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 0)
)
_GBondTdimPortConfTable_Object = MibTable
gBondTdimPortConfTable = _GBondTdimPortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gBondTdimPortConfTable.setStatus("current")
_GBondTdimPortConfEntry_Object = MibTableRow
gBondTdimPortConfEntry = _GBondTdimPortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1)
)
gBondTdimPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondTdimPortConfEntry.setStatus("current")
_GBondTdimFecAdminState_Type = TruthValue
_GBondTdimFecAdminState_Object = MibTableColumn
gBondTdimFecAdminState = _GBondTdimFecAdminState_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 1),
    _GBondTdimFecAdminState_Type()
)
gBondTdimFecAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimFecAdminState.setStatus("current")


class _GBondTdimFecWordSize_Type(Unsigned32):
    """Custom type gBondTdimFecWordSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_GBondTdimFecWordSize_Type.__name__ = "Unsigned32"
_GBondTdimFecWordSize_Object = MibTableColumn
gBondTdimFecWordSize = _GBondTdimFecWordSize_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 2),
    _GBondTdimFecWordSize_Type()
)
gBondTdimFecWordSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimFecWordSize.setStatus("current")
if mibBuilder.loadTexts:
    gBondTdimFecWordSize.setUnits("octets")


class _GBondTdimFecRedundancySize_Type(Unsigned32):
    """Custom type gBondTdimFecRedundancySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
    )


_GBondTdimFecRedundancySize_Type.__name__ = "Unsigned32"
_GBondTdimFecRedundancySize_Object = MibTableColumn
gBondTdimFecRedundancySize = _GBondTdimFecRedundancySize_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 3),
    _GBondTdimFecRedundancySize_Type()
)
gBondTdimFecRedundancySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimFecRedundancySize.setStatus("current")
if mibBuilder.loadTexts:
    gBondTdimFecRedundancySize.setUnits("octets")


class _GBondTdimFecInterleaverType_Type(Integer32):
    """Custom type gBondTdimFecInterleaverType based on Integer32"""
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


_GBondTdimFecInterleaverType_Type.__name__ = "Integer32"
_GBondTdimFecInterleaverType_Object = MibTableColumn
gBondTdimFecInterleaverType = _GBondTdimFecInterleaverType_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 4),
    _GBondTdimFecInterleaverType_Type()
)
gBondTdimFecInterleaverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimFecInterleaverType.setStatus("current")


class _GBondTdimFecInterleaverDepth_Type(Unsigned32):
    """Custom type gBondTdimFecInterleaverDepth based on Unsigned32"""
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


_GBondTdimFecInterleaverDepth_Type.__name__ = "Unsigned32"
_GBondTdimFecInterleaverDepth_Object = MibTableColumn
gBondTdimFecInterleaverDepth = _GBondTdimFecInterleaverDepth_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 5),
    _GBondTdimFecInterleaverDepth_Type()
)
gBondTdimFecInterleaverDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimFecInterleaverDepth.setStatus("current")
_GBondTdimServiceUpDownEnable_Type = TruthValue
_GBondTdimServiceUpDownEnable_Object = MibTableColumn
gBondTdimServiceUpDownEnable = _GBondTdimServiceUpDownEnable_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 1, 1, 6),
    _GBondTdimServiceUpDownEnable_Type()
)
gBondTdimServiceUpDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimServiceUpDownEnable.setStatus("current")
_GBondTdimPortCapabilityTable_Object = MibTable
gBondTdimPortCapabilityTable = _GBondTdimPortCapabilityTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gBondTdimPortCapabilityTable.setStatus("current")
_GBondTdimPortCapabilityEntry_Object = MibTableRow
gBondTdimPortCapabilityEntry = _GBondTdimPortCapabilityEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1)
)
gBondTdimPortCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondTdimPortCapabilityEntry.setStatus("current")
_GBondTdimFecSupported_Type = TruthValue
_GBondTdimFecSupported_Object = MibTableColumn
gBondTdimFecSupported = _GBondTdimFecSupported_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1, 1),
    _GBondTdimFecSupported_Type()
)
gBondTdimFecSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFecSupported.setStatus("current")


class _GBondTdimFecMaxWordSize_Type(Unsigned32):
    """Custom type gBondTdimFecMaxWordSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_GBondTdimFecMaxWordSize_Type.__name__ = "Unsigned32"
_GBondTdimFecMaxWordSize_Object = MibTableColumn
gBondTdimFecMaxWordSize = _GBondTdimFecMaxWordSize_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1, 2),
    _GBondTdimFecMaxWordSize_Type()
)
gBondTdimFecMaxWordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFecMaxWordSize.setStatus("current")
if mibBuilder.loadTexts:
    gBondTdimFecMaxWordSize.setUnits("octets")


class _GBondTdimFecMaxRedundancySize_Type(Unsigned32):
    """Custom type gBondTdimFecMaxRedundancySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
    )


_GBondTdimFecMaxRedundancySize_Type.__name__ = "Unsigned32"
_GBondTdimFecMaxRedundancySize_Object = MibTableColumn
gBondTdimFecMaxRedundancySize = _GBondTdimFecMaxRedundancySize_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1, 3),
    _GBondTdimFecMaxRedundancySize_Type()
)
gBondTdimFecMaxRedundancySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFecMaxRedundancySize.setStatus("current")
if mibBuilder.loadTexts:
    gBondTdimFecMaxRedundancySize.setUnits("octets")


class _GBondTdimFecInterleaverTypeSupported_Type(Integer32):
    """Custom type gBondTdimFecInterleaverTypeSupported based on Integer32"""
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


_GBondTdimFecInterleaverTypeSupported_Type.__name__ = "Integer32"
_GBondTdimFecInterleaverTypeSupported_Object = MibTableColumn
gBondTdimFecInterleaverTypeSupported = _GBondTdimFecInterleaverTypeSupported_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1, 4),
    _GBondTdimFecInterleaverTypeSupported_Type()
)
gBondTdimFecInterleaverTypeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFecInterleaverTypeSupported.setStatus("current")


class _GBondTdimFecMaxInterleaverDepth_Type(Unsigned32):
    """Custom type gBondTdimFecMaxInterleaverDepth based on Unsigned32"""
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


_GBondTdimFecMaxInterleaverDepth_Type.__name__ = "Unsigned32"
_GBondTdimFecMaxInterleaverDepth_Object = MibTableColumn
gBondTdimFecMaxInterleaverDepth = _GBondTdimFecMaxInterleaverDepth_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 2, 1, 5),
    _GBondTdimFecMaxInterleaverDepth_Type()
)
gBondTdimFecMaxInterleaverDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFecMaxInterleaverDepth.setStatus("current")
_GBondTdimPortStatusTable_Object = MibTable
gBondTdimPortStatusTable = _GBondTdimPortStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gBondTdimPortStatusTable.setStatus("current")
_GBondTdimPortStatusEntry_Object = MibTableRow
gBondTdimPortStatusEntry = _GBondTdimPortStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3, 1)
)
gBondTdimPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondTdimPortStatusEntry.setStatus("current")
_GBondTdimCrc4Errors_Type = Counter32
_GBondTdimCrc4Errors_Object = MibTableColumn
gBondTdimCrc4Errors = _GBondTdimCrc4Errors_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3, 1, 1),
    _GBondTdimCrc4Errors_Type()
)
gBondTdimCrc4Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimCrc4Errors.setStatus("current")
_GBondTdimCrc6Errors_Type = Counter32
_GBondTdimCrc6Errors_Object = MibTableColumn
gBondTdimCrc6Errors = _GBondTdimCrc6Errors_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3, 1, 2),
    _GBondTdimCrc6Errors_Type()
)
gBondTdimCrc6Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimCrc6Errors.setStatus("current")
_GBondTdimCrc8Errors_Type = Counter32
_GBondTdimCrc8Errors_Object = MibTableColumn
gBondTdimCrc8Errors = _GBondTdimCrc8Errors_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3, 1, 3),
    _GBondTdimCrc8Errors_Type()
)
gBondTdimCrc8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimCrc8Errors.setStatus("current")


class _GBondTdimFltStatus_Type(Bits):
    """Custom type gBondTdimFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("serviceDown", 0),
          ("wrongConfig", 1))
    )

_GBondTdimFltStatus_Type.__name__ = "Bits"
_GBondTdimFltStatus_Object = MibTableColumn
gBondTdimFltStatus = _GBondTdimFltStatus_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 3, 1, 4),
    _GBondTdimFltStatus_Type()
)
gBondTdimFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimFltStatus.setStatus("current")
_GBondTdimServiceTable_Object = MibTable
gBondTdimServiceTable = _GBondTdimServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    gBondTdimServiceTable.setStatus("current")
_GBondTdimServiceEntry_Object = MibTableRow
gBondTdimServiceEntry = _GBondTdimServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1)
)
gBondTdimServiceEntry.setIndexNames(
    (0, "GBOND-TDIM-MIB", "gBondTdimServiceIdx"),
)
if mibBuilder.loadTexts:
    gBondTdimServiceEntry.setStatus("current")
_GBondTdimServiceIdx_Type = GBondTdimServiceIndex
_GBondTdimServiceIdx_Object = MibTableColumn
gBondTdimServiceIdx = _GBondTdimServiceIdx_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1, 1),
    _GBondTdimServiceIdx_Type()
)
gBondTdimServiceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gBondTdimServiceIdx.setStatus("current")
_GBondTdimServiceIfIdx_Type = InterfaceIndex
_GBondTdimServiceIfIdx_Object = MibTableColumn
gBondTdimServiceIfIdx = _GBondTdimServiceIfIdx_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1, 2),
    _GBondTdimServiceIfIdx_Type()
)
gBondTdimServiceIfIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimServiceIfIdx.setStatus("current")


class _GBondTdimServiceType_Type(Integer32):
    """Custom type gBondTdimServiceType based on Integer32"""
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


_GBondTdimServiceType_Type.__name__ = "Integer32"
_GBondTdimServiceType_Object = MibTableColumn
gBondTdimServiceType = _GBondTdimServiceType_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1, 3),
    _GBondTdimServiceType_Type()
)
gBondTdimServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimServiceType.setStatus("current")


class _GBondTdimServiceSize_Type(Unsigned32):
    """Custom type gBondTdimServiceSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 255),
    )


_GBondTdimServiceSize_Type.__name__ = "Unsigned32"
_GBondTdimServiceSize_Object = MibTableColumn
gBondTdimServiceSize = _GBondTdimServiceSize_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1, 4),
    _GBondTdimServiceSize_Type()
)
gBondTdimServiceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondTdimServiceSize.setStatus("current")
if mibBuilder.loadTexts:
    gBondTdimServiceSize.setUnits("octets")


class _GBondTdimServiceOperState_Type(Integer32):
    """Custom type gBondTdimServiceOperState based on Integer32"""
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


_GBondTdimServiceOperState_Type.__name__ = "Integer32"
_GBondTdimServiceOperState_Object = MibTableColumn
gBondTdimServiceOperState = _GBondTdimServiceOperState_Object(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 4, 1, 5),
    _GBondTdimServiceOperState_Type()
)
gBondTdimServiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondTdimServiceOperState.setStatus("current")
_GBondTdimConformance_ObjectIdentity = ObjectIdentity
gBondTdimConformance = _GBondTdimConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 2)
)
_GBondTdimGroups_ObjectIdentity = ObjectIdentity
gBondTdimGroups = _GBondTdimGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 1)
)
_GBondTdimCompliances_ObjectIdentity = ObjectIdentity
gBondTdimCompliances = _GBondTdimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 2)
)

# Managed Objects groups

gBondTdimBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 1, 1)
)
gBondTdimBasicGroup.setObjects(
      *(("GBOND-TDIM-MIB", "gBondTdimCrc4Errors"),
        ("GBOND-TDIM-MIB", "gBondTdimCrc6Errors"),
        ("GBOND-TDIM-MIB", "gBondTdimCrc8Errors"),
        ("GBOND-TDIM-MIB", "gBondTdimFecSupported"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceIfIdx"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceType"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceSize"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceOperState"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceUpDownEnable"),
        ("GBOND-TDIM-MIB", "gBondTdimFltStatus"))
)
if mibBuilder.loadTexts:
    gBondTdimBasicGroup.setStatus("current")

gBondTdimFecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 1, 2)
)
gBondTdimFecGroup.setObjects(
      *(("GBOND-TDIM-MIB", "gBondTdimFecSupported"),
        ("GBOND-TDIM-MIB", "gBondTdimFecAdminState"),
        ("GBOND-TDIM-MIB", "gBondTdimFecWordSize"),
        ("GBOND-TDIM-MIB", "gBondTdimFecRedundancySize"),
        ("GBOND-TDIM-MIB", "gBondTdimFecInterleaverType"),
        ("GBOND-TDIM-MIB", "gBondTdimFecInterleaverDepth"),
        ("GBOND-TDIM-MIB", "gBondTdimFecMaxWordSize"),
        ("GBOND-TDIM-MIB", "gBondTdimFecMaxRedundancySize"),
        ("GBOND-TDIM-MIB", "gBondTdimFecInterleaverTypeSupported"),
        ("GBOND-TDIM-MIB", "gBondTdimFecMaxInterleaverDepth"))
)
if mibBuilder.loadTexts:
    gBondTdimFecGroup.setStatus("current")

gBondTdimAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 1, 3)
)
gBondTdimAlarmConfGroup.setObjects(
    ("GBOND-TDIM-MIB", "gBondTdimServiceUpDownEnable")
)
if mibBuilder.loadTexts:
    gBondTdimAlarmConfGroup.setStatus("current")


# Notification objects

gBondTdimServiceUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 0, 1)
)
gBondTdimServiceUp.setObjects(
      *(("GBOND-TDIM-MIB", "gBondTdimServiceIfIdx"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceOperState"))
)
if mibBuilder.loadTexts:
    gBondTdimServiceUp.setStatus(
        "current"
    )

gBondTdimServiceDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 3, 1, 1, 0, 2)
)
gBondTdimServiceDown.setObjects(
      *(("GBOND-TDIM-MIB", "gBondTdimServiceIfIdx"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceOperState"))
)
if mibBuilder.loadTexts:
    gBondTdimServiceDown.setStatus(
        "current"
    )


# Notifications groups

gBondTdimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 1, 4)
)
gBondTdimNotificationGroup.setObjects(
      *(("GBOND-TDIM-MIB", "gBondTdimServiceUp"),
        ("GBOND-TDIM-MIB", "gBondTdimServiceDown"))
)
if mibBuilder.loadTexts:
    gBondTdimNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gBondTdimCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 211, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gBondTdimCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBOND-TDIM-MIB",
    **{"GBondTdimServiceIndex": GBondTdimServiceIndex,
       "gBondTdimMIB": gBondTdimMIB,
       "gBondTdimObjects": gBondTdimObjects,
       "gBondTdimPort": gBondTdimPort,
       "gBondTdimPortNotifications": gBondTdimPortNotifications,
       "gBondTdimServiceUp": gBondTdimServiceUp,
       "gBondTdimServiceDown": gBondTdimServiceDown,
       "gBondTdimPortConfTable": gBondTdimPortConfTable,
       "gBondTdimPortConfEntry": gBondTdimPortConfEntry,
       "gBondTdimFecAdminState": gBondTdimFecAdminState,
       "gBondTdimFecWordSize": gBondTdimFecWordSize,
       "gBondTdimFecRedundancySize": gBondTdimFecRedundancySize,
       "gBondTdimFecInterleaverType": gBondTdimFecInterleaverType,
       "gBondTdimFecInterleaverDepth": gBondTdimFecInterleaverDepth,
       "gBondTdimServiceUpDownEnable": gBondTdimServiceUpDownEnable,
       "gBondTdimPortCapabilityTable": gBondTdimPortCapabilityTable,
       "gBondTdimPortCapabilityEntry": gBondTdimPortCapabilityEntry,
       "gBondTdimFecSupported": gBondTdimFecSupported,
       "gBondTdimFecMaxWordSize": gBondTdimFecMaxWordSize,
       "gBondTdimFecMaxRedundancySize": gBondTdimFecMaxRedundancySize,
       "gBondTdimFecInterleaverTypeSupported": gBondTdimFecInterleaverTypeSupported,
       "gBondTdimFecMaxInterleaverDepth": gBondTdimFecMaxInterleaverDepth,
       "gBondTdimPortStatusTable": gBondTdimPortStatusTable,
       "gBondTdimPortStatusEntry": gBondTdimPortStatusEntry,
       "gBondTdimCrc4Errors": gBondTdimCrc4Errors,
       "gBondTdimCrc6Errors": gBondTdimCrc6Errors,
       "gBondTdimCrc8Errors": gBondTdimCrc8Errors,
       "gBondTdimFltStatus": gBondTdimFltStatus,
       "gBondTdimServiceTable": gBondTdimServiceTable,
       "gBondTdimServiceEntry": gBondTdimServiceEntry,
       "gBondTdimServiceIdx": gBondTdimServiceIdx,
       "gBondTdimServiceIfIdx": gBondTdimServiceIfIdx,
       "gBondTdimServiceType": gBondTdimServiceType,
       "gBondTdimServiceSize": gBondTdimServiceSize,
       "gBondTdimServiceOperState": gBondTdimServiceOperState,
       "gBondTdimConformance": gBondTdimConformance,
       "gBondTdimGroups": gBondTdimGroups,
       "gBondTdimBasicGroup": gBondTdimBasicGroup,
       "gBondTdimFecGroup": gBondTdimFecGroup,
       "gBondTdimAlarmConfGroup": gBondTdimAlarmConfGroup,
       "gBondTdimNotificationGroup": gBondTdimNotificationGroup,
       "gBondTdimCompliances": gBondTdimCompliances,
       "gBondTdimCompliance": gBondTdimCompliance}
)
