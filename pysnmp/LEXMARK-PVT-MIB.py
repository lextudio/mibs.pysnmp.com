# SNMP MIB module (LEXMARK-PVT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEXMARK-PVT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:49 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lexmark_ObjectIdentity = ObjectIdentity
lexmark = _Lexmark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641)
)
_Adapter_ObjectIdentity = ObjectIdentity
adapter = _Adapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1)
)
_Opsys_ObjectIdentity = ObjectIdentity
opsys = _Opsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 1)
)


class _OpsysCodeRev_Type(DisplayString):
    """Custom type opsysCodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysCodeRev_Type.__name__ = "DisplayString"
_OpsysCodeRev_Object = MibScalar
opsysCodeRev = _OpsysCodeRev_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 1),
    _OpsysCodeRev_Type()
)
opsysCodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCodeRev.setStatus("mandatory")


class _OpsysJobTimeout_Type(Integer32):
    """Custom type opsysJobTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_OpsysJobTimeout_Type.__name__ = "Integer32"
_OpsysJobTimeout_Object = MibScalar
opsysJobTimeout = _OpsysJobTimeout_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 2),
    _OpsysJobTimeout_Type()
)
opsysJobTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsysJobTimeout.setStatus("mandatory")


class _OpsysCurrentJob_Type(DisplayString):
    """Custom type opsysCurrentJob based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysCurrentJob_Type.__name__ = "DisplayString"
_OpsysCurrentJob_Object = MibScalar
opsysCurrentJob = _OpsysCurrentJob_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 3),
    _OpsysCurrentJob_Type()
)
opsysCurrentJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCurrentJob.setStatus("mandatory")
_OpsysRAMSize_Type = Integer32
_OpsysRAMSize_Object = MibScalar
opsysRAMSize = _OpsysRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 4),
    _OpsysRAMSize_Type()
)
opsysRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysRAMSize.setStatus("mandatory")
_OpsysNVRAMSize_Type = Integer32
_OpsysNVRAMSize_Object = MibScalar
opsysNVRAMSize = _OpsysNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 5),
    _OpsysNVRAMSize_Type()
)
opsysNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysNVRAMSize.setStatus("mandatory")
_OpsysROMSize_Type = Integer32
_OpsysROMSize_Object = MibScalar
opsysROMSize = _OpsysROMSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 6),
    _OpsysROMSize_Type()
)
opsysROMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysROMSize.setStatus("mandatory")


class _OpsysROMType_Type(DisplayString):
    """Custom type opsysROMType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysROMType_Type.__name__ = "DisplayString"
_OpsysROMType_Object = MibScalar
opsysROMType = _OpsysROMType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 7),
    _OpsysROMType_Type()
)
opsysROMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysROMType.setStatus("mandatory")


class _OpsysProtocols_Type(Integer32):
    """Custom type opsysProtocols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OpsysProtocols_Type.__name__ = "Integer32"
_OpsysProtocols_Object = MibScalar
opsysProtocols = _OpsysProtocols_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 8),
    _OpsysProtocols_Type()
)
opsysProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysProtocols.setStatus("mandatory")
_OpsysTimeToReset_Type = Integer32
_OpsysTimeToReset_Object = MibScalar
opsysTimeToReset = _OpsysTimeToReset_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 9),
    _OpsysTimeToReset_Type()
)
opsysTimeToReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsysTimeToReset.setStatus("mandatory")


class _OpsysCardPartNo_Type(DisplayString):
    """Custom type opsysCardPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysCardPartNo_Type.__name__ = "DisplayString"
_OpsysCardPartNo_Object = MibScalar
opsysCardPartNo = _OpsysCardPartNo_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 10),
    _OpsysCardPartNo_Type()
)
opsysCardPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCardPartNo.setStatus("mandatory")


class _OpsysCardEC_Type(DisplayString):
    """Custom type opsysCardEC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysCardEC_Type.__name__ = "DisplayString"
_OpsysCardEC_Object = MibScalar
opsysCardEC = _OpsysCardEC_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 11),
    _OpsysCardEC_Type()
)
opsysCardEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCardEC.setStatus("mandatory")
_OpsysCurrentJobTable_Object = MibTable
opsysCurrentJobTable = _OpsysCurrentJobTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 12)
)
if mibBuilder.loadTexts:
    opsysCurrentJobTable.setStatus("mandatory")
_OpsysCurrentJobEntry_Object = MibTableRow
opsysCurrentJobEntry = _OpsysCurrentJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 12, 1)
)
opsysCurrentJobEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "opsysCurrentJobEntryIndex"),
)
if mibBuilder.loadTexts:
    opsysCurrentJobEntry.setStatus("mandatory")
_OpsysCurrentJobEntryIndex_Type = Integer32
_OpsysCurrentJobEntryIndex_Object = MibTableColumn
opsysCurrentJobEntryIndex = _OpsysCurrentJobEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 12, 1, 1),
    _OpsysCurrentJobEntryIndex_Type()
)
opsysCurrentJobEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCurrentJobEntryIndex.setStatus("mandatory")


class _OpsysCurrentJobString_Type(DisplayString):
    """Custom type opsysCurrentJobString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OpsysCurrentJobString_Type.__name__ = "DisplayString"
_OpsysCurrentJobString_Object = MibTableColumn
opsysCurrentJobString = _OpsysCurrentJobString_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 12, 1, 2),
    _OpsysCurrentJobString_Type()
)
opsysCurrentJobString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysCurrentJobString.setStatus("mandatory")


class _OpsysDeviceType_Type(OctetString):
    """Custom type opsysDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_OpsysDeviceType_Type.__name__ = "OctetString"
_OpsysDeviceType_Object = MibScalar
opsysDeviceType = _OpsysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 13),
    _OpsysDeviceType_Type()
)
opsysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysDeviceType.setStatus("mandatory")


class _OpsysAdapterName_Type(OctetString):
    """Custom type opsysAdapterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_OpsysAdapterName_Type.__name__ = "OctetString"
_OpsysAdapterName_Object = MibScalar
opsysAdapterName = _OpsysAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 14),
    _OpsysAdapterName_Type()
)
opsysAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysAdapterName.setStatus("mandatory")


class _OpsysAdapterCapabilities_Type(OctetString):
    """Custom type opsysAdapterCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OpsysAdapterCapabilities_Type.__name__ = "OctetString"
_OpsysAdapterCapabilities_Object = MibScalar
opsysAdapterCapabilities = _OpsysAdapterCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 1, 15),
    _OpsysAdapterCapabilities_Type()
)
opsysAdapterCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsysAdapterCapabilities.setStatus("mandatory")
_Lexlink_ObjectIdentity = ObjectIdentity
lexlink = _Lexlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 2)
)


class _LexlinkActivated_Type(Integer32):
    """Custom type lexlinkActivated based on Integer32"""
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


_LexlinkActivated_Type.__name__ = "Integer32"
_LexlinkActivated_Object = MibScalar
lexlinkActivated = _LexlinkActivated_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 2, 1),
    _LexlinkActivated_Type()
)
lexlinkActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexlinkActivated.setStatus("mandatory")


class _LexlinkNickname_Type(DisplayString):
    """Custom type lexlinkNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_LexlinkNickname_Type.__name__ = "DisplayString"
_LexlinkNickname_Object = MibScalar
lexlinkNickname = _LexlinkNickname_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 2, 2),
    _LexlinkNickname_Type()
)
lexlinkNickname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexlinkNickname.setStatus("mandatory")
_Lexipx_ObjectIdentity = ObjectIdentity
lexipx = _Lexipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 3)
)


class _LexipxActivated_Type(Integer32):
    """Custom type lexipxActivated based on Integer32"""
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


_LexipxActivated_Type.__name__ = "Integer32"
_LexipxActivated_Object = MibScalar
lexipxActivated = _LexipxActivated_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 1),
    _LexipxActivated_Type()
)
lexipxActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxActivated.setStatus("mandatory")


class _LexipxLoginName_Type(DisplayString):
    """Custom type lexipxLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_LexipxLoginName_Type.__name__ = "DisplayString"
_LexipxLoginName_Object = MibScalar
lexipxLoginName = _LexipxLoginName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 2),
    _LexipxLoginName_Type()
)
lexipxLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxLoginName.setStatus("mandatory")


class _LexipxNetNumber_Type(DisplayString):
    """Custom type lexipxNetNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LexipxNetNumber_Type.__name__ = "DisplayString"
_LexipxNetNumber_Object = MibScalar
lexipxNetNumber = _LexipxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 3),
    _LexipxNetNumber_Type()
)
lexipxNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxNetNumber.setStatus("mandatory")


class _LexipxSAPMode_Type(Integer32):
    """Custom type lexipxSAPMode based on Integer32"""
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


_LexipxSAPMode_Type.__name__ = "Integer32"
_LexipxSAPMode_Object = MibScalar
lexipxSAPMode = _LexipxSAPMode_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 4),
    _LexipxSAPMode_Type()
)
lexipxSAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxSAPMode.setStatus("mandatory")


class _LexipxServerMode_Type(Integer32):
    """Custom type lexipxServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pserver", 1),
          ("rprinter", 2))
    )


_LexipxServerMode_Type.__name__ = "Integer32"
_LexipxServerMode_Object = MibScalar
lexipxServerMode = _LexipxServerMode_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 5),
    _LexipxServerMode_Type()
)
lexipxServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxServerMode.setStatus("mandatory")
_LexipxNumPorts_Type = Integer32
_LexipxNumPorts_Object = MibScalar
lexipxNumPorts = _LexipxNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 6),
    _LexipxNumPorts_Type()
)
lexipxNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxNumPorts.setStatus("mandatory")
_LexipxPortInfoTable_Object = MibTable
lexipxPortInfoTable = _LexipxPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7)
)
if mibBuilder.loadTexts:
    lexipxPortInfoTable.setStatus("mandatory")
_LexipxPortInfoEntry_Object = MibTableRow
lexipxPortInfoEntry = _LexipxPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7, 1)
)
lexipxPortInfoEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexipxPortInfoIndex"),
)
if mibBuilder.loadTexts:
    lexipxPortInfoEntry.setStatus("mandatory")
_LexipxPortInfoIndex_Type = Integer32
_LexipxPortInfoIndex_Object = MibTableColumn
lexipxPortInfoIndex = _LexipxPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7, 1, 1),
    _LexipxPortInfoIndex_Type()
)
lexipxPortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxPortInfoIndex.setStatus("mandatory")


class _LexipxPortInfoPollIntvl_Type(Integer32):
    """Custom type lexipxPortInfoPollIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_LexipxPortInfoPollIntvl_Type.__name__ = "Integer32"
_LexipxPortInfoPollIntvl_Object = MibTableColumn
lexipxPortInfoPollIntvl = _LexipxPortInfoPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7, 1, 2),
    _LexipxPortInfoPollIntvl_Type()
)
lexipxPortInfoPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxPortInfoPollIntvl.setStatus("mandatory")


class _LexipxPortInfoEnable_Type(Integer32):
    """Custom type lexipxPortInfoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LexipxPortInfoEnable_Type.__name__ = "Integer32"
_LexipxPortInfoEnable_Object = MibTableColumn
lexipxPortInfoEnable = _LexipxPortInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7, 1, 3),
    _LexipxPortInfoEnable_Type()
)
lexipxPortInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxPortInfoEnable.setStatus("mandatory")


class _LexipxPortInfoBannerPage_Type(Integer32):
    """Custom type lexipxPortInfoBannerPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 3),
          ("off", 1),
          ("postscript", 2))
    )


_LexipxPortInfoBannerPage_Type.__name__ = "Integer32"
_LexipxPortInfoBannerPage_Object = MibTableColumn
lexipxPortInfoBannerPage = _LexipxPortInfoBannerPage_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 7, 1, 4),
    _LexipxPortInfoBannerPage_Type()
)
lexipxPortInfoBannerPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxPortInfoBannerPage.setStatus("mandatory")
_LexipxNumPrefServers_Type = Integer32
_LexipxNumPrefServers_Object = MibScalar
lexipxNumPrefServers = _LexipxNumPrefServers_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 8),
    _LexipxNumPrefServers_Type()
)
lexipxNumPrefServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxNumPrefServers.setStatus("mandatory")
_LexipxPrefSrvrTable_Object = MibTable
lexipxPrefSrvrTable = _LexipxPrefSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 9)
)
if mibBuilder.loadTexts:
    lexipxPrefSrvrTable.setStatus("mandatory")
_LexipxPrefSrvrEntry_Object = MibTableRow
lexipxPrefSrvrEntry = _LexipxPrefSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 9, 1)
)
lexipxPrefSrvrEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexipxPrefSrvrIndex"),
)
if mibBuilder.loadTexts:
    lexipxPrefSrvrEntry.setStatus("mandatory")
_LexipxPrefSrvrIndex_Type = Integer32
_LexipxPrefSrvrIndex_Object = MibTableColumn
lexipxPrefSrvrIndex = _LexipxPrefSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 9, 1, 1),
    _LexipxPrefSrvrIndex_Type()
)
lexipxPrefSrvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxPrefSrvrIndex.setStatus("mandatory")


class _LexipxPrefSrvrName_Type(DisplayString):
    """Custom type lexipxPrefSrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_LexipxPrefSrvrName_Type.__name__ = "DisplayString"
_LexipxPrefSrvrName_Object = MibTableColumn
lexipxPrefSrvrName = _LexipxPrefSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 9, 1, 2),
    _LexipxPrefSrvrName_Type()
)
lexipxPrefSrvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxPrefSrvrName.setStatus("mandatory")
_LexipxConnSrvrTable_Object = MibTable
lexipxConnSrvrTable = _LexipxConnSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10)
)
if mibBuilder.loadTexts:
    lexipxConnSrvrTable.setStatus("mandatory")
_LexipxConnSrvrEntry_Object = MibTableRow
lexipxConnSrvrEntry = _LexipxConnSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1)
)
lexipxConnSrvrEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexipxConnSrvrIndex"),
)
if mibBuilder.loadTexts:
    lexipxConnSrvrEntry.setStatus("mandatory")
_LexipxConnSrvrIndex_Type = Integer32
_LexipxConnSrvrIndex_Object = MibTableColumn
lexipxConnSrvrIndex = _LexipxConnSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 1),
    _LexipxConnSrvrIndex_Type()
)
lexipxConnSrvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrIndex.setStatus("mandatory")


class _LexipxConnSrvrName_Type(DisplayString):
    """Custom type lexipxConnSrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LexipxConnSrvrName_Type.__name__ = "DisplayString"
_LexipxConnSrvrName_Object = MibTableColumn
lexipxConnSrvrName = _LexipxConnSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 2),
    _LexipxConnSrvrName_Type()
)
lexipxConnSrvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrName.setStatus("mandatory")


class _LexipxConnSrvrNet_Type(DisplayString):
    """Custom type lexipxConnSrvrNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LexipxConnSrvrNet_Type.__name__ = "DisplayString"
_LexipxConnSrvrNet_Object = MibTableColumn
lexipxConnSrvrNet = _LexipxConnSrvrNet_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 3),
    _LexipxConnSrvrNet_Type()
)
lexipxConnSrvrNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrNet.setStatus("mandatory")


class _LexipxConnSrvrNode_Type(DisplayString):
    """Custom type lexipxConnSrvrNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LexipxConnSrvrNode_Type.__name__ = "DisplayString"
_LexipxConnSrvrNode_Object = MibTableColumn
lexipxConnSrvrNode = _LexipxConnSrvrNode_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 4),
    _LexipxConnSrvrNode_Type()
)
lexipxConnSrvrNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrNode.setStatus("mandatory")


class _LexipxConnSrvrConnNum_Type(Integer32):
    """Custom type lexipxConnSrvrConnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexipxConnSrvrConnNum_Type.__name__ = "Integer32"
_LexipxConnSrvrConnNum_Object = MibTableColumn
lexipxConnSrvrConnNum = _LexipxConnSrvrConnNum_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 5),
    _LexipxConnSrvrConnNum_Type()
)
lexipxConnSrvrConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrConnNum.setStatus("mandatory")


class _LexipxConnSrvrConnId_Type(Integer32):
    """Custom type lexipxConnSrvrConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexipxConnSrvrConnId_Type.__name__ = "Integer32"
_LexipxConnSrvrConnId_Object = MibTableColumn
lexipxConnSrvrConnId = _LexipxConnSrvrConnId_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 6),
    _LexipxConnSrvrConnId_Type()
)
lexipxConnSrvrConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrConnId.setStatus("mandatory")


class _LexipxConnSrvrPSConnID_Type(Integer32):
    """Custom type lexipxConnSrvrPSConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexipxConnSrvrPSConnID_Type.__name__ = "Integer32"
_LexipxConnSrvrPSConnID_Object = MibTableColumn
lexipxConnSrvrPSConnID = _LexipxConnSrvrPSConnID_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 10, 1, 7),
    _LexipxConnSrvrPSConnID_Type()
)
lexipxConnSrvrPSConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxConnSrvrPSConnID.setStatus("mandatory")


class _LexipxFrameType_Type(Integer32):
    """Custom type lexipxFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LexipxFrameType_Type.__name__ = "Integer32"
_LexipxFrameType_Object = MibScalar
lexipxFrameType = _LexipxFrameType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 11),
    _LexipxFrameType_Type()
)
lexipxFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxFrameType.setStatus("mandatory")
_LexipxTrapTable_Object = MibTable
lexipxTrapTable = _LexipxTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12)
)
if mibBuilder.loadTexts:
    lexipxTrapTable.setStatus("mandatory")
_LexipxTrapEntry_Object = MibTableRow
lexipxTrapEntry = _LexipxTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12, 1)
)
lexipxTrapEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexipxTrapIndex"),
)
if mibBuilder.loadTexts:
    lexipxTrapEntry.setStatus("mandatory")
_LexipxTrapIndex_Type = Integer32
_LexipxTrapIndex_Object = MibTableColumn
lexipxTrapIndex = _LexipxTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12, 1, 1),
    _LexipxTrapIndex_Type()
)
lexipxTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexipxTrapIndex.setStatus("mandatory")


class _LexipxTrapMask_Type(Integer32):
    """Custom type lexipxTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexipxTrapMask_Type.__name__ = "Integer32"
_LexipxTrapMask_Object = MibTableColumn
lexipxTrapMask = _LexipxTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12, 1, 2),
    _LexipxTrapMask_Type()
)
lexipxTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxTrapMask.setStatus("mandatory")


class _LexipxTrapNetworkAddress_Type(OctetString):
    """Custom type lexipxTrapNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LexipxTrapNetworkAddress_Type.__name__ = "OctetString"
_LexipxTrapNetworkAddress_Object = MibTableColumn
lexipxTrapNetworkAddress = _LexipxTrapNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12, 1, 3),
    _LexipxTrapNetworkAddress_Type()
)
lexipxTrapNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxTrapNetworkAddress.setStatus("mandatory")


class _LexipxTrapNodeAddress_Type(OctetString):
    """Custom type lexipxTrapNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LexipxTrapNodeAddress_Type.__name__ = "OctetString"
_LexipxTrapNodeAddress_Object = MibTableColumn
lexipxTrapNodeAddress = _LexipxTrapNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 12, 1, 4),
    _LexipxTrapNodeAddress_Type()
)
lexipxTrapNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxTrapNodeAddress.setStatus("mandatory")


class _LexipxTrapType_Type(Integer32):
    """Custom type lexipxTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("individual", 2),
          ("multiplexed", 1))
    )


_LexipxTrapType_Type.__name__ = "Integer32"
_LexipxTrapType_Object = MibScalar
lexipxTrapType = _LexipxTrapType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 13),
    _LexipxTrapType_Type()
)
lexipxTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxTrapType.setStatus("mandatory")


class _LexipxGSQ_Type(Integer32):
    """Custom type lexipxGSQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_LexipxGSQ_Type.__name__ = "Integer32"
_LexipxGSQ_Object = MibScalar
lexipxGSQ = _LexipxGSQ_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 3, 14),
    _LexipxGSQ_Type()
)
lexipxGSQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexipxGSQ.setStatus("mandatory")
_Lextalk_ObjectIdentity = ObjectIdentity
lextalk = _Lextalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 4)
)


class _LextalkActivated_Type(Integer32):
    """Custom type lextalkActivated based on Integer32"""
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


_LextalkActivated_Type.__name__ = "Integer32"
_LextalkActivated_Object = MibScalar
lextalkActivated = _LextalkActivated_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 4, 1),
    _LextalkActivated_Type()
)
lextalkActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextalkActivated.setStatus("mandatory")


class _LextalkAddress_Type(DisplayString):
    """Custom type lextalkAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_LextalkAddress_Type.__name__ = "DisplayString"
_LextalkAddress_Object = MibScalar
lextalkAddress = _LextalkAddress_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 4, 2),
    _LextalkAddress_Type()
)
lextalkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextalkAddress.setStatus("mandatory")


class _LextalkName_Type(DisplayString):
    """Custom type lextalkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LextalkName_Type.__name__ = "DisplayString"
_LextalkName_Object = MibScalar
lextalkName = _LextalkName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 4, 3),
    _LextalkName_Type()
)
lextalkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextalkName.setStatus("mandatory")


class _LextalkZone_Type(DisplayString):
    """Custom type lextalkZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LextalkZone_Type.__name__ = "DisplayString"
_LextalkZone_Object = MibScalar
lextalkZone = _LextalkZone_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 4, 4),
    _LextalkZone_Type()
)
lextalkZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextalkZone.setStatus("mandatory")


class _LextalkType_Type(DisplayString):
    """Custom type lextalkType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LextalkType_Type.__name__ = "DisplayString"
_LextalkType_Object = MibScalar
lextalkType = _LextalkType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 4, 5),
    _LextalkType_Type()
)
lextalkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextalkType.setStatus("mandatory")
_Lextcp_ObjectIdentity = ObjectIdentity
lextcp = _Lextcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 5)
)


class _LextcpActivated_Type(Integer32):
    """Custom type lextcpActivated based on Integer32"""
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


_LextcpActivated_Type.__name__ = "Integer32"
_LextcpActivated_Object = MibScalar
lextcpActivated = _LextcpActivated_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 1),
    _LextcpActivated_Type()
)
lextcpActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextcpActivated.setStatus("mandatory")


class _LextcpBootpEnable_Type(Integer32):
    """Custom type lextcpBootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LextcpBootpEnable_Type.__name__ = "Integer32"
_LextcpBootpEnable_Object = MibScalar
lextcpBootpEnable = _LextcpBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 2),
    _LextcpBootpEnable_Type()
)
lextcpBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextcpBootpEnable.setStatus("mandatory")
_LextcpAddressServ_Type = IpAddress
_LextcpAddressServ_Object = MibScalar
lextcpAddressServ = _LextcpAddressServ_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 3),
    _LextcpAddressServ_Type()
)
lextcpAddressServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextcpAddressServ.setStatus("mandatory")
_LextcpNumNPAPservers_Type = Integer32
_LextcpNumNPAPservers_Object = MibScalar
lextcpNumNPAPservers = _LextcpNumNPAPservers_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 4),
    _LextcpNumNPAPservers_Type()
)
lextcpNumNPAPservers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextcpNumNPAPservers.setStatus("mandatory")
_LextcpNPAPserversTable_Object = MibTable
lextcpNPAPserversTable = _LextcpNPAPserversTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 5)
)
if mibBuilder.loadTexts:
    lextcpNPAPserversTable.setStatus("mandatory")
_LextcpNPAPserversEntry_Object = MibTableRow
lextcpNPAPserversEntry = _LextcpNPAPserversEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 5, 1)
)
lextcpNPAPserversEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lextcpNPAPserverIndex"),
)
if mibBuilder.loadTexts:
    lextcpNPAPserversEntry.setStatus("mandatory")
_LextcpNPAPserverIndex_Type = Integer32
_LextcpNPAPserverIndex_Object = MibTableColumn
lextcpNPAPserverIndex = _LextcpNPAPserverIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 5, 1, 1),
    _LextcpNPAPserverIndex_Type()
)
lextcpNPAPserverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextcpNPAPserverIndex.setStatus("mandatory")
_LextcpNPAPserverAddress_Type = IpAddress
_LextcpNPAPserverAddress_Object = MibTableColumn
lextcpNPAPserverAddress = _LextcpNPAPserverAddress_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 5, 1, 2),
    _LextcpNPAPserverAddress_Type()
)
lextcpNPAPserverAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextcpNPAPserverAddress.setStatus("mandatory")
_Lexhttp_ObjectIdentity = ObjectIdentity
lexhttp = _Lexhttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6)
)


class _LexhttpEnable_Type(Integer32):
    """Custom type lexhttpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LexhttpEnable_Type.__name__ = "Integer32"
_LexhttpEnable_Object = MibScalar
lexhttpEnable = _LexhttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 1),
    _LexhttpEnable_Type()
)
lexhttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpEnable.setStatus("mandatory")


class _LexhttpNumLinks_Type(Integer32):
    """Custom type lexhttpNumLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexhttpNumLinks_Type.__name__ = "Integer32"
_LexhttpNumLinks_Object = MibScalar
lexhttpNumLinks = _LexhttpNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 2),
    _LexhttpNumLinks_Type()
)
lexhttpNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhttpNumLinks.setStatus("mandatory")


class _LexhttpBytesRemaining_Type(Integer32):
    """Custom type lexhttpBytesRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexhttpBytesRemaining_Type.__name__ = "Integer32"
_LexhttpBytesRemaining_Object = MibScalar
lexhttpBytesRemaining = _LexhttpBytesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 3),
    _LexhttpBytesRemaining_Type()
)
lexhttpBytesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhttpBytesRemaining.setStatus("mandatory")


class _LexhttpResetLinks_Type(Integer32):
    """Custom type lexhttpResetLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_LexhttpResetLinks_Type.__name__ = "Integer32"
_LexhttpResetLinks_Object = MibScalar
lexhttpResetLinks = _LexhttpResetLinks_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 4),
    _LexhttpResetLinks_Type()
)
lexhttpResetLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpResetLinks.setStatus("mandatory")
_LexhttpLinkTable_Object = MibTable
lexhttpLinkTable = _LexhttpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    lexhttpLinkTable.setStatus("mandatory")
_LexhttpLinkTableEntry_Object = MibTableRow
lexhttpLinkTableEntry = _LexhttpLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5, 1)
)
lexhttpLinkTableEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexhttpLinkTableIndex"),
)
if mibBuilder.loadTexts:
    lexhttpLinkTableEntry.setStatus("mandatory")


class _LexhttpLinkTableIndex_Type(Integer32):
    """Custom type lexhttpLinkTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexhttpLinkTableIndex_Type.__name__ = "Integer32"
_LexhttpLinkTableIndex_Object = MibTableColumn
lexhttpLinkTableIndex = _LexhttpLinkTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5, 1, 1),
    _LexhttpLinkTableIndex_Type()
)
lexhttpLinkTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhttpLinkTableIndex.setStatus("mandatory")


class _LexhttpLinkTableStatus_Type(Integer32):
    """Custom type lexhttpLinkTableStatus based on Integer32"""
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
        *(("customOn", 2),
          ("defaultOff", 4),
          ("defaultOn", 5),
          ("eraseCustom", 6),
          ("linkOff", 1),
          ("useDefault", 3))
    )


_LexhttpLinkTableStatus_Type.__name__ = "Integer32"
_LexhttpLinkTableStatus_Object = MibTableColumn
lexhttpLinkTableStatus = _LexhttpLinkTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5, 1, 2),
    _LexhttpLinkTableStatus_Type()
)
lexhttpLinkTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpLinkTableStatus.setStatus("mandatory")


class _LexhttpLinkTableLabel_Type(DisplayString):
    """Custom type lexhttpLinkTableLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LexhttpLinkTableLabel_Type.__name__ = "DisplayString"
_LexhttpLinkTableLabel_Object = MibTableColumn
lexhttpLinkTableLabel = _LexhttpLinkTableLabel_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5, 1, 3),
    _LexhttpLinkTableLabel_Type()
)
lexhttpLinkTableLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpLinkTableLabel.setStatus("mandatory")


class _LexhttpLinkTableURL_Type(DisplayString):
    """Custom type lexhttpLinkTableURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LexhttpLinkTableURL_Type.__name__ = "DisplayString"
_LexhttpLinkTableURL_Object = MibTableColumn
lexhttpLinkTableURL = _LexhttpLinkTableURL_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 5, 1, 4),
    _LexhttpLinkTableURL_Type()
)
lexhttpLinkTableURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpLinkTableURL.setStatus("mandatory")


class _LexhttpConfigEnable_Type(Integer32):
    """Custom type lexhttpConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LexhttpConfigEnable_Type.__name__ = "Integer32"
_LexhttpConfigEnable_Object = MibScalar
lexhttpConfigEnable = _LexhttpConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 6, 6),
    _LexhttpConfigEnable_Type()
)
lexhttpConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhttpConfigEnable.setStatus("mandatory")
_Lexdhcp_ObjectIdentity = ObjectIdentity
lexdhcp = _Lexdhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7)
)


class _LexdhcpDhcpEnable_Type(Integer32):
    """Custom type lexdhcpDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LexdhcpDhcpEnable_Type.__name__ = "Integer32"
_LexdhcpDhcpEnable_Object = MibScalar
lexdhcpDhcpEnable = _LexdhcpDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 1),
    _LexdhcpDhcpEnable_Type()
)
lexdhcpDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexdhcpDhcpEnable.setStatus("mandatory")


class _LexdhcpRarpEnable_Type(Integer32):
    """Custom type lexdhcpRarpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LexdhcpRarpEnable_Type.__name__ = "Integer32"
_LexdhcpRarpEnable_Object = MibScalar
lexdhcpRarpEnable = _LexdhcpRarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 2),
    _LexdhcpRarpEnable_Type()
)
lexdhcpRarpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexdhcpRarpEnable.setStatus("mandatory")


class _LexdhcpAddressSource_Type(Integer32):
    """Custom type lexdhcpAddressSource based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 2),
          ("manual", 1),
          ("rarp", 4))
    )


_LexdhcpAddressSource_Type.__name__ = "Integer32"
_LexdhcpAddressSource_Object = MibScalar
lexdhcpAddressSource = _LexdhcpAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 3),
    _LexdhcpAddressSource_Type()
)
lexdhcpAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexdhcpAddressSource.setStatus("mandatory")


class _LexdhcpWinsStatus_Type(Integer32):
    """Custom type lexdhcpWinsStatus based on Integer32"""
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
        *(("pending", 3),
          ("registered", 2),
          ("rejected", 4),
          ("unregistered", 1))
    )


_LexdhcpWinsStatus_Type.__name__ = "Integer32"
_LexdhcpWinsStatus_Object = MibScalar
lexdhcpWinsStatus = _LexdhcpWinsStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 4),
    _LexdhcpWinsStatus_Type()
)
lexdhcpWinsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexdhcpWinsStatus.setStatus("mandatory")
_LexdhcpWinsServer_Type = IpAddress
_LexdhcpWinsServer_Object = MibScalar
lexdhcpWinsServer = _LexdhcpWinsServer_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 5),
    _LexdhcpWinsServer_Type()
)
lexdhcpWinsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexdhcpWinsServer.setStatus("mandatory")


class _LexdhcpHostname_Type(DisplayString):
    """Custom type lexdhcpHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LexdhcpHostname_Type.__name__ = "DisplayString"
_LexdhcpHostname_Object = MibScalar
lexdhcpHostname = _LexdhcpHostname_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 6),
    _LexdhcpHostname_Type()
)
lexdhcpHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexdhcpHostname.setStatus("mandatory")
_LexdhcpLeaseLength_Type = Integer32
_LexdhcpLeaseLength_Object = MibScalar
lexdhcpLeaseLength = _LexdhcpLeaseLength_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 7),
    _LexdhcpLeaseLength_Type()
)
lexdhcpLeaseLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexdhcpLeaseLength.setStatus("mandatory")
_LexdhcpTimetoExpire_Type = Integer32
_LexdhcpTimetoExpire_Object = MibScalar
lexdhcpTimetoExpire = _LexdhcpTimetoExpire_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 8),
    _LexdhcpTimetoExpire_Type()
)
lexdhcpTimetoExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexdhcpTimetoExpire.setStatus("mandatory")
_LexdhcpDNSServer_Type = IpAddress
_LexdhcpDNSServer_Object = MibScalar
lexdhcpDNSServer = _LexdhcpDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 5, 7, 9),
    _LexdhcpDNSServer_Type()
)
lexdhcpDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexdhcpDNSServer.setStatus("mandatory")
_Lexhdwr_ObjectIdentity = ObjectIdentity
lexhdwr = _Lexhdwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 6)
)


class _LexhdwrNumPorts_Type(Integer32):
    """Custom type lexhdwrNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LexhdwrNumPorts_Type.__name__ = "Integer32"
_LexhdwrNumPorts_Object = MibScalar
lexhdwrNumPorts = _LexhdwrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 1),
    _LexhdwrNumPorts_Type()
)
lexhdwrNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhdwrNumPorts.setStatus("mandatory")
_LexhdwrPortTable_Object = MibTable
lexhdwrPortTable = _LexhdwrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lexhdwrPortTable.setStatus("mandatory")
_LexhdwrPortTableEntry_Object = MibTableRow
lexhdwrPortTableEntry = _LexhdwrPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1)
)
lexhdwrPortTableEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lexhdwrPortTableIndex"),
)
if mibBuilder.loadTexts:
    lexhdwrPortTableEntry.setStatus("mandatory")
_LexhdwrPortTableIndex_Type = Integer32
_LexhdwrPortTableIndex_Object = MibTableColumn
lexhdwrPortTableIndex = _LexhdwrPortTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 1),
    _LexhdwrPortTableIndex_Type()
)
lexhdwrPortTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhdwrPortTableIndex.setStatus("mandatory")


class _LexhdwrPortTableType_Type(Integer32):
    """Custom type lexhdwrPortTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("parallel", 2),
          ("serial", 3))
    )


_LexhdwrPortTableType_Type.__name__ = "Integer32"
_LexhdwrPortTableType_Object = MibTableColumn
lexhdwrPortTableType = _LexhdwrPortTableType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 2),
    _LexhdwrPortTableType_Type()
)
lexhdwrPortTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhdwrPortTableType.setStatus("mandatory")
_LexhdwrPortTableParm1_Type = Integer32
_LexhdwrPortTableParm1_Object = MibTableColumn
lexhdwrPortTableParm1 = _LexhdwrPortTableParm1_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 3),
    _LexhdwrPortTableParm1_Type()
)
lexhdwrPortTableParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm1.setStatus("mandatory")
_LexhdwrPortTableParm2_Type = Integer32
_LexhdwrPortTableParm2_Object = MibTableColumn
lexhdwrPortTableParm2 = _LexhdwrPortTableParm2_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 4),
    _LexhdwrPortTableParm2_Type()
)
lexhdwrPortTableParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm2.setStatus("mandatory")
_LexhdwrPortTableParm3_Type = Integer32
_LexhdwrPortTableParm3_Object = MibTableColumn
lexhdwrPortTableParm3 = _LexhdwrPortTableParm3_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 5),
    _LexhdwrPortTableParm3_Type()
)
lexhdwrPortTableParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm3.setStatus("mandatory")
_LexhdwrPortTableParm4_Type = Integer32
_LexhdwrPortTableParm4_Object = MibTableColumn
lexhdwrPortTableParm4 = _LexhdwrPortTableParm4_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 6),
    _LexhdwrPortTableParm4_Type()
)
lexhdwrPortTableParm4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm4.setStatus("mandatory")
_LexhdwrPortTableParm5_Type = Integer32
_LexhdwrPortTableParm5_Object = MibTableColumn
lexhdwrPortTableParm5 = _LexhdwrPortTableParm5_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 7),
    _LexhdwrPortTableParm5_Type()
)
lexhdwrPortTableParm5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm5.setStatus("mandatory")
_LexhdwrPortTableParm6_Type = Integer32
_LexhdwrPortTableParm6_Object = MibTableColumn
lexhdwrPortTableParm6 = _LexhdwrPortTableParm6_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 8),
    _LexhdwrPortTableParm6_Type()
)
lexhdwrPortTableParm6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm6.setStatus("mandatory")


class _LexhdwrPortTableParm7_Type(Integer32):
    """Custom type lexhdwrPortTableParm7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 1),
          ("on", 2))
    )


_LexhdwrPortTableParm7_Type.__name__ = "Integer32"
_LexhdwrPortTableParm7_Object = MibTableColumn
lexhdwrPortTableParm7 = _LexhdwrPortTableParm7_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 9),
    _LexhdwrPortTableParm7_Type()
)
lexhdwrPortTableParm7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm7.setStatus("mandatory")


class _LexhdwrPortTableParm8_Type(Integer32):
    """Custom type lexhdwrPortTableParm8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("npapActive", 2),
          ("npapInactive", 1))
    )


_LexhdwrPortTableParm8_Type.__name__ = "Integer32"
_LexhdwrPortTableParm8_Object = MibTableColumn
lexhdwrPortTableParm8 = _LexhdwrPortTableParm8_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 10),
    _LexhdwrPortTableParm8_Type()
)
lexhdwrPortTableParm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm8.setStatus("mandatory")


class _LexhdwrPortTableParm9_Type(Integer32):
    """Custom type lexhdwrPortTableParm9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("printer", 1))
    )


_LexhdwrPortTableParm9_Type.__name__ = "Integer32"
_LexhdwrPortTableParm9_Object = MibTableColumn
lexhdwrPortTableParm9 = _LexhdwrPortTableParm9_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 6, 2, 1, 11),
    _LexhdwrPortTableParm9_Type()
)
lexhdwrPortTableParm9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lexhdwrPortTableParm9.setStatus("mandatory")
_Lexmac_ObjectIdentity = ObjectIdentity
lexmac = _Lexmac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 7)
)


class _LexmacType_Type(DisplayString):
    """Custom type lexmacType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LexmacType_Type.__name__ = "DisplayString"
_LexmacType_Object = MibScalar
lexmacType = _LexmacType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 7, 1),
    _LexmacType_Type()
)
lexmacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexmacType.setStatus("mandatory")
_LexmacSpeed_Type = Gauge32
_LexmacSpeed_Object = MibScalar
lexmacSpeed = _LexmacSpeed_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 7, 2),
    _LexmacSpeed_Type()
)
lexmacSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexmacSpeed.setStatus("mandatory")


class _LexmacConnType_Type(Integer32):
    """Custom type lexmacConnType based on Integer32"""
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
        *(("aui", 1),
          ("bnc", 2),
          ("stp", 3),
          ("utp", 4))
    )


_LexmacConnType_Type.__name__ = "Integer32"
_LexmacConnType_Object = MibScalar
lexmacConnType = _LexmacConnType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 7, 3),
    _LexmacConnType_Type()
)
lexmacConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexmacConnType.setStatus("mandatory")
_LexmacUAA_Type = PhysAddress
_LexmacUAA_Object = MibScalar
lexmacUAA = _LexmacUAA_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 7, 4),
    _LexmacUAA_Type()
)
lexmacUAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexmacUAA.setStatus("mandatory")
_LexmacLAA_Type = PhysAddress
_LexmacLAA_Object = MibScalar
lexmacLAA = _LexmacLAA_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 7, 5),
    _LexmacLAA_Type()
)
lexmacLAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lexmacLAA.setStatus("mandatory")
_Lextrap_ObjectIdentity = ObjectIdentity
lextrap = _Lextrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 8)
)
_LextrapDestNum_Type = Integer32
_LextrapDestNum_Object = MibScalar
lextrapDestNum = _LextrapDestNum_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 1),
    _LextrapDestNum_Type()
)
lextrapDestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextrapDestNum.setStatus("mandatory")
_LextrapDestTable_Object = MibTable
lextrapDestTable = _LextrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 2)
)
if mibBuilder.loadTexts:
    lextrapDestTable.setStatus("mandatory")
_LextrapDestEntry_Object = MibTableRow
lextrapDestEntry = _LextrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 2, 1)
)
lextrapDestEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "lextrapDestIndex"),
)
if mibBuilder.loadTexts:
    lextrapDestEntry.setStatus("mandatory")
_LextrapDestIndex_Type = Integer32
_LextrapDestIndex_Object = MibTableColumn
lextrapDestIndex = _LextrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 2, 1, 1),
    _LextrapDestIndex_Type()
)
lextrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lextrapDestIndex.setStatus("mandatory")
_LextrapDestIPAddr_Type = IpAddress
_LextrapDestIPAddr_Object = MibTableColumn
lextrapDestIPAddr = _LextrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 2, 1, 2),
    _LextrapDestIPAddr_Type()
)
lextrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextrapDestIPAddr.setStatus("mandatory")


class _LextrapDestMask_Type(Integer32):
    """Custom type lextrapDestMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LextrapDestMask_Type.__name__ = "Integer32"
_LextrapDestMask_Object = MibTableColumn
lextrapDestMask = _LextrapDestMask_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 2, 1, 3),
    _LextrapDestMask_Type()
)
lextrapDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextrapDestMask.setStatus("mandatory")


class _LextrapIPTrapType_Type(Integer32):
    """Custom type lextrapIPTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("individual", 2),
          ("multiplexed", 1))
    )


_LextrapIPTrapType_Type.__name__ = "Integer32"
_LextrapIPTrapType_Object = MibScalar
lextrapIPTrapType = _LextrapIPTrapType_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 8, 3),
    _LextrapIPTrapType_Type()
)
lextrapIPTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lextrapIPTrapType.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 1, 9)
)


class _TimeReset_Type(Integer32):
    """Custom type timeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_TimeReset_Type.__name__ = "Integer32"
_TimeReset_Object = MibScalar
timeReset = _TimeReset_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 1),
    _TimeReset_Type()
)
timeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeReset.setStatus("mandatory")


class _TimeSource_Type(Integer32):
    """Custom type timeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netware", 3),
          ("none", 1),
          ("ntp", 2))
    )


_TimeSource_Type.__name__ = "Integer32"
_TimeSource_Object = MibScalar
timeSource = _TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 2),
    _TimeSource_Type()
)
timeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSource.setStatus("mandatory")


class _TimeUTCOffset_Type(Integer32):
    """Custom type timeUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_TimeUTCOffset_Type.__name__ = "Integer32"
_TimeUTCOffset_Object = MibScalar
timeUTCOffset = _TimeUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 3),
    _TimeUTCOffset_Type()
)
timeUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeUTCOffset.setStatus("mandatory")


class _TimeDSTEnable_Type(Integer32):
    """Custom type timeDSTEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TimeDSTEnable_Type.__name__ = "Integer32"
_TimeDSTEnable_Object = MibScalar
timeDSTEnable = _TimeDSTEnable_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 4),
    _TimeDSTEnable_Type()
)
timeDSTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDSTEnable.setStatus("mandatory")


class _TimeDSTStartDate_Type(OctetString):
    """Custom type timeDSTStartDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_TimeDSTStartDate_Type.__name__ = "OctetString"
_TimeDSTStartDate_Object = MibScalar
timeDSTStartDate = _TimeDSTStartDate_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 5),
    _TimeDSTStartDate_Type()
)
timeDSTStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDSTStartDate.setStatus("mandatory")


class _TimeDSTEndDate_Type(OctetString):
    """Custom type timeDSTEndDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_TimeDSTEndDate_Type.__name__ = "OctetString"
_TimeDSTEndDate_Object = MibScalar
timeDSTEndDate = _TimeDSTEndDate_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 6),
    _TimeDSTEndDate_Type()
)
timeDSTEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDSTEndDate.setStatus("mandatory")


class _TimeDSTOffset_Type(Integer32):
    """Custom type timeDSTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_TimeDSTOffset_Type.__name__ = "Integer32"
_TimeDSTOffset_Object = MibScalar
timeDSTOffset = _TimeDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 7),
    _TimeDSTOffset_Type()
)
timeDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDSTOffset.setStatus("mandatory")
_TimeServerAddress_Type = IpAddress
_TimeServerAddress_Object = MibScalar
timeServerAddress = _TimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 8),
    _TimeServerAddress_Type()
)
timeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerAddress.setStatus("mandatory")


class _TimeServerName_Type(DisplayString):
    """Custom type timeServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TimeServerName_Type.__name__ = "DisplayString"
_TimeServerName_Object = MibScalar
timeServerName = _TimeServerName_Object(
    (1, 3, 6, 1, 4, 1, 641, 1, 9, 9),
    _TimeServerName_Type()
)
timeServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerName.setStatus("mandatory")
_Printer_ObjectIdentity = ObjectIdentity
printer = _Printer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 2)
)
_Prtgen_ObjectIdentity = ObjectIdentity
prtgen = _Prtgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 2, 1)
)
_PrtgenNumber_Type = Integer32
_PrtgenNumber_Object = MibScalar
prtgenNumber = _PrtgenNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 1),
    _PrtgenNumber_Type()
)
prtgenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenNumber.setStatus("mandatory")
_PrtgenInfoTable_Object = MibTable
prtgenInfoTable = _PrtgenInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2)
)
if mibBuilder.loadTexts:
    prtgenInfoTable.setStatus("mandatory")
_PrtgenInfoEntry_Object = MibTableRow
prtgenInfoEntry = _PrtgenInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1)
)
prtgenInfoEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "prtgenPrinterIndex"),
)
if mibBuilder.loadTexts:
    prtgenInfoEntry.setStatus("mandatory")
_PrtgenPrinterIndex_Type = Integer32
_PrtgenPrinterIndex_Object = MibTableColumn
prtgenPrinterIndex = _PrtgenPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 1),
    _PrtgenPrinterIndex_Type()
)
prtgenPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenPrinterIndex.setStatus("mandatory")


class _PrtgenPrinterName_Type(DisplayString):
    """Custom type prtgenPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtgenPrinterName_Type.__name__ = "DisplayString"
_PrtgenPrinterName_Object = MibTableColumn
prtgenPrinterName = _PrtgenPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 2),
    _PrtgenPrinterName_Type()
)
prtgenPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenPrinterName.setStatus("mandatory")


class _PrtgenPeripheralID_Type(DisplayString):
    """Custom type prtgenPeripheralID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtgenPeripheralID_Type.__name__ = "DisplayString"
_PrtgenPeripheralID_Object = MibTableColumn
prtgenPeripheralID = _PrtgenPeripheralID_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 3),
    _PrtgenPeripheralID_Type()
)
prtgenPeripheralID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenPeripheralID.setStatus("mandatory")


class _PrtgenCodeRevision_Type(DisplayString):
    """Custom type prtgenCodeRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtgenCodeRevision_Type.__name__ = "DisplayString"
_PrtgenCodeRevision_Object = MibTableColumn
prtgenCodeRevision = _PrtgenCodeRevision_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 4),
    _PrtgenCodeRevision_Type()
)
prtgenCodeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenCodeRevision.setStatus("mandatory")
_PrtgenResValue_Type = Integer32
_PrtgenResValue_Object = MibTableColumn
prtgenResValue = _PrtgenResValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 5),
    _PrtgenResValue_Type()
)
prtgenResValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenResValue.setStatus("mandatory")


class _PrtgenSerialNo_Type(DisplayString):
    """Custom type prtgenSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtgenSerialNo_Type.__name__ = "DisplayString"
_PrtgenSerialNo_Object = MibTableColumn
prtgenSerialNo = _PrtgenSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 2, 1, 6),
    _PrtgenSerialNo_Type()
)
prtgenSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenSerialNo.setStatus("mandatory")
_PrtgenStatusTable_Object = MibTable
prtgenStatusTable = _PrtgenStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3)
)
if mibBuilder.loadTexts:
    prtgenStatusTable.setStatus("mandatory")
_PrtgenStatusEntry_Object = MibTableRow
prtgenStatusEntry = _PrtgenStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1)
)
prtgenStatusEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "prtgenStatPrinterIndex"),
)
if mibBuilder.loadTexts:
    prtgenStatusEntry.setStatus("mandatory")
_PrtgenStatPrinterIndex_Type = Integer32
_PrtgenStatPrinterIndex_Object = MibTableColumn
prtgenStatPrinterIndex = _PrtgenStatPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 1),
    _PrtgenStatPrinterIndex_Type()
)
prtgenStatPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatPrinterIndex.setStatus("mandatory")
_PrtgenStatusIRC_Type = Integer32
_PrtgenStatusIRC_Object = MibTableColumn
prtgenStatusIRC = _PrtgenStatusIRC_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 2),
    _PrtgenStatusIRC_Type()
)
prtgenStatusIRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusIRC.setStatus("mandatory")


class _PrtgenStatusOutHopFull_Type(Integer32):
    """Custom type prtgenStatusOutHopFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("notFull", 1),
          ("unknown", 3))
    )


_PrtgenStatusOutHopFull_Type.__name__ = "Integer32"
_PrtgenStatusOutHopFull_Object = MibTableColumn
prtgenStatusOutHopFull = _PrtgenStatusOutHopFull_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 3),
    _PrtgenStatusOutHopFull_Type()
)
prtgenStatusOutHopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusOutHopFull.setStatus("mandatory")


class _PrtgenStatusInputEmpty_Type(Integer32):
    """Custom type prtgenStatusInputEmpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("notEmpty", 1),
          ("unknown", 3))
    )


_PrtgenStatusInputEmpty_Type.__name__ = "Integer32"
_PrtgenStatusInputEmpty_Object = MibTableColumn
prtgenStatusInputEmpty = _PrtgenStatusInputEmpty_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 4),
    _PrtgenStatusInputEmpty_Type()
)
prtgenStatusInputEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusInputEmpty.setStatus("mandatory")


class _PrtgenStatusPaperJam_Type(Integer32):
    """Custom type prtgenStatusPaperJam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jamed", 2),
          ("notJammed", 1),
          ("unknown", 3))
    )


_PrtgenStatusPaperJam_Type.__name__ = "Integer32"
_PrtgenStatusPaperJam_Object = MibTableColumn
prtgenStatusPaperJam = _PrtgenStatusPaperJam_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 5),
    _PrtgenStatusPaperJam_Type()
)
prtgenStatusPaperJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusPaperJam.setStatus("mandatory")


class _PrtgenStatusTonerError_Type(Integer32):
    """Custom type prtgenStatusTonerError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTonerError", 1),
          ("tonerError", 2),
          ("unknown", 3))
    )


_PrtgenStatusTonerError_Type.__name__ = "Integer32"
_PrtgenStatusTonerError_Object = MibTableColumn
prtgenStatusTonerError = _PrtgenStatusTonerError_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 6),
    _PrtgenStatusTonerError_Type()
)
prtgenStatusTonerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusTonerError.setStatus("mandatory")


class _PrtgenStatusSrvcReqd_Type(Integer32):
    """Custom type prtgenStatusSrvcReqd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noServiceRequired", 1),
          ("serviceRequired", 2),
          ("unknown", 3))
    )


_PrtgenStatusSrvcReqd_Type.__name__ = "Integer32"
_PrtgenStatusSrvcReqd_Object = MibTableColumn
prtgenStatusSrvcReqd = _PrtgenStatusSrvcReqd_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 7),
    _PrtgenStatusSrvcReqd_Type()
)
prtgenStatusSrvcReqd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusSrvcReqd.setStatus("mandatory")


class _PrtgenStatusDiskError_Type(Integer32):
    """Custom type prtgenStatusDiskError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diskError", 2),
          ("noDiskError", 1),
          ("unknown", 3))
    )


_PrtgenStatusDiskError_Type.__name__ = "Integer32"
_PrtgenStatusDiskError_Object = MibTableColumn
prtgenStatusDiskError = _PrtgenStatusDiskError_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 8),
    _PrtgenStatusDiskError_Type()
)
prtgenStatusDiskError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusDiskError.setStatus("mandatory")


class _PrtgenStatusCoverOpen_Type(Integer32):
    """Custom type prtgenStatusCoverOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coverOpen", 2),
          ("noCoverOpen", 1),
          ("unknown", 3))
    )


_PrtgenStatusCoverOpen_Type.__name__ = "Integer32"
_PrtgenStatusCoverOpen_Object = MibTableColumn
prtgenStatusCoverOpen = _PrtgenStatusCoverOpen_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 9),
    _PrtgenStatusCoverOpen_Type()
)
prtgenStatusCoverOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusCoverOpen.setStatus("mandatory")


class _PrtgenStatusPageComplex_Type(Integer32):
    """Custom type prtgenStatusPageComplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complexPage", 2),
          ("noComplexPage", 1),
          ("unknown", 3))
    )


_PrtgenStatusPageComplex_Type.__name__ = "Integer32"
_PrtgenStatusPageComplex_Object = MibTableColumn
prtgenStatusPageComplex = _PrtgenStatusPageComplex_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 10),
    _PrtgenStatusPageComplex_Type()
)
prtgenStatusPageComplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusPageComplex.setStatus("mandatory")


class _PrtgenStatusLineStatus_Type(Integer32):
    """Custom type prtgenStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unknown", 3))
    )


_PrtgenStatusLineStatus_Type.__name__ = "Integer32"
_PrtgenStatusLineStatus_Object = MibTableColumn
prtgenStatusLineStatus = _PrtgenStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 11),
    _PrtgenStatusLineStatus_Type()
)
prtgenStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusLineStatus.setStatus("mandatory")


class _PrtgenStatusBusy_Type(Integer32):
    """Custom type prtgenStatusBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("notBusy", 1),
          ("unknown", 3))
    )


_PrtgenStatusBusy_Type.__name__ = "Integer32"
_PrtgenStatusBusy_Object = MibTableColumn
prtgenStatusBusy = _PrtgenStatusBusy_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 12),
    _PrtgenStatusBusy_Type()
)
prtgenStatusBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusBusy.setStatus("mandatory")


class _PrtgenStatusWaiting_Type(Integer32):
    """Custom type prtgenStatusWaiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notWaiting", 1),
          ("unknown", 3),
          ("waiting", 2))
    )


_PrtgenStatusWaiting_Type.__name__ = "Integer32"
_PrtgenStatusWaiting_Object = MibTableColumn
prtgenStatusWaiting = _PrtgenStatusWaiting_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 13),
    _PrtgenStatusWaiting_Type()
)
prtgenStatusWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusWaiting.setStatus("mandatory")


class _PrtgenStatusWarming_Type(Integer32):
    """Custom type prtgenStatusWarming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notWarming", 1),
          ("unknown", 3),
          ("warming", 2))
    )


_PrtgenStatusWarming_Type.__name__ = "Integer32"
_PrtgenStatusWarming_Object = MibTableColumn
prtgenStatusWarming = _PrtgenStatusWarming_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 14),
    _PrtgenStatusWarming_Type()
)
prtgenStatusWarming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusWarming.setStatus("mandatory")


class _PrtgenStatusPrinting_Type(Integer32):
    """Custom type prtgenStatusPrinting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPrinting", 1),
          ("printing", 2),
          ("unknown", 3))
    )


_PrtgenStatusPrinting_Type.__name__ = "Integer32"
_PrtgenStatusPrinting_Object = MibTableColumn
prtgenStatusPrinting = _PrtgenStatusPrinting_Object(
    (1, 3, 6, 1, 4, 1, 641, 2, 1, 3, 1, 15),
    _PrtgenStatusPrinting_Type()
)
prtgenStatusPrinting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgenStatusPrinting.setStatus("mandatory")
_Attachment_ObjectIdentity = ObjectIdentity
attachment = _Attachment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 3)
)
_Fax_ObjectIdentity = ObjectIdentity
fax = _Fax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 3, 1)
)
_FaxNumber_Type = Integer32
_FaxNumber_Object = MibScalar
faxNumber = _FaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 1),
    _FaxNumber_Type()
)
faxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxNumber.setStatus("mandatory")
_FaxTable_Object = MibTable
faxTable = _FaxTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2)
)
if mibBuilder.loadTexts:
    faxTable.setStatus("mandatory")
_FaxEntry_Object = MibTableRow
faxEntry = _FaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1)
)
faxEntry.setIndexNames(
    (0, "LEXMARK-PVT-MIB", "faxIndex"),
)
if mibBuilder.loadTexts:
    faxEntry.setStatus("mandatory")
_FaxIndex_Type = Integer32
_FaxIndex_Object = MibTableColumn
faxIndex = _FaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 1),
    _FaxIndex_Type()
)
faxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxIndex.setStatus("mandatory")


class _FaxPort_Type(Integer32):
    """Custom type faxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(145,
              146,
              147,
              148,
              149)
        )
    )
    namedValues = NamedValues(
        *(("serial1", 145),
          ("serial2", 146),
          ("serial3", 147),
          ("serial4", 148),
          ("serial5", 149))
    )


_FaxPort_Type.__name__ = "Integer32"
_FaxPort_Object = MibTableColumn
faxPort = _FaxPort_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 2),
    _FaxPort_Type()
)
faxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxPort.setStatus("mandatory")


class _FaxAdapterCapabilities_Type(Integer32):
    """Custom type faxAdapterCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FaxAdapterCapabilities_Type.__name__ = "Integer32"
_FaxAdapterCapabilities_Object = MibTableColumn
faxAdapterCapabilities = _FaxAdapterCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 3),
    _FaxAdapterCapabilities_Type()
)
faxAdapterCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxAdapterCapabilities.setStatus("mandatory")


class _FaxModemCapabilities_Type(Integer32):
    """Custom type faxModemCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FaxModemCapabilities_Type.__name__ = "Integer32"
_FaxModemCapabilities_Object = MibTableColumn
faxModemCapabilities = _FaxModemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 4),
    _FaxModemCapabilities_Type()
)
faxModemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxModemCapabilities.setStatus("mandatory")


class _FaxSelectedCapabilities_Type(Integer32):
    """Custom type faxSelectedCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FaxSelectedCapabilities_Type.__name__ = "Integer32"
_FaxSelectedCapabilities_Object = MibTableColumn
faxSelectedCapabilities = _FaxSelectedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 5),
    _FaxSelectedCapabilities_Type()
)
faxSelectedCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxSelectedCapabilities.setStatus("mandatory")


class _FaxActiveCapabilities_Type(Integer32):
    """Custom type faxActiveCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FaxActiveCapabilities_Type.__name__ = "Integer32"
_FaxActiveCapabilities_Object = MibTableColumn
faxActiveCapabilities = _FaxActiveCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 6),
    _FaxActiveCapabilities_Type()
)
faxActiveCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxActiveCapabilities.setStatus("mandatory")


class _FaxIDString_Type(DisplayString):
    """Custom type faxIDString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FaxIDString_Type.__name__ = "DisplayString"
_FaxIDString_Object = MibTableColumn
faxIDString = _FaxIDString_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 7),
    _FaxIDString_Type()
)
faxIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxIDString.setStatus("mandatory")


class _FaxInitString_Type(DisplayString):
    """Custom type faxInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FaxInitString_Type.__name__ = "DisplayString"
_FaxInitString_Object = MibTableColumn
faxInitString = _FaxInitString_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 8),
    _FaxInitString_Type()
)
faxInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxInitString.setStatus("mandatory")


class _FaxNumberRings_Type(Integer32):
    """Custom type faxNumberRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FaxNumberRings_Type.__name__ = "Integer32"
_FaxNumberRings_Object = MibTableColumn
faxNumberRings = _FaxNumberRings_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 9),
    _FaxNumberRings_Type()
)
faxNumberRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxNumberRings.setStatus("mandatory")


class _FaxScaling_Type(Integer32):
    """Custom type faxScaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cropToFit", 2),
          ("scaleToFit", 1))
    )


_FaxScaling_Type.__name__ = "Integer32"
_FaxScaling_Object = MibTableColumn
faxScaling = _FaxScaling_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 10),
    _FaxScaling_Type()
)
faxScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxScaling.setStatus("mandatory")


class _FaxBinaryEncoding_Type(Integer32):
    """Custom type faxBinaryEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii85", 2),
          ("taggedBinary", 1))
    )


_FaxBinaryEncoding_Type.__name__ = "Integer32"
_FaxBinaryEncoding_Object = MibTableColumn
faxBinaryEncoding = _FaxBinaryEncoding_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 11),
    _FaxBinaryEncoding_Type()
)
faxBinaryEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxBinaryEncoding.setStatus("mandatory")


class _FaxPrinterPort_Type(Integer32):
    """Custom type faxPrinterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              130,
              255)
        )
    )
    namedValues = NamedValues(
        *(("firstAvail", 255),
          ("parallel1", 129),
          ("parallel2", 130))
    )


_FaxPrinterPort_Type.__name__ = "Integer32"
_FaxPrinterPort_Object = MibTableColumn
faxPrinterPort = _FaxPrinterPort_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 13),
    _FaxPrinterPort_Type()
)
faxPrinterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxPrinterPort.setStatus("mandatory")
_FaxInputTray_Type = Integer32
_FaxInputTray_Object = MibTableColumn
faxInputTray = _FaxInputTray_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 14),
    _FaxInputTray_Type()
)
faxInputTray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxInputTray.setStatus("mandatory")
_FaxOutputBin_Type = Integer32
_FaxOutputBin_Object = MibTableColumn
faxOutputBin = _FaxOutputBin_Object(
    (1, 3, 6, 1, 4, 1, 641, 3, 1, 2, 1, 15),
    _FaxOutputBin_Type()
)
faxOutputBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxOutputBin.setStatus("mandatory")

# Managed Objects groups


# Notification objects

irCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 0)
)
irCleared.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irCleared.setStatus(
        ""
    )

irCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 1)
)
irCondition.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irCondition.setStatus(
        ""
    )

irOutputFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 2)
)
irOutputFull.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irOutputFull.setStatus(
        ""
    )

irLoadPaper = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 3)
)
irLoadPaper.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irLoadPaper.setStatus(
        ""
    )

irPaperJam = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 4)
)
irPaperJam.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irPaperJam.setStatus(
        ""
    )

irTonerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 5)
)
irTonerLow.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irTonerLow.setStatus(
        ""
    )

irServiceReq = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 6)
)
irServiceReq.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irServiceReq.setStatus(
        ""
    )

irDiskErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 7)
)
irDiskErr.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irDiskErr.setStatus(
        ""
    )

irCoverOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 8)
)
irCoverOpen.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irCoverOpen.setStatus(
        ""
    )

irPageComplexity = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 9)
)
irPageComplexity.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irPageComplexity.setStatus(
        ""
    )

irOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 10)
)
irOffline.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irOffline.setStatus(
        ""
    )

irClearedTypeII = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 1, 0, 11)
)
irClearedTypeII.setObjects(
    ("LEXMARK-PVT-MIB", "prtgenStatusIRC")
)
if mibBuilder.loadTexts:
    irClearedTypeII.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEXMARK-PVT-MIB",
    **{"lexmark": lexmark,
       "adapter": adapter,
       "irCleared": irCleared,
       "irCondition": irCondition,
       "irOutputFull": irOutputFull,
       "irLoadPaper": irLoadPaper,
       "irPaperJam": irPaperJam,
       "irTonerLow": irTonerLow,
       "irServiceReq": irServiceReq,
       "irDiskErr": irDiskErr,
       "irCoverOpen": irCoverOpen,
       "irPageComplexity": irPageComplexity,
       "irOffline": irOffline,
       "irClearedTypeII": irClearedTypeII,
       "opsys": opsys,
       "opsysCodeRev": opsysCodeRev,
       "opsysJobTimeout": opsysJobTimeout,
       "opsysCurrentJob": opsysCurrentJob,
       "opsysRAMSize": opsysRAMSize,
       "opsysNVRAMSize": opsysNVRAMSize,
       "opsysROMSize": opsysROMSize,
       "opsysROMType": opsysROMType,
       "opsysProtocols": opsysProtocols,
       "opsysTimeToReset": opsysTimeToReset,
       "opsysCardPartNo": opsysCardPartNo,
       "opsysCardEC": opsysCardEC,
       "opsysCurrentJobTable": opsysCurrentJobTable,
       "opsysCurrentJobEntry": opsysCurrentJobEntry,
       "opsysCurrentJobEntryIndex": opsysCurrentJobEntryIndex,
       "opsysCurrentJobString": opsysCurrentJobString,
       "opsysDeviceType": opsysDeviceType,
       "opsysAdapterName": opsysAdapterName,
       "opsysAdapterCapabilities": opsysAdapterCapabilities,
       "lexlink": lexlink,
       "lexlinkActivated": lexlinkActivated,
       "lexlinkNickname": lexlinkNickname,
       "lexipx": lexipx,
       "lexipxActivated": lexipxActivated,
       "lexipxLoginName": lexipxLoginName,
       "lexipxNetNumber": lexipxNetNumber,
       "lexipxSAPMode": lexipxSAPMode,
       "lexipxServerMode": lexipxServerMode,
       "lexipxNumPorts": lexipxNumPorts,
       "lexipxPortInfoTable": lexipxPortInfoTable,
       "lexipxPortInfoEntry": lexipxPortInfoEntry,
       "lexipxPortInfoIndex": lexipxPortInfoIndex,
       "lexipxPortInfoPollIntvl": lexipxPortInfoPollIntvl,
       "lexipxPortInfoEnable": lexipxPortInfoEnable,
       "lexipxPortInfoBannerPage": lexipxPortInfoBannerPage,
       "lexipxNumPrefServers": lexipxNumPrefServers,
       "lexipxPrefSrvrTable": lexipxPrefSrvrTable,
       "lexipxPrefSrvrEntry": lexipxPrefSrvrEntry,
       "lexipxPrefSrvrIndex": lexipxPrefSrvrIndex,
       "lexipxPrefSrvrName": lexipxPrefSrvrName,
       "lexipxConnSrvrTable": lexipxConnSrvrTable,
       "lexipxConnSrvrEntry": lexipxConnSrvrEntry,
       "lexipxConnSrvrIndex": lexipxConnSrvrIndex,
       "lexipxConnSrvrName": lexipxConnSrvrName,
       "lexipxConnSrvrNet": lexipxConnSrvrNet,
       "lexipxConnSrvrNode": lexipxConnSrvrNode,
       "lexipxConnSrvrConnNum": lexipxConnSrvrConnNum,
       "lexipxConnSrvrConnId": lexipxConnSrvrConnId,
       "lexipxConnSrvrPSConnID": lexipxConnSrvrPSConnID,
       "lexipxFrameType": lexipxFrameType,
       "lexipxTrapTable": lexipxTrapTable,
       "lexipxTrapEntry": lexipxTrapEntry,
       "lexipxTrapIndex": lexipxTrapIndex,
       "lexipxTrapMask": lexipxTrapMask,
       "lexipxTrapNetworkAddress": lexipxTrapNetworkAddress,
       "lexipxTrapNodeAddress": lexipxTrapNodeAddress,
       "lexipxTrapType": lexipxTrapType,
       "lexipxGSQ": lexipxGSQ,
       "lextalk": lextalk,
       "lextalkActivated": lextalkActivated,
       "lextalkAddress": lextalkAddress,
       "lextalkName": lextalkName,
       "lextalkZone": lextalkZone,
       "lextalkType": lextalkType,
       "lextcp": lextcp,
       "lextcpActivated": lextcpActivated,
       "lextcpBootpEnable": lextcpBootpEnable,
       "lextcpAddressServ": lextcpAddressServ,
       "lextcpNumNPAPservers": lextcpNumNPAPservers,
       "lextcpNPAPserversTable": lextcpNPAPserversTable,
       "lextcpNPAPserversEntry": lextcpNPAPserversEntry,
       "lextcpNPAPserverIndex": lextcpNPAPserverIndex,
       "lextcpNPAPserverAddress": lextcpNPAPserverAddress,
       "lexhttp": lexhttp,
       "lexhttpEnable": lexhttpEnable,
       "lexhttpNumLinks": lexhttpNumLinks,
       "lexhttpBytesRemaining": lexhttpBytesRemaining,
       "lexhttpResetLinks": lexhttpResetLinks,
       "lexhttpLinkTable": lexhttpLinkTable,
       "lexhttpLinkTableEntry": lexhttpLinkTableEntry,
       "lexhttpLinkTableIndex": lexhttpLinkTableIndex,
       "lexhttpLinkTableStatus": lexhttpLinkTableStatus,
       "lexhttpLinkTableLabel": lexhttpLinkTableLabel,
       "lexhttpLinkTableURL": lexhttpLinkTableURL,
       "lexhttpConfigEnable": lexhttpConfigEnable,
       "lexdhcp": lexdhcp,
       "lexdhcpDhcpEnable": lexdhcpDhcpEnable,
       "lexdhcpRarpEnable": lexdhcpRarpEnable,
       "lexdhcpAddressSource": lexdhcpAddressSource,
       "lexdhcpWinsStatus": lexdhcpWinsStatus,
       "lexdhcpWinsServer": lexdhcpWinsServer,
       "lexdhcpHostname": lexdhcpHostname,
       "lexdhcpLeaseLength": lexdhcpLeaseLength,
       "lexdhcpTimetoExpire": lexdhcpTimetoExpire,
       "lexdhcpDNSServer": lexdhcpDNSServer,
       "lexhdwr": lexhdwr,
       "lexhdwrNumPorts": lexhdwrNumPorts,
       "lexhdwrPortTable": lexhdwrPortTable,
       "lexhdwrPortTableEntry": lexhdwrPortTableEntry,
       "lexhdwrPortTableIndex": lexhdwrPortTableIndex,
       "lexhdwrPortTableType": lexhdwrPortTableType,
       "lexhdwrPortTableParm1": lexhdwrPortTableParm1,
       "lexhdwrPortTableParm2": lexhdwrPortTableParm2,
       "lexhdwrPortTableParm3": lexhdwrPortTableParm3,
       "lexhdwrPortTableParm4": lexhdwrPortTableParm4,
       "lexhdwrPortTableParm5": lexhdwrPortTableParm5,
       "lexhdwrPortTableParm6": lexhdwrPortTableParm6,
       "lexhdwrPortTableParm7": lexhdwrPortTableParm7,
       "lexhdwrPortTableParm8": lexhdwrPortTableParm8,
       "lexhdwrPortTableParm9": lexhdwrPortTableParm9,
       "lexmac": lexmac,
       "lexmacType": lexmacType,
       "lexmacSpeed": lexmacSpeed,
       "lexmacConnType": lexmacConnType,
       "lexmacUAA": lexmacUAA,
       "lexmacLAA": lexmacLAA,
       "lextrap": lextrap,
       "lextrapDestNum": lextrapDestNum,
       "lextrapDestTable": lextrapDestTable,
       "lextrapDestEntry": lextrapDestEntry,
       "lextrapDestIndex": lextrapDestIndex,
       "lextrapDestIPAddr": lextrapDestIPAddr,
       "lextrapDestMask": lextrapDestMask,
       "lextrapIPTrapType": lextrapIPTrapType,
       "time": time,
       "timeReset": timeReset,
       "timeSource": timeSource,
       "timeUTCOffset": timeUTCOffset,
       "timeDSTEnable": timeDSTEnable,
       "timeDSTStartDate": timeDSTStartDate,
       "timeDSTEndDate": timeDSTEndDate,
       "timeDSTOffset": timeDSTOffset,
       "timeServerAddress": timeServerAddress,
       "timeServerName": timeServerName,
       "printer": printer,
       "prtgen": prtgen,
       "prtgenNumber": prtgenNumber,
       "prtgenInfoTable": prtgenInfoTable,
       "prtgenInfoEntry": prtgenInfoEntry,
       "prtgenPrinterIndex": prtgenPrinterIndex,
       "prtgenPrinterName": prtgenPrinterName,
       "prtgenPeripheralID": prtgenPeripheralID,
       "prtgenCodeRevision": prtgenCodeRevision,
       "prtgenResValue": prtgenResValue,
       "prtgenSerialNo": prtgenSerialNo,
       "prtgenStatusTable": prtgenStatusTable,
       "prtgenStatusEntry": prtgenStatusEntry,
       "prtgenStatPrinterIndex": prtgenStatPrinterIndex,
       "prtgenStatusIRC": prtgenStatusIRC,
       "prtgenStatusOutHopFull": prtgenStatusOutHopFull,
       "prtgenStatusInputEmpty": prtgenStatusInputEmpty,
       "prtgenStatusPaperJam": prtgenStatusPaperJam,
       "prtgenStatusTonerError": prtgenStatusTonerError,
       "prtgenStatusSrvcReqd": prtgenStatusSrvcReqd,
       "prtgenStatusDiskError": prtgenStatusDiskError,
       "prtgenStatusCoverOpen": prtgenStatusCoverOpen,
       "prtgenStatusPageComplex": prtgenStatusPageComplex,
       "prtgenStatusLineStatus": prtgenStatusLineStatus,
       "prtgenStatusBusy": prtgenStatusBusy,
       "prtgenStatusWaiting": prtgenStatusWaiting,
       "prtgenStatusWarming": prtgenStatusWarming,
       "prtgenStatusPrinting": prtgenStatusPrinting,
       "attachment": attachment,
       "fax": fax,
       "faxNumber": faxNumber,
       "faxTable": faxTable,
       "faxEntry": faxEntry,
       "faxIndex": faxIndex,
       "faxPort": faxPort,
       "faxAdapterCapabilities": faxAdapterCapabilities,
       "faxModemCapabilities": faxModemCapabilities,
       "faxSelectedCapabilities": faxSelectedCapabilities,
       "faxActiveCapabilities": faxActiveCapabilities,
       "faxIDString": faxIDString,
       "faxInitString": faxInitString,
       "faxNumberRings": faxNumberRings,
       "faxScaling": faxScaling,
       "faxBinaryEncoding": faxBinaryEncoding,
       "faxPrinterPort": faxPrinterPort,
       "faxInputTray": faxInputTray,
       "faxOutputBin": faxOutputBin}
)
