# SNMP MIB module (LLDP-EXT-DOT3-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT3-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:07 2024
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

(ifGeneralInformationGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifGeneralInformationGroup")

(lldpV2Extensions,
 lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2Extensions",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(LldpV2PowerPortClass,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2PowerPortClass")

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

lldpV2Xdot3MIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623)
)
lldpV2Xdot3MIB.setRevisions(
        ("2009-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpV2Xdot3Objects_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Objects = _LldpV2Xdot3Objects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1)
)
_LldpV2Xdot3Config_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Config = _LldpV2Xdot3Config_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1)
)
_LldpV2Xdot3PortConfigTable_Object = MibTable
lldpV2Xdot3PortConfigTable = _LldpV2Xdot3PortConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigTable.setStatus("current")
_LldpV2Xdot3PortConfigEntry_Object = MibTableRow
lldpV2Xdot3PortConfigEntry = _LldpV2Xdot3PortConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigEntry.setStatus("current")


class _LldpV2Xdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpV2Xdot3PortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("macPhyConfigStatus", 0),
          ("maxFrameSize", 3),
          ("powerViaMDI", 1),
          ("unused", 2))
    )

_LldpV2Xdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpV2Xdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpV2Xdot3PortConfigTLVsTxEnable = _LldpV2Xdot3PortConfigTLVsTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1, 1, 1),
    _LldpV2Xdot3PortConfigTLVsTxEnable_Type()
)
lldpV2Xdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpV2Xdot3LocalData_ObjectIdentity = ObjectIdentity
lldpV2Xdot3LocalData = _LldpV2Xdot3LocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2)
)
_LldpV2Xdot3LocPortTable_Object = MibTable
lldpV2Xdot3LocPortTable = _LldpV2Xdot3LocPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortTable.setStatus("current")
_LldpV2Xdot3LocPortEntry_Object = MibTableRow
lldpV2Xdot3LocPortEntry = _LldpV2Xdot3LocPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1)
)
lldpV2Xdot3LocPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortEntry.setStatus("current")
_LldpV2Xdot3LocPortAutoNegSupported_Type = TruthValue
_LldpV2Xdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegSupported = _LldpV2Xdot3LocPortAutoNegSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 1),
    _LldpV2Xdot3LocPortAutoNegSupported_Type()
)
lldpV2Xdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegSupported.setStatus("current")
_LldpV2Xdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpV2Xdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegEnabled = _LldpV2Xdot3LocPortAutoNegEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 2),
    _LldpV2Xdot3LocPortAutoNegEnabled_Type()
)
lldpV2Xdot3LocPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegEnabled.setStatus("current")


class _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpV2Xdot3LocPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegAdvertisedCap = _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 3),
    _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type()
)
lldpV2Xdot3LocPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegAdvertisedCap.setStatus("current")


class _LldpV2Xdot3LocPortOperMauType_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPortOperMauType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2Xdot3LocPortOperMauType_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPortOperMauType_Object = MibTableColumn
lldpV2Xdot3LocPortOperMauType = _LldpV2Xdot3LocPortOperMauType_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 4),
    _LldpV2Xdot3LocPortOperMauType_Type()
)
lldpV2Xdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortOperMauType.setStatus("current")
_LldpV2Xdot3LocPowerTable_Object = MibTable
lldpV2Xdot3LocPowerTable = _LldpV2Xdot3LocPowerTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerTable.setStatus("current")
_LldpV2Xdot3LocPowerEntry_Object = MibTableRow
lldpV2Xdot3LocPowerEntry = _LldpV2Xdot3LocPowerEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1)
)
lldpV2Xdot3LocPowerEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerEntry.setStatus("current")
_LldpV2Xdot3LocPowerPortClass_Type = LldpV2PowerPortClass
_LldpV2Xdot3LocPowerPortClass_Object = MibTableColumn
lldpV2Xdot3LocPowerPortClass = _LldpV2Xdot3LocPowerPortClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 1),
    _LldpV2Xdot3LocPowerPortClass_Type()
)
lldpV2Xdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPortClass.setStatus("current")
_LldpV2Xdot3LocPowerMDISupported_Type = TruthValue
_LldpV2Xdot3LocPowerMDISupported_Object = MibTableColumn
lldpV2Xdot3LocPowerMDISupported = _LldpV2Xdot3LocPowerMDISupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 2),
    _LldpV2Xdot3LocPowerMDISupported_Type()
)
lldpV2Xdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerMDISupported.setStatus("current")
_LldpV2Xdot3LocPowerMDIEnabled_Type = TruthValue
_LldpV2Xdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpV2Xdot3LocPowerMDIEnabled = _LldpV2Xdot3LocPowerMDIEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 3),
    _LldpV2Xdot3LocPowerMDIEnabled_Type()
)
lldpV2Xdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerMDIEnabled.setStatus("current")
_LldpV2Xdot3LocPowerPairControlable_Type = TruthValue
_LldpV2Xdot3LocPowerPairControlable_Object = MibTableColumn
lldpV2Xdot3LocPowerPairControlable = _LldpV2Xdot3LocPowerPairControlable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 4),
    _LldpV2Xdot3LocPowerPairControlable_Type()
)
lldpV2Xdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPairControlable.setStatus("current")


class _LldpV2Xdot3LocPowerPairs_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPowerPairs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpV2Xdot3LocPowerPairs_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPowerPairs_Object = MibTableColumn
lldpV2Xdot3LocPowerPairs = _LldpV2Xdot3LocPowerPairs_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 5),
    _LldpV2Xdot3LocPowerPairs_Type()
)
lldpV2Xdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPairs.setStatus("current")


class _LldpV2Xdot3LocPowerClass_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPowerClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpV2Xdot3LocPowerClass_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPowerClass_Object = MibTableColumn
lldpV2Xdot3LocPowerClass = _LldpV2Xdot3LocPowerClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 6),
    _LldpV2Xdot3LocPowerClass_Type()
)
lldpV2Xdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerClass.setStatus("current")
_LldpV2Xdot3LocMaxFrameSizeTable_Object = MibTable
lldpV2Xdot3LocMaxFrameSizeTable = _LldpV2Xdot3LocMaxFrameSizeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSizeTable.setStatus("current")
_LldpV2Xdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpV2Xdot3LocMaxFrameSizeEntry = _LldpV2Xdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3, 1)
)
lldpV2Xdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSizeEntry.setStatus("current")


class _LldpV2Xdot3LocMaxFrameSize_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpV2Xdot3LocMaxFrameSize_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocMaxFrameSize_Object = MibTableColumn
lldpV2Xdot3LocMaxFrameSize = _LldpV2Xdot3LocMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3, 1, 1),
    _LldpV2Xdot3LocMaxFrameSize_Type()
)
lldpV2Xdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSize.setStatus("current")
_LldpV2Xdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpV2Xdot3RemoteData = _LldpV2Xdot3RemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3)
)
_LldpV2Xdot3RemPortTable_Object = MibTable
lldpV2Xdot3RemPortTable = _LldpV2Xdot3RemPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortTable.setStatus("current")
_LldpV2Xdot3RemPortEntry_Object = MibTableRow
lldpV2Xdot3RemPortEntry = _LldpV2Xdot3RemPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1)
)
lldpV2Xdot3RemPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortEntry.setStatus("current")
_LldpV2Xdot3RemPortAutoNegSupported_Type = TruthValue
_LldpV2Xdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegSupported = _LldpV2Xdot3RemPortAutoNegSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 1),
    _LldpV2Xdot3RemPortAutoNegSupported_Type()
)
lldpV2Xdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegSupported.setStatus("current")
_LldpV2Xdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpV2Xdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegEnabled = _LldpV2Xdot3RemPortAutoNegEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 2),
    _LldpV2Xdot3RemPortAutoNegEnabled_Type()
)
lldpV2Xdot3RemPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegEnabled.setStatus("current")


class _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpV2Xdot3RemPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegAdvertisedCap = _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 3),
    _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type()
)
lldpV2Xdot3RemPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegAdvertisedCap.setStatus("current")


class _LldpV2Xdot3RemPortOperMauType_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPortOperMauType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2Xdot3RemPortOperMauType_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPortOperMauType_Object = MibTableColumn
lldpV2Xdot3RemPortOperMauType = _LldpV2Xdot3RemPortOperMauType_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 4),
    _LldpV2Xdot3RemPortOperMauType_Type()
)
lldpV2Xdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortOperMauType.setStatus("current")
_LldpV2Xdot3RemPowerTable_Object = MibTable
lldpV2Xdot3RemPowerTable = _LldpV2Xdot3RemPowerTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerTable.setStatus("current")
_LldpV2Xdot3RemPowerEntry_Object = MibTableRow
lldpV2Xdot3RemPowerEntry = _LldpV2Xdot3RemPowerEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1)
)
lldpV2Xdot3RemPowerEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerEntry.setStatus("current")
_LldpV2Xdot3RemPowerPortClass_Type = LldpV2PowerPortClass
_LldpV2Xdot3RemPowerPortClass_Object = MibTableColumn
lldpV2Xdot3RemPowerPortClass = _LldpV2Xdot3RemPowerPortClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 1),
    _LldpV2Xdot3RemPowerPortClass_Type()
)
lldpV2Xdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPortClass.setStatus("current")
_LldpV2Xdot3RemPowerMDISupported_Type = TruthValue
_LldpV2Xdot3RemPowerMDISupported_Object = MibTableColumn
lldpV2Xdot3RemPowerMDISupported = _LldpV2Xdot3RemPowerMDISupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 2),
    _LldpV2Xdot3RemPowerMDISupported_Type()
)
lldpV2Xdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerMDISupported.setStatus("current")
_LldpV2Xdot3RemPowerMDIEnabled_Type = TruthValue
_LldpV2Xdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpV2Xdot3RemPowerMDIEnabled = _LldpV2Xdot3RemPowerMDIEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 3),
    _LldpV2Xdot3RemPowerMDIEnabled_Type()
)
lldpV2Xdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerMDIEnabled.setStatus("current")
_LldpV2Xdot3RemPowerPairControlable_Type = TruthValue
_LldpV2Xdot3RemPowerPairControlable_Object = MibTableColumn
lldpV2Xdot3RemPowerPairControlable = _LldpV2Xdot3RemPowerPairControlable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 4),
    _LldpV2Xdot3RemPowerPairControlable_Type()
)
lldpV2Xdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPairControlable.setStatus("current")


class _LldpV2Xdot3RemPowerPairs_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPowerPairs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpV2Xdot3RemPowerPairs_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPowerPairs_Object = MibTableColumn
lldpV2Xdot3RemPowerPairs = _LldpV2Xdot3RemPowerPairs_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 5),
    _LldpV2Xdot3RemPowerPairs_Type()
)
lldpV2Xdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPairs.setStatus("current")


class _LldpV2Xdot3RemPowerClass_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPowerClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpV2Xdot3RemPowerClass_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPowerClass_Object = MibTableColumn
lldpV2Xdot3RemPowerClass = _LldpV2Xdot3RemPowerClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 6),
    _LldpV2Xdot3RemPowerClass_Type()
)
lldpV2Xdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerClass.setStatus("current")
_LldpV2Xdot3RemMaxFrameSizeTable_Object = MibTable
lldpV2Xdot3RemMaxFrameSizeTable = _LldpV2Xdot3RemMaxFrameSizeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSizeTable.setStatus("current")
_LldpV2Xdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpV2Xdot3RemMaxFrameSizeEntry = _LldpV2Xdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3, 1)
)
lldpV2Xdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSizeEntry.setStatus("current")


class _LldpV2Xdot3RemMaxFrameSize_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpV2Xdot3RemMaxFrameSize_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemMaxFrameSize_Object = MibTableColumn
lldpV2Xdot3RemMaxFrameSize = _LldpV2Xdot3RemMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3, 1, 1),
    _LldpV2Xdot3RemMaxFrameSize_Type()
)
lldpV2Xdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSize.setStatus("current")
_LldpV2Xdot3Conformance_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Conformance = _LldpV2Xdot3Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2)
)
_LldpV2Xdot3Compliances_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Compliances = _LldpV2Xdot3Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1)
)
_LldpV2Xdot3Groups_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Groups = _LldpV2Xdot3Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT3-V2-MIB",
     "lldpV2Xdot3PortConfigEntry")
)
lldpV2Xdot3PortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpV2Xdot3ConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 1)
)
lldpV2Xdot3ConfigGroup.setObjects(
    ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3PortConfigTLVsTxEnable")
)
if mibBuilder.loadTexts:
    lldpV2Xdot3ConfigGroup.setStatus("current")

lldpV2Xdot3LocSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 2)
)
lldpV2Xdot3LocSysGroup.setObjects(
      *(("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPortAutoNegSupported"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPortAutoNegEnabled"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPortAutoNegAdvertisedCap"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPortOperMauType"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerPortClass"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerMDISupported"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerMDIEnabled"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerPairControlable"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerPairs"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocPowerClass"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3LocMaxFrameSize"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocSysGroup.setStatus("current")

lldpV2Xdot3RemSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 3)
)
lldpV2Xdot3RemSysGroup.setObjects(
      *(("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPortAutoNegSupported"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPortAutoNegEnabled"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPortAutoNegAdvertisedCap"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPortOperMauType"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerPortClass"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerMDISupported"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerMDIEnabled"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerPairControlable"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerPairs"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemPowerClass"),
        ("LLDP-EXT-DOT3-V2-MIB", "lldpV2Xdot3RemMaxFrameSize"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpV2Xdot3TxRxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3TxRxCompliance.setStatus(
        "current"
    )

lldpV2Xdot3TxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3TxCompliance.setStatus(
        "current"
    )

lldpV2Xdot3RxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT3-V2-MIB",
    **{"lldpV2Xdot3MIB": lldpV2Xdot3MIB,
       "lldpV2Xdot3Objects": lldpV2Xdot3Objects,
       "lldpV2Xdot3Config": lldpV2Xdot3Config,
       "lldpV2Xdot3PortConfigTable": lldpV2Xdot3PortConfigTable,
       "lldpV2Xdot3PortConfigEntry": lldpV2Xdot3PortConfigEntry,
       "lldpV2Xdot3PortConfigTLVsTxEnable": lldpV2Xdot3PortConfigTLVsTxEnable,
       "lldpV2Xdot3LocalData": lldpV2Xdot3LocalData,
       "lldpV2Xdot3LocPortTable": lldpV2Xdot3LocPortTable,
       "lldpV2Xdot3LocPortEntry": lldpV2Xdot3LocPortEntry,
       "lldpV2Xdot3LocPortAutoNegSupported": lldpV2Xdot3LocPortAutoNegSupported,
       "lldpV2Xdot3LocPortAutoNegEnabled": lldpV2Xdot3LocPortAutoNegEnabled,
       "lldpV2Xdot3LocPortAutoNegAdvertisedCap": lldpV2Xdot3LocPortAutoNegAdvertisedCap,
       "lldpV2Xdot3LocPortOperMauType": lldpV2Xdot3LocPortOperMauType,
       "lldpV2Xdot3LocPowerTable": lldpV2Xdot3LocPowerTable,
       "lldpV2Xdot3LocPowerEntry": lldpV2Xdot3LocPowerEntry,
       "lldpV2Xdot3LocPowerPortClass": lldpV2Xdot3LocPowerPortClass,
       "lldpV2Xdot3LocPowerMDISupported": lldpV2Xdot3LocPowerMDISupported,
       "lldpV2Xdot3LocPowerMDIEnabled": lldpV2Xdot3LocPowerMDIEnabled,
       "lldpV2Xdot3LocPowerPairControlable": lldpV2Xdot3LocPowerPairControlable,
       "lldpV2Xdot3LocPowerPairs": lldpV2Xdot3LocPowerPairs,
       "lldpV2Xdot3LocPowerClass": lldpV2Xdot3LocPowerClass,
       "lldpV2Xdot3LocMaxFrameSizeTable": lldpV2Xdot3LocMaxFrameSizeTable,
       "lldpV2Xdot3LocMaxFrameSizeEntry": lldpV2Xdot3LocMaxFrameSizeEntry,
       "lldpV2Xdot3LocMaxFrameSize": lldpV2Xdot3LocMaxFrameSize,
       "lldpV2Xdot3RemoteData": lldpV2Xdot3RemoteData,
       "lldpV2Xdot3RemPortTable": lldpV2Xdot3RemPortTable,
       "lldpV2Xdot3RemPortEntry": lldpV2Xdot3RemPortEntry,
       "lldpV2Xdot3RemPortAutoNegSupported": lldpV2Xdot3RemPortAutoNegSupported,
       "lldpV2Xdot3RemPortAutoNegEnabled": lldpV2Xdot3RemPortAutoNegEnabled,
       "lldpV2Xdot3RemPortAutoNegAdvertisedCap": lldpV2Xdot3RemPortAutoNegAdvertisedCap,
       "lldpV2Xdot3RemPortOperMauType": lldpV2Xdot3RemPortOperMauType,
       "lldpV2Xdot3RemPowerTable": lldpV2Xdot3RemPowerTable,
       "lldpV2Xdot3RemPowerEntry": lldpV2Xdot3RemPowerEntry,
       "lldpV2Xdot3RemPowerPortClass": lldpV2Xdot3RemPowerPortClass,
       "lldpV2Xdot3RemPowerMDISupported": lldpV2Xdot3RemPowerMDISupported,
       "lldpV2Xdot3RemPowerMDIEnabled": lldpV2Xdot3RemPowerMDIEnabled,
       "lldpV2Xdot3RemPowerPairControlable": lldpV2Xdot3RemPowerPairControlable,
       "lldpV2Xdot3RemPowerPairs": lldpV2Xdot3RemPowerPairs,
       "lldpV2Xdot3RemPowerClass": lldpV2Xdot3RemPowerClass,
       "lldpV2Xdot3RemMaxFrameSizeTable": lldpV2Xdot3RemMaxFrameSizeTable,
       "lldpV2Xdot3RemMaxFrameSizeEntry": lldpV2Xdot3RemMaxFrameSizeEntry,
       "lldpV2Xdot3RemMaxFrameSize": lldpV2Xdot3RemMaxFrameSize,
       "lldpV2Xdot3Conformance": lldpV2Xdot3Conformance,
       "lldpV2Xdot3Compliances": lldpV2Xdot3Compliances,
       "lldpV2Xdot3TxRxCompliance": lldpV2Xdot3TxRxCompliance,
       "lldpV2Xdot3TxCompliance": lldpV2Xdot3TxCompliance,
       "lldpV2Xdot3RxCompliance": lldpV2Xdot3RxCompliance,
       "lldpV2Xdot3Groups": lldpV2Xdot3Groups,
       "lldpV2Xdot3ConfigGroup": lldpV2Xdot3ConfigGroup,
       "lldpV2Xdot3LocSysGroup": lldpV2Xdot3LocSysGroup,
       "lldpV2Xdot3RemSysGroup": lldpV2Xdot3RemSysGroup}
)
