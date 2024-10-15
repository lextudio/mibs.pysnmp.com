# SNMP MIB module (Wellfleet-MIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:40 2024
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

(wfMobileIpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfMobileIpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMobileIpHaTable_Object = MibTable
wfMobileIpHaTable = _WfMobileIpHaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1)
)
if mibBuilder.loadTexts:
    wfMobileIpHaTable.setStatus("mandatory")
_WfMobileIpHaEntry_Object = MibTableRow
wfMobileIpHaEntry = _WfMobileIpHaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1)
)
wfMobileIpHaEntry.setIndexNames(
    (0, "Wellfleet-MIP-MIB", "wfMobileIpHaAddr"),
    (0, "Wellfleet-MIP-MIB", "wfMobileIpHaCct"),
)
if mibBuilder.loadTexts:
    wfMobileIpHaEntry.setStatus("mandatory")


class _WfMobileIpHaCreate_Type(Integer32):
    """Custom type wfMobileIpHaCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfMobileIpHaCreate_Type.__name__ = "Integer32"
_WfMobileIpHaCreate_Object = MibTableColumn
wfMobileIpHaCreate = _WfMobileIpHaCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 1),
    _WfMobileIpHaCreate_Type()
)
wfMobileIpHaCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpHaCreate.setStatus("mandatory")


class _WfMobileIpHaEnable_Type(Integer32):
    """Custom type wfMobileIpHaEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfMobileIpHaEnable_Type.__name__ = "Integer32"
_WfMobileIpHaEnable_Object = MibTableColumn
wfMobileIpHaEnable = _WfMobileIpHaEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 2),
    _WfMobileIpHaEnable_Type()
)
wfMobileIpHaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpHaEnable.setStatus("mandatory")


class _WfMobileIpHaState_Type(Integer32):
    """Custom type wfMobileIpHaState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfMobileIpHaState_Type.__name__ = "Integer32"
_WfMobileIpHaState_Object = MibTableColumn
wfMobileIpHaState = _WfMobileIpHaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 3),
    _WfMobileIpHaState_Type()
)
wfMobileIpHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMobileIpHaState.setStatus("mandatory")
_WfMobileIpHaAddr_Type = IpAddress
_WfMobileIpHaAddr_Object = MibTableColumn
wfMobileIpHaAddr = _WfMobileIpHaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 4),
    _WfMobileIpHaAddr_Type()
)
wfMobileIpHaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMobileIpHaAddr.setStatus("mandatory")
_WfMobileIpHaCct_Type = Integer32
_WfMobileIpHaCct_Object = MibTableColumn
wfMobileIpHaCct = _WfMobileIpHaCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 5),
    _WfMobileIpHaCct_Type()
)
wfMobileIpHaCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMobileIpHaCct.setStatus("mandatory")
_WfMobileIpHaProtoMap_Type = OctetString
_WfMobileIpHaProtoMap_Object = MibTableColumn
wfMobileIpHaProtoMap = _WfMobileIpHaProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 6),
    _WfMobileIpHaProtoMap_Type()
)
wfMobileIpHaProtoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpHaProtoMap.setStatus("mandatory")


class _WfMobileIpHaStatsEnable_Type(Integer32):
    """Custom type wfMobileIpHaStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfMobileIpHaStatsEnable_Type.__name__ = "Integer32"
_WfMobileIpHaStatsEnable_Object = MibTableColumn
wfMobileIpHaStatsEnable = _WfMobileIpHaStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 7),
    _WfMobileIpHaStatsEnable_Type()
)
wfMobileIpHaStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpHaStatsEnable.setStatus("mandatory")
_WfMobileIpHaDebugLevel_Type = Integer32
_WfMobileIpHaDebugLevel_Object = MibTableColumn
wfMobileIpHaDebugLevel = _WfMobileIpHaDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 1, 1, 8),
    _WfMobileIpHaDebugLevel_Type()
)
wfMobileIpHaDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpHaDebugLevel.setStatus("mandatory")
_WfMobileIpSpiTable_Object = MibTable
wfMobileIpSpiTable = _WfMobileIpSpiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2)
)
if mibBuilder.loadTexts:
    wfMobileIpSpiTable.setStatus("mandatory")
_WfMobileIpSpiEntry_Object = MibTableRow
wfMobileIpSpiEntry = _WfMobileIpSpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2, 1)
)
wfMobileIpSpiEntry.setIndexNames(
    (0, "Wellfleet-MIP-MIB", "wfMobileIpSpiValue"),
)
if mibBuilder.loadTexts:
    wfMobileIpSpiEntry.setStatus("mandatory")


class _WfMobileIpSpiCreate_Type(Integer32):
    """Custom type wfMobileIpSpiCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfMobileIpSpiCreate_Type.__name__ = "Integer32"
_WfMobileIpSpiCreate_Object = MibTableColumn
wfMobileIpSpiCreate = _WfMobileIpSpiCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2, 1, 1),
    _WfMobileIpSpiCreate_Type()
)
wfMobileIpSpiCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpSpiCreate.setStatus("mandatory")


class _WfMobileIpSpiValue_Type(Integer32):
    """Custom type wfMobileIpSpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_WfMobileIpSpiValue_Type.__name__ = "Integer32"
_WfMobileIpSpiValue_Object = MibTableColumn
wfMobileIpSpiValue = _WfMobileIpSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2, 1, 2),
    _WfMobileIpSpiValue_Type()
)
wfMobileIpSpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMobileIpSpiValue.setStatus("mandatory")
_WfMobileIpSpiKey_Type = OctetString
_WfMobileIpSpiKey_Object = MibTableColumn
wfMobileIpSpiKey = _WfMobileIpSpiKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2, 1, 3),
    _WfMobileIpSpiKey_Type()
)
wfMobileIpSpiKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpSpiKey.setStatus("mandatory")


class _WfMobileIpSpiAuthType_Type(Integer32):
    """Custom type wfMobileIpSpiAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("md5", 1)
    )


_WfMobileIpSpiAuthType_Type.__name__ = "Integer32"
_WfMobileIpSpiAuthType_Object = MibTableColumn
wfMobileIpSpiAuthType = _WfMobileIpSpiAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 2, 1, 4),
    _WfMobileIpSpiAuthType_Type()
)
wfMobileIpSpiAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMobileIpSpiAuthType.setStatus("mandatory")
_WfHaMobilityBindingTable_Object = MibTable
wfHaMobilityBindingTable = _WfHaMobilityBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3)
)
if mibBuilder.loadTexts:
    wfHaMobilityBindingTable.setStatus("mandatory")
_WfHaMobilityBindingEntry_Object = MibTableRow
wfHaMobilityBindingEntry = _WfHaMobilityBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1)
)
wfHaMobilityBindingEntry.setIndexNames(
    (0, "Wellfleet-MIP-MIB", "wfHaMobilityBindingIdx"),
    (0, "Wellfleet-MIP-MIB", "wfHaMobilityBindingCOA"),
)
if mibBuilder.loadTexts:
    wfHaMobilityBindingEntry.setStatus("mandatory")
_WfHaMobilityBindingIdx_Type = Integer32
_WfHaMobilityBindingIdx_Object = MibTableColumn
wfHaMobilityBindingIdx = _WfHaMobilityBindingIdx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 1),
    _WfHaMobilityBindingIdx_Type()
)
wfHaMobilityBindingIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingIdx.setStatus("mandatory")
_WfHaMobilityBindingMN_Type = IpAddress
_WfHaMobilityBindingMN_Object = MibTableColumn
wfHaMobilityBindingMN = _WfHaMobilityBindingMN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 2),
    _WfHaMobilityBindingMN_Type()
)
wfHaMobilityBindingMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingMN.setStatus("mandatory")
_WfHaMobilityBindingCOA_Type = IpAddress
_WfHaMobilityBindingCOA_Object = MibTableColumn
wfHaMobilityBindingCOA = _WfHaMobilityBindingCOA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 3),
    _WfHaMobilityBindingCOA_Type()
)
wfHaMobilityBindingCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingCOA.setStatus("mandatory")
_WfHaMobilityBindingSourceAddress_Type = IpAddress
_WfHaMobilityBindingSourceAddress_Object = MibTableColumn
wfHaMobilityBindingSourceAddress = _WfHaMobilityBindingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 4),
    _WfHaMobilityBindingSourceAddress_Type()
)
wfHaMobilityBindingSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingSourceAddress.setStatus("mandatory")


class _WfHaMobilityBindingRegFlags_Type(Integer32):
    """Custom type wfHaMobilityBindingRegFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaMobilityBindingRegFlags_Type.__name__ = "Integer32"
_WfHaMobilityBindingRegFlags_Object = MibTableColumn
wfHaMobilityBindingRegFlags = _WfHaMobilityBindingRegFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 5),
    _WfHaMobilityBindingRegFlags_Type()
)
wfHaMobilityBindingRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingRegFlags.setStatus("mandatory")


class _WfHaMobilityBindingRegIDLow_Type(Integer32):
    """Custom type wfHaMobilityBindingRegIDLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaMobilityBindingRegIDLow_Type.__name__ = "Integer32"
_WfHaMobilityBindingRegIDLow_Object = MibTableColumn
wfHaMobilityBindingRegIDLow = _WfHaMobilityBindingRegIDLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 6),
    _WfHaMobilityBindingRegIDLow_Type()
)
wfHaMobilityBindingRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingRegIDLow.setStatus("mandatory")


class _WfHaMobilityBindingRegIDHigh_Type(Integer32):
    """Custom type wfHaMobilityBindingRegIDHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaMobilityBindingRegIDHigh_Type.__name__ = "Integer32"
_WfHaMobilityBindingRegIDHigh_Object = MibTableColumn
wfHaMobilityBindingRegIDHigh = _WfHaMobilityBindingRegIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 7),
    _WfHaMobilityBindingRegIDHigh_Type()
)
wfHaMobilityBindingRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingRegIDHigh.setStatus("mandatory")


class _WfHaMobilityBindingTimeGranted_Type(Integer32):
    """Custom type wfHaMobilityBindingTimeGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaMobilityBindingTimeGranted_Type.__name__ = "Integer32"
_WfHaMobilityBindingTimeGranted_Object = MibTableColumn
wfHaMobilityBindingTimeGranted = _WfHaMobilityBindingTimeGranted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 8),
    _WfHaMobilityBindingTimeGranted_Type()
)
wfHaMobilityBindingTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingTimeGranted.setStatus("mandatory")


class _WfHaMobilityBindingTimeRemaining_Type(Integer32):
    """Custom type wfHaMobilityBindingTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaMobilityBindingTimeRemaining_Type.__name__ = "Integer32"
_WfHaMobilityBindingTimeRemaining_Object = MibTableColumn
wfHaMobilityBindingTimeRemaining = _WfHaMobilityBindingTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 3, 1, 9),
    _WfHaMobilityBindingTimeRemaining_Type()
)
wfHaMobilityBindingTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaMobilityBindingTimeRemaining.setStatus("mandatory")
_WfHaIpxMobilityBindingTable_Object = MibTable
wfHaIpxMobilityBindingTable = _WfHaIpxMobilityBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4)
)
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingTable.setStatus("mandatory")
_WfHaIpxMobilityBindingEntry_Object = MibTableRow
wfHaIpxMobilityBindingEntry = _WfHaIpxMobilityBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1)
)
wfHaIpxMobilityBindingEntry.setIndexNames(
    (0, "Wellfleet-MIP-MIB", "wfHaIpxMobilityBindingIdx"),
    (0, "Wellfleet-MIP-MIB", "wfHaIpxMobilityBindingCOA"),
)
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingEntry.setStatus("mandatory")
_WfHaIpxMobilityBindingIdx_Type = Integer32
_WfHaIpxMobilityBindingIdx_Object = MibTableColumn
wfHaIpxMobilityBindingIdx = _WfHaIpxMobilityBindingIdx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 1),
    _WfHaIpxMobilityBindingIdx_Type()
)
wfHaIpxMobilityBindingIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingIdx.setStatus("mandatory")


class _WfHaIpxMobilityBindingMN_Type(OctetString):
    """Custom type wfHaIpxMobilityBindingMN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfHaIpxMobilityBindingMN_Type.__name__ = "OctetString"
_WfHaIpxMobilityBindingMN_Object = MibTableColumn
wfHaIpxMobilityBindingMN = _WfHaIpxMobilityBindingMN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 2),
    _WfHaIpxMobilityBindingMN_Type()
)
wfHaIpxMobilityBindingMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingMN.setStatus("mandatory")
_WfHaIpxMobilityBindingCOA_Type = IpAddress
_WfHaIpxMobilityBindingCOA_Object = MibTableColumn
wfHaIpxMobilityBindingCOA = _WfHaIpxMobilityBindingCOA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 3),
    _WfHaIpxMobilityBindingCOA_Type()
)
wfHaIpxMobilityBindingCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingCOA.setStatus("mandatory")
_WfHaIpxMobilityBindingSourceAddress_Type = IpAddress
_WfHaIpxMobilityBindingSourceAddress_Object = MibTableColumn
wfHaIpxMobilityBindingSourceAddress = _WfHaIpxMobilityBindingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 4),
    _WfHaIpxMobilityBindingSourceAddress_Type()
)
wfHaIpxMobilityBindingSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingSourceAddress.setStatus("mandatory")


class _WfHaIpxMobilityBindingRegFlags_Type(Integer32):
    """Custom type wfHaIpxMobilityBindingRegFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaIpxMobilityBindingRegFlags_Type.__name__ = "Integer32"
_WfHaIpxMobilityBindingRegFlags_Object = MibTableColumn
wfHaIpxMobilityBindingRegFlags = _WfHaIpxMobilityBindingRegFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 5),
    _WfHaIpxMobilityBindingRegFlags_Type()
)
wfHaIpxMobilityBindingRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingRegFlags.setStatus("mandatory")


class _WfHaIpxMobilityBindingRegIDLow_Type(Integer32):
    """Custom type wfHaIpxMobilityBindingRegIDLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaIpxMobilityBindingRegIDLow_Type.__name__ = "Integer32"
_WfHaIpxMobilityBindingRegIDLow_Object = MibTableColumn
wfHaIpxMobilityBindingRegIDLow = _WfHaIpxMobilityBindingRegIDLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 6),
    _WfHaIpxMobilityBindingRegIDLow_Type()
)
wfHaIpxMobilityBindingRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingRegIDLow.setStatus("mandatory")


class _WfHaIpxMobilityBindingRegIDHigh_Type(Integer32):
    """Custom type wfHaIpxMobilityBindingRegIDHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaIpxMobilityBindingRegIDHigh_Type.__name__ = "Integer32"
_WfHaIpxMobilityBindingRegIDHigh_Object = MibTableColumn
wfHaIpxMobilityBindingRegIDHigh = _WfHaIpxMobilityBindingRegIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 7),
    _WfHaIpxMobilityBindingRegIDHigh_Type()
)
wfHaIpxMobilityBindingRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingRegIDHigh.setStatus("mandatory")


class _WfHaIpxMobilityBindingTimeGranted_Type(Integer32):
    """Custom type wfHaIpxMobilityBindingTimeGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaIpxMobilityBindingTimeGranted_Type.__name__ = "Integer32"
_WfHaIpxMobilityBindingTimeGranted_Object = MibTableColumn
wfHaIpxMobilityBindingTimeGranted = _WfHaIpxMobilityBindingTimeGranted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 8),
    _WfHaIpxMobilityBindingTimeGranted_Type()
)
wfHaIpxMobilityBindingTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingTimeGranted.setStatus("mandatory")


class _WfHaIpxMobilityBindingTimeRemaining_Type(Integer32):
    """Custom type wfHaIpxMobilityBindingTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfHaIpxMobilityBindingTimeRemaining_Type.__name__ = "Integer32"
_WfHaIpxMobilityBindingTimeRemaining_Object = MibTableColumn
wfHaIpxMobilityBindingTimeRemaining = _WfHaIpxMobilityBindingTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21, 4, 1, 9),
    _WfHaIpxMobilityBindingTimeRemaining_Type()
)
wfHaIpxMobilityBindingTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHaIpxMobilityBindingTimeRemaining.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MIP-MIB",
    **{"wfMobileIpHaTable": wfMobileIpHaTable,
       "wfMobileIpHaEntry": wfMobileIpHaEntry,
       "wfMobileIpHaCreate": wfMobileIpHaCreate,
       "wfMobileIpHaEnable": wfMobileIpHaEnable,
       "wfMobileIpHaState": wfMobileIpHaState,
       "wfMobileIpHaAddr": wfMobileIpHaAddr,
       "wfMobileIpHaCct": wfMobileIpHaCct,
       "wfMobileIpHaProtoMap": wfMobileIpHaProtoMap,
       "wfMobileIpHaStatsEnable": wfMobileIpHaStatsEnable,
       "wfMobileIpHaDebugLevel": wfMobileIpHaDebugLevel,
       "wfMobileIpSpiTable": wfMobileIpSpiTable,
       "wfMobileIpSpiEntry": wfMobileIpSpiEntry,
       "wfMobileIpSpiCreate": wfMobileIpSpiCreate,
       "wfMobileIpSpiValue": wfMobileIpSpiValue,
       "wfMobileIpSpiKey": wfMobileIpSpiKey,
       "wfMobileIpSpiAuthType": wfMobileIpSpiAuthType,
       "wfHaMobilityBindingTable": wfHaMobilityBindingTable,
       "wfHaMobilityBindingEntry": wfHaMobilityBindingEntry,
       "wfHaMobilityBindingIdx": wfHaMobilityBindingIdx,
       "wfHaMobilityBindingMN": wfHaMobilityBindingMN,
       "wfHaMobilityBindingCOA": wfHaMobilityBindingCOA,
       "wfHaMobilityBindingSourceAddress": wfHaMobilityBindingSourceAddress,
       "wfHaMobilityBindingRegFlags": wfHaMobilityBindingRegFlags,
       "wfHaMobilityBindingRegIDLow": wfHaMobilityBindingRegIDLow,
       "wfHaMobilityBindingRegIDHigh": wfHaMobilityBindingRegIDHigh,
       "wfHaMobilityBindingTimeGranted": wfHaMobilityBindingTimeGranted,
       "wfHaMobilityBindingTimeRemaining": wfHaMobilityBindingTimeRemaining,
       "wfHaIpxMobilityBindingTable": wfHaIpxMobilityBindingTable,
       "wfHaIpxMobilityBindingEntry": wfHaIpxMobilityBindingEntry,
       "wfHaIpxMobilityBindingIdx": wfHaIpxMobilityBindingIdx,
       "wfHaIpxMobilityBindingMN": wfHaIpxMobilityBindingMN,
       "wfHaIpxMobilityBindingCOA": wfHaIpxMobilityBindingCOA,
       "wfHaIpxMobilityBindingSourceAddress": wfHaIpxMobilityBindingSourceAddress,
       "wfHaIpxMobilityBindingRegFlags": wfHaIpxMobilityBindingRegFlags,
       "wfHaIpxMobilityBindingRegIDLow": wfHaIpxMobilityBindingRegIDLow,
       "wfHaIpxMobilityBindingRegIDHigh": wfHaIpxMobilityBindingRegIDHigh,
       "wfHaIpxMobilityBindingTimeGranted": wfHaIpxMobilityBindingTimeGranted,
       "wfHaIpxMobilityBindingTimeRemaining": wfHaIpxMobilityBindingTimeRemaining}
)
