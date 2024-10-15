# SNMP MIB module (LLDP-EXT-DOT3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:12 2024
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

(lldpExtensions,
 lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpExtensions",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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

lldpXdot3MIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623)
)
lldpXdot3MIB.setRevisions(
        ("2005-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpPowerPortClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPD", 2),
          ("pClassPSE", 1))
    )



class LldpLinkAggStatusMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_LldpXdot3Objects_ObjectIdentity = ObjectIdentity
lldpXdot3Objects = _LldpXdot3Objects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1)
)
_LldpXdot3Config_ObjectIdentity = ObjectIdentity
lldpXdot3Config = _LldpXdot3Config_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1)
)
_LldpXdot3PortConfigTable_Object = MibTable
lldpXdot3PortConfigTable = _LldpXdot3PortConfigTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTable.setStatus("current")
_LldpXdot3PortConfigEntry_Object = MibTableRow
lldpXdot3PortConfigEntry = _LldpXdot3PortConfigEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigEntry.setStatus("current")


class _LldpXdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpXdot3PortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("linkAggregation", 2),
          ("macPhyConfigStatus", 0),
          ("maxFrameSize", 3),
          ("powerViaMDI", 1))
    )

_LldpXdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpXdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpXdot3PortConfigTLVsTxEnable = _LldpXdot3PortConfigTLVsTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1, 1, 1),
    _LldpXdot3PortConfigTLVsTxEnable_Type()
)
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3LocalData_ObjectIdentity = ObjectIdentity
lldpXdot3LocalData = _LldpXdot3LocalData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2)
)
_LldpXdot3LocPortTable_Object = MibTable
lldpXdot3LocPortTable = _LldpXdot3LocPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortTable.setStatus("current")
_LldpXdot3LocPortEntry_Object = MibTableRow
lldpXdot3LocPortEntry = _LldpXdot3LocPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1)
)
lldpXdot3LocPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortEntry.setStatus("current")
_LldpXdot3LocPortAutoNegSupported_Type = TruthValue
_LldpXdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpXdot3LocPortAutoNegSupported = _LldpXdot3LocPortAutoNegSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 1),
    _LldpXdot3LocPortAutoNegSupported_Type()
)
lldpXdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegSupported.setStatus("current")
_LldpXdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3LocPortAutoNegEnabled = _LldpXdot3LocPortAutoNegEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 2),
    _LldpXdot3LocPortAutoNegEnabled_Type()
)
lldpXdot3LocPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegEnabled.setStatus("current")


class _LldpXdot3LocPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3LocPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3LocPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3LocPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3LocPortAutoNegAdvertisedCap = _LldpXdot3LocPortAutoNegAdvertisedCap_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 3),
    _LldpXdot3LocPortAutoNegAdvertisedCap_Type()
)
lldpXdot3LocPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3LocPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3LocPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3LocPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3LocPortOperMauType_Object = MibTableColumn
lldpXdot3LocPortOperMauType = _LldpXdot3LocPortOperMauType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 4),
    _LldpXdot3LocPortOperMauType_Type()
)
lldpXdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortOperMauType.setStatus("current")
_LldpXdot3LocPowerTable_Object = MibTable
lldpXdot3LocPowerTable = _LldpXdot3LocPowerTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerTable.setStatus("current")
_LldpXdot3LocPowerEntry_Object = MibTableRow
lldpXdot3LocPowerEntry = _LldpXdot3LocPowerEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1)
)
lldpXdot3LocPowerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerEntry.setStatus("current")
_LldpXdot3LocPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3LocPowerPortClass_Object = MibTableColumn
lldpXdot3LocPowerPortClass = _LldpXdot3LocPowerPortClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 1),
    _LldpXdot3LocPowerPortClass_Type()
)
lldpXdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPortClass.setStatus("current")
_LldpXdot3LocPowerMDISupported_Type = TruthValue
_LldpXdot3LocPowerMDISupported_Object = MibTableColumn
lldpXdot3LocPowerMDISupported = _LldpXdot3LocPowerMDISupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 2),
    _LldpXdot3LocPowerMDISupported_Type()
)
lldpXdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDISupported.setStatus("current")
_LldpXdot3LocPowerMDIEnabled_Type = TruthValue
_LldpXdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpXdot3LocPowerMDIEnabled = _LldpXdot3LocPowerMDIEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 3),
    _LldpXdot3LocPowerMDIEnabled_Type()
)
lldpXdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDIEnabled.setStatus("current")
_LldpXdot3LocPowerPairControlable_Type = TruthValue
_LldpXdot3LocPowerPairControlable_Object = MibTableColumn
lldpXdot3LocPowerPairControlable = _LldpXdot3LocPowerPairControlable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 4),
    _LldpXdot3LocPowerPairControlable_Type()
)
lldpXdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairControlable.setStatus("current")


class _LldpXdot3LocPowerPairs_Type(Integer32):
    """Custom type lldpXdot3LocPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3LocPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3LocPowerPairs_Object = MibTableColumn
lldpXdot3LocPowerPairs = _LldpXdot3LocPowerPairs_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 5),
    _LldpXdot3LocPowerPairs_Type()
)
lldpXdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairs.setStatus("current")


class _LldpXdot3LocPowerClass_Type(Integer32):
    """Custom type lldpXdot3LocPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3LocPowerClass_Type.__name__ = "Integer32"
_LldpXdot3LocPowerClass_Object = MibTableColumn
lldpXdot3LocPowerClass = _LldpXdot3LocPowerClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 6),
    _LldpXdot3LocPowerClass_Type()
)
lldpXdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerClass.setStatus("current")
_LldpXdot3LocLinkAggTable_Object = MibTable
lldpXdot3LocLinkAggTable = _LldpXdot3LocLinkAggTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggTable.setStatus("current")
_LldpXdot3LocLinkAggEntry_Object = MibTableRow
lldpXdot3LocLinkAggEntry = _LldpXdot3LocLinkAggEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1)
)
lldpXdot3LocLinkAggEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggEntry.setStatus("current")
_LldpXdot3LocLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3LocLinkAggStatus_Object = MibTableColumn
lldpXdot3LocLinkAggStatus = _LldpXdot3LocLinkAggStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1, 1),
    _LldpXdot3LocLinkAggStatus_Type()
)
lldpXdot3LocLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggStatus.setStatus("current")


class _LldpXdot3LocLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3LocLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3LocLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3LocLinkAggPortId_Object = MibTableColumn
lldpXdot3LocLinkAggPortId = _LldpXdot3LocLinkAggPortId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1, 2),
    _LldpXdot3LocLinkAggPortId_Type()
)
lldpXdot3LocLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggPortId.setStatus("current")
_LldpXdot3LocMaxFrameSizeTable_Object = MibTable
lldpXdot3LocMaxFrameSizeTable = _LldpXdot3LocMaxFrameSizeTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeTable.setStatus("current")
_LldpXdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3LocMaxFrameSizeEntry = _LldpXdot3LocMaxFrameSizeEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4, 1)
)
lldpXdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeEntry.setStatus("current")


class _LldpXdot3LocMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3LocMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3LocMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3LocMaxFrameSize_Object = MibTableColumn
lldpXdot3LocMaxFrameSize = _LldpXdot3LocMaxFrameSize_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4, 1, 1),
    _LldpXdot3LocMaxFrameSize_Type()
)
lldpXdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSize.setStatus("current")
_LldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot3RemoteData = _LldpXdot3RemoteData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3)
)
_LldpXdot3RemPortTable_Object = MibTable
lldpXdot3RemPortTable = _LldpXdot3RemPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortTable.setStatus("current")
_LldpXdot3RemPortEntry_Object = MibTableRow
lldpXdot3RemPortEntry = _LldpXdot3RemPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1)
)
lldpXdot3RemPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortEntry.setStatus("current")
_LldpXdot3RemPortAutoNegSupported_Type = TruthValue
_LldpXdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpXdot3RemPortAutoNegSupported = _LldpXdot3RemPortAutoNegSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 1),
    _LldpXdot3RemPortAutoNegSupported_Type()
)
lldpXdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegSupported.setStatus("current")
_LldpXdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3RemPortAutoNegEnabled = _LldpXdot3RemPortAutoNegEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 2),
    _LldpXdot3RemPortAutoNegEnabled_Type()
)
lldpXdot3RemPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegEnabled.setStatus("current")


class _LldpXdot3RemPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3RemPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3RemPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3RemPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3RemPortAutoNegAdvertisedCap = _LldpXdot3RemPortAutoNegAdvertisedCap_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 3),
    _LldpXdot3RemPortAutoNegAdvertisedCap_Type()
)
lldpXdot3RemPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3RemPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3RemPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3RemPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3RemPortOperMauType_Object = MibTableColumn
lldpXdot3RemPortOperMauType = _LldpXdot3RemPortOperMauType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 4),
    _LldpXdot3RemPortOperMauType_Type()
)
lldpXdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortOperMauType.setStatus("current")
_LldpXdot3RemPowerTable_Object = MibTable
lldpXdot3RemPowerTable = _LldpXdot3RemPowerTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTable.setStatus("current")
_LldpXdot3RemPowerEntry_Object = MibTableRow
lldpXdot3RemPowerEntry = _LldpXdot3RemPowerEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1)
)
lldpXdot3RemPowerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerEntry.setStatus("current")
_LldpXdot3RemPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object = MibTableColumn
lldpXdot3RemPowerPortClass = _LldpXdot3RemPowerPortClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 1),
    _LldpXdot3RemPowerPortClass_Type()
)
lldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPortClass.setStatus("current")
_LldpXdot3RemPowerMDISupported_Type = TruthValue
_LldpXdot3RemPowerMDISupported_Object = MibTableColumn
lldpXdot3RemPowerMDISupported = _LldpXdot3RemPowerMDISupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 2),
    _LldpXdot3RemPowerMDISupported_Type()
)
lldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDISupported.setStatus("current")
_LldpXdot3RemPowerMDIEnabled_Type = TruthValue
_LldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpXdot3RemPowerMDIEnabled = _LldpXdot3RemPowerMDIEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 3),
    _LldpXdot3RemPowerMDIEnabled_Type()
)
lldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDIEnabled.setStatus("current")
_LldpXdot3RemPowerPairControlable_Type = TruthValue
_LldpXdot3RemPowerPairControlable_Object = MibTableColumn
lldpXdot3RemPowerPairControlable = _LldpXdot3RemPowerPairControlable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 4),
    _LldpXdot3RemPowerPairControlable_Type()
)
lldpXdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairControlable.setStatus("current")


class _LldpXdot3RemPowerPairs_Type(Integer32):
    """Custom type lldpXdot3RemPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3RemPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3RemPowerPairs_Object = MibTableColumn
lldpXdot3RemPowerPairs = _LldpXdot3RemPowerPairs_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 5),
    _LldpXdot3RemPowerPairs_Type()
)
lldpXdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairs.setStatus("current")


class _LldpXdot3RemPowerClass_Type(Integer32):
    """Custom type lldpXdot3RemPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3RemPowerClass_Type.__name__ = "Integer32"
_LldpXdot3RemPowerClass_Object = MibTableColumn
lldpXdot3RemPowerClass = _LldpXdot3RemPowerClass_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 6),
    _LldpXdot3RemPowerClass_Type()
)
lldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerClass.setStatus("current")
_LldpXdot3RemLinkAggTable_Object = MibTable
lldpXdot3RemLinkAggTable = _LldpXdot3RemLinkAggTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTable.setStatus("current")
_LldpXdot3RemLinkAggEntry_Object = MibTableRow
lldpXdot3RemLinkAggEntry = _LldpXdot3RemLinkAggEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1)
)
lldpXdot3RemLinkAggEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggEntry.setStatus("current")
_LldpXdot3RemLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object = MibTableColumn
lldpXdot3RemLinkAggStatus = _LldpXdot3RemLinkAggStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1, 1),
    _LldpXdot3RemLinkAggStatus_Type()
)
lldpXdot3RemLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggStatus.setStatus("current")


class _LldpXdot3RemLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3RemLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3RemLinkAggPortId_Object = MibTableColumn
lldpXdot3RemLinkAggPortId = _LldpXdot3RemLinkAggPortId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1, 2),
    _LldpXdot3RemLinkAggPortId_Type()
)
lldpXdot3RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggPortId.setStatus("current")
_LldpXdot3RemMaxFrameSizeTable_Object = MibTable
lldpXdot3RemMaxFrameSizeTable = _LldpXdot3RemMaxFrameSizeTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTable.setStatus("current")
_LldpXdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3RemMaxFrameSizeEntry = _LldpXdot3RemMaxFrameSizeEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4, 1)
)
lldpXdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeEntry.setStatus("current")


class _LldpXdot3RemMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3RemMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSize_Object = MibTableColumn
lldpXdot3RemMaxFrameSize = _LldpXdot3RemMaxFrameSize_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4, 1, 1),
    _LldpXdot3RemMaxFrameSize_Type()
)
lldpXdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSize.setStatus("current")
_LldpXdot3Conformance_ObjectIdentity = ObjectIdentity
lldpXdot3Conformance = _LldpXdot3Conformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2)
)
_LldpXdot3Compliances_ObjectIdentity = ObjectIdentity
lldpXdot3Compliances = _LldpXdot3Compliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 1)
)
_LldpXdot3Groups_ObjectIdentity = ObjectIdentity
lldpXdot3Groups = _LldpXdot3Groups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2)
)
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT3-MIB",
     "lldpXdot3PortConfigEntry")
)
lldpXdot3PortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXdot3ConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 1)
)
lldpXdot3ConfigGroup.setObjects(
    ("LLDP-EXT-DOT3-MIB", "lldpXdot3PortConfigTLVsTxEnable")
)
if mibBuilder.loadTexts:
    lldpXdot3ConfigGroup.setStatus("current")

lldpXdot3LocSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 2)
)
lldpXdot3LocSysGroup.setObjects(
      *(("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegSupported"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegEnabled"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegAdvertisedCap"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortOperMauType"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPortClass"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerMDISupported"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerMDIEnabled"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPairControlable"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPairs"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerClass"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocLinkAggStatus"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocLinkAggPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocMaxFrameSize"))
)
if mibBuilder.loadTexts:
    lldpXdot3LocSysGroup.setStatus("current")

lldpXdot3RemSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 3)
)
lldpXdot3RemSysGroup.setObjects(
      *(("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegSupported"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegEnabled"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegAdvertisedCap"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortOperMauType"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPortClass"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerMDISupported"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerMDIEnabled"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPairControlable"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPairs"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerClass"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggStatus"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggPortId"),
        ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemMaxFrameSize"))
)
if mibBuilder.loadTexts:
    lldpXdot3RemSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXdot3Compliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT3-MIB",
    **{"LldpPowerPortClass": LldpPowerPortClass,
       "LldpLinkAggStatusMap": LldpLinkAggStatusMap,
       "lldpXdot3MIB": lldpXdot3MIB,
       "lldpXdot3Objects": lldpXdot3Objects,
       "lldpXdot3Config": lldpXdot3Config,
       "lldpXdot3PortConfigTable": lldpXdot3PortConfigTable,
       "lldpXdot3PortConfigEntry": lldpXdot3PortConfigEntry,
       "lldpXdot3PortConfigTLVsTxEnable": lldpXdot3PortConfigTLVsTxEnable,
       "lldpXdot3LocalData": lldpXdot3LocalData,
       "lldpXdot3LocPortTable": lldpXdot3LocPortTable,
       "lldpXdot3LocPortEntry": lldpXdot3LocPortEntry,
       "lldpXdot3LocPortAutoNegSupported": lldpXdot3LocPortAutoNegSupported,
       "lldpXdot3LocPortAutoNegEnabled": lldpXdot3LocPortAutoNegEnabled,
       "lldpXdot3LocPortAutoNegAdvertisedCap": lldpXdot3LocPortAutoNegAdvertisedCap,
       "lldpXdot3LocPortOperMauType": lldpXdot3LocPortOperMauType,
       "lldpXdot3LocPowerTable": lldpXdot3LocPowerTable,
       "lldpXdot3LocPowerEntry": lldpXdot3LocPowerEntry,
       "lldpXdot3LocPowerPortClass": lldpXdot3LocPowerPortClass,
       "lldpXdot3LocPowerMDISupported": lldpXdot3LocPowerMDISupported,
       "lldpXdot3LocPowerMDIEnabled": lldpXdot3LocPowerMDIEnabled,
       "lldpXdot3LocPowerPairControlable": lldpXdot3LocPowerPairControlable,
       "lldpXdot3LocPowerPairs": lldpXdot3LocPowerPairs,
       "lldpXdot3LocPowerClass": lldpXdot3LocPowerClass,
       "lldpXdot3LocLinkAggTable": lldpXdot3LocLinkAggTable,
       "lldpXdot3LocLinkAggEntry": lldpXdot3LocLinkAggEntry,
       "lldpXdot3LocLinkAggStatus": lldpXdot3LocLinkAggStatus,
       "lldpXdot3LocLinkAggPortId": lldpXdot3LocLinkAggPortId,
       "lldpXdot3LocMaxFrameSizeTable": lldpXdot3LocMaxFrameSizeTable,
       "lldpXdot3LocMaxFrameSizeEntry": lldpXdot3LocMaxFrameSizeEntry,
       "lldpXdot3LocMaxFrameSize": lldpXdot3LocMaxFrameSize,
       "lldpXdot3RemoteData": lldpXdot3RemoteData,
       "lldpXdot3RemPortTable": lldpXdot3RemPortTable,
       "lldpXdot3RemPortEntry": lldpXdot3RemPortEntry,
       "lldpXdot3RemPortAutoNegSupported": lldpXdot3RemPortAutoNegSupported,
       "lldpXdot3RemPortAutoNegEnabled": lldpXdot3RemPortAutoNegEnabled,
       "lldpXdot3RemPortAutoNegAdvertisedCap": lldpXdot3RemPortAutoNegAdvertisedCap,
       "lldpXdot3RemPortOperMauType": lldpXdot3RemPortOperMauType,
       "lldpXdot3RemPowerTable": lldpXdot3RemPowerTable,
       "lldpXdot3RemPowerEntry": lldpXdot3RemPowerEntry,
       "lldpXdot3RemPowerPortClass": lldpXdot3RemPowerPortClass,
       "lldpXdot3RemPowerMDISupported": lldpXdot3RemPowerMDISupported,
       "lldpXdot3RemPowerMDIEnabled": lldpXdot3RemPowerMDIEnabled,
       "lldpXdot3RemPowerPairControlable": lldpXdot3RemPowerPairControlable,
       "lldpXdot3RemPowerPairs": lldpXdot3RemPowerPairs,
       "lldpXdot3RemPowerClass": lldpXdot3RemPowerClass,
       "lldpXdot3RemLinkAggTable": lldpXdot3RemLinkAggTable,
       "lldpXdot3RemLinkAggEntry": lldpXdot3RemLinkAggEntry,
       "lldpXdot3RemLinkAggStatus": lldpXdot3RemLinkAggStatus,
       "lldpXdot3RemLinkAggPortId": lldpXdot3RemLinkAggPortId,
       "lldpXdot3RemMaxFrameSizeTable": lldpXdot3RemMaxFrameSizeTable,
       "lldpXdot3RemMaxFrameSizeEntry": lldpXdot3RemMaxFrameSizeEntry,
       "lldpXdot3RemMaxFrameSize": lldpXdot3RemMaxFrameSize,
       "lldpXdot3Conformance": lldpXdot3Conformance,
       "lldpXdot3Compliances": lldpXdot3Compliances,
       "lldpXdot3Compliance": lldpXdot3Compliance,
       "lldpXdot3Groups": lldpXdot3Groups,
       "lldpXdot3ConfigGroup": lldpXdot3ConfigGroup,
       "lldpXdot3LocSysGroup": lldpXdot3LocSysGroup,
       "lldpXdot3RemSysGroup": lldpXdot3RemSysGroup}
)
